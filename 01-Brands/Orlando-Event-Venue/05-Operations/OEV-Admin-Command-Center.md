---
brand: Orlando-Event-Venue
domain: operations
area: tools
subarea: admin-command-center
note_type: canonical
status: active
source: curated + public-site + oev-dna-pdf
canonical: true
last_updated: 2026-04-27
used_for_ai: true
sensitivity: internal
hub_role: child
---

# OEV Admin Command Center

## Parent
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|Orlando Event Venue - Brand Home]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Sales-Home|OEV Sales Home]]

## Children
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Lead-Definition|OEV Lead Definition]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Sales-Process|OEV Sales Process]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Sales/Follow-Up-Rules|OEV Follow-Up Rules]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Pricing-Logic|OEV Pricing Logic]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Payment-Rules|OEV Payment Rules]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Collection-Process|OEV Collection Process]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/KPIs|OEV KPIs]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Source-Reconciliation|OEV Source Reconciliation]]

## Related
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Positioning|OEV Positioning]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Offers|OEV Offers]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Value-Proposition|OEV Value Proposition]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Constraints|OEV Constraints]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Opportunities|OEV Opportunities]]
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-Staff-Operations-Console|OEV Staff Operations Console]]

## Strategy References
Deferred — Value-Equation, Lead-Magnets, Trust-Building, Referral-Loops, Testing-Loops

## Purpose
This note defines what the **admin-side operating system** of Orlando Event Venue should help Luis or any admin/operator do quickly and accurately. It is not just a dashboard description. It is the control center for demand, booking conversion, website alignment, payment movement, event readiness, and post-event closeout.

This note should be used when the question is any variation of:
- What is happening with leads right now?
- What is blocking a booking from becoming cash?
- What website promise is creating friction or mismatch?
- Which events are not ready yet?
- What should admin do next today?

## Core Job Of This Tool
The admin command center exists to answer five things without forcing the team to open five systems:

1. **Demand** — where inquiries are coming from, what they are asking for, and whether they fit OEV.
2. **Conversion** — who is close to paying a deposit, who is stuck, and why.
3. **Readiness** — which confirmed events are truly ready and which still have missing inputs.
4. **Cash movement** — what is paid, what is pending, and what needs follow-up.
5. **Alignment** — whether the website, the quoting logic, and the actual operating rules are saying the same thing.

## What This Tool Must Represent
At minimum, this tool should unify three layers of truth:

### 1. Public-Facing Promise Layer
What OEV currently tells the market through the website:
- modern Orlando venue framing,
- corporate events, workshops, and celebrations,
- up to 90 guests,
- 90 chairs + 10 tables,
- prep kitchen,
- two bathrooms,
- free parking,
- cleaning fee,
- hourly and day pricing,
- optional production capabilities,
- simplified booking path.

### 2. Commercial Logic Layer
What the internal OEV DNA says must happen for the business to work:
- hourly bookings are structured around a 4-hour minimum,
- cleaning is required,
- the buyer must fit the rules,
- the date should be blocked through a 50% deposit,
- production packages are required when technical equipment is involved,
- certain event types or requests should be disqualified early,
- add-ons should only appear when they solve a stated obstacle,
- truthful urgency should be used only when real.

### 3. Operational Readiness Layer
What has to be true for an event to move from “won” to “safe to execute”:
- client fit is confirmed,
- date/time are locked,
- guest count is valid,
- bar service package confirmed (or confirmed as None),
- bar service vendor assigned if package is selected (vendor notified via GHL trigger),
- package/add-on needs are clear,
- final payment plan is clear,
- cleaning staff assigned,
- inspection flow is ready,
- review capture path exists.

## What The Admin Dashboard Should Let You See At A Glance

### A. Lead Intake Snapshot
This section should answer:
- how many inbound leads came in today,
- by source,
- by event type,
- by urgency,
- by fit level,
- by response status.

Useful fields:
- lead source,
- event type,
- requested date,
- guest count,
- alcohol need,
- A/V need,
- current stage,
- assigned owner,
- next follow-up time.

### B. Booking Conversion Pipeline
This section should answer:
- who is still browsing,
- who received pricing,
- who is quote-ready,
- who received the booking link,
- who has not paid deposit,
- who has paid deposit,
- who is confirmed,
- who is at risk of going cold.

Recommended stage logic:
- New Inquiry
- Qualified / Fit Confirmed
- Quote Sent
- Booking Link Sent
- Deposit Pending
- Confirmed
- Pre-Event Ready
- Event Complete
- Closed / Review Requested

### C. Website-to-Sales Alignment Section
This is one of the highest-value uses of the admin tool.

It should not only show demand. It should surface **mismatch risk** between what the site says and what sales/ops require.

Examples of mismatch risk:
- site sounds frictionless but sales depends on rule-heavy compliance,
- public pricing sounds simpler than the true minimum booking economics,
- site implies no deposit or unclear deposit expectations while internal logic depends on deposit to block dates,
- site attracts event types that ops does not really want,
- site CTA invites broad demand but qualification rules are narrow.

This section should answer:
- what promise the website is making,
- what buyers are actually expecting,
- where friction starts,
- what copy or checkout logic needs updating.

### D. Revenue / Payment Control
This section should answer:
- who owes a deposit,
- who owes final payment,
- which invoices are incomplete,
- what events are blocked due to payment uncertainty,
- what the average booking value is,
- what attach rate exists by production or execution add-on,
- where margin is being lost.

Core fields:
- invoice total,
- deposit due,
- deposit paid,
- balance due,
- all services selected (each rendered as a conditional line item — only appears if selected),
- bar service package + subtotal (if selected),
- booking value,
- payment status,
- follow-up owner.

**Invoice structure — all services as conditional line items:**
```
BASE RENTAL
  [Hourly / Daily] Rental      [X] hrs × $140.00       $[amount]
  Cleaning Fee                                           $199.00

SERVICES                          (only render if selected)
  AV — [Package Name]          [X] hrs × $[rate]        $[amount]
  Setup & Breakdown                                      $100.00
  Tablecloth Rental             [qty] × $5 + $25 clean  $[amount]
  Beverage Station (non-alc.)   [guests] × $6.00        $[amount]
  Bar Service — [Package Name]  [guests] × $[rate]      $[amount]

  Subtotal                                              $[sum]
  Processing Fee (3.5%)                                 $[fee]
  ─────────────────────────────────────────────────────
  TOTAL                                                 $[total]
  Deposit Paid (50%)                                    $[amount]
  Balance Due                                           $[amount]
```
No line renders at $0. If a service was not selected, it does not appear on the invoice at all.

### E. Event Readiness Queue
This should be the admin bridge into staff operations.

It should answer:
- which upcoming events are actually ready,
- which ones still need inputs,
- which ones have staff assigned,
- which ones have unresolved constraints,
- which ones need escalation.

Status suggestion:
- Pending Inputs
- Awaiting Deposit
- Awaiting Final Payment
- Awaiting Package Confirmation
- Awaiting Staff Assignment (includes bar vendor assignment when package is selected)
- Awaiting Vendor Contact (bar package selected, vendor assigned, but `bar_customer_contacted = false`)
- Ready For Ops
- Day-Of Active
- Post-Event Review Pending

**Bar service coordination label — on each booking card:**
- `⚠ Awaiting Vendor Contact` — vendor assigned but task not yet complete
- `✓ Customer Contacted` — vendor marked task complete; coordination confirmed

**Pre-Event Ready gate for bar service:**
A booking cannot move to Pre-Event Ready if `bar_package ≠ None` and `bar_customer_contacted = false`. Admin sees:
```
⛔ Cannot move to Pre-Event Ready.
   Bar service selected but vendor contact not confirmed.
   → Ensure bar vendor is assigned and has contacted the client.
```

## Website Layer — What Admin Needs To Know
This command center must include a condensed operational understanding of the main website, because the site is not just a marketing asset. It is the **front door of qualification and expectation setting**.

### Website’s Core Jobs
The website should:
- attract the right event types,
- frame OEV as professional and controlled,
- communicate minimum economics without overwhelming the lead,
- reduce low-fit inquiries,
- move qualified buyers toward booking or tour,
- hand off cleanly into sales and CRM.

### Website Must Be Evaluated By These Questions
- Does it attract the buyers OEV actually wants most?
- Does it make the venue feel simple without hiding critical constraints?
- Does it explain enough to reduce low-quality inquiries?
- Does it create trust around pricing and process?
- Does it push to the right next step: quote, booking link, tour, or direct contact?
- Does it create avoidable confusion for deposit, alcohol, package, or setup expectations?

### Website Sections The Admin Tool Should Track
- Hero / positioning
- Event-type framing
- Pricing visibility
- Booking CTA structure
- Rules / restrictions visibility
- Production / AV framing
- Tour request logic
- Social proof / reviews
- FAQ or objection handling content

## Recommended Admin Views
If this becomes a real dashboard, these are the views that matter most:

### View 1 — Today’s Booking Board
Focus: fast operational decision-making.

Should show:
- new leads today,
- leads needing response,
- deposit-pending leads,
- confirmed events missing required inputs,
- overdue balances,
- events inside 7 days.

### View 2 — Sales Health
Focus: conversion bottlenecks.

Should show:
- lead volume by source,
- conversion by stage,
- % quote sent,
- % booking link sent,
- % deposit conversion,
- lost reasons.

### View 3 — Revenue Quality
Focus: economics.

Should show:
- average booking value,
- add-on attach rate,
- day-vs-hourly mix,
- cleaning fee consistency,
- production package uptake,
- refunds/cancellations/credits.

### View 4 — Promise Mismatch Log
Focus: website and offer cleanup.

Should show:
- repeated objections,
- repeated confusion,
- repeated rule violations,
- repeated expectation mismatch,
- what copy or process should change.

## Required Data Objects
The admin tool should organize the business around a few stable objects:

### Lead Object
Contains:
- who they are,
- what event they want,
- for when,
- for how many,
- fit level,
- urgency,
- booking status,
- next action.

### Booking Object
Contains:
- event type,
- booked date/time,
- core rental structure,
- add-ons (all services selected: AV package, setup/breakdown, tablecloths, beverage station, bar service),
- bar service package and guest count (if selected),
- bar vendor assigned (name + GHL user),
- bar customer contacted status (`oev_bar_customer_contacted` — toggled by vendor),
- payment status,
- staffing status (cleaning staff + bar vendor),
- readiness status,
- event closeout status.

### Commercial Risk Object
Contains:
- objection type,
- website mismatch,
- disqualification reason,
- late-payment risk,
- rule-compliance risk,
- add-on ambiguity,
- escalation need.

## Operational Questions Claude Should Be Able To Answer From This Note
If Claude uses this note correctly, it should be able to answer:
- What should admin pay attention to today?
- Where are leads getting stuck?
- Is the website attracting the wrong type of inquiry?
- Which stages need automation?
- Which events are not ready for staff handoff?
- What metrics matter most weekly?
- What should be changed in the website, funnel, or payment flow?

## Failure Modes This Tool Must Catch
- Too many low-fit inquiries from the website
- Pricing confusion causing dead leads
- Deposit ambiguity causing delay
- Confirmed events with missing operational inputs
- Add-ons sold without proper execution readiness
- Events moving too late into staff readiness
- Admin manually checking too many places for one answer

## Highest-Leverage Improvements This Tool Should Enable
- Tighter website-to-booking alignment
- Faster lead qualification
- Cleaner deposit conversion
- Better visibility into what is blocking revenue
- Earlier ops readiness detection
- Better weekly decision-making instead of reactive fire drills

## What Must Be Added Once Real Dashboard Screenshots/Exports Are Available
Replace assumptions with the actual:
- page names,
- tab names,
- exact pipeline stages,
- real filters,
- real field names,
- actual automations,
- actual card/column logic,
- real KPI calculations.

## Build Standard For This Note
This note is only useful if it helps someone:
- audit the website,
- improve the booking funnel,
- diagnose admin bottlenecks,
- design a better dashboard,
- or route Claude to the right operational context.

If it becomes a vague description of “a dashboard that shows things,” it has failed.
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Automations|OEV GoHighLevel Automations]]