---
title: DR | COACH HUB — Page Design Standard
brand: Discipline-Rift
area: notion-design
note_type: standard
source_repo: CLAUDE-TRELLIS/domains/ops/notion/dr-coach-wiki/design-standard.md
synced: 2026-09-17
tags:
  - brand/discipline-rift
  - notion-design
up:
  - "[[01-Brands/Discipline-Rift/Notion/_index]]"
---

# DR | COACH HUB — Page Design Standard

Set 2026-09-06. Applies to every page in the DR | COACH HUB Notion wiki.

- Database: `3b904528-85a8-80f9-b1a8-fa3538cc11d2`
- Data source: `9e004528-85a8-8241-a291-073b041ed639`
- 108 pages, all rows of the wiki database

---

## 1. The problem this solves

Coaches were not clicking through to subpages. They did not know the pages existed.

Cause was not missing emojis — 103 of 108 pages already had icons. The cause was the **link type**. Newer index pages used plain markdown links, which render as bare underlined text and throw the target page's icon away.

The older COACH CURRICULUM page already did it right. This standard is a restoration of that pattern, not a new invention.

---

## 2. Link types — know which one you are writing

| Markdown | Renders as | Use |
|---|---|---|
| `[TEXT](url)` | bare underlined text, **no icon** | never for navigation; inline prose only |
| `<mention-page url="..."/>` | inline chip: target's **icon + live title** | default for all navigation |
| `<page url="...">TITLE</page>` | full-width row: icon + title | only when target is a real child page |

**The `<page>` rule.** `<page>` only works when the target is already a `child_page` block of the page you are editing. Everything else — data-source rows, unrelated pages — silently downgrades to a mention, or returns a 400. Since almost every hub page is a database row, **mentions are the normal case**. Full-width rows are the exception.

Both good types show the icon. That icon is the affordance. It is the whole fix.

---

## 2b. Navigation rule — every subpage is visibly tappable (set 2026-09-16, Cristian)

Problem observed live on 2026-09-16: coaches still skip subpages. On a phone the mention chip shows
the target icon with a small "open" arrow overlaid, and coaches read it as decoration, not as a door.
START HERE still says "Schedule (linked in Notion)" in prose instead of putting the door right there.

**The rule.** If a coach needs to open a page, the link to it must look like a button, not like a word.

1. **Every navigation link gets a leading arrow and is bold.** Write it as
   `**→** <mention-page url="..."/>` on its own line. The arrow is plain text before the chip, so it
   renders on every client. Never a bare chip mid-sentence for something a coach must open.
2. **Primary doors get a heading.** On hub and index pages, the main destinations (the 6 hubs from
   the home page, the sport hub from CURRICULUM, the week page from a sport hub) go as
   `### → <mention-page url="..."/>` so they render bigger and bold. Secondary links inside a card
   stay as rule 1. *Verified 2026-09-17: `### → <mention-page/>` inside a callout is accepted by `API-update-page-markdown` and renders as a bold heading with the chip. Rolled out to every hub the same day.*
3. **No prose pointers.** Never write "linked in Notion", "see X", "linked here", "find it in the
   hub". Put the door on the next line. If the target exists, link it; if it does not exist, flag it
   with a ⚠️ yellow callout.
4. **External tools get the same treatment.** Coach Dashboard, the season schedule, the WhatsApp
   join link: `**→ [COACH DASHBOARD](https://disciplinerift.com/coach/)**`. Bold, arrow, uppercase
   title, one per line. Do not print the raw URL as its own line under a label.
5. **One-line italic under every door** stays mandatory (section 3, rule 3): what is behind it and
   when to open it. Arrow tells you it opens; the italic tells you why.
6. **The child-page rows Notion appends at the bottom of a page** (`<page>` blocks after the 🚩
   callout) are duplicates of doors already in the cards. Leave them; do not link to them from
   prose. Coaches should never need to scroll past the 🚩 callout to find a door.
7. **`[TEXT](url)` to a Notion page is a defect** everywhere, including inline prose. Replace with
   the chip. Section 2 already says this; this rule makes it auditable.

Grep for defects: `grep -n "linked in\|see the\|find it in" ` on any exported page, plus any
`<mention-page` not preceded by `**→**` or `### →`.

Applies to: every page in the database, every card, every callout. No exceptions for archive or
internal pages; they simply get fewer doors.

---

## 2c. Database properties — no Owner (set 2026-09-17, Luis)

The wiki's built-in **Owner** (people) property was removed from the `DR | COACH HUB` data source on 2026-09-17. It showed "CLAUDE" on every row and told a coach nothing.

- Do not re-add an Owner, Author, Created by or Assignee property to this database.
- Do not set a people property on new rows. The row properties a page carries are: Type, Sport, Section, Status, Order, Year, Verification, Last edited time.
- Do not mention authorship in page bodies either ("built by", "written by"). The page is DR's.
- If ownership of a page ever needs tracking, it goes in `CURRICULUM RESTRUCTURE` or the vault, not on the row.

---

## 3. The page recipe

Every index page follows this shape:

```
<callout icon="📢" color="gray_bg">
	Coach! [one line: what this page is for]. Every row below is a page: tap it.
</callout>
# PAGE TITLE
<callout icon="🏐" color="gray_bg">
	**SECTION LABEL**
	### → <mention-page url="..."/>
	*Status or one-line description.*
	**→** <mention-page url="..."/>
	*One line: what is behind it, when to open it.*
</callout>
<callout icon="/icons/brain_green.svg" color="gray_bg">
	**NEXT SECTION**
	**→** <mention-page url="..."/>
	*One line.*
</callout>
<callout icon="⚠️" color="yellow_bg">
	**GAP** — what is missing and what a coach should do instead.
</callout>
<callout icon="🚩" color="gray_bg">
	Read your week before you drive out, not in the parking lot.
</callout>
```

Rules:

1. Open with a `📢` gray callout addressed to **"Coach!"**, then the H1.
2. Group every set of links into a **gray callout card** with a bold label on line 1. The card edge is what makes the group scannable on a phone.
3. Italic one-liner under a link carries status: *Placeholder, needs content* · *Superseded* · *Not ready*. Never delete a status note to make a page look cleaner.
4. Known gaps get a `⚠️` **yellow** callout. Yellow means "do not go looking for this."
5. Close with a `🚩` TAKE ACTION callout.
6. Every door follows section 2b: arrow, bold, italic one-liner. No prose pointers.

---

## 4. Icon vocabulary

Structural cards use the DR green SVG set. Sport cards use the sport emoji. Do not freelance.

| Icon | Use |
|---|---|
| `/icons/flag-pennant_green.svg` | SHARED WITH EVERY SPORT |
| `/icons/brain_green.svg` | SKILLS |
| `/icons/gradebook_green.svg` | RESOURCES |
| 🏐 🏈 🎾 🏓 | volleyball · flag · tennis · pickleball |
| 📢 | opening "Coach!" callout |
| 💡 | clarifying note |
| ⚠️ (yellow_bg) | gap / not built yet |
| 🚩 | TAKE ACTION |
| 🎲 | games |
| 🏛️ | conferences |

Write SVG icons as `icon="/icons/brain_green.svg"`. Notion stores them as native icon objects (`{name: "brain", color: "green"}`).

---

## 5. How to apply it (API mechanics)

Use `API-update-page-markdown`. **Read the page first** and check `unknown_block_ids`.

| Page condition | Method |
|---|---|
| Clean, no child pages, no unknown blocks | `replace_content` |
| Has real child pages | `update_content` (targeted find-and-replace) |
| Has `<unknown/>` blocks | `update_content`, or leave alone |
| Page is only a PDF/file block | `insert_content` with `position: {type: "start"}` |

### Traps — all verified the hard way

- **`replace_content` destroys `<unknown/>` blocks.** Aliases and `copy_indicator` blocks vanish. Resolve them first with `API-retrieve-a-block` — an "alias" is usually just a `link_to_page` whose target you can reproduce as a mention.
- **`replace_content` scrambles child pages.** It interleaves them at original positions.
- **`update_content` CAN move child pages.** Remove the `<page url>` tag from its old location and reinsert the same tag in the new location, both as `contentUpdates` in the **same call**. Verified on COACH DASHBOARD.
- **Never rewrite a `<file src="file://...">` tag.** Re-emitting it risks the attachment. Insert around it instead.
- Leave `allow_deleting_content` unset. It defaults to false and protects child pages.

---

## 6. Status

### Applied

| Page | What changed |
|---|---|
| VOLLEYBALL CURRICULUM | 4 cards; 6 shared pages lifted out of a prose sentence into rows |
| TENNIS CURRICULUM | 2 cards + gaps callout |
| PICKLEBALL CURRICULUM | 2 cards; season table kept; weeks 4–6 gap flagged |
| FLAG CURRICULUM | 6 cards; alias block resolved to TIERS and preserved |
| COACH TRAINING | 4 cards; all descriptions kept |
| GAMES | card + not-yet-extracted callout |
| COACH DASHBOARD | 5 child pages **moved** up as full-width rows; duplicate link list deleted |
| READING SHELF | header + gap callout added above the PDF |
| **Navigation rule rollout (2026-09-17)** | §2b applied to every page with doors: 6 hubs, 4 sport hubs, 21 week pages, 7 problem pages, 4 method pages, 3 volleyball banks, 3 conferences, 5 templates, CURRICULUM RESTRUCTURE. Prose pointers removed. External doors (schedule folder, Dashboard) as `**→ [NAME](url)**`. Mirror under `COACH-HUB/` is stale for these pages until the next sync |
| START HERE / COACHING TODAY / TAKING ATTENDANCE / ARRIVAL / ROSTER / COACH DASHBOARD / DASHBOARD PROBLEMS | roster-email screenshot routine (no signal inside schools) added 2026-09-17 |
| READING SHELF (2026-09-17) | placeholder removed, seven books in three cards, PDF kept at the bottom |
| OUR CULTURE (2026-09-17) | one line expanded to kids / parents / each other, sourced from FUELED, CORE VALUES, BEING A COACH |

Icons set on 5 bare pages: 🔑 LOGGING IN · ✅ TAKING ATTENDANCE · 🗓️ HOW THE SCHEDULE WORKS · 💬 MESSAGING PARENTS · 🛟 WHEN SOMETHING BREAKS

### Deliberately not touched

**COACH CURRICULUM** — already compliant, and holds 11 `copy_indicator` blocks a write would destroy.

### Not done

1. **Naked PDF pages.** Coach opens the page and sees a raw PDF with no title or context. Same treatment as READING SHELF: DRILLS · VOLLEYBALL BOOKS · COACHING SCIENCE · NFL · NUGGETS · FUNDAMENTALS · DRILLS (coach-curriculum copy).
2. **Week and skill pages.** Most open on a bare `*(Developmental Volleyball)*` line with no callout and no H1. MOVING and DEFENDING have no H1 at all. ~40 pages. Mechanical, low risk, high consistency win.
3. **Raw list pages.** VOLLEYBALL TIERS and TIER SYSTEM are bold text lists with no header or card.

---

## 7. Open decisions — need Luis

These block work, they are not design calls.

- **Duplicates.** PASSING · SETTING · SERVING · ATTACKING · DEFENDING · MOVING · COMMUNICATING · DRILLS · TERMINOLOGY · TIERS each exist twice (COACH CURRICULUM copy + sport copy). WEEK 1–6 exist twice. Coaches can land on the wrong copy. Which is canonical?
- **Wiki properties are empty on all 108 rows** — Type, Sport, Section, Status, Order, Year. Filling Sport + Section would let the hub home filter to "show me only volleyball." Bigger navigation win than anything above.
- **Content gaps, not design gaps:** volleyball Week 6 duplicates Week 3 · pickleball weeks 4–6 do not exist · WORKSHOPS is five titles with no content · ARRIVAL / DISMISSAL / EMERGENCIES / INCIDENTS / PARENTS carry open "FOR LUIS" question blocks.
