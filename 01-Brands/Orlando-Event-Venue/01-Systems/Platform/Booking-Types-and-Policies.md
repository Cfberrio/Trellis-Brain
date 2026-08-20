---
brand: Orlando-Event-Venue
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT docs/features/BOOKING-TYPES-COMPARISON.md + docs/features/EXTERNAL-BOOKING-IMPLEMENTATION-SUMMARY.md"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - platform
  - booking
---

# Booking Types and Policies

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Booking-Calendar-Sequence|Booking Calendar Sequence]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Sales-Process|OEV Sales Process]]

## The three booking origins
Behaviour is driven by a `booking_policies` row selected from `booking_origin`, not by scattered conditionals. Changing what a booking type does means editing its policy.

| | Website | Internal | External |
|---|---|---|---|
| Origin | Client on the web | Admin dashboard | Admin dashboard |
| `booking_origin` | `website` | `internal` | `external` |
| Policy | `WEBSITE_FULL_FLOW` | `INTERNAL_BLOCK_FLOW` | `EXTERNAL_BLOCK_FLOW` |
| `lead_source` | `website` | `internal_admin` | `external_admin` |
| Name convention | as entered | as entered | `External - [Name]` |
| Payment path | `pending → deposit_paid → fully_paid` | `invoiced` | `invoiced` |
| Requires payment | Yes | No | No |
| Stripe checkout | Yes | No | No |
| Deposit / balance emails | Yes | No | No |
| Booking confirmation email | Yes | No | No |
| 30d / 7d reminders | Yes | No | No |
| 1-day reminder | Yes | Yes | No |
| Host report | Yes | Yes | No |
| Guest report | Yes | Yes | No |
| Cleaning report | Yes (custodial) | No | No |
| Staff assignment | From wizard or later | From wizard or later | Only after creation |
| "Assigned to booking" staff email | Yes | Yes | Yes |
| GHL calendar sync | Yes | Yes | Yes |
| Blocks availability | Yes | Yes | Yes |

## When to use each
- **Website booking** — normal paying client. Full automation chain: deposit → confirmation → reminders → staff assignment → event → host report → cleaning report → balance → close.
- **Internal booking** — OEV's own use of the room, or a client handled off-platform, where the date must be blocked and staff notified but no client-facing money flow should fire.
- **External booking** — a partner or externally-managed event that occupies the venue. Blocks the calendar, notifies staff, and stays silent to the client. Since 2026-08 the full website flow can be run for an external booking while skipping the balance chain, when the event needs client comms but not OEV collection.

## Why this design holds up
Policy rows mean a new booking type is a data change, not a refactor. It is also the same mechanism that makes multi-venue possible: a second venue reuses the state machine and only swaps its policy flags. See [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]] §multi-venue.

## Edge cases to respect
- External booking with staff assigned: staff still receives assignment email even though the client receives nothing.
- Changing `booking_origin` after creation does not retroactively fire skipped automations. Treat origin as close to immutable; if it must change, verify which jobs were never scheduled.
- Website booking with no staff assigned still runs client comms; the reports that depend on staff will not fire.

## Next step
Any new booking origin must be added as a policy row plus a line in this table before it ships, so the comms matrix stays legible to non-developers.
