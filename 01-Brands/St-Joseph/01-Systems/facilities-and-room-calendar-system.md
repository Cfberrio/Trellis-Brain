---
brain_note_id: "note:27e10bc4-fc1e-4ea6-a456-834ce4d5ed08"
canonical_key: "facilities-room-calendar-system"
brand_id: "st_joseph"
---
# Facilities and Room Calendar System

## Canonical Statement

- **fact**: The Facilities & room calendar system is built and ready for demonstration as of Oct 2, covering rooms: Church, Social Hall, Hall BC, GH, IJ, K, P, Conference Room, and Annex.
- **rule**: Recurrence is modeled using Nth-week rules (e.g., 2nd Tuesday) rather than simple weekly swaps; Tuesday follows a 4-week cycle for Spanish formation, Men's Fraternity, Emmaus, and Holy Hour.
- **fact**: The system includes conflict detection for double-booking and noise rules (loud next to quiet), with space priority settings to determine which booking yields.
- **fact**: Calendar features include per-room/program ICS feeds and per-booking security/lock-up notes; email invites to leaders are not yet built.

## Evidence Log

- 2026-10-07T20:16:26.858Z — `clickup:86e3etjg6`
  - `e1` (source_body): Rooms as resources: Church, Social Hall, Hall BC, GH, IJ, K, P, Conference Room, Annex... It is already built (ready early) and can be shown to the parish whenever they want. Verified against the code Oct 2.
  - `e2` (source_body): Recurrence: weekly, Nth week of the month (e.g. 2nd Tuesday), last Friday. Tuesday is modeled as Nth-Tuesday rules, not a weekly swap. Johanna described a 4-week cycle that differs from the Sept 28 version.
  - `e3` (source_body): Conflict detection: double-booking plus noise rules (loud next to quiet). Space priority per ministry; conflicts show which booking should yield.
  - `e4` (source_body): Per-booking setup, lock-up owner, security notes. Calendar feeds (ICS) per room/program work; email invites to leaders are not built.

## Provenance

- Source: `clickup` `86e3etjg6`
- Source hash: `8dc379ff03e3b9da4f6c2e5c01ee701f8ca26f5d8c0d3eee10731cd4cc7e267d`
- Observed at: 2026-10-07T20:16:26.858Z
- Agent run: `aa40624c-9bdc-4e06-b8e9-b276df334204`
- Validation run: `b888e924-db52-4b7c-934e-97adcfb37d2d`
