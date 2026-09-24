---
brand: Orlando-Event-Venue
area: marketing
subarea: creative
note_type: asset
status: draft
canonical: false
used_for_ai: false
source_type: generated
source_reference: "Built 2026-09-22 from the venue stage photo (2644x1536) + OEV Visual Identity tokens. Render script: render.py in this folder."
owner: Cristian
last_updated: 2026-09-22
sensitivity: internal
related_systems:
  - meta-ads
  - website
hub_role: leaf
tags:
  - oev
  - creative
  - paid-social
up:
  - "[[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Marketing-Home]]"
related:
  - "[[01-Brands/Orlando-Event-Venue/00-Brand-Core/Visual-Identity]]"
  - "[[01-Brands/Orlando-Event-Venue/01-Systems/Finance/Pricing-Logic]]"
  - "[[01-Brands/Orlando-Event-Venue/00-Brand-Core/Rules-and-Fees]]"
---

# OEV Creative — Full Day Special $899 (4:5)

## Files
- `OEV-Full-Day-Special-899-1080x1350.png` — variant A (blue, control). Meta feed / IG 4:5
- `OEV-Full-Day-Special-899-2160x2700-master.png` — A, 2x master
- `OEV-Full-Day-Special-899-RED-1080x1350.png` — variant B (red, banner layout)
- `OEV-Full-Day-Special-899-RED-2160x2700-master.png` — B, 2x master
- `render-red.py` — B build script
- `oev-lockup-stacked-white.png` — stacked white lockup composed per Visual Identity spec (wordmark 1200w, icon 1.5x wordmark height, gap 10%). The 20-file logo package in Visual Identity is not on this machine; this file fills the `lockup-stacked/white` slot until the package is committed.
- `render.py` — reproducible build (PIL, v3). Edit copy or positions and re-run.

## Copy (as approved)
```
EVENT VENUE
[ FULL DAY SPECIAL · 24-HOUR ACCESS ]
$899
[ BALDWIN PARK AREA ]
◦ UP TO 90 GUESTS
◦ NO CATERING RESTRICTIONS
◦ INCLUDED: CHAIRS, TABLES, PREP KITCHEN, PARKING
[ CHECK IF YOUR DATE IS OPEN ↓ ]
```

## Build spec (v3, 2026-09-22)
- Canvas 1080x1350. Source photo 1.7:1 extended to 4:5 by outpainting ceiling and floor (Higgsfield outpaint), original hi-res pasted back over the center with feathered seams. Not cropped. Projection screen left as shot. No gradients or fades anywhere.
- Layout: everything centered. Top: stacked white lockup → EVENT VENUE (Avenir Next Heavy 27, tracked 7, ink stroke) → price card → BALDWIN PARK AREA pill. Middle band (wall, stage, screen) clear. Bottom: three bullets → CTA pill, 100px bottom margin.
- Price card ("ticket stamp"): ink `#0B0F19` at 92% with 4px accent keyline, radius 18. Rows: FULL DAY SPECIAL (Avenir Next Heavy 24, tracked 5) / `$899` (Helvetica Neue Condensed Black 148, cap 128px) / 24-HOUR ACCESS on a full-width accent bar (Avenir Next Heavy 24, tracked 5). BALDWIN PARK AREA sits under the card in an ink pill with accent outline.
- Bullets: Avenir Next Heavy 24, tracked 2, white with a 1.6px ink outline, no shadow (removed 2026-09-22 on client request), hollow accent ring markers. CTA: accent pill, Avenir Next Heavy 24, arrow in Arial Bold, soft ink shadow.
- Colors: accent `#0284C7`, ink `#0B0F19`, white. Nothing else.
- Selection: three variants (stacked lockup / price-tag row / ticket card) were rendered and ranked by three independent reviews (client lens, art-director lens, phone lens). Ticket card won 3 of 3. Judge fixes applied: price down 12%, labels up to 24px, thicker keyline, BALDWIN PARK AREA boxed so it does not float over the light strips.

## Variant B (red) — A/B test, 2026-09-22
Same photo, same copy, same logo. Differences from A: accent `#DC2626` instead of `#0284C7`; price lockup moves from a stacked ink card in the ceiling to a red rounded panel on the floor (y 846-998, 70px side margins) holding one row: `$899` (Helvetica Neue Condensed Black 120) | white rule | FULL DAY SPECIAL over 24-HOUR ACCESS (Avenir Next Heavy 29). BALDWIN PARK AREA is an ink tab with white outline sitting on the panel's top edge. Bullets and CTA below the panel; top of the frame holds only the logo and EVENT VENUE (48px, tracked 9, ink stroke, dropped 62px below the logo).

Selection: three red layouts rendered (bullets-top/price-bottom card, red banner, red circle badge) and ranked by three independent reviews (client, art director, growth). Banner won 3 of 3 on legibility, price cohesion and distinctness from A. Fixes applied: inset the band into a rounded panel instead of edge to edge, moved it below the stage step, labels up 12%, bullet shadow removed to match A.

Test framing:
- Hypothesis: grouping price with the CTA on the floor (B) beats price in the ceiling (A) on link clicks and date-check submissions. Color is confounded with layout on purpose; this is a "which creative" test, not a color test.
- Primary metric: cost per date-check submission (GHL form). Secondary: CTR, thumb-stop rate.
- Run: same audience, same budget split 50/50, same copy in the ad text, minimum 7 days or 50 submissions per variant, whichever comes first. Do not read results before then.
- Owner: Cristian sets up, Luis decides which survives.

## v2 (superseded)
Centered stack with ink gradients top and bottom and a 312px `$899`. Rejected 2026-09-22: fades unwanted, price too big, price not fused with FULL DAY SPECIAL / 24-HOUR ACCESS, bullets hard to read.

## v1 (superseded)
Right-aligned copy over the right wall and floor, Arial Black ink type, screen replaced with a brand slide. Rejected 2026-09-22: type did not stand out, price font looked wrong, screen edit unwanted.

## Fact check against the vault
- $899 / 24-hour access / 90 max / prep kitchen / free parking: match Pricing-Logic and Rules-and-Fees.
- "NO CATERING RESTRICTIONS": Rules-and-Fees rule 5 allows outside caterers with liability insurance and bans on-site cooking (prep kitchen is staging + re-heating only). The line is approved copy, but it overstates the policy. Flagged, not changed.
- $199 cleaning fee is not on the creative. Pricing-Logic shows daily special = $899 + $199 cleaning. Ad-platform disclosure is a decision for Luis.
