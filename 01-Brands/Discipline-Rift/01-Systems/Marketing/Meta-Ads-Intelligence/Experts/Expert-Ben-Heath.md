---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/ben-heath.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/ben-heath.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Ben Heath"
---

# Ben Heath

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Jon-Loomer|Jon Loomer]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Sam-Piliero|Sam Piliero]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/ben-heath.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** ben-heath
**Watchlist priority:** 2
**Topics:** creative_testing · delivery · creative_strategy · campaign_structure · targeting · budgeting
**Sources processed:** 4 (Phase 1–2) · **60/60 YouTube videos fully reviewed** (Phase 3, 2026-08-19)
**Last updated:** 2026-08-19 (Phase 3 complete-corpus review — 290,762 words; 18 claims added, campaign-structure guidance superseded, one live platform bug recorded)
**Panel status:** **VETTED_OPERATOR** — 4 dated sources, live account walkthroughs, and the only operator in the panel who routinely works examples through local and multi-location businesses. Status reflects demonstrated operation, **not** agreement: his evidence is self-reported throughout. Phase 3 revised one part of that: six passages in 60 videos do contain figures from real client accounts — see the Phase 3 section at the end of this file, which is the current statement of what this source supports and supersedes the Sept–Oct 2025 campaign-structure guidance recorded above.
**Independence cluster:** **BEN HEATH** — new, independent. Not Sam Piliero, not Nick Theriot, not Jon Loomer, and **not** the Foxwell ecosystem (`andrew-foxwell.md` / `courtney-fritts.md`). His agreement with any of them counts as a separate voice.

**Ingestion basis.** This file is a **selective** ingestion. The source was discovered and extracted on 2026-08-14 (`knowledge/research-runs/2026-08-14_youtube-apify/`), then **audited before ingestion** (`.../audit/youtube-source-audit.md`). The audit verdict was **`INGEST_SELECTIVELY`**, authorising **two** claims out of nine audited. The seven not carried here were duplicative, already first-party on file, unquantified, or overstated by the original extraction — they are listed in §Not ingested. **The audit, not the extraction report, is the controlling document for everything below.**

## Sources processed

| Canonical URL | Type | Published | Captured | Claims ingested | Questions |
|---|---|---|---|---|---|
| `https://www.youtube.com/watch?v=onFwSud9C2Y` | youtube (15:10, auto-generated EN captions) | 2026-02-10 | 2026-08-14 | **2** (of 9 audited) | D1, D4 |

**Stated context.** Agency operator — Heath Media. Self-reported and **unverified**: *"we're spending more than 15 million dollars a month across hundreds of ad accounts"* (0:14); channel description claims $300M+ lifetime spend, $1.2B+ revenue, 5,000+ businesses, 11+ years. **Follower count and claimed scale rank nothing in this domain.** The on-screen walkthrough is a **leads** campaign optimizing **cost per lead**, run in his own mentorship business — lead-gen context, closer to DR's shape than the ecommerce sources dominating this corpus, though still not local, geo-constrained, or seasonal.

**Retrieval.** Apify MCP (`starvibe/youtube-video-transcript`, run `HpkeM8QdnjhpZ1VsM`, dataset `Z4w7ByR8SfGgf1u8r`). Complete transcript with timestamps preserved at `knowledge/research-runs/2026-08-14_youtube-apify/ben-heath-new-way-test-facebook-ads-post-andromeda-transcript.md`.

---

## Evidence limitations — binding on every claim below

1. **Walkthrough evidence only. No outcome dataset is shown anywhere in the video.** He demonstrates *setup*; he never displays a completed test, a result table, or a before/after. The one figure he gives (*"a 10% 15% difference between the black and white version and the color version"*) is explicitly hypothetical — *"We could see, for example…"*.
2. **Practitioner interpretation is not platform mechanics.** Where he describes what Meta's delivery system does, that is his observation or reading, never a platform fact. Current first-party Meta documentation governs (`knowledge/official-meta/`).
3. **Commercial interests are present and disclosed in-source:** a paid **Hyros** affiliate read (8:35–9:38), and promotion of his own **Skool mentorship product** — which is also the account and the ad creative used in the demo. Neither invalidates the walkthrough; both are recorded.
4. **No account, spend, or conversion volume is disclosed for any observation.** Conversion volume is the variable DR's problem turns on, and this source is silent on it throughout.
5. **Implementation remains budget-dependent for DR.** Nothing here establishes that DR can fund what he does. `output/wave-2b-creative-operating-method.md` D1 Option C (native Creative Testing) remains **DEFERRED**, unchanged by this ingestion.
6. **Auto-generated captions.** ASR defects are preserved and flagged in the transcript file rather than reconstructed.

---

## Claims — YouTube (2026-02-10)

### creative_testing — BEN-01 — Look-alike ads may be treated as one creative, with delivery reportedly concentrating on one of them

```yaml
claim_id: BEN-01
topic: creative_testing
source_support: PARTIALLY_SUPPORTED   # audit §3 BEN-B; he bounds the claim himself
conservative_claim: >-
  In his agency's experience, Meta sometimes — explicitly not always — treats minor variants of a
  single creative (text overlay, background colour, colour vs black-and-white, a swapped video hook
  on an otherwise identical body) as the same ad, with the reported effect that only one of them
  receives meaningful delivery.
recommended_action: >-
  Where several ads in one ad set are minor variants of each other, treat them as one creative for
  planning purposes rather than assuming each will be delivered and read independently.
context: introducing multiple creatives into one ad set post-Andromeda
business_type: agency portfolio (mixed); the on-screen demo is lead-gen
spend_level: "self-reported $15M/month across hundreds of accounts — no per-observation spend disclosed"
conversion_volume_context: null
research_question_ids: [D1, D4]
question_link_origin: retrospective
published_at: 2026-02-10
source_url: https://www.youtube.com/watch?v=onFwSud9C2Y
author: Ben Heath
timestamp: "0:48, 1:56, 7:19, 11:39"
confidence: medium-low
evidence_basis: multi_account_experience
evidence_basis_details: >-
  Reported from agency practice across unnamed accounts. No account, spend, conversion volume,
  measurement, or data of any kind is shown. He explicitly bounds the frequency at 11:39.
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
principle_transfers: yes
implementation_transfers: untested
```

**Modality is part of the claim, not a caveat on it.** He asserts it once (0:48) and hedges everywhere else:

> **[0:48]** "Meta **will** just pick one of those, put that into the auction, the others won't get a fair crack at it."
> **[1:56]** "Meta **could easily** look at those and go, 'Nah, they're all the same thing.'"
> **[11:39]** "with Andromeda, this **doesn't seem to happen all the time**, by the way, cuz I have a lot of people say this, and yes, **we've seen it in some instances, but not all**."

**What he does NOT establish:** that it always happens · any frequency · any account, spend or volume in which it was observed · any measurement · that Meta documents this · that this is what "Andromeda" is.

#### ⚠ Platform validation — `PARTIALLY_SUPPORTED`. The boundary is load-bearing.

First-party Meta, *Demystifying Creative Diversification* (`facebook.com/business/news/demystifying-creative-diversification`, retrieved 2026-08-14):

> *"When multiple ads look or feel alike, these are seen as variations of the same creative, meaning learnings and delivery optimizations are shared at the creative level – not just the individual ad level."*

And Meta draws the same iteration/diversification line he does — *"Creative iteration might produce two ads with identical visuals, but different text CTAs"*, contrasted with diversification producing *"two distinctly different pieces of creative"* differing in *"look, feel, storyline, and message."*

| | Status |
|---|---|
| **The grouping premise** — look-alike ads are seen as variations of one creative, with learnings and delivery optimizations shared at creative level | **SUPPORTED by Meta first-party** |
| **The suppression consequence** — one enters the auction, the rest are starved of budget and get no fair chance | **NOT established by Meta first-party.** Grouping is not suppression. |

**Therefore this must never be recorded, quoted, or reused as "Andromeda suppresses similar ads."** That formulation is not supported and is explicitly rejected by the audit. The Andromeda announcement page itself **does not address similarity or duplication between an advertiser's own ads at all**.

*Retrieval caveat:* the Meta quote above was obtained through WebFetch's summarising layer and reported as verbatim; the page was not read raw. One adjacent phrase in that output (*"effectively limiting their reach potential"*) was the **reader's gloss, not Meta's text**, and is excluded. Re-retrieve raw before this quote carries a decision alone.

**PRINCIPLE:** Creative starvation may be driven by **redundancy** — similarity to another running ad — and not only by ad **count**. Differentiation and batch size are separate levers.
**IMPLEMENTATION:** Make ads within one ad set format- or visually-distinct; route near-identical variants through the native creative testing tool rather than the open ad set.

**applicability_to_DR:** high (principle) · low/unknown (implementation) · **modification_required:** yes
**reason:** The **principle** is directly relevant and does not depend on budget: if look-alike ads are optimized as one creative, then creative **composition** matters independently of creative **count** — a distinction the current batch-size reasoning in Wave 2B does not carry, since it is derived from how thinly delivery spreads across N ads. The **implementation** is untested for DR: the routing half depends on native Creative Testing, which remains DEFERRED on funding grounds.

**relationship_to_existing: `CONTEXTUALIZES`.** The project already holds the **symptom** through Foxwell & Fairbrother — *"If you give Andromeda 10 ads, most likely two or three will get 80% of the total spend, with the rest being starved of budget"* (`multi_account_experience`, weak, FOXWELL ECOSYSTEM). That is **volume**-framed. Ben is **similarity**-framed, from an independent cluster. Different causal stories with different operating consequences: under the volume story the response is *fewer ads*; under the similarity story the response is *more differentiated ads*. **Ingested as independent supporting evidence on a distinct axis — not as a new rule, and not as a replacement for the Foxwell observation.**

> **No hypothesis is changed by this ingestion.** The implication for batch-size reasoning is recorded here for a **future synthesis task** and is deliberately not acted on. `output/wave-2b-creative-operating-method.md` is untouched; the provisional 2–3 creatives per round stands exactly as written.

---

### creative_testing — BEN-04 — He selects the exposure mechanism by the size of the creative difference

```yaml
claim_id: BEN-04
topic: creative_testing
source_support: PARTIALLY_SUPPORTED   # audit §3 BEN-C; stated as a hedged habit, not a rule
conservative_claim: >-
  He reports using natural delivery for coarse comparisons (image vs video, UGC vs produced vs
  founder-led) and reaching for the native creative testing tool for fine ones, on the basis that
  large creative differences are delivered anyway while small ones may not be.
recommended_action: >-
  When choosing between letting ads compete naturally and running a controlled comparison, consider
  how large the difference between the creatives actually is — not only whether a controlled test is
  affordable.
context: choosing between natural in-ad-set delivery and Meta's native creative testing tool
business_type: agency portfolio (mixed); demo is lead-gen
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D4]
question_link_origin: retrospective
published_at: 2026-02-10
source_url: https://www.youtube.com/watch?v=onFwSud9C2Y
author: Ben Heath
timestamp: "9:40, 10:14"
confidence: medium
evidence_basis: multi_account_experience
evidence_basis_details: >-
  Described as agency habit, hedged throughout ("not as important", "we'd often find", "less likely",
  "probably"). No account, spend, volume, or comparative result presented.
evidence_strength: weak
platform_validation_status: NOT_APPLICABLE
principle_transfers: yes
implementation_transfers: no
```

> **[9:40]** "it's **not as important** if you are testing very different ads anyway. So, if for example, you're testing an image ad versus a video ad, Meta's going to treat those different ads. The Andromeda update's not going to get in the way. You'll be able to test. Now, the delivery's **probably** going to overlap."
> **[10:14]** "**what we'd often find** is that the initial round of testing, we're **less likely** to use the creative testing tool because we're finding out the big stuff… But then when we want to get into the more detail, and often the winning happens in working out the detail, then we're going to use the the creative testing tool a lot."

**The distinction is unambiguous in content; the modality is a habit, not a rule.** Recorded as an `OPERATOR_METHOD` heuristic. **The word "criterion" — used in the original extraction — is a formalisation the source does not support and is not carried here.**

**PRINCIPLE:** Match the exposure mechanism to the **magnitude of the creative difference** being tested. Natural delivery can answer coarse questions; it may not be able to answer fine ones.
**IMPLEMENTATION:** Coarse round in the open ad set; fine round via native Creative Testing.

**applicability_to_DR:** high (principle) · **modification_required:** yes
**reason:** The principle is scale-independent and adds a dimension the project's existing framework does not carry. `platform_validation_status: NOT_APPLICABLE` — a method-selection heuristic Meta documentation cannot validate. Its premise partially inherits BEN-01's `PARTIALLY_SUPPORTED` status.

**relationship_to_existing: `NEW` (modest), and strictly additive.** `output/wave-2b-creative-operating-method.md` §D4 already specifies **five conditions** under which controlled exposure is justified for DR — the question matters to a decision, natural delivery cannot answer it, DR can fund an interpretable test slice, the method isolates the question, and the learning cost is worth paying. **All five are affordability and design conditions.** None addresses *which kind of creative question natural delivery can answer in the first place*. Ben's heuristic speaks to that and **conflicts with none of the five**.

> **What this claim does NOT say, and must not be inflated into:**
> - It does **not** show that DR needs controlled testing.
> - It does **not** show that natural delivery is invalid. Natural competition remains DR's current method.
> - It does **not** authorise DR to use controlled exposure. **Fundability is unchanged**, and the five Wave 2B conditions still govern — condition 3 (a fundable, interpretable test slice) is the one that currently fails.
>
> **USEFUL PRINCIPLE ≠ CURRENTLY FUNDABLE DR IMPLEMENTATION.** This is ingested as the former only.

---

## Open mechanics discrepancy — BEN-06 — NOT a claim, NOT adopted

```yaml
claim_id: BEN-06
status: RE_VERIFICATION_TRIGGER
platform_fact: NO
adopted_rule: NO
evidence_type: ON_SCREEN_PLATFORM_OBSERVATION
source_url: https://www.youtube.com/watch?v=onFwSud9C2Y
timestamp: "3:20, 3:50"
observed_at: 2026-02-10
ui_context: "leads campaign, his own account, £25/day, UK interface"
discrepancy:
  practitioner_live_ui_observation: "up to five"
  corroborating_practitioner: >-
    Jon Loomer, "You can create between two and five test ads."
    See knowledge/experts/jon-loomer.md — graded OUTDATED against Meta's current page.
  existing_first_party_record: "2 to 7 copies / compare up to 7 creative variants"
  first_party_source: knowledge/official-meta/creative-testing-ab-testing-and-delivery-diagnostics.md
governing_value: "2-7 — first-party documentation governs platform mechanics. UNCHANGED."
action:
  future_first_party_reverification_required: true
```

**What happened.** At 3:20 Ben is **reading the Ads Manager interface aloud** — *"it says here it here it says, 'Compare up to **five** different versions of your creative in a test that helps ensure delivery to new test ads.'"* — and restates it at 3:50 as *"we can test between two and five different ads."* This is a **reported UI string**, not his methodology. The original extraction misclassified it as practitioner methodology; the audit corrected that.

**Why it is recorded rather than dismissed.** `jon-loomer.md` already records *"You can create between two and five test ads"* and grades it **`OUTDATED`** on the reasoning that the ceiling was raised after his 2026-01-02 update. Ben's video is **2026-02-10** and reports the same **5**. Two independent practitioners now report 5 from what each describes as the live interface, while the help-page text on file says 7. *"Loomer is simply outdated"* is no longer an adequate explanation.

**What is NOT resolved here, deliberately.** Whether the help text and the live UI differ; whether the ceiling varies by campaign type or objective (Ben's is a **leads** campaign; Loomer's context was **Complete Registration**); or whether one retrieval is stale. **This run does not resolve it and does not attempt to.**

**Handling rules:**
- **The project continues to hold 2–7.** First-party documentation governs platform mechanics.
- **Do not change 2–7 to 2–5** anywhere in `official-meta/`.
- **Do not change 2–5 to 2–7** inside Ben's or Loomer's source representation. Both are recorded accurately with provenance.
- Re-verification requires a **rendered browser** — `facebook.com/business/help` returns a title-only JS shell to WebFetch (confirmed again during the audit).
- If the ceiling proves **objective-dependent**, that is materially relevant to DR, because DR's eventual objective would determine it.

---

## Not ingested from this source

Seven of the nine audited claims were **rejected for ingestion**. Recorded so they are not re-proposed:

| ID | Subject | Why not ingested |
|---|---|---|
| **BEN-02** | Native creative testing tool guarantees delivery to test ads and separates their delivery | **DUPLICATES.** Already on file first-party and in more detail — *"delivery provided to new test ads"*, the Highest-volume bid-strategy requirement, the *"no more than 20%"* budget suggestion, and *"A confidence level is not included."* |
| **BEN-03** | Meta's UI showed £25/day × 7 days is insufficient to read cost per lead | **REINFORCES only, and the original framing was wrong.** The UI stated *"Since your duration or budget changed, the recommended key metric was updated in the drop-down"* — an `ON_SCREEN_PLATFORM_OBSERVATION`. The **insufficiency reading is Ben's**, and he labels it as his own: *"without actually saying it, but I can translate for you to some extent."* The conclusion it points at is already the project's position, and **Jon Loomer actually ran the mechanism** at $50/day on a registration-type event (`self_reported_test`, moderate — the strongest in corpus). Loomer outranks this on every axis. |
| **BEN-05** | Two-stage: resolve variants in the tool, promote the winner into the live ad set | Clean procedure, **stated but never demonstrated end-to-end**, and stage 1 requires the tool. Left at MAYBE by the audit; not authorised. |
| **BEN-07** | The "20+ completely different creatives" standard is unrealistic; sustainable cadence wins | `OPINION`, no data. The "standard" is **his own unattributed characterisation** of prevailing advice. Reinforces an existing position without adding evidence. |
| **BEN-08** | Hooks materially change performance; hook-swap testing survives via the tool | Magnitude unquantified (*"massively varying differences"*), no data. |
| **BEN-09** | Meta *"usually"* shifts spend to the winner but *"it doesn't always happen"* — check manually | Minor operational check; contextualises the on-file first-party *"the test does not make any automatic changes based on the results."* Not material. |
| — | *"Andromeda suppresses similar creatives"* as a flat statement | **Explicitly rejected.** Not supported by the source (he self-bounds) and not established by Meta first-party. See BEN-01. |

---

## Contradictions and tensions within this source

| # | Tension | Status |
|---|---|---|
| 1 | **BEN-01** (similar creatives may not be delivered) vs **BEN-07** (*"four very different creatives and perhaps a few variations… That's absolutely fine"*) — same speaker | **Preserved.** He bridges it with the testing tool, not by dropping either. BEN-07 is not ingested; the tension is recorded because it bears on how firmly BEN-01 can be read. |
| 2 | **BEN-06** — his live-UI "up to five" vs the on-file first-party "2 to 7" | **Preserved unresolved.** First-party governs. See above. |
| 3 | **BEN-07** (sustainable small cadence) vs the volume emphasis reaching the project through the Foxwell ecosystem | Genuine practitioner disagreement between independent clusters. Recorded; neither side ingested from this source. |

## Independence note

**BEN HEATH is a new, independent cluster.** He is not part of the Foxwell ecosystem and does not cite it. Where he and Foxwell/Fairbrother point at the same phenomenon (creative starvation), that is **two independent voices on a symptom** — but they attribute it to **different causes** (similarity vs volume), so their agreement is narrower than it first appears and must not be counted as convergence on a mechanism.

---

# Phase 2 ingestion — 2026-08-19

**Run:** `knowledge/research-runs/2026-08-19_phase2-expert-corpus/`.

**The 2026-08-14 audit cap still governs this file.** That audit admitted 2 of 9 claims — the lowest survival rate of any source in this knowledge base. Phase 2 therefore ingests **selectively and with a hard cap of six claims**, prioritizing (a) statements about **local, multi-location and service businesses**, which is the lane he uniquely covers, and (b) statements that **conflict with the rest of the panel**, because a recorded disagreement is more useful than a fifth voice agreeing.

**Not carried from Phase 2 (deliberately):** general beginner setup walkthroughs, pixel-installation instruction, generic scaling encouragement, and any Andromeda mechanism claim. The Andromeda exclusion is deliberate — the earlier audit found his Andromeda creative-grouping premise only partially supported against Meta first-party sources, and nothing retrieved in Phase 2 resolves that.

## Sources processed (Phase 2)

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.youtube.com/watch?v=hHuxr_ancXQ` | youtube (auto captions) | 2025-11-18 | 2026-08-19 | **7** | C1, E3, F1, C4, E1 |
| `https://www.youtube.com/watch?v=crId74rHjuA` | youtube (auto captions) | 2025-10-07 | 2026-08-19 | 2 | C3, D1 |
| `https://www.youtube.com/watch?v=dAJyqo6wnq4` | youtube (auto captions) | 2026-01-06 | 2026-08-19 | 1 | A2, A3 |

**Stated context:** UK agency (Heath Media) serving ecommerce, service businesses and agencies. **He is the only panel member who routinely works examples through local, multi-location businesses** — the Oxford/Bath/Bristol example below is the closest structural analogue to DR's multi-campus situation found anywhere in the corpus.

---

## Claims — Phase 2

### campaign_structure — For a multi-location local business, start with one campaign and bundle the locations

```yaml
topic: campaign_structure
claim: A local business with several locations can run separate campaigns per location, but for most such businesses the recommendation is to start with one campaign — bundling the locations together, or using one location if they must be separate — and only spread out later.
recommended_action: "Start a multi-location local business in a single campaign with locations bundled; separate per-location campaigns only later, and only when the extra work is justified."
context: "Worked through a UK local business with locations in Oxford, Bath and Bristol. CORRECTED 2026-08-19 — this advice is given INSIDE an omnipresent-content awareness campaign: performance goal is maximize reach, there is no conversion event, Advantage campaign budget is off, and each ad set holds one frequency-capped ad. It is not advice about a conversion campaign."
business_type: local_service
spend_level: null
conversion_volume_context: null
research_question_ids: [C1, E3]
question_link_origin: prospective
published_at: 2025-11-18
source_url: https://www.youtube.com/watch?v=hHuxr_ancXQ
author: Ben Heath
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as his standing recommendation with an acknowledgement that his agency has built the separated version for some clients ('We've certainly set things up that way'). No performance comparison between bundled and separated is presented."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "If you are like, well, I'm a local business and I've got one location in Oxford, another location in Bath and another location in Bristol… for most people, I'd recommend starting with the one campaign, with the one location if they have to be separate or bundling them together, and you can always look to spread things out later on."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** It is the only claim in the corpus made explicitly about a multi-location local business, which is DR's structural situation across campuses. It reaches the same answer E3 reached from platform mechanics — locations bundled inside one campaign, separation deferred — from an operator whose agency has built both versions. But see the correction immediately below: **the campaign type is not comparable to DR's, and the reason he gives for bundling is not the reason E3 gives.** It corroborates directionally; it does not prove, and it is not the close structural analogue this file originally called it.

> #### ⚠ CORRECTION — 2026-08-19, after reviewing the full 81-minute video
>
> **This claim was originally recorded as `applicability_to_DR: high`, `implementation_transfers: yes`, and described as *"the closest structural analogue to DR's multi-campus situation found anywhere in the corpus."* That was too generous, and the fields above have been downgraded accordingly.**
>
> Phase 2 ingested this claim from an extracted passage. Reading the whole video shows what the passage lost:
>
> 1. **It is advice about an awareness campaign, not a conversion campaign.** The campaign objective is Awareness (or Engagement), the performance goal is **maximize reach** (5:28), there is **no conversion event anywhere in it**, and Advantage campaign budget is deliberately switched **off**. DR's E3 question is about conversion delivery — learning phase, signal density, allocation between campuses. Those mechanics are not present in what he is describing.
> 2. **His stated reason for bundling is manageability, not performance.** At 16:20: *"this campaign just becomes completely unmanageable. If you start having multiple adsets per location, per campaign becomes really tricky."* E3's reason is about not fragmenting sparse conversion signal. Same conclusion, different mechanism — so this is **not** independent confirmation of E3's reasoning, only of its output.
> 3. **The optimizer is deliberately disabled in this structure.** One ad per ad set, frequency capped at one impression per seven days, expressly so that Meta *cannot* concentrate delivery on the best performer (44:40). Any inference about how delivery allocates across bundled locations does not carry over to a campaign where the optimizer is doing its normal job.
>
> **What survives:** the principle that a multi-location local business should start bundled and earn separation later. **What does not:** treating this as practitioner evidence from a campaign type comparable to DR's. **E3's conclusion is unchanged — it never depended on this claim** — but E3 should record that it still has **no practitioner evidence from a comparable campaign type** in the local lane.
>
> **Revisit threshold: `NOT_DISCLOSED`.** Asked implicitly when he would stop bundling, he says separation *"can absolutely be worth it for certain businesses"* and *"you can always look to spread things out later on"* — without naming a spend level, audience size, performance signal, or any other trigger. **No threshold is inferred from this source.**

---

### campaign_structure — Fourteen single-ad ad sets with a 7-day frequency cap, to stay present without fatiguing

```yaml
topic: campaign_structure
claim: His "omnipresent content" structure runs 14 identical ad sets, each containing exactly one ad, each capped at one impression per seven days, targeting warm custom audiences — producing roughly two different ads per day per person across the week and building familiarity without repeating the same asset.
recommended_action: "Duplicate one fully configured ad set 13 times so all 14 are identical, place a different ad in each, and cap frequency at one impression per 7 days per ad set."
context: Warm-audience content campaign for businesses with a longer relationship-building cycle; audiences built from 180-day website visitors and customer lists.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C1, F1, D1]
question_link_origin: prospective
published_at: 2025-11-18
source_url: https://www.youtube.com/watch?v=hHuxr_ancXQ
author: Ben Heath
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Full build demonstrated in Ads Manager as agency practice. **No performance data, no comparison against a consolidated alternative, and no stated spend floor** — despite the structure requiring budget to be divided 14 ways."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "we've got 14 different adsets that are identical, but we are going to have a different ad in each adset… Each adset has a frequency cap of one impression every seven days… 14 ads means that on average you're going to see two different ads per day across the week."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** **Recorded because it is the panel's sharpest structural disagreement, not because DR should consider it.** Every other practitioner in this knowledge base — Loomer, Faris/Kiel, Foxwell, Theriot, Tomlinson — argues that splitting into many ad sets divides budget, creates auction overlap and starves learning. This does exactly that, deliberately, and justifies it on **exposure management** rather than on optimization. It is unbuildable at DR's spend for the reason C1 and B1 already establish: 14 ad sets sharing a budget that cannot fund one. The **principle** worth keeping is the underlying observation — that repeated exposure to the *same* asset fatigues faster than rotating assets — which supports D1's diversity rationale without requiring his architecture. Note the honest possibility that he is solving a real problem the consolidation camp ignores: nobody else in the corpus addresses deliberate exposure pacing at all.

---

### targeting — Build warm custom audiences at maximum retention windows when the goal is presence

```yaml
topic: targeting
claim: For a presence/relationship campaign, build custom audiences as large as the platform allows — all website visitors at the maximum 180-day retention rather than the 30-day default — plus customer and lead lists, because the aim is the largest warm pool rather than a precise one.
recommended_action: "Set website-visitor custom audiences to the maximum retention window when the purpose is repeated exposure rather than immediate conversion."
context: Setting up audiences for the omnipresent content campaign.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [F1]
question_link_origin: prospective
published_at: 2025-11-18
source_url: https://www.youtube.com/watch?v=hHuxr_ancXQ
author: Ben Heath
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Configuration walked through on screen; the 180-day maximum is a platform limit he points at in the interface, and the recommendation to use it is his practice, unevidenced."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "the audience retention default is 30 but if I hover over here we can see that the maximum time is 180 and for the same reason as I just mentioned previously we want the largest possible custom audience"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** Converges with Sam Piliero's "smaller business, wider windows" point from an independent source: **the smaller the traffic, the longer the window has to be for the pool to contain anyone.** For DR, whose registration traffic arrives in seasonal bursts, a 180-day window is the difference between a warm audience that spans a full season cycle and one that empties between windows. F1 stays deferred — none of this argues for a separate retargeting structure — but if DR ever builds warm audiences for exclusion or reporting purposes, maximum retention is the right default and it is free to set.

---

### campaign_structure — Keep a separate testing campaign because Meta will not fund new ads next to proven winners

```yaml
topic: campaign_structure
claim: A separate testing campaign is necessary because when winning ads exist in a campaign, Meta concentrates spend on them and new ads struggle to receive enough budget to be evaluated; his split is roughly 80% scaling campaign, 20% testing campaign, both targeting the same combined warm and cold audience.
recommended_action: "Run a scaling campaign and a testing campaign against the same audience, splitting budget roughly 80/20, rather than consolidating everything into one campaign."
context: Account architecture for an advertiser starting in 2026; he notes they rarely separate warm from cold.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [C3, D1]
question_link_origin: prospective
published_at: 2025-10-07
source_url: https://www.youtube.com/watch?v=crId74rHjuA
author: Ben Heath
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as an observed pattern ('what we found is…') across agency accounts; no data, no account example, no spend floor given for when the split becomes affordable."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "the reason why we don't just consolidate all into one campaign is because what we found is that if you have winning ads and you try and introduce new ads, Meta will often not spend much money on the new ads… In terms of budget split, we're normally going to be looking at something like an 80/20 split."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** **Directly contradicts Nick Theriot's single-CBO position and sits on the same axis C3 already recorded as a live conflict** — now with a third and fourth voice (Piliero's packs, Foxwell/Fairbrother's Method 1) on the separation side. The underlying observation is not in dispute and is platform-documented in effect: delivery concentrates on proven ads. What is disputed is the remedy. C3's answer for DR stands unchanged — DR has no winner pool to protect and cannot fund two campaigns — and D1's answer stands too, since Meta's own creative-testing mechanism keeps the test in-campaign. **The 80/20 split is worth noting as the second independent "cap testing at ~20% of budget" statement in this corpus** (Piliero's is the other), which is the closest thing to a convergent number the panel produces on testing budget.

---

### creative_testing — Multiply hooks against a small number of full ads

```yaml
topic: creative_testing
claim: Producing two full video ads and ten hook variations each yields twenty ads that function as genuinely different creative, because roughly 90% of viewers never get past the first three seconds — and hooks are far cheaper to produce than full assets (his figure: 20 for the price of about 3 at $500 per asset).
recommended_action: "Commission a small number of full creative assets plus many hook variations from the same creator, rather than commissioning many complete assets."
context: Working with creators/influencers on paid creative production.
business_type: unstated
spend_level: "$500 per video asset used as the production cost example"
conversion_volume_context: null
research_question_ids: [D1]
question_link_origin: prospective
published_at: 2025-10-07
source_url: https://www.youtube.com/watch?v=crId74rHjuA
author: Ben Heath
timestamp: null
confidence: high
evidence_basis: opinion
evidence_basis_details: "The production-economics arithmetic is concrete and checkable; **the '90% or so of people aren't going to make it past those first three seconds' figure is asserted with a hedge and no source**, and it is the load-bearing premise. No performance comparison between hook-variant sets and distinct assets is presented."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "It might take them another hour to do all 10 different hooks. But if you have the two full ads with the 10 different hooks, you have 20 different ads… 90% or so of people aren't going to make it past those first three seconds… So to them, they never saw the rest of it anyway."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **The most budget-appropriate creative-production advice in the corpus** — everyone else's volume guidance presumes production capacity DR does not have, and this one lowers the cost of variety instead of raising the required output. It fits D1's 2-3 per round well: three ads sharing a body but leading with genuinely different hooks (safety, skill progression, schedule/logistics) is achievable from one filming session. **Two cautions:** the 90% figure is unsourced and should not be repeated as fact, and hook variants of one asset are *less* diverse than the concept diversity Foxwell puts first — so this is a way to execute variety cheaply, not a substitute for having more than one idea.

---

### optimization — Choose value optimization when lead values differ materially between services

```yaml
topic: optimization
claim: Where a business sells services of very different value, maximizing number of conversions treats a $200 lead and a $5,000 lead identically; maximizing value of conversions accepts a higher cost per lead in exchange for weighting delivery toward the more valuable ones — but it requires values to be sent back to Meta.
recommended_action: "Use maximize number of conversions for a single-service campaign; use maximize value of conversions where service values differ, and ensure the pixel is sending lead values."
context: Beginner campaign setup, discussing lead-gen performance goals.
business_type: lead_gen
spend_level: null
conversion_volume_context: null
research_question_ids: [A2, A3]
question_link_origin: prospective
published_at: 2026-01-06
source_url: https://www.youtube.com/watch?v=dAJyqo6wnq4
author: Ben Heath
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Explains the tradeoff and its tracking prerequisite; no data on the resulting lead-quality difference is presented."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "if you go with maximize value of conversions, then Meta is going to not just try and get as many conversions as possible, but optimize and weight it in favor of the more valuable conversions. In other words, you might end up paying more in terms of cost per lead, but that's a trade-off you'd be happy to make"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** Relevant to A2/A3 as a **third quality-safeguard mechanism** alongside Loomer's value rules and the Tier 11 event-segmentation approach — all three encode advertiser-held quality information into something the delivery system optimizes toward, rather than into targeting. It does not apply to DR today: DR sells essentially one season product at one price, so there is no value dispersion to weight, and sending values back to Meta runs into the same child-data constraints A3 flagged. It becomes live only if DR's offer set diverges in price — the same trigger Faris and Tomlinson name for campaign separation.

---

# Corrective full-video review — 2026-08-19

**Source re-opened:** `https://www.youtube.com/watch?v=hHuxr_ancXQ` — *"My UPDATED Meta Ad Strategy That's Beating Everyone Right Now (Omnipresent Content)"*, **1:21:02**, published **2025-11-18**, 40,162 views at capture.

**Why it was re-opened.** Phase 2 ingested three claims from this video from extracted passages. It is the only source in the corpus that works an example through a multi-location local business, so the extraction was checked against the whole video. **The check found a scope error** — recorded as the correction on the multi-location claim above — and surfaced four claims the passage-level pass had missed.

**The 2026-08-14 audit cap of six claims on this expert is lifted for this source by operator instruction.** Claim-level auditing still applies: everything below carries its own evidence grade, and nothing was admitted for being interesting.

**Retrieval:** transcript already on disk from Phase 2 (18,488 words, untimestamped). One new Apify call for **timestamps only** — `supreme_coder/youtube-transcript-scraper`, `outputFormat: "srt"`, run `H2scNFFL27z8LRVQY`, dataset `aa5Vd75wYpEkV2k13`, 2,643 segments. **`TRANSCRIPT_COMPLETE`** — last segment starts 80:59 of 81:02. **Timestamps in this section are exact**, unlike the `null` timestamps on the Phase 2 claims above.

**Campaign type — read this before using anything below.** This video does not describe a conversion campaign. It describes a warm-audience **awareness/reach** campaign: objective Awareness or Engagement, performance goal *maximize reach of ads*, no conversion event, no learning phase, Advantage campaign budget off, 14 identical ad sets holding one frequency-capped ad each. Claims are scoped accordingly.

**Fit gate he sets on himself:** the strategy is for businesses where a customer is worth **≥$1,000** and the sale requires demonstrating expertise. He states *"more than half of all businesses don't meet that criteria"* (78:23). **DR does not meet it on a single season registration.** See the last claim in this section.

**Evidence health of this source, stated plainly:** in 81 minutes there is **not one client result** — no CPA, no lead volume, no before/after, no case study. The only outcome figure in the entire video sits inside a paid Hyros segment, describes his own account, and uses two currencies in one sentence (*"we've generated 96,000 but £58,000 of that was not reported by meta"*, 54:33). Everything below is graded `weak` or `none` for that reason.

**Commercial interests, both disclosed in-video:** Hyros affiliate segment (53:40-55:10) and recurring promotion of his own mentorship program (19:40-21:20 and throughout). His own agency is the worked example for why the strategy works.

---

### targeting — Bundle only geographies with similar costs, because the optimizer chases the cheapest one

```yaml
topic: targeting
claim: When several geographies share one ad set, the delivery system allocates toward whichever is cheapest on the optimized metric rather than whichever converts best; he therefore only combines locations whose CPMs are comparable, citing India versus the UK as a pair he would not bundle because reach is far cheaper in India while conversion rates are lower.
recommended_action: "Before combining locations in a single ad set, check that they are comparable in cost on the metric being optimized; heterogeneous cost inside one geo target is an allocation risk."
context: "Setting the locations field of a reach-optimized ad set for his own agency, which has clients in 50+ countries."
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: [E3, C1]
question_link_origin: prospective
published_at: 2025-11-18
source_url: https://www.youtube.com/watch?v=hHuxr_ancXQ
author: Ben Heath
timestamp: "15:27-15:53"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD with a stated mechanism rather than a bare rule. No data shown - but the reasoning is specific and checkable, which is more than most claims in this panel offer."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "if we were to say advertise in India where we do have clients, it's going to be tricky putting that into this same adset because remember this adset is optimized to maximize reach and people are much less expensive to reach in India than they are in the UK. But we know that our conversion rates are likely to be lower there. So if you are adding in multiple countries into your locations, just make sure they are similar in terms of your CPMs."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **The most useful thing in this video for DR, and it is not the multi-location claim.** DR bundles a union of campus serviceability areas into one ad set. This names a specific mechanism by which that bundling could skew delivery toward the cheapest-to-reach campus areas rather than the best-converting ones — and unlike almost everything else in this corpus, **it is checkable in DR's own geography breakdown without running an experiment.** ⚠ **Scope limit, stated by him:** he says this about a **reach-optimized** ad set. The conversion-campaign analogue — the optimizer chasing the cheapest conversions rather than the cheapest impressions — is plausible and is **not** what he claimed, and must not be attributed to him. Treat this as a **diagnostic prompt for DR's own data**, not as a finding.

---

### targeting — Hard controls versus suggestions, and don't revert to the legacy targeting structure

```yaml
topic: targeting
claim: The audience-controls section of the ad set is a hard constraint the system respects, while anything placed in the Advantage+ audience section is a suggestion the system may go outside; he recommends against switching back to original audience options because in his agency's experience the downsides outweigh the control gained.
recommended_action: "Put only business-mandatory constraints (location, minimum age, exclusions, language) in the hard-control section, leave everything else as suggestions, and do not revert to the legacy hard-targeting structure."
context: "Targeting setup walkthrough. He adds no detail targeting at all and leaves age and gender open, arguing the old advice to narrow with interests is obsolete under the suggestion model."
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: [C4, E1]
question_link_origin: prospective
published_at: 2025-11-18
source_url: https://www.youtube.com/watch?v=hHuxr_ancXQ
author: Ben Heath
timestamp: "11:59 / 12:24 / 13:01 / 38:28"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "The hard-versus-suggestion split is a description of platform behaviour shown on screen. The recommendation not to revert is asserted as agency experience - 'we're just seeing worse results' - with no data."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "anything selected within this section is a hard boundary, a hard constraint" · "Anything added in down here in this advantage plus audience section is a suggestion. It's not a hard constraint" · "whilst it might sound like you have more control… the downsides nearly always outweigh the upsides. We're just seeing worse results."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** An independent operator arriving at **exactly DR's current audience posture** — Advantage+ Audience as baseline, hard business controls kept hard (location, adult minimum age, exclusions), no interests as a clean starting point, and no reversion to legacy targeting. Independence matters here because Heath is not in the Foxwell or CTC clusters and does not cite them. ⚠ **The hard-constraint/suggestion split is a platform-mechanics claim and must be checked against `knowledge/official-meta/` before it is relied on.** It matches how Jon Loomer describes the same interface, but two practitioners agreeing is not first-party documentation, and this domain does not let practitioner explanation substitute for it.

---

### campaign_structure — The placements default is right when the performance goal is the real outcome

```yaml
topic: campaign_structure
claim: Advantage+ placements is the correct default for a conversion-based campaign, but wrong for a reach-optimized campaign, because maximizing reach lets the system satisfy the goal with cheap low-value inventory; he therefore switches to manual placements and deselects Audience Network for this campaign type only.
recommended_action: "Keep Advantage+ placements when the performance goal is the outcome you actually want; override it only when the optimized metric is a proxy that cheap inventory satisfies trivially."
context: "Placement section of the reach-optimized omnipresent campaign. He notes having seen misconfigured omnipresent campaigns where most impressions landed on Audience Network."
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: []
question_link_origin: none
published_at: 2025-11-18
source_url: https://www.youtube.com/watch?v=hHuxr_ancXQ
author: Ben Heath
timestamp: "41:03 / 42:06 / 42:22"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD plus an OPERATOR_OBSERVATION about misconfigured accounts. No impression-distribution data is shown."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "if we were running a conversionbased campaign I'd be absolutely fine with you leaving that as advantage plus placements" · "meta can put our ads on the less valuable placement options because that maximizes reach"

**applicability_to_DR:** medium · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** untested
**reason:** `research_question_ids` is empty on purpose — **placements are a settled default in this domain and get no further research budget.** Recorded because it does something the settled default does not: it names **the condition under which the default is wrong**, and gives the mechanism. DR optimizes for a conversion, so the exception does not apply and **nothing changes for DR**. The value is having the exception written down, so that if DR ever runs a reach- or engagement-optimized campaign, the placement default is already known to need review.

---

### campaign_structure — He scopes his own strategy out of businesses like DR

```yaml
topic: campaign_structure
claim: The omnipresent content strategy only works where a customer is worth at least $1,000 to the business over time and the sale requires demonstrating expertise; it is wrong for low-value or impulse purchases, and he estimates more than half of all businesses do not meet the criteria.
recommended_action: "Do not adopt a many-touch presence architecture unless customer value can absorb many paid impressions before the sale."
context: "Explicit fit criteria, stated mid-video and restated as the closing message. The $20 ecommerce product is his counter-example."
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: []
question_link_origin: none
published_at: 2025-11-18
source_url: https://www.youtube.com/watch?v=hHuxr_ancXQ
author: Ben Heath
timestamp: "55:33 / 56:19 / 78:23"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Self-reported client-selection criteria across agency accounts. No data behind the $1,000 figure or the 'more than half' estimate - both are his judgement."
evidence_strength: weak
platform_validation_status: NOT_APPLICABLE
```

> "the business see the best results are ones where customers are worth at least $1,000 to your business once they do become customers. Not necessarily all in one go in that initial transaction, but over time" · "If you're selling a $20 e-commerce product, that's basically an impulse purchase" · "more than half of all businesses don't meet that criteria"

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** **Recorded specifically to stop this architecture being borrowed later because it looked impressive.** DR's season registration does not clear his $1,000 bar. It could only be argued to clear it via multi-season parent lifetime value, which **DR has not established and which is not assumed here.** The transferable principle is real and general: a many-touch presence strategy only pays when the customer's value can absorb many paid impressions before the sale. `$1,000` is `PRACTITIONER_SPECIFIC` and is **not** adopted as a DR threshold. Note the integrity point — an operator publicly bounding his own advice is rare in this panel and makes his other claims easier to trust, not harder.

---

### campaign_structure — Review note on the 14-ad-set claim already on file

The Phase 2 record of the 14-ad-set omnipresent structure is **accurate and is not changed**. The full video adds the reason Phase 2 omitted, and it materially narrows the disagreement:

> "if we lumped all these ads into one adset, the frequency control is set at the adset level, then what Meta would do is they would prioritize the best performing ads and those would get much more distribution as opposed to the others. That's not what we're after." — **44:40**

He is **not** disputing that consolidation improves optimization. He is **declining optimization on purpose**, in a campaign type where there is no conversion to optimize, in order to buy equal exposure across 14 assets. The panel's sharpest structural conflict is therefore **not** "Heath versus everyone else on campaign structure" — it is Heath solving an exposure-pacing problem nobody else in the corpus addresses at all, using a mechanism that would be wrong for the problems they are solving.

Two further details from the full video, neither ingested as a claim:
- **Fallback structure:** if only 10 ads can be produced, run 10 ad sets and tighten the cap to one impression per 5 days to preserve the two-ads-per-day effect (75:50).
- **Creative refresh:** a full rebuild of all 14 ads every **3-6 months**, adjusted by how fast the audience itself turns over — his examples of fast-turnover audiences are wedding photography and newborn products (76:17). **This is relevant to DR's seasonal cycle and is the one piece of his creative-refresh reasoning that is not budget-gated**, but it is an unevidenced rule of thumb and is recorded here rather than ingested.

---

## Contradictions within this author (Phase 2)

- **Consolidation.** He recommends **one campaign** for a multi-location local business, and simultaneously runs **14 ad sets** in his omnipresent structure and a **separate testing campaign** in his general architecture. These are reconcilable (geography bundled, exposure and testing separated) but he never states the reconciliation, and a reader could take either as his position on structure.
- **Audience separation.** "We very rarely separate those out… more likely to keep those combined" (warm and cold in the same campaigns) sits awkwardly beside an entire strategy built on warm-only custom audiences at maximum retention.

## Cross-panel disagreements this ingestion sharpens

| Question | Heath | Opposing voices |
|---|---|---|
| Separate testing campaign? | **Yes**, 80/20 — Meta starves new ads next to winners | Theriot: no, one CBO; Meta's own creative testing stays in-campaign |
| Many ad sets? | **Yes**, 14, for exposure pacing | Loomer, Faris/Kiel, Foxwell, Tomlinson: splitting divides budget and overlaps audiences |
| Multi-location local business? | **One campaign, bundled** — but for *manageability*, inside an awareness campaign | (no opposing voice found — agrees with E3's output, not its reasoning. **Downgraded 2026-08-19**, see the correction on that claim) |
| Bundling unlike geographies? | **No** — comparable costs only, or the optimizer chases the cheapest | (no opposing voice — nobody else in the corpus raises it) |
| Advantage+ placements? | **Yes for conversion campaigns**, no for reach-optimized ones | Agrees with the domain's settled default and adds the exception |
| Legacy targeting controls? | **No** — hard controls only, everything else a suggestion | Loomer describes the same split; agrees |
| Warm-audience retention window? | **Maximum (180d)** | Piliero: flex by business size, wider when small (agrees) |

## Open questions from this author (Phase 2)

1. What spend floor does the 14-ad-set omnipresent structure require? He never states one, and the structure's cost is the whole question for any small advertiser.
2. Is the 7-day-per-ad-set frequency cap doing what he claims at the *account* level, given that all 14 ad sets target the same people? Nobody in the corpus measures cross-ad-set frequency.
3. The "90% don't get past three seconds" figure is load-bearing for his production advice and is unsourced.
4. His local multi-location material is the lane the panel is thinnest in. **Is there more of it?** A targeted pass over his service-business content would be worth more to DR than anything else remaining in his catalogue. **Reinforced 2026-08-19:** now that the one multi-location passage is known to come from an awareness campaign, the panel has **no practitioner evidence at all** on multi-location geography in a *conversion* campaign. That gap is now the sharpest one in this file.
5. **Spend claim inconsistency, unresolved.** He says *"more than $200 million"* on Meta ads twice in-video (00:20, 66:11); his channel description says *"$300M+"*. Neither is verifiable and the two disagree. Recorded, not resolved — it does not invalidate anything above, but it is the kind of number that gets repeated as fact.
6. **Under what conditions would he stop bundling locations?** Asked implicitly, answered with *"can absolutely be worth it for certain businesses"* and *"you can always look to spread things out later on"* — **`NOT_DISCLOSED`**, no threshold inferred. If any of his material states one, it is worth retrieving.

## Validation queue from this author

| Claim | Why it needs first-party checking |
|---|---|
| Hard controls vs. Advantage+ suggestions | Platform-mechanics claim now load-bearing for DR's audience posture. Matches Loomer, but practitioner agreement is not documentation |
| Andromeda / consolidated-campaign framing (67:35, not ingested) | The 2026-08-14 audit already found his Andromeda premise only partially supported; nothing in the full video resolves it. **Dara Denney describes the same systems differently and neither has been checked** |
| Frequency cap behaviour across identical ad sets | His whole structure assumes per-ad-set caps compose into a predictable account-level frequency. Nobody in the corpus measures this |

---

# Phase 3 — complete video corpus review, 2026-08-19

**Scope:** all **60** downloaded `ben-heath` YouTube videos, **290,762 words**, read start to finish in chronological order via `data/raw/phase3/serve.py`. No passage sampling. Publication range **2025-07-22 → 2026-08-18**; 58 of 60 fall inside the `CURRENT` window, 2 are `HISTORICAL` (2025-07-22, 2025-07-29).

## Coverage reconciliation

| Status | Count |
|---|---|
| `FULLY_REVIEWED_USEFUL` | 44 |
| `FULLY_REVIEWED_DUPLICATIVE` | 6 |
| `FULLY_REVIEWED_LOW_VALUE` | 8 |
| `FULLY_REVIEWED_NOT_RELEVANT` | 2 |
| `TRANSCRIPT_INCOMPLETE` / `TRANSCRIPT_UNAVAILABLE` | 0 |
| **Total** | **60** |

`DUPLICATIVE`: `kuSq-pmNfnM`, `crId74rHjuA`, `dAJyqo6wnq4`, `JLlcwojiVtw`, `q7W4hgLb2mE`, `p8pthMjKKXk` — long omnibus tutorials whose every substantive position appears, better dated and better argued, in a single-topic video elsewhere in the corpus.
`LOW_VALUE`: `NY-_GV7TNes` (65-second recap), `M2VReAjHiN8`, `_MIWfyD91yc`, `TpZrPY6jTE8` (sponsored AI-tool demos — Poppy, Arcads, Higgsfield/Arcads MCP), `487xP7cEP6I`, `1Oq_yxUr254` (ad-reaction videos with no transferable structure), `V9puDlCF-KM` (disabled-ad-account recovery — operationally real, no DR decision attached), `gmNefChzGBI` (platform tier list; its numbers are unsourced).
`NOT_RELEVANT`: `ZB0qXMU2kxY` (Business Manager setup), `qIlJjn_y3fc` (Hostinger/Hermes hosting sponsor).

## Corpus caveat — commercial framing, and a corpus that is a sales funnel

Every video in this corpus is an ad for something Heath sells, and **what he sells changed three times inside the review window.** The mentorship program (through ~Feb 2026) → the Ben Heath Inner Circle, 10 live calls/month at "less than $60 per session" (from ~Mar 2026) → **Ben Heath Meta Ads Academy**, a Skool community with a 112-video course at "$49 per month introductory," launched days before `G1og9QXdkZQ` (2026-08-03). Two of his own social-proof numbers — *"82% of people that join my mentorship program see a notable improvement in ROAS within 30 days"* and the recurring Tara *"0.7 to 8.03"* / Zoe *"35,000 raffle tickets"* wins — are read verbatim from a script in at least eight videos and are **`self_reported`, unaudited, and not usable as evidence of anything.**

Sponsor reads are dense (Hyros in ~20 videos, HubSpot ~7, Particl, Motion, Holo, ClickMagick, Arcads, Higgsfield, Hostinger). **Every statistic delivered inside a sponsor segment is vendor marketing copy and is excluded from every claim below.** That specifically excludes the "Meta tracking is consistently off by 20–30%, as much as 50%+ for long-term sales" figure (Hyros read, `p8pthMjKKXk` / `du6rDgRf06g`) and the £96,000/£58,000 Hyros dashboard example repeated in ~20 videos.

**Scale claims drift and must not be quoted as precise.** Across 60 videos he variously states $150M / $200M / $300M+ lifetime spend, 1,000 / 1,200 / 1,400+ ad accounts in the business manager, 3,000 / 5,000+ clients, $700M / $1.2B generated, and "$15 million a month" vs "$97 million last year" vs "just shy of $100 million in 2025" current spend. The direction is consistent — a genuinely large agency — but **no single figure survives as a citable number.** Recorded as `PRACTITIONER_SPECIFIC`, order-of-magnitude only.

## ⚠ Corpus-integrity defect — one factual error in `XtoJVbu4Bys`

`XtoJVbu4Bys` (2026-07-02, "5 Levels Of Meta Ads Strategy") analyses **Huel** as its level-5 example for roughly four minutes, then concludes: *"So, **Shein** sits firmly at level five with so many bases covered."* Shein is never analysed anywhere in the video. This is a scripting/read error, not an ASR artefact (the surrounding sentence is grammatical). **Nothing from that video may be attributed to Shein.** Flagged because Phase 2-style passage extraction over that segment would have produced a Shein claim built on Huel's teardown.

## Corpus-level findings

### F-1 · Campaign structure reversed inside the window — the two-campaign default was retired

This is the most consequential change in the corpus and Phase 2 captured only its first half.

| Date | Video | Stated default |
|---|---|---|
| 2025-09-09 | `kuSq-pmNfnM` | Consolidate; "many ad accounts producing great results operating with literally one Advantage+ campaign" |
| 2025-09-23 | `IRyR9PzSnM8` | **Two campaigns for "the vast vast majority of businesses"** — a scaling campaign and a testing campaign, one ad set each, same targeting; 80/20 budget split |
| 2025-10-07 | `crId74rHjuA` | Same two-campaign structure, "if I started again" |
| 2026-01-13 | `v_u9qcbW5hY` | Separate testing campaign is now **option 2 of 4**, and is explicitly **gated**: *"If you're generating less than 50 conversions per week, don't do this"* |
| 2026-02-17 | `13s-G9Uj51A` | **Default is one campaign, one ad set, 20+ ads.** Two campaigns demoted to an exception for accounts that cannot get spend onto new creative |
| 2026-02-20 | `XLagiyzYYpE` | Small budgets: "fewer campaigns, often just one campaign, one ad set" |
| 2026-08-12 | `du6rDgRf06g` | $100/month: "one campaign, one ad set, one offer." Multiple campaigns and separate testing campaigns are explicitly a **$100,000/month** behaviour |

**The reversal is not presented as a reversal.** He never says the September recommendation was wrong; the default simply changes underneath the viewer. Anything ingested from the Sept–Oct 2025 window that carries "scaling campaign + testing campaign" as Heath's structural recommendation is **superseded** — and DR, at low conversion volume, falls on the one-campaign side of his own gate.

### F-2 · The 50-conversions-per-week gate is the single most load-bearing number in the corpus

It appears independently in four contexts and governs a different decision in each:

- **Learning-limited exit** (`dlVx7HgKL_I`, 2026-03-31) — Meta's stated requirement is 50 results/week of *the event you optimise for*; he adds from experience that ad sets do exit at 20–40 and he has never seen one above 50 stay limited.
- **Whether a separate testing campaign is allowed** (`v_u9qcbW5hY`, 2026-01-13) — below 50/week, don't split.
- **Whether to optimise for value instead of volume** (`6TRy9eUAPVg`, 2026-08-18) — "if you're only generating a handful of conversions a week, then don't do it."
- **Which funnel step to optimise for** (`6TRy9eUAPVg`) — pick *the lowest event in the funnel you have enough volume for*, with 20–25/week floated as the working floor per step.

**This is the number that decides most of DR's structural questions**, and it is Meta's published threshold restated by an operator, not his own finding.

### F-3 · Andromeda: he dates it, dissents on the panic, and dissents on the campaign structures being sold around it

`a6-l6BD3dDg` (2026-11-11) reads Meta's own engineering post on screen and states the publication date: **2 December 2024**, with rollout taking ~a year, which is why it became a topic of conversation in late 2025. **This is a citable date from a first-party Meta document read on camera — it is the cleanest resolution available in the panel to the Denney (Dec 2024) vs Piliero (mid-2025) disagreement, and it says both were describing different things: Denney the publication, Piliero the rollout.** It should be checked directly against `knowledge/official-meta/` rather than adopted from him.

He then makes two dissents worth keeping. First, against the drop-off narrative: results falling in late 2025 could equally be Q4 seasonality or CPM inflation, and "not all advertisers' results have gotten worse." Second, and pointedly: *"it's quite clear whenever I see these crazy campaign structures being talked about, especially in relation to Andromeda, that these people don't really run many live ad campaigns."* **A named operator with a large book calling the post-Andromeda restructure advice impractical is a real minority position in this panel and should be preserved as one.**

### F-4 · He runs directly against the corpus consensus on how much creative volume is realistic

Every other expert in the panel and Heath himself push "20+ ads per ad set, all different." But in `onFwSud9C2Y` (2026-02-10) he breaks ranks with his own advice:

> *"To produce 20 pieces of ad creative that are totally different from one another and run all those in an ad set together, I think is unrealistic for a ton of businesses. And actually I'm starting to see this put people off... It's like if I have to make 20, I'm not going to bother making one."*
>
> *"Better to go with a creative production schedule that you can stick to as opposed to the one that's perfect."*

**For DR — small team, no in-house video capacity — this is the more usable version of the recommendation, and it comes from the same source as the 20+ number.** Both should travel together; quoting only the 20+ figure misrepresents him.

### F-5 · A live, dated platform bug that changes how DR should scale right now

`G1og9QXdkZQ` (2026-08-03), recorded from a hotel room specifically to get it out fast: across **multiple** client ad accounts, increasing the budget on an existing well-performing campaign or ad set is causing results to **go to zero or drop 90%+** — not the normal ROAS-degrades-as-you-scale relationship, a total collapse. His interim workaround is to **duplicate the campaign/ad set, start the duplicate at the higher budget, and turn the original off** — while stating twice that this is *not* what he would normally do and that horizontal duplication is data fragmentation.

**Unconfirmed by Meta, self-reported, and by his own account it has not hit every account.** But it is 16 days old at review, it comes from an operator with 1,400+ accounts to observe, and it directly contradicts the scaling method he taught 11 weeks earlier in `FyWyHJh_6Ng`. **This is the highest-priority item in the corpus to re-check before DR next raises a budget.**

### F-6 · A resolution — the closest comparable-campaign-type evidence for DR's multi-campus question

The ⚠ CORRECTION above records that the multi-location bundling claim came from an **awareness** campaign and that E3 therefore had *"no practitioner evidence from a comparable campaign type in the local lane."* **`13s-G9Uj51A` (2026-02-17) partially closes that gap, and points the other way.** Describing the consolidated conversion-campaign default, he names exactly one surviving exception:

> *"There is an exception and that's location-based targeting. We will often test different locations... if it's a locally based business that has multiple locations. So, if it's a gym franchise, for example, you might want to test, right, we're going to advertise in this city versus this city versus this city for that individual unit... and we're going to separate out performance."*
>
> *"It's not a coincidence that... the location targeting falls within the control section... those are hard boundaries."*

So in a **conversion** campaign he keeps geography separable while consolidating everything else — because location is the only targeting input Meta treats as a hard constraint rather than a suggestion. That is the opposite structural instinct from the awareness-campaign advice, and the mechanism he gives (hard boundary → clean read) is a *measurement* argument, not the signal-density argument E3 runs on. **The two are not in contradiction — different campaign types — but E3 now has a comparable-type data point, and it cuts toward per-metro separability being legitimate where the read matters.** It still does not answer at what volume separation is affordable; that is governed by F-2.

## Claims

```yaml
- id: BH-P3-01
  claim: >
    His stated default campaign structure for the majority of businesses is now one campaign,
    one ad set, and 20+ ads, having previously recommended two campaigns (scaling + testing).
    Separate testing campaigns are gated on generating 50+ of the optimised conversion event
    per week; below that, new creative goes into the same ad set.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=13s-G9Uj51A
  corroborating_sources: [v_u9qcbW5hY, XLagiyzYYpE, du6rDgRf06g]
  published_at: 2026-02-17
  captured_at: 2026-08-19
  evidence_basis: MULTI_ACCOUNT_EXPERIENCE
  evidence_basis_details: >
    Agency-wide default across a stated 1,200–1,400 ad accounts. No account, spend figure, or
    before/after result is attached to the structure change itself.
  evidence_strength: MODERATE
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [E1, E3, B2]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: no
  principle_transfers: yes
  implementation_transfers: yes
  reason: >
    DR is on the low-volume side of his own gate, so the recommendation resolves cleanly:
    one campaign, one ad set, no separate testing campaign. Supersedes the Sept–Oct 2025
    two-campaign guidance in this file's earlier sections.

- id: BH-P3-02
  claim: >
    In a conversion campaign he keeps location separable across ad sets while consolidating
    every other targeting variable, because location sits in the ad set "controls" section as a
    hard boundary whereas interests, age, gender and custom audiences are suggestions Meta may
    ignore — making location the only input that yields a clean per-segment read.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=13s-G9Uj51A
  published_at: 2026-02-17
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Stated as current agency practice with a gym-franchise multi-location example. No campaign,
    spend, or result data. The controls-vs-suggestions distinction is demonstrated on screen in
    Ads Manager.
  evidence_strength: MODERATE
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [E3, C1]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    First evidence in the local lane from a campaign type comparable to DR's — see F-6. The
    mechanism (hard boundary → attributable read) transfers; whether DR can afford the volume
    cost of splitting metros is decided by BH-P3-03, not by this claim.

- id: BH-P3-03
  claim: >
    Meta's requirement to exit the learning phase is 50 results per week of the specific event
    the ad set optimises for; in his experience ad sets sometimes exit at 20–40 and he has never
    seen one above 50 remain learning-limited. Where 50/week of the true end event is
    permanently unrealistic, he recommends optimising for a higher-funnel event that does occur
    often enough — explicitly as a test-and-compare, not a rule.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=dlVx7HgKL_I
  corroborating_sources: [6TRy9eUAPVg, v_u9qcbW5hY]
  published_at: 2026-03-31
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_OBSERVATION
  evidence_basis_details: >
    The 50 figure is Meta's published threshold restated. The 20–40 observation and the
    "never seen above 50 stay limited" assertion are his own, across the agency book, with no
    counts given.
  evidence_strength: MODERATE
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [A2, A3, B2, E3]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: no
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    This is the arithmetic that decides A2/A3 and E3 for DR. If paid registrations per metro
    per week cannot approach the threshold, the choice is between a higher-funnel optimisation
    event and accepting a permanently learning-limited ad set — and he is explicit that a
    learning-limited ad set can still be profitable, which is the part most likely to be lost.

- id: BH-P3-04
  claim: >
    He explicitly rejects the advice that new ad accounts must "warm up the pixel" with traffic
    or engagement campaigns before running conversion campaigns, calling it "absolute nonsense."
    New accounts should run leads or sales from day one and optimise for the real end event.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=vaBxYgZ7MAU
  published_at: 2026-05-27
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Asserted forcefully with a mechanism (Meta's optimisation is literal; link clicks from bots
    still count as link clicks). No test, no account comparison, no data.
  evidence_strength: WEAK
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [A2, D1]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: no
  principle_transfers: yes
  implementation_transfers: yes
  reason: >
    Cheap to act on, expensive to get wrong in the other direction, and it closes a piece of
    folklore DR is likely to encounter. Weak evidence, but the mechanism is checkable against
    Meta documentation and the cost of following it is zero.

- id: BH-P3-05
  claim: >
    Diagnostic framework mapping observed campaign symptoms to the layer at fault —
    no conversions at all → offer problem; some conversions with low hook rate and low CTR →
    creative problem; some conversions with high hook rate and high CTR → landing page /
    post-click problem; many conversions but unprofitable → business-model problem (pricing,
    upsell, LTV); many conversions and profitable → scale.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=vaBxYgZ7MAU
  published_at: 2026-05-27
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Presented as the framework he applies on client and mentorship calls. No validation data.
    He states the creative branch is the most common outcome he encounters.
  evidence_strength: MODERATE
  context_completeness: COMPLETE
  platform_validation_status: NOT_APPLICABLE
  research_question_ids: [F1, C4, G1]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: no
  principle_transfers: yes
  implementation_transfers: yes
  reason: >
    The most directly usable thing in the corpus. It is a triage routine, not a performance
    claim, so it costs nothing to adopt and it stops DR from attributing an offer failure to
    creative or a landing-page failure to targeting.

- id: BH-P3-06
  claim: >
    Testing should proceed in a fixed priority order — offer first, then angle (one angle per
    ad, never bundled), then creative style, then hook, and only then minor variables such as
    primary text, headline, background colour or CTA button. Most tests fail, and testing
    temporarily worsens account-level results by design.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=8dJxOaZrK1M
  corroborating_sources: [inJWYXen3Xc]
  published_at: 2026-03-03
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Worked through on his own agency offer with five named angles (results, scale, time saving,
    anxiety alleviation, status) and the stated finding that results won. No numbers attached
    to that finding.
  evidence_strength: MODERATE
  context_completeness: PARTIAL
  platform_validation_status: NOT_APPLICABLE
  research_question_ids: [C1, C2, C4]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    The ordering matters more than the tactics: it tells DR not to spend its small testing
    budget on headline variants before the offer and angle are settled. DR's own angle set
    (skill development · childcare logistics · social belonging · parental anxiety about
    falling behind · status) has to be written and tested, not inherited.

- id: BH-P3-07
  claim: >
    A high-leverage way to build a new ad is to compute hook rate (3-second video plays ÷
    impressions) as a custom column, then find an ad with a low hook rate but a good cost per
    result and combine its body with the hook from an ad with a high hook rate but a poor cost
    per result.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=bAo6SICFyIE
  published_at: 2026-03-10
  captured_at: 2026-08-19
  evidence_basis: REAL_ACCOUNT_EXAMPLE
  evidence_basis_details: >
    Demonstrated live in his own lead-generation account for the agency's done-for-you service,
    optimising for website schedules. Visible figures: best hook rate ~27% at ~£30 per website
    schedule from 64 results; the identified candidate at 15.55% hook rate but £11.02 per
    website schedule from 33 results; worst hook rates 7–9% with negligible spend.
    PRACTITIONER_SPECIFIC — a UK marketing-agency lead funnel, not a youth-sports registration.
  evidence_strength: MODERATE
  context_completeness: COMPLETE
  platform_validation_status: NOT_APPLICABLE
  research_question_ids: [C2, C4]
  question_link_origin: retrospective
  applicability_to_DR: medium
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    The diagnostic split — hook performance and body performance are separable and separately
    measurable — is sound and cheap. The implementation needs enough video ads with enough
    volume to populate the two quadrants, which DR does not yet have.

- id: BH-P3-08
  claim: >
    Meta changed the definition of click-through attribution: social and media clicks (likes,
    reactions, comments, shares, "see more" expansions, video plays) no longer trigger a
    click-through attributed conversion — only a click on the ad's destination link does. Those
    interactions move to a new category, engage-through attribution, which counts a video played
    for 5+ seconds. Reported conversions will fall for many advertisers as a result.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=4mYjto4VeIk
  published_at: 2026-04-07
  captured_at: 2026-08-19
  evidence_basis: REAL_ACCOUNT_EXAMPLE
  evidence_basis_details: >
    Shows the new attribution UI in one of his accounts, and a link-clicks-vs-all-clicks column
    comparison across four of his own campaigns — the two video-heavy campaigns run at close to
    3× more all-clicks than link clicks (415 link clicks vs 1,179 all clicks on one), the two
    image-heavy campaigns much closer. PRACTITIONER_SPECIFIC.
  evidence_strength: MODERATE
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [D1, D2, D3]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: no
  principle_transfers: yes
  implementation_transfers: no
  reason: >
    A platform-mechanics assertion, therefore UNVALIDATED until checked against first-party
    Meta documentation — but if correct it means any DR before/after comparison spanning
    April 2026 is measuring two different things. The 3× ratio on video-heavy campaigns
    indicates the size of the artefact, not a DR estimate.

- id: BH-P3-09
  claim: >
    Meta will target warm audiences inside an ad set explicitly configured for cold audiences,
    and vice versa, because custom audiences sit in the suggestion layer rather than the
    controls layer — so a separate retargeting campaign or ad set is usually pointless and
    fragments conversion data.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=YZ_zNzXHOio
  corroborating_sources: [13s-G9Uj51A, BO-CLO9lhr8, JLlcwojiVtw]
  published_at: 2026-03-17
  captured_at: 2026-08-19
  evidence_basis: REAL_ACCOUNT_EXAMPLE
  evidence_basis_details: >
    A client sales campaign shown on screen, configured open/cold — whole US, open age and
    gender, no custom audiences, one interest as a suggestion. Audience-segment breakdown:
    ~$80,000 spent, ~$47–48k of it on new audience, so ~40% went to engaged audience plus
    existing customers; of 942 purchases generated, more than half came from those warm
    segments at a visibly lower cost per purchase. PRACTITIONER_SPECIFIC — client account,
    industry NOT_DISCLOSED.
  evidence_strength: STRONG
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [C1, E1, E3]
  question_link_origin: retrospective
  applicability_to_DR: medium
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    The strongest single piece of account evidence in the corpus — a real spend figure, a real
    conversion count, and a real segment split, all visible on screen. But it is an account
    with a large existing customer base; DR's warm audiences are small, so the ratio does not
    transfer even though the mechanism does. He also states the correct instrumentation
    (define engaged audience and existing customers in advertising settings, then read the
    audience-segments breakdown), which DR should do regardless.

- id: BH-P3-10
  claim: >
    For local businesses, the location-targeting option "reach more people likely to respond to
    your ads" — which extends delivery to people merely interested in the selected city or
    region rather than located in it — should be deselected, accepting Meta's warning of a
    ~6.7% higher cost per result, because leads from outside the service area cannot be served.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=dAJyqo6wnq4
  published_at: 2026-01-06
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Demonstrated in Ads Manager with Meta's own on-screen warning quoted. The 6.7% figure is
    Meta's estimate displayed in the interface for that configuration, not his measurement, and
    is configuration-specific.
  evidence_strength: MODERATE
  context_completeness: COMPLETE
  platform_validation_status: UNVALIDATED
  research_question_ids: [C1, E3, G1]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: no
  principle_transfers: yes
  implementation_transfers: yes
  reason: >
    Directly operational for DR. Orlando has substantial visitor and relocation-interest
    traffic; a registration for an after-school programme cannot be fulfilled for someone
    merely interested in Orlando. This is a one-checkbox geo-accuracy improvement and it
    passes the DR recommendation gate on geo accuracy alone.

- id: BH-P3-11
  claim: >
    Where a lead-generation business cannot feed real revenue back to Meta, differing lead
    values can be estimated and passed as conversion values — by routing different services or
    different qualification answers to different thank-you pages firing different-valued
    conversion events — so that "maximize value of conversions" can be used instead of
    "maximize number of conversions." Separately, an instant form's conditional logic can close
    the form for unqualified respondents so they never register as a lead at all.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=FiZ9IEQteMU
  corroborating_sources: [6TRy9eUAPVg]
  published_at: 2026-02-03
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Worked through with a hypothetical roofing business — full replacement at $20,000 closing
    1 in 5 → $4,000 per lead; repairs at $2,000 closing 1 in 2 → $1,000 per lead. The numbers
    are illustrative, not measured. The conditional-logic setup is demonstrated live.
  evidence_strength: MODERATE
  context_completeness: COMPLETE
  platform_validation_status: UNVALIDATED
  research_question_ids: [A2, A3, D2, D4]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    DR's registrations are not equal — season length, sport, multi-child households and
    re-enrolment probability differ — and this is a concrete mechanism for telling Meta so
    without waiting for a CRM integration. It also interacts with F-2: value optimisation
    needs volume, and he says so explicitly.

- id: BH-P3-12
  claim: >
    Value rules should be built only on information Meta cannot already observe — repeat
    purchase rate, refund rate, lead-to-customer conversion rate, lifetime value beyond the
    attribution window. Building a value rule on something Meta can already see (which
    demographic buys most) is a mistake, because Meta is already optimising toward it.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=6TRy9eUAPVg
  corroborating_sources: [bv8AsY0xkIk, 1Or1B4L_bdY, JLlcwojiVtw, du6rDgRf06g]
  published_at: 2026-08-18
  captured_at: 2026-08-19
  evidence_basis: MULTI_ACCOUNT_EXPERIENCE
  evidence_basis_details: >
    The distinction is stated as the common mistake he sees. The recurring supporting example
    is a jewellery client he has consulted for over several years, where men bought women's
    jewellery as gifts and did not repeat, so bids were raised for women — a real client
    situation, but the uplift percentages he types on screen (50%, 60%, 70%, 80%) are
    demonstration values, and he says explicitly the correct figure must come from the
    advertiser's own data.
  evidence_strength: MODERATE
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [C1, A3, D4]
  question_link_origin: retrospective
  applicability_to_DR: medium
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: no
  reason: >
    The invisible-information test is the useful part and it generalises. DR cannot implement
    this yet — it has no measured differential in re-enrolment or lifetime value by segment to
    put in the field — but knowing the test exists tells DR what to start measuring. Note that
    Meta itself warns on the creation screen that cost per result may rise.

- id: BH-P3-13
  claim: >
    Meta's creative testing tool, found at the ad level, splits the audience into non-
    overlapping segments per test ad and forces delivery to each, which is how ad variants
    that Andromeda would otherwise treat as near-duplicates (different hooks on the same body,
    different text overlays on the same image) can still be tested. Delivery returns to normal
    when the test ends. The limit was raised from five test ads to seven.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=onFwSud9C2Y
  corroborating_sources: [v_u9qcbW5hY, 8dJxOaZrK1M, 6TRy9eUAPVg]
  published_at: 2026-02-10
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Demonstrated live four separate times across the corpus. He repeatedly flags the same trap:
    the default comparison metric is cost per post engagement and must be changed to the real
    conversion metric, and Meta will warn that the budget or duration is too small to reach
    confidence on it.
  evidence_strength: MODERATE
  context_completeness: COMPLETE
  platform_validation_status: UNVALIDATED
  research_question_ids: [C2, C4, E1]
  question_link_origin: retrospective
  applicability_to_DR: medium
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    Solves a real problem for a one-ad-set account, which is DR's structure. The constraint is
    F-2 again: a clean read on cost per registration needs volume DR may not have, and his own
    on-screen warning shows Meta saying so at £25/day over 7 days.

- id: BH-P3-14
  claim: >
    Meta has begun rolling out embedded calendar bookings inside instant forms (Calendly and
    GoHighLevel first, HubSpot expected, global availability expected October), so a prospect
    can book a time slot without leaving Facebook or Instagram, with contact details carried
    over automatically and retained even if the booking is not completed.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=HBM3ShZ2dLE
  published_at: 2026-07-23
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_OBSERVATION
  evidence_basis_details: >
    Read from Meta's own support documentation on screen; he confirms the feature is present in
    some of his ad accounts and not others. No performance data — his statement that it will
    reduce his own cost per lead is a prediction, and he labels it as one.
  evidence_strength: WEAK
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [A1, A2, D2]
  question_link_origin: retrospective
  applicability_to_DR: medium
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    Potentially relevant if DR ever routes parents to a trial session, campus visit or call
    rather than straight to registration checkout. Recorded as a platform capability to verify,
    not as a recommendation — its value to DR depends entirely on whether an appointment step
    belongs in DR's funnel, which A1 has not settled.

- id: BH-P3-15
  claim: >
    Meta's own reported figures for partnership ads (ads running from both the brand's and a
    creator's account): 13% higher click-through rate and 71% higher brand lift versus
    non-partnership ads. Meta's CMO states on camera that Meta's priority is moving advertiser
    spend toward creators because the ROI is better, and that the selection criterion should be
    authenticity and audience match rather than reach.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=wwdvrZBjock
  corroborating_sources: [gbcQq19jbjs]
  published_at: 2026-07-20
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_OBSERVATION
  evidence_basis_details: >
    The 13% / 71% figures are Meta marketing statistics relayed by Heath, not measured by him.
    The CMO statements are first-hand and on camera in a filmed interview with Alex Schultz —
    including "advertisers are getting better ROI when they're doing authentic stuff with
    creators and then boosting them as ads," and "focus on authentic match that you can boost
    with ads as a business, not focus on reach first."
  evidence_strength: MODERATE
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [C1, C3, S1]
  question_link_origin: retrospective
  applicability_to_DR: medium
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    A platform vendor stating its own product is effective is an interested party, and the
    numbers are Meta's marketing. What raises this above the corpus baseline is that it is a
    named executive on camera stating a strategic priority — which is a reliable signal about
    where the platform will invest, whatever it says about ROI. For DR the transferable form
    is local: an Orlando parent-audience or youth-sports creator, not a national name.

- id: BH-P3-16
  claim: >
    Since roughly 2026-08-01, increasing the budget on an existing well-performing Meta campaign
    or ad set has, in a material number of accounts, caused results to fall to zero or drop by
    90%+ — distinct from the normal degradation of return as spend rises. His interim workaround
    is to duplicate the campaign or ad set, launch the duplicate at the higher budget, and turn
    the original off.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=G1og9QXdkZQ
  published_at: 2026-08-03
  captured_at: 2026-08-19
  evidence_basis: MULTI_ACCOUNT_EXPERIENCE
  evidence_basis_details: >
    Observed across an unspecified number of client accounts out of a stated 1,400+; he says
    explicitly it has not affected every account and that some scaled normally. No counts, no
    account identifiers, no before/after figures. Unacknowledged by Meta. He states he would
    normally never scale this way and that duplication causes its own problems, including
    previous best-performing ads sometimes receiving no spend in the duplicate.
  evidence_strength: WEAK
  context_completeness: PARTIAL
  platform_validation_status: UNVALIDATED
  research_question_ids: [B2, B3, E1]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: yes
  principle_transfers: no
  implementation_transfers: no
  reason: >
    Weak evidence and explicitly temporary — but it is 16 days old, it contradicts his own
    standing scaling method, and the failure mode it describes would be catastrophic and
    misread as a creative or seasonality problem. Recorded as a live condition to re-verify
    before DR's next budget increase, NOT as a method. If the bug is resolved, this claim
    expires and BH-P3-17 governs.

- id: BH-P3-17
  claim: >
    Scaling should be stepped, with the percentage increment shrinking as spend rises — he is
    comfortable roughly doubling from $50/day to $100/day, then ~50% to $150, tapering to ~20%
    increments by $800–1,000/day — holding each step 5–10 days depending on conversion volume,
    on the existing campaign rather than a duplicate. Stepping also reveals the account's
    scaling ceiling, which a single large jump destroys the ability to learn.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=FyWyHJh_6Ng
  corroborating_sources: [du6rDgRf06g]
  published_at: 2026-05-19
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Presented as two alternative methods chosen by advertiser temperament — automated rules at
    ~3% daily with cost-per-result conditions, or manual stepped increases. The worked ceiling
    example (6.0 ROAS at $50/day degrading through 5.2, 4.9, 4.6, 4.3, 4.1 to a ~$400/day
    ceiling at a 4.0 target) is illustrative arithmetic, explicitly not measured data.
  evidence_strength: MODERATE
  context_completeness: COMPLETE
  platform_validation_status: NOT_APPLICABLE
  research_question_ids: [B2, B3]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: partial
  reason: >
    The scaling-ceiling concept is the valuable part and DR does not have one established. The
    specific percentages are PRACTITIONER_SPECIFIC and the hold period is governed by DR's
    conversion volume, not by his 5–10 days. Currently in tension with BH-P3-16.

- id: BH-P3-18
  claim: >
    A "one angle per ad" creative framework: define a single narrow ideal customer, list the
    distinct reasons that customer might buy, build one ad per reason, and test which reason
    wins — rather than bundling every benefit into one ad. He reports the winning angle
    frequently is not the one the advertiser expected.
  level: EXTERNAL_PRACTITIONER_CLAIM
  source_url: https://www.youtube.com/watch?v=inJWYXen3Xc
  corroborating_sources: [8dJxOaZrK1M]
  published_at: 2026-02-27
  captured_at: 2026-08-19
  evidence_basis: OPERATOR_METHOD
  evidence_basis_details: >
    Worked through twice on his own agency service for two different buyers — small-business
    owners (winning angle: results) versus enterprise marketing managers (winning angle:
    anxiety alleviation / defensible decision, supported by scale and Meta-partner credentials).
    He states which angle won in each case but gives no figures.
  evidence_strength: MODERATE
  context_completeness: COMPLETE
  platform_validation_status: NOT_APPLICABLE
  research_question_ids: [C1, C3]
  question_link_origin: retrospective
  applicability_to_DR: high
  modification_required: yes
  principle_transfers: yes
  implementation_transfers: yes
  reason: >
    Structurally the same insight as the Denney awareness-level framing, arrived at
    independently and expressed as a build instruction rather than a diagnosis. DR's angles
    must be written from DR's own parent research; the framework says only that they be
    separated, one per ad, and raced against each other.
```

## Real-account evidence in this corpus

Six passages contain figures from an actual account rather than illustration. Everything else in 60 videos is method, demonstration in an example account, or Meta's own marketing.

| Video | Date | Account | Figures shown | Named? |
|---|---|---|---|---|
| `qvZYdX1RkdY` | 2025-10-21 | DIY fitted-furniture products client | Before: $26,473 spend → ~$107,000 revenue, 4.07 ROAS. Month 6: $43,000 spend → ~$202–203,000, 4.7 ROAS. Post-ad-spend profit ~$81k → ~$160k | No — "can't say the name or even the industry" |
| `YZ_zNzXHOio` | 2026-03-17 | Client sales campaign | ~$80,000 spend, ~$47–48k to new audience, 942 purchases, >half from warm segments | No |
| `bAo6SICFyIE` | 2026-03-10 | His own agency lead funnel | Hook rates 7–27%; £11.02–£86 per website schedule across ads; 64 and 33 result samples | Own account |
| `4mYjto4VeIk` | 2026-04-07 | His own accounts | 415 link clicks vs 1,179 all clicks on one campaign; four campaigns compared | Own account |
| `zO3UOcVHEp0` | 2026-06-03 | Three client accounts | (a) 3 purchases at £357 CPA against a stated >£5,000 average customer value; (b) 11 leads at ~£14 CPL, stated 154% above Meta's lead-gen benchmark, trend improved 52%; (c) 709 results at $94 CPA, ROAS 1.62 top / 0.69 bottom | No |
| `6s1iHL2mv0g` | 2026-04-14 | His own Ad Library page | 220 ads total; one ad ran 2025-06-18 → 2026-02-04 | Own account |

**None of these is a youth-sports, registration, or geo-constrained business.** `qvZYdX1RkdY` is the nearest structural analogue in one respect only — it is a smaller account where the reported win was ROAS 4.07 → 4.7 while roughly doubling spend, i.e. profit doubling without a headline multiple, which is the realistic shape of a DR improvement.

## Contradictions

### Within this author

1. **Campaign structure** — two campaigns as the default for "the vast vast majority of businesses" (2025-09-23) vs one campaign, one ad set as the default with two campaigns as an exception (2026-02-17). Never acknowledged. See F-1.
2. **Creative volume** — "20+ ads per ad set, produce way more creative" (repeated throughout) vs "20 totally different creatives is unrealistic for a ton of businesses… better a schedule you can stick to" (2026-02-10). He holds both simultaneously.
3. **Scaling method** — step the existing campaign, never duplicate (2026-05-19, restated 2026-08-12) vs duplicate and kill the original (2026-08-03). Environment-forced and explicitly temporary, but live.
4. **Location structure** — bundle all locations into one campaign because multiple ad sets per location becomes unmanageable (2025-11-18, awareness campaign) vs location is the one variable still worth separating across ad sets because it is a hard control (2026-02-17, conversion campaign). Different campaign types; see F-6.
5. **Ad-set-level targeting inputs** — "I'm not convinced that adding much in here makes any difference anymore" and "Meta will probably ignore them" (2025-10-07, 2026-01-06) vs consistently adding interest suggestions in every subsequent demonstration and recommending them for new accounts. He resolves this as "very little downside," not as a performance claim.

### Against Meta, inside his own videos

He recommends deselecting Audience Network and narrowing placements for any campaign not optimising for a true conversion event, and deselecting the local "reach more people likely to respond" option — in both cases quoting Meta's own on-screen warning that results will be worse and overriding it with a reason. He also flags the AI Business Assistant recommending Advantage+ Audience on an account where it was already enabled, and warns generally: *"be skeptical around the advice on increasing budgets. Who's that serving?"* **He is not a Meta mouthpiece, which raises the value of the places where he does agree with Meta.**

### Against other panel members

- **vs Piliero / Denney on Andromeda's date** — he supplies the primary document date (2 Dec 2024, Meta engineering post read on camera) plus a ~1-year rollout, which reconciles rather than contradicts them. See F-3.
- **vs Denney on retargeting** — Denney runs none at any budget; Heath runs no *separate* retargeting campaign but insists the warm audience is being served anyway and must be instrumented and measured. Not the same position; Heath's is the weaker version of the same conclusion.
- **vs Piliero on account structure** — Piliero's method is structural; Heath's 2026 position is that structure has been substantially automated away and the remaining leverage is offer, angle, and creator sourcing. Direct disagreement about where the leverage lives.
- **vs the whole panel on post-Andromeda restructuring** — F-3. He is the only voice calling the elaborate new structures a sign the person recommending them does not run many live campaigns.
- **Convergence** — creators/partnership ads as the highest-leverage lever appears in his corpus with more force than anywhere else in the panel, and it is now corroborated by Meta's CMO on camera as Meta's own priority. Two independent clusters plus the platform itself.

## Open questions from this corpus

1. **Is the budget-increase bug (BH-P3-16) real, and is it still live?** Highest priority. Check before DR raises any budget.
2. **What does `knowledge/official-meta/` say about the click-through / engage-through attribution redefinition (BH-P3-08)?** If confirmed, any DR measurement window spanning April 2026 is discontinuous.
3. **Does Meta's own documentation confirm the 2 Dec 2024 Andromeda publication date and the retrieval-stage description?** This would settle the panel's date dispute against a primary source.
4. **What is DR's actual weekly volume of the candidate optimisation events, per metro?** Everything structural in this file — BH-P3-01, -02, -03, -11, -13 — resolves on that number and it is not yet on file.
5. **Does the "reach more people likely to respond" setting (BH-P3-10) currently exist in DR's ad account, and is it on?**
6. **Is there a youth-activities or parent-audience creator in the Orlando market at a workable price?** BH-P3-15 is the panel's strongest convergent recommendation and DR has no evidence about local supply.

## What must NOT be carried into DR from this corpus

- **Any of his scale figures as precise numbers** — spend, account count, client count, revenue generated. They contradict each other across the corpus.
- **The "82% see notable ROAS improvement in 30 days" mentorship statistic**, and the Tara / Zoe testimonials. Scripted marketing, unaudited.
- **Every figure delivered inside a sponsor read** — Hyros tracking-gap percentages, the £96,000/£58,000 dashboard, Motion, Particl, Holo, ClickMagick, Arcads, Higgsfield claims.
- **The TikTok / platform tier-list numbers** in `gmNefChzGBI` (average TikTok ROAS 2.2–2.5, CPCs 40–50% lower than Facebook). No source given.
- **Anything attributed to Shein** — see the corpus-integrity defect above.
- **The two-campaign scaling/testing structure** as his current recommendation. Superseded.
- **The "$100/day is a small budget, under $600/month is tiny" bracket** as a DR benchmark. It is a UK agency's framing, not a statement about what DR needs per metro.
- **The Starbucks "$14,000 lifetime customer value" figure.** Widely circulated, unsourced here.
