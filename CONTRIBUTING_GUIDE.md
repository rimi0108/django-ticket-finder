# Django 첫 기여를 위한 티켓 선별 가이드

Claude가 티켓을 분석할 때 참고하는 기준 문서입니다.

---

## 좋은 티켓의 조건 — Vulture 전략

패치가 이미 존재하지만 오래 방치된 티켓을 이어서 완성하는 전략입니다.

| 조건 | 값 |
|------|----|
| Type | Bug |
| Triage Stage | **Accepted** |
| Has patch | Yes |
| Patch needs improvement | Yes |
| Last modified | **6개월 이상 전** |

**핵심 원리**: 원 작성자가 자리를 비웠을 가능성이 높고, 이미 방향이 정해져 있어서 첫 기여자가 이어받기 좋습니다.

> ⚠️ Triage Stage가 **Unreviewed**인 티켓은 논의 없이 바로 닫힐 가능성이 크므로 피하세요.

---

## 피해야 할 티켓

### 1. 최근 활동이 있는 티켓
- 누군가 assigned되어 있거나 최근 6개월 내에 수정된 티켓
- 다른 사람이 작업 중일 수 있어 충돌 가능성이 높음

### 2. 너무 오래된 티켓
- 생성된 지 8년 이상 된 티켓은 댓글이 많고 맥락 파악이 어려움
- 오래된 버전(Django 1.x) 기준으로 작성된 티켓은 현재 코드베이스와 많이 달라졌을 수 있음

### 3. 복잡한 환경 설정이 필요한 티켓
- Oracle DB, 특정 인프라(Docker, Kubernetes), MS SQL 등
- 환경을 직접 세팅해야 재현 가능한 티켓은 초보자에게 진입 장벽이 높음

### 4. 커뮤니티 합의가 먼저 필요한 티켓
- 새 기능 제안, 설계 변경, RFC가 필요한 티켓
- Breaking change, deprecation 관련 논의
- 코드 작성 전에 django-developers 메일링 리스트 토론이 선행돼야 하는 티켓

---

## 레드플래그 — 이미 문제가 있는 티켓

티켓 댓글을 읽을 때 아래 신호가 있으면 기여를 피하세요.

| 신호 | 의미 |
|------|------|
| "already fixed", "fixed in #XXXX", "fixed by commit" | 이미 다른 커밋/티켓으로 수정됨 |
| "duplicate of", "already reported" | 중복 티켓 |
| "wontfix", "not a bug", "by design", "working as intended" | 수정 거부 또는 의도된 동작 |
| "closing as", "suggest closing", "should be closed" | 종료 제안됨 |
| "cannot reproduce", "can't reproduce", "no longer reproduces" | 재현 불가 |
| "needs design decision", "mailing list first", "django-developers" | 커뮤니티 합의 먼저 필요 |

---

## 난이도 판단 기준

### 🟢 쉬움
- Template system, Forms, Utilities, contrib.admin (UI), Error reporting, Testing framework
- 댓글 7개 이하, 생성 3년 미만
- 수정 범위가 명확하고 한두 파일 내에서 해결 가능한 버그

### 🟡 보통
- Migrations, contrib.auth, Core (Serialization), Internationalization
- 댓글 8~14개, 또는 생성 4~7년
- 여러 파일을 수정해야 하거나 테스트 작성이 필요한 경우

### 🔴 어려움
- Database layer (models, ORM), HTTP handling, Core (Cache), Signals
- 댓글 15개 이상, 또는 생성 8년 이상
- SQL 쿼리 생성 로직, 쿼리셋 내부, 마이그레이션 엔진 등 Django 코어 깊은 곳을 수정해야 하는 경우

---

## 좋은 티켓의 점수 기준 (참고)

| 점수 | 조건 |
|------|------|
| +50 | 수정 6~12개월 전 (벌처 최적) |
| +35 | 수정 12~24개월 전 |
| +35 | 미할당 |
| -10 | 담당자 있음 + 수정 6개월 이상 전 (담당자 이탈 가능성) |
| -25 | 담당자 있음 + 수정 3개월 미만 (현재 진행 중) |
| -40 | 생성 8년 이상 |
| -45 | 댓글 30개 이상 |
| -60 | 🚨 이미 수정됨 |
| -55 | 🚨 중복 / wontfix |
| -45 | 🚨 종료 제안됨 |

---

## 기여 프로세스 요약

1. 이 도구로 티켓을 선별한다
2. 티켓 페이지와 첨부 패치를 읽는다
3. Django 레포를 클론한다: `git clone https://github.com/django/django.git`
4. 개발 환경 세팅: [Django contributing guide](https://docs.djangoproject.com/en/dev/internals/contributing/)
5. 패치를 개선하고 테스트를 실행한 뒤 Trac에 업로드한다

**참고 링크**
- [Django Trac 쿼리](https://code.djangoproject.com/query)
- [Triaging tickets 가이드](https://docs.djangoproject.com/en/dev/internals/contributing/triaging-tickets/)
- [Writing code 가이드](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/)
