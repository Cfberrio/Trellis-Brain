---
brain_note_id: "dest:unknown:34bd9b2fe025a38b51a16c7d6876306e"
canonical_key: "unknown/34bd9b2fe025a38b51a16c7d6876306e"
brand_id: "unknown"
---
# Tarea: Fix Composio settings and add luistorresportillo123@gmail.com

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: Habla de varias marcas (`MULTI_BRAND`)
- reason: `The task involves configuring a tool (Composio) that manages connections for multiple distinct brands including Discipline Rift, Cheese To Share, and Orlando Event Venue. Since the infrastructure being fixed serves all these brands simultaneously, it is classified as MULTI.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3avhpv` · [Abrir en ClickUp](https://app.clickup.com/t/86e3avhpv)

**Contenido original**

Objective
Fix Composio's MCP settings so it can access luistorresportillo123@gmail.com for sending email and scheduling via Google Calendar.
Context
Composio currently has 6 active Gmail connections (aliases: DISCIPLINERIFT GMAIL, TROVERO, CHEESETOSHARE GMAIL, CHEESETOSHARE INFO, ORLANDOEVENTVENUE, DISCIPLINERIFT INFO), but none are aliased to luistorresportillo123@gmail.com. There are also two expired unlabeled connections that might be the right one. The Google Calendar connection is also EXPIRED.

To Keep in Mind
Link the Gmail account: Run composio link gmail → sign in as luistorresportillo123@gmail.com, or identify which existing alias maps to that inbox.
Re-link Google Calendar: Run composio link googlecalendar to restore calendar-based scheduling.
Optionally add Bash(composio execute GMAIL_GET_PROFILE+) to permissions so Composio can auto-resolve inboxes in the future.
After linking, verify you can call GMAIL_SEND_EMAIL via Composio with the correct sender address.

**Comentarios**

- **2026-09-18 · Cristian Berrío**: Ya linkee tu cuenta de gmail a composio, a que cuenta quieres que linkee lo de google calendar ? @Luis Torres
- **2026-09-18 · Luis Torres**: Google calendar? Como asi?
- **2026-09-18 · Cristian Berrío**: En el task sale linkear google calendar

_Sincronizado por Brain: 2026-10-01T03:13:38.777Z_
