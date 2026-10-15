---
brain_note_id: "note:3765864b-ca8e-49db-aebe-30a90e8495c6"
canonical_key: "sms-automation-ghl-supabase-claude"
brand_id: "trellis_core"
---
# SMS Automation System (GHL, Supabase, Claude Code)

## Canonical Statement

- **process**: Automated SMS response system architecture: GoHighLevel receives messages, a Supabase cron job runs every two minutes to fetch unread messages, queries a context database, and sends the data to Claude Code for drafting.
- **decision**: The AI agent does not send SMS directly; it creates a draft as an internal note in GoHighLevel for human review and manual sending to maintain control.
- **fact**: The SMS automation system using Supabase and Claude Code operates at a cost of approximately $10-$15 USD per month.

## Evidence Log

- 2026-10-15T17:18:04.085Z — `clickup_doc_page:8cqnrff-14777/8cqnrff-21277`
  - `e1` (source_body): Llega el mensaje a GoHighLevel. Un cron en Supabase corre cada dos minutos. Agarra los mensajes sin leer. Consulta mi base de datos con el contexto de la empresa. Y se lo manda a Claude Code. Pero acá está la clave. El agente no manda el mensaje. Te deja un draft como nota interna.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-14777/8cqnrff-21277`
- Source hash: `dfb49ddf15edf947b390d12ca7b9a66de1f84664cfddb445799c0e379d68abc0`
- Observed at: 2026-10-15T17:18:04.085Z
- Agent run: `7b58e64e-381e-4b97-b72f-2b00bee6dbd0`
- Validation run: `351e0d11-7316-449b-97fb-f612a09a69a9`
