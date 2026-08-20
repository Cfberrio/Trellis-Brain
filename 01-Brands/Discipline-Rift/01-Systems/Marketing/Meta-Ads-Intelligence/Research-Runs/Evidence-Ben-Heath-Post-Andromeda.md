---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/ben-heath-new-way-test-facebook-ads-post-andromeda-evidence.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/ben-heath-new-way-test-facebook-ads-post-andromeda-evidence.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/research-run
  - discipline-rift
aliases:
  - "Ben Heath Andromeda evidence"
---

# Evidence map — Ben Heath — "The NEW WAY To Test Facebook Ads (Post Andromeda)"

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Ben-Heath|Ben Heath]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Transcript-Ben-Heath-Post-Andromeda|Transcripción cruda]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/ben-heath-new-way-test-facebook-ads-post-andromeda-evidence.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Paired raw source:** `ben-heath-new-way-test-facebook-ads-post-andromeda-transcript.md`
**Level:** EXTERNAL PRACTITIONER CLAIM. Nothing here is a DR hypothesis, DR test result, or operating rule.
**Ingested into `knowledge/experts/`?** **No.** This run produces source evidence for later evaluation only.

---

## 1. Why this video was selected

- **Duplication test passed before extraction.** The project's open items include *what to do when
  Meta gives a new creative little or no spend*, *natural delivery vs controlled exposure*, and
  *how many creatives to introduce at once*. This video is about exactly those three, and about a
  platform change (**Andromeda**) that post-dates most of the project's practitioner evidence.
- **Independent cluster.** Not Sam Piliero, Nick Theriot, Jon Loomer, or the Foxwell ecosystem.
  Andromeda currently enters the project only through **one** Foxwell-ecosystem line in
  `output/wave-2b-creative-operating-method.md` ("give Andromeda 10 ads, two or three take 80% of
  spend") and one undefined mention in `knowledge/experts/sam-piliero.md`. A second, independent
  voice on the same mechanism is worth having.
- **Tier 1 / Tier 2 mix.** He performs a live Ads Manager walkthrough of the native creative testing
  flow in his own lead-gen account, including the settings screen and Meta's own inline warning.
- **Recency.** **2026-02-10** — the most recent substantive practitioner source in the project on
  creative testing, and post-Andromeda.
- **Business type fits better than most.** The demo is a **leads campaign optimizing cost per lead**
  for his own mentorship service — lead-gen, not ecommerce. DR is a registration business; a
  lead-gen demo transfers more cleanly than a catalog/purchase one.

### Selection caveats, stated up front

- **Two commercial interests inside the video**: a paid **Hyros** affiliate read (8:35–9:38) and
  promotion of his own **mentorship/Skool** product — which is also the account and the ad creative
  used in the demo.
- **Scale claims are self-reported** ($15M/month, $300M+ lifetime, hundreds of accounts) and
  unverified. The channel carries its own "does not guarantee results" disclaimer.
- **No test results are shown.** He demonstrates *setup*, not outcomes. The one figure he gives
  (10–15% difference between colour and black-and-white) is explicitly hypothetical —
  *"We could see, for example…"*.

---

## 2. ⚠ Conflict with first-party Meta documentation — recorded, not resolved

He states the native creative testing tool compares **"up to five different versions"** and that you
can *"test between two and five different ads"* (3:29, 3:50).

`knowledge/official-meta/creative-testing-ab-testing-and-delivery-diagnostics.md` §1 quotes Meta
first-party: *"you can compare up to **7** creative variants"* and *"You can create **2 to 7**
copies."*

**Per §16 of the run brief and the domain source hierarchy, current first-party Meta documentation
is the authority on platform mechanics.** The practitioner figure is recorded as what he said and
what his UI apparently showed; it does **not** override the documented value. Possible explanations
(rollout variation, regional UI, misreading) are **not** asserted — none was verified.

**Additional detail he does not mention**, already held first-party and unchanged by this source:
the tool requires the **Highest volume** bid strategy; Meta suggests **no more than 20%** of
existing budget goes to test ads; test ads **keep running after the test** and Meta makes **no
automatic changes**; and the result carries **no confidence level**.

---

## 3. Evidence map

### B-1 — ★ Andromeda suppresses *similar* creatives, not merely surplus ones

- **Claim:** Post-Andromeda, if several ads are near-duplicates of one another (minor tweaks —
  text overlay, background colour, price banner, colour vs black-and-white, or a swapped video
  hook on an otherwise identical body), **Meta selects one and enters only that one into the
  auction; the rest get no fair chance and no budget.** Genuinely different ads — different format
  or clearly different visuals — are each treated as separate ads and delivered.
- **Timestamps:** 0:48 (*"Meta will just pick one of those, put that into the auction, the others
  won't get a fair crack at it"*) · 1:56 (*"they're all the same thing. We're only going to choose
  one, and that's the only one that actually gets any any budget"*) · 11:39 (same mechanism applied
  to 40-second videos differing only in the first few seconds).
- **Evidence type:** `OPERATOR_OBSERVATION` — reported from agency practice across accounts. He is
  careful to bound it: *"with Andromeda, this doesn't seem to happen all the time, by the way…
  yes, we've seen it in some instances, but not all"* (11:39). **No account data shown.**
- **Account context:** agency portfolio, self-reported $15M/month across hundreds of accounts;
  mixed business types; specific spend/volume per observation `NOT_DISCLOSED`.
- **Principle:** The unit Meta suppresses is **redundancy**, not count. Creative starvation is
  driven by *similarity to another running ad*, not simply by how many ads are in the ad set.
- **Implementation:** Make each ad in an ad set visually/format-distinct; route near-identical
  variants through the creative testing tool instead.
- **DR transferability:** **HIGH (principle).** If correct, it changes what "small provisional
  creative batch" should mean for DR: a batch of 3 near-identical variations may effectively be a
  batch of **one funded ad**. Differentiation matters as much as size.
- **Existing evidence relationship:** `ADDS_NEW_EVIDENCE`. The project's only prior Andromeda line
  (Foxwell/Fairbrother, via Wave 2B) describes the **symptom** — a few of ten ads take most of the
  spend. This proposes a **cause** — similarity-based deduplication — and a second, independent
  observer of it. It also **bounds** it ("not all"), which the existing line does not.
- **Platform status:** `UNVALIDATED`. Meta's own documented rationale for the creative testing tool
  ("delivery provided to new test ads") is *consistent* with a delivery-suppression problem
  existing, but Meta does not, in what has been retrieved so far, describe similarity-based auction
  exclusion. **Flag for a first-party verification pass; do not treat as a platform fact.**

---

### B-2 — ★ The native creative testing tool is the sanctioned way to force delivery to near-identical variants

- **Claim:** Meta's in-Ads-Manager creative testing tool (ad level) both **guarantees test ads get
  budget** and **separates their delivery** — *"group A within our audience is going to see this
  ad, group B… is going to see this ad"* — so near-identical variants can be compared. After the
  test, Meta *"usually"* shifts spend to the winner, but *"it doesn't always happen"* and you
  should **double-check**; turning off the loser returns delivery to normal.
- **Timestamps:** 3:01–3:50 (location and purpose) · 4:04 (budget share to test ads) · 4:17
  (duration, default 7 days) · 4:39 (comparison metric) · 7:19–8:12 (separate delivery; verify the
  post-test shift yourself).
- **Evidence type:** `OPERATOR_METHOD` + on-screen `REAL_ACCOUNT_EXAMPLE` (his own leads campaign,
  his own mentorship ad, £25/day).
- **Account context:** lead-gen; his own account; **£25/day**; objective leads; comparison metric
  set to cost per lead; conversion volume `NOT_DISCLOSED`.
- **Principle:** When natural delivery will not fund a variant, **controlled exposure inside the
  existing structure** is the alternative to either guessing or building a separate structure.
- **Implementation:** Ad-level creative test, 2–5 (per him) variants, chosen budget share, ≥7 days,
  comparison metric manually set to the real outcome metric.
- **DR transferability:** **HIGH (principle) / MEDIUM (implementation, budget-gated — see B-3).**
  This is the concrete mechanism for DR's open "controlled exposure may sometimes be justified"
  hypothesis, and it lives **inside the existing campaign**, which is DR's constraint.
- **Existing evidence relationship:** `REINFORCES_EXISTING` at the platform layer — the tool and its
  in-campaign, delivery-provided design are **already documented first-party** in the project. What
  is new is (a) the *decision rule* for when to reach for it (B-4), and (b) the operator warning
  that the **post-test spend shift is not reliable and must be checked manually**, which is
  consistent with Meta's own documented "the test does not make any automatic changes" but is not
  the same statement.

---

### B-3 — ★★ Meta's own UI signalled that £25/day over 7 days is too little to read a cost-per-lead test

- **Claim:** With a **£25 daily budget** over the **default 7-day** test, Ads Manager defaulted the
  comparison metric to **cost per post engagement**, and on switching it to **cost per lead**
  surfaced: *"Since your duration or budget changed, the recommended key metric was updated in the
  drop-down… Using this metric can help you get more information results with high confidence."*
  His reading: at that spend and duration you likely **cannot** determine which ad produced a better
  cost per lead; the fix is **more budget, more time, or both**.
- **Timestamps:** 4:04 (£25/day) · 5:04 (the on-screen notice, read aloud) · 5:19 (his translation
  and the remedy).
- **Evidence type:** `REAL_ACCOUNT_EXAMPLE` — this is the **strongest evidence item in either
  video**, because the constraint is asserted by **Meta's own interface on screen**, not by the
  practitioner. His interpretation of it remains `OPERATOR_OBSERVATION`.
- **Account context:** lead-gen; £25/day; 7 days; cost-per-lead comparison; volume `NOT_DISCLOSED`.
- **Principle:** A creative test's readability is **budget × duration × outcome-event rarity**. When
  those are too small, the platform will steer you toward a **shallower proxy metric** rather than
  the outcome you actually care about.
- **Implementation:** Raise budget and/or extend duration until a real-outcome comparison is viable.
- **DR transferability:** **HIGH.** DR runs at roughly **$2.70/day** — well below the £25/day that
  Meta's own UI already flagged as thin, and DR's outcome event (paid season registration) is
  rarer than a lead. The direct implication for DR: a native creative test optimized to DR's real
  outcome is, on this evidence, **very unlikely to return a readable verdict**, and DR would face
  the same proxy-metric pressure. This does not make the tool useless to DR — it makes *the metric
  DR could actually read* the open question.
- **Existing evidence relationship:** `ADDS_NEW_EVIDENCE` — and it is the piece with the most direct
  bearing on DR. Wave 2B already held that a dedicated testing structure needs enough budget/data;
  this shows the **same floor applies to controlled exposure inside the existing campaign**, so
  "test inside the current ad set" does not escape the volume problem. It also connects to the
  first-party A/B guidance already on file (*"tests shorter than 7 days may produce inconclusive
  results"*, *"Your A/B Test should have a budget that will produce enough results"* — **no figure
  given**). Still no defensible number. **None is manufactured here.**
- **Numbers:** `PRACTITIONER_SPECIFIC` — `£25/day`, `7 days`. The £25 figure is **his demo
  account's budget, not a Meta-stated threshold.** Meta stated no number; it changed a default.

---

### B-4 — Decision rule: when the creative testing tool is needed, and when it is not

- **Claim:** The tool is **not important** when the ads are already very different (image vs video,
  clearly different visuals) — Andromeda will not get in the way and both will be delivered, though
  their delivery **will overlap**, which may be desirable. Use natural delivery for the **first,
  coarse round** (image vs video, UGC vs produced vs founder-led). Use the tool for the **fine
  round**, where *"often the winning happens in working out the detail."*
- **Timestamps:** 9:40 (boundary condition) · 10:14 (coarse round without the tool; fine round with).
- **Evidence type:** `OPERATOR_METHOD`.
- **Account context:** agency practice; `NOT_DISCLOSED` per account.
- **Principle:** **Match the exposure mechanism to the size of the creative difference.** Big
  differences survive natural delivery; small differences need controlled exposure.
- **Implementation:** Coarse round = natural delivery in the ad set. Fine round = creative testing
  tool.
- **DR transferability:** **HIGH (principle).** This is a usable, budget-agnostic decision rule and
  it maps onto DR's actual open question ("natural delivery vs controlled exposure") as a
  *conditional* rather than a preference. Implementation is still gated by B-3.
- **Existing evidence relationship:** `ADDS_NEW_EVIDENCE` — the project holds "controlled exposure
  may sometimes be justified" without a criterion for *when*. This supplies a criterion:
  **the magnitude of the creative difference.**

---

### B-5 — Sequencing: resolve variants in the test, then promote the winner into the ad set

- **Claim:** Test five hooks (same body) inside the creative testing tool, identify the winner, then
  *"put that into your ad set without the creative testing, alongside other very different ads"* —
  where the next comparison is between genuinely distinct concepts (UGC vs founder-led vs product
  demo).
- **Timestamp:** 12:26.
- **Evidence type:** `OPERATOR_METHOD`.
- **Account context:** agency practice; `NOT_DISCLOSED`.
- **Principle:** Two different questions need two different mechanisms — *which variant of this
  concept* is a controlled question; *which concept* is a delivery question.
- **Implementation:** Tool → winner → live ad set alongside distinct concepts.
- **DR transferability:** **MEDIUM.** The two-stage shape is clean and matches DR's single-ad-set
  reality, but stage one is the budget-gated one (B-3), and DR's creative production volume is far
  below "five hooks per body."
- **Existing evidence relationship:** `ADDS_NEW_EVIDENCE` — a concrete procedure for *how* a new
  creative enters an existing ad set, which the project holds as a hypothesis without a method.

---

### B-6 — ⚠ Push-back on the "20 completely different creatives" standard

- **Claim:** The prevailing post-Andromeda recommendation — produce 20+ ad creatives, each
  completely different — is *"unrealistic for a ton of businesses"* and is actively **deterring**
  advertisers from producing any. *"If I have to make 20, I'm not going to bother making one."*
  Preferred: a creative production schedule you can sustain, likened to a diet —
  *"if you just tested a couple of new ads every now and then, compounded over time that can make a
  massive difference."* A campaign with **four very different creatives plus a few variations** is
  *"absolutely fine."*
- **Timestamps:** 13:13 · 13:34 · 14:11 · 14:25.
- **Evidence type:** `OPINION` — reasoned, explicitly about feasibility, with **no data**.
- **Account context:** none given for this claim.
- **Principle:** A sustainable testing cadence beats an optimal one that is never executed.
- **Implementation:** ~4 distinct creatives + a few variations; add a couple periodically.
- **Numbers:** `PRACTITIONER_SPECIFIC` — `20+`, `four`. Not adopted.
- **DR transferability:** **HIGH (principle).** DR is precisely the kind of low-production-capacity
  advertiser the 20-creative standard would stall.
- **Existing evidence relationship:** `REINFORCES_EXISTING` (small provisional batches) and
  **`CHALLENGES_EXISTING` external consensus** — it is direct counter-pressure on the volume-heavy
  Andromeda advice that reached the project through the Foxwell-ecosystem line in Wave 2B.
  **Note the tension with B-1 from the same speaker:** he argues both that similar creatives get
  suppressed *and* that four-plus-variations is fine. He resolves it via the tool (B-2/B-4), not by
  abandoning either claim. **Recorded as-is.**

---

### B-7 — Hooks materially change performance, and hook-swap testing survives Andromeda

- **Claim:** The hook (roughly the first 3 seconds) can make an otherwise-identical video perform
  very differently. Advertisers claiming hook-swap testing is dead post-Andromeda are wrong — it
  works, but only **through the creative testing tool**.
- **Timestamps:** 10:36 (hook importance) · 11:13 (2 bodies × 10 hooks = 20 ads) · 12:47 (*"please
  do not throw out the hook method"*).
- **Evidence type:** `OPERATOR_OBSERVATION` — *"you'll often see massively varying differences in
  results between the different hook options."* Magnitude unquantified, no data shown.
- **Account context:** agency practice; `NOT_DISCLOSED`.
- **Principle:** Cheap front-end variation is a high-leverage production strategy, but it produces
  exactly the near-identical assets Andromeda suppresses.
- **DR transferability:** **MEDIUM.** Production-efficient and relevant to DR's parent-facing video,
  but hook-swap volume (10 per body) is far above DR's capacity, and the tool gate (B-3) applies.
- **Existing evidence relationship:** `ADDS_NEW_EVIDENCE` (modest) — names a specific creative
  practice put at risk by the B-1 mechanism, and the workaround.

---

## 4. What is genuinely new

1. **A proposed cause for creative starvation** (B-1): **similarity-based** auction deduplication,
   independently observed and explicitly bounded ("not all"). The project previously held only the
   symptom, from one non-independent cluster.
2. **Meta's own interface flagging that a small budget cannot support an outcome-metric creative
   test** (B-3) — the single most DR-relevant item in this run, and the only claim in either video
   where the evidence is generated by the platform on screen rather than asserted by the speaker.
3. **A criterion for choosing natural delivery vs controlled exposure** (B-4): the magnitude of the
   creative difference.
4. **A concrete two-stage procedure** for introducing creative into a live ad set (B-5).
5. **Independent counter-pressure on the 20-creative standard** (B-6).

## 5. What duplicates existing evidence

- The creative testing tool's existence, its in-campaign design, and delivery-to-test-ads →
  **already documented first-party** in `official-meta/creative-testing-ab-testing-and-delivery-diagnostics.md` §1, in more detail than given here.
- "Small, sustainable creative batches" → already the DR hypothesis.
- "7 days minimum for a readable test" → already held first-party via the A/B guidance.

## 6. Contradictions preserved

| # | Contradiction | Status |
|---|---|---|
| 1 | **He says 2–5 test variants; Meta documentation says 2–7.** | **Preserved. Meta docs govern. Practitioner figure recorded, not adopted, not explained away.** |
| 2 | B-1 (similar creatives get suppressed) vs B-6 ("four creatives plus a few variations is absolutely fine") — same speaker | **Preserved.** He bridges it with the tool, not by dropping either claim. |
| 3 | B-6 (sustainable small cadence) vs the Foxwell-ecosystem-derived volume emphasis already in Wave 2B | **Preserved as a genuine practitioner disagreement between independent clusters.** |
| 4 | He says Meta *usually* shifts spend to the test winner but *"it doesn't always happen"*; Meta documents that the test makes **no automatic changes** | **Preserved.** Not the same statement; not merged. |

## 7. Transferability summary

| Claim | Principle transfers | Implementation transfers |
|---|---|---|
| B-1 similarity suppression | yes | n/a (mechanism) |
| B-2 creative testing tool | yes | partial — budget-gated by B-3 |
| B-3 budget floor for a readable test | yes | yes (as a constraint DR is below) |
| B-4 coarse vs fine decision rule | yes | yes |
| B-5 two-stage sequencing | yes | partial (production volume) |
| B-6 sustainable cadence | yes | partial (numbers not adopted) |
| B-7 hook-swap testing | partial | no (10 hooks per body) |

## 8. Handling rules attached to this source

- **The 2–5 variant figure is superseded by Meta's documented 2–7.** Do not cite his number as
  platform behaviour.
- **B-1 is `UNVALIDATED` against first-party documentation.** It is a practitioner mechanism claim.
  Do not upgrade it. It warrants a targeted first-party verification pass before it informs any DR
  decision.
- Do not convert `£25/day`, `7 days`, `20+`, `four creatives`, or `10 hooks` into DR numbers.
- Self-reported scale ($15M/month, $300M+, hundreds of accounts) is **unverified** and is not
  evidence of claim quality.
- Two commercial interests are present in the video (Hyros affiliate; his own mentorship product,
  which is also the demo account). Neither invalidates the walkthrough, both are disclosed here.
