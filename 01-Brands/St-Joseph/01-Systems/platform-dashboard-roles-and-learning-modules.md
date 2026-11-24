---
brain_note_id: "note:25205b80-e06b-406f-879a-f946a9bbf8f2"
canonical_key: "platform-dashboard-roles-learning"
brand_id: "st_joseph"
---
# Platform Dashboard Roles and Learning Modules

## Canonical Statement

- **rule**: The platform uses a three-tier dashboard hierarchy: Admin (staff/parish office), Leaders (Catechists and Leaders), and St. Joseph Adults (adult learners).
- **definition**: Naming conventions: Use 'St. Joseph Adults' (or 'Adults') instead of 'Catechumens'. The dashboard for Catechists and Leaders is titled 'Leaders'.
- **rule**: Hierarchy: Admin manages Catechists; Catechists manage Leaders. Luis Torres is the supervisor for all Catechists by default.
- **process**: Learning content is organized into monthly modules. Admin can assign specific modules to individuals to clear absences (pending confirmation of make-up logic).
- **rule**: Access Control: Catechists can see future content; Adults cannot. Leaders and Catechists are restricted from viewing sensitive Sacrament case notes and documents unless approved.

## Evidence Log

- 2026-10-06T01:38:56.524Z — `clickup:86e3k18rn`
  - `e1` (source_body): Hierarchy: Admin → Catechists → Leaders. Admin manages catechists... Luis Torres is the supervisor over all catechists for now. ... Do not use the word "Catechumens" anywhere in the UI. The dashboard is called St. Joseph Adults ("Adults" for short).
  - `e2` (source_child): Assign module: from an absence or from the person's record. Settings → Learning: make-up switch (does completing an assigned module clear the absence?). It is OFF until Luis confirms.

- 2026-11-24T23:05:29.039Z — `clickup:1dfqjx6vnc0` (validation `2ccb0caa-5be2-47d1-8066-374210d25905`)
  - `e1` (source_child): el 12 de noviembre definiste las reglas del camino de sacramentos (cinco estados, el líder lleva la ficha de cada persona y marca Ready, el staff revisa y asigna la fecha, los escrutinios solo para no bautizados). Eso se construyó y se publicó el 13.
- **fact**: The sacramental path logic (five states, leader-managed readiness, staff-approved dates, and scrutiny restrictions for non-baptized seekers) is built and ready for deployment in the platform.

- 2026-11-24T23:06:13.980Z — `clickup:1dfqjx6vxz3` (validation `0f905c57-fd86-4839-933c-f5ef3250ca23`)
  - `e1` (source_child): ya quedaron listos los accesos de los líderes. Cada uno entra en formation-foundations.lovable.app/leaders con su correo y solo ve su grupo y su gente.
  - `e2` (source_child): no hace falta un paso de aprobación para las faltas. Ya no existen ausencias justificadas o injustificadas. Si alguien avisa que va a faltar, no nos importa para el conteo; solo nos ayuda a saber mejor qué pasa con esa persona. La regla es una sola: si faltan, tienen que venir a las formation nights, y además deben seguir alimentando su formación con sus lecturas.
- **rule**: Absences do not require a formal approval process; they are tracked for informational purposes. If a seeker misses a session, they must attend formation nights and continue their readings.
- **fact**: Session content for the Leaders dashboard is derived from the PowerPoint presentations provided by the catechist.

- 2026-11-24T23:06:28.832Z — `clickup:1dfqjx6vxz2` (validation `f961f6f3-35d3-487e-9169-49268807ddb8`)
  - `e1` (source_child): Los 3 menores de College D (Emerson, Cadence y Suarmy) se quedan donde están. Los tres pueden recibir los sacramentos como adultos. No los saques ni los pases a Youth Faith Formation.
- **fact**: Minors under 18 in the OCIA program (specifically those in College D) are permitted to remain in their assigned groups and are eligible to receive sacraments as adults; they are not to be transferred to Youth Faith Formation.

## Provenance

- Source: `clickup` `86e3k18rn`
- Source hash: `d8e6bc071f439011e15c3b30b345b142aa7bb85351651d51697d0822f1514309`
- Observed at: 2026-10-06T01:38:56.524Z
- Agent run: `1b777c85-1703-44cf-ab59-397ce3cec808`
- Validation run: `70cf8704-8ca6-44f9-a8c7-e01b4c1255dc`
