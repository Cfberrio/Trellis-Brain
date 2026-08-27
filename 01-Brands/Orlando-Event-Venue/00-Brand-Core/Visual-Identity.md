---
brand: Orlando-Event-Venue
area: brand-core
subarea: visual
note_type: core
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Logo variant package generated 2026-08-26 from the existing OEV icon + wordmark source PNGs. Repo path: OEV-PROJECT/brand/oev-logos/"
owner: Luis
last_updated: 2026-08-26
sensitivity: internal
related_systems:
  - website
  - email
  - ghl
hub_role: leaf
tags:
  - oev
  - brand
  - visual-identity
---

# OEV Visual Identity

## Parent
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|OEV Brand Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Voice-and-Tone|OEV Voice and Tone]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Positioning|OEV Positioning]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Email-Design-System|OEV Email Design System]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Website-One-Page-Redesign-2026-07|Website One-Page Redesign]]

## Purpose
Canonical visual identity for Orlando Event Venue: logo variants, color tokens, and typography. Written 2026-08-26 alongside the email rebrand, which was the first system to consume it end to end.

This note governs **appearance only**. It never governs copy. Copy authority lives in [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Language-Rules|OEV Language Rules]] and the ClickUp communications spec.

---

## Logo Package

Twenty PNG files, four formats x five variants. Repo path `OEV-PROJECT/brand/oev-logos/`.

| Format | Folder | What it is |
|---|---|---|
| Icon | `icon/` | The mark alone. Favicons, avatars, app icons, small placements |
| Wordmark | `wordmark/` | "ORLANDO EVENT VENUE" type alone. Wide, short placements |
| Lockup horizontal | `lockup-horizontal/` | Icon left, wordmark right. Default for headers and letterheads |
| Lockup stacked | `lockup-stacked/` | Icon above, wordmark below. Square and vertical placements |

Five variants per format, named `oev-{format}-{variant}.png`:

| Variant | Use |
|---|---|
| `fullcolor-light` | Default. Blue + ink, for light backgrounds |
| `fullcolor-dark` | Blue + white, for dark backgrounds |
| `black` | Single ink. Fax, engraving, one-color print |
| `white` | Single white. Photos, dark solids, video overlays |
| `blue` | Single brand blue. Watermarks, tonal placements |

### Both lockups are new
Horizontal and stacked lockups did not exist before 2026-08-26. They were composed from the existing icon and wordmark:
- **Horizontal**: icon at 600px height, wordmark at 82% of that height, gap 18% of icon height.
- **Stacked**: wordmark 1200px wide, icon at 1.5x wordmark height centered above, gap 10%.

### Blue was inconsistent before this package
The shipped icon used `#10AFEB`. The shipped wordmark used `#00BBFE`. Two different blues in the same identity. The package normalizes both to **`#00BBFE`**.

If you find an old asset with `#10AFEB`, it predates 2026-08-26. Replace it, do not match it.

### Status
Files exist on disk and are **not yet committed** to the repo. Pending review before commit.

---

## Color Tokens

Two related but distinct palettes. Do not mix them.

### Logo blue
`#00BBFE` — the mark's own blue. Used **inside logo artwork only**.

### Product and email palette
The web app's primary is `hsl(200 98% 39%)` = `#0284C7`. Every product surface, email, and UI element derives from it. These are the exact tokens exported by `supabase/functions/_shared/email-layout.ts`:

| Token | Hex | Role |
|---|---|---|
| `accent` | `#0284C7` | Primary. Buttons, links, accent type |
| `accentBright` | `#38BDF8` | Links and accents on dark grounds |
| `accentDeep` | `#0369A1` | Drenched module grounds, section eyebrows |
| `ink` | `#0B0F19` | Headline and hard-value type |
| `black` | `#000000` | Header and footer ground. Matches the logo's own background |
| `text` | `#3B4252` | Body copy |
| `muted` | `#64748B` | Labels, captions, fallback text |
| `line` | `#E2E8F0` | Hairlines, card borders |
| `softBlue` | `#EAF4FB` | Module ground, tinted toward the brand hue |
| `success` | `#059669` | Paid, confirmed |
| `danger` | `#DC2626` | Cancelled, failed |
| `amber` | `#D97706` | Balance due, expiring links |

Neutrals are tinted toward the brand hue on purpose. `#3B4252` and `#64748B` are not neutral grays; they carry a blue bias so they sit with the accent instead of fighting it.

### Rules
- Never pure `#FFF` text on `#0284C7` below 14px. Drop to `accentDeep` or invert the module.
- `amber` is reserved for money that is owed. Not for warnings, not for highlights.
- `black` appears only in the email header and footer. It is not a body ground. A body module on black reads as a different brand.

---

## Typography

Email cannot load webfonts reliably, so the email system runs on system stacks:

| Role | Stack | Treatment |
|---|---|---|
| Display | `'Arial Black', Arial, Helvetica, sans-serif` | 900 weight, italic, uppercase, `letter-spacing: -1px` |
| Body | `Arial, Helvetica, sans-serif` | 15px, `line-height: 1.65` |
| Label | `Arial, Helvetica, sans-serif` | 12px, bold, uppercase, `letter-spacing: 2.5px` |

The display treatment is the identity carrier. Heavy condensed italic uppercase at 32-44px, two-tone: first line `ink`, second line `accent`. It replaces photography entirely.

The web app is not bound to these stacks. This table governs email and any surface that cannot load a webfont.

---

## What This Identity Rejects
- **Photography in email.** Type and color carry the design. Photos were tried and removed 2026-08-26; they rendered huge, loaded slowly, and buried the message.
- **Nested cards.** One card depth. A card inside a card is always wrong.
- **Category-reflex palettes.** No cream-and-terracotta, no gradient hero, no acid-green pop.
