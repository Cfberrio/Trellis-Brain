---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Retention — 'Churn Checklist #3: Incentivize Customer Activation' (pp. 22–23); Pro Tip: Usage Churn (p. 23)"
sensitivity: internal
hub_role: leaf
book: Retention
---

# Hormozi — Activation Incentives

## Parent
- [[00-Book-Home|Retention — Book Home]]

## Purpose
Lever #3 of the [[Hormozi-Churn-Checklist|Churn Checklist]]. Once activation behavior is identified ([[Hormozi-Activation-Points|lever #1]]) and customers are onboarded toward it ([[Hormozi-Customer-Onboarding|lever #2]]), make it worth their while to keep doing it. Defines the unlockables palette and — critically — the **post-churn-point timing rule**: place additional unlocks just past the periods where customers historically cancel.

## Core Idea
> "A vast majority of cancellations come from people in the bottom two tiers of engagement. The more a customer uses the product, the longer they stay."

Engagement causes retention. Therefore: **reward engagement directly**, and **time additional rewards to land just past the moments customers usually leave.**

## Framework / Structure

### The unlockables palette
Reward types that work for activation incentives (Skool examples — generalizable):
- **Courses that unlock** at engagement levels.
- **1-on-1 consulting calls** — single calls or bundles, unlocked at duration or status milestones.
- **Tickets to live or virtual events.**
- **Higher-tier call access** (e.g., a separate weekly call only available above level X).
- **Status indicators** — custom badges, profile images, public flags marking the customer as "in."
- **Permanent unlocks at hard-to-reach levels** — Skool's level 8 unlock = free lifetime access.

The pattern: activation behavior → recognition + new access. Status unlocks (badges, public callouts) are nearly free to operate and disproportionately effective; they convert engagement into identity.

### Post-churn-point timing rule
> "By putting some incentives just after major churn points, you can retain more customers on the edge. Easy and effective."

If most customers leave after month 3, put a noticeable unlock at month 4. The customer arriving at the "should I cancel?" moment in month 3 has a visible reason to stay one more cycle. By month 4, the unlock is delivered, identity is reinforced, and the original churn moment has passed.

Recommended unlock placement (Hormozi default):
- One unlock just past the average customer lifespan.
- One unlock 30 days after that.
- One unlock 3 months after that.
- One unlock another 3 months after that.

The cadence is "tighter near the cliff, wider after the cliff is crossed." Pull from the unlockables palette above.

### Two distinct purposes
Activation incentives do two different jobs simultaneously:
1. **Reward activation behavior** (incentivize the use that leads to retention).
2. **Reward duration itself** (incentivize staying past the typical churn window).

Hormozi treats them as one lever because they share the same delivery mechanic (unlockables) but the design intent differs. Operators should plan **both** sets of unlocks.

### Usage Churn (the leading-indicator complement)
A Pro Tip embedded in this section: **"Usage Churn"** is the state of being subscribed but no longer using the product.

- Annual contract + 6-month usage stop → almost-certain non-renewal.
- Monthly subscription + 2-week usage stop → cancellation likely within next billing cycle.

**Operator move:** intercept the moment usage drops; re-onboard them; activate the unlockable they were close to. Usage Churn detection makes this lever's incentives *targeted* — you can deliver a targeted unlock right when the customer is drifting.

This concept also appears in [[Hormozi-Activation-Points|Activation Points]] (it is a leading-indicator construct) and is the link between the two levers.

## Strategic Implications
- **Status > stuff.** Custom badges, public callouts, and "you're in" indicators outperform their cost per unit of retention. They convert behavior into identity, and identity is harder to cancel than a subscription.
- **Timing beats magnitude.** A small unlock placed 1 day past the typical cancellation cliff outperforms a large unlock placed at random. Cliff-aware design is the lever's force multiplier.
- **Incremental ship is fine.** Operators do not need the full unlockables matrix on day one. Each unlock added has a positive marginal effect on its own — start with one cliff-aligned unlock, then add.
- **Engagement tier segmentation is what makes this work.** Without tier data, incentives spray; with tier data, incentives target. The infrastructure to segment engagement is a prerequisite for this lever's full effect.
- **Usage Churn intercepts pay back asymmetrically.** A handful of saves per month against a near-zero cost (an automated nudge plus an operator follow-up) often funds the entire retention budget.

## Practical Use
1. **List your engagement tiers.** Map customer behavior into ~3–5 tiers from "barely active" to "deeply active." This is the targeting layer.
2. **Map current cancellation timing.** What month do most customers leave? (e.g., month 3, month 6, month 12).
3. **Design the activation-behavior unlocks first.** Pick 2–3 unlockables from the palette tied to specific tier thresholds.
4. **Design the cliff-aware unlocks second.** Place one unlock just past each major churn window. Pull from the palette.
5. **Add status mechanics universally.** Badges and public callouts cost almost nothing operationally; ship them broadly.
6. **Stand up Usage Churn detection.** Define usage thresholds; flag customers below threshold; trigger the intercept playbook.
7. **Re-test placement annually.** Cancellation timing drifts as the product / customer base changes; re-map the cliffs.

## Notes / Limits
- **Unlocks cannibalize the core if they replace it.** The unlockables palette is *additional* value — courses on top, calls on top, status on top. If unlocks become substitutes for the main offer, the main offer's value perception erodes.
- **Status mechanics work only when public.** A badge nobody sees is an internal flag, not a status signal. Public visibility is required for the identity effect.
- **"Free for life at level 8" can backfire if level 8 is too easy.** Set the bar where reaching it is genuinely a meaningful achievement and a meaningful retention investment.
- **Usage Churn intercepts are awkward when overdone.** Three nudges in a week feels like surveillance. Once-per-cliff is the rule.

## Source Basis
- *$100M Playbook: Retention*, "Churn Checklist #3: Incentivize Customer Activation" (pp. 22–23) — engagement → retention rule; Skool unlockables list (courses, 1-1 calls, tickets, higher-tier calls, badges, level-8 free-for-life); post-churn-point unlock placement rule with default cadence.
- *Retention*, "Pro Tip: Usage Churn" (p. 23) — usage-decline-precedes-cancellation; intercept window; annual / monthly examples.
- Indexed in [[Hormozi-Retention-Source-Map|Retention — Source Map]].

## Related
- [[Hormozi-Activation-Points|Hormozi — Activation Points]]
- [[Hormozi-Customer-Onboarding|Hormozi — Customer Onboarding]]
- [[Hormozi-Customer-Journey-Milestones|Hormozi — Customer Journey Milestones]]
- [[Hormozi-Churn-Checklist|Hormozi — Churn Checklist]]
- [[Hormozi-Value-Per-Second|Hormozi — Value Per Second]]
- [[00-Book-Home|Retention — Book Home]]
- [[Hormozi-Retention-Source-Map|Retention — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]
