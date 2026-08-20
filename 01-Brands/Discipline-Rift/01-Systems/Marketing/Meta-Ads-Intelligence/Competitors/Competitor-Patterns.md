---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/competitors/patterns.md"
repo_path: domains/ads/meta/intelligence/competitors/patterns.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/competitor
  - discipline-rift
aliases:
  - "Competitor patterns"
  - "Patrones de competidores"
---

# Meta Ad Library — cross-advertiser creative patterns

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitors-Index|Competidores — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Ad-Scripting-Playbook|DR Ad Scripting Playbook]]
- [[01-Brands/Discipline-Rift/02-Communication/Marketing-Language-Library|DR Marketing Language Library]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/competitors/patterns.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Capture date:** 2026-08-13 · Sprint 1, first full sweep
**Preflight source:** reused same-day Task 0 validation (2026-08-13)

> **How consensus is counted here.** By independent `brand_family`, never by ad count and never by advertiser page count. KidStrong HQ and KidStrong Windermere are one family; them agreeing is one brand talking to itself. i9 Sports contributes 39 of 99 ads and gets exactly one family's worth of weight.
>
> **What Ad Library does not publish, and what is therefore absent from this file:** spend, CPA, ROAS, conversions, revenue, profitability, targeting geography, audience composition, budget, campaign structure, ad-set structure. No ad below is called a winner.
>
> **Longevity is a proxy** for "the advertiser kept choosing to run it" and nothing else.

## Dataset snapshot

| | |
|---|---|
| Advertisers scraped | 6 |
| Unique brand families | 5 — `i9-sports`, `super-soccer-stars`, `kidstrong`, `skyhawks`, `soccer-shots` |
| Local (Orlando-metro) advertisers | 2 — KidStrong Windermere, Soccer Shots Orlando |
| National advertisers | 4 — i9 Sports, Super Soccer Stars, KidStrong HQ, Skyhawks |
| Ads analyzed (unique) | 99 |
| Raw records captured | 103 across 7 captures (4 duplicates from a redundant same-day Soccer Shots run, deduped by `<page_id>:<ad_id>`) |
| Capture date | 2026-08-13 |
| `sample_status` | **`unknown` for all 6 advertisers** |

**Completeness is not established for any advertiser in this sweep.** The Actor's full-extraction output carries no completeness signal — `isResultComplete` exists only in count-only mode, and page-level `hiddenAds`/`hasBlankAds` describe ad visibility rather than retrieval completeness. No advertiser hit its configured cap, but retrieving fewer ads than the cap is not evidence of having retrieved them all. Read every count below as **"at least this many"**, and read every "the only ad that…" statement as "the only ad in what was retrieved".

This does not weaken the pattern claims — an unretrieved ad can only add messages, not remove the ones observed — but it does weaken any claim about *absence*, such as "Skyhawks runs no incentive" or "Soccer Shots never mentions coaches". Those are statements about the sample, not proven statements about the advertiser.

Ads by advertiser: i9 39 · Super Soccer Stars 24 · KidStrong Windermere 12 · KidStrong HQ 11 · Skyhawks 9 · Soccer Shots Orlando 4.

**Sample-shape warning that applies to everything below:** 79 of 99 ads are national. The Orlando-local evidence in this sweep is 16 ads from 2 brand families, and 11 of those 16 are a baby-program launch outside DR's age band. The local read is thin by construction.

## Cross-brand repeated patterns

Two ads sharing wording inside one advertiser is repetition. Two independent brand families doing the same thing is the only thing called a pattern here.

---

**pattern:** Confidence / character growth stated as the headline outcome for the child
**independent brand families observed:** 5 of 5
**which families:** i9-sports, super-soccer-stars, kidstrong, skyhawks, soccer-shots
**local/national mix:** both (2 local families, 4 national advertisers)
**evidence examples:** i9 `1550070483189472` ("build confidence, teach life skills") · SSS `907689909044350` ("the confidence, coordination, and friendships that carry from the field into the classroom") · KidStrong HQ `1580452850188777` ("96% of kids experience a boost in self-confidence") · Skyhawks `1828492721446408` ("we build confidence, teamwork, and lasting friendships") · Soccer Shots `1044491151441513` ("Confidence & character building")
**confidence:** high — universal in the captured set, directly quoted from ad copy

---

**pattern:** Beginner acceptance stated explicitly rather than implied
**independent brand families observed:** 4 of 5
**which families:** i9-sports, super-soccer-stars, skyhawks, soccer-shots (kidstrong does not — it frames as "science-based training program")
**local/national mix:** both
**evidence examples:** i9 `1622745849637650` ("Tailored skill development for all skill levels… No pressure, just play") · SSS `1053712297304989` cards ("Getting Started Is the Fun Part", "Ages 1 to 10, All Skill Levels") · Skyhawks `1321643169947617` ("whether your child is picking up a ball for the first time") · Soccer Shots `1044491151441513` ("Give your child their first step onto the field")
**confidence:** high

---

**pattern:** Coach credential used as the proof element
**independent brand families observed:** 4 of 5
**which families:** i9-sports, super-soccer-stars, kidstrong, skyhawks (soccer-shots does not mention coaches in any of its 4 ads)
**local/national mix:** both
**evidence examples:** KidStrong `1421885689760251` ("certified coaches lead 45-minute classes") · Skyhawks `1725639242428595` ("certified coaches who know how to make every moment count") · SSS `1053712297304989` ("small groups, expert coaches") · i9 `3124522577751153` ("Supportive coaches focused on building confidence")
**confidence:** high

---

**pattern:** An explicit incentive runs as its own creative line
**independent brand families observed:** 4 of 5
**which families:** super-soccer-stars ($45 code + 100% free trial), kidstrong (free class, local page only), soccer-shots (early bird), i9-sports ($10 referral credit) — skyhawks runs none
**local/national mix:** both
**evidence examples:** SSS `2270727753726204` ("100% FREE trial class… Limited September spots") and `881946464989123` ("Use code IGFALL45 to save $45") · KidStrong Windermere `1383563240621284` ("Try a FREE Class", CTA `Get offer`) · Soccer Shots `1044491151441513` ("Fall Season Registration Now Open! Early Bird Pricing!") · i9 `918860043798394` ("$10 credit for every new family")
**confidence:** high for presence of an incentive; **nothing observable about whether any of them worked**

---

**pattern:** The qualifying age band is written into the ad copy
**independent brand families observed:** 3 of 5
**which families:** i9-sports, super-soccer-stars, kidstrong (skyhawks and soccer-shots state no age in their captured copy)
**local/national mix:** both
**evidence examples:** i9 `2269556310245647` ("kids 5–14") · SSS `1016105374549231` ("ages 1 to 10") · KidStrong `4587976504764754` ("kids ages 1–11")
**confidence:** medium — clear where present, but two families' silence may reflect creative style rather than a decision

---

**pattern:** Season / back-to-school calendar trigger drives the campaign
**independent brand families observed:** 3 of 5
**which families:** super-soccer-stars, soccer-shots, kidstrong (Windermere's "School Year Ahead" card and "Classes start 8/17") — i9 and skyhawks run undated evergreen copy
**local/national mix:** both
**evidence examples:** SSS `907689909044350` ("Back to school, back to soccer… Fall classes now open") · Soccer Shots `1066841339622661` ("Fall Park Season Registration Now Open!") · KidStrong Windermere `1272462759279601` ("Classes start 8/17")
**confidence:** medium-high

---

**pattern:** Copy held constant while media and/or CTA vary across many ad IDs
**independent brand families observed:** 3 of 5
**which families:** kidstrong (HQ: 11 ads, identical body, CTA split `Book now`/`Learn more`/`See details`, 9 video + 2 image), skyhawks (9 ads, identical body and title, 6 image + 3 video), i9-sports (6 identical "Empower girls" ads; 6 identical referral ads)
**local/national mix:** national only — no local advertiser in this sweep shows the pattern
**evidence examples:** KidStrong HQ `1580452850188777` / `4587976504764754` / `1421885689760251` (same copy, three different CTAs) · Skyhawks `1828492721446408` … `2428180057674056` (nine, one message)
**confidence:** high that the structure exists; **zero visibility into results.** What is observable is a variation set, not a validated test

---

**pattern:** Place named inside the creative rather than left to targeting
**independent brand families observed:** 2 of 5
**which families:** super-soccer-stars (NYC, Manhattan, Jersey City, Hoboken, New Jersey), soccer-shots (Orlando, "your community", "your child's school")
**local/national mix:** 1 national + 1 local
**evidence examples:** SSS `906996449106228` ("Fall classes now open in Jersey City") · Soccer Shots `1047985764268781` ("📍Played right here in your community")
**confidence:** medium — meets the 2-family bar, but only just

---

Below the 2-family bar and therefore **not** consensus: sport-specific landing pages (i9 only), quantified proof statistics (kidstrong only), topical event hooks (soccer-shots only), waitlist/early-interest mechanics (kidstrong only).

## Local patterns

**Sample: 2 advertisers, 2 brand families, 16 ads — and 11 of those 16 are KidStrong Windermere's BabyStrong (6–12 months) launch, outside DR's age band entirely.** Read everything here as a lead, not a finding. One more local advertiser going active would materially change these counts.

What both local advertisers do, that no national advertiser in the sweep does:

- **Send traffic to a local or program-level destination.** `windermere.kidstrong.com/…` and `ss-osb.soccershots.com/page/class-registration?progId=…` — never a national homepage. Both national KidStrong and Skyhawks send to a national root domain instead.
- **Use a soft CTA.** `Learn more` on 15 of 16 local ads (the exception is the one `Get offer` free-class ad). The national advertisers lean `Sign up`.
- **Carry a date or a registration window.** "Classes start 8/17", "Fall Season Registration Now Open".

What they do not share: Soccer Shots names coaches nowhere and states no age band; KidStrong Windermere does both. With n=2 families, that difference is not interpretable.

## National patterns

4 advertisers, 4 brand families, 79 ads. **These ads cannot be assumed to target Orlando.** Meta exposes no geo targeting for US commercial ads, and Super Soccer Stars' creative actively names NYC and New Jersey — evidence that at least one of these national pages is running creative for markets DR does not operate in.

Directional observations only:

- **Hard-convert CTA is the norm** — i9 `Sign up` 33/39, SSS `Sign up` 20/24, Skyhawks `Sign up` 9/9.
- **Message breadth splits the field.** i9 segments creative by sport with matched landing pages; Skyhawks runs one undifferentiated message to a homepage with no sport, age, offer or location named. Both are national advertisers of similar program type making opposite specificity choices.
- **Volume is concentrated in structural repetition, not distinct ideas.** Across 79 national ads there are roughly a dozen distinct messages; the rest are format and CTA variants of them.

## Local vs national within-brand comparison (KidStrong)

**This is one brand family compared with itself. It is not cross-brand consensus and is not counted as such anywhere above.** It is the cleanest natural experiment in the watchlist because the underlying offer is identical.

| Dimension | KidStrong HQ (national, 11 ads) | KidStrong Windermere (local, 12 ads) |
|---|---|---|
| **Hook** | One fixed hook: "🏃‍♂️ACCEPTING NEW MEMBERS🏃‍♂️" | Launch hooks: "BabyStrong Is Coming", "Strong starts here.", "Built for babies – and you." |
| **Offer** | None in any ad | Free class (1 ad); early-access list (11 ads) |
| **Angle** | structure + coach credential + quantified outcome | urgency + developmental outcome |
| **CTA** | `Book now` 6 / `Learn more` 3 / `See details` 2 | `Learn more` 11 / `Get offer` 1 |
| **Localization** | National site, "Find your local KidStrong" | Local subdomain on 12/12 ads; no city named in copy |
| **Urgency** | None | 11/12 ads — "spots fill fast", "Classes start 8/17" |
| **Proof / credibility** | "96% of kids experience a boost in self-confidence"; "certified coaches"; "science-based" | Largely absent — the 96% statistic does not appear on the local page's ads |
| **Program framing** | Core kids 1–11, 45-minute weekly classes | 11/12 ads on a 6–12-month baby program; 1 ad on core kids |

The two levels are running materially different campaigns rather than local variants of one campaign. Local adds an offer, a date and urgency; local drops the quantified proof point. Whether that trade is deliberate or simply a launch taking over the local calendar is **not observable** from Ad Library.

## Long-running creative patterns

**LONGEVITY IS A PROXY, NOT PERFORMANCE PROOF.** Ranked for inspection only.

| Advertiser | Longest-running ad | Days (proxy) | What it is |
|---|---|---|---|
| Super Soccer Stars | `2042597273277714` | 108 | B2B franchise recruitment — *not* parent-facing |
| i9 Sports | `1296206572498680` and 8 others from 2026-06-24 | 50 | Sport-specific DCO sets (soccer, basketball, T-ball, flag football, volleyball) |
| Soccer Shots Orlando | `1044491151441513` | 37 | "Soccer at Your Child's School!" — school-season line |
| KidStrong Windermere | `2250833115665202` | 18 | BabyStrong early-interest |
| Skyhawks | `1828492721446408` | 12 | The single fixed message |
| KidStrong HQ | `1580452850188777` | 9 | The single fixed message |

Two things are observable across the longer-running parent-facing set:

1. **The oldest parent-facing creatives carry no date-specific claim.** i9's 50-day sport sets and Soccer Shots' 37-day school ad are evergreen in wording; the dated seasonal creative (KidStrong Windermere's 8/17, SSS's fall push) is all recent. This may simply mean dated creative is newly launched for the fall window rather than that undated creative survives longer. Both readings fit the data; a second capture in ~30 days would separate them, and that is the cheapest next measurement available.
2. **Longevity does not track ad volume.** Skyhawks and KidStrong HQ run the highest structural repetition and the shortest-lived ads in the sweep.

## Contradictions

Where the brands materially disagree — these are more useful than the agreements, because they mark the places where DR actually has a choice rather than a default.

- **CTA intent.** Hard-convert `Sign up` (i9, Super Soccer Stars, Skyhawks — 3 families) vs soft `Learn more` (KidStrong, Soccer Shots — 2 families). Both local advertisers sit on the soft side; both are also the two advertisers with the most specific destinations. No performance evidence resolves this.
- **Specificity.** i9 splits creative by sport with matched `/ppc/<sport>` landing pages; Skyhawks runs one message with no sport, no age, no offer and a homepage destination. Same category, opposite bets.
- **Positioning of the same parent decision.** i9 sells "No pressure, just play" (fun-first). KidStrong sells "science-based training program… 96% of kids experience a boost in self-confidence" (structured development). These are opposed frames aimed at overlapping buyers.
- **Incentives.** 4 of 5 families run an explicit incentive; Skyhawks runs none at all.
- **Format.** Soccer Shots is 100% video, KidStrong HQ 82% video, i9 is 56% DCO catalog, Skyhawks 67% static image. No format consensus exists in this data.

## Candidate creative observations for DR

**Not recommendations.** These are observations worth evaluating later against DR's own performance data. No experiment is designed here, and nothing below has been checked against DR's account.

---

**1. Lead with delivery location in the hook, not with the sport benefit**
- **evidence:** Soccer Shots Orlando `1044491151441513`, `1349843410626050` — ad title "Soccer at Your Child's School! ⚽️🏫", the only ad in 99 to put the delivery location in the title
- **brand-family count:** 1 (soccer-shots). Below the consensus bar
- **applicability_to_DR:** high — on-campus convenience is one of DR's three stated deliverables, and this comes from the closest local delivery-model analog running ads
- **modification_required:** no
- **key caveat:** single family, 4-ad sample, and Soccer Shots' age band (18mo–8y) only overlaps DR's at 6–8. Its own performance is unknown

---

**2. State the qualifying age band inside the creative**
- **evidence:** i9 `2269556310245647` ("kids 5–14"), SSS `1016105374549231` ("ages 1 to 10"), KidStrong `4587976504764754` ("ages 1–11")
- **brand-family count:** 3 of 5
- **applicability_to_DR:** high — DR's 6–12 band is a hard qualifier and mis-qualified clicks are expensive on a small local account
- **modification_required:** no
- **key caveat:** all three sources are national advertisers with wider bands than DR's. The tactic transfers; the numbers do not

---

**3. Pair a season start date with an open-registration trigger**
- **evidence:** KidStrong Windermere `1272462759279601` ("Classes start 8/17"), Soccer Shots `1066841339622661` ("Fall Park Season Registration Now Open!"), SSS `907689909044350` ("Fall classes now open")
- **brand-family count:** 3 of 5, including both local families
- **applicability_to_DR:** high — DR sells seasons with real start dates and a real registration window
- **modification_required:** no
- **key caveat:** date-specific creative in this sweep is all recent, so it has no longevity record yet. DR must also use only real dates — no manufactured urgency

---

**4. Send the click to a program-level destination, not a homepage**
- **evidence:** Soccer Shots `1044491151441513` → `ss-osb.soccershots.com/page/class-registration?progId=25320`; i9 `1296206572498680` → `/ppc/soccer`; KidStrong Windermere → `windermere.kidstrong.com`. Counter-example: Skyhawks, 9/9 ads → homepage
- **brand-family count:** 3 of 5
- **applicability_to_DR:** high — post-click fit sits inside DR's own recommendation gate (offer-message fit, creative clarity)
- **modification_required:** no
- **key caveat:** no conversion evidence for any of these destinations. This is a structural observation only

---

**5. Hold copy constant and vary one element at a time**
- **evidence:** KidStrong HQ `1580452850188777` / `4587976504764754` / `1421885689760251` — identical copy, three CTAs; Skyhawks 9 ads, one message, media varied
- **brand-family count:** 3 of 5 (kidstrong, skyhawks, i9)
- **applicability_to_DR:** medium — improves learning conditions on a small account where muddled tests waste real budget
- **modification_required:** yes — DR's volume is far below these advertisers', so a 9-variant structure would starve every cell. The principle transfers; the scale does not
- **key caveat:** the structure is observable, the outcome is not. Nobody knows whether these tests taught the advertiser anything

---

**6. Beginner acceptance stated in plain words**
- **evidence:** Skyhawks `1321643169947617` ("picking up a ball for the first time"), i9 `1622745849637650` ("all skill levels… No pressure, just play"), SSS carousel card "Getting Started Is the Fun Part", Soccer Shots `1044491151441513` ("their first step onto the field")
- **brand-family count:** 4 of 5
- **applicability_to_DR:** high — DR is beginner-friendly and fun-first by definition
- **modification_required:** no
- **key caveat:** it is the most crowded message in the category. Doing it does not differentiate DR; *not* doing it is the bigger risk

---

**7. Confidence as the headline promise**
- **evidence:** all 5 families
- **brand-family count:** 5 of 5
- **applicability_to_DR:** low as written
- **modification_required:** yes
- **key caveat:** **DR's claim rules forbid this framing.** Confidence, friends, sportsmanship and discipline may appear only as supported byproducts, never as the primary promise, and DR must not publish a measured claim it does not track. KidStrong's "96%" is exactly the kind of claim DR cannot copy. Listed because it is the single most universal pattern in the data and its universality is itself the argument against leading with it

---

**8. An explicit low-friction first step**
- **evidence:** SSS `2270727753726204` (100% free trial class), KidStrong Windermere `1383563240621284` (free class), Soccer Shots `1044491151441513` (early bird), i9 `918860043798394` ($10 referral credit)
- **brand-family count:** 4 of 5
- **applicability_to_DR:** medium
- **modification_required:** yes — offer and guarantee decisions belong to the DR domain, not to this file, and DR's context bars mentioning a guarantee that is not finalized
- **key caveat:** Ad Library shows the offer existing, never whether it paid for itself. Skyhawks runs none and we cannot say it is wrong

---

**Observed defect, recorded for accuracy rather than as a DR lead:** all 6 i9 referral ads (`918860043798394`, `1706459393737451`, `1048981687479652`, `1050086220798262`, `934616286321912`, `986398034381055`) point at `wptest.i9sports.com/refer-a-friend` — a staging hostname in live creative. Also, KidStrong Windermere `2470033500142202` carries two cards with contradictory start dates (6/22 and 8/17). Both are observations about competitor QA, not transferable creative patterns.

## Traceability

Every ad ID above resolves through `data/index.json` (keyed `<facebook_page_id>:<ad_id>`) to its capture, Actor run ID, dataset ID and raw evidence file under `data/raw/`. Normalized records are in `data/normalized/2026-08-13_<slug>.json`. Per-advertiser detail is in `competitors/ads/<slug>.md`.
