---
brain_note_id: "note:019d65f9-5719-4352-aec5-ba7c0dbb32fb"
canonical_key: "oev-workflow-statuses"
brand_id: "orlando_event_venue"
---
# OEV Workflow Statuses and Force Sync Process

## Canonical Statement

- **definition**: Statuses in OEV represent stages in the workflow for bookings or tasks, indicating progress or required actions.
- **process**: Common OEV statuses include 'in_progress', 'post_event' (event finished, post-actions active), 'completed', and 'pending_report' (missing required guest report).
- **process**: The 'Force Sync' tool allows manual status updates to bypass blockers, such as marking a missing report as completed to move a booking from 'pending_report' to 'post_event'.
- **rule**: Staff must verify current status before manual actions and document any manual status changes to maintain traceability.

## Evidence Log

- 2026-10-09T00:42:27.878Z — `clickup_doc_page:8cqnrff-10577/8cqnrff-9177`
  - `e1` (source_body): Los estatus en OEV representan las diferentes etapas o situaciones en las que puede encontrarse un elemento (por ejemplo, un booking o tarea) dentro del flujo de trabajo.
  - `e2` (source_body): in_progress: El elemento está en proceso. post_event: El evento principal ha finalizado... completed: El proceso ha terminado satisfactoriamente. pending_report: Falta completar un reporte.
  - `e3` (source_body): Al usar el botón Force Sync, el sistema marca el reporte como completado y cambia el estatus a post_event, permitiendo continuar el proceso.
  - `e4` (source_body): Verifica siempre el estatus antes de realizar acciones manuales... Documenta cualquier cambio manual de estatus para mantener trazabilidad.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-10577/8cqnrff-9177`
- Source hash: `d2df8725ad9c03ccc8912899f418f14423cbd15bf93690ec4acca67dd0693a36`
- Observed at: 2026-10-09T00:42:27.878Z
- Agent run: `96e19846-d768-441d-9a1d-a139744b09f0`
- Validation run: `65ea924c-82c8-4d9c-a89d-bec46677833d`
