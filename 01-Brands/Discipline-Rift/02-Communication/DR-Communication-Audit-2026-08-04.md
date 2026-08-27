---
brand: Discipline-Rift
area: communication
note_type: audit
status: active
canonical: false
used_for_ai: true
source_type: derived
owner: Luis
last_updated: 2026-08-04
sensitivity: internal
hub_role: leaf
related_notes:
  - "[[DR-Communication-Engine]]"
  - "[[communication-rules]]"
  - "[[Sequences/DR-Registration-Sequence]]"
  - "[[Sequences/DR-Lead-Magnet-Sequence]]"
  - "[[Sequences/DR-Season-Reminder-Sequence]]"
  - "[[../00-Brand-Core/Avatar]]"
  - "[[../06-DNA/Money-Model]]"
---

# DR Communication Audit — 2026-08-04

## Parent
- [[Communication-Home|DR Communication Home]]

## Scope & method

Audited every parent-facing, coach-facing, and applicant-facing message DR sends, across three sources:

1. **Shipped** — 14 live templates extracted from ClickUp doc `8cqnrff-21297` (NOTIFICATIONS branch) on 2026-08-03. This is what people actually receive.
2. **Documented** — [[Templates/Operational-Email-Library]], [[communication-rules]].
3. **Designed** — [[DR-Communication-Engine]] + the three sequence docs (all `status: draft`, last touched 2026-07-23).

Lenses applied: `/avatar`, `/offers`, `/lead-nurture`, `/lead-magnets`, `/marketing-psychology`, `/product-marketing-context`.

---

## Headline finding

**DR's communication problem is not a writing problem. It is a shipping problem.**

The designed system in this vault is strong — segment-aware, psychologically sound, risk-reversed, built for re-enrollment. It has been sitting in draft since 2026-07-23. Meanwhile the system parents actually receive is a set of unstyled n8n receipts written in January, still carrying bugs first flagged on 2026-04-21.

| Layer | Templates | Last real change | Status |
|---|---|---|---|
| Shipped (ClickUp / n8n) | 14 | 2026-02-03 (weekly set) | Live |
| Designed (Engine + sequences) | 3 sequences, ~20 messages | 2026-07-23 | **Draft** |

Everything good is unshipped. Everything shipped is thin.

Two structural consequences:

- **[[DR-Communication-Engine]] declares "n8n is retired."** Every live template is n8n. The retirement has not happened. Until it does, the Engine is aspirational and [[communication-rules]] — still marked `canonical: true` and still documenting n8n — is what governs reality.
- **Four bugs were flagged 2026-04-21, re-flagged 2026-07-23, and are still live 2026-08-03.** The problem is not the bugs. It is that no one owns clearing them.

---

## 1. Offer lens — the Value Equation is absent from live comms

Value Equation = **(Dream Outcome × Perceived Likelihood) / (Time Delay × Effort)**

Every one of the four levers is missing from all 14 live templates.

| Lever | DR's strongest asset | Appearances in live comms |
|---|---|---|
| Dream Outcome | "We actually teach the sport" — skill, character, teamwork, communication, leadership | **0 / 14** |
| Perceived Likelihood | **Value Guarantee — 100% refund, any time during the season** | **0 / 14** |
| Time Delay | Tier System — "progress you can see," baseline → end-of-season | **0 / 14** |
| Effort & Sacrifice | "No transportation needed — coaches handle everything from dismissal, on campus" | **0 / 14** |

Live comms describe **logistics** (schedules, dates, what to bring) and **drills** (passing, serving, attacking). They never describe **what the parent is buying**.

**The single highest-value missing line in the entire system is the Value Guarantee.** Per the Product Marketing Context (`CLAUDE-TRELLIS/.agents/product-marketing-context.md`, referred to below as PMC) it is finalized as the headline risk reversal. Risk reversal does its hardest work at the moment money leaves the account — and DR's registration confirmation, which fires at exactly that moment, is a payment receipt with an emergency contact field. A first-time parent reading it has no answer to *"did I just waste this?"*

**Fix:** add the guarantee line to the registration confirmation, the 7-day reminder, and the season-close email. Three lines of copy. No engineering.

---

## 2. Avatar lens — three segments defined, one message sent

[[../00-Brand-Core/Avatar]] defines three parent segments with detection signals, ranked obstacles, message angles, and standard closes:

| Segment | Buying | Detection signal |
|---|---|---|
| 1 — Anxious beginner | Psychological safety + belonging | Asks "is this for beginners?" |
| 2 — Logistics-overwhelmed | Convenience + reduced decision fatigue | Asks "what time does it end?" |
| 3 — Price-sensitive | Certainty + predictable commitment | Asks "what's included?" |

**Zero of the 14 live templates differentiate by segment.** Every parent receives identical copy. The segment routing rule (route by behavior, tag in GHL) exists on paper and is not wired into any communication.

Worse, live comms are under-personalized even at the base level:

- The **weekly emails use `[Parent/Guardian Name]`** — a bracket placeholder — and **never mention the student's name at all.** [[communication-rules]] §8 states the student first name is the parent's primary reference point. Six emails, six weeks, no child's name.
- The **countdown reminders** use `{{ $json.name }}` — which resolves to the *team/season* name, not the student's.
- **No live template names the coach, the school, or the specific practice location.** "Coach Santiago, Friday at Deerwood" reads as a program with its act together. "There are 30 days left until the start of {{ $json.name }}" reads as a mail merge.

The **secondary avatar (school gatekeeper)** has a full documented proof package — dismissal one-pager, safety standards, coach credibility, comms boundaries, equity statement. None of it exists as a communication asset in the live system.

**Fix (cheapest first):** wire `{STUDENT_FIRST_NAME}` into all six weekly emails and all three countdowns. This is a merge-field change, not a rewrite, and it is the highest ratio of impact to effort in the audit.

---

## 3. Lead-nurture lens — the four pillars

### Speed — **broken, and it is the biggest revenue leak**

**There is no cart-recovery sequence.** A parent who starts registration and doesn't pay receives nothing, ever. [[Sequences/DR-Registration-Sequence]] designs it (R1 at +1hr, R2 at +24hr, R3 at +72hr, then stop) — draft only.

Recovery probability decays with the log of elapsed time; days 0–2 hold most of what is recoverable. Right now DR captures none of it. Of every gap in this audit, this is the one with a direct, immediate dollar value attached.

Also unverified: whether the registration confirmation fires **within seconds** of payment or on a batch. The Engine flags this as the highest-leverage timing in the sequence. `[NEEDS CONFIRMATION — owner: dev]`

### Availability — **undefined**

No response-time SLA appears in any communication. Only **1 of 14** live templates invites a reply (Parent Assistance). The registration confirmation says "don't hesitate to contact us" but gives no channel expectation. The school-facing promise — *"Parents contact us directly, we don't route questions through your office"* — is a commitment DR has made to schools without a documented SLA behind it.

### Personalization — **weakest pillar**

Covered above. Base-level personalization (student name) is missing from 6 of 14 templates entirely.

### Volume — **structurally sound, fatigue risk unconfirmed**

The 30/7/1 countdown exists and is the right shape. But [[DR-Communication-Engine]] §9 warns these must fire **only for the first session / season start** — firing three countdowns per session would train parents to ignore DR. Nothing in the live templates indicates which scope is implemented. `[NEEDS CONFIRMATION — owner: dev]`

### DR's version of BAMFAM — **missing**

For DR, "book the next meeting from this meeting" translates to **book the next season from inside the current one.** Live Week 6 closes with *"we look forward to more volleyball ahead"* and stops. No re-enrollment link. No deadline. No tier advancement. No review ask.

That is the warmest audience DR will ever have — a parent who just watched six weeks of visible improvement — and the system asks them for nothing.

---

## 4. Lead-magnet lens — five good assets, zero distribution

[[Templates/Parent-Guides-Library]] contains five finished, genuinely strong guides. Guide 1 ("5 Questions Every Parent Should Ask") reframes the entire category. Guide 3 ("4 Red Flags a Youth Program Is Overpromising") positions DR by contrast without naming a competitor — the four red flags are precisely the four things DR doesn't do.

**None of them are delivered by any live communication.** The `LEAD FUNNEL` page in the live ClickUp doc is an empty page with a title.

This means DR has:
- No email capture for parents not ready to register
- No nurture path for a parent whose school isn't covered yet
- No reciprocity asset in market before the ask
- No list to activate when a new school opens

[[Sequences/DR-Lead-Magnet-Sequence]] designs all of it — 6 emails, guide-per-email, offer at #4. Draft only.

**Fix:** this is the largest unbuilt revenue system DR has. The content cost is already sunk — the guides are written. What's missing is a capture form, a delivery email, and five scheduled sends.

---

## 5. Marketing-psychology lens — engineered moments that aren't built

| Principle | DR's natural fit | Live status |
|---|---|---|
| **Peak-End Rule** | Week 4 = peak, Week 6 = ending | Both designed, neither built. Live Week 4 is a drill description; live Week 6 has no ask. |
| **Zeigarnik / open loop** | Tier System — "finish this season, advance to Tier 2" | Never mentioned in any live email |
| **Goal-gradient** | 6-week season with visible tier progress | No progress shown at any point |
| **Loss aversion** | "Your spot is held, teams are filling" | No cart recovery exists |
| **Reciprocity** | 5 parent guides | Never given |
| **Social proof** | "Running at 55 schools across Central Florida" | **0 / 14** templates |
| **Authority** | Level 2 background checks, trained coaches, founder with 10 years coaching | **0 / 14** templates |
| **Commitment & consistency** | The 30/7/1 countdown re-confirms the decision three times | Happens accidentally; never framed |

The Tier System deserves separate emphasis. It is simultaneously an **open loop** (unfinished business the mind returns to), a **progress bar** (goal-gradient), and DR's **continuity mechanism** (per [[../06-DNA/Money-Model]], revenue expands through re-enrollment, not more weeks). It is the single most commercially important idea DR owns — and it appears in zero live parent communications.

---

## 6. Canon conflicts — the governance problem

Seven direct contradictions between documents that are all marked `canonical: true` or authoritative. Anyone writing DR copy today will get a different answer depending on which file they open.

| # | Conflict | Source A | Source B |
|---|---|---|---|
| 1 | **"fun-first"** | PMC v2: *"Don't use 'fun-first.' It undersells the teaching."* | [[../00-Brand-Core/Voice-and-Tone]] lists it under **Words DR Prefers**; [[../00-Brand-Core/Avatar]] uses it as the Segment 1 angle; [[Marketing-Language-Library]] Cat. 1; [[communication-rules]] §12 |
| 2 | **Acquisition offer** | PMC v2: *"NO first-practice trial."* | [[../06-DNA/Money-Model]]: entry offer = *"First-Practice Pass (or 2-Practice Starter)"* |
| 3 | **Public pricing** | PMC: *"no dollar figures anywhere; price only at checkout"* | [[../06-DNA/Money-Model]]: *"Canonical posted price: $129 per season"*; [[../00-Brand-Core/Objections]] quotes "$129 sounds simple" |
| 4 | **Age range** | PMC: 6–12 finalized | Live site FAQ: 5–11 (flagged in PMC, still unresolved) |
| 5 | **SMS** | [[communication-rules]] §7: *"No DR communication currently uses SMS as a primary channel"* | [[DR-Communication-Engine]]: *"SMS is now a real, sanctioned channel"* |
| 6 | **Automation platform** | [[DR-Communication-Engine]]: *"n8n is retired"* | [[communication-rules]] (`canonical: true`) documents n8n as the platform; all 14 live templates are n8n |
| 7 | **Merge syntax** | Engine mandates `{UPPERCASE}` | **Four** syntaxes in production: `{{ .Token }}` (Go/Supabase), `${VAR}` (server), `{{ $json.x }}` (n8n), `[Bracket]` (weekly set) |

Conflicts 1, 2, and 3 are the dangerous ones — they change what goes in front of a paying customer. Conflict 7 is why merge fields keep breaking: with four syntaxes live, a copy-paste between templates produces a broken variable by default.

**Fix:** the Engine already claims supersession. Make it real — set [[communication-rules]] to `status: superseded`, and reconcile 1/2/3 explicitly rather than leaving both versions marked canonical.

---

## 7. Live bug register

Confirmed present in ClickUp as of 2026-08-03.

| # | Template | Bug | First flagged | Severity |
|---|---|---|---|---|
| 1 | 08 Coach Application | Opens `Hi name,` — variable never wired | 2026-04-21 | **Ships broken to every applicant** |
| 2 | 02 Registration Confirmation | Still `${VAR}` syntax, un-normalized | 2026-07-23 | Breaks on any platform migration |
| 3 | 06 Coach Session Reminder | `json.name` delimiter issue | 2026-04-21 | Renders literally if unfixed |
| 4 | 03 / 04 Reminders | Banner reportedly reads "1-Day Reminder" | 2026-04-21 | Unverifiable from text — banner is an image `[NEEDS VISUAL CHECK]` |
| 5 | 02 Registration Confirmation | Phone renders `(407) 6147454` — unformatted | New | Credibility |
| 6 | 02 Registration Confirmation | `contactus` missing a space | New | Credibility |
| 7 | 04 7-Day Reminder | `info@disciplinerift.com` printed twice | New | Credibility |
| 8 | 05 1-Day Reminder | Internal note *"Do you like this personality?"* left in body | New | **Ships an internal note to parents if copied as-is** |
| 9 | 13 Week 5 | Subject says "Moving", body says "Movement" | New | Polish |
| 10 | 14 Week 6 | Subject says "Communicating", body says "Communication" | New | Polish |
| 11 | 06 Coach Session Reminder | Raw Vercel preview URL `dash-board-coaches-whpv.vercel.app` sent to coaches | New | Trust + link durability |

Bugs 1 and 8 are the two that put visibly broken text in front of a real person.

---

## 8. Coverage map — where the silence is

```
LEAD                    → nothing. No capture, no guides, no nurture.
Registration started    → nothing. No cart recovery.
Paid                    → 02 Registration Confirmation (receipt, no reassurance)
30 / 7 / 1 days out     → 03 / 04 / 05 (logistics only, no coach, no student name)
Season weeks 1–6        → 09–14 (volleyball only; brackets, not merge fields)
Player misses practice  → 07 Parent Assistance ✓ (the best-written live template)
Season ends             → nothing. No re-enroll, no review, no tier result.
Between seasons         → nothing.
```

Two more structural gaps:

**Sport coverage.** Weekly sequences exist for volleyball only. Tennis, pickleball, and flag football parents receive the countdown reminders and then go dark for the entire season. [[Sequences/DR-Season-Reminder-Sequence]] notes the banks need building once per sport; the skill focus data already exists in `05-Operations/Training/By-Sport/`.

**Coach coverage.** Parents get 9 touchpoints. Coaches get **1** — a reactive nag when a session record is missing. No acceptance email, no onboarding, no weekly session plan, no schedule-change notice, no season wrap. Coach quality and consistency is a stated pillar of the school-facing pitch; the coach comms layer doesn't support it.

---

## 9. Prioritized action plan

Ranked by revenue impact ÷ effort. Items 1–4 are copy-only and need no engineering.

| # | Action | Effort | Why it ranks here | Owner |
|---|---|---|---|---|
| 1 | Add the **Value Guarantee** line to registration confirmation, 7-day reminder, season close | 3 lines | Strongest asset DR owns, currently used nowhere. Risk reversal at the moment of payment. | Content |
| 2 | Fix bugs **1 and 8** (`Hi name,` / internal note in body) | 10 min | Visibly broken text reaching real people | Dev |
| 3 | Wire **`{STUDENT_FIRST_NAME}`** into all 6 weekly emails + 3 countdowns | Merge fields | Highest impact-to-effort ratio in the audit | Dev |
| 4 | Build the **season-close re-enrollment email** — tier result + deadline + review ask | 1 email | Peak sentiment, warmest audience, currently asked for nothing | Content → n8n |
| 5 | Ship **cart recovery** (R1 / R2 / R3 already written) | 3 messages + trigger | Only item with directly recoverable revenue attached | Dev + Content |
| 6 | Resolve **canon conflicts 1, 2, 3**; mark [[communication-rules]] superseded | 1 decision session | Everything downstream inherits the ambiguity | Luis |
| 7 | Confirm **fatigue scope** — do 30/7/1 fire once or per session? | Verification | If per-session, parents are already being trained to ignore DR | Dev |
| 8 | Ship the **lead-magnet sequence** — guides are written, needs capture + delivery | 1 form + 6 emails | Largest unbuilt system; content cost already sunk | Content + Dev |
| 9 | Build **weekly banks** for tennis, pickleball, flag football | 18 emails | Structure proven; skill data already in vault | Content |
| 10 | Build **coach comms layer** — acceptance, onboarding, weekly plan, season wrap | 4 emails | Closes the widest coverage gap; reuses existing triggers | Content → n8n |
| 11 | Move coach dashboard to a **DR subdomain**, update template 06 | Dev | Trust + link durability | Dev |
| 12 | Clear remaining copy bugs (5, 6, 7, 9, 10) | 20 min | Cheap credibility | Content |

---

## The one-sentence version

DR has already written a better communication system than the one it is running — the work is not to design it again, it is to ship items 1–5 above and stop letting April's bugs reach August's parents.

---

## Open questions requiring a decision

1. **Is "fun-first" in or out?** Four canonical docs say in, the PMC says out. Copy cannot be written consistently until this resolves.
2. **Is there a first-practice trial?** The DNA money model is built on one; the PMC forbids it. This determines the entire acquisition offer.
3. **Is $129 public or checkout-only?** Objections doc quotes it as if parents see it; PMC forbids public pricing.
4. **Is n8n actually being retired, and by when?** If yes, fixing n8n templates is throwaway work and the sequence rebuild should target the new sender. If no, the Engine needs amending. This changes the sequencing of every dev item above.
