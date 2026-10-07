---
brain_note_id: "note:4fa69d5d-0b84-46ca-885e-9e1f0a30a12a"
canonical_key: "st-joseph-connect-data-architecture"
brand_id: "st_joseph"
---
# St-Joseph-Connect Data Architecture

## Canonical Statement

- **fact**: The st.-joseph-connect platform uses a Supabase-based schema including entities for people, children, guardians, programs, terms, sessions, rooms, registrations, attendance, and sacrament profiles.
- **rule**: Access control is managed via Row-Level Security (RLS) with roles including admin, staff, data manager, catechist, and volunteer, segmented by functional area.
- **fact**: The system supports bilingual (EN/ES) participant pages, while staff screens remain English-only.
- **fact**: Data architecture for families links children to multiple guardians directly; there is no separate household record.

## Evidence Log

- 2026-10-07T15:20:45.427Z — `clickup:86e3etj5v`
  - `e1` (source_body): Core schema in the st.-joseph-connect repo (supabase/migrations). Verified against the code Oct 2. Core entities built: people, children + guardians, programs (with formation years and groups), terms, sessions, rooms, room bookings, registrations, form definitions, attendance...
  - `e2` (source_body): Roles & permissions: admin, staff, data manager, catechist, volunteer + access by area (adults receiving sacraments, AFF, youth, children, events, everything) Row-level security on every table, audit log
  - `e3` (source_body): EN/ES: participant pages are bilingual; staff screens are English only
  - `e4` (source_body): Households with two parents: children link to several guardians, but there is no household record

## Provenance

- Source: `clickup` `86e3etj5v`
- Source hash: `89f63d33bef8be2071bf9e3adb3bf596ade395d1c8eb05b9566f476275f271ba`
- Observed at: 2026-10-07T15:20:45.427Z
- Agent run: `4ce329ca-2283-4966-9d6f-52f4d9a8e027`
- Validation run: `f00423e5-e9ca-4927-8c8e-45c52ec85e6a`
