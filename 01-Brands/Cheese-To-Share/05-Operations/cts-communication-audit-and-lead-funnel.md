---
brain_note_id: "note:8d34cbaf-9b1f-441d-8522-3160e14ff5d1"
canonical_key: "communication-audit-lead-funnel"
brand_id: "cheese_to_share"
---
# CTS Communication Audit and Lead Funnel

## Canonical Statement

- **fact**: The primary brand email (cheesetosharenaturalfood@gmail.com) functions as an operations and vendor hub, not a direct customer channel; human customer inquiries via direct email are effectively zero.
- **fact**: Actual customer demand and catering inquiries enter exclusively through the Wix website forms ('Contact' and 'How can we help?'), which are often buried by automated platform reports and job applications.
- **process**: There is a critical failure in the catering lead follow-up process: high-value leads (including recurring B2B opportunities like Fooda and joinlolo) frequently receive no response, and premature invoicing without menu confirmation has led to customer confusion and cancellations.
- **rule**: To operationalize the inbox, the brand must separate employment applications from customer leads using Gmail filters and implement an auto-response for the contact form that includes the catering menu and a quote link.

## Evidence Log

- 2026-10-17T22:36:32.822Z — `clickup_doc_page:8cqnrff-21917/8cqnrff-30117`
  - `e1` (source_body): This inbox is an operations & vendor hub, not a customer channel. Direct customer email (catering inquiries, quote requests, menu questions) is effectively zero.
  - `e2` (source_body): El sitio web ES el canal de clientes. Todo inquiry real de consumidor entró por el form Wix, no por email directo.
  - `e3` (source_body): El form mezcla clientes con aplicantes de trabajo en el mismo inbox. Sin separación, los leads de catering se pierden entre CVs.
  - `e4` (source_body): El cuello de botella #1 de CTS no es generar demanda — es responderla. Los leads llegan por el form y mueren sin follow-up.
  - `e5` (source_body): Katie Reekie... Se envió factura antes de confirmar el pedido/menú. Cliente confundido, canceló. Falta un paso de cotización/confirmación antes de cobrar.
  - `e6` (source_body): Separar el form de empleo del de clientes — filtro Gmail: "Come Work With Us" → label "Hiring", archivar; Contact/How can we help → label "Leads-Clientes" destacado.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21917/8cqnrff-30117`
- Source hash: `6ad82931890e9b400f263b0f8a093d4394466b9929237c6e70ec6d3c4667630d`
- Observed at: 2026-10-17T22:36:32.822Z
- Agent run: `22308bca-e2c6-439d-88c4-a6f835cd55fe`
- Validation run: `5a084372-4685-4596-b407-e420d0e55443`
