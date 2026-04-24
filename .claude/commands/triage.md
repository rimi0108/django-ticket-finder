Analyze a Django Trac ticket for first-time contributors. Arguments: $ARGUMENTS

First, read CONTRIBUTING_GUIDE.md in the current directory — it defines what makes a good ticket, red flags to watch for, and difficulty criteria. Use it as the basis for your analysis.

Parse the arguments: the first token is the ticket ID (number), the second optional token is the language ("ko" for Korean, "en" for English — default: "ko").

Steps:
1. Fetch the ticket page at https://code.djangoproject.com/ticket/{ticket_id} using WebFetch.
2. Read the full content: title, component, status, description, and all comments.
3. Produce a structured triage report.

If language is "ko", write the entire report in Korean. Otherwise write in English.

---

Korean report format:

## 🎫 티켓 #{ticket_id} 트리아지 리포트

**제목**: {title}
**컴포넌트**: {component}
**상태**: {status} / {owner or 미할당}
**링크**: https://code.djangoproject.com/ticket/{ticket_id}

---

### 버그 요약
한두 문장으로 무슨 버그인지 설명.

### 기여자가 해야 할 일
구체적으로 뭘 코딩/수정해야 하는지 명확하게 설명.

### 난이도
🟢 쉬움 / 🟡 보통 / 🔴 어려움 — 이유 한 문장.

### 레드플래그
아래 항목 중 해당하는 것이 있으면 명시 (없으면 "없음"):
- 이미 수정됨 (커밋/PR/다른 티켓으로)
- 중복 티켓
- 재현 불가
- 종료 제안됨
- 커뮤니티 합의 먼저 필요 (설계 논의, RFC 필요)
- 의도된 동작 (wontfix)

### 첫 기여자 추천 여부
✅ 추천 / ⚠️ 주의 / ❌ 비추천 — 이유 한 문장.

### 참고할 Django 코드 위치
관련 모듈/파일 경로 힌트 (알 수 있는 범위에서).

---

English report format:

## 🎫 Ticket #{ticket_id} Triage Report

**Title**: {title}
**Component**: {component}
**Status**: {status} / {owner or unassigned}
**Link**: https://code.djangoproject.com/ticket/{ticket_id}

---

### Bug Summary
One or two sentences describing the bug.

### What the contributor needs to do
Concrete description of what code changes are needed.

### Difficulty
🟢 Easy / 🟡 Medium / 🔴 Hard — one sentence reason.

### Red Flags
List any that apply (or "None"):
- Already fixed (by commit / PR / another ticket)
- Duplicate
- Cannot reproduce
- Closing proposed
- Needs community consensus first (design discussion, RFC)
- Working as intended (wontfix)

### Recommendation for first-time contributors
✅ Recommended / ⚠️ Caution / ❌ Not recommended — one sentence reason.

### Relevant Django code areas
Hints about which modules/files to look at.
