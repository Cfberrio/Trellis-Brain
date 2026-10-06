---
brain_note_id: "note:cccc8478-5507-4997-9891-8b356a8c1498"
canonical_key: "booking-verification-process"
brand_id: "orlando_event_venue"
---
# OEV Booking Verification Process

## Canonical Statement

- **process**: The OEV booking process requires a photo of the front of the guest's driver's license (camera or file upload) during the signature step.
- **rule**: Driver's license data is stored in a private bucket; files are automatically deleted 30 days after the event. Files without a completed reservation are deleted after 48 hours.
- **rule**: Access to driver's licenses is restricted to the admin role via a dedicated dashboard (/admin/driver-licenses) with links that expire in 10 minutes.
- **rule**: Security measures include edge function validation of file types and a rate limit of 8 upload attempts per hour per IP.

## Evidence Log

- 2026-09-24T18:25:10.363Z — `clickup:86e3dtdk7`
  - `e1` (source_child): Hecho y en producción — el booking pide foto del frente de la licencia (cámara o archivo) y el admin la ve en una sección nueva... Ve un aviso de que su información está segura y de que se borra 30 días después del evento... los archivos están en almacenamiento privado; solo el rol admin los ve

## Provenance

- Source: `clickup` `86e3dtdk7`
- Source hash: `c267345f64ef3a567b2003a9730c57ae6fcafe25e3883b1ae502fc89d003ad4f`
- Observed at: 2026-09-24T18:25:10.363Z
- Agent run: `c902db40-9667-4bc2-9f5e-3e1dc697c569`
- Validation run: `08bf1e31-b2a7-46cc-8345-60088ed96bb0`
