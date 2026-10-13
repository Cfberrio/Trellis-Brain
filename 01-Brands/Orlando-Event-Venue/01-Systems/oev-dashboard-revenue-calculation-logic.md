---
brain_note_id: "note:25593ed7-8c75-43bb-9c6e-2cf5f8364108"
canonical_key: "oev-dashboard-revenue-logic"
brand_id: "orlando_event_venue"
---
# OEV Dashboard Revenue Calculation Logic

## Canonical Statement

- **process**: The revenue reporting function get_daily_generated_revenue uses the America/New_York timezone to ensure bookings made in the evening (e.g., after 8:00 PM EST) are attributed to the correct calendar day rather than the following day.
- **fact**: A previous reporting error caused bookings made late in the evening to appear on the next day's dashboard due to UTC offset; this was corrected by forcing the New York timezone in the calculation logic.

## Evidence Log

- 2026-10-13T20:51:09.580Z — `clickup:86dzqqd3v`
  - `e1` (source_child): Timezone corregido — La función get_daily_generated_revenue ahora usa America/New_York en lugar de UTC. El booking de Arlene Lorenzo (creado Feb 9 a las 8:05 PM EST) ahora aparecerá correctamente en Feb 9.
  - `e2` (source_child): ya hice la correcion de la zona horaria
  - `e3` (source_child): Es decir como el booking se hizo a las 8 y pico de la noche lo tomo para el otro dia pero si se esta calculando bien el total y todo sirve

## Provenance

- Source: `clickup` `86dzqqd3v`
- Source hash: `e0cdbe1c6cb4beafd4c759b1ffaaad71142633ffac10dbd634ee51e0120e1ee1`
- Observed at: 2026-10-13T20:51:09.580Z
- Agent run: `d68249b9-5473-4a4c-9da0-7c53b0302255`
- Validation run: `cd180f46-89f8-43b6-af1c-6a458a69eec7`
