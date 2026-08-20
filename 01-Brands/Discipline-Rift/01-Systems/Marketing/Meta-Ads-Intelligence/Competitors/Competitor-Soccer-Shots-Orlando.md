---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/competitors/ads/soccer-shots-orlando.md"
repo_path: domains/ads/meta/intelligence/competitors/ads/soccer-shots-orlando.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/competitor
  - discipline-rift
aliases:
  - "Soccer Shots Orlando"
---

# Soccer Shots Orlando (Orlando-local)

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitors-Index|Competidores — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Patterns|Patrones entre anunciantes]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Ad-Scripting-Playbook|DR Ad Scripting Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/competitors/ads/soccer-shots-orlando.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Captured:               2026-08-13
Scope:                  local
Brand family:           `soccer-shots`
Ads analyzed:           4 unique
Ad-count completeness:  4 retrieved this capture; completeness NOT established
Sample status:          unknown
Source run(s):          `8fgtd72HvYhrwf2pE` / dataset `GG288I0eSfj02nq8K` · `kCiWws4pcfiV7RbQy` / dataset `Rs1ZDFupvm5P6SuaI`
Raw file(s):            `data/raw/2026-08-13_soccer-shots-orlando_8fgtd72HvYhrwf2pE_meta-ad-library.json` · `data/raw/2026-08-13_soccer-shots-orlando_kCiWws4pcfiV7RbQy_meta-ad-library.json`
Completeness note:      The Actor's full-extraction output carries no completeness signal (`isResultComplete` exists only in count-only mode). Retrieving fewer ads than the cap is not evidence of completeness, so this sample is `unknown`: treat every count here as "at least this many".
Normalized:             `data/normalized/2026-08-13_soccer-shots-orlando.json`

> Longevity figures below are a **PROXY for nothing more than "the advertiser kept running it."** Ad Library publishes no spend, CPA, ROAS, conversions or revenue for these ads, and none is inferred anywhere in this file.

## Caveats

- Local Orlando territory advertiser and the closest local delivery-model analog to DR that is actually running ads (single-sport, on-campus at schools, coach-led, parent payer).
- Age range is 18 months to 8 years. Overlap with DR's 6–12 band exists only at 6–8. Messaging aimed at toddler/preschool parents does not transfer to DR's core audience.
- **Smallest sample in the watchlist (4 ads).** A single repeated angle here is not a trend. Every claim in this file is a 4-ad claim.
- Identity/extraction note: the numeric page URL recorded in the watchlist (`facebook.com/410250322333195`) and the vanity URL (`facebook.com/soccershotsorlando`) both resolve to page id 410250322333195 and both returned the same 4 ads in this sweep. Two captures exist for that reason; they are deduped to 4 unique ads.
- A second Orlando-area territory (Soccer Shots Orlando South) remains unresolved from Task 0 and was not scraped.

## Creative inventory

| ad ID | start | days running (PROXY) | format | hook | offer | angle | CTA | landing page | conf |
|---|---|---|---|---|---|---|---|---|---|
| `1044491151441513` | 2026-07-07 | 37 | VIDEO | The World Cup has inspired millions of young players to dream big. | early bird pricing | price | Learn more | https://www.ss-osb.soccershots.com/page/class-registration… | high |
| `1349843410626050` | 2026-07-08 | 36 | VIDEO | Soccer excitement is everywhere! | early bird pricing | price | Learn more | https://www.ss-osb.soccershots.com/page/class-registration… | high |
| `1047985764268781` | 2026-08-12 | 1 | VIDEO | Watching the world’s best players compete inspires millions… but the b | — | convenience | Learn more | https://www.ss-osb.soccershots.com/page/class-registration… | high |
| `1066841339622661` | 2026-08-12 | 1 | VIDEO | The excitement of soccer is everywhere… and now it’s your child’s turn | — | beginner_friendly | Learn more | https://www.ss-osb.soccershots.com/page/class-registration… | high |

## Repeated patterns inside this advertiser

**Delivery location is the headline, not a detail.** Two of four ads use the ad title "Soccer at Your Child's School! ⚽️🏫" (`1044491151441513`, `1349843410626050`). This is the only advertiser in the sweep that puts *where the program happens* in the title.

**A topical event hook on all four ads.** Every ad opens on World Cup / world-championship energy: "The World Cup has inspired millions of young players to dream big", "Soccer excitement is everywhere!", "Watching the world's best players compete inspires millions…", "The excitement of soccer is everywhere…".

**Two program lines in one small set.** The two July ads (school-season, progId=25320) and the two August ads (park season, Saturday mornings, progId=25319) run different program framings from the same page.

**Local proof language in the newer pair:** "Join families across Orlando", "📍Played right here in your community".

**Season + early-bird trigger:** "Fall Season Registration Now Open! Early Bird Pricing!" on the July pair.

**Deep program-level destinations** (`ss-osb.soccershots.com/page/class-registration?progId=…`) rather than a homepage — the most specific post-click match in the sweep.

**CTA is `Learn more` on all four** — no hard-convert CTA anywhere in this set.

## Longest-running creatives

**LONGEVITY PROXY — NOT PERFORMANCE PROOF.** These are ranked for inspection only. They are not winners, best ads, or top performers; no performance evidence exists for any of them.

| ad ID | days running (proxy) | start | format | hook | angle |
|---|---|---|---|---|---|
| `1044491151441513` | 37 | 2026-07-07 | VIDEO | The World Cup has inspired millions of young players to dream big. | price |
| `1349843410626050` | 36 | 2026-07-08 | VIDEO | Soccer excitement is everywhere! | price |
| `1047985764268781` | 1 | 2026-08-12 | VIDEO | Watching the world’s best players compete inspires millions… but the b | convenience |
| `1066841339622661` | 1 | 2026-08-12 | VIDEO | The excitement of soccer is everywhere… and now it’s your child’s turn | beginner_friendly |

## Potential relevance to DR

- **Observable:** "Soccer at Your Child's School!" used as the ad title by the closest local delivery-model analog. **Why it may matter to DR:** on-campus convenience is one of DR's three core deliverables, and this is direct evidence that a local competitor leads with delivery location rather than sport benefit. **Limit:** 4-ad sample, one advertiser, one brand family. This is a lead worth testing, not a validated pattern.
- **Observable:** program-level registration destinations rather than a homepage. **Why:** post-click fit is one of the levers DR's own gate lists (offer-message fit, creative clarity). **Limit:** says nothing about their conversion rate.
- **Observable:** explicit local proof language ("across Orlando", "right here in your community"). **Why:** DR is Orlando-only and local clarity is a brand rule. **Limit:** the phrases are unremarkable on their own; their value is that a same-market competitor bothers to use them.
- **Observable:** a topical event hook (World Cup) on 100% of their active set. **Why:** it is a seasonal attention device available to DR too. **Limit:** event hooks decay, and DR's audience is 6–12 beginners whose parents may not be following the tournament at all.

*No recommendation is made here. These are observations for later evaluation against DR's own performance data.*
