---
brain_note_id: "note:af61afe3-2507-46a8-9b0e-1937d20a9924"
canonical_key: "platform-architecture-and-dashboard-roles"
brand_id: "st_joseph"
---
# Platform Architecture and Dashboard Roles

## Canonical Statement

- **definition**: The platform uses a three-tier dashboard hierarchy: Admin (staff/parish office), Leaders (Catechists and Leaders), and St. Joseph Adults (adult learners).
- **rule**: The dashboard for adult learners must be called 'St. Joseph Adults' (or 'Adults' for short); the term 'Catechumens' is prohibited in the UI.
- **rule**: Role Hierarchy: Admin manages Catechists; Catechists manage Leaders. Luis Torres is the default supervisor for all Catechists.
- **process**: Learning content is organized into monthly modules. Catechists can view both past and future content, while adult learners only see content for dates that have passed or modules specifically assigned to them.
- **rule**: One person can hold multiple roles (e.g., a Catechist who is also an adult learner) using a single login to switch between dashboards.

## Evidence Log

- 2026-10-07T15:08:05.361Z — `clickup:86e3k18rn`
  - `e1` (source_body): Hierarchy: Admin → Catechists → Leaders. Admin manages catechists... Do not use the word "Catechumens" anywhere in the UI. The dashboard is called St. Joseph Adults... One person, many roles... One login, and the person switches between the dashboards.
  - `e2` (source_child): Content (past / future)... Catechist also gets Leaders (tasks and messages to their leaders) and People (creates access for their own leaders).

## Provenance

- Source: `clickup` `86e3k18rn`
- Source hash: `746fd5e74f377354df063e1de339945552b5cd9b0d396df67a1f48c9deea1143`
- Observed at: 2026-10-07T15:08:05.361Z
- Agent run: `79d6c32f-6088-4aad-83bb-ebcb9c249c4b`
- Validation run: `2457640d-a6e7-4d38-a80a-171a69a3c174`
