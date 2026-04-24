# Recommended Django Tickets for Contributors

> Generated: 2026-04-23  
> Filter: `Stage=Accepted`, `Type=Bug`, `Has patch=Yes`, `Patch needs improvement=Yes`  
> Strategy: **Vulture** — pick up stale patches that need finishing

---

## Scoring Criteria

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

---

## Top 15 Recommended Tickets

| Rank | Score | Ticket | Component | Status | Last Modified | Notes |
|------|-------|--------|-----------|--------|---------------|-------|
| 1 | 🟡 40 | [#23268](https://code.djangoproject.com/ticket/23268) Fixtures: Natural Key support for Generic Foreign Keys | Core (Serialization) | new / unassigned | 2025-06-27 | modified 10mo ago (vulture sweet spot) / 생성 12년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned |
| 2 | 🟡 40 | [#26223](https://code.djangoproject.com/ticket/26223) Squashing migrations with preserve_default=False keeps the default | Migrations | new / unassigned | 2025-10-20 | modified 6mo ago (vulture sweet spot) / 생성 10년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned |
| 3 | 🟡 40 | [#28594](https://code.djangoproject.com/ticket/28594) Value error on related user name during save of user model | contrib.auth | new / unassigned | 2025-05-15 | modified 11mo ago (vulture sweet spot) / 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned |
| 4 | 🟡 40 | [#28646](https://code.djangoproject.com/ticket/28646) Migration calls "CREATE INDEX" when one already exists when 'unique' field attribute is added (PostgreSQL) | Migrations | new / unassigned | 2025-08-31 | modified 8mo ago (vulture sweet spot) / 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned |
| 5 | 🟡 40 | [#28944](https://code.djangoproject.com/ticket/28944) Chaining values()/values_list() after QuerySet.select_for_update(of=()) crashes | Database layer (models, ORM) | new / unassigned | 2025-09-20 | modified 7mo ago (vulture sweet spot) / 생성 8년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned |
| 6 | 🟡 40 | [#33450](https://code.djangoproject.com/ticket/33450) Integer primary key is wrongly casted to UUID when filtering GenericRelation on model with UUID primary key. | contrib.contenttypes | assigned / Clifford Gama | 2025-05-20 | modified 11mo ago (vulture sweet spot) / assigned: Clifford Gama |
| 7 | 🟡 40 | [#35333](https://code.djangoproject.com/ticket/35333) Template tag `unlocalize` does not work with `date` and `time` filters. | Template system | assigned / Ahmed Nassar | 2025-05-20 | modified 11mo ago (vulture sweet spot) / assigned: Ahmed Nassar |
| 8 | 🟡 40 | [#35673](https://code.djangoproject.com/ticket/35673) ExceptionReporter.get_traceback_data() does not handle when request.GET data exceeds DATA_UPLOAD_MAX_NUMBER_FIELDS | Error reporting | assigned / Ahmed Nassar | 2025-08-11 | modified 8mo ago (vulture sweet spot) / assigned: Ahmed Nassar |
| 9 | 🟡 40 | [#35902](https://code.djangoproject.com/ticket/35902) migrate --syncdb and TEST_MIGRATE break for models with fields requiring extensions, and custom collation or types on Postgres | Migrations | assigned / wadhah mahrouk | 2025-05-07 | modified 12mo ago (vulture sweet spot) / assigned: wadhah mahrouk |
| 10 | 🟡 40 | [#35911](https://code.djangoproject.com/ticket/35911) FilteredSelectMultiple Widget Not Functional in Inline Formset After Form Deletion | contrib.admin | assigned / Antoliny | 2025-08-01 | modified 9mo ago (vulture sweet spot) / assigned: Antoliny |
| 11 | 🟡 40 | [#36168](https://code.djangoproject.com/ticket/36168) Backwards migration to replaced migration when other app has squashed migrations can lead to FieldDoesNotExist error due to incorrect state | Migrations | assigned / houston0222 | 2025-09-29 | modified 7mo ago (vulture sweet spot) / assigned: houston0222 |
| 12 | 🟡 40 | [#36248](https://code.djangoproject.com/ticket/36248) Bulk deletion of model referred to by a SET_NULL key can exceed parameter limit | Database layer (models, ORM) | assigned / bobince | 2025-09-25 | modified 7mo ago (vulture sweet spot) / assigned: bobince |
| 13 | 🟡 40 | [#36259](https://code.djangoproject.com/ticket/36259) Unsaved related object with primary_key=True field does not raise unsaved object error | Database layer (models, ORM) | assigned / Clifford Gama | 2025-06-07 | modified 11mo ago (vulture sweet spot) / assigned: Clifford Gama |
| 14 | 🟡 40 | [#36336](https://code.djangoproject.com/ticket/36336) Incorrect size of first autocomple in Inlines with "collapse" class (on chromium based browsers?) | contrib.admin | assigned / yassershkeir | 2025-07-14 | modified 9mo ago (vulture sweet spot) / assigned: yassershkeir |
| 15 | 🟡 40 | [#36472](https://code.djangoproject.com/ticket/36472) GeneratedField(primary_key=True) crashes on create(), and other issues | Database layer (models, ORM) | assigned / David Sanders | 2025-08-13 | modified 8mo ago (vulture sweet spot) / assigned: David Sanders |

---

## Details

### 1. [🟡 #23268] Fixtures: Natural Key support for Generic Foreign Keys

- **Link**: https://code.djangoproject.com/ticket/23268
- **Component**: Core (Serialization)
- **Status**: new / unassigned
- **Last modified**: 2025-06-27
- **Created**: 2014-08-11
- **Score**: 40 (modified 10mo ago (vulture sweet spot) / 생성 12년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned)

### 2. [🟡 #26223] Squashing migrations with preserve_default=False keeps the default

- **Link**: https://code.djangoproject.com/ticket/26223
- **Component**: Migrations
- **Status**: new / unassigned
- **Last modified**: 2025-10-20
- **Created**: 2016-02-15
- **Score**: 40 (modified 6mo ago (vulture sweet spot) / 생성 10년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned)

### 3. [🟡 #28594] Value error on related user name during save of user model

- **Link**: https://code.djangoproject.com/ticket/28594
- **Component**: contrib.auth
- **Status**: new / unassigned
- **Last modified**: 2025-05-15
- **Created**: 2017-09-13
- **Score**: 40 (modified 11mo ago (vulture sweet spot) / 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned)

### 4. [🟡 #28646] Migration calls "CREATE INDEX" when one already exists when 'unique' field attribute is added (PostgreSQL)

- **Link**: https://code.djangoproject.com/ticket/28646
- **Component**: Migrations
- **Status**: new / unassigned
- **Last modified**: 2025-08-31
- **Created**: 2017-09-27
- **Score**: 40 (modified 8mo ago (vulture sweet spot) / 생성 9년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned)

### 5. [🟡 #28944] Chaining values()/values_list() after QuerySet.select_for_update(of=()) crashes

- **Link**: https://code.djangoproject.com/ticket/28944
- **Component**: Database layer (models, ORM)
- **Status**: new / unassigned
- **Last modified**: 2025-09-20
- **Created**: 2017-12-19
- **Score**: 40 (modified 7mo ago (vulture sweet spot) / 생성 8년 전 (너무 오래된 티켓 - 논의 많을 가능성) / unassigned)

### 6. [🟡 #33450] Integer primary key is wrongly casted to UUID when filtering GenericRelation on model with UUID primary key.

- **Link**: https://code.djangoproject.com/ticket/33450
- **Component**: contrib.contenttypes
- **Status**: assigned / Clifford Gama
- **Last modified**: 2025-05-20
- **Created**: 2022-01-19
- **Score**: 40 (modified 11mo ago (vulture sweet spot) / assigned: Clifford Gama)

### 7. [🟡 #35333] Template tag `unlocalize` does not work with `date` and `time` filters.

- **Link**: https://code.djangoproject.com/ticket/35333
- **Component**: Template system
- **Status**: assigned / Ahmed Nassar
- **Last modified**: 2025-05-20
- **Created**: 2024-03-26
- **Score**: 40 (modified 11mo ago (vulture sweet spot) / assigned: Ahmed Nassar)

### 8. [🟡 #35673] ExceptionReporter.get_traceback_data() does not handle when request.GET data exceeds DATA_UPLOAD_MAX_NUMBER_FIELDS

- **Link**: https://code.djangoproject.com/ticket/35673
- **Component**: Error reporting
- **Status**: assigned / Ahmed Nassar
- **Last modified**: 2025-08-11
- **Created**: 2024-08-13
- **Score**: 40 (modified 8mo ago (vulture sweet spot) / assigned: Ahmed Nassar)

### 9. [🟡 #35902] migrate --syncdb and TEST_MIGRATE break for models with fields requiring extensions, and custom collation or types on Postgres

- **Link**: https://code.djangoproject.com/ticket/35902
- **Component**: Migrations
- **Status**: assigned / wadhah mahrouk
- **Last modified**: 2025-05-07
- **Created**: 2024-11-10
- **Score**: 40 (modified 12mo ago (vulture sweet spot) / assigned: wadhah mahrouk)

### 10. [🟡 #35911] FilteredSelectMultiple Widget Not Functional in Inline Formset After Form Deletion

- **Link**: https://code.djangoproject.com/ticket/35911
- **Component**: contrib.admin
- **Status**: assigned / Antoliny
- **Last modified**: 2025-08-01
- **Created**: 2024-11-14
- **Score**: 40 (modified 9mo ago (vulture sweet spot) / assigned: Antoliny)

### 11. [🟡 #36168] Backwards migration to replaced migration when other app has squashed migrations can lead to FieldDoesNotExist error due to incorrect state

- **Link**: https://code.djangoproject.com/ticket/36168
- **Component**: Migrations
- **Status**: assigned / houston0222
- **Last modified**: 2025-09-29
- **Created**: 2025-02-04
- **Score**: 40 (modified 7mo ago (vulture sweet spot) / assigned: houston0222)

### 12. [🟡 #36248] Bulk deletion of model referred to by a SET_NULL key can exceed parameter limit

- **Link**: https://code.djangoproject.com/ticket/36248
- **Component**: Database layer (models, ORM)
- **Status**: assigned / bobince
- **Last modified**: 2025-09-25
- **Created**: 2025-03-11
- **Score**: 40 (modified 7mo ago (vulture sweet spot) / assigned: bobince)

### 13. [🟡 #36259] Unsaved related object with primary_key=True field does not raise unsaved object error

- **Link**: https://code.djangoproject.com/ticket/36259
- **Component**: Database layer (models, ORM)
- **Status**: assigned / Clifford Gama
- **Last modified**: 2025-06-07
- **Created**: 2025-03-16
- **Score**: 40 (modified 11mo ago (vulture sweet spot) / assigned: Clifford Gama)

### 14. [🟡 #36336] Incorrect size of first autocomple in Inlines with "collapse" class (on chromium based browsers?)

- **Link**: https://code.djangoproject.com/ticket/36336
- **Component**: contrib.admin
- **Status**: assigned / yassershkeir
- **Last modified**: 2025-07-14
- **Created**: 2025-04-19
- **Score**: 40 (modified 9mo ago (vulture sweet spot) / assigned: yassershkeir)

### 15. [🟡 #36472] GeneratedField(primary_key=True) crashes on create(), and other issues

- **Link**: https://code.djangoproject.com/ticket/36472
- **Component**: Database layer (models, ORM)
- **Status**: assigned / David Sanders
- **Last modified**: 2025-08-13
- **Created**: 2025-06-18
- **Score**: 40 (modified 8mo ago (vulture sweet spot) / assigned: David Sanders)
