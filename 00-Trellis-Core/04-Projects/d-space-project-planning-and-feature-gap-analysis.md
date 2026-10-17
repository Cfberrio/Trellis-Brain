---
brain_note_id: "note:1a0929e1-2ef2-4cac-b93f-51cab881d3af"
canonical_key: "d-space-project-planning"
brand_id: "trellis_core"
---
# D-Space Project Planning and Feature Gap Analysis

## Canonical Statement

- **decision**: Prioritize P0 features for D'Space: Stripe webhook for deposits, admin UI button for balance payment links, cleaning reports (checklist/photos), and guest post-event reports.
- **rule**: D'Space guest capacity is capped at 100 in the frontend; bookings exceeding this must be redirected to a tour.
- **rule**: The approval SLA for bookings is set to 24 hours and must be visible on the booking page and home.
- **fact**: D'Space backend uses a time-based state machine (WF1), balance reminders (WF2), GHL sync, and a two-axis model (event/payment) supporting multi-space operations.
- **decision**: Service-tier (Self-Serve/Attended) is removed from the UX; the frontend will send 'self_serve' as a default value while keeping the DB column intact.

## Evidence Log

- 2026-10-17T18:49:43.142Z — `clickup_doc_page:8cqnrff-21457/8cqnrff-29177`
  - `e1` (source_body): P0 — Cerrar el loop antes de operar de verdad... 1. Deposit Stripe webhook (#1)... 2. Botón de link de balance en UI admin (#2)... 3. Cleaning report (#5)... 4. Guest post-event report (#6).
  - `e2` (source_body): Service-tier eliminado (Self-Serve/Attended) del UX... Cap 100 invitados en /book (front-end): bloquea >100, redirige a tour... approvalSlaHours=24 — SLA de confirmación visible en /book y home.
  - `e3` (source_body): D'Space ya es más fuerte que OEV en el backend: máquina de estados por tiempo (WF1), recordatorios de balance (WF2), sync a GHL, webhook de Stripe para balance + Connect transfer, modelo de dos ejes (event/payment), guard multi-espacio (EXCLUDE), payroll completo.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21457/8cqnrff-29177`
- Source hash: `6907dd2e3869d3baea02b74d5bf6d834f397caa990dddc1810d6b7b0af588961`
- Observed at: 2026-10-17T18:49:43.142Z
- Agent run: `a0dcc8d2-7bff-44e1-a186-212010ce8910`
- Validation run: `d30e6f85-c905-4d40-a57b-f928a3782b4c`
