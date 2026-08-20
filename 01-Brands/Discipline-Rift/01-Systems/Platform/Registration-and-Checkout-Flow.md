---
brand: Discipline-Rift
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/superpowers/specs 2026-06-22-existing-parent-login-flow, 2026-06-22-stripe-payment, 2026-06-25-self-serve-reenroll, 2026-08-01-pending-payment-resume + commits Jul–Aug 2026"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - platform
  - registration
---

# Registration and Checkout Flow

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|DR Platform Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Payments-Fees-and-Receipts|Payments, Fees and Receipts]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Team-Status-and-Season-Model|Team Status and Season Model]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Waitlist-System|Waitlist System]]
- [[01-Brands/Discipline-Rift/06-DNA/Conversion|DR Conversion DNA]]

## The funnel
Every entry point routes to one action: **REGISTER**, which always opens with "Find Your School".

```
Find your school → pick team → parent identity (OTP) → student details
→ review + coupon → Stripe Checkout → paid → confirmation + receipt
```

## Parent identity — OTP, not passwords
Parents authenticate with a one-time code. Field-level fixes that mattered more than they sound:
- iOS hold-to-paste menu was missing on the OTP field. Fixed.
- Codes pasted with surrounding whitespace are accepted, and the field carries one-time-code autofill.
- "Use a different account" resets the account state instead of leaving stale identity behind.

Every one of these was a real drop-off. The OTP step is the narrowest part of the funnel and deserves that level of attention.

## Returning parents — re-enroll fast path
A returning parent does not repeat the full wizard. They get a **re-enroll fast path** with team search, and the team picker lists **only teams with `status = 'open'`** so a parent can never start a registration into a team that cannot accept them.

## Abandoned checkouts resume
Before August 2026, a parent who abandoned checkout and came back was told they were **"already enrolled"** — a dead end that read as a bug and silently lost paid-traffic conversions. Now an unpaid enrollment is **resumed** instead of blocked.

Related mechanic: an unpaid seat is held for **5 minutes**, then released. Long enough to complete payment, short enough that a full team is not fake-full.

## Scarcity and honesty
The register surface shows an animated **"Few Spots"** badge instead of an exact spot count. Exact counts invited disbelief and went stale between renders; the badge conveys urgency without asserting a number the system cannot guarantee.

## Instrumentation
The funnel is measured end to end in the first-party ledger, and mirrored to Meta where consent allows:

`landing → register_started → CompleteRegistration → InitiateCheckout → Purchase`, plus an `otp_sent` step added in August 2026 to expose losses at the identity gate.

See [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Tracking-and-Attribution|Meta Tracking and Attribution]] for the event contract and idempotency rules.

## Standing rules
- Never show a price before the payment step. Before that: "low cost, everything included".
- The Value Guarantee — 100% refund anytime during the season — is repeated at every decision point.
- A registration that cannot be completed must explain the reason and offer the next action (waitlist, another team, contact), never a dead end.
