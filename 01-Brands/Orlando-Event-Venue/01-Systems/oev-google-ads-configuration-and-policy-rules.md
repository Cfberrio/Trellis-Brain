---
brain_note_id: "note:874b3d8d-f707-4a23-9953-d7fd27d92a19"
canonical_key: "google-ads-config-rules"
brand_id: "orlando_event_venue"
---
# OEV Google Ads Configuration and Policy Rules

## Canonical Statement

- **decision**: Google Ads PMax signals should include in-market segments and competitor website browsing data ('people who browse types of websites').
- **rule**: In Google Ads conversion tracking, the 'purchase' event from GA4 must be set as Primary, while 'booking_deposit_paid' must be set as Secondary to avoid double counting.
- **process**: If images are flagged for religious content, request a manual review as it is a false positive; the business is not prohibited by policy. Alternatively, replace the flagged image.

## Evidence Log

- 2026-10-18T04:59:56.482Z — `clickup_doc_page:8cqnrff-22337/8cqnrff-31137`
  - `e1` (source_body): Signals de la PMax: Asset groups → Signals → añadir in-market segments y sitios web de 1–2 competidores ("people who browse types of websites").
  - `e2` (source_body): Pedir que verifiquen: import del key event purchase de GA4 → Ads, y que booking_deposit_paid quede como Secondary (dos Primary en el mismo goal = doble conteo).
  - `e3` (source_body): Asset group pausado por imágenes religiosas: despausar; si el sistema vuelve a flaggear, el rep abre caso de revisión manual — las políticas no prohíben el negocio, es falso positivo del filtro automático.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22337/8cqnrff-31137`
- Source hash: `d25fc7a2624207f8d3e427d20c0b3852773bf2d50d7dd72c3b68ead2944029c2`
- Observed at: 2026-10-18T04:59:56.482Z
- Agent run: `0c59fd6b-02bf-4d14-a4b3-27344c49a846`
- Validation run: `a1c85ca9-4916-4e5a-96c3-26498fe8c4f9`
