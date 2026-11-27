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

- 2026-11-24T23:07:10.917Z — `clickup_chat_thread:8cqnrff-2077/80170057809052` (validation `94a54f23-3461-433d-90fc-2c5f59727c53`)
  - `e1` (source_child): El acceso comenzará con los líderes de cada pilar o grupo... Se asignará a los asistentes sin grupo respetando los comentarios existentes, equilibrando los grupos y procurando no superar quince personas por grupo. Los menores de dieciocho no deben asignarse... Cada líder recibirá una contraseña inicial
- **rule**: Dashboard access for leaders is initialized via individual passwords; leaders are instructed to change these upon first login to verify their assigned groups.
- **rule**: Group assignment logic: Groups should not exceed 15 participants. Minors under 18 are not to be assigned to these groups.

- 2026-11-26T05:08:28.004Z — `clickup:1dfqjx6w547` (validation `4a29116c-09fd-4590-9ab4-9e484f9c6559`)
  - `e1` (source_child): En admin, Leaders, hay un botón Download data que baja un Excel con una pestaña de resumen y una por cada grupo... Los líderes ahora tienen un botón Not answering en My group... También agregué Edit contact en la ficha de OCIA candidate para que puedas cambiar nombre, teléfono y email.
- **process**: Admin dashboard includes a 'Download data' feature providing an Excel report with group summaries, individual sacramental status, attendance, and unresponsive flags.
- **process**: Leaders can mark participants as 'Not answering' in the dashboard, which flags the record in red for Admin review.
- **process**: Staff can edit contact information (name, phone, email) directly within the OCIA candidate profile.

- 2026-11-27T05:06:36.436Z — `clickup:1dfqjx6vxz3` (validation `8f2ef485-e6de-4dbb-bf13-3af44b77ed93`)
  - `e1` (source_child): Lideres coordinan la reunión, ellos la crean con fecha, lugar de reunion, contenido que compartir con el grupo y marcan quien esta ausente
  - `e2` (source_child): No dejalo y que ellos puedan modificar el schedule y content
  - `e3` (source_child): Yes, permitamos mensajeria
  - `e4` (source_child): Para sesiones de formacion (ingles y español) catequista, o cualquier persona como lider o admin tambien puede
- **rule**: Leaders manage their own group meetings, including setting date, time, location, and content. They have full visibility and edit access to their group's schedule and session materials.
- **rule**: Leaders have messaging capabilities within the dashboard to communicate with their group members via WhatsApp or email.
- **rule**: Session content (PowerPoint or other materials) for formation nights can be uploaded by catechists, leaders, or admins, and is accessible to all leaders for their respective sessions.

## Provenance

- Source: `clickup` `86e3k18rn`
- Source hash: `d8e6bc071f439011e15c3b30b345b142aa7bb85351651d51697d0822f1514309`
- Observed at: 2026-10-06T01:38:56.524Z
- Agent run: `1b777c85-1703-44cf-ab59-397ce3cec808`
- Validation run: `70cf8704-8ca6-44f9-a8c7-e01b4c1255dc`
