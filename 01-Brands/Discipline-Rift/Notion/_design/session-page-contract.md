---
title: DR Session Page Contract
brand: Discipline-Rift
area: notion-design
note_type: standard
source_repo: CLAUDE-TRELLIS/domains/ops/notion/dr-coach-wiki/session-page-contract.md
synced: 2026-09-17
tags:
  - brand/discipline-rift
  - notion-design
up:
  - "[[01-Brands/Discipline-Rift/Notion/_index]]"
---

# DR Session Page Contract

Binding format for every coach-facing session page in the DR Notion wiki.

Derived by reverse-engineering the two handmade reference pages Luis built by hand:
**BEING A COACH** and **THE HAND OF A COACH**. Those two are the standard. This file
exists so every new session page matches them without Luis having to rebuild by hand.

Do not deviate from this contract. If a session's content does not fit it, cut the
content, not the format.

---

## The non-negotiables

1. **A session page teaches one idea.** If it teaches two, it is two pages.
2. **Few points chosen hard.** The handmade pages are short. Length is not quality.
   A session page that dumps the whole deck has failed the contract.
3. **Never paste source text.** Slides and transcripts are raw material. Rewrite into
   coach-facing instruction: second person, present tense, imperative where it earns it.
4. **Gaps get flagged, never invented.** If the source never said what the five fingers
   meant, the page says so. No filling in blanks with plausible content.
5. **Emoji series must be internally consistent.** One semantic family per page
   (hands for the five fingers, 🚩 for consequence, tools for a toolbox). Never a
   grab-bag of decorative emoji.

---

## Block skeleton

Sections marked *(optional)* are omitted when the content does not call for them.
Everything else appears in this order.

```
1. COLD OPEN          > colored quote block carrying the hook or thesis
2. HERO IMAGE         (optional) image + fully formatted caption
3. ### **CONCEPT**    (optional) H3, bold
4. TOGGLE             <details>, summary = the one-line thesis
                      children = ### PURPOSE / ### LEADERSHIP style H3 + one bullet each
5. ---                divider
6. FRAMEWORK MEMBERS  repeated block, one per member, separated by ---
                      <callout icon="<series emoji>" color="gray_bg"> **NAME** </callout>
                      followed by **Bold label**: definition bullets
7. ### ALL-CAPS H3    named sub-sections; short bullets, then nested gray_bg callouts
                      holding exactly one idea each
8. NUMBERED LIST      when the idea is a progression or sequence (3 steps is the house length)
9. ### TAKE ACTION!   closer. 🚩 gray_bg callouts carrying the stat or the stakes
10. PUNCHLINE         final callout ends with `= <conclusion>` then the line in `inline code`
```

## Syntax reference (Notion enhanced-markdown dialect)

Children of a callout or toggle are indented with a **literal tab**.

```markdown
> Hook line with **bold**. {color="brown"}

### **CONCEPT**
<details>
<summary>One-line thesis goes here.</summary>
	### PURPOSE
	- One bullet.
</details>

---

<callout icon="☝🏽" color="gray_bg">
	**FRAMEWORK MEMBER NAME**
</callout>
- **Definition**: what it is.
- **Goal**: what it achieves.

### ALL-CAPS SECTION
- Lead-in bullet.
	<callout icon="🪜" color="gray_bg">
		One idea, one callout.
	</callout>

### TAKE ACTION!
<callout icon="🚩" color="gray_bg">
	The stat or the stakes.
	= the conclusion `the punchline`
</callout>
```

## House conventions

| Element | Rule |
|---|---|
| Section headers | `###` H3, ALL CAPS |
| Callout color | `gray_bg` for every framework/idea callout. No color variety |
| Cold-open quote | `{color="brown"}` for origin/etymology hooks, `{color="blue"}` for mission/vision |
| Framework members | always a callout with the name in bold, never a bare heading |
| Bullet pattern | `**Bold label**: definition` |
| Dividers | `---` between framework members and between major sections |
| Progressions | numbered lists, 3 items where possible |
| Punchline | inline `code`, reserved for the one line the coach should remember |
| Page title | `<YEAR> S<N> - Title Case Name` for sessions; ALL CAPS for evergreen pages |
| Page icon | one emoji matching the page's semantic family |

## Gap-flag pattern

When source material names something it never defines:

```markdown
<callout icon="⚠️" color="gray_bg">
	**GAP:** <what is missing>. Recover from <where it might exist> before this page ships to coaches.
</callout>
```

Known open gaps as of 2026-08-11:

| Gap | Source | Where it might exist |
|---|---|---|
| "First Day of Practice" 5-step walkthrough | 2025 S2 deck, numbered placeholders, no content | Session 2 edited video |
| DR Team Non-Negotiables list | 2025 S2, QR/Form link only | `forms.gle/Q2Vp6MVfaa3dhZJt9` |
| 2025 Sessions 4 & 5 (Tennis / Volleyball Fundamentals) | video only, never written | DR TRAINING EDITED VIDEOS/ |
| "Conscious Coaching" Chapter 5 notes | 2024 FORMAT doc skips it | the book |
| 2023 Session 4 "Group Cheers" exercise | named in agenda, not on slides | coach memory |

**Resolved 2026-08-11:** the five fingers of THE HAND OF A COACH were flagged in the
Obsidian vault as never captured in writing. They were captured all along. The five
concepts documented immediately below that very gap flag *are* the five fingers, they
were just never labeled as such during extraction. Confirmed against Notion:
Locus of Control · Empathetic Feedback · Recognition · Negotiation · Psychological Safety.
Both vault notes have been corrected.

## Reference implementations

| Page | Status | What it demonstrates |
|---|---|---|
| BEING A COACH | handmade by Luis | cold open → hero image → progression → nested callouts → TAKE ACTION with stats |
| THE HAND OF A COACH | handmade by Luis | CONCEPT toggle → five framework members as a consistent emoji series |
| 2025 S2 - One Hundred 1% Solutions | built to contract | full skeleton end-to-end, including punchline and age-segment callouts |
