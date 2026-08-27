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
last_updated: 2026-08-27
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
| 1 | OTP Email | Account verification | Transactional | Supabase Auth | Matches ClickUp `01. OTP Email` — verbatim ✅ |
| 2 | Registration Confirmation | Payment processed | Transactional | Code (`email-templates.ts`) | **Code is live; ClickUp page 02 is stale pre-fix design** — see [[#Changelog — 2026-08-25|changelog]] |
| 3 | 30-Day Reminder | 30 days pre-season | Reminder | n8n | Matches ✅ — footer tagline outdated (see [[#Known issues open at 2026-08-27\|open issues]]) |
| 4 | 7-Day Reminder | 7 days pre-season | Reminder | n8n | Matches ✅ — footer was missing here, added 2026-08-27 |
| 5 | 1-Day Reminder | 1 day pre-season | Reminder | n8n | Matches ✅ — footer was missing here, added 2026-08-27 |
| 6 | Coach Session Reminder | Daily — session not logged | Coach ops | n8n | Matches ✅ — merge-field bug from 2026-04 is **fixed** in source |
| 7 | Parent Assistance (no-show) | Student missed practice | Attendance | n8n | Matches ✅ |
| 8 | Coach Application Confirmation | Coach applied | Recruiting | Form → mailer | Matches ⚠️ — still hardcoded `Hi name,` (open bug) |
| 9 | Parent Guide | Lead opts into 3-minute guide | Nurture / lead magnet | **DR-rebranded 2026-08-25**, code-only (not in this doc's original 8) |
| 10 | Waitlist Invite | Admin clicks Invite on Manage Roster | Roster ops | **DR-rebranded 2026-08-25**, code-only (not in this doc's original 8) |

## 1. OTP Email

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/01-OTP-Email|ClickUp `01.  OTP Email`]]*

> **DISCIPLINE RIFT**
> Encouraging students to find their discipline and sport
>
> **Welcome to Discipline Rift!**
> Thank you for joining the Discipline Rift community. We're excited to have you with us!
>
> **Verification Code:**
> `{{ .Token }}`
>
> Use this code to verify your account.
> This code will expire in 24 hours for security purposes.

Merge token is `{{ .Token }}` — **Supabase Auth syntax**, not n8n `{{ $json.* }}`. Expiry copy says **24 hours**; keep it matched to the Supabase Auth OTP TTL, not to an n8n workflow setting.

## 2. Registration Confirmation

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/02-Registration-Confirmation|ClickUp `02. Registration Confirmation`]]*

> [!info] Historical only — see [[#Changelog — 2026-08-25|changelog]] for the live version
> The quote below is the **pre-fix, off-brand** design (class-based CSS, `display:flex`/`display:grid`, `linear-gradient`, generic blue/green). It is preserved here for reference. The email parents receive today comes from `registrationConfirmationHtml()` in code — DR blue `#0497F7`, table + inline-style layout, itemized receipt with processing fee, black footer.

> **DISCIPLINE RIFT**
> ✅ Registration Successful!
>
> Your payment has been processed successfully.
>
> **PAYMENT CONFIRMATION**
> Amount: $`${AMOUNT}`
> Payment confirmed on: `${DATE}`
>
> **STUDENT INFORMATION**
> Full Name: `${STUDENT_FIRST_NAME} ${STUDENT_LAST_NAME}`
> Grade: `${GRADE}`
> Emergency Contact: `${EMERGENCY_CONTACT_NAME}`
> Emergency Phone: `${EMERGENCY_PHONE}`
>
> **TEAM INFORMATION**
> Team Name: `${TEAM_NAME}`
> School: `${SCHOOL_NAME}`
> Location: `${SCHOOL_LOCATION}`
> Price: `${TEAM_PRICE}`
> Description: `${TEAM_DESCRIPTION}`
>
> **PRACTICE SCHEDULE**
> `${PRACTICE_OCCURRENCES}`
> Coach: `${COACH_NAME}`
> Location: `${LOCATION}`
> Schedule shown in Miami timezone (EST/EDT)
>
> ---
> Discipline Rift
> Support: info@disciplinerift.com
> Phone: (407) 614-7454
> Web: www.disciplinerift.com

## 3. 30-Day Reminder

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/03-30-Day-Reminder-N8N|ClickUp `03. 30 day reminder (N8N)`]]*

> Hi `{{ $json.firstname }}`,
>
> There are 30 days left until the start of `{{ $json.name }}`.
>
> Make sure to remind your child about the practices! Here's the complete schedule:
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> See your child on the court!
> — Discipline Rift Team
>
> Discipline Rift - Youth Sports Development
> Developing Young Athletes in Volleyball, Tennis, & Pickleball
> Contact: info@disciplinerift.com — (407) 614-7454

## 4. 7-Day Reminder

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/04-7-Day-Reminder-N8N|ClickUp `04. 7 day reminder (N8N)`]]*

> Hi `{{ $json.firstname }}`,
>
> There are seven days left until the start of `{{ $json.name }}`.
>
> Make sure to remind your child about the practices! Here's the complete schedule:
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> See your child on the court!
> — Discipline Rift Team
>
> Discipline Rift - Youth Sports Development
> Developing Young Athletes in Volleyball, Tennis, & Pickleball
> Contact: info@disciplinerift.com — (407) 614-7454

⚠️ The live ClickUp page prints the `info@disciplinerift.com` link **twice** in the footer. Fix in n8n on next edit.

## 5. 1-Day Reminder

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/05-1-Day-Reminder-N8N|ClickUp `05. 1 day Reminder (N8N)`]]*

> **Discipline Rift — 1-Day Reminder for `{{ $json.name }}`**
>
> Hi `{{ $json.firstname }}`,
>
> There is **one day** left until the start of **`{{ $json.name }}`**.
>
> Make sure to remind your child about the practices! Here's the complete schedule:
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> See your child on the court!
> — Discipline Rift Team
>
> Discipline Rift - Youth Sports Development
> Developing Young Athletes in Volleyball, Tennis, & Pickleball
> Contact: info@disciplinerift.com — (407) 614-7454

⚠️ The live ClickUp page ends with an internal editorial line — **"Do you like this personality?"**. That is a note to the team, not email copy; confirm it is not inside the n8n HTML body.

## 6. Coach Session Reminder

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/COACHES-N8N/06-Coach-Session-Reminder|ClickUp `06. Coach session reminder`]]*

> **Discipline Rift — Session Record Reminder**
>
> Hello `{{ $json.name }}`,
>
> We noticed that today's session has not been submitted in the Coach Dashboard.
>
> Please log in and complete the session information so we can keep attendance and session records up to date.
>
> Go to Coach Dashboard: https://dash-board-coaches-whpv.vercel.app/
>
> Thank you!
> Contact: info@disciplinerift.com — (407) 614-7454

Notes (2026-08-27):
- The 2026-04 bug flag "uses bare `json.name` without delimiters" is **resolved** — the live source now uses `{{ $json.name }}`. See [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] §Email 06.
- Dashboard link still points at the Vercel preview host `https://dash-board-coaches-whpv.vercel.app/`. No custom DR domain in the vault. Confirm this is the intended production URL before the next coach-facing send.

## 7. Parent Assistance (Attendance Note)

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/07-Parent-Assistance-N8N|ClickUp `07. Parent Assistance (N8N)`]]*

> **Discipline Rift — Attendance Note**
>
> Hi `{{ $json.parentfn }}`,
>
> We missed `{{ $json.studentfn }}` at practice today for `{{ $json.team }}`.
>
> We know things come up — schedules change, rides run late, or something at school pops up. If there was any issue getting to practice today, just let us know so we can note it on our end.
>
> Our goal is to keep every player progressing and feeling part of the team, so thanks for helping us keep attendance up to date.
>
> You can reply to this email or reach us here if you need to update anything about today's session.
>
> See you at the next practice!
> Discipline Rift

## 8. Coach Application Confirmation

*Verbatim source: [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/08-Confirmation-Application|ClickUp `08. Confirmation application`]]*

> [!bug] Open bug, still present 2026-08-27
> The live source literally reads **"Hi name,"** — the applicant first-name merge field was never wired. Every applicant receives "Hi name,". Flagged originally 2026-04-21 in [[01-Brands/Discipline-Rift/02-Communication/communication-rules|DR Communication Rules]] §Email 08; re-checked against ClickUp today and **not fixed**.

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

| # | Issue | Where | Impact |
|---|---|---|---|
| 8 | `Hi name,` — first-name merge field never wired | ClickUp `08. Confirmation application` | Every coach applicant gets an unpersonalized greeting |
| 3–5 | Footer tagline reads *"Developing Young Athletes in Volleyball, Tennis, & Pickleball"* — **omits Flag Football**, which DR runs (see [[01-Brands/Discipline-Rift/00-Brand-Core/Offers|DR Offers]], [[01-Brands/Discipline-Rift/06-DNA/Offer|DR Offer DNA]], and the ClickUp SPORT DESCRIPTIONS pages) | n8n reminder templates | Under-sells the catalog to flag-football parents |
| 4 | `info@disciplinerift.com` printed twice in the footer | ClickUp `04. 7 day reminder (N8N)` | Sloppy footer |
| 5 | Editorial line *"Do you like this personality?"* sits at the end of the page | ClickUp `05. 1 day Reminder (N8N)` | Risk of shipping an internal note to parents |
| 2 | Phone written `(407) 6147454` (no dash) on the ClickUp page | ClickUp `02. Registration Confirmation` | Cosmetic; live code version already uses `(407) 614-7454` |
| 6 | Coach Dashboard link is a Vercel preview URL (`dash-board-coaches-whpv.vercel.app`) | ClickUp `06. Coach session reminder` | Fragile / off-brand link in coach-facing mail |
| 1, 3–8 | None of these have been through the Gmail-safety rebuild that #2/#9/#10 got | n8n / Supabase Auth templates | Unknown render quality; banner still a ClickUp-attachment image URL |

## Operating rules

- **Voice anchor:** "humility, perseverance, adaptability" (per Coach Application).
- **Standard sign-off:** Discipline Rift — info@disciplinerift.com — (407) 614-7454.
- **Tone:** warm, operational, parent-friendly. Never marketing-pushy.
- **Template merge fields:** match GHL / n8n payload — confirm field names before changing. Templates 2, 9, 10 are code now — merge is plain JS interpolation, not `{{ }}`/`${}` tokens; the tokens shown in §2/§9/§10 above are illustrative of the old system, not the live one.
- **Image attachments:** banner image attached to templates 1, 3–8 (`https://t9017418223.p.clickup-attachments.com/...`). Templates 2, 9, 10 use the hosted DR wordmark/brand assets instead — see [[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec|DR Email Design Spec]] §12.
