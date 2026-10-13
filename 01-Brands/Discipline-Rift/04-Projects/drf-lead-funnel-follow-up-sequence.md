---
brain_note_id: "note:43f178b8-e383-462b-9066-95531061995c"
canonical_key: "drf-lead-funnel-follow-up"
brand_id: "discipline_rift"
---
# DRF Lead Funnel Follow-up Sequence

## Canonical Statement

- **rule**: Lead follow-up communications (SMS/Email) must only be sent between 9:00 AM and 6:00 PM local time (America/New_York).
- **process**: The DR Franchisee SMS sequence consists of 3 touches: Immediate (link), Day 2 at 10:30 AM (nudge), and Day 3 at 4:30 PM (final reminder).
- **process**: The DR Franchisee email sequence consists of 5 touches: Immediate (link), 2 hours later (benefits), Day 2 at 9:15 AM (FAQs), Day 3 at 1:00 PM (social proof), and Day 6 at 11:00 AM (closing note).
- **rule**: If a lead trigger occurs between 6:01 PM and 8:59 AM, the automation start time must be deferred to 10:00 AM the following day.

## Evidence Log

- 2026-10-13T23:53:56.412Z — `clickup_doc_page:8cqnrff-11737/8cqnrff-11417`
  - `e1` (source_body): Only send between 9:00 AM–6:00 PM local time (America/New_York).
  - `e2` (source_body): SMS (3 total) ... SMS #1 — Immediate (0 minutes) ... SMS #2 — Next day (≈ 18–24 hours later) at 10:30 AM ... SMS #3 — Day 3 (≈ 48–72 hours later) at 4:30 PM
  - `e3` (source_body): Email (5 total) ... Email #1 — Immediate ... Email #2 — Same day (2 hours later) ... Email #3 — Next day at 9:15 AM ... Email #4 — Day 3 at 1:00 PM ... Email #5 — Day 6 at 11:00 AM
  - `e4` (source_body): If trigger happens: ... 6:01 PM–8:59 AM: treat the “start time” as 10:00 AM next day, then run the schedule.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-11737/8cqnrff-11417`
- Source hash: `890e6c99c80fc07269541a83a6d8a4b320e84177de0d0c6c58f8c6ab1de0eedb`
- Observed at: 2026-10-13T23:53:56.412Z
- Agent run: `7d10a638-6719-4635-b050-ab7f4890298f`
- Validation run: `d5e312e3-5062-4370-9213-603c67016121`
