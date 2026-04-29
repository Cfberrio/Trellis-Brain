---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Retention — 'Churn Checklist #1: Figure Out Your Activation Points' (pp. 17–19); Pro Tip: Usage Churn (p. 23)"
sensitivity: internal
hub_role: leaf
book: Retention
---

# Hormozi — Activation Points

## Parent
- [[00-Book-Home|Retention — Book Home]]

## Purpose
Lever #1 of the [[Hormozi-Churn-Checklist|Churn Checklist]] and the highest-leverage move in the entire Retention playbook. Defines what an activation point is, how to find it via top-20% common-factor analysis, and how to use it to update both messaging (acquire the right customers) and onboarding (drive every new customer to it). Without an identified activation point, the rest of the Churn Checklist has no target.

## Core Idea
> "Every customer that does (X thing) or gets (Y result) stays for longer than customers who don't."
>
> "All roads lead to activation."

An activation point is a **leading indicator of retention** — a behavior or result that predicts long-stay customers. Find the one (or two) thing your top-20% customers do that your churned customers do not, then engineer the entire business to drive every new customer to do that thing as fast as possible.

## Framework / Structure

### Definition
An activation point is the specific, observable, early behavior that predicts long-term retention.

Template: *"Every customer that does X or gets Y stays for longer than customers who don't."*

Worked examples:
- **B2B service company:** first time they get leads.
- **SaaS company:** first time they log in and see the dashboard with their own data.
- **Physical product:** first time they use the consumable product.
- **Skool host:** gets at least 3 group members.
- **Skool member:** reaches engagement level 3.
- **Gym Launch operator:** recoups their investment within 30 days (this is the [[../06-Fast-Cash/Hormozi-Fast-Cash-Play|Fast Cash Play]] — 8% → 3% churn in 6 months).

Engagement levels work too: Skool segments customers into engagement tiers; tier 3 = highest retention. The exact threshold matters less than (a) recognizing engagement matters and (b) segmenting customers by it so retention tools can target precisely.

### How to find your activation point (5-step recipe)
1. **Find your churned customers.** Pull all data you can about everyone who left.
2. **Filter to customers who stayed at least 3 months.** (3 months is convention; pick whatever timeframe fits your sales cycle and price point.)
3. **Sort that list by who spent the most.** Take the **top 20%**.
4. **Learn everything you can about them** — demographics, psychographics, income, business size, revenue. Survey if data is missing.
5. **Identify how they used your product and how you treated them.** Apply the [[Hormozi-Common-Factors-Method|Common Factors Method]]: overlap factors across the top 20%; the recurring ones are your activation-point candidates. Narrow to ~5 factors and test down the list.

> "Some will matter and some won't. But find the ones that do, and you'll win big."

### Two outputs (both mandatory)
Once the activation point is identified, two updates follow.

**Output 1 — Update messaging.**
Re-target paid ads, organic content, and sales copy to the *profile* of the people who hit the activation point. Stop selling to your whole TAM; start selling to the segment that historically activates and stays.

> Gym Launch case: a competitor sold the same number of people but Hormozi made **70× more profit** because Hormozi's customers were worth $42,000 (vs. competitor's $5,000) in year one. Same CAC, same audience size — but Hormozi only ran ads to people who matched the top-20% activation profile. Result: 70× LTV per acquired customer.

**Output 2 — Update onboarding.**
Redesign onboarding so every new customer is driven to the activation point fast. Do not rely on the customer to find it organically. Make hitting it the explicit goal of week 1.

> Gym Launch case: churn was 8% and the team wanted 4%. Question asked: *"When do people first get value from the product?"* Answer: long-stay customers recouped their investment in the first 30 days. Solution: shipped the [[../06-Fast-Cash/Hormozi-Fast-Cash-Play|Fast Cash Play]] and pushed every client to recoup investment within 30 days. **Churn went 8% → 3% in 6 months.**

Onboarding mechanics live in [[Hormozi-Customer-Onboarding|Customer Onboarding]] (lever #2).

### Usage Churn — the leading indicator of cancellation
A customer still subscribed but no longer using the product is in **usage churn**. They have already churned mentally; the billing has not caught up yet.

- Annual contract, 6-month usage cliff → almost-certain non-renewal at month 12.
- Monthly subscription, 2-week usage cliff → often cancels within the next billing cycle.

**Operator move:** monitor usage at customer level. The moment it drops below the activation threshold, intercept. Do not wait for cancellation. By the time cancellation happens, the save window has usually closed.

(Source physically lives inside the Incentivize Activation section on p. 23 but logically belongs to Activation Points — it is the leading-indicator companion. See also [[Hormozi-Activation-Incentives|Activation Incentives]].)

### "Who > What" — the higher-order play
> "One of the highest-leverage things you can do in a business is simply serve better customers."

Improving a $100M business by 10% returns the same percentage as improving a $1M business by 10% — but 100× the dollars. Activation-point work is also customer-quality work: by selecting for customers who match the top-20% profile, you are not just lowering churn, you are upgrading the whole customer base.

## Strategic Implications
- **Activation point > everything else.** Hormozi calls this the highest-leverage move in retention. Without it, every other lever lacks a target and dilutes effort.
- **Acquisition and retention converge on the same insight.** The activation-point analysis tells you who your best customers are; that profile becomes the targeting input for paid acquisition. One analysis, two outputs, multiplied effect (Gym Launch's 70× profit example).
- **The activation point is a usage variable, not a satisfaction variable.** Surveys ask what people *say*; usage logs show what people *do*. Find activation points in the latter.
- **Drift is real — re-run every 6–12 months.** The customer base evolves; the activation point evolves with it. Re-running the analysis is a recurring operating practice, not a one-time project.
- **Customer-quality upgrade compounds.** Selecting for the top-20% profile means the next year's customer base is denser with high-LTV customers, which makes the *next* activation analysis even cleaner.

## Practical Use
1. **Pull every churned customer record** from the last 12+ months.
2. **Filter to customers who stayed ≥ 3 months** (or your own threshold).
3. **Sort by spend; take the top 20%.**
4. **Survey them or pull behavioral data** — demographics + how they used the product + what you/your team did for them.
5. **Apply Common Factors Analysis** ([[Hormozi-Common-Factors-Method|method]]). List candidate activation points. Narrow to ~5.
6. **Pick the leading 1–2 candidates.** A/B test if dataset allows; otherwise ship and watch the metric.
7. **Update paid + organic messaging** to attract the profile.
8. **Update onboarding** to drive every new customer to the activation point ([[Hormozi-Customer-Onboarding|lever #2]]).
9. **Stand up usage monitoring.** Define the activation threshold; flag any customer whose usage drops below it; trigger an outreach.
10. **Re-test every 6–12 months.** Re-run steps 1–6 to catch drift.

## Notes / Limits
- **Sample size matters.** Top-20% of a small churn sample (e.g., < 30 customers total) produces noisy candidates. With small datasets, supplement with structured customer interviews to reach pattern density.
- **Multiple activation points may exist for multi-product businesses.** Run the analysis per product, not at the company level.
- **Activation points are not goals to advertise.** Customers should not feel manipulated toward "the activation behavior." The point is to remove friction so the right behavior happens naturally.
- **Some businesses have lagging-indicator activation points** (e.g., "had a positive ROI in year 1"). These work for messaging and onboarding design but not for usage-churn intercepts. Pair every lagging indicator with a leading-indicator proxy (an early-stage behavior that correlates).

## Source Basis
- *$100M Playbook: Retention*, "Churn Checklist #1: Figure Out Your Activation Points" (pp. 17–19) — definition; template; Skool examples; 5-step find-your-activation-point recipe; Author Note: All Roads Lead to Activation; Bonus: Update Messaging (Gym Launch 70× profit example); Updating Onboarding (Gym Launch 8% → 3% via Fast Cash Play); Author Note: Who > What; common activation-point examples (B2B / SaaS / physical product).
- *Retention*, "Pro Tip: Usage Churn" (p. 23) — usage-decline-precedes-cancellation rule; intercept window.
- Indexed in [[Hormozi-Retention-Source-Map|Retention — Source Map]].

## Related
- [[Hormozi-Common-Factors-Method|Hormozi — Common Factors Method]]
- [[Hormozi-Customer-Onboarding|Hormozi — Customer Onboarding]]
- [[Hormozi-Activation-Incentives|Hormozi — Activation Incentives]]
- [[Hormozi-Churn-Checklist|Hormozi — Churn Checklist]]
- [[Hormozi-Five-Horsemen-Of-Retention|Hormozi — Five Horsemen of Retention]]
- [[../06-Fast-Cash/Hormozi-Fast-Cash-Play|Hormozi — Fast Cash Play]]
- [[../09-Lifetime-Value/Hormozi-Crazy-Eight|Hormozi — The Crazy Eight]]
- [[00-Book-Home|Retention — Book Home]]
- [[Hormozi-Retention-Source-Map|Retention — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]
