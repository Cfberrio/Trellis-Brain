---
title: OEV Website Policies v1
brand: Orlando Event Venue
owner: Luis Torres
last_updated: 2026-07-21
status: draft — not publishable until Decision Register is cleared
sensitivity: internal
used_for_ai: true
source_reference: "Rules-and-Fees.md, Payment-Rules.md, Pricing-Logic.md, Post-Booking-Email-Sequence.md, Voice-Agent-FAQ.md, 04-pricing-and-booking-scope.md"
---

# OEV Website Policies v1

Five documents for `orlandoeventvenue.org`. Everything grounded in existing OEV canon is written as final text. Everything not in canon is marked `[DECIDE — …]` and must be answered before publishing.

**Not legal advice.** These are operator-drafted templates built from OEV's own documented rules. Have counsel review before publishing, especially §Limitation of Liability, §Governing Law, and the alcohol clause.

**Publish at:** `/privacy` · `/terms` · `/booking-policy` · `/cookies` · plus on-form SMS copy at `/book` and the popup.

---

## DECISION REGISTER — clear these before publishing

### A. Hard blockers (cannot publish without an answer)

| # | Decision | Why it blocks | Recommended default |
|---|---|---|---|
| A1 | **Legal entity name + type + state** | Every policy names a contracting party. Vault has trade name only. Ministry parent entity is implied (`orlandoglobalministries@gmail.com`, "GlobalChurch" SSID) but never named. | Confirm from Sunbiz. If non-profit, state the 501(c)(3) name. |
| A2 | **Cancellation + refund terms** | `Refund-Rules.md` says outright: "Refund rules are not fully specified… should not be inferred casually." Voice agent currently dodges the question to customers. | Adopt the tiered schedule drafted in §3.6 below. |
| A3 | **Alcohol policy — pick ONE of four** | Canon contains: (a) in-house bar only, (b) licensed outside vendor + $250 vetting fee, (c) beer & wine only, (d) not allowed without written approval. All four are live in customer-facing assets. | Adopt (b) — newest (2026-07-01), most specific, explains the non-profit rationale. |
| A4 | **Governing law / venue / dispute resolution** | No clause exists anywhere. | Florida; Orange County. |
| A5 | **Mailing address for legal notice** | Only the venue address exists. | Use venue address unless a separate registered address exists. |

### B. Contradictions to reconcile (already reaching customers)

| # | Conflict | Where it hurts |
|---|---|---|
| B1 | Hourly rate **$139 vs $140** (+ $99 weekday promo) | Solved in this draft by never publishing a rate — checkout is the price of record. Still must be fixed in emails/scripts. |
| B2 | Overtime / late cleanup **$350/hr (canonical) vs $200/hr** | Two live customer emails still say $200. If a customer is billed $350 after receiving a $200 email, that is an unenforceable charge. **Fix templates before publishing the $350 figure.** |
| B3 | **"Doors closed after 9 PM" vs 24-hour daily rate vs a sold 9pm–2am booking** | Already caused a written customer dispute in which the client asked for a copy of the agreement — and no agreement exists. Highest-exposure item in the file. |
| B4 | Setup/breakdown fee: **$100 flat vs $199 flat vs $199 + $199** | Three values in canon. Not published here; resolve before quoting. |
| B5 | Basic A/V **$79 vs $89/hr** | Not published here; resolve before quoting. |
| B6 | Catering: **"zero restrictions"** vs COI required + no on-site cooking + $500 penalty | Both sentences sit in the same Step-01 email. §2.7 below reconciles them; confirm it's right. |
| B7 | Balance due **"15 days" vs "~2 weeks"** | §3.3 uses 15 days. Confirm. |
| B8 | The word **"deposit"** is banned by `Language-Rules.md` but used in live emails, the FAQ, and the voice agent | These policies use "first 50%" throughout, per the language rule. Templates still need fixing. |

### C. Not found — needs a business answer, not a lookup

No-show definition and fee · reschedule fee and window · renter-side event insurance requirement · security-guard trigger and price · minimum age to sign a reservation · CCTV footage retention period · published business hours · A2P 10DLC registration status · analytics/pixel inventory for the cookie policy.

### D. Compliance flags

- **D1 — Voice agent AI disclosure.** `Voice-Agent-Master-Prompt.md:32` instructs: "Do NOT mention you are an AI unless the caller directly asks." Combined with call recording and Whisper transcription, this is worth raising with counsel. §1.4 below discloses both; the script should match.
- **D2 — Cameras and noise sensors** monitor events and post-event review triggers penalties. This must be disclosed pre-booking, not only in a post-payment email. §1.5 and §2.9 do that.
- **D3 — "Your Agreement at a Glance" currently arrives *after* payment.** That is not enforceable acceptance. §2.1 makes the Terms a pre-checkout click-wrap. Dev change required.

---

# PAGE 1 — PRIVACY POLICY
**Publish at:** `/privacy`

**Orlando Event Venue Privacy Policy**
Last updated: [PUBLICATION DATE]

## 1.1 Introduction

`[DECIDE A1 — LEGAL ENTITY NAME]`, operating as Orlando Event Venue ("Orlando Event Venue," "we," "us," or "our"), respects your privacy. This Privacy Policy explains how we collect, use, share, and protect information when you visit orlandoeventvenue.org, request a tour, submit a reservation, contact us by phone, email, or text, or attend an event at our venue at 3847 E Colonial Dr, Orlando, FL 32803.

## 1.2 Information we collect

**You give us directly:**
- Name, email address, and phone number
- Event details: event type, requested date and time, guest count, setup needs, add-on selections
- Reservation number and billing details associated with your booking
- Photos and notes you submit through the post-event Guest Report
- Any information you include in messages, calls, or forms

**Collected automatically when you use the website:**
- IP address, browser and device type, referring source, pages viewed, and on-site activity, collected through cookies and analytics tools. See our Cookie Policy.

**Collected at the venue:**
- **Video from interior and entry cameras.** Cameras operate throughout your event and footage may be reviewed after the event to assess venue condition and policy compliance.
- **Sound level readings from noise sensors.** These record volume levels, not conversation content.

**Collected when you call us:**
- Calls may be recorded and transcribed for service quality, staff training, and reservation accuracy. Some inbound calls are handled by an automated voice assistant. You may ask to speak with a person at any time.

**We do not collect payment card numbers.** All payments are processed by Stripe on Stripe's systems. We receive confirmation of payment and the last digits of the card, not the full card number.

## 1.3 How we use information

- To respond to inquiries, schedule tours, and prepare quotes
- To process reservations, payments, and balance reminders
- To send confirmations, access instructions, reminders, and operational updates about your booking
- To send promotional messages, **only where you have separately agreed to receive them**
- To maintain venue safety, enforce the Venue Rules, and assess damage or policy violations
- To improve the website, our service, and staff training
- To meet legal obligations and resolve disputes

## 1.4 Automated calls, recording, and AI tools

We use automated systems to handle some phone calls, draft responses, and transcribe recordings. Automated systems assist our staff; final decisions about your reservation, charges, refunds, and disputes are made by a person. If you would prefer not to be handled by an automated assistant, tell us and we will route you to staff.

## 1.5 Cameras and monitoring at the venue

By booking an event, you acknowledge that the venue is monitored by interior and entry cameras and by noise sensors, and you agree to inform your guests and vendors of this. Footage and sensor data may be used to assess compliance with the Venue Rules, document damage, support or contest a fee, and cooperate with law enforcement where required. Recordings are retained for `[DECIDE — RETENTION PERIOD, e.g. 30 days]` unless retained longer for an open incident, dispute, or legal requirement.

## 1.6 Text messages (SMS)

If you provide a mobile number and affirmatively opt in, you agree to receive SMS or MMS messages from Orlando Event Venue about your reservation — confirmations, balance reminders, access instructions, and event-day reminders — and, where you separately opt in, promotional messages.

Message frequency varies. Message and data rates may apply. Reply **STOP** to opt out, **HELP** for help, or contact us at orlandoeventvenue@gmail.com or 407-974-5979. Consent to receive text messages is not a condition of booking.

**We do not sell or share your mobile number or SMS consent with third parties for their own marketing.**

## 1.7 Who we share information with

We share information with service providers who operate our business on our behalf, under contract and only for that purpose:

| Provider | Purpose |
|---|---|
| Stripe | Payment processing |
| GoHighLevel | CRM, booking records, email and SMS delivery |
| Website hosting and analytics providers | Site operation and performance |
| Bar service and approved outside vendors | Delivering the services you booked |

We may also disclose information where required by law, to enforce our Terms of Use or Venue Rules, to protect the safety of people or property, or in connection with a sale or transfer of the business.

**We do not sell your personal information.**

## 1.8 Data retention

We keep reservation records, payment records, and related communications for as long as needed to operate the venue, meet tax and accounting requirements, resolve disputes, and enforce our agreements. Camera footage and sensor data are retained per §1.5.

## 1.9 Your rights

Depending on where you live, you may have the right to request access to, correction of, or deletion of your personal information, and to opt out of certain uses. Florida residents may have rights under the Florida Digital Bill of Rights. Send requests to orlandoeventvenue@gmail.com. We will verify your identity before acting on a request.

## 1.10 Security

We use reasonable administrative, technical, and physical safeguards to protect personal information. No method of transmission or storage is completely secure, and we cannot guarantee absolute security.

## 1.11 Children

Our website and booking services are intended for adults. We do not knowingly collect personal information from children under 13 through the website.

## 1.12 Contact

Orlando Event Venue
3847 E Colonial Dr, Orlando, FL 32803
orlandoeventvenue@gmail.com · 407-974-5979
orlandoeventvenue.org

## 1.13 Updates

We may update this Privacy Policy. The updated version takes effect when posted with a new date.

---

# PAGE 2 — TERMS OF USE
**Publish at:** `/terms`

**Orlando Event Venue Terms of Use**
Last updated: [PUBLICATION DATE]

## 2.1 Acceptance

By using orlandoeventvenue.org, requesting a tour, submitting a reservation, or paying for a booking, you agree to these Terms of Use, the Booking, Cancellation & Refund Policy, the Venue Rules in §2.8, and the Privacy Policy.

**If you book on behalf of an organization, you confirm you are authorized to bind it.** The person who books is the responsible party for the reservation, including guest and vendor conduct and any fees assessed.

## 2.2 What we provide

Orlando Event Venue rents event space at 3847 E Colonial Dr, Orlando, FL 32803, with optional add-ons including audio/visual production, bar service, staffing, and photo/video coverage. Capacity is **90 guests maximum**.

## 2.3 Reservations are not confirmed until we confirm them

Submitting a request does not hold a date. **A date is held only when the first 50% payment is received.** We confirm reservations in writing, typically within 24 hours of payment.

We may decline, modify, or reschedule a request based on availability, operational limits, safety concerns, suspected fraud, or prior policy violations. If we decline after payment, you receive a full refund.

## 2.4 Pricing and payment

- Rates, fees, and add-on pricing are those displayed at checkout at the time of booking. **Checkout is the price of record.**
- A cleaning fee of **$199 per reservation** applies to all bookings.
- A card processing fee of **3.5%** applies at checkout.
- Payment is **50% to hold the date** and **50% before the event**, per §3.3.
- Discount codes apply to the base rental only — never to the cleaning fee, A/V, bar service, or other add-ons.
- Payment links expire in 24–48 hours. Ask us and we will resend one.
- All payments are processed online through Stripe. We do not accept payment by phone.
- **Multi-day events are booked as separate reservations, one per day, each with its own 50% to hold.**

## 2.5 Your booked time includes setup and breakdown

Your booked block covers everything: load-in, setup, the event itself, breakdown, and load-out. Plan on **setup and breakdown together consuming roughly half of a booked block**, with the event running in the remainder. If you need more time, book more time.

Staying past your booked end time is charged at **$350 per hour** `[BLOCKER B2 — live emails still say $200/hr; fix templates first]`.

## 2.6 Your responsibilities

You agree to:
- Provide accurate contact and event information
- Stay within the 90-guest maximum
- Follow the Venue Rules in §2.8 and inform your guests and vendors of them
- Restore tables and chairs to their original layout
- Complete checkout: turn off all lights, remove all personal items, place all trash bags on the back patio (not inside the venue), and lock the door
- Submit the post-event Guest Report, which closes out your reservation and documents venue condition

## 2.7 Catering and outside vendors

**You may use any caterer you want.** We do not require you to use a preferred vendor list for food.

Two conditions apply:
1. **Professional caterers must provide proof of liability insurance** and meet health and safety requirements.
2. **No on-site cooking.** The prep kitchen is for staging and re-heating only.

Pre-packaged and chain-restaurant food is fine.

## 2.8 Venue Rules and non-compliance fees

These rules are part of your reservation. Fees below are charged to the responsible party.

| Rule | Fee for non-compliance |
|---|---|
| Alcohol must be served by a licensed, vetted vendor. Our default vendor is Chara Mobile Bar. Using a different bartender requires approval and a **$250 administrative vetting fee**. Liquor must be picked up by the vendor, not delivered to the venue. No BYOB. Guests must be 21+ to consume. `[DECIDE A3]` | $500. Event may be terminated without refund if severe. |
| No drugs on the property. | $500 + immediate termination. Law enforcement may be notified. |
| No smoking or vaping indoors or in the immediate outdoor surroundings. | $500 cleaning/deodorizing. |
| No pets. Certified service animals are welcome with documentation. | $250 cleaning. |
| No on-site cooking. Outside caterers require proof of liability insurance. | $500. |
| No glitter, confetti, rice, or sparklers. | $500 cleaning. |
| Setup + breakdown must fit within your booked time. | Overtime $350/hour; $300 cleaning if the space is not restored. |
| Music and noise must stay within local ordinances. Doors closed after 9 PM. `[BLOCKER B3]` | $350. Event may be terminated without refund if severe. |
| Maximum occupancy: 90 guests. | $500. Local authorities may shut down the event. |
| No nails, staples, or residue-leaving tape. No open flames or candles unless pre-approved. Use of stage, screens, lighting, or A/V requires the matching production add-on. | $400 per violation. |
| You are liable for damage to the venue, furniture, or equipment. | Repair or replacement at cost; $400 minimum for minor damage. |
| Tables and chairs must be restored to the original layout. | $400. |

**We do not hold a security deposit.** Damage and non-compliance fees are invoiced after the event.

## 2.9 Monitoring and termination

Interior and entry cameras and noise sensors monitor the venue during your event, and footage may be reviewed afterward. Serious violations — drugs, repeated alcohol violations, exceeding occupancy, or severe noise — may result in **termination of the event without refund**.

## 2.10 Alcohol liability

Where bar service is provided, Orlando Event Venue is not liable for alcohol-related incidents beyond the scope of the bar service provider's insurance. You are responsible for ensuring no one under 21 is served or consumes alcohol at your event.

## 2.11 SMS terms

If you opt in to text messages, you agree to receive SMS from Orlando Event Venue about your reservation and, where separately consented to, promotional messages. Message frequency varies. Message and data rates may apply. Reply STOP to cancel, HELP for help. Carriers are not liable for delayed or undelivered messages.

## 2.12 Intellectual property

Website content, branding, photography, and materials are owned by or licensed to us and may not be copied or used without permission.

## 2.13 Disclaimer

The website and venue services are provided "as is" and "as available" to the fullest extent permitted by law. We do not guarantee uninterrupted website access or error-free operation.

## 2.14 Limitation of liability

To the fullest extent permitted by law, our total liability arising from your reservation will not exceed the amount you paid for that reservation, and we will not be liable for indirect, incidental, special, consequential, or punitive damages, including lost profits or lost opportunity, arising from your use of the website, your event, cancellation, delay, or messaging failures.

## 2.15 Indemnification

You agree to indemnify and hold harmless Orlando Event Venue, its owners, staff, and vendors from claims, damages, losses, and expenses arising from your event, your guests' or vendors' conduct, your breach of these Terms or the Venue Rules, or your violation of law.

## 2.16 Force majeure

Neither party is liable for failure to perform due to causes beyond reasonable control, including severe weather, hurricane, fire, flood, utility failure, government order, or public health emergency. If such an event prevents your booking, §3.7 applies.

## 2.17 Changes to these Terms

We may update these Terms by posting a revised version. Material changes apply going forward and do not retroactively change already-confirmed reservations unless you agree.

## 2.18 Governing law

These Terms are governed by the laws of the State of Florida, without regard to conflict-of-law rules. Venue for any dispute is Orange County, Florida. `[DECIDE A4 — confirm; decide whether to add arbitration]`

## 2.19 Contact

orlandoeventvenue@gmail.com · 407-974-5979

---

# PAGE 3 — BOOKING, CANCELLATION & REFUND POLICY
**Publish at:** `/booking-policy` — and link it from checkout **before** the pay button

> **This entire page is `[DECIDE A2]`.** `Refund-Rules.md` states that refund rules are not specified and must not be inferred. What follows is a **recommended default** built from OEV's actual cash model (50% holds the date, balance at 15 days, inventory purchased at 3 days) — not extracted canon. Luis must approve or change the numbers before this goes live.

## 3.1 Scope

This policy applies to all reservations at Orlando Event Venue.

## 3.2 How a reservation is confirmed

A date is held only when the **first 50% payment** is received. We send written confirmation, typically within 24 hours. Requests, quotes, and tours do not hold a date.

## 3.3 Payment schedule

| Stage | Amount | When |
|---|---|---|
| First payment | 50% of the total | At booking — this holds the date |
| Final payment | Remaining 50% | 15 days before the event |

If your event is within 15 days of booking, the balance link is sent immediately. Totals include the $199 cleaning fee, any add-ons, and the 3.5% card processing fee. Multi-day events are separate reservations, each with its own 50%.

## 3.4 Guest count and add-on changes

Guest count and bar/catering-linked add-ons may be changed up to **3 days before your event**. After that, **no refund is available for reductions** — inventory has already been purchased for your event.

## 3.5 Rescheduling `[DECIDE — recommended default]`

- More than 30 days before your event: reschedule once at no charge, subject to availability.
- 15–30 days before: reschedule once, subject to availability, with a `[$___]` rescheduling fee.
- Less than 15 days before: treated as a cancellation under §3.6.

New dates must be within 12 months of the original date. Rate differences between the original and new date apply.

## 3.6 Cancellation and refunds `[DECIDE A2 — recommended default]`

Cancellations must be sent in writing to orlandoeventvenue@gmail.com and are effective when we receive them.

| You cancel | Outcome |
|---|---|
| More than 30 days before the event | Full refund of amounts paid, less the 3.5% card processing fee |
| 15–30 days before | 50% of the total is retained; the remainder is refunded or issued as venue credit valid 12 months |
| Less than 15 days before | No refund. The full booking total remains due |
| No-show | No refund |

Non-refundable in all cases: the 3.5% card processing fee, third-party vendor charges already committed on your behalf, and any inventory purchased under §3.4.

**Termination for cause is not a cancellation.** If your event is ended early for a serious Venue Rule violation under §2.9, no refund is due and non-compliance fees still apply.

## 3.7 If we cancel or change your booking

If we cancel a confirmed reservation for weather, safety, staffing, facility failure, or another cause, you may choose:
1. A new date at no additional charge, subject to availability;
2. Venue credit valid 12 months; or
3. A full refund of amounts paid.

If we materially change what you booked, we will tell you promptly and you may choose any of the three options above.

## 3.8 Damage and post-event fees

Non-compliance fees under §2.8 and damage assessed after the event are invoiced separately and due within `[DECIDE — e.g. 14 days]` of invoice. Camera footage may be used to document them.

## 3.9 Chargebacks

Contact us first. We will work to resolve any billing issue. Filing a chargeback without contacting us may result in loss of future booking privileges, to the extent permitted by law.

## 3.10 Exceptions

Any exception must be approved by us in writing. Rights that cannot be waived under Florida law are unaffected.

---

# PAGE 4 — COOKIE POLICY
**Publish at:** `/cookies`

**Orlando Event Venue Cookie Policy**
Last updated: [PUBLICATION DATE]

## 4.1 What cookies are

Cookies are small text files stored on your device when you visit a website. They keep the site working, remember your preferences, and help us understand how the site is used.

## 4.2 Cookies we use

| Type | Purpose |
|---|---|
| Strictly necessary | Core site functions, booking form, checkout, security |
| Analytics | How visitors find and use the site, so we can improve it |
| Functional | Remembering your preferences and form progress |
| Marketing | Advertising and remarketing, where those tools are active |

`[DECIDE — list actual tools: Google Analytics? Meta Pixel? Google Ads tag? GoHighLevel tracking? The vault has no analytics inventory. Audit the site before publishing this table.]`

## 4.3 Managing cookies

You can manage cookies through your browser settings and through any cookie preference tool on our site. Blocking some cookies may affect site functionality, including the booking form.

## 4.4 Updates

We may update this Cookie Policy. Changes take effect when posted.

---

# PAGE 5 — SMS CONSENT NOTICE
**Place on the booking form and the lead-magnet popup, next to the phone field**

Two separate, **unchecked** checkboxes. Do not combine them. Do not pre-check either.

**Checkbox 1 — transactional (booking):**

> By checking this box, you agree to receive SMS messages from Orlando Event Venue about your booking, including confirmations, payment reminders, access instructions, and event-day updates. Message frequency varies. Message and data rates may apply. Reply STOP to opt out and HELP for help. Consent is not a condition of purchase. See our [Privacy Policy](/privacy) and [Terms of Use](/terms).

**Checkbox 2 — marketing (optional):**

> By checking this box, you agree to receive promotional SMS messages from Orlando Event Venue, including special offers, promo codes, and availability updates. Message frequency varies. Message and data rates may apply. Reply STOP to opt out and HELP for help. Consent is not a condition of purchase. See our [Privacy Policy](/privacy) and [Terms of Use](/terms).

**First message in any program must include:** `Reply STOP to opt out, HELP for help. Msg & data rates may apply.` — this matches the existing `Voice-Agent-Master-Prompt.md:47` rule. Extend it to the popup and GHL sequences, which currently have no consent text at all.

**Auto-reply for HELP:**
> Orlando Event Venue: for help call 407-974-5979 or email orlandoeventvenue@gmail.com. Msg & data rates may apply. Reply STOP to unsubscribe.

**Auto-reply for STOP:**
> You are unsubscribed from Orlando Event Venue messages. No further messages will be sent. Reply HELP for help.

---

## IMPLEMENTATION CHECKLIST

- [ ] Clear Decision Register items A1–A5
- [ ] Reconcile contradictions B1–B8 in emails, the FAQ, and voice-agent scripts, not just here
- [ ] **Move Terms acceptance before checkout.** "Your Agreement at a Glance" currently arrives after payment — that is not enforceable acceptance
- [ ] Add unchecked SMS consent checkboxes to `/book` and the popup; remove any pre-checked state
- [ ] Confirm A2P 10DLC campaign registration with the SMS provider
- [ ] Audit the site for analytics and pixels; complete the §4.2 table
- [ ] Add a cookie consent banner if marketing pixels are active
- [ ] Post signage at the venue entrance disclosing camera monitoring
- [ ] Set and document the camera footage retention period
- [ ] Replace every customer-facing use of "deposit" with "first 50%" per `Language-Rules.md:61`
- [ ] Fix the $200/hr late-cleanup figure in `Booking-Calendar-Sequence.md` before enforcing $350/hr
- [ ] Have counsel review §2.14, §2.15, §2.18, and the alcohol clause
