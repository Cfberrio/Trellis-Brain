---
brain_note_id: "note:15082340-901a-4b80-899d-b2c4cdbca3e6"
canonical_key: "marketing-performance-analysis-july-2026"
brand_id: "orlando_event_venue"
---
# OEV Marketing Performance Analysis - July 2026

## Canonical Statement

- **fact**: The HOST100 discount popup was non-functional from May 29 to July 9, 2026, due to a production database migration error, resulting in zero lead captures via that channel during June.
- **fact**: Google Ads conversion tracking (purchase and booking_deposit_paid events) was missing from the site code during the mid-2026 Performance Max campaign, preventing algorithmic optimization.
- **fact**: Approximately 49% of leads in 2026 requested dates that were already reserved, indicating that date availability is a primary bottleneck and follow-up speed is a critical conversion factor.
- **fact**: Human intervention is the primary driver for conversion; 61% of 2026 web bookings used personalized discount codes created during direct conversations, while the automated drip sequence converts at ~6%.

## Evidence Log

- 2026-10-18T04:57:42.318Z — `clickup_doc_page:8cqnrff-22337/8cqnrff-31057`
  - `e1` (source_body): El popup de descuento estuvo 100% roto durante toda la campaña. Desde el 29 de mayo (rebrand a HOST100), cada persona que llenó el popup recibió "Something went wrong. Please try again." — el lead no se guardaba, no entraba a GHL
  - `e2` (source_body): Los dos eventos de conversión configurados en Google Ads (purchase y booking_deposit_paid) nunca existieron en el código del sitio. Google Ads no recibió ni una conversión real en todo el periodo.
  - `e3` (source_body): La disponibilidad de fechas es un cuello de botella real: de 149 leads de 2026 que indicaron fecha preferida, 73 (49%) querían una fecha que terminó reservada por otro cliente.
  - `e4` (source_body): El cierre real es humano: 35 de 57 reservas web de 2026 usaron cupón, casi todos códigos personalizados creados en conversación directa (BABY, MARI, SAVE100…). El drip automático del popup convierte ~6% solo.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22337/8cqnrff-31057`
- Source hash: `29f5d7af6d1abc30d8477b61a3bc189bb96b403e424c5dd636342cf09b01324b`
- Observed at: 2026-10-18T04:57:42.318Z
- Agent run: `e3289848-4325-4c23-9eba-01e958309b9f`
- Validation run: `41774296-6a42-43b7-a8ea-1e83ff3a3d61`
