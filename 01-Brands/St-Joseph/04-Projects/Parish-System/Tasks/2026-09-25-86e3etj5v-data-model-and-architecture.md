---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3etj5v"
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

# Data model & architecture (extensible to Phase 2)

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 5 🍁
- Tarea padre: [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3etj5v](https://app.clickup.com/t/86e3etj5v) |
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
Se pidió diseñar el modelo de datos y la arquitectura del sistema, extensible a la Fase 2. El esquema principal vive en el repo st.-joseph-connect (supabase/migrations) y se verificó contra el código el 2 de octubre: entidades centrales, roles y permisos por área, seguridad a nivel de fila, bitácora de auditoría, ganchos para Fase 2, emails familiares compartidos, registro de llamadas y libretos de ritos. Quedan abiertos: el ERD y su revisión con Luis, pantallas de staff en español, un registro de hogar (household) para dos padres y un formulario/pantalla para servidores de Emaús.

## Descripción
Core schema in the [st.-joseph-connect](https://github.com/Cfberrio/st.-joseph-connect) repo (supabase/migrations). Verified against the code Oct 2.

Core entities built: people, children + guardians, programs (with formation years and groups), terms, sessions, rooms, room bookings, registrations, form definitions, attendance, adults-receiving-sacraments profiles, sacrament paths per group, documents, payments, events, catechist assignments, rites booklets, calendar feeds, audit log.

- [ ] ERD + review with Luis
- [x] Roles & permissions: admin, staff, data manager, catechist, volunteer + access by area (adults receiving sacraments, AFF, youth, children, events, everything)
- [x] Row-level security on every table, audit log (Settings → Audit). Backups: Lovable Cloud.
- [ ] EN/ES: participant pages are bilingual; staff screens are English only
- [x] Phase 2 hooks: program kinds for youth, children, young adults, ministries; rooms
- [ ] Households with two parents: children link to several guardians, but there is no household record
- [x] Shared family emails: matched by email + first name, "Data clear" flag
- [ ] Emmaus server vs walker: stored on each registration from the import; no server form or screen yet
- [x] Call campaign log (caller, 3 attempts, outcome)
- [x] Rites booklets per year; formation year and groups

## Subtareas
_Sin subtareas._

## Adjuntos
_Sin adjuntos._

## Comentarios
_Sin comentarios._

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj6r-module-1-registration-engine|Module 1: Registration engine]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjca-module-4-sacraments-ocia|Module 4: Sacraments (OCIA)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjjr-module-7-branding-bilingual-ui-launch-training|Module 7: Branding, bilingual UI, launch & staff training]]
