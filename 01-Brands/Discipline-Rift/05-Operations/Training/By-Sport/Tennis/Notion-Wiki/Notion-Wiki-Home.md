---
brand: Discipline-Rift
area: training
sport: Tennis
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: notion_wiki
notion_db: DR TENNIS
notion_db_id: d7a0a9e9-4ba4-49b8-b1a0-0cf65df45be1
notion_url: https://app.notion.com/p/d7a0a9e94ba449b8b1a00cf65df45be1
last_updated: 2026-08-11
---

# DR Tennis Notion Wiki

## Parent
- [[Tennis-Home]]

## What this is
Mirror of the **DR TENNIS** Notion wiki — the coach-facing platform DR uses as its central resource to learn, work, and plan ahead. Pulled 2026-08-11 via the Notion API.

The Notion wiki holds 17 top-level pages. Seven of them (the six weekly curriculum sessions plus Group Dynamics) already existed in this vault as PDF extractions under `../Source-Docs/`. The remaining ten are the coaching doctrine layer and were not in the vault before this pull.

## Doctrine layer
- [[Start-Here]] — mission and vision
- [[Core-Values]] — humility, perseverance, adaptability
- [[DR-Formula]] — Knowledge + Skill × Attitude²
- [[DR-Method-FUELED]] — Friendly, Upfront, Enthusiastic, Leader, Efficient
- [[DR-Culture]] — how FUELED and core values fit together
- [[DR-Team]] — the 10 coach responsibilities
- [[Being-a-Coach]] — origin of "coach," moral responsibility, retention case
- [[The-Hand-of-a-Coach]] — locus of control, empathetic feedback, recognition, negotiation, psychological safety

## Curriculum layer
- [[6-Week-Season]] — season map, life lessons per week, six-tier player system
- [[Group-Dynamics-Leading-Different-Groups]] — Group A vs Group B coaching

## Scheduling layer
- [[DR-Tennis-Calendar]] — the DR TENNIS CALENDAR inline database, all 180 rows. Four seasons per year (Fall, Late Fall, Late Winter, Spring). Source is a full year stale — ends 2025-05-16.

### Weekly sessions
Mirrored from Notion in `Curriculum/`. These supersede the older OCR extractions in `../Source-Docs/` — same sessions, but structurally clean and with named drills intact.

- [[Week-1-Forehands]]
- [[Week-2-Backhands-and-Forehands-Review]]
- [[Week-3-Volleys-Forehands-and-Backhands-Review]]
- [[Week-4-Serves-Forehands-and-Backhands-Review]]
- [[Week-5-All-Skills-Review]]
- [[Week-6-All-Skills-Assessment]]

Every session follows the same shape: Introduction → Warm-up → Skill breakdown → main skill block (30 min) → Game of the Day → Life Lesson. Week 6 replaces the skill block with the assessment and closes with the End of Season Celebration.

The `../Source-Docs/` PDF extractions are kept as the historical record of the original PDFs. Do not use them for coaching or AI context — they carry OCR damage and lack drill names.

## Not pulled
- **COMING SOON** (`70f20a5d-7e19-4d78-a80e-db53a8de396d`) — placeholder page, empty in Notion. Nothing to mirror.
- **DR TENNIS CALENDAR** archived duplicate (`11104528-85a8-818e-b958-000b4071b565`) — in Notion's trash as of 2026-08-11. The live copy is mirrored at [[DR-Tennis-Calendar]].
- Court and drill diagrams, page covers, and icons hosted on Notion S3. These are expiring signed URLs and cannot be durably mirrored — each is marked in place with a callout pointing back to Notion. Roughly 15 diagrams across the weekly sessions.

Everything else in the DR TENNIS wiki is now mirrored. Verified 2026-08-11 against a full API listing: 17 top-level pages (16 with content, all mirrored, plus the empty COMING SOON) and the calendar database.

## Known source issues
Found during the pull. These are defects in the Notion source, not the mirror — fixing them means editing Notion.

### Volleyball contamination
Several tennis pages contain unedited volleyball content, which suggests the tennis curriculum was cloned from the volleyball one and not fully rewritten.

1. **Week 4 FORM block** is the most serious. The section that should teach the tennis serve is written entirely in volleyball terms — "Volleyball Equivalent," "hold the volleyball," "strike with the palm of your hand." It does not describe a tennis serve at all. A coach following this page literally cannot teach the Week 4 skill.
2. **Week 4 drills** — the Target Drill is labeled a serve drill but its setup and stated purpose reference volleys, and three of its four Deep Practice drills are Week 3's volley drills unchanged.
3. **Tennis Tag** (Weeks 2–6) has players tagging "with the volleyball" and describes "chasers with volleyballs," contradicting its own tennis-ball setup line.
4. **[[Group-Dynamics-Leading-Different-Groups]]** references "basic volleyball skills," "setting, spiking, and serving," and "lower the net." Present in both the Notion and PDF versions, so it is original to the source doc.

### Other defects
5. **[[Being-a-Coach]]** cites golf retention statistics (National Golf Foundation, 25% of kids aged 6–12) inside the tennis wiki. The drop-off argument holds but the sport-specific numbers are wrong here.
6. **"Second week" opener** — Weeks 3, 4, 5, and 6 all opened with "welcome them to the second week of the tennis season." Corrected in the mirror, still wrong in Notion.
7. **Game of the Day intro** says "for forehands" on every week regardless of the actual skill.
8. **Week 1 Skill section** says the day's focus is "Forehand & Backhand," but Week 1 is the forehand week and backhands are Week 2.
9. **Week 6 Life Lesson** tells players to "come back next week" in the final session of the season.

Items 1 and 2 block correct delivery of Week 4 and should be fixed before the next season runs. The rest are cosmetic or judgment calls for the curriculum owner.
