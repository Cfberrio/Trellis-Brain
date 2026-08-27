---
brand: Orlando-Event-Venue
area: communication
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
sensitivity: internal
hub_role: communication-hub
last_updated: 2026-08-26
---

# Orlando Event Venue — Communication Home

## Parent
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|OEV Brand Home]]

## Children
- [[01-Brands/Orlando-Event-Venue/02-Communication/OEV-Communication-Manual|OEV Communication Manual]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Email-Design-System|OEV Email Design System]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/GHL-Email-Templates|OEV GHL Email Templates]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Booking-Calendar-Sequence|Booking Calendar Sequence]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Tour-Sequence|Tour Sequence]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Pop-Up-Lead-Magnet-Sequence|Pop-Up Lead Magnet Sequence]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/General-Invoice-Templates|General Invoice Templates]]

## Related
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Voice-and-Tone|OEV Voice and Tone]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Language-Rules|OEV Language Rules]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Visual-Identity|OEV Visual Identity]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Sales-Home|OEV Sales Home]]

## Purpose
Hub for all Orlando Event Venue communication rules, client-facing messaging standards, and channel logic.

## Two Layers, Kept Separate

Communication splits into a layer that owns **what emails say** and a layer that owns **how they look**. Changing one must never quietly change the other.

### What they say
The active manual is [[01-Brands/Orlando-Event-Venue/02-Communication/OEV-Communication-Manual|OEV Communication Manual]], which documents:
- core voice and writing rules for all OEV channels
- full channel logic matrix (email vs SMS by touchpoint type)
- canonical access instructions for 1-day and day-of reminders
- venue rules, pricing reference, and merge field reference for automations
- post-booking sequence logic, tour sequence, and lead capture flow
- subject line system and signature blocks

Copy authority for guest-facing email is the ClickUp spec doc "OEV POST BOOKING COMMUNICATIONS" plus [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Language-Rules|OEV Language Rules]].

### How they look
[[01-Brands/Orlando-Event-Venue/02-Communication/Email-Design-System|OEV Email Design System]] — the rendering layer added 2026-08-26. Shared module, stacked color modules, no photography. Its governing rule: **design carries emphasis, wording never changes.**

## Channels
- **Supabase edge functions** — transactional email sent by the platform. Eleven guest-facing functions, all on the design system. See [[01-Brands/Orlando-Event-Venue/02-Communication/Email-Design-System|Email Design System]].
- **GoHighLevel** — lifecycle email and all SMS. Five rebuilt templates in [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/GHL-Email-Templates|GHL Email Templates]]; automation wiring in [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Automations|OEV GoHighLevel Automations]].

Both channels can address the same touchpoint. Before enabling an automation on one side, check whether the other already covers it — there is a known unresolved overlap on the balance-due email.
