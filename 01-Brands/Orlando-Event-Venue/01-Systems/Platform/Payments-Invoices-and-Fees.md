---
brand: Orlando-Event-Venue
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT docs/features/INVOICES.md, docs/features/STRIPE-BALANCE-CONNECT-GHL.md, docs/features/REVENUE-REPORTS-SCHEMA.md + commits Jun–Aug 2026"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - platform
  - finance
---

# Payments, Invoices and Fees

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Payment-Rules|OEV Payment Rules]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Pricing-Logic|OEV Pricing Logic]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/General-Invoice-Templates|General Invoice Templates]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]]

## There are three different "invoice" systems
Do not treat them as one. They have different tables, different emails and different state machines.

1. **Booking deposit / balance** — the website flow. Deposit (typically 50%) then remaining balance, both through Stripe Checkout.
2. **Add-on invoice on a booking** — extra services sold after the booking exists: production packages (per hour), optional services (flat rate), bar service (per guest).
3. **Standalone invoice** — an invoice with no booking attached, including recurring invoices.

## Remaining balance — the reference pattern
The balance flow is the cleanest example of the platform's payment pattern and is the one to copy for other venues.

1. `create-balance-payment-link` authenticates, then applies **state guards** — it refuses to build a link for a booking in the wrong state.
2. The processing fee is computed **dynamically** at link-build time, not stored as a magic number.
3. The Checkout Session carries a **Stripe Connect transfer**, so the venue's share moves automatically rather than being reconciled by hand.
4. Everything needed for the receipt is **persisted before** redirecting the client. This is what makes the receipt reproducible if the webhook is delayed.
5. The direct balance email is **manual only** — the automatic path goes through the scheduled job.
6. `stripe-webhook` confirms the payment, routes on `payment_type`, marks the booking, and sends the balance confirmation with a PDF receipt.
7. `sync-to-ghl` hands a booking snapshot to GoHighLevel, with send guards and retry resilience.

## Processing fee
The processing fee is persisted across **all** monetary tables. Before June 2026 it was computed in some surfaces and not others, which made invoice totals disagree with Stripe. The fix was to store it everywhere and add a fee-integrity test suite. The same pattern was later ported to Discipline Rift — see [[01-Brands/Discipline-Rift/01-Systems/Platform/Payments-Fees-and-Receipts|DR Payments, Fees and Receipts]].

Revenue reports were also corrected to match Stripe on every surface, not just the main report.

## Receipts and documents
- Deposit and balance confirmations attach an **itemized PDF receipt**.
- Deposit/balance receipt PDFs are titled **"Invoice"** (renamed 2026-07-23) because clients were forwarding them to accounting.
- Confirmation emails are hardened: alert on PDF generation failure, timezone-safe dates, ASCII-safe subject lines so Gmail renders them, and whitespace-only lines stripped before quoted-printable encoding (the cause of garbled emails and stray `=20`).

## Coupons and discounts
Coupons support a `total` discount target in addition to line-level targets. The active public offer is **PLAN50** via the Event Planning Kit popup; `HOST100`, `SAVE100` and `SAVE50` are deactivated. See [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit|Lead Magnet — Event Planning Kit]].

## Redirects and conversion tracking
- Stripe redirects land on the real domain with state-aware confirmation pages, after a period where the fallback pointed at a domain that did not serve the app.
- A GA4 purchase conversion event fires on booking confirmation. See [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Google-Ads-Post-Mortem-2026-06|Google Ads Post-Mortem — June 2026]] for why this instrumentation was missing during the June campaign.

## Rules to keep
- Money never moves the operational axis of the booking.
- The fee formula has one source of truth; if it is duplicated client and server, the two copies must be byte-identical and covered by a round-trip test.
- Persist before redirecting. A receipt that cannot be rebuilt is a support ticket.
