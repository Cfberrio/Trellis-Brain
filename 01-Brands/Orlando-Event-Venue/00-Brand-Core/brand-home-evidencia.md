---
brain_note_id: "note:5098de88-0816-4dae-9c67-ed121dba09f4"
canonical_key: "00-brand-core-brand-home-evidencia"
brand_id: "orlando_event_venue"
---
# Brand Home — Evidencia

## Canonical Statement

- **process**: Rescheduling a booking in the OEV admin panel automatically updates GHL, regenerates the invoice with the new date, and recalculates the balance, lifecycle, and feedback triggers.
- **rule**: The reschedule process validates against past dates and blackout periods before moving booking blocks.

## Evidence Log

- 2026-09-30T20:42:56.100Z — `clickup:86e3gv11u`
  - `e1` (source_body): After the reschedule is successfully saved, the system also needs to resend the invoice reflecting the updated booking date. Ensure the invoice is regenerated or re-triggered with the correct new date and sent to the client.
  - `e2` (source_child): reprogramar ahora actualiza GHL, reconstruye cadena 30/7/1, balance, lifecycle y feedback, mueve bloques y valida fechas pasadas/blackouts.

- 2026-10-01T18:00:20.429Z — `clickup:86e3etjgz` (validation `7ad6444a-1b4b-4c43-a595-2686083b76a0`)
  - `e1` (source_body): Use both retreats as the first real run of the Events module... Men's Fraternity Retreat (Sept 26–27): registration list, payments, attendance... Women's Silent Retreat (Sat Oct 10, one day)... Reconcile with the Gift Central report
- **fact**: OEV is piloting an 'Events module' using retreats (Men's Fraternity and Women's Silent Retreat) to refine registration, payment, and attendance requirements.
- **fact**: Event registration and payment data are reconciled against the Gift Central report.

- 2026-10-03T20:22:55.240Z — `clickup_chat_thread:8cqnrff-2077/80170035656066` (validation `2cea19c3-d7dd-4214-86fe-b159e7888cf2`)
  - `e1` (source_body): También tenemos pendiente el tema de los ads de Google de OEV. Estan pausados actualmente
- **fact**: As of June 2026, Orlando Event Venue Google Ads are currently paused.

## Provenance

- Source: `clickup` `86e3gv11u`
- Source hash: `ae8b61fa5b00c43978f97d6a8d7dea4fd76f893510d5848e48b76faf6bf4052a`
- Observed at: 2026-09-30T20:42:56.100Z
- Decision: `a8ddc09a-4f60-4459-89f7-73506d6faf61`
- Upstream agent run: `2955fa8d-21ac-4a6d-a61f-84540b9e761a`
- Validation run: `1e9dcee4-93d1-4b03-85d3-bc74575b6f37`
