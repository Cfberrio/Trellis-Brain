---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Lead Nurture — 'Lead Nurture' intro + Description (pp. 1–4); 'Four Pillars of Lead Nurture' (pp. 5–6); 'Execution Conclusion' (pp. 36–37)"
sensitivity: internal
hub_role: leaf
book: Lead-Nurture
---

# Hormozi — Lead Nurture: Four Pillars

## Parent
- [[00-Book-Home|Lead Nurture — Book Home]]

## Purpose
Umbrella concept of the *Lead Nurture* playbook. Defines the operational scope ("medium-term lead nurture" — the time after a lead expresses interest and before they buy), the three core metrics that govern this layer (schedule rate, show rate, throughput), and the four empirically-validated drivers that move the throughput number. Sets the structural target the four pillar notes operationalize.

## Core Idea
> "If they do not show, they cannot buy."
>
> Show rate is one of the most leveraged numbers in a business. Improving it does not require new leads, new offers, or new ads — it requires reducing the friction between **opt-in** and **showing up to buy**.

The book's empirical premise: across ~20,000 leads/day of portfolio data and 4,000+ daily appointments managed by ALAN, four variables — and only four — correlate strongly with show-up rate:

1. **Availability** — number of open appointment slots.
2. **Speed to contact** — how fast you respond to leads + how soon they can schedule.
3. **Personalization** — how relevant and useful each touch is to the individual lead.
4. **Volume** — how many times you reach out before giving up.

Combined effect: **20–40% lift in revenue is typical; 200%+ is achievable** when all four pillars are run at near-max. At 20% margins, 20–40% revenue lift = 2×–3× profit in year one.

## Framework / Structure

### Scope: medium-term lead nurture
Lead nurture has three time horizons. This playbook addresses only the middle one:
- **Short-term** = the call/text in the moments after opt-in. Covered here under [[Hormozi-Lead-Nurture-Speed|Pillar II: Speed]].
- **Medium-term = the 30-day window between opt-in and sale.** This is the playbook's target. The optimization metric is **30-day show rate**.
- **Long-term** = re-engagement of cold leads (emails, podcasts, content). Explicitly **out of scope** of this playbook ("I cover long-term follow up in other places"). Covered structurally only as the off-ramp at the end of the [[Hormozi-Lead-Nurture-Volume|Volume]] outreach cadence.

### Core metrics (definitions)
The book introduces three metrics that frame every downstream tactic. Use these names — they are referenced across all four pillar notes.

| Metric | Definition | Formula |
|---|---|---|
| Schedule rate | % of engaged leads who schedule an appointment | scheduled / engaged |
| Show rate | % of scheduled leads who show up to the appointment | shown / scheduled |
| Throughput | % of engaged leads who show up | shown / engaged (= schedule rate × show rate) |

Worked example from the book: 100 leads → 50% schedule rate → 50 appointments → 50% show rate → 25 shows → **25% throughput**.

Throughput is the dependent variable. The four pillars are the independent variables.

### The Four Pillars

| # | Pillar | One-line driver | Canonical note |
|---|---|---|---|
| 1 | Availability | If leads cannot schedule, they cannot show. | [[Hormozi-Lead-Nurture-Availability\|Availability]] |
| 2 | Speed | The faster you reach them and the sooner they meet you, the more show. | [[Hormozi-Lead-Nurture-Speed\|Speed]] |
| 3 | Personalization | Relevance and reciprocity raise show probability per touch. | [[Hormozi-Lead-Nurture-Personalization\|Personalization]] |
| 4 | Volume | More touches → more responses → more schedules → more shows. | [[Hormozi-Lead-Nurture-Volume\|Volume]] |

The book closes with a **fifth implicit pillar** in the Execution Conclusion: **execution** — actually doing the boring work, supported by a culture that rewards process. Treated as its own canonical: [[Hormozi-Lead-Nurture-Execution-Culture|Execution Culture]].

### Empirical ranking of pillar leverage
The book ranks Availability as the **single biggest** lever ("more than speed, availability is the biggest predictor… an almost perfect correlation with throughput"). Speed is second. Personalization and Volume compound on top. This ordering matters: an operator with limited bandwidth should fix Availability first, Speed second, then layer Personalization and Volume.

## Strategic Implications

- **Show rate is the lowest-hanging revenue lever in most businesses.** Hormozi's repeated observation: most operators ignore show rate because (a) they think they can't move it, (b) they don't know how, or (c) they have "more important" work. (a) and (b) are wrong; (c) is rarely true. The cost-to-impact ratio of show-rate work beats most other revenue work.
- **The four pillars are independent inputs, not stages.** They are not a funnel. They run in parallel. An operator who only fixes Speed but ignores Availability caps their gain at the slot ceiling. Compound math is multiplicative.
- **Throughput is the right scoreboard.** Measuring schedule rate alone hides ghosting; measuring show rate alone hides booking friction. Throughput captures both. Ranking sales reps on throughput-equivalents (lead-to-close) prevents close-rate myopia — see [[Hormozi-Lead-Nurture-Execution-Culture|Execution Culture]].
- **Long-term nurture is a different game.** Treating cold-list re-engagement as if it were medium-term nurture (high touch frequency, urgency, real-time scheduling) burns the list. Keep them structurally separate.
- **Capacity precedes everything.** Pillars II–IV require sales capacity to absorb the leads they pull through. Operators who cannot staff for fast-response and 7-day reach-out cadences should fix capacity before running this playbook — otherwise the ceiling is hit at the rep level, not the funnel.
- **Pillar I (Availability) gates Pillar II (Speed).** The book's mechanism: opening more slots creates calendar gaps; those gaps become the time during which reps execute fast contact. Fix Availability first to *create the resource* Speed needs.

## Practical Use

Operator diagnostic when show rate is the constraint:

1. **Measure the baseline.** Compute schedule rate, show rate, throughput by source and by rep. (See [[Hormozi-Lead-Nurture-Execution-Culture|Execution Culture]] for the three-metric ranking.)
2. **Score each pillar.** Rate the business 1–5 on each pillar against the book's standards (see each pillar note's Practical Use checklist).
3. **Fix in the empirical leverage order.** Availability → Speed → Personalization → Volume. Avoid the temptation to start with whichever is most "fun" or visible.
4. **Re-measure.** Throughput should move within 30 days for Availability + Speed fixes. Personalization + Volume stack on top in the next 30–60 days.
5. **Wire the culture.** None of the above sticks without execution. Stand up the metrics, the rewards, and the -isms — see [[Hormozi-Lead-Nurture-Execution-Culture|Execution Culture]].

## Notes / Limits

- **Industry baselines vary.** Some industries have structurally higher show rates than others (high-ticket B2B vs. impulse retail). The four pillars apply universally; the absolute throughput number is industry-relative. Aim for "best in class within your industry," not a fixed target.
- **The 4-pillar model is empirical, not theoretical.** It came from machine-learning analysis of ~1M appointment rows, not from first principles. Variables that *should* matter (script wording, rep tenure, time of day) showed weaker correlations than the four pillars. Trust the rank order.
- **Out-of-scope explicitly.** Acquisition (getting opt-ins), offer construction, long-term cold-list re-engagement, and post-sale fulfillment are not addressed here. Use other playbooks for those layers.
- **Compliance matters.** Several Volume tactics (rapid double-dial, multi-channel outreach) are subject to TCPA / regional telecom and privacy law. The book reminds operators to follow local laws — this is a real constraint, not a footnote.

## Source Basis
- *$100M Playbook: Lead Nurture*, "Lead Nurture" intro (pp. 1–3) — COVID/ALAN/Vlad origin establishes the four data findings empirically.
- *Lead Nurture*, "Description" (pp. 3–4) — schedule rate / show rate / throughput definitions; 20–40% revenue lift framing; medium-term scope.
- *Lead Nurture*, "Four Pillars of Lead Nurture" (pp. 5–6) — the four-driver model with one-liner descriptions and InsideSales.com / RAIN Group statistics.
- *Lead Nurture*, "Pillar I — Description" (p. 8) — availability ranked as biggest single predictor.
- *Lead Nurture*, "Execution Conclusion" (pp. 36–37) — five-point summary (Convenience / Speed / Personalization / Volume / Execute) reinforcing the umbrella.
- Indexed in [[Hormozi-Lead-Nurture-Source-Map|Lead Nurture — Source Map]].

## Related
- [[Hormozi-Lead-Nurture-Availability|Hormozi — Pillar I: Availability]]
- [[Hormozi-Lead-Nurture-Speed|Hormozi — Pillar II: Speed]]
- [[Hormozi-Lead-Nurture-Personalization|Hormozi — Pillar III: Personalization]]
- [[Hormozi-Lead-Nurture-Volume|Hormozi — Pillar IV: Volume]]
- [[Hormozi-BAMFAM|Hormozi — BAMFAM]]
- [[Hormozi-Lead-Nurture-Execution-Culture|Hormozi — Lead Nurture Execution Culture]]
- [[00-Book-Home|Lead Nurture — Book Home]]
- [[Hormozi-Lead-Nurture-Source-Map|Lead Nurture — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]
