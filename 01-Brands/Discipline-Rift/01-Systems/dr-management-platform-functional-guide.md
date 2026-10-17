---
brain_note_id: "note:a6ad0e58-ca6a-4cdb-886b-9b3b5552a5dc"
canonical_key: "dr-management-platform-guide"
brand_id: "discipline_rift"
---
# DR Management Platform Functional Guide

## Canonical Statement

- **definition**: DisciplineRift is a real-time web-based sports management platform used by coaches to manage daily operations and by administrators to supervise the organization.
- **rule**: The platform supports three user types: Coaches (access assigned teams, take attendance, message parents via one-time email codes), Administrators (full visibility, global attendance, email campaigns, read-only message monitoring), and Parents (separate app, messages sync to coach chat).
- **process**: Attendance is recorded via a student list ordered by last name; changes are saved automatically to the database in real-time without a manual save button.
- **rule**: Messaging supports individual and broadcast (team-wide) formats, allowing attachments up to 25MB. Broadcasts create individual message copies for parents while maintaining a single batch view for the coach.
- **process**: The system generates automatic weekly attendance reports sent to coaches with a CC to administrators, including team summaries and a 'Top 5' list of absent students.
- **fact**: Data is stored in a Supabase cloud database with row-level security rules ensuring coaches only access their assigned data while admins have global access.

## Evidence Log

- 2026-10-17T18:47:40.130Z — `clickup_doc_page:8cqnrff-21377/8cqnrff-29077`
  - `e1` (source_body): DisciplineRift es una herramienta web de gestión deportiva. Sirve para que los entrenadores (coaches) de DisciplineRift manejen su día a día y para que los administradores supervisen toda la operación desde un solo lugar.
  - `e2` (source_body): Coach: Página principal, con un código de un solo uso que llega a su correo... Administrador: Dirección /admin, con correo y contraseña. Vista total... Padre de Familia: No tiene acceso a esta app. Usa una aplicación separada.
  - `e3` (source_body): Guardado automático: apenas se presiona un botón, el cambio se guarda solo en la base de datos. No hay que confirmar ni presionar "guardar".
  - `e4` (source_body): Se pueden enviar imágenes y videos de hasta 25 MB... Mensajes de Equipo (Broadcast): Permite enviar un solo mensaje a todos los padres de un equipo al mismo tiempo.
  - `e5` (source_body): Cuando el coach envía un mensaje a todos los padres de un equipo, el sistema en realidad crea una copia del mensaje para cada padre, pero les pone a todas una misma "etiqueta de lote".
  - `e6` (source_body): Cada semana, el sistema genera y envía solo un reporte de asistencia por correo... A cada coach con la información de sus equipos. Con copia (CC) a todos los administradores.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21377/8cqnrff-29077`
- Source hash: `80d2e50bb39786ede1ca9b4a1af6af241e9e91910c24225d58d4d015ddfd0b32`
- Observed at: 2026-10-17T18:47:40.130Z
- Agent run: `4d758c51-7c2d-4345-a533-045c331126f8`
- Validation run: `478fcc8d-7640-49e6-8a81-844931de9591`
