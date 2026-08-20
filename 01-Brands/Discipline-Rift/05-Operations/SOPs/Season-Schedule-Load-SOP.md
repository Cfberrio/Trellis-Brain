---
brand: Discipline-Rift
area: operations
subarea: sops
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/dr-season-schedule-standard.md (written 2026-07-16 loading Winter 2026 / Early Spring 2027 / Late Spring 2027 from '26-27 DR SEASON SCHEDULE.xlsx')"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - sop
  - operations
---

# Season Schedule Load SOP

## Parent
- [[01-Brands/Discipline-Rift/05-Operations/SOPs/SOPs-Home|DR SOPs Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Team-Status-and-Season-Model|Team Status and Season Model]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Admin-Dashboard|Admin Dashboard]]

## Purpose
Turn the yearly **DR SEASON SCHEDULE** spreadsheet into `team` + `session` rows in the database, without losing information the spreadsheet encodes non-textually.

## Trigger
A new season block needs to open for registration (FALL / WINTER / SPRING / LATE SPRING).

## Owner
Cristian, with school-list decisions confirmed by Domis.

## Source
`26-27 DR SEASON SCHEDULE.xlsx` in Google Drive, owned by the DR info inbox. One sheet per season block.

## Steps

### 1. Read the spreadsheet correctly
Layout per day: four columns `[arrival-time, school, date, blank]`. Monday occupies columns 1–4, Tuesday 5–8, Wednesday 9–12, Thursday 13–16, Friday 17–20. School name sits in column `4N-2`, arrival/practice time in `4N-3`, week date in `4N-1`.

### 2. Read sport from the CELL FILL COLOUR, not the text
This is the step that breaks every naive import. **A plain-text export loses the colour and therefore the sport.** Parse the `.xlsx` binary and read the cell fill.

| Fill (ARGB) | Sport |
|---|---|
| `FF6FA8DC` blue | flag_football |
| `FFB6D7A8` green | volleyball |
| `FFF9CB9C` orange | pickleball |
| `FFFFE599` yellow | tennis |

**Gotcha:** week-label header cells ("WEEK 3", "S2 WEEK 1", "THANKSGIVING BREAK") share the pickleball orange. Filter them out — a real team cell always has a time in its left neighbour.

### 3. Read the time convention
A cell reading `2:45 / 3:15-4:15` means **arrival 2:45 (discard)** and **practice 3:15–4:15**. Only the range goes to the database, as 24-hour `start_time` / `end_time`, e.g. `15:15-16:15`.

### 4. Copy team attributes, do not re-derive them
The roster is the same every season, so copy attributes from the existing **Fall** teams, which already carry the correct names, prices and caps.

- Default: price 129, capacity 20, sport per colour, `is_active true`.
- Name format: `<SPORT> <SCHOOL>` in uppercase, e.g. `VOLLEYBALL ATWATER BAY`.
- Exceptions are listed in [[01-Brands/Discipline-Rift/01-Systems/Platform/Team-Status-and-Season-Model|Team Status and Season Model]] and must be applied by hand.

### 5. Apply the exclusions
- **The First Academy** and **The Christ School** appear on the sheet every season but are **not** entered. Decision 2026-07-16.
- Archived Fall pickleball teams are not replicated.
- **Winter has no Orangewood** — private school, Fall and Spring only.

### 6. Verify before opening registration
- Team count per sport matches the sheet after filtering header cells.
- No team carries an arrival time as its start time.
- Statuses are correct so the register page shows exactly the intended teams.

## QA standard
A season is loaded correctly when a parent on the public register page sees the right teams, at the right times, at the right prices, and no excluded school appears.

## Completion definition
Season teams and sessions exist, statuses are set, and the exclusions above were re-confirmed rather than assumed.
