---
brain_note_id: "note:404a03e6-744c-4bdf-b345-3dbb91be86cd"
canonical_key: "registration-engine-specs"
brand_id: "st_joseph"
---
# Registration Engine Specifications (OCIA and Adult Formation)

## Canonical Statement

- **rule**: OCIA registration (Candidate Form v2) does not require church registration; groups are assigned based on form answers.
- **process**: Adult Formation uses a QR sign-in asking 'What describes you today?' (OCIA / parent / learning more) to sort participants.
- **rule**: Parents are marked as 'Required' when a child is in sacrament prep; child classes are stored as free text and not linked to Camino.
- **rule**: Late registrants after the cutoff are marked 'next cycle' and are not eligible for sacraments in the current cycle.
- **process**: New parish registrations trigger an email to the office; Camino CSV exports use neutral columns until a sample import file is provided.

## Evidence Log

- 2026-10-07T20:17:51.326Z — `clickup:86e3etj6r`
  - `e1` (source_body): OCIA form without a church-registration requirement: Candidate Form v2... Groups are assigned from the answers.
  - `e2` (source_body): Adult Formation form with role: the website says "Adults do not need to register"; the QR sign-in asks "What describes you today?" (OCIA / parent / learning more) and sorts people.
  - `e3` (source_body): Parent ↔ child link: children and guardians are stored and parents are "Required" when a child is in sacrament prep; the child's class is free text, not linked to Camino
  - `e4` (source_body): Registration cutoff → late registrants marked "next cycle" (not sacrament-eligible this cycle)
  - `e5` (source_body): Parish membership data for Wendy (Camino): an email to the office is queued per new parish registration; Camino CSV exports use neutral columns until we get a sample Camino import file

## Provenance

- Source: `clickup` `86e3etj6r`
- Source hash: `649addcbe4b0994ba7497a7ce1c35690daaef7fbef6faa3af5d55a8e59a6c804`
- Observed at: 2026-10-07T20:17:51.326Z
- Agent run: `7d11cddf-98e7-44f6-8e6d-3931d7366a88`
- Validation run: `3003ad9f-1fc2-4a0e-b1b8-6fa951a504a3`
