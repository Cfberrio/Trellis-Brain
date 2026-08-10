---
brand: Discipline-Rift
area: communication
subarea: campaigns
note_type: reference
status: active
canonical: false
used_for_ai: true
source_type: derived
source_reference: "Trellis repo domains/content/discipline-rift/campaigns/2026-08-email-rewrite-retrospective.md — analysis of Luis's 2026-08-09/10 breakdown of the first-week email draft"
owner: Luis
last_updated: 2026-08-10
sensitivity: internal
hub_role: leaf
audience: parent
channel: [email]
---

## Parent
- [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|DR Communication Home]]

## Related
- [[DR-Parent-Email-Template|DR Parent Email Template]] — the binding rules this analysis produced
- [[DR-First-Week-Of-School-Campaign-2026-08|First Week of School Campaign]] — the email under analysis

# DR — Email Rewrite Retrospective (First-Week Campaign, 2026-08)

**What this is:** Full analysis of Luis's breakdown of the first-draft parent email and the modifications worked through 2026-08-09/10. This is the training document for what "up to par" parent copy means. Binding artifacts derived from it: campaign §0 (five rules), [parent-email-template.md](../parent-email-template.md), design-spec §5.2/§10.1 rulings.

---

## A · The five corrections — what each protects

| # | Correction | Surface fix | What it protects |
|---|---|---|---|
| 1 | "Saying we're not entertaining… comes off as an insecurity they may have: my child will get distracted" | Delete the attention gap | The parent's image of their own child. Never hand a parent their private worry back as a diagnosis; never imply practice is dull |
| 2 | "Doesn't look good to parents… who have already done the sport. We're also wanting retention" | Delete "most of our players have never played" | The returning family's reason to stay. Beginner-only positioning trades retention for acquisition |
| 3 | "No need to explain our methods… saying we have a methodology that helps with X is enough" | Delete method names | The parent's trust. A lecture talks down; a fact reassures. Science is for coaches |
| 4 | "Are you seriously suggesting parents shouldn't ask players how practice was?" | "You won't have to ask" → "if you ask and just hear 'Fine'" | The parent-child relationship. Dashboard adds the coach's perspective so parents ask deeper questions — never a substitute. The insight (child under-narrates) was right; the conclusion was backwards |
| 5 | "Almost a whole essay. Choose the points that are most valuable and stick to that" | ~490 → ~230 words | The parent's time and attention |

**Unifying principle: Luis edits to protect relationships; the draft was written to win arguments.** Every deletion removed persuasion armor; nothing cut was information a warm-list parent needed.

## B · The rewrite, element by element

| Element | Draft | Luis's action | Principle |
|---|---|---|---|
| Subject | Curiosity ("The one thing not on the school supply list") | → "Back to school this Tuesday. Are you ready?" | Calendar-anchored, plain, direct question |
| Preview | Gap as threat | → Gap as open question ("what will fill your child's time after 3 PM?") | Gap frame survives only as a question, only in subject/preview |
| Opening | Supply list ritual | Kept nearly verbatim | Concrete, situational, parent's-eye = what worked |
| Pivot | Fear ("the block fills itself") | → Positive self-answering question + 80% movement stat | Positivity, then evidence |
| CTA | One, late | → Two renders, first immediately after the hook | Warm list can act before being educated |
| Readiness gaps | Three | → Two; attention deleted; coordination reframed as coach observation ("we're seeing larger groups of players behind") | Population observation ≠ child diagnosis |
| Difficulty gap | "…follows them into a classroom" | Kept nearly verbatim | The one gap that empowers rather than stings |
| Season description | Six weeks / ages / beginner block | Deleted | House list knows what DR is; description is the website's job |
| Method | Teach/rep/play + retrieval naming + editorializing | Kept teach/drill/play + luck line; cut name + asides | Method as fact. Luck line survived — it's the parent's risk, not our cleverness |
| Week-one urgency | Tier ladder, "team forms without them" | Deleted | Zero urgency mechanics in touch one |
| Convenience | Verbatim line | Kept + added header "Easy for you — we will do what is necessary" | Benefit named before mechanism |
| Dashboard | "You won't have to ask" + weekly | → "If you ask and just hear 'Fine'" + update after EVERY practice | Relationship preserved; cadence fact corrected |
| Proof stack | Level 2 / supervised / 55 schools | Deleted | Trust proof lives on the site and later touches |
| Guarantee | "Our value is the teaching" | → "teaching the skills and the passion for the sport" | Passion is part of the deliverable |
| Close | Deadlines, REG_MINUTES | → "Wishing your child a valuable, enriched school year." | Close warm, never a squeeze |

## C · Scoreboard

Survived: hook ritual, difficulty gap + classroom line, teach/drill/play, luck line (Q13 translated), convenience line, dashboard concept, guarantee skeleton.
Died: all persuasion architecture — fear frame, proof stack, urgency, method lecture, season explainer, founder asides.
Numbers: ~490 → ~230 words · 3 gaps → 2 · 5 proof points → 0 · 4 urgency lines → 0 · 1 late CTA → 2 renders, one early.

Luis's additions were exactly four: evidence (80%), warmth ("Easy for you," closing wish), scope (passion in the guarantee), an earlier ask. **When Luis adds, it's evidence or warmth. When Luis cuts, it's persuasion.**

## D · Production round (ChatGPT build)

Rulings: white canvas enforced (dark drift gets inverted); DISCIPLINE RIFT approved as giant-word hero with nothing under it; copy compresses again at design ("everything else: 80%") — approval doesn't freeze copy; the deliverable is the render — Luis corrects by looking, not reading. Process finding: his raw draft, not the cleaned repo copy, was the production source → triggered the pipeline reroute.

## E · System changes shipped

Five rules (campaign §0) · design rulings in email-design-spec §5.2/§10.1 · parent-email-template.md (structure contract, 230-word cap) · cold/warm routing split (funnel DNA = pop-up nurture only) · new chain: template draft → rules check → Claude builds GHL HTML → Luis reacts to render → QA on final artifact → send.
