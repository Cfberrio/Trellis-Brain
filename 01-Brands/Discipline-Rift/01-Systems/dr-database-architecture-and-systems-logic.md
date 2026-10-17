---
brain_note_id: "note:3426e6ca-58d8-4245-9ee6-1dfca112c2fe"
canonical_key: "dr-database-architecture"
brand_id: "discipline_rift"
---
# DR Database Architecture and Systems Logic

## Canonical Statement

- **fact**: The Discipline Rift database is organized into connected entities: Schools, Teams, Sessions, Registrations, Parents, Students, Payments, Attendance, and Coaches.
- **rule**: Access control is enforced at the database level (RLS); Parents access via OTP (One-Time Password) and only see their children's data; Coaches only see assigned teams.
- **process**: The system prevents overselling by reserving a spot for several minutes once a parent begins the payment process; it displays 'Full' once capacity is reached.
- **rule**: Attendance tracking is standardized into four states: present, absent, late, and justified.
- **fact**: Automated workflows include CRM syncing (GoHighLevel), abandoned cart reminders, AI-generated SMS drafts for unanswered messages, and practice reminders.

## Evidence Log

- 2026-10-17T15:54:14.865Z — `clickup_doc_page:8cqnrff-21297/8cqnrff-28957`
  - `e1` (source_body): Una Escuela tiene varios Equipos... Cada Equipo tiene Sesiones... Un Padre tiene uno o varios Estudiantes... Cada Estudiante se Inscribe a un equipo, y esa inscripción genera un Pago.
  - `e2` (source_body): Padres entran con su correo + un código de un solo uso (OTP)... Coaches igual, pero solo ven los equipos que tienen asignados... Es un candado real en la base de datos.
  - `e3` (source_body): Cuando un papá empieza a pagar, el sistema le aparta el cupo por unos minutos. Si el equipo está lleno, avisa “lleno” en vez de venderlo dos veces. Adiós sobreventa.
  - `e4` (source_body): La asistencia ahora distingue: presente, ausente, tarde, justificado (antes solo “sí/no”).
  - `e5` (source_body): Newsletter → CRM... Carrito abandonado... Borradores de SMS con IA... Recordatorios de práctica.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21297/8cqnrff-28957`
- Source hash: `919b693864d665c40c6c1e4b65d7d8163c9446da5f53ad5da9d8516f1ada8f3d`
- Observed at: 2026-10-17T15:54:14.865Z
- Agent run: `db761d2b-7d6d-4288-b2a0-c9e506a31b66`
- Validation run: `9dd3ef6c-e0a6-4f27-af0a-4a148003ee8d`
