---
brain_note_id: "note:8f53bf7c-d79b-468a-889f-18c0aa8c6773"
canonical_key: "formation-system-implementation-decisions"
brand_id: "st_joseph"
---
# Formation System Implementation Decisions

## Canonical Statement

- **decision**: The formation system is owned by the parish; the nonprofit plan was dropped.
- **process**: Attendance check-in uses a QR code that rotates every 2 minutes to prevent fraud; geolocation is not used.
- **rule**: Attendance rules: summer sessions never count; a weekday class counts as the week's class; all parents are required/invited to attend, but sacrament-prep parents are strictly 'Required'.
- **fact**: Project phases: P1 Events & Retreats, P2 Adult Formation & OCIA, P3 Weekly Schedule & Check-In. Parish-wide sacramental records and certificates are moved to a Future phase.
- **decision**: Internal staff-facing labels use 'Sacraments', while public-facing pages retain 'OCIA'.

## Evidence Log

- 2026-10-07T20:15:20.640Z — `clickup:86e3j54f1`
  - `e1` (source_body): Owned by the parish. Proposal wording ("one system, owned by the parish") stays; nonprofit plan dropped from the records.
  - `e2` (source_body): No geolocation anywhere in the build... the QR was a fixed code per session; it now changes every 2 minutes (link must be opened within 2–4 min, then 30 minutes to finish the form).
  - `e3` (source_body): Parent + Module 3: summer never counts; weekday class = the week's class... all parents required and invited; sacrament-prep parents are "Required".
  - `e4` (source_body): Parent retitled "P1 Events & Retreats → P2 Adult Formation & OCIA → P3 Weekly Schedule & Check-In"; scope rewritten by phase.
  - `e5` (source_body): Parish-wide sacramental records and certificates = Future phase. Added back to the proposal's Future list.
  - `e6` (source_body): The Oct 2 review call (after this task was written) settled it: staff menu and page title say "Sacraments"; public pages keep "OCIA".

## Provenance

- Source: `clickup` `86e3j54f1`
- Source hash: `0d4b057bf6f9d26843e32dedb7a4e9b52ea6ea11f1f12d667a394e70c47b3243`
- Observed at: 2026-10-07T20:15:20.640Z
- Agent run: `122e0fe1-5896-4692-94c0-d5d24bd0bc2f`
- Validation run: `bce35182-c05a-4719-adae-33b621878545`
