---
brain_note_id: "note:ed7cff6f-83af-4ad0-a16b-336194e2a6c0"
canonical_key: "sms-automation-agent-ghl-claude-code"
brand_id: "trellis_core"
---
# SMS Automation Agent - GHL and Claude Code

## Canonical Statement

- **process**: The SMS automation system uses a Supabase cron job running every two minutes to fetch unread messages from GoHighLevel.
- **decision**: The AI agent does not send messages directly; it creates a draft as an internal note for human review and approval.
- **rule**: If a human opens the chat before the agent processes the message, the agent will not generate a response.
- **fact**: The system operates at a cost of approximately $10-$15 per month while handling hundreds of messages daily.

## Evidence Log

- 2026-10-15T17:17:44.903Z — `clickup_doc_page:8cqnrff-14777/8cqnrff-21217`
  - `e1` (source_body): El SMS entra a GoHighLevel. Un cron en Supabase corre cada dos minutos. Agarra los mensajes sin leer. Consulta mi base de datos con el contexto de la marca. Y se lo manda a Claude Code. Pero acá está la clave. El agente no manda el mensaje. Te deja un draft como nota interna. Tú revisas. Tú mandas.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-14777/8cqnrff-21217`
- Source hash: `cdc4cfaf6776f9838db571968ec65058dda808d79ef3dd1185c00a9b1dc7022d`
- Observed at: 2026-10-15T17:17:44.903Z
- Agent run: `bff31b00-532d-4a90-8478-d067c0dddb2b`
- Validation run: `da6d6db2-8d0a-425a-815f-86f5a0846fc9`
