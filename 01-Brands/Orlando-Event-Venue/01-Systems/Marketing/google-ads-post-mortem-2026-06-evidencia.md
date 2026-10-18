---
brain_note_id: "note:61cef04a-e715-42cc-a4a5-f51dd9234b61"
canonical_key: "01-systems-marketing-google-ads-post-mortem-2026-06-evidencia"
brand_id: "orlando_event_venue"
---
# Google Ads Post Mortem 2026 06 — Evidencia

## Canonical Statement

- **rule**: Before running Google Ads, the purchase event must be deployed and verified in GA4 DebugView, marked as a key event, and stripe.com added to unwanted referrals.
- **process**: Capture UTM parameters and gclid for all leads and reservations to enable attribution analysis.
- **rule**: Mandatory 'cancellation reason' field must be required when a reservation is cancelled to improve funnel analysis.
- **decision**: Use Search with exact keywords for low-volume campaigns (<15-30 conversions/month); transition to PMax only once conversion history is established.
- **rule**: All campaign leads in GHL must be tagged with a specific outcome (e.g., no response, date occupied, price, closed) for accurate reporting.

## Evidence Log

- 2026-10-18T05:00:31.174Z — `clickup_doc_page:8cqnrff-22337/8cqnrff-31157`
  - `e1` (source_body): Deploy del evento purchase (código listo, falta push)... GA4: marcar purchase como key event... GA4: stripe.com en unwanted referrals
  - `e2` (source_body): Capturar UTM + gclid en leads y reservas... Campo motivo de cancelación obligatorio al cancelar una reserva... Disciplina en GHL: todo lead de campaña se marca con resultado
  - `e3` (source_body): PMax sin conversiones = tirar presupuesto... considerar arrancar con Search + keywords exactas (más control) y dejar PMax cuando haya ≥15–30 conversiones/mes

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22337/8cqnrff-31157`
- Source hash: `797c54d7ce6eb7054b19b4091c62d0bb5a5a2ff4d2ee6cab378b43c73757bbf9`
- Observed at: 2026-10-18T05:00:31.174Z
- Decision: `3310037b-0c89-451d-a89e-93b5bc8411f9`
- Upstream agent run: `6ab1bcc8-20ca-433b-b800-94497457356b`
- Validation run: `e744c5cc-17a1-495a-8f18-7d9fa4f2d6a2`
