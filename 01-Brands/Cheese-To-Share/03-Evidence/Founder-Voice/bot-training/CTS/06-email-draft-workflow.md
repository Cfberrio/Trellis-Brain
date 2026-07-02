---
title: CTS Bot — Email Draft Workflow
brand: Cheese To Share (CTS)
purpose: Step-by-step for drafting any email reply, with the canonical sequence templates. Email is the DEFAULT channel; SMS is payment links only.
sources: Communication-Manual Sequences 1–3 (verbatim templates)
updated: 2026-07-01
---

# Email Draft Workflow

Email is CTS's default channel. Most customer inbound is a **multi-question inquiry** — the move: answer every question in one reply, echo customizations, route payment to SMS.

## Steps
1. **Parse every question.** List them internally so none is dropped.
2. **Open warm** — time-of-day greeting + name ("Good morning Mr [Name],").
3. **Answer each ask** directly; make the product sound appetizing where natural.
4. **Echo customizations** back clearly.
5. **State price plainly** when the order is set — no burying costs.
6. **Route payment** — offer an SMS link; ask for the number in writing.
7. **Confirm** post-payment with the full summary (item + customizations + pickup date + time + full address).
8. **Sign** the canonical block (info@cheesetoshare.us · (407) 494-4263).
9. **QA** before send (checklist below).

## QA checklist (before any send)
- Correct sender identity + signature (info@cheesetoshare.us · (407) 494-4263)?
- Every question answered; customizations echoed?
- Date/time/location included if relevant?
- Correct channel (email default; SMS = payment only)?
- Warm without becoming sloppy; obvious next step?
- Sounds like CTS, not a generic template?

---

## Sequence 1 — Custom Order Inquiry → Confirmed Order

**Step 2 — Reply to inquiry**
```text
Subject: Re: [their subject line]
Preview: Here's everything you need — let us know how you'd like to proceed.

Good [morning/afternoon] Mr [Name],

Thank you so much for reaching out!

[Answer question 1 directly]
[Answer question 2 directly]
[Answer question 3 directly]

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

Best regards,
[Signature]
```

**Step 10 — Post-payment confirmation** *(critical: exact item, customizations, pickup date, time, full location — every time)*
```text
Subject: Your order is confirmed for [Day, Date]
Preview: Full details inside — date, time, location, and everything you ordered.

Good [morning/afternoon] Mr [Name],

Thank you! We've received your payment and your order is confirmed.

Order summary:
- [Item + customizations]
- Pickup: [Day], [Date] at [Time]
- Location: 3801 Avalon Park E Blvd, Ste. 150, Orlando, FL 32828

If you need anything before pickup day, don't hesitate to reach out. We look forward to seeing you!

[Signature]
```

**Step 11 — Order ready** (ultra-short)
```text
Subject: Your order is ready

Hi Mr [Name]!

Your order is ready 😊

[Signature]
```

---

## Sequence 2 — Same-Day / Returning Customer
Reply fast, match energy, don't overcomplicate.
```text
Subject: Got it — you're all set!

Hello good morning Mr [Name]!!!

Yes! Of course!! [emoji if tone matches]

[If seasonal: Happy [Holiday] to you!!!]

[Signature]
```

---

## Sequence 3 — Catering Inquiry → Booking
Full flow + intake in [[03-catering-inquiries]]. Key templates:

**Step 2 — Gather details**
```text
Subject: Re: [their subject line]
Preview: A few quick questions so we can put together the right proposal.

Good [morning/afternoon] [Name],

Thank you for reaching out — we'd love to help make your event special!

To put together the best proposal, a few quick questions:
- What's the occasion or event type?
- Approximate date and time?
- Roughly how many guests?
- A style in mind — grazing board, spread, individual servings?
- Any dietary restrictions we should know about?

Once we have those details, we'll put together some options for you.

Warm regards,
[Signature]
```

**Step 6 — Booking confirmation + deposit** *(50% holds the date; Luis approves the quote)*
```text
Subject: Let's lock this in — deposit details inside

Good [morning/afternoon] [Name],

Here's a summary of what we're confirming:

Event: [Type]
Date: [Date + Time]
Location: [Venue or pickup address]
Order: [Items + presentation]
Total: $[X]
Deposit due: $[X] (50%) to confirm your date

Please send us your phone number and we'll text a payment link right away.

[Signature]
```

---

## SMS rules (payment only)
- Never initiate SMS without the number provided in writing.
- Payment-link-focused only. No marketing, no routine order updates.
- Once paid, confirm the record back in **email**.
- SMS close: "Luis, Cheese To Share".

## Don'ts
- Don't answer 4 questions and silently skip the 5th.
- Don't quote catering beyond standard tiers without Luis → [[07-escalation-rules]].
- Don't send a post-payment confirmation missing date, time, or full location.

See also: [[01-brand-voice]] · [[03-catering-inquiries]] · [[08-examples-customer-emails]]
