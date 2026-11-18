---
brain_note_id: "note:5f9cd40d-0403-40b2-bef2-2d602b8ba26a"
canonical_key: "sacramental-process-rules"
brand_id: "st_joseph"
---
# Sacramental Process and System Rules

## Canonical Statement

- **process**: The sacramental process is now organized into a single 'Sacraments' group rather than OCIA. Staff must approve a candidate's file before a sacrament date is assigned. Dates are no longer assigned automatically.
- **rule**: Rites and scrutinies are only displayed for non-baptized candidates. Baptized Christians receiving sacraments do not participate in these rites.
- **rule**: Leaders have full read/write access to their assigned candidates' files, including marriage history and sacramental status. Every edit made by a leader is tracked with a timestamp in the profile's edit history.
- **rule**: Assigning sacrament dates is restricted to staff with specific permissions. Leaders can view dates but cannot modify them.

## Evidence Log

- 2026-11-18T04:30:02.325Z — `clickup:86e40cv5h`
  - `e1` (source_body): The software reproduces the problem today: It assigns a rite date to almost everyone automatically. It has no per-person record of verified facts.
  - `e2` (source_child): Get rid of the OCIA group. Make one group: everyone receiving sacraments. Inside that group, each profile shows which sacraments the person is receiving, has their file, is assigned to a small group, and is assigned to an initiation person.
  - `e3` (source_child): The app no longer gives anyone a date automatically. Only staff assign a date, when they approve a person's file. They now show only for people who are not baptized: Acceptance, Election, Scrutinies, Presentations, Ephphetha and the preparation rites.
  - `e4` (source_child): Leaders can see AND edit everything for their people: history, dates, marriage info, sacraments, all of it. Every leader edit needs a timestamp and goes into an edit history under each profile.
  - `e5` (source_child): Reviewing Ready files and assigning dates is a permission now. Admins always have it, for anyone else you tick it in People. Without it nobody can change a date from any screen.

## Provenance

- Source: `clickup` `86e40cv5h`
- Source hash: `0f307c05d96502296283ed3aaa4d82e5d149becf5dc24741d206e1e64c6d84a8`
- Observed at: 2026-11-18T04:30:02.325Z
- Agent run: `d6d50cc4-bb93-4e98-a389-4ceb5e9dd6f9`
- Validation run: `93eb847d-11d1-4e5b-83c1-657174d3e9ae`
