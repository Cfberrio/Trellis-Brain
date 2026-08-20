---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/CLAUDE.md"
repo_path: domains/ads/meta/intelligence/CLAUDE.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/method
  - discipline-rift
aliases:
  - "Meta Ads Operating Rules"
  - "Reglas de operación Meta Ads Intelligence"
---

# Reglas de operación — Meta Ads Intelligence

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-System-Plan|Plan del sistema]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-How-To-Use|Cómo usar el sistema]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-Structure-Full-Method|Método completo de estructura DR]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitors-Index|Competidores — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/CLAUDE.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

## Mission
This domain looks **outward**: what other advertisers run on Meta, what Meta officially documents, what credible public experts claim.

`domains/ads/meta/discipline-rift/` looks **inward**: DR's own account, its real numbers, its diagnostics and rehab SOPs. Two domains on purpose. They meet at one file — `output/dr-playbook.md`, later consumed as optional input by phase 3.

Intelligence exists to improve decisions, not to accumulate research. The only outputs that count as finished work: creative decisions, campaign hypotheses, runnable experiments, and DR recommendations backed by traceable evidence.

If this system only produces reading material, it failed.

## The two halves of project success
External research is **Half 1**. It ends in DR hypotheses, never in proof.

**Half 2** — not yet built — validates and corrects those hypotheses with DR's own results, on three axes that must each be checked, never assumed:

- **AUDIENCE** — are the ads reaching the right people?
- **MESSAGE** — is the creative producing the intended response from that audience?
- **STRUCTURE** — is the architecture behaving as the research predicted?

The loop: research → DR hypothesis → campaign → real DR data → audience + message + structure diagnosis → controlled change → DR test result → better next decision.

The project is not complete when a playbook exists. It is complete when a repeatable system checks all three axes against DR's own data and improves the campaigns over time. Domain split for Half 2: `intelligence/` holds external knowledge and transferable hypotheses; `discipline-rift/` holds actual account state, experiments, results and operating rules. An explicit bridge will connect them later — it is not built yet, and nothing here may modify the DR domain in anticipation of it.

## How to describe DR in research
For research purposes DR is: **a local youth-sports registration business — constrained geography (Orlando), parent purchasers, child participants (6–12), relatively low advertising volume, final desired outcome = paid season registration.**

Do **not** categorize DR as "lead-gen" (or "ecommerce", or anything else that presupposes a Meta objective). Which campaign objective and optimization event fit DR — Lead, a sales/registration conversion, or an intermediate event — is an open research question in `knowledge/research-questions.md`, not a premise. Baking an objective label into the methodology pre-answers the question the research exists to settle.

## Domain boundaries
Do not modify, unless a later approved integration task explicitly requires it:
- `domains/ads/meta/discipline-rift/`
- `ads-meta-dr-phase1-extract`, `ads-meta-dr-phase2-diagnostic`, `ads-meta-dr-phase3-campaign-rehab`
- `google-ads-phase*` skills

Do not create: duplicate DR context, a database, Anthropic API infrastructure, TypeScript ingestion pipelines, or scraping infrastructure beyond what the Apify MCP already provides.

Claude Code is the orchestrator. There is no second system.

Everything new lives under `domains/ads/meta/intelligence/` plus the intel skill files.

## Source hierarchy
1. Actual DR performance data
2. Official Meta documentation
3. Observable competitor behavior in Meta Ad Library
4. Agreement among multiple independent experts
5. Single expert opinion

This is **not** simplistic voting. Different evidence answers different questions, and a lower tier is not automatically overruled — it is answering something the higher tier does not address.

Competitor creative shows observable messaging behavior. It cannot override DR's own conversion data. Meta documentation defines what the platform does; it does not tell you what converts Orlando parents. Expert opinion generates hypotheses; it does not settle them.

When two tiers genuinely conflict on the same question, state the conflict explicitly. Do not resolve it silently in favor of the higher tier.

## Knowledge levels
Every material statement in this system belongs to exactly one level. Never let a statement drift upward silently.

| Level | What it is | Example |
|---|---|---|
| **PLATFORM FACT** | Current first-party Meta behavior/documentation, dated and retrieved first-hand | Meta lists "Adding a new ad to your ad set" as an always-significant edit |
| **EXTERNAL PRACTITIONER CLAIM** | A recommendation or reported result from an outside practitioner. May be supported, conflicting, outdated, unvalidated; strongly or weakly evidenced (`evidence_basis` / `evidence_strength`). Never automatically a DR recommendation | "Run one CBO for testing and scaling" |
| **COMPETITOR OBSERVATION** | Something visibly observable in public competitor advertising. Private performance is never inferred from it | Soccer Shots Orlando uses school-location framing |
| **DR HYPOTHESIS** | A belief we intend to test for DR, derived from any mix of the above plus business logic. A hypothesis is not a result | "Naming the child's school may improve qualified parent response" |
| **DR TEST RESULT** | Something actually observed from a defined DR experiment or campaign observation. Must retain: date, campaign/context, variable tested, result, sample/volume, metric, limitations, and whether the read was directional or sufficiently strong | — |
| **DR PROVEN OPERATING RULE** | Highest internal level. Requires sufficiently strong or repeated DR evidence to serve as an operating default. **Never promoted after one small test.** Remains revisable when conditions change | — |

Rules that keep the levels honest:

- External practitioner evidence — however specific — is **not proof for DR**. A `self_reported_case_study` stays self-reported unless independently verified.
- **PLATFORM FACT, EXTERNAL PRACTITIONER CLAIM, and COMPETITOR OBSERVATION are parallel evidence inputs, not rungs of a ladder.** Nothing climbs from one into another. The only promotion path in this system is DR HYPOTHESIS → DR TEST RESULT → DR PROVEN OPERATING RULE, each step backed by recorded DR evidence. No level-skipping.
- Demotion is normal: a proven rule contradicted by newer DR evidence or changed platform behavior gets demoted, with the date and the reason.
- **`platform_validation_status`** (`UNVALIDATED` / `SUPPORTED` / `PARTIALLY_SUPPORTED` / `CONFLICTING` / `OUTDATED` / `INSUFFICIENT_EVIDENCE` / `NOT_APPLICABLE`) grades exactly one dimension of an external claim: whether **current first-party Meta documentation** supports its platform/mechanism component. Authoritative definitions live in `ads-meta-intel-ingest/SKILL.md §Step 5`. `NOT_APPLICABLE` marks outcome/creative/strategy assertions platform documentation cannot validate. The field lives inside the EXTERNAL PRACTITIONER CLAIM level and promotes nothing.
- An external claim has three **separate** assessment dimensions, never merged: platform validation (vs Meta docs), cross-source corroboration/conflict (vs other practitioners, recorded at synthesis), and transferability (vs DR's context). A DR test result **never mutates any of them** — "practitioner proposed X; Meta could not validate it; DR later observed Y" stays exactly that.
- Field history: `platform_validation_status` was named `validation_status` before 2026-08-13; renamed because the old definition ("Meta documentation **or DR data** backs it") collapsed the platform layer and the DR layer into one word.

## Numeric threshold rule
**Never force an exact numerical threshold when credible evidence does not establish one.** A research conclusion may instead be: a range; a conditional rule; an observable revisit trigger; a qualitative minimum condition; or "no defensible numeric threshold found." Exact numbers are allowed only when supported by traceable evidence. A stop condition asking for a threshold is satisfied by any of these honest forms — it is never a mandate to manufacture false precision, and practitioner folklore never becomes a number.

## Principle vs implementation
A practitioner claim usually bundles a mechanism and a tactic. Evaluate them separately, always:

- **Principle** — the underlying mechanism ("adding creative to a live ad set resets its learning").
- **Implementation** — the tactic built on it ("therefore launch a new ad set per creative round").

A principle can transfer to DR while its implementation cannot — this has been the single most common outcome so far. Claims carry `principle_transfers` and `implementation_transfers` (`yes | partial | no | untested`); older claims carry the distinction in `reason` prose and are not rewritten.

## Evidence saturation — the stopping rule for research
There is **no source quota**. Never adopt a rule like "every question needs 2 sources."

A question is sufficiently researched when **additional credible independent evidence is unlikely to materially change the decision.** Some questions close on strong first-party Meta documentation plus one highly comparable practitioner case and no credible contradiction. Others need 3, 4 or more independent sources because practitioners materially disagree. Source count is evidence *context*, not the stopping rule.

Each material question's own `stop_condition` in `knowledge/research-questions.md` states what saturation looks like for that question. Research is driven by that file — by questions, not by gurus.

## Source selection for practitioner research
**Relevance first.** Prefer contexts that share DR's constraints: local services, appointment/registration businesses, education/enrichment, youth activities, memberships, geo-constrained acquisition, low conversion volume, constrained budgets. Do not require a perfect match — a high-quality ecommerce source can still teach transferable Meta mechanics; its claims simply carry the transferability discount they already get.

**Evidence over fame.** Follower count and agency fame rank nothing. Prefer sources that explain what they did and why, state account context (business type, spend, volume), show evidence where possible, and expose enough detail to evaluate transferability. `evidence_basis` exists to make this rankable.

**Recency.** Prefer current material. Older content that is uniquely valuable may be stored — dated, with the relevant Meta behavior re-verified against `knowledge/official-meta/` before it informs any decision.

**Independence.** People repeating the same framework are not independent confirmations. Record known relationships and shared discourse (podcast circuits, mutual citation) when identified; weight agreement accordingly.

## Settled defaults — do not spend research on these
**Placements.** Current first-party Meta guidance recommends Advantage+ placements (staying opted into all placements) as the default. Treat that default as established. This does **not** mean a placement can never be excluded later — DR's own evidence, changed platform guidance, or a material specific constraint can reopen it. But "should we use all placements by default?" gets no further practitioner-research budget. Recorded with rationale in `knowledge/research-questions.md`.

## Tool routing
Native tools first.

- **WebSearch** — discovery, public-source identification, advertiser identity checks.
- **WebFetch** — articles, landing pages, official Meta documentation.
- **Apify MCP** — only when native tools cannot reliably retrieve what is needed. In practice: Meta Ad Library, Instagram Reel extraction/transcription, YouTube subtitles/transcripts.

Cost rule: do not spend Apify credit on anything native tools retrieve adequately.

## Apify operating principles
- Verify the **current** Actor and input schema before every execution. Never assume a schema from memory or from a previous run.
- Preserve raw evidence before interpreting it. Raw dump first, analysis second.
- Actor-specific field names must never leak downstream. Normalize to this domain's schema at the boundary, so swapping Actors does not break anything built on top.
- Normalize before analysis.
- Preferred Meta Ad Library Actor for Sprint 1: `apify/facebook-ads-scraper`.
- Use a fallback Actor only when required information cannot be reliably obtained from the preferred one.

The detailed sequence of MCP calls belongs in `ads-meta-intel-adlib/SKILL.md`, not here.

## Competitor semantics
Distinguish two things that are easy to conflate:

- **Business competitor** — competes with DR for the same Orlando parent's decision, budget, and after-school slot.
- **Advertising intelligence source** — an advertiser whose live creative is worth learning from.

A national advertiser can be a strong intelligence source without being a verified Orlando advertising competitor. Presence in the watchlist means the second thing, never automatically the first.

`brand_family` governs independent-brand consensus. Two advertisers sharing a `brand_family`:
- may be compared against each other
- may support a national-vs-local comparison
- count as **one** independent brand in cross-brand consensus

Specifically: KidStrong HQ and KidStrong Windermere are separate advertisers and one brand. Them agreeing is one brand talking to itself, not consensus.

## Local vs national evidence
**National advertisers.** Their creative may be analyzed. Their Orlando targeting must not be assumed — Meta exposes no geo targeting for US commercial ads. Their observed creative is directional creative evidence, not local-market delivery evidence.

**Local Orlando advertisers.** Stronger evidence about messaging used by an advertiser operating in DR's actual market. Still reveals nothing about targeting, spend, CPA, ROAS, or conversions unless explicitly published.

## Meta Ad Library evidence rules
Allowed observations: advertiser; active/inactive status when provided; ad creative; copy; opening hook; visible offer; CTA; media format; landing destination; start date when supplied; observable longevity; visible active variations.

Forbidden inference unless explicitly supported by the data: spend, CPA, ROAS, conversions, revenue, profitability, targeting geography, audience composition, budget, campaign structure, ad-set structure, "winning ad".

Never call an active ad a winner.

## Longevity
Longevity is a **prioritization proxy**. It is not performance proof.

A long-running ad earns closer inspection because the advertiser has kept choosing to run it. That is the whole of the claim.

Longevity alone establishes nothing about profit, CPA, conversion rate, ROAS, or spend. Every downstream output using longevity must label it as a proxy at the point of use — not once in a footnote.

## Current watchlist semantics
Read `config/competitors.yaml`. Do not hardcode the advertiser list here; the file is the single source of truth and it changes.

Section meanings:
- `competitors:` — active advertisers used for intelligence extraction
- `inactive_reference:` — strong business-model references with zero active ads at latest validation; kept as business context, not scraped
- `unresolved:` — identity or Ad Library presence not sufficiently established

Revalidate advertiser activity before any future sweep. Counts in the file are point-in-time.

Never silently move an entry from `unresolved:` into active or inactive. Resolution requires a new verification, recorded.

## Dates and evidence freshness
Every material observation preserves `captured_at`, and where available `published_at`, `start_date`, `first_seen`, `last_verified_at`.

A point-in-time ad count must never later be presented as a live value.

No undated strategy enters the playbook.

## Evidence traceability
Every material claim traces to something checkable: advertiser, source URL, Meta documentation URL, Actor run ID, dataset ID, raw file, capture date.

No traceable source, no material claim. If something is unknown, it is `null` — not a plausible guess.

## DR context
Do not create `config/dr-context.md`. A second DR context desynchronizes from the first, guaranteed.

Always read `domains/ads/meta/discipline-rift/CLAUDE.md` when adapting intelligence to DR.

Load Obsidian Brand-Core (`Trellis-Brain/01-Brands/Discipline-Rift/00-Brand-Core/`) only when a task genuinely requires deeper brand direction — Avatar, Objections, Positioning. Not by default.

## DR recommendation gate
A proposed recommendation must improve at least one of:
- setup quality
- tracking / signal quality
- learning conditions
- geo accuracy
- placement control
- creative clarity
- offer-message fit

If it improves none of them, leave it out. Interesting is not a criterion.

## Transferability
Never blindly copy into DR: ecommerce strategies, national franchise strategies, competitive youth-sports strategies, elite / high-performance messaging.

DR is local Orlando, parent payer, kids 6–12, beginner-friendly, fun-first, coach-led, on-campus after-school. Its banned language and claim rules live in the DR domain context and are binding on anything this domain proposes.

Every recommendation carries:

```yaml
applicability_to_DR: high | medium | low
modification_required: yes | no
```

## Consensus integrity
Number of ads is not number of brands.

A high-volume advertiser must not dominate consensus because it happens to run more creatives. Consensus operates primarily at independent `brand_family` level, and the count of independent families is stated whenever consensus is claimed.

## Cost discipline
During MVP: **preflight/count → shortlist → full scrape.** Not scrape-everything-then-decide.

No recurring schedules, no webhooks during MVP.

## Current stage
Sprint 1 (competitor sweep), the official Meta base, the expert-ingestion test batch (2 practitioners, 16 claims), and playbook v1 are complete and committed. The evidence model now includes `evidence_basis` / `evidence_strength` and the knowledge levels above.

**Next stage: question-driven practitioner research** — currently **Wave 1A (A1/A2/A3: outcome + signal)**, driven by `knowledge/research-questions.md` under the evidence-saturation rule and its research waves. Wave 1B (B1/B2/B3: volume + budget) is gated on 1A's parameterization gate, because budget cannot be researched before the outcome being purchased is chosen — and 1B evidence may reopen A2/A3.

Ownership split: **`ads-meta-intel-research`** owns discovery — question → discovery → pre-screen → shortlist → saturation decision; **`ads-meta-intel-ingest`** stays ingestion-only and receives shortlisted URLs plus their `research_question_ids`. Every retrieval traces QUESTION → SOURCE → CLAIM.

`research_question_ids` means **the current backlog questions a source or claim materially informs** — not why it happened to be fetched. `question_link_origin` (`prospective` / `retrospective` / `none`) records which case applies, so evidence gathered before a question existed can still answer it. A claim's IDs are always a subset of its source's. Still deferred until the evidence demands them: the full synthesis engine (`ads-meta-intel-playbook` skill, 14-point scoring), contradiction databases, recurring discovery, dashboards, automation, schedules/webhooks. Improve the incoming evidence first; decide the minimum synthesis implementation after the next research batch shows what is actually needed.

## Acceptance criterion
Each stage earns the next only by changing or sharpening at least one concrete DR decision or experiment.

If a stage does not, stop. Do not expand the system merely because the pipeline works technically.
