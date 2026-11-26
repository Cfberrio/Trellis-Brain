---
brain_note_id: "note:059c5fb1-0c64-4e81-afc7-afaa068542b6"
canonical_key: "dr-management-platform-spec"
brand_id: "discipline_rift"
---
# DR Management Platform Specification

## Canonical Statement

- **process**: The platform uses a real-time architecture where messages and attendance updates sync instantly via a live connection, with a 10-second polling fallback to ensure data consistency.
- **process**: Coaches access the dashboard via a passwordless 6-digit email code; administrators use email/password credentials restricted to an authorized list.
- **process**: The messaging system supports individual and broadcast messages with file attachments up to 25MB; read receipts are managed via a dedicated 'seen' registry.
- **process**: Administrators have a 'read-only' monitoring dashboard to view all coach-parent conversations in real-time, including attachments.
- **process**: Weekly attendance reports are automatically generated and emailed to coaches, with CCs to administrators, detailing session metrics and the top 5 absent students.

## Evidence Log

- 2026-10-17T15:53:04.666Z — `clickup_doc_page:8cqnrff-21297/8cqnrff-28737`
  - `e1` (source_body): DisciplineRift es una herramienta web de gestión deportiva. Sirve para que los entrenadores (coaches) de DisciplineRift manejen su día a día y para que los administradores supervisen toda la operación desde un solo lugar.
  - `e2` (source_body): Coach: Solo sus equipos asignados. Toma asistencia y se comunica con los padres... Administrador: Vista total: toda la asistencia de la organización... Padre de Familia: No tiene acceso a esta app. Usa una aplicación separada.
  - `e3` (source_body): El coach no usa contraseña. En su lugar, la app le envía un código de 6 dígitos a su correo... Login del Administrador — Correo y contraseña... Solo los correos en una lista autorizada pueden entrar.
  - `e4` (source_body): Guardado automático: apenas se presiona un botón, el cambio se guarda solo en la base de datos... El sistema calcula automáticamente las fechas individuales hacia adelante desde hoy.
  - `e5` (source_body): Se pueden enviar imágenes y videos de hasta 25 MB... La app consulta cada 10 segundos si hay mensajes nuevos sin leer... gracias al tiempo real, muchos mensajes llegan al instante.
  - `e6` (source_body): Cada semana, el sistema genera y envía solo un reporte de asistencia por correo... Top 5 ausentes: los 5 estudiantes con más faltas esa semana... Con copia (CC) a todos los administradores.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21297/8cqnrff-28737`
- Source hash: `42cf77660a8f4bcb98b5779a80532f7566e43c24523e9d883c5fbd1f211da116`
- Observed at: 2026-10-17T15:53:04.666Z
- Agent run: `f23da537-8c2c-44b6-ab0a-bd47e8815e1c`
- Validation run: `b1b36aa7-8f18-46b3-afbd-b4349c351c21`
