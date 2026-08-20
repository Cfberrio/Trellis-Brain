---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/audit/youtube-source-audit.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/audit/youtube-source-audit.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/research-run
  - discipline-rift
aliases:
  - "YouTube source audit"
---

# Pre-ingestion audit — the two Apify YouTube sources

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/audit/youtube-source-audit.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Run type:** AUDIT. **No ingestion performed. No existing knowledge modified.**
**Date:** 2026-08-14
**Audited:** the two transcripts + the two evidence maps + the run README created earlier today under
`knowledge/research-runs/2026-08-14_youtube-apify/`.
**Authority rule applied throughout:** the **transcript** is authoritative for what the practitioner
said. The earlier evidence maps are a **prior interpretation under audit**, not evidence.

---

## 0. HEADLINE FINDINGS

Four findings dominate this audit, and three of them are corrections to the prior run.

1. **The prior run treated `$2.70/day` as DR's current budget.** It is not. Wave 2A states it
   explicitly: *"Historical spend ~$2.70–3.70/day — **context, not a confirmed current budget**"*,
   and the campaign is **PAUSED** (extracts through 2026-05-12). **Every ratio built on it is
   withdrawn, not corrected** — including "~370× below", which was additionally mispaired
   (it compared DR to her *$1,000/day account-level phase label*, while calling it her
   *$100–200/ad-set floor*).
2. **Most of what the prior run called "genuinely new" is already in Wave 2B**, usually in a
   stronger, platform-anchored form. Specifically: the spend+CPA kill conjunction, the
   practitioner-spend-floor class, the native creative testing tool and its budget-slice problem,
   the "2–5 vs 2–7" discrepancy, and the Andromeda starvation symptom.
3. **Ben's Andromeda claim is now PARTIALLY VERIFIED against Meta first-party** — and this is the
   single most valuable outcome of this audit. Meta's own creative-diversification page states
   look-alike ads are *"seen as variations of the same creative"* with learnings and delivery
   optimizations *"shared at the creative level"*. That confirms the **grouping premise**. It does
   **not** confirm Ben's **consequence** (one enters the auction, the rest get nothing).
4. **Ben's "up to five" is an on-screen UI reading, not his methodology** — the prior run
   misclassified it. Combined with Loomer's already-on-file *"two to five test ads"* (graded
   `OUTDATED` in Wave 2B), there are now **two independent reports of 5**, one of them from a
   **2026** video. This is no longer safely dismissible as outdated; it is an **open first-party
   re-verification item**.

---

## 1. CLAIM LEDGER

Source support key: `DIRECTLY_SUPPORTED` · `PARTIALLY_SUPPORTED` · `INFERRED` · `NOT_SUPPORTED` · `AMBIGUOUS`
Evidence type key: `OPERATOR_CLAIM` · `SELF_REPORTED_OPERATOR_OBSERVATION` · `ON_SCREEN_PLATFORM_OBSERVATION` · `OPERATOR_METHOD` · `OPINION`

| ID | Expert | Claim (as prior run represented it) | Source support | Evidence type | TS | Existing relation | Transfer | Platform verification | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **DARA-01** | Denney | At low budget use **one campaign**; it is all creative testing | DIRECTLY_SUPPORTED | OPERATOR_METHOD + weak REAL_ACCOUNT_EXAMPLE | 0:32, 0:44 | **REINFORCES** C1/D1 | HIGH principle / LOW impl (ASC) | n/a | Ingest MAYBE |
| **DARA-02** | Denney | Dedicated testing structure justified ~**$1,000/day**; **$100–200/ad set/day** | **SPLIT** — $100–200 DIRECTLY_SUPPORTED as personal recommendation; **"$1,000/day = the floor for a testing campaign" is INFERRED** | OPERATOR_METHOD / OPINION | 6:42, 8:00 | **DUPLICATES** Wave 2B SPEND RULE (same rejected class) | LOW | n/a | **NO** |
| **DARA-03** | Denney | Kill only when CPA misses **and** Meta spends heavily | PARTIALLY_SUPPORTED — conjunction real, **"rule" modality is extractor-added** | OPERATOR_METHOD (scoped to low-budget tier) | 2:39 | **DUPLICATES** Wave 2B D3/D4 "Enough spend + weak response" row | MEDIUM | n/a | MAYBE (as corroboration only) |
| **DARA-04** | Denney | Adding tests to performing campaigns "tanked" performance, repeatedly | PARTIALLY_SUPPORTED as observation; **NOT_SUPPORTED as causal evidence** | SELF_REPORTED_OPERATOR_OBSERVATION | 10:21 | **REINFORCES** an already-accepted cost (significant edit resets learning) | MEDIUM | n/a | MAYBE |
| **DARA-05** | Denney | At growth tier she rejects adding ads to the live structure | DIRECTLY_SUPPORTED — **the prior run under-reported this** | OPERATOR_METHOD | 7:22 | **CHALLENGES** H1 conditionally (growth tier only) | LOW at DR scale | n/a | MAYBE |
| **DARA-06** | Denney | Cadence: 10 to start, +1–2/week, statics-first | DIRECTLY_SUPPORTED | OPERATOR_METHOD | 1:36, 2:39 | **REINFORCES** H5 shape; number contradicts DR's 2–3 | LOW (number) / MEDIUM (shape) | n/a | NO |
| **DARA-07** | Denney | No single correct method; 6–7-figure brands run one campaign | DIRECTLY_SUPPORTED | OPERATOR_OBSERVATION / OPINION | 8:30, 15:40 | **REINFORCES** Wave 2B's no-universal-method finding | HIGH as framing | n/a | MAYBE |
| **DARA-08** | Denney | Start at the real objective, not a proxy | DIRECTLY_SUPPORTED as stated; **rationale is UNSUPPORTED_ASSERTION** | OPINION | 1:04 | **IRRELEVANT_TO_CURRENT_DR_DECISIONS** — Wave 1A settled this first-party | LOW/UNKNOWN | not attempted | **NO** |
| **BEN-01** | Heath | Andromeda suppresses **similar** creatives — one enters the auction, rest starved | **PARTIALLY_SUPPORTED** — he bounds it himself ("not all", "could easily", "might") | OPERATOR_CLAIM | 0:48, 1:56, 11:39 | **CONTEXTUALIZES** the Foxwell volume-symptom already on file | HIGH principle | **PARTIALLY_VERIFIED** — see §5A | **YES** (bounded form) |
| **BEN-02** | Heath | Native creative testing tool guarantees delivery + separates delivery | DIRECTLY_SUPPORTED (he reads the UI + walks the flow) | ON_SCREEN_PLATFORM_OBSERVATION + OPERATOR_METHOD | 3:20–8:12 | **DUPLICATES** — already first-party on file, in more detail | MEDIUM | already on file | NO |
| **BEN-03** | Heath | Meta's UI showed £25/day × 7 days is insufficient to read cost per lead | **PARTIALLY_SUPPORTED — and materially overstated by the prior run.** UI ≠ what he says it means | UI string = ON_SCREEN_PLATFORM_OBSERVATION; sufficiency reading = OPERATOR interpretation (**self-labeled**) | 4:04, 5:04, 5:19 | **REINFORCES** Wave 2B's existing Option-C deferral | MEDIUM | PARTIALLY_VERIFIED — see §5B | MAYBE (bounded form) |
| **BEN-04** | Heath | Decision criterion: natural delivery for coarse, tool for fine | PARTIALLY_SUPPORTED — described as habit ("we'd often find", "less likely"), **"criterion" is extractor formalization** | OPERATOR_METHOD | 9:40, 10:14 | **NEW** (modest) — Wave 2B has the *when-permitted* conditions but not a difference-magnitude heuristic | HIGH principle | n/a | **YES** (as heuristic, not rule) |
| **BEN-05** | Heath | Two-stage: resolve variants in the tool → promote winner into the ad set | DIRECTLY_SUPPORTED (stated; not demonstrated end-to-end) | OPERATOR_METHOD | 12:26 | **NEW** (modest) — a procedure Wave 2B lacks | MEDIUM — gated by tool fundability | n/a | MAYBE |
| **BEN-06** | Heath | 2–5 test variants | **DIRECTLY_SUPPORTED as a UI reading — misclassified by the prior run as his methodology** | ON_SCREEN_PLATFORM_OBSERVATION | 3:29, 3:50 | **DUPLICATES + REOPENS** — Loomer's identical "2 to 5" is on file, graded `OUTDATED` | n/a | **UNRESOLVED — see §5C** | **YES** as a re-verification trigger |
| **BEN-07** | Heath | The 20-creative post-Andromeda standard is unrealistic; sustainable cadence wins | DIRECTLY_SUPPORTED as his opinion; **"standard" is his own characterization, unattributed** | OPINION | 13:13–14:25 | **REINFORCES** H5 | HIGH principle | n/a | MAYBE |
| **BEN-08** | Heath | Hooks matter; hook-swap testing survives via the tool | PARTIALLY_SUPPORTED — magnitude unquantified | SELF_REPORTED_OPERATOR_OBSERVATION | 10:36, 12:47 | **CONTEXTUALIZES** BEN-01 | MEDIUM | n/a | NO |
| **BEN-09** | Heath | Meta "usually" shifts spend to the winner but *"doesn't always happen"* — check manually | DIRECTLY_SUPPORTED | OPERATOR_METHOD | 7:54 | **CONTEXTUALIZES** first-party *"the test does not make any automatic changes"* | MEDIUM | not separately verified | MAYBE |

**Counts — 17 material claims audited:**
`DIRECTLY_SUPPORTED` **8** · `PARTIALLY_SUPPORTED` **6** · `INFERRED` **1** (the DARA-02 floor reading) · `NOT_SUPPORTED` **1** (DARA-04 as causal evidence) · `SPLIT/AMBIGUOUS` **1** (DARA-02 overall).

---

## 2. DARA — MANDATED DEEP AUDIT

### DARA-A → ledger DARA-03 — the "two-condition kill rule"

**Exact wording (2:39), full surrounding sentence:**
> *"…start with 10 ad creatives at those lower budgets and then you can start to add another ad
> creative or two every single week **and I wouldn't worry too much about turning ads off unless
> they really aren't meeting your CPA goal and for some reason the algorithm is spending a lot on
> them** otherwise I would just let them run."*

**What she actually establishes:** at the **low-budget tier only**, her default posture is *leave ads
running*; she departs from that default when an ad both misses CPA and is absorbing meaningful
spend. The conjunction is genuinely in her words.

**What she does NOT establish:**
- She does **not** state it as a rule, law, or threshold. The modality is *"I wouldn't worry too
  much about… unless"* — a reluctance heuristic. *"for some reason"* is conversational aside
  phrasing, not a defined condition.
- She gives **no** definition of "spending a lot", **no** CPA figure, **no** window, **no** account.
- She does **not** claim it generalizes beyond the tier she is describing.
- **No data of any kind is shown.**

**Verdict: the conjunction is `DIRECTLY_SUPPORTED`; calling it a "two-condition kill rule" is
extractor formalization (`PARTIALLY_SUPPORTED`).**

**Deduplication — this is the important part.** Wave 2B §D4 already contains this exact conjunction
in a stronger form, as a row in the situation table: **"Enough spend + weak response"** → *"Possible
genuine weakness"* → *"If repeated across windows → directional dominated-performance kill at next
round."* Wave 2B's version is **strictly better**: it is platform-anchored in the breakdown effect,
it adds the repetition requirement Dara omits, it names the confounds she does not, and it labels
the output DIRECTIONAL rather than a kill. **Relationship: `DUPLICATES`.**

The prior run's statement that this supplied *"the positive half the project didn't have"* is
**INCORRECT** — the project has it.

---

### DARA-B → ledger DARA-02 — the numbers

**Exact wordings:**
- 6:42 — *"if you are past that lean testing phase and you consistently starting to spend **$1,000
  per day** or **$30,000 per month** or even up to **$50,000 per month** you have entered into what
  I call the **growth testing phase**."*
- 8:00 — *"now I **typically recommend $100 to $200 per adset per day**."*
- 13:39 — *"I see most brands here launching creative tests at **200 per day** and then they'll let
  it run for **7 days** or so or maybe until it gets to **a th000** [≈ $1,000]."*

**Classification of each:**

| Figure | What it actually is | Label |
|---|---|---|
| $1,000/day · $30k–50k/mo | **Her definition of a phase label** ("what I call the growth testing phase") | `PRACTITIONER_SPECIFIC` — **a naming boundary, not a stated funding minimum** |
| $100–200/ad set/day | Her personal recommendation — *"I typically recommend"* | `PRACTITIONER_SPECIFIC` |
| $200/day, 7 days, ~$1,000 total | **Observed market practice at the $1M+/mo tier** — *"I see most brands here"* | `ACCOUNT_SPECIFIC` / `EXAMPLE_ONLY` |

**She never says a dedicated testing campaign *requires* $1,000/day.** She says that at $1,000/day
you are in the phase where she *uses* one. The prior run's phrasing — *"her own funding floor"*,
*"the level at which a dedicated testing campaign becomes justified"* — is **`INFERRED`**. The
direction of her practice supports the reading, but she does not assert it.

**Deduplication:** Wave 2B SPEND RULE already covers this entire class —
*"No defensible spend threshold exists. No first-party figure; every practitioner figure found
($100/day minimum-spend limits, $50/day test budgets) comes from accounts 15–40× DR's historical
spend. None adopted, none invented."* Dara's figures are another member of that already-rejected
set. **Relationship: `DUPLICATES`. Ingestion recommendation: NO.**

**All ratios comparing these to DR are withdrawn** — see §4.

---

### DARA-C → ledger DARA-04 / DARA-05 — "tanked"

**Exact wording (10:21):**
> *"having your testing in a different campaign from your scaling helps keep the data quite a bit
> cleaner and it also stops from muddying performance with unproven tests… **I can't tell you how
> many times I've added a creative test to an otherwise performing campaign and I saw performance
> tank** ultimately this is going to give you a lot more stability across your campaigns."*

Audit against the brief's checklist:

| Question | Answer |
|---|---|
| Once or repeatedly? | **Repeatedly** — *"I can't tell you how many times"*. **No count given.** |
| Campaign or ad-set level? | **Campaign.** She says campaign, twice. Never ad set. **DR's question is ad-set-level.** |
| Account type? | Ecommerce. Specific accounts `NOT_DISCLOSED`. |
| Budget level? | Growth tier context ($30k–50k/mo+). **Not her low-budget tier.** |
| Results/data shown? | **None.** |
| Causality demonstrated? | **No.** No control, no isolation, no counterfactual, no confound handling. |

**Second, stronger statement the prior run under-reported — DARA-05 (7:22):**
> *"**instead of tossing one to two new ads into an ASC every time you want to test a creative I
> actually create a new ads set here for each testing concept.**"*

This is a **more direct** rejection of existing-structure introduction than the "tanked" line, and
the prior evidence map did not surface it as its own claim. Recorded here.

**Is this a refutation of H1 (existing-ad-set introduction)? NO.** Reasons, in order:

1. **Level mismatch.** She is arguing campaign separation. H1 is about ad-set-level introduction
   inside a single campaign. These are different questions (the brief's §9 distinction).
2. **Tier mismatch — and she contradicts herself across tiers.** At the low-budget tier the *same
   speaker* prescribes putting everything in one campaign and calls it "all creative testing"
   (DARA-01). DR's structural situation resembles her low tier, not her growth tier.
3. **Already priced in.** Wave 2B D1 §META MECHANICS already states the cost: adding an ad is an
   always-significant edit that **resets that ad set's learning**, and concludes *"Both are true:
   introduction has a real cost and must still happen."* Dara's observation is a weaker,
   undocumented restatement of a cost the project **already accepted from Meta's own
   documentation**.
4. **Her mitigation is the one Wave 2B already evaluated and rejected for DR** (Option B, new ad set
   per round) on fragmentation grounds — and rejected partly *because* Meta's own creative-testing
   feature delivers the same benefit in-campaign.

**Verdict: `REINFORCES` an already-accepted cost. `CHALLENGES` only at growth tier, where DR is not.
Not a refutation.**

---

### DARA-D → ledger DARA-01 — what "consolidated" actually means

The brief warns against collapsing distinct structure concepts. She bundles **three** things in one
passage; they must be separated:

| Concept | Her exact words | Transfers to DR? |
|---|---|---|
| **Campaign count = 1** | 0:32 *"at this stage we are only using one campaign"* | **YES, as principle.** Reinforces C1. |
| **No separate testing structure** | 0:32 *"So in theory it's all creative testing"* | **YES, as principle.** Reinforces C3/D1. |
| **Vehicle = Advantage+ Shopping Campaign** | 2:58 *"I'm using Advantage Plus shopping campaigns for testing at this level"*; 3:20 *"if you're just using one ASC this is truly the most Consolidated type of setup"* | **NO.** ASC is a sales/catalog product. DR's outcome is paid season registration. Not available/applicable. |

Her stated **reason** is the one part that transfers cleanly and is worth recording:
> 3:34 — *"you want to make sure that your budget allows you to get out of the learning phase and
> this setup will help you do that at that lower budget."*

That is a **learning-phase-exit argument for consolidation at low budget** — same mechanism family
as Meta's own *"By combining similar ad sets, you also combine learnings"* already on file.
`REINFORCES`, does not add a new mechanism.

---

## 3. BEN — MANDATED DEEP AUDIT

### BEN-A → ledger BEN-03 — separating the UI from the interpretation

**Parameters, exactly as stated:** budget **£25/day** (4:04, his words: *"this is only got a £25
daily budget"*) · duration **default 7 days** (4:17) · default comparison metric **cost per post
engagement** (4:39) · he changes it to **cost per lead** (4:39) · campaign type **leads**, his own
mentorship/agency business (3:01, 6:33) · conversion volume `NOT_DISCLOSED`.

**What is literally on screen** (his verbatim reading, 5:04):
> *"Since your duration or budget changed, the recommended key metric was updated in the drop-down."*
> *"Using this metric can help you get more information results with high confidence."*

**What Ben says it means** (5:19) — and note he **explicitly flags this as his own translation**:
> *"what they're basically saying here, **without actually saying it, but I can translate for you to
> some extent**, is that, 'Look, only spending 25 pounds per day over a 7-day period and optimizing
> cost per lead, that might not be either enough spent or long enough to be able to know which ads
> within this test produce a better cost per lead.'"*

**The two are not the same evidence.**

| | Content | Class |
|---|---|---|
| Meta UI | The **recommended key metric changes with budget/duration**, and using the recommended metric is framed as helping get results *"with high confidence"* | `ON_SCREEN_PLATFORM_OBSERVATION` |
| Ben | £25/day × 7 days is **insufficient** to read cost-per-lead | **OPERATOR INTERPRETATION — self-labeled as such** |

**The UI does not say:** that the budget is insufficient · that cost-per-lead cannot be read ·
that £25 is too low · anything naming a threshold. It says a *recommendation* was *updated*.

**Prior run's rendering — *"Meta's own UI flagged that £25/day over 7 days cannot reliably read a
cost-per-lead comparison"* — is `INFERENCE_PRESENTED_AS_FACT`.** It attributes Ben's explicitly
self-labeled translation to Meta.

**What survives, and it is still worth something:** *Meta's creative-test UI makes its
recommended comparison metric a function of budget and duration, and frames shallower metrics as
the higher-confidence choice when budget/duration are small.* That is a real, on-screen platform
behaviour and is **new to the project as an observation** — the project's on-file first-party
material covers the tool's setup and the *"A confidence level is not included"* output statement,
but not this input-side metric recommendation behaviour.

**Deduplication:** the *conclusion* it points to — a small budget cannot fund an interpretable
creative test — is **already the project's position**, reached independently and more strongly.
Wave 2B Option C is already **DEFERRED** because *"Meta suggests 'no more than 20%' of existing
budget for the test slice — a trivial absolute amount at DR's scale."* And **Jon Loomer already ran
the mechanism** at $50/day on a `Complete Registration` event — graded in Wave 2B as
`self_reported_test`, **`moderate` strength, "the strongest in corpus"**, and the only source that
actually executed it. **Loomer outranks Ben on this question on every axis: he ran it, on a
registration-type event, and it is already ingested.** `REINFORCES`, not new.

---

### BEN-B → ledger BEN-01 — Andromeda modality

**Every relevant statement, with its modality intact:**

| TS | Words | Modality |
|---|---|---|
| 0:48 | *"Meta **will** just pick one of those, put that into the auction, the others won't get a fair crack at it"* | **Assertive** |
| 1:56 | *"Meta **could easily** look at those and go, 'Nah, they're all the same thing'"* | **Possibility** |
| 2:11 | *"**whilst the system might not recognize them as different ads**, we know that that can have a bigger impact"* | Possibility |
| 7:19 | *"Meta **could easily** look at those two ads and go, 'These are the same thing'"* | Possibility |
| 11:39 | *"with Andromeda, this **doesn't seem to happen all the time**, by the way, cuz I have a lot of people say this, and yes, **we've seen it in some instances, but not all**"* | **Explicit self-bounding** |
| 11:39 | *"what Meta will now do is they **might** look at two ads…"* | Possibility |

**Conservative restatement of what he establishes:** *In his agency's experience, Meta sometimes —
not always — treats minor variants of one creative as the same ad, with the effect that only one of
them receives meaningful delivery.*

**What he does NOT establish:** that it always happens · any frequency · any account, spend, or
volume in which it was observed · any measurement · that Meta documents this behaviour · that this
is what "Andromeda" is.

**Classification: `OPERATOR_CLAIM`, self-bounded. NOT a platform fact from Ben.**

The prior evidence map **did** record the "not all" bound correctly. The prior **chat report** did
not — it stated *"Andromeda suppresses similar creatives"* flatly. `OVERSTATED`.

**Relationship to existing:** `CONTEXTUALIZES`. The project already holds the **symptom** via
Foxwell/Fairbrother (*"give Andromeda 10 ads, most likely two or three will get 80% of the total
spend, with the rest being starved"*) — a **volume**-framed observation, weak evidence, one
ecosystem. Ben proposes a **similarity**-framed mechanism from an **independent** cluster. Those are
different causal stories with **different operating consequences** for DR:

> Under the volume story, DR's answer is *fewer ads*. Under the similarity story, DR's answer is
> *more differentiated ads* — and a batch of three near-identical variants may be functionally one
> funded ad regardless of how small the batch is.

**This distinction is the single genuinely decision-relevant thing either video contributes**, and
it is now **partially supported by Meta first-party** (§5A).

---

### BEN-C → ledger BEN-04 — is there actually a criterion?

**Exact wordings:**
- 9:40 — *"it's **not as important** if you are testing very different ads anyway… The Andromeda
  update's not going to get in the way. You'll be able to test. Now, the delivery's **probably**
  going to overlap."*
- 10:14 — *"**what we'd often find** is that the initial round of testing, we're **less likely** to
  use the creative testing tool because we're finding out the big stuff… But then when we want to
  get into the more detail… then we're going to use the creative testing tool a lot."*

**Assessment:** the distinction is **explicit and unambiguous in content** — big creative
differences survive natural delivery, small ones need the tool. But it is stated as a **description
of habit**, hedged throughout (*"not as important"*, *"often find"*, *"less likely"*, *"probably"*).

**Calling it a "criterion" or "decision rule" is extractor formalization.** It is an
`OPERATOR_METHOD` heuristic. The underlying idea should survive ingestion; the word "rule" should
not.

**Relationship:** `NEW`, modestly. Wave 2B §D4 already specifies **five conditions under which
controlled exposure is permitted** — but all five are about *whether it is worth and possible to
do*. None addresses **which kind of creative question natural delivery can and cannot answer**.
Ben's heuristic slots into that gap and does **not** conflict with the five conditions.

---

### BEN-D → ledger BEN-06 — what "2–5" actually refers to

**This is a misclassification in the prior run, and it matters.**

At 3:20 Ben is **reading the Ads Manager interface aloud**:
> *"you can see it here it says here it here it says, **'Compare up to five different versions of
> your creative in a test that helps ensure delivery to new test ads.'**"*

Then at 3:50, restating it: *"we can test between two and five different ads."*

**So "2–5" refers to: copies/test ads within one native creative test — i.e. exactly the same
quantity Meta's help page calls "2 to 7 copies".** It is **not** concepts, not iterations, not his
own methodology. It is an `ON_SCREEN_PLATFORM_OBSERVATION` that **conflicts with the first-party
help-page text already on file.**

**Critical context the prior run missed:** Wave 2B already records **Jon Loomer's *"two to five test
ads"*** and grades it **`OUTDATED`** against Meta's current *"2 to 7"*. That grading assumed Loomer's
figure was stale. **Ben's video is 2026-02-10 and reports the same 5.** Two independent
practitioners now report 5 from what they describe as the live interface, while the help page says 7.

**This does not overturn the source hierarchy** — first-party documentation still governs platform
mechanics, so the project must continue to hold **2–7**. But *"Loomer is outdated"* is now a weaker
explanation than it was, and the discrepancy needs a real answer (rollout variation? campaign-type
dependence? objective dependence? UI/doc drift?).

**Action: this is a re-verification trigger, not an ingestion of Ben's number.** Recorded in §5C.

---

### BEN-E → ledger BEN-05 — the two-stage procedure

**Exact wording (12:26):**
> *"let's say you test five different hooks, same main body of the ad, but different hooks, find out
> which is the winner, and then **put that into your ad set without the creative testing, alongside
> other very different ads.** That's when you then test, okay, this is a UGC-style ad versus
> founder-led versus product demonstration video ad um type setup."*

| Question | Answer |
|---|---|
| Exact steps? | (1) variants of one concept → native creative test; (2) winner → live ad set, alongside **structurally different** ads |
| Demonstrated? | **No.** Stated only. The on-screen demo covers stage 1 setup, never a completed test or a promotion |
| Specific to the tool? | **Yes — stage 1 requires the native creative testing tool** |
| Applies to normal delivery? | **Stage 2 only** |
| Assumes a budget DR cannot support? | **Stage 1 does**, on his own account: his £25/day demo is where the UI downgraded the metric recommendation. DR's current budget is **not established** (§4), so the honest statement is that stage 1's fundability for DR is **UNKNOWN, and Wave 2B's Option-C deferral remains the governing position** |

**Relationship:** `NEW` (modest). Wave 2B has *where* creative goes (existing ad set) and *when*
controlled exposure is permitted, but no articulated **sequence** for combining the two. Note that
stage 2 — promoting a resolved winner into the live ad set alongside differentiated ads — is
**fully consistent with H1**, not a challenge to it.

---

## 4. TRANSFERABILITY — AND THE WITHDRAWN RATIOS

### 4.1 The budget baseline problem — a correction to the prior run

Project ground truth, verbatim from `output/wave-2a-campaign-architecture-framework.md`:

> *"Historical spend ~$2.70–3.70/day — **context, not a confirmed current budget**"* · source:
> *"Wave 1B; DR extracts through 2026-05-12, **campaign PAUSED**"* · consequence:
> *"Architecture must not assume today's budget is either that figure or a larger one."*

And `knowledge/research-questions.md`: *"Current spend context (~$2.70/day, campaign paused, data
2026-05-12) is preserved as **transferability context, not as a fixed constraint**."*

**Therefore DR's current live daily budget is `NOT_ESTABLISHED`.**

The prior run wrote *"DR runs at roughly $2.70/day"* (Ben evidence map, line 146) and *"DR runs
~$2.70/day"* in the completion report. **Both are `INCORRECT`** — they present a historical figure
from a paused campaign as a current operating budget, which is precisely the derivation Wave 2A
forbids.

### 4.2 Ratio audit

| Ratio as written | Arithmetic | Verdict |
|---|---|---|
| *"roughly 1/37th of her minimum single testing ad set"* (Dara map, D-2) | $2.70 ÷ $100 = **37.0 — arithmetically correct** | **WITHDRAWN** — correct arithmetic on an invalid baseline |
| *"which DR is ~370× below"* applied to **D-2's funding floor** (Dara map, contradictions table) | $2.70 vs $1,000 = 370×, but **D-2's floor is $100–200/ad set/day**, not $1,000/day. $2.70 vs $100–200 = **37–74×** | **INCORRECT — mispaired referent**, and **WITHDRAWN** on the baseline grounds above |
| *"DR runs at roughly $2.70/day — well below the £25/day"* (Ben map) | Also crosses **GBP→USD** with no stated rate | **WITHDRAWN** — invalid baseline plus an unstated currency conversion |

**Replacement language, and the strongest defensible form:** *DR's historical spend (~$2.70–3.70/day,
campaign paused as of the 2026-05-12 extracts) is one to two orders of magnitude below every budget
figure either practitioner discusses. DR's current budget is not established, so no ratio is stated.*

### 4.3 Transferability by dimension

| Dimension | Dara | Ben | Consequence |
|---|---|---|---|
| **Business model** | **Ecommerce**, explicitly (*"for e-commerce"*, 0:29) | **Lead gen / info product** — his own mentorship business, leads campaign, cost per lead | Ben is the closer fit; **neither is local, geo-constrained, or a seasonal registration business** |
| **Budget** | $5k–15k/mo (low tier) → $1M+/mo | £25/day demo; agency portfolio self-reported $15M/mo | Both far above DR's historical context; **no ratio stated** |
| **Signal density** | Purchases, ecommerce volume — `NOT_DISCLOSED` in every claim | Leads — volume `NOT_DISCLOSED`; his own UI flagged the demo as thin | **Neither discloses conversion volume anywhere.** This is the variable DR's problem turns on, and both sources are silent on it |
| **Meta product availability** | **Advantage+ Shopping Campaigns** — sales/catalog. **Not applicable to DR's registration outcome** | Native Creative Testing on a **leads** campaign — **applicable in principle**, deferred on funding | Dara's vehicle does not transfer at all; Ben's does, conditionally |
| **Account maturity** | Explicitly stratifies by maturity | Not addressed | Dara's stratification is her most transferable contribution |

---

## 5. META FIRST-PARTY VERIFICATION

Three mechanics claims isolated from the transcripts and checked narrowly. First-party only.

### 5A — Similarity / Andromeda

**Claim:** Meta's current delivery system suppresses or deduplicates highly similar creatives such
that only one receives meaningful delivery.
**Practitioner source:** Ben Heath, 0:48 / 1:56 / 7:19 / 11:39 (self-bounded — *"in some instances,
but not all"*).

**Meta sources checked:**
- `facebook.com/business/news/demystifying-creative-diversification`
- `facebook.com/business/news/the-creative-advantage-unlocking-the-power-of-diversification-with-meta-andromeda`

**Result: `PARTIALLY_VERIFIED`.**

**The premise is first-party confirmed.** From *Demystifying Creative Diversification*:
> *"When multiple ads look or feel alike, **these are seen as variations of the same creative**,
> meaning **learnings and delivery optimizations are shared at the creative level – not just the
> individual ad level**."*

And Meta itself draws Ben's exact iteration/diversification line:
> *"Creative iteration might produce **two ads with identical visuals, but different text CTAs**"* —
> contrasted with diversification, which produces *"two distinctly different pieces of creative"*
> and assets differing in *"look, feel, storyline, and message."*

**The consequence is not confirmed.** Meta says look-alike ads are **grouped**, with learnings and
delivery optimization **shared**. Meta does **not** say that one is selected into the auction while
the others receive no budget or no fair chance. **Grouping is not suppression**, and the gap between
those two statements is exactly the load-bearing part of Ben's claim.

The Andromeda page **does not address similarity or duplication between an advertiser's own ads at
all**; it describes Andromeda as retrieval-model capacity and defines creative diversification as
*"the practice of creating a wide range of ad creatives with different themes, messages, and
visuals."*

> **Handling note.** The automated page reader added the gloss *"effectively limiting their reach
> potential compared to truly distinct assets."* **That phrase is the reader's inference, not
> Meta's text**, and is not treated as first-party wording anywhere in this audit.

**What can now be said:** *Meta first-party confirms that ads which look or feel alike are treated
as variations of a single creative, with learnings and delivery optimizations shared at creative
level rather than per-ad. Meta does not state that all but one such ad is denied delivery.*

**What cannot be said:** that Meta documents similarity-based auction exclusion; that this is what
"Andromeda" does; that near-identical ads receive no spend.

**Consequence for DR:** the **operating implication survives even on the confirmed half.** If
near-identical ads are optimized as one creative, then a small DR batch of minor variants does not
buy the diversity a small batch of distinct concepts would — **regardless of whether the suppression
consequence is real.** That is a genuine, first-party-grounded refinement to H5.

### 5B — Test sample sufficiency and metric recommendation

**Claim:** Meta's creative test UI may recommend a different (shallower) comparison metric when
budget or duration are limited, implying the chosen business outcome may not be measurable.
**Practitioner source:** Ben Heath, 5:04 (reading the UI) and 5:19 (his interpretation).

**Meta sources checked:** `facebook.com/business/help/1423851372208214` (Set Up a Creative Test) and
`facebook.com/business/help/239549606692303` (About confidence in your tests and experiments).
**Both returned the title-only JS shell to WebFetch** — the known behaviour for
`facebook.com/business/help`, documented in the Wave 3 run. **Not retrieved this run.**

**Result: `PARTIALLY_VERIFIED`, from material already on file.**

Supporting first-party already in `knowledge/official-meta/creative-testing-ab-testing-and-delivery-diagnostics.md`:
- *"Your A/B Test should have a budget that will produce enough results to confidently determine a
  winning strategy."* — **no figure given.**
- *"tests shorter than 7 days may produce inconclusive results."*
- *"if your test didn't run long enough to collect enough data to determine a winner, you'll see a
  recommendation to extend the test."*
- And for creative testing specifically: **"A confidence level is not included."**

**Verified:** Meta does treat budget/duration as determinants of whether a test can be read, and
does surface recommendations when they are inadequate.
**Not verified:** the specific input-side behaviour Ben shows — the **recommended key metric
changing as a function of budget/duration**. No first-party page confirming that was retrieved.
**Not verified and not assertable:** any threshold. Meta states none.

> **Contamination warning — recorded so it is not repeated.** Web search for this claim surfaced
> *"80% confidence"*, *"20 days"*, *"automatic publication of the test winner"*, and *"statistical
> significance in seven days at the earliest"* from **`developers.meta.com/horizon`** — that is
> **Meta Horizon Store creative A/B testing for Quest app listings, a different product entirely.**
> None of it applies to Meta Ads Manager and **none of it is used in this audit.** Note it directly
> contradicts the Ads-side *"A confidence level is not included"* — which is itself evidence that
> the two products must never be merged.

### 5C — 2–5 vs 2–7

**Claim under audit:** how many test ads a native creative test supports.
**Practitioner sources:** Ben Heath 3:20/3:50 (**reading the live UI**, 2026-02-10) and Jon Loomer
(**already on file**, graded `OUTDATED`).
**Meta source:** the help page text already on file — *"you can compare up to **7** creative
variants"*, *"You can create **2 to 7** copies."* The live page was **not re-retrievable this run**
(JS shell).

**Result: `TOO_VAGUE_TO_VERIFY` this run — and reclassified as an open discrepancy.**

**Governing position is unchanged: first-party documentation wins, the project holds 2–7.** But the
prior explanation — that Loomer's "2 to 5" was simply outdated — is now weaker, because a second
independent practitioner reports **5** from the interface in a **2026** video. Two possibilities
remain live and neither is established: the help text and the live UI differ, or the limit varies by
campaign type/objective (Ben's is a **leads** campaign; Loomer's was **Complete Registration**).

**This is materially relevant to DR**, because if the ceiling is objective-dependent, DR's eventual
objective determines it. **Flagged for a rendered-browser re-retrieval, not resolved here.**

---

## 6. HYPOTHESIS IMPACT

**No hypothesis is edited by this audit.**

| ID | Hypothesis | Verdict | Why |
|---|---|---|---|
| **H1** | Existing-ad-set creative introduction | **UNCHANGED** | DARA-04/05 challenge **campaign** separation at **growth tier**, not ad-set introduction at DR's tier — a level mismatch and a tier mismatch. The cost they point at is already accepted first-party (significant edit resets learning). Ben's BEN-05 stage 2 is **consistent** with H1. Dara at low tier **supports** it. |
| **H2** | Batched edits, deliberate change window | **UNCHANGED** | Neither source addresses change-window procedure. DARA-06's "+1–2 every week" is a *cadence*, not a batching-vs-dripping argument, and comes with no evidence. |
| **H3** | Low-volume individual ads may be unreadable | **CONFIDENCE_UP (marginal)** | BEN-03's UI observation is a second, independent, platform-surfaced instance of "small budget → the chosen outcome metric may not be readable". Marginal only, because Loomer's executed $50/day test already established this more strongly and is already ingested. |
| **H4** | No-spend ≠ bad creative | **UNCHANGED** | DARA-03 is consistent with it but adds nothing Wave 2B D4 lacks. **BEN-01 would matter if verified in full** — a *similarity* cause for no-spend would be a genuine new branch of the D4 diagnostic tree. On the currently verified half (grouping, shared optimization) it **reinforces without adding a branch**. Revisit if 5A upgrades. |
| **H5** | Start small, re-derive batch size | **NEEDS_REWORDING** | **The only hypothesis this run genuinely puts pressure on.** Wave 2B derives batch size purely from *how thinly delivery is spread across N ads* — a **count** model. Meta first-party (§5A) now confirms that **look-alike ads are optimized as one creative**, which means **composition matters independently of count**: 3 near-identical variants ≠ 3 creatives. The number 2–3 is not challenged; the **rationale is incomplete**. Rewording is a separate, later decision. |
| **H6** | Controlled exposure useful when fundable | **CONFIDENCE_UP** | BEN-03 adds an independent instance of the funding constraint; **BEN-04** adds the missing complementary axis — *which kind of question* natural delivery can answer, not just *whether a test is affordable*. Wave 2B's five permission conditions are all affordability/design conditions; Ben's heuristic is about question type. Additive, non-conflicting. |

**Also unchanged:** C1 (campaign count — DARA-01 and DARA-07 reinforce), C3 (testing/scaling
separation — DARA-02 duplicates the already-rejected practitioner-figure class), and the D1 batch
**number** itself.

---

## 7. THE SYNTHESIS PROPOSED IN THE BRIEF

> *"Existing-ad-set introduction may remain the least-bad practical starting method for DR while
> simultaneously being an unreliable environment for obtaining interpretable creative comparisons."*

**Verdict: `SUPPORTED`** — and note it is supported **primarily by evidence the project already
held**, not by these two videos.

**Support for the first half (least-bad practical method):**
- Meta first-party: the native creative-introduction feature is built to work *"in an existing
  campaign… There's no need to merge them into another campaign where the learnings would reset."*
- Meta consolidation guidance: *"By combining similar ad sets, you also combine learnings."*
- Every alternative is rejected on grounds independent of preference: second ad set fragments a thin
  budget (Wave 2B Option B); A/B testing needs audience broadening DR **cannot** do because
  residency is the qualification (Option D, platform-grounded); native Creative Testing's 20% slice
  is trivial at DR's scale (Option C, deferred).
- **New here:** Dara independently prescribes exactly this at her low-budget tier (DARA-01), and
  reports six/seven-figure operators doing the same (DARA-07).

**Support for the second half (unreliable comparison environment):**
- Wave 2B's own arithmetic: at every batch size, per-ad weekly impressions land far below any
  readable level — *"no batch size makes individual ads readably comparable at current delivery."*
- The breakdown effect makes unequal delivery **expected**, so unequal delivery cannot be the
  finding.
- *"WHAT COUNTS AS A WINNER — At DR's current delivery: **nothing.**"*
- **New here:** BEN-03's UI observation (small budget/duration shifts the recommended metric toward
  a shallower one) and, on the verified half of §5A, the fact that similar ads are optimized as one
  creative — which further reduces how many genuinely independent comparison units a small batch
  contains.

**The two halves do not conflict, and that is the point.** "Best available place to put creative"
and "place where creative can be compared" are different claims about different properties. The
honest current position: **DR has a defensible creative-introduction method and does not currently
have a creative-testing method at all.** Wave 2B already says this in substance (D3 STATUS:
*"the numeric layer is `NO_USEFUL_EVIDENCE_FOUND`"*; D1: no N makes ads comparable). This audit finds
**no evidence that changes it**, and mild independent reinforcement of both halves.

---

## 8. APIFY COMPLETION REPORT AUDIT

Material statements from the earlier run, scored.

| # | Prior statement | Score | Correction |
|---|---|---|---|
| 1 | *"DR runs at roughly $2.70/day"* | **INCORRECT** | Historical, campaign **PAUSED**. Wave 2A: *"context, not a confirmed current budget."* Current budget `NOT_ESTABLISHED`. |
| 2 | *"DR runs ~370× below her testing floor"* | **INCORRECT** | Invalid baseline **and** mispaired referent (370× is vs her $1,000/day phase label; her stated floor is $100–200/ad set/day → 37–74×). **Withdrawn entirely.** |
| 3 | *"a two-condition kill rule"* — presented as *"the positive half the project didn't have"* | **INCORRECT (dedup) + OVERSTATED (modality)** | Wave 2B D4 already has the identical conjunction, with a repetition requirement Dara omits. Her phrasing is *"I wouldn't worry too much about… unless"* — a heuristic, not a rule. |
| 4 | *"her own funding floor"* / *"the level at which a dedicated testing campaign becomes justified"* | **INFERENCE_PRESENTED_AS_FACT** | She defines a **phase label** at $1,000/day. She never states a requirement. |
| 5 | *"tanked performing campaigns, repeatedly"* | **ACCURATE_BUT_OVERSTATED** | Wording accurate and repetition is stated. But: **campaign-level, not ad-set**, growth tier not DR's tier, no count, no data, **no causality**. Presenting it as counter-pressure on H1 conflates levels. |
| 6 | *"Meta's own UI flagged that £25/day over 7 days cannot reliably read a cost-per-lead test"* | **INFERENCE_PRESENTED_AS_FACT** | The UI said a **recommended metric was updated** because budget/duration changed. The insufficiency reading is **Ben's**, and he explicitly labels it as his own translation. |
| 7 | *"the strongest single item in the run… platform-generated evidence"* | **OVERSTATED** | The UI string is genuine on-screen evidence, but the **conclusion** it supports is already the project's position, and **Jon Loomer's executed $50/day creative test** — already ingested, graded the strongest in corpus — is stronger evidence for it. The prior run never compared against Loomer. |
| 8 | *"Andromeda suppresses similar creatives"* (chat report phrasing) | **OVERSTATED** | Ben self-bounds: *"in some instances, but not all"*, *"could easily"*, *"might"*. The evidence **map** recorded the bound correctly; the **report** dropped it. |
| 9 | *"a controlled exposure criterion"* | **ACCURATE_BUT_OVERSTATED** | The content is real; the **formalization to "criterion" is the extractor's.** He describes a hedged habit. |
| 10 | *"a two-stage procedure"* | **ACCURATE** | Explicitly stated at 12:26. Correctly flagged as stated-not-demonstrated and budget-gated. |
| 11 | *"the 20-creative post-Andromeda standard"* | **PARTIALLY_ACCURATE** | It is **Ben's characterization** of prevailing advice, attributed to no one. The prior run wrote it as an established standard. |
| 12 | *"Ben says 2–5; Meta docs say 2–7 — a conflict"* | **PARTIALLY_ACCURATE** | Conflict is real; **classification was wrong** (it is a UI reading, not his methodology) and **the dedup was missed** — Loomer's identical "2 to 5" is already on file and already graded `OUTDATED`. Two independent reports of 5 now warrant re-verification, not dismissal. |
| 13 | *"Independence clusters: DARA DENNEY (new), BEN HEATH (new)"* | **ACCURATE** | Neither appears in existing expert files or the Wave 2B cluster list. |
| 14 | *"Transcript status COMPLETE"* for both | **ACCURATE** | Coverage matches stated durations; ASR defects flagged rather than reconstructed. Handling was sound. |
| 15 | *"Published 2025-03-28, pre-Andromeda"* (Dara) | **ACCURATE** | Correctly caught the title/date discrepancy; the transcript's three "2025" references confirm it. **This was the prior run's best catch.** |
| 16 | Recommendation *"BOTH_WORTH_INGESTING"* | **OVERSTATED** | Rests on findings scored INCORRECT (#1–3), INFERRED (#4, #6) and OVERSTATED (#7, #8). Re-decided independently in §10. |

**Pattern in the prior run's failures — worth recording for future extraction runs:** it audited the
**sources** competently (dating, ASR defects, commercial disclosures, self-reported scale all handled
well) but **did not audit its own inferences**, and **did not check its "new" claims against Wave 2B
before calling them new**. Four of its five headline "net-new" items were already in the knowledge
base. **Deduplication must happen before novelty is asserted, not after.**

---

## 9. INGESTION CANDIDATES

Only claims worth later consideration. **Nothing here is ingested.**

```yaml
ingestion_candidate:
  claim_id: BEN-01
  expert: Ben Heath
  source: https://www.youtube.com/watch?v=onFwSud9C2Y
  timestamp: "0:48, 1:56, 7:19, 11:39"
  conservative_claim: >
    In his agency's experience, Meta sometimes — explicitly not always — treats minor variants of a
    single creative (text overlay, background colour, colour vs black-and-white, a swapped video
    hook on an otherwise identical body) as the same ad, with the reported effect that only one of
    them receives meaningful delivery.
  evidence_type: OPERATOR_CLAIM   # self-bounded: "in some instances, but not all"
  context: >
    Agency portfolio, self-reported $15M/month across hundreds of accounts. No specific account,
    spend, conversion volume, or measurement disclosed for this observation. No data shown.
  principle: >
    Creative starvation may be driven by REDUNDANCY (similarity to another running ad), not only by
    ad COUNT. Differentiation and batch size are separate levers.
  implementation: >
    Make ads in one ad set format- or visually-distinct; route near-identical variants through the
    native creative testing tool instead of the open ad set.
  relationship_to_existing: >
    CONTEXTUALIZES the Foxwell/Fairbrother volume-framed starvation observation already in Wave 2B.
    Different causal story, different operating consequence, and an independent cluster.
  dr_transferability: HIGH (principle) / UNKNOWN (implementation — tool fundability not established)
  confidence: medium-low
  numeric_provenance: none — no figures attached to this claim
  platform_validation: >
    PARTIALLY_VERIFIED. Meta first-party (Demystifying Creative Diversification) confirms the
    GROUPING premise: ads that "look or feel alike" are "seen as variations of the same creative",
    with "learnings and delivery optimizations shared at the creative level". Meta does NOT confirm
    the SUPPRESSION consequence. Ingest the grouping half as first-party-supported; ingest the
    suppression half only as a bounded operator claim.
  ingestion_recommendation: YES
```

```yaml
ingestion_candidate:
  claim_id: BEN-04
  expert: Ben Heath
  source: https://www.youtube.com/watch?v=onFwSud9C2Y
  timestamp: "9:40, 10:14"
  conservative_claim: >
    He reports using natural delivery for coarse comparisons (image vs video, UGC vs produced vs
    founder-led) and reaching for the native creative testing tool for fine ones, on the basis that
    large creative differences are delivered anyway while small ones may not be.
  evidence_type: OPERATOR_METHOD   # hedged habit — "we'd often find", "less likely", not a rule
  context: Agency practice. No account, spend, or volume disclosed.
  principle: >
    Match the exposure mechanism to the MAGNITUDE of the creative difference being tested. Natural
    delivery can answer coarse questions; it may not be able to answer fine ones.
  implementation: Coarse round in the open ad set; fine round via native Creative Testing.
  relationship_to_existing: >
    NEW, modestly. Wave 2B D4 specifies five conditions for permitting controlled exposure — all
    about affordability and design. None addresses which KIND of question natural delivery can
    answer. Complementary, not conflicting.
  dr_transferability: HIGH (principle) / gated (implementation — see H6 and Option C deferral)
  confidence: medium
  numeric_provenance: none
  platform_validation: >
    NOT_APPLICABLE as stated — it is an operating heuristic, not a platform mechanic. Its premise
    partially inherits BEN-01's PARTIALLY_VERIFIED status.
  ingestion_recommendation: YES
```

```yaml
ingestion_candidate:
  claim_id: BEN-06
  expert: Ben Heath
  source: https://www.youtube.com/watch?v=onFwSud9C2Y
  timestamp: "3:20, 3:50"
  conservative_claim: >
    Reading the Ads Manager interface aloud on 2026-02-10, he reports it stating "Compare up to five
    different versions of your creative in a test that helps ensure delivery to new test ads", and
    restates the range as two to five test ads.
  evidence_type: ON_SCREEN_PLATFORM_OBSERVATION   # NOT his methodology — prior run misclassified
  context: Leads campaign, his own account, £25/day, UK interface.
  principle: n/a — a reported platform limit.
  implementation: n/a
  relationship_to_existing: >
    DUPLICATES Jon Loomer's "two to five test ads", already on file and graded OUTDATED against
    Meta's documented "2 to 7". Two independent reports of 5 now exist, one from 2026.
  dr_transferability: n/a — platform mechanic, governed by first-party documentation
  confidence: n/a
  numeric_provenance: >
    "up to five" = REPORTED_UI_STRING (second-hand, screen not inspectable).
    "2 to 7 copies" = META_PLATFORM_GUIDANCE (help-page text on file).
  platform_validation: >
    Governing value remains 2-7 per first-party documentation. The discrepancy is UNRESOLVED and
    "Loomer is outdated" is no longer an adequate explanation.
  ingestion_recommendation: MAYBE   # ingest as a re-verification trigger, never as a platform limit
```

```yaml
ingestion_candidate:
  claim_id: DARA-01
  expert: Dara Denney
  source: https://www.youtube.com/watch?v=7knQyPYLmfo
  timestamp: "0:32, 3:34"
  conservative_claim: >
    For ecommerce brands spending roughly $5k-15k/month or lower she uses a single campaign and no
    separate testing structure, on the stated reasoning that consolidation helps the budget exit the
    learning phase. Her vehicle is an Advantage+ Shopping Campaign.
  evidence_type: OPERATOR_METHOD   # plus an unquantified real-account example, no results shown
  context: >
    Ecommerce, $5k-15k/month or lower, sales objective optimizing purchases, new/early brands.
    Conversion volume NOT_DISCLOSED. Published 2025-03-28 — PRE-ANDROMEDA.
  principle: >
    Below some budget level, splitting spend across structures buys nothing because no structure is
    individually readable; consolidation additionally concentrates budget toward learning-phase exit.
  implementation: One Advantage+ Shopping Campaign holding ~10 creatives.
  relationship_to_existing: >
    REINFORCES C1 and D1 from an independent cluster and by a different route (budget logic and
    learning-phase exit rather than DR's fragmentation constraints).
  dr_transferability: HIGH (principle) / LOW (implementation — ASC is a sales/catalog product not
    applicable to DR's paid-season-registration outcome)
  confidence: medium-low
  numeric_provenance: "$5k-15k/month = PRACTITIONER_SPECIFIC; 10 creatives = PRACTITIONER_SPECIFIC"
  platform_validation: >
    NOT_APPLICABLE for the method itself. Its learning-phase rationale is directionally consistent
    with Meta's existing consolidation guidance already on file.
  ingestion_recommendation: MAYBE   # corroboration of a settled decision; adds no new decision value
```

```yaml
ingestion_candidate:
  claim_id: DARA-07
  expert: Dara Denney
  source: https://www.youtube.com/watch?v=7knQyPYLmfo
  timestamp: "8:30, 15:40"
  conservative_claim: >
    She states there is no single correct way to test on Meta, and reports knowing several six- to
    seven-figure brands running the one-campaign method rather than her own two-campaign structure.
  evidence_type: OPERATOR_OBSERVATION / OPINION
  context: Referenced brands' contexts NOT_DISCLOSED.
  principle: >
    Testing methodology is a decision under constraints, not a best practice. Consolidation is not
    only a beginner posture.
  implementation: n/a
  relationship_to_existing: >
    REINFORCES Wave 2B's no-universal-method finding, which currently rests largely on the Foxwell
    ecosystem contradicting itself. An independent voice strengthens it.
  dr_transferability: HIGH as framing discipline; nothing to implement.
  confidence: low
  numeric_provenance: '"six to seven figure" = ACCOUNT_SPECIFIC, unspecified brands'
  platform_validation: NOT_APPLICABLE
  ingestion_recommendation: MAYBE
```

**Explicitly NOT ingestion candidates:** DARA-02 (duplicates an already-rejected figure class),
DARA-03 (duplicated and weaker than Wave 2B D4), DARA-06 (number conflicts with DR's derivation and
carries no evidence), DARA-08 (Wave 1A settled it first-party), BEN-02 (already first-party on file,
in more detail), BEN-08 (unquantified).

**Borderline, deliberately left at MAYBE:** DARA-04 (real observation, no causality, wrong level),
BEN-03 (real UI observation, but its conclusion is already held and Loomer's executed test is
stronger), BEN-05 (clean procedure, stage 1 fundability for DR unknown), BEN-07 (opinion),
BEN-09 (minor operational check).

---

## 10. SOURCE VERDICTS

### DARA DENNEY — `KEEP_AS_RAW_SOURCE_ONLY`

**Why.** Every claim that survives audit either duplicates Wave 2B (the kill conjunction, the
practitioner spend-figure class), reinforces an already-settled decision (one campaign, no universal
method), or fails to transfer (ASC vehicle, 10-creative batch, growth-tier campaign separation). Her
one apparently-challenging claim (DARA-04/05) is **campaign-level at growth tier** and does not
reach H1. **No claim in this video would change a DR decision.** She is a genuinely independent,
competent operator and the budget-tier stratification is a useful mental model — that is worth
keeping accessible as a raw source, and it is not worth a knowledge-base entry.

The additional discount: **published 2025-03-28, pre-Andromeda**, ecommerce-scoped by her own words,
**no performance data shown anywhere in 17 minutes.**

**If a later run disagrees, DARA-01 and DARA-07 are the only two defensible entries** — both as
corroboration of settled positions, neither as new evidence.

### BEN HEATH — `INGEST_SELECTIVELY`

**Why.** Two claims justify it and the rest do not.

- **BEN-01** is the only claim in either video that is (a) materially new, (b) from an independent
  cluster, (c) **partially verified against Meta first-party in this audit**, and (d) capable of
  changing a DR operating decision — it makes creative **composition** matter independently of
  batch **count**, which the current H5 rationale does not capture.
- **BEN-04** fills a real, identified gap in Wave 2B's controlled-exposure conditions.
- **BEN-06** is worth carrying as a **re-verification trigger**, not as a number.

Everything else duplicates (BEN-02), reinforces without adding (BEN-03, BEN-07), is unquantified
(BEN-08), or is minor (BEN-05, BEN-09).

Ingest **only the conservative restatements in §9**, with the modality bounds intact —
*"in some instances, but not all"* is part of the claim, not a caveat on it.

---

# PRE-INGESTION GATE

```text
DARA:
KEEP_AS_RAW_SOURCE_ONLY

BEN:
INGEST_SELECTIVELY
```

```text
READY_FOR_INGESTION_DECISION:
YES
```

`YES` means the evidence is now sufficiently audited for a **separate future ingestion run**.
**It does not authorize ingestion.** No ingestion was performed. No existing knowledge was modified.

## Carried forward for a future run (not actioned here)

1. **Re-retrieve with a rendered browser** (the `facebook.com/business/help` JS shell blocks
   WebFetch): `Set Up a Creative Test in Meta Ads Manager` (2–5 vs 2–7; whether the ceiling depends
   on objective/campaign type) and `About confidence in your tests and experiments`.
2. **Verify the input-side metric-recommendation behaviour** Ben demonstrates — whether Meta
   documents the recommended key metric changing as a function of budget/duration.
3. **Chase the suppression half of 5A** — whether any first-party page states a delivery consequence
   for grouped look-alike creatives, beyond shared learnings and optimization.
4. **H5 rewording** — the composition-vs-count point, if BEN-01 is ingested. A Wave 2B decision, not
   an audit decision.
5. **Never reuse the withdrawn ratios.** DR's current budget is `NOT_ESTABLISHED`.
