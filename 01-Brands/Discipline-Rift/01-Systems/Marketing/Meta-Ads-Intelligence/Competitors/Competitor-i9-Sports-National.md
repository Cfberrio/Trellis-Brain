---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/competitors/ads/i9-sports-national.md"
repo_path: domains/ads/meta/intelligence/competitors/ads/i9-sports-national.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/competitor
  - discipline-rift
aliases:
  - "i9 Sports"
---

# i9 Sports (national)

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitors-Index|Competidores — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Patterns|Patrones entre anunciantes]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Ad-Scripting-Playbook|DR Ad Scripting Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/competitors/ads/i9-sports-national.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Captured:               2026-08-13
Scope:                  national
Brand family:           `i9-sports`
Ads analyzed:           39 unique
Ad-count completeness:  39 retrieved this capture; completeness NOT established
Sample status:          unknown
Source run(s):          `jBnYC2JFpBp7eBmPL` / dataset `hVfchRqKFlo1XlDRM`
Raw file(s):            `data/raw/2026-08-13_i9-sports-national_jBnYC2JFpBp7eBmPL_meta-ad-library.json`
Completeness note:      The Actor's full-extraction output carries no completeness signal (`isResultComplete` exists only in count-only mode). Retrieving fewer ads than the cap is not evidence of completeness, so this sample is `unknown`: treat every count here as "at least this many".
Normalized:             `data/normalized/2026-08-13_i9-sports-national.json`

> Longevity figures below are a **PROXY for nothing more than "the advertiser kept running it."** Ad Library publishes no spend, CPA, ROAS, conversions or revenue for these ads, and none is inferred anywhere in this file.

## Caveats

- National corporate page. **Orlando geo-targeting cannot be verified** from Ad Library — Meta publishes no geo targeting for US commercial ads. Treat as directional creative evidence, not local-market evidence.
- Largest creative sample in the watchlist (39 of 99 ads = 39%). Volume is not evidence weight; do not let this advertiser dominate cross-brand patterns.
- The local franchise page (i9 Sports East Orange County FL, id 2523077341091962) ran zero active ads at Task 0 validation — all i9 creative observed lives on this corporate page.
- Task 0 count-only preflight returned `isResultComplete: false` with a floor of ≥39. This sweep retrieved exactly 39 with a limit of 60, so the limit did not bind. Completeness above 39 is still not *proven* by the Actor.
- 22 of 39 ads are DCO (dynamic catalog) creatives whose top-level body is an unrendered template placeholder (`{{product.brand}}`). Hooks for those ads were read from the first catalog card, not from the delivered ad — one interpretation step away from what a parent actually sees.

## Creative inventory

| ad ID | start | days running (PROXY) | format | hook | offer | angle | CTA | landing page | conf |
|---|---|---|---|---|---|---|---|---|---|
| `1008202565137066` | 2026-06-24 | 50 | DCO | i9 Sports Youth Soccer Leagues & Programs | — | fun | Sign up | https://www.i9sports.com/ppc/soccer | medium |
| `1042809224945758` | 2026-06-24 | 50 | DCO | i9 Sports Youth Flag Football Leagues & Programs | — | outcome | Sign up | https://www.i9sports.com/ppc/flag-football | medium |
| `1296206572498680` | 2026-06-24 | 50 | DCO | i9 Sports Youth Soccer Leagues & Programs | — | fun | Sign up | https://www.i9sports.com/ppc/soccer | medium |
| `1478347610711832` | 2026-06-24 | 50 | DCO | i9 Sports Youth Volleyball Leagues & Programs | — | beginner_friendly | Sign up | https://www.i9sports.com/ppc/volleyball | medium |
| `1627175161684817` | 2026-06-24 | 50 | DCO | i9 Sports Youth Basketball Leagues & Programs | — | fun | Sign up | https://www.i9sports.com/ppc/basketball | medium |
| `1682147336423127` | 2026-06-24 | 50 | DCO | Start Your Child’s Sports Journey with i9 Sports | — | fun | Sign up | https://www.i9sports.com/ | medium |
| `1723511738806515` | 2026-06-24 | 50 | DCO | ⚾ Start Your Child’s Sports Journey with i9 Sports T-Ball | — | beginner_friendly | Sign up | https://www.i9sports.com/ppc/baseball | medium |
| `1764964574871289` | 2026-06-24 | 50 | DCO | i9 Sports Youth Flag Football Leagues & Programs | — | outcome | Sign up | https://www.i9sports.com/ppc/flag-football | medium |
| `1909562339705992` | 2026-06-24 | 50 | DCO | ⚾ Start Your Child’s Sports Journey with i9 Sports T-Ball | — | beginner_friendly | Sign up | https://www.i9sports.com/ppc/baseball | medium |
| `2008342500557422` | 2026-06-24 | 50 | DCO | ⚾ Start Your Child’s Sports Journey with i9 Sports T-Ball | — | beginner_friendly | Sign up | https://www.i9sports.com/ppc/baseball | medium |
| `2269556310245647` | 2026-06-24 | 50 | DCO | i9 Sports Youth Basketball Leagues & Programs | — | fun | Sign up | https://www.i9sports.com/ppc/basketball | medium |
| `1550070483189472` | 2026-06-25 | 49 | VIDEO | 🌟 Give Your Child the Best Start with i9 Sports! | — | convenience | Sign up | https://www.i9sports.com/ | high |
| `1828350981881822` | 2026-07-01 | 43 | VIDEO | ⚽ Build Confidence and Skills with i9 Sports Soccer! | — | convenience | Sign up | https://www.i9sports.com/ppc/soccer | high |
| `1931645064209342` | 2026-07-03 | 41 | IMAGE | ⚾ Start Strong with i9 Sports T-Ball! | — | convenience | Sign up | https://www.i9sports.com/ppc/baseball | high |
| `1384778886871607` | 2026-07-04 | 40 | VIDEO | ⚾ Start Strong with i9 Sports T-Ball! | — | convenience | Sign up | https://www.i9sports.com/ppc/baseball | high |
| `2197990800981265` | 2026-07-05 | 39 | VIDEO | 🏀 Elevate Your Game with i9 Sports Basketball! | — | convenience | Sign up | https://www.i9sports.com/ppc/basketball | high |
| `1359401592819201` | 2026-07-13 | 31 | VIDEO | ⚾ Start Strong with i9 Sports T-Ball! | — | convenience | Sign up | https://www.i9sports.com/ppc/baseball | high |
| `1050251531296715` | 2026-07-16 | 28 | DCO | Gains are for the girls | — | identity | Sign up | https://www.i9sports.com/ | medium |
| `1352529347082546` | 2026-07-16 | 28 | DCO | Gains are for the girls | — | identity | Sign up | https://www.i9sports.com/ | medium |
| `1360254345436709` | 2026-07-16 | 28 | DCO | Gains are for the girls | — | identity | Sign up | https://www.i9sports.com/ | medium |
| `1733632164618601` | 2026-07-16 | 28 | DCO | Gains are for the girls | — | identity | Sign up | https://www.i9sports.com/ | medium |
| `2082372338984246` | 2026-07-16 | 28 | DCO | Gains are for the girls | — | identity | Sign up | https://www.i9sports.com/ | medium |
| `1048981687479652` | 2026-07-17 | 27 | DCO | Better Together! | $10 credit per referred family | price | See details | https://wptest.i9sports.com/refer-a-friend | medium |
| `1050086220798262` | 2026-07-17 | 27 | DCO | Better Together! | $10 credit per referred family | price | See details | https://wptest.i9sports.com/refer-a-friend | medium |
| `1706459393737451` | 2026-07-17 | 27 | DCO | Better Together! | $10 credit per referred family | price | See details | https://wptest.i9sports.com/refer-a-friend | medium |
| `1914407569251537` | 2026-07-17 | 27 | IMAGE | Empower girls to achieve their dreams! | — | identity | Sign up | https://www.i9sports.com/ | high |
| `2267654307398272` | 2026-07-17 | 27 | IMAGE | Empower girls to achieve their dreams! | — | identity | Sign up | https://www.i9sports.com/ | high |
| `918860043798394` | 2026-07-17 | 27 | DCO | Better Together! | $10 credit per referred family | price | See details | https://wptest.i9sports.com/refer-a-friend | medium |
| `934616286321912` | 2026-07-17 | 27 | DCO | Better Together! | $10 credit per referred family | price | See details | https://wptest.i9sports.com/refer-a-friend | medium |
| `986398034381055` | 2026-07-17 | 27 | DCO | Better Together! | $10 credit per referred family | price | See details | https://wptest.i9sports.com/refer-a-friend | medium |
| `1622745849637650` | 2026-07-20 | 24 | IMAGE | Empower girls to achieve their dreams! | — | identity | Sign up | https://www.i9sports.com/ | high |
| `3124522577751153` | 2026-07-27 | 17 | IMAGE | Empower girls to achieve their dreams! | — | identity | Sign up | https://www.i9sports.com/ | high |
| `4516242701993442` | 2026-07-27 | 17 | VIDEO | 🏈 Master Flag Football with i9 Sports! | — | convenience | Sign up | https://www.i9sports.com/ppc/flag-football | high |
| `1356387525987629` | 2026-07-31 | 13 | VIDEO | 🌟 Give Your Child the Best Start with i9 Sports! | — | convenience | Sign up | https://www.i9sports.com/ | high |
| `1611224800556359` | 2026-08-03 | 10 | VIDEO | ⚽ Build Confidence and Skills with i9 Sports Soccer! | — | convenience | Sign up | https://www.i9sports.com/ppc/soccer | high |
| `3410836212424308` | 2026-08-03 | 10 | IMAGE | ⚾ Start Strong with i9 Sports T-Ball! | — | convenience | Sign up | https://www.i9sports.com/ppc/baseball | high |
| `1595562072166177` | 2026-08-04 | 9 | IMAGE | Empower girls to achieve their dreams! | — | identity | Sign up | https://www.i9sports.com/ | high |
| `1041681065271115` | 2026-08-09 | 4 | IMAGE | 🏀 Elevate Your Game with i9 Sports Basketball! | — | convenience | Sign up | https://www.i9sports.com/ppc/basketball | high |
| `2123015871614010` | 2026-08-10 | 3 | IMAGE | Empower girls to achieve their dreams! | — | identity | Sign up | https://www.i9sports.com/ | high |

## Repeated patterns inside this advertiser

**Sport-segmented creative + matching landing page.** Separate creative families for soccer, basketball, T-ball, flag football and volleyball, each pointing at its own `/ppc/<sport>` landing page (e.g. `1296206572498680` soccer, `1627175161684817` basketball, `1723511738806515` T-ball, `1042809224945758` flag football, `1478347610711832` volleyball). Message-to-destination match is deliberate, not incidental.

**Explicit age band in nearly every ad.** "ages 3–14", "ages 3–6", "kids 5–14", "ages 4–14", "ages 7–14" — the qualifying age is stated in the copy rather than left to targeting.

**No-pressure framing repeated across sports** (29/39 ads carry a fun/no-pressure signal): "pressure-free environment", "No pressure programs—just fun", "No pressure, just play".

**One CTA dominates.** `Sign up` on 33/39; the 6 exceptions are the referral ads, which use `See details`.

**A distinct girls-focused creative family** (11 ads): "Girls Belong Here" / "Gains are for the girls" — identity-led rather than sport-led.

**A referral-offer family** (6 ads, `$10 credit per referred family`) — the only explicit incentive this advertiser runs.

**Observable defect worth noting:** all 6 referral ads point at `https://wptest.i9sports.com/refer-a-friend` — a staging/test hostname running in live creative. Recorded as an observation, not a strategic inference.

## Longest-running creatives

**LONGEVITY PROXY — NOT PERFORMANCE PROOF.** These are ranked for inspection only. They are not winners, best ads, or top performers; no performance evidence exists for any of them.

| ad ID | days running (proxy) | start | format | hook | angle |
|---|---|---|---|---|---|
| `1008202565137066` | 50 | 2026-06-24 | DCO | i9 Sports Youth Soccer Leagues & Programs | fun |
| `1042809224945758` | 50 | 2026-06-24 | DCO | i9 Sports Youth Flag Football Leagues & Programs | outcome |
| `1296206572498680` | 50 | 2026-06-24 | DCO | i9 Sports Youth Soccer Leagues & Programs | fun |
| `1478347610711832` | 50 | 2026-06-24 | DCO | i9 Sports Youth Volleyball Leagues & Programs | beginner_friendly |
| `1627175161684817` | 50 | 2026-06-24 | DCO | i9 Sports Youth Basketball Leagues & Programs | fun |

## Potential relevance to DR

- **Observable:** sport-segmented creative paired with a sport-specific landing page. **Why it may matter to DR:** DR sells distinct sports seasons and currently has the same structural option. **Transferability limit:** i9 is national with franchise-wide catalog infrastructure; a DR version would be a small manual set, and nothing here shows whether the split outperformed a generic ad.
- **Observable:** the qualifying age band is written into the copy on nearly every ad. **Why:** DR's 6–12 band is a hard qualifier and mis-qualified clicks cost real budget on a small account. **Limit:** i9's band (3–14) is wider than DR's; the tactic transfers, the number does not.
- **Observable:** explicit no-pressure/fun framing repeated across every sport family. **Why:** DR is beginner-friendly and fun-first by definition, and this is the same parent. **Limit:** i9's delivery is weekend leagues at venues, not on-campus after-school. DR's version must not borrow league framing.

*No recommendation is made here. These are observations for later evaluation against DR's own performance data.*
