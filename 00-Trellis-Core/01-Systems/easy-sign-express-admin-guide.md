---
brain_note_id: "note:fc232bce-61c0-497c-a108-92779fda2278"
canonical_key: "easy-sign-express-admin-guide"
brand_id: "trellis_core"
---
# Easy Sign Express - Admin Guide

## Canonical Statement

- **rule**: The admin dashboard for Easy Sign Express uses email and password authentication on a dedicated route, unlike standard users who use Google login.
- **process**: Administrators can access the dashboard at https://easy-sign-express.lovable.app/auth/admin.
- **fact**: The admin dashboard provides an overview of platform metrics (users, document status, activity), user management (details, audit events, suspension/reactivation), and a global audit log.
- **rule**: Account suspension prevents users from using the app or sending requests; this action is reversible via the 'Reactivate' function.

## Evidence Log

- 2026-10-18T04:51:37.545Z — `clickup_doc_page:8cqnrff-22317/8cqnrff-30957`
  - `e1` (source_body): Los usuarios normales entran con Google; el admin usa email + contraseña en una ruta aparte (no depende de Google).
  - `e2` (source_body): Entra a: https://easy-sign-express.lovable.app/auth/admin
  - `e3` (source_body): Overview — métricas de toda la plataforma... Users — lista de todos los usuarios... Documents — todos los documentos... Audit log — registro de auditoría global.
  - `e4` (source_body): Al suspender un usuario: no puede usar la app (ve pantalla "Account suspended") ni enviar solicitudes. Reversible con Reactivar.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22317/8cqnrff-30957`
- Source hash: `8151b0e4a742e14ab65b1c18b876f4fc227b324ac3cd2f810b3a59ba4890ba20`
- Observed at: 2026-10-18T04:51:37.545Z
- Agent run: `5e5e2f45-25cc-4ead-8f05-1cd2c94333be`
- Validation run: `ff33251d-ec2b-4fb2-bcd9-53cd1f88b599`
