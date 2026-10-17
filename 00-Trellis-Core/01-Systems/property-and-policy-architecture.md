---
brain_note_id: "note:ae6d0e1c-96e7-458f-918a-095c1a8f8922"
canonical_key: "property-policy-architecture"
brand_id: "trellis_core"
---
# Property and Policy Architecture

## Canonical Statement

- **definition**: The system organizes data using a 'Property as a Folder' metaphor, where each property belongs to one company and contains all its associated policies.
- **fact**: Each policy entry stores the original PDF, AI-extracted key data (insurer, premium, dates), risk/opportunity analysis, and automated renewal reminders.
- **rule**: Automated renewal reminders are triggered at 90, 60, and 30 days before expiration; the 90-day alert initiates the quote request process.
- **process**: Policy lifecycle follows a path from Draft to Active, then to Expired (when replaced) or Cancelled.
- **proposal**: Future architecture plans include 'Master Policies' (one policy covering multiple properties), grouping properties by zone, and tracking payment types (full, partial, escrow).

## Evidence Log

- 2026-10-17T07:07:36.643Z — `clickup_doc_page:8cqnrff-19877/8cqnrff-26437`
  - `e1` (source_body): Pensá cada propiedad como una carpeta. Dentro de esa carpeta viven todas sus pólizas. ... Una propiedad pertenece a una empresa. Una póliza pertenece a una sola propiedad.
  - `e2` (source_body): Documento (PDF), Lectura automática (datos clave: aseguradora, número de póliza, precio, fechas), Análisis (riesgos, huecos de cobertura), Recordatorios.
  - `e3` (source_body): Avisos automáticos 90, 60 y 30 días antes de que venza. El aviso de 90 días dispara el pedido de cotizaciones.
  - `e4` (source_body): Borrador ──► Activa ──► Vencida (cuando llega una nueva que la reemplaza) │ └────────► Cancelada
  - `e5` (source_body): Master policy (una póliza para muchas casas). ... Agrupar propiedades por zona. ... Tipo de pago (completo, pago parcial, o a través del banco).

## Provenance

- Source: `clickup_doc_page` `8cqnrff-19877/8cqnrff-26437`
- Source hash: `1dd358844fd31bebe4a4e1e06279160e907c97ad66daf2d1908ba3f2a52b7bc3`
- Observed at: 2026-10-17T07:07:36.643Z
- Agent run: `2e659685-7eb2-458c-a688-bc69f757eccf`
- Validation run: `0d3d1273-f173-4840-95dd-0c78ce04a474`
