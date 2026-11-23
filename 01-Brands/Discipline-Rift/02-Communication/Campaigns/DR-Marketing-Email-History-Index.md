---
brand: Discipline-Rift
area: communication
subarea: campaigns
note_type: index
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Búsqueda exhaustiva 2026-11-23: GHL API (export de mensajes email 2026-01-29→2026-11-22, 38,014 envíos), Gmail info@ vía Composio (2022-09→2026-11), ClickUp (carpeta DR > MARKETING EMAILS 901711199324 y más), vault + repos locales."
owner: Luis
last_updated: 2026-11-23
sensitivity: internal
hub_role: hub
audience: parent
channel: [email, sms]
up:
  - "[[01-Brands/Discipline-Rift/02-Communication/Communication-Home]]"
related:
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Marketing-Email-Language-Guide]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Campaigns/DR-App-Download-Campaign-2026-11]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-ghl-gmail]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-clickup]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-local]]"
---

# Historial de correos de marketing DR — índice

Todos los correos de marketing a padres que encontramos, con fecha y dónde está el texto literal.
**Cómo escribir uno nuevo:** [[01-Brands/Discipline-Rift/02-Communication/DR-Marketing-Email-Language-Guide]].

## Resumen

| Época | Herramienta | Cuántos | Texto literal en |
| --- | --- | --- | --- |
| 2022-09 → 2023-08 | Wix Shoutout | 13 (recuperados de respuestas de padres) | [[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-ghl-gmail]] §M1–M13 |
| 2024 → 2025 | Gmail info@ | ~20 (DRVC, updates semanales, promos) | [[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-ghl-gmail]] |
| 2026-02 → 2026-11 | GHL (luis@ → coachluis@ desde 31-jul) | 16 campañas (1,450–2,330 envíos c/u) + series de workflow | [[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-ghl-gmail]] §G1–G32 |
| 2026-02 → 2026-09 | ClickUp (drafts y finales) | ~7 correos + 2 docs "Editing Principles" de Luis | [[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-clickup]] |
| 2026-06 → 2026-11 | Repo DR / vault | 6 enviados + drafts + reglas | [[01-Brands/Discipline-Rift/03-Evidence/Marketing-Emails-Verbatim/Marketing-Emails-local]] |

## Dónde vive cada cosa (fuente original)

- **GHL:** campañas y workflows (Newsletter Lead ×3, Registration Abandoned ×3, Season Start, Weekly, Absence). Templates guardados (incl. "DR EMAILS", feb-2026) **no leídos**: la llave `GHL_PRIVATE_KEY_DR` no tiene scope de email builder (401).
- **ClickUp:** carpeta **DR › MARKETING EMAILS** (901711199324): doc "09.05" (8cqnrff-24277, Labor Day final + Winter draft + Principles Round Two) y "Editing Principles: Sept 5, 2026" (8cqnrff-24237). Doc LEAD MAGNET (8cqnrff-10997). INTERNS › COMMS (8cqnrff-11657, re-inscripción fin de temporada). Tarea [DR Marketing Emails](https://app.clickup.com/t/86dznpvkj) (Bekah, 6-feb-2026, PDF "Spring After School Starts Here"). BIZ DEV doc "DR" (8cqnrff-5297, Lead DNA / Conversion DNA, dic-2025).
- **Gmail info@:** copias recibidas de las campañas GHL + envíos directos 2024–2025.
- **Repo DR:** `disciplinerift/docs/emails/*.html` (campañas oct–nov enviadas desde el admin) y `supabase/functions/_shared/` (correos automáticos).
- **Wix:** correos 2022–2023 solo sobreviven citados en respuestas de padres.

## Huecos conocidos

- Templates guardados en GHL (falta scope o la llave `GHL_API_KEY`).
- HTML final de Luis del Back to School (11-ago) no archivado; hay versión del build.
- Emails v1 del popup de 18h y 40h: solo fragmentos.
- Doc ClickUp "EMAIL MKT" (8cqnrff-10857) tiene una contraseña en texto plano → mover a gestor y rotar.

---

## Inventario GHL + Gmail

### 1a. GHL (sent via GHL / Mailgun, from luis@ / coachluis@ / info@disciplinerift.com)

| # | Source | Name / subject | First sent | Last sent | Sends | Sender | Type |
|---|---|---|---|---|---|---|---|
| G1 | GHL campaign | No school tomorrow! Important information | 2026-02-15 | 2026-02-15 | 1768 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G2 | GHL campaign | After school time can be wasted... we fix that | 2026-02-20 | 2026-02-20 | 1699 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G3 | GHL workflow | Here you go! 3-minute Parent Guide | 2026-02-23 | 2026-11-22 | 520 | Discipline Rift <luis@disciplinerift.com> | Workflow: Newsletter Lead (email 1) |
| G4 | GHL workflow | Sports: This is where most parents hesitate | 2026-02-23 | 2026-10-23 | 206 | Discipline Rift <luis@disciplinerift.com> | Workflow: Newsletter Lead (email 2) |
| G5 | GHL workflow | Last chance to secure your child's spot this season | 2026-02-26 | 2026-10-23 | 189 | Discipline Rift <luis@disciplinerift.com> | Workflow: Newsletter Lead (email 3) |
| G6 | GHL campaign | Sports after Spring Break? One Week Away | 2026-03-15 | 2026-03-15 | 18 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G7 | GHL campaign | Stressed from Spring break? Time to take action | 2026-03-16 | 2026-03-16 | 1829 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G8 | GHL campaign | It's time. Last Season of the year | 2026-03-19 | 2026-03-19 | 1824 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G9 | GHL campaign | Ready for tomorrow? | 2026-03-22 | 2026-03-22 | 1826 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G10 | GHL workflow | Nos hemos dado cuenta de que te has perdido nuestras novedades | 2026-05-05 | 2026-05-05 | 3 | Discipline Rift <luis@disciplinerift.com> | Workflow: re-engagement (ES) |
| G11 | GHL workflow | Finish your registration | 2026-05-26 | 2026-06-19 | 110 | Discipline Rift <luis@disciplinerift.com> | Workflow: Registration Abandoned (1) |
| G12 | GHL workflow | Second Attempt | 2026-05-27 | 2026-06-20 | 109 | Discipline Rift <luis@disciplinerift.com> | Workflow: Registration Abandoned (2) |
| G13 | GHL workflow | Final Email | 2026-05-29 | 2026-06-22 | 108 | Discipline Rift <luis@disciplinerift.com> | Workflow: Registration Abandoned (3) |
| G14 | GHL campaign | Discipline Rift: Next Steps | 2026-07-31 | 2026-07-31 | 13 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G15 | GHL campaign | Back to school this Tuesday, are you ready? | 2026-08-09 | 2026-08-18 | 2236 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G16 | GHL campaign | First week is done. Is your child ready? | 2026-08-16 | 2026-08-18 | 2214 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G17 | GHL campaign | Long weekend! Volleyball starts this week | 2026-09-05 | 2026-09-05 | 2187 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G18 | GHL campaign | Happy Labor Day! Volleyball is here | 2026-09-07 | 2026-09-08 | 1974 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G19 | GHL campaign | Next sports season is here. [child] isn't registered yet | 2026-10-04 | 2026-10-05 | 1473 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G20 | GHL campaign | Good things come to an end! isn't registered for next season | 2026-10-11 | 2026-10-11 | 2331 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G21 | GHL campaign | season is coming to an end. | 2026-10-18 | 2026-10-18 | 2262 | Discipline Rift <info@disciplinerift.com> | Campaign |
| G22 | GHL campaign | practices begin this week at . There may still be room! | 2026-10-26 | 2026-10-26 | 1451 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G23 | GHL campaign | Practice is Happening as Scheduled | 2026-11-02 | 2026-11-02 | 20 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G24 | GHL workflow | 7-day: We're seven days away from VOLLEYBALL HILLCREST! | 2026-09-03 | 2026-10-23 | 355 | Discipline Rift <info@disciplinerift.com> | Workflow: Season Start Reminder (7-day) |
| G25 | GHL workflow | 1-day: Volleyball is tomorrow! | 2026-09-07 | 2026-11-02 | 621 | Discipline Rift <info@disciplinerift.com> | Workflow: Season Start Reminder (1-day) |
| G26 | GHL workflow | [child]'s First Volleyball Practice Is Tomorrow | 2026-09-01 | 2026-11-02 | 547 | Discipline Rift <info@disciplinerift.com> | Workflow: Season Start Reminder (first practice) |
| G27 | GHL workflow | Tomorrow, We Start Seeing Volleyball Differently | 2026-09-01 | 2026-10-27 | 358 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder (wk1) |
| G28 | GHL workflow | Volleyball Gets More Challenging Tomorrow | 2026-09-01 | 2026-11-10 | 549 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder |
| G29 | GHL workflow | Tomorrow, We're Building on What They Learned in Volleyball | 2026-09-01 | 2026-11-05 | 640 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder |
| G30 | GHL workflow | It's Time to Put Everything Together in Volleyball | 2026-09-01 | 2026-11-03 | 290 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder |
| G31 | GHL workflow | How Far They've Come in Volleyball. Final Practice Tomorrow | 2026-09-01 | 2026-11-10 | 356 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder (final) |
| G32 | GHL workflow | A note about [child]'s session | 2026-09-01 | 2026-11-20 | 411 | Discipline Rift <info@disciplinerift.com> | Workflow: Parent Absence |

Excluded from GHL (operational, not marketing): coach/parent new-message notifications, "Still waiting: unread message", coach session-record reminders, receipts/invoices, staff campaigns to coaches (Meet the Families, Coaching Resources, DR Team Fall Schedule, Required: Review Annual Schedule, private-lesson availability), practice-canceled notices, test sends. Per-school duplicates of the season-start and weekly reminders (tennis/pickleball/soccer/flag football variants) exist with the same structure; only the volleyball version is reproduced.

### 1b. Gmail (info@disciplinerift.com)

| # | Source | Subject | Date | Sender | Type |
|---|---|---|---|---|---|
| M1 | Gmail | Re: Last 2 Week to Register - Sign up Today! | 2022-10-13 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M2 | Gmail | Re: Limited Time Christmas Offer - Sign up today! | 2022-12-20 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M3 | Gmail | Re: Registrations Now Open - Sign up today! | 2022-12-13 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M4 | Gmail | Re: Late Spring Registrations now open - Don't miss out!! | 2023-02-10 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M5 | Gmail | Re: Limited Time Offer Ends Today! - Sign Up Now! | 2023-01-02 | [parent reply quoting DR blast] | Wix Shoutout blast (recovered from reply quote) |
| M6 | Gmail | Re: Programs Start Next Week - Register Today! | 2023-01-11 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M7 | Gmail | Re: Last week To Sign Up - Don't Miss out! | 2023-01-10 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M8 | Gmail | Re: Limited Spots Available - Don't Miss Out! | 2022-10-26 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M9 | Gmail | Re: Late Fall Registrations - Sign up Today! | 2022-10-18 | [parent reply quoting DR blast] | Wix Shoutout blast (recovered from reply quote) |
| M10 | Gmail | Re: School Starts Tomorrow-Register Today!!! | 2023-08-09 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M11 | Gmail | Re: Tennis and Volleyball Camps Now Available!! - DR Sports & Athletics | 2023-04-13 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M12 | Gmail | Re: Season Update - DR Sports & Athletics | 2022-12-05 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M13 | Gmail | Re: Looking forward to seeing you at WINDERMERE ELEMENTARY VOLLEYBALL | 2022-09-01 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M14 | Gmail | Updated Schedule Late Spring Season - DR Sports & Athletics | 2023-04-13 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M15 | Gmail | Welcome to DRVC Pre-Season - Your Journey Begins Tomorrow! 10U LIME | 2024-03-11 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M16 | Gmail | Congratulations! Volleyball Club Team Placement | 2024-03-03 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M17 | Gmail | First Day of Volleyball - Week 1 with DR Sports & Athletics | 2025-04-10 | Discipline Rift <info@disciplinerift.com> | Weekly season update (2025) |
| M18 | Gmail | Volleyball Week 2 with DR Sports & Athletics | 2025-04-17 | Discipline Rift <info@disciplinerift.com> | Weekly season update (2025) |
| M19 | Gmail | Last Week of Volleyball with DR Sports & Athletics | 2025-05-07 | Discipline Rift <info@disciplinerift.com> | Weekly season update (2025) |
| M20 | Gmail | DRVC Volleyball Tryouts – This Saturday! | 2025-05-28 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M21 | Gmail | Tomorrow - Fall Season Discipline Rift | 2025-09-15 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M22 | Gmail | Practice is today! Orangewood Tennis | 2025-08-20 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M23 | Gmail | Reminder:  VOLLEYBALL INDEPENDENCE Starts tomorrow! | 2025-11-04 | info@disciplinerift.com | Season start reminder |
| M24 | Gmail | Reminder: VOLLEYBALL WATER SPRING Starts in 7 days! | 2026-01-19 | info@disciplinerift.com | Season start reminder |
| M25 | Gmail | DR Tennis Spring Season | 2025-11-11 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M26 | Gmail | Eagle Creek Afterschool Clubs Spring Semester | 2025-11-18 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M27 | Gmail | Prueba Newsletter | 2025-11-24 | DisciplineRift <info@disciplinerift.com> | Newsletter test send |
| M28 | Gmail | Prueba Newsletter 5 | 2025-11-24 | DisciplineRift <luis@disciplinerift.com> | Newsletter test send |
| M29 | Gmail | Their Health won’t wait for “Later” - Spring Season | 2025-12-06 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M30 | Gmail | Spring Volleyball - Discipline Rift | 2026-01-08 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M31 | Gmail | Spring Pickleball Season 🥒  Dates & Flyer | 2026-01-08 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M32 | Gmail | Registration | 2025-12-22 | info@disciplinerift.com | Promo / announcement |
| M33 | Gmail | No school tomorrow! Important information | 2026-02-15 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M34 | Gmail | After school time can be wasted... we fix that | 2026-02-20 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M35 | Gmail | 6255 New Independence Pkwy, Winter Garden, FL 34787 Season Ended Last Week – New Registration Now Open | 2026-03-03 | info@disciplinerift.com | Weekly season update (2025) |
| M36 | Gmail | Stressed from Spring break? Time to take action | 2026-03-16 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M37 | Gmail | Thank You for Coming Today | 2026-03-17 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M38 | Gmail | It's time. Last Season of the year | 2026-03-19 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M39 | Gmail | Ready for tomorrow? | 2026-03-22 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M40 | Gmail | THANK YOU from UCF Knight Shadow & Summer 2026 info! | 2026-03-26 | [parent reply quoting DR blast] | Promo / announcement |
| M41 | Gmail | Season Update? Prep for Fall | 2026-05-04 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M42 | Gmail | Preparing you for the DR Fall Season | 2026-07-28 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M43 | Gmail | Back to school this Tuesday, are you ready? | 2026-08-09 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M44 | Gmail | First week is done. Is your child ready? | 2026-08-16 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M45 | Gmail | Long weekend! Volleyball starts this week | 2026-09-05 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M46 | Gmail | Happy Labor Day! Volleyball is here | 2026-09-07 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M47 | Gmail | Volleyball Starts Thursday! | 2026-09-08 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M48 | Gmail | [child] is all set for Volleyball at Hamlin Elementary School - Fall 2026 schedule | 2026-09-16 | <info@disciplinerift.com> | Welcome / confirmation |
| M49 | Gmail | You're all set — [child]'s Fall 2026 Volleyball team is confirmed | 2026-09-21 | <info@disciplinerift.com> | Welcome / confirmation |
| M50 | Gmail | Next sports season is here. [child] isn't registered yet | 2026-10-04 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M51 | Gmail | Good things come to an end! isn't registered for next season | 2026-10-11 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M52 | Gmail | season is coming to an end. | 2026-10-18 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M53 | Gmail | Here you go! 3-minute Parent Guide | 2026-10-23 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M54 | Gmail | One week until VOLLEYBALL INNOVATION starts | 2026-10-23 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M55 | Gmail | Volleyball starts tomorrow | 2026-10-25 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M56 | Gmail | practices begin this week at . There may still be room! | 2026-10-26 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M57 | Gmail | Winter Flag Football at Pinecrest Avalon has spots open | 2026-10-26 | Discipline Rift <info@disciplinerift.com> | Promo / re-enroll |
| M58 | Gmail | Pinecrest Avalon Winter: Flag Football Mondays, Tennis Tuesdays | 2026-10-26 | <info@disciplinerift.com> | Promo / re-enroll |
| M59 | Gmail | Pinecrest Avalon Winter: Soccer starts Thursday | 2026-10-27 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M60 | Gmail | [child] is not registered for volleyball yet | 2026-10-30 | Discipline Rift <info@disciplinerift.com> | Promo / re-enroll |
| M61 | Gmail | Hope Prep Girls' 15U Volleyball / 2027 Season Dates | 2026-11-12 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M62 | Gmail | Summer Camp Schedule - July 20–24 | 2026-07-19 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M63 | Gmail | You're in! [child]'s Fall 2026 practice schedule | 2026-10-08 | <info@disciplinerift.com> | Welcome / confirmation |


## Inventario ClickUp

| # | Item | Location / URL | Author | Date | Type |
|---|---|---|---|---|---|
| A1 | Volleyball Season Launch — Email 1 "Long weekend" + Email 2 "Labor Day push" (Fall 2026) | DR > MARKETING EMAILS > doc "09.05" page "09.05" — https://app.clickup.com/9017418223/docs/8cqnrff-24277/8cqnrff-36577 | Luis Torres | 2026-09-05 (sends 9/5–9/7) | Finalized email (sent via GHL, Labor Day weekend) |
| A2 | Winter Volleyball Season — Email 1 "Registration is open" + Email 2 "Decision push" | same doc, page "09.26" — https://app.clickup.com/9017418223/docs/8cqnrff-24277/8cqnrff-37817 | Luis Torres | 2026-09-26 | Draft/template (send dates placeholders; sent status unknown) |
| R1 | "Editing Principles (Sept 5, 2026): What Luis Changes and Why" (8 principles) | DR > MARKETING EMAILS > doc 8cqnrff-24237 — https://app.clickup.com/9017418223/docs/8cqnrff-24237/8cqnrff-36517 | Luis Torres | 2026-09-05 | Guideline / Luis feedback (before→after edits) |
| R2 | "Editing Principles: Round Two — The Labor Day Edits" (principles 9–14 + checklist) | doc "09.05" page — https://app.clickup.com/9017418223/docs/8cqnrff-24277/8cqnrff-36597 | Luis Torres | 2026-09-05 | Guideline / Luis feedback |
| B0–B5 | Parent Guide lead-magnet: pop-up copy + nurture Email 1 (0h), Email 2 (18h), Email 3 (40h) + paired SMS; abandoned-registration placeholders | DR > DR folder > doc "LEAD MAGNET" 8cqnrff-10997 — https://app.clickup.com/9017418223/docs/8cqnrff-10997/8cqnrff-9797 | Cristian Berrío (pages) + Luis Torres (edited copy) | 2026-02-17 → edited 2026-02-23 | Template / automation (GHL "Newsletter Lead (3 correos)", live per COMMS DR map; stops on registration) |
| C1–C2 | End-of-Season "Season Ended Last Week – New Registration Now Open" (email + SMS), 2 versions | DR > INTERNS > doc "COMMS" 8cqnrff-11657 — https://app.clickup.com/9017418223/docs/8cqnrff-11657/8cqnrff-10997 | Luis Torres | 2026-03-03 / 2026-03-04 | Template (re-enroll; sent per site, Spring 2026 EOS mass send documented in PROCESSES > SMS video) |
| D1–D3 | "DR Marketing Emails" assignment + 2 Spring email drafts "Spring After School Starts Here" (CTA Reply SPRING) | DR > INTERNS > Bekah > task 86dznpvkj — https://app.clickup.com/t/86dznpvkj (attachment PDF) | Brief: Luis Torres; drafts: Bekah | brief 2026-02-06; PDF 2026-02-20 | Brief = guideline; PDF = intern draft (send unknown) |
| R3 | Nurture/welcome-series playbook (Email 0–6, cadence, 1 CTA per email) | BRANDS > BIZ DEV > doc "DR" 8cqnrff-5297 pages 5) Lead DNA, 6) Conversion DNA — https://app.clickup.com/9017418223/docs/8cqnrff-5297/8cqnrff-3757 | Luis Torres | 2025-12-22 / 2026-01-01 | Guideline (strategy) |
| R4 | Parent email voice brief (weekly emails) | task 86dzew0v1 — https://app.clickup.com/t/86dzew0v1 | Luis Torres | 2026-01-26 | Guideline (Luis). Attached PDFs (v1–v3, 2026-01-28 → 2026-02-02) are in-season practice reminders, not marketing; not transcribed |
| R5 | "Messages to Parents" rules (warmth first, never imply parent is late, merge-field caution) | DR > INTERNS > doc "PROCESSES" page — https://app.clickup.com/9017418223/docs/8cqnrff-11677/8cqnrff-38397 | Luis Torres | 2026-10-04 | Guideline (SMS-focused) |
| R6 | Misc Luis rules (refund promo only pre-registration; marketing only to non-registered; app-adoption D1/D3/D6/D9/D12 plan) | tasks 86e3zqk3t, chat DR \| Executives, SyncUp 10/29 doc 8cqnrff-26677 | Luis Torres | 2026-09-03 → 2026-11-09 | Guideline / feedback |
| — | GHL "EMAIL MKT" doc (SETUP = video summary of building HTML emails in GHL; SCREENSHOTS = SOP for grabbing frames from approved videos for email images) | GHL space doc 8cqnrff-10857 | Luis Torres | 2026-02-16 / 2026-06-07 | Process (no copy). NOTE: page contains a plaintext shared-account password — do not copy |
| — | COMMS DR "Mapa de comunicaciones actuales" (lists live marketing flows: Parent Guide, Newsletter Lead 3 emails at 0/18/40h, manual Campaigns) | doc 8cqnrff-27437 page 8cqnrff-40837 | Cristian Berrío | 2026-11-12 | Inventory/map (no copy) |

**Looked at and excluded as not outbound marketing** (operational/transactional): weekly practice reminders & 30/7/1-day season reminders (DISCIPLINERIFT.COM > NOTIFICATIONS pages), Weather / Season Cancellation templates (8cqnrff-27637, 8cqnrff-24957), Windermere date-change, Hope Prep start-date update, Village Park cancellation emails (DR | Executives chat), EOS Faculty email, TFA private-lesson booking texts, EMAIL AUTOMATION / REPLIELS bot reply examples (BOT DATA), outreach-to-schools docs (INTERNS > OUTREACH), ad/video scripts (DR Ads Campaigns, Volleyball Registration Campaign — Finalized Content, SCRIPTS REVISIONS, CONTENT INVENTORY), DR GUIDES (lead-magnet article content, ARCHIVES).

---


## Inventario local (repo + vault)

| # | File | What it is | Date | Status |
|---|---|---|---|---|
| 1 | `DISCIPLINERIFT/disciplinerift/supabase/functions/_shared/email-templates.ts` → `parentGuideHtml()` + `send-parent-guide/index.ts` | "Here you go! 3-minute Parent Guide": the lead-magnet email (newsletter/popup opt-in) | code last changed 2026-11-04; seen in info@ Sent 2026-06-25 | **LIVE-AUTO / SENT** |
| 2 | `Trellis-Brain/.../03-Evidence/Founder-Voice/email-sent-analysis-2026-06-30.md` §A1 | Same Parent Guide email as captured from the Sent folder; also has a faculty cold-outreach template | extracted 2026-06-30 | **SENT** (evidence) |
| 3 | git `a78b5c7:domains/content/discipline-rift/email-html/2026-08-back-to-school.html` | Back-to-school primary, GHL-ready HTML build (the "verified reference build") | 2026-08-10 | **SENT** (shipped subject 2026-08-11; Luis's ChatGPT HTML is the true ground truth and was never archived) |
| 4 | `Trellis-Brain/.../02-Communication/Campaigns/DR-First-Week-Of-School-Campaign-2026-08.md` (= git `campaigns/2026-08-first-week-of-school-email.md`) | First-week-of-school campaign: approved primary + Variants B/C + **Luis's 5 rules** | last_updated 2026-08-10 | Primary **APPROVED**; B/C **DRAFT** (pending Luis's read); §0 **RULE** |
| 5 | `Trellis-Brain/.../Campaigns/DR-Email-Rewrite-Retrospective-2026-08.md` | Analysis of Luis's rewrite: what he cut and added | 2026-08-10 | **RULE** |
| 6 | `Trellis-Brain/.../02-Communication/DR-Parent-Email-Template.md` | Binding house-list drafting contract (10 slots, 230-word cap) | 2026-08-10, assets resolved 2026-08-25 | **RULE** (canonical) |
| 7 | `Trellis-Brain/.../02-Communication/DR-Email-Design-Spec.md` §5.2, §5.9, §6, §9, §10, §10.1, §11 | Render contract + copy rules + pre-send checklist | 2026-08-25 | **RULE** |
| 8 | `DISCIPLINERIFT/disciplinerift/docs/emails/campaign-unregistered-attended-winter26-{andover,baldwin-park,hamlin}.html` + `ghl-unregistered-attended-winter26.html` | "X is not registered for volleyball yet" (attended practice without registering) | sent 2026-10-30 (3/3 via info@) | **SENT** |
| 9 | `.../docs/emails/campaign-winter-pinecrest-avalon-days.html` | Winter re-enroll: "Flag Football Mondays, Tennis Tuesdays" (correction + spots) | sent 2026-10-26 (22 recipients, dashboard) | **SENT** |
| 10 | `.../docs/emails/campaign-winter-pinecrest-avalon-soccer.html` | Winter re-enroll: "Soccer starts Thursday" | sent 2026-10-27 (22/22 via Composio Gmail) | **SENT** |
| 11 | `.../docs/emails/campaign-youre-in-{isai-deerwood,marcella-sunblaze}-oct8.html` | "You're in for Fall 2026" (mid-season add) | 2026-10-08 | **SENT** (transactional-ish) |
| 12 | `.../docs/emails/campaign-season-cancel-low-registration.html` | Season canceled due to low registration | 2026-10-26 | **SENT**, TRANSACTIONAL |
| 13 | `.../docs/emails/campaign-{storm,rainy,weather,makeup,practice-on,no-practice,delayed,correction,tournament,cancel-week}-*.html` (~25 files) + `faculty-*.html` | Operational one-off parent/faculty campaigns | 2026-09-30 → 2026-11-20 | **SENT**, TRANSACTIONAL (not transcribed; same shell/sign-off as #8–#10) |
| 14 | `email-templates.ts` → `waitlistInviteHtml()` + `waitlist-invite/index.ts` | "You're invited to register for {team}" | live since 2026-08-18 (manual invite) | **LIVE-AUTO** |
| 15 | `email-templates.ts` → `seasonReminderHtml()` / `seasonReminderSubject()` | 15/7/1-day season-start reminders | live 2026-09-01 | **LIVE-AUTO**, TRANSACTIONAL |
| 16 | `Trellis-Brain/.../ClickUp-Verbatim/WEEKLY-N8N/09…14-*.md` | Weekly practice-eve emails, Weeks 1–6 (Luis's own final draft 2026-08-31) | 2026-08-31 | TRANSACTIONAL (Luis-written) |
| 17 | `Trellis-Brain/.../Templates/Operational-Email-Library.md` + `ClickUp-Verbatim/03,04,05` | 15/7/1-day reminder copy rewrites (n8n era) | 2026-08-31 | TRANSACTIONAL (superseded in production by #15) |
| 18 | `Trellis-Brain/.../Sequences/DR-Lead-Magnet-Sequence.md` | 6-email lead-magnet sequence (guides + SIBLING code) | 2026-07-23 | **DRAFT** |
| 19 | `Trellis-Brain/.../Sequences/DR-Registration-Sequence.md` (Branch B R1–R3) | Cart-recovery emails/SMS | 2026-07-23 | **DRAFT** (a real GHL abandonment automation exists; its copy is not stored locally) |
| 20 | git `a78b5c7:.../popup-funnel-v2/03-lead-funnel.md` | Lead funnel v2: guide delivery + 10% code + SMS + 72h close | 2026-08-11 | **DRAFT** ("Draft v1 for review") |
| 21 | git `a78b5c7:.../popup-funnel-v2/03-sequence-a…, 04-sequence-b…, 05-abandoned-registration.md, 01-popup.md, 02-lead-magnet.md, 00-audit-live-v1.md` | 30-day nurture branches, abandoned-registration and popup specs; the audit describes the live v1 funnel | 2026-08-04 → 08-11 | **DRAFT** (00 = audit of live v1) |
| 22 | git `a78b5c7:.../dr-comms-rewrite-prompt.md`, `dr-marketing-context-from-qa.md`; git `69be6e6:.agents/product-marketing-context.md` | Language contract, banned words, claim rule, structural rules S1–S10 | 2026-07-09 → 08-11 | **RULE** (partly superseded by #4–#7) |
| 23 | `Trellis-Brain/.../02-Communication/Marketing-Language-Library.md` | Keyword buckets + excluded terms (ClickUp KEYWORDS - ADS / MARKETING) | 2026-05-21 | **RULE** |
| 24 | `Trellis-Brain/.../02-Communication/communication-rules.md` | Voice rules, subject-line rules, signature, "what DR is not" | authored 2026-04-21, verified 2026-08-27 | **RULE** (older; partly superseded) |
| 25 | `Trellis-Brain/.../00-Brand-Core/Voice-and-Tone.md` | Voice posture, avoid list, cultural refrains | 2026-09-17 | **RULE** |
| 26 | `Trellis-Brain/.../02-Communication/DR-Parent-Communication-Philosophy.md` | Luis's parent message, verbatim (2026-09-15/16 dictation) | 2026-09-17 | **RULE** |
| 27 | `Trellis-Brain/.../02-Communication/DR-Communication-Audit-2026-08-04.md` §6 | Canon conflicts (fun-first, pricing, trial, age, SMS, syntax) | 2026-08-04 | **RULE** (context) |
| 28 | `Trellis-Brain/02-Meetings/2026-10-29 SyncUp DR Executives (26677).md` | Luis: emails should read as written by the coach; app-adoption cadence D1/D3/D6 email, D9 SMS, D12 "last chance" | 2026-10-29 | **RULE** / decision |
| 29 | `DISCIPLINERIFT/disciplinerift/docs/proposals/2026-11-23-app-download-campaign.md` | Draft copy for the "Download the app" campaign (D1–D12) | 2026-11-23 | **DRAFT** (today; pending Luis) |
| 30 | `Trellis-Brain/.../00-Brand-Core/offers-evidencia.md` l.73 | Fragment from ClickUp "Volleyball Registration Campaign — Finalized Content": "It was only $129 for a six-week season…" | observed 2026-10-21 | fragment only (full page is in ClickUp, not local) |
| 31 | DR memory: `project-dr-winter26-sms-invite.md`, `project-dr-pinecrest-soccer-winter-send.md`, `project-dr-unreg-attended-winter26.md`, `project-dr-refund-promo-registered.md` | Send records + Fall→Winter SMS line | Oct–Nov 2026 | **SENT** (records) |
| 32 | `Trellis-Brain/.../03-Evidence/Founder-Voice/bot-training/01-PARENTS.md` | Luis's real 1:1 parent replies | 2026 | voice reference (not marketing) |
| 33 | `Trellis-Brain/.../02-Communication/fall-campaign-and-content-strategy-2026.md` | Fall angle: "Don't know what to do this year? Try sports." | 2026-10-16 | **RULE** / decision |

**Not found locally (gaps):**
- **The GHL-built marketing campaigns.** Memory says they carry "100% refund" and "Value Guarantee" in the footer, but the GHL API has no scope for email templates.
- **The live GHL newsletter-nurture copy.** `dr_ghl_newsletter` only posts to a webhook.
- **The live GHL abandonment copy.**
- **The v1 popup emails at 18h and 40h.** Only the audit's quoted fragments survive: "REGISTER FOR THE SEASON", "Before registration closes, here is the direct link", "Our upcoming season is filling and we finalize rosters soon", signed "From Coach Luis".
- **No old Wix newsletters** anywhere.
- **Nothing relevant in ~/Downloads or ~/Desktop.** The only DR file there, `Mensajes-Coaches-Winter-2026.pdf`, is a coach-message stats report.

---

