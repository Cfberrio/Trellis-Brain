---
brain_note_id: "note:250f274e-54ae-4e9b-a893-c61ae441d16e"
canonical_key: "oev-tour-process"
brand_id: "orlando_event_venue"
---
# OEV Tour Process

## Canonical Statement

- **process**: The OEV tour process is a guided walkthrough where guests call the venue manager upon arrival. It is distinct from the booking process and does not use reservation numbers or a Tour Page.
- **rule**: Tour communications (TC01, T01, T02, T03) are automated via GHL. T01 and T02 share a single SMS body to ensure consistency. T03 (post-tour follow-up) is sent only if no booking has been completed.
- **rule**: Appointment merge fields (e.g., {{appointment.start_time}}) must be used for date/time. Do not use separate date or time fields as they do not exist in GHL and will render blank.

## Evidence Log

- 2026-10-22T01:44:29.178Z — `clickup_doc_page:8cqnrff-4977/8cqnrff-11917`
  - `e1` (source_body): The tour is a guided walkthrough. The guest arrives at the venue and calls Luis at 407 974 5979. Luis lets them in, guides them through the space on a normal phone call... Tours do not have a reservation number and do not use a Tour Page.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-4977/8cqnrff-11917`
- Source hash: `d5e6470a3ce365ece755886eebc35573810e0a3339f1b93d0d58d4c26bbdb70d`
- Observed at: 2026-10-22T01:44:29.178Z
- Agent run: `2c80794a-7472-4d0a-a4ef-9e059ef31af2`
- Validation run: `bf6fca03-e98d-46af-a3b8-1622196cd8ae`
