Find the best Django Trac tickets for first-time contributors and analyze each one with AI. Arguments: $ARGUMENTS

First, read CONTRIBUTING_GUIDE.md in the current directory — it defines what makes a good ticket, red flags to watch for, and difficulty criteria. Use it as the basis for all analysis.

The argument is the language: "ko" for Korean (default), "en" for English.

---

## Step 1 — Fetch candidate tickets

Run this bash command to get the initial scored list (fast, no HTTP enrichment):

```bash
python main.py --no-details --top 30 2>&1
```

Parse the output to identify the top 10 ticket IDs by score.

## Step 2 — Deep AI analysis for each top ticket

For each of the top 10 tickets, fetch the full ticket page using WebFetch:
`https://code.djangoproject.com/ticket/{ticket_id}`

Read the title, component, status/owner, description, and ALL comments carefully.

For each ticket, assess:

1. **실제 난이도** (Actual difficulty)
   - What Django internals knowledge is needed?
   - How many files likely need changes?
   - Is the fix path clear from the existing discussion?
   - 🟢 쉬움 / 🟡 보통 / 🔴 어려움

2. **할 일** (What to do)
   - One concrete sentence: what code change is needed?

3. **레드플래그** (Red flags)
   - Already fixed elsewhere?
   - Duplicate?
   - Cannot reproduce?
   - Closing proposed?
   - Needs design consensus / RFC?
   - Wontfix / by design?

4. **첫 기여자 추천 여부** (Good first issue?)
   - ✅ 추천 / ⚠️ 주의 / ❌ 비추천

## Step 3 — Output the final report

If language is "ko", write everything in Korean. Otherwise in English.

Present the results in this format:

---

# 🦅 Django 기여 추천 티켓 (AI 분석)

> 전략: 패치가 있지만 오래된 티켓을 이어받는 **벌처 전략**  
> AI가 각 티켓 페이지를 직접 읽고 분석한 결과입니다.

---

For each ticket (ranked by combined score + AI assessment):

## {rank}. [{score}점] #{ticket_id} — {title}

- **링크**: https://code.djangoproject.com/ticket/{ticket_id}
- **컴포넌트**: {component}
- **상태**: {status} / {owner or 미할당}
- **마지막 수정**: {age}
- **난이도**: {🟢/🟡/🔴} {easy/medium/hard} — {reason}
- **할 일**: {concrete action}
- **레드플래그**: {flags or 없음}
- **추천**: {✅/⚠️/❌} {reason}

---

After all tickets, add a short summary:

## 🏆 최종 추천

Top 3 picks with a one-line reason each. Prioritize: high score + low difficulty + no red flags + ✅ recommended.
