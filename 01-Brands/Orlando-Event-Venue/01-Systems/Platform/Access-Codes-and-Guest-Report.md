---
brand: Orlando-Event-Venue
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT commits 2026-06-18 → 2026-08-03 (accesscode series) + docs/features/RESCHEDULE-BOOKING.md"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - platform
  - operations
---

# Access Codes and Guest Report

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]]
- [[01-Brands/Orlando-Event-Venue/05-Operations/Agent/Voice-Agent-Knowledge-Pack|Voice Agent Knowledge Pack]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Automation-Jobs-and-Cron|Automation, Jobs and Cron]]

## What it is
A single client-facing page that carries everything the host needs to physically run their event: building and suite access, venue rules, and, after the event, the guest report. It replaced a scattered set of emails and manual messages.

## Two states, one page
The page is **date-gated**. Before the day of the event it stays locked with explanatory copy; the access details only unlock on the event date. Two states in total:

1. **Before event day** — locked state, sets expectations, no codes exposed.
2. **Event day and after** — access details plus the venue rule tables, and after the event it becomes the **guest report** flow.

Unifying the access page with the post-event guest report is what removed a whole manual step from closeout.

## Venue rules
Rules are rendered as **full rule tables grouped by category heading**, matching the operations spec. The earlier version showed category headings only, which read as incomplete to hosts.

The page also carries a **direct review link**, which is the moment of highest goodwill and therefore the correct place to ask for the review.

## Recurring access codes
Recurring clients — FCG, Global, Guest — have seeded recurring codes rather than a fresh code per booking. This removed per-event manual code issuance for the venue's repeat renters.

## Access information handling
Wi-Fi and access details are delivered through this page and through the balance confirmation copy, not scattered in ad-hoc emails. Credentials themselves are not documented in this vault; they live in the operational store. When venue access details change, update the access page seed, the balance confirmation copy and the [[01-Brands/Orlando-Event-Venue/05-Operations/Agent/Voice-Agent-Knowledge-Pack|Voice Agent Knowledge Pack]] together, or the three surfaces drift apart.

## Interaction with reschedule
Rescheduling a booking recreates the host-report jobs for the new date. The access page follows the booking's event date, so a rescheduled event automatically re-locks and re-unlocks on the correct day. Reschedule is blocked for `cancelled` and `closed` bookings and validates date conflicts against bookings that block the calendar.

## Next step
The recurring-code list (FCG, Global, Guest) is an operational fact that changes with the client roster. Whoever adds a recurring renter must add the seed and note it here.
