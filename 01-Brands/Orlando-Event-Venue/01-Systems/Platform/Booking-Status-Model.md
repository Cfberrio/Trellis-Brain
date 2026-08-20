---
brand: Orlando-Event-Venue
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT docs/LOGICA-ESTADOS-CONCEPTUAL.md + docs/REFERENCIA-LOGICA-ESTADOS-BOOKINGS.md"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - platform
  - booking
---

# Booking Status Model

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Types-and-Policies|Booking Types and Policies]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Payments-Invoices-and-Fees|Payments, Invoices and Fees]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Payment-Rules|OEV Payment Rules]]

## Core idea: a booking has two parallel lives
The common modelling mistake is one status column that mixes "where is the event in its lifecycle" with "how much has the client paid". That produces impossible states like confirmed-but-unpaid-and-half-paid.

The model uses **two independent axes**. A real booking is always one point on each axis at the same time, for example `(confirmed, deposit_paid)`.

> Golden rule: a payment event **never** moves the operational axis, and an operational action **never** moves the financial axis. They meet only in guards.

## Operational axis (lifecycle)
```
pending ──▶ confirmed ──▶ pre_event_ready ──▶ in_progress ──▶ post_event ──▶ closed
   └────────────┴───────────────┴──────────────────┴──────────────┴──▶ cancelled
```

| State | Meaning | Moved by |
|---|---|---|
| `pending` | Request arrived, nobody reviewed it | Client |
| `confirmed` | Venue accepts, commitment exists | Deposit payment or admin |
| `pre_event_ready` | Staff, logistics and services ready; automatic countdown starts | Admin, with checklist |
| `in_progress` | Event is happening | The clock |
| `post_event` | Event ended, closeout pending | The clock |
| `closed` | Terminal happy state | Admin |
| `cancelled` | Terminal unhappy state | Admin or client |

Three motors move this axis: human action (admin decisions), the clock (date-driven transitions), and the cancellation exception. `closed` and `cancelled` are terminal.

## Financial axis (payment)
```
pending ──▶ deposit_paid ──▶ fully_paid
   ├──▶ failed      (retryable)
   ├──▶ refunded    (usually after cancellation)
   └──▶ invoiced    (alternate route for external / add-on clients)
```
The motor is always money in or money out. Never the calendar, never the operational admin, except an explicit manual override.

## "LEAD" is derived, not stored
> **LEAD** = `lifecycle: pending` AND `payment: pending`

A request with no money yet. It does not block the calendar. In the admin list, `pending` splits visually into **Leads** (no deposit) and **Pending Review** (deposit paid, deserves real review).

Other derived states, also never stored:
- **Blocks calendar** = `payment ∈ {deposit_paid, fully_paid, invoiced}` and `lifecycle ≠ cancelled`. Only bookings with money occupy dates.
- **Ready for event** can exist as a flag separate from the lifecycle.

Modelling lesson: do not add an `is_lead` column. Derive it, and it can never go inconsistent.

## Guards — where the axes do meet
| Transition | Guard |
|---|---|
| → `confirmed` | Normally requires deposit paid (configurable per venue) |
| → `pre_event_ready` | Extra services resolved (e.g. bar vendor assigned and client contacted) |
| → `cancelled` | Forbidden if already `closed` / completed |
| Reschedule | Forbidden if `cancelled` or `closed` |
| Block calendar date | Only when money exists, never for leads |

Business logic lives in the guards, not in the transitions. That keeps each axis clean and rejects with a readable message ("Cannot mark ready: bar vendor not assigned").

## Multi-venue configurability
The state machine is identical for every venue. What changes is which guards and automations are switched on, via policy flags: `requires_payment`, `auto_lifecycle_transitions`, `requires_staff_assignment`, plus communication flags (confirmation, deposit reminders, balance reminders).

This is the mechanism that lets Reliable Venues replicate OEV without forking the logic. See [[01-Brands/Reliable-Venues/D-space/Logica-de-Estados|D-space Lógica de Estados]] for the sibling implementation.

## Why this matters commercially
Splitting the axes is what makes "why did this lead not close" answerable. A lead stuck at `(pending, pending)` is a sales problem; a booking stuck at `(confirmed, deposit_paid)` two days before the event is a collection problem. One column would hide both.
