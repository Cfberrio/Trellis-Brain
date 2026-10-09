---
brain_note_id: "note:13c00701-c131-4a29-a3cf-19a1173ec0a7"
canonical_key: "oev-workflow-statuses"
brand_id: "orlando_event_venue"
---
# OEV Workflow Statuses

## Canonical Statement

- **process**: The OEV workflow follows a standard status sequence: Planificación (initial setup), Aprobado (reviewed/ready for execution), Realizado (event completion), and Post-Event (reports and closure).
- **rule**: Status changes in OEV can be manual or automatic (triggered by system rules like checklist completion) and determine available actions and required information for the next stage.
- **fact**: The 'Aprobado' status is the trigger for assigning staff and activating event-related automations such as email sequences.

## Evidence Log

- 2026-10-09T00:41:46.776Z — `clickup_doc_page:8cqnrff-10537/8cqnrff-9137`
  - `e1` (source_body): Un booking inicia en "Planificación", pasa a "Aprobado" cuando está listo, luego a "Realizado" tras el evento, y finalmente a "Post-Event" para cierre y reportes.
  - `e2` (source_body): El cambio de estatus puede ser manual (por el usuario/admin) o automático (por reglas del sistema, como completar un checklist). El estatus determina qué acciones están disponibles.
  - `e3` (source_body): Aprobado... Acción: Permite pasar a la ejecución, asignar staff o activar automatizaciones.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-10537/8cqnrff-9137`
- Source hash: `3ad3e6f0417a1fa4a47ba07038953abbfc6d1d33fe67b43126af97982d3a73ec`
- Observed at: 2026-10-09T00:41:46.776Z
- Agent run: `7c344d96-ab26-4c7e-9099-32f7a68d7748`
- Validation run: `a547fb0a-bdfb-4566-a8b0-197df236ef71`
