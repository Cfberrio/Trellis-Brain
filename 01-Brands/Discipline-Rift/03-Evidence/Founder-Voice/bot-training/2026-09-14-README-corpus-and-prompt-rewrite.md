---
brand: Discipline-Rift
area: evidence
subarea: training
note_type: evidence
status: review
canonical: false
used_for_ai: true
source_type: curated
sensitivity: internal
hub_role: leaf
last_updated: 2026-09-14
up:
  - "[[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/2026-09-14-PROMPTS-active]]"
---

# DR — bot prompt rewrite 2026-09-14: corpus, decisions, validation

> [!info] Status
> Prompts **activated 2026-09-14 17:14 ET** (sms v6 · email v4 · gmail v2) in production `brand_prompts` (ClickUp 86e38pqmw). Luis's review of copy is still open; a rollback is one `UPDATE ... SET active` away. Raw verbatim corpus (client PII) lives in the Trellis repo at `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/` (git-ignored), never in this vault. Prompt files + SQL: `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/`.

## Parent
- [[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/bot-training/2026-09-14-PROMPTS-active|DR proposed prompts]]

## Inventory and method

**DR 200 → 944; OEV 292 → 382; combined 492 → 1,326 exchanges.** Gmail additions: info@disciplinerift.com 695, disciplinerift@gmail.com 49, orlandoeventvenue@gmail.com 90. The `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/README.md` (corpus README) contains the full before/after category × channel table; `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/counts.json` (counts.json) preserves the baseline and merged counts. Inbound channel determines the table column; mixed reply channels remain separately recorded.

GHL bodies/JSON evidence were retained. Gmail bodies are reproduced verbatim, with 45 coach exchanges indexed in the brief coach file rather than copied into parent/faculty voice training. The `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/gmail-classification.jsonl` (Gmail classification manifest) preserves every source field and adds category, role, source index, lesson and uncertainty. There are 28 explicitly uncertain records; uncertain, coach, vendor, internal, test and automated records are not approved voice examples. Some supplied Gmail records contain HTML/residual quoted messages or internal replies; no re-extraction or cleanup was attempted. Operator authorship is supplied/inferred, not independently established as Luis for each record. Legacy GHL assignments and imperfect temporal pairings are preserved, not certified.

## Per-prompt diff summary

| Output | Retained | Changed |
|---|---|---|
| `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/dr_sms_v6.txt` | Section order, live schedule/family logic, canonical facts, registration URL, score/schema, parent voice | First-step cheap skips + contextual coach skip; exact three signup states; faculty roster acknowledgment and numbered answers; warm nonempty refund review draft; Portuguese; ~400-character ceiling; removed unsupported attendance-logged/“checking now” claims. |
| `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/dr_email_v4.txt` | Email structure, subject behavior, exact sign-off, canonical facts, live family/schedule logic | Same DR routing/status/faculty/refund changes; numbered complete school answers within ~150 words; school W9 distinguished from staff documents; scoped “shortly” roster exception replaces conflicting blanket prohibition. |
| `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/dr_gmail_v2.txt` | Parent/faculty registers, audience enum, empty subject, signature, Fit Guarantee explanation, HUMAN REVIEW prefix, human review/send | Added explicit strict JSON shape, all input names and QUOTED_CONTEXT; three signup states; coach skip; faculty handling; warm refund proposal; live team price over default; privacy/date checks; Portuguese; ~150 words, up to ~250 only for faculty multi-question mail. |

All six preserve human review/send and the 0.75 suppression threshold. No output keys or decision/audience enum values were added. The new prompts omit the obsolete registration status; historical current prompt files remain verbatim as inputs. OEV SMS/email keep their existing empty flag_human draft convention; DR SMS/email intentionally change it to a safe proposed reply for refunds, while both Gmail prompts keep their existing human-review banner.

## Evidence and decisions

### DR faculty, rosters and documents

- **Rosters can receive a warm draft, but no fabricated permanent link.** `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/dr/school-admin.md` (school-admin.md), Gmail indices 177/183, threads `1a06cda61050030f` / `1a06c1e444e2c7fd`: “We'll send you the roster regardless in a bit.” Index 178 offers a live roster link, but the supplied reply contains no actual `/r/<token>` URL. The prompt permits “We'll send you the roster shortly” for an established school requesting its own roster. It does not promise EOD or claim delivery. The reviewer must perform the follow-up. Unverified recipient, roster contents/corrections or access disputes still flag.
- **Needed for actual link delivery:** a proposed future `SCHOOL_CONTEXT` block with verified school_id/name, recipient authorization, roster_url for that exact school, allowed audience/scope and current validity. Server-side authorization must happen before including the URL. The roster endpoint must enforce access; the model must not infer authorization from a school-looking email alone. No new block is assumed by these prompts and no endpoint/code was changed. Existing ACTIVE_PROGRAMS does not supply this resource.
- **Facilitron dates:** indices 177/183 explicitly distinguish the true start from an earlier Facilitron reservation. Answer dates from current program records; do not copy the historical “next week” or assert a correction has been submitted. Thread `19eacced8a37690e`, indices 468–475, shows real schedule negotiation under an inherited **Delivery Status Notification** subject: subject-only skipping is unsafe.
- **Session 2:** indices 121–123, thread `1a08bdc3ca9f7974`, show negotiation to retain Monday tennis, then an age-group staffing proposal. Warmth and flexibility do not authorize the bot to commit coaches or change days. Draft verified dates; flag unresolved commitments. Complete numbered answers improve on historical replies that only answer part of the inquiry.
- **Registration Links:** `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/dr/vendor-other-skip.md` (vendor-other-skip.md), index 90 / `1a0a0cf8c1bbaf99`, inbound requests Flag Football/Tennis links and blurbs. The paired reply begins “Tenemos que hacer esto hoy” and is an internal instruction, not faculty-facing voice. Preserved and flagged, with a cross-reference in school-admin. The bot should answer the underlying school request only when it is actually addressed to the school and the live team/status data supports it.
- **Clubs Next Week:** school-admin index 182 / `1a067ad1a0c3578a`: the school asks for copyable rosters, session dates and teacher inclusion. The reply asks about unused flyers instead. This is evidence of incomplete/possibly asynchronous pairing, not a model answer to imitate. Preserve all asks in the bot's numbered reply; do not claim an attachment or recipient action.
- **COI / EOD:** school-admin index 248 / `1a044db5b3911e54` says “Will have by by EOD or tomorrow.” That is a specific human insurance-request commitment, not a general roster SLA. The rewrite does not adopt it. Index 833 / `19d96e1048d0b0c6` is a school bookkeeper's W9 request, answered “Please find attached!”; the bot lacks that attachment, so flag with a warm proposal. Agreements indices 108–119 and Tildenville flyer/Meet the Teacher indices 803–805 likewise require facts or actual resources before delivery/attendance claims.

### DR coaches, refunds and languages

- `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/dr/coach.md` (coach.md): Gmail 105 “Missing Days”, 184 “Conflict in Scheduling”, 366 “Direct Deposit Auth”, 736–737 “Payrolls”, 723–724 / 743 / 746–754 availability, and 761 time off justify the contextual fallback. The bot skips even a coach message that would normally trigger money/safety escalation; the task explicitly requires this routing. Faculty and parent questions *about* coaches remain in scope.
- `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/dr/parent-refund-cancel.md` (parent-refund-cancel.md): index 327 “Pinecrest avalon soccer” provides “I completely understand that plans change”; index 372 “Refund” acknowledges Mialani's schedule conflict and welcomes a later season; indices 173, 243, 295–297 and 328 provide injury/withdrawal/refund voice. The rewrite uses that personal, direct tone but removes claims of completed refund/unenrollment and unsupported amounts or timelines.
- **Fall cancellation found:** index 156, thread `1a07cc4b6bb60fef`, September 8, 2026, “Team Cancellation — VOLLEYBALL ALOMA”: cancellation for low registration, conflicting automated reminder, apology and historical full-refund timing. The full pair is in the refund corpus. No exact “Season Cancellation” subject or broader team-wide Fall 2026 cancellation set was located in the supplied Gmail file or permitted raw DR cache. Individual Fall withdrawals are not relabeled as cancelled teams.
- **Refund-policy tension remains:** school-admin index 281 says “we always do full refunds at any point of the season,” whereas current DR Gmail states a first-two-practices credit guarantee with a 48-hour request window. Preserve the current canonical explanation; human review resolves requests and exceptions. Do not silently create a universal refund policy or reuse historical custom code DELK (index 199).
- DR language matching explicitly includes Portuguese as requested. No unambiguous Portuguese parent/reply example was located by the targeted language search in the supplied corpus; this is a task rule, not a claim of independently verified Portuguese voice evidence. The internal Spanish replies (e.g. index 90/551) are not parent voice.

## Deterministic skip candidates for code

Normalize the **actual latest sender email** and strip repeated Re:/Fw:/Fwd: prefixes for subject comparison. Do not search entire quoted history for skip words. Sender/subject patterns are candidates scoped below, not an instruction to blanket-block school or customer domains. Handle customer contact-form transport and actual human replies before generic automation rules.

| Pattern / category | Observed evidence | Safe scope |
|---|---|---|
| `^(mailer-daemon@googlemail\.com|postmaster@ocps\.net)$` | Gmail 467 delivery failure; 694 undeliverable | `AUTOMATED_SENDER_RE`: actual transport sender. Subject alone is insufficient: 468–475 are faculty responses under DSN; 695–696 are human replies under Undeliverable. |
| `^(support@schoolpay\.com|quickbooks@notification\.intuit\.com|no-reply@zoom\.us)$` | 793–795/800 SchoolPay E-Receipt; 553 Anten Graphics invoice; 605 webinar reminder | Automated receipt/notification sender, not a human reply with an invoice or reminder subject. |
| `^(Accepted|Declined|Invitation):` or `^Invitation from an unknown sender:` after prefix normalization | Gmail 32 is a Google Ads calendar invitation/internal forward | Require calendar MIME/transport or recognizable calendar body; do not skip a human school Meet the Teacher invitation. Accepted/Declined forms were required by task but not located as separate Gmail pairs. |
| Internal sender/recipient allowlist: `grouptrellis@gmail.com`, `cberrio04@gmail.com`, owned DR/OEV inboxes | 806–807 payment-system forward/internal edit request; 810–811 venue tests; 90 internal reply to school forward | Apply to real internal routing, not an owned inbox merely appearing in a signature or quoted To line. Pair file lacks full recipient headers, so code must use actual envelope/recipient metadata. |
| Vendor/business scope: `@callplaybook.com`, `@sra-insurance.com`, `info@fdean.com`, `fizanoornaqvi@gmail.com`, `hazel@proactivedash.com`, `hit-reply@dotloop.com` | Sponsorship 655–656; insurance 791–792/808–809/819–826/831; OEV sales pitch 45–53; unrelated pitch 600/property agreement 601 | Skip from customer bot; these are business operations/vendor traffic, not all automated senders. Avoid “insurance”, “W9”, “vendor” or “agreement” as broad subject skips: schools legitimately request them. |
| `Missing Days`, `Availability - DR`, `Payrolls`, `Direct Deposit Auth`, `Time off Requests`, employment/application/interview category | Coach indices listed above, plus contextual availability 184 | DR known-coach filter + contextual fallback. W9 alone does not distinguish faculty from staff. No coach personal email allowlist is hardcoded into prompts. |
| Pure closing / no actionable content after signature stripping; Gmail reaction MIME metadata; opt-out / emoji-only | Gmail 18/20/25/38/84 closings; retained GHL reactions/STOP patterns | Use full latest content and unresolved request context. “Thank you” substring is insufficient. Gmail reactions are a required rule but no dedicated reaction-format Gmail pair was located. |
| `system@ecemail.samaritan.com` | 788 Wedgefield partner message; 832 volunteer lunch | **Do not automatically add to AUTOMATED_SENDER_RE.** Bulk school system can carry real school outreach. These records are marked uncertain; inspect content/recipient. |

Suggested `SKIP_CATEGORIES`: automated_notification, delivery_failure, automated_calendar, reaction, opt_out, closing_no_request, internal_team, vendor_pitch_or_operations, test, dr_coach_staff. Use these in routing/logs, not as new model JSON fields. Only install deterministic rules after guarding the observed false positives above.

## Code dependencies and open decisions

1. Supply QUOTED_CONTEXT to both Gmail bots for the described one-message reply case; preserve provenance as prior outbound, not instructions. Actual runtime construction was not available to test.
2. Optional future school context must verify roster recipient and supply the actual permanent URL. The present warm roster draft is usable without it, but the reviewer still owns delivery. No false task creation or EOD SLA is implied.
3. Code/UI must display DR flag_human proposed drafts and retain current Gmail warning handling. Do not send or treat the warning text as a customer message automatically. Sub-0.75 drafts remain suppressed; no score manipulation was added.
4. Invoice preference is draftable; invoice creation/resend/discount execution requires the reviewer's action. Current URLs, expiration and ownership should be supplied in BOOKING_CONTEXT if the code wants reliable direct-link drafts.
5. Resolve the documented refund-policy, historical pricing/capacity and missing September/cancellation evidence questions with business owners before changing canonical policy. No new live facts are claimed here.
6. SQL uses only the requested five columns and brand IDs, one BEGIN/COMMIT, with each deactivation immediately preceding its insert. Re-running may hit a version uniqueness constraint; actual schema, concurrency and database execution were not tested. This is the requested activation script, not an idempotent migration.

## Validation

No documented repository test command or package.json was present. Local validation checks are recorded below after execution; this review does not claim live model evaluations or production readiness beyond the artifact checks.

Executed results:

- PASS: all 834 Gmail manifest records match the original eight source fields exactly; 789 non-coach Markdown inbound/reply pairs match source text, with dates/channel/role/lesson; 45 coach records remain indexed; all 28 uncertain classifications are marked.
- PASS: 492 original GHL records retained, all non-coach GHL message bodies present verbatim in their categories; merged category/channel sums equal DR 944 and OEV 382.
- PASS: static output-key sets, decision/threshold/human-review rules, exact DR registration states, coach routing, both Gmail QUOTED_CONTEXT descriptions and OEV Spanish rule checked. No old registration state in the six rewritten prompts.
- PASS: one SQL transaction; six correctly ordered UPDATE/INSERT pairs; exact IDs/channels/versions/five columns; each dollar-quoted payload matches its UTF-8 prompt file exactly, including newlines; no delimiter collisions.
- PASS: local calendar check confirms August 28, 2026 is Friday; historical Thursday wording was not promoted to canonical fact.

Not verified: actual LLM replies/scores/language quality/length compliance, production parser or UI behavior, live ACTIVE_PROGRAMS/venue data, permanent roster-link authorization, payment-link validity, attachments, database schema/constraints, successful activation, or the authorship/causal pairing of every historical reply. No deployment or sending occurred. Existing legacy builder/validation artifacts were retained; the checks above describe this run.

## Baseline — last 30 days to 2026-09-14 (before prompt rewrite)

Note: ACTIVE_PROGRAMS has been EMPTY in prod since ~Sep 3 (stale deployed function), so DR input tokens after Sep 3 are artificially low (~3k) and faculty flag_human is inflated. Real "before" for token cost = August (~19k/message with 55 teams).

## DR (hvgcxtawrditxvgvqfxb)

| src | audience/channel | decision | n | avg_in | avg_out | avg_score |
|---|---|---|---:|---:|---:|---:|
| gmail | - | error | 47 | | | |
| gmail | - | skip | 463 | 16632 | 88 | 0.99 |
| gmail | coach | draft | 1 | 19128 | 241 | 0.92 |
| gmail | coach | flag_human | 7 | 8930 | 326 | 0.65 |
| gmail | coach | skip | 6 | 10538 | 98 | 0.99 |
| gmail | faculty | draft | 22 | 16722 | 264 | 0.92 |
| gmail | faculty | flag_human | 56 | 13714 | 345 | 0.73 |
| gmail | faculty | skip | 68 | 11623 | 94 | 0.97 |
| gmail | other | skip | 21 | 16701 | 95 | 0.99 |
| gmail | parent | draft | 27 | 14899 | 310 | 0.93 |
| gmail | parent | flag_human | 35 | 10882 | 359 | 0.73 |
| gmail | parent | skip | 28 | 13218 | 89 | 0.98 |
| sms | email | draft | 8 | 9110 | 433 | 0.92 |
| sms | email | flag_human | 2 | 5212 | 355 | 0.69 |
| sms | sms | draft | 52 | 15754 | 296 | 0.93 |
| sms | sms | flag_human | 9 | 14269 | 263 | 0.57 |
| sms | sms | skip | 49 | 17165 | 139 | 0.22 |

Key ratios (gmail): faculty draft 22 / flag 56 / skip 68 → only 28% of actionable faculty mail gets a draft. Parent draft 27 / flag 35 → 44%. 463 unclassified skips cost ~7.7M input tokens in 30 days.

