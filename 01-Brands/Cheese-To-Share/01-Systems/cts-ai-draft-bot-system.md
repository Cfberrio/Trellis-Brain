---
brain_note_id: "note:0fef3cd0-2109-45cd-a789-1ebc45e28f02"
canonical_key: "ghl-ai-draft-bot"
brand_id: "cheese_to_share"
---
# CTS AI Draft Bot System

## Canonical Statement

- **process**: The GHL AI Draft Bot (ghl-draft) polls unread SMS and email every 2 minutes to generate internal drafts for manual review, never sending directly to maintain the founder's personal touch.
- **rule**: The bot uses a 'warm-neighbor' voice: greeting by time of day, using 'Mr [Name]', expressing enthusiasm ('Yes! Of course!!'), and prioritizing appetite over logistics.
- **rule**: Catering policies for the bot: minimum 25 guests for per-guest services, 1 week standard notice, 50% deposit to confirm, and final quotes must be signed by Luis.
- **process**: The bot performs inbox classification before drafting: customers get drafts, while vendors, job applicants, and automated reports are flagged for human handling.

## Evidence Log

- 2026-10-17T22:42:20.613Z — `clickup_doc_page:8cqnrff-22017/8cqnrff-30257`
  - `e1` (source_body): bot que lee las conversaciones unread de GHL (SMS + email)... genera un borrador con la voz warm-neighbor del founder. Se postea como nota interna [AI DRAFT — copy/edit/send manually] — nunca envía directo.
  - `e2` (source_body): Voz warm-neighbor: saludo por hora + "Mr [Name]" (formalidad cálida), entusiasmo real ("Yes! Of course!!"), apetito primero y logística después ("made for sharing", "board", "gathering")
  - `e3` (source_body): policies canónicas: mínimo 25 guests en servicios per-guest, 1 semana de notice estándar / hasta 15 días para setups custom, 50% deposit para confirmar, balance 24h antes, quotes finales las da Luis.
  - `e4` (source_body): Clasificación de inbox ANTES de draftear... cliente → draft; vendor/ops → flag_human (relación humana); reportes automáticos → skip; compliance/payroll → flag_human confidencial; jobs → flag_human hacia hiring.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22017/8cqnrff-30257`
- Source hash: `638f38e7eaf83670e2bfbbb5b25fa2e3c9168475bf7b669b0f213323986bd988`
- Observed at: 2026-10-17T22:42:20.613Z
- Agent run: `4e95e8b1-e51d-4241-9426-206308b84115`
- Validation run: `e98d6bb5-97dd-408d-bdce-db25e4907de7`
