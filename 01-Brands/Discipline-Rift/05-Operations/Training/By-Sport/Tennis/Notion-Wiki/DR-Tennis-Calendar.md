---
brand: Discipline-Rift
area: training
sport: Tennis
note_type: reference
status: stale-source
canonical: true
used_for_ai: true
sensitivity: internal
source_type: notion_wiki
notion_db: DR TENNIS CALENDAR (1)
notion_data_source_id: 17304528-85a8-816a-b0a3-000bdea82878
notion_parent_db_id: d7a0a9e9-4ba4-49b8-b1a0-0cf65df45be1
season_coverage: 2024-25
last_updated: 2026-08-11
---

# DR Tennis Calendar

## Parent
- [[Notion-Wiki-Home]]

## What this is
Mirror of the **DR TENNIS CALENDAR** inline database inside the DR TENNIS Notion wiki — the season-scheduling layer that sits alongside the coaching curriculum. Pulled 2026-08-11 via the Notion API. All 180 rows retrieved, one row per practice day, no gaps.

Rows carry only a title and a date. The `Location` and `Coach` properties exist on the database but are **empty on every row** — there is no per-site or per-coach scheduling data in Notion. Rows have no page bodies.

Because every row is a day-label rather than a distinct entry, the 180 rows are collapsed below into contiguous blocks. Nothing is lost — the day pattern is Mon–Fri with no exceptions (36 of each weekday).

## Duplicate source resolved
Two calendar databases existed under DR TENNIS:

| Data source | Status |
|---|---|
| `DR TENNIS CALENDAR` (`11104528-85a8-818e-b958-000b4071b565`) | Archived / in trash as of 2026-08-11. Near-identical copy. Not mirrored. |
| `DR TENNIS CALENDAR (1)` (`17304528-85a8-816a-b0a3-000bdea82878`) | Live. This is the mirrored source. |

The live one is the copy with the `Coach` property, which the archived one lacks.

## 2024-25 season map

| Dates | Days | Block |
|---|---|---|
| 2024-09-09 | 1 | BAD WEATHER DAY |
| 2024-09-10 → 09-13 | 4 | START — FALL SEASON |
| 2024-09-16 → 09-25 | 8 | FALL SEASON |
| 2024-09-26 | 1 | HURRICANE DAY |
| 2024-09-27 → 10-11 | 11 | FALL SEASON |
| 2024-10-14 | 1 | HOLIDAY — NO PRACTICE |
| 2024-10-15 → 10-18 | 4 | FALL SEASON |
| 2024-10-21 → 10-25 | 5 | LAST WEEK — FALL SEASON |
| 2024-10-28 → 11-01 | 5 | FIRST WEEK — LATE FALL SEASON (only teams that finished the previous season) |
| 2024-11-04 → 11-22 | 15 | LATE FALL SEASON |
| 2024-11-25 → 11-29 | 5 | THANKSGIVING WEEK — NO PRACTICE |
| 2024-12-02 → 12-13 | 10 | LATE FALL SEASON |
| 2024-12-16 → 12-20 | 5 | MAKE UP WEEK — LATE FALL SEASON |
| 2024-12-23 → 2025-01-24 | 25 | CHRISTMAS BREAK — NO PRACTICE |
| 2025-01-27 → 01-31 | 5 | FIRST WEEK — LATE WINTER SEASON |
| 2025-02-03 → 03-07 | 25 | LATE WINTER SEASON |
| 2025-03-10 → 03-28 | 15 | SPRING BREAK — NO PRACTICE |
| 2025-03-31 → 04-04 | 5 | FIRST WEEK — SPRING SEASON |
| 2025-04-07 → 05-16 | 30 | SPRING SEASON |

## Structural read
Four selling seasons per year, not two:

1. **Fall** — early Sep to late Oct, ~7 weeks
2. **Late Fall** — late Oct to mid-Dec, ~7 weeks including a make-up week, gated to teams that finished Fall
3. **Late Winter** — late Jan to early Mar, ~6 weeks
4. **Spring** — late Mar to mid-May, ~7 weeks

Late Fall is the only season with an explicit continuity gate — it is a re-enrollment season for existing teams, not an acquisition season. That maps to the 6-week curriculum in [[6-Week-Season]] running roughly four times a year with a make-up week absorbing weather loss.

Weather is a budgeted cost, not an exception: two named loss days in Fall 2024 alone (BAD WEATHER DAY, HURRICANE DAY) plus a dedicated make-up week.

## Source issues
Defects in the Notion source, not the mirror. Fixing them means editing Notion.

1. **Calendar is a full year stale.** It ends 2025-05-16. There are no 2025-26 entries and none for 2026-27. Any coach opening this page today sees last year's schedule with no indication it has expired.
2. **Christmas break is mislabeled.** The block runs 2024-12-23 → 2025-01-24, five weeks, and covers all of January. Late Winter starts 01-27. Everything after the first week of January is off-season gap, not Christmas break.
3. **Spring break is three weeks** (2025-03-10 → 03-28). Same pattern — a real break plus off-season gap collapsed under one label.
4. **Location and Coach are empty on all 180 rows.** The properties are defined but unused, so the calendar cannot answer where or who — only when.
5. **Duplicate database.** The archived copy sat live alongside the real one until today.

## Next step
Decision needed from the curriculum owner: either populate the 2026-27 season dates in Notion and split the break labels from the off-season gaps, or retire the calendar page and point coaches at whatever tool actually holds the live schedule. Right now it reads authoritative and is wrong.
