---
brand: Discipline-Rift
area: training
sport: Pickleball
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: notion_wiki
notion_db: DR PICKLEBALL
notion_db_id: 2ba04528-85a8-8046-8cef-f55da0bb7aef
notion_url: https://app.notion.com/p/2ba0452885a880468ceff55da0bb7aef
last_updated: 2026-08-11
---

# DR Pickleball Notion Wiki

## Parent
- [[Pickleball-Home]]

## What this is
Mirror of the **DR PICKLEBALL** Notion wiki — the coach-facing platform DR uses as its central resource to learn, work, and plan ahead. Pulled 2026-08-11 via the Notion API.

The wiki holds 14 pages. Twelve carry content and are all mirrored here. Nothing in this folder existed in the vault before this pull — pickleball had no PDFs and no source library, so this mirror is the entire pickleball curriculum.

## Doctrine layer
Identical in substance to the tennis wiki's doctrine layer — this is DR-wide coaching material that happens to be duplicated into each sport's wiki in Notion.

- [[Start-Here]] — mission and vision
- [[Core-Values]] — humility, perseverance, adaptability
- [[DR-Formula]] — Knowledge + Skill × Attitude²
- [[DR-Method-FUELED]] — Friendly, Upfront, Enthusiastic, Leader, Efficient
- [[DR-Culture]] — how FUELED and core values fit together
- [[DR-Team]] — the 10 coach responsibilities
- [[Being-a-Coach]] — origin of "coach," moral responsibility, retention case
- [[The-Hand-of-a-Coach]] — **empty in Notion.** The tennis version of this page has real content (locus of control, empathetic feedback, recognition, negotiation, psychological safety). The pickleball copy was never written.

## Curriculum layer
- [[6-Week-Season]] — season map and life lessons per week
- [[Group-Dynamics-Leading-Different-Groups]] — Group A vs Group B coaching

### Weekly sessions
Mirrored from Notion in `Curriculum/`.

- [[Week-1-Forehands]]
- [[Week-2-Backhands-and-Forehands-Review]]
- [[Week-3-Dinks-Forehands-and-Backhands-Review]]
- Week 4 — Serves — **does not exist in Notion**
- Week 5 — Drop shots — **does not exist in Notion**
- Week 6 — Rallying + Assessment — **does not exist in Notion**

Every built session follows the same shape: Introduction → Warm-up → Skill breakdown → main skill block (30 min) → Game of the Day → Life Lesson.

### Derived notes (not Notion pages)
Two blocks appear byte-identical in all three sessions. They are factored out here so an edit happens once instead of three times. They are the only files in this folder that do not correspond 1:1 to a Notion page.

- [[Shared-Warm-Up]] — stretches, THE LINES GAME, PICKLEBALL SIMON SAYS, and the Week-3-only Handshake Grip / Frying Pan Bounce
- [[Shared-Life-Lesson-Protocol]] — the Word of the Week closing routine

## Not pulled
- **COMING SOON** (`2ba04528-85a8-8122-8456-c90403de068f`) — placeholder page, empty in Notion. Nothing to mirror.
- One **untitled empty row** in the database (`2ba04528-85a8-8164-b808-c6d877b6cc5a`) — no title, no content. Likely an accidental row; worth deleting in Notion.
- Court and drill diagrams, page covers, and icons hosted on Notion S3. These are expiring signed URLs and cannot be durably mirrored. Two matter: the court-lines diagram used in THE LINES GAME, and the Around the World rotation diagram in Week 3. Both are marked in place.

## Known source issues
Defects in the Notion source, not the mirror. Fixing them means editing Notion.

### Missing curriculum
1. **Weeks 4, 5, and 6 do not exist.** The season table in [[6-Week-Season]] defines them — Serves, Drop shots, Rallying + Assessment — but no pages were ever built. This is the single biggest gap: half a sold season has no lesson plan. Tennis, by contrast, has all six.
2. **[[The-Hand-of-a-Coach]] is empty** while its tennis counterpart is fully written. Straight copy-across would fix it.

### Cross-sport contamination
The pickleball curriculum was cloned from the tennis and volleyball ones and not fully rewritten.

3. **Week 1 Team Expectations** tells players to "arrive on time for tennis class" and describes "6 weeks of tennis classes." Left as-is in the mirror and flagged inline.
4. **[[Group-Dynamics-Leading-Different-Groups]]** tells coaches to focus on "basic volleyball skills" and "setting, spiking, and serving," and to "lower the net." Same defect as the tennis copy — original to the shared source doc.
5. **[[Being-a-Coach]]** cites golf retention statistics (National Golf Foundation, 25% of kids aged 6–12) inside the pickleball wiki. The drop-off argument holds; the sport-specific numbers are wrong here. Same defect as tennis.
6. **Warm-up games** say "racket" throughout rather than "paddle," and THE LINES GAME instructs the coach to call out "tennis court lines."

### Other defects
7. **Game of the Day intro** says "for forehands" in Weeks 2 and 3 regardless of the actual skill. Same defect as tennis.
8. **Week 3 life lesson mismatch** — the season table assigns Confidence + Adaptability, but the page delivers "Teamwork & Adaptability," and its own explanatory text defines confidence rather than teamwork.
9. **Week 1 Accuracy Challenge** has a second drill (Dinking Domino) collapsed into it mid-sentence — "aim consistentlying Domino**" — an unrepaired paste. Preserved in the mirror as a parenthetical.
10. **Week 2 drill base setup** says players "hit the ball towards the cones with their forehand stroke" inside the backhand block.

Item 1 is the one that affects delivery. Items 3–6 are credibility risks if a parent or coach ever reads the material. The rest are cosmetic.
