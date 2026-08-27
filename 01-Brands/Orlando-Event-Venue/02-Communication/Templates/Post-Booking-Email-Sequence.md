---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Restructured 2026-05-27. Guest Report flow consolidated onto the /accesscode page — same link serves door code + Wi-Fi pre-event, and Guest Report + review post-event. Standalone post-event SMS eliminated. 2026-06-18: merged the standalone review reminder (old Step 08) into the 1-hour reminder (Step 07) — the final SMS now carries access link + Guest Report pointer + review seed in one touch. Sequence is now 7 steps."
owner: Luis
last_updated: 2026-06-18
sensitivity: internal
related_systems:
  - ghl
  - website
hub_role: leaf
---

# Post-Booking Email + SMS Sequence

## Parent
- [[../Communication-Home|OEV Communication Home]]

## Related
- [[../OEV-Communication-Manual|OEV Communication Manual]]
- [[../../00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]]
- [[../../06-DNA/Fulfillment|OEV Fulfillment]]
- [[../../06-DNA/Conversion|OEV Conversion]]
- [[../../05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]

## Purpose
Canonical post-booking sequence. Email is reserved for records, payment links, and access instructions. SMS handles reminders and personal touchpoints. **The `/accesscode` page is dual-purpose**: before/during the event it serves the door code + Wi-Fi; after the event it serves the Guest Report + review prompt. The customer enters their reservation number on the same page either way. No standalone post-event SMS is needed for checkout, Guest Report, or review collection. **The review ask is folded into the 1-hour reminder (Step 07)** as a seed — "during your event, grab a few photos; afterward, post them on Google with a quick review" — so the sequence ends on a single, high-attention SMS rather than a separate post-event nudge. The sequence is 7 steps.

## Design Principles Applied
- **One page, one identifier (reservation #)** — reduces cognitive load and friction. Customer learns the page once, uses it for everything.
- **Peak-End Rule** — first touch (Step 01) and last touch (Step 07, fired at the highest-attention moment) carry the most memory weight. Both warmth-first.
- **Reciprocity** — Step 07 explains *why* the review helps them ("helps planners like you find us").
- **Loss Aversion** — Step 02 frames remaining payment as protecting the date they own.
- **Cognitive Load (Hick's Law)** — Step 03 chunked. Eliminated the multi-job post-event SMS in favor of self-serve on the access page; folded the review ask into Step 07 so the sequence ends on one SMS, not two.
- **Personal signoff close-in** — Steps 06 + 07 sign with a real name (Luis).
- **Marketing-machine seeds** — Step 07 carries the photo + review seed; access page collects photos with permission flag via Guest Report; the review link itself is the social-proof asset.

## Channel Matrix
| # | Step | Email | SMS | PDF Invoice (dev) | Trigger |
|---|---|---|---|---|---|
| 01 | 50% Received + Booking Under Review | ✅ | — | ✅ | Website event: 50% payment received |
| 02 | Remaining 50% Due | ✅ | ✅ | — | 15 days before event date |
| 03 | Fully Paid + Access Instructions | ✅ | — | ✅ | Website event: final payment received |
| 04 | 30-Day Check-in | ✅ | — | — | 30 days before event date |
| 05 | 7-Day Check-in | — | ✅ | — | 7 days before event date |
| 06 | 1-Day Access Reminder | — | ✅ | — | 1 day before event date |
| 07 | 1-Hour Reminder + Review Seed | — | ✅ | — | 1 hour before event start time |

**Volume:** 4 emails + 4 SMS.

## Variables Used
- `{{contact.first_name}}` / `{{contact.full_name}}`
- `{{contact.oev_reservation_number}}`
- `{{contact.oev_event_type}}`
- `{{contact.oev_event_date}}`
- `{{contact.oev_booking_type}}`
- `{{contact.oev_number_of_guests}}`
- `{{contact.oev_balance_amount}}`
- `{{contact.oev_balance_link_expires_at}}`
- `{{contact.oev_balance_payment_url}}`
- Website-side: `${firstName}`, `${booking.*}`, `${formattedDate}`, `${timeRange}`, etc.

## Standard References
- **Access page** (dual-purpose, entered via reservation #): `https://orlandoeventvenue.org/accesscode`
  - Before/during event: door code + Wi-Fi
  - After event: Guest Report form + review link
- Review URL (direct, also lives on the access page): `https://g.page/r/CU-yUA0El90UEAE/review`
- Canonical rules + fees: [[../../00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]]

## Signature Block (every email)
```
Reservation #: {{contact.oev_reservation_number}}
Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803
```

## SMS Signoff Convention
- **Steps 02 / 05:** ` — Orlando Event Venue Team`
- **Steps 06 + 07 (close-in execution):** ` — Luis & the OEV Team` — personal trust lift at execution moments.

---

## 01 — 50% Received + Booking Under Review — Email

**Subject:** 50% Received | Orlando Event Venue
**Preview:** We've got your 50%. Your date is being held — we'll confirm within 24 hours.

```
Hi {{contact.first_name}},

Welcome to Orlando Event Venue. We've got your 50% — your date is being held.

Here's the deal: we'll review your booking details (timing, capacity, venue readiness) and confirm within about 24 hours. Hold off on invitations until we confirm — saves trouble if anything needs to shift.

Save this email. It's the one place where everything you need before event day lives: reservation #, payment timeline, day-of rules, and what to expect. From here on, most reminders arrive as short texts. Email stays for receipts, your payment link, and your access instructions.

Your Booking
Reservation #: {{contact.oev_reservation_number}}
Event Type: {{contact.oev_event_type}}
Date: {{contact.oev_event_date}}
Guest Count: {{contact.oev_number_of_guests}}
Booking Type: {{contact.oev_booking_type}}

What's Included
- Up to 90 guests
- 10 tables + 90 chairs
- Prep kitchen (staging + re-heating only — no on-site cooking)
- 2 bathrooms
- Free parking

Catering
Zero restrictions — bring any caterer you want. Professional caterers must show proof of liability insurance.

Bar Service
All alcohol service runs through us. Packages and add-ons are on our website.

Wi-Fi
Wi-Fi credentials will be on your access page along with your door code on event day — both update together.

Payment Timeline
Your remaining 50% is due 15 days before your event. We'll send a secure payment link by email with a short text reminder. Your full access instructions arrive with that final-payment email.

Your Agreement at a Glance
By booking, you agree to these terms. We share them up front so there are no surprises. Cameras and noise sensors monitor the event; severe violations may terminate the event without refund.

- Maximum 90 guests: $500. Local authorities may shut down the event.
- Setup + breakdown = 50% of your booked time, combined. Overtime: $350/hour + $300 cleaning if not restored.
- All alcohol through our bar service. No outside alcohol, no outside bartenders, no BYOB. Guests 21+ to consume: $500 + possible termination without refund.
- No drugs: $500 + immediate termination. Law enforcement may be notified.
- No smoking or vaping indoors or in the immediate outdoor surroundings: $500 cleaning/deodorizing.
- No pets (service animals welcome with documentation): $250 cleaning.
- No on-site cooking (prep kitchen is for staging + re-heating). Outside caterers must show proof of liability insurance: $500 for unauthorized cooking or unapproved caterers.
- No glitter, confetti, rice, or sparklers: $500 cleaning.
- Music + noise within local ordinances. Doors closed after 9 PM: $350 + possible termination if severe.
- No nails, staples, residue tape, or open flames unless pre-approved. Stage/screens/AV require the matching production add-on: $400 per violation.
- Damage to venue, furniture, or equipment: repair/replacement at cost, $400 minimum.
- Tables + chairs must be restored to original layout: $400 if not restored.

If guest count, timing, or event needs change, just reply to this email and we'll update your booking.

Reservation #: {{contact.oev_reservation_number}}
Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803
```

> **Dev only (not customer-facing):** automation must generate and attach a PDF invoice for the first 50% payment. Don't mention in the email body.

---

## 02 — Remaining 50% Due — Email + SMS

### Email
**Subject:** Remaining 50% Due | Orlando Event Venue
**Preview:** Your date stays held when this payment lands. Secure payment link below.

```
Hi {{contact.first_name}},

Quick reminder — the remaining 50% for your event is now due. Your date stays held when this payment lands.

Amount Due: {{contact.oev_balance_amount}}
Payment Link Expires: {{contact.oev_balance_link_expires_at}}

Pay Securely Here
{{contact.oev_balance_payment_url}}

Once payment is in, your booking updates automatically and you'll receive your final receipt along with your access instructions for event day. If you've already paid, you're all set.

Reply here or call 407-974-5979 if anything looks off.

Reservation #: {{contact.oev_reservation_number}}
Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803
```

### SMS
```
Hi {{contact.first_name}} — your remaining 50% for Orlando Event Venue is due. Paying secures your date. Link is in your email. Reply here if you need help. — Orlando Event Venue Team
```

---

## 03 — Fully Paid + Access Instructions — Email

**Subject:** You're Set — Access Instructions for Event Day | Orlando Event Venue
**Preview:** Fully paid. Here's how access works on event day — and what to do after.

```
Hi ${firstName},

You're set. Final payment is in, your booking at Orlando Event Venue is fully paid, and we're looking forward to hosting you.

Payment Received: ${formatCurrency(booking.amount_paid)}

Your Booking
Reservation #: ${booking.reservation_number}
Event Date: ${formattedDate}
Event Time: ${timeRange}
Booking Type: ${formattedBookingType}
Guests: ${booking.number_of_guests}
Event Type: ${booking.event_type}

Payment Summary
Total: ${formatCurrency(booking.total_amount)}
First 50%: ${formatCurrency(booking.deposit_amount)}
Second 50%: ${formatCurrency(booking.balance_amount)}
Status: Fully Paid

Your Access Page (one link, used before and after the event)
https://orlandoeventvenue.org/accesscode

Enter your reservation number on the page:
${booking.reservation_number}

- Before / during your event: the page shows your live door code + Wi-Fi. The code rotates per booking.
- After your event ends: the same page becomes your Guest Report (2 min — photos of the venue) and your review link.

The day before your event you'll get a short text with the access link, and again 1 hour before.

Entry Steps (once you have the code from the access page)
1. Arrive at Colonial Town Center and look for the GLOBAL sign with 3847 displayed.
2. Facing the GLOBAL sign, go to the door on the left side of the building.
3. Find the black lockbox with the touchscreen keypad.
4. Tap the screen to wake it, then enter the code from the access page.
5. Open the lockbox and retrieve the magnetic key.
6. Tap the magnetic key on the sensor on the right side of the door.
7. Return the key to the lockbox immediately and close it.
8. Inside, locate the remote labeled "Light" on the left wall — left-side buttons turn lights on. Return the remote when done.

Before You Leave
- Turn off all lights (right-side buttons on the light pad).
- Place all trash bags on the back patio. No trash inside.
- Restore tables and chairs to the original layout.
- Take all personal items with you.
- Lock the door securely.

After You Leave
Head back to the same access page — once your booking ends, it switches to show the Guest Report (a quick photo walkthrough so we can close out your reservation) and a quick review link. Same URL, same reservation number:
https://orlandoeventvenue.org/accesscode

If your event went well, a 60-second Google review helps other planners find us — thank you in advance.

If anything needs to change before event day, reply here.

Reservation #: ${booking.reservation_number}
Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803

Please keep this email for your records.
```

> **Dev only (not customer-facing):** automation must generate and attach a PDF invoice for the final 50% payment. Don't mention in the email body.
>
> Code variables `booking.deposit_amount` / `booking.balance_amount` stay as-is. Only customer-facing labels say "First 50%" / "Second 50%" per the OEV language rule against "deposit" wording.

---

## 04 — 30-Day Check-in — Email

**Subject:** 30 Days Until Your Event | Orlando Event Venue
**Preview:** Quick check-in — most events at this stage are finalizing a few details.

```
Hi {{contact.first_name}},

Your event at Orlando Event Venue is 30 days out.

Most events at this stage are confirming final headcount, catering, and any AV needs. If anything has shifted on your end — guest count, timing, add-ons — reply here and we'll update your booking before event week.

Your Booking
Reservation #: {{contact.oev_reservation_number}}
Date: {{contact.oev_event_date}}
Guests: {{contact.oev_number_of_guests}}

What's Coming
- 15 days before your event: secure payment link for the remaining 50%, plus your full access instructions emailed the moment payment is in.
- 7 days before: short text check-in.
- 1 day before + 1 hour before: short text reminders with your access link.
- After your event: the same access link becomes your Guest Report + review page. Use your reservation number to enter.

Reservation #: {{contact.oev_reservation_number}}
Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803
```

> **Dev option for richer personalization:** branch the "Most events at this stage..." line by `{{contact.oev_event_type}}`:
> - Workshop / training: *"Most workshops at this stage are finalizing AV setup and catering windows."*
> - Corporate / conference / meeting: *"Most corporate events at this stage are confirming headcount and AV requirements."*
> - Birthday / party / celebration: *"Most celebrations at this stage are finalizing catering and guest count."*
> - Default: *"Most events at this stage are confirming final headcount, catering, and any AV needs."*

---

## 05 — 7-Day Check-in — SMS

```
Hi {{contact.first_name}} — 7 days out. Final headcount confirmed? Caterer locked in? Reply with any updates. Day before, we'll text the access code link. Reservation #{{contact.oev_reservation_number}}. — Orlando Event Venue Team
```

---

## 06 — 1-Day Access Reminder — SMS

```
Hi {{contact.first_name}} — tomorrow's the day. Your door code + Wi-Fi will be here on arrival: https://orlandoeventvenue.org/accesscode (enter reservation #{{contact.oev_reservation_number}}). Same link becomes your Guest Report + review after the event. Reply if you need anything. — Luis & the OEV Team
```

---

## 07 — 1-Hour Reminder + Review Seed — SMS

```
Hi {{contact.first_name}} — it's almost time! Your door code + Wi-Fi are here: https://orlandoeventvenue.org/accesscode (enter reservation #{{contact.oev_reservation_number}}) — same link becomes your quick Guest Report after the event. Grab a few photos while you're celebrating; posting them on Google with a 60-second review helps planners like you find us: https://g.page/r/CU-yUA0El90UEAE/review — Luis & the OEV Team
```

> **Trigger:** 1 hour before event start time. This is the final SMS in the sequence — it does three jobs in one touch: (1) points to the access page for the live door code + Wi-Fi, (2) flags that the same link flips to the Guest Report after the event, and (3) plants the photo + review seed at the highest-attention moment. The review link goes out here once; there is no separate post-event review SMS.
>
> **Note (operator tradeoff):** the review link is now delivered *before* the event rather than 24h after. This trades the better-timed post-event ask for a leaner sequence and a single high-attention send. If review volume drops, the fastest recovery is re-adding a lightweight post-event SMS (old Step 08) or letting the access page's post-event Guest Report mode carry the review prompt on its own.

---

## Operational Rules

### Information delivery rules
- **Reservation number**: in every email body **and** every email signature footer; embedded in every SMS that requires the access lookup (Steps 05–07).
- **Access page (`/accesscode`)** is dual-purpose:
  - Pre-event / during-event: serves door code + Wi-Fi (gated by reservation #).
  - Post-event: serves Guest Report form + review link (gated by reservation #).
  - The website determines mode by current time vs. event-end time.
- **Wi-Fi credentials**: live only on the access page (rotate with door code). Never sent in email or SMS.
- **Door code**: never sent in any email or SMS. Lives only on the access page.
- **Guest Report**: not collected via SMS or email. Self-serve on the access page after the event.
- **Checkout steps (lights, trash, tables, lock)**: live in Step 03 email under "Before You Leave." Also surfaced on the access page so the customer can pull them up on their phone if needed.

### SMS signoff rules
- Standard signoff: ` — Orlando Event Venue Team`
- **Close-in execution moments (Steps 06 + 07):** use ` — Luis & the OEV Team`.

### PDF invoice rules (developer instructions only)
- **Step 01 email**: PDF invoice attached for the first 50% payment.
- **Step 03 email**: PDF invoice attached for the final 50% payment.
- PDF includes: reservation #, event date, line-item breakdown, payment amount, total + balance remaining.
- **Not mentioned in customer-facing email copy.**
- Step 02 does **not** include a PDF — it's a payment-link email, not a payment-receipt email.

### Trigger sequence
- Step 01 fires immediately on 50% payment (website event).
- Step 02 fires 15 days before event date (email + SMS pair fire together).
- Step 03 fires on final payment (website event), with full access instructions including the post-event Guest Report flow.
- Step 04 fires 30 days before event date.
- Step 05 fires 7 days before event date.
- Step 06 fires 1 day before event date.
- **Step 07 fires 1 hour before event start time** — final SMS. Carries access link + Guest Report pointer + review seed (with direct review link). No separate post-event review SMS fires.

### Marketing-machine integration
- **Step 07** — photo + review seed (the review link is delivered here, once).
- **Access page Guest Report** — photo collection with opt-in permission flag (dev needs to add checkbox to the report form on the page).
- **Access page review link + Step 07 review link** — social proof asset.

Bigger marketing-machine system (lifecycle ads, testimonial competition, social scrape) lives in [[../../06-DNA/Conversion|OEV Conversion DNA]] when scoped.

### Edge cases
- **Customer pays late (final payment within 30 days of event):** Step 03 still fires on payment with access instructions. If payment lands within 7 days, Step 03 is critical — it's the only email containing access info + the post-event Guest Report flow.
- **Customer pays final balance before 30-day mark:** they receive Step 03 first, then Step 04 (30-day check-in). Fine — the 30-day email doesn't repeat access info.
- **Admin QA after Step 01 finds an issue:** staff reaches out manually.
- **Bar package selected:** no special block needed in Step 01 — the rule (no outside alcohol) applies universally.
- **SMS bounce (no mobile on file):** fall back to email for that specific touchpoint and flag the contact for staff follow-up.
- **Customer never returns to access page post-event:** the review ask already went out in Step 07. Guest Report completion is tracked on the page; if uncompleted after a configurable threshold, staff can manually nudge.
- **No post-event review nudge:** by design, the review ask fires once (Step 07, pre-event). If a review hasn't landed within a set window after booking-end, the fallback is a manual staff nudge or re-introducing a post-event SMS — not an automated send in this version.

### Rules + fees source
Always reconcile to [[../../00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]] before changing the Step 01 "Your Agreement at a Glance" block. If a rule or fee changes, update Rules-and-Fees first, then this template.

### Dev handoff specific to this version
- **`/accesscode` page must support dual mode:**
  - Pre-event / during-event (current time ≤ event-end time): show door code + Wi-Fi.
  - Post-event (current time > event-end time): show Guest Report form (with photo permission checkbox) + Google review link.
  - Both modes gated by reservation number.
- **Guest Report form on the access page** should match the previous standalone Guest Report content (photo walkthrough of venue: door, main area, tables/chairs, bathrooms, kitchen + close-out checkboxes).
- **Tracking**: the page should record Guest Report completion timestamp, photo permission flag, and any review-click events so automations can skip redundant nudges.

---

## Scope Note — added 2026-08-26

This note is canonical for **sequence logic**: triggers, the channel matrix, information-delivery rules, edge cases, and dev handoff.

It is **no longer current for copy**. The email bodies transcribed above are the 2026-05-27 version. Subject lines, step numbering, and body text have moved since. Copy authority is now the ClickUp spec doc "OEV POST BOOKING COMMUNICATIONS" plus the live templates.

Rendering is a separate layer entirely. Every guest-facing email now renders through the shared design system, and the plain-text blocks above do not describe how anything looks:
- [[../Email-Design-System|OEV Email Design System]] — the rendering layer, its module vocabulary, and the rule that design carries emphasis while wording never changes
- [[GHL-Email-Templates|OEV GHL Email Templates]] — the five rebuilt GHL-side templates
- [[../../00-Brand-Core/Visual-Identity|OEV Visual Identity]] — logo package, color tokens, typography

**Open task:** reconcile the copy in this note against the ClickUp spec, or strip the copy blocks and leave this note purely as sequence logic.
