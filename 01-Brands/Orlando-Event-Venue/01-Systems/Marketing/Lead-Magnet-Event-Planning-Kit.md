---
brand: Orlando-Event-Venue
area: systems
subarea: marketing
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT commit 3f152d2 (2026-08-04) implementing ClickUp 8cqnrff-4977 / 8cqnrff-11737 + follow-up commits cdfe60a, 7a4e4f1"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - marketing
  - lead-magnet
---

# Lead Magnet — Event Planning Kit

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Marketing-Home|OEV Marketing Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Pop-Up-Lead-Magnet-Sequence|Pop-Up Lead Magnet Sequence]] — **superseded**, kept for history
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Google-Ads-Post-Mortem-2026-06|Google Ads Post-Mortem — June 2026]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Lead-Definition|OEV Lead Definition]]

## Offer history — read this first
The public discount offer has changed three times. Anything in this vault referencing SAVE100 or HOST100 as the live offer is out of date.

| Offer | Period | Status |
|---|---|---|
| SAVE100 / SAVE50 | until 2026-05-29 | deactivated |
| HOST100 | 2026-05-29 → 2026-08-04 | deactivated — and broken in production for most of its life, see the post-mortem |
| **PLAN50** | 2026-08-04 → current | **active default coupon** |

## What the magnet is now
An **Event Planning Kit** plus **$50 off**, replacing the pure discount offer. The kit gives the planner something usable before they ever talk to OEV, which is a better fit for a venue whose buyer is organizing a real event under time pressure.

## Popup
- Copy leads with the kit and the $50 off.
- Fields: first name, email, **required event date**, phone.
- The event-type dropdown was removed.
- Spec-defined error messages, and a confirmation screen without kit/email buttons.
- Persists phone, consent evidence and lead source on `popup_leads`.
- `send-popup-lead` forwards the event date to GHL as `oev_event_date`.

Capturing the event date at popup time is what makes the date-collision problem from the June post-mortem actionable: the venue can see immediately whether a lead is chasing a contested date.

## `/planning-kit` page
Eleven spec sections with tickable checklists and fillable worksheets saved per device, exported as a **vector PDF** (jsPDF, lazy loaded). Tables stack into labelled blocks below 640px so nothing is cut off on phones.

## Email drip
Rewritten as **OEV-LM-E01 / E02 / E03** with kit links and no expiry language. Both follow-ups are measured from email 1 (**18h** and **36h**), and the drip sends at **8:00 AM Orlando time**, not at fixed hour offsets from signup. A later fix stopped the drip from skipping runs and then firing in bursts.

## Deferred
Per the spec's developer note: per-contact PLAN50 expiry is not implemented. The coupon is currently a shared code with no per-lead expiry window.

## Next step
Retire or annotate any older asset still promoting HOST100 or SAVE100 — GHL templates, ad copy, and the legacy sequence note linked above.
