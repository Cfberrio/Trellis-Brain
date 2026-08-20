---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase3-full-video-extraction/per-video/jon-loomer-notes.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase3-full-video-extraction/per-video/jon-loomer-notes.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/research-run
  - discipline-rift
aliases:
  - "Jon Loomer phase 3 notes"
---

# Jon Loomer — full-video review working notes

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Jon-Loomer|Jon Loomer]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase3-full-video-extraction/per-video/jon-loomer-notes.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Status:** videos 0-36 of 60 reviewed in full (chronological). Notes written incrementally so context loss cannot destroy the pass.

Corpus: 60 videos, 54,891 words, **all CURRENT** (2025-12-31 → 2026-08-19). Format: solo "Pubcast Shots" (his own topic) alternating with listener-question episodes. 3-12 min each. Sponsor reads are his own products (Power Hitters Club Elite, coaching, The Loop) and are excluded.

---

## THE SINGLE MOST IMPORTANT FINDING — his method changed mid-corpus

This is the temporal-evolution case the run brief asks for, and it would have been invisible to passage sampling.

| Period | Position on introducing new creative |
|---|---|
| **2026-01-06 → ~2026-04** (`b6_4nv_nLPU`, `21xBd19tc0w`, `nT0D1t_0r1U`) | **Start every new ad set with a creative test** using Meta's native creative testing tool, inside the ad set where the ads will live. Reason: (a) you learn how an ad performs when given forced equal budget, (b) the tool cannot test *existing* ads, so testing later requires duplicating ads — "super messy". |
| **2026-05-04 onward** (`bz2qGzNBbRo`) | **Superseded.** A new feature — **"push delivery to this ad"** — lets you force a % of budget to a *single existing ad* for a set period. "There's no longer a reason to start new ads with a test because I can always answer questions later with push delivery if necessary. And I no longer feel like I need to create at least two ads at a time." |

**Why this matters more than anything else in his corpus for DR:** DR's creative hypothesis holds that *"no-spend is an allocation condition, not automatically a creative verdict"* and that *"controlled exposure can sometimes be justified."* Push delivery is a **native, in-place, non-structural mechanism for controlled exposure** — it does not require a second campaign, a second ad set, or a budget split. That is precisely the funded mitigation the Denney contradiction (D-1 vs D-5) left DR without.

⚠ He did **not** have the feature at time of recording — "I unfortunately don't have it yet, but I'm going to use the hell out of it when I do." So this is **an announced feature and a stated intent, not an operator result.** Availability for DR's account is unverified and this must be checked in Ads Manager before it informs anything.

---

## Real-account evidence (the rare cases where he shows his own data)

### L-A — Value rules moved a bad age band from 70% of budget to the smallest share
His own lead-gen account. Breakdown by age showed 65+ plus 55-64 consuming **70% of budget** at cheap cost and low quality. Previous fix was to *restrict* the age range, which he rejects because it forces Meta to dump the budget into the adjacent band. Instead: **bid −50% on 65+, −20% on 55-64.** Result: 65+ became the *lowest* percentage of budget; 55-64 fell below the 18-24 group. `REAL_ACCOUNT_EXAMPLE` · before/after distribution stated, no CPA/CPL figures. (`IqNq_Poh3Ow` 2026-01-13, restated `WfoA-2u5KEA` 2026-03-02.)

### L-B — Remarketing share decays measurably as the warm pool exhausts
Using audience segments + breakdown on his own account: remarketing takes **~25% of budget early, falling to 5-10%** as the pool is used up. Offered as the mechanism behind "campaigns start strong then decline." `REAL_ACCOUNT_EXAMPLE`. (`7WMrhoGnEX4` 2026-01-22; the 20-25% figure restated `WfoA-2u5KEA`.) **Directly relevant to DR: the smaller the warm pool, the faster the decay** — he names small audiences and niche products as accelerants.

### L-C — Social proof may be worth far less than assumed
An ad with **6,000+ comments**, running over a year for a professional service, peaked at **$50/lead**. He duplicated it with minor edits so it started from **zero social proof**. The new ad ran at **$46/lead in its first two weeks** — no build-up period, no underperformance. He explicitly calls the difference "probably within a range of randomness." `REAL_ACCOUNT_TEST` (informal, n=1, not controlled). (`7FlZpLkK7Lc` 2026-04-06.)

### L-D — Click attribution used to count non-link clicks
2024 test: built an ad with **no hyperlink anywhere**, instructing people to click the image and then separately visit a page. Meta reported **20+ conversions, all as click-through.** This led to Meta's 2026 change: click-through now requires a link click; social/other clicks moved to **"engage-through"**, which has a **1-day window** versus click-through's 7-day default. `REAL_ACCOUNT_TEST` — a genuine designed experiment, the strongest single piece of evidence in his corpus. (`lOhs1arlsLU` 2026-03-16.)

### L-E — A test he ran against his own belief
Stuck with an underperforming ad set through "a week of below average results" rather than killing it; it recovered. Offered as evidence for judging on 7-day windows, not daily. (`awYIlUr2RGs` 2026-03-09.)

---

## His operating philosophy as of the current material

**Targeting (`WfoA-2u5KEA` 2026-03-02 — the cleanest single statement):**
- No audience suggestions at all. No age/gender restriction. No detailed targeting. No lookalikes.
- Almost never restricts by custom audience (remarketing) — Meta already spends 20-25% there and he can prove it with breakdowns.
- **Only settings he touches: locations and exclusions** — the two things that are *audience controls*, i.e. hard constraints Meta respects.
- Demographic problems get solved with **value rules**, never with restriction.
- Combines similar countries in one ad set "unless I can get significant volume from splitting them up."

**Structure:** minimum campaigns and ad sets. Separate creative-testing campaigns are "counterproductive, especially for anything other than the highest budgets." Every added ad set/campaign risks auction overlap, audience segmentation and diluted budget.

**Creative:** "stack creative diversity in phases" — do not obey Meta's diversification guidance literally at modest budget. One theme at a time, learn, then build a *uniquely different* next set.

**Diagnosis:** ads first, always. "When you're not getting the results you want, create new ads."

---

## Claim candidates — reviewed in full context, ranked by DR value

### HIGH VALUE

**LO-1 — Legitimate reasons to split campaigns/ad sets, and location is one of them** (`-DE7MHI6YLo` 2026-01-15)
He lists the *only* cases he accepts: separate business objectives; separate product lines needing dedicated budget; **"you need to promote multiple locations for your business, so you need to dedicate separate budget to each location"**; and controlling remarketing share for brands with huge warm audiences. **Every one is gated on the same condition, stated three times: "you need to have the budget to efficiently drive results in each campaign or ad set. If not, you're just making results worse for the sake of complexity."**
→ **This is the C1/E3 evidence the corpus was missing.** It is a *conversion-campaign* statement from an independent operator — unlike the Heath multi-location passage, which came from an awareness campaign. Location separation is legitimate **in principle**; it is **budget-gated in practice**. For DR that resolves to: stay bundled.

**LO-2 — Native creative testing tool: test inside the live ad set, 2-5 ads** (`b6_4nv_nLPU`, `nT0D1t_0r1U`, `LwHtofIL8Ac`)
Mechanics as he describes them: start a test when creating/editing an ad; up to 5 (possibly 10) ads; **cannot test existing ads**; you assign a % of the existing campaign/ad-set budget (Meta suggests ~20%, he sets 100% when the ad set is new); choose duration and success metric; budget is spread evenly during the test; when it ends the ads **keep running** in the same ad set with normal delivery.
He starts new ad sets with **2-5 ads**, not 20-30. **DR's provisional 2-3 batch sits inside his stated range** — from an operator who reached it independently.
⚠ **He states his own volume floor:** *"if I'm testing five ads at $20 per day to sell something, I'm unlikely to get the volume necessary to learn anything meaningful"* and *"five ads split up $50 per day for a week... that's $10 per day for each ad"* → **test 2 ads instead, or extend to two weeks.** `PRACTITIONER_SPECIFIC`, but the *reasoning* (ads × days × budget must clear the conversion volume needed for a read) transfers exactly.

**LO-3 — Push delivery supersedes the above** (`bz2qGzNBbRo` 2026-05-04) — see the evolution box. Announced feature + intent, **not** a result.

**LO-4 — Too many ads in one ad set may hurt, and pruning is a legitimate lever** (`lNP3lybp5Yg` 2026-05-06)
Meta's old "no more than six ads per ad set" guidance was **removed** around the Andromeda updates. His current position: start with **a couple of ads**; let it run 1-2 weeks; if results are good, don't touch it; if not, add more. And — a change from his older advice — *"I'm also starting to see evidence that it can help to prune a bit if you aren't getting great results… the delivery algorithm can get a bit lost when it has too many options for the budget."* He labels this **"truly just a hunch at this point, and Meta hasn't come out and said it."**
→ Honest self-labelling of an unproven belief. Directly relevant to DR's small-batch hypothesis; **must be carried with his own hedge attached.**

**LO-5 — Value rules as the future of delivery control** (`5LEjQP8nlCs` 2026-04-27, `IqNq_Poh3Ow`, `j8803_J6Dug` pending)
The mechanism DR cares about: encode advertiser-held quality information as a *bid adjustment* rather than an audience restriction. A test version he is in extends value rules to **custom-audience labels** (qualified/disqualified lead, high/low value customer, at-risk, churned). ⚠ Platform-mechanics claims throughout → `UNVALIDATED`.

**LO-6 — Seasonal structure: evergreen ad set + per-season ad sets under CBO** (`fn1PiqDN_Nk` 2026-01-29)
For a seasonal product business: one evergreen ad set running year-round, plus a new ad set per season/holiday started with a creative test of **2-5 ads**; turn the old seasonal ad set off **on performance, not on the calendar** — *"even if the holiday has passed, there's no reason to stop that ad set if it's still getting good results."* Next year, the ad set restarts carrying the prior year's ads. He **resists ad-set spending limits** unless a specific problem demands them.
→ **DR runs six-week seasons.** This is the only structural advice in the corpus addressed to a seasonal advertiser. Note it is CBO with multiple ad sets — more complexity than DR runs today — and it is a `NOT_DISCLOSED`-budget answer to a listener, not an account he operates.

### MEDIUM VALUE

**LO-7 — Customer personas do not need separate ad sets** (`kKGDk-D9Ego` 2026-02-26). His worked example is literally *"soccer moms between 35 and 44"* vs *"empty-nester moms between 55 and 64"* — different creative, same ad set, because "Meta will find the right audience for the right combination." Splitting is only for the 50-ad limit, and then purely organisational, still under CBO.

**LO-8 — Audience suggestions are an illusion of control** (`m4JmGFzhlNw`, `mR84yVP2_Qw`). Detailed targeting is a suggestion under **11 performance goals**, lookalikes under **9**. Location targeting and exclusions are **never** suggestions — they are audience controls Meta respects. ⚠ The two counts are the already-flagged platform claim; `UNVALIDATED`.

**LO-9 — New accounts: do not "warm up" the pixel** (`lc0heU-54ik` 2026-04-15). Calls page-building, awareness/traffic warm-up and pixel-seasoning "nonsense… they may even hurt you," because top-of-funnel optimization fills your history and built-in remarketing audiences with low-quality engagement. **Optimize for the real action from day one.** Notes a new account will have a **low daily spending limit** that only rises by spending against it. `OPINION` with a stated mechanism; no data.

**LO-10 — Attribution: what each conversion type means** (`L8fiEfHgGy8`, `lOhs1arlsLU`). Click-through within 1 day = most intent; engage-through = interest but no site visit, **1-day window**; view-through = "flimsiest of all." Practical instruction: use **breakdown by attribution setting** and **compare attribution settings** rather than taking the headline number. → Bears directly on DR's 7-day-click/1-day-view starting hypothesis.

**LO-11 — Long buying cycles** (`SDN08ixAQrk` 2026-03-25). First: **confirm the long cycle is real in data** rather than assumed from price. A later click can start a *new* 7-day window, so a long cycle does not automatically break attribution. If volume is genuinely too low, lead generation is a reasonable alternative — "remain dedicated to a conversion of some kind." → Relevant to DR's open objective/event question; **weaker than the first-party documentation that settled Wave 1A.**

**LO-12 — Niche/small audiences are not the problem** (`yXc2cAd_B0E` 2026-04-08). "Technically, I don't believe a business can be too niche for Meta" — if the real-world market is big enough to be profitable, the people are reachable. What decides success is creative, offer, qualification and follow-up, not targeting. Explicitly `OPINION`, no data.

**LO-13 — Lead quality is mostly controlled outside the ads** (`hOCXyTee_S4` 2026-01-27). Own account: new lead magnet, real (non-bot) leads, low welcome-email open/click. Fixed domain settings, confirmation page, subject line, and added a 3-day reminder automation. → Maps onto DR's measurement layer 3 (qualified response).

**LO-14 — Server-side tracking, cheapest viable path** (`9kAGSaHQERk` 2026-01-08). Pixel alone is no longer dependable. Conversions API Gateway via **Stape (~$10/month)**, which reuses existing pixel events and deduplicates. CRM events are a much bigger lift and carry deduplication risk; one clean approach is sending CRM events **only** for transactions that never touch the website. Declares no affiliation. → DR's signal quality is a live constraint; this is the most concrete, cheapest implementation path in the corpus.

**LO-15 — Diagnose before blaming the platform** (`awYIlUr2RGs`, `7OjOzuRS41k`, `EyMqJVjA9_c`). Five causes of a sudden drop: **randomness** (explicitly worst at ~10 conversions/day — DR's volume range), recent changes causing auction overlap or restarting the customer journey, competitive/seasonal CPM shifts, website problems, event delays. Judge on **7-day windows**. Do not kill previously-working ad sets over a bad day or two.

### LOW VALUE / NOT RELEVANT (reviewed, not ingested)
- `mBTdn55KkYA` popups on landing pages — generic, no data.
- `0cINc9ds3Pc` excluding repeat purchasers of one product — ecommerce-specific problem DR does not have.
- `IXxVMKrZ4nQ` reaching only new customers — same family; useful line is "confirm there is a problem before excluding."
- `7Kumj5fkXic`, `XJdmsh30xMk` agency/client access and transparency — agency operations, not Meta operating knowledge. (`XJdmsh30xMk` has real practical value for Trellis-as-agency, but is out of scope for DR ads intelligence.)
- `SYRjZdE0qS8` CPM by country — the transferable line is *"if overall conversion volume and stability are a problem, I'd combine the countries into the same ad set"*, which is the same consolidation logic as LO-1. Recorded there.
- `nsavNI9b1dY` Meta's creative-reporting opacity — no DR decision; useful only as a caution that per-asset performance is not visible in flexible format/related media/AI creative.
- `raTwalw99ig` manual bidding — he has not used it in years; explicitly "I haven't used manual bidding in years." Honest non-answer.
- `L8fiEfHgGy8` credit-stealing — folded into LO-10.
- `EyMqJVjA9_c`, `TKRs1ENTDSA`, `7OjOzuRS41k`, `ufPIYVdvL1o`, `7FlZpLkK7Lc` (partly) — discipline/mindset content. Real value, but it is method-hygiene, not Meta mechanics. Folded into LO-15.

---

## Contradictions inside his own corpus

1. **Creative testing tool: essential → largely obsolete**, four months apart, by his own account (LO-2 vs LO-3). He states the reason openly. **This is evolution, not inconsistency — but any claim sourced from the January material must carry the May supersession.**
2. **"Let low-spend ads run" → "pruning may help."** In `lNP3lybp5Yg` he says his past advice was to let it go, and he now suspects the opposite at modest budget. He flags it as a hunch.
3. **"Never restrict by age/gender" vs. an entire feature for adjusting by age/gender.** He resolves this himself: restriction is the old way, value-rule bidding is the new way. Recorded as resolved-by-speaker.
4. **He recommends against separate remarketing structures, then lists the conditions under which he would build one** (huge warm audience, or prospecting far more profitable). Conditional, not contradictory.

## Platform-mechanics claims requiring first-party validation
- Detailed targeting is a suggestion under **11** performance goals; lookalikes under **9**.
- Location targeting and custom-audience **exclusions are always hard constraints**, never suggestions.
- Click-through now requires a **link** click; social/other clicks → **engage-through**, **1-day** window.
- Meta **removed** its "no more than six ads per ad set" guidance.
- Creative testing tool: max 5 (or 10) ads, cannot test existing ads, ~20% budget default, even spend during test.
- **"Push delivery to this ad"** exists and behaves as described. ⚠ **He did not have it.**
- Customer lifecycle strategy / new-customer-only ad-set option — described as "in testing", "mysterious".
- Value rules for custom-audience labels — a test he is in, not general availability.
