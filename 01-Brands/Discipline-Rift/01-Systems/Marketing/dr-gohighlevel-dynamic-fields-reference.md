---
brain_note_id: "note:e476beb9-65d4-4a3f-9564-56ad6342bb8b"
canonical_key: "ghl-dynamic-fields-reference"
brand_id: "discipline_rift"
---
# DR GoHighLevel Dynamic Fields Reference

## Canonical Statement

- **fact**: Discipline Rift uses specific GoHighLevel dynamic fields for SMS and email marketing, including {{contact.season}}, {{contact.season_interest}}, {{contact.source_system}}, {{contact.student_levels}}, {{contact.student_names}}, and {{contact.team_names}}.
- **rule**: When using dynamic fields in marketing, distinguish between parent-level fields (safe for marketing) and school/POC-level fields to avoid blank rendering in parent emails.
- **rule**: Do not guess merge tag codes from field names; verify the unique key in GHL Settings > Custom Fields to ensure accuracy for fields like 'City_' or 'dr intended sport'.

## Evidence Log

- 2026-10-04T20:39:51.301Z — `clickup:86e3jtbne`
  - `e1` (source_body): Build one reference doc with every dynamic field (merge tag) available for Discipline Rift in GoHighLevel... Season {{contact.season}} confirmed... Student Names {{contact.student_names}} confirmed... Mark which fields are parent-level (safe for parent marketing emails) vs school/POC-level.

## Provenance

- Source: `clickup` `86e3jtbne`
- Source hash: `7ddda282e4e4d8ef7e149db23c323b72c1394dcf8f120362ae09b66062736b77`
- Observed at: 2026-10-04T20:39:51.301Z
- Agent run: `1e0fde44-615a-45fd-b125-54dd7beb2b9c`
- Validation run: `916a394a-0f06-4840-8661-7d338cf0dd4a`
