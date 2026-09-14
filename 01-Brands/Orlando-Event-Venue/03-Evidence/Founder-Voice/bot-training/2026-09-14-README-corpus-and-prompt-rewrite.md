---
brand: Orlando-Event-Venue
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
  - "[[01-Brands/Orlando-Event-Venue/03-Evidence/Founder-Voice/bot-training/2026-09-14-PROMPTS-active]]"
---

# OEV — bot prompt rewrite 2026-09-14: corpus, decisions, validation

> [!info] Status
> Prompts **drafted, not activated**. `brand_prompts` in production still runs the previous versions. Activation waits for Luis's review (ClickUp 86e38pqmw). Raw verbatim corpus (client PII) lives in the Trellis repo at `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/` (git-ignored), never in this vault. Prompt files + SQL: `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/`.

## Parent
- [[01-Brands/Orlando-Event-Venue/03-Evidence/Founder-Voice/bot-training/2026-09-14-PROMPTS-active|OEV proposed prompts]]

## Inventory and method

**DR 200 → 944; OEV 292 → 382; combined 492 → 1,326 exchanges.** Gmail additions: info@disciplinerift.com 695, disciplinerift@gmail.com 49, orlandoeventvenue@gmail.com 90. The `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/README.md` (corpus README) contains the full before/after category × channel table; `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/counts.json` (counts.json) preserves the baseline and merged counts. Inbound channel determines the table column; mixed reply channels remain separately recorded.

GHL bodies/JSON evidence were retained. Gmail bodies are reproduced verbatim, with 45 coach exchanges indexed in the brief coach file rather than copied into parent/faculty voice training. The `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/gmail-classification.jsonl` (Gmail classification manifest) preserves every source field and adds category, role, source index, lesson and uncertainty. There are 28 explicitly uncertain records; uncertain, coach, vendor, internal, test and automated records are not approved voice examples. Some supplied Gmail records contain HTML/residual quoted messages or internal replies; no re-extraction or cleanup was attempted. Operator authorship is supplied/inferred, not independently established as Luis for each record. Legacy GHL assignments and imperfect temporal pairings are preserved, not certified.

## Per-prompt diff summary

| Output | Retained | Changed |
|---|---|---|
| `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/oev_sms_v3.txt` | Canonical rates, venue facts, booking/availability logic, empty escalation draft convention, JSON keys | First-step skips; Spanish replies to Spanish inbound; ~400-character ceiling; current-customer Stripe link rules; missing discount email handling; hours + invoice preference exception; conflicting quote escalation; no “wide open” claim outside calendar window. |
| `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/oev_email_v3.txt` | Canonical pricing, venue facts, package scope, subject/sign-off, JSON keys, empty escalation draft convention | Same OEV skip/language/invoice/price-conflict rules; ≤~150 words; narrow two-question exception for hours and invoice preference; out-of-window availability uncertainty. |
| `domains/ops/ghl/sms-draft/prompts/v4-2026-09-14/oev_gmail_v3.txt` | Live pricing precedence and missing-pricing failsafe, contact-form handling, audience enum, empty subject, HUMAN REVIEW prefix/sign-off | QUOTED_CONTEXT + full named input contract; protected human replies under invoice subjects; first-step skips; Spanish; ≤~150 words; exact same-customer links; invoice preference exception; historical quote conflicts; reordered data descriptions to put BOOKING_CONTEXT before pricing. |

All six preserve human review/send and the 0.75 suppression threshold. No output keys or decision/audience enum values were added. The new prompts omit the obsolete registration status; historical current prompt files remain verbatim as inputs. OEV SMS/email keep their existing empty flag_human draft convention; DR SMS/email intentionally change it to a safe proposed reply for refunds, while both Gmail prompts keep their existing human-review banner.

## Evidence and decisions

### OEV pricing, invoices and language

- `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/oev/invoice-payment.md` (invoice-payment.md), Gmail 0 / `1a08c616637d7d9e`: $280 off for two free hours and an offered **$100 partner discount on both invoices**. This is negotiated approval, not a new public entitlement. Index 2 / `1a08441ce1ced11e` includes an exact Stripe URL after a split-payment request. Reuse the *pattern*, never this customer's historical link. Only a verified current link for the same invoice/customer may be included.
- `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/oev/booking-inquiry.md` (booking-inquiry.md), Gmail 3 / `1a081ae2ce1a7885`: “Can you pls specify the hours?” followed by “Would you like one invoice with the total amount or two split invoices?” This supports the narrow two-question exception. Invoice creation, changed terms and custom discounts still require a human.
- GHL conversation `HX4HzK0HVpjDp74JKB5i`, June 24, `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/oev/invoice-payment.md` (invoice-payment.md): parent/client never received the discount email; human gives **SAVE100** in the reply. Conversations `Aq7tTlVMkUm9rhf1RYNt` and `F1HTbdDhX9p5JWY3pO52` reinforce putting the code in the body.
- **Spanish is supported:** `domains/ops/ghl/sms-draft/data/raw/bot-training-corpus/oev/booking-inquiry.md` (booking-inquiry.md), GHL July 1, 2026, reply message `9WjbykVkNZwapsV2jq1D`: “Buenos dias! Si está disponible. A que hora lo necesitan?” April 9, message `BP8NaXDLp9skwyq5yFzI`: “Buenos dias! Saludos. Te parece a las 12pm Martes?” These are full Spanish replies in the candidate-human corpus, not merely an opener. Therefore all OEV rewrites answer Spanish in Spanish, otherwise English. No external authorship verification was performed.
- **Canonical pricing retained:** SMS/email $140/hour with a four-hour minimum, $899 daily, $199 cleaning, $99/hour weekday promo; Gmail uses VENUE_SERVICES_AND_PRICING and retains its missing-block failsafe. Gmail 82 shows $700 for 9pm–2am plus $199 cleaning; Gmail 84/88 show the canonical hourly/daily rates. No historical custom amount overrides current pricing.
- **Unresolved pricing conflicts:** GHL invoice-payment, conversation `g9yVjGtu22ntfTDO754T`, July 21, 2026: the reply beginning “Hey Chad! Welcome back” in that file: it states $149/hour × two four-hour blocks = $1,112, which is arithmetically wrong ($149 × 8 = $1,192; $278 is 25% of $1,112, not $1,192). Historical Gmail 29 quotes Basic $89/hour and Streaming $159/hour versus canonical $79/$149. Gmail 83 quotes old flat add-ons/tablecloth prices; Gmail 76 gives a custom $800 full-day offer and alcohol exception. None became canonical facts. Any conflict with a customer's actual quote flags for review.
- **Requested September rate discrepancy could not be confirmed as a rental rate:** the retained September 4 GHL exchange quotes LED $99/hour, and the permitted raw cache also has an outbound-only Basic $79/hour quote that day. The September Gmail partner-discount thread implies $140/hour through $280 for two hours, but does not state a conflicting base rate. The task's “/hour” reference does not include a numeric value. No alternative September rental rate was invented or silently chosen. The $149/hour Chad discrepancy above is a separate located conflict.
- Other historical inconsistencies: Gmail 54 says 2,000 sq ft vs canonical ~1,830; a GHL reply permits 100 guests vs canonical cap 90; Gmail 29 calls August 28, 2026 “Thursday” (it is Friday). Retain current canonical capacity/size and compute dates. Out-of-window calendar data cannot prove “wide open,” so that assertion was removed. Historical replies making holds, internal-meeting moves or alcohol exceptions are not bot permissions.

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

## OEV (vsvsgesgqjtwutadcshi)

| src | audience/channel | decision | n | avg_in | avg_out | avg_score |
|---|---|---|---:|---:|---:|---:|
| gmail | - | error | 5 | | | |
| gmail | - | skip | 77 | | | |
| gmail | customer | draft | 1 | 7477 | 385 | 0.87 |
| gmail | customer | flag_human | 5 | 8025 | 324 | 0.59 |
| gmail | customer | skip | 2 | 7672 | 90 | 0.95 |
| gmail | lead | draft | 2 | 7553 | 439 | 0.89 |
| gmail | lead | flag_human | 3 | 4161 | 324 | 0.57 |
| gmail | other | skip | 4 | 7053 | 85 | 1.00 |
| gmail | vendor | skip | 6 | 7758 | 79 | 0.98 |
| sms | email | draft | 5 | 8551 | 567 | 0.93 |
| sms | email | flag_human | 2 | 7287 | 459 | 0.58 |
| sms | email | processing (stuck) | 2 | | | |
| sms | email | skip | 1 | 5551 | 130 | 0.25 |
| sms | sms | draft | 11 | 6567 | 281 | 0.90 |
| sms | sms | flag_human | 9 | 6053 | 239 | 0.44 |
| sms | sms | processing (stuck) | 14 | | | |
| sms | sms | skip | 10 | 5109 | 111 | 0.13 |

Key: 16 OEV messages stuck in `processing` (code fix pending deploy). Gmail: only 3 drafts vs 8 flag_human on real leads/customers.
