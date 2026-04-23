# Recommended Django Tickets for Contributors

> Generated: 2026-04-23  
> Filter: `Stage=Accepted`, `Type=Bug`, `Has patch=Yes`, `Patch needs improvement=Yes`  
> Strategy: **Vulture** — pick up stale patches that need finishing

---

## Scoring Criteria

| Score | Condition |
|-------|-----------|
| +50 | Modified 6–12 months ago (Vulture sweet spot) |
| +35 | Modified 12–24 months ago (Vulture good) |
| +15 | Modified 24–48 months ago (older) |
| +20 | Unassigned |
| −30 | Modified < 6 months ago (recently active) |
| −10 | Already assigned |

---

## Top 15 Recommended Tickets

| Rank | Score | Ticket | Component | Status | Last Modified | Notes |
|------|-------|--------|-----------|--------|---------------|-------|
| 1 | 🟢 70 | [#23268](https://code.djangoproject.com/ticket/23268) Fixtures: Natural Key support for Generic Foreign Keys | Core (Serialization) | new / unassigned | 2025-06-27 | modified 10mo ago (vulture sweet spot) / unassigned |
| 2 | 🟢 70 | [#26223](https://code.djangoproject.com/ticket/26223) Squashing migrations with preserve_default=False keeps the default | Migrations | new / unassigned | 2025-10-20 | modified 6mo ago (vulture sweet spot) / unassigned |
| 3 | 🟢 70 | [#28594](https://code.djangoproject.com/ticket/28594) Value error on related user name during save of user model | contrib.auth | new / unassigned | 2025-05-15 | modified 11mo ago (vulture sweet spot) / unassigned |
| 4 | 🟢 70 | [#28646](https://code.djangoproject.com/ticket/28646) Migration calls "CREATE INDEX" when one already exists when 'unique' field attribute is added (PostgreSQL) | Migrations | new / unassigned | 2025-08-31 | modified 8mo ago (vulture sweet spot) / unassigned |
| 5 | 🟢 70 | [#28944](https://code.djangoproject.com/ticket/28944) Chaining values()/values_list() after QuerySet.select_for_update(of=()) crashes | Database layer (models, ORM) | new / unassigned | 2025-09-20 | modified 7mo ago (vulture sweet spot) / unassigned |
| 6 | 🟡 55 | [#13539](https://code.djangoproject.com/ticket/13539) The delete confirmation page does not check for object-level permissions when building the related list | contrib.admin | new / unassigned | 2024-11-07 | modified 18mo ago (vulture good) / unassigned |
| 7 | 🟡 55 | [#15130](https://code.djangoproject.com/ticket/15130) Model.validate_unique method doesn't take in account multi-db | Database layer (models, ORM) | new / unassigned | 2024-05-27 | modified 23mo ago (vulture good) / unassigned |
| 8 | 🟡 55 | [#23251](https://code.djangoproject.com/ticket/23251) Use a temporary folder to store uploaded files during tests | Testing framework | new / unassigned | 2024-10-15 | modified 18mo ago (vulture good) / unassigned |
| 9 | 🟡 55 | [#26756](https://code.djangoproject.com/ticket/26756) Changing of model's verbose_name does not change the names of the model's permissions | contrib.auth | new / unassigned | 2025-04-10 | modified 13mo ago (vulture good) / unassigned |
| 10 | 🟡 40 | [#13314](https://code.djangoproject.com/ticket/13314) "FileField" validation does not account for "upload_to" when counting characters | Forms | assigned / Andrew Northall | 2025-05-12 | modified 12mo ago (vulture sweet spot) / assigned: Andrew Northall |
| 11 | 🟡 40 | [#23557](https://code.djangoproject.com/ticket/23557) Prevent silent extension of explicit GROUP BY when using order_by | Database layer (models, ORM) | assigned / ontowhee | 2025-06-07 | modified 11mo ago (vulture sweet spot) / assigned: ontowhee |
| 12 | 🟡 40 | [#25656](https://code.djangoproject.com/ticket/25656) Recent Actions admin section contains link to edit form even when user does not have edit permission | contrib.admin | assigned / AP Jama | 2025-07-20 | modified 9mo ago (vulture sweet spot) / assigned: AP Jama |
| 13 | 🟡 40 | [#25991](https://code.djangoproject.com/ticket/25991) A new implementation for exclude() queries | Database layer (models, ORM) | assigned / Eddy ADEGNANDJOU | 2025-05-19 | modified 11mo ago (vulture sweet spot) / assigned: Eddy ADEGNANDJOU |
| 14 | 🟡 40 | [#26619](https://code.djangoproject.com/ticket/26619) BaseCache incr method will reset the timeout | Core (Cache system) | assigned / Simone Macri | 2025-09-19 | modified 7mo ago (vulture sweet spot) / assigned: Simone Macri |
| 15 | 🟡 40 | [#27775](https://code.djangoproject.com/ticket/27775) Signed cookies does not support custom expiry | contrib.sessions | assigned / Abe Hanoka | 2025-08-26 | modified 8mo ago (vulture sweet spot) / assigned: Abe Hanoka |

---

## Details

### 1. [🟢 #23268] Fixtures: Natural Key support for Generic Foreign Keys

- **Link**: https://code.djangoproject.com/ticket/23268
- **Component**: Core (Serialization)
- **Status**: new / unassigned
- **Last modified**: 2025-06-27
- **Created**: 2014-08-11
- **Score**: 70 (modified 10mo ago (vulture sweet spot) / unassigned)

### 2. [🟢 #26223] Squashing migrations with preserve_default=False keeps the default

- **Link**: https://code.djangoproject.com/ticket/26223
- **Component**: Migrations
- **Status**: new / unassigned
- **Last modified**: 2025-10-20
- **Created**: 2016-02-15
- **Score**: 70 (modified 6mo ago (vulture sweet spot) / unassigned)

### 3. [🟢 #28594] Value error on related user name during save of user model

- **Link**: https://code.djangoproject.com/ticket/28594
- **Component**: contrib.auth
- **Status**: new / unassigned
- **Last modified**: 2025-05-15
- **Created**: 2017-09-13
- **Score**: 70 (modified 11mo ago (vulture sweet spot) / unassigned)

### 4. [🟢 #28646] Migration calls "CREATE INDEX" when one already exists when 'unique' field attribute is added (PostgreSQL)

- **Link**: https://code.djangoproject.com/ticket/28646
- **Component**: Migrations
- **Status**: new / unassigned
- **Last modified**: 2025-08-31
- **Created**: 2017-09-27
- **Score**: 70 (modified 8mo ago (vulture sweet spot) / unassigned)

### 5. [🟢 #28944] Chaining values()/values_list() after QuerySet.select_for_update(of=()) crashes

- **Link**: https://code.djangoproject.com/ticket/28944
- **Component**: Database layer (models, ORM)
- **Status**: new / unassigned
- **Last modified**: 2025-09-20
- **Created**: 2017-12-19
- **Score**: 70 (modified 7mo ago (vulture sweet spot) / unassigned)

### 6. [🟡 #13539] The delete confirmation page does not check for object-level permissions when building the related list

- **Link**: https://code.djangoproject.com/ticket/13539
- **Component**: contrib.admin
- **Status**: new / unassigned
- **Last modified**: 2024-11-07
- **Created**: 2010-05-14
- **Score**: 55 (modified 18mo ago (vulture good) / unassigned)

### 7. [🟡 #15130] Model.validate_unique method doesn't take in account multi-db

- **Link**: https://code.djangoproject.com/ticket/15130
- **Component**: Database layer (models, ORM)
- **Status**: new / unassigned
- **Last modified**: 2024-05-27
- **Created**: 2011-01-20
- **Score**: 55 (modified 23mo ago (vulture good) / unassigned)

### 8. [🟡 #23251] Use a temporary folder to store uploaded files during tests

- **Link**: https://code.djangoproject.com/ticket/23251
- **Component**: Testing framework
- **Status**: new / unassigned
- **Last modified**: 2024-10-15
- **Created**: 2014-08-06
- **Score**: 55 (modified 18mo ago (vulture good) / unassigned)

### 9. [🟡 #26756] Changing of model's verbose_name does not change the names of the model's permissions

- **Link**: https://code.djangoproject.com/ticket/26756
- **Component**: contrib.auth
- **Status**: new / unassigned
- **Last modified**: 2025-04-10
- **Created**: 2016-06-14
- **Score**: 55 (modified 13mo ago (vulture good) / unassigned)

### 10. [🟡 #13314] "FileField" validation does not account for "upload_to" when counting characters

- **Link**: https://code.djangoproject.com/ticket/13314
- **Component**: Forms
- **Status**: assigned / Andrew Northall
- **Last modified**: 2025-05-12
- **Created**: 2010-04-09
- **Score**: 40 (modified 12mo ago (vulture sweet spot) / assigned: Andrew Northall)

### 11. [🟡 #23557] Prevent silent extension of explicit GROUP BY when using order_by

- **Link**: https://code.djangoproject.com/ticket/23557
- **Component**: Database layer (models, ORM)
- **Status**: assigned / ontowhee
- **Last modified**: 2025-06-07
- **Created**: 2014-09-25
- **Score**: 40 (modified 11mo ago (vulture sweet spot) / assigned: ontowhee)

### 12. [🟡 #25656] Recent Actions admin section contains link to edit form even when user does not have edit permission

- **Link**: https://code.djangoproject.com/ticket/25656
- **Component**: contrib.admin
- **Status**: assigned / AP Jama
- **Last modified**: 2025-07-20
- **Created**: 2015-10-31
- **Score**: 40 (modified 9mo ago (vulture sweet spot) / assigned: AP Jama)

### 13. [🟡 #25991] A new implementation for exclude() queries

- **Link**: https://code.djangoproject.com/ticket/25991
- **Component**: Database layer (models, ORM)
- **Status**: assigned / Eddy ADEGNANDJOU
- **Last modified**: 2025-05-19
- **Created**: 2015-12-28
- **Score**: 40 (modified 11mo ago (vulture sweet spot) / assigned: Eddy ADEGNANDJOU)

### 14. [🟡 #26619] BaseCache incr method will reset the timeout

- **Link**: https://code.djangoproject.com/ticket/26619
- **Component**: Core (Cache system)
- **Status**: assigned / Simone Macri
- **Last modified**: 2025-09-19
- **Created**: 2016-05-16
- **Score**: 40 (modified 7mo ago (vulture sweet spot) / assigned: Simone Macri)

### 15. [🟡 #27775] Signed cookies does not support custom expiry

- **Link**: https://code.djangoproject.com/ticket/27775
- **Component**: contrib.sessions
- **Status**: assigned / Abe Hanoka
- **Last modified**: 2025-08-26
- **Created**: 2017-01-25
- **Score**: 40 (modified 8mo ago (vulture sweet spot) / assigned: Abe Hanoka)
