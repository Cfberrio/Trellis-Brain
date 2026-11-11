---
brain_note_id: "note:7de2f45d-a0ea-42d4-baae-ebd955606664"
canonical_key: "session-attendance-qr-pdf-generator"
brand_id: "st_joseph"
---
# System Feature: Session Attendance QR PDF Generator

## Canonical Statement

- **process**: The St. Joseph platform includes a 'Download PDF' feature within the 'Show QR' interface for sessions. This generates a single-page, portrait-oriented attendance check-in sheet using the session's specific data (program, date, time, room, topic, and QR code). The feature supports both English and Spanish, ensures layout integrity for long text, and does not trigger attendance check-ins upon download.

## Evidence Log

- 2026-11-11T20:24:52.423Z — `clickup:86e3zwmjy`
  - `e1` (source_body): Add a Download PDF option under the existing Show QR option in Schedule > Sessions, allowing staff to download and print an attendance check-in sheet for the exact session and date selected.
  - `e2` (source_child): the check-in sheet PDF is built... Where: Schedule > Sessions > Show QR. There is a new Download PDF button right under the code... Everything comes from that session's own data... Downloading changes nothing: no check-in is made and attendance stays as it is.

## Provenance

- Source: `clickup` `86e3zwmjy`
- Source hash: `1d728281c8fc5d3dfea93f9780d635f06f59066d55a1565befb7cbb3e24a044c`
- Observed at: 2026-11-11T20:24:52.423Z
- Agent run: `b282d4cf-91fd-4078-a789-21a6e015dbb7`
- Validation run: `477599ac-b48c-429f-81f0-4892e1f57273`
