---
brain_note_id: "note:a3cfa23f-2e19-4d6f-a2c7-4c9626d79b2c"
canonical_key: "ai-gmail-draft-agent"
brand_id: "discipline_rift"
---
# DR AI Gmail Draft Agent

## Canonical Statement

- **process**: The AI Gmail Draft Agent (info@disciplinerift.com) generates response drafts in Gmail threads within 1–2 minutes for human review; it is strictly prohibited from sending emails directly.
- **rule**: The agent classifies responders into three categories: Parents (warm/coach tone), Faculty/Schools (formal/institutional, high priority), and Coach/Staff (appreciative/precise).
- **rule**: The agent must flag for human review and not draft standard replies for: refunds, credits, complaints, injuries, emergencies, contracts, child conduct, coach issues, or legal matters.
- **fact**: The agent uses live program data (teams, schools, schedules, prices) and specific parent context (children, payments) to respond, defaulting to a follow-up promise if data is missing.

## Evidence Log

- 2026-10-18T04:46:55.917Z — `clickup_doc_page:8cqnrff-22157/8cqnrff-30497`
  - `e1` (source_body): Estado: EN PRODUCCIÓN desde 2026-07-03. Vivo 24/7 en la nube.
  - `e2` (source_body): NUNCA envía correos. Las herramientas de envío no existen en la lista de permisos del código. Humano siempre revisa y envía.
  - `e3` (source_body): El bot clasifica cada remitente y cambia el registro: Parent — tono simple, cálido... Faculty/escuelas — tono formal-institucional... Coach/staff — cálido, apreciativo
  - `e4` (source_body): flag_human — reembolsos/créditos, quejas, lesiones, emergencias, contratos, conducta de un niño, problemas con coaches, legal → borrador "⚠️ HUMAN REVIEW", no enviar tal cual
  - `e5` (source_body): Programas ACTIVOS en vivo (equipo, escuela, deporte, horarios, coach, precio) desde la base del sitio DR... Contexto del padre: sus hijos, equipos, horarios y pagos

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22157/8cqnrff-30497`
- Source hash: `42d0162b936f2db359fb040854e7da95866aaa2645c7ec096abc55764e3c0b4d`
- Observed at: 2026-10-18T04:46:55.917Z
- Agent run: `cc89889f-56e4-4d4a-909f-8970b125bad1`
- Validation run: `6e66c096-b48b-4f2d-8dbd-d266b35d3bfb`
