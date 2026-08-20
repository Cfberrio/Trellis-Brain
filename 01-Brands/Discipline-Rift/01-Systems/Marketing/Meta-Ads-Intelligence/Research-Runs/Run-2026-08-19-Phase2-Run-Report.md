---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase2-expert-corpus/RUN-REPORT.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase2-expert-corpus/RUN-REPORT.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/research-run
  - discipline-rift
aliases:
  - "Phase 2 run report"
---

# Phase 2 Expert Corpus — Extraction Run Report

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-runs/2026-08-19_phase2-expert-corpus/RUN-REPORT.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Run date:** 2026-08-19
**Scope:** bulk retrieval of the Phase 1 expert panel's public material into a dated, traceable corpus.
**What this run did NOT do:** no claim extraction, no expert files written, no `sources-index.json` mutation, no `experts.yaml` change, no ingestion into `knowledge/experts/`. Claim-level work belongs to `ads-meta-intel-ingest` with its audit and `platform_validation_status` grading, and is gated on human review of this corpus.

---

## 1. What exists now

| Artifact | Path |
|---|---|
| Normalized corpus (1 JSON object per document) | `data/normalized/phase2/corpus.jsonl` |
| Per-expert coverage index | `data/normalized/phase2/index.json` |
| Human-readable manifest (counts, date precision, priority docs) | `data/normalized/phase2/MANIFEST.md` |
| Raw Apify output, unmodified | `data/raw/phase2/youtube/**`, `data/raw/phase2/web/**` |
| Pipeline scripts | `data/raw/phase2/{pull.sh,normalize.py,make_manifest.py}` |

Raw-before-interpretation is preserved: every normalized record is reproducible from the raw dataset files, and every raw file came from a named Apify dataset ID.

**Headline numbers are in `MANIFEST.md`** — it is regenerated from the corpus, so it cannot drift from it. At time of writing: **927 documents / 3,155,618 words** across 11 people — **666 inside the Aug 2025 → Aug 2026 window**, 260 HISTORICAL, 1 quarantined for missing date.

---

## 2. Corpus record schema

```json
{
  "id": "yt:VIDEOID | web:slug",
  "expert": "canonical panel slug",
  "platform": "youtube | web",
  "url": "source URL",
  "title": "...",
  "date": "YYYY-MM-DD | null",
  "date_precision": "exact | month | server-modified | null",
  "tier": "CURRENT | HISTORICAL | NO_DATE",
  "text": "full transcript or full article markdown",
  "word_count": 0,
  "duration_s": null,
  "views": null,
  "description": "...",
  "spend_level": null,
  "business_context": null,
  "extracted_at": "YYYY-MM-DD"
}
```

`spend_level` and `business_context` are deliberately `null` on every record. They are **claim-level** fields and must be filled from what the source actually says at ingestion — never inferred from who the speaker is. This is domain Rule 2 in `config/experts.yaml`.

`tier` implements the recency rule: `CURRENT` = published 2025-08-01 → 2026-08-31, `HISTORICAL` = older, `NO_DATE` = quarantined and not ingestible.

---

## 3. Method

**Discovery/metadata → transcripts → normalize.** Three stages, because no single Actor gave both reliable publication dates and full text.

1. **YouTube channel index** — `grow_media/youtube-channel-video-scraper`. Provides the authoritative `date`, title, description, views, duration per video. This is the only source of publisher-declared dates for video.
2. **YouTube transcripts** — `supreme_coder/youtube-transcript-scraper` (channel URL expanded into videos). Returns transcript text but *no publication date*, so records are joined to stage 1 on `videoId`.
3. **Web/blog/podcast pages** — `apify/website-content-crawler` (cheerio; playwright only where needed). Returns markdown plus JSON-LD/OpenGraph metadata, which is where article dates come from.
4. **Normalization** — `normalize.py` joins, deduplicates by URL, extracts dates, assigns tier, and writes the corpus. Actor-specific field names never reach the corpus (domain rule: normalize at the boundary so swapping Actors breaks nothing downstream).

Datasets were downloaded to disk with `curl` against the public dataset endpoint rather than read through the MCP tool, so full transcripts never entered the model context. Cost of the whole run stayed inside the Apify free tier.

---

## 4. Limits hit, and how they were handled

| Limit | Effect | Response |
|---|---|---|
| `starvibe/youtube-video-transcript` free tier caps ~50 transcripts/day | Blocked after Nick Theriot (40) + Dara Denney (8) | Switched to `supreme_coder/youtube-transcript-scraper` (credit-based, no daily cap) |
| Apify account memory ceiling 16 GB across concurrent runs | Crawler launches rejected | Ran crawlers at 1–2 GB, staggered |
| Transcript Actor OOM at default memory (exit 137) | First 6 transcript runs died partway | Re-ran at 4 GB; recovered |
| `jonloomer.com` returns 403 to WebFetch | Phase 1 could not verify his post dates first-hand | Crawled via Apify proxy + sitemap start URLs — **Phase 1's open flag is now closed**: his 2026 cadence is confirmed from his own site |
| Blog/podcast pagination not followed by default | Perpetual Traffic and Jon Loomer initially returned <10 pages | Explicit `page/N` and sitemap start URLs |
| Some sites publish no machine-readable date | Would have quarantined ~100 Sam Tomlinson issues | Added fallbacks with explicit precision labels (see below) |

---

## 5. Known weaknesses in this corpus — read before ingesting

1. **Not every date is publisher-declared.** `date_precision` records which is which. `month` (inferred from WordPress media paths) and `server-modified` (HTTP Last-Modified — an upper bound, not a publication date) must be re-verified before any claim leans on recency. Only `exact` is safe for recency arguments.
2. **Transcripts are auto-generated captions.** Numbers spoken aloud ("three to two to two", "eight ROAS") are transcription-error-prone. Any numeric claim pulled from a video must be verified against the video itself before ingestion — do not trust a figure that exists only in a caption.
3. **Coverage is uneven by design and by accident.** Foxwell's YouTube is nearly dormant (his output is the blog — captured). Andrew Faris and Taylor Holiday are audio-first, so their corpus is transcript-only. Barry Hott's site is short-form; his word count is genuinely small, not truncated.
4. **HISTORICAL is large for Jon Loomer** (~110 docs back to 2011) because his site archive crawled cleanly. That is fine as background but must not be used to describe current platform behavior — his own 2026 posts document how much has changed.
5. **Channel-level extraction pulled some off-topic videos.** Not every document is about Meta Ads. Topic filtering happens at ingestion, not here.
6. **No paid/gated material was accessed** — Foxwell Founders, Power Hitters Club, Disrupter Academy. Their absence is a real gap in the corpus, not an oversight to fix by other means.
7. **Panel independence still applies.** These people appear on each other's podcasts. Agreement between them is weak evidence (domain Rule 4).

---

## 6. Gaps not closed by this run

- **Local service / education / enrollment practitioners** — still the panel's weakest lane, exactly as flagged in Phase 1. Nothing in this corpus fixes it. Ralph Burns' Tier 11 material is the closest available analogue.
- **Emily Hirsh** — Phase 1 alternate whose 2026 recency was unverified. Not extracted; the verification decision is still open.
- **Charley Tichenor / Savannah Sanchez / Nima Gardideh** — alternates, not extracted. Tichenor's method material is largely gated.
- **X/LinkedIn long-form** — not extracted. Both need authenticated scraping; deferred deliberately.

---

## 7. What should happen next (decisions, not work already done)

1. **Human review of the panel and this corpus** — Phase 1's approval question was never answered by a human. Nothing here should be ingested as claims until it is.
2. **Topic filter + priority slice.** `MANIFEST.md` lists the 25 longest CURRENT documents as a starting extraction queue. A topic filter (structure / creative / measurement / lead-gen) should be applied before claim extraction so effort lands on relevant documents.
3. **Claim extraction runs through `ads-meta-intel-ingest`**, not through a new pipeline — one source at a time, each claim carrying `spend_level`, `business_context`, `evidence_basis`, `platform_validation_status`, and `research_question_ids` tied to `knowledge/research-questions.md`.
4. **Ben Heath stays capped.** The 2026-08-14 audit ingested 2 of 9 audited claims. Nothing in this run changes that; his volume is now the largest in the corpus, which makes the cap more important, not less.

---

## 8. Traceability

Every raw file is named for its source and lists its item count in `MANIFEST.md`. Apify dataset IDs used in this run are recorded in `data/raw/phase2/{poller*.sh,pull.sh}` invocation history and in each raw filename's provenance below:

- YouTube indexes: `data/raw/phase2/youtube/_index/*.json`
- YouTube transcripts: `data/raw/phase2/youtube/<expert>/transcripts*.json`
- Web crawls: `data/raw/phase2/web/<source>*.json`

Re-running `normalize.py` regenerates the corpus deterministically from these files.
