---
title: Discipline Rift: Coach Hub Architecture
brand: Discipline-Rift
area: notion-design
note_type: standard
source_repo: CLAUDE-TRELLIS/domains/ops/notion/dr-coach-wiki/template-architecture.md
synced: 2026-09-17
tags:
  - brand/discipline-rift
  - notion-design
up:
  - "[[01-Brands/Discipline-Rift/Notion/_index]]"
---

# Discipline Rift: Coach Hub Architecture

> **SUPERSEDED 2026-08-11.** This document carries the six-section model
> (Start Here / DR Training / How We Practice / Curriculums / Coach Operations / Resources).
> That model was replaced twice: first by a five-section model, then by the final section
> names after `THE FLOOR` and `WHEN IT GOES WRONG` were rejected. Do not build from this file.
>
> Live documents, in reading order:
> 1. [restructure-analysis.md](restructure-analysis.md), the audit and the rulings
> 2. [main-page-design.md](main-page-design.md), the five sections and the root layout
> 3. [subpage-restructure.md](subpage-restructure.md), every page and what happens to its body
> 4. [page-templates.md](page-templates.md), the block template per page type
> 5. [migration-plan.md](migration-plan.md), the order of operations
>
> What is still worth reading here: the session inventory, the 2024 three-talk structure,
> the 153-method vault sweep, and the contradictions list. The section model is not.

One Notion hub for every coach, every sport. Not one wiki per sport.

- **Hub:** `DISCIPLINE RIFT | COACH HUB` — https://app.notion.com/p/3b90452885a880f9b1a8fa3538cc11d2
- **Data source:** `9e004528-85a8-8241-a291-073b041ed639`
- **Page body format:** [session-page-contract.md](session-page-contract.md)
- **Built from:** a full sweep of all 249 markdown files in the Discipline Rift Obsidian
  vault (8 parallel readers, 2026-08-11) plus every page in the Notion source.

---

## The design rule

A coach opens this hub with one of six questions. Each question is one section.
Nothing else earns a top-level slot.

| A coach asks | Section |
|---|---|
| Who are we, and what do I stand for? | **START HERE** |
| How do I get better at coaching? | **DR TRAINING** |
| How do I run a practice? | **HOW WE PRACTICE** |
| What am I teaching this week? | **CURRICULUMS** |
| What do I owe after practice? | **COACH OPERATIONS** |
| Where do I read more? | **RESOURCES** |

Skills and weeks are **not** top-level. They live inside their sport's curriculum,
because a coach only ever needs them in the context of a season.

Methods are stated **once**, in HOW WE PRACTICE, because the method is the same in
every sport. Only the sport's content changes.

---

## Database properties

| Property | Values |
|---|---|
| `Section` | Start Here · DR Training · How We Practice · Curriculums · Coach Operations · Resources · Forms |
| `Type` | Hub · Topic · Conference · Curriculum · Week · Skill · Method · Glossary · Reference · Form |
| `Sport` | All Sports · Volleyball · Tennis · Pickleball · Flag Football |
| `Year` | 2023 · 2024 · 2025 (conferences and the topics first taught there) |
| `Status` | Live · Draft · Needs Recovery |

Existing `Page`, `Verification`, `Last edited time` are unchanged. `Owner` was removed 2026-09-17 (design-standard §2c): never re-add it. `Verification`
is already the right "a human signed this off" mechanism — use it, don't replace it.

**Views to build once:** Board by `Section` (the front door) · Board by `Sport` filtered
to `Section = Curriculums` · Table filtered to `Status = Needs Recovery` (the work queue) ·
Board by `Year` filtered to `Type = Conference`.

---

## 1. START HERE

Who we are. A coach reads this once, in week one, and never needs it again.

| Page | State |
|---|---|
| START HERE — mission & vision | live, handmade |
| OUR CORE VALUES — Humility/Humble · Perseverance/Hungry · Adaptability/Smart | live, handmade |
| OUR CULTURE — FUELED is how we do things, values are how we connect | live, handmade |
| THE SIX CORE PILLARS — Decide · Plan · Feedback · CFU · Culture · Growth | build |
| WHAT WE PROMISE FAMILIES — the auditable season promise + 3 deliverables | build |
| WHO YOU ARE COACHING — the 7 student design constraints (S1–S7) | build |

---

## 2. DR TRAINING

Coach development. Two things live here, and the distinction matters:

- **Topics** — evergreen. What a coach needs to know. Rewritten to the page contract.
- **Conferences** — historical. What was taught on a given day, who presented, run of show.

A conference page is a thin index that links to the topics it covered. The content lives
in the topic. This is why "Being a Coach" is a topic, not a session artifact — it was
2023 Session 1, but what it teaches is permanent.

### Topics

| Page | State |
|---|---|
| WHAT IT MEANS TO BE A COACH | live, handmade · was `BEING A COACH` |
| THE HAND OF A COACH — 5 leadership skills | live, handmade |
| FUELED — HOW WE COACH | live · was `DR METHOD` · **error fixed, see below** |
| THE COACHING FORMULA — Knowledge + Skill × Attitude² | live · was `DR FORMULA` |
| COACH EXPECTATIONS — the 10 standards | live · was `DR TEAM` |
| ONE HUNDRED 1% SOLUTIONS | live · built to contract as the reference implementation |
| TALENT = SKILL + PASSION — incl. M+/M−/M+ and the Chicago study | build |
| BUILDING AN IRRESISTIBLE ENVIRONMENT — incl. the DR Coach Approach | build |
| ROW THE BOAT — the oar, purpose/mission/vision | build |
| THE GOLF BALL — dimples as lived experience | build |
| YOUR TWO GOALS — teach life lessons, develop talent | build |
| LEADING DIFFERENT GROUPS — Group A (K–2) vs Group B (3–5) | build · in Tennis + Pickleball vault, missing from Notion |
| COACHING BY AGE — Funny Joes (K–2) and Cool Jess (3–5) | build |
| FEEDBACK THAT WORKS — sandwich method, specific/actionable/timely, recognition-to-correction balance | build |
| NO YELLING — reasoning-first correction | build |
| CONFIDENCE RECOVERY — lower the bar, raise empathy | build |
| SIGNS OF MENTAL GROWTH — the observable-behaviour checklist | build |
| THE PARENTS YOU WILL MEET — P1–P10 and what to do about each | build |
| THE SEVEN COACH FAILURE MODES — C1–C7 | build |

### Conferences

| Page | State |
|---|---|
| 2023 CONFERENCE — DR Team Fall Training · 2:00–5:30 PM, 735 Herndon Ave · Luis & Diego | build · 5 sessions + scavenger hunt |
| 2024 CONFERENCE — three talks | build · see below |
| 2025 CONFERENCE — "relationship-first youth sports" | build · 3 written sessions + 2 video-only |

**2024 ran as three talks**, per Luis's agenda — theme: *lead with purpose and enthusiasm ·
connect · coaches are more than employees, they are the leading role of the team · you are
a leader, you are a friend, you are a role model.*

- **Talk 1** — company overview · journey as fallouts · core values · player impact: the three
  coaching-team fallouts (lack of commitment, lack of resources, lack of valuable content)
- *Game · Break*
- **Talk 2** — coaches training: analogy → connect the dots → actual content. The analogies are
  The Golf Ball and Row the Boat; the content is Your Two Goals, Talent = Skill + Passion,
  Irresistible Environment. Links to those topics rather than restating them.
- **Talk 3** — testimonials: Justin, Shannon. **Never captured.** Stub + gap flag.
- Reference: Conscious Coaching notes, Ch. 1–4 and 6. Ch. 5 missing.

Backlog ideas recorded in the 2024 agenda but never built into slides — keep as backlog on
the Talk 2 page, do not invent into content: *core values applied on court · consequences,
everything is earned · curriculum, go the extra mile.*

### Workshops

| Page | State |
|---|---|
| WORKSHOP TRACK 1–5 — beginners · safety · practice structure · positive correction · running a clinic | **Needs Recovery** — the five workshops are named as DR's stated training standard but never written. This is the biggest single content gap found. |

---

## 3. HOW WE PRACTICE

The universal method. Sport-agnostic, stated once, used every session. This section is the
product — it is what makes a DR practice a DR practice.

| Page | State |
|---|---|
| THE PRACTICE STRUCTURE — 7 BLOCKS | live · was `DR PRACTICE`, the Discipline Rift Universal Practice Structure |
| THE 60-MINUTE CLOCK — B1–B7 timings with one coach action each | build |
| WARM-UP — movement prep & practice primer (Quick Feet → Step → Pivot) | build |
| THE VOCABULARY TRANSFER RULE — why the warm-up names the movement | build |
| DECISION-RESPONSE TRAINING — See → Decide → Act | live · was `WHY DR PRACTICE?` |
| THE TIER SYSTEM — Ready → Control → Connector → Flow → Strategist → Leader | build · **this is the universal ladder, distinct from per-sport tiers** |
| PRACTICE-DEMAND TIERS — Tier 1/3/5 without splitting the group | build |
| THE PRACTICE METHODS — blocked · serial · interleaved · randomized · retrieval · spaced | build · incl. the canonical "how they intertwine" paragraph |
| CHECKING FOR UNDERSTANDING — Micro-CFU · observable evidence · exit criteria | build |
| THE SKILL TEACHING LOOP — breakdown → demo → imitation → correction → repetition | build · incl. Paso 1–4 |
| FAST TEACHING MOVES — perception question · freeze · recreate · replay | build |
| THE ONE-CUE RULE + the weekly coach self-check | build |
| MAXIMIZE EVERY MINUTE — the six operating standards | build |
| MEANING WINDOWS — 20–40s open · 1–2 freezes · 60s close | build |
| LIFE LESSON PROTOCOL — "Word of the Week" | build |
| THE LIFE LESSON BANK — what the sport teaches, in coach-sayable lines | build |
| JOB ZONE — elimination that still teaches | build · already referenced inside Week 1 with no page to link to |
| WEEK 1 CULTURE INSTALL — command presence · attention callouts · 4 non-negotiables · "scrimmage is earned" | build |
| ACTIONS & CONSEQUENCES + the 3 call-out rule | build |
| THE WEEK-1 DISCIPLINE DEFINITION — discipline is not punishment | build |
| THE COACH PHRASE BANK — what you actually say | build |
| ICE BREAKERS & TEAM BONDING — five named activities | build |
| THE LEADERSHIP LADDER — assistant coach pathway | build |
| SEASON GAMIFICATION — team XP · weekly badge ladder · constraint bonuses | build |
| PRACTICE DESIGN TEMPLATE — the five-section write-up a coach fills in weekly | build |
| WEEK-BEFORE PREP & DAY-ONE STANDARD | build |
| COACHING TERMS A–Z — ~70 terms in 9 families | live · was `TERMINOLOGY` |

---

## 4. CURRICULUMS

One page per sport. Weeks and skills nest inside. All four sports have complete
curriculums in the vault; only volleyball is in Notion today.

| Sport | In Notion | In vault |
|---|---|---|
| **VOLLEYBALL** | ✅ 6 weeks · 7 skills · tiers 1–6 · drills · books | + 7 skill modules with cue chains, Crab Position & the 3 P's, pass-vs-set rule |
| **TENNIS** | ❌ | 6-week cumulative-review progression · 6 tiers by stroke · forehand/backhand/volley/serve · handshake grip method · drill library · game-of-the-day library · Week 5 review + Week 6 assessment protocols · 180-row calendar |
| **PICKLEBALL** | ❌ | 6-week season · forehand drive/backhand/dink · drill & game library · shared warm-up · Simon Says |
| **FLAG FOOTBALL** | ❌ | 6 full 60-minute session plans · 8 skill domains · NFL FLAG cue set & progressions · Got It/Almost/Still Working feedback checklists · Zones Game · formations playbook (9×3) · agility & conditioning sets |

Each sport curriculum page carries: the 6-week focus order · the week pages · the skill
pages with their cue chains · the sport's tier table · its drill and game libraries · its books.

`WEEK 1 - PASSING & SETTING` is the model. It already implements all 7 blocks with coach
scripts, cues, Micro-CFUs, and add-on option menus. Every other week in every sport should
match it. It is the best-built page in the wiki.

---

## 5. COACH OPERATIONS

The job around the practice. Currently absent from Notion entirely, and it is the section
most likely to cause a real incident if a coach can't find it.

| Page | State |
|---|---|
| SESSION-DAY FLOW — log in · pick team · pick session · take attendance · message parents | build |
| THE TWO-MINUTE LOG — every session logged before you leave campus | build |
| PRACTICE REPORT + INJURY FORM — field by field, submit path, escalation triggers | build |
| WRITING A GOOD PRACTICE LOG — worked strong/weak examples | build |
| PER-SESSION CAPTURE — attendance · win moment · clips | build |
| ATTENDANCE & ABSENCE LOOP | build |
| SUPERVISION, DISMISSAL & SAFETY — bell to pickup | build |
| INJURY RESPONSE ON COURT — and who may clear a return to play | build |
| ACCIDENT REPORT | live |
| ESCALATION RULES — what you hand to a human instead of deciding | build |
| BEHAVIOR ESCALATION — talk to the parent before you remove a kid | build |
| COMMUNICATION BOUNDARIES — you message about the player, DR handles logistics | build |
| SPEAKING TO ADULTS — parent/faculty voice + the three promises nobody may make | build |
| AVAILABILITY, BLACKOUT DATES & TIME OFF | build |
| PRACTICE CANCELLATION — the coach-facing slice | build |
| ONBOARDING — three things before assignment | build |
| SEASON-CLOSE DUTIES + END OF SEASON CELEBRATION | build |
| DELIVERY ROLES — head coach · assistant/floater · program operator | build |
| PROGRAM PARAMETERS YOU MUST BE ABLE TO QUOTE — ratio, group size, grades, tiers, length | build |

---

## 6. RESOURCES

| Page | State |
|---|---|
| COACHING LIBRARY — The Coach's Guide to Teaching (Lemov) | live · was `COACHING SCIENCE`. Lemov is the intellectual source of DR's entire practice vocabulary. |
| VOLLEYBALL BOOKS | live · was `FUNDAMENTALS` |
| CHILDREN'S BILL OF RIGHTS IN SPORTS — Aspen Project Play | build · the external standard DR aligns coach training to |
| FOUNDER Q&A — 55 questions | build · optional, coach-relevant extract only |
| TALKS | slot, empty until content exists |

---

## What the sweep found that the wiki did not have

153 unique named methods across the vault. Of the 112 that apply to every sport:

- **49 are entirely missing from Notion**
- **40 are partially there** — named in one page but never given their own definition
- **23 are properly covered**

The largest missing clusters, in order of how often a coach would reach for them:
the warm-up architecture · the universal tier ladder · Job Zone · the Life Lesson
Protocol · Week 1 culture install · the whole of Coach Operations · the Workshop track.

## Contradictions that must be resolved before coaches read this

These are not gaps. These are places where the vault disagrees with itself, and a
coach hub cannot ship a contradiction.

1. **How many blocks is a practice?** Volleyball and flag football run **7 blocks**.
   Tennis and pickleball run **6**. One document calls a **5-block** format
   "non-negotiable." All three claim to be the standard. Pick one and make the others
   sport-level variations of it.

2. **Three different things are called "Tier System."** (a) the universal behaviour
   ladder Ready→Control→Connector→Flow→Strategist→Leader, (b) the practice-demand
   Tier 1/3/5 device for running a mixed group without splitting it, (c) per-sport skill
   tier tables. Rename (b) to *practice-demand tiers* and (c) to *<Sport> Tiers*.

3. **"DR Practice" means two things.** The `DR PRACTICE` page is the whole 7-block
   universal structure. `WHY DR PRACTICE?` uses "DR" to mean **Decision-Response** —
   the Block 5/6 decision layer. Renamed to `DECISION-RESPONSE TRAINING` to break the
   collision, but confirm that reading is right.

4. **FUELED was wrong in Notion — fixed.** The page said "5-Letter Acronym" and listed
   five: Friendly, Upfront, Enthusiastic, Leader, Efficient. FUELED is six. **Driven**
   was missing. Corrected in this hub; the live volleyball wiki still has the five-letter
   version.

5. **The vault flagged a gap that was never a gap.** Both staff-training notes recorded
   that the five fingers of The Hand of a Coach were never written down. The five
   concepts sitting directly below that flag *are* the five fingers — the extraction
   never labelled them. Both notes corrected 2026-08-11.

## Open gaps — named but never written

| Gap | Where referenced | Where it might exist |
|---|---|---|
| Workshops 1–5 content | stated as the coach training standard | nowhere in writing |
| "First Day of Practice" 5-step walkthrough | 2025 Talk 2 deck, numbered placeholders | Session 2 edited video |
| DR Team Non-Negotiables list | 2025, QR/Form link only | `forms.gle/Q2Vp6MVfaa3dhZJt9` |
| 2025 Sessions 4 & 5 — Tennis / Volleyball Fundamentals | video only | DR TRAINING EDITED VIDEOS/ |
| 2024 Talk 3 testimonials — Justin, Shannon | agenda only | coach memory |
| Conscious Coaching Ch. 5 | 2024 FORMAT doc skips it | the book |
| 2023 "Group Cheers" exercise | 2023 agenda, not on slides | coach memory |
| Coach-produced content standard | referenced as an expectation | undefined |

## Rebrand status

- Hub title → `DISCIPLINE RIFT | COACH HUB` ✅
- **Manual fix needed:** the database *description* still reads "©2024 COPYRIGHT. DR SPORTS
  & ATHLETICS, TORRES RIVERO LLC." The Notion API has no database-description endpoint, so
  this one line must be edited in the DB settings by hand. Should read
  `©2026 COPYRIGHT. DISCIPLINE RIFT, TORRES RIVERO LLC. ALL RIGHTS RESERVED`.
- The workspace account is already `DISCIPLINE RIFT / info@disciplinerift.com`.
