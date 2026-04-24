#!/usr/bin/env python3
"""Pick good Django Trac tickets for first-time contributors."""

import argparse
import sys
from datetime import datetime, timezone, date

from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

from trac import Ticket, fetch_tickets, enrich_tickets, RED_FLAGS

console = Console()


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

# Keywords that suggest complex environment setup — penalty applied if found in summary
_COMPLEX_ENV_KEYWORDS = [
    "oracle", "sql server", "mssql", "ms sql",
    "mongodb", "cassandra", "elasticsearch",
    "docker", "kubernetes", "k8s",
]

# Keywords that suggest the ticket needs broad community consensus rather than just a patch
_CONSENSUS_KEYWORDS = [
    "deprecat", "rfc", "proposal", "design decision",
    "should we", "bikeshed", "breaking change",
    "architecture", "separation of concern",
]


def score_ticket(ticket: Ticket) -> tuple[int, list[str]]:
    """Return (score, reasons). Higher score = better candidate."""
    score = 0
    reasons: list[str] = []
    days = ticket.modified_days_ago

    if days is None:
        return 0, ["수정일 정보 없음"]

    months = days / 30

    # 1. Last-modified score (Vulture strategy)
    if 6 <= months < 12:
        score += 50
        reasons.append(f"수정 {months:.0f}개월 전 (벌처 최적)")
    elif 12 <= months < 24:
        score += 35
        reasons.append(f"수정 {months:.0f}개월 전 (벌처 적합)")
    elif 24 <= months < 48:
        score += 15
        reasons.append(f"수정 {months:.0f}개월 전 (오래됨)")
    elif months >= 48:
        score += 5
        reasons.append(f"수정 {months:.0f}개월 전 (매우 오래됨)")
    else:
        score -= 30
        reasons.append(f"수정 {months:.1f}개월 전 (최근 활동 있음 - 주의)")

    # 2. Creation date penalty — old tickets accumulate discussion and are harder to follow
    if ticket.created:
        created_years = (datetime.now(timezone.utc) - ticket.created).days / 365
        if created_years >= 8:
            score -= 40
            reasons.append(f"생성 {created_years:.0f}년 전 (너무 오래된 티켓 - 논의 많을 가능성)")
        elif created_years >= 5:
            score -= 20
            reasons.append(f"생성 {created_years:.0f}년 전 (오래된 티켓)")
        elif created_years >= 3:
            score -= 5
            reasons.append(f"생성 {created_years:.0f}년 전")

    # 3. Assignment status — unassigned is the strongest positive signal
    if ticket.is_unassigned:
        score += 35
        reasons.append("미할당")
    else:
        score -= 25
        reasons.append(f"할당됨: {ticket.owner}")

    # 4. Complex environment setup detection
    text = (ticket.summary + " " + ticket.component).lower()
    for kw in _COMPLEX_ENV_KEYWORDS:
        if kw in text:
            score -= 25
            reasons.append(f"복잡한 환경 설정 필요 ({kw})")
            break

    # 5. Community consensus / design discussion detection
    summary_lower = ticket.summary.lower()
    for kw in _CONSENSUS_KEYWORDS:
        if kw in summary_lower:
            score -= 20
            reasons.append(f"커뮤니티 합의 필요 가능성 ({kw})")
            break

    # 6. Django version filed against (old version = likely long-standing complex issue)
    if ticket.version:
        major = ticket.version.split(".")[0]
        if major == "1":
            score -= 15
            reasons.append(f"Django {ticket.version} 기준 제출 (구버전)")
        elif major == "2":
            score -= 5
            reasons.append(f"Django {ticket.version} 기준 제출")

    # 7. Comment count
    if ticket.num_comments >= 0:
        if ticket.num_comments >= 30:
            score -= 45
            reasons.append(f"댓글 {ticket.num_comments}개 (논의 매우 복잡 — 피할 것)")
        elif ticket.num_comments >= 15:
            score -= 25
            reasons.append(f"댓글 {ticket.num_comments}개 (논의 복잡)")
        elif ticket.num_comments >= 8:
            score -= 10
            reasons.append(f"댓글 {ticket.num_comments}개")
        else:
            score += 5
            reasons.append(f"댓글 {ticket.num_comments}개 (논의 적음)")

    # 8. Red flags from ticket content analysis
    _penalty_map = {tag: penalty for _, tag, _, penalty in RED_FLAGS}
    _label_map = {tag: label for _, tag, label, _ in RED_FLAGS}
    for flag in ticket.red_flags:
        penalty = _penalty_map.get(flag, -30)
        label = _label_map.get(flag, flag)
        score += penalty
        reasons.append(f"🚨 {label} ({penalty}점)")

    return score, reasons


# ---------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------

def filter_tickets(
    tickets: list[Ticket],
    min_age_months: float,
    max_age_months: float,
    unassigned_only: bool,
    component: str | None,
) -> list[Ticket]:
    result = []
    for t in tickets:
        days = t.modified_days_ago
        if days is None:
            continue
        months = days / 30
        if months < min_age_months:
            continue
        if months > max_age_months:
            continue
        if unassigned_only and not t.is_unassigned:
            continue
        if component and component.lower() not in t.component.lower():
            continue
        result.append(t)
    return result


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def _age_label(days: int | None) -> str:
    if days is None:
        return "?"
    months = days / 30
    if months < 1:
        return f"{days}일 전"
    if months < 12:
        return f"{months:.0f}개월 전"
    years = months / 12
    return f"{years:.1f}년 전"


def _score_color(score: int) -> str:
    if score >= 60:
        return "green"
    if score >= 30:
        return "yellow"
    return "red"


def display_tickets(scored: list[tuple[int, list[str], Ticket]], top_n: int) -> None:
    table = Table(
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
        title=f"[bold]Django 기여 추천 티켓 Top {min(top_n, len(scored))}[/bold]",
        title_style="bold white",
    )
    has_comments = any(t.num_comments >= 0 for _, _, t in scored[:top_n])

    table.add_column("점수", justify="center", width=6)
    table.add_column("ID", justify="right", width=7)
    table.add_column("요약", width=46)
    table.add_column("컴포넌트", width=18)
    table.add_column("상태/담당자", width=14)
    table.add_column("수정", width=10)
    if has_comments:
        table.add_column("댓글", justify="center", width=5)

    for score, reasons, ticket in scored[:top_n]:
        color = _score_color(score)
        owner_label = "미할당" if ticket.is_unassigned else ticket.owner[:12]
        status_text = f"{ticket.status}\n[dim]{owner_label}[/dim]"
        summary = ticket.summary if len(ticket.summary) <= 46 else ticket.summary[:43] + "..."

        row = [
            Text(str(score), style=f"bold {color}"),
            f"[link={ticket.url}]#{ticket.id}[/link]",
            summary,
            ticket.component[:18],
            status_text,
            _age_label(ticket.modified_days_ago),
        ]
        if has_comments:
            c = ticket.num_comments
            comment_color = "red" if c >= 30 else "yellow" if c >= 15 else "green"
            row.append(Text(str(c) if c >= 0 else "?", style=comment_color))
        table.add_row(*row)

    console.print()
    console.print(table)

    console.print("\n[bold cyan]추천 티켓 상세:[/bold cyan]")
    for i, (score, reasons, ticket) in enumerate(scored[:top_n], 1):
        color = _score_color(score)
        console.print(f"\n  [{color}]{i}. #{ticket.id}[/{color}] {ticket.summary}")
        console.print(f"     URL : [underline]{ticket.url}[/underline]")
        console.print(f"     사유: {' | '.join(reasons)}")


# ---------------------------------------------------------------------------
# Markdown export
# ---------------------------------------------------------------------------

def _score_badge(score: int) -> str:
    if score >= 60:
        return "🟢"
    if score >= 30:
        return "🟡"
    return "🔴"


def save_markdown(
    scored: list[tuple[int, list[str], Ticket]],
    top_n: int,
    path: str,
    lang: str = "ko",
) -> None:
    today = date.today().strftime("%Y-%m-%d")
    top = min(top_n, len(scored))

    if lang == "en":
        _save_markdown_en(scored, top, path, today)
    else:
        _save_markdown_ko(scored, top, path, today)


def _score_reason_en(reasons: list[str]) -> str:
    mapping = {
        "미할당": "unassigned",
        "수정 ": "modified ",
        "개월 전 (벌처 최적)": "mo ago (vulture sweet spot)",
        "개월 전 (벌처 적합)": "mo ago (vulture good)",
        "개월 전 (오래됨)": "mo ago (old)",
        "개월 전 (매우 오래됨)": "mo ago (very old)",
        "개월 전 (최근 활동 있음 - 주의)": "mo ago (recently active — caution)",
        "할당됨: ": "assigned: ",
    }
    result = []
    for r in reasons:
        translated = r
        for ko, en in mapping.items():
            translated = translated.replace(ko, en)
        result.append(translated)
    return " / ".join(result)


def _save_markdown_ko(scored, top, path, today):
    lines = [
        "# Django 기여 추천 티켓",
        "",
        f"> 생성일: {today}  ",
        "> 조건: `Stage=Accepted`, `Type=Bug`, `Has patch=Yes`, `Patch needs improvement=Yes`  ",
        "> 전략: 수정된 지 오래됐지만 패치가 있는 티켓을 이어서 완성하는 **벌처 전략**",
        "",
        "---",
        "",
        "## 점수 기준",
        "",
        "| 점수 | 조건 |",
        "|------|------|",
        "| +50 | 수정 6~12개월 전 (벌처 최적) |",
        "| +35 | 수정 12~24개월 전 (벌처 적합) |",
        "| +15 | 수정 24~48개월 전 |",
        "| +35 | 미할당 티켓 |",
        "| -25 | 담당자 있음 |",
        "| -5  | 생성 3년 이상 |",
        "| -20 | 생성 5년 이상 (오래된 티켓) |",
        "| -40 | 생성 8년 이상 (논의 많을 가능성) |",
        "| -25 | 복잡한 환경 설정 필요 (Oracle 등) |",
        "| -20 | 커뮤니티 합의 필요 가능성 |",
        "| -30 | 수정 6개월 미만 (최근 활동) |",
        "",
        "---",
        "",
        f"## 추천 티켓 Top {top}",
        "",
        "| 순위 | 점수 | 티켓 | 컴포넌트 | 상태 | 마지막 수정 | 비고 |",
        "|------|------|------|----------|------|-------------|------|",
    ]
    for i, (score, reasons, ticket) in enumerate(scored[:top], 1):
        badge = _score_badge(score)
        owner = "미할당" if ticket.is_unassigned else ticket.owner
        modified = ticket.modified.strftime("%Y-%m-%d") if ticket.modified else "?"
        note = " / ".join(reasons)
        lines.append(
            f"| {i} | {badge} {score} | [#{ticket.id}]({ticket.url}) {ticket.summary} | "
            f"{ticket.component} | {ticket.status} / {owner} | {modified} | {note} |"
        )
    lines += ["", "---", "", "## 상세", ""]
    for i, (score, reasons, ticket) in enumerate(scored[:top], 1):
        badge = _score_badge(score)
        owner = "미할당" if ticket.is_unassigned else ticket.owner
        modified = ticket.modified.strftime("%Y-%m-%d") if ticket.modified else "?"
        created = ticket.created.strftime("%Y-%m-%d") if ticket.created else "?"
        lines += [
            f"### {i}. [{badge} #{ticket.id}] {ticket.summary}",
            "",
            f"- **링크**: {ticket.url}",
            f"- **컴포넌트**: {ticket.component}",
            f"- **상태**: {ticket.status} / {owner}",
            f"- **마지막 수정**: {modified}",
            f"- **생성일**: {created}",
            f"- **점수**: {score} ({' | '.join(reasons)})",
            "",
        ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def _save_markdown_en(scored, top, path, today):
    lines = [
        "# Recommended Django Tickets for Contributors",
        "",
        f"> Generated: {today}  ",
        "> Filter: `Stage=Accepted`, `Type=Bug`, `Has patch=Yes`, `Patch needs improvement=Yes`  ",
        "> Strategy: **Vulture** — pick up stale patches that need finishing",
        "",
        "---",
        "",
        "## Scoring Criteria",
        "",
        "| Score | Condition |",
        "|-------|-----------|",
        "| +50 | Modified 6–12 months ago (Vulture sweet spot) |",
        "| +35 | Modified 12–24 months ago (Vulture good) |",
        "| +15 | Modified 24–48 months ago (older) |",
        "| +35 | Unassigned |",
        "| −25 | Already assigned |",
        "| −5  | Created 3+ years ago |",
        "| −20 | Created 5+ years ago (old ticket) |",
        "| −40 | Created 8+ years ago (likely heavy discussion) |",
        "| −25 | Complex environment required (Oracle, etc.) |",
        "| −20 | Possible community consensus needed |",
        "| −30 | Modified < 6 months ago (recently active) |",
        "",
        "---",
        "",
        f"## Top {top} Recommended Tickets",
        "",
        "| Rank | Score | Ticket | Component | Status | Last Modified | Notes |",
        "|------|-------|--------|-----------|--------|---------------|-------|",
    ]
    for i, (score, reasons, ticket) in enumerate(scored[:top], 1):
        badge = _score_badge(score)
        owner = "unassigned" if ticket.is_unassigned else ticket.owner
        modified = ticket.modified.strftime("%Y-%m-%d") if ticket.modified else "?"
        note = _score_reason_en(reasons)
        lines.append(
            f"| {i} | {badge} {score} | [#{ticket.id}]({ticket.url}) {ticket.summary} | "
            f"{ticket.component} | {ticket.status} / {owner} | {modified} | {note} |"
        )
    lines += ["", "---", "", "## Details", ""]
    for i, (score, reasons, ticket) in enumerate(scored[:top], 1):
        badge = _score_badge(score)
        owner = "unassigned" if ticket.is_unassigned else ticket.owner
        modified = ticket.modified.strftime("%Y-%m-%d") if ticket.modified else "?"
        created = ticket.created.strftime("%Y-%m-%d") if ticket.created else "?"
        lines += [
            f"### {i}. [{badge} #{ticket.id}] {ticket.summary}",
            "",
            f"- **Link**: {ticket.url}",
            f"- **Component**: {ticket.component}",
            f"- **Status**: {ticket.status} / {owner}",
            f"- **Last modified**: {modified}",
            f"- **Created**: {created}",
            f"- **Score**: {score} ({_score_reason_en(reasons)})",
            "",
        ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Django Trac에서 기여하기 좋은 티켓을 찾아줍니다.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--min-age", type=float, default=6.0, metavar="MONTHS",
                        help="최소 마지막 수정 경과 개월 수")
    parser.add_argument("--max-age", type=float, default=48.0, metavar="MONTHS",
                        help="최대 마지막 수정 경과 개월 수")
    parser.add_argument("--top", type=int, default=15, metavar="N",
                        help="상위 N개 티켓 표시")
    parser.add_argument("--unassigned-only", action="store_true",
                        help="미할당 티켓만 표시")
    parser.add_argument("--component", type=str, default=None, metavar="KEYWORD",
                        help="컴포넌트 이름 필터 (예: admin, ORM)")
    parser.add_argument("--max-fetch", type=int, default=500, metavar="N",
                        help="Trac에서 가져올 최대 티켓 수")
    parser.add_argument("--no-patch-filter", action="store_true",
                        help="패치 필터 없이 전체 Accepted Bug 티켓 검색")
    parser.add_argument("--md", type=str, default=None, metavar="FILE",
                        help="결과를 마크다운 파일로 저장 (예: good-tickets.md)")
    parser.add_argument("--lang", type=str, default="ko", choices=["ko", "en"],
                        help="마크다운 출력 언어 (ko / en)")
    parser.add_argument("--no-details", action="store_true",
                        help="댓글 수 조회 생략 (빠른 실행)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    has_patch = not args.no_patch_filter
    patch_needs_improvement = not args.no_patch_filter

    console.print("[bold]Django Trac에서 티켓을 가져오는 중...[/bold]", end=" ")

    try:
        tickets = fetch_tickets(
            has_patch=has_patch,
            patch_needs_improvement=patch_needs_improvement,
            max_results=args.max_fetch,
        )
    except Exception as e:
        console.print(f"\n[red]오류: {e}[/red]")
        sys.exit(1)

    console.print(f"[green]{len(tickets)}개 티켓 로드 완료[/green]")

    filtered = filter_tickets(
        tickets,
        min_age_months=args.min_age,
        max_age_months=args.max_age,
        unassigned_only=args.unassigned_only,
        component=args.component,
    )

    if not filtered:
        console.print("[yellow]조건에 맞는 티켓이 없습니다. --min-age 또는 --max-age를 조정해보세요.[/yellow]")
        sys.exit(0)

    # 1차 스코어링 (댓글 수 제외)
    scored = sorted(
        [(score_ticket(t)[0], score_ticket(t)[1], t) for t in filtered],
        key=lambda x: x[0],
        reverse=True,
    )

    if not args.no_details:
        # 상위 후보만 상세 조회 (서버 rate limit 방지를 위해 순차 요청)
        candidates = [t for _, _, t in scored[:args.top * 2]]
        console.print(
            f"상위 {len(candidates)}개 티켓 분석 중 (댓글 수 + 레드플래그)",
            end="",
        )
        def _progress(done, total):
            if done % 5 == 0 or done == total:
                console.print(f" {done}/{total}", end="", highlight=False)
        enrich_tickets(candidates, delay=0.4, progress_callback=_progress)
        console.print(" [green]완료[/green]")

        # 댓글 수 반영해서 재스코어링
        scored = sorted(
            [(score_ticket(t)[0], score_ticket(t)[1], t) for t in filtered],
            key=lambda x: x[0],
            reverse=True,
        )

    console.print(f"필터 결과: [bold]{len(filtered)}개[/bold] 티켓 (수정 {args.min_age:.0f}–{args.max_age:.0f}개월 전)")

    display_tickets(scored, top_n=args.top)

    console.print(
        f"\n[dim]전체 결과: https://code.djangoproject.com/query?"
        f"status=new&status=assigned&type=Bug&stage=Accepted"
        f"{'&has_patch=1&patch_needs_improvement=1' if has_patch else ''}[/dim]\n"
    )

    if args.md:
        save_markdown(scored, top_n=args.top, path=args.md, lang=args.lang)
        console.print(f"[bold green]저장 완료:[/bold green] {args.md}\n")


if __name__ == "__main__":
    main()
