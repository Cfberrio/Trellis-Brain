---
brain_note_id: "dest:unknown:1e25b1f208565a9721a5e542afa44f7d"
canonical_key: "unknown/1e25b1f208565a9721a5e542afa44f7d"
brand_id: "unknown"
---
# Tarea: Module 2: Payments & automatic reconciliation (replace Gift Central links)

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The task describes a payment and reconciliation module for a parish management system (mentioning OCIA, Emmaus servers, and retreats). While it involves technical implementation details similar to Trellis Core, the specific context (parish operations, Gift Central) does not align with the defined brands: Cheese To Share, Discipline Rift, or Orlando Event Venue.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3etj7p` · [Abrir en ClickUp](https://app.clickup.com/t/86e3etj7p)

**Contenido original**

Phase 1. Verified against the code Oct 2.

Gateway decided: Stripe (Checkout + webhook, amount set on the server)
Stripe account in the parish's name: legal name, EIN, bank, authorized representative. Test mode on a temporary account until then.
Event-specific pricing; Adult Formation and OCIA are free
Automatic registration ↔ payment matching (Stripe webhook; Gift Central rows auto-matched by email, name and amount)
Reconciliation screen replacing the manual Tuesday process (Payments: balance due, to reconcile, paid, waived/refunded)
Interim: import the weekly Gift Central report (CSV)
"To reconcile" status: imported lists don't show who paid, so imported paid-event registrations wait as "To reconcile" (no reminder emails) until a payment is matched. Emmaus servers stay "No charge" until the parish says whether servers pay.
Asked the parish: how to reconcile payments already made (Gift Central report for the retreats?)

_Sincronizado por Brain: 2026-10-03T02:57:18.744Z_
