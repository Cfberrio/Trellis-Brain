---
brain_note_id: "note:a237a282-a574-4682-a604-5b55de112ff1"
canonical_key: "dr-coach-app-standard"
brand_id: "discipline_rift"
---
# DR Coach App and Coach Hub Standard

## Canonical Statement

- **decision**: Discipline Rift will replace Notion with a native 'Coach Hub' inside the DR Coach App to host all coaching curriculum and training materials.
- **rule**: The Coach Hub must support view tracking to monitor when coaches last reviewed the curriculum; a lack of review for 2+ weeks triggers a quality check.
- **process**: The Coach Hub hierarchy will mirror Notion's structure (Team Space > Pages > Sub-pages) and support direct inline editing and AI-assisted content updates via Claude.
- **fact**: The DR Coach App uses a single login (email + code) for both coaches and parents, with native iOS push notifications for inter-user messaging.

## Evidence Log

- 2026-10-01T22:09:44.458Z — `clickup:86e3dhu94`
  - `e1` (source_body): Build a Coach Hub section inside the DR Coach App that fully replaces Notion. All active coaches must have access. The goal is to eliminate the Notion subscription and bring all curriculum/training content into our own platform.
  - `e2` (source_child): App nativa: bienvenida + un solo login (email + código) que manda a coach o a padre. ... Push de mensajes: coach escribe → le llega al padre; padre escribe → le llega a los coaches del equipo.

- 2026-10-09T00:29:54.014Z — `clickup:86e3dhu94` (validation `3f0dafae-17d6-4d79-8847-65a723abbba8`)
  - `e1` (source_child): App nativa: bienvenida + un solo login (email + código) que manda a coach o a padre. ... Push de mensajes: coach escribe → le llega al padre; padre escribe → le llega a los coaches del equipo. Tocar la notificación abre Messages. ... Arreglado: los badges de no leídos no se actualizaban en vivo.
- **decision**: The DR Coach App uses a single login (email + code) that routes users to either the coach or parent interface based on their profile.
- **fact**: Native iOS push notifications are functional: messages sent by coaches reach parents, and parent replies reach all coaches assigned to the team.
- **fact**: The app supports real-time unread message badges and notification-to-message deep linking on iOS.

## Provenance

- Source: `clickup` `86e3dhu94`
- Source hash: `e38eaa064d94e30fcb4ed1eb5f1a118fbc91dac02586e56985c74b0e701a1ce3`
- Observed at: 2026-10-01T22:09:44.458Z
- Agent run: `7446be28-1f1e-46e2-93d6-8280a1937ac1`
- Validation run: `15ce1207-e161-4a70-ae97-b806f3c0c39b`
