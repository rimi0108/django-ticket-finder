import json
import os
import re

import anthropic

_client: anthropic.Anthropic | None = None


def check_api_key() -> bool:
    """Return True if ANTHROPIC_API_KEY is set."""
    return bool(os.environ.get("ANTHROPIC_API_KEY"))

_PROMPT_TEMPLATE = """\
You are a Django contributor advisor. Analyze this Django bug tracker ticket \
and help a first-time contributor decide whether to work on it.

Ticket summary: {summary}
Component: {component}

Ticket content (description + comments):
{text}

Respond with ONLY a valid JSON object — no markdown, no explanation:
{{
  "difficulty": "easy|medium|hard",
  "difficulty_reason": "One sentence explaining the technical complexity",
  "action_needed": "One clear sentence: exactly what the contributor needs to do to fix this",
  "additional_red_flags": ["list any concerns not obvious from metadata, e.g. already_fixed / duplicate / needs_consensus / controversial / not_reproducible / closing_proposed — empty list if none"],
  "good_first_issue": true or false
}}"""


def analyze_with_claude(stripped_text: str, summary: str, component: str) -> dict:
    """
    Call Claude to analyze a ticket and return structured assessment.
    Returns an empty dict on any failure so callers can degrade gracefully.
    """
    global _client
    if _client is None:
        _client = anthropic.Anthropic()

    # Keep context window manageable: trim to ~6000 chars
    text = stripped_text[:6000]

    prompt = _PROMPT_TEMPLATE.format(
        summary=summary,
        component=component,
        text=text,
    )

    try:
        response = _client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = response.content[0].text.strip()
        # Strip markdown code fences if model wraps the JSON anyway
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        return json.loads(raw)
    except Exception:
        return {}
