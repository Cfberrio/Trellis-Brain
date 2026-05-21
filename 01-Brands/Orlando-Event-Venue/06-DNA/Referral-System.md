---
brand: Orlando-Event-Venue
area: dna
note_type: leaf
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-7037 page 8cqnrff-4957 (STRATEGY / DNA / OEV / 11) Referral System)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Referral System

## Parent
- [[DNA-Home|OEV DNA Home]]

## Related
- [[Retention|OEV Retention]]
- [[Money-Model|OEV Money Model]]
- [[../05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]
- [[../04-Projects/Venue-Partnerships/Partnerships-Home|Venue Partnerships]]

## Purpose
Trackable, cashflow-safe, capacity-protected partner referral system for Orlando Event Venue.

## 1. What A "Qualified Referral" Is
A referral is qualified ONLY IF all are true:
1. **New lead** (not already in OEV CRM under same phone/email)
2. Fits venue constraints (≤90 guests, rules accepted, beer & wine only)
3. Pays the **50% deposit to block the date**
4. Event reaches **Post-Event inspection complete** (not cancelled / not chargeback)

> Don't pay for "interest." Pay for **real bookings that get delivered**.

## 2. Referral Rewards

Partner chooses one:
- **A) Cash payout** (paid after event closes)
- **B) OEV credit** (higher value, protects cash)

### Standard rewards

**Tier 1 — Corporate / Workshop bookings (ideal):**
- **$100 cash** OR **$150 OEV credit** per qualified booking

**Tier 2 — Personal events (schedule-filler):**
- **$50 cash** OR **$75 OEV credit** per qualified booking

### Bonus (only when it increases margin)
If booking includes **production package for 3+ hours** (Basic/LED/Workshop):
- **+$25 cash** OR **+$40 credit**

### Payout timing (cashflow rule)
- Reward **earned when deposit is paid**
- **Paid 7 days after event end** AND post-event inspection complete (Closed / Review Complete)
- If event cancelled or chargeback → **no payout**

### Stacking rules (prevents margin collapse)
- **Cannot combine** partner referral reward with **$100 Baby Shower Content Credit** (pick one incentive)
- Cannot stack with any other discounts unless approved

## 3. Capacity Controls

### Program throttle rules
1. **Monthly cap per partner:** max **5 qualified payouts/month**
2. **Total program cap:** max **25 qualified payouts/month** (across all partners)
3. **Last-minute rule:** bookings inside **7 days** of event date get **no referral payout** (ops planning protection)

### Green Inventory Rule
Referral rewards apply ONLY IF the event date is in a Green Inventory window:
- **14+ days out** OR
- **Mon–Thu dates** (typically easier ops)

If prime high-demand day (Fri–Sun) inside 14 days → can still accept the booking, but **no referral payout**.

## 4. How Partners Refer

### Method A (recommended) — Unique referral link
Each partner gets a link like:
```
oev-booking.com/availability?ref=PARTNERNAME
```
Lead submits date/time → CRM tags lead automatically.

### Method B (fallback) — Text intro template
Partner texts OEV:
- Name + Phone + Date/Time + Event type + Guest count

Admin tags: `REF–Partner–[Name]`

## 5. Partner-Facing One-Message Script (copy/paste)
> "If you need a venue in Orlando (up to 90 guests), Orlando Event Venue can confirm availability fast.
>
> Use this link to check dates + get pricing: [partner link].
>
> Once you place the 50% deposit, the date is blocked. Beer & wine are allowed (no liquor)."

## 6. Internal SOP (CRM + automation)

### CRM Fields / Tags (required)
- Field: `ref_partner_id`
- Tag: `REF–Partner–[Name]`
- Field: `ref_reward_type` (cash / credit)
- Field: `ref_reward_amount`
- Field: `ref_status` (pending / earned / payable / paid)

### Automation rules

| Stage Trigger | Action |
|---|---|
| Deposit paid → status Confirmed | Set `ref_status = earned`. Create task "Confirm staff assignment" |
| Status → Post-Event | Trigger inspection checklist |
| Inspection complete | Move to Closed/Review Complete |
| Status → Closed/Review Complete | If `ref_status = earned` → set `ref_status = payable`. Auto-generate payout request. Notify partner. |
| 7 days after Closed/Review Complete | Pay cash / issue credit. Set `ref_status = paid` |

## 7. Cashflow Budget Guardrail
- **Max referral payouts/month:** **$1,500 cash** (example: 15 corporate bookings × $100)
- Credits can be higher (future spend) but cap also: e.g., **$2,250 credit/month**

If caps hit → continue accepting referrals, mark as **"rollover"** to next month's payout queue.

## 8. Baby Shower Example (how it fits)
- Partner refers a baby shower lead
- If using the **$100 Content Credit** (review + testimonial trade) → **no partner payout** (avoid stacking)
- If no promo credit applied → partner gets **$50 cash / $75 credit** after event closes

## Active Partner Templates

### Initial Outreach (sample — Caleb / VIPCO partnership pitch)
> Hey Caleb,
>
> Happy Monday, brother. Hope you're doing well.
>
> I wanted to follow up and officially send over the referral partnership idea we discussed for Orlando Event Venue.
>
> We'd love to have you as a referral partner for OEV. The structure is simple:
>
> **Your custom referral code:** We create a custom discount code with your name or company name attached. For example, your code could be **CALEB** or **VIPCO**.
>
> **How it works:**
> - Your referral receives **$50 off** their booking when they use your code at checkout
> - We track the reservation through your custom code
> - For every completed booking made with your code, **you receive $100** as the referral partner
>
> **So in summary:**
> - $50 off for the client
> - $100 referral payout to you for each booked event
>
> **About OEV:** Orlando Event Venue is a modern event space near Downtown Orlando at 3847 E Colonial Dr, Orlando, FL 32803. Flexible booking, no catering restrictions, free parking, simple pricing for corporate events, celebrations, workshops, presentations.
>
> **Highlights:**
> - $140/hour with 4-hour minimum
> - $899 daily special with 24-hour access
> - 90 chairs + 10 tables, prep kitchen, two bathrooms
> - Optional production packages (AV / LED / streaming / presentations)
>
> Let me know if you'd like me to set up your custom code and I can get it ready right away.
>
> Best,
> Luis Torres
> Manager, Orlando Event Venue Team
> 407-974-5979
> orlandoeventvenue.org
> orlandoeventvenue@gmail.com
> 3847 E Colonial Dr Orlando, FL 32803
