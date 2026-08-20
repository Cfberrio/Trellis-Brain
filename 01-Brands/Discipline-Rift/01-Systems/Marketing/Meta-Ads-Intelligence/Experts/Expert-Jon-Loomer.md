---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/jon-loomer.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/jon-loomer.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Jon Loomer"
---

# Jon Loomer

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Ben-Heath|Ben Heath]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/jon-loomer.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** jon-loomer
**Watchlist priority:** 2
**Topics:** platform_changes · measurement · targeting · campaign_structure · optimization · budgeting · retargeting
**Sources processed:** 6 articles + **60 YouTube videos (full-source review)**
**Last updated:** 2026-08-19 (Phase 3 — complete video corpus reviewed start to finish)
**Panel status:** **VETTED_OPERATOR** — 60 dated videos across an 8-month window plus 6 articles, weekly publishing cadence, and **six first-hand account examples including two designed tests**. He is the best-matched source in this knowledge base for DR's *scale and structure*, and explicitly **not** a source for anything geo-specific: he states he does not run ads for a local business.
**Evidence model:** v2. Evidence is **self-reported practice and mechanics explanation**, not independently verified.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.jonloomer.com/meta-campaign-objectives-best-practices/` | article | 2023-06-19 (last updated 2025-03-01) | 2026-08-13 | **5** | A1, A2, A3 |
| `https://www.jonloomer.com/advantage-campaign-budget-best-practices/` | article | 2023-06-28 (last updated 2025-03-01) | 2026-08-14 | **5** | C2, C4 |
| `https://www.jonloomer.com/meta-creative-testing/` | article | 2025-10-13 (last updated 2026-01-02) | 2026-08-14 | **4** | D1, D3, D4 |

**Stated context:** general Meta advertisers; Loomer's own account is a small info-product/training business. No client spend or volume disclosed anywhere in the source.

**Retrieval note:** `jonloomer.com` returns **HTTP 403 to WebFetch**. This source was retrieved with a **rendered browser** (Playwright). Publication and modification dates were read from the page's own `article:published_time` / `article:modified_time` metadata and the visible byline ("June 19, 2023 … Last updated: March 1, 2025"), resolving the date that discovery could not establish.

**Dating caution:** the article is two and a half years old with a partial 2025 revision. Its objective/performance-goal enumerations are **descriptions of the Ads Manager UI at time of writing** and must be checked against `official-meta/campaign-objectives-and-optimization-events.md` before use — Meta changed this surface during the article's life, and the article itself contains evidence of that (see Contradictions).

---

## Claims — article (2023-06-19, updated 2025-03-01)

### campaign_structure — The objective gates which options exist; it does not itself change delivery

```yaml
topic: campaign_structure
claim: The campaign objective determines which conversion locations and performance goals are available, but delivery is identical across objectives when the performance goal is the same.
recommended_action: "Treat the objective as a gateway to the performance goal you want, not as a separate delivery instruction."
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [A1]
published_at: 2023-06-19
source_url: https://www.jonloomer.com/meta-campaign-objectives-best-practices/
author: Jon Loomer
evidence: "The objective impacts optimization, but not in the way many advertisers think. The methods available to optimize your ads are impacted by the objective you select, but the influence stops there." / "If you choose Impressions as your performance goal, there is no difference in how your ads will be delivered." / "No, there won't be a greater focus on sales if you set your performance goal to Impressions while using the Sales objective, rather than the Traffic objective. Delivery will be the same."
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Mechanics explanation asserted from long practice. No test, comparison, or account data presented for the identical-delivery claim."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **This reframes A1 substantially.** If true, the objective question is not "which objective makes Meta try harder to sell" but "which objective exposes the performance goal and conversion event I actually want" — a much more tractable question, and one the platform documentation can answer directly.

`PARTIALLY_SUPPORTED`: Meta corroborates the *gating* half explicitly — *"The ad objective and conversion location you choose will determine what performance goals are available"* and *"The performance goal of your ad set can be different from your ad objective."* Meta does **not** state the stronger half — that delivery is identical across objectives given the same performance goal. That is Loomer's inference, and no first-party source found confirms or denies it.

---

### campaign_structure — Use Sales for any website conversion event

```yaml
topic: campaign_structure
claim: Since Meta allowed all website conversion events under the Sales objective, Sales is the appropriate objective for any website conversion, including lead-type events.
recommended_action: "Use the Sales objective for any website conversion event, rather than the Leads objective, because additional features (audience segments) are only available under Sales."
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [A1]
published_at: 2023-06-19
source_url: https://www.jonloomer.com/meta-campaign-objectives-best-practices/
author: Jon Loomer
evidence: "Once Meta started making all website conversion event optimization available for sales campaigns, I've started using the Sales objective for all website conversions." / "Meta made a change that allows you to use the Sales objective (including Advantage+ Shopping Campaigns) for any website conversion event. Since audience segments are only available for Sales campaigns, I've started using the Sales objective for any website conversion event as a result."
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "His own stated practice, with a named reason (feature availability). No performance comparison between Sales and Leads is presented — the argument is about available features, not measured results."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **The single most on-point external claim for A1**, and it contradicts the common agency default of using Leads for local service businesses.

`PARTIALLY_SUPPORTED`: Meta's current Help Centre confirms the platform premise — Sales → Website accepts `Complete registration` among its conversion events, so the objective genuinely does accommodate a registration event. It also confirms Sales → Website uniquely carries both the conversion goals and the shallower landing-page-view / link-click goals, which is an *additional* structural argument Loomer does not make. Meta does not confirm his feature rationale (audience segments) nor any performance benefit. Note this is a **feature-availability argument, not a performance argument** — he never claims Sales outperforms Leads.

---

### campaign_structure — Choose the performance goal first, then the objective

```yaml
topic: campaign_structure
claim: The decision order should be reversed from Meta's presentation — decide the performance goal first, then select whichever objective exposes it.
recommended_action: "Start from the outcome you want, identify the performance goal that produces it, then choose the objective most closely aligned with that performance goal."
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [A1, A2]
published_at: 2023-06-19
source_url: https://www.jonloomer.com/meta-campaign-objectives-best-practices/
author: Jon Loomer
evidence: "It's somewhat backwards, but you may want to think of your performance goal prior to your objective. Meta's intention is that the objective will lead to your desired performance goal, but that won't always be the case." / "Start with what you want to accomplish. Then consider the ideal performance goal to complete that task. From there, find the objective that is most closely aligned with that performance goal."
timestamp: null
confidence: high
evidence_basis: opinion
evidence_basis_details: "Reasoning about decision order; follows logically from his gating claim above. No evidence presented, and none is really required for a procedural recommendation."
evidence_strength: none
platform_validation_status: NOT_APPLICABLE
```

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** Costs nothing, and it is the correct sequencing for DR specifically — DR's binding constraint is which *event* is reachable at its volume (A2), so letting the event drive the objective is the order that respects the actual constraint. This is a procedural claim; the absence of evidence is not a weakness in the way it would be for a performance claim.

---

### optimization — Top-of-funnel optimization buys volume without regard to quality

```yaml
topic: optimization
claim: When the delivery system optimizes for top-of-funnel actions it maximizes the count of those actions with no consideration of their quality.
recommended_action: "Do not optimize for Landing Page Views or Link Clicks when the goal is quality outcomes."
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [A2, A3]
published_at: 2023-06-19
source_url: https://www.jonloomer.com/meta-campaign-objectives-best-practices/
author: Jon Loomer
evidence: "Whenever the algorithm optimizes for top-of-the-funnel engagement, it cares only about volume of those actions and not the quality of them." / "I'm not a fan of this objective. The primary issue with it is that Meta doesn't provide any unique options for driving quality traffic. Landing Page Views and Link Clicks, for example, will only drive a bunch of clicks. You likely want more than that."
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Asserted from practice. No test or account data comparing top-of-funnel optimization against a deeper goal is presented in this source."
evidence_strength: weak
platform_validation_status: INSUFFICIENT_EVIDENCE
```

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **This is the counter-position to the up-funnel move, and it lands squarely on DR's current setup** — DR optimizes `LANDING_PAGE_VIEWS` today, which is precisely what this claim says produces volume without quality.

`INSUFFICIENT_EVIDENCE`: Meta states that the performance goal is *"the desired outcome that our system bids on in the ad auction"*, which is consistent with the mechanism, and Meta separately notes *"we may prioritize higher-quality clicks"* — a partial hedge in the other direction. Nothing available resolves whether the practical consequence is as severe as claimed. Held as a well-motivated hypothesis, not a fact.

---

### optimization — Use Engagement + Website + a custom event when you want quality traffic

```yaml
topic: optimization
claim: For quality traffic to a website, the Engagement objective with a Website conversion location and a custom event defining quality outperforms the Traffic objective.
recommended_action: "To drive quality traffic, use the Engagement objective with the Website conversion location and a custom event representing the quality action, instead of the Traffic objective."
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [A1, A2, A3]
published_at: 2023-06-19
source_url: https://www.jonloomer.com/meta-campaign-objectives-best-practices/
author: Jon Loomer
evidence: "If quality traffic is a priority, I'd recommend utilizing the Engagement objective and custom events that measure quality traffic actions." / "When I care about driving quality traffic to a blog post, I utilize the Engagement objective with the Website conversion location. I then use a custom event that represents quality traffic as the performance goal."
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "His own standing practice on his own site. No comparison against the alternative is presented."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** Introduces a **third objective path** that the platform research had not surfaced as a candidate: Engagement → Website with a custom event. Meta's current documentation partly supports the premise — Engagement → Website exists and offers *"Maximize number of conversions"* — but its documented conversion-event list for Engagement → Website **excludes `Complete registration`**, which Leads and Sales both include. So this route may be usable for a shallow "qualified visit"-style custom event but appears unable to name registration itself. Recorded as a real option with a documented limitation, not a recommendation. Converges with Kerhoas and Gardideh on custom/qualified events from a third independent direction.

---

## Claims — article: Advantage Campaign Budget Best Practices (2023-06-28, updated 2025-03-01)

**Retrieved** 2026-08-14 with a rendered browser (`jonloomer.com` returns HTTP 403 to WebFetch — same constraint as the first source). Byline read from the page: *"June 28, 2023 by Jon Loomer"*, *"Last updated: March 1, 2025"*.

**Stated context:** general Meta advertisers. **No spend level, client, account size, or conversion volume is disclosed anywhere in the article.** The worked example uses three ad sets at $20/day each. Content is mechanics explanation plus stated best practice; no test, comparison, or account data is presented for any claim below.

**Dating caution:** same as the first source — a mid-2023 article with a partial 2025 revision. Its UI descriptions and eligibility rules must be checked against `official-meta/campaign-budget-and-consolidation.md` before use.

### CBO / ABO — Ad sets that must differ in budget type, bid strategy, performance goal or delivery require ad set budgets

```yaml
topic: CBO / ABO
claim: Advantage+ campaign budget forces a common budget type, bid strategy and standard delivery across all ad sets in the campaign, and (under Highest Volume bidding) a common performance goal; ad sets that need to differ on any of these require ad set budgets.
recommended_action: "If you need ad sets that differ by budget type, bid strategy, performance goal, or delivery, use ad set budgets instead of Advantage+ campaign budget."
context: campaigns containing more than one ad set
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C2]
published_at: 2023-06-28
source_url: https://www.jonloomer.com/advantage-campaign-budget-best-practices/
author: Jon Loomer
evidence: "A common budget type will be used for all ad sets (daily or lifetime). / A common bid strategy will be utilized across all ad sets. / If using the Highest Volume bid strategy, the same optimization event (Performance Goal) will be utilized across all ad sets. / Standard delivery will automatically apply. / If you want to create ad sets that differ by budget type, bid strategy, performance goal, or delivery, you'll need to utilize ad set budgets."
timestamp: "Eligibility requirements"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Platform-mechanics description stated from practice; no data, test, or Meta citation shown in the article for the constraint list."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

> "If you want to create ad sets that differ by budget type, bid strategy, performance goal, or delivery, you'll need to utilize ad set budgets."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **The single most decision-relevant claim in this source for DR**, because it is the one that binds C2 to Wave 1A. Wave 1A's ladder explicitly contemplates DR moving between optimization events, and a plausible future DR structure is two ad sets on *different* rungs simultaneously (e.g. a registration-optimized ad set alongside an LPV-optimized one). If this constraint holds, Advantage+ campaign budget prohibits that combination under Highest Volume bidding while ad set budgets permit it. **`PARTIALLY_SUPPORTED`:** Meta's own decision criteria corroborate the direction — *"You have mixed optimization goals or bid strategies"* is listed by Meta as a reason to use ad set budgets (`official-meta/campaign-budget-and-consolidation.md`). Meta's first-party statement of the eligibility *requirement itself* was **not retrieved first-hand this run**, so the hard-constraint form of the claim remains practitioner-sourced.

### CBO / ABO — Advantage+ campaign budget suits multiple, similarly-sized ad sets with a common configuration

```yaml
topic: CBO / ABO
claim: The ideal conditions for Advantage+ campaign budget are multiple ad sets with similarly sized audiences, no need to customize bid strategy/budget type/performance goal per ad set, and a willingness to leave it alone.
recommended_action: "Use Advantage+ campaign budget when creating multiple similarly-sized ad sets with a common configuration and a hands-off approach; keep audience sizes similar between ad sets."
context: campaigns with multiple ad sets
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C2]
published_at: 2023-06-28
source_url: https://www.jonloomer.com/advantage-campaign-budget-best-practices/
author: Jon Loomer
evidence: "the ideal situation to use Advantage Campaign Budget is when… 1. You're creating multiple ad sets for similarly sized audiences. 2. You have no need to customize the bid strategy, budget type, or performance goal by ad set. 3. You trust the optimization from Advantage Campaign Budget and will have a hands-off approach." / "Keep audience sizes similar between ad sets. Oftentimes, advertisers will have multiple ad sets within a campaign for cold and warm audiences. This approach is not ideal for Advantage Campaign Budget. In all likelihood, most of the budget will be distributed to the larger audience."
timestamp: "Best Practices / When Should You Use It?"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated best practice; the budget-flows-to-the-larger-audience mechanism is asserted ('in all likelihood'), with no data or test shown."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

> "You're creating multiple ad sets for similarly sized audiences."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** DR currently satisfies none of the three stated conditions — it has one ad set, so "multiple similarly-sized ad sets" is not evaluable. **`PARTIALLY_SUPPORTED`:** Meta corroborates two of the three conditions from its own side — *"Advantage+ campaign budget is best suited for campaigns with at least 2 ad sets"*, and *"You have a large difference in audience size between your ad sets"* is Meta's own stated reason to prefer ad set budgets. Condition 3 ("trust it, hands-off") is a disposition, not a platform behavior, and documentation cannot validate it.

### CBO / ABO — Adding an ad set triggers a two-hour re-adjustment period

```yaml
topic: CBO / ABO
claim: Adding a new ad set to a campaign using Advantage+ campaign budget causes a two-hour re-adjustment period, separate from the learning phase.
recommended_action: "Limit changes to campaigns running Advantage+ campaign budget."
context: Advantage+ campaign budget campaigns
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C2]
published_at: 2023-06-28
source_url: https://www.jonloomer.com/advantage-campaign-budget-best-practices/
author: Jon Loomer
evidence: "Limit changes. Whenever you add a new ad set to your campaign, there will be a two-hour re-adjustment period. Additionally, any significant changes to the campaign settings will restart the learning phase."
timestamp: "Best Practices #2"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Specific mechanism with a specific duration asserted; no source or evidence given for the two-hour figure."
evidence_strength: weak
platform_validation_status: INSUFFICIENT_EVIDENCE
```

> "Whenever you add a new ad set to your campaign, there will be a two-hour re-adjustment period."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** untested · **implementation_transfers:** untested
**reason:** **A precise number with no traceable origin — exactly the shape of claim this domain's numeric-threshold rule exists to quarantine.** `INSUFFICIENT_EVIDENCE`: no first-party page retrieved mentions a re-adjustment period of any duration. What Meta *does* state on the adjacent question is more reassuring and is already on file (`significant-edits.md`): adding a new ad set to an Advantage+ campaign budget campaign does **not** cause existing ad sets to re-enter the learning phase. Do not cite the two-hour figure as fact anywhere downstream.

### CBO / ABO — Read results at campaign level, not ad set level

```yaml
topic: measurement
claim: With Advantage+ campaign budget, performance should be evaluated at campaign level; ad-set-level results become the wrong unit of analysis.
recommended_action: "Stop evaluating results at the ad set level when running Advantage+ campaign budget; judge the campaign."
context: Advantage+ campaign budget campaigns
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C2]
published_at: 2023-06-28
source_url: https://www.jonloomer.com/advantage-campaign-budget-best-practices/
author: Jon Loomer
evidence: "Get out of the habit of looking at your results at the ad set level. All that matters is how the campaign performs." / "if you're going to use Campaign Budget Optimization, you need to go all in. Trust it. Keep your hands off. Allow it to do its work and optimize without your interruptions or restrictions."
timestamp: "Best Practices #4–5"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Operating disposition asserted as best practice; no evidence presented that intervention degrades outcomes."
evidence_strength: none
platform_validation_status: PARTIALLY_SUPPORTED
```

> "Get out of the habit of looking at your results at the ad set level. All that matters is how the campaign performs."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** partial
**reason:** `PARTIALLY_SUPPORTED` — Meta lists *"You measure results at the campaign level"* as one of the goals that make Advantage+ campaign budget a fit, and states results are read *"at the campaign level, rather than at the ad set level."* Meta presents this as a **fit criterion for choosing the mode**; Loomer converts it into a prescription about how to behave. Those are different claims and the second is not Meta's. For DR the practical content is a readability cost, not a rule: at one ad set the two levels are the same number, and the loss only begins when a second ad set exists — precisely when DR would most want to read them separately at low volume.

### CBO / ABO — Advantage+ campaign budget prefers volume and colder, larger audiences

```yaml
topic: CBO / ABO
claim: Advantage+ campaign budget performs best with more volume to work with, making it better suited to colder, larger audience targeting than to small warm audiences.
recommended_action: null
context: choice of audience type when using Advantage+ campaign budget
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C2]
published_at: 2023-06-28
source_url: https://www.jonloomer.com/advantage-campaign-budget-best-practices/
author: Jon Loomer
evidence: "While you could technically use this with smaller and warmer audiences if those audiences are similar sizes, the ads algorithm tends to do best with more volume to work with. This is ideal for colder audience targeting when you have a common approach across ad sets."
timestamp: "When Should You Use It?"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Performance tendency asserted ('tends to do best'); no data, test, or account comparison presented."
evidence_strength: none
platform_validation_status: NOT_APPLICABLE
```

> "the ads algorithm tends to do best with more volume to work with."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** untested · **implementation_transfers:** no
**reason:** `NOT_APPLICABLE` — a performance assertion about algorithm behavior that Meta documentation is not capable of validating; Meta publishes no performance claim for either budget mode. Directionally unhelpful for DR either way: DR is a low-volume, geo-constrained advertiser, which is the opposite of the condition described, but nothing here establishes a consequence. **Recorded as unvalidated opinion; must not become a reason to prefer either mode for DR.**

---

## Claims — article: Meta's Creative Testing Tool (2025-10-13, updated 2026-01-02)

**Retrieved** 2026-08-14, rendered browser (`jonloomer.com` → HTTP 403 to WebFetch). Dates read from the page's `article:published_time` / `article:modified_time` metadata and the visible byline.

**Stated context:** the author's own account, promoting a **free registration** for his newsletter ("The Loop"). **He discloses concrete test parameters:** `Complete Registration` optimization event, expected cost per result *"in the $3-5 range"*, **$50/day dedicated to the test**, ended *"a little early to write this blog post."* This is the most context-disclosed source in the corpus for creative testing — and note the outcome is a **free lead-magnet signup, not a paid registration**, so the event depth is not comparable to DR's paid season registration.

**This source is materially stronger than his other two:** he actually ran the thing and reports the outcome, rather than describing practice.

### creative_testing — Meta's creative test equalizes spend across test ads, which normal delivery does not

```yaml
topic: creative_testing
claim: Meta's native creative testing feature prevents the delivery system from optimizing budget toward particular ads during the test, so each test ad receives similar spend and can be compared; outside a test, Meta does not distribute budget evenly.
recommended_action: "Use the creative testing feature when you want comparable spend across ads rather than Meta's normal optimized distribution."
context: campaigns using the Highest Volume bid strategy
business_type: unstated (author's own info-product/newsletter business)
spend_level: "$50/day dedicated to the test"
conversion_volume_context: "expected cost per result $3-5 on a Complete Registration event (free signup)"
research_question_ids: [D1, D4]
published_at: 2025-10-13
source_url: https://www.jonloomer.com/meta-creative-testing/
author: Jon Loomer
evidence: "This feature allows you to prevent Meta from optimizing delivery to specific ads so that you can get a clearer idea of how each ad in the test will perform while given similar ad spend. Since it's an A/B test, there won't be overlap between the ads (each person will only see one of the ads)." / "When the test has completed, delivery of your ads will continue. But the test is complete, so Meta will not be focused on maintaining similar ad spend across your ads."
timestamp: "How it Works / 8. After the test"
confidence: high
evidence_basis: self_reported_test
evidence_basis_details: "Author ran an actual creative test on his own account and reports setup parameters ($50/day, Complete Registration, $3-5 expected CPA) and a result ordering. Screenshots referenced; no underlying data table reproduced in text."
evidence_strength: moderate
platform_validation_status: SUPPORTED
```

> "This feature allows you to prevent Meta from optimizing delivery to specific ads so that you can get a clearer idea of how each ad in the test will perform while given similar ad spend."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** `SUPPORTED` — Meta's own page states the feature provides *"delivery… to new test ads"* and is set up *"in an existing campaign… with delivery system learnings retained."* **This is the single most useful claim in the wave for D4**: it identifies the documented mechanism that answers "I cannot tell whether this ad is bad or just starved." Implementation transfers only *partially* for DR because Meta suggests *"no more than 20% of your existing budget"* for the test slice — at DR's historical spend that slice is a trivial absolute amount spread across multiple ads.

### creative_testing — The test does not fix budget distribution afterward, and results may contradict Meta's own allocation

```yaml
topic: creative_testing
claim: After a creative test ends, Meta resumes optimized (uneven) distribution and may not favor the ad the test identified as top performer; test results should be used to learn, not to correct Meta's allocation.
recommended_action: "Use creative test results to inform the next batch of creative, not to try to force Meta to spend on the test winner. Do not overreact to results from a small sample."
context: after a creative test completes
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [D3, D4]
published_at: 2025-10-13
source_url: https://www.jonloomer.com/meta-creative-testing/
author: Jon Loomer
evidence: "Once the test is completed, your ads will continue to run without the restrictions of your creative test settings. That means that Meta will no longer split your budget evenly between your ads. And it's possible that Meta won't distribute the most budget to the highest performing ad from your test (or the least budget to the lowest performer)." / "Resist the urge to overreact to these results, particularly if they represent a small sample size." / "Your main goal of using the creative testing feature shouldn't be to fix how Meta is distributing your budget. Instead, it's to learn from results while budget is distributed evenly."
timestamp: "Recommendations #3–#4"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Operating advice following his test; the specific assertion that Meta may not favor the test winner afterward is stated from observation, without a documented case."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

> "Your main goal of using the creative testing feature shouldn't be to fix how Meta is distributing your budget. Instead, it's to learn from results while budget is distributed evenly."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** `PARTIALLY_SUPPORTED` — Meta corroborates the mechanical half: *"After the test, the test ads will continue to run… using the original campaign or ad set budget. The test does not make any automatic changes based on the results."* Meta does **not** state that its post-test allocation may contradict the test winner; that is Loomer's observation. The "don't overreact to a small sample" advice is disposition, not platform behavior — but it converges with Meta's own *"A confidence level is not included"* and with the breakdown-effect page. **Scale-independent and free to adopt.**

### creative_testing — Aim for meaningful event volume before trusting a creative test

```yaml
topic: creative_testing
claim: Test budget, duration and number of ads should be set so the test can accumulate meaningful optimization events; the author uses ~50 events in a week as his reference point and considers results below that less meaningful.
recommended_action: "Set test budget, length and ad count against your expected cost per action, aiming for enough events that a repeat test would produce similar results."
context: setting up a creative test
business_type: unstated
spend_level: "$50/day in his own test"
conversion_volume_context: "references the ~50 optimized events per week rule of thumb"
research_question_ids: [D1, D3]
published_at: 2025-10-13
source_url: https://www.jonloomer.com/meta-creative-testing/
author: Jon Loomer
evidence: "Consider your expected Cost Per Action when determining the test budget, length of your test, and number of ads to be tested. I would always start with the old rule of thumb of 50 optimized events in a week. If you're not able to get that, your results are less meaningful. You want results that are so clear that if you ran the test again, you'd get similar results." / "Even in my test above, I'd likely run it for a longer window next time. I'd love to see the highest performing ad get closer to 50 conversions by itself."
timestamp: "Recommendations #1"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Explicitly labels the 50/week figure as an 'old rule of thumb' rather than a derived threshold; his own test is conceded to fall short of what he would want."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

> "I would always start with the old rule of thumb of 50 optimized events in a week. If you're not able to get that, your results are less meaningful."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** `PARTIALLY_SUPPORTED` — the ~50/week figure traces to Meta's learning-phase framing, which Meta states in hedged form (*"about 50"*, exit is *"as soon as they can deliver stably"*) and which `learning-limited.md` explicitly says is not a penalty. **The transferable content is not the number** — it is the reproducibility test: *"results that are so clear that if you ran the test again, you'd get similar results."* That is a usable low-volume standard for DR and costs nothing. **The 50-per-ad target does not transfer**: he concedes his own $50/day test missed it; DR's delivery is orders of magnitude below. Counted as **one claim from the same origin as every other 50/week citation in this corpus**, per the standing framework-independence warning.

### creative_testing — The feature cannot test existing ads, only new duplicates

```yaml
topic: creative_testing
claim: Creative testing only works on newly duplicated ads, not on ads already running, which limits its usefulness for diagnosing why an existing ad is receiving little budget.
recommended_action: null
context: limitation of the feature
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [D4]
published_at: 2025-10-13
source_url: https://www.jonloomer.com/meta-creative-testing/
author: Jon Loomer
evidence: "My primary complaint about the creative testing feature is that you can't test existing ads. You have to duplicate an existing (active or draft) ad, and the duplicates will be part of the test." / "If you have five ads in an active ad set, you may question why Meta is distributing a high percentage of your budget to one ad and a low percentage to another. A test consisting of these five ads to confirm that distribution would help answer these questions. But you have to create new ads."
timestamp: "Functionality Complaints"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Limitation observed directly while using the feature. No recommendation offered — recorded as null rather than inferred."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

> "you can't test existing ads. You have to duplicate an existing (active or draft) ad, and the duplicates will be part of the test."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** n/a
**reason:** `PARTIALLY_SUPPORTED` — Meta's page confirms the duplication mechanic (*"Choose the number of copies you'd like to make of this ad"*, and the originating ad is not in the test), without framing it as a limitation. **Directly material to D4:** it means the creative test **cannot be used to adjudicate an existing no-spend ad** — the exact question DR would most want answered. The tool answers "which of these new creatives performs better under equal spend", not "why is my running ad starved."

### Correction against first-party documentation — ad count

Loomer states: *"You can create between two and five test ads."* **Meta's current page states *"You can create 2 to 7 copies"* and *"compare up to 7 creative variants."*** Retrieved the same day (2026-08-14) from `official-meta/creative-testing-ab-testing-and-delivery-diagnostics.md`.

Graded **`OUTDATED`, not `CONFLICTING`** — the article was last updated 2026-01-02 and the ceiling appears to have been raised since. Per the ingest contract, *"Advice ages. Being early is not being wrong."* Recorded because it is a live demonstration of why first-party retrieval precedes practitioner material.

---

## Contradictions within this author

**One, and it is internal to a single article.** In the Engagement section he writes that Sales performance goals *"require a conversion value"*, offering Engagement as the workaround for optimizing to non-value events:

> "Since performance goals under the Sales objective require a conversion value, you may instead want to use Engagement and the Website conversion location if optimizing for standard events further up the funnel (Add to Cart, Initiate Checkout, View Content)."

In the Sales section of the same article he states the opposite, as a change Meta made:

> "Meta made a change that allows you to use the Sales objective (including Advantage+ Shopping Campaigns) for any website conversion event."

The Sales-section statement is the later position and matches current Meta documentation (Sales → Website lists many non-value events including `Complete registration`). Reading: the Engagement paragraph is **stale text surviving a partial 2025 revision**. Recorded rather than silently resolved, because it is direct evidence that this source's UI enumerations age unevenly and must be checked against first-party documentation before use.

## Open questions from this author

- The identical-delivery-across-objectives claim is asserted, never tested, and is not confirmed by Meta.
- The Sales-over-Leads recommendation rests on feature availability (audience segments), with no performance comparison offered.
- Performance-goal lists are per-objective aggregates across all conversion locations, so they do not by themselves show what is available for a given objective + Website combination — do not read them as conflicting with Meta's per-location tables.
- Nothing in this source addresses low-volume accounts or what happens when the chosen event is too rare.

**From the Advantage Campaign Budget article (2026-08-14):**

- The **two-hour re-adjustment period** is stated with no source and appears in no first-party page retrieved. Origin unknown.
- **Neither article addresses the single-ad-set case.** Every claim assumes a campaign with multiple ad sets; the article never says what Advantage+ campaign budget does, or is worth, when a campaign contains exactly one. That is DR's actual situation and this source does not reach it.
- No spend, client, or volume context is disclosed anywhere, so nothing here can be scoped by account size — including the "does best with more volume" assertion, which names no volume.
- "Trust it, keep your hands off" is asserted as a disposition with no evidence that intervention degrades results.

---

# Phase 2 ingestion — 2026-08-19

**Run:** `knowledge/research-runs/2026-08-19_phase2-expert-corpus/`. Three further jonloomer.com articles.

**Retrieval note that closes a Phase 1 flag:** jonloomer.com returns HTTP 403 to native WebFetch, which is why Phase 1 could not verify his publication dates first-hand. The Phase 2 crawl reached the site through the Apify proxy, so **his 2026 cadence is now confirmed from his own site** — the corpus holds 243 of his documents, 119 of them inside the recency window.

**Date-precision warning:** two of the three articles below carry exact dates from page metadata. `meta-ads-master-brief` exposed no publication date and is tiered **`UNDATED`** — its date shown here is an HTTP `Last-Modified` timestamp and is **not** a publication date. Its claims may describe behaviour from any time; several of them reference features (Audience Segments, value rules by custom audience, a 10-asset creative workflow "currently in test") that place it recent, but that is inference.

## Sources processed (Phase 2)

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.jonloomer.com/meta-ads-targeting-2026/` | article | 2026-03-23 | 2026-08-19 | 3 | E1, E2, A3 |
| `https://www.jonloomer.com/restrict-audience-meta-advertising/` | article | 2025-12-15 | 2026-08-19 | 2 | E1, A2 |
| `https://www.jonloomer.com/meta-ads-master-brief/` | article | **null (UNDATED — Last-Modified only)** | 2026-08-19 | 3 | C1, F1, B2 |

**Stated context:** independent educator who runs his own tests on his own accounts. Business types referenced include **lead generation** explicitly — rare in this corpus. Spend context is small-to-mid; he discusses $10-20/day budgets directly, which no other panel member does.

---

## Claims — Phase 2

### optimization — Use value rules to fix a demographic quality problem instead of restricting the audience

```yaml
topic: optimization
claim: When Meta concentrates budget on a demographic producing cheap low-quality results, restricting that demographic pushes the same problem into the adjacent one and removes valuable customers; bidding down on it instead keeps everyone eligible while collapsing its share of spend. In his own lead-generation case, bidding 90% less on 65+ and 20% less on 55-64 moved 65+ from 45% of spend to under 2%.
recommended_action: "Diagnose the demographic quality problem first, then apply value rules to bid down on the low-quality segment rather than excluding it. Reserve restrictions for legally age-restricted products."
context: His own lead-generation advertising, where Meta repeatedly concentrated budget on people 65+ producing cheap, low-quality leads.
business_type: lead_gen
spend_level: null
conversion_volume_context: null
research_question_ids: [A3, E1]
question_link_origin: prospective
published_at: 2026-03-23
source_url: https://www.jonloomer.com/meta-ads-targeting-2026/
author: Jon Loomer
timestamp: null
confidence: high
evidence_basis: self_reported_test
evidence_basis_details: "His own account, with before/after spend distribution quoted (65+ from 45% of spend to under 2%) and the failed prior approach described (age restriction merely displaced budget to 55-64). Distribution shift is reported; downstream lead quality improvement is asserted, not quantified."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "He repeatedly found Meta concentrating budget on people 65+, producing cheap, low-quality leads. His old fix was restricting by age, but that simply moved budget to 55–64 and eliminated valuable customers. Instead, he now bids 90% less on 65+ and 20% less on 55–64, dropping spend on 65+ from 45% to under 2% while keeping everyone in the mix."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **A3 asked for a concrete, obtainable quality safeguard, and this is the first practitioner-demonstrated one found — from a lead-gen account, with a measured before/after, and it does not touch child data.** The mechanism is exactly A3's shape: the advertiser holds information Meta does not (who is actually qualified), and encodes it as a bid adjustment rather than as an exclusion. The failure mode he describes is also DR's risk profile — a cheap, easily-bought optimized action that never becomes a paid registration. **Two limits before this becomes a DR plan:** it presumes enough delivery for spend distribution to be readable at all, which DR does not have today; and DR's disqualifier is residency/school, not age band, so the equivalent lever would have to be geographic or audience-label based, which is a different and unproven application. Do not confuse this with E1's audience configuration — value rules are a bidding layer, not a targeting restriction.

---

### targeting — Detailed targeting and lookalikes are only restrictable under performance goals nobody should use

```yaml
topic: targeting
claim: Under 11 of the most common performance goals, detailed targeting inputs are treated as suggestions and cannot be enforced; lookalike inputs are suggestions under 9. Restriction is only possible with light-touch goals (reach, impressions, ThruPlay, interactions, page likes), which produce low-quality results by their nature.
recommended_action: "Do not plan around restricting by interest or lookalike. If you are optimizing for a conversion, treat those inputs as suggestions; if you need guardrails badly enough to use a light-touch goal, reconsider the goal."
context: Mechanics of what can and cannot be constrained under current performance goals.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [E1, A2]
question_link_origin: prospective
published_at: 2025-12-15
source_url: https://www.jonloomer.com/restrict-audience-meta-advertising/
author: Jon Loomer
timestamp: "Bottom Line"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Enumerates the specific performance goals in each bucket from hands-on account observation; presented as platform mechanics rather than as a tested result. Counts are precise enough to be checkable against Meta documentation, which is exactly what the validation pass should do."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "You cannot restrict by detailed targeting when using 11 of the most common performance goals… If you're using one of the remaining nine performance goals (rarely recommended), adding some guardrails with detailed targeting restrictions will help, though it won't fully solve the likely problems you'll have related to quality."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** Corroborates E1's control-versus-suggestion split — already established as a **platform fact** from Meta's own documentation, which outranks this — and adds an operationally useful detail E1 does not record: the restrictability depends on **which performance goal is selected**, and the goals where restriction still works are the ones that buy worthless actions. That closes a loophole a future operator might otherwise reach for: "if we optimize for engagement we can at least control who sees it." **Flag for the validation pass**: the specific counts (11 and 9) are checkable against first-party documentation and should be confirmed rather than trusted.

---

### targeting — Do not restrict age or gender to match the ideal customer profile

```yaml
topic: targeting
claim: Restricting age or gender to reflect a known customer profile is rarely necessary and prevents Meta from spending even small amounts on segments that could convert; where a demographic genuinely produces cheap low-quality results, the fix is value rules rather than exclusion.
recommended_action: "Avoid demographic restrictions except for legally age-restricted products; solve proven demographic quality problems with bid adjustments."
context: Targeting guidance for 2026; includes the worked counter-example of a service for women-owned businesses where a purchase goal needs no gender restriction but an engagement goal would deliver to men.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [E1, E2]
question_link_origin: prospective
published_at: 2026-03-23
source_url: https://www.jonloomer.com/meta-ads-targeting-2026/
author: Jon Loomer
timestamp: null
confidence: high
evidence_basis: opinion
evidence_basis_details: "Reasoned from delivery mechanics with an illustrative example; the value-rules alternative carries his own account evidence (previous claim) but this general rule does not."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "Restricting your audience also restricts the algorithm, preventing Meta from spending even a small amount of your budget on a group that could lead to results."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** partial
**reason:** Consistent with E1, which keeps an adult minimum age as a control and adds no other demographic constraint. His worked example is the one worth carrying: the *performance goal* determines whether a demographic problem appears at all — an engagement-level goal invites the wrong people in a way a conversion goal does not. That is directly relevant to A2's ladder, where the temptation at DR's volume is to optimize for a shallower event. **The cheap-event risk is not just noisy data; it is a delivery problem that pulls budget toward people who will never register.**

---

### campaign_structure — One campaign and one ad set is the efficient starting point, and splitting waters down budget

```yaml
topic: campaign_structure
claim: The most efficient starting structure is one campaign and one ad set optimized for a conversion; every additional campaign or ad set divides the budget, invites auction overlap and audience fragmentation, and makes reaching roughly 50 optimized events per week harder. Advertisers over-complicate to solve imagined problems, often out of emotional attachment to a particular ad.
recommended_action: "Start with one campaign and one ad set on a single business goal; add complexity only for a legitimate reason, not to control delivery of a favoured ad."
context: His general operating approach.
business_type: unstated
spend_level: null
conversion_volume_context: "~50 optimized events per week referenced as the learning threshold"
research_question_ids: [C1, C3]
question_link_origin: prospective
published_at: null
source_url: https://www.jonloomer.com/meta-ads-master-brief/
author: Jon Loomer
timestamp: "Simplify Campaign Structure and Consolidate"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as his standing approach with the mechanism explained ($100 in one ad set versus split across five). No account comparison presented. **Source is UNDATED** — a Last-Modified header only."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "The most efficient starting point is one campaign and one ad set, optimized for a conversion, with budget consolidated into a single business goal. **Every extra campaign and ad set waters down your budget.** In a vacuum, $100 in one ad set is more efficient than $100 split across five."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** DR's exact architecture, described as the *default* rather than as a limitation — which matters, because DR's 1/1/1 was reached by elimination and could easily be read as a deficiency to outgrow. Combined with Faris/Kiel on audience overlap and Foxwell on under-fed splits, C1 now has three independent practitioners naming the same mechanism from different angles. **Undated source**, so it cannot be used to assert current platform behaviour; the structural argument is nonetheless the same one Meta's consolidation guidance supports.

---

### budgeting — There is no universally right budget; derive it from expected cost per optimized action

```yaml
topic: budgeting
claim: The right budget depends on the goal and an honest expected cost per optimized action — for a $100 product, conservatively assume $100 to get a sale. At $10-20/day a beginner will make little impact but the spend is still worthwhile for learning.
recommended_action: "Set budget from expected cost per action rather than from a benchmark, and treat very small budgets as tuition rather than as a performance program."
context: Budget guidance for advertisers starting out.
business_type: unstated
spend_level: "$10-20/day discussed explicitly"
conversion_volume_context: null
research_question_ids: [B2]
question_link_origin: prospective
published_at: null
source_url: https://www.jonloomer.com/meta-ads-master-brief/
author: Jon Loomer
timestamp: null
confidence: high
evidence_basis: opinion
evidence_basis_details: "Judgement offered as guidance; no data. **Source is UNDATED.**"
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "there's no universal 'right' number. It depends on your goal and an honest expected cost per optimized action. If you sell a $100 product, conservatively assume it costs $100 to get a sale. For beginners, $10–$20/day makes little impact but is still worthwhile for gaining experience."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **The only source in the entire corpus that addresses budgets in DR's actual range rather than treating $10k/day as the small case** — B2 was closed as far as external evidence allows precisely because nothing existed at this scale. His derivation method is the one B2 specifies (event choice → expected cost → volume → budget), and his framing gives DR honest language for its situation: at very low budgets the spend buys *experience*, not evidence. **It supplies no cost-per-registration figure and must not be read as endorsing $10-20/day as sufficient** — B1's arithmetic still governs. DR's historical ~$2.70/day sits below even his tuition tier.

---

### retargeting — Meta already spends 20-25% of budget on remarketing without being asked, and it can be proven

```yaml
topic: retargeting
claim: With Advantage+ Audience on, Meta defaults to prioritizing past converters, pixel activity and prior ad engagement; the Audience Segments report (reporting-only, Sales objective) typically shows roughly 20-25% of budget going to remarketing with no advertiser input, sometimes 10-40%. A separate remarketing campaign therefore reaches those people twice and creates auction overlap. Remarketing's low costs and high ROAS are often propped up by view-through conversions.
recommended_action: "Before building any remarketing structure, define Engaged Audience and Existing Customers segments and read the Audience Segments breakdown to see how much remarketing is already happening. Treat separate remarketing as a rare exception, not the rule."
context: Sales campaigns with Advantage+ Audience enabled; he notes higher shares for new campaigns and bottom-of-funnel goals.
business_type: unstated
spend_level: null
conversion_volume_context: "20-25% typical, 10-40% range"
research_question_ids: [F1, G2]
question_link_origin: prospective
published_at: null
source_url: https://www.jonloomer.com/meta-ads-master-brief/
author: Jon Loomer
timestamp: "Remarketing Happens Automatically"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Percentages presented as what the Audience Segments report 'typically reveals' across accounts he has examined; he credits the tool with changing his own understanding. No dataset published, no per-account figures shown. **Source is UNDATED**, and Audience Segments availability/behaviour may have changed."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "Breaking down a Sales campaign this way typically reveals that Meta spends roughly 20–25% of budget on remarketing without any inputs (sometimes 10–40%…). **The implication is decisive:** if Meta already reaches these people, a separate remarketing campaign just reaches them twice, creating auction overlap."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **The strongest external support found for F1's deferral, and it reframes the question.** F1 was deferred because DR has no warm pool worth targeting; this claim says the more important reason is that a separate structure would be *redundant* rather than merely premature — Meta is already allocating a fifth or more of budget to warm users unprompted. It also converges with Foxwell's harvesting diagnostic on the same reporting surface. Two DR-specific cautions: the Audience Segments report requires a **Sales objective**, which A1 has not settled, so availability is conditional on a decision not yet made; and his warning that remarketing metrics are propped up by view-through conversions is doubly relevant to DR, whose G1 setting includes a 1-day view window.

---

### creative_testing — Persona-targeted ads belong in the same ad set

```yaml
topic: creative_testing
claim: Ads written for different personas do not need separate ad sets — place them in one ad set and let Meta match each ad to the right person. Keep text variations within an ad similar in style, persona or angle so results are not watered down.
recommended_action: "Put persona-specific creative in a single ad set rather than building an ad set per persona."
context: Creative structure under current delivery; he notes a Meta creative workflow in test allowing up to 10 assets per ad with per-creative breakdowns.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, E2]
question_link_origin: prospective
published_at: null
source_url: https://www.jonloomer.com/meta-ads-master-brief/
author: Jon Loomer
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as practice; no test presented. **Source is UNDATED.**"
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "You don't need separate ad sets per persona; place persona-focused ads in the same ad set and let Meta match them."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** Resolves the practical tension between Dara Denney's persona-mapped creative and DR's single-ad-set architecture: **segment the message, not the delivery.** DR can brief distinct parent personas (safety-first, skill-development, convenience/logistics) as separate ads inside its one ad set without adding structure, which is the only version of persona thinking DR's budget can support. Undated source; the instruction nonetheless requires no modification and costs nothing to follow.

---

## Contradictions within this author (Phase 2)

- **Suggestions: harmless or useful?** In the targeting guide he says lookalike suggestions "probably" do not hurt and might help new accounts, then says he has "serious doubts whether they make a difference" and that Meta removed language indicating they are prioritized. He is candid that the impact is unknowable, which is honest but leaves no operating rule.
- **Simplicity as default vs exception.** "One campaign, one ad set" is stated as the efficient starting point and immediately qualified as "the starting point, not an absolute rule", without specifying what a legitimate reason to add complexity looks like — the same gap C4 fills for DR with explicit revisit triggers.

## Open questions from this author (Phase 2)

1. The performance-goal restriction counts (11 detailed-targeting, 9 lookalike) are precise and checkable. **Confirm against first-party Meta documentation** — this is the highest-value validation task from this file.
2. Audience Segments requires a Sales objective. If A1 resolves toward Leads → Website, does DR lose access to the diagnostic that would prove how much remarketing is already happening?
3. His value-rules example adjusts bids by age. Can value rules be applied on a geographic or custom-audience-label basis in a way that would encode DR's actual qualifier (serviceable catchment), and what data would DR need to label those audiences without touching child data?
4. `meta-ads-master-brief` is undated and carries three of these claims. Its real publication date should be established before any of them informs a decision.

---

# Phase 3 — full YouTube corpus review (2026-08-19)

**Run:** `knowledge/research-runs/2026-08-19_phase3-full-video-extraction/`
**Method:** every video read start to finish, chronologically. **No passage sampling** — that was the Phase 2 defect this run exists to correct.

## Corpus coverage

```yaml
downloaded_videos: 60
fully_reviewed: 60
useful: 35
duplicative: 9
low_value: 10
not_relevant: 6
unavailable: 0
words: 54891
date_range: 2025-12-31 .. 2026-08-19
tier: CURRENT (60/60)
```

Format: the *Pubcast Shots* podcast — solo episodes on a topic he chose, alternating with listener-question episodes. 3-12 minutes each. Every episode ends with a promotion for his own products (Power Hitters Club Elite, coaching, The Loop, ad briefs); **all sponsor reads are his own and are excluded from claims.**

**This is the densest and most DR-relevant single corpus in the knowledge base.** Reason: he is the only panel member whose entire thesis is built for *small budgets and simple structures*, and the only one publishing at weekly cadence inside the recency window. His limitation is the mirror image: **he does not run a local business and says so.**

---

## ⚠ His method changed mid-corpus — the finding passage sampling would have destroyed

| Period | Position on introducing new creative |
|---|---|
| **2026-01-06 → ~2026-04** | **Start every new ad set with a creative test** using Meta's native creative testing tool, *inside the ad set where the ads will live.* Rationale: you learn how each ad performs on forced equal budget, and the tool cannot test *existing* ads, so testing later means duplicating ads — "super messy." |
| **2026-05-04 onward** | **Superseded by "push delivery to this ad."** *"There's no longer a reason to start new ads with a test because I can always answer questions later with push delivery if necessary. And I no longer feel like I need to create at least two ads at a time."* |

**Any claim sourced from his January material must carry the May supersession.** Both positions are recorded below; neither is deleted.

---

## Claims — Phase 3

### campaign_structure — The legitimate reasons to split, and every one is budget-gated

```yaml
topic: campaign_structure
claim: Separate campaigns or ad sets are justified only by a specific business reason - separate objectives, separate product lines needing dedicated budget, promoting multiple locations that each need dedicated budget, or controlling remarketing share for a brand with a very large warm audience - and in every case only if there is enough budget to drive meaningful results in each one.
recommended_action: "Before adding a campaign or ad set, name the business reason and confirm each resulting unit can still be funded to a meaningful result; otherwise consolidate."
context: Listener question - are there situations where multiple campaigns are still recommended.
business_type: unstated
objective: conversions (implied throughout)
spend_level: null
conversion_volume_context: null
research_question_ids: [C1, C2, E3]
question_link_origin: prospective
published_at: 2026-01-15
source_url: https://www.youtube.com/watch?v=-DE7MHI6YLo
author: Jon Loomer
timestamp: "full episode, 5:25"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD. Stated as his standing recommendation with reasoning; no account example or data attached to any of the four cases."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "you need to promote multiple locations for your business. So you need to dedicate separate budget to each location… But even in these cases, you know what I'm gonna say. You need to have the budget to efficiently drive results in each campaign or ad set. If not, you're just making results worse for the sake of complexity."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **This is the multi-location evidence E3 was missing, and it is better evidence than the Ben Heath passage that previously carried that role.** Heath's version came from an *awareness* campaign optimizing for reach; this is a conversion-campaign statement, from an operator in a different cluster, and it supplies the conditional Heath never gave: **location separation is legitimate in principle and budget-gated in practice.** For DR at current spend that resolves cleanly to *stay bundled* — and it gives DR a stated revisit trigger (per-campus budget sufficient for meaningful results) rather than the `NOT_DISCLOSED` Heath left behind.

---

### creative_testing — Meta's native creative testing tool keeps the test inside the live ad set

```yaml
topic: creative_testing
claim: Meta's creative testing tool allocates a defined share of an existing campaign or ad-set budget to a temporary A/B test of up to five (or ten) new ads for a chosen duration and success metric, spreading budget evenly during the test; when the test ends the ads keep running in the same ad set under normal delivery. Existing ads cannot be tested.
recommended_action: "Introduce new creative as a test inside the ad set where the ads will live, rather than building a separate testing campaign and migrating winners."
context: His stated process for introducing all new ads, as of early 2026. He starts a new ad set with a test of two to five ads and assigns 100% of budget because no other ads exist yet.
business_type: info_product (his own account)
objective: conversions
performance_goal: leads / purchases
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D2, D3, C1]
question_link_origin: prospective
published_at: 2026-01-06
source_url: https://www.youtube.com/watch?v=b6_4nv_nLPU
author: Jon Loomer
timestamp: "full episode; process described 2:30-5:10"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD, demonstrated as his own process across several episodes. The tool's mechanics are described from the UI. No performance comparison against any other testing method is presented."
evidence_strength: weak
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

> "One of the advantages of the creative testing tool is that you can keep your ads in the existing ad set… When I create a new ad set, it starts with a test. So, I don't immediately publish 20 or 30 ads. It will begin with a small handful, somewhere between two and five."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **This is the mechanism that resolves the contradiction Dara Denney left open** — she prescribes introducing creative into the live structure at low budget *and* reports that doing so has repeatedly destabilised performing campaigns, with a separate-campaign mitigation DR cannot fund. A native in-ad-set test is a mitigation that costs **no additional structure**. It also independently lands on **2-5 ads**, bracketing DR's provisional 2-3.
⚠ **He states his own volume floor and it applies to DR:** *"if I'm testing five ads at $20 per day to sell something, I'm unlikely to get the volume necessary to learn anything all that meaningful"* — and separately, five ads on $50/day for a week is *"$10 per day for each ad… that's where you might want to test two ads at a time or extend the test to two weeks."* The **arithmetic** (ads × days × budget must clear the conversion volume needed for a read) transfers exactly; the dollar figures are `PRACTITIONER_SPECIFIC` and are not adopted. **Availability of this tool in DR's account is unverified.**

---

### creative_testing — Push delivery supersedes test-first, and makes controlled exposure structure-free

```yaml
topic: creative_testing
claim: A newer feature, "push delivery to this ad", forces a set percentage of budget to a single existing ad for a designated period. Because questions about an under-delivered ad can now be answered after the fact, he no longer starts new ads with a creative test and no longer feels obliged to create at least two ads at a time.
recommended_action: "Use push delivery to answer 'would this ad have worked if funded?' rather than restructuring, splitting budget, or killing the dominant ad."
context: Announced change to his own process. He states repeatedly that he does not yet have the feature.
business_type: info_product (his own account)
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D3, D4]
question_link_origin: prospective
published_at: 2026-05-04
source_url: https://www.youtube.com/watch?v=bz2qGzNBbRo
author: Jon Loomer
timestamp: "full episode; feature discussed 1:40-3:10"
confidence: high
evidence_basis: opinion
evidence_basis_details: "OPERATOR_METHOD stated as intent, NOT as result. He says plainly: 'I unfortunately don't have it yet, but I'm going to use the hell out of it when I do.' No outcome of any kind is reported. In a later episode he tempers it further - push delivery and killing the dominant ad are 'more for peace of mind than they are for likely solutions'."
evidence_strength: none
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

> "you can push delivery to a single existing ad for a designated amount of time… There's no longer a reason to start new ads with a test because I can always answer questions later with push delivery if necessary." · and later, on an ad taking 50% of budget: *"If you're getting 10% to one ad, push that to 30% for a few days or a week and see what happens… the most likely result is that you'll confirm that pushing that budget didn't help."*

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** untested
**reason:** DR holds that *"no-spend is an allocation condition, not automatically a creative verdict"* and that *"controlled exposure can be justified conditionally."* Push delivery is **a native, in-place, non-structural way to buy that answer** — no second campaign, no second ad set, no manual budget split, which is what made controlled exposure unaffordable for DR before. **But treat this as a lead to verify, not evidence:** he never used it, reports no outcome, and predicts the most likely result is that forcing budget changes nothing. **Check availability in DR's Ads Manager before it informs any plan.**

---

### creative_strategy — Stack creative diversity in phases rather than launching a large batch

```yaml
topic: creative_strategy
claim: At modest budget, do not implement Meta's creative-diversification guidance literally with ten or twenty ads at once; launch one coherent theme (as few as one or two ads), let it run one to two weeks, and only if aggregate results are unsatisfactory build a second, uniquely different set - different format, visuals, personas, messaging.
recommended_action: "Add creative in phases, learning from each batch before building the next, instead of front-loading diversity."
context: Worked through his own account - a new ad set for a lead magnet, five image variants differing only by colour, run as a 7-day creative test taking the full budget, then a completely different second phase.
business_type: info_product (his own account)
objective: leads
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D2, D4]
question_link_origin: prospective
published_at: 2026-01-20
source_url: https://www.youtube.com/watch?v=21xBd19tc0w
author: Jon Loomer
timestamp: "full episode; own-account example 2:40-5:00"
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "REAL_ACCOUNT_EXAMPLE from his own account with the structure and sequence described concretely - but no result is reported for either phase. The method is shown; the outcome is not."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "for the rest of us, it can be a complete waste of time, energy, and resources… Meta will almost always focus most of your budget on a small number of ads. And you'll be asking yourself why you ever bothered." · restated 2026-06-29: *"Truthfully, you can launch with just one or two."*

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **The most directly usable creative-operations guidance in the entire corpus for DR's scale.** Every other practitioner's diversification advice presumes production capacity and budget DR does not have; this explicitly carves out the modest-budget case and gives a sequence rather than a volume target. It supports DR's small-batch and deliberate-batching hypotheses, and it supplies the missing decision rule between batches: **judge the ad set in aggregate, and only build the next phase if aggregate performance is unsatisfactory.** Note he pointedly ignores Meta's own "five colour variants aren't diverse" guidance when his goal is to isolate one variable — a useful precedent for DR testing a single message dimension.

---

### creative_strategy — Creative fatigue is usually misdiagnosed, and the exception is local businesses

```yaml
topic: creative_strategy
claim: Most apparent creative fatigue is actually the algorithmic shift from an exhausted remarketing audience to prospecting; the true test of an ad is its performance after that shift. Genuine creative fatigue is now rare - except where the audience is genuinely limited, which he names as local businesses and isolated remarketing audiences, where Meta runs out of new people and reaches the same individuals repeatedly.
recommended_action: "Before treating a decline as creative fatigue, break results down by audience segment to check whether remarketing share has fallen; judge an ad by its performance in the prospecting-dominant period."
context: "He cites an account spending close to $1,000 per day that ran the same two ads for two years and reports the ads are more effective today than two years ago."
business_type: unstated (the $1,000/day account is not identified)
spend_level: "~$1,000/day for the two-year example"
conversion_volume_context: null
research_question_ids: [D1, D4, E1, F1]
question_link_origin: prospective
published_at: 2026-07-01
source_url: https://www.youtube.com/watch?v=vI592T5NXdk
author: Jon Loomer
timestamp: "full episode; local-business exception ~1:50; two-year example ~4:20"
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "MULTI_ACCOUNT_EXPERIENCE plus one REAL_ACCOUNT_EXAMPLE ($1,000/day, two ads, two years, 'more effective today'). No CPA, ROAS or conversion figures for that account; the mechanism is demonstrable via breakdowns but no breakdown is shown on screen."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "The most common situation when this would be a problem now is when you have a very limited audience. So, that could be because you're a local business or because you're isolating a remarketing audience. When that's the case, Meta quickly runs out of new people to reach. So, you just keep reaching the same people over and over." · **"You can't do anything about a limited audience when running ads for a local business."**

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **This is the single most important claim in his corpus for DR, and it cuts against DR's interest.** The panel's dominant message — creative fatigue is overblown, ride winners for months — is explicitly scoped by its own author **to exclude businesses like DR.** DR is geo-bounded to campus catchments; by his reasoning the pool empties and re-exposure is unavoidable, which makes creative refresh a **structural necessity for DR rather than the optional lever it is for a national advertiser.** The transferable diagnostic (check remarketing share before blaming the creative) still applies. What does **not** transfer is his reassurance. ⚠ He is not a local operator and says so elsewhere — this is reasoning from mechanism, not from a local account.

---

### targeting — The only inputs he touches are locations and exclusions

```yaml
topic: targeting
claim: He uses no audience suggestions, no age or gender restriction, no detailed targeting and no lookalike audiences, and almost never restricts by custom audience; the only targeting inputs he sets are locations and exclusions, which are audience controls Meta treats as hard constraints. Demographic problems are solved with value rules rather than restriction.
recommended_action: "Set location and exclusions only; leave age, gender, interests and lookalikes untouched and solve proven demographic problems with value rules."
context: A dedicated episode summarising his complete 2026 targeting approach.
business_type: info_product (his own account)
objective: conversions
spend_level: null
conversion_volume_context: null
research_question_ids: [E1, C4, F1]
question_link_origin: prospective
published_at: 2026-03-02
source_url: https://www.youtube.com/watch?v=WfoA-2u5KEA
author: Jon Loomer
timestamp: "full episode; summary 4:35-5:20"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD for his own account, supported by the value-rules and remarketing-share examples recorded below. The claim that suggestions do nothing is explicitly unprovable by his own admission - 'there's no way to prove one way or the other'."
evidence_strength: weak
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

> "In most cases, the only settings I touch are locations and exclusions, which are audience controls."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** DR's audience hypothesis is Advantage+ Audience baseline, hard business controls kept hard (location, adult minimum age, exclusions), no interests as a clean starting baseline. **This is that hypothesis, arrived at independently, stated as an operating default rather than a caveat.** It converges with Ben Heath's identical posture from a different cluster. The one DR-specific divergence: DR's adult-minimum-age control is a *business* constraint, not a performance choice, so it stays regardless of what he recommends.

---

### optimization — Value rules: two questions that must both be yes

```yaml
topic: optimization
claim: A value rule is warranted only when both conditions hold - you have information Meta does not (lead quality, customer lifetime value), and there is a problem proven in data (Meta is actually spending a large share of budget on the problem group). Value rules deliberately raise costs, so applying one without a proven problem is self-inflicted damage.
recommended_action: "Require both a genuine information advantage and a demonstrated misallocation in your own breakdowns before creating any value rule."
context: A corrective episode responding to advertisers over-using the feature. Criteria available at time of recording - age, gender, device platform, mobile OS, location, audiences, conversion location, placement.
business_type: info_product (his own account)
objective: leads
spend_level: null
conversion_volume_context: "he cites 40% of budget going to over-65s as the kind of misallocation that qualifies"
research_question_ids: [A3, E1]
question_link_origin: prospective
published_at: 2026-08-12
source_url: https://www.youtube.com/watch?v=j8803_J6Dug
author: Jon Loomer
timestamp: "full episode; the two questions 2:10-5:30"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD. The gate itself is reasoning, not data - but it is grounded in his own repeated account example (see below) and is unusually self-limiting for a practitioner recommending a feature."
evidence_strength: weak
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

> "value rules, by nature of what they do, intentionally increase costs. Why would you intentionally increase costs unless it's truly necessary?" · "The fact that people over 65 represent low-quality leads isn't enough by itself to apply a value rule because unless Meta is actually spending a large percentage of my budget there, there is no problem to be solved."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** A3 asks for an obtainable quality safeguard. The Phase 2 claim already on file records that value rules **worked** in his account; **this claim records the gate that stops DR from reaching for them prematurely.** Both are needed — without the gate, "use value rules" becomes exactly the reflexive micromanagement the rest of his corpus argues against. For DR the practical reading is: do not build a value rule until a DR breakdown shows real budget going somewhere DR knows is unqualified.

---

### measurement — Most advertisers should default to incremental attribution

```yaml
topic: measurement
claim: Standard attribution (7-day click, 1-day view, 1-day engaged view) credits conversions that the ad may not have caused, which inflates results - especially for remarketing. Incremental attribution instead models whether the ad actually caused the conversion. He believes the vast majority of advertisers would be better off using incremental full-time, though he does not always use it himself because he interrogates his own results.
recommended_action: "Either switch to incremental attribution, or use breakdown by attribution setting and compare attribution settings before any scaling or pausing decision."
context: An evolving opinion he explicitly flags as having changed over the prior year.
business_type: info_product (his own account)
spend_level: null
conversion_volume_context: null
research_question_ids: [G1, G2]
question_link_origin: prospective
published_at: 2026-07-29
source_url: https://www.youtube.com/watch?v=Xx_hBs9Re8s
author: Jon Loomer
timestamp: "full episode"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_OBSERVATION - 'I found that results from incremental attribution tend to line up more or less with your click-through attribution results from standard attribution.' Stated as his finding, with no dataset, no account named and no figures."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "the vast majority of advertisers make mistakes because they don't know what to do with results that come from standard attribution… I found that results from incremental attribution tend to line up more or less with your click-through attribution results."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** untested
**reason:** DR's starting hypothesis is 7-day click / 1-day view. **This is the first source in the knowledge base arguing that the reporting default is the wrong default for most advertisers**, and it is directly relevant because DR's measurement design already treats the business registration ledger as final truth. The convergence he reports — incremental ≈ click-through — is exactly what DR would want to verify against its own ledger. Not adopted: it is an unquantified observation about accounts unlike DR's, and DR's conversion volume may be far too low for a modelled attribution to behave the way it does at his scale.

---

### measurement — Judge in aggregate, on 7-day windows, and expect randomness at low volume

```yaml
topic: measurement
claim: Day-to-day results are dominated by randomness, most severely at low conversion volume; performance should be evaluated at the ad-set (or campaign, under CBO) level in aggregate over roughly seven-day windows, not per ad and not per day. Five ordinary causes of a sudden drop - randomness, your own recent changes, competitive/seasonal CPM shifts, website problems, event delays - should be excluded before concluding anything about creative.
recommended_action: "Diagnose sudden performance drops against the five ordinary causes and a 7-day window before changing creative or structure."
context: "He names roughly 10 conversions per day as the volume range that produces the wildest swings."
business_type: unstated
spend_level: null
conversion_volume_context: "~10 conversions/day cited as the volatile range"
research_question_ids: [D4, G2]
question_link_origin: prospective
published_at: 2026-03-09
source_url: https://www.youtube.com/watch?v=awYIlUr2RGs
author: Jon Loomer
timestamp: "full episode"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD plus one unquantified personal example - he held an underperforming ad set through a week of below-average results and it recovered. No data shown."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: NOT_APPLICABLE
```

> "You will drive yourself crazy obsessing over day-to-day results, especially if you're dealing with low volume of results… Evaluate performance based on 7-day windows because averages are more important and predictable than spikes."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **DR sits below the volume he names as the volatile range**, which makes this more binding for DR than for him. It supports DR's `NOT_EVALUABLE` verdict as a legitimate outcome and its rejection of a fixed calendar gate, while supplying the diagnostic checklist DR's measurement layer 1 needs. Costs nothing and requires no structure.

---

### campaign_structure — Every change must solve a problem proven in data

```yaml
topic: campaign_structure
claim: Restrictions and added structure should each be traceable to a specific problem demonstrated in the advertiser's own breakdowns; the common alternative is decisions based on assumptions about the ideal customer. He names one campaign with five ad sets of one ad each - built to force Meta to show every ad - as a case where the control gained is worthless and the fragmentation, auction overlap and diluted budget are real.
recommended_action: "For each restriction or added structure, state the problem it solves and the data proving that problem exists; if you cannot, remove it."
context: A recurring theme, stated most directly in two episodes.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C1, C2, C4, E1]
question_link_origin: prospective
published_at: 2026-06-08
source_url: https://www.youtube.com/watch?v=A8DT8k3s2GQ
author: Jon Loomer
timestamp: "full episode; the five-ad-set example 1:20-2:30"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD, drawn from accounts he has audited. No specific account or figures given. The five-ad-set example is second-hand - someone described their setup to him."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "If you're optimizing for purchases, you're splitting up your budget five ways to test ads. You'll already struggle to get meaningful data, and now you're all but guaranteeing it."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** Directly supports DR's rejection of manual forcing and its one-campaign / one-ad-set posture, and names the specific anti-pattern (one ad per ad set for exposure control) that **Ben Heath's omnipresent structure implements deliberately.** Recording both keeps that disagreement visible rather than resolved by preference — see the cross-panel table below.

---

### creative_testing — Too many ads in one ad set may hurt, flagged by him as a hunch

```yaml
topic: creative_testing
claim: Meta removed its former guidance of no more than six ads per ad set around the Andromeda updates. He now suspects, without proof, that too many ads for the available budget can leave the delivery algorithm "a bit lost", and that pruning ads Meta rarely shows is a legitimate thing to try when aggregate results are poor.
recommended_action: "Start with a couple of ads and add more only as needed; if results are poor after many rounds, consider pausing the ads Meta rarely shows."
context: Listener question about whether ad volume can hurt delivery.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D2]
question_link_origin: prospective
published_at: 2026-05-06
source_url: https://www.youtube.com/watch?v=lNP3lybp5Yg
author: Jon Loomer
timestamp: "full episode"
confidence: medium
evidence_basis: opinion
evidence_basis_details: "OPERATOR_OBSERVATION explicitly self-labelled as unproven: 'that truly is just a hunch at this point, and Meta hasn't come out and said it.' Also a reversal of his own prior advice, which he states."
evidence_strength: none
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

> "I've just had the sense that the delivery algorithm can get a bit lost when it has too many options for the budget. Now, that truly is just a hunch at this point."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** Recorded **because of the hedge, not despite it.** It is the corpus's only voice suggesting an upper bound on creative volume at modest budget, and it points the same direction as DR's small-batch hypothesis — but an explicitly unproven hunch cannot support a DR rule, and the removal of Meta's six-ad guidance means there is no documented number to fall back on either. Per the numeric-threshold rule: **no number is adopted.**

---

### optimization — Do not "warm up" a new account with top-of-funnel campaigns

```yaml
topic: optimization
claim: Building followers, running awareness/engagement/traffic campaigns, or "seasoning the pixel" before running conversion campaigns is counterproductive, because top-of-funnel optimization fills account history and the built-in remarketing audiences with low-quality engagement. Optimize for the real action from day one. A new ad account will also carry a low daily spending limit that rises only by spending against it.
recommended_action: "Start a new account optimizing for the actual desired conversion; do not run warm-up campaigns."
context: Listener question - new Facebook page, new ad account, new dataset.
business_type: unstated
objective: sales / leads
spend_level: null
conversion_volume_context: null
research_question_ids: [A2, A3]
question_link_origin: prospective
published_at: 2026-04-15
source_url: https://www.youtube.com/watch?v=lc0heU-54ik
author: Jon Loomer
timestamp: "full episode"
confidence: high
evidence_basis: opinion
evidence_basis_details: "OPINION with a stated mechanism. 'There is no evidence that starting with top-of-the-funnel actions will be beneficial' - he offers none for the converse either."
evidence_strength: none
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** untested
**reason:** Relevant if DR ever opens a fresh account or a new campaign for a new season, and a direct counter to widely-repeated warm-up folklore. **It does not resolve DR's open objective question** — Wave 1A settled that from first-party documentation, which outranks this. The **daily spending limit** point is a concrete operational fact worth knowing at DR's scale.

---

### measurement — Server-side tracking, cheapest viable path

```yaml
topic: measurement
claim: The website pixel alone is no longer dependable because of privacy law and browser behaviour, producing incomplete data and worse optimization. The simplest route to Conversions API coverage for web events is the Conversions API Gateway - via Stape at roughly $10/month, or a no-cost one-click option he references later - which reuses the events already defined on the pixel and deduplicates them. Sending CRM events is a much larger technical lift with real deduplication risk; one clean approach is to send CRM events only for transactions that never touch the website.
recommended_action: "Cover web events through the Conversions API Gateway first; add CRM events only where a purchase completes off-site, and only with deduplication handled."
context: Listener question about the cheapest reliable setup. He declares no affiliation with Stape and says he has used it about five years.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [A3, G2]
question_link_origin: prospective
published_at: 2026-01-08
source_url: https://www.youtube.com/watch?v=9kAGSaHQERk
author: Jon Loomer
timestamp: "full episode"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD - five years of personal use of the named tool. No match-rate or performance data presented."
evidence_strength: weak
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** DR's signal density is a live constraint and its registration completes in a business system. **This is the most concrete and cheapest implementation path anywhere in the corpus for improving that signal**, and the CRM-events-only-for-off-site-transactions pattern is close to DR's actual shape. Naming a specific vendor is `PRACTITIONER_SPECIFIC` and is not a recommendation to adopt it; the architecture is what transfers. Any DR implementation must respect the child-data constraints A3 already recorded.

---

### targeting — Location targeting reaches people "living in or recently in" the area

```yaml
topic: targeting
claim: Meta location targeting is imperfect and will reach people both living in and recently in the targeted location; he accepts this and states there is no solution for it. He explicitly notes he has little reason to worry about it because he does not run ads for a local business.
recommended_action: null
context: One item in a list of seven things he deliberately does not spend time on.
business_type: info_product (his own account)
spend_level: null
conversion_volume_context: null
research_question_ids: [E3]
question_link_origin: prospective
published_at: 2026-06-10
source_url: https://www.youtube.com/watch?v=HkNfvTLbVaM
author: Jon Loomer
timestamp: "full episode; location item ~3:20"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_OBSERVATION, and an explicit disclaimer of local expertise in the same breath. No data."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "Now, granted, I have very little reason to worry about this cuz I'm not running ads as a local business. But, I also fully understand how imperfect Meta's location targeting is. Even when targeting by country, I'll reach people both living in or recently in that location."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** **The mechanism is exactly what DR's geography hypothesis already assumes** — campus radius is a *serviceability proxy*, not proof a child attends that school, and creative plus landing page must carry the qualification. This is an independent statement that the location control leaks, from someone with no incentive to say so. **His conclusion — accept it, do not fight it — does not transfer**, because for him location error is cosmetic and for DR it is the difference between a serviceable and an unserviceable registration. Note the honesty marker: he disclaims local expertise in the same sentence, and that disclaimer should attach to every geo statement of his.

---

### platform_changes — Customer lifecycle strategy does nothing new (a debunk, first-hand)

```yaml
topic: platform_changes
claim: The "customer lifecycle strategy" feature, widely described on social media as giving Meta new powers to identify and exclude existing customers, does nothing new. Having obtained the feature, he reports it still requires you to manually select the custom audiences to exclude; it only moves that exclusion to the top of the ad set and makes the intent explicit.
recommended_action: "Require screenshots or first-party documentation before acting on a claimed new feature capability."
context: Used as a case study in how Meta-ads misinformation spreads from a single screenshot.
business_type: n/a
spend_level: null
conversion_volume_context: null
research_question_ids: [F1]
question_link_origin: prospective
published_at: 2026-06-22
source_url: https://www.youtube.com/watch?v=uRHIMFwpMMI
author: Jon Loomer
timestamp: "full episode"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "REAL_ACCOUNT_EXAMPLE - he has the feature and describes what it actually does, having previously and publicly doubted the viral claims. One of the few first-hand corrections in the corpus."
evidence_strength: moderate
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** low · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** n/a
**reason:** No DR decision depends on this feature. Retained because **it is a documented instance of a viral practitioner claim being wrong**, which is direct evidence for this domain's own rule that agreement among practitioners is weak evidence — the claim spread through experienced advertisers and large brands alike before anyone with the feature checked it. `evidence_strength: moderate` is the highest grade awarded anywhere in this file, and it is awarded to a **debunk**.

---

## Real-account evidence in this corpus

| # | What he did | What he reported | Grade |
|---|---|---|---|
| **L-A** | Own lead-gen account: 65+ and 55-64 together consumed **70% of budget** at cheap cost and low quality. Bid **−50% on 65+, −20% on 55-64** via value rules instead of restricting age. | 65+ fell to the **lowest** share of budget; 55-64 fell below the 18-24 group. **Distribution before/after only — no CPL or quality figures.** | `REAL_ACCOUNT_EXAMPLE` |
| **L-B** | Defined audience segments, broke results down by segment across an ad set's life. | Remarketing takes **~25% of budget early, falling to 5-10%** as the warm pool exhausts. Offered as the mechanism behind "starts strong then declines". | `REAL_ACCOUNT_EXAMPLE` |
| **L-C** | Duplicated an ad carrying **6,000+ comments** so the copy started from **zero social proof**; original had run over a year for a professional service, peaking at **$50/lead**. | New ad ran at **$46/lead over its first two weeks**, with **no build-up period**. He calls the gap "probably within a range of randomness that doesn't matter". | `REAL_ACCOUNT_TEST` (n=1, uncontrolled) |
| **L-D** | 2024: built an ad with **no hyperlink anywhere**, instructing viewers to click the image and then separately visit a page that fired a conversion event. | Meta reported **20+ conversions, all as click-through** — proving click-through then counted non-link clicks. Meta has since split these into **engage-through**, window **1 day** vs click-through's 7. | `REAL_ACCOUNT_TEST` — **a genuine designed experiment, the strongest single piece of evidence in his corpus** |
| **L-E** | Held an underperforming ad set through a full week rather than killing it. | It recovered. Used to argue for 7-day windows. | `OPERATOR_OBSERVATION`, unquantified |
| **L-F** | (Second-hand) An account spending ~**$1,000/day ran the same two ads for two years.** | Reports the ads are **more effective today than two years ago**. No figures, account not identified. | `REAL_ACCOUNT_EXAMPLE`, weak |

---

## Contradictions within his own corpus

1. **Creative testing tool: "a huge part of my process" (Jan) → "no longer a reason to start new ads with a test" (May).** He states the reason — push delivery. **Evolution, not inconsistency, but January claims must not be quoted as current.**
2. **"Let low-spend ads run" → "pruning may help."** He acknowledges the reversal and labels the new position a hunch.
3. **"Never restrict by age or gender" alongside an entire feature for adjusting delivery by age and gender.** Resolved by him: restriction is the old tool, value-rule bidding is the new one.
4. **Recommends against separate remarketing structures, then lists when he would build one** (very large warm audience, or prospecting materially more profitable). Conditional, not contradictory.
5. **Push delivery framed as the reason to abandon test-first (May 4) and, two weeks later, as "more for peace of mind than… likely solutions" (May 20, restated June 29).** Enthusiasm and expectation are not aligned; both are recorded.

## Changes over time
His trajectory across eight months runs consistently in one direction: **less control, less structure, fewer ads at launch, more weight on aggregate results and on interrogating attribution.** The only movement *toward* intervention is the pruning hunch (2) and the value-rules gate — and the gate is itself a restriction on intervening.

## Conflicts with other operators

| Question | Loomer | Opposing voice |
|---|---|---|
| Separate testing campaign? | **No** — "counterproductive, especially for anything other than the highest budgets"; test inside the live ad set | **Ben Heath**: yes, 80/20, because Meta starves new ads next to winners · **Dara Denney**: yes, above ~$1,000/day |
| Many ad sets for exposure control? | **No** — names one-ad-per-ad-set as the anti-pattern; fragmentation, overlap, diluted budget | **Ben Heath**: 14 single-ad ad sets, deliberately, for frequency pacing |
| Creative fatigue? | **Rare and usually misdiagnosed** — *except for local businesses*, where he says it is unavoidable | **Foxwell ecosystem**: volume-driven refresh as standard practice |
| Separate remarketing structure? | **No** — remarketing happens naturally, provable by breakdowns | **Sam Piliero**: builds explicit retargeting structures |
| Persona-based ad sets? | **No** — same ad set, different ads | — (agrees with Denney's creative-side segmentation) |
| Attribution default? | **Incremental for most advertisers** | — (no other panel voice on this) |

## Relevance to DR — where he is strongest and where he must not be used
**Strongest:** small-budget structure discipline, creative cadence at modest budget, the in-ad-set testing mechanism, attribution literacy, diagnosis before action, and the tracking-foundation path. On these he is the best-matched source in the knowledge base.

**Must not be used for:** anything geo-specific. **He states plainly that he does not run ads for a local business.** His acceptance of location leakage, his combine-similar-countries habit, and his reassurance about creative fatigue are all reasoning from a national/global account. The one place he speaks to local businesses directly — the creative-fatigue exception — **works against** DR, and is recorded as such.

## Platform claims awaiting Meta validation
- Detailed targeting is a suggestion under **11** performance goals; lookalikes under **9**. *(Carried from Phase 2; restated in this corpus.)*
- Location targeting and custom-audience **exclusions are always hard constraints**, never suggestions.
- Click-through now requires a **link** click; social and other clicks moved to **engage-through** with a **1-day** window.
- Meta **removed** its "no more than six ads per ad set" guidance.
- Creative testing tool mechanics: up to 5 (or 10) ads, **cannot test existing ads**, ~20% budget default, even spend during the test, ads persist afterwards.
- **"Push delivery to this ad"** exists and behaves as described. ⚠ **He did not have the feature when he described it.**
- Customer lifecycle strategy adds no new exclusion capability. *(He has the feature — first-hand, but still a practitioner report.)*
- Value rules criteria list, and the audience-label extension he is testing.
- Incremental attribution "tends to line up with click-through results."
- A **no-cost one-click Conversions API Gateway** option exists.

## Open questions from this corpus
1. **Is the creative testing tool available in DR's ad account, and is push delivery?** Both underpin the highest-value claims here and neither is verified for DR.
2. **His volume floor is stated but never derived.** "Five ads at $20/day won't teach you anything" — what is the underlying rule? Without it, the arithmetic cannot be scaled down to DR's budget, which is exactly what DR needs.
3. **The local creative-fatigue exception is asserted, not measured.** He gives no way to detect pool exhaustion in a geo-bounded audience or to judge how fast it happens. For DR this is the most consequential unknown in the file.
4. **Does the remarketing-share decay curve (25% → 5-10%) look different when the warm pool is a few thousand parents rather than a national list?** The mechanism predicts faster exhaustion; nobody in the corpus measures it.
