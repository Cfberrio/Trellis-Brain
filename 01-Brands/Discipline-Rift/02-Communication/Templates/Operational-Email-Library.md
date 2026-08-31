---
brand: Discipline-Rift
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: ClickUp Doc 8cqnrff-21297 → page NOTIFICATIONS (8cqnrff-28797),
  children 8cqnrff-6557, 6577, 6617, 6637, 6597, 6657, 6677, 6697 (templates 1, 3-8);
  templates 2, 9, 10 now sourced from code — see Changelog.
  (Old frontmatter pointed at doc 8cqnrff-8437 — that doc is a different, near-empty
  doc; corrected 2026-08-27.)
owner: Luis Torres
last_updated: 2026-08-31
last_verified_against_clickup: 2026-08-27
sensitivity: internal
hub_role: leaf
---

# DR Operational Email Library

## Parent
- [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|DR Communication Home]]

## Related
- [[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec|DR Email Design Spec]] — the render contract these three templates now follow (tables, inline styles, DR blue, black footer)
- [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season|Parent Communication — Volleyball Season]]
- [[01-Brands/Discipline-Rift/02-Communication/Templates/School-Outreach-Email-Templates|School Outreach Email Templates]]
- [[01-Brands/Discipline-Rift/06-DNA/Conversion|DR Conversion]]

## Purpose

Canonical operational email templates used across the registration → reminder → attendance flow.

> [!warning] Templates 2, 9, 10 migrated off this doc (2026-08-25)
> This note originally described the **n8n-era** ClickUp source for these templates. n8n is retired ([[01-Brands/Discipline-Rift/02-Communication/Communication-Home|Communication Home]]). The live source of truth for **Registration Confirmation**, **Parent Guide**, and **Waitlist Invite** is now code: `~/Documents/DISCIPLINERIFT/disciplinerift/supabase/functions/_shared/email-templates.ts`. The quoted block below for template #2 is kept as **historical record of the pre-fix design** — do not copy it into a live send. See [[#9. Parent Guide (migrated 2026-08-25)|§9]] and [[#10. Waitlist Invite (migrated 2026-08-25)|§10]] below, and the [[#Changelog — 2026-08-25|changelog]] at the bottom for what changed and why.
>
> Reminder templates (#3–5), Coach Session Reminder (#6), Parent Assistance (#7), and Coach Application Confirmation (#8) are unaffected.

> [!note] Engine status corrected 2026-08-27
> "n8n retired" is **only true for #2, #9, #10** (moved to Supabase edge functions). In the live ClickUp source the reminder + weekly families are still explicitly labelled n8n: pages `03. 30 day reminder (N8N)`, `04. 7 day reminder (N8N)`, `05. 1 day Reminder (N8N)`, `07. Parent Assistance (N8N)`, and the containers `COACHES (N8N)` and `WEEKLY (N8N)`. Treat n8n as **still the sending engine for #3–#7 and the 6-week volleyball sequence** until Luis confirms otherwise.
> #1 OTP is neither n8n nor this repo's mailer — it is a **Supabase Auth** template (merge token `{{ .Token }}`, not `{{ $json.* }}`).

Use this note as the source of truth before editing any live template.

## Template index

| # | Template | Trigger | Channel | Engine | Status (verified against ClickUp 2026-08-27) |
|---|---|---|---|---|---|
| 1 | OTP Email | Account verification | Transactional | Supabase Auth | **Copy rewritten 2026-08-31 — pending paste into Supabase Dashboard** (see [[#Changelog — 2026-08-31|changelog]]) |
| 2 | Registration Confirmation | Payment processed | Transactional | Code (`email-templates.ts`) | **Reorder + invoice redesign proposed 2026-08-31, not yet implemented in code** — see [[#Changelog — 2026-08-31|changelog]] |
| 3 | 15-Day Reminder (renamed from 30-Day) | 15 days pre-season | Reminder | n8n | **Rewritten 2026-08-31 — pending update in n8n/ClickUp** (cadence 30→15 days, new merge fields needed) |
| 4 | 7-Day Reminder | 7 days pre-season | Reminder | n8n | **Rewritten 2026-08-31 — pending update in n8n/ClickUp** |
| 5 | 1-Day Reminder | 1 day pre-season | Reminder | n8n | **Rewritten 2026-08-31 — pending update in n8n/ClickUp** |
| 6 | Coach Session Reminder | Daily — session not logged | Coach ops | n8n | **Link corrected 2026-08-31 — pending update in n8n/ClickUp** (Vercel preview → real `/coach` route) |
| 7 | Parent Assistance (no-show) | Student missed practice | Attendance | n8n | **Rewritten 2026-08-31 — pending update in n8n/ClickUp** |
| 8 | Coach Application Confirmation | Coach applied | Recruiting | Form → mailer | **Rewritten 2026-08-31 — pending update in form/mailer** (see [[#Changelog — 2026-08-31|changelog]]) |
| 9 | Parent Guide | Lead opts into 3-minute guide | Nurture / lead magnet | **DR-rebranded 2026-08-25**, code-only (not in this doc's original 8) |
| 10 | Waitlist Invite | Admin clicks Invite on Manage Roster | Roster ops | **DR-rebranded 2026-08-25**, code-only (not in this doc's original 8) |

## 1. OTP Email

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/01-OTP-Email|ClickUp `01.  OTP Email`]] (pre-rewrite copy — still the live version in Supabase until this is pasted in)*

> [!todo] Rewritten 2026-08-31 — paste into Supabase Dashboard → Auth → Email Templates
> Feedback: the old greeting ("Thank you for joining the Discipline Rift community. We're excited to have you with us!") was empty filler — no value to the reader. Replace with something warmer and more direct that signals urgency/value, and close the email on a warm note after the code instead of ending cold on the expiry line.

> **DISCIPLINE RIFT**
> Encouraging students to find their discipline and sport
>
> **Your season is about to start.**
> You're only one step away. Verify your account to activate it.
>
> **Verification Code:**
> `{{ .Token }}`
>
> Use this code to verify your account.
> This code will expire in 24 hours for security purposes.
>
> We look forward to seeing your child practice with our coaches and our teams.
>
> Discipline Rift

Merge token is `{{ .Token }}` — **Supabase Auth syntax**, not n8n `{{ $json.* }}`. Expiry copy says **24 hours**; keep it matched to the Supabase Auth OTP TTL, not to an n8n workflow setting. No code file backs this template — it lives only in the Supabase Auth dashboard, so it can't be edited by a commit; someone with dashboard access has to paste the new copy in.

## 2. Registration Confirmation

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/02-Registration-Confirmation|ClickUp `02. Registration Confirmation`]] (stale pre-fix design, not live anywhere)*

> [!todo] Reorder proposed 2026-08-31 — MD-only, not yet implemented in code, see [[#Changelog — 2026-08-31|changelog]]
> Live version still comes from `registrationConfirmationHtml()` in `~/Documents/DISCIPLINERIFT/disciplinerift/supabase/functions/_shared/email-templates.ts`, unchanged (receipt → student → team → schedule order, no season in the headline, old invoice). The order and invoice below are the proposed rewrite — deliberately docs-only for now until the final copy is confirmed, then it gets implemented in code.
>
> Feedback driving the 2026-08-31 change: the schedule is the most important thing a parent needs, so it now renders **first**, ahead of payment/emergency-contact info. Section order follows an explicit importance hierarchy: **coach + practice times → team → price → emergency contact.**

**Section order (top → bottom):**

1. **Hero:** "Registration Successful! `{{studentFirstName}}` is now registered for `{{SEASON_NAME}}`." (falls back to team name if the team has no season set)
2. **Practice Schedule** (emphasized card, top) — occurrences, **Coach**, Location, "Schedule shown in Miami timezone (EST/EDT)"
3. **Team Information** — Team, School, Location, program description
4. **Payment Receipt** — subtotal, processing fee, total paid, paid-on date
5. **Student** — name, grade, emergency contact name/phone (least-important info, now last)
6. Footer: `Discipline Rift · Torres Rivero LLC`, `713 W. Yale Street, Orlando, FL 32804`, contact line

**Invoice PDF (attached, redesigned 2026-08-31):** now carries the registered legal identity, which was missing before:
> Discipline Rift DBA / Torres Rivero LLC
> FEI/EIN: 86-3157842
> 926 Spring Palms Loop, Orlando, FL 32828

This block is on both the header band and the footer of the PDF (`~/Documents/DISCIPLINERIFT/disciplinerift/supabase/functions/_shared/invoice-pdf.ts`). Note: this address differs from the `713 W. Yale Street` address in the confirmation *email* footer (`DR_ADDRESS` in `email-templates.ts`, unchanged) — that constant is the everyday mailing/contact address; the invoice now shows the **principal address on the LLC filing** instead, per Luis's instruction. Flag if these two should actually match.

## 3. 15-Day Reminder (renamed from 30-Day)

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/03-30-Day-Reminder-N8N|ClickUp `03. 30 day reminder (N8N)`]] (still 30-day, not yet updated to match this rewrite)*

> [!todo] Rewritten 2026-08-31, links corrected 2026-08-31 — pending changes in n8n + ClickUp
> Cadence change: **30 days → 15 days** before season start (update the n8n trigger delay and rename the ClickUp page). Copy changes: address parent by name up front, tell them to get their child ready, add the season schedule, and tell parents coaches communicate through the Parent Dashboard rather than through admin — plus in-person after practice. Also drop "youth sports development" / "young athletes" language — DR develops **young players** in volleyball, tennis, pickleball, and flag football (flag football was missing from the old tagline; see the open issue this replaces).
>
> **Link corrected 2026-08-31:** all parent-coach messaging goes through the Parent Dashboard's messages section, never a coach's personal number or email — confirmed by Luis. The dashboard URL is real, not a placeholder: `https://www.disciplinerift.com/dashboard` (root `app/dashboard` in the frontend repo; the deep-linked messages route is `https://www.disciplinerift.com/dashboard/messages`, used today by `send-pending-message-notifications`). Also dropped "reach out directly if needed" — that implied a channel outside the dashboard, which doesn't exist.
>
> **New merge field needed:** `{{ $json.coachName }}` — confirm it exists in the n8n payload before shipping; it wasn't used by the old template. `parentDashboardUrl` is no longer a merge field, it's the static link above.

> Hi `{{ $json.firstname }}`,
>
> We're 15 days away from `{{ $json.name }}`! Make sure your child is ready. We're ready for them.
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> Coach `{{ $json.coachName }}` will be communicating with you through the Parent Dashboard. Message the coach anytime at https://www.disciplinerift.com/dashboard/messages. You're also welcome to say hi in person after practice.
>
> Before every practice, make sure your child:
> - Brings a water bottle and a snack to eat beforehand
> - Uses the bathroom before practice starts (there's a break before practice too, but it's best to go first)
>
> See your child on the court!
> Discipline Rift Team
>
> Discipline Rift
> Developing young players in volleyball, tennis, pickleball, and flag football
> Contact: info@disciplinerift.com · (407) 614-7454

## 4. 7-Day Reminder

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/04-7-Day-Reminder-N8N|ClickUp `04. 7 day reminder (N8N)`]] (not yet updated to match this rewrite)*

> [!todo] Rewritten 2026-08-31 — pending update in n8n + ClickUp
> Adds what to bring (water, a snack, comfortable clothes to play in), puts the schedule right after the reminder line, then coach, then sign-off. Mission tagline in the footer changes to the line Luis wants standardized across every operational email: *"Teaching developmental skills and inspiring passion for sport."* This also fixes the known duplicate-email-link bug in the old footer.

> Hi `{{ $json.firstname }}`,
>
> We're seven days away from `{{ $json.name }}`! Make sure to remind your child about practice: they'll need water, a snack for before practice, and comfortable clothes to play in.
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> Coach: `{{ $json.coachName }}`
>
> See your child on the court!
> Discipline Rift Team
>
> Discipline Rift
> Teaching developmental skills and inspiring passion for sport
> Contact: info@disciplinerift.com · (407) 614-7454

## 5. 1-Day Reminder

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/05-1-Day-Reminder-N8N|ClickUp `05. 1 day Reminder (N8N)`]] (not yet updated to match this rewrite)*

> [!todo] Rewritten 2026-08-31 — pending update in n8n + ClickUp; MD-only, not final
> Leads with the sport + "is tomorrow!" instead of a generic countdown, adds an excitement line naming the child(ren), then schedule → team → coach. This rewrite also drops the internal editorial line "Do you like this personality?" that was sitting at the end of the live ClickUp page — closes that open issue below, pending the actual ClickUp/n8n edit.
>
> **New merge fields needed:** `{{ $json.sport }}`, `{{ $json.childrenNames }}`, `{{ $json.coachName }}` — confirm these exist in the n8n payload; `{{ $json.name }}` (team) and `{{ $json.firstname }}` (parent) already did.

> Hi `{{ $json.firstname }}`,
>
> `{{ $json.sport }}` is tomorrow!
>
> We're very excited to see `{{ $json.childrenNames }}` at practice.
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> Team: `{{ $json.name }}`
> Coach: `{{ $json.coachName }}`
>
> See you on the court!
> Discipline Rift Team
>
> Discipline Rift
> Developing young players in volleyball, tennis, pickleball, and flag football
> Contact: info@disciplinerift.com · (407) 614-7454

## 6. Coach Session Reminder

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/COACHES-N8N/06-Coach-Session-Reminder|ClickUp `06. Coach session reminder`]] (still the Vercel preview link, not yet updated to match this fix)*

> [!todo] Link corrected 2026-08-31 (Luis) — pending update in n8n + ClickUp
> `https://dash-board-coaches-whpv.vercel.app/` was a Vercel preview host, not the real Coach Dashboard. The real one is `/coach` in `~/Documents/DISCIPLINERIFT/disciplinerift` (TanStack Start on Cloudflare Workers, OTP-gated, confirmed live at `src/routes/coach`), on the production domain from `src/lib/seo.ts` (`SITE_URL = "https://www.disciplinerift.com"`). Corrected link: `https://www.disciplinerift.com/coach`. Also replaced the em dash in the contact line with a middle dot, same as the other rewrites.

> **Discipline Rift — Session Record Reminder**
>
> Hello `{{ $json.name }}`,
>
> We noticed that today's session has not been submitted in the Coach Dashboard.
>
> Please log in and complete the session information so we can keep attendance and session records up to date.
>
> Go to Coach Dashboard: https://www.disciplinerift.com/coach
>
> Thank you!
> Contact: info@disciplinerift.com · (407) 614-7454

Notes (2026-08-27, link corrected 2026-08-31):
- The 2026-04 bug flag "uses bare `json.name` without delimiters" is **resolved** — the live source now uses `{{ $json.name }}`. See [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] §Email 06.
- Dashboard link fixed 2026-08-31: was the Vercel preview host `https://dash-board-coaches-whpv.vercel.app/`, now `https://www.disciplinerift.com/coach`, matching the live `/coach` route and the canonical `SITE_URL` in `src/lib/seo.ts`. Not yet pushed to n8n/ClickUp.

## 7. Parent Assistance (Attendance Note)

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/07-Parent-Assistance-N8N|ClickUp `07. Parent Assistance (N8N)`]] (not yet updated to match this rewrite)*

> [!todo] Rewritten 2026-08-31, corrected 2026-08-31 — pending update in n8n + ClickUp; MD-only, not final
> Names the sport alongside the team in the "we missed you" line, adds a "hope they're doing well" line, softens the advance-notice ask (thanks parents who already told us, nudges the ones who didn't, framed as courtesy, not a scolding), keeps the accountability line, and adds the Parent Dashboard messages link before the sign-off.
>
> **Correction 2026-08-31 (Luis):** parents can never message a coach directly, not a personal number, not a personal email. The Parent Dashboard has a dedicated messages section that's the only channel to a coach, so the original draft's "Message Coach `{{ coachName }}` directly: `{{ coachContact }}`" line is wrong and is removed. Replaced with the real messages link: `https://www.disciplinerift.com/dashboard/messages` (same route the `send-pending-message-notifications` cron already deep-links to with `?team=&parent=`).
>
> **New merge fields needed:** `{{ $json.sport }}` — confirm it exists in the n8n payload; `{{ $json.parentfn }}`, `{{ $json.studentfn }}`, `{{ $json.team }}` already did. `coachName`, `coachContact`, and `parentDashboardUrl` are no longer needed, drop them from the payload spec.

> Hi `{{ $json.parentfn }}`,
>
> We missed `{{ $json.studentfn }}` at practice today for `{{ $json.sport }}`, on `{{ $json.team }}`.
>
> Hope `{{ $json.studentfn }}` is doing well. They were missed at today's practice!
>
> If you already let us know about the absence, thank you for the heads up. If not, a heads-up in advance helps. We're coaches, not chasing down students before practice starts, so knowing ahead of time means one less thing to track.
>
> Our goal is to keep every player progressing and connected to the team, so thanks for helping us keep everyone accountable.
>
> Questions about today's practice? Message us anytime through your Parent Dashboard: https://www.disciplinerift.com/dashboard/messages
>
> Hope to see `{{ $json.studentfn }}` at the next practice!
>
> Discipline Rift
> Contact: info@disciplinerift.com · (407) 614-7454

## 8. Coach Application Confirmation

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/08-Confirmation-Application|ClickUp `08. Confirmation application`]] (stale pre-fix copy, live version still hardcoded "Hi name,")*

> [!todo] Rewritten 2026-08-31 — pending update in form/mailer, see [[#Changelog — 2026-08-31|changelog]]
> Source of the fix: [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] §Email 08 and §9 Known Bugs #4 — the only mandatory item is wiring `{{ $json.firstname }}` to the opening salutation (flagged 2026-04-21, still open 2026-08-27, "will produce visibly broken emails in production"). Luis's own audit of that draft also logged two improvement opportunities, applied below: replace the `[X business days]` placeholder with a concrete number, and add a line on what DR looks for in a coach to reinforce brand standards at application stage. Third opportunity (link to a coach resources/FAQ page) **not applied** — no such page confirmed to exist yet.
>
> Subject and body below are Luis's own drafted template from communication-rules.md §Email 08, not a new rewrite — this pass only closes the bug and fills the placeholder.

**Subject:** We got your application. Here's what happens next

> Hi `{{ $json.firstname }}`,
>
> Thanks for applying to coach with Discipline Rift.
>
> We've received your application and will review it within 5 business days.
>
> What happens next:
> 1. Our team reviews your application
> 2. If there's a fit, we'll reach out to schedule an interview
> 3. Selected coaches complete our onboarding process
>
> We're looking for coaches who can hold a group's attention and treat every player, nervous or confident, with the same patience.
>
> In the meantime, feel free to reply to this email with any questions.
>
> Talk soon,
> The Discipline Rift Coaching Team

Old (still-live) copy, kept for reference:

> Hi `[name]`,
>
> Thanks for applying to be a coach at Discipline Rift!
>
> Our mission is to help young players grow through humility, perseverance, and adaptability — and we're excited you want to be part of that journey.
>
> We'll review your application and reach out soon if it's a fit.
>
> Until then, learn more about our coaching culture through our social media channels.
>
> – The DR Team
> info@disciplinerift.com

## 9. Parent Guide (migrated 2026-08-25)

Lead-magnet email — "3-minute Parent Guide," signed as Coach Luis, five tips + season pitch + two CTAs. Not part of the original ClickUp 8-template set; it lived only in code (`parentGuideHtml()`) and had the same class-based/`linear-gradient` build as the pre-fix Registration Confirmation. Rebuilt on the shared DR shell — see [[#Changelog — 2026-08-25|changelog]]. Copy is unchanged from the pre-existing version; only the markup changed.

> **DISCIPLINE RIFT**
>
> **Here you go! Your 3-minute Parent Guide**
> From Coach Luis at Discipline Rift
>
> Hi `{{firstName}}`,
>
> What if this was the season your child did not just participate… But discovered something about themselves?
>
> Five tips: *Start Every Week with Curiosity* · *Create a 10 Minute Ritual* · *Celebrate Small Wins* · *Let Them Teach You* · *Talk About Growth*
>
> [REGISTER FOR THE SEASON] · [FIND YOUR SCHOOL]
>
> *What if this season everything shifts?*

Trigger: `send-parent-guide` edge function. Live source: `parentGuideHtml(name)` in `email-templates.ts`.

## 10. Waitlist Invite (migrated 2026-08-25)

Sent only when an admin clicks **Invite** on Manage Roster — see [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|Communication Home]] waitlist notes. No seat is held, the link never expires, so copy carries no deadline/scarcity language (enforced by a test: `waitlist-email.test.ts` bans "expire," "48 hour," "holding," "hurry," etc.). Not part of the original ClickUp 8-template set. Rebuilt on the shared DR shell.

> **DISCIPLINE RIFT**
>
> **You're invited to register!**
> A spot is open on `{{teamName}}`
>
> Hi `{{parentName}}`,
>
> Good news — a spot is available on **`{{teamName}}`** (`{{sport}}`), and we'd love to have your child join us.
>
> [REGISTER NOW]
>
> **What happens next**
> 1. Tap the button above to open your registration.
> 2. Confirm your details and complete checkout.
> 3. Your child's spot on `{{teamName}}` is confirmed. Done.

Trigger: `waitlist-invite` edge function. Live source: `waitlistInviteHtml(d)` in `email-templates.ts`.

## Changelog — 2026-08-25

**Bug found:** ClickUp 86e2za2bj — parents saw literal `=20` in the Registration Confirmation email. Root cause: `denomailer` 1.6.0's `quotedPrintableEncode` is broken (`replaceAll("=", "=3D")` discards its own result, so `=` is never escaped; the 74-char fold loop then drops the char it cut on the last iteration → corrupt quoted-printable stream).

**Fix:** `sendMail()` in `_shared/email.ts` no longer passes `html:` to denomailer — the body now goes as base64 `mimeContent` (RFC 2045, 76-char folded). This is the single choke point for every transactional email in this repo, so it fixed all of them at once, not just Registration Confirmation.

**Rebrand:** while fixing the encoding bug, the underlying design was also off-brand and structurally fragile for Gmail — class-based `<style>` blocks, `display:flex`, `display:grid`, `linear-gradient()`. Gmail (web, app, and forwards) is unreliable with all four. Three templates were rebuilt on a shared table + inline-style shell (`drShell` / `drHeader` / `drFooter` / `drButton` in `email-templates.ts`), using the tokens from [[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec|DR Email Design Spec]] (`#0497F7` / `#0378C6` / Inter stack / outlined cards / black footer):

- **Registration Confirmation** (`registrationConfirmationHtml`) — receipt itemizes registration + processing fee (3.25% + $0.25) → total; student card; team card; full practice schedule.
- **Parent Guide** (`parentGuideHtml`) — new §9 above.
- **Waitlist Invite** (`waitlistInviteHtml`) — new §10 above.

Not touched: `jobApplicationHtml` (internal-only, staff inbox) and `paymentNotifyHtml` (internal-only, already table-based).

**Verification:** rendered with real sample data via `bun`, screenshotted in Playwright at 660px (desktop) and 375px (mobile) — no horizontal scroll, no clipped text, buttons full-width on mobile. Test suite asserts Gmail-safety directly: no `display:flex`, no `display:grid`, no `linear-gradient`, no `<style>` outside the Outlook `mso` conditional comment. 15 tests across `email-templates.test.ts` + `waitlist-email.test.ts`, all passing.

**Commits (`~/Documents/DISCIPLINERIFT/disciplinerift`, `main`):**
- `75992b4` — kill `=20` (base64 body) + rebrand Registration Confirmation
- `e1eae82` — rebrand Parent Guide + Waitlist Invite to the same shell

**Deployed:** `dr_ghl_registered`, `send-parent-guide`, `submit-application`, `waitlist-invite`, `ghl-sync-contacts` — manually redeployed by Domis (`supabase functions deploy … --project-ref hvgcxtawrditxvgvqfxb`; the CLI-linked account used by Claude Code gets a 403 on this project, so this step cannot be automated end-to-end yet).

**Not done in this pass:** #1 OTP, #3–5 reminders, #6 coach reminder, #7 attendance note, #8 coach application — still on whatever their original engine is; not verified against Gmail-safety in this pass. `jobApplicationHtml` still has one `linear-gradient()` header (internal-only, low risk, left as-is).

## Changelog — 2026-08-27 (verification pass vs ClickUp)

Full re-read of ClickUp Doc `8cqnrff-21297` → **NOTIFICATIONS** and its children. What changed in this note:

- **Source pointer fixed.** Frontmatter said doc `8cqnrff-8437`; that doc holds a single empty page. The real source is `8cqnrff-21297` / page `8cqnrff-28797` (NOTIFICATIONS). Same correction applied to [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season|Parent Communication — Volleyball Season]].
- **Engine claim corrected.** "n8n retired" was over-broad — see the callout at the top. #3–#7 and the weekly volleyball sequence are still n8n-labelled at source.
- **#1 OTP** — body verified verbatim; added that the merge token is Supabase Auth `{{ .Token }}`, not n8n syntax.
- **#3–#5** — bodies verified verbatim. Footer block (`Youth Sports Development` / sports line / contact) was documented only under #3; now added to #4 and #5 to match source.
- **#6** — verified; the 2026-04 merge-field bug is fixed at source. Dashboard URL still a Vercel preview host.
- **#7** — verified verbatim.
- **#8** — verified; `Hi name,` bug still open.
- **Weekly volleyball (#09–#14)** — all six verified verbatim against ClickUp; no drift.

## Known issues open at 2026-08-27

| # | Issue | Where | Impact | Status |
|---|---|---|---|---|
| 8 | `Hi name,` — first-name merge field never wired | ClickUp `08. Confirmation application` | Every coach applicant gets an unpersonalized greeting | **Fixed in §8 rewrite, pending push to form/mailer** |
| 3–5 | Footer tagline reads *"Developing Young Athletes in Volleyball, Tennis, & Pickleball"* — **omits Flag Football**, which DR runs (see [[01-Brands/Discipline-Rift/00-Brand-Core/Offers|DR Offers]], [[01-Brands/Discipline-Rift/06-DNA/Offer|DR Offer DNA]], and the ClickUp SPORT DESCRIPTIONS pages) | n8n reminder templates | Under-sells the catalog to flag-football parents | **Fixed in §3 rewrite, pending push to n8n** |
| 4 | `info@disciplinerift.com` printed twice in the footer | ClickUp `04. 7 day reminder (N8N)` | Sloppy footer | **Fixed in §4 rewrite, pending push to n8n** |
| 5 | Editorial line *"Do you like this personality?"* sits at the end of the page | ClickUp `05. 1 day Reminder (N8N)` | Risk of shipping an internal note to parents | **Fixed in §5 rewrite, pending push to n8n** |
| 2 | Phone written `(407) 6147454` (no dash) on the ClickUp page | ClickUp `02. Registration Confirmation` | Cosmetic; live code version already uses `(407) 614-7454` | Open (ClickUp page still stale; live code unaffected) |
| 6 | Coach Dashboard link is a Vercel preview URL (`dash-board-coaches-whpv.vercel.app`) | ClickUp `06. Coach session reminder` | Fragile / off-brand link in coach-facing mail | **Fixed in §6, pending push to n8n** — real link is `https://www.disciplinerift.com/coach` |
| 1, 3–8 | None of these have been through the Gmail-safety rebuild that #2/#9/#10 got | n8n / Supabase Auth templates | Unknown render quality; banner still a ClickUp-attachment image URL | Open |

## Changelog — 2026-08-31 (copy rewrite from Luis feedback)

Six templates rewritten from Luis's dictated feedback (first pass covered #1–#4; a follow-up round added #5 and #7). **This is a documentation-only pass** — Luis asked explicitly not to touch the live registration-confirmation code until the copy is confirmed, so nothing here is implemented anywhere yet. A `registrationConfirmationHtml()`/`invoice-pdf.ts` reorder for #2 was drafted and unit-tested in code earlier today, then **reverted at Luis's request** — the live code is back to its original order/copy. Every section below is a proposal to review, not a live change.

- **#1 OTP** — warmer opener ("Your season is about to start. You're only one step away.") replacing empty "welcome to the community" filler; added a warm sign-off after the code ("We look forward to seeing your child practice with our coaches and our teams."). Lives only in the Supabase Auth dashboard — no repo file to commit even once approved.
- **#2 Registration Confirmation** — proposed reorder: Practice Schedule (coach + times) first, then Team, then Payment, then Student/emergency-contact last, matching the importance hierarchy Luis gave (coach → team → times → price → emergency contact). Headline would name the season (`team.season`, present in the `team` table but not currently passed to the email). Invoice PDF redesign would add the registered legal identity (DBA, FEI/EIN, principal address), which is missing today. **Not implemented** — code is unchanged; this is the spec for when Luis confirms the final copy.
- **#3 30→15-Day Reminder** — cadence cut from 30 to 15 days; copy now names the parent, tells them to get their child ready, adds the schedule, and explains coaches communicate through the Parent Dashboard or in person, not through admin. Tagline corrected to "young players in volleyball, tennis, pickleball, and flag football" (previously said "young athletes" and omitted flag football — closes a known issue above). Uses the real Parent Dashboard messages link (`https://www.disciplinerift.com/dashboard/messages`, corrected 2026-08-31 per Luis) instead of a placeholder merge field. Needs one new merge field (`coachName`) added to the n8n payload.
- **#4 7-Day Reminder** — adds what to bring (water, snack, comfortable clothes), schedule ordered right after the reminder line, coach name added, footer tagline standardized to "Teaching developmental skills and inspiring passion for sport." Also fixes the known duplicate-footer-link bug.
- **#5 1-Day Reminder** — leads with the sport + "is tomorrow!" instead of a generic countdown, adds an excitement line naming the child(ren), then schedule → team → coach. Drops the internal editorial line "Do you like this personality?" that was sitting at the end of the live ClickUp page. Needs three new merge fields (`sport`, `childrenNames`, `coachName`).
- **#7 Parent Assistance** — names the sport alongside the team in the "we missed you" line, adds a "hope they're doing well" line, softens the advance-notice ask (thanks parents who already told us, nudges the ones who didn't, framed as courtesy not a scolding), keeps the accountability line, and adds the Parent Dashboard messages link before the sign-off. **Corrected 2026-08-31 (Luis):** the first draft had a "message the coach directly" line with a `coachContact` field — dropped, parents can never message a coach directly, only through the Parent Dashboard's messages section. Uses the real link `https://www.disciplinerift.com/dashboard/messages` instead of a placeholder. Needs one new merge field (`sport`).
- **#8 Coach Application Confirmation** — closes the open `Hi name,` bug (2026-04-21, still shipping broken as of 2026-08-27) by wiring `{{ $json.firstname }}` to the salutation, per Luis's own §Email 08 audit and §9 Known Bugs #4 in communication-rules.md. New subject "We got your application. Here's what happens next" and body are Luis's already-drafted template from that doc, not a new rewrite; this pass only fills the `[X business days]` placeholder (set to 5 business days) and adds one line on what DR looks for in a coach — both improvement opportunities Luis flagged in the same audit. The third opportunity (FAQ/resources link) is skipped — no such page confirmed.

- **#6 Coach Session Reminder** — link-only fix, no copy changes. The Coach Dashboard link was a Vercel preview host (`dash-board-coaches-whpv.vercel.app`), not the real destination. Corrected to `https://www.disciplinerift.com/coach`, the live `/coach` route in `disciplinerift` (confirmed against `src/routes/coach` and the canonical `SITE_URL` in `src/lib/seo.ts`). Contact-line em dash also swapped for a middle dot to match the rest of the pass.

**Not touched in this pass:** #9, #10 — Luis's feedback only covered #1–#7 (copy) and #6 (link only). Nothing in this changelog is live anywhere (n8n, ClickUp, Supabase, or code) until Luis reviews and it gets pushed to each system separately.

## Operating rules

- **Voice anchor:** "humility, perseverance, adaptability" (per Coach Application).
- **Standard sign-off:** Discipline Rift — info@disciplinerift.com — (407) 614-7454.
- **Tone:** warm, operational, parent-friendly. Never marketing-pushy.
- **Template merge fields:** match GHL / n8n payload — confirm field names before changing. Templates 2, 9, 10 are code now — merge is plain JS interpolation, not `{{ }}`/`${}` tokens; the tokens shown in §2/§9/§10 above are illustrative of the old system, not the live one.
- **Image attachments:** banner image attached to templates 1, 3–8 (`https://t9017418223.p.clickup-attachments.com/...`). Templates 2, 9, 10 use the hosted DR wordmark/brand assets instead — see [[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec|DR Email Design Spec]] §12.
