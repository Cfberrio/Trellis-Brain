---
brain_note_id: "note:fd1ec5f2-c88a-4675-ae1c-e9e779c1fd88"
canonical_key: "dr-roas-attribution-mechanism"
brand_id: "discipline_rift"
---
# DR ROAS Attribution Mechanism

## Canonical Statement

- **process**: Discipline Rift uses a deterministic attribution system where the ad set that paid for the click is credited with the sale. The system tracks visitors via UTM tags and fbclid, stores them in a tracking_visitor table, and links them to a parent account upon email verification. The final attribution is determined by the last paid click, and conversions are reported to Meta via both Pixel and CAPI using a shared event_id for deduplication.

## Evidence Log

- 2026-10-20T18:12:05.452Z — `clickup_doc_page:8cqnrff-23377/8cqnrff-35377`
  - `e1` (source_body): El anuncio que pagó el click se lleva la venta. No la escuela que eligió el padre. No el deporte. El click. Todo el sistema existe para responder una sola pregunta: cuando entra un pago, ¿qué anuncio trajo a esa persona?

## Provenance

- Source: `clickup_doc_page` `8cqnrff-23377/8cqnrff-35377`
- Source hash: `2b3c78418ab7dbae6f1b2de4f17295debfd1d68b742ce27bd668e1241d7f268a`
- Observed at: 2026-10-20T18:12:05.452Z
- Agent run: `63877122-abaa-4f6b-9f74-2e96f2151c0c`
- Validation run: `d67ea9ef-881f-44aa-b4a0-a0fa2a129efe`
