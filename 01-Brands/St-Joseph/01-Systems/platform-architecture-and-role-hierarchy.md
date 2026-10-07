---
brain_note_id: "note:a85cdbb8-5276-49b2-9638-17b1b033e54a"
canonical_key: "platform-architecture-roles"
brand_id: "st_joseph"
---
# Platform Architecture and Role Hierarchy

## Canonical Statement

- **rule**: The platform uses a three-tier dashboard hierarchy: Admin (staff/parish office), Leaders (Catechists and Leaders), and St. Joseph Adults (all adult learners).
- **rule**: Naming convention: The dashboard for adult learners is 'St. Joseph Adults' (or 'Adults'). The term 'Catechumens' must not be used in the UI.
- **process**: Hierarchy and Supervision: Admin manages Catechists; Catechists manage their assigned Leaders. Luis Torres is the default supervisor for all Catechists.
- **rule**: Content Visibility: Catechists can see both past and future content; adult learners only see past/current content. Leaders see 'new content' as assigned.
- **process**: Learning Module: Content is organized by month (e.g., Module 1 = October). Admin can assign specific modules to individuals to clear absences or for self-paced learning.

## Evidence Log

- 2026-10-07T15:19:38.504Z — `clickup:86e3k18rn`
  - `e1` (source_body): Hierarchy: Admin → Catechists → Leaders. Admin manages catechists (and can manage leaders directly if needed). Catechists manage their leaders. Luis Torres is the supervisor over all catechists for now.
  - `e2` (source_body): Do not use the word "Catechumens" anywhere in the UI. The dashboard is called St. Joseph Adults ("Adults" for short).
  - `e3` (source_body): Supervisor is a field on the person, not hardcoded. Default catechist supervisor = Luis Torres. Admin can reassign.
  - `e4` (source_body): Content, split into Past content and Future content (this is the key differentiator: catechists can see what's coming, not just what happened)
  - `e5` (source_body): Future content visibility: catechists see it, adults don't.
  - `e6` (source_body): Content is organized into modules, one per month: Module 1 = everything covered in October... Admin can assign a specific module to a specific person. Main use: someone missed a date, admin assigns them that module.

## Provenance

- Source: `clickup` `86e3k18rn`
- Source hash: `b33c9a58a9c7b13e1861464f134aaf608772ff35e7b0decf2e16be0354de883e`
- Observed at: 2026-10-07T15:19:38.504Z
- Agent run: `f757e829-915d-45d9-998b-ea78903a72d5`
- Validation run: `704d2612-97b4-46b6-9679-99c720e959d9`
