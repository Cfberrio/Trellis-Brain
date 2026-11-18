---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3r1g9k"
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
  - week-oct-19
---

# Fix Sacraments Excel export grouping, filters and formatting

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 19 🪪

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3r1g9k](https://app.clickup.com/t/86e3r1g9k) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | — |
| Creada | 2026-10-15 13:06 |
| Actualizada | 2026-10-16 11:02 |
| Cerrada | 2026-10-16 11:02 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis reportó que el Excel descargado desde la página Sacraments mezclaba a quienes asisten y quienes no, y pidió mejor organización, filtros y formato, corrigiendo la generación del export y no un archivo puntual. Cristian lo dejó hecho y publicado el 15 de octubre: columna Participation status con bloques por estado y colores, filtros de Excel en cada pestaña, descarga que respeta los filtros de la página (con sufijo "-filtered"), nueva pestaña Summary y mejoras de legibilidad, sin cambiar datos de participantes. Se probó con cuentas demo en tres descargas que coincidieron con los conteos del dashboard. No quedan pendientes abiertos en los comentarios; los archivos de muestra quedaron guardados localmente.

## Descripción
## Objective
Improve the Excel workbook downloaded from the dashboard's Sacraments page so people are organized correctly within each worksheet, attending and not-attending participants are not mixed together, and staff can filter and read the export easily. Fix the export generation, not just one downloaded file.
## Context
Luis reported that the current export mixes attending and not-attending people and needs better organization and formatting. Source: [https://app.clickup.com/t/9017418223/86e3p6vdw?comment=90170263046910](https://app.clickup.com/t/9017418223/86e3p6vdw?comment=90170263046910).

The screenshot shows `adults-receiving-sacraments-2026-10-15` with worksheets for Adult Sacraments - Catholic, OCIA - Baptized other Christian, OCIA - Unbaptized, OCIA - Baptism to verify, and Special cases. Visible columns include Name, Phone, Email, Address, Contact incomplete, Group, Sacraments needed, and Rite. Long values are clipped and the visible header has no filter controls.

![](https://t9017418223.p.clickup-attachments.com/t9017418223/31279390-c761-47b8-8f04-0c06d51e0844/image.png)
## To Keep in Mind
*   Preserve the existing group worksheets and put each person in the correct group using the dashboard's actual group data.
*   Within every worksheet, keep attending and not-attending participants together in separate, clearly labeled blocks using the existing participation-status values. Show other or unset statuses distinctly rather than guessing. Sort names alphabetically within each status group.
*   Include a clearly labeled participation-status column and working Excel column filters. Support filtering by the relevant existing dashboard fields, including participation status, group, sacraments needed and rite. Keep any date-specific attendance separate from overall participation status.
*   Ensure the export respects the applicable dashboard filters and clearly identifies the exported scope so filtered downloads do not unexpectedly include other participants.
*   Improve readability with bold, contrasting headers, frozen header rows, sensible column widths, wrapped long text, consistent alignment and alternating row shading. Keep the data range filterable without merged cells or decorative rows breaking sorting and filtering.
*   Preserve all existing useful columns and data. Keep phone numbers as text and do not alter contact details, sacramental classifications or participant records as part of this export-format fix.
*   Test every worksheet and filtered/unfiltered downloads against the dashboard: correct group and status placement, matching row counts, no missing or duplicated participants, useful handling of blank statuses and empty groups, and no clipped critical information. Open a newly generated workbook in Excel to verify the result.
*   Deliver a sample regenerated workbook and evidence that attending and not-attending participants are correctly separated.

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| image.png | png | 2026-10-15 13:06 | Luis Torres |

## Comentarios
### 2026-10-15 15:19 · Cristian Berrío
✅ Done and published. The "Excel by group" button on the Sacraments page now generates the new workbook.

What changed
Attending and not attending are no longer mixed. Every group tab starts with a Participation status column, using the same values as the dashboard's "Attendance this formation year" chips. People are grouped by status in this order: Registered & attending → Attending, not registered → Registered, not attending → No class yet → Status not set (people with no class registration, shown as their own group instead of guessed). Each status has its own color, a darker line separates the groups, and names are sorted by last name inside each group.
Excel filters work. Every tab has filter arrows in the header row, so you can filter by status, group, sacraments needed, rite or any other column. There are no merged cells or extra rows inside the table, so sorting and filtering cover everything.
The download follows the page filters. It only includes the people shown on screen. The button shows the count (for example "Excel by group (6)"), and the file name ends in "-filtered" when filters are on.
New Summary tab (first tab): export date and time, scope (all or filtered, with each filter listed), what each status means, and counts per tab and status.
Easier to read: a bold dark header that stays visible when scrolling, Status and Name stay visible when scrolling right, set column widths with wrapped text (nothing cut off), and alternating row shading that stays correct after sorting or filtering.
Unchanged: the same group tabs plus Special cases (each person shows their real group), all the old columns, and phone numbers kept as text. Classes held / Classes attended / Last class stay in their own columns, separate from the overall status. No participant data was changed.

How it was tested (demo accounts with made-up people, not real parishioners)
Downloaded from the page three ways: no filters (81 people), "Registered, not attending" (6) and "Unbaptized" (35). Every file matched the dashboard counts: groups 30 / 9 / 35 / 7 and statuses 74 / 6 / 0 / 1. Nobody was missing or duplicated, every person was on their correct group tab, and the filtered files only had the filtered people.
Automated checks also cover empty groups (the tab stays with a "Nobody in this group" note), people with no status, Special cases and phone numbers starting with 0.
Sample files from the demo data are saved locally (Downloads/sacraments-export-86e3r1g9k).

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-08-86e3myy1e-fix-ocia-classification-baptized-catholics|Fix OCIA classification (baptized Catholics)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-13-86e3pxguj-reconcile-ocia-attendance-registrations-withdrawals|Reconcile OCIA attendance, registrations, withdrawals]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-21-86e3uf6kw-subgrupos-de-matrimonio-en-excel-de-sacramentos|Subgrupos de matrimonio en Excel de Sacramentos]]
- Solicitud original en la semana OCT 19 🪪: [86e3p6vdw](https://app.clickup.com/t/9017418223/86e3p6vdw?comment=90170263046910)
