---
brain_note_id: "note:4ca67289-3e41-4c22-a29a-d6ab8e0b3898"
canonical_key: "communication-system-specs"
brand_id: "st_joseph"
---
# Communication System Specifications and Outbox Process

## Canonical Statement

- **process**: Email communication uses an Outbox system where messages are queued and must be manually sent by a staff member; automated scheduling is not yet implemented.
- **fact**: The system uses Luis's St. Joseph account for sending emails until an Adult Formation address is established.
- **fact**: SMS functionality is limited to opening the device's native messaging app; there is no integrated SMS service provider.
- **process**: Follow-up sequences and session reminders (available in English and Spanish) are managed manually via templates and a 'Follow-ups' list that tracks the last message date.
- **fact**: Weekly summary reports are available on-screen with Print/CSV options but are not automatically emailed.

## Evidence Log

- 2026-10-07T15:20:12.030Z — `clickup:86e3etjea`
  - `e1` (source_body): Email goes through an Outbox: messages are queued and a staff member presses Send. Nothing is scheduled yet.
  - `e2` (source_body): Sending account: Luis's St. Joseph account for now; move to the Adult Formation address when it exists.
  - `e3` (source_body): SMS only opens the phone's messaging app (no SMS service)
  - `e4` (source_body): Follow-ups suggests who to contact and shows "last messaged"; no automatic sequences... Session reminders (EN/ES): template exists, picks each person's language; sent by hand
  - `e5` (source_body): Weekly summary report: on screen with print/CSV; not emailed

## Provenance

- Source: `clickup` `86e3etjea`
- Source hash: `cbf484965ca00c5905f3f7081a26296d94e6a0a0d0aa24719de6fa5b54738f16`
- Observed at: 2026-10-07T15:20:12.030Z
- Agent run: `5546a2b8-b017-4390-9d9b-5b72a26930e2`
- Validation run: `3aac6e6f-f911-483c-9bb9-5ee641dbd71b`
