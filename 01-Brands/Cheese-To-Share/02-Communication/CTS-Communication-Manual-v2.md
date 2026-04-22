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
last_updated: 2026-04-22
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

## Core Email Flows

### Flow 1 — Custom Order Inquiry → Confirmed Order

**Trigger:** Customer emails with product/customization questions before ordering.

### Standard sequence
1. Customer inquires
2. CTS replies and answers all questions in one email
3. Customer narrows down options
4. CTS confirms feasibility
5. Customer places order and asks for price/payment
6. CTS confirms order, quotes price, offers SMS payment link, asks for phone number
7. Customer provides phone number
8. CTS sends payment link by SMS
9. Customer pays and confirms
10. CTS sends final confirmation with order details, date, time, and location
11. Day-of: CTS sends order-ready notification

### Step 2 — Reply to inquiry
```text
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

### Step 6 — Order confirmed + payment request
```text
Good [morning/afternoon] Mr [Name],

Thank you so much for your message! Yes, we can absolutely prepare that exactly as you described.

[Repeat customizations back clearly]

The total cost will be $[X], and this price includes [board/packaging/etc.] — no need to return it.

We can send a payment link by text. If you'd like to proceed, please send us your phone number.

Please let us know if you have any other questions. We look forward to preparing something special for you.

Best regards,
[Signature]
```

### Step 10 — Post-payment confirmation
```text
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

### Critical rule
The post-payment confirmation must always include:
- exact item ordered
- customizations
- pickup date
- pickup time
- full pickup location

No customer should have to send a follow-up email just to confirm where or when to pick up.

---

### Flow 2 — Same-Day / Returning Customer Order

**Trigger:** Returning customer emails a same-day or near-term order with customizations.

### What matters most
- reply fast
- confirm clearly
- match customer energy
- do not overcomplicate

### Quick order confirmation
```text
Hello good morning Mr [Name]!!!

Yes! Of course!! [emoji if tone matches]

[If seasonal: Happy [Holiday] to you!!!]

[Signature]
```

### Order ready notification
```text
Hi Mr [Name]!

Your order is ready 😊

[Signature]
```

### Rules
- Speed is a brand signal
- Match the customer's energy
- If the order is complex, briefly echo back the important customizations
- Keep the ready notification short

---

### Flow 3 — Seasonal / Holiday Special Orders

**Trigger:** Seasonal menu activation, inbound questions about seasonal items, or limited-time product pushes.

### Seasonal announcement template
```text
Subject: [Holiday] specials are here — order yours before [date]

Hi [Name],

[Seasonal hook — 1 sentence that makes it sound appetizing]

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

### Rules
- Lead with appetite or occasion
- Include deadline
- Keep CTA simple
- Send seasonal announcements as a short sequence, not constant blasts

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

| Type | Pattern | Example |
|---|---|---|
| Operational outbound | Direct, descriptive | "Your order is confirmed for February 14" |
| Seasonal announcement | Hook + deadline | "Valentine's boards are available — order before Feb 12" |
| Review request | Warm + specific | "How was your order, Mr Derek?" |
| Order ready | Ultra-short | "Your order is ready" |

### Rules
- Operational emails: clarity over cleverness
- Seasonal emails: appetite or occasion first, deadline second
- Use customer name in subject only when it feels naturally personal
- Do not chain marketing into old operational threads unnecessarily

---

## Review and Follow-Up Opportunity

CTS should actively ask for reviews after successful orders instead of relying only on a passive signature button.

### Review request template
```text
Subject: How was your order, Mr [Name]?

Hi Mr [Name],

It was great seeing you on [day]. Hope everything was a hit!

If you have a moment, we'd love to hear how it went. A quick review helps us a lot:

[LEAVE A REVIEW button]

See you next time,
Luis
Cheese To Share
```

---

## Improvement Recommendations

### 1. Standardize post-payment confirmation
Make the confirmation email the point where the customer no longer has to ask anything basic.

### 2. Seasonal sequence
Use a simple 2-email seasonal sequence:
- email 1: launch
- email 2: last chance

### 3. Review request automation
Trigger a review request 24–48 hours after pickup.

### 4. Capture more customer emails
Build email capture at pickup and in structured ordering flows.

### 5. Centralize vendor account records
Maintain one reference note with:
- rep names
- account terms
- billing agreements
- account IDs
- current issues

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
