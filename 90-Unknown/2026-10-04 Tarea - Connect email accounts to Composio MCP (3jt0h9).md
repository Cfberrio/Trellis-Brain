---
brain_note_id: "dest:unknown:1cbaa7505632cbe66485f2890dcfdc37"
canonical_key: "unknown/1cbaa7505632cbe66485f2890dcfdc37"
brand_id: "unknown"
---
# Tarea: Connect email accounts to Composio MCP

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: Habla de varias marcas (`MULTI_BRAND`)
- reason: `The task involves connecting multiple email accounts across several Trellis brands including Cheese To Share, Discipline Rift, and Orlando Event Venue (Reliable Venues) to a central MCP tool.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3jt0h9` · [Abrir en ClickUp](https://app.clickup.com/t/86e3jt0h9)

**Contenido original**

Objective
Connect every in-scope Google account (Chrome profiles listed below) to the Composio MCP so Claude has email access across all of them.
Context
Luis wants email access through Composio for each of his active accounts. The accounts come from his Chrome profile list (screenshot). The current Composio connection is only logged into info@disciplinerift.com (DR @info), not grouptrellis@gmail.com, which is why actions against other accounts (e.g. luistorresportillo123@gmail.com) fail with a 404. Each account needs its own connection via composio link (e.g. composio link gmail / composio link googlecalendar) while logged into that account.

Request:

Accounts to connect
Trellis (grouptrellis@gmail.com)
Cheese (Work)
Cheese to (cheesetoshare.us)
Cheese to Share
Discipline
Discipline (disciplinerift.com)
DR (disciplinerift.com): likely the already-connected info@disciplinerift.com, verify
Empanada (Work)
Fraternity (Work)
Impulsa Fortuna
Luis
LUIS
Luis (disciplinerift.com)
Out of scope for now (bottom 5)
Luis (reliablevenues.com)
luis alejandro
Orlando
Orlando
Tovero's (Work)
To Keep in Mind
Log into the correct Google account during each OAuth step; Composio silently binds to whichever account is active in the browser.
After each connection, verify by listing that account's inbox/calendars and confirm the email address matches.
Grant email (Gmail) scope at minimum; add Calendar if needed for the same account.
Record the email address behind each Chrome profile name, since several profile names (Luis, LUIS, Discipline) don't show the address.

_Sincronizado por Brain: 2026-10-04T16:11:55.540Z_
