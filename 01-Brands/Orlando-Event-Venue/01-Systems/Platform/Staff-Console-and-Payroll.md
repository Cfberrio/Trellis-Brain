---
brand: Orlando-Event-Venue
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT docs/features/STAFF-DASHBOARD.md + docs/features/PAYROLL.md + commits Jul 2026 (staff addons #7, hours editing #1)"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - platform
  - operations
---

# Staff Console and Payroll

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-Staff-Operations-Console|OEV Staff Operations Console]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]]
- [[01-Brands/Orlando-Event-Venue/06-DNA/Fulfillment|OEV Fulfillment DNA]]

## What the staff console is
A role-based web panel for venue staff only. Each member logs in and sees **only their own** bookings, calendar, payments and role-specific tasks.

| Role | Scope |
|---|---|
| Production | Operate A/V during package hours |
| Assistant | Assigned tasks during the event |
| Custodial | Cleaning, cleaning reports, inventory |
| Bar Vendor | Bar service, client contact |

The sidebar **hides** what a role cannot use. Inventory and standalone assignments appear only for Custodial. Client contact is full for Bar Vendor, limited for Production, hidden for the rest.

## Views
```
/staff/login                              StaffLogin (public)
/staff                                    My Bookings (home)
/staff/bookings/:id                       Booking detail
/staff/bookings/:id/cleaning-report       Cleaning report
/staff/schedule                           Calendar
/staff/payments                           My Payments
/staff/standalone                         Standalone assignments (Custodial)
/staff/standalone/:id/cleaning-report     Standalone cleaning report
/staff/inventory                          Inventory and storage (Custodial)
```

Booking lifecycle colour code is consistent across every view: pending yellow, confirmed blue, pre-event-ready indigo, in progress green, post event purple, closed grey, cancelled red. Role accents: Production purple, Bar Vendor amber, Assistant orange, Custodial neutral.

Mobile-first: tables collapse into stacked cards, sidebar becomes a drawer.

## Two changes shipped July 2026
- **Client add-ons visible to assigned staff.** Staff can now see what the client actually bought for their event, deduplicated by exact match on `addons_detail` rather than substring matching.
- **Per-booking hours editing.** Global event hours and per-person staff hour overrides are editable from the booking, with a helper pair (`getAssignmentHours`, `isValidTimeRange`) that tolerates mixed `HH:MM` / `HH:MM:SS` values and guards Production assignments.

Branding was applied in August 2026: OEV logo on staff sidebar, staff login and admin sidebar, plus a bold brand treatment on both shells.

## Payroll — the concept that matters
Pay is **never typed in by hand**. It is generated from the work.

```
Staff assigned to a booking or standalone cleaning
        ▼ assignment completed (status = completed)
System GENERATES payroll items (one line per concept)
        ▼ each item is born "pending"
Admin reviews, adjusts (bonus / deduction), marks "paid"
        ▼
Staff sees the item as Paid in their own view
```

A **payroll item is a pay line, not a cheque**. One night of work can produce several items — hours plus a bonus — each with its own paid/pending state.

Categories in OEV: Hourly (Production), Hourly (Bar Vendor), Cleaning Fee, Celebration Surcharge, Assistant Fee, Bar Vendor Flat Fee, Bonus (positive), Deduction (always negative).

**Admin view** — Payroll Reports: date-range selector (defaults to current month), four KPI cards (Total Owed, Paid, Pending, Staff count), two tabs (All Staff Payroll, Standalone Cleanings). One row per employee, expandable into their individual pay lines for editing and adjustments.

**Staff view** — My Payments: only their own earned, paid and pending amounts.

The transferable principle for any other venue or brand: **separate automatic calculation from the manual "paid" mark**, and allow adjustments on top of the base calculation. The formula changes per business; the separation does not.

## Known history
- Payroll hours override and the date-range filter were fixed in June 2026, with tests.
- The admin payroll UI was reverted to English and the Reminders module removed in the same pass.
