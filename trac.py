import csv
import io
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

TRAC_BASE = "https://code.djangoproject.com"
TRAC_QUERY = f"{TRAC_BASE}/query"

_DATE_FORMAT = "%b %d, %Y, %I:%M:%S %p"

# (phrases_to_match, tag, korean_label, score_penalty)
RED_FLAGS: list[tuple[list[str], str, str, int]] = [
    (
        ["already fixed", "has been fixed", "this was fixed", "fixed in #", "fixed by commit",
         "was fixed in", "this is fixed", "got fixed"],
        "already_fixed",
        "이미 다른 커밋/티켓으로 수정됨",
        -60,
    ),
    (
        ["duplicate of", "this is a duplicate", "it's a duplicate", "already reported"],
        "duplicate",
        "중복 티켓",
        -55,
    ),
    (
        ["wontfix", "won't fix", "will not fix", "not a bug", "this is by design",
         "as designed", "this is intended behavior", "working as intended"],
        "wontfix",
        "수정 거부 또는 의도된 동작",
        -55,
    ),
    (
        ["closing as", "should be closed", "can be closed", "propose to close",
         "propose closing", "suggest closing", "closing this ticket",
         "close this ticket", "i'll close", "will close this",
         "i would close", "should close", "marked as invalid",
         "closing as invalid", "closing as worksforme"],
        "closing_proposed",
        "종료 제안됨",
        -45,
    ),
    (
        ["cannot reproduce", "can't reproduce", "no longer reproduces",
         "unable to reproduce", "no longer an issue", "not reproducible",
         "works in current django", "fixed in django"],
        "cant_reproduce",
        "재현 불가 가능성",
        -35,
    ),
    (
        ["needs design decision", "design discussion needed", "needs consensus",
         "needs broader discussion", "django-developers", "mailing list first"],
        "needs_consensus",
        "커뮤니티 합의 먼저 필요",
        -30,
    ),
]


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
    red_flags: list[str] = field(default_factory=list)  # list of tags
    # AI analysis fields (populated only when --ai-analysis is used)
    ai_difficulty: Optional[str] = None        # "easy" | "medium" | "hard"
    ai_action: Optional[str] = None            # what the contributor needs to do
    ai_red_flags: list[str] = field(default_factory=list)
    ai_good_first_issue: Optional[bool] = None

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
    stage: str | list[str] = "Accepted",
    has_patch: bool = True,
    patch_needs_improvement: bool = True,
    easy_pickings: bool = False,
    max_results: int = 500,
) -> list[Ticket]:
    stages = [stage] if isinstance(stage, str) else stage
    params = [
        ("status", "new"),
        ("status", "assigned"),
        ("format", "csv"),
        ("max", str(max_results)),
        ("col", "id"),
        ("col", "summary"),
        ("col", "status"),
        ("col", "owner"),
        ("col", "component"),
        ("col", "version"),
        ("col", "changetime"),
        ("col", "time"),
        ("col", "easy"),
    ]
    if ticket_type:
        params.append(("type", ticket_type))

    for s in stages:
        params.append(("stage", s))
    if has_patch:
        params.append(("has_patch", "1"))
    if patch_needs_improvement:
        params.append(("patch_needs_improvement", "1"))

    url = f"{TRAC_QUERY}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "django-ticket-finder/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        content = response.read().decode("utf-8-sig")

    tickets = []
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        try:
            ticket_id = int(row["id"])
        except (KeyError, ValueError):
            continue

        # Client-side easy pickings filter — Trac's CSV endpoint ignores the
        # easy_pickings URL param, so we fetch the column and filter manually.
        if easy_pickings and row.get("Easy pickings", "").strip() != "1":
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


def _analyze_ticket_page(ticket_id: int) -> tuple[int, list[str], str]:
    """
    Fetch ticket page and return (comment_count, red_flag_tags, stripped_text).
    Detects patterns in comments that indicate a ticket is problematic.
    stripped_text is used for AI analysis when --ai-analysis is enabled.
    """
    url = f"{TRAC_BASE}/ticket/{ticket_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "django-ticket-finder/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception:
        return 0, [], ""

    comment_count = html.count('id="comment:')

    # Strip HTML tags and normalize whitespace for pattern matching
    text = re.sub(r"<[^>]+>", " ", html).lower()
    text = re.sub(r"\s+", " ", text)

    found_flags = []
    for phrases, tag, _label, _penalty in RED_FLAGS:
        for phrase in phrases:
            if phrase in text:
                found_flags.append(tag)
                break

    return comment_count, found_flags, text


def enrich_tickets(
    tickets: list[Ticket],
    delay: float = 0.4,
    progress_callback=None,
    ai_analysis: bool = False,
) -> None:
    """Fetch comment counts and red flags sequentially to avoid rate limiting."""
    if ai_analysis:
        from ai import analyze_with_claude

    for i, ticket in enumerate(tickets):
        count, flags, text = _analyze_ticket_page(ticket.id)
        ticket.num_comments = count
        ticket.red_flags = flags
        if ai_analysis and text:
            result = analyze_with_claude(text, ticket.summary, ticket.component)  # noqa: F821
            ticket.ai_difficulty = result.get("difficulty")
            ticket.ai_action = result.get("action_needed")
            ticket.ai_red_flags = result.get("additional_red_flags", [])
            ticket.ai_good_first_issue = result.get("good_first_issue")
        if progress_callback:
            progress_callback(i + 1, len(tickets))
        if i < len(tickets) - 1:
            time.sleep(delay)
