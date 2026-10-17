---
brain_note_id: "note:e670329a-8a04-4d2e-a787-5b63869caaa0"
canonical_key: "renewal-os-mvp-requirements"
brand_id: "trellis_core"
---
# RenewalOS MVP Technical and Functional Requirements

## Canonical Statement

- **decision**: The RenewalOS MVP development ecosystem is centralized through Trellis, utilizing Supabase and Logo for database management across multiple environments.
- **rule**: The system must extract specific data points from Evidence of Insurance (EOI) documents, including policy number, premium, dates, and payment type (Escrow, Partial, or Full).
- **preference**: For large property portfolios, user permissions should be manageable by category (e.g., by region like 'Winter Haven' or 'Florida') rather than individual property assignments to reduce administrative friction.
- **decision**: A feature will be implemented allowing holders to request that their brokers upload policies directly to the system.

## Evidence Log

- 2026-10-17T07:06:10.092Z — `clickup_doc_page:8cqnrff-19817/8cqnrff-26277`
  - `e1` (source_body): En base de datos utilizamos dos supabase y Logo... la compañía en Colombia es la compañía que tiene acceso... simplemente lo metemos todo a través de Trellis.
  - `e2` (source_body): que lea el payment type, que el sistema entienda que localice esa profesión, que pongan escrow y que si partial payment, escrow, partial payment... si full payment, que ponga full payment
  - `e3` (source_body): si tengo mil propiedades... casi que mejor le doy mi usuario a la manager en vez de que tal vez sea algo como por mira, quiero darle acceso a esta persona a todas las propiedades que estén, no sé, en Paul County.
  - `e4` (source_body): creamos una función para que holder le pida al provider que monte la póliza. Si por ejemplo yo agendé con, yo hice una póliza con Oriana el año pasado, yo puedo añadir ahí el nombre de Oriana y correo Oriana y eso le pide esa le manda un correo.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-19817/8cqnrff-26277`
- Source hash: `75c2634577a70bf9660ec181b16c7d1f5ad5eb35d04a5254e5c8d0dd846a95a9`
- Observed at: 2026-10-17T07:06:10.092Z
- Agent run: `19a1cb7f-aa77-4a07-a9fc-df231062996a`
- Validation run: `53dbdef3-6019-41cf-82db-7680324b9c08`
