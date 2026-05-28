---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Restructured 2026-05-28. Lead magnet pop-up + email/SMS sequence. $100 booking credit, code HOST100, 7-day expiry. Founder-led Luis voice across all touches. Touch 4 added at day 6 (24h before expiry) for the loss-aversion final tap."
owner: Luis
last_updated: 2026-05-28
sensitivity: internal
related_systems:
  - ghl
  - website
hub_role: leaf
---

# Pop-Up Lead Magnet Sequence

## Parent
- [[../Communication-Home|OEV Communication Home]]

## Related
- [[../OEV-Communication-Manual|OEV Communication Manual]]
- [[../../00-Brand-Core/Brand-Home|OEV Brand Home]]
- [[Tour-Sequence|Tour Sequence]]
- [[Post-Booking-Email-Sequence|Post-Booking Email + SMS Sequence]]

## Purpose
Canonical pop-up lead magnet + email/SMS nurture sequence. Captures website leads with a **$100 booking credit (HOST100)** good for 7 days, delivered immediately via email + SMS. Four-touch cadence over the 7-day expiry window converts opt-ins to bookings or tours.

## Design Principles
- **Reciprocity** — visitor gives email/phone, receives instant value (the $100 credit) and a clear next step.
- **Loss Aversion (date-stamped credit)** — 7-day expiry creates real, non-manufactured urgency. Touch 4 at day 6 is the highest-leverage tap (24h before loss).
- **Identity-first opener** — Email 1 leads with the non-profit identity. Community framing differentiates OEV from corporate-feeling Orlando venues.
- **Founder-led (Luis voice)** — Emails 2 + 3 + all SMS signed by Luis. Trust lift across the sequence.
- **BAMFAM** — every touch offers two paths: book the date directly OR book a tour first. Reduces the opt-in → booking gap.
- **Single-job SMS** — each SMS has one clear action. Touch 4 SMS is intentionally the shortest (final tap, loss-aversion).
- **Real scarcity only** — calendar references in Email 3 use real OEV booking state, not manufactured urgency. Refresh monthly to avoid stale claims.

## Channel Matrix
| # | Touch | Time | Channel | Job |
|---|---|---|---|---|
| 1 | Welcome + credit delivery | Immediate | Email + SMS | Deliver value, set context |
| 2 | Founder-led + tour option | 18 hours | Email + SMS | Add proof, offer intermediate step (tour) |
| 3 | Last scheduled reminder + calendar urgency | 36 hours | Email + SMS | Real scarcity pitch |
| 4 | Expiry warning *(SMS only)* | Day 6 (~24h before expiry) | SMS | Loss-aversion final tap |

**Volume:** 3 emails + 4 SMS over 7 days.

## Variables Used
- `{{First Name}}` / `[First Name]`
- `{{email}}` *(echoed back in popup confirmation screen)*

## Standard References
- Booking URL: `https://orlandoeventvenue.org/book`
- Tour booking URL: *(populated from website tour scheduler — see [[Tour-Sequence|Tour Sequence]])*
- Credit code: `HOST100` ($100 off base rental, 7-day expiry)

---

## POPUP

**Headline:** Get $100 Off Your Event at Orlando Event Venue
**Subheadline:** Apply it when you reserve any open date. We'll text + email your code in 60 seconds.

**Fields:**
- Name
- Email
- Phone (so we can text your code)
- What kind of event? *(dropdown: Corporate / Workshop / Birthday or Celebration / Non-Profit Gathering / Other)*

**Consent:** [Keep existing compliance language]

**Button:** Send My $100

**Confirmation screen:**
```
✅ Your $100 is on its way. Check your email + text in the next 60 seconds.

Already know your date? Book it now — open dates aren't held until 50% is in.

Want to see the space first? Book your tour online.

Questions? Call or text 407-974-5979.
```

---

## EMAIL 1 — Immediate

**Subject:** Your $100 OEV Credit Is Here | Apply It at Booking
**Preview:** Code HOST100. Good 7 days. Here's what it unlocks.

```
Hi [First Name],

Welcome! Happy you're here.

We're a local non-profit venue on Colonial Drive, built for corporate events, workshops, and gatherings up to 90 guests.

The $100 you just unlocked applies at booking, on top of what's already included.

──────────────────────
Your Booking Credit Code
HOST100
$100 off your base rental
Good for 7 days — apply at checkout
──────────────────────

Reserve your date here:
https://orlandoeventvenue.org/book

What's included with every rental
- Up to 90 guests + 10 tables + 90 chairs
- Prep kitchen for caterers (zero restrictions — bring any caterer you want)
- Free parking — 200+ spots in the Colonial Town Center plaza
- Wall-sized LED stage screen + AV (available via package)
- Bar service available through us if your event needs it

Heads-up: open dates aren't actually held until 50% lock-in goes through. If you have a date in mind, locking it in this week is the safest move.

Questions? Reply to this email, or call/text 407-974-5979.

Luis with the Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr, Orlando, FL 32803
```

---

## SMS 1 — Immediate

```
Hi {{First Name}} — Orlando Event Venue here. Your $100 credit is ready.

Code: HOST100 (good 7 days, apply at checkout)

Open dates aren't held until 50% is in — reserve here: https://orlandoeventvenue.org/book

Questions? Reply or call 407-974-5979. — Luis & the OEV Team
```

---

## EMAIL 2 — 18h

**Subject:** Quick note from Luis (your $100 still works)
**Preview:** What past hosts liked. Plus: want to see the venue first?

```
Hi [First Name],

Quick note from Luis at Orlando Event Venue.

Most planners take a few days at this stage — totally normal. While you're deciding, a few things worth knowing:

What past hosts have told us they liked
- Catering is wide open. No preferred-vendor list, no restrictions. Bring whoever you want.
- Free parking, 200+ spots, no garage fees.
- We're a non-profit, so weekday non-profit bookings get 50% off the base rental (text us if interested).

──────────────────────
Your Booking Credit Code
HOST100
$100 off your base rental — good 7 days
──────────────────────

Two simple next steps:

1. Want to see the space first? Find a day/time that works and book a quick tour online.
2. Already know your date? Lock it in here — 50% holds the date: https://orlandoeventvenue.org/book

Luis & the OEV Team
407-974-5979
orlandoeventvenue.org
```

---

## SMS 2 — 18h

```
Hi {{First Name}} — Luis at OEV. Want to see the space before you commit? Book the tour for free online. Or lock your date now: https://orlandoeventvenue.org/book

Your $100 (HOST100) still works. — Luis
```

---

## EMAIL 3 — 36h

**Subject:** Last call on your $100 + a real heads-up on the calendar
**Preview:** Where we are on bookings + the simplest path to lock your date.

```
Hi [First Name]!

Last reminder I'll send on your $100 credit.

A real calendar note: we're booked through the next month. Open dates in the following month are filling up — if you have a date in mind, this is the right window to lock it in.

──────────────────────
Your Booking Credit Code
HOST100
$100 off your base rental — good for 7 days
──────────────────────

Two ways forward:

1. Reserve your date directly: https://orlandoeventvenue.org/book — 50% holds the date.
2. Call or text me at 407-974-5979 and I'll walk you through it.

Luis & the OEV Team
407-974-5979
orlandoeventvenue.org
```

> **Brand-voice note:** "the next month" / "the following month" is intentionally generic so the email doesn't go stale. If you want sharper real-scarcity language with a real month name, swap to "[Month]" and refresh the value monthly. Vague scarcity is OK; manufactured scarcity is not.

---

## SMS 3 — 36h

```
{{First Name}}, last reminder on your $100 OEV credit. We're booked through the next month; if you have a date in mind here's the link: https://orlandoeventvenue.org/book. Or call/text 407-974-5979. — Luis
```

---

## TOUCH 4 — Day 6 (~24h before expiry) — SMS only

```
{{First Name}} — your $100 OEV credit (HOST100) expires tomorrow. If you have a date in mind, lock it here: https://orlandoeventvenue.org/book — Luis
```

> **Trigger:** Day 6 from opt-in (24 hours before the credit expires).
> **Why SMS only:** inbox volume already at 3 emails by Touch 3. SMS-only keeps the final tap high-signal and personal.
> **Skip rule:** if a booking is detected before this trigger fires, skip.

---

## Operational Rules

### Information delivery rules
- **Credit code (HOST100)** surfaced in every email + every SMS (except Touch 4, where it's the focus of the message).
- **Booking URL** (https://orlandoeventvenue.org/book) appears in every touch.
- **Tour booking option** introduced in Email 2 + SMS 2 (BAMFAM — smaller commitment for visitors not ready to book directly).
- **Luis voice** carried through Emails 2 + 3 and SMS 2 + 3 + 4. Email 1 + SMS 1 use the team voice for the welcome moment.

### Cadence
- **Touch 1**: immediate (within 60 seconds of opt-in). Email + SMS together.
- **Touch 2**: 18 hours after opt-in. Email + SMS together.
- **Touch 3**: 36 hours after opt-in. Email + SMS together.
- **Touch 4**: day 6 from opt-in (24h before credit expiry). SMS only.

### Skip rules
- **All touches after the booking event**: if a booking is detected for the contact (matched by email or phone) at any point in the sequence, skip all remaining touches.
- **Touch 4**: skip if a booking is detected before the day-6 trigger fires.

### Trigger sequence
- **Touch 1 (Email + SMS)** fires immediately on popup submission.
- **Touch 2 (Email + SMS)** fires 18 hours after opt-in.
- **Touch 3 (Email + SMS)** fires 36 hours after opt-in.
- **Touch 4 (SMS only)** fires day 6 after opt-in.

### Edge cases
- **Email-only opt-in (no phone provided)**: all SMS touches skipped automatically; email touches continue as scheduled.
- **SMS opt-out**: respect immediately. Email touches continue if email opt-in stands.
- **Touch 4 lands during off-hours**: schedule for daytime delivery (e.g., 9 AM – 7 PM local) to avoid late-night SMS friction.

---

## Dev Handoff

### Credit code mechanics
- Code: `HOST100`
- Discount: $100 off base rental
- Expiry: **7 days from opt-in** (date-stamped per contact)
- Application: at checkout on `/book`
- One-use per contact (prevent stacking with itself)

### Popup field validation
- Email and Phone: required
- Event type dropdown: required for personalization downstream (may drive future event-type-specific email branching)
- Name: required (used in every touch)

### Tour booking link
The "Book the tour for free online" CTA in Email 2 + SMS 2 should link to the website tour scheduler. See [[Tour-Sequence|Tour Sequence]] for the full tour flow that kicks off when a visitor books a tour.

### Tracking
- Popup conversion rate (% of popup views → submissions)
- Touch open rates (Emails 1–3)
- SMS click rates (Touches 1–4)
- Code redemption rate (% of opt-ins who redeem HOST100 at checkout)
- Time from opt-in to booking
- Touch attribution: which touch fired immediately before the booking event

### Calendar refresh process (Email 3 + SMS 3)
- "We're booked through the next month" is intentionally generic.
- **Option (stronger):** swap to "[Month]" + refresh the value monthly. Requires an ops process to update the live template at the start of each month.
- Keep generic if the ops process can't be reliably maintained — vague-but-true beats specific-but-stale.

### Future expansions to consider
- **Referral viral loop**: "Share your $100 with a friend, both get $50" — adds Marketing-Ideas #93 viral mechanics
- **Waitlist capture for sold-out dates**: if visitor's preferred date is unavailable, capture for a waitlist (Marketing-Ideas #79)
- **Touch 5 (lapsed re-engagement)**: 30 days after credit expiry, offer a new code at a reduced value (e.g., $50). Optional, only if open-rate data justifies it.
