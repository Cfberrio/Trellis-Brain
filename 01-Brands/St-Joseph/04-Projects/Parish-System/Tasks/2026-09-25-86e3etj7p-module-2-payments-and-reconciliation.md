---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3etj7p"
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

# Module 2: Payments & automatic reconciliation (replace Gift Central links)

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 5 🍁
- Tarea padre: [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3etj7p](https://app.clickup.com/t/86e3etj7p) |
| Estado | aprobado |
| Prioridad | normal |
| Creada por | Cristian Berrío |
| Asignados | Cristian Berrío |
| Creada | 2026-09-25 13:43 |
| Actualizada | 2026-10-07 11:17 |
| Cerrada | 2026-10-07 08:59 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Se pidió el módulo de pagos y conciliación automática para reemplazar los enlaces de Gift Central. Se decidió Stripe (Checkout + webhook, monto fijado en el servidor); al 2 de octubre estaban construidos los precios por evento (Adult Formation y OCIA gratis), el cruce automático registro-pago, la pantalla de conciliación que reemplaza el proceso manual de los martes, la importación CSV de Gift Central y el estado "To reconcile" para listas importadas. Quedan abiertos: la cuenta de Stripe a nombre de la parroquia (nombre legal, EIN, banco, representante) y la respuesta de la parroquia sobre cómo conciliar pagos ya hechos.

## Descripción
Phase 1. Verified against the code Oct 2.

- [x] Gateway decided: **Stripe** (Checkout + webhook, amount set on the server)
- [ ] Stripe account in the parish's name: legal name, EIN, bank, authorized representative. Test mode on a temporary account until then.
- [x] Event-specific pricing; Adult Formation and OCIA are free
- [x] Automatic registration ↔ payment matching (Stripe webhook; Gift Central rows auto-matched by email, name and amount)
- [x] Reconciliation screen replacing the manual Tuesday process (Payments: balance due, to reconcile, paid, waived/refunded)
- [x] Interim: import the weekly Gift Central report (CSV)
- [x] **"To reconcile" status:** imported lists don't show who paid, so imported paid-event registrations wait as "To reconcile" (no reminder emails) until a payment is matched. Emmaus servers stay "No charge" until the parish says whether servers pay.
- [ ] **Asked the parish:** how to reconcile payments already made (Gift Central report for the retreats?)

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
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjgz-retreats-pilot-emmaus-silent-retreat-never-alone|Retreats pilot]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-13-86e3px9da-guide-kori-through-stripe-setup|Guide Kori through Stripe setup]]
