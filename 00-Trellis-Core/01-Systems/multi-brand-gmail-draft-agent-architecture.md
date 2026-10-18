---
brain_note_id: "note:e8695c45-11a8-4b5a-a461-3908abbb872b"
canonical_key: "gmail-draft-agent-architecture"
brand_id: "trellis_core"
---
# Multi-Brand Gmail Draft Agent Architecture

## Canonical Statement

- **decision**: Trellis uses a multi-brand Gmail draft agent architecture where each brand (CTS, OEV, DR) has its own isolated Supabase edge function and Composio project to ensure data isolation and brand-specific logic.
- **rule**: The system is restricted to 'draft-only' via a code-level allowlist of tools (read thread, read message, create draft); the 'send' tool is explicitly excluded to ensure human review.
- **fact**: Claude Haiku 4.5 is used for draft generation due to cost-efficiency and sufficient quality (scores 0.85–0.95), with a mandatory human review flag for scores below 0.75.
- **process**: Security layers include HMAC-SHA256 signature verification for webhooks, anti-echo filters to prevent self-response, and deduplication using gmail_message_id.
- **rule**: When creating drafts via Composio, the email address must be passed in a pure format (no names) and a subject is mandatory even when responding in a thread.

## Evidence Log

- 2026-10-18T04:47:35.383Z — `clickup_doc_page:8cqnrff-22177/8cqnrff-30517`
  - `e1` (source_body): Tres edge functions, una por proyecto Lovable de marca (no una central). Cada función lee la base de datos de SU marca... Tres proyectos Composio (no uno). Restricción real: 1 URL de webhook por proyecto.
  - `e2` (source_body): Draft-only por allowlist de código (no por prompt). La función tiene una lista blanca de 3 herramientas: leer hilo, leer mensaje, crear borrador. Enviar NO está en la lista.
  - `e3` (source_body): Haiku 4.5 (no Opus). Para borradores que un humano revisa igual, la calidad de Haiku alcanza (scores reales 0.85–0.95) a ~1/5 del costo. Score gate 0.75 + flag_human para dinero/quejas/legal.
  - `e4` (source_body): HMAC-SHA256 en cada webhook... Filtros pre-modelo: no-reply/notificaciones, categorías promo/social, anti-echo (no se responde a sí mismo)... Dedup por gmail_message_id (UNIQUE en DB).
  - `e5` (source_body): Composio rechaza destinatario "Nombre <email>"; hay que pasar el email puro... el schema de Composio CAMBIÓ y ahora exige subject aun respondiendo en hilo.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22177/8cqnrff-30517`
- Source hash: `8a8f246907c49f29f3bd6c74212cd5e898f0201f9e7f3ebad7c985b5b9d5e0d1`
- Observed at: 2026-10-18T04:47:35.383Z
- Agent run: `93ae85b4-a817-4de0-a549-f3ee8eb46018`
- Validation run: `a757092f-9581-4c2a-9168-552aa03b9d80`
