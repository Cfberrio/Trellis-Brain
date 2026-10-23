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

- 2026-10-20T02:00:51.400Z — `clickup_doc_page:8cqnrff-25577/8cqnrff-39237#brand=orlando_event_venue` (validation `938adc0a-7b71-43fd-8bba-8b1ed3d6d033`)
  - `e1` (source_body): Se decidió no editar el listing viejo y, en su lugar, abrir un listing nuevo en la cuenta nueva.
- **decision**: For PeerSpace, the strategy is to avoid editing the existing listing and instead create a new listing under a new account.

- 2026-10-21T01:42:26.015Z — `clickup:86e3twwk8` (validation `aa6c4234-14d2-4d2d-b5bf-4969a5c593ac`)
  - `e1` (source_body): Decisión: estrategia multicanal, no migración total. ... Ejecutar el piloto multicanal de 60 días: mantener Peerspace, lanzar Giggster + Tagvenue + Eventective, reforzar Google Business Profile y la web propia, y medir reservas netas por origen.
- **decision**: OEV is adopting a multi-channel marketing strategy, maintaining Peerspace while expanding to Giggster and Tagvenue to increase lead volume, while keeping all bookings and payments within the existing CRM and booking systems.

- 2026-10-22T01:42:29.334Z — `clickup_doc_page:8cqnrff-4897/8cqnrff-2877` (validation `8519f3d0-d750-4efa-bcca-4eaaa67a66df`)
  - `e1` (source_body): Subject: Reservation Confirmation for Your Event... Important Notes: Setup and Breakdown Times... Alcohol Policy... Setup and Breakdown Responsibility... Prohibited Items... Production/AV Needs
- **fact**: OEV uses standardized email templates for reservation confirmation, pre-event reminders, and post-event follow-up, which include venue details, setup/breakdown policies, alcohol policies, and prohibited items.

- 2026-10-23T01:38:49.549Z — `clickup_doc_page:8cqnrff-5957/8cqnrff-3997` (validation `7446bc4d-561a-4f0b-abb6-c40f2b1b9f16`)
  - `e1` (source_body): ![](https://t9017418223.p.clickup-attachments.com/t9017418223/52e5eab5-d34f-464c-8e16-9c3de1de263b/image.png)

![](https://t9017418223.p.clickup-attachments.com/t9017418223/cd38be93-bdf0-4590-aa18-43d3153e5d64/oev-logo-icon.png)
- **fact**: The Orlando Event Venue brand utilizes a specific logo and icon set for its visual identity.

- 2026-10-23T17:54:41.487Z — `clickup_doc_page:8cqnrff-7037/8cqnrff-4737` (validation `0d5ae284-bbba-49dd-9f92-03878470a5b5`)
  - `e1` (source_body): Primary model (recommended focus: corporate + workshops)
We help corporate teams and local hosts run smooth, professional events via a flexible 90-guest venue + optional staffed AV/LED/streaming production, and we get paid via hourly/day venue rental + cleaning fee + add-on production packages.
- **fact**: The OEV business model is structured into a primary focus on corporate teams and workshops (venue rental + cleaning + production packages) and a secondary focus on social celebrations (venue rental + cleaning + setup/production add-ons).

## Provenance

- Source: `clickup` `86e3gv11u`
- Source hash: `ae8b61fa5b00c43978f97d6a8d7dea4fd76f893510d5848e48b76faf6bf4052a`
- Observed at: 2026-09-30T20:42:56.100Z
- Decision: `a8ddc09a-4f60-4459-89f7-73506d6faf61`
- Upstream agent run: `2955fa8d-21ac-4a6d-a61f-84540b9e761a`
- Validation run: `1e9dcee4-93d1-4b03-85d3-bc74575b6f37`
