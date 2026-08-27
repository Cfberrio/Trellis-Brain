---
brand: Discipline-Rift
area: training
sport: Flag Football
note_type: home
status: active
canonical: true
used_for_ai: true
sensitivity: internal
source: Notion — DR FLAG FOOTBALL database (8b21e3be-6eda-420f-94c7-1bd858dee615)
pulled: 2026-08-11
---

# Notion Wiki Home — DR Flag Football

Full mirror of the Notion `DR FLAG FOOTBALL` space, pulled 2026-08-11. 33 top-level pages; every one is represented below.

In Notion this is a **flat database at workspace root** — no folders. Core Values sits at the same level as Week 4. The only organization is the COACH CURRICULUM hub page's link callouts, which are hand-maintained and exist nowhere in the data. The folder structure here is the vault's, not Notion's.

## Season + System

| File | What it is |
|---|---|
| [Curriculum-Overview](Curriculum-Overview.md) | Notion "START" — program overview, age groups (Funny Joes K–2, Cool Jess 3–5), six skill domains, supporting systems |
| [DR-Practice-Structure](DR-Practice-Structure.md) | The universal 7-block practice architecture, sport-agnostic. The backbone every week plan runs on |
| [Season-Design-6-Sessions](Season-Design-6-Sessions.md) | 60-min block template + six-session summary + season-long gamification layer (XP, badges, constraint bonuses) |
| [Season-Design-Skill-Domains](Season-Design-Skill-Domains.md) | The eight skill domains for the sport |
| [Tier-System](Tier-System.md) | Six tiers (Ready → Control → Connector → Flow → Strategist → Leader) with cues, common errors, CFU, and Joes/Jess split |
| [Terminology](Terminology.md) | ~70 terms across nine categories — the shared coaching language |
| [Practice-Design-Template](Practice-Design-Template.md) | The write-up template a coach fills in per week |

## Curriculum — the six weekly sessions

Each is a complete 60-minute session plan built on the 7-block spine, with one cue of the week.

| Week | Cue |
|---|---|
| [Week 1 — Throwing + Catching](Curriculum/Week-1-Throwing-and-Catching.md) | STEP to your target |
| [Week 2 — Catching + Communication](Curriculum/Week-2-Catching-and-Communication.md) | Diamond hands at chest |
| [Week 3 — Ball Carrying + Flag Pulling](Curriculum/Week-3-Ball-Carrying-and-Flag-Pulling.md) | Eyes on hips |
| [Week 4 — Ball Carrying + QB Handoff](Curriculum/Week-4-Ball-Carrying-and-QB-Handoff.md) | Tuck + lock it away |
| [Week 5 — Handoffs + Running Lanes](Curriculum/Week-5-Handoffs-and-Running-Lanes.md) | Inside elbow up |
| [Week 6 — Play Action + 4th Down](Curriculum/Week-6-Offensive-Strategy-Play-Action-and-4th-Down.md) | Sell the fake |

## Skills + Games

| File | Origin |
|---|---|
| [Warm-Ups](Skills/Warm-Ups.md) | DR-authored — Quick Feet → Step → Pivot progression, vocabulary transfer rule |
| [Zones-Game](Skills/Zones-Game.md) | DR-authored — field zones 1–5, scoring/conversion/first-down logic |
| [Throwing](Skills/Throwing.md) | NFL Flag reference |
| [Catching](Skills/Catching.md) | NFL Flag reference |
| [Flag-Pulling](Skills/Flag-Pulling.md) | NFL Flag reference |
| [Agility-Drills](Skills/Agility-Drills.md) | NFL Flag reference |
| [Conditioning](Skills/Conditioning.md) | NFL Flag reference |
| [Formations](Skills/Formations.md) | NFL Flag 5-on-5 playbook, 9 formations × 3 plays |

## Resources
- [NFL-Flag-Curriculum](Resources/NFL-Flag-Curriculum.md) — PDF pointer
- [Nuggets](Resources/Nuggets.md) — PDF pointer

## Doctrine layer

Shared across all DR sports, not flag-football-specific, but lives in this Notion space.

- [Start-Here](Start-Here.md) — mission + vision
- [Core-Values](Core-Values.md) — Humility / Perseverance / Adaptability (Humble / Hungry / Smart)
- [DR-Formula](DR-Formula.md) — Knowledge + Skill × Attitude²
- [DR-Method-FUELED](DR-Method-FUELED.md) — Friendly, Upfront, Enthusiastic, Leader, Efficient
- [DR-Culture](DR-Culture.md) — "We are coachable"
- [DR-Team](DR-Team.md) — the 10 coach standards
- [Being-a-Coach](Being-a-Coach.md) — origin of "coach," moral responsibility
- [The-Hand-of-a-Coach](The-Hand-of-a-Coach.md) — locus of control, empathetic feedback, recognition, negotiation, psychological safety

---

# Defect list

Found while pulling. These are problems in the Notion source, not in the mirror.

**1. The weeks table on COACH CURRICULUM is empty.** NOTES and LIFE LESSONS are blank for all six weeks. The Word-of-the-Week / life-lesson layer is defined in [Practice-Design-Template](Practice-Design-Template.md) and referenced in [DR-Practice-Structure](DR-Practice-Structure.md), but has never been filled in. This is the largest gap between the method and what a coach runs.

**2. Two pages both titled "SEASON DESIGN."** One is the eight skill domains; one is the 60-min block template plus six-session plan. Different content, identical title, sitting in the same flat database. Split here as `-Skill-Domains` and `-6-Sessions`.

**3. Two pages with identical content.** "THROWING" and "HOW TO THROW A FOOTBALL" are byte-for-byte the same NFL Flag article. Mirrored once as [Throwing](Skills/Throwing.md).

**4. Zones Game contains two stacked drafts.** A current 5-zone version (with the middle no-run zone and first-down marker) and an earlier 4-zone version, in the same page, with no marker saying which is live. Both preserved in the mirror and labeled, but coaches reading the page in Notion could teach the wrong field logic.

**5. Golf statistic in Being-a-Coach.** The retention stat ("only 25% of kids aged 6–12 consistently stick with golf") is a leftover from a pre-football version of the doctrine deck. Never re-sourced for football.

**6. Week 1 skips Step 6.** Block 1 runs Step 1–5 then Step 7. Numbering gap is in the Notion source.

**7. Two competing week-plan versions exist.** The full session plans in [Curriculum/](Curriculum/) and the one-paragraph week summaries inside [Season-Design-6-Sessions](Season-Design-6-Sessions.md) describe the same six weeks with drifting detail (e.g. Week 3 is "Pass Patterns + YAC" in the summary but "Ball Carrying + Flag Pulling" in the actual plan). The session plans are the live version.

**8. Notion pages named "NFL" and "NUGGETS" have no content** — each is a bare PDF attachment. Text of both PDFs is in [Source-Docs](../Source-Docs/) and [Books](../Books/).

**9. Formations diagrams are external images.** 27 play diagrams hosted on `nflstatic.s3.amazonaws.com`. Not mirrored — the text descriptions are, but a coach needs the Notion page or the PDF to see the routes.
