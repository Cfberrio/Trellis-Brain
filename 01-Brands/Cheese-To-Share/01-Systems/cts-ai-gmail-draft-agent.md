---
brain_note_id: "note:65fe1f99-37bf-49ea-bba6-af63b4c580c4"
canonical_key: "cts-ai-gmail-draft-agent"
brand_id: "cheese_to_share"
---
# CTS AI Gmail Draft Agent

## Canonical Statement

- **fact**: The AI Gmail Draft Agent is in production as of 2026-07-03, operating 24/7 to process incoming emails to info@cheesetoshare.us.
- **rule**: The AI agent never sends emails; it only creates drafts in Gmail for human review and manual sending.
- **process**: The agent categorizes emails into 'draft' (standard response), 'skip' (spam/marketing), or 'flag_human' (refunds, complaints, or low confidence scores < 0.75).
- **rule**: The agent uses live menu data and customer order history to respond; if data is missing, it must state it will confirm rather than inventing information.
- **process**: Operational changes to the bot's behavior are managed via the 'brand_prompts' table in the Lovable project rather than code changes.

## Evidence Log

- 2026-10-18T04:45:09.601Z — `clickup_doc_page:8cqnrff-22117/8cqnrff-30457`
  - `e1` (source_body): Estado: EN PRODUCCIÓN desde 2026-07-03. Vivo 24/7 en la nube. ... Cuando un cliente escribe a info@cheesetoshare.us, en ~1–2 minutos aparece un borrador de respuesta
  - `e2` (source_body): NUNCA envía correos. Es técnicamente imposible: el código solo tiene permiso para leer hilos y crear borradores — las herramientas de envío no existen en su lista de permisos. Un humano siempre da el clic final.
  - `e3` (source_body): Claude (Haiku 4.5) elige una de tres: draft ... skip ... flag_human ... Además hay un umbral de confianza: si el modelo no está seguro (score < 0.75), el borrador se marca para revisión humana automáticamente.
  - `e4` (source_body): Menú en vivo ... Órdenes del remitente ... Regla anti-inventos: si un dato no está en la base, el borrador dice "Let me confirm that for you and get right back" — nunca adivina precios.
  - `e5` (source_body): No se toca código. El comportamiento vive en la tabla brand_prompts (proyecto Lovable de CTS, canal "gmail"). Se crea una versión v2 del prompt con la corrección y se activa

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22117/8cqnrff-30457`
- Source hash: `d169c737fdc1f7b025b865815994e86a6a3f272af52309191cc4bc6abad4fbe9`
- Observed at: 2026-10-18T04:45:09.601Z
- Agent run: `a2c74403-0ffc-4675-a9c1-36dd891360ff`
- Validation run: `327e9c3e-8c08-4b59-91e6-ea2bbd924b70`
