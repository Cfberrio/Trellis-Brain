---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/ralph-burns.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/ralph-burns.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Ralph Burns"
  - "Tier 11"
  - "Perpetual Traffic"
---

# Ralph Burns (Tier 11 / Perpetual Traffic)

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/ralph-burns.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** ralph-burns
**Watchlist priority:** 1
**Topics:** campaign_structure · measurement · targeting · budgeting · bid_cost_controls · lead_gen
**Sources processed:** 5
**Last updated:** 2026-08-19
**Evidence model:** v2 — every claim carries `evidence_basis` / `evidence_basis_details` / `evidence_strength`. All evidence is **self-reported by the speakers**; nothing here is independently verified.

**Why this source exists in the panel:** it is the only entry with verified non-ecommerce breadth. Tier 11's published client examples include service and subscription businesses (Lawn Doctor, AirSculpt, Credit Repair Cloud, Mindvalley — tiereleven.com, retrieved 2026-08-19). Every other panel member reasons from DTC. That does **not** make his advice transferable to DR by default; see each claim's transferability read.

## ⚠ Two source-integrity warnings — read before using any quote

1. **Ralph Burns is the host, not always the claimant.** Perpetual Traffic is an interview show. Most operating detail below comes from **John Moran** (Tier 11 media buyer, runs their paid test accounts), **Ricardo Pouwels** (Tier 11 growth strategist), or outside guests. Each claim's `author` field names the actual speaker. Attributing a guest's claim to Burns would be a fabrication, and treating Burns + his own staff as independent voices would violate the domain's consensus rule — **Tier 11 is one brand talking to itself.**
2. **Text is auto-generated captions.** The transcripts contain systematic ASR corruption: "Ncac" (nCAC), "Cappy imports" (CAPI imports), "cheer 11"/"to 11"/"211" (Tier 11), "Jem" (GEM), "purchase a moon" (purchase immune). Quotes below are reproduced **as captured**, not cleaned, so the corruption stays visible. **No numeric figure from these transcripts may be promoted to a decision input without checking the source audio.** Confidence is capped at `medium` for that reason alone.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims |
|---|---|---|---|---|
| `https://perpetualtraffic.com/podcast/episode-765-how-advantage-sales-is-changing-the-meta-ads-game-forever` | podcast page + transcript | null (page carries no first-party date; HTTP Last-Modified only) | 2026-08-19 | 3 |
| `https://perpetualtraffic.com/podcast/episode-767-how-to-crush-it-with-glp-1s-trts-on-meta-using-the-sticky-pixel-strategy` | podcast page + transcript | null | 2026-08-19 | 2 |
| `https://perpetualtraffic.com/podcast/episode-791-5-missed-forecasts-then-one-budget-shift-then-4-straight-hits` | podcast page + transcript | null | 2026-08-19 | 2 |
| `https://perpetualtraffic.com/podcast/episode-801-from-2-5m-to-4m-a-month-ad-spend-barely-changed-heres-why` | podcast page + transcript | **2026-07-28** | 2026-08-19 | 1 |
| `https://perpetualtraffic.com/podcast/episode-804-bad-data-and-10-minute-video-ads-were-killing-this-account-heres-the-fix` | podcast page + transcript | **2026-08-18** | 2026-08-19 | 2 |

**On the null dates:** the episode pages expose no machine-readable publication date; the crawl captured only an HTTP `Last-Modified` header, which is a server timestamp, not a publication date. Episode numbering (765 → 804) establishes **order**, and the two dated anchors (801 = 2026-07-28, 804 = 2026-08-18) establish that the numbered series is weekly — but interpolating dates for 765/767/791 would be manufacturing evidence, so they stay `null`. All five are inside the 2025-08→2026-08 window by corpus tier assignment; a claim leaning on *precise* recency must re-verify first.

**Stated context:** Tier 11 is an agency; the accounts discussed are DTC ecommerce, supplements, telehealth (GLP-1/TRT), a fishing app + store, and a premium pet brand. Spend levels stated in-episode range from **$25,000 to over $1,000,000** on a single scaling example, and one guest frames the advice as applying to brands "spending at least $50,000 a month". **DR spends roughly three to four orders of magnitude below that.**

---

## Claims

### campaign_structure — Consolidate geo-split campaigns when per-campaign volume is too thin to read

```yaml
topic: campaign_structure
claim: When budget is split across state-by-state campaigns and each is producing only a handful of weekly purchases (some zero), collapse them into one campaign and move the states into targeting instead.
recommended_action: Consolidate the split campaigns into a single campaign, target the desired states inside that campaign's targeting, and write creative whose message works across all of them.
context: An account splitting campaigns by US state at a budget too small to give each split meaningful volume.
business_type: ecommerce
spend_level: "~$150,000/month on Meta stated for this account"
conversion_volume_context: "5 to 10 purchases per week on one ad, some ads at zero"
research_question_ids: [C1, E3]
published_at: 2026-08-18
source_url: https://perpetualtraffic.com/podcast/episode-804-bad-data-and-10-minute-video-ads-were-killing-this-account-heres-the-fix
author: Tier 11 growth strategist (guest; name not resolvable from the captions)
timestamp: null
confidence: medium
evidence_basis: self_reported_case_study
evidence_basis_details: "Named client situation (fishing app + ecommerce store) with the pre-consolidation symptom quantified as 5-10 weekly purchases per ad; the post-change result is asserted qualitatively ('spending a lot more efficiently') with no figures."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "was with the budget that we're running, how are these getting sufficient spend on each state and that were targeting as well… at the end of the week you're only getting like maybe 5 to 10 purchases on on one of these ads, even that some are getting zero in some cases… So my thought is, why don't we just consolidate these campaigns down where we're splitting everything out, put it into one campaign… you don't have your state specific, but still target those states that you want to… put them in the targeting"

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **This is the closest structural analogue to DR found anywhere in the corpus.** It is the same decision E3 already resolved — geography belongs inside one campaign's targeting, not in separate campaigns — reached independently, by an operator, from the *same* diagnostic DR faces: the splits could not each accumulate readable volume. It does not prove DR's architecture; it removes the "but nobody does that" objection and gives C1/E3 the third independent structural voice C1 explicitly asked for. Note the asymmetry that keeps it honest: this account was thin **relative to a $150k/month budget spread across many states**; DR is thin in absolute terms. The reasoning transfers; the scale does not.

---

### targeting — Meta treats advertiser audience inputs as suggestions, and treats exclusions as seed data

```yaml
topic: targeting
claim: Uploaded audiences, lookalike seeds and exclusions are no longer binding instructions — Meta's documentation frames them as recommendations, and an exclusion list may be used as a seed to identify good customers rather than to suppress them.
recommended_action: null
context: Post-Advantage+ delivery; speaker contrasts it with the 2012-era custom-audience behaviour he used for years.
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: [E1]
published_at: null
source_url: https://perpetualtraffic.com/podcast/episode-761-why-meta-is-the-best-ad-platform-on-the-planet-in-2026-part-3
author: John Moran (Tier 11)
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Asserted as a reading of Meta's documentation ('you look in all of their documentation'); no document cited, no test shown."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "you can give us recommendations. We're going to view them as suggestions. And by the way, if you put them in as exclusions, we're just going to use that as a seed audience to figure out who's your best customer and completely ignore the exclusions"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** untested
**reason:** The **suggestion-vs-control distinction is already a platform fact for DR** — Wave 3 resolved it first-hand from Meta's own text, which is a stronger source than this claim. What this adds is a practitioner reporting the same asymmetry from the delivery side, plus a sharper allegation about **exclusions** specifically. That part matters to DR because E1's configuration relies on *Custom audiences to exclude* being one of the documented hard controls. **This claim and Meta's documentation appear to disagree about exclusions, and that conflict must not be resolved here** — flag it for the validation pass. No DR action follows from an unevidenced podcast assertion.

---

### targeting — Broad targeting self-corrects demographics that manual targeting would have forced

```yaml
topic: targeting
claim: Running deliberately broad (all genders, 18-65) in a heavily gender-skewed category still delivered to the correct demographic split, because delivery — not targeting — found the buyers.
recommended_action: Do not narrow demographics manually to match the known customer profile; let broad delivery find the split.
context: TRT (testosterone replacement) offer, a category the speaker states is ~90% male.
business_type: ecommerce
spend_level: null
conversion_volume_context: "campaign live since Christmas Eve; ~400 leads/day at the time of recording"
research_question_ids: [E1]
published_at: null
source_url: https://perpetualtraffic.com/podcast/episode-767-how-to-crush-it-with-glp-1s-trts-on-meta-using-the-sticky-pixel-strategy
author: John Moran (Tier 11)
timestamp: null
confidence: medium
evidence_basis: self_reported_case_study
evidence_basis_details: "Live account walked through on screen share; states the delivered audience came back ~91/9 male/female against an ~90% male market. Screen share is described, not independently verifiable from the transcript."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "my TRT, which is a male dominated industry with about 90% market share of men. Women, 65, 18. To 65, all gender. Is that the stupidest thing you'll ever do?… It's almost a 91 nine like we're getting 92 eight. And I mean, it's nailing it."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** Supports E1's decision not to hand-narrow demographics — but the mechanism it relies on is **volume**: at ~400 leads/day the delivery system has enough signal to find the 9-in-10. DR has no such signal density, so "broad will sort it out" is an untested promise at DR's scale. It also does **not** touch DR's actual qualification problem, which is residency and school attendance, neither of which delivery can infer. Adopt as reassurance about *demographics*; ignore as guidance about *qualification*.

---

### targeting — CAPI custom-event imports used to force new-customer acquisition when native exclusions fail

```yaml
topic: targeting
claim: With Advantage+ Sales defaulting on and native exclusions and existing-customer bid caps being ignored, the workaround is importing custom conversion events via CAPI segmented by new vs returning customer (and by product), then optimizing against those.
recommended_action: Import segmented custom events (new customer / returning customer / by product) through CAPI and optimize the campaign toward the new-customer event instead of relying on audience exclusions.
context: Advantage+ Sales campaigns after it became the default campaign type; ecommerce with a returning-customer base.
business_type: ecommerce
spend_level: "example figures from $3,517 spend upward; separately a $25,000 → $1,000,000+ scale example"
conversion_volume_context: "35 purchases in one cited cell, 50 in another"
research_question_ids: [A3, E1]
published_at: null
source_url: https://perpetualtraffic.com/podcast/episode-765-how-advantage-sales-is-changing-the-meta-ads-game-forever
author: John Moran (Tier 11)
timestamp: null
confidence: medium
evidence_basis: self_reported_test
evidence_basis_details: "Screen-shared comparison across campaign cells: without the new-customer event, 16 of 35 purchases were new; with it, 42 of 50. Speaker separately states he has spent 'over $1 million' of his own money testing. No underlying data exported or shown outside the screen share; figures are ASR-transcribed."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "when we exclude existing customers, when we set our existing customer bid cap to zero, it gets ignored… what if we wanted the immune purchases? But what if we had them? Only new customers… 50 sales, 42 new customers… We've increased this from a 50% to now. Like at 85%."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** The **principle is the most valuable thing Tier 11 says for DR**: when the platform will not respect an audience instruction, encode the distinction you care about **in the event you optimize toward** rather than in targeting. That is exactly the shape of A3's quality-safeguard question. The **implementation does not transfer and partly cannot**: it requires CAPI plus a customer database that can label events, and DR's participants are 6-12, where Meta's Business Tools Terms restrict what may be sent and what an event may be named or defined by — the same compliance gate A3 already flagged. Treat as evidence that event-level qualification is a real technique, not as a build instruction.

---

### bid_cost_controls — Set cost caps per product/margin, not one global target

```yaml
topic: bid_cost_controls
claim: A single account-wide cost cap is wrong when gross margin varies by product; the acceptable acquisition cost should differ per product because the profit it can fund differs.
recommended_action: Set cost caps (and acquisition-cost targets) per product according to that product's gross profitability rather than applying one blended target across the account.
context: Supplement basket where gross profitability ranges 70% down to 40% by product.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: []
question_link_origin: none
published_at: null
source_url: https://perpetualtraffic.com/podcast/episode-765-how-advantage-sales-is-changing-the-meta-ads-game-forever
author: John Moran (Tier 11)
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Argued from margin logic. The adjacent scaling figure ($25k → $1M+ with a 9% drop in cost per first-time customer) is attached by the speaker to the new-customer event strategy, not to per-product cost caps, and is therefore not counted as evidence for this claim."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "Their gross profitability varies from 70% down to 40%. Based upon the individual product… product A at a 70% gross profit, you should not have the same Ncac as product B with a 40% gross profit. It just doesn't make sense."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** The principle — acquisition cost ceilings follow unit economics, not habit — is sound and survives translation: DR's ceiling per paid registration should follow season margin. The implementation is unusable now: DR sells essentially one product type, runs one ad set, has **no measured cost per registration at all** (B2 is open precisely because that number does not exist), and cost caps at DR's spend risk suppressing delivery entirely. Revisit only if B2 ever closes with a real number.

---

### measurement — Channel-level ROAS targets misallocate budget; use one blended north-star

```yaml
topic: measurement
claim: Setting separate ROAS/CPA targets per channel produces bad allocation because channels behave differently and bottom-of-funnel channels take credit for demand created elsewhere; one blended metric (nCAC / MER) should govern instead.
recommended_action: Drop per-channel targets. Track total ad spend against total revenue and new customers, pick a single north-star (they use cost per new customer, plus MER), and move budget between channels to move that one number.
context: Multi-channel DTC account (Meta, TikTok, Google, Amazon, native, CTV) where an agency controlled only part of spend.
business_type: ecommerce
spend_level: "eight-figure business; ~$2.5M → ~$4M revenue/month"
conversion_volume_context: null
research_question_ids: [G2]
published_at: 2026-07-28
source_url: https://perpetualtraffic.com/podcast/episode-801-from-2-5m-to-4m-a-month-ad-spend-barely-changed-heres-why
author: Ricardo Pouwels (Tier 11)
timestamp: null
confidence: medium
evidence_basis: self_reported_case_study
evidence_basis_details: "Named-shape case (premium DTC pet brand, unnamed) over ~12 months with figures quoted for revenue, nCAC direction and MER ($1 in → $9.74 out). Many variables changed simultaneously — channel mix, budget reallocation, creative, agency scope — so the attribution to the metric change specifically is the speakers'."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "there was a certain market target for meta, a certain target for TikTok and a target for Google and which, as you know, never works because the channels behave differently and Google often just steals credit from the other channels… we just started tracking total ad spend, total revenue… And then we had our single Northstar metrics… which was Ncac or the cost per unit for this business."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** G2's practitioner layer was `NO_USEFUL_EVIDENCE_FOUND`; this is the first credible practitioner statement of the blended-measurement position found for this domain. The principle aligns with G2's existing contract — **Meta-attributed conversions are not the business ledger** — and reinforces separating the two numbers. The implementation assumes multiple paid channels to reallocate between; DR has essentially one. For DR the usable residue is narrow but real: judge the season by total spend against total paid registrations from DR's own records, and treat Meta's reported number as a separate, lesser figure.

---

### measurement — Give a test enough time or the result is a false negative

```yaml
topic: measurement
claim: Tests are routinely cut at ~30 days before their true impact is visible, especially when the existing channels are performing and the test budget is a small slice.
recommended_action: Commit sufficient time to a test up front rather than terminating it at a month.
context: Large multi-channel account allocating 5-10% of budget to a new-channel test.
business_type: ecommerce
spend_level: "5-10% of an eight-figure business's budget"
conversion_volume_context: null
research_question_ids: [D3]
published_at: 2026-07-28
source_url: https://perpetualtraffic.com/podcast/episode-801-from-2-5m-to-4m-a-month-ad-spend-barely-changed-heres-why
author: Ricardo Pouwels (Tier 11)
timestamp: null
confidence: medium
evidence_basis: experience_claim
evidence_basis_details: "Stated as agency practice while narrating the case; no comparison of cut-early vs run-long tests shown."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "we can't afford to spend like 5 or 10% of our budget on a new test. But especially for those tests, we have to give it sufficient time. Otherwise we'll just end up cutting the test after 30 days. Never fully seeing the true impact or potential impact of those initiatives."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** Points the same direction as D3's conclusion that premature kills are the larger risk at low volume — but note what it is **not**. D2's ≥7-day review gate was deliberately removed and replaced with an *evidence* condition, and this claim is a **calendar** argument ("30 days"), which is exactly the form D2 rejected. Use it as corroboration that impatience is the common failure; do **not** let it reintroduce a day-count gate.

---

### measurement — Read cross-channel brand lift through branded organic search impressions

```yaml
topic: measurement
claim: Growth in branded organic search impressions over a comparable prior period is a usable read on upper-funnel advertising's effect, independent of whether those searches were clicked.
recommended_action: Compare branded search impressions in Google Search Console period-over-period alongside paid spend changes, and treat the impression delta — not the clicks — as the lift signal.
context: Account where organic search revenue rose alongside Meta spend and the two were being credited separately.
business_type: ecommerce
spend_level: null
conversion_volume_context: "impressions 180,000 → ~305,000 over a 90-day comparison"
research_question_ids: [G2]
published_at: null
source_url: https://perpetualtraffic.com/podcast/episode-764-why-your-organic-traffic-isnt-organic-brand-lift-breakdown-feeder-2-0
author: John Moran (Tier 11)
timestamp: null
confidence: medium
evidence_basis: self_reported_case_study
evidence_basis_details: "Live walkthrough of one account's Search Console comparison with figures read on screen; no control period, no holdout, and the causal link to Meta spend is asserted."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "What I care about in Brand Lift is the impressions over the last three months, compared to the impressions of the previous months, went from 180,000 to a 305. Did they click on brand or did they click on non brand at that point I don't care. All I know is that people who are looking for me went a lot higher"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** The principle answers a real DR problem G2 named: ad-driven demand that lands somewhere Meta cannot see. A parent shown a DR ad plausibly searches "Discipline Rift" or the school's program name rather than clicking. Branded-search impressions are free to check and DR can do it. The caveat is severity of noise: at DR's impression volume the branded-search series will be small and seasonal (registration windows), so this is a **directional** read at best and must never be presented as attribution.

---

### creative_strategy — Diversify visual format, not just message iterations, to avoid the similarity trap

```yaml
topic: creative_testing
claim: Producing many iterations of one visual format leaves an account "similar" in the eyes of current delivery; the useful axis of diversity is distinct visual formats (green screen, listicle, expert explainer, comment response, us-vs-them) carrying the same proven message.
recommended_action: Hold the proven messaging angle fixed and produce deliberately different visual formats against it, rather than producing small iterations of the same format.
context: Andromeda-era creative production; speaker is the CEO of a creative-analytics vendor.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [D1]
published_at: null
source_url: https://perpetualtraffic.com/podcast/episode-769-the-biggest-creative-trends-in-2026-revealed-with-reza-khadjavi
author: Reza Khadjavi (CEO, Motion) — guest
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Framework argued and demonstrated inside the speaker's own product UI. No performance comparison between diversified and non-diversified accounts presented. **Commercial interest: the speaker sells the creative-tagging tool that measures this, and the episode carries a Motion discount code — the recommendation and the vendor's revenue point the same way.**"
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "if it's if all you're doing is green screen, the chances that you're going to fall into like similarity track is high. But… if you got green screen on one and you've got, listicle on another one, an expert explainer on another one, like, you know, that you're being like horizontally broad"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** partial
**reason:** D1 already chose 2-3 creatives per round for **diversity and delivery health** rather than for readability, and this claim describes what "diverse" should mean at the asset level — useful, because DR's provisional rule says how many but not how different. The transfer limit is scale: this advice assumes an account producing dozens of assets where format families can be compared. At 2-3 per round DR cannot measure which format wins; it can only ensure the round is not three versions of one idea. Adopt as a **briefing rule**, not as a measurement plan. Discount the source for vendor incentive.

---

## Contradictions within this author

- **Exclusions.** John Moran states Meta ignores exclusions and repurposes them as seed audiences (ep. 761), while the same team's workaround (ep. 765) is built on encoding new-vs-returning in the *event*, implicitly accepting that audience-level exclusion is unreliable. These are consistent with each other but **inconsistent with Meta's own documentation**, which lists "Custom audiences to exclude" among the hard Audience controls (`knowledge/official-meta/`, Wave 3). Recorded for the validation pass; not resolved here.
- **Calendar vs evidence.** Ep. 801 argues tests need a longer *calendar* window, while the account walkthroughs elsewhere in the corpus judge campaigns on accumulated volume. The author does not reconcile the two.

## Open questions from this author

1. Does the exclusion behaviour he describes reflect Advantage+ Sales specifically, or all campaign types? The transcript does not scope it.
2. His new-customer CAPI event technique presumes a customer database that can label an event as new-vs-returning at fire time. What is the minimum data infrastructure for that, and does anything equivalent exist for a **registration** business where the "customer" is a parent and the participant is a child?
3. Every figure quoted here is ASR-transcribed. Which of them survive checking against the source audio?
4. Tier 11's non-ecommerce clients (Lawn Doctor, AirSculpt, Credit Repair Cloud) are named on their site but did **not** appear in the episodes retrieved. Is there published material on those accounts? That, not the DTC material, is what would actually inform A1.
