# pick-good-django-ticket

A CLI tool that automatically finds the best Django tickets to contribute to as a first-time contributor.

It queries the [Django Trac](https://code.djangoproject.com/query) system and scores tickets using the **Vulture Strategy** — finding tickets that already have a patch but haven't been updated in a while, making them ideal candidates to pick up and finish.

## Strategy

### Vulture Strategy

Look for tickets where:
- **Stage**: Accepted (not Unreviewed — those get closed without discussion)
- **Type**: Bug
- **Has patch**: Yes — someone already did the groundwork
- **Patch needs improvement**: Yes — the patch has feedback but was never fixed
- **Last modified**: 6+ months ago — the original author has likely moved on

These tickets are low-competition and have a clear path to completion.

### What to avoid

| Signal | Why |
|--------|-----|
| Recently active (< 6 months) | Someone may already be working on it |
| Very old with many comments | Complex history, hard to catch up |
| Requires Oracle / special infra | Environment setup will block you |
| New feature proposals | Needs community consensus — too much energy for beginners |

## Scoring

| Score | Condition |
|-------|-----------|
| +50 | Modified 6–12 months ago (Vulture sweet spot) |
| +35 | Modified 12–24 months ago (still good) |
| +15 | Modified 24–48 months ago (older) |
| +20 | Unassigned |
| −30 | Modified < 6 months ago (too recently active) |
| −10 | Already assigned to someone |

## Installation

```bash
pip install -r requirements.txt
```

**Requirements**: Python 3.10+, `rich`

## Usage

```bash
# Basic run — Top 15 tickets using Vulture strategy
python main.py

# Show only unassigned tickets
python main.py --unassigned-only

# Filter by component
python main.py --component admin
python main.py --component Migrations
python main.py --component ORM

# Adjust age range (in months)
python main.py --min-age 12 --max-age 24

# Save results to Markdown (Korean)
python main.py --md good-tickets.md

# Save results to Markdown (English)
python main.py --md good-tickets.md --lang en

# Include tickets without a patch (broader search)
python main.py --no-patch-filter

# Combine options
python main.py --unassigned-only --component admin --top 5 --md admin-tickets.md
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--min-age MONTHS` | `6` | Minimum months since last modification |
| `--max-age MONTHS` | `48` | Maximum months since last modification |
| `--top N` | `15` | Number of tickets to display |
| `--unassigned-only` | false | Only show tickets with no owner |
| `--component KEYWORD` | — | Filter by component name (partial match) |
| `--max-fetch N` | `500` | Max tickets to fetch from Trac |
| `--no-patch-filter` | false | Disable has_patch / patch_needs_improvement filter |
| `--md FILE` | — | Save results as a Markdown file |
| `--lang` | `ko` | Markdown language: `ko` (Korean) or `en` (English) |

## Output Example

```
Django Trac에서 티켓을 가져오는 중... 191개 티켓 로드 완료
필터 결과: 71개 티켓 (수정 6–48개월 전)

  1. #23268 Fixtures: Natural Key support for Generic Foreign Keys
     URL : https://code.djangoproject.com/ticket/23268
     사유: 수정 10개월 전 (벌처 최적) | 미할당
```

## How to contribute to Django

1. Browse the output and pick a ticket that interests you
2. Read the ticket and its patch on Trac
3. Clone Django: `git clone https://github.com/django/django.git`
4. Set up the dev environment: [Django contributing guide](https://docs.djangoproject.com/en/dev/internals/contributing/)
5. Improve the patch, run the tests, and submit via Trac

**Useful links**
- [Django Trac query](https://code.djangoproject.com/query)
- [Triaging tickets guide](https://docs.djangoproject.com/en/dev/internals/contributing/triaging-tickets/)
- [Writing code guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/)
