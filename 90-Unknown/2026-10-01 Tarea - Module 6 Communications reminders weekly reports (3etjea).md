---
brain_note_id: "dest:unknown:c5df12d9f525e9dce9253dc1d3ecab0b"
canonical_key: "unknown/c5df12d9f525e9dce9253dc1d3ecab0b"
brand_id: "unknown"
---
# Tarea: Module 6: Communications, reminders & weekly reports

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The content describes a specific parish/church management implementation (OCIA, parish registration, Camino import, St. Joseph account) which does not align with the defined brands: Cheese To Share (food), Discipline Rift (gaming/fitness), Orlando Event Venue (events), or Trellis Core (generic platform). It appears to be a specific client project or vertical not listed in the provided brands.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3etjea` · [Abrir en ClickUp](https://app.clickup.com/t/86e3etjea)

**Contenido original**

Verified against the code Oct 2. Email goes through an Outbox: messages are queued and a staff member presses Send. Nothing is scheduled yet.

Deploy email sending (send-queued-emails, send-login-code). Sending account: Luis's St. Joseph account for now; move to the Adult Formation address when it exists.
Reminders for missing certificates: email template + Follow-ups list work by hand; SMS only opens the phone's messaging app (no SMS service)
Follow-up sequences for people who haven't responded: Follow-ups suggests who to contact and shows "last messaged"; no automatic sequences
Session reminders (EN/ES): template exists, picks each person's language; sent by hand
Weekly summary report: on screen with print/CSV; not emailed
Wendy gets an email per new parish registration (queued)
Export for Wendy → Camino: CSV with neutral columns until we get a sample Camino import file
Printable schedule: each group has a public schedule link with a Print button (EN/ES), e.g. the OCIA schedule to hand out on Sunday
Call script for the call campaign: Luis writes it

_Sincronizado por Brain: 2026-10-03T02:58:21.998Z_
