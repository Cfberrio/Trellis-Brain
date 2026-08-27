---
brand: Discipline-Rift
area: communication
subarea: design-system
note_type: manual
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Google Drive folder 1cVCYpQE8-CS8OsZtDsQEAOZFMUirdqTj — 'DR Website - Design System & Layout Reference.md' + index.html (built homepage prototype, Jul 7 2026)"
owner: Luis
last_updated: 2026-08-25
sensitivity: internal
related_systems: []
related_notes:
  - "[[Communication-Home]]"
  - "[[Marketing-Language-Library]]"
  - "[[01-Brands/Discipline-Rift/00-Brand-Core/Voice-and-Tone|DR Voice and Tone]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library|DR Operational Email Library]]"
hub_role: leaf
---

# Discipline Rift — Email Design Spec

**Purpose:** Write and build marketing emails that look like they came from disciplinerift.com. This is the site design system translated into what email clients can actually render.

**Source of truth:** `DR Website - Design System & Layout Reference.md` + `index.html` (Google Drive, folder `1cVCYpQE8-CS8OsZtDsQEAOZFMUirdqTj`). Copy rules come from [website-structure.md](website-structure.md) §11 and [.agents/product-marketing-context.md](../../../.agents/product-marketing-context.md) §"WEBSITE BUILD DECISIONS — v2".

**Platform:** GHL email builder. Merge syntax `{{contact.*}}` only.

---

## 1. The design in one paragraph

DR is a **minimalist, white-canvas brand with a single blue accent**. It borrows Verizon's homepage structure — giant-word hero, one message per section, huge vertical breathing room, outlined rounded cards, a solid-color promo band — and strips it to white / grayscale / black / `#0497F7`. Nothing is decorated. Emphasis comes from **scale and negative space**, not from color variety, gradients, shadows, or illustration. Sport colors exist but are almost never used. The feeling to hit: *clean, confident, uncrowded, a little oversized.* If an email looks busy, it's off-brand — regardless of what it says.

**The three moves that make something read as DR:**
1. One oversized blue phrase carrying the message, with white space around it.
2. Thin blue outlines on white cards (border-first — not fills, not shadows).
3. One solid blue band that holds the offer, with a white pill button inside it.

---

## 2. Color tokens

Email has no CSS variables. Hard-code these hex values inline.

| Role | Hex | Where it goes in an email |
|---|---|---|
| White | `#FFFFFF` | Default background. Text on blue/black. |
| Black | `#0B0B0B` | Footer. Occasional full-bleed contrast block. |
| **Blue (brand)** | **`#0497F7`** | The one accent: buttons, links, section headings, giant hero phrase, card outlines. |
| Blue ink | `#0378C6` | Button fill when button text is under 18px (see §8). |
| Gray 900 | `#1D1D1F` | Headline text on white. Body text that must be high-contrast. |
| Gray 700 | `#3f4147` | Nav/secondary link text. |
| Gray 500 | `#6B7280` | Body copy, captions, legal. |
| Gray 300 | `#c9ccd1` | Dashed image-slot borders. |
| Gray 200 | `#E5E7EB` | Neutral card borders, dividers, hairlines. |
| Gray 50 | `#F5F6F8` | Soft section fill (the "band-soft" alternating block). |

**Sport colors — restricted.** Only inside a sport-specific module: a small dot next to a sport name, or a per-sport email where that sport is the subject. Never as nav, button, background, or heading color.

| Sport | Graphics | Text on white |
|---|---|---|
| Volleyball | `#66D43D` | `#66D43D` |
| Tennis | `#E6DD19` | **`#B9B117`** — darkened for legibility. Never set `#E6DD19` as text on white. |
| Pickleball | `#F25F22` | `#F25F22` |
| Flag Football | `#0497F7` (brand blue) | `#0497F7` |

---

## 3. Typography

**Font stack.** The site uses Inter. Web fonts are unreliable in email — do not fight it. Use:

```
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
```

Add for Outlook so it doesn't fall back to Times:
```html
<!--[if mso]><style>* { font-family: Arial, sans-serif !important; }</style><![endif]-->
```

**Ethnocentric is wordmark-only.** It appears only inside the logo image. Never as live text.

**Email type scale** (600px body — the site's `clamp()` sizes are for a 1200px canvas and must come down):

| Role | Size / weight | Line-height | Color | Notes |
|---|---|---|---|---|
| Preheader | 1 line, hidden | — | — | 40–90 chars, never repeats the subject |
| Eyebrow / label | 12–13px / 700 | 16px | `#6B7280` | UPPERCASE, `letter-spacing:.08em` |
| **Giant phrase (hero)** | **40–52px / 900** | 44–52px | `#0497F7` | `letter-spacing:-.03em`. Mobile: 32–36px |
| Hero pre-line | 18–20px / 800 | 26px | `#1D1D1F` | Sits above the giant phrase |
| Hero post-line | 20–22px / 800 | 28px | `#1D1D1F` | Sits below |
| Section H2 | 28–32px / 900 | 34–38px | `#0497F7` | Centered. `letter-spacing:-.025em` |
| Card title | 20–22px / 900 | 26px | `#0497F7` | |
| Card subline | 15px / 800 | 20px | `#0497F7` | |
| Body | 16px / 400 | 25px | `#6B7280` | Never below 14px |
| Button label | 16–18px / 800 | 20px | `#FFFFFF` | UPPERCASE for REGISTER |
| Legal / footer meta | 12–13px / 400 | 18px | `#8b8f97` | |

Always set `line-height` in **px**, not unitless — Outlook ignores unitless values.

---

## 4. Layout system

| Rule | Email value | Site equivalent |
|---|---|---|
| Body width | **600px** table, centered | 1200px container |
| Side gutters | 24px desktop / 16px mobile | same |
| Section rhythm (vertical padding) | **40–56px** top and bottom | 96–128px |
| Gap between stacked cards | 16px | 22px |
| Card padding | 28px 26px | 32px 30px |
| Card radius | 20px (Outlook will square it — fine) | 26px |
| Button radius | 999px pill (Outlook squares it — fine) | 999px |
| Border weight | 1.5px `#0497F7` emphasized · 1px `#E5E7EB` neutral | same |
| Shadows | **none** | hover-only on site; email has no hover |

**Structural rules:**
- Tables for all layout. No flexbox, no grid, no `aspect-ratio`, no `clamp()`, no `backdrop-filter`.
- Padding on `<td>`, never on `<div>` or `<p>`.
- The site's 3-across card rows **stack vertically** in email. Do not try to keep 3 columns at 600px — two columns maximum, and only for short items like the season checklist.
- Section rhythm is the brand. Under-padding is the most common way an email stops looking like DR.

---

## 5. Component translations

### 5.1 Header
Blue DR monogram on white, left-aligned, 26px tall, with 24px gutters and a 1px `#E5E7EB` bottom hairline. Optional right-side text link `REGISTER` in `#0497F7`/700. Keep it to one row. No nav menu in email.

### 5.2 Giant-word hero
The single most recognizable DR element. Three stacked lines, centered:

```
Sports at your child's school where   ← 18px / 800 / #1D1D1F
coaches actually teach.               ← 44px / 900 / #0497F7
Right after school.                   ← 20px / 800 / #1D1D1F
```

Then the audience line at 14px `#6B7280`: `Elementary · K through 5th · Beginner-friendly to advanced · No transportation needed` (phrasing per §9 — "beginner-friendly to advanced")

Adapt the blue line per campaign — it's a slot, not fixed copy. Keep it to **3–6 words**, and keep the surrounding white space (40px+ above and below). The sports line may be color-coded, hero-only, using the text hexes in §2.

**Ruling (Luis, 2026-08-09 production run):** the brand name itself — `DISCIPLINE RIFT` — is an approved giant-word hero, rendered in the same big blue centered layout **with nothing under it**. No tagline, no subline. The wordmark moment stands alone.

**Ruling (same run):** "Low cost — everything included" renders as **black text on a white background** when it appears outside the blue promo band. Never white-on-black — when a build drifts dark, the correction is always back to the white canvas.

### 5.3 Promo band (the offer container)
Solid `#0497F7` table, 20px radius, 32px padding, white text. Holds: eyebrow → H2 in white → 2-column checklist with white ticks → 100% guarantee seal → white pill button.

Checklist ticks: use a 20px transparent PNG tick, or a `✓` in white 700. Do not build circular tick backgrounds with `border-radius` — Outlook renders squares.

The site's rotated white "Low cost / everything included" bubble **cannot rotate in email**. Two options: (a) flatten it to a pre-rendered transparent PNG, or (b) drop it and put the same words as a white 13px/800 line under the checklist. Option (b) is safer and reads clean.

### 5.4 Eyeglass card
White background, `1.5px solid #0497F7`, 20px radius, 28px padding. Contents top to bottom: big blue word (22px/900) → blue subline (15px/800) → gray body (16px/400) → blue `→` arrow, right-aligned. Stack them vertically with 16px gaps.

### 5.5 Numbered steps
46px blue circle with a white number (use an image or a table cell with `bgcolor="#0497F7"`), then a 19px/900 `#1D1D1F` title, then 15px `#6B7280` body. On the site these sit on a `#F5F6F8` band — reproduce that as a full-width gray-50 table row.

### 5.6 Tier cards
The site tilts and overlaps four squares (outlined blue → solid blue → outlined black → solid black). **No rotation in email.** Either export the tilted stack as a single PNG, or render four straight 20px-radius squares in a row using the same four fills. Caption below: 14px/700 `#6B7280`.

### 5.7 Sport tiles
1.5px `#E5E7EB` outlined box, line icon, then a 9px colored dot + sport name at 15px/800. **The dots are the only place sport color belongs** in a general email.

### 5.8 Image slots
Conceptual imagery only — **no real coach or player photos, ever** (hard brand rule). 20px radius, 4:3. In dev drafts, use a dashed `#c9ccd1` border with italic 13px `#6B7280` placeholder text, same as the site prototype. Always write real `alt` text: images are off by default in Outlook, and the CTA must never live inside an image.

### 5.9 Footer
`#0B0B0B` background. White DR mark, tagline at 14px `#8b8f97`, links at 15px/600 `#e7e9ec`, meta at 13.5px, legal at 12.5px `#71757d`. Canonical block:

```
Value Guarantee · Running at 55 schools in Central Florida
713 W Yale St, Orlando FL 32804 · (407) 614-7454
info@disciplinerift.com · Instagram · TikTok · Facebook
Privacy · Terms · © Discipline Rift (Torres Rivero LLC)
```

---

## 6. Buttons

One primary CTA per email. Label is **`REGISTER`** (uppercase) unless the email's job is genuinely something else.

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td align="center" bgcolor="#0497F7" style="border-radius:999px;">
      <a href="{{link}}" style="display:inline-block; padding:16px 34px; font-family:'Inter',Arial,sans-serif;
         font-size:18px; font-weight:800; color:#FFFFFF; text-decoration:none; border-radius:999px;">REGISTER</a>
    </td>
  </tr>
</table>
```

- **Primary:** blue fill, white text.
- **Secondary (ghost):** white fill, `1.5px solid #0497F7`, blue text.
- **On the blue band:** white fill, `#0378C6` text.
- No hover states — they don't exist in email. Don't design around them.

---

## 7. Dark mode

Apple Mail, iOS Mail, and Outlook.com auto-invert. A white-canvas brand is exactly the case that breaks badly.

```html
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
```

```css
@media (prefers-color-scheme: dark) {
  .dr-canvas { background:#0B0B0B !important; }
  .dr-head   { color:#FFFFFF !important; }
  .dr-body   { color:#c7cace !important; }
  .dr-card   { background:#0B0B0B !important; border-color:#0497F7 !important; }
}
```

- Blue `#0497F7` works on both white and `#0B0B0B` — leave it alone in both modes.
- Ship the **white** DR mark as a transparent PNG for dark mode; a white-background logo becomes a glaring white rectangle.
- The blue promo band already survives inversion. It's the safest place to put the offer.

---

## 8. Accessibility (carried from the site rules)

- `#0497F7` on white is **3.1:1** — fine for large/bold text and UI, **not** for body copy. Blue text only at **≥18px or bold**. Set body copy in `#1D1D1F` or `#6B7280`, never blue.
- White on `#0497F7` is also 3.1:1. It clears the large-text bar at **18px/800**, which is why the button above is 18px. If you need a 16px button label, switch the fill to `#0378C6` (4.7:1) instead.
- Never set Tennis `#E6DD19` as text on white.
- Real `alt` text on every image. Semantic heading order. Minimum 14px body.

---

## 9. Copy rules that constrain the design

These are hard brand rules, not preferences. They change what you can put in a layout.

- **No dollar figures. Anywhere.** A real number appears only at the payment step. Emails say **"Low cost — everything included."** This means: no price bubble, no crossed-out number, no "$X off," no price-anchor block. (The Drive design doc's §5 still shows a `$129 / season` example — that is stale and superseded by the v2 rule.)
- **"No transportation needed"** — that exact phrasing. Never "no driving," never "no pickup." Parents still pick up.
- **Value Guarantee wording (Luis ruling — supersedes the earlier "real teaching and real progress" phrasing; see parent-email-template.md §2.8):** "Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season." Site footer still needs aligning to this wording (campaign open item 4).
- **Teaching leads.** "We actually teach" is the anchor of every asset. Confidence, friends, and discipline are byproducts, never the promise.
- **Banned on parent-facing emails:** *fun-first, elite, high-performance, next level, serious athlete, future champion, tryouts*, and athlete-development-as-the-central-promise.
- **Say "beginner-friendly to advanced"** — never beginner-only.
- **Only sanctioned proof:** "Running at 55 schools across Central Florida" and founder Luis Torres (10 years, club director). **Never fabricate a testimonial or a stat.**
- **Tier = season.** One tier is earned per season, not within a season.
- Audience line: **Elementary · K through 5th** (not "ages 6–12" — that's stale).
- **No trial.** The offer is one 6-week season, framed as low commitment.

---

## 10. Section order that reads as DR

The homepage rhythm, compressed to an email. Use 3–5 of these, not all:

1. Header (logo + REGISTER link)
2. **Giant-word hero** — the campaign message
3. One-line audience/qualifier
4. Primary CTA
5. **Blue promo band** — what's included + guarantee seal + white button
6. Value Guarantee statement in plain text on white
7. Two or three **eyeglass cards**, stacked
8. Numbered steps on a `#F5F6F8` band
9. Proof line — "Running at 55 schools across Central Florida"
10. Sport tiles with color dots
11. Closing CTA — blue full-width band, white button
12. Black footer

**One message per section.** If a section is arguing two things, split it or cut one.

---

## 10.1 Subject + preview rules (Luis, 2026-08-09 production run)

- **Subject style:** calendar-anchored, plain, direct question. Shipped example: `Back to school this Tuesday. Are you ready?` Curiosity-angle subjects lost to this.
- **The after-school-gap frame** ("what fills the time after 3 PM?") is allowed in the subject or preview **as an open question only** — never in the body as fear.
- Expect copy to compress at the design stage. Write lines that survive halving.

## 11. Pre-send checklist

- [ ] One primary CTA, repeated at most twice, labeled `REGISTER`
- [ ] Zero dollar figures
- [ ] "No transportation needed" phrasing exact
- [ ] No banned words
- [ ] No fabricated proof; only 55 schools / Luis Torres
- [ ] No real coach or player photos
- [ ] Sport colors confined to dots or a single-sport module
- [ ] Blue text is ≥18px or bold everywhere it appears
- [ ] Section padding ≥40px — it should feel too airy in the editor
- [ ] Alt text on every image; CTA is live text, not an image
- [ ] Dark mode checked in Apple Mail
- [ ] Rendered at 600px and at 375px
- [ ] Preheader written, not auto-pulled
- [ ] Merge tags are `{{contact.*}}` and have fallbacks
- [ ] `{{contact.first_name}}` fallback set to "there" in the GHL merge-field editor — checked per send; the HTML cannot carry it
- [ ] Unsubscribe href swapped BY HAND to this GHL account's unsubscribe link/trigger — GHL does NOT auto-replace `[UNSUBSCRIBE_LINK]` or any bracket token
- [ ] Bracket-token grep: search the full source for `[` — zero tokens outside HTML comments in a campaign file at send time (hrefs, preheader, footer included)
- [ ] Footer carries address, phone, and unsubscribe

---

## 12. Related files

| File | What it gives you |
|---|---|
| [website-structure.md](website-structure.md) | Canonical v2 site blueprint — IA, page-by-page copy, offer rules |
| [campaigns/2026-08-first-week-of-school-email.md](campaigns/2026-08-first-week-of-school-email.md) | Worked example of the campaign doc format |
| [site-snapshots/2026-08-04/](site-snapshots/2026-08-04/) | Live-site copy as ground truth |
| `DR Website - Design System & Layout Reference.md` (Drive) | Full design system incl. v2/v3 addenda |
| `index.html` (Drive) | Built homepage — the reference render |
| `DR Website - Image Generation Brief.md` (Drive) | Prompts for the 5 conceptual image slots |

**Open item:** the DR mark needs three web-hosted PNGs for email — blue on transparent, white on transparent, and a 20px white tick. Confirm they exist in `Brand Assets/01 Logos/Main Logos` and get them onto a public URL before the first send.

**RESOLVED (2026-08-25):** the open item is closed. The DR mark now has a hosted **email asset kit** — derived from the hi-res master in Drive `01_MAIN LOGOS/DR LOGO blue.png` (1563px), served by the website itself (deploys with it, stable URLs):

| URL | Use |
|---|---|
| `https://disciplinerift.com/brand/dr-mark-blue-52h.png` | Header mark on white (render at height 26px — file is @2x) |
| `https://disciplinerift.com/brand/dr-mark-white-52h.png` | Black footer + dark mode |
| `https://disciplinerift.com/brand/dr-tick-white-20.png` (+ `-40` @2x) | Promo-band checklist tick |
| `https://disciplinerift.com/brand/dr-mark-{blue\|white\|ink\|black}-256w.png` | General use, 256px wide |
| `https://disciplinerift.com/brand/dr-tile-{blue\|black\|outline-blue\|outline-black}-256.png` | §5.6 tier row, straight (no rotation) |

Full kit (more sizes incl. 1024w) lives in `~/Documents/DISCIPLINERIFT/brand-kit/png/`; regeneration script inline in that folder's git history. Master source: Drive folder `1jWNnaYqUuY1hEHO499QzfKaRmQ836qAs`.

**Boilerplate built (2026-08-25):** the GHL marketing boilerplate referenced by parent-email-template §4 now exists at `~/Documents/DISCIPLINERIFT/brand-kit/email/dr-boilerplate-ghl.html` — every slot (header, giant hero, copy slots, eyeglass card, blue promo band, guarantee, tier row, close, black footer) is an independently deletable table block, hosted asset URLs already wired, `[REGISTER_URL]`/`[UNSUBSCRIBE_LINK]`/`[PREHEADER]` tokens to swap per send.

**Transactional shell shipped (2026-08-25):** the tokens and rules above are now also load-bearing for **code-rendered transactional email**, not just GHL marketing sends. Three parent-facing templates in `~/Documents/DISCIPLINERIFT/disciplinerift/supabase/functions/_shared/email-templates.ts` (Registration Confirmation, Parent Guide, Waitlist Invite) were rebuilt on a shared shell — `drShell` / `drHeader` / `drFooter` / `drButton` — using this doc's color tokens, font stack, table-only layout rule, and black footer spec, after a `=20` encoding bug (denomailer) forced a full audit of the transactional path. Full changelog, root cause, and before/after: [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library#Changelog — 2026-08-25|Operational Email Library § Changelog]].
