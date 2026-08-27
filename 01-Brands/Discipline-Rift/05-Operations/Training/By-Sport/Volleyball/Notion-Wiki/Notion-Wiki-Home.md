---
brand: Discipline-Rift
area: training
sport: Volleyball
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: notion_wiki
notion_db: DR VOLLEYBALL
notion_db_id: f43a3615-5ebc-4e8e-a0a5-916ce470e1d9
notion_data_source_id: 9ef62878-38f6-4f45-a878-a8a61c7408b8
notion_url: https://app.notion.com/p/f43a36155ebc4e8ea0a5916ce470e1d9
last_updated: 2026-08-11
---

# DR Volleyball Notion Wiki

## Parent
- [[Volleyball-Home]]

## What this is
Mirror of the **DR VOLLEYBALL** Notion wiki — the coach-facing platform DR uses as its central resource to learn, work, and plan ahead ("Welcome DR Team!"). Pulled 2026-08-11 via the Notion API. Companion to the DR TENNIS mirror pulled the same day.

The Notion database holds 31 top-level pages. 30 have content and are all mirrored here; COMING SOON is empty. Volleyball is DR's spearhead sport, and this wiki is materially deeper than the tennis one: it carries a rewritten, learning-science-based practice system (DR-UPS) and per-skill teaching modules that the tennis wiki does not have. Most curriculum content was rewritten in Notion in March–April 2026, which supersedes the older PDF extractions in `../Source-Docs/`.

## Doctrine layer (shared with Tennis wiki)
- [[Start-Here]] — mission and vision
- [[Core-Values]] — humility, perseverance, adaptability
- [[DR-Formula]] — Knowledge + Skill × Attitude²
- [[DR-Method-FUELED]] — Friendly, Upfront, Enthusiastic, Leader, Efficient
- [[DR-Culture]] — FUELED + core values
- [[DR-Team]] — the 10 coach responsibilities
- [[Being-a-Coach]] — origin of "coach," moral responsibility, retention case
- [[The-Hand-of-a-Coach]] — locus of control, empathetic feedback, recognition, negotiation, psychological safety

## Practice-system layer (volleyball-only — the 2026 rewrite)
This is the layer the tennis wiki lacks. It is Lemov-aligned (*The Coach's Guide to Teaching*) and defines how every DR practice is structured:

- [[Why-DR-Practice]] — what DR Practice is/is not; See → Decide → Act; why decisions are delayed until skills are stable
- [[DR-Practice]] — the **Discipline Rift Universal Practice Structure (DR-UPS)**: 7 blocks, any sport, mixed experience
- [[Terminology]] — the coaching glossary: 60+ terms across 9 families (decision-making, practice design, CFU, cognitive load…)
- [[Tier-System]] — six-tier volleyball player progression (observable evidence, not age)
- [[Coach-Curriculum]] — the wiki's navigation hub ("your bread and water to coach every practice")

## Skill modules (`Skills/`)
Per-skill teaching contracts: numbered sequences, named cues, non-negotiables, week-by-week progression. Same-language-across-all-coaches is the design principle.

- [[Skills/Passing|Passing]] — Ready → Pancakes → Low → Up; "Pancakes & Syrup," "Surfboards"
- [[Skills/Setting|Setting]] — Ready → Beat it. Stop. → Hershey Kiss → Finger Tips + Up
- [[Skills/Serving|Serving]] — underhand open-palm: Ready → Hold → Open Palm → Finish
- [[Skills/Attacking|Attacking]] — written as a full 7-block DR-UPS session (Ready → Left–Right → Plant → Up → High Hand → Finish)
- [[Skills/Defending|Defending]] — Ready → Read → Move → Platform → Up; positions taught as places, not roles
- [[Skills/Moving|Moving]] — Step / Step–Shuffle / Step–Shuffle–Shuffle; movement as a standalone skill
- [[Skills/Communicating|Communicating]] — group voice → individual voice → in-play voice; "Mine on three"

## Weekly curriculum (`Curriculum/`)
All six sessions follow the 7-block DR-UPS structure with cues, Micro-CFUs, tiering, and exit criteria. These supersede the OCR extractions in `../Source-Docs/` — same sessions, structurally clean, with named drills and add-on option menus intact.

- [[Curriculum/Week-1-Passing-and-Setting|Week 1 — Passing + Setting]] — "Platform early"; Lines Game, Crab Game, Jailbreak
- [[Curriculum/Week-2-Serving|Week 2 — Serving]] — "Freeze your finish"; Minute-to-Win-It, Serving Ladder, Run to Serve
- [[Curriculum/Week-3-Attacking|Week 3 — Attacking]] — "timing, not power"; near-duplicate of the Attacking module (see defects)
- [[Curriculum/Week-4-Defending|Week 4 — Defending]] — "feet first"; Positional Defense, Reaction Challenge, Seam Digging
- [[Curriculum/Week-5-Moving|Week 5 — Moving]] — "move first, then play"; Defensive Drills 6.1, Setter Footwork, Chaos Passing
- [[Curriculum/Week-6-Communicating|Week 6 — Communicating]] — ⚠️ content is a passing/setting session, not communication (see defects)

## Operations layer
- [[Accident-Report]] — incident report template (severity, mechanism, care, parent contact, return-to-play, sign-off)

## Resource shelves (PDF pages)
- [[Drills]] — 4 drill books; 3 already in `../Books/`, **Volleyball_Drills.pdf missing from the vault**
- [[Fundamentals]] — 2 books, both already in `../Books/`
- [[Coaching-Science]] — *The Coach's Guide to Teaching* (Lemov) — **not in the vault**, Notion attachment only; it is the source text behind the practice-system layer

## Not pulled
- **COMING SOON** (`07d9ea2e-0ec7-4872-9c6f-593e8851a155`) — placeholder page, empty in Notion. Nothing to mirror.
- Skill-module photos and drill diagrams hosted on Notion S3 (expiring signed URLs) — each is marked in place with a callout. Roughly 12 across Passing, Setting, Serving, Being a Coach, and Week 1.
- PDF attachments on the resource-shelf pages (the Notion API exposes no durable download URL). The two missing from the vault are listed above.

Everything else in the DR VOLLEYBALL wiki is mirrored. Verified 2026-08-11 against a full API listing of the data source: 31 pages, no pagination.

## Known source issues
Defects in the Notion source, not the mirror — fixing them means editing Notion.

1. **Week 6 title/content mismatch (most serious).** "WEEK 6 - Communicating" contains a passing/setting session — North Star "Pass/Set to a target with control," pass-vs-set decision rule, Jailbreak. The communication progression from the [[Skills/Communicating|Communicating module]] is never delivered as a session. Either the page is mis-titled or the real Week 6 session was never written. A coach following the wiki will end the season without a communication practice.
2. **Week 3 duplicates the Attacking module.** The 7-block body of [[Curriculum/Week-3-Attacking]] is nearly identical to [[Skills/Attacking]]. Two copies of the same plan will drift apart on the next edit.
3. **Leftover ChatGPT artifacts.** Week 3 ends with "If you want, I can turn this into a clean curriculum card…" and Week 4 ends with "If you want, I can do Week 5 next…" — assistant closing lines pasted into Notion without cleanup. Cosmetic, but visible to every coach.
4. **Golf statistics in [[Being-a-Coach]].** Retention stats cite the National Golf Foundation (25% of kids aged 6–12 stick with golf) inside the volleyball wiki — same defect as the tennis wiki.
5. **Week 6 says "next week."** The Block 7 spacing preview tells players to re-test "next week" in the final session of the season — same end-of-season defect as the tennis wiki.
6. **Communicating module opens mid-sentence.** [[Skills/Communicating]]'s purpose statement is trimmed in the source.
7. **Coach Curriculum table is empty.** The WEEKS | NOTES | LIFE LESSONS table on [[Coach-Curriculum]] has no content — unlike Tennis, the volleyball wiki does not define per-week life lessons anywhere.

Item 1 blocks correct delivery of Week 6 and should be resolved before the next volleyball season runs. Items 2–3 are cleanup for the curriculum owner.
