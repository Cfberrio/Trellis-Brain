---
brain_note_id: "note:14cb35ff-60b3-4b19-9ffa-f7c0f198d674"
canonical_key: "virtual-tour-technical-spec"
brand_id: "orlando_event_venue"
---
# OEV 3D Virtual Tour Technical Specification

## Canonical Statement

- **rule**: The OEV 3D tour uses a custom Three.js (WebGL) viewer that projects photos onto a cylinder; the visible arc is determined by the aspect ratio (68° × width/height), capped between 66° and 104°.
- **rule**: Ideal photo capture for the tour is a 3:2 aspect ratio (e.g., 6000x4000) to maximize both visible arc (104°) and height. Published resolution must be ≤ 4096 px wide for mobile WebGL compatibility.
- **process**: Capture requirements: horizontal rectilinear panoramas (no fisheye), sRGB color space, HDR or balanced exposure, and camera height at ~1.5m in the center of the room.
- **process**: Development pipeline: Original photos from Google Drive are optimized (3:2 crop, ≤4096px, JPEG ~85%) and placed in 'src/assets/tour/' with specific filenames (entrance, lobby, lounge, etc.).

## Evidence Log

- 2026-10-18T16:06:22.730Z — `clickup_doc_page:8cqnrff-22497/8cqnrff-31417`
  - `e1` (source_body): El tour no usa fotos 360° esféricas: es un visor propio hecho con Three.js (WebGL) que curva cada foto sobre el interior de un cilindro... arco visible = 68° × (ancho ÷ alto), limitado entre 66° y 104°.
  - `e2` (source_body): Dev optimiza: recorte a 3:2, redimensionar a ≤4096 px de ancho, JPEG ~85%, sRGB. Archivos van a src/assets/tour/ con estos nombres: entrance.jpg, lobby.jpg...

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22497/8cqnrff-31417`
- Source hash: `dc50bc30fbdae17b2d2e428ebf92cc1fc90d72522e678de8e6d3cb49a89bb39c`
- Observed at: 2026-10-18T16:06:22.730Z
- Agent run: `2c9ffc25-427e-4a81-b288-5831e2de232e`
- Validation run: `7935dff2-3153-4135-ae09-5f67081fb60d`
