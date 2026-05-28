---
brand: Orlando-Event-Venue
area: systems
subarea: finance
note_type: system
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Market DNA + money model DNA"
owner: Luis
last_updated: 2026-04-21
sensitivity: internal
related_notes: ["[[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|Orlando Event Venue - Brand Home]]", "[[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Sales-Home|OEV Sales Home]]"]
hub_role: child
tags: [oev, pricing]
---

# OEV Pricing Logic

## Parent
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|Orlando Event Venue - Brand Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Payment-Rules|OEV Payment Rules]]

## Base Economics
- Hourly rate: $140/hr.
- Hourly minimum: 4 hours.
- Required cleaning fee: $199.
- Hourly minimum booking floor: $759.
- Daily special: $899 + $199 cleaning = $1,098.

## Booking Channel
All bookings are processed online — booking form, payments, quotes, and invoices are fully online. No in-person or phone-only payment paths.

## Pricing Function
Pricing should screen for buyers who need a real venue outcome, not a free or ultra-cheap room.

## Upsell Economics
- Basic package: $79/hr.
- LED package: $99/hr.
- Workshop package: $149/hr.
- Setup & breakdown: $100 flat.
- Tablecloth rental: $5 each + $25 cleaning.

## Bar Service Pricing (per guest)
Bar service is a first-class upsell available for all private events. Quoted and invoiced per guest count confirmed at booking.

| Package | Price/Guest |
|---|---|
| House Beer & Wine | $18.00 |
| Essential Bar | $25.63 |
| Signature Bar (Most Popular) | $32.13 |
| Bespoke Bar | $39.63 |
| Additional Bar Hour (add-on) | $5.00 |

**Quoting rule:** Multiply selected package rate × confirmed guest count. Add as a separate line item on the invoice.
**Discount rule:** Bar service packages are excluded from all discounts including non-profit.
**Sequencing rule:** Present bar service after the client confirms booking type and guest count — not before fit is established.

## Discount Rules

| Discount | Amount | Applies to | Condition |
|---|---|---|---|
| Multi-day workshop | 25% off | Base rental only | 2–3 day booking |
| Large / repeat corporate | Up to 50% off | Base rental only | Management approval required |
| Non-profit | 50% off | Base rental only | Monday–Friday bookings only; proof of non-profit status required |

**Global discount rule:** Discounts apply to base rental only. Never apply to cleaning fee, AV packages, bar service, setup & breakdown, tablecloths, or any other add-on.


---

## Update Log

### 2026-05-20 — Pricing reconciled to live website + new offers from Luis × Non-Profit Inquiry call

Source: [[01-Brands/Orlando-Event-Venue/04-Training/Source-Calls/2026-05-20_Luis_NonProfit_Inquiry|Source Call 2026-05-20]]

This block is the canonical pricing reference. Any conflicting values above are stale.

#### Confirmed pricing (live website, 2026-05-20)

**Rental**
- Hourly: $139/hour, 4-hour minimum
- Daily: $899/day, 24-hour access
- Cleaning fee: $199/reservation (auto-applied)
- Processing fee: 3.5% per transaction

**Production packages (per hour)**
- Basic A/V: $89/hour
- LED Wall: $99/hour (includes Basic)
- Workshop/Streaming: $149/hour (includes Basic + LED)

**Bar service (per guest)**
- House Beer & Wine: $18/guest
- Essential Bar: $25.63/guest
- Signature Bar: $32.13/guest (Most Popular)
- Bespoke Bar: $39.63/guest

**Extras**
- Setup & breakdown service: $199 flat per reservation
- Tablecloth: $5/each + $25 cleaning

#### Included with rental
- Main venue space
- 90 chairs
- 10 tables
- Prep kitchen
- Two bathrooms
- Free parking
- "All day and night" availability for daily rate

#### Pricing logic rules

1. **Discount applies to base rental only.** Never applies to cleaning fee, AV, bar service, or any add-on.
2. **Multi-day bookings = separate reservations.** A Fri+Sat+Sun event is entered as three bookings, each with its own 50% hold. Calculate totals per day, then sum.
3. **Production packages stack inside themselves.** LED includes Basic. Streaming includes both. The package fee is the total — don't add Basic separately when LED or Streaming is selected.
4. **Bar service is per-guest, not per-hour.** Use confirmed guest count, not max occupancy.
5. **Setup & breakdown is flat $199.** Not hourly. Bought once per reservation.
6. **Tablecloths add cleaning every time.** $5 rental + $25 cleaning fee, regardless of quantity rented.

#### Live-quote workflow (canonical sales technique)
When quoting on a call, do not read from this note. Instead, open the live website, book a placeholder date, build the booking with the customer's specs, and read the total off the website. Documented in [[01-Brands/Orlando-Event-Venue/04-Training/Call-Communication-Approach#1. Live-Quote on the Website|Call Communication Approach]].

#### Sample multi-day non-profit quote (from real call)

Friday hourly (5 hr) + Saturday daily, non-profit:
```
Friday — 5 hr @ $139         $695
Friday — cleaning            $199
                             ─────
Friday total:                $894

Saturday — daily             $899
Saturday — cleaning          $199
                             ─────
Saturday total:              $1,098

Two-day subtotal:            $1,992
Non-profit weekend discount: -$199 (waives Sat cleaning)
                             ─────
TOTAL:                       $1,793

50% holds each booking.
```

#### Deprecated / verify with Luis
- Beverage station (non-alcoholic) at $6/person/day — listed historically but not on current website
