---
brand: Discipline-Rift
area: projects
subarea: coach-hub-rebuild
note_type: playbook
status: active
canonical: false
used_for_ai: true
source_type: mirror
source_reference: "Canonical copy is domains/ops/notion/dr-coach-wiki/sport-curriculum-rebuild-playbook.md in the CLAUDE-TRELLIS repo. This vault file is a mirror for Obsidian-side discovery; if the two disagree, the repo file wins."
owner: Luis
last_updated: 2026-09-22
sensitivity: internal
hub_role: leaf
up:
  - "[[01-Brands/Discipline-Rift/04-Projects/Coach-Hub-Rebuild/Coach-Hub-Rebuild-Home]]"
related:
  - "[[01-Brands/Discipline-Rift/05-Operations/Training/Method/Method-Home]]"
  - "[[01-Brands/Discipline-Rift/04-Projects/Coach-Hub-Rebuild/DR-Notion-Curriculum-Change-Proposal-2026-09-17]]"
---

# Sport Curriculum Rebuild — reusable session playbook

> [!info] Mirror, not canonical
> This is a vault mirror of `domains/ops/notion/dr-coach-wiki/sport-curriculum-rebuild-playbook.md` in the CLAUDE-TRELLIS repo. That repo file is the source of truth (git history, gets edited first). Re-sync this file when the repo file changes.

**Why this exists:** the tennis rebuild (2026-09-21) worked, but it took several rounds of correction across one long session — and mid-rollout a *second, parallel session* had already rebuilt large parts of the same live Notion pages, which nearly caused silent overwrites and duplicate pages. Doing this for flag football, pickleball, or any other sport, split across multiple future sessions with limited context per session, needs the workflow turned into copy-paste prompts — not re-derived from memory each time.

These two prompts are final, generated and refined across the tennis rebuild session. **Prompt 1** reconciles a sport's *old curriculum* (the pre-rebuild material DR was already using) against the current live Notion build. **Prompt 2** does the same job for *external sport books/resources* attached as source material. Both converge on the same output shape: a coverage-mapped Gamified Challenge bank, a real change proposal with an approval gate, and a disciplined apply/verify/changelog phase. Use whichever matches what's attached to the session — sometimes both, back to back, on the same sport.

---

## Prompt 1 — Old curriculum reconciliation

Use when the attached files are **the sport's own retired/legacy curriculum** — old PDFs, exports, drill lists, progression systems DR was using before the Notion rebuild.

```
We are working on the curriculum for [SPORT].

I am attaching the old curriculum and old curriculum resources for this sport to this
session.

These attached files are the historical source material you must analyze. They may
include a PDF of the old curriculum, old curriculum exports, games, drills, activities,
progression systems, visuals, teaching instructions, season structures, or other
archived curriculum material.

Your job is to:

1. Exhaustively analyze the OLD curriculum/resources ATTACHED TO THIS SESSION.
2. Use the Notion MCP to access the CURRENT live DR curriculum inside the DR | COACH HUB
   Notion page.
3. Read the current live curriculum deeply enough to understand what is actually there
   today.
4. Reconcile the attached old curriculum against the current curriculum.
5. Determine what valuable material was preserved, lost, superseded, weakened, or should
   be adapted.
6. Improve the current curriculum structure, progression ladders, skill/problem logic,
   and Gamified Challenge banks using the strongest grounded material from the old
   curriculum.
7. Produce a complete change proposal before modifying anything in Notion.

The goal is NOT to restore the old curriculum.

The goal is to make the CURRENT DR curriculum stronger using anything valuable that can
be recovered from the old curriculum attached to this session.

---

# SOURCE PRECEDENCE

When sources disagree, use this hierarchy:

1. Current DR Method / approved DR teaching methodology
2. Current approved sport-specific methodology, tiers, sequencing, or progression
   documents
3. Current live curriculum inside DR | COACH HUB, accessed through the Notion MCP
4. Old curriculum/resources ATTACHED TO THIS SESSION

The old curriculum is source material. It does not automatically override the current
DR methodology.

---

# PHASE 1 — READ THE CURRENT LIVE CURRICULUM

Use the Notion MCP. Find DR | COACH HUB. Locate the live curriculum for [SPORT]. Pull the
current state fresh.

Do NOT rely on: memory, previous Claude sessions, previous ChatGPT sessions, an old
Notion export, a previous description of the curriculum, a previously generated
proposal.

Read what is actually live now. Inspect all relevant areas, including where applicable:
sport hub, season structure, practice/week structure, skill pages, skill subpages,
progression ladders, problems, evidence/mastery criteria, Warm-Up Games, Gamified
Challenges, CFU Games, other activity/game banks, individual challenge cards, skill
connections, tier/sequencing pages, coach instructions, existing visuals.

Do not stop at index pages. Open the actual child pages and individual challenge cards
when needed to understand what already exists. Before calling something missing, verify
that it is not already covered somewhere else under a different name.

---

# PHASE 2 — ANALYZE EVERY ATTACHED OLD CURRICULUM RESOURCE

Read every old curriculum resource ATTACHED TO THIS SESSION. Create an inventory
showing: file/source, skills covered, subskills, teaching cues, common problems,
corrections, progressions, games, drills, gamified activities, CFU concepts,
competitive activities, season structure, tier/progression concepts,
assessment/evidence, visuals, coach instructions, other useful curriculum material.

Do not silently ignore content. If multiple resources repeat the same concept,
reconcile them instead of counting them as separate ideas.

---

# PHASE 3 — EXTRACT THE OLD MATERIAL

For every meaningful SKILL or teaching component, capture: skill, purpose, technical
sequence, key cues, common player problems, coach corrections, progression ideas,
evidence of success, connections to other skills.

For every GAME, DRILL, CHALLENGE, or ACTIVITY, capture: original name, source, skill
being trained, specific player problem it can help solve, setup, equipment, player
configuration, rules, scoring/win condition, how the round ends, progression,
easier/harder variations if provided, what the coach observes.

If a source names an activity but does not provide enough information to actually run
it, classify it as: NAMED BUT UNSOURCED — SOURCE REQUIRED. Do not invent the missing
rules.

---

# DR PROGRESSION LADDER METHODOLOGY

One of the most important parts of this reconciliation is evaluating and improving the
Progression Ladder. Using Level 1 / Level 2 / Level 3, or another clear progression
structure, is completely acceptable. What matters is what each rung actually
represents.

Every meaningful rung of the ladder should answer:
1. What SKILL are we working on?
2. What PROBLEM are the players currently having with that skill?
3. What GAMIFIED CHALLENGE are we using to solve that problem?
4. What VARIATION or progression changes the demand?
5. What EVIDENCE tells the coach the players are ready to progress?

Conceptually:
LEVEL/RUNG 1 — Skill → Problem → Gamified Challenge → Variation → Evidence
LEVEL/RUNG 2 — Skill → New Problem → Gamified Challenge → Variation → Evidence
LEVEL/RUNG 3 — Skill → New Problem → Gamified Challenge → Variation → Evidence

The ladder can progress in different ways.

## TYPE A — Multiple problems within the same skill

A player may continue working on the same skill while the problem changes. Example
(passing): Level 1 — Skill: Passing, Problem: cannot consistently create/control the
platform. Level 2 — Skill: Passing, Problem: can pass stationary but loses control when
moving. Level 3 — Skill: Passing, Problem: can move and pass but struggles with angles,
seams, communication, or decision-making. This is DEPTH within the skill.

## TYPE B — Multiple skills with multiple problems

The ladder may also progress across connected skills: Level 1 — Skill A, Problem A.
Level 2 — Skill B, Problem B. Level 3 — Skill A + Skill B, Problem C. This allows the
coach to move from isolated skill development into skill connection. The ladder does
NOT have to remain on only one skill.

## TYPE C — Different players may be on different rungs

Players working on the same skill may be solving different problems. Beginners may be
solving Skill: Passing / Problem: platform-contact, while advanced-beginners solve
Skill: Passing / Problem: movement, angles, seams, communication, or accuracy. The coach
may temporarily divide players into separate lines/groups/stations so each group works
the challenge appropriate to its current problem. This is not necessarily a permanent
player classification system. The important idea: group players according to the
problem they currently need to solve. A player may need a beginner-level challenge for
one skill and a more advanced challenge for another skill.

---

# GAMIFIED CHALLENGE DEFINITION

A Gamified Challenge is essentially a drill with a game component. It creates purposeful
repetitions while making the learning experience fun and engaging. The drill component
provides the skill repetition. The game component can include: points, teams, targets,
races, levels, zones, consecutive-success goals, personal records, team records,
accuracy goals, time challenges, player vs. player competition, team vs. team
competition, achievement thresholds, role upgrades, other appropriate game mechanics.
The game component must support the learning objective. Do not turn a drill into a
random competition that destroys the technique being taught.

# PLAYER PROBLEM → GAMIFIED CHALLENGE

Gamified Challenges should not exist as random games. Every challenge must answer: what
problem does this solve? The bank should function conceptually as: SKILL → PLAYER
PROBLEM → GAMIFIED CHALLENGE OPTIONS. Therefore, when reconciling the old curriculum, do
not merely ask "what games did we lose?" — ask: which player problems did these old
activities solve, and do we currently have strong Gamified Challenges for those
problems?

# GAMIFIED CHALLENGE VARIATIONS

Every strong Gamified Challenge should have useful variations, letting the coach adapt
the same challenge to the rung/problem players are currently working through. Example
(passing): pass, step + pass, shuffle + pass, call the ball + pass, change target,
change angle, seams/responsibility, add movement, add communication, connect pass into
the next skill. These are examples only — use the actual needs of the sport and
attached source material. Variations should intentionally manipulate: movement,
distance, direction, accuracy, target size, speed, communication, decision-making,
pressure, opposition, number of players, skill connection, game realism. Do not add
random variations merely to make a card longer.

---

# PHASE 4 — RECONCILE OLD VS CURRENT

Compare the old curriculum against what is actually live inside DR | COACH HUB.
Classify material as:

ALREADY PRESERVED — the current curriculum already contains the concept or an improved
version.
RESTORE — valuable old content disappeared and remains compatible with current DR
methodology.
ADAPT — the original idea is valuable, but its old format needs to become a modern DR
skill page, challenge, ladder step, CFU, etc.
ENRICH — the current curriculum is correct but the old resource adds useful depth.
SWAP — a weak current challenge can be replaced with a stronger grounded challenge.
ADD — a valuable concept fills a genuine current gap.
SUPERSEDED — the old material was intentionally replaced by a stronger current
methodology. Do not restore it.
DUPLICATE — the same function already exists in the current curriculum under another
title.
RETIRE — the old approach conflicts with current DR methodology.
SOURCE GAP — the old source suggests something existed but does not provide enough
information to reconstruct it honestly.

---

# PHASE 5 — AUDIT AND IMPROVE THE GAMIFIED CHALLENGE BANKS

This is a MAJOR output of this work. Do not merely verify that a challenge bank exists.
Determine whether the bank gives coaches enough solutions to the actual problems
players encounter.

For EVERY major skill, identify: the main problems beginner players are likely to
experience; the main problems advanced-beginner players are likely to experience;
problems that appear later as the player progresses; which current Gamified Challenges
solve each problem; which old curriculum activities solved those problems; which
current challenges and old activities are duplicates; which problems currently have
multiple strong solutions; which problems have only one weak solution; which problems
have no good Gamified Challenge; which old drills/games can be adapted into stronger DR
Gamified Challenges; which challenge variations are needed to make progression
possible.

Create a coverage map conceptually like:

| Skill | Level/Rung | Player Problem | Current Challenge | Old Resource Candidate | Recommendation | Variations | Evidence |
|---|---|---|---|---|---|---|---|

The objective is NOT to have the largest possible activity bank. The objective is:
every important recurring player problem should have useful Gamified Challenge options
available to the coach.

# DEVELOPING GAMIFIED CHALLENGES FROM OLD MATERIAL

If the old curriculum contains a useful drill but it is not gamified enough, do not
automatically reject it. Determine whether its learning mechanism can become a
stronger DR Gamified Challenge. For each candidate ask: what skill does it train? what
specific problem does it solve? which ladder rung/level could it serve? which players
would benefit? what is the core repetition? what game mechanic can make it engaging?
how does the player/team score or progress? what easier/harder variations make sense?
what does the coach watch for? what evidence signals the player should move to the next
rung? Do not invent technical teaching principles unsupported by the sources or current
DR methodology.

# REQUIRED GAMIFIED CHALLENGE INFORMATION

A strong challenge should communicate enough information for a coach to run it without
guessing. Use the current DR Notion design standard, but conceptually include: Skill,
Problem, Level/Ladder Fit, Setup, Challenge, Game Component, Progress/Win, Variations,
Coach Watches For, Evidence, Next Problem.

---

# PHASE 6 — RECOVER VISUALS

Inspect the attached old curriculum for visuals worth recreating. For each worthwhile
visual identify: source, current Notion page, what it shows, why it improves coach
understanding, what a recreated visual should contain. Examples: body positioning,
movement sequence, contact point, court/field position, spacing, activity setup,
progression ladder, decision-making. Do not recommend visuals solely for decoration.

---

# PHASE 7 — FINAL RECONCILIATION REPORT

DO NOT MODIFY NOTION YET.

First give me: 1) current live curriculum structure, 2) attached old-resource
inventory, 3) material already preserved, 4) valuable content that appears to have been
lost, 5) content to restore, 6) content to adapt, 7) pages to enrich, 8) activities to
swap, 9) old systems that should remain retired, 10) duplicate material, 11)
Progression Ladder improvements, 12) Gamified Challenge bank coverage analysis, 13)
new/adapted Gamified Challenges proposed, 14) missing player-problem coverage, 15)
variation opportunities, 16) visuals worth recreating, 17) remaining source gaps, 18)
exact current Notion pages affected.

Every change should use: KEEP, RESTORE, ADAPT, ENRICH, SWAP, ADD, RETIRE, DUPLICATE,
SOURCE GAP. Use actual Notion links wherever possible.

---

# APPROVAL GATE

STOP. Do not change the live curriculum until I explicitly approve the proposed scope.

After approval:
1. Re-fetch each specific page through the Notion MCP immediately before editing.
2. Confirm its current content.
3. Check whether another session added equivalent content.
4. Preserve strong existing work.
5. Preserve existing page IDs whenever practical.
6. Avoid duplicate pages/cards.
7. Apply only approved changes.
8. Re-fetch after each significant change.
9. Confirm the page rendered correctly.
10. Verify child pages, links, mentions, tables, and unrelated content remain intact.
11. Produce a changelog.

The final objective is: use the OLD CURRICULUM RESOURCES ATTACHED TO THIS SESSION to
strengthen the CURRENT [SPORT] curriculum inside DR | COACH HUB, especially its
Progression Ladders and Gamified Challenge banks, without undoing improvements already
made.
```

---

## Prompt 2 — Sport books / resource enrichment

Use when the attached files are **external sport books or curricula** (not DR's own old material) — e.g. youth-coaching resources, national-federation guides, third-party activity decks, supplied as Markdown.

```
We are improving the CURRENT live DR curriculum for [SPORT] using the sport
books/resources I am attaching to this session as Markdown (.md) files.

The Markdown files ATTACHED TO THIS SESSION are the source books you must analyze. Do
NOT assume books from another conversation or session are available.

The current DR curriculum is located in Notion inside the DR | COACH HUB. You MUST use
the Notion MCP to access it.

Your job is to:

1. Exhaustively analyze every sport-book Markdown file ATTACHED TO THIS SESSION.
2. Use the Notion MCP to pull the current [SPORT] curriculum fresh from DR | COACH HUB.
3. Understand the current skills, problems, Progression Ladders, challenge banks,
   CFUs, and season structure.
4. Compare the book content against what is actually live.
5. Identify where the books provide genuine additional value.
6. Use the books to improve the curriculum, especially the Progression Ladders and
   Gamified Challenge banks.
7. Develop new/adapted Gamified Challenges when grounded book material provides a
   useful learning mechanism.
8. Produce a complete proposal before modifying Notion.

This is an ENRICHMENT and DEVELOPMENT workflow. Do not automatically rebuild things
that are already strong.

---

# SOURCE PRECEDENCE

1. Current DR Method / approved teaching methodology
2. Current approved sport-specific methodology, tiers, sequencing, or progression
   documents
3. Current live curriculum inside DR | COACH HUB, retrieved through the Notion MCP
4. Sport books/resources ATTACHED TO THIS SESSION

The books provide knowledge, activities, games, teaching concepts, and potential
solutions. They do not automatically override DR methodology.

---

# PHASE 1 — PULL THE CURRENT LIVE CURRICULUM

Use the Notion MCP. Find DR | COACH HUB. Locate [SPORT]. Pull the current live
curriculum fresh. Do not rely on: previous conversations, memory, previous exports,
previous proposals, previous descriptions of the Notion structure.

Inspect enough of the live curriculum to understand: skills, subskills, skill teaching
pages, problems, corrections, Progression Ladders, evidence/mastery, Warm-Up Games,
Gamified Challenges, CFU Games, other game/activity banks, individual challenge cards,
skill connections, season progression, tier/sequencing structure, coach instructions,
existing visuals. Do not stop at the bank indexes — read individual cards when
evaluating whether something already exists.

---

# PHASE 2 — BUILD THE CURRENT BASELINE

Before evaluating the books, map what is already live. For every major skill,
determine: skill, existing ladder levels/rungs, problems currently identified,
Gamified Challenges currently connected to those problems, existing challenge
variations, evidence/mastery, skill connections, gaps.

The baseline should answer: what are we currently teaching? what player problems are we
currently designing for? what Gamified Challenges do coaches currently have available
to solve those problems? where is the bank thin?

---

# PHASE 3 — ANALYZE EVERY ATTACHED BOOK

Read EVERY Markdown book/resource ATTACHED TO THIS SESSION. Extract useful: skills,
subskills, technical cues, teaching sequences, tactical concepts, common errors, player
problems, corrections, drills, games, challenges, competitive formats, warm-ups,
small-sided activities, decision-making activities, progressions, assessments, CFU
concepts, coaching language, activity variations, visual concepts.

Do not limit extraction only to activities already formatted as games — a technically
valuable drill can become useful raw material for a DR Gamified Challenge. Do not use
outside knowledge to pretend the source says something it does not.

# ACTIVITY EXTRACTION STANDARD

For every sufficiently described drill/game/activity capture: exact name, source book,
skill, player problem, setup, equipment, player configuration, rules, scoring/win
condition if present, how the round/activity ends, progression, variations,
easier/harder versions, coach observation points, potential DR use.

If the book names an activity but does NOT explain it sufficiently, classify it: NAMED
BUT UNSOURCED — COMPANION RESOURCE REQUIRED. Do not invent the rules.

---

# DR PROGRESSION LADDER METHODOLOGY

The Progression Ladder can use Level 1 / Level 2 / Level 3, or additional levels/rungs
when justified — nothing wrong with numbered levels. What matters is that every rung
has curriculum logic. Every rung should identify: SKILL (what are the players learning
or applying?), PROBLEM (what's stopping success right now?), GAMIFIED CHALLENGE (what
drill-with-a-game-component solves it?), VARIATION (how do we modify demand?), EVIDENCE
(what does the coach need to see before progressing?).

## The ladder may deepen one skill

Several rungs may use the SAME skill while solving increasingly sophisticated problems.
Example: Level 1 — Passing / platform-contact. Level 2 — Passing / passing after
movement. Level 3 — Passing / angles-seams-communication-decision. Progression through
depth.

## The ladder may also connect multiple skills

Level 1 — Skill A / Problem A. Level 2 — Skill B / Problem B. Level 3 — Skill A + Skill
B / Problem C. Level 4 — Skill A + Skill B under movement/decision-making / Problem D.
Moves from isolated skill execution into skill connection and representative gameplay.

## Multiple player problems may exist at once

Not every player needs the same challenge. Beginners solving Passing/platform-contact,
advanced-beginners solving Passing/movement-accuracy-angles-seams — the coach may
temporarily divide players into lines/groups/stations, using a different challenge or
variation per group. Group according to the problem being solved. Do not permanently
lock players into one level across the entire sport.

---

# GAMIFIED CHALLENGE DEFINITION

A Gamified Challenge is a drill with a game component designed to create useful
repetitions while making the experience fun. The drill supplies the learning
repetition; the game mechanic supplies engagement. Possible mechanics: points, targets,
teams, races, levels, zones, streaks, personal records, team records, time challenges,
player vs. player, team vs. team, achievement thresholds, accuracy goals, role
upgrades, other appropriate mechanics. The mechanic must support the learning
objective. Fun is important, but the challenge must still solve a specific player
problem.

---

# PHASE 4 — MAP BOOK CONTENT AGAINST LIVE NOTION

Compare every useful book concept against what is actually live. Classify it as:

ALREADY COVERED — the current DR curriculum already handles it strongly.
ENRICH — current content is strong but the book adds useful depth (better cue, problem
definition, progression, variation, scoring, setup, coach observation, or success
evidence).
SWAP — a current activity is weak/generic and the book provides a stronger grounded
solution to the same problem.
ADD — the book fills a genuine curriculum gap.
ADAPT INTO GAMIFIED CHALLENGE — the book contains a useful drill or activity, but it
should be redesigned into the DR challenge format.
DUPLICATE — the same function already exists under another title.
SOURCE GAP — a curriculum problem exists but the attached books do not provide enough
grounded material to solve it. Do not fabricate the missing material.

---

# PHASE 5 — DEVELOP THE GAMIFIED CHALLENGE BANKS

This is a central objective of the book analysis. For EVERY major skill, determine:
problems beginners encounter; problems advanced-beginners encounter; new problems as
the skill improves; which problems correspond to each ladder level/rung; which current
DR Gamified Challenges solve those problems; which book activities could solve those
problems; which current/book activities are duplicates; which problems have several
strong solutions; which problems have thin coverage; which problems have no
appropriate Gamified Challenge; which book drills can be adapted into NEW DR Gamified
Challenges; which challenge variations can create additional progression without
requiring an entirely new game.

Build a coverage matrix conceptually like:

| Skill | Level/Rung | Player Problem | Current DR Challenge | Book Candidate | Recommendation | Variations | Evidence |
|---|---|---|---|---|---|---|---|

Do not aim for an arbitrary number of games. Aim for strong problem coverage.

# DEVELOPING NEW GAMIFIED CHALLENGES FROM BOOK MATERIAL

A book drill does NOT need to already look like a DR challenge. If its learning
mechanism is strong, determine how it can become one. For every candidate ask: Skill —
what's being trained? Problem — what exact player problem does it solve? Ladder Fit —
where could it fit? Core Repetition — what useful repetition does the original
activity create? Game Component — how can the repetition become engaging without
destroying its purpose (points, targets, teams, races, levels, streaks, zones, accuracy
goals, personal best, opponent challenge, time constraint)? Progress/Win — what defines
success? Variations — how can we alter it for different problems/player states? Coach
Watches For — what should the coach observe? Evidence — what indicates the problem is
improving? Next Problem — what's likely appropriate afterward?

# GAMIFIED CHALLENGE VARIATIONS

Variations are extremely important — a single well-designed challenge may solve
several related problems when the coach can manipulate the demand. Example (passing):
pass, step + pass, shuffle + pass, call the ball, change target, change platform angle,
read seams, add communication, add movement, connect the pass into another skill. These
are examples only — use the actual sport and source material. Variations may
manipulate: movement, distance, accuracy, direction, target size, speed, communication,
decision-making, pressure, defender/opponent involvement, player numbers, skill
combinations, game realism. Every variation should have a reason.

# REQUIRED CHALLENGE INFORMATION

When proposing a new or substantially rebuilt Gamified Challenge, provide enough
information for the coach to run it. Conceptually include: Skill, Problem,
Level/Progression-Ladder Fit, Setup, Challenge, Game Component, Progress/Win,
Variations, Coach Watches For, Evidence, Next Problem/Next Rung. Follow the CURRENT DR
Notion structure/design when actually writing the card — do not impose a new visual
format if the Coach Hub already has an approved card convention.

---

# PHASE 6 — CONNECTION BETWEEN SKILLS

Look specifically for book material that can create meaningful bridges. Possible
progression logic: Skill A → deeper Skill A; Skill B → deeper Skill B; then A + B → A +
B with movement → A + B with communication → A + B with decision-making → A + B under
pressure → representative gameplay. Do not force that exact pattern on every sport —
use the natural relationships between its actual skills.

# PHASE 7 — SEASON IMPACT

Do not automatically redesign the season because we found new games. Determine whether
the findings justify changes to skill sequence, progression timing, retrieval
opportunities, skill connections, challenge selection, CFUs, practice progression.
Continue respecting the DR idea of NEW + RETRIEVAL + CONNECTION. If the books
strengthen the banks but do not require changing the season architecture, say so.

# PHASE 8 — VISUAL OPPORTUNITIES

Identify book concepts that should become visuals in Notion. For each one identify:
book/source, exact current Notion page, what needs to be illustrated, why a visual
improves understanding, future image-generation brief. Potential categories:
technique, starting position, contact point, movement sequence, court/field
positioning, player spacing, activity setup, progression ladder, skill connection,
decision-making. Only recommend visuals with instructional value.

---

# PHASE 9 — CHANGE PROPOSAL

DO NOT MODIFY NOTION YET. Produce a detailed plan.

For every proposed book-derived improvement provide: change ID, source book, source
activity/concept, exact current Notion page, actual Notion link, skill, level/rung if
applicable, player problem, current DR solution, proposed solution, classification
(ALREADY COVERED / ENRICH / SWAP / ADD / ADAPT INTO GAMIFIED CHALLENGE / DUPLICATE /
SOURCE GAP), variations, evidence, progression impact, season impact, visual
recommendation if relevant.

Then provide a GAMIFIED CHALLENGE BANK DEVELOPMENT SUMMARY: for each major skill show
problems covered well, problems with thin coverage, problems with no challenge,
existing challenges to retain, existing challenges to enrich, book activities worth
adapting, new Gamified Challenges proposed, useful variations, duplicate candidates
rejected.

Then provide WHERE CHANGES LAND: for each affected Notion page show adds,
enrichments, swaps, new/adapted Gamified Challenges, duplicates rejected, remaining
gaps.

STOP. Wait for my explicit approval before modifying DR | COACH HUB.

---

# PHASE 10 — APPLY APPROVED CHANGES

After approval, before every page change: re-fetch the exact page via the Notion MCP;
confirm its current live state; check for newly added equivalent content; search/read
similarly named challenge cards; apply only the approved change. Prefer enriching an
existing page/card instead of creating a duplicate. Preserve existing page IDs
whenever practical. Do not replace a strong DR activity merely because a book contains
another activity. Do not add activities simply to increase quantity — the bank exists
to give coaches strong solutions to player problems.

# PHASE 11 — SOURCE INTEGRITY

Preserve source information for book-derived material using the current DR
source-note convention. Distinguish between: directly sourced activity, adapted
activity based on a source, DR-original challenge. If we significantly gamify or alter
a book drill, do not misrepresent the resulting DR challenge as verbatim book content.

# PHASE 12 — VERIFY

After every significant write, re-fetch the affected page through the Notion MCP.
Verify: content rendered correctly, tables work, page mentions/links work, child pages
remain intact, no duplicate pages/cards appeared, no unrelated content disappeared, the
challenge still fits the current DR Coach Hub design conventions. A successful write
response is not enough.

---

# FINAL CHANGELOG

At completion report: pages modified, existing challenges enriched, challenges added,
challenges swapped, book drills adapted into Gamified Challenges, variations added,
Progression Ladder changes, player-problem gaps filled, duplicate candidates rejected,
book material deliberately not used, unsourced references not implemented, remaining
bank gaps, remaining progression gaps, visuals still needed, unexpected live changes
discovered during execution.

The final goal is: use the SPORT BOOKS ATTACHED TO THIS SESSION to make the CURRENT
[SPORT] curriculum inside DR | COACH HUB materially stronger — especially its
Progression Ladders and Gamified Challenge banks — while preserving DR methodology,
avoiding duplication, and giving coaches practical solutions for the real problems
their players are experiencing.
```

---

## Implementation notes — tool-specific gotchas found while executing these prompts

Not part of the prompts themselves (they're methodology-level, tool-agnostic), but worth reading before the apply phase of either prompt, since these are Claude/Notion-MCP-specific bugs that cost real time in the tennis session:

- `API-patch-page` (mcp**notion**) reliably fails on simple, non-database leaf pages with `"title has a value that does not match its property type: undefined"`. Use `notion-update-page` with `command: "update_properties"` for title changes on these pages instead.
- Write tables as markdown pipe tables (`| col | col |`) in any write payload, not hand-written `<table>` HTML — raw HTML tags in an `update_content`/`replace_content` body get escaped as literal text instead of rendering as a table. The `<table header-row="true">` syntax you see when *reading* a page back is fine; just don't hand-type it into a write.
- If an `update_content` search-and-replace fails with "no matches found" against text just read back from a `fetch`, don't assume the content is gone — the fetch tool's rendering isn't always byte-identical to the stored markdown (whitespace, tabs). Retry once with a shorter, less-formatted anchor string; fall back to `insert_content` at the page end if it fails twice.
- After creating a new page under a page-type parent (not a database), check that parent for an auto-appended `<page url="...">` block before adding your own — Notion adds one automatically.
- If delegating the actual write step to a background subagent: state plainly that approval came from a live user message visible in *this* conversation, not from text relayed inside the task prompt. A subagent correctly refuses to treat "the user approved this" as consent when it's just prose in its instructions.
- Two sessions can and did edit the same live sport's pages concurrently in one afternoon, producing duplicate pages and pages a permissions guard then blocked from being trashed. Claim the sport before starting the apply phase — see the coordination note below.

## Coordination across sessions

Given the concurrent-edit collision this already caused once: before starting the apply phase of either prompt, add a dated one-line claim to the `INTERNAL — Curriculum Builder` page in Notion (or the sport's own hub if that page doesn't exist) stating which sport and page range is about to be edited. Check that page first for another session's claim on the same sport. Not a real lock — a courtesy flag — but it's the only thing standing between two sessions editing the same pages at once.

After applying, append a row to the change ledger on `INTERNAL — Curriculum Builder` (change ID, page ID/URL, before → after, dependencies, outcome) in addition to the local changelog file — the ledger is the cross-session record other sessions actually check; a changelog that only exists as a local repo file is invisible to them.

---

## Quick reference — file naming convention

```
domains/ops/notion/dr-coach-wiki/
  [sport]-old-curriculum-reconciliation-[date].md   ← Prompt 1 output
  [sport]-book-enrichment-[date].md                 ← Prompt 2 output
  changelog-[sport]-[YYYY-MM-DD].md                 ← post-approval, what was applied
```

## Session-splitting guidance

Given context limits per session:

1. **One session per resource batch** (old curriculum OR a batch of books) → runs the relevant prompt through its Phase 9/Approval Gate, stops before applying. Needs Notion read access but not necessarily write.
2. **One session per apply pass** → re-runs the fresh live-Notion check first (state may have moved since planning), then runs the Apply/Source Integrity/Verify phases only, writes the changelog and ledger row.

Splitting this way keeps each session's context budget on either analysis or writing, not both at once — which is what made the tennis session run long.
