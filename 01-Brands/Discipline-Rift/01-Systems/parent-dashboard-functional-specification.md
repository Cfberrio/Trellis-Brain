---
brain_note_id: "note:4373dc75-b9a5-401f-9aa7-e3c513dc2dfc"
canonical_key: "parent-dashboard-spec"
brand_id: "discipline_rift"
---
# Parent Dashboard Functional Specification

## Canonical Statement

- **definition**: The Parent Dashboard is a mobile-first private control center for parents to manage schedules, skill progress, coach communication, and payment history for their children.
- **rule**: Access to the dashboard is passwordless, utilizing a one-time password (OTP) sent via email that expires after 10 minutes.
- **process**: Skill progression is tracked via a tiered system (Levels) where each skill is marked as Consistent (mastered), In Development, or Locked.
- **rule**: The dashboard uses a unique color-coding system per child to allow parents with multiple children to distinguish schedules and profiles at a glance.
- **process**: Communication is handled via real-time team-based chats between parents and coaches, supporting attachments up to 25MB and daily email reminders for unread messages.

## Evidence Log

- 2026-10-17T15:53:36.894Z — `clickup_doc_page:8cqnrff-21297/8cqnrff-28757`
  - `e1` (source_body): Es el centro de control privado para los padres. Desde un solo lugar pueden gestionar y seguir todo lo relacionado con la participación deportiva de sus hijos: horarios, progreso de habilidades, comunicación con entrenadores y pagos.
  - `e2` (source_body): El acceso es sin contraseña: el padre usa un código temporal que llega por correo (código de un solo uso, "OTP"). ... El código expira en 10 minutos.
  - `e3` (source_body): muestra el progreso deportivo de cada hijo mediante un sistema de niveles (tiers). ... Estado de cada habilidad: ✓ Consistente (ya la domina), ● En desarrollo (la trabaja ahora), 🔒 Bloqueada (de un nivel futuro).
  - `e4` (source_body): Un color único por hijo: el mismo color identifica a cada hijo en todas las secciones (avatar, tarjetas, calendario). Las familias con varios hijos los distinguen de un vistazo.
  - `e5` (source_body): Chat directo entre el padre y los entrenadores... Mensajes en tiempo real... Adjuntos: fotos y videos (hasta 25 MB). ... recibe, además, un correo recordatorio (máximo uno por conversación al día) si no respondió.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21297/8cqnrff-28757`
- Source hash: `00c633526554dbac4ba52c0142eae6fa375ec977e52ec9e025a4a2e1c2bb2c2f`
- Observed at: 2026-10-17T15:53:36.894Z
- Agent run: `9b5e036d-d79c-4c34-a899-80f688ecad9a`
- Validation run: `1d221353-b689-403e-8f9d-6321edc57b79`
