---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/README.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/README.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/research-run
  - discipline-rift
aliases:
  - "YouTube Apify run"
---

# Research run — 2026-08-14 — YouTube practitioner extraction (Apify)

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/README.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Type:** Targeted source acquisition. **NOT a new research wave.** No wave reopened.
**Purpose:** Obtain at most **two** high-value YouTube practitioner sources containing operational
Meta Ads evidence that written sources may not have captured.
**Baseline:** HEAD `3bad2a7`. Waves 1A / 1B / 2A / 2B / 3 unmodified.
**Paid retrieval:** Apify. **Spent: ~$0.13** (see §5).

## What this run did NOT do

Per the run brief §17, this run did **not**: rewrite Wave 1/2/3; modify the DR hypothesis; touch
`output/dr-playbook.md`; touch `knowledge/experts/`; touch `knowledge/research-questions.md`;
change any expert conclusion; declare an operating rule; or touch any live Meta Ads system.
It produced **source evidence for later evaluation**, nothing else.

## Artifacts

| File | Contents |
|---|---|
| `dara-denney-test-creatives-every-budget-transcript.md` | Video 1 — identity, extraction metadata, complete transcript with timestamps |
| `dara-denney-test-creatives-every-budget-evidence.md` | Video 1 — selection rationale, 7-claim evidence map, transferability, contradictions |
| `ben-heath-new-way-test-facebook-ads-post-andromeda-transcript.md` | Video 2 — identity, extraction metadata, complete transcript with timestamps |
| `ben-heath-new-way-test-facebook-ads-post-andromeda-evidence.md` | Video 2 — selection rationale, 7-claim evidence map, transferability, contradictions, **conflict with first-party Meta docs** |

## 1. Discovery (Phase A — metadata only)

**Actor:** `logiover/youtube-search-scraper` — run `iIeFcdM517OHoaIxY`, dataset `LE2nS5MzgKh7f8ZY2`.
Six queries, one run, `type: video`, `sortBy: relevance`, US/en, 6 results per query.
**36 rows returned → 26 unique videos**, inspected by lightweight metadata only (title, URL,
channel, publish age, duration, view count, description snippet). **No comments scraped. No channel
scraped. No related-video crawl. No transcript pulled during discovery.**

Queries used:
1. `Dara Denney creative testing every budget`
2. `Meta ads creative testing low budget 2026`
3. `Facebook ads creative not getting spend ad set`
4. `Meta ads testing and scaling same campaign structure`
5. `Meta ads creative testing ads manager walkthrough`
6. `Facebook ads local business lead gen creative testing`

### Actors evaluated and rejected before discovery

| Actor | Why not used |
|---|---|
| `api-ninja/youtube-search-scraper` | Enforces a **$0.10 minimum charge per run** and a 20-result floor. Three queries would have cost ≥$0.30 — above the project's precedent batch budget for no added evidence. |
| `crawlerbros/youtube-search-scraper` | **Failed**: the Actor rejects `meta.origin: 'MCP'` with a Pydantic enum validation error. Actor-side defect, not fixable from input. Run `0v8Oim78lMdb2Z6Xx`, 0 items. |
| `supreme_coder/youtube-transcript-scraper` | Would have pulled transcripts during *discovery* — violates the two-transcript cap. |

## 2. Selection

| # | Video | Decision |
|---|---|---|
| 1 | **Dara Denney — How to Test Facebook Ads Creatives at Every Budget** (`7knQyPYLmfo`) | **SELECTED.** Named priority candidate; live ad-account walkthrough at three budget tiers; directly answers how methodology changes with budget. |
| 2 | **Ben Heath — The NEW WAY To Test Facebook Ads (Post Andromeda)** (`onFwSud9C2Y`) | **SELECTED.** Independent cluster; most recent source (2026-02-10); post-Andromeda; live Ads Manager walkthrough in a **lead-gen** account; addresses creative starvation, controlled exposure, and creative volume. Passed the duplication test before extraction. |

**Independence clusters after this run:** META FIRST-PARTY · SAM · NICK · LOOMER · FOXWELL
ECOSYSTEM · **DARA DENNEY (new)** · **BEN HEATH (new)**.

## 3. Rejected finalists

| Video | Expert | Reason |
|---|---|---|
| DON'T Use One Facebook Ads Campaign (Do This Instead) (`m7jsPB3qMIU`) | Sam Piliero | `DUPLICATIVE` — Sam is an existing cluster and campaign separation is already covered in Wave 2A. Its contrarian value is real but it re-argues a settled-enough question rather than the open creative-delivery ones. |
| The BEST Facebook Ads Campaign Structure for 2026 (`TIs3ID-9a3o`) | Sam Piliero | `DUPLICATIVE` — same cluster, campaign architecture already covered by Wave 2A. |
| Meta Ads Creative Strategy in 2026: The Full System (`vUbLw80KTpo`) | Blue Sense Digital | `LOWER_VALUE_THAN_SELECTED_VIDEO` — 2h20m; ecommerce-scale oriented; extraction cost/benefit poor against two tighter sources answering the same questions. |
| I Tested 1,000+ Facebook Ads, These 3 Print For Home Service Businesses (`xMt7CMz9yLc`) | Steve Hunsaker | `LOWER_VALUE_THAN_SELECTED_VIDEO` — **highest business-model fit in the pool** (local service, lead gen), but the content is creative *angles*, not testing structure or delivery behaviour. **Best candidate for a future run if the open question shifts to message/offer.** |
| Copy This Meta Ads Testing Strategy for Better Results (`8dJxOaZrK1M`) | Ben Heath | `DUPLICATIVE` — same cluster as the selected Video 2, older, and the post-Andromeda video is the stronger of the two. |
| The BEST Facebook Ad Campaign Structure for 2026 (`13s-G9Uj51A`) | Ben Heath | `DUPLICATIVE` — same cluster; campaign structure already covered. |
| Why Does My Facebook Campaign Only Spend On One Ad? (`dlyS_AizIEQ`) | Ecommerce Alley | `LOWER_VALUE_THAN_SELECTED_VIDEO` — exactly on-topic (unequal spend) but 2:57 long; the same ground is covered with a mechanism in Video 2. |
| Meta Ads in 2026: How Many Creatives Do You Actually Need to Launch? (`1BAn7dDmn6E`) | Motion | `LOWER_VALUE_THAN_SELECTED_VIDEO` — 3:55; vendor-produced. |
| NEW Meta & Facebook Ads Creative Testing Feature Explained (`k1Ie8jBC7mI`) | Dr. Matt Shiver | `DUPLICATIVE` — feature explainer for the native creative testing tool, which the project **already holds first-party** in `official-meta/creative-testing-ab-testing-and-delivery-diagnostics.md` §1. |
| How to CRUSH Meta Ads with a Small Budget in 2026 (`AVjmQfJT9iA`) | LYFE Marketing | `TOO_GENERIC` |
| Meta Ads 2026 Update: Creative Testing Strategy to Scale Faster (`PZJ6pw_xyAE`) | Institute Of Digital Studies | `NO_OPERATIONAL_EVIDENCE` — 5:48, 216 views, feature-announcement framing. |
| Facebook Ads Not Spending? Step-By-Step Fix (`ubl-MFEWxmQ`) | AdAmigo AI | `NO_OPERATIONAL_EVIDENCE` |
| Copy This Facebook Ads Strategy, It'll Blow Up Your Business (`_-y0NZ30VKE`) | Jared Robinson | `TOO_GENERIC` — "copy this / blow up your business" framing, no account context in metadata. |
| HOW TO TEST YOUR FACEBOOK ADS (`KztSubtTZG4`), 10 STRATEGIES TO PROFIT (`_zQajrvXMd0`) | Dara Denney | `OUTDATED` — 6 years old. |
| The 10 Best Creatives to Test on All Facebook Ad Accounts (`MiurhGwirfY`) | Dara Denney | `OUTDATED` — 3 years old, pre-Andromeda by a wide margin. |
| Others (`CCsty8R0UaA`, `KmbEjy0UBT8`, `O_j7X89QApk`, `SUz8X9M-Cmc`, `bxBJrp54LlY`, `KAuxJabBkpA`, `IRyR9PzSnM8`, `Z4YWKO8T_3M`) | various | `LOWER_VALUE_THAN_SELECTED_VIDEO` / off-question (analytics, tier lists, scaling, home-service offers). |

## 4. Extraction

**Actor:** `starvibe/youtube-video-transcript`.

| Video | Run | Dataset | Transcript |
|---|---|---|---|
| Dara Denney `7knQyPYLmfo` | `ikyrKAGH2aM7NlwrK` | `xT5aaEkGr7n0a3yA7` | **COMPLETE** (auto-generated EN, 0.12→1027.28 s of 1026 s) |
| Ben Heath `onFwSud9C2Y` | `HpkeM8QdnjhpZ1VsM` | `Z4w7ByR8SfGgf1u8r` | **COMPLETE** (auto-generated EN, 0→911.4 s of 910 s) |

**Full transcript extractions: 2. Cap respected. No third video extracted.**

Both transcripts are auto-generated. ASR defects are **preserved verbatim and flagged** in each
transcript file rather than reconstructed — including two points in the Dara transcript where the
captions **drop the word naming the budget mode** (ABO is the likely intent from context; the
captions do not contain it, so it is not asserted).

Raw Apify JSON was **not** committed. The transcript files preserve source identity, all useful
metadata, and the complete timestamped transcript; the raw payloads remain retrievable from the
dataset IDs above.

## 5. Cost

| Item | Approx. |
|---|---|
| Discovery — `logiover/youtube-search-scraper`, 12 billed results + start | ~$0.06 |
| Extraction — `starvibe/youtube-video-transcript` × 2 | ~$0.01 |
| Failed run — `crawlerbros`, 0 items | ~$0.03 compute |
| **Total** | **~$0.13** |

Under the project's per-batch precedent ($0.25). Reported as approximate: Apify bills per event and
final settlement may differ slightly.

## 6. Outcome

Both videos add operational evidence the project did not have, and neither is a restatement of the
existing hypothesis set. The strongest single item in the run is **B-3** — Meta's own Ads Manager
interface signalling that a £25/day, 7-day test cannot reliably read a cost-per-lead comparison —
because DR operates roughly an order of magnitude below that budget with a rarer outcome event.

**Recommendation: `BOTH_WORTH_INGESTING`.** Ingestion itself is a separate, later decision and is
**not** performed here.

### Items flagged for a first-party verification pass before informing any DR decision

1. **Similarity-based auction deduplication** (Ben Heath B-1) — `UNVALIDATED`. A mechanism claim
   about Meta delivery that current retrieved documentation does not describe.
2. **Test-variant count** — he says 2–5; first-party documentation on file says **2–7**. Meta
   documentation governs; the conflict is recorded, not resolved.
