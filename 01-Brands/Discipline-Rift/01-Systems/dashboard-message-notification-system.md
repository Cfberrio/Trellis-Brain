---
brain_note_id: "note:2e1007d8-b32b-4b35-9dd6-96fc3c5e42a0"
canonical_key: "dashboard-message-notifications"
brand_id: "discipline_rift"
---
# Dashboard Message Notification System

## Canonical Statement

- **rule**: Unread dashboard messages trigger a maximum of two notification emails: Email 1 immediately (next hourly run) and Email 2 six business hours later if still unread.
- **rule**: Notification business hours are 7:00 AM – 9:00 PM Orlando time; messages are not sent at night and the 6-hour reminder window pauses outside these hours.
- **rule**: A safety cap of 2 emails per person per rolling 24 hours is enforced; notifications are only sent for teams with 'ongoing' or 'closed' status.
- **process**: Notifications are triggered by Supabase edge functions and pg_cron, with GHL workflows ('DR | Webhook - Parent New Messages' and 'DR | Webhook - Coach New Messages') handling the email rendering.

## Evidence Log

- 2026-10-17T18:39:36.647Z — `clickup_doc_page:8cqnrff-21297/8cqnrff-36917`
  - `e1` (source_body): Emails a parent or a coach when they have unread messages in the Discipline Rift dashboard. ... Maximum two emails per cycle. ... Business hours = 7:00 AM – 9:00 PM Orlando. ... Safety cap: 2 emails per person per rolling 24 h. ... Only teams with status ongoing or closed.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21297/8cqnrff-36917`
- Source hash: `0dc492c01fdeecd73572b0e303b448b1f4c9c0333a9c118e2cd7786a9c786077`
- Observed at: 2026-10-17T18:39:36.647Z
- Agent run: `13057c85-095a-44a6-834d-5da409cf6206`
- Validation run: `3026c459-6578-4b20-b8a7-3ad126272e32`
