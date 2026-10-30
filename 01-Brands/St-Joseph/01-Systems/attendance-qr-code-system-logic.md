---
brain_note_id: "note:259549a5-802c-4d06-a4aa-99d44f778239"
canonical_key: "attendance-qr-code-logic"
brand_id: "st_joseph"
---
# Attendance QR Code System Logic

## Canonical Statement

- **process**: Attendance QR codes are now static for the duration of a session. Each session has a unique, non-rotating QR code that remains valid throughout the session day and the following day. The system prevents cross-session check-ins and allows for sharing via direct link or screenshot.

## Evidence Log

- 2026-10-30T18:42:00.060Z — `clickup:86e3xd8fn`
  - `e1` (source_body): The QR holds the session's own link (/checkin/<session code>). It works after any amount of time, from a screenshot, or on another phone. Each session keeps its own code. One session's code can't check anyone into a different session.

## Provenance

- Source: `clickup` `86e3xd8fn`
- Source hash: `1ef9fa18b700414cb8e6e6bb02814e56b8d94615291b994bb5a50a738cc39293`
- Observed at: 2026-10-30T18:42:00.060Z
- Agent run: `eeba6126-9e30-4b09-851b-b5feb8454870`
- Validation run: `541eb350-1a73-40f2-8a60-580c4f604e84`
