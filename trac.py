import csv
import io
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

TRAC_BASE = "https://code.djangoproject.com"
TRAC_QUERY = f"{TRAC_BASE}/query"

# Format seen in Trac CSV: "Apr 22, 2026, 9:37:12 AM"
_DATE_FORMAT = "%b %d, %Y, %I:%M:%S %p"


@dataclass
class Ticket:
    id: int
    summary: str
    status: str
    owner: str
    component: str
    modified: Optional[datetime]
    created: Optional[datetime]
    url: str
    version: str = ""
    num_comments: int = -1  # -1 = not fetched yet

    @property
    def is_unassigned(self) -> bool:
        return not self.owner or self.owner.lower() in ("nobody", "")

    @property
    def modified_days_ago(self) -> Optional[int]:
        if not self.modified:
            return None
        return (datetime.now(timezone.utc) - self.modified).days

    @property
    def created_years_ago(self) -> Optional[float]:
        if not self.created:
            return None
        return (datetime.now(timezone.utc) - self.created).days / 365


def _parse_date(date_str: str) -> Optional[datetime]:
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip(), _DATE_FORMAT).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def fetch_tickets(
    *,
    ticket_type: str = "Bug",
    stage: str = "Accepted",
    has_patch: bool = True,
    patch_needs_improvement: bool = True,
    max_results: int = 500,
) -> list[Ticket]:
    params = [
        ("status", "new"),
        ("status", "assigned"),
        ("type", ticket_type),
        ("stage", stage),
        ("format", "csv"),
        ("max", str(max_results)),
        ("col", "id"),
        ("col", "summary"),
        ("col", "status"),
        ("col", "owner"),
        ("col", "component"),
        ("col", "version"),
        ("col", "changetime"),  # "Modified" column in CSV
        ("col", "time"),        # "Created" column in CSV
    ]
    if has_patch:
        params.append(("has_patch", "1"))
    if patch_needs_improvement:
        params.append(("patch_needs_improvement", "1"))

    url = f"{TRAC_QUERY}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "django-ticket-finder/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        content = response.read().decode("utf-8-sig")  # strip BOM if present

    tickets = []
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        try:
            ticket_id = int(row["id"])
        except (KeyError, ValueError):
            continue

        tickets.append(
            Ticket(
                id=ticket_id,
                summary=row.get("Summary", "").strip(),
                status=row.get("Status", "").strip(),
                owner=row.get("Owner", "").strip(),
                component=row.get("Component", "").strip(),
                modified=_parse_date(row.get("Modified", "")),
                created=_parse_date(row.get("Created", "")),
                url=f"{TRAC_BASE}/ticket/{ticket_id}",
                version=row.get("Version", "").strip(),
            )
        )

    return tickets


def fetch_comment_count(ticket_id: int) -> int:
    """Scrape a ticket page and count the number of comments."""
    url = f"{TRAC_BASE}/ticket/{ticket_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "django-ticket-finder/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode("utf-8", errors="ignore")
        return html.count('id="comment:')
    except Exception:
        return 0


def enrich_with_comments(
    tickets: list[Ticket],
    delay: float = 0.5,
    progress_callback=None,
) -> None:
    """Fetch comment counts sequentially to avoid rate limiting."""
    import time
    for i, ticket in enumerate(tickets):
        ticket.num_comments = fetch_comment_count(ticket.id)
        if progress_callback:
            progress_callback(i + 1, len(tickets))
        if i < len(tickets) - 1:
            time.sleep(delay)
