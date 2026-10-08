---
brain_note_id: "note:a8c81332-e281-45ee-be04-39cb631715a1"
canonical_key: "events-module-import-reconciliation"
brand_id: "st_joseph"
---
# Events Module: Data Import and Reconciliation Process

## Canonical Statement

- **rule**: During event data imports, duplicates are merged where the latest response takes precedence, though alternative spellings are noted.
- **process**: Imported registrations are set to 'To reconcile' status by default, which suppresses reminder emails until a payment is matched via reports (e.g., Gift Central).
- **rule**: Shared emails are permitted in the system, and existing users are reused during imports. Emergency contacts, home parish, and allergy information are maintained specifically on each registration record.
- **decision**: For the Men's Emmaus Retreat, walkers and servers are kept as distinct groups within the system data.

## Evidence Log

- 2026-10-07T20:16:13.161Z — `clickup:86e3etjgz`
  - `e1` (source_body): Import rules: duplicates merged (latest response wins, other spellings noted), shared emails allowed, people already in the app reused, emergency contacts / home parish / allergies kept on each registration
  - `e2` (source_body): Imported as "To reconcile" (no reminder emails until a payment is matched). Reconcile with the Gift Central report
  - `e3` (source_body): Men's Emmaus Retreat (Oct 9–11, $150): 33 walkers + 48 servers imported, walkers and servers kept apart

## Provenance

- Source: `clickup` `86e3etjgz`
- Source hash: `3c520b4ca00613f59cbd982da57a261fb4d808b1d67102d4e4507d2cc1574fae`
- Observed at: 2026-10-07T20:16:13.161Z
- Agent run: `1d6273f9-eb8e-4979-9a56-ecf672ed2ee1`
- Validation run: `6455c491-37e5-4d78-8e9f-4de1e4bcd72e`
