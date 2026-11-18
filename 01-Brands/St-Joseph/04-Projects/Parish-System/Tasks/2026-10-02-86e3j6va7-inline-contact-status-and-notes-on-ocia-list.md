---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3j6va7"
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
  - week-oct-5
---

# Add inline contact status and notes editing to OCIA candidates list

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 5 🍁
- Tarea padre: [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3j6va7](https://app.clickup.com/t/86e3j6va7) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | Cristian Berrío |
| Creada | 2026-10-02 13:07 |
| Actualizada | 2026-10-07 11:16 |
| Cerrada | 2026-10-07 08:59 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis pidió poder cambiar el estado de contacto/entrevista y agregar notas directamente desde la lista de candidatos de OCIA (/admin/ocia-candidates), sin abrir cada perfil, para agilizar las sesiones de llamadas con 145 candidatos. El 2 de octubre Cristian lo construyó y lo guardó localmente (visible al publicar): la columna de estado (antes "Interview") es un botón con Not contacted / Contacted / Scheduled / Interviewed que guarda al instante, y una columna nueva de notas con la última nota, fecha y conteo, con autor y hora, compartidas con el perfil y con las notas de la lista maestra de Johanna ya importadas. Elegir "Interviewed" no registra fecha ni entrevistador (eso sigue en el perfil) y no hizo falta cambiar la base de datos; quedaba pendiente publicar.

## Descripción
## Objective
Let staff update a candidate's **contact/interview status** and **add notes** directly from the _Adults receiving sacraments_ (OCIA candidates) list, without opening the candidate profile. Workflow should be: see "Not contacted" → click → switch to "Contacted" → move to the next row.
## Context
Current list view (`/admin/ocia-candidates`):

![](https://t9017418223.p.clickup-attachments.com/t9017418223/f294526c-fa2e-4caf-9f39-b56ee0705fc2/Screenshot%202026-10-02%20at%201.05.16%E2%80%AFPM.png)

Right now the **Interview** column shows a read-only badge ("Not contacted", "Interviewed"). To change it, or to jot a note after a call, staff have to open each profile. With 145 candidates (66 registered but not attending), that's way too many clicks for a call-through session.

Requested by Luis in [https://app.clickup.com/t/9017418223/86e3ercb4?comment=90170258218577](https://app.clickup.com/t/9017418223/86e3ercb4?comment=90170258218577).
## To Keep in Mind
*   **Status:** make the Interview badge a clickable inline dropdown (e.g. Not contacted → Contacted → Interview scheduled → Interviewed). One click to open, one to pick, saves instantly, no modal, no page reload.
*   **Notes:** add a Notes column or a small note icon per row that opens an inline popover/textarea. Show a preview of the latest note (truncated) in the row. Save on blur or Enter.
*   Notes edited inline must be the same notes shown on the candidate profile (single source of truth). Ideally timestamp + author on each note.
*   Optimistic UI with a quick saved indicator; roll back and show an error if the save fails.
*   Clicking the status/notes controls must NOT trigger the row click that opens the profile.
*   Existing filters ("Any interview status") and the Excel by group export should reflect the updated status immediately.
*   Keyboard friendly would be a plus (tab to next row) since staff will be blasting through a call list.

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| Screenshot 2026-10-02 at 1.05.16 PM.png | png (image/png) | 2026-10-02 13:07 | Luis Torres (al crear la tarea) |

## Comentarios
### 2026-10-02 17:05 · Cristian Berrío
Update (Oct 2): contact status and notes can now be edited straight from the candidates list

Built and saved locally. It appears once the latest version is published.

What staff can do now on Sacraments (the candidates list):
Contact status: the column (formerly "Interview") is now a button. Click it and choose Not contacted, Contacted, Scheduled or Interviewed. It saves right away, with no need to open the profile.
Notes: new column showing each person's latest note, its date and how many notes they have. Click it to read the recent notes and add a new one (for example "Called, left voicemail"). Notes keep who wrote them and when.
Johanna's master-list comments were already imported as notes, so the history is there from day one.
A note added on a person's profile page also shows up in the list.
Clicking anywhere else on the row still opens the full profile.
The "Any contact status" filter shows, for example, everyone still "Not contacted" (the call list).

Notes:
Choosing "Interviewed" only changes the status. The interview date and interviewer are still entered on the profile, so we don't record a wrong date automatically.
No database changes were needed.

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjca-module-4-sacraments-ocia|Module 4: Sacraments (OCIA)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-02-86e3j53x0-apply-oct-2-review-corrections|Apply Oct 2 review corrections]]
