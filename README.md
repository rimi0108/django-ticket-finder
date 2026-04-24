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

### Last Modified

| Score | Condition |
|-------|-----------|
| +50 | Modified 6–12 months ago (Vulture sweet spot — original author likely moved on) |
| +35 | Modified 12–24 months ago (Vulture good) |
| +15 | Modified 24–48 months ago (older) |
| +5  | Modified 48+ months ago |
| −30 | Modified < 6 months ago (recently active — someone may be working on it) |

### Creation Date

| Score | Condition |
|-------|-----------|
| −5  | Created 3+ years ago |
| −20 | Created 5+ years ago (old ticket) |
| −40 | Created 8+ years ago (long history, hard to catch up) |

### Assignment

| Score | Condition |
|-------|-----------|
| +35 | Unassigned |
| −25 | Already assigned |

### Comment Count

| Score | Condition |
|-------|-----------|
| +5  | 0–7 comments (easy to follow) |
| −10 | 8–14 comments |
| −25 | 15–29 comments (complex discussion) |
| −45 | 30+ comments (very complex — avoid) |

### Other Penalties

| Score | Condition |
|-------|-----------|
| −15 | Filed against Django 1.x (old version) |
| −5  | Filed against Django 2.x |
| −25 | Complex environment required (Oracle, Docker, etc.) |
| −20 | Possible community consensus needed (RFC, design discussion, etc.) |

### Red Flags (auto-detected from ticket content)

| Score | Condition |
|-------|-----------|
| −60 | Already fixed by another commit/ticket |
| −55 | Duplicate ticket |
| −55 | Wontfix / working as intended |
| −45 | Closing proposed |
| −35 | Cannot reproduce |
| −30 | Community consensus required first |

## Installation

```bash
pip install -r requirements.txt
```

**Requirements**: Python 3.10+, `rich`

## Usage

```bash
# Basic run — Top 15 tickets using Vulture strategy
python main.py

# Easy Pickings mode — tickets explicitly marked "beginner-friendly" by maintainers
python main.py --easy-pickings
python main.py --easy-pickings --top 10 --md easy-tickets.md

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

# AI-powered analysis — uses Claude Haiku to assess difficulty, what to do, and red flags
export ANTHROPIC_API_KEY=sk-ant-...
python main.py --ai-analysis
python main.py --ai-analysis --top 10 --md good-tickets.md

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
| `--easy-pickings` | false | Search tickets marked "easy pickings" by Django maintainers |
| `--ai-analysis` | false | Use Claude Haiku AI to analyze difficulty, action needed, and red flags (`ANTHROPIC_API_KEY` required) |
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
