---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-4977 (Developer/OEV/EMAILS WEBSITE) pages 8cqnrff-10257, 8cqnrff-10717, 8cqnrff-10737"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# OEV General Invoice Templates (Stripe)

## Parent
- [[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home|OEV Communication Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Booking-Calendar-Sequence|Booking Calendar Sequence]]
- [[01-Brands/Orlando-Event-Venue/06-DNA/Money-Model|OEV Money Model]]

## Purpose

Stripe-driven invoice email templates for standalone (non-booking) invoices. Three templates: invoice send, admin confirmation, and customer payment confirmation.

## 14. General Invoice — Stripe Link

**Subject:** Invoice INV-YYYYMMDD-XXXX – $XXX.XX | Orlando Event Venue

> **INVOICE**
> Orlando Event Venue
> Reference: INV-YYYYMMDD-XXXX
>
> Hi [Nombre],
>
> You have a new invoice from Orlando Event Venue. Please review the details below and complete your payment at your earliest convenience.
>
> **DESCRIPTION**
> [Título del invoice]
> [Descripción del invoice si existe]
>
> Amount Due: $XXX.XX
>
> [ Pay Now ]
>
> If the button doesn't work, copy and paste this link:
> https://checkout.stripe.com/...
>
> If you have any questions about this invoice, simply reply to this email and we'll be happy to help.
>
> Orlando Event Venue
> 3847 E Colonial Dr, Orlando, FL 32803
>
> *This is an automated email. Please keep it for your records.*

## 15. General Invoice — Payment Confirmation Admin (Internal)

**Subject:** Invoice Paid: INV-YYYYMMDD-XXXX – $XXX.XX

> **INVOICE PAID**
> A standalone invoice payment has been received.
>
> **AMOUNT RECEIVED**
> $XXX.XX
>
> **Invoice Details:**
> Invoice: INV-YYYYMMDD-XXXX
> Title: [Título del invoice]
> Customer Email: customer@email.com
> Amount: $XXX.XX
>
> *This is an internal notification. Do not forward to customers.*
>
> Orlando Event Venue - 3847 E Colonial Dr, Orlando, FL 32803

## 16. General Invoice — Payment Confirmation Guest

**Subject:** Payment Confirmation — INV-YYYYMMDD-XXXX | Orlando Event Venue

> **PAYMENT CONFIRMATION**
> Orlando Event Venue
> INV-YYYYMMDD-XXXX
>
> Hi [Nombre],
>
> Thank you for your payment! Here's a summary of the transaction:
>
> **PAYMENT COMPLETE**
> $XXX.XX
>
> Invoice: INV-YYYYMMDD-XXXX
> Description: [Título del invoice]
> Status: Paid
>
> Please keep this email as your receipt. If you have any questions, simply reply to this email and we'll be happy to help.
>
> Orlando Event Venue
> 3847 E Colonial Dr, Orlando, FL 32803
>
> *This is an automated email. Please keep it for your records.*

## Invoice format

- **Reference format:** `INV-YYYYMMDD-XXXX` (e.g., `INV-20260225-0001`)
- **Numbering:** sequential per day (0001, 0002, ...)
- **Payment processor:** Stripe
- **Currency:** USD

## When to use a general invoice (vs booking invoice)

Use general invoice for:
- Damage / penalty fees (late cleanup, no-show, restoration)
- Standalone services not tied to a booking (consult, photo session)
- Refund corrections / balance adjustments
- Add-on services billed post-booking

For booking-related payments (deposit + balance), use the [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Booking-Calendar-Sequence|Booking Calendar Sequence]] templates instead.
