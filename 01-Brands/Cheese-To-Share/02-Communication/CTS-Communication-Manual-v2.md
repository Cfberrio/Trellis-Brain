---
brand: Cheese-To-Share
area: communication
domain: manual
note_type: canonical
status: active
used_for_ai: true
owner: Luis Torres
primary_contact_email: info@cheesetoshare.us
legacy_email: cheesetosharenaturalfood@gmail.com
primary_rep: Luis Torres
channel_stack:
  - email
  - sms
  - GoTab
  - Toast POS
last_updated: 2026-04-23
---

# Cheese To Share — Communication Manual

## Parent
- [[Communication-Home]]

## Related
- [[Brand-Home]]
- [[Positioning]]
- [[Offers]]
- [[Value-Proposition]]
- [[Website-Home]]
- [[Menu-Page]]
- [[Catering-Page]]
- [[Location-Page]]
- [[Story-Page]]
- [[Contact-Page]]
- [[Sales-Process]]
- [[Pricing-Logic]]
- [[Onboarding-Process]]
- [[Support-Home]]
- [[Retention-Strategy]]

## Purpose
This file is the canonical source of truth for all Cheese To Share customer-facing, vendor-facing, and internal operational communication. It defines how CTS writes, responds, confirms, follows up, and escalates across email and SMS.

## Canonical Contact Standard

### Brand-standard email
**info@cheesetoshare.us**

This is the canonical CTS communication email and should be used across:
- website contact page
- footer
- catering pages
- inquiry forms
- signatures
- confirmation emails
- follow-up emails
- internal documentation

### Legacy email
**cheesetosharenaturalfood@gmail.com**

This may still appear in older systems, older signatures, or live pages that have not yet been updated. It should be treated as a legacy address, not the brand-standard address.

### Rule
When there is a conflict between old references and newer documentation, **info@cheesetoshare.us** wins.

---

## Ownership and Approval

### Owner
Luis Torres

### Operational senders
- Luis Torres
- Erika Portillo (only when operationally appropriate and using the correct signature block)

### Changes that require approval before going live
- signature changes
- primary contact information
- payment flow wording
- SMS usage rules
- seasonal campaign announcements
- catering confirmation language
- vendor escalation templates

### Rule
No automation, template, or system should overwrite the canonical communication standard without explicit approval.

---

## Brand Voice

CTS communicates like a warm, enthusiastic local business that genuinely knows and likes its customers.

Not corporate.  
Not scripted.  
Not cold.

### Core voice attributes
- **Neighborly** — customers are treated like regulars, even on first contact
- **Enthusiastic but not fake** — exclamation points used naturally, not as performance
- **Warm formality** — "Mr Dustin", "Mr Derek" — respectful without being stiff
- **Responsive** — speed of reply signals how much CTS cares
- **Appetite-driven** — language should make the product sound good, not just logistically correct

### Voice in practice

**Formal-casual balance**
> "Good morning Mr Dustin!"  
> "Yes! Of course!! 👍😂"  
> "Warm regards, Luis Torres"

Same rep, same thread. The formality adjusts to the customer's energy — not the other way around.

### Time-of-day greetings used consistently
- Morning reply → "Good morning [Mr/Name]"
- Afternoon reply → "Good afternoon [Mr/Name]"
- Evening reply → "Good evening [Mr/Name]" or "Good night [Name]" if the tone is already warm and informal

### Emoji use
- Used naturally as punctuation or emphasis, not decoration
- Common: 😊 👍 😂 💛
- Acceptable on: quick confirmations, pickup-ready notifications, holiday messages
- Not appropriate on: price quotes, vendor/ops emails, issue escalations, deposits, policy clarifications

### Closing lines
- Customer emails: "Warm regards", "Best regards", "Have a great day!", "Have a wonderful Sunday!"
- Quick/casual replies: a light emoji close is acceptable
- Vendor/ops: "Thank you", "I'll keep you posted"

---

## Signature Block

### Canonical outbound signature
```text
Luis Torres
Lead Representative
Cheese To Share
(407) 276-3234
info@cheesetoshare.us
https://www.cheesetoshare.us/
[REVIEW US button]
```

### Rules
- Signature on every outbound email, including quick replies
- "Lead Representative" is the correct title
- Review link should always be active
- If Erika Portillo sends an operational email, her name should replace Luis's name rather than sending under his identity
- No outbound signature should use the legacy Gmail as the primary address

---

## Customer Segments

| Segment | Who | Main channel | Voice level |
|---|---|---|---|
| New inquiries | First-time contact, found CTS online or at market | Email | Warm, informative, answers everything |
| Returning customers | Previous order, references past experience | Email | Casual, personal, faster |
| Catering / large order | Advance orders, customizations, seasonal specials | Email + SMS | Thorough, confirms every detail |
| Vendors / suppliers | Toast, GoTab, third-party tools | Email | Professional, documented, clear asks |

---

## Channel Purpose

| Channel | Purpose | Rule |
|---|---|---|
| Email | Main communication channel for inquiries, custom orders, confirmations, vendor issues, and follow-up | Default channel for CTS |
| SMS | Payment link delivery only | No marketing or casual updates by SMS |
| GoTab | Structured catering order capture | Use when the customer is ready to order through a systemized flow |
| Toast POS | Payments / POS issue handling | Operational and vendor-related use only |

### Rule
CTS communication is primarily email-led. SMS exists only to support payment completion when needed.

---

## Email Sequence Library

All sequences include a metadata block: Trigger, Goal, Length, Timing, and Exit Conditions. Every email template includes Subject and Preview text.

---

### Sequence 1 — Custom Order Inquiry → Confirmed Order

```
Trigger: Customer emails with product or customization questions before ordering
Goal: Convert inquiry into paid, confirmed order
Length: 4–6 touchpoints (customer-paced, not timed)
Channel: Email primary; SMS for payment link only
Exit conditions: Payment received + final confirmation sent | No response after 3 follow-ups
```

**Flow**

| Step | Action | Sender |
|---|---|---|
| 1 | Customer inquires | Customer |
| 2 | CTS replies, answers all questions in one email | CTS |
| 3 | Customer narrows down options | Customer |
| 4 | CTS confirms feasibility | CTS |
| 5 | Customer places order, asks for price/payment | Customer |
| 6 | CTS confirms order, quotes price, requests phone for payment | CTS |
| 7 | Customer provides phone number | Customer |
| 8 | CTS sends payment link by SMS | CTS |
| 9 | Customer pays and confirms | Customer |
| 10 | CTS sends final confirmation with full order summary | CTS |
| 11 | Day-of: CTS sends order-ready notification | CTS |

**Step 2 — Reply to inquiry**
```text
Subject: Re: [their subject line]
Preview: Here's everything you need — let us know how you'd like to proceed.

Good [morning/afternoon] Mr [Name],

Thank you so much for reaching out!

[Answer question 1 directly]
[Answer question 2 directly]
[Answer question 3 directly]
[Answer question 4 directly]

Please let us know how you'd like to proceed and we'll be happy to help finalize the details.

Warm regards,
[Signature]
```

**Step 6 — Order confirmed + payment request**
```text
Subject: Your order is all set — one last step
Preview: Send us your number and we'll text you a payment link right away.

Good [morning/afternoon] Mr [Name],

Thank you so much for your message! Yes, we can absolutely prepare that exactly as you described.

[Repeat customizations back clearly]

The total cost will be $[X], and this price includes [board/packaging/etc.] — no need to return it.

We can send a payment link by text. If you'd like to proceed, please send us your phone number.

Please let us know if you have any other questions. We look forward to preparing something special for you.

Best regards,
[Signature]
```

**Step 10 — Post-payment confirmation**
```text
Subject: Your order is confirmed for [Day, Date]
Preview: Full details inside — date, time, location, and everything you ordered.

Good [morning/afternoon] Mr [Name],

Thank you! We've received your payment and your order is confirmed.

Order summary:
- [Item + customizations]
- Pickup: [Day], [Date] at [Time]
- Location: [Full address]

If you need anything or have questions before pickup day, don't hesitate to reach out.

We look forward to seeing you!

[Signature]
```

**Step 11 — Order ready**
```text
Subject: Your order is ready
Preview: Come by whenever you're ready — we'll see you soon.

Hi Mr [Name]!

Your order is ready 😊

[Signature]
```

**Critical rule**
Post-payment confirmation must always include: exact item ordered, customizations, pickup date, pickup time, full pickup location. No customer should follow up just to confirm where or when to pick up.

---

### Sequence 2 — Same-Day / Returning Customer Order

```
Trigger: Returning customer emails a same-day or near-term order
Goal: Fast confirmation, matched energy, clean handoff to pickup
Length: 2 emails (confirmation + ready notification)
Channel: Email
Exit conditions: Order ready notification sent
```

**What matters most**
- Reply fast
- Confirm clearly
- Match customer energy
- Do not overcomplicate

**Quick order confirmation**
```text
Subject: Got it — you're all set!
Preview: [No preview needed for quick sends]

Hello good morning Mr [Name]!!!

Yes! Of course!! [emoji if tone matches]

[If seasonal: Happy [Holiday] to you!!!]

[Signature]
```

**Order ready notification**
```text
Subject: Your order is ready
Preview: Come pick it up whenever you're ready.

Hi Mr [Name]!

Your order is ready 😊

[Signature]
```

**Rules**
- Speed is a brand signal — reply fast
- Match the customer's energy
- Echo back key customizations if the order is complex
- Keep the ready notification short

---

### Sequence 3 — Catering Inquiry → Booking

```
Trigger: Customer inquires about catering for an event
Goal: Convert inquiry into confirmed, deposited catering booking
Length: 5–6 touchpoints (customer-paced)
Channel: Email primary; GoTab for structured order capture; SMS for deposit payment
Exit conditions: Deposit received + event date confirmed | No response after 2 follow-ups
```

**Flow**

| Step | Action | Sender |
|---|---|---|
| 1 | Customer inquires about catering | Customer |
| 2 | CTS replies, gathers event details | CTS |
| 3 | Customer provides event details | Customer |
| 4 | CTS sends catering proposal | CTS |
| 5 | Customer approves or requests changes | Customer |
| 6 | CTS confirms scope, requests deposit via SMS | CTS |
| 7 | Deposit received — CTS sends booking confirmation | CTS |
| 8 | 48–72 hrs before event: pre-event logistics confirmation | CTS |

**Step 2 — Catering inquiry reply**
```text
Subject: Re: [their subject line]
Preview: A few quick questions so we can put together the right proposal.

Good [morning/afternoon] [Name],

Thank you for reaching out — we'd love to help make your event special!

To put together the best proposal, a few quick questions:

- What's the occasion or event type?
- Approximate date and time?
- Roughly how many guests?
- Do you have a style in mind — grazing board, spread, individual servings?
- Any dietary restrictions we should know about?

Once we have those details, we'll put together some options for you.

Warm regards,
[Signature]
```

**Step 4 — Catering proposal**
```text
Subject: Catering proposal for [Event / Date]
Preview: Here's what we're thinking — let us know what you'd like to adjust.

Good [morning/afternoon] [Name],

Based on what you've shared, here's what we'd suggest:

[Option 1: Name + description + price]
[Option 2: Name + description + price, if applicable]

Presentation: [Setup style, boards, packaging]
Serves: [Guest count range]
Logistics: [Pickup / delivery / on-site setup]
Deposit required: $[Amount or %]
Full payment due: [Timeline]

We can customize this — just let us know what feels right and we'll lock in the details.

Best regards,
[Signature]
```

**Step 6 — Booking confirmation + deposit request**
```text
Subject: Let's lock this in — deposit details inside
Preview: One last step to confirm your catering booking.

Good [morning/afternoon] [Name],

Here's a summary of what we're confirming:

Event: [Type]
Date: [Date + Time]
Location: [Venue or pickup address]
Order: [Items + presentation]
Total: $[X]
Deposit due: $[X] to confirm your date

Please send us your phone number and we'll text a payment link right away.

[Signature]
```

**Step 7 — Booking confirmed**
```text
Subject: Your catering booking is confirmed — [Date]
Preview: Full event details inside. We're looking forward to it.

Good [morning/afternoon] [Name],

Your deposit is received and your catering booking is confirmed.

Event summary:
- Event: [Type]
- Date: [Date] at [Time]
- Location: [Full address or venue]
- Order: [Items + presentation]
- Remaining balance: $[X] due [date / at pickup]

We'll be in touch 48 hours before the event to confirm logistics. If anything changes before then, just reach out.

Warm regards,
[Signature]
```

**Step 8 — Pre-event logistics confirmation (send 48–72 hrs out)**
```text
Subject: Final details for your event on [Date]
Preview: Confirming everything is set — just reply if anything has changed.

Hi [Name],

Your event is coming up on [Date] and we wanted to confirm everything is on track.

Order: [Items + presentation]
Pickup/Delivery: [Time + location]
Remaining balance: $[X] due at pickup [if applicable]

If anything has changed or you have questions, just reply here.

Looking forward to it!

[Signature]
```

---

### Sequence 4 — Seasonal / Holiday Campaign

```
Trigger: Seasonal menu activation or limited-time product push
Goal: Drive pre-orders before deadline
Length: 2 emails
Timing: Email 1 on launch day; Email 2 (last chance) 2–3 days before order deadline
Channel: Email
Exit conditions: Order placed | Order deadline passed
```

**Email 1 — Launch**
```text
Subject: [Holiday] specials are here — order yours before [date]
Preview: [One appetizing sentence about the seasonal offering]

Hi [Name],

[Seasonal hook — 1 sentence that makes it sound appetizing and occasion-specific]

This [season/holiday], we're offering:
- [Special item 1]
- [Special item 2]
- [Customization note if applicable]

Order by [deadline] for pickup through [date].

[CTA button: Order Now]

Questions? Just reply or call us at (407) 276-3234.

Talk soon,
Luis Torres
Cheese To Share
```

**Email 2 — Last chance (send 2–3 days before deadline)**
```text
Subject: Last chance — [Holiday] orders close [day]
Preview: Don't miss out — we're taking orders until [date].

Hi [Name],

Just a reminder — [holiday] orders close on [date].

[1 sentence making it sound worth acting on]

[CTA button: Order Before It's Too Late]

Questions? Reply here or call (407) 276-3234.

Talk soon,
Luis Torres
Cheese To Share
```

**Rules**
- Lead with appetite or occasion, not logistics
- Include deadline in both subject lines
- 2 emails per seasonal push only — launch + last chance
- Never add a third blast to the same seasonal thread

---

### Sequence 5 — Review Request

```
Trigger: Order ready notification sent (pickup assumed complete)
Timing: 24–48 hours after order-ready notification
Goal: Capture Google review while experience is fresh
Length: 1 email — no follow-up
Channel: Email
Exit conditions: Review submitted | 48 hours elapsed with no response
```

```text
Subject: How was your order, Mr [Name]?
Preview: Hope everything was a hit — a quick note from us inside.

Hi Mr [Name],

It was great seeing you on [day]. Hope everything was a hit!

If you have a moment, we'd love to hear how it went. A quick review helps us a lot:

[LEAVE A REVIEW button]

See you next time,
Luis
Cheese To Share
```

**Rules**
- Send 24–48 hours after pickup — not same-day
- Only send after clean, completed orders
- Do not send after any complaint, confusion, or issue thread
- One request per order — no follow-up if no response

---

### Sequence 6 — Re-Engagement

```
Trigger: No order or contact in 60+ days from a previously active customer
Goal: Reconnect and prompt next order
Length: 2 emails
Timing: Email 1 at 60-day mark; Email 2 seven days later if no response
Channel: Email
Exit conditions: Order placed | Unsubscribed | No response after Email 2
```

**Email 1 — Check-in**
```text
Subject: It's been a while — hope you're doing well
Preview: We've missed you. A little something inside.

Hi [Name],

It's been a little while since your last order and we just wanted to check in.

We've been adding [new item / seasonal item] and thought you might enjoy it.

Whenever you're ready for your next order, we're here.

[CTA button: Order Now]

Warm regards,
Luis Torres
Cheese To Share
```

**Email 2 — Last touch (send 7 days after Email 1 if no response)**
```text
Subject: One last thing before we stop reaching out
Preview: We'll keep your spot — just let us know when you're back.

Hi [Name],

We don't want to fill your inbox — so this is our last check-in for a while.

If you ever want to place an order or ask about something seasonal, just reply here and we'll pick right up.

Take care,
Luis
Cheese To Share
```

**Rules**
- Tone stays warm — no promotional pressure, no discounts
- Only runs on customers who have previously placed an order, not cold contacts
- After Email 2 with no response, remove from active re-engagement list

---

## SMS Communication Rules

CTS uses SMS exclusively for payment links.

### Standard SMS flow
1. Customer places order via email
2. CTS offers payment link
3. Customer provides number in writing
4. CTS sends link by SMS
5. Customer confirms payment
6. Communication returns to email

### Rules
- Never initiate SMS without the customer providing the number in writing
- SMS content should be payment-link-focused only
- No promotional messaging via SMS
- No routine order updates via SMS
- Once payment is complete, the order record should be confirmed back in email

---

## Vendor and Operational Communication

CTS communicates with vendors in a distinct mode:
- professional
- documented
- clear asks
- no fluff
- no emotional escalation

### GoTab
Use for catering order infrastructure and scheduling management.

#### Standard approach
```text
Hey [Name], hope all is well.

[Specific request]

[Specific details: dates, names, phone numbers, issue scope]

Thank you,
[Signature]
```

### Toast POS
Use for billing, POS, hardware/software, or account issues.

#### Escalation template
```text
Hi [Name],

Thank you for checking in. I wanted to update you on an issue we just escalated with [support team] and loop you in.

Background:
[Original agreement or setup]

What happened:
[Where the system diverged]

Current status:
[What has already been done]

What we need:
[Exact outcome required]

I'll keep you posted. Please let me know if you need anything from me in the meantime.

Thank you,
[Signature]
```

### Rule
Vendor emails must define:
- history
- issue
- current status
- exact ask

Never send a vague escalation.

---

## Failure Handling

### Payment link not received
Reply within the same business window and resend immediately. Confirm the number before resending.

### Wrong pickup time or customer confusion
Clarify the confirmed time and re-send the order summary in one clean email.

### Item unavailable
Do not improvise silently. Offer replacement options clearly and wait for confirmation if the substitution changes the experience meaningfully.

### Late pickup
Acknowledge politely, confirm if order is being held, and give the current next step without guilt language.

### Catering deposit paid but details incomplete
Send a structured follow-up asking only for the missing items. Do not bury missing details inside a long paragraph.

### Vendor issue unresolved
Move from normal support email to documented escalation. Preserve dates, agreements, and names.

---

## Subject Line Patterns

| Type | Pattern | Preview text approach | Example subject |
|---|---|---|---|
| Operational outbound | Direct, descriptive | Extend with key detail | "Your order is confirmed for February 14" |
| Payment request | Action + outcome | Urgency without pressure | "Your order is all set — one last step" |
| Catering confirmation | Event anchor + confidence signal | Full details in email | "Your catering booking is confirmed — [Date]" |
| Seasonal announcement | Hook + deadline | Appetizing 1-liner | "Valentine's boards are available — order before Feb 12" |
| Review request | Warm + specific | Soft intrigue | "How was your order, Mr Derek?" |
| Order ready | Ultra-short | Logistics nudge | "Your order is ready" |
| Re-engagement | Genuine, non-promotional | Keep it human | "It's been a while — hope you're doing well" |

### Rules
- Operational emails: clarity over cleverness
- Seasonal emails: appetite or occasion first, deadline second
- Preview text extends the subject — never repeat it
- Use customer name in subject only when it feels naturally personal
- Do not chain marketing into old operational threads

---

## Sequence Metrics

Minimum metrics to track per sequence once email automation is active.

| Sequence | Key metric | Target | Watch for |
|---|---|---|---|
| Seq 1 — Custom order | Time to payment from first email | Under 24 hrs | Long back-and-forth = missing info in initial reply |
| Seq 2 — Same-day | Reply time | Under 2 hrs | Delayed ready notification erodes trust |
| Seq 3 — Catering | Deposit rate from proposal sent | 70%+ | Low rate = proposal too vague or missing logistics |
| Seq 4 — Seasonal | Open rate | 35–45% | Below 30% = subject line or list problem |
| Seq 4 — Seasonal | Order conversion | 15–25% of opens | Below 10% = CTA or timing issue |
| Seq 5 — Review | Review submission rate | 20–30% of sends | Below 15% = timing off or wrong segment |
| Seq 6 — Re-engagement | Email 1 reply or click rate | 10–15% | Below 5% = list is stale or segment too broad |

**Rules**
- Track open rate and click rate at minimum once automation is live
- Do not optimize sequences based on fewer than 30 sends
- Review sequence performance monthly, not per campaign

---

## Improvement Recommendations

### Priority 1 — Implement now

1. **Post-payment confirmation standard** — Sequence 1, Step 10 defines this. Audit any existing GHL or GoTab templates against this standard before activating.
2. **Seasonal 2-email structure** — Enforce launch + last chance only. No ad-hoc seasonal blasts outside this structure.
3. **Catering pre-event confirmation** — Sequence 3, Step 8 should be templated in GHL and fired automatically 48–72 hrs after deposit received.

### Priority 2 — Build next

4. **Review request automation** — Trigger Sequence 5 automatically 24–48 hrs after order-ready notification. Map the trigger in GHL or n8n.
5. **Email capture at pickup** — Build intake at pickup (QR code, tablet, or verbal ask). Route captured emails into the active customer segment.
6. **Re-engagement automation** — Build Sequence 6 in GHL. Set 60-day inactivity trigger on active customer segment.

### Priority 3 — Infrastructure

7. **Vendor account reference note** — Create one Obsidian note with rep names, account terms, billing agreements, account IDs, and current open issues for GoTab and Toast.
8. **Legacy email migration** — Audit all active pages, signatures, and automations for cheesetosharenaturalfood@gmail.com. Migrate everything to info@cheesetoshare.us.

---

## QA Checklist Before Any Communication Goes Live

- Is the sender identity correct?
- Is the signature using **info@cheesetoshare.us**?
- Are date, time, and location included if relevant?
- Are all customizations echoed back clearly?
- Is the correct channel being used?
- Is the message warm without becoming sloppy?
- Is the ask or next step obvious?
- Does the message sound like CTS and not like a generic template?

---

## What CTS Communication Is Not

- Not a high-volume blast brand
- Not corporate
- Not cold
- Not vague about customizations
- Not SMS-first
- Not interchangeable with OEV or DR voice

---

## Final Rule

When there is any uncertainty, CTS communication should favor:
- warmth
- clarity
- confirmation of details
- and fast response

The goal is not just to complete a transaction.  
The goal is to make the customer feel personally taken care of.

---

## Contact and Access Reference

| System | Contact | Access / note |
|---|---|---|
| Canonical CTS email | info@cheesetoshare.us | Primary brand-standard |
| Legacy CTS email | cheesetosharenaturalfood@gmail.com | Legacy only; not canonical |
| CTS phone | (407) 276-3234 | Primary phone |
| CTS website | cheesetoshare.us | Main site |
| GoTab | Client Success team | Catering operations |
| Toast POS | Account/support contacts | POS / billing issues |

---

*This file is the source of truth for all Cheese To Share communication patterns. Updates to voice, flows, contacts, or channel rules should be reflected here first.*
