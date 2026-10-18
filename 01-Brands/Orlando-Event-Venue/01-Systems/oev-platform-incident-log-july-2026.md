---
brain_note_id: "note:0eecac3d-2329-477b-b0bc-3c5fbfa78cc7"
canonical_key: "oev-platform-incident-log-july-2026"
brand_id: "orlando_event_venue"
---
# OEV Platform Incident Log - July 2026

## Canonical Statement

- **fact**: A database migration failure on 2026-05-29 caused the discount popup (HOST100) to fail for 6 weeks because the 'event_type' column was missing in production.
- **fact**: The discount popup failure resulted in an estimated loss of 40-90 leads between May 29 and July 9, 2026, as contacts were not synced to GHL and coupon emails were not sent.
- **fact**: As of 2026-07-09, conversion tracking was found to be non-existent; the site only sent GA4 page views, lacking 'purchase' and 'booking_deposit_paid' events.
- **fact**: Stripe checkout was found to break attribution because 'stripe.com' was not included in the 'unwanted referrals' list in GA4.
- **decision**: The 'purchase' event was implemented on 2026-07-09, using the booking deposit value and reservation number as the transaction ID to prevent duplication.

## Evidence Log

- 2026-10-18T04:58:52.816Z — `clickup_doc_page:8cqnrff-22337/8cqnrff-31097`
  - `e1` (source_body): el 29 de mayo se deployó el rebrand del popup de descuento (SAVE100 → HOST100). El nuevo código guarda el campo event_type del lead, pero la migración de base de datos que agregaba esa columna nunca se aplicó en producción... todo envío del popup falló desde el 29 de mayo hasta el 9 de julio.
  - `e2` (source_body): El evento purchase no existía. El único tag en el sitio era el snippet base de GA4... booking_deposit_paid tampoco existe... Stripe rompe la atribución: el cliente sale a checkout.stripe.com a pagar y vuelve; sin stripe.com en 'unwanted referrals' de GA4, la conversión se atribuye a Stripe.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22337/8cqnrff-31097`
- Source hash: `3de14d751e7b883cb4abc205e8de19a33776aa4086e79a134d96b3e82b0301d2`
- Observed at: 2026-10-18T04:58:52.816Z
- Agent run: `7dd49c8c-69d3-4b27-98ca-572f0f6e9193`
- Validation run: `58db9576-e8a8-4a4b-b905-834e4ab00883`
