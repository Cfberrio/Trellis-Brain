---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3etj6r"
owner: Cristian
last_updated: 2026-11-17
sensitivity: internal
related_systems:
  - clickup
  - st-joseph-connect
related_notes:
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home]]"
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system]]"
hub_role: leaf
tags:
  - st-joseph
  - clickup-task
  - week-oct-5
---

# Module 1: Registration engine (OCIA, Adult Formation, Events)

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 5 🍁
- Tarea padre: [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3etj6r](https://app.clickup.com/t/86e3etj6r) |
| Estado | aprobado |
| Prioridad | high |
| Creada por | Cristian Berrío |
| Asignados | Cristian Berrío |
| Creada | 2026-09-25 13:43 |
| Actualizada | 2026-10-07 11:17 |
| Cerrada | 2026-10-07 08:59 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Se pidió el motor de inscripciones para eventos (Fase 1) y OCIA (Fase 2). Al 2 de octubre estaban construidos el constructor de formularios, el Candidate Form v2 de OCIA (sin requisito de registro parroquial, asigna grupo según respuestas), el corte de inscripción ("next cycle"), el flujo directo a las listas, la importación de datos existentes y los 13 formularios del sitio web agregados el 28 de septiembre. Quedan abiertos: decidir con la parroquia si Adult Formation mantiene formulario o solo QR, enlazar la clase del niño con Camino, el formato de importación de Camino para Wendy y el formulario de servidores de Men's Emmaus.

## Descripción
Phase 1 (events) and Phase 2 (OCIA) registration. Verified against the code Oct 2.

- [x] Form builder with flexible questions (field types, options, conditional questions)
- [x] OCIA form without a church-registration requirement: **Candidate Form v2** (redesigned from the Tree and Data meetings; the parish's 13-question Microsoft Form stays as the historical source). Groups are assigned from the answers.
- [ ] Adult Formation form with role: the website says "Adults do not need to register"; the QR sign-in asks "What describes you today?" (OCIA / parent / learning more) and sorts people. **Asked the parish:** keep a form or QR sign-in only?
- [ ] Parent ↔ child link: children and guardians are stored and parents are "Required" when a child is in sacrament prep; the child's class is free text, not linked to Camino
- [x] Registration cutoff → late registrants marked "next cycle" (not sacrament-eligible this cycle)
- [ ] Parish membership data for Wendy (Camino): an email to the office is queued per new parish registration; Camino CSV exports use neutral columns until we get a sample Camino import file
- [x] Submissions flow straight into the lists (people, registrations, profiles, children)
- [x] Existing data imported: OCIA master list, sign-in sheets, catechists, retreat and Gospel of John Microsoft Forms exports; in-app importer for event registrants
- [x] Parish website forms added Sept 28 (13): baptism inquiry, baptism prep class, marriage inquiry, marriage mentor training, parish registration, catechist sign-up, Agape market, Spanish Bible study, Never Alone, Men's Emmaus walkers, Women's Emmaus walkers and servers, Trunk or Treat
- [ ] Men's Emmaus **server** form: servers came from the Microsoft Form export; no server form in the app yet

## Subtareas
_Sin subtareas._

## Adjuntos
_Sin adjuntos._

## Comentarios
_Sin comentarios._

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj5v-data-model-and-architecture|Data model & architecture]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj7p-module-2-payments-and-reconciliation|Module 2: Payments & reconciliation]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj9x-module-3-attendance-qr-check-in-absence-rules|Module 3: Attendance, QR check-in & absence rules]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjca-module-4-sacraments-ocia|Module 4: Sacraments (OCIA)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjgz-retreats-pilot-emmaus-silent-retreat-never-alone|Retreats pilot]]
