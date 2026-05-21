---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-4977 (Developer/OEV/EMAILS WEBSITE) page 8cqnrff-11737 (POP UPS)"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# OEV Pop-Up Lead Magnet — $100 Booking Credit Sequence

## Parent
- [[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home|OEV Communication Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/06-DNA/Lead|OEV Lead]]
- [[01-Brands/Orlando-Event-Venue/06-DNA/Conversion|OEV Conversion]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Booking-Calendar-Sequence|Booking Calendar Sequence]]

## Purpose

Website pop-up + 3-step email/SMS nurture for unbooked leads. Trigger: visitor enters Name + Email + Phone + Preferred Event Date via website pop-up. Code: **SAVE100** ($100 off base rental).

## Pop-Up Form

**Headline:** Get a **$100 Event Booking Credit**

**Subheadline:** Still planning your event? Enter your info and we'll send your **$100 Event Booking Credit** instantly by email and text so you can apply it when you reserve your date.

**Fields:**
- Name
- Email
- Phone Number
- Preferred Event Date

**Consent copy:** [Keep existing compliance language]

**Button:** **Send My $100 Credit**

**Confirmation screen:**
> ### Check Your Email
> Your **$100 Event Booking Credit** has been sent to **[email]**.

**Support line:** Questions? Call or text **407-974-5979**

## Email 1 — Immediate Delivery

**Subject:** Your $100 Event Booking Credit Is Here | Orlando Event Venue

> Hi [First Name],
>
> As promised, here is your **$100 Event Booking Credit** for Orlando Event Venue.
>
> ──────────────────────
> **Your Booking Credit Code**
> **SAVE100**
> $100 off your base rental
> ──────────────────────
>
> You can apply this credit when you reserve your event date.
>
> If you already know your date, the next step is simple:
>
> **Reserve your venue here:**
> https://orlandoeventvenue.org/book
>
> We can't hold dates without a reservation, so if you have a date in mind, reserve it now and apply your credit at booking.
>
> Orlando Event Venue Team
> 407-974-5979
> orlandoeventvenue.org
> orlandoeventvenue@gmail.com
> 3847 E Colonial Dr Orlando, FL 32803

## SMS 1 — Immediate

> Hi `{{First Name}}` — this is Orlando Event Venue 👋
> Your **$100 Event Booking Credit** is ready.
> Code: **SAVE100**
> If you already know your date, reserve here and apply your credit at booking:
> https://orlandoeventvenue.org/book
> We can't hold dates without a reservation.

## Email 2 — 18h Reminder

**Subject:** Reserve Your Date + Use Your $100 Booking Credit | Orlando Event Venue

> Hi [First Name],
>
> We noticed you haven't reserved your date yet.
>
> Your **$100 Event Booking Credit** is still available, and if you already have a date in mind, the best next step is to book now.
>
> ──────────────────────
> **Your Booking Credit Code**
> **SAVE100**
> $100 off your base rental
> ──────────────────────
>
> We can't hold dates without a reservation, and our calendar continues to fill.
>
> **Reserve your date here:**
> https://orlandoeventvenue.org/book
>
> If you're ready to move forward, reserve now and apply your credit at booking.

## SMS 2 — 18h

> Quick reminder `{{First Name}}` — your **$100 Event Booking Credit** is still available.
> If you already know your date, reserve now and apply your credit at booking:
> https://orlandoeventvenue.org/book

## Email 3 — 30h Final Reminder

**Subject:** Final Reminder: Reserve Your Date + Apply Your $100 Credit | Orlando Event Venue

> Hi [First Name],
>
> This is your final reminder to reserve your date and apply your **$100 Event Booking Credit** at booking.
>
> ──────────────────────
> **Your Booking Credit Code**
> **SAVE100**
> $100 off your base rental
> ──────────────────────
>
> If you're ready to move forward, reserve your event date now:
> https://orlandoeventvenue.org/book
>
> If you already have your date in mind, don't wait. We can't hold dates without a reservation.

## SMS 3 — 30h

> Last reminder `{{First Name}}` — reserve your date now and apply your **$100 Event Booking Credit**.
> Code: **SAVE100**
> Reserve here:
> https://orlandoeventvenue.org/book

## Sequence cadence

| Touch | Channel | Timing |
|---|---|---|
| Pop-up form fill | Web | T+0 (lead capture) |
| Email 1 | Email | T+0 (immediate) |
| SMS 1 | SMS | T+0 (immediate) |
| Email 2 | Email | T+18h |
| SMS 2 | SMS | T+18h |
| Email 3 | Email | T+30h |
| SMS 3 | SMS | T+30h |

## Code rules

- Code: **SAVE100**
- Applies to: base rental only (not cleaning, add-ons, or production packages)
- Stacking: cannot combine with referral partner discount or other promo codes
- Validity: must be applied at booking checkout, not post-reservation
