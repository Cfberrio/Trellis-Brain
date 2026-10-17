---
brain_note_id: "note:743015f5-2737-4ee4-9d7e-e3092adbd738"
canonical_key: "ai-customer-service-grounding-rules"
brand_id: "discipline_rift"
---
# AI Customer Service Grounding Rules

## Canonical Statement

- **rule**: The DR AI bot uses PARENT_CONTEXT to provide personalized responses to parents by identifying their family via email or phone, allowing it to discuss specific student names, teams, schedules, and payment status.
- **rule**: AI responses regarding practice cancellations must use real database dates (canceled_practice_dates) and are prohibited from inventing reasons for the cancellation if the data is not provided.
- **rule**: AI responses regarding payments are limited to reporting 'paid' or 'pending' status; disputes and refunds must be flagged for human intervention.
- **fact**: The AI system (v3) now identifies specific coaches by session (e.g., 'Coach Avarey Johnson leads volleyball at Laureate Park') instead of providing generic responses.

## Evidence Log

- 2026-10-17T22:41:39.485Z — `clickup_doc_page:8cqnrff-21997/8cqnrff-30297`
  - `e1` (source_body): Nombre del coach por sesión — "¿Cómo se llama el coach?" → "Coach Avarey Johnson leads volleyball at Laureate Park." ... Prácticas canceladas (canceled_practice_dates) ... Regla anti-error: nunca inventa el motivo de la cancelación si la data no lo dice.
  - `e2` (source_body): PARENT_CONTEXT — bloque nuevo por contacto: al escribir un padre, la función busca su familia por email ... e le inyecta al modelo sus hijos, equipos, horarios con coach, estado de enrollment y último pago. ... Pagos: responde paid/pending desde la DB. Disputas y refunds siguen en flag_human.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21997/8cqnrff-30297`
- Source hash: `742d71f8b42dfd59893a79240b91dcfd4503219344c8c4443a13f5504ae535a5`
- Observed at: 2026-10-17T22:41:39.485Z
- Agent run: `4bb70b22-f386-408c-aff3-4627f0e83cdf`
- Validation run: `25f597f7-f829-4c64-8def-a79e65abcc05`
