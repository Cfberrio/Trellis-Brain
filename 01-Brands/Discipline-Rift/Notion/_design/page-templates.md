---
title: Coach Hub: Page Templates
brand: Discipline-Rift
area: notion-design
note_type: standard
source_repo: CLAUDE-TRELLIS/domains/ops/notion/dr-coach-wiki/page-templates.md
synced: 2026-09-17
tags:
  - brand/discipline-rift
  - notion-design
up:
  - "[[01-Brands/Discipline-Rift/Notion/_index]]"
---

# Coach Hub: Page Templates

Strict block templates per page type. Two different authors following these should produce
structurally identical pages. If content does not fit the template, cut the content.

## Universal rules

1. **One in-body H1, matching the page title.** Index and hub pages open with the 📢 "Coach!" callout, then `# PAGE TITLE` (design-standard §3). The title appears twice, title bar and heading. That is intended, decided 2026-09-17 by Luis. Session pages built to the session-page-contract skip the H1 and open with the cold-open quote instead.
2. **Heading depth.** `##` for major sections, `###` for sub-sections. One `#` only (the title), and never skip
   a level.
3. **One emoji family per page.** No decorative grab-bags.
4. **Callout colour is `gray_bg`, except gaps.** A known gap, a not-built-yet, a safety override or a "do not go looking for this" is a `⚠️ yellow_bg` card (design-standard §3 rule 4, §4). Nothing else is coloured.
5. **`---` between major sections.** Never two dividers in a row, and never a trailing one.
6. **No fake formatting.** Never the U+0332 combining underline. Use real bold, or a real Notion
   underline annotation. Fake underline breaks search and copy-paste.
7. **No dashes as sentence punctuation.** Labels take a colon. Asides take a comma or brackets.
   Coach-facing copy reads worse with them and it is the fastest way to spot text nobody edited.
   Allowed: the en dash in a range or pairing (`26–27`, `2:45 / 3:15–4:15`, `arrival / start–end`, `WEEK 2–6`) and the em dash in a fixed page title (`WEEK 3 — DINKS`). Decided 2026-09-17.
8. **Every image is DR-hosted and captioned.** No external domains, and no expiring signed URLs
   in anything that will be exported.
9. **No authoring residue.** No "if you want, I can…", no "emphasize the internal analysis", no
   stray `@`, no trailing empty blocks. Grep for `If you want` before publishing.
10. **Every defined term links on first use**, or it is not a defined term.
11. **Sibling pages are identical in skeleton.** A missing section is a defect, not a variation.

## Diagram rule

A page earns a diagram only when the thing being taught is spatial, or has simultaneous moving
parts, such that a coach cannot execute it from text in ten seconds. Court layout, player
positions, movement paths, spacing. Everything else gets words.

Five conditions, all required:

1. **DR-authored and DR-hosted.** Never hotlinked. If DR did not draw it, DR does not ship it.
2. **Captioned** with the block it belongs to and the one thing to look at.
3. **No competing model.** A diagram may not introduce a framework that is absent from
   `COACHING TERMS`.
4. **Sport-labelled or sport-neutral.** On a page covering four sports, one volleyball diagram
   is a defect.
5. **One per page, under the heading it explains.** Never a stack. The default is zero images.

---

## WEEK PAGE

```markdown
<callout icon="🎯" color="gray_bg">
	**NORTH STAR:** <the one outcome>
	**CUE:** "<the one cue, in quotes>"
	**LIFE LESSON:** <the value, one line>
</callout>
<callout icon="⏱️" color="gray_bg">
	60 minutes. If you get 40, cut Block 4 to 8 and Block 6 to 8. Never cut Block 1 or 7.
</callout>
---
## BLOCK 1 · CULTURE ROUTINE + BELONGING · 2-3 min
**Coach does**
1. <numbered script>
**Micro-CFU:** <the check>
**Next:** <why Block 2 follows>
---
## BLOCK 2 · RETRIEVAL WARM-UP · 5-7 min
[... identical field set, every block, all seven ...]
---
## THE SWAPS
<details>
<summary>Pick ONE. Add no time.</summary>
	### <SWAP NAME>
	- **Setup** / **Run** / **Score** / **Focus**
</details>
---
## DRILL SOURCES
| Drill | Block | Source |
```

Every block carries exactly these fields, in this order, with these labels: `Purpose` ·
`Coach does` · `Practice emphasis` · `Micro-CFU` · `Exit criteria` · `Next`.

No substitutes. Not "Design:", not "Coach focus:", not "Design principles:", not "Fast teaching
moves:". A coach learns one scan pattern and then uses it seven times.

Exit criteria take a hit rate plus a process condition, as in *"3 of 5 over while holding the
finish."* Never a vibe.

Block names are fixed across all weeks and all sports. Block 5 is `DR TEACHING (GUIDED
DECISIONS)` everywhere. Block 7 is `DEBRIEF + RETRIEVAL + SPACING` everywhere.

The header field is labelled `NORTH STAR`. Not "Primary Learning Target", not "North Star skill",
not "North Star Learning Target".

---

## SKILL PAGE

```markdown
<callout icon="🎯" color="gray_bg">
	**<SKILL> BY NUMBERS:** 1 <name> → 2 <name> → 3 <name> → 4 <name>
	The order never changes. Only the movement added before position 1 changes.
</callout>
---
## POSITION 1 · <NAME>
- **Do:** <the action>
- **Why:** <one sentence>
- **Breaks when:** <the failure>
[image, captioned, if and only if the position is spatial]
---
[positions 2, 3, 4 with the identical field set]
---
## KEY TEACHING CUES
| Cue | Use when | Creates |
---
## COACH REMINDER
1. <root-cause question first>
...
- Fix one thing at a time.
---
## HOW IT PROGRESSES
- **Pattern A:** <early weeks>
- **Pattern B:** <around week 4>
```

Four positions is the canon. `DEFENDING`'s five is permitted only if the page documents it as a
deliberate exception. `KEY TEACHING CUES` and `COACH REMINDER` are both mandatory, because they
are the on-court lookup, and they are currently missing from four of seven pages.

---

## METHOD PAGE

For the cross-sport devices being lifted out of the week pages. Sport-neutral language only. If
the page needs a volleyball word, the example goes in a toggle labelled by sport.

```markdown
> <the device in one sentence> {color="brown"}
### **WHAT IT IS**
<details>
<summary><the one-line thesis></summary>
	### PURPOSE
	- <one bullet>
</details>
---
## HOW TO RUN IT
1. <step>
---
## WHEN TO USE IT
<callout icon="✅" color="gray_bg">
	<the trigger>
</callout>
<callout icon="🚫" color="gray_bg">
	<when not to>
</callout>
---
## IN YOUR SPORT
<details><summary>Volleyball</summary>	- <example></details>
<details><summary>Tennis</summary>	- <example></details>
<details><summary>Pickleball</summary>	- <example></details>
<details><summary>Flag Football</summary>	- <example></details>
---
### TAKE ACTION!
<callout icon="🚩" color="gray_bg">
	<the one thing to do next practice>
	= <conclusion> `<punchline>`
</callout>
```

---

## CONFERENCE PAGE

```markdown
> <the year's theme, one line> {color="brown"}
<callout icon="📍" color="gray_bg">
	<date/time> · <venue> · hosted by <names>
</callout>
---
### RUN OF SHOW
<table> # | SEGMENT | WHO | MIN </table>
---
<callout icon="📚" color="gray_bg">
	<span underline="true">**WHAT WAS TAUGHT**</span>
	**→** <mention-page url="..."/>
	*<what it covers>*
</callout>
---
### <SESSION N · NAME>   [only for sessions with no topic page]
---
<callout icon="⚠️" color="gray_bg">
	**GAP:** <what is missing> · <where it might be>
</callout>
```

A conference page is a record, not a teaching page. Content that is still true lives in a topic
page and gets linked. If a session's content exists nowhere else, it goes here with a gap flag
and never gets reconstructed.

---

## HUB PAGE

Per the vault convention, a hub carries judgment and a defect register rather than only links,
and every downward link is annotated.

```markdown
<callout icon="💡" color="gray_bg">
	<who this section is for and when to open it>
</callout>
<callout icon="⚠️" color="gray_bg">
	**NOT YET TRUSTWORTHY:** <page> · <why> · <owner>
</callout>
---
<callout icon="<family emoji>" color="gray_bg">
	<span underline="true">**<GROUP NAME>**</span>
	**→** <mention-page url="..."/>
	*<what it covers and when to open it>*
	**→** <mention-page url="..."/>
	*<what it covers and when to open it>*
</callout>
---
### TAKE ACTION!
<callout icon="🚩" color="gray_bg">
	<the one thing a coach should do with this section>
</callout>
```

A bare list of links is a defect, and every nav callout currently in the hub fails this.

Hubs also state provenance and supersession in prose: which source this mirrors, what was not
pulled and why, and what is defective upstream.

---

## Pre-publish checklist

- [ ] Title is 1-4 words, no mechanism suffix, no What/How/Why/When opener
- [ ] Exactly one in-body H1 on index/hub pages (none on session pages), heading levels unbroken
- [ ] Sibling pages share the skeleton exactly
- [ ] Every block carries the full field set with the standard labels
- [ ] No dashes as sentence punctuation; ranges and fixed titles may keep theirs
- [ ] Grep clean for `If you want` · U+0332 · stray `@` · trailing empty blocks · `TEAM ROSTERS`
- [ ] Every image DR-hosted and captioned, zero external domains
- [ ] Every defined term links to `COACHING TERMS` on first use
- [ ] Hub links annotated rather than bare
- [ ] No Owner / author / people property on the row, no "built by" in the body (design-standard §2c)
- [ ] Every door is `**→** <mention-page/>` (or `### →` for primary doors); zero `[TEXT](url)` to Notion pages; zero "linked in Notion" prose (design-standard.md §2b)
- [ ] Gaps flagged, never filled
