---
brand: Discipline-Rift
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift commits 2026-08-10 → 2026-08-14 (team status refactor) + docs/dr-season-schedule-standard.md"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - platform
  - data-model
---

# Team Status and Season Model

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|DR Platform Home]]

## Related
- [[01-Brands/Discipline-Rift/05-Operations/SOPs/Season-Schedule-Load-SOP|Season Schedule Load SOP]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Waitlist-System|Waitlist System]]
- [[01-Brands/Discipline-Rift/01-Systems/DR-Shared-Entities-and-Integrations|DR Shared Entities and Integrations]]

## One status field, no booleans
August 2026 retired `is_ongoing` and `is_active`. **`team.status` is the only source of truth.** Two overlapping booleans plus a status field made "can a parent register for this team" unanswerable without reading code, and the three sources disagreed in production.

`ongoing` is now a real status value, and **Season** is an explicit field on the team form.

## What each surface shows
| Surface | Rule |
|---|---|
| Public register / team picker | Only `open` teams |
| Register page | Also surfaces `ongoing` teams (a season already in progress can still accept a late join) |
| Coach dashboard | Only seasons that have actually started |
| Admin | Everything, with the status visible and editable |

Status hierarchy and season ordering are applied consistently, with a default season so admin screens do not open on an arbitrary one.

## Season as a first-class concept
Teams repeat across seasons with the same roster of schools. The season blocks are **FALL / WINTER / SPRING / LATE SPRING**. "Clone Season" copies an entire season — teams plus sessions — into a new one with bulk date adjustment, which is the mechanism that makes a four-season year operable by one person.

## Loading a new season
The yearly DR SEASON SCHEDULE spreadsheet is the source. The full procedure, including the non-obvious parts, is in [[01-Brands/Discipline-Rift/05-Operations/SOPs/Season-Schedule-Load-SOP|Season Schedule Load SOP]]. Two facts worth surfacing here because they shape the data model:

- **Sport is encoded as the fill colour of the school cell**, not as text. A plain-text export silently loses the sport.
- Team attributes (name, price, capacity) are **copied from the existing Fall teams**, not re-derived per season, because the roster is stable and the exceptions are hand-maintained.

## Known exceptions (as of 2026-07-16)
- Sculptor Charter: `DEVELOPMENTAL PROGRAM (1st-5th)` $129 Friday; `15U TEAM (7th-8th)` $169 Thursday.
- Orangewood Christian: `TENNIS ORANGEWOOD` $149, capacity 12, Wednesday, private calendar. **No Winter** — private school, Fall and Spring only.
- `VOLLEYBALL WINDERMERE` capacity **24**, not the default 20.
- `FLAG FOOTBALL PINECREST AVALON` is one team with **two weekly sessions** (Tue + Thu).
- Default otherwise: price $129, capacity 20, `is_active true`, name `<SPORT> <SCHOOL>` uppercase.

## Deliberate exclusions
**The First Academy** (Thursday tennis, Friday pickleball) and **The Christ School** (Friday tennis) appear on the schedule every season but were **never entered in Fall**, and are kept out to stay consistent. Decision 2026-07-16, confirmed by Domis. Archived Fall pickleball teams (Orangewood, Pinecrest Avalon) are `status='archived'` and not replicated.

This is a registration-exclusion decision with revenue impact, not a data-entry detail. Revisit it deliberately, not accidentally.
