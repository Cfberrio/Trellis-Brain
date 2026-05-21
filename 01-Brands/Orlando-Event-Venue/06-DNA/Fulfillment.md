---
brand: Orlando-Event-Venue
area: dna
note_type: leaf
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "OEV-specific Fulfillment synthesized from Doc 8cqnrff-4977 (BOOKING CALENDAR / 10-step post-booking sequence) + Brand-Home + GoHighLevel-Operating-System notes"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Fulfillment

## Parent
- [[DNA-Home|OEV DNA Home]]

## Related
- [[Conversion|OEV Conversion]]
- [[Retention|OEV Retention]]
- [[../02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]]
- [[../05-Operations/OEV-Admin-Command-Center|Admin Command Center]]
- [[../05-Operations/OEV-Staff-Operations-Console|Staff Operations Console]]
- [[../05-Operations/OEV-GoHighLevel-Operating-System|GHL Operating System]]
- [[../05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]

## Purpose
How OEV produces results: deliver a smooth, compliant event experience from deposit-paid → post-event review without surprises.

## Activation Point Candidates (pick + measure)
Per template: *"Every customer who does X stays longer / re-books more than customers who don't."*

For venue rentals:
- **AP1 (commitment depth):** "Every booking where the customer pays the remaining 50% balance at least 15 days before event re-books at a higher rate."
- **AP2 (engagement):** "Every booking where the customer opens the 30-day reminder email and replies with confirmed details has higher show satisfaction."
- **AP3 (post-event proof):** "Every booking with a completed Guest Report + Google review re-books at a higher rate."

## Critical Path (booking → review)

### Stage 1 — Deposit Received (T-event = book day)
- Welcome email: 50% deposit confirmed + team will review in 24 hours
- **Do not send invitations yet** (review pending)
- Booking moves to **Pending Review** status in admin

### Stage 2 — Booking Confirmed (T-event-N days)
- Email: "Your Event Is Confirmed | Date Locked In"
- What's included: 90 chairs, 10 tables, prep kitchen, 2 bathrooms
- Remaining balance due 15 days before event
- Access instructions emailed 1 day before event
- Booking moves to **Confirmed** status

### Stage 3 — Pre-Event Prep
- **Day -30:** 30-day reminder email (review key details + Wi-Fi info + reminders about prohibited items)
- **Day -15:** Remaining balance reminder (email + SMS) with payment link
- **Day -7:** 7-day reminder email (venue info + Wi-Fi + reminders about prohibited items)

### Stage 4 — Event Day Ready
- **Day -1:** Access instructions emailed (lockbox code, magnetic key, lights, checkout steps) + SMS reminder
- **Day 0 hour -1:** 1-hour reminder (email + SMS) with full access instructions repeated

### Stage 5 — Event In Progress
- Customer accesses venue per Day -1 instructions
- Customer setup + execution + breakdown WITHIN booking window
- Staff inspection scheduled (if applicable)

### Stage 6 — Post-Event Inspection
- **After booking ends:** Guest Report sent (email + SMS) — 2–3 min checklist with photos/videos of door, main area, tables/chairs, bathrooms, kitchen
- Customer replies DONE when complete
- Internal inspection logged → fees decision

### Stage 7 — Review Request
- Email-only review request: "Action Needed Orlando Event Venue"
- Google review link: `g.page/r/CU-yUA0El90UEAE/review`
- Booking moves to **Closed / Review Complete** when review received

## Roles Required

### Program Operator (Admin) — Sales Lead
- Booking confirmations + customer comms cadence
- Payment link sends + reconciliation
- 30/15/7/1-day reminder send orchestration
- Pending → Confirmed → Closed transitions

### Operations Manager
- Pre-event setup + tech check + incident log
- Day-of inspection coordination
- Fee decision (overtime / damage)

### Tech / AV (when production package included)
- Setup + equipment check before event
- Stand-by during contracted tech hours
- Equipment teardown

## Quality Control (Weekly Dashboard)
- % bookings with deposit received → confirmed within 24h SLA
- % bookings with remaining balance paid >= 15 days before event
- % bookings with Guest Report submitted
- % bookings with Google review completed
- Cancellation rate
- Incident / fee events

## Save Plays
- **Customer didn't pay remaining balance by Day -15:** SMS + call within 24h. Confirm payment link working. Escalate to Luis after 48h.
- **Customer missing access info on Day -1:** Manual re-send + SMS confirmation requested.
- **Guest Report not submitted within 48h post-event:** Email follow-up + soft escalation if incident suspected.

## Quality Standards (non-negotiable)
- All customer-facing emails use the canonical templates in [[../02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]]
- Wi-Fi credentials communicated only in 30-day reminder + 7-day reminder (not earlier — prevents premature use)
- Access instructions communicated only 1 day before (NOT in confirmation — prevents access before booking starts)
- Lockbox code = booking-date-coded (per Brand-Home rules)
