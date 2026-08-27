---
title: Policy Decision Tracker
owner: Luis Torres
last_updated: 2026-07-21
status: active
sensitivity: internal
used_for_ai: true
---

# Policy Decision Tracker — 4 Brands

Tracks the blocking decisions across the four website policy packs. Nothing publishes until its brand's blockers are cleared.

**Policy packs:**
- `01-Brands/Orlando-Event-Venue/01-Systems/Legal/OEV-Website-Policies-v1.md`
- `01-Brands/Cheese-To-Share/01-Systems/Legal/CTS-Website-Policies-v1.md`
- `01-Brands/Discipline-Rift/01-Systems/Legal/DR-Website-Policies-v1.md`
- `01-Brands/Trellis-Fields/01-Systems/Legal/TF-Website-Policies-v1.md`

## Blocks all four

| # | Decision | Owner | Status |
|---|---|---|---|
| X1 | Confirm legal entity name, type, and state for each brand (Sunbiz) | Luis | ☐ |
| X2 | Confirm governing law and venue — Florida / Orange County assumed throughout | Luis + counsel | ☐ |
| X3 | Confirm A2P 10DLC campaign registration status per sending number | Cristian | ☐ |
| X4 | Audit each live site for analytics and advertising pixels; complete each Cookie Policy table | Cristian | ☐ |
| X5 | Counsel review pass across all four packs | Luis | ☐ |

## Ranked by exposure

| Rank | Brand | Top blocker | Why it ranks here |
|---|---|---|---|
| 1 | **DR** | Waiver, medical authorization, photo release — none exist | Minors in physical activity on school campuses, with no signed risk documents |
| 2 | **DR** | "100% refund, any time. No windows. No fine print." | Uncapped published promise contradicted by both the alternate guarantee design and actual practice |
| 3 | **DR** | LLC vs non-profit — both stated in writing, one to a school district | Contradictory representations about the contracting entity |
| 4 | **DR** | DRF franchise-adjacent representations with no FDD | "Own a license," territory assignment and loss, $0 cost, stipend |
| 5 | **OEV** | No cancellation or refund policy at all | Customers already asked for the agreement in writing; none exists |
| 6 | **OEV** | Alcohol policy — four contradictory versions live | All four reach customers today |
| 7 | **CTS** | No cancellation or refund policy at all | `Refund-Rules.md` lists it as unknown |
| 8 | **TF** | Entity not confirmed filed; no address, phone, email, or domain | Cannot publish any policy naming a party |

## Per-brand blockers

**OEV** — entity name · cancellation/refund terms · alcohol policy (pick 1 of 4) · governing law · notice address · camera retention period · terms acceptance moved before checkout
**CTS** — entity name · cancellation/refund terms · balance due 24h vs 14 days · delivery and travel fees · sales tax treatment · governing law · define or delete "returning board refund may apply"
**DR** — entity (LLC vs non-profit) · refund policy version · waiver + medical + photo release · ages 6–12 vs K–5 · governing law · DRF franchise review · backend RLS and public buckets before publishing security claims
**TF** — entity filing status · which entity contracts and controls data · Colombia personnel data access · address/phone/email/domain · governing law · commercial terms · IP position · AI provider training-exclusion answer

## Cross-cutting fixes that are not policy work

1. **SMS consent is non-compliant at all three consumer brands.** None has an unchecked opt-in checkbox with frequency, rate, STOP, and HELP disclosures. DR has one combined line. CTS relies on "customer sent their number in writing." OEV has consent text in the voice-agent script but nothing on the popup or booking form.
2. **Marketing and transactional SMS are mixed.** CTS's review-request text and DR's re-enrollment nudges are marketing sent under transactional consent.
3. **Two brands have written rules that contradict their own live automations.** `CTS-Communication-Manual-v2.md:638-655` ("SMS = payment links only") and DR `communication-rules.md:650` ("no SMS as a primary channel"). Both are dead rules that will keep generating contradictions until rewritten.
4. **OEV's terms arrive after payment.** "Your Agreement at a Glance" is a post-payment email, not enforceable acceptance.
5. **Photo/media consent is missing at CTS and DR**, while both actively capture and publish event imagery.
