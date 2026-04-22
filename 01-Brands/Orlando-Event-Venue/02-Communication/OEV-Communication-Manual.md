---
brand: Orlando-Event-Venue
domain: communication
area: manual
subarea: canonical
note_type: canonical
status: active
source: user-provided communication rules
canonical: true
used_for_ai: true
hub_role: manual
last_updated: 2026-04-21
tags:
  - OEV
  - communication
  - email
  - sms
  - reminders
  - internal
  - client
---

# OEV Communication Manual

## Parent
- [[Communication-Home]]
- [[Brand-Home]]

## Related
- [[Voice-and-Tone]]
- [[Language-Rules]]
- [[Sales-Home]]
- [[Follow-Up-Rules]]
- [[Payment-Rules]]
- [[Support-Process]]
- [[Message]]
- [[Constraints]]
- [[KPIs]]

## Purpose
This note is the **single source of truth** for Orlando Event Venue communication across:
- client-facing email
- client-facing SMS
- internal/admin notifications
- reminders
- payment communication
- lead capture follow-up
- tour communication
- marketing-adjacent promotional follow-up when tied to booking action

Use this file before writing or automating any OEV communication.

---

## Core Communication Rule
OEV communicates like a venue host who respects the client's time and event.

Every message must do these 3 things:
1. state what happened
2. state what happens next
3. make it easy to reach a real human

If a message does not reduce confusion, friction, or decision delay, it should be rewritten.

---

## Voice and Tone

### What OEV should sound like
- clear
- direct
- operational
- calm
- trustworthy
- helpful
- time-respectful
- venue-host, not generic business

### What OEV should not sound like
- overly promotional in transactional messages
- vague
- fluffy
- “agency-like”
- too casual
- too clever
- emotionally manipulative
- mixed between sales + ops + marketing in the same message

### Writing rules
- use the client's first name whenever appropriate
- lead with the useful thing, not filler
- one message = one main action
- treat automation like a real human wrote it
- make the next step obvious
- prefer operational precision over sounding “fancy”

### Avoid
- “Just reaching out to let you know…”
- double CTA emails
- repeated subject + preview text
- generic sign-offs
- sending access details too early
- mixing marketing copy into transactional messages

---

## Standard Signature Block

### Client-facing signature
Orlando Event Venue Team  
407-974-5979  
orlandoeventvenue.org  
orlandoeventvenue@gmail.com  
3847 E Colonial Dr, Orlando, FL 32803

### Automated footer
This is an automated email. Please keep it for your records.

### Internal footer
This is an internal notification. Do not forward to customers.

---

## Subject Line System

### Transactional
`[Status] | Orlando Event Venue`

Example:
- Deposit Received | Orlando Event Venue
- Final Payment Received | Orlando Event Venue

### Confirmation
`Your [Thing] Is [State] | Orlando Event Venue`

Example:
- Your Event Is Confirmed | Orlando Event Venue
- Your Tour Is Confirmed | Orlando Event Venue

### Reminder
`[Timeframe] Until Your Event | Orlando Event Venue`

Example:
- 30 Days Until Your Event | Orlando Event Venue
- 7 Days Until Your Event | Orlando Event Venue

### Action needed
`[Action Context] | Orlando Event Venue`

Example:
- Remaining Balance Due | Orlando Event Venue
- Your Access Instructions for Tomorrow | Orlando Event Venue

### Internal/admin
`[Context] — [Reservation or Invoice ID]`

Example:
- OEV Payment Received — OEV-WRSPVF
- Invoice Paid — INV-1024

### Preview text rule
Preview text must extend the subject, not repeat it.

---

## Channel Logic

| Touchpoint | Email | SMS | Rule |
|---|---|---|---|
| Deposit received | Yes | No | Record + reassurance |
| Booking confirmed | Yes | No | Detailed info-heavy confirmation |
| Remaining balance due | Yes | Yes | Payment is time-sensitive |
| Final payment received | Yes | No | Receipt-style confirmation |
| 30-day reminder | Yes | No | Info-heavy planning reminder |
| 7-day reminder | Yes | No | Rules + prep reminder |
| 1-day reminder | Yes | Yes | Access details are critical |
| 1-hour reminder | Yes | Yes | Day-of urgency |
| Post-event guest report | Yes | Yes | Close-out action required |
| Review request | Yes | No | Low-friction ask |
| Tour confirmed | Yes | No | Detailed logistics |
| Tour reminder (same day) | Yes | Yes | Day-of logistics |
| Tour 1-hour reminder | No | Yes | Fast trigger |
| Tour follow-up | Yes | No | Sales follow-up |
| Admin tour reminder | No | Yes | Internal only |
| Lead capture promo | Yes | Yes | Fast delivery required |
| Invoice sent | Yes | No | Payment + records |
| Invoice paid (internal) | Yes | No | Internal notification |
| Invoice paid (guest) | Yes | No | Receipt + confirmation |

### Important channel rule
Do not send SMS just because it is available.  
Use SMS only when speed, urgency, or completion rate matters.

---

## SMS Rules
- always open with first name when possible
- one action per SMS
- under 160 characters when possible
- do not dump details into SMS
- refer to email when full context is needed
- do not use marketing language inside transactional SMS
- only include links when action is required

### SMS structure
`Hi [First Name] — [what happened]. [what to do next]. [how to get help].`

---

## Canonical Access Instructions
These steps should be used consistently in 1-day and 1-hour access communication.

### Entry
1. Arrive at Colonial Town Center and look for the GLOBAL sign with 3847 displayed.
2. Facing the GLOBAL sign, go to the door on the left side of the building.
3. Find the black lockbox with touchscreen keypad.
4. Wake the screen and enter code: `03302026`
5. Retrieve the magnetic key.
6. Tap the magnetic key on the sensor on the right side of the door.
7. After unlocking, return the key to the lockbox immediately and close it.
8. Inside the venue, locate the remote labeled “Light” on the left wall.
9. Use the left-side buttons to turn on the lights.
10. Return the remote to its original place.

### Checkout
- turn off all lights
- place all trash bags on the back patio
- do not leave trash bags inside the venue
- lock the door securely
- remove all personal items

### Security rule
The access code should only be sent 1 day before the event and in day-of operational reminders when necessary.  
Do not include it in earlier reminders.

---

## Wi-Fi
Network: GlobalChurch  
Password: Orlandoministry

Use in:
- 30-day reminder
- 7-day reminder
- event-prep communication when relevant

---

## Venue Rules
Use whenever rules need to be stated clearly.

- maximum occupancy: 90 guests
- setup and breakdown must stay within booking window
- late cleanup fee: $200/hour
- no alcohol, drugs, smoking, pets, glitter, confetti, or rice
- no nails, staples, residue tape, or open flames unless pre-approved

### Important note
If operational policy changes, update this section first before changing templates.

---

## Pricing Reference
Use for tours, inquiries, quote follow-up, and sales clarification.

- Hourly rate: $140/hour
- Hourly minimum: 4 hours
- Daily rate: $899/day
- Daily access: 24-hour
- Cleaning fee: $199/reservation
- Processing fee: 3.5% per transaction
- AV/Production basic: $79/hour
- LED screen production: $99/hour
- Beverage station: $6/person/day

### Discount rule
Discount applies to base rental only.  
It does **not** apply to AV, cleaning, beverage service, or other add-ons unless explicitly approved.

### Multi-day reference
- 2–3 day workshop: 25% off base rental
- large/repeat multi-date corporate: up to 50% off base rental with management approval

---

## Merge Fields / Dynamic Data
Use these fields when building automations or templates.

- first name = `{{contact.first_name}}`
- full name = `{{contact.full_name}}`
- reservation number = `{{contact.oev_reservation_number}}`
- event type = `{{contact.oev_event_type}}`
- event date = `{{contact.oev_event_date}}`
- booking type = `{{contact.oev_booking_type}}`
- guest count = `{{contact.oev_number_of_guests}}`
- balance amount = `{{contact.oev_balance_amount}}`
- balance link expiry = `{{contact.oev_balance_link_expires_at}}`
- balance payment URL = `{{contact.oev_balance_payment_url}}`

Guest report URL pattern:
`https://orlandoeventvenue.org/guest/report/{{contact.oev_reservation_number}}`

---

## Communication by Function

### 1. Sales / inquiry communication
Goal:
- answer availability
- answer price clearly
- reduce uncertainty
- move toward booking, tour, or proposal

Rules:
- answer their main question first
- if availability is known, say it early
- if pricing is relevant, include it proactively
- do not make them ask twice for cost
- stack value with price
- always give a next step

### 2. Confirmation communication
Goal:
- reduce uncertainty
- lock expectation
- prevent surprises
- reinforce operational trust

Rules:
- confirm exactly what is locked
- include date, event type, booking type, guest count when relevant
- explain what comes next
- remind them access instructions come later

### 3. Reminder communication
Goal:
- keep the event moving smoothly
- reduce forgotten actions
- surface timing-sensitive tasks at the right time

Rules:
- reminder emails should be operational, not salesy
- reminder SMS should be short and action-driven
- if urgency is low, keep reminder email-only
- if urgency is high, use email + SMS

### 4. Payment communication
Goal:
- make payment obvious
- reduce delay
- reduce support friction
- give confidence after payment

Rules:
- amount due must be visible
- link must be easy to find
- expiry must be stated when relevant
- if already paid, say no action is needed
- payment confirmations should read like records, not marketing

### 5. Support / issue communication
Goal:
- reduce confusion fast
- solve the issue with the fewest steps possible
- keep trust even when something went wrong

Rules:
- state issue clearly
- state next step clearly
- avoid blame language
- avoid over-explaining before solving
- if escalation is needed, say who takes over next

### 6. Internal/admin communication
Goal:
- help staff act fast
- reduce missed tasks
- preserve operational traceability

Rules:
- internal messages should include exact identifiers
- include client name, phone, email, reservation/invoice ID when relevant
- internal notifications must never read like client-facing copy
- always mark internal notifications clearly

---

## Sequence Logic Summary

### Post-booking flow
1. Deposit received
2. Booking confirmed
3. Remaining balance due
4. Final payment received
5. 30-day reminder
6. 7-day reminder
7. 1-day reminder
8. 1-hour reminder
9. Post-event guest report
10. Review request

### Tour flow
1. Tour confirmed
2. Same-day reminder
3. 1-hour reminder
4. Tour follow-up
5. Internal admin tour reminder

### Lead capture promo flow
1. Immediate email + SMS
2. 18-hour reminder
3. 30-hour final reminder

### Standalone invoice flow
1. invoice sent
2. internal payment confirmation
3. guest payment confirmation

---

## Decision Rules

### Use email only when
- more detail is required
- record-keeping matters
- the action is not urgent
- the message includes multiple important details

### Use email + SMS when
- action is time-sensitive
- access is involved
- payment is due
- same-day execution matters
- close-out action is required

### Use SMS only when
- the communication is short
- timing is critical
- the recipient does not need a long explanation
- it is internal ops or 1-hour trigger style communication

---

## Boundaries
Do not:
- combine marketing and transactional communication in the same message
- send access instructions too early
- bury pricing when the inquiry is clearly price-driven
- write clever subject lines
- use pressure language unless the urgency is real
- improvise venue rules in one-off replies
- create a second version of the truth outside this manual

If a special case appears, resolve it here after decision — not by leaving it undocumented.

---

## Good Communication Standard
A strong OEV message should feel like:
- the sender knows exactly what stage the customer is in
- the sender knows what the customer needs next
- the sender is reducing friction, not adding to it
- the sender is making the venue feel reliable

---

## Anti-Examples
Weak communication usually looks like:
- filler at the top
- vague next steps
- missing price
- missing action
- mixed intent
- overly long SMS
- confirmation messages without operational detail
- reminders that do not actually remind the user of anything useful

---

## How Claude Should Use This Note
When Claude is writing or restructuring communication for OEV, this note should be treated as the canonical communication layer.

Claude should consult in this order:
1. [[Communication-Home]]
2. this note
3. [[Voice-and-Tone]]
4. [[Language-Rules]]
5. the relevant operational system note:
   - [[Sales-Home]]
   - [[Follow-Up-Rules]]
   - [[Payment-Rules]]
   - [[Support-Process]]
6. historical evidence only if examples are needed

Claude should not use another brand's communication logic unless explicitly instructed.

---

## Maintenance Rule
Any change to:
- pricing
- venue rules
- access instructions
- channel logic
- signature block
- payment timing
- reminder timing

must be updated here first.

This file is the communication source of truth for OEV.
