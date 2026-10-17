---
brain_note_id: "note:00b6e780-8205-46c1-af06-e3063b2aee7a"
canonical_key: "oev-ai-draft-bot-system"
brand_id: "orlando_event_venue"
---
# OEV AI Draft Bot System

## Canonical Statement

- **process**: The OEV AI Draft Bot polls unread GHL conversations every 2 minutes via a Supabase edge function to generate response drafts as internal notes; it never sends messages directly to clients.
- **rule**: Drafts are only posted if the model's confidence score is >= 0.75; scores below this threshold are flagged for human review and logged for calibration.
- **fact**: The bot uses live grounding data including current local time, a 90-day availability calendar (bookings, blocks, and 48h notice rules), and specific contact booking context.
- **rule**: The bot is prohibited from promising response times, handling day-of urgent requests, or sharing access codes unless the event is within 24 hours and codes are already in the thread.

## Evidence Log

- 2026-10-17T22:40:10.764Z — `clickup_doc_page:8cqnrff-21977/8cqnrff-30217`
  - `e1` (source_body): bot que lee las conversaciones unread de GHL (SMS + email), consulta la base de datos real del venue, y genera un borrador de respuesta con la voz del operador. El borrador se postea como nota interna... nunca envía directo al cliente
  - `e2` (source_body): si decision=draft pero score < 0.75, el draft se degrada a flag_human y NO se postea (queda en el log para calibración).
  - `e3` (source_body): VENUE_AVAILABILITY — calendario real de los próximos 90 días construido desde la DB... BOOKING_CONTEXT — los bookings del propio contacto (match por email, fallback últimos 7 dígitos del teléfono)
  - `e4` (source_body): prohibido prometer plazos ("in a few minutes") porque el draft lo envía un humano después; day-of / "we're here" → flag_human... códigos de acceso solo si ya están en el thread y el evento es <24h

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21977/8cqnrff-30217`
- Source hash: `bd7db4a8ad3e943cd5c5d9f98c34fd9e02a05f5fa53ba483936d5199741d04cd`
- Observed at: 2026-10-17T22:40:10.764Z
- Agent run: `8472207b-87c9-4c66-a513-e19558ffc232`
- Validation run: `41a00979-1e5f-4419-903d-c6dd8cdaa962`
