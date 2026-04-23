# Django 기여 추천 티켓

> 생성일: 2026-04-23  
> 조건: `Stage=Accepted`, `Type=Bug`, `Has patch=Yes`, `Patch needs improvement=Yes`  
> 전략: 수정된 지 오래됐지만 패치가 있는 티켓을 이어서 완성하는 **벌처 전략**

---

## 점수 기준

| 점수 | 조건 |
|------|------|
| +50 | 수정 6~12개월 전 (벌처 최적) |
| +35 | 수정 12~24개월 전 (벌처 적합) |
| +15 | 수정 24~48개월 전 |
| +20 | 미할당 티켓 |
| -10 | 담당자 있음 |
| -15 | 생성 5년 이상 (오래된 티켓) |
| -30 | 생성 8년 이상 (논의 많을 가능성) |
| -25 | 복잡한 환경 설정 필요 (Oracle 등) |
| -20 | 커뮤니티 합의 필요 가능성 |
| -30 | 수정 6개월 미만 (최근 활동) |

---

## 추천 티켓 Top 15

| 순위 | 점수 | 티켓 | 컴포넌트 | 상태 | 마지막 수정 | 비고 |
|------|------|------|----------|------|-------------|------|
| 1 | 🟡 40 | [#23268](https://code.djangoproject.com/ticket/23268) Fixtures: Natural Key support for Generic Foreign Keys | Core (Serialization) | new / 미할당 | 2025-06-27 | 수정 10개월 전 (벌처 최적) / 생성 12년 전 (너무 오래된 티켓 - 논의 많을 가능성) / 미할당 |
| 2 | 🟡 40 | [#26223](https://code.djangoproject.com/ticket/26223) Squashing migrations with preserve_default=False keeps the default | Migrations | new / 미할당 | 2025-10-20 | 수정 6개월 전 (벌처 최적) / 생성 10년 전 (너무 오래된 티켓 - 논의 많을 가능성) / 미할당 |
| 3 | 🟡 40 | [#28594](https://code.djangoproject.com/ticket/28594) Value error on related user name during save of user model | contrib.auth | new / 미할당 | 2025-05-15 | 수정 11개월 전 (벌처 최적) / 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) / 미할당 |
| 4 | 🟡 40 | [#28646](https://code.djangoproject.com/ticket/28646) Migration calls "CREATE INDEX" when one already exists when 'unique' field attribute is added (PostgreSQL) | Migrations | new / 미할당 | 2025-08-31 | 수정 8개월 전 (벌처 최적) / 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) / 미할당 |
| 5 | 🟡 40 | [#28944](https://code.djangoproject.com/ticket/28944) Chaining values()/values_list() after QuerySet.select_for_update(of=()) crashes | Database layer (models, ORM) | new / 미할당 | 2025-09-20 | 수정 7개월 전 (벌처 최적) / 생성 8년 전 (너무 오래된 티켓 - 논의 많을 가능성) / 미할당 |
| 6 | 🟡 40 | [#33450](https://code.djangoproject.com/ticket/33450) Integer primary key is wrongly casted to UUID when filtering GenericRelation on model with UUID primary key. | contrib.contenttypes | assigned / Clifford Gama | 2025-05-20 | 수정 11개월 전 (벌처 최적) / 할당됨: Clifford Gama |
| 7 | 🟡 40 | [#35333](https://code.djangoproject.com/ticket/35333) Template tag `unlocalize` does not work with `date` and `time` filters. | Template system | assigned / Ahmed Nassar | 2025-05-20 | 수정 11개월 전 (벌처 최적) / 할당됨: Ahmed Nassar |
| 8 | 🟡 40 | [#35673](https://code.djangoproject.com/ticket/35673) ExceptionReporter.get_traceback_data() does not handle when request.GET data exceeds DATA_UPLOAD_MAX_NUMBER_FIELDS | Error reporting | assigned / Ahmed Nassar | 2025-08-11 | 수정 8개월 전 (벌처 최적) / 할당됨: Ahmed Nassar |
| 9 | 🟡 40 | [#35902](https://code.djangoproject.com/ticket/35902) migrate --syncdb and TEST_MIGRATE break for models with fields requiring extensions, and custom collation or types on Postgres | Migrations | assigned / wadhah mahrouk | 2025-05-07 | 수정 12개월 전 (벌처 최적) / 할당됨: wadhah mahrouk |
| 10 | 🟡 40 | [#35911](https://code.djangoproject.com/ticket/35911) FilteredSelectMultiple Widget Not Functional in Inline Formset After Form Deletion | contrib.admin | assigned / Antoliny | 2025-08-01 | 수정 9개월 전 (벌처 최적) / 할당됨: Antoliny |
| 11 | 🟡 40 | [#36168](https://code.djangoproject.com/ticket/36168) Backwards migration to replaced migration when other app has squashed migrations can lead to FieldDoesNotExist error due to incorrect state | Migrations | assigned / houston0222 | 2025-09-29 | 수정 7개월 전 (벌처 최적) / 할당됨: houston0222 |
| 12 | 🟡 40 | [#36248](https://code.djangoproject.com/ticket/36248) Bulk deletion of model referred to by a SET_NULL key can exceed parameter limit | Database layer (models, ORM) | assigned / bobince | 2025-09-25 | 수정 7개월 전 (벌처 최적) / 할당됨: bobince |
| 13 | 🟡 40 | [#36259](https://code.djangoproject.com/ticket/36259) Unsaved related object with primary_key=True field does not raise unsaved object error | Database layer (models, ORM) | assigned / Clifford Gama | 2025-06-07 | 수정 11개월 전 (벌처 최적) / 할당됨: Clifford Gama |
| 14 | 🟡 40 | [#36336](https://code.djangoproject.com/ticket/36336) Incorrect size of first autocomple in Inlines with "collapse" class (on chromium based browsers?) | contrib.admin | assigned / yassershkeir | 2025-07-14 | 수정 9개월 전 (벌처 최적) / 할당됨: yassershkeir |
| 15 | 🟡 40 | [#36472](https://code.djangoproject.com/ticket/36472) GeneratedField(primary_key=True) crashes on create(), and other issues | Database layer (models, ORM) | assigned / David Sanders | 2025-08-13 | 수정 8개월 전 (벌처 최적) / 할당됨: David Sanders |

---

## 상세

### 1. [🟡 #23268] Fixtures: Natural Key support for Generic Foreign Keys

- **링크**: https://code.djangoproject.com/ticket/23268
- **컴포넌트**: Core (Serialization)
- **상태**: new / 미할당
- **마지막 수정**: 2025-06-27
- **생성일**: 2014-08-11
- **점수**: 40 (수정 10개월 전 (벌처 최적) | 생성 12년 전 (너무 오래된 티켓 - 논의 많을 가능성) | 미할당)

### 2. [🟡 #26223] Squashing migrations with preserve_default=False keeps the default

- **링크**: https://code.djangoproject.com/ticket/26223
- **컴포넌트**: Migrations
- **상태**: new / 미할당
- **마지막 수정**: 2025-10-20
- **생성일**: 2016-02-15
- **점수**: 40 (수정 6개월 전 (벌처 최적) | 생성 10년 전 (너무 오래된 티켓 - 논의 많을 가능성) | 미할당)

### 3. [🟡 #28594] Value error on related user name during save of user model

- **링크**: https://code.djangoproject.com/ticket/28594
- **컴포넌트**: contrib.auth
- **상태**: new / 미할당
- **마지막 수정**: 2025-05-15
- **생성일**: 2017-09-13
- **점수**: 40 (수정 11개월 전 (벌처 최적) | 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) | 미할당)

### 4. [🟡 #28646] Migration calls "CREATE INDEX" when one already exists when 'unique' field attribute is added (PostgreSQL)

- **링크**: https://code.djangoproject.com/ticket/28646
- **컴포넌트**: Migrations
- **상태**: new / 미할당
- **마지막 수정**: 2025-08-31
- **생성일**: 2017-09-27
- **점수**: 40 (수정 8개월 전 (벌처 최적) | 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) | 미할당)

### 5. [🟡 #28944] Chaining values()/values_list() after QuerySet.select_for_update(of=()) crashes

- **링크**: https://code.djangoproject.com/ticket/28944
- **컴포넌트**: Database layer (models, ORM)
- **상태**: new / 미할당
- **마지막 수정**: 2025-09-20
- **생성일**: 2017-12-19
- **점수**: 40 (수정 7개월 전 (벌처 최적) | 생성 8년 전 (너무 오래된 티켓 - 논의 많을 가능성) | 미할당)

### 6. [🟡 #33450] Integer primary key is wrongly casted to UUID when filtering GenericRelation on model with UUID primary key.

- **링크**: https://code.djangoproject.com/ticket/33450
- **컴포넌트**: contrib.contenttypes
- **상태**: assigned / Clifford Gama
- **마지막 수정**: 2025-05-20
- **생성일**: 2022-01-19
- **점수**: 40 (수정 11개월 전 (벌처 최적) | 할당됨: Clifford Gama)

### 7. [🟡 #35333] Template tag `unlocalize` does not work with `date` and `time` filters.

- **링크**: https://code.djangoproject.com/ticket/35333
- **컴포넌트**: Template system
- **상태**: assigned / Ahmed Nassar
- **마지막 수정**: 2025-05-20
- **생성일**: 2024-03-26
- **점수**: 40 (수정 11개월 전 (벌처 최적) | 할당됨: Ahmed Nassar)

### 8. [🟡 #35673] ExceptionReporter.get_traceback_data() does not handle when request.GET data exceeds DATA_UPLOAD_MAX_NUMBER_FIELDS

- **링크**: https://code.djangoproject.com/ticket/35673
- **컴포넌트**: Error reporting
- **상태**: assigned / Ahmed Nassar
- **마지막 수정**: 2025-08-11
- **생성일**: 2024-08-13
- **점수**: 40 (수정 8개월 전 (벌처 최적) | 할당됨: Ahmed Nassar)

### 9. [🟡 #35902] migrate --syncdb and TEST_MIGRATE break for models with fields requiring extensions, and custom collation or types on Postgres

- **링크**: https://code.djangoproject.com/ticket/35902
- **컴포넌트**: Migrations
- **상태**: assigned / wadhah mahrouk
- **마지막 수정**: 2025-05-07
- **생성일**: 2024-11-10
- **점수**: 40 (수정 12개월 전 (벌처 최적) | 할당됨: wadhah mahrouk)

### 10. [🟡 #35911] FilteredSelectMultiple Widget Not Functional in Inline Formset After Form Deletion

- **링크**: https://code.djangoproject.com/ticket/35911
- **컴포넌트**: contrib.admin
- **상태**: assigned / Antoliny
- **마지막 수정**: 2025-08-01
- **생성일**: 2024-11-14
- **점수**: 40 (수정 9개월 전 (벌처 최적) | 할당됨: Antoliny)

### 11. [🟡 #36168] Backwards migration to replaced migration when other app has squashed migrations can lead to FieldDoesNotExist error due to incorrect state

- **링크**: https://code.djangoproject.com/ticket/36168
- **컴포넌트**: Migrations
- **상태**: assigned / houston0222
- **마지막 수정**: 2025-09-29
- **생성일**: 2025-02-04
- **점수**: 40 (수정 7개월 전 (벌처 최적) | 할당됨: houston0222)

### 12. [🟡 #36248] Bulk deletion of model referred to by a SET_NULL key can exceed parameter limit

- **링크**: https://code.djangoproject.com/ticket/36248
- **컴포넌트**: Database layer (models, ORM)
- **상태**: assigned / bobince
- **마지막 수정**: 2025-09-25
- **생성일**: 2025-03-11
- **점수**: 40 (수정 7개월 전 (벌처 최적) | 할당됨: bobince)

### 13. [🟡 #36259] Unsaved related object with primary_key=True field does not raise unsaved object error

- **링크**: https://code.djangoproject.com/ticket/36259
- **컴포넌트**: Database layer (models, ORM)
- **상태**: assigned / Clifford Gama
- **마지막 수정**: 2025-06-07
- **생성일**: 2025-03-16
- **점수**: 40 (수정 11개월 전 (벌처 최적) | 할당됨: Clifford Gama)

### 14. [🟡 #36336] Incorrect size of first autocomple in Inlines with "collapse" class (on chromium based browsers?)

- **링크**: https://code.djangoproject.com/ticket/36336
- **컴포넌트**: contrib.admin
- **상태**: assigned / yassershkeir
- **마지막 수정**: 2025-07-14
- **생성일**: 2025-04-19
- **점수**: 40 (수정 9개월 전 (벌처 최적) | 할당됨: yassershkeir)

### 15. [🟡 #36472] GeneratedField(primary_key=True) crashes on create(), and other issues

- **링크**: https://code.djangoproject.com/ticket/36472
- **컴포넌트**: Database layer (models, ORM)
- **상태**: assigned / David Sanders
- **마지막 수정**: 2025-08-13
- **생성일**: 2025-06-18
- **점수**: 40 (수정 8개월 전 (벌처 최적) | 할당됨: David Sanders)
