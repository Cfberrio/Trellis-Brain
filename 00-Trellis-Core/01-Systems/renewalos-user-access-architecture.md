---
brain_note_id: "note:e793b9d2-32ad-4401-9e0d-340230d0da3b"
canonical_key: "renewal-os-user-access-architecture"
brand_id: "trellis_core"
---
# RenewalOS User Access Architecture

## Canonical Statement

- **decision**: The user access architecture is based on three levels: the specific App used (Owner, Broker, or Internal Console), the Company level (access to all properties), and the Property level (access to a single unit).
- **definition**: Standard roles include: Owner (full control), Co-owner (full control), Manager (management without invitation rights), Viewer/CPA (read-only), Broker (limited access for quoting), and Company Admin (manages all properties in a company).
- **rule**: Security rules: Invitation links expire in 14 days. A property must always have at least one owner. Broker access is automatically revoked when a quote is closed unless they win the bid.
- **proposal**: Future architecture goals include access by zone (grouping properties by city/state/tag), chain delegation (managers inviting others with equal/lesser power), and custom per-person permissions.

## Evidence Log

- 2026-10-17T07:07:00.459Z — `clickup_doc_page:8cqnrff-19877/8cqnrff-26417`
  - `e1` (source_body): 1) ¿A qué edificio entra? → la App que usa. 2) ¿Qué piso (empresa) abre? → acceso a una empresa completa. 3) ¿Qué oficina (casa) abre? → acceso a una sola propiedad
  - `e2` (source_body): Dueño: Todo sobre sus propiedades... Manager: Gestiona las propiedades... pero no puede invitar gente nueva. Viewer / CPA: Solo mira. No toca nada.
  - `e3` (source_body): El enlace vence a los 14 días por seguridad... una propiedad siempre debe tener al menos un dueño... Broker temporal: cuando se cierra, se le quita el acceso automáticamente.
  - `e4` (source_body): Qué PROPONEMOS agregar (a futuro): Acceso por zona... Delegación en cadena... Permisos a medida.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-19877/8cqnrff-26417`
- Source hash: `14e8819c237a8984278b79b9ff66a0c7f0dba9f53256102c01884aa37facf0ec`
- Observed at: 2026-10-17T07:07:00.459Z
- Agent run: `09a52916-48b5-46bd-bfd7-0989ca2abb34`
- Validation run: `92932b94-95e2-4697-862a-002d5f43b1ec`
