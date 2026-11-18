---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3xd8fn"
owner: Cristian
last_updated: 2026-11-17
sensitivity: internal
related_systems:
  - clickup
  - st-joseph-connect
related_notes:
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home]]"
hub_role: leaf
tags:
  - st-joseph
  - clickup-task
  - week-nov-2
---

# Keep one QR code per session instead of rotating every 2 minutes

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: NOV 2 🥩

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3xd8fn](https://app.clickup.com/t/86e3xd8fn) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | — |
| Creada | 2026-10-30 10:52 |
| Actualizada | 2026-10-31 18:53 |
| Cerrada | 2026-10-31 18:53 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis pidió quitar la rotación del QR de asistencia cada 2 minutos y dejar un código fijo por sesión, porque el 22/10 (Adult Faith Formation en inglés) el código no funcionó y la asistencia se tomó en papel. Cristian confirmó la causa el 30/10: la pantalla se mandó como captura por texto y el código vencía a los 2–4 minutos. Ahora el QR lleva el enlace propio de la sesión (/checkin/<session code>), sin vencimiento, con botón Copy link, y sigue abierto solo el día de la sesión y el siguiente; el cambio de base de datos ya estaba en producción. Al momento del comentario faltaba que Cristian hiciera push y publicara (commit 555f310) para los cambios de pantalla.

## Descripción
## Objective
Remove the function that changes the attendance QR code every 2 minutes. Keep one QR code for each session, unchanged throughout that session.
## Context
Luis requested this change in the October 30 comment on NOV 2 🥩 ([https://app.clickup.com/t/86e3vqpkn](https://app.clickup.com/t/86e3vqpkn)). The supplied screenshot shows the QR check-in for Adult Faith Formation (English), Thursday, October 22, 2026, 6:30 PM to 8:00 PM, at Church, for “Part 2: Finding what prayer style works for you: Lectio Divina.” Melanie reported that the code did not work, so attendance was collected on paper instead. The screenshot documents the failed check-in; the exact technical cause has not been verified.

![](https://t9017418223.p.clickup-attachments.com/t9017418223/229bcc41-0775-42a4-a576-66962fe0e2f3/image.png)
## To Keep in Mind
*   Use a separate QR code for each session, not one shared code for every session.
*   Remove the 2-minute rotation and any matching token-expiration behavior that would invalidate the session's unchanged code while check-in is open.
*   Verify that the same code still works after more than 2 minutes, including when displayed as a shared screenshot or on another phone.
*   Confirm check-ins are recorded against the correct session and that one session's code does not check someone into a different session.
*   Keep existing attendance records intact.

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| image.png | png | 2026-10-30 10:52 | — |
| image.png | png | 2026-10-30 10:52 | — |

## Comentarios
### 2026-10-30 11:02 · Cristian Berrío
Done: each session now has one QR code, and it doesn't change.

Why Oct 22 failed (confirmed): the presenter screen was sent as a screenshot by text. The old code expired 2–4 minutes after it appeared, so by the time people scanned the screenshot it no longer worked. Prod shows 0 QR check-ins for that session and 1 paper entry. The other sessions that week, where the live screen was used, worked (Oct 19: 16, Oct 21: 21).

What changed
The QR holds the session's own link (/checkin/<session code>). It works after any amount of time, from a screenshot, or on another phone.
Each session keeps its own code. One session's code can't check anyone into a different session.
Check-in is still only open on the day of the session (and the day after). Cancelled sessions are still refused.
Presenter view: the "changes every 2 minutes" text is gone, and there's a new Copy link button so you can text the link instead of a screenshot.
Existing attendance records were not touched.

Status
Database change is already live. Old QR screenshots and the current published screen already work, so it's fixed today, even before the next publish.
The screen changes (Copy link, removed text) show up once Cristian pushes and publishes (commit 555f310).

Tested on prod (in a transaction that was rolled back, nothing saved): link with no token ✔, link with an old expired token ✔, check-in without a pass recorded on the correct session (the other session's count stayed the same) ✔, closed session refused ✔.

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-30-86e3xd8fp-manual-attendance-oct-22-adult-faith-formation|Manual attendance Oct 22 Adult Faith Formation]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-09-86e3zwmjy-print-ready-attendance-qr-pdf|Print-ready attendance QR PDF]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj9x-module-3-attendance-qr-check-in-absence-rules|Module 3 attendance, QR check-in]]
