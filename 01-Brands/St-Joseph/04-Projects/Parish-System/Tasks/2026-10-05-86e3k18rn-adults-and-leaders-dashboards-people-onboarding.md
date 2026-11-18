---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3k18rn"
owner: Cristian
last_updated: 2026-11-17
sensitivity: internal
related_systems:
  - clickup
  - st-joseph-connect
related_notes:
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home]]"
hub_role: leaf
tags:
  - st-joseph
  - clickup-task
  - week-oct-5
---

# Build the St. Joseph Adults and Leaders dashboards, People onboarding, and close out open rollout items

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 5 🍁

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3k18rn](https://app.clickup.com/t/86e3k18rn) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | — |
| Creada | 2026-10-05 10:22 |
| Actualizada | 2026-10-07 11:16 |
| Cerrada | 2026-10-07 08:56 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis pidió construir los dos dashboards que faltaban (St. Joseph Adults y Leaders, con roles Catechist y Leader), la página People para el onboarding y la jerarquía Admin → Catechists → Leaders, además de cerrar los pendientes heredados de las subtareas del proyecto padre. Cristian reportó el 5 de octubre que los tres dashboards, People y Learning quedaron construidos, con la base de datos en producción y el código en GitHub (main @ ed46d92), pendiente de Publish en Lovable; también cerró cuatro pendientes heredados (acceso de leader más estrecho, envío del weekly report, check-in por persona en eventos, push de los fixes locales). El interruptor de make-up en Settings → Learning quedó apagado hasta que Luis confirme si completar un módulo asignado borra la ausencia. El 7 de octubre Luis pidió replicar el sandbox de dashboards para Discipline Rift y Brain creó la subtarea 86e3m8qbh.

## Descripción
## Objective
Now that the **Admin dashboard** and the public frontend exist in Build and roll out the St. Joseph parish system (P1 Events & Retreats → P2 Adult Formation & OCIA → P3 Weekly Schedule & Check-In) ([https://app.clickup.com/t/86e3ercb4](https://app.clickup.com/t/86e3ercb4)), build the two remaining dashboards and the role hierarchy that ties all three together:

1. **Admin**: staff/parish office (already built; gets a new **People** page)
2. **St. Joseph Adults**: every adult who is learning/being formed, in any program (OCIA, Adult Faith Formation, Bible study, etc.)
3. **Leaders**: one dashboard with two roles inside it, **Catechist** and **Leader**

Hierarchy: **Admin → Catechists → Leaders**. Admin manages catechists (and can manage leaders directly if needed). Catechists manage their leaders. Luis Torres is the supervisor over all catechists for now.

Also close out the items still open on the parent's subtasks (listed at the bottom).

Source: [https://app.clickup.com/t/86e3jryaj?comment=90170258763441](https://app.clickup.com/t/86e3jryaj?comment=90170258763441).

* * *

## Context
### Naming
*   Do **not** use the word "Catechumens" anywhere in the UI. The dashboard is called **St. Joseph Adults** ("Adults" for short).
*   The catechist dashboard is called **Leaders**, not "Catechists". Catechist and Leader are **roles** inside it.
### 1\. St. Joseph Adults dashboard
One login for every adult, regardless of program. What they see depends on what they're registered for.

**Profile**
*   Personal info they fill out and update themselves: address, birthday, contact info, and every participant field we already store on the admin side
*   Document uploads (baptismal certificate, marriage certificate, etc.), the same documents admin tracks in Sacraments
*   Parish registration form, submitted digitally
*   Any other program forms, submitted digitally from here

**Modules (left nav)**
*   **Learning**
*   **Schedule**: only for programs they're registered in
*   **Attendance**: their own record
*   **Events**: browse and register

**Not registered yet?** They can browse every available program and sign up for one that fits them (adult programs specifically).
### 2\. Learning module (lives in the Adults dashboard)
*   Content is organized into **modules, one per month**: Module 1 = everything covered in October, Module 2 = November, etc.
*   Inside each module, **each formation date gets its own topic page** with all the resources and the full breakdown of what happened that day, so an adult can learn on their own.
*   Modules have **completion tracking**: an adult works through a module and marks it complete.
*   **Admin can assign a specific module to a specific person.** Main use: someone missed a date, admin assigns them that module, and they're **required** to complete it.
### 3\. Leaders dashboard (roles: Catechist, Leader)
**Catechist** sees:
*   **Schedule**
*   **Content**, split into **Past content** and **Future content** (this is the key differentiator: catechists can see what's coming, not just what happened)
*   **Events**
*   **Leaders**: the leaders they oversee
*   **People**: create access for their leaders and give them permissions

How it works in practice (OCIA example): one catechist oversees \~5 leaders. Leaders help break down the material, run small groups, and take on specific tasks. The catechist needs to:
*   Assign leaders (to their group, to small groups, to specific tasks)
*   Communicate directly with their assigned leaders

**Leader** sees:
*   Old content
*   New content
*   Schedule
*   Where they're assigned
*   How the small groups are distributed
### 4\. People page (Admin + Leaders dashboards)
This is the onboarding hub and it's a must-have.
*   **Admin People page**: a breakdown of every single registered person with dashboard access, across all three dashboards.
*   From here admin can **create a profile, add their email, set the role** (catechist or leader), fill in their info, and **assign a supervisor**. For catechists the supervisor is the admin owner, currently Luis Torres.
*   **Catechist People page**: same idea, scoped down. Catechists create access for their own leaders and set what those leaders can see/do.
### What already exists (don't rebuild)
Per Data model & architecture (extensible to Phase 2) ([https://app.clickup.com/t/86e3etj5v](https://app.clickup.com/t/86e3etj5v)) and Module 7: Branding, bilingual UI, launch & staff training ([https://app.clickup.com/t/86e3etjjr](https://app.clickup.com/t/86e3etjjr)): roles admin / staff / data manager / catechist / volunteer with access by area, row-level security, audit log, people + documents + registrations + attendance + catechist assignments tables, and a bilingual participant **/me portal**. The Adults dashboard should grow out of /me; the Leaders dashboard extends the catechist role.

* * *

## To Keep in Mind
*   **One person, many roles.** A catechist can also be an adult learner; a leader can be in a Bible study. One login, and the person switches between the dashboards their roles unlock. Don't create duplicate accounts.
*   **Map the existing "volunteer" role to "Leader"** instead of adding a parallel role. Today volunteers have the same access as catechists (Module 3: Attendance, QR check-in & absence rules ([https://app.clickup.com/t/86e3etj9x](https://app.clickup.com/t/86e3etj9x))); Leaders must get a narrower set.
*   **Supervisor is a field on the person**, not hardcoded. Default catechist supervisor = Luis Torres. Admin can reassign.
*   **Privacy:** leaders and catechists must not see restricted Sacraments case notes (marriage/annulment), documents, or health/allergy info unless the parish approves. Allergy visibility is still an open question to the parish (Retreats pilot: Men's Emmaus (Oct 9–11), Women's Silent Retreat (Oct 10), "Never Alone" (Oct 16–18) ([https://app.clickup.com/t/86e3etjgz](https://app.clickup.com/t/86e3etjgz))).
*   **Assigned modules tie into attendance:** a missed session should make it easy for admin to assign the matching month's module, and completion should count toward the make-up/excused logic in Module 3: Attendance, QR check-in & absence rules ([https://app.clickup.com/t/86e3etj9x](https://app.clickup.com/t/86e3etj9x)). Confirm with Luis whether completing an assigned module clears an absence.
*   **Future content** visibility: catechists see it, adults don't. Confirm whether leaders see future content (Luis's list says "new content").
*   **Leader communication** goes through the existing Outbox. Email sending still isn't deployed (Module 6: Communications, reminders & weekly reports ([https://app.clickup.com/t/86e3etjea](https://app.clickup.com/t/86e3etjea))), so that's a blocker for this feature.
*   **Bilingual EN/ES** on the Adults dashboard (participant pages already are). Leaders dashboard should be EN/ES too since Spanish formation runs Tuesdays.
*   **All document uploads must support drag-and-drop**, not just click-to-browse.
*   Mobile-first: adults and leaders will mostly use this on their phones.
*   Test with at least one real profile per role: admin, catechist, leader, registered adult, unregistered adult.
*   Still open from the parent's subtasks (carry over)

    **Launch blockers**

    *   Publish in Lovable (published URL still shows "Build incomplete") and set up the domain (Module 7: Branding, bilingual UI, launch & staff training ([https://app.clickup.com/t/86e3etjjr](https://app.clickup.com/t/86e3etjjr)))
    *   Deploy email sending (send-queued-emails, send-login-code) (Module 6: Communications, reminders & weekly reports ([https://app.clickup.com/t/86e3etjea](https://app.clickup.com/t/86e3etjea)))
    *   Send the open-questions message to the parish and log the date; push/publish the locally committed fixes (Reconcile and correct every St. Joseph project record against all sources (Sept 24 to Oct 1) ([https://app.clickup.com/t/86e3j54f1](https://app.clickup.com/t/86e3j54f1)))

    **Access** (Get access: parish email, database, church calendar, catechist Excel ([https://app.clickup.com/t/86e3etj2r](https://app.clickup.com/t/86e3etj2r)))

    *   Parish database access and Microsoft church calendar access: not confirmed
    *   Sample Camino import file (Wendy) so CSV exports stop using neutral columns
    *   Apple business developer + Google Play accounts for mobile apps

    **Data model** (Data model & architecture (extensible to Phase 2) ([https://app.clickup.com/t/86e3etj5v](https://app.clickup.com/t/86e3etj5v)))

    *   No household record for two-parent households
    *   Emmaus server form/screen not built

    **Registration** (Module 1: Registration engine (OCIA, Adult Formation, Events) ([https://app.clickup.com/t/86e3etj6r](https://app.clickup.com/t/86e3etj6r)))

    *   Parish answer: Adult Formation form vs QR sign-in only
    *   Men's Emmaus server form in the app
    *   Child's class is free text, not linked to Camino

    **Payments** (Module 2: Payments & automatic reconciliation (replace Gift Central links) ([https://app.clickup.com/t/86e3etj7p](https://app.clickup.com/t/86e3etj7p)))

    *   Stripe account in the parish's name (legal name, EIN, bank, rep); still on test mode
    *   How to reconcile payments already made (Gift Central report)
    *   Do Emmaus servers pay?

    **Attendance** (Module 3: Attendance, QR check-in & absence rules ([https://app.clickup.com/t/86e3etj9x](https://app.clickup.com/t/86e3etj9x)))

    *   Volunteer/leader role still has catechist-level access
    *   Weekly report is on screen only, not emailed

    **Sacraments** (Module 4: Sacraments (OCIA): groups, sacrament paths, documents & calls ([https://app.clickup.com/t/86e3etjca](https://app.clickup.com/t/86e3etjca)))

    *   Confirm certificate flow with Yolanda and Wendy
    *   Separate marriage class (\~12 to 14 people): Mary to decide
    *   Staff review of Pass / Fail / ? and group placement rules

    **Communications** (Module 6: Communications, reminders & weekly reports ([https://app.clickup.com/t/86e3etjea](https://app.clickup.com/t/86e3etjea)))

    *   No automatic sequences or scheduled reminders; session reminders and weekly summary sent by hand
    *   SMS only opens the phone's messaging app
    *   Call script: Luis writes it

    **Rooms** (Module 8: Facilities & room calendar (Future phase, ready early) ([https://app.clickup.com/t/86e3etjg6](https://app.clickup.com/t/86e3etjg6)))

    *   Parish to confirm the Tuesday room map week by week
    *   Email invites to leaders not built
    *   Decide with Brandon and Visionary (Jack): this calendar vs Outlook room mailboxes

    **Retreats pilot** (Retreats pilot: Men's Emmaus (Oct 9–11), Women's Silent Retreat (Oct 10), "Never Alone" (Oct 16–18) ([https://app.clickup.com/t/86e3etjgz](https://app.clickup.com/t/86e3etjgz)))

    *   Women's Silent Retreat real capacity (system says 30, 85 signed up)
    *   Delete the 4 test registrations (after approval)
    *   Confirm prices and Emmaus departure/return times
    *   Retreat attendance + lessons learned into the Events module

    **Launch** (Module 7: Branding, bilingual UI, launch & staff training ([https://app.clickup.com/t/86e3etjjr](https://app.clickup.com/t/86e3etjjr)))

    *   Training dates, go-live date, short staff training, rollout plan with Luis and Fr. Benjamin

## Subtareas
_Sin subtareas._

## Adjuntos
_Sin adjuntos._

## Comentarios
### 2026-10-05 10:24 · Luis Torres
@Brain I want you to remap this new task by taking in the pending things that we didn't get to complete before and putting them here, and also organizing them into multiple different subtasks. You keep making references to the old subtasks, but we're going to stop working on that subtask. Take the information that I put in here to create this new subtask: a task with the new things that we're going to be doing, considering the things that were not accomplished before. Some of the things that were accomplished before were already done, so it's up to Chris to mark them as finished.

#### ↳ Respuesta 2026-10-05 10:25 · Brain
On it, Luis. Plan: rewrite this task so it's fully self-contained (no more pointers to the old modules), then split the work into 10 subtasks right here, each with Objective / Context / To Keep in Mind. Old done stuff stays with Chris to close.

Proposed subtasks
Roles, hierarchy & People pages: Admin → Catechist → Leader, volunteer mapped to Leader with narrower access, supervisor field (default Luis), one login for many roles, Admin + Catechist People onboarding
St. Joseph Adults dashboard: profile, drag-and-drop doc uploads, digital parish registration and program forms, Schedule / Attendance / Events, browse and sign up for programs, EN/ES, mobile-first
Learning module: one module per month, a topic page per formation date, completion tracking, admin assigns modules for missed dates (linked to attendance make-up logic)
Leaders dashboard: Catechist view (past + future content, leaders, assignments, small groups, messaging) and Leader view
Launch blockers & go-live: publish in Lovable + domain, deploy email sending, push the local fixes, training dates, go-live date, staff training, rollout plan with Fr. Benjamin
Communications & automation: automatic sequences and reminders, emailed weekly report, real SMS, email invites to leaders, call script (yours)
Data model & registration gaps: household record, Men's Emmaus server form, child's class linked to Camino, Camino sample import (Wendy)
Payments go-live: Stripe in the parish's name, reconcile Gift Central payments, do Emmaus servers pay
Retreats → Events: Silent Retreat capacity (30 vs 85), delete the 4 test registrations, prices and Emmaus times, attendance + lessons learned into Events
Parish decisions & access: send the open-questions message, DB + Microsoft calendar access, Apple/Google dev accounts, Adult Formation form vs QR, certificate flow (Yolanda/Wendy), marriage class (Mary), Pass/Fail review, Tuesday room map, calendar vs Outlook (Brandon/Jack), allergy visibility

They'll all be unassigned unless you want them on Chris.
Create all 10 + rewrite taskSame, but assign ChrisCancel

### 2026-10-05 17:14 · Cristian Berrío
Status update: dashboards built and pushed to GitHub (main @ ed46d92)

The three dashboards, People onboarding and Learning are built. The database changes are already in production, and the code is on GitHub. The live site does not show any of it until someone clicks Publish in Lovable.

Admin
People page: every person with access to any of the three dashboards. From here admin creates the profile, adds the email, sets the role, supervisor, groups and leader permissions. The invitation goes out through the Outbox.
Content tab on each group: one page per formation date, with drag-and-drop files. When the same topic is taught on several days (e.g. AFF Mon/Wed/Thu), it counts as one topic and the page can be shared across those dates.
Assign module: from an absence or from the person's record.
Settings → Learning: make-up switch (does completing an assigned module clear the absence?). It is OFF until Luis confirms.

Leaders (/leaders), EN/ES, mobile-first
Everyone: Home, Schedule (list + QR), Content (past / future), Small groups, Events.
Catechist also gets Leaders (tasks and messages to their leaders) and People (creates access for their own leaders and sets their permissions, only within their groups).
volunteer is now leader, with a narrower set: attendance/QR only with the "take attendance" permission, and future content only with the "future content" permission.

St. Joseph Adults (/me), grown out of the existing portal
Home, Learning (modules by month, mark topics as seen), Schedule, Attendance, Events, Programs (browse and sign up if not registered), Documents (drag-and-drop) and full Profile.
The parish registration form and program forms are filled inside the dashboard, already prefilled with the person's data.
No "Catechumens" wording anywhere.

Across the app
One account per email, with a switcher between the dashboards a person's roles unlock. No duplicate accounts.
Privacy: catechists and leaders no longer see registration answers (allergies, OCIA marriage answers). They see who is registered, not the answers. Only staff do.
Access rules are covered by an automated test suite (35 checks: catechist, leader, adult and stranger boundaries). All pass.

Carry-over items closed by this work
✅ Volunteer/leader role no longer has catechist-level access
✅ Weekly report has "Email this report" and a lessons-learned field (sends through the Outbox)
✅ Per-person check-in at events
✅ Locally committed fixes pushed to GitHub

### 2026-10-07 08:58 · Luis Torres
@Brain Cris was able to successfully build a sandbox where, with one link, you can see all of the different dashboard accesses that we have created.

This was done using this task and instructions that I gave to him directly.

I want to build the same sandbox for Discipline Rift, so that from one link we can access all the different dashboards that we have built out. Anytime we make changes on any of those dashboards, those changes also reflect on the sandbox.

This is for demonstration purposes, as we have both seen and observed that people are loving the systems that we're building. Having a link with all of the different dashboards in one link that can access all the different dashboards (as in a sandbox view) is pretty awesome.

Create a subtask to do this for Discipline Rift and put it under the task below. 86e3jryaj

#### ↳ Respuesta 2026-10-07 08:59 · Brain
I created 86e3m8qbh under OCT 5 and assigned it to Cris, since he built the St. Joseph sandbox. The main rule in it: the sandbox runs on the same live app as the real site and only uses fake data, so every dashboard change shows up there automatically.

What's in the subtask
The St. Joseph method, reused: I didn't find a write-up of the St. Joseph sandbox itself, so I based this on the Oct 5 sync notes. That setup is a /demo route on the same database, with every demo record tagged sandbox so it can be wiped later, filled with fake people, and the links kept in one place.

Dashboards in the hub: the public site and registration, Admin, Coach, Coach Hub, the Parent portal and the mobile app if it can be shown. Each one opens in one click already logged in as a demo user for that role. Cris should check the list in case I missed a dashboard.

Guardrails:
No real kids, parents or coaches show up anywhere.
Demo users can't trigger real emails or texts (GoHighLevel, Outbox, roster sends, coach reminders), real Stripe charges, or show up in admin numbers.
There's one button to wipe the demo data and reload a fresh set.
The hub works on a phone.
Demo content follows DR brand rules: the 55 schools line is the only stat, with no fake testimonials.

When it's done: Cris posts the link and a short how-to in the task and saves it in the Sandbox bookmarks folder.

I left the Brand field empty because I couldn't set the DisciplineRift option from here, so tag it by hand if your filters need it.

Sources
app.clickup.com/t/86e3k18rn?comment=90170259805411 
 

86e3k18rn

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system|Build and roll out the St. Joseph parish system]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj5v-data-model-and-architecture|Data model & architecture]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjjr-module-7-branding-bilingual-ui-launch-training|Module 7: Branding, bilingual UI, launch & training]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj9x-module-3-attendance-qr-check-in-absence-rules|Module 3: Attendance, QR check-in & absence rules]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjgz-retreats-pilot-emmaus-silent-retreat-never-alone|Retreats pilot]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjea-module-6-communications-reminders-weekly-reports|Module 6: Communications, reminders & weekly reports]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-02-86e3j54f1-reconcile-every-project-record-sept-24-to-oct-1|Reconcile every project record (Sept 24 to Oct 1)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj2r-get-access-parish-email-database-calendar-catechist-excel|Get access: parish email, database, calendar, catechist Excel]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj6r-module-1-registration-engine|Module 1: Registration engine]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj7p-module-2-payments-and-reconciliation|Module 2: Payments & reconciliation]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjca-module-4-sacraments-ocia|Module 4: Sacraments (OCIA)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjg6-module-8-facilities-and-room-calendar|Module 8: Facilities & room calendar]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-08-86e3myy1e-fix-ocia-classification-baptized-catholics|Fix OCIA classification (baptized Catholics)]]
- Sandbox para Discipline Rift (subtarea creada por Brain): [86e3m8qbh](https://app.clickup.com/t/86e3m8qbh)
