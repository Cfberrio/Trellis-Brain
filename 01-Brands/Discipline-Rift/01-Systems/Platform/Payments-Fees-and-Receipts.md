---
brand: Discipline-Rift
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/processing-fee-and-receipts.md (ClickUp 86e2e8kqc) + docs/superpowers/specs/2026-06-22-stripe-payment-design.md + commits Aug 2026"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - platform
  - finance
---

# Payments, Fees and Receipts

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|DR Platform Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]]
- [[01-Brands/Discipline-Rift/06-DNA/Money-Model|DR Money Model]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Payments-Invoices-and-Fees|OEV Payments, Invoices and Fees]] — the pattern this mirrors

## Approach
Mirrors OEV: **Stripe Checkout Sessions** with the fee as a separate line item, and the receipt is **DR's own branded email** over Gmail SMTP. No Stripe Dashboard configuration, no Stripe-hosted invoices. Business identity lives in code.

## Processing fee — 3.25% + $0.25
- One source of truth for the formula, duplicated client and server as **byte-identical** files, covered by a round-trip test proving `split(totalWithFee(S)) === S`.
- `fee = round(subtotal¢ × 3.25%) + 25¢`, computed on the **post-coupon** subtotal.
- A **$0 order carries no fee**.
- `create-checkout-session` adds a second Stripe line item labelled **"Processing Fee (3.25% + $0.25)"**. `payment.amount` records subtotal + fee.
- Covers **both** register and re-enroll, since both call the same function.
- The register and re-enroll wizards show an itemized **Processing fee** row and updated total. The fee is visible, never buried.

Worked example: team **$150** → fee **$5.13** → total **$155.13**. With a $20 coupon: subtotal $130 → fee **$4.48** → total **$134.48**.

## Receipt to the parent
The existing payment confirmation (fired by `dr_ghl_registered` when `payment.status → paid`) was upgraded into a real **receipt**:
- A Payment Receipt section itemizing Registration (subtotal) + Processing Fee + **Total Paid**, with paid date and the Stripe payment-intent reference.
- Footer carries the legal business identity: **Discipline Rift · Torres Rivero LLC**, 713 W. Yale Street, Orlando, FL 32804.

The subtotal/fee split is recovered from the charged total with an exact inverse of the fee formula, so no schema change was needed.

## Internal notification
A payment-received notification email goes to the DR inbox on every paid registration, with an ASCII-safe subject line and a Gmail-safe table layout — both were required before the email rendered correctly.

## Rules to keep
- The fee formula has exactly one definition. If it is duplicated for client and server, the copies must be byte-identical and tested together.
- Deploy scope for a fee or receipt change is **frontend publish + `create-checkout-session` + `dr_ghl_registered`**. Missing one of the three ships a visible inconsistency to parents.
- Revenue truth is `payment.status = 'paid'` in the database, never an ad platform's reported conversions.
