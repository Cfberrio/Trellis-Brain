---
brain_note_id: "note:8d7d0a09-0fa1-4a06-a42d-d1dc367d23e8"
canonical_key: "access-control-rules"
brand_id: "orlando_event_venue"
---
# OEV Access Control and Content Rules

## Canonical Statement

- **rule**: Guest access to the venue access code page (/accesscode) is time-gated: it opens 1 hour before the booking start time (or midnight of the event day if no start time) and closes exactly at the booking end time.
- **fact**: Access code page content, including entry instructions, lighting steps, and section titles, is dynamic and editable via the admin dashboard sidebar under 'Page Content'.
- **rule**: Recurring access codes for staff and specific tenants (DR TEAM, FCG, Global) are exempt from time-gating and remain active based on admin-defined expiration dates.

## Evidence Log

- 2026-10-01T03:15:39.591Z — `clickup:86e3bwhn4`
  - `e1` (source_child): Guest access to /accesscode is time-gated per booking... access opens 1 hour before start_time... and closes exactly at end_time... Recurring codes (DR TEAM, FCG, Global) are unaffected — separate mechanism (admin pause + expires_on date), stay always-on for staff/vendors.
  - `e2` (source_child): Access page content is now editable from admin. New sidebar item "Page Content" (below Pricing) → /admin/page-content.

## Provenance

- Source: `clickup` `86e3bwhn4`
- Source hash: `32c3dc14c7400729a5231d87c599f649ac1dc90cca510a5acff1c302d8ba73ec`
- Observed at: 2026-10-01T03:15:39.591Z
- Agent run: `2b2d7ff3-142b-4337-9a7b-9d28b2949dda`
- Validation run: `cc649a02-57d4-4c1f-9d58-dd978356dac3`
