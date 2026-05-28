---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Restructured 2026-05-28. Remote-guided tour model: visitor self-accesses the venue using a Tour Reservation # on the same /accesscode page used by booking customers; staff joins live on video call to walk them through the space. Two follow-up touches (email + SMS) after the tour."
owner: Luis
last_updated: 2026-05-28
sensitivity: internal
related_systems:
  - ghl
  - website
hub_role: leaf
---

# Tour Sequence

## Parent
- [[../Communication-Home|OEV Communication Home]]

## Related
- [[../OEV-Communication-Manual|OEV Communication Manual]]
- [[../../00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]]
- [[Post-Booking-Email-Sequence|Post-Booking Email + SMS Sequence]]
- [[../../05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]

## Purpose
Canonical tour sequence for the remote-guided tour model. Visitor books a tour through the website, receives a **Tour Reservation #** at booking, and uses that # on the same `/accesscode` page that booking customers use to retrieve the door code during their tour window. Staff joins the visitor live on a video call to walk them through the space. Two post-tour follow-ups (email + SMS each) close the loop.

## Design Principles
- **One access mechanism for the whole brand** — tour visitors and booking customers both use `/accesscode` with their respective reservation #. Customers learn the page once.
- **Self-access + live guidance** — no staff travel required, but the visitor still gets a guided walkthrough through the video call. Best of both worlds.
- **Peak-End Rule** — first touch (Step 01) and last follow-up (Step 06) carry the most memory weight. Both warmth-first.
- **Cognitive Load (Hick's Law)** — pre-tour reminders are short and single-job. Step 05 follow-up email is recap + CTA; pricing detail trimmed to discounts only (full pricing on the website).
- **Personal Luis voice on close-in execution + follow-ups** — Steps 02–07 signed with Luis to lift trust during execution and decision moments.
- **BAMFAM** — every post-tour message offers two clear paths: reserve directly, or reply/call to talk.

## Channel Matrix
| # | Step | Email | SMS | Trigger |
|---|---|---|---|---|
| 01 | Tour Confirmed + Access Instructions | ✅ | — | Tour booking received |
| 02 | 24-Hour Reminder | ✅ | ✅ | 24 hours before tour |
| 03 | 1-Hour Reminder | — | ✅ | 1 hour before tour |
| 04 | Internal Admin Reminder | — | ✅ *(internal)* | 1 hour before tour |
| 05 | Tour Follow-up #1 — Recap + Pricing | ✅ | ✅ | 2 hours after tour ends |
| 06 | Tour Follow-up #2 — Check-in | ✅ | ✅ | Day 5 *(skip if booked)* |

**Volume:** 3 emails + 4 SMS external + 1 internal.

## Variables Used
- `{{first_name}}` / `{{last_name}}` / `{{phone}}` / `{{email}}`
- `{{tour_reservation_number}}` — assigned at booking, format `TOUR-XXXX` (4-char alphanumeric)
- `{{tour_date}}` / `{{tour_time}}`
- `{{tour_video_link}}` — populated from the booking tool / video platform

## Standard References
- Public access page (door code lookup, dual-use): `https://orlandoeventvenue.org/accesscode`
- Booking URL: `https://orlandoeventvenue.org/book`
- Tour booking URL: `https://orlandoeventvenue.org/tour` *(if separate from /book)*

## Signature Block (every external email)
```
Luis & the Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr, Orlando, FL 32803
```

## SMS Signoff Convention
- Steps 02 + 05 SMS: ` — Luis & the OEV Team`
- Steps 03 + 06 SMS (close-in execution + final follow-up): ` — Luis`

---

## 01 — Tour Confirmed + Access Instructions — Email

**Subject:** Tour Confirmed for {{tour_date}} | Orlando Event Venue
**Preview:** Your remote-guided tour is on the calendar. Here's how it works.

```
Hi {{first_name}},

Welcome to Orlando Event Venue. Your tour is on the calendar — looking forward to walking you through the space.

Here's the deal: this is a self-access tour with a live video walkthrough. You'll let yourself into the venue using our access page (same one our booking customers use), and we'll be on a video call with you the whole time to guide you through everything, answer questions, and show you the corners you want to see.

Save this email. It's the one place where everything you need lives: tour reservation #, access page, video call link, and entry steps.

Your Tour
Tour Reservation #: {{tour_reservation_number}}
Date: {{tour_date}}
Time: {{tour_time}}
Location: Orlando Event Venue — 3847 E Colonial Dr, Orlando, FL 32803

Your Access Page (same one our booking customers use)
https://orlandoeventvenue.org/accesscode

Enter your Tour Reservation # on the page:
{{tour_reservation_number}}

The page shows your door code during your tour window. We'll text you the access page link again 24 hours before and 1 hour before your tour.

Your Video Call Link
{{tour_video_link}}

(Add the tour to your calendar so you don't miss it.)

How It Works
1. Arrive at the venue at {{tour_time}}.
2. Pull your door code from the access page above using your Tour Reservation #.
3. Let yourself in using the entry steps below.
4. Once you're inside, jump on the video call — we'll take it from there and walk you through the space live (~15–20 min).

Entry Steps (once you have the code from the access page)
1. Arrive at Colonial Town Center and look for the GLOBAL sign with 3847 displayed.
2. Facing the GLOBAL sign, go to the door on the left side of the building.
3. Find the black lockbox with the touchscreen keypad.
4. Tap the screen to wake it, then enter the code from the access page.
5. Open the lockbox and retrieve the magnetic key.
6. Tap the magnetic key on the sensor on the right side of the door.
7. Return the key to the lockbox immediately and close it.
8. Inside, locate the remote labeled "Light" on the left wall — left-side buttons turn lights on.

Quick Things to Know
- We're a local non-profit venue, set up for events up to 90 guests
- Catering is wide open — bring any caterer you want
- Free parking on-site (Colonial Town Center plaza, 200+ spots)
- All alcohol runs through our bar service if your event needs it

Need to reschedule? Reply to this email or call/text 407-974-5979.

Looking forward to it,

Luis with the Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr, Orlando, FL 32803
```

> **Dev note:** include an `.ics` calendar attachment so the tour auto-adds to the visitor's calendar. Reduces no-shows materially.

---

## 02 — 24-Hour Reminder — Email + SMS

### Email
**Subject:** Your Tour Is Tomorrow at {{tour_time}} | Orlando Event Venue
**Preview:** Access page + video link + quick reminder of how it works.

```
Hi {{first_name}},

Quick reminder — your tour at Orlando Event Venue is tomorrow at {{tour_time}}.

Tour Reservation #: {{tour_reservation_number}}
Time: {{tour_time}}
Location: 3847 E Colonial Dr, Orlando, FL 32803

How It Works
You'll let yourself into the venue using our access page, then hop on the video call so we can walk you through it.

Your Access Page (pull your door code here):
https://orlandoeventvenue.org/accesscode
(Enter Tour Reservation #: {{tour_reservation_number}})

Your Video Call Link:
{{tour_video_link}}

How to Find the Venue
Park in Colonial Town Center plaza (free, 200+ spots). Look for the GLOBAL sign with 3847 displayed. The venue entrance is the door on the left side of the building.

See you tomorrow,

Luis & the Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
3847 E Colonial Dr, Orlando, FL 32803
```

### SMS
```
Hi {{first_name}} — your OEV tour is tomorrow at {{tour_time}}. Pull your door code: https://orlandoeventvenue.org/accesscode (Tour Res #{{tour_reservation_number}}). Then join the call: {{tour_video_link}}. — Luis & the OEV Team
```

---

## 03 — 1-Hour Reminder — SMS

```
Hi {{first_name}} — your OEV tour starts in 1 hour. Door code: https://orlandoeventvenue.org/accesscode (Tour Res #{{tour_reservation_number}}). Once you're in, jump on the call: {{tour_video_link}}. — Luis
```

---

## 04 — Internal Admin Reminder — SMS *(internal)*

```
OEV remote tour — starts in 1 hour

Name: {{first_name}} {{last_name}}
Time: {{tour_time}}
Tour Res #: {{tour_reservation_number}}
Phone: {{phone}}
Email: {{email}}
Video call link: {{tour_video_link}}

Be camera-ready on the call at {{tour_time}}. Guest will let themselves in and join the video call from inside the venue.
```

---

## 05 — Tour Follow-up #1 — Email + SMS (2h after tour ends)

### Email
**Subject:** Thanks for touring OEV — next steps + full pricing
**Preview:** Quick recap, all-in pricing, and the simplest path to lock your date.

```
Hi {{first_name}},

Thanks for touring today! Great walking you through it.

A quick recap of what's available:

What's included with every rental
- Up to 90 guests + 10 tables + 90 chairs
- Prep kitchen for caterers (zero restrictions — bring any caterer)
- Free parking — 200+ spots in Colonial Town Center plaza
- Wall-sized LED stage screen + AV available via package
- Bar service available through us if your event needs it

Discounts you may qualify for
- 2–3 day workshop: 25% off base rental
- Non-profit weekday booking: 50% off base rental
- Non-profit weekend booking: cleaning fee waived

Two ways forward:

1. Reserve your date directly: https://orlandoeventvenue.org/book — 50% holds the date.
2. Call or text me at 407-974-5979 if you want to talk through specifics.

Open dates are being taken — if you have a date in mind, this is the right window to lock it in.

Luis & the Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803
```

### SMS
```
Hi {{first_name}} — Luis at OEV. Thanks for touring today! Just emailed you a quick recap + discounts. If you have a date in mind, lock it here: https://orlandoeventvenue.org/book — Luis
```

> **Note:** the full pricing list (hourly $139/hr, daily $899, production package per-hour rates, bar service per-guest rates) was intentionally trimmed from this email. Discounts stay; full pricing lives on the website. If you want a one-liner like *"Full pricing: orlandoeventvenue.org/pricing"* added, slot it under "Discounts you may qualify for."

---

## 06 — Tour Follow-up #2 — Email + SMS (Day 5, skip if booked)

### Email
**Subject:** Quick check-in from Luis | Orlando Event Venue
**Preview:** Any questions after your tour? Calendar update + the simplest path forward.

```
Hi {{first_name}},

Just checking in — wanted to see if you had any questions after your tour with us earlier this week.

A real calendar note: open dates are filling. If you have a date in mind, this is the right window to lock it in.

Two ways forward:

1. Reserve your date directly: https://orlandoeventvenue.org/book — 50% holds the date.
2. Reply to this email or call/text 407-974-5979 if you want to talk through anything.

If timing isn't right yet, no pressure — we'll be here when it is.

Luis & the Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803
```

### SMS
```
Hi {{first_name}} — Luis at OEV. Quick check-in: still considering the venue? Happy to answer any questions. If your date's still open, lock it here: https://orlandoeventvenue.org/book — Luis
```

> **Trigger:** Day 5 after the tour. **Skip both email + SMS if a booking is detected** before this trigger fires.

---

## Operational Rules

### Information delivery rules
- **Tour Reservation #** is the key identifier — surfaced in every external message + every email signature.
- **Access page link** is introduced in Step 01 email and repeated in Steps 02 (email + SMS) and 03 (SMS).
- **Entry steps** live in Step 01 email only. SMS reminders never re-walk entry steps.
- **Video call link** appears in Step 01, 02 (email + SMS), 03 (SMS), and 04 (internal). Not needed in post-tour follow-ups.
- **Calendar attachment (.ics)** must accompany Step 01 email.

### SMS signoff rules
- Steps 02 + 05 SMS: `— Luis & the OEV Team`
- Steps 03 + 06 SMS (close-in execution + final follow-up): `— Luis`

### Trigger sequence
- **Step 01** fires immediately on tour booking (website event).
- **Step 02** fires 24 hours before tour (email + SMS together).
- **Step 03** fires 1 hour before tour (customer SMS).
- **Step 04** fires 1 hour before tour (staff SMS, internal).
- **Step 05** fires 2 hours after tour ends (email + SMS together).
- **Step 06** fires Day 5 after tour, **skip if booking detected** in the meantime.

### Edge cases
- **No-show:** if the visitor doesn't join the video call within 10 minutes of tour start, staff should manually flag and reach out to reschedule. (Future automation: a "Sorry we missed you — reschedule here" email triggered automatically.)
- **Tour booking < 24 hours out:** Step 02 still fires immediately; Step 03 fires 1h before normally.
- **Visitor reschedules:** all upcoming touchpoints regenerate against the new tour datetime.
- **Visitor books a venue date during the tour itself:** Steps 05 + 06 should still fire — Step 05 as a thank-you/confirmation, Step 06 skipped by the booking-detected rule.

### Rules + fees source
If asked about venue rules or fees during a tour or in Step 05 follow-up, reconcile to [[../../00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]].

---

## Dev Handoff

### `/accesscode` page now supports 3 modes
Gated by identifier type + timing:

| Identifier | When | Shows |
|---|---|---|
| Booking reservation # | current time ≤ event-end | Door code + Wi-Fi |
| Booking reservation # | current time > event-end | Guest Report + review |
| **Tour reservation #** | within tour window (±30 min) | **Door code only** *(no Wi-Fi — short visit)* |
| Tour reservation # | outside window | "Tour not active" message + phone fallback (407-974-5979) |

### Tour Reservation # format
Suggest `TOUR-XXXX` (4-char alphanumeric) to distinguish from booking reservation #s. Generated at the moment the visitor books a tour.

### Video call platform
Pick one (Zoom, Google Meet, Whereby — all work). `{{tour_video_link}}` populates from the booking tool.

### Calendar attachment
Step 01 email must include an `.ics` attachment so the tour auto-adds to the visitor's calendar. Reduces no-shows materially.

### Tour booking source
Assumes tours are booked from the website's tour scheduler. Each tour booking generates a unique Tour Reservation # at the moment of booking.

### Skip rule for Step 06
If a venue booking (not tour booking) is detected for the contact between Step 05 and the Day 5 trigger, skip Step 06 entirely (both email + SMS).
