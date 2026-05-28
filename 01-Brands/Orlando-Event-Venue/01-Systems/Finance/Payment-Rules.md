---
brand: Orlando-Event-Venue
area: systems
subarea: finance
note_type: system
status: review
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Internal DNA PDF; website reconciliation pending"
owner: Luis
last_updated: 2026-04-21
sensitivity: internal
related_notes: ["[[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Pricing-Logic|OEV Pricing Logic]]", "[[01-Brands/Orlando-Event-Venue/00-Brand-Core/Source-Reconciliation|OEV Source Reconciliation]]"]
hub_role: child
tags: [oev, payment]
---

# OEV Payment Rules

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Pricing-Logic|OEV Pricing Logic]]

## Related
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Source-Reconciliation|OEV Source Reconciliation]]

## Current Internal Rule
A 50% deposit is required to hold the date, with the remaining 50% due per reservation terms.

## Business Meaning
The deposit is the first true commitment event and should be treated as the main booking conversion milestone.

## Warning
This rule must be reconciled against any public website or checkout messaging that suggests a different booking promise.


---

## Update Log

### 2026-05-20 — No-deposit framing + non-profit discount mechanics from Luis × Non-Profit Inquiry call

Source: [[01-Brands/Orlando-Event-Venue/04-Training/Source-Calls/2026-05-20_Luis_NonProfit_Inquiry|Source Call 2026-05-20]]

#### Canonical: OEV does not charge "deposits"

The 50% upfront payment is **not a deposit.** Luis explicitly rejects the word on customer-facing calls. It's framed as **"holding the date"** or **"50% to lock."**

**Rationale (Luis's own words):** "We don't charge deposits because we mainly work with community and trusted individuals and organizations. There's no need to charge deposits."

This framing is intentional. It positions OEV as community-aligned, not transactional.

#### Payment structure
- 50% paid online at the time of booking → holds the date
- Remaining 50% paid before the event (per Communication Manual reminder flow)
- Cleaning fee + add-ons applied to total before the 50/50 split

#### Reps must never say
- "We need a deposit"
- "Put down a deposit"
- "Your deposit is..."
- "Non-refundable deposit"

#### Reps must say
- "50% holds your date"
- "Half upfront, half before the event"
- "Pay half to lock it in"
- "Half now, half later — that's all"

See [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Language-Rules|Language Rules]] for full canonical phrasing.

#### Non-profit discount mechanics (new)

Two separate non-profit offers exist:

| Booking days | Discount | Mechanic | Requires |
|---|---|---|---|
| Mon–Fri | 50% off base rental | Code applied to base rental line | Proof of non-profit status |
| Sat–Sun (weekend) | $199 cleaning-fee waiver | Code applied to cleaning fee line | Proof of non-profit status |

**Sales rep workflow:**
1. Confirm the customer is a registered non-profit (501(c)(3) or equivalent).
2. Request proof: 501(c)(3) letter, EIN documentation, or non-profit registration.
3. Apply the matching discount to the booking.
4. Document the discount and proof in the customer record (GHL + Admin).
5. Tag the customer for commission tracking.

**Pending reconciliation:** confirm with Luis whether a non-profit booking a Fri+Sat+Sun multi-day event can stack the weekday 50%-off-base discount on the Friday booking with the weekend $199-cleaning-fee-waiver on the Saturday and Sunday bookings. Default assumption: yes, since each day is a separate reservation, but verify before quoting.

#### Multi-day payment workflow (new)

Each day is a separate reservation. Each reservation requires its own 50% to hold.

For a 3-day booking:
- Day 1 reservation: 50% to hold Day 1
- Day 2 reservation: 50% to hold Day 2
- Day 3 reservation: 50% to hold Day 3

Total upfront cash = 50% of (Day 1 + Day 2 + Day 3).

**Communication rule:** when quoting a multi-day total over email, break it down per day with each 50% line item visible. Do not present a single combined "50% deposit" number — it breaks the language rule and obscures the structure.
