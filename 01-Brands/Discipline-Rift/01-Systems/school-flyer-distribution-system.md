---
brain_note_id: "note:4eba2b9f-b1ec-4a10-951d-de80d22b86b6"
canonical_key: "school-flyer-distribution-system"
brand_id: "discipline_rift"
---
# School Flyer Distribution System

## Canonical Statement

- **process**: The admin dashboard allows sending school flyers to faculty in one click, automatically pre-selecting sports with open registrations.
- **rule**: Flyer email templates use dynamic variables ({school}, {sports}, {link}) and recipients are defaulted to the 'Flyers' role in the system.
- **rule**: To ensure email delivery and avoid server timeouts, flyer PDFs should be optimized to 1–2 MB rather than full print size (5–8 MB).
- **fact**: The system supports flyers for Volleyball, Tennis, Pickleball, and Flag Football; Soccer is currently a known gap.

## Evidence Log

- 2026-10-15T21:33:25.012Z — `clickup:86e3qxv75`
  - `e1` (source_child): /dashboard/flyers está en producción... el admin manda los flyers de una escuela a su faculty en 1 clic. Un solo correo lleva el PDF y el PNG de cada deporte marcado; vienen preseleccionados los que tienen inscripciones abiertas... rehacer los PDF de imprenta (5–8 MB) a 1–2 MB.

## Provenance

- Source: `clickup` `86e3qxv75`
- Source hash: `ff338e4f28132c152ada0de5a2c9c36a9ed274c44f588806e1070785fce82152`
- Observed at: 2026-10-15T21:33:25.012Z
- Agent run: `1f0e5816-3c0c-494c-835f-0a31414bd698`
- Validation run: `373f06ac-17f6-4a9b-9cf4-22b1600e9ee6`
