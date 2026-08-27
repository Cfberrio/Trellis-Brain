---
title: DR Website Policies v1
brand: Discipline Rift
owner: Luis Torres
last_updated: 2026-07-21
status: draft — not publishable until Decision Register is cleared; counsel review required
sensitivity: internal
used_for_ai: true
source_reference: "website-structure.md (v2), 05-program-info-scope.md, pottershouse-facility-use-agreement.md, pottershouse-agreement-for-services-mou.md, Practice-Cancellation-Comms-SOP.md, Practice-Report-Schema.md, product-marketing-context.md"
---

# DR Website Policies v1

Five website documents for `disciplinerift.com`, plus a list of registration-flow documents that are missing and matter more than the website pages.

**Read this first.** DR is the highest-risk of the four brands, for three reasons that have nothing to do with website copy:

1. **DR serves minors.** There is no waiver, no assumption-of-risk language, no medical treatment authorization, and no photo release anywhere in the vault. Those are registration-flow documents, not website pages, and they are a bigger gap than any policy below. See Page 6.
2. **The published refund promise is unlimited.** "100% refund, any time during the season. No windows. No fine print." That is a real, uncapped financial exposure, and it contradicts both the alternate Fit Guarantee in `06-DNA/Offer.md` and what DR actually does in practice (partial, discretionary refunds).
3. **The franchise/license page makes franchise-adjacent representations** — "you would own a license," "DR covers 100% of the core costs," territory assignment and revocation — with no FDD referenced anywhere. That is a counsel question, not a copywriting question.

**Not legal advice.** Counsel review is required before any of this publishes.

**Publish at:** `/privacy` · `/terms` · `/refund-policy` · `/cookies` · plus on-form SMS copy at Registration Step 3. Spanish mirrors required at `/es/privacidad`, `/es/terminos`, `/es/politica-de-reembolso`, `/es/cookies`.

---

## DECISION REGISTER — clear these before publishing

### A. Hard blockers

| # | Decision | Why it blocks | Recommended default |
|---|---|---|---|
| A1 | **Entity: LLC or non-profit?** `product-marketing-context.md` says `Legal entity: Torres Rivero LLC`. Two signed school agreements say DR is "a non-profit youth sports organization registered through the School Board of Orange County." | These are mutually exclusive descriptions of the contracting party. Both are in writing, one of them to a school district. | Resolve with counsel before anything publishes. This is not a copy fix. |
| A2 | **Refund policy: 100% anytime, or bounded?** Three versions exist: (a) `/refund-policy` v2 — 100% any time, no windows; (b) `Offer.md` Option A — full credit if requested within 48h of practice #2; (c) actual practice — partial discretionary refunds ($90 on a $129 season). | You cannot publish (a) and operate (c). | §3.5 drafts **(a) as written**, because it is the canonical v2 spec and it is DR's differentiator. If Luis will not honor it literally, switch to (b) before launch — not after. |
| A3 | **Participant waiver, medical authorization, and photo release** | None exist. DR supervises 6–12 year olds in physical activity on school campuses. | Draft with counsel. See Page 6. |
| A4 | **Ages served: 6–12 or K–5th?** Live site says 5–11 (stale). School agreements say K–5th. Canon says 6–12. One parent thread mentions boys around age 14. | Age range drives the COPPA analysis and the waiver. | Publish **6–12**, per `Constraints.md:21` and the "finalized" note. Fix the live FAQ. |
| A5 | **Governing law / venue for parents** | The only governing-law clause in the repo is in a school MOU (Florida, Orange County). Nothing parent-facing. | Florida; Orange County. Decide separately whether to mirror the MOU's arbitration clause for parents — arbitration clauses against consumers on behalf of minors need counsel. |
| A6 | **Franchise/DRF representations** | "Own a license," "$0 cost," stipend, territory assignment and loss — no FDD, no state franchise registration, nothing. | **Escalate to counsel before the DRF landing page runs paid traffic.** Do not draft franchise terms in-house. |

### B. Contradictions to reconcile

| # | Conflict | Note |
|---|---|---|
| B1 | Price **$129** (canon, contracts, site) vs **$149** ("$149 season / $129 in some schools") | Policies don't publish a price — checkout is price of record — but the season fee appears in the refund policy context. Resolve it. |
| B2 | Sports: **3 live** (volleyball, tennis, pickleball) vs **4** (adds flag football, which has its own page) | Cosmetic for policies, real for the site. |
| B3 | **"No DR communication currently uses SMS as a primary channel… not for marketing or sequence nurture"** (`communication-rules.md:650`) vs live GHL SMS marketing automations, popup SMS sequences, registration-abandonment SMS, and a mass-SMS SOP | The rule is dead on arrival. Rewrite it. The policies below are written for the system that exists. |
| B4 | **Photo/media permission field existed in v1 registration, removed in v2** — while coaches actively upload photos and video per athlete and the Safety page promises "we post real practices, drills, and moments" | Put the field back. §1.7 and Page 6 address it. |
| B5 | **First-Practice Pass / trial**: v2 says "No trial. There is no First-Practice Pass anywhere in the tree." `Money-Model.md` still specifies it as the entry offer | Policies assume no trial. |
| B6 | **DR Home Club monthly, "cancel anytime"** is listed as a live dashboard product while `Constraints.md:35` says "Continuity offers are not yet finalized as active products" | §3.7 drafts subscription terms. If Home Club isn't live, delete that section rather than publish terms for a product that doesn't exist. |

### C. Not found

EIN, formation state, registered agent, 501(c) determination · deposits and payment-plan split terms · late fee / failed payment / chargeback policy · data retention and deletion process · accessibility statement content (page is routed, never written) · A2P 10DLC registration status · cookie/pixel inventory (Meta Pixel is implied by the ads domain but never documented).

### D. Compliance flags

- **D1 — Backend security gaps recorded in `DR-Backend-Migration.md`:** "RLS off en ~20 tablas PII" and public `resume` / `attachements` buckets. **A privacy policy that promises reasonable safeguards while row-level security is off on twenty tables of PII — including children's data — is a liability, not a protection.** Fix the backend before publishing §1.10.
- **D2 — COPPA.** Every documented flow has the parent as account holder and payer; children are entered as data by the parent. That is the right structure and keeps DR out of direct COPPA collection. **Do not add a child login, child-facing app, or child-submitted content without a COPPA review.**
- **D3 — Injury records.** `Practice-Report-Schema.md` collects injury severity, return-to-play status, and photos. Access rules exist internally. The privacy policy must disclose this collection to parents — §1.4 does.
- **D4 — Level 2 background screening** is documented for coaches under Fla. Stat. §§1012.465, 1012.467, 1012.468. This is a trust asset. §2.7 states it publicly.

---

# PAGE 1 — PRIVACY POLICY
**Publish at:** `/privacy` · ES at `/es/privacidad`

**Discipline Rift Privacy Policy**
Last updated: [PUBLICATION DATE]

## 1.1 Introduction

`[DECIDE A1 — ENTITY]`, operating as Discipline Rift ("Discipline Rift," "we," "us," or "our"), provides after-school youth sports programs in Central Florida. This policy explains how we handle information when you visit disciplinerift.com, register a child, use the parent dashboard, apply to coach, or communicate with us.

**This policy is written for parents and guardians.** Accounts are held by adults. Children do not create accounts, log in, or submit information to us directly.

## 1.2 Information we collect

**From the parent or guardian:**
- Your name, email address, mobile number, and account password
- Billing information, processed by our payment provider
- School, season, and program selections
- Your child's first name, grade, age, and experience level
- Emergency contact name and phone number
- Allergies or medical notes you choose to share
- Your communication and reminder preferences

**About the participant, generated during the program:**
- Attendance
- Skill progress and coach notes
- Injury or incident records, including what happened, severity, whether the participant was removed from practice, return-to-play status, and whether a parent was contacted
- Photos and video captured at practices `[see §1.7]`

**From coach applicants:**
- Contact details, résumé, work history, and background screening status

**Automatically from the website:**
- IP address, device and browser information, referring source, pages viewed, and language preference, through cookies and similar technologies. See our Cookie Policy.

**We do not store payment card numbers.** Payments and any saved card are handled by our payment provider through tokenization. We never see or store your full card number.

## 1.3 How we use information

- To register your child, take payment, and manage your season
- To build rosters, assign coaches, and run practices
- To contact you about schedule changes, cancellations, and make-up dates
- To send weekly progress updates and reminders you have opted into
- To respond in an emergency and contact you about an injury
- To send re-enrollment reminders for the next season, where you have opted in
- To improve our programs and train our coaches
- To meet legal, insurance, and school-district requirements

## 1.4 Injury and health information

If your child is injured during a practice, our coaches record what happened, the severity, whether your child was removed from practice, and return-to-play status, and we contact you. These records are treated as sensitive. Access is restricted to the participant's parent or guardian, the assigned coach and administrators, and school medical staff where return-to-play requires it. **Photos of injuries are never shared in any public-facing channel.**

## 1.5 Emergencies

In an emergency, our coaches follow the host school's on-site emergency procedures, contact emergency services as appropriate, notify you, and notify the school's designated contact.

## 1.6 Text messages (SMS)

If you provide a mobile number and opt in, you agree to receive SMS from Discipline Rift about your child's season — schedule changes, same-day cancellations, location changes, and reminders — and, where you separately opt in, weekly progress updates, re-enrollment reminders, and promotions.

Message frequency varies. Message and data rates may apply. Reply **STOP** to opt out, **HELP** for help, or contact info@disciplinerift.com or (407) 614-7454. Consent is not a condition of registration.

**We do not sell or share your mobile number or SMS consent with third parties for their own marketing.**

## 1.7 Photos and video

Coaches may capture photos and short video at practices to document sessions, support coaching feedback, and show our programs publicly.

**We ask for your permission at registration and you can change it at any time in your dashboard.** If you decline, we will not publish images in which your child is identifiable. `[DECIDE B4 — the permission field must be restored to the registration flow; it was removed in v2 while media capture continued]`

## 1.8 Who we share information with

Service providers who operate our systems under contract, and only for that purpose:

| Provider | Purpose |
|---|---|
| Supabase | Data storage, authentication, media storage |
| Twilio | SMS delivery |
| GoHighLevel | CRM, email and SMS sequences |
| Payment provider | Payment processing and saved-card tokenization |
| Email delivery provider | Transactional and program emails |
| Website and dashboard hosting | Running our sites |

We also share limited information with **host schools and facilities** where required for campus access, rosters, check-in and check-out, and emergency procedures.

**We do not sell your personal information, and we do not share children's information for advertising.**

## 1.9 Retention

We keep registration, attendance, payment, and communication records for as long as needed to run our programs, meet insurance, tax, and school-district requirements, and resolve disputes. Injury records are retained longer where required. You may request deletion under §1.11; some records must be retained by law.

## 1.10 Security

We use administrative, technical, and physical safeguards to protect information, including restricted access to injury records and private storage for uploaded files. No system is completely secure.

`[BLOCKER D1 — do not publish this section while row-level security is off on PII tables and file buckets are public. Fix the backend first.]`

## 1.11 Your rights and choices

You may:
- Access or correct your account and your child's information in the parent dashboard
- Change communication and photo permissions at any time
- Request deletion of your account and your child's records
- Opt out of marketing email and SMS at any time

Email info@disciplinerift.com. Florida residents may have additional rights under the Florida Digital Bill of Rights.

## 1.12 Children's privacy

Discipline Rift's website and registration are for adults. **Children do not create accounts and do not submit information to us directly.** Information about a participant is provided by their parent or guardian. If you believe a child has provided us information directly, contact us and we will delete it.

## 1.13 Contact

Discipline Rift
713 W Yale St, Orlando, FL 32804
(407) 614-7454 · info@disciplinerift.com · disciplinerift.com

## 1.14 Updates

We may update this policy. Changes take effect when posted.

---

# PAGE 2 — TERMS OF USE
**Publish at:** `/terms` · ES at `/es/terminos`

**Discipline Rift Terms of Use**
Last updated: [PUBLICATION DATE]

## 2.1 Acceptance

By using disciplinerift.com, creating a parent account, or registering a child, you agree to these Terms, our Refund Policy, and our Privacy Policy. You confirm you are the parent or legal guardian of the child you are registering, or are authorized to register them.

## 2.2 Our programs

Discipline Rift runs after-school youth sports seasons on school campuses in Central Florida. A season is **six consecutive weeks**, one session per week, one hour per session, beginning after student dismissal. Seasons are designed to fit within the school calendar. Equipment is included.

Programs serve ages **6–12** `[DECIDE A4]`. Some programs run for specific grade bands. Sessions typically run with a coach-to-participant ratio of approximately 1:10.

## 2.3 Registration and your account

You create a parent account and register your child through our registration flow. You are responsible for the accuracy of the information you provide — particularly your child's grade, allergies or medical notes, and emergency contact — and for keeping it current.

You are responsible for activity under your account and for keeping your password secure.

## 2.4 Payment

- The season fee is the amount shown at checkout. **Checkout is the price of record.**
- Discount codes, including the sibling discount, apply as shown at checkout.
- **Saving your card is optional.** If you save a card, it is stored to make re-enrollment one tap. **We do not auto-charge you. You approve every season.** You can remove your card at any time in your dashboard.
- Where a payment plan is offered, the season fee is split across scheduled payments with no additional fee. `[DECIDE — split terms are undefined in canon]`

## 2.5 Enrollment minimums and program changes

A session may be cancelled if registrations fall below the minimum required to run it. Where that happens, we notify you no later than **two weeks before the session start date** and refund you in full.

We may adjust practice times, locations, or coaches based on school access, weather, or staffing. We will tell you as soon as we know.

## 2.6 Missed practices, cancellations, and make-ups

- **If your child misses a practice**, they pick up at the next one. Our coaches structure seasons so participants can catch up. We do not refund or credit individual missed practices.
- **If we cancel a practice** — weather, facility issue, coach emergency, or anything that makes the session unsafe or impossible — **we make it up by extending the season by one week.** We notify you as early as we can.

## 2.7 Supervision, safety, and dismissal

- Our coaches meet participants at the designated spot at dismissal and supervise them for the full session.
- Check-in and check-out are recorded. **Participants are released only to authorized parties or to coordinated aftercare.** Keep your authorized pickup list current in your dashboard.
- **All coaches and staff working with students complete Level 2 background screening through OCPS** in compliance with Florida Statutes §§1012.465, 1012.467, and 1012.468, and wear visible badges on campus.
- Discipline Rift carries general liability insurance.

## 2.8 Assumption of risk

Youth sports involve physical activity and a risk of injury. By registering, you acknowledge that risk on behalf of your child.

`[DECIDE A3 — this sentence is a placeholder, not a waiver. A standalone participant waiver, assumption of risk, and release drafted by counsel and signed at registration is required. See Page 6.]`

## 2.9 Code of conduct

We expect participants, parents, and spectators to treat coaches, staff, school personnel, and other families with respect. We may remove a participant from a program for conduct that endangers others or repeatedly disrupts sessions. Where we remove a participant for conduct, refunds are at our discretion.

## 2.10 What we promise, and what we do not

Discipline Rift teaches sport skills, character, teamwork, communication, and leadership, and works to build a genuine passion for the game.

**We do not promise athletic outcomes, team placement, college recruitment, or scholarships**, and we do not operate a college recruiting or placement service. Any program that promises a "scholarship pipeline" without checkable results is selling hope — we do not sell that.

## 2.11 SMS terms

If you opt in, you agree to receive SMS from Discipline Rift about your child's season and, where separately consented to, progress updates, re-enrollment reminders, and promotions. Message frequency varies. Message and data rates may apply. Reply STOP to cancel, HELP for help. Carriers are not liable for delayed or undelivered messages.

## 2.12 Intellectual property

Website content, curriculum, drills, playbooks, branding, and materials are owned by or licensed to us. Materials provided to you for home use are for your family's personal, non-commercial use only and may not be redistributed.

## 2.13 Disclaimer

The website and dashboard are provided "as is" and "as available" to the fullest extent permitted by law.

## 2.14 Limitation of liability

To the fullest extent permitted by law, our total liability arising from your registration will not exceed the amount you paid for the applicable season, and we will not be liable for indirect, incidental, special, or consequential damages. **Nothing in these Terms limits liability that cannot be limited under Florida law, including liability for personal injury caused by our negligence to the extent Florida law does not permit that limitation.**

`[Counsel: Florida law constrains pre-injury releases signed by parents on behalf of minors. This section and §2.8 must be drafted together.]`

## 2.15 Indemnification

You agree to indemnify and hold harmless Discipline Rift from claims arising from your breach of these Terms, inaccurate information you provided, or conduct by you or your child that violates §2.9.

## 2.16 Force majeure

Neither party is liable for failure to perform due to causes beyond reasonable control, including severe weather, hurricane, tornado, flood, fire, act of God, school or facility closure, epidemic, pandemic, or government order. Where a season is disrupted, §2.6 and §3.6 apply.

## 2.17 Changes

We may update these Terms. Material changes apply going forward and do not change a season already paid for unless you agree.

## 2.18 Governing law

Governed by the laws of the State of Florida. Venue for disputes is Orange County, Florida. `[DECIDE A5]`

## 2.19 Contact

info@disciplinerift.com · (407) 614-7454

---

# PAGE 3 — REGISTRATION, CANCELLATION & REFUND POLICY
**Publish at:** `/refund-policy` · ES at `/es/politica-de-reembolso`

## 3.1 The Value Guarantee

> **100% refund, any time.**
>
> Discipline Rift's value is the teaching. We actually teach sports after school — breaking down skills and building skill, character, teamwork, communication, and leadership, and helping your child develop a real passion for the game.
>
> **If we don't deliver that value, you get a 100% refund, any time during the season. No windows. No fine print.**
>
> And no transportation needed — everything is handled by our coaches from the moment of dismissal, on campus, right after school.

> ⚠️ **`[DECIDE A2]` — this is the single most consequential open decision in this file.** As written, this is an unlimited, uncapped, season-long refund right with no conditions. `Offer.md` proposes a bounded alternative (full credit toward another season if requested within 48 hours of practice #2, chosen specifically because it is "conditional (limits abuse), credit (protects cash), time-bound (prevents end-of-season refunds)"). Real refunds issued to date have been partial and discretionary.
>
> Publish the version DR will actually honor. Publishing the unlimited version and then negotiating partial refunds is worse than publishing a bounded guarantee — it creates a written promise DR is on record breaking.

## 3.2 How to request a refund

Email info@disciplinerift.com or call (407) 614-7454 with your child's name, school, and season. Refunds are issued to the original payment method. Allow `[DECIDE — e.g. 5–10 business days]` for the refund to appear.

## 3.3 What a season includes

Six consecutive weekly sessions, one hour each, after dismissal, with equipment included, at your child's school.

## 3.4 Missed practices

Missed practices are not refunded or credited individually. Coaches re-anchor each skill so participants can catch up. See §2.6.

## 3.5 Cancellations by you

Under the Value Guarantee in §3.1, you may request a full refund at any time during the season. Once the season has ended, the guarantee no longer applies.

`[If DR adopts the bounded alternative instead, replace this section with: "You may request a full credit toward another sport or the next season by emailing us within 48 hours after your child's second practice."]`

## 3.6 Cancellations by us

- **Below minimum enrollment:** if a session does not reach the minimum number of registrations, we cancel and refund in full, with notice no later than two weeks before the session start date.
- **Cancelled individual practices:** made up by extending the season by one week. No refund is due for a made-up practice.
- **Season cancelled after it starts:** you receive a pro-rated refund for the sessions not delivered, or a full credit toward the next season, your choice.

## 3.7 DR Home Club (monthly membership) `[DECIDE B6 — delete this section if Home Club is not live]`

- Billed monthly to your saved payment method.
- **Cancel anytime** from your dashboard. Cancellation takes effect at the end of the current billing month.
- We do not pro-rate partial months. You keep access through the end of the month you paid for.
- Digital materials are for your family's personal use and are not refundable once accessed, except under the Value Guarantee.

## 3.8 Re-enrollment

Seasons do not auto-renew. **If you saved a card, it is stored only to make re-enrollment one tap — we never charge it without your approval.** Remove it any time in your dashboard.

## 3.9 Transfers

Ask us. Moving your registration to a different sport, school, or season may be possible where space allows.

## 3.10 Chargebacks

Contact us first — the Value Guarantee means you should never need a chargeback. Filing one without contacting us may result in loss of future registration privileges, to the extent permitted by law.

---

# PAGE 4 — COOKIE POLICY
**Publish at:** `/cookies` · ES at `/es/cookies`

**Discipline Rift Cookie Policy**
Last updated: [PUBLICATION DATE]

## 4.1 What cookies are

Small text files stored on your device when you visit our site. They keep the site working, remember your choices, and help us understand how the site is used.

## 4.2 Cookies we use

| Type | Purpose |
|---|---|
| Strictly necessary | Login, registration flow, checkout, security |
| Functional | Remembering your language choice (English/Spanish) and registration progress through checkout |
| Analytics | Understanding how families find and use the site |
| Marketing | Advertising and remarketing, where active |

`[DECIDE — audit and list actual tools. Meta advertising is run for DR, so a Meta Pixel is likely present and must be disclosed. No inventory exists in the vault.]`

## 4.3 Managing cookies

Manage cookies through your browser settings and any preference tool on our site. Blocking some cookies will break registration and login.

## 4.4 Updates

We may update this policy. Changes take effect when posted.

---

# PAGE 5 — SMS CONSENT NOTICE
**Place at Registration Step 3 (Parent Account), next to the mobile number field**

The current consent line — `Text and email me season updates and my child's weekly progress.` — is a single combined checkbox with no opt-out keywords, no frequency disclosure, and no rate disclosure. Replace it with two separate, **unchecked** checkboxes.

**Checkbox 1 — program and safety messages:**

> By checking this box, you agree to receive SMS messages from Discipline Rift about your child's season, including schedule changes, same-day cancellations, location changes, and practice reminders. Message frequency varies. Message and data rates may apply. Reply STOP to opt out and HELP for help. Consent is not a condition of registration. See our [Privacy Policy](/privacy) and [Terms of Use](/terms).

**Checkbox 2 — progress updates and program news (optional):**

> By checking this box, you agree to receive SMS messages from Discipline Rift with your child's weekly progress updates, re-enrollment reminders, and program news. Message frequency varies. Message and data rates may apply. Reply STOP to opt out and HELP for help. Consent is not a condition of registration. See our [Privacy Policy](/privacy) and [Terms of Use](/terms).

**Note on re-enrollment nudges.** The retention sequence sends SMS at the start of the final two weeks, on the last practice day, and 10 days post-season. Those are marketing messages and belong under Checkbox 2. So do the popup SMS sequence and registration-abandonment SMS.

**Spanish versions required** — the registration flow is fully mirrored in Spanish and consent must be captured in the language the parent is using.

**HELP auto-reply:**
> Discipline Rift: for help call (407) 614-7454 or email info@disciplinerift.com. Msg & data rates may apply. Reply STOP to unsubscribe.

**STOP auto-reply:**
> You are unsubscribed from Discipline Rift messages. No further messages will be sent. Reply HELP for help.

---

# PAGE 6 — MISSING REGISTRATION DOCUMENTS
**Not website pages. These are the bigger gap.**

Website policies govern the site. These govern what happens when a 7-year-old is on a field with a DR coach. **None of them exist in any form.**

| Document | Where it goes | Why it matters |
|---|---|---|
| **Participant waiver, assumption of risk, and release** | Signed by parent/guardian at registration, before Step 5 Payment | The only current risk language is one placeholder sentence in §2.8. Florida constrains pre-injury releases signed on behalf of minors — this must be drafted by counsel, not adapted from a template. |
| **Medical treatment and emergency authorization** | Registration | Coaches already follow school emergency procedures and record injuries. There is no authorization on file permitting emergency treatment or naming who may consent. |
| **Photo and media release** | Registration, with a dashboard toggle | Media is captured per athlete today and the Safety page promises public posting. The v1 permission field was removed in v2. Restore it. |
| **Authorized pickup list and release-to-third-party consent** | Registration, editable in dashboard | Check-out policy says participants are released "only to authorized parties." There is no documented mechanism for the parent to name them. |
| **Coach agreement and background-check consent** | Coach application | Level 2 screening is documented; the applicant's consent to it is not. |
| **DRF license / franchise disclosure package** | Before any DRF applicant signs or pays anything | `[DECIDE A6]` — counsel, not marketing. |

---

## IMPLEMENTATION CHECKLIST

- [ ] **Resolve A1 (LLC vs non-profit) with counsel** — two contradictory descriptions are already in writing, one to a school district
- [ ] **Decide A2 (Value Guarantee) and publish only what DR will honor**
- [ ] **Commission A3 registration documents with counsel** — waiver, medical authorization, photo release
- [ ] **Escalate A6 (DRF franchise representations) to counsel before running paid traffic to that page**
- [ ] Fix the backend before publishing §1.10: enable RLS on PII tables, make `resume` and `attachements` buckets private with signed URLs
- [ ] Restore the photo/media permission field to the registration flow
- [ ] Replace the single combined SMS consent line with two unchecked checkboxes, English and Spanish
- [ ] Rewrite `communication-rules.md:650` — the "no SMS" rule contradicts every live automation
- [ ] Confirm A2P 10DLC campaign registration with Twilio
- [ ] Update the live FAQ from ages 5–11 to 6–12
- [ ] Resolve the $129 / $149 price inconsistency
- [ ] Audit for Meta Pixel and analytics; complete §4.2
- [ ] Write the accessibility statement — the page is routed and empty
- [ ] Publish Spanish mirrors of all four policy pages
- [ ] Have counsel review §2.8, §2.14, §2.18, and Page 6 in full
