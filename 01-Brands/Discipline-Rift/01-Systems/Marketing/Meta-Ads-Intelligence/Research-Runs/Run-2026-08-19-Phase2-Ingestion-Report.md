---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase2-expert-corpus/INGESTION-REPORT.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase2-expert-corpus/INGESTION-REPORT.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/research-run
  - discipline-rift
aliases:
  - "Phase 2 ingestion report"
---

# Phase 2 Ingestion — Completion Report

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase2-expert-corpus/INGESTION-REPORT.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Date:** 2026-08-19
**Scope:** claim extraction from the Phase 2 corpus into `knowledge/experts/`, following `ads-meta-intel-ingest/SKILL.md`.
**Authorisation:** the operator approved the Phase 1 panel and chose the broad scope — full expert profiles, 8-12 claims each, with honest labelling where a claim maps to no open research question.

---

## 1. Numbers

| | |
|---|---|
| Sources processed | **43** |
| Sources skipped (already indexed) | **1** |
| Claims extracted | **95** |
| Expert files written | **6 new**, **5 appended** |
| Sources index | 14 → **57** records |
| Claims on file (all time) | 51 → **146** |
| Watchlist | 11 → **16** experts |

### Per expert

| Expert | Sources | Claims | Undated sources | File |
|---|---|---|---|---|
| Ralph Burns | 8 | 13 | 6 | new |
| Sam Tomlinson | 4 | 12 | 0 | new |
| Taylor Holiday | 6 | 11 | 0 | new |
| Dara Denney | 4 | 10 | 0 | new |
| Andrew Faris | 4 | 9 | 0 | new |
| Jon Loomer | 3 | 8 | 1 | appended |
| Nick Theriot | 3 | 8 | 0 | appended |
| Barry Hott | 2 | 6 | 2 | new |
| Andrew Foxwell | 4 | 6 | 0 | appended |
| Sam Piliero | 2 | 6 | 0 | appended |
| Ben Heath | 3 | 6 | 0 | appended (capped) |

**Skipped as already indexed:** `youtube.com/watch?v=FCc0Nl1Ivxw` (Sam Piliero, "The NEW BEST Facebook Ads Campaign Structure for 2026") — processed 2026-08-13, raw transcript on file. Not re-processed; used only to confirm his architecture is unchanged eight months on.

**Zero-claim sources (a legitimate outcome, recorded):** 2 — `foxwelldigital.com/blog/why-your-meta-ads-are-failing-and-its-not-metas-fault` and `youtube.com/watch?v=T2atKNvRVmo` (CTC service description).

**Retrieval method:** Apify for everything (YouTube transcripts, blog/podcast crawls). Native WebFetch was used once, to verify that hottgrowth.com publishes no dates. **Apify Actors used:** `grow_media/youtube-channel-video-scraper`, `supreme_coder/youtube-transcript-scraper`, `starvibe/youtube-video-transcript`, `apify/website-content-crawler`. Total cost stayed inside the free tier.

---

## 2. Research-question coverage

Question IDs attached across the 43 sources (a source may inform several):

`D1` 15 · `G2` 14 · `C1` 10 · `E1` 9 · `F1` 9 · `D2` 6 · `D3` 6 · `C4` 5 · `E2` 5 · `C3` 4 · `A3` 3 · `E3` 3 · `D4` 3 · `B1` 3 · `B2` 3 · `B3` 2 · `G1` 2 · `A2` 2 · `S2` 2 · `S1` 1

**5 sources carry `research_question_ids: []` with `question_link_origin: none`.** Those are the honest cases the operator authorised: material that is genuinely actionable (bid-strategy mechanics, per-product cost caps, diminishing returns) but informs no currently open question. They are recorded rather than force-mapped.

**Question-mapping origin:** all Phase 2 sources are `prospective` — the corpus was retrieved to serve this panel, and claims were mapped to questions they materially inform. The **subset invariant holds**: every claim's IDs are a subset of its source's.

---

## 3. Evidence quality — the honest summary

**`evidence_strength` distribution is poor, and that is the finding.** Across 95 claims: a handful reach `moderate`, the large majority are `weak` or `none`. Only four bodies of work in the entire panel present anything resembling a study — Common Thread Collective's cost-control and incrementality work, Foxwell's incrementality gradient, Jon Loomer's own-account value-rules test, and Sam Tomlinson's worked arithmetic.

Everything else is experience asserted without data. That is not a defect of the extraction; it is what the source material contains. **The panel's median claim would not survive a demand for evidence, and the corpus now says so on every claim rather than smoothing it over.**

`platform_validation_status` is **`UNVALIDATED` on all 95** — no exceptions, per Step 5.

### Commercial interests recorded on-claim
Motion (Reza Khadjavi via Perpetual Traffic; Dara Denney is Motion's Chief Evangelist), Marpipe (Denney sponsor), a measurement vendor guest on Andrew Faris's show, Tier 11's own Data Suite, and Foxwell's paid membership. Each is named in the `evidence_basis_details` of the claim it touches.

### Independence clusters — agreement is not corroboration
- **ctc**: Taylor Holiday ↔ Andrew Faris (Faris is CTC's former head of strategy; mutual guests).
- **tier-11**: Ralph Burns + John Moran + Ricardo Pouwels are one brand talking to itself.
- **foxwell**: Andrew Foxwell ↔ Courtney Fritts.
- Independent: Tomlinson, Loomer, Theriot, Piliero, Heath, Hott, Denney.

---

## 4. Corrections made during this run

1. **`UNDATED` tier added to the corpus.** 72 documents had been tiered `CURRENT` on the strength of an HTTP `Last-Modified` header, which is a server timestamp, not a publication date. The normalizer was corrected so a Last-Modified value can never produce a recency tier. Affected: all of Barry Hott (30), most of Ralph Burns (28), some Jon Loomer (14).
2. **Barry Hott's recency claim withdrawn.** Verified by direct fetch that hottgrowth.com publishes no dates at all. His entire contribution is quarantined as UNDATED and cannot support any statement about current Meta behaviour.
3. **A Phase 1 flag closed.** jonloomer.com returns 403 to WebFetch, which is why Phase 1 could not verify his dates first-hand. The Apify crawl reached the site: **his 2026 cadence is confirmed from his own site**, 119 documents inside the recency window.

---

## 5. Answers to the skill's two mandatory questions

### Q1 — Did this ingest produce at least one MATERIAL claim advancing a target research question? **YES.**

The four that matter most:

1. **Sam Tomlinson's learning-phase arithmetic** (B1/B2) — target CPA × required events versus actual budget, worked on a real account. DR can run this calculation today with numbers it already has, and it settles that the historical budget cannot produce stable delivery regardless of what the registration cost turns out to be.
2. **Phil Kiel's audience-overlap mechanism** via Andrew Faris (C1) — splitting into many campaigns buys overlap, not reach. C1 previously rested on the *absence* of a reason to split; it now has a positive mechanism, and one that bites harder for a small geo-bounded audience than for the accounts he audits.
3. **Jon Loomer's value-rules test** (A3) — a lead-gen account where bidding down on a low-quality age band moved its share of spend from 45% to under 2%, after a hard restriction had failed. A3 asked for a concrete, obtainable quality safeguard; this is the first practitioner-demonstrated one, and it does not touch child data.
4. **Ben Heath on multi-location local businesses** (E3) — start bundled in one campaign, separate later. E3 previously had **no practitioner evidence at all** in the local lane; this is an operator whose agency has built both versions reaching the same answer.

### Q2 — How many material claims are platform-checkable?

Roughly **20 of 95** touch a platform mechanism a validation pass could resolve against `knowledge/official-meta/`. The highest-value ones:

- Loomer's counts: detailed targeting is a suggestion under 11 performance goals, lookalikes under 9.
- Piliero: removing an ad-set spending minimum "is not going to reset your learnings" — against `significant-edits.md`, which lists changes to a live ad set as always significant.
- Tier 11 (John Moran): Meta ignores exclusions and reuses them as seed audiences — against Meta's documented Audience *controls*.
- Denney and Heath describe Andromeda/GEM differently, and **neither has been checked**.

The remaining ~75 are outcome, creative or strategy assertions that platform documentation cannot validate and will likely triage to `NOT_APPLICABLE`. **No status was assigned here** — triage belongs to the validation pass.

---

## 6. What this run deliberately did not do

- No `platform_validation_status` other than `UNVALIDATED`.
- No DR recommendation, campaign change, or experiment design.
- No modification of `domains/ads/meta/discipline-rift/`, the DR phase skills, or the Google Ads pipeline.
- No research-question status changed. Several claims bear on questions currently marked `ENOUGH_EVIDENCE`; **none of them reopens a question on its own**, and reopening is a separate, deliberate decision with its own dated rationale.
- No paid or gated material accessed (Foxwell Founders, Power Hitters Club, Disrupter Academy).

---

## 7. Open items, ranked

1. **Run the validation pass** on the ~20 platform-checkable claims. The Piliero learning-reset claim and the two conflicting Andromeda accounts are the priority — the first affects whether a widely-taught system carries a hidden cost, the second is an unresolved contradiction already sitting in this knowledge base.
2. **Date Ralph Burns' episodes.** Six of his eight sources are UNDATED, and he is the panel's only non-ecommerce anchor. Show notes or the podcast feed should carry real dates.
3. **Retrieve Tier 11's non-ecommerce client material.** The service and subscription clients that justified his inclusion did not appear in the episodes retrieved. That, not more DTC case studies, is what would actually inform A1.
4. **Verify Emily Hirsh's 2026 recency.** Still the panel's nearest analogue to a considered, emotional, non-instant purchase decision — and still unverified.
5. **Ben Heath's local/service catalogue.** His multi-location material is the thinnest-covered lane in the panel and he has more of it.
6. **Re-check any numeric figure taken from auto-captions** before it informs a decision. Every transcript-sourced number in this run is flagged but unverified.
