---
brain_note_id: "note:75059c27-b5cf-4756-895d-6d2b271492aa"
canonical_key: "drf-lead-funnel-automation"
brand_id: "discipline_rift"
---
# DRF Lead Funnel Automation Rules

## Canonical Statement

- **rule**: Franchisee lead communications must only be sent between 9:00 AM and 6:00 PM local time (America/New_York).
- **process**: If a franchisee lead triggers an automation after 6:00 PM, the first touch must be scheduled for 10:00 AM the following day.
- **process**: The franchisee application reminder sequence consists of 3 SMS (Immediate, Day 2 at 10:30 AM, Day 3 at 4:30 PM) and 5 Emails (Immediate, +2 hours, Day 2 at 9:15 AM, Day 3 at 1:00 PM, Day 6 at 11:00 AM).
- **fact**: The initial franchisee lead magnet form captures first name, email, phone number, and sport experience (sport name and years).

## Evidence Log

- 2026-10-14T22:02:20.918Z — `clickup_doc_page:8cqnrff-12617/8cqnrff-13257`
  - `e1` (source_body): Only send between 9:00 AM–6:00 PM local time (America/New_York). If the lead comes in after 6:00 PM, schedule the “next touch” for 10:00 AM next day.
  - `e2` (source_body): Keep SMS to 3 total... Keep email at 5 total... SMS #1 — Immediate... SMS #2 — Next day... at 10:30 AM... SMS #3 — Day 3... at 4:30 PM... Email #1 — Immediate... Email #2 — Same day (2 hours later)... Email #3 — Next day at 9:15 AM... Email #4 — Day 3 at 1:00 PM... Email #5 — Day 6 at 11:00 AM.
  - `e3` (source_body): If trigger happens: 9:00 AM–6:00 PM: run the schedule as-is. 6:01 PM–8:59 AM: treat the “start time” as 10:00 AM next day, then run the schedule.
  - `e4` (source_body): Step 1 — Quick Info (Lead Magnet) 1. First name 2. Email 3. Phone number 4. Sport experience

## Provenance

- Source: `clickup_doc_page` `8cqnrff-12617/8cqnrff-13257`
- Source hash: `08ba254d5a233c43c7dc078ff45d48c06d11e7db758c341e5c092cc55163d6b0`
- Observed at: 2026-10-14T22:02:20.918Z
- Agent run: `34bd302c-a09d-41d8-9bf2-af38c6beb409`
- Validation run: `c79e3337-03a5-44bf-86a9-66d23d77b91c`
