---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3rvdtb"
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
  - week-oct-19
---

# Implement phase 4 St. Joseph Admin dashboard changes

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 19 🪪
- Tarea padre: [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-16-86e3rgkv1-propose-ocia-leader-groups-leaders-email-admin-changes|Propose OCIA leader groups, leaders email, and Admin dashboard changes for Leaders]]

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3rvdtb](https://app.clickup.com/t/86e3rvdtb) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | — |
| Creada | 2026-10-17 15:44 |
| Actualizada | 2026-10-19 12:51 |
| Cerrada | 2026-10-19 12:51 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Subtarea creada el 17/10 tras la aprobación de la propuesta, limitada a la sección 4 (dashboard de Admin): tarjetas Leaders/Catechists/Staff en el home, drag-and-drop y página de grupo en Leaders, People como área de accesos con pestañas Admin · Staff · Catechist · Leader, sección Staff con importador, columnas de catequistas, EN/ES y drag-and-drop en cargas. Cristian publicó todo el 19/10 en formation-foundations.lovable.app, solo interno y probado con usuarios demo; los grupos quedaron como en la hoja de Luis (7 grupos, 66 personas). Quedaron abiertos: el Excel de staff, el nombre del grupo admin interno, la ortografía de "Kori", el rol de Deacon Gary y líderes para 4 grupos.

## Descripción
## Objective
Implement section 4, **Admin dashboard proposal**, of the approved OCIA proposal. Finish the missing dashboard features and adjustments for internal admin use. **Luis will decide and finalize all group composition and leader assignments. Do not generate, rebalance, finalize or populate groups from the proposed Excel, and do not work on the leaders email.**
## Context
Luis approved the proposal on October 17 and requested a subtask focused only on phase 4: [https://app.clickup.com/t/86e3rgkv1?comment=90170263764687](https://app.clickup.com/t/86e3rgkv1?comment=90170263764687).

Sources: Propose OCIA leader groups, leaders email, and Admin dashboard changes for Leaders ([https://app.clickup.com/t/86e3rgkv1](https://app.clickup.com/t/86e3rgkv1)), Propose OCIA leader groups, leaders email, and Admin dashboard changes for Leaders ([https://app.clickup.com/t/86e3rgkv1](https://app.clickup.com/t/86e3rgkv1)), Build the St. Joseph Adults and Leaders dashboards, People onboarding, and close out open rollout items ([https://app.clickup.com/t/86e3k18rn](https://app.clickup.com/t/86e3k18rn)), Reconcile OCIA attendance, registrations, profile notes and withdrawals in the St. Joseph database ([https://app.clickup.com/t/86e3pxguj](https://app.clickup.com/t/86e3pxguj)), and OCIA Team Game Plan: Road to Sunday 10/25 ([https://doc.clickup.com/d/h/8cqnrff-25917/e1161e35d63ecb7/8cqnrff-39057](https://doc.clickup.com/d/h/8cqnrff-25917/e1161e35d63ecb7/8cqnrff-39057)).

Original brainstorm recording:
[https://t9017418223.p.clickup-attachments.com/t9017418223/4f4a35d4-7475-46d5-b03a-9c05b0be073a/Would%20you%20help%20with%20OCIA%3F%20Brainstorming%20today%20at%205%3A15%20-%2010-15-2026.mp4?filename=Would%20you%20help%20with%20OCIA%3F%20Brainstorming%20today%20at%205%3A15%20-%2010-15-2026.mp4](https://t9017418223.p.clickup-attachments.com/t9017418223/4f4a35d4-7475-46d5-b03a-9c05b0be073a/Would%20you%20help%20with%20OCIA%3F%20Brainstorming%20today%20at%205%3A15%20-%2010-15-2026.mp4?filename=Would%20you%20help%20with%20OCIA%3F%20Brainstorming%20today%20at%205%3A15%20-%2010-15-2026.mp4)

The approved proposal distinguishes already-built functionality from remaining work. Verify the current implementation before changing it; preserve what already works.
### A. Admin home
*   Add three summary cards beneath the existing home stats: **Leaders, Catechists, Staff**.
*   Each card shows relevant live counts and opens its corresponding section.
### B. Leaders section and group management
*   Preserve the separate **Leaders** left-nav entry, groups board, contact exports and counters already reported built.
*   Keep group cards showing season of life, assigned leader, member count (x/10), and a **Needs leader** badge when unassigned.
*   Add admin drag-and-drop between groups, retaining an accessible/mobile alternative to dragging. This supports Luis's manual decisions; it must not automatically change group composition.
*   Build the group detail page: member names, phone/email, last three attendances, needs chips (convalidation, baptism certificate, sponsor, documents), hangout log with date and attendees, prayer list, and leader notes.
*   Add last check-in and each leader's pending-item checklist to the roster. Reuse the existing owner-based Pending tab data rather than duplicating the 19 items reported loaded.
*   Verify copy/export contacts per group or leader still works.
*   Derive counters from current data, not hardcoded proposal totals.
*   **Exclude automated Suggest groups changes and all actual grouping/leader-assignment decisions from this subtask.**
### C. People and access
*   Make People an access/roles area only, with tabs ordered **Admin · Staff · Catechist · Leader**. Remove the Adults category and reconcile the extra Facilitators / Priest & deacon categories into the approved role model without losing people or their role history.
*   Show Kori and Father Ben in the parish Admin category; do not send invitations or grant new access as a side effect.
*   Add a separate internal admin group, hidden from parish-facing views. Luis must confirm its name before final naming; do not guess it.
*   Ensure every person name/row throughout the app opens that person's profile, including admins whose profiles are mostly empty. People and Leaders reportedly already support this; audit the remaining locations.
*   Support one person with multiple roles rather than duplicate records.
### D. Staff
*   Verify the section is named **Staff**, with Holidays as a tab and the directory/empty-tab skeleton preserved.
*   Prepare the Staff import path. Import the staff Excel only when Luis supplies the correct list; the proposal marks it as missing. Do not invent staff records or substitute the catechist list.
### E. Catechists
*   Preserve the existing directory records, phone/email and multi-role links.
*   Add program, language and notes columns from the source directory where available. The parent links [08-Catechist-Directory-and-Checkpoints.xlsx](https://t9017418223.p.clickup-attachments.com/t9017418223/b9a20efc-76b1-4296-a682-18cf5337ecae/08-Catechist-Directory-and-Checkpoints.xlsx).
*   Verify Christo, Anais, Morgan, Kat and Brenda retain both Catechist/directory and Leader roles as appropriate, with no duplicate people.
*   Confirm Deacon Gary's final role with Luis before changing it.
### F. Adults and cross-app polish
*   Verify the **Adults** rename and **Adults · Youth · Kids** tabs already reported built. Build only Adults; Youth and Kids remain placeholders.
*   Complete EN/ES support for the admin screens (reported English-only).
*   Make every upload/import area support drag-and-drop as well as click-to-browse.
*   Complete mobile-first layout and interaction checks across all changed screens.
## To Keep in Mind
*   Approval is for this implementation scope. Keep the work internal: no leader logins, invitations, system emails/texts, candidate-facing groups, or parish-facing release/access changes.
*   Luis owns final group membership and leader assignment. Do not import the tentative grouping workbook or act on its proposed assignments.
*   Leaders' contact exports and any future leader-facing views may include contact information and needs chips only, never Sacraments case notes, marriage answers, health/allergy information, or sensitive staff-only fields. Do not leak those fields through exports.
*   Preserve the baptism-based OCIA vs Adult Sacraments split and existing Archive/Move behavior.
*   Groups are not assigned Sunday seating and must not be announced to candidates.
*   Use demo users only for testing. Do not alter real participant memberships or send real communications during QA.
*   Open inputs: staff Excel, internal admin group name, Kori spelling, and Deacon Gary's role. Complete independent work while leaving those dependent decisions unresolved.
*   Completion means the remaining phase 4 features are implemented and tested, already-built features pass regression checks, and unresolved inputs are clearly documented without guessed values.

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| 08-Catechist-Directory-and-Checkpoints.xlsx | xlsx | 2026-10-17 15:44 | — |
| Would you help with OCIA? Brainstorming today at 5:15 - 10-15-2026.mp4 | mp4 | 2026-10-17 15:44 | — |
| Would you help with OCIA? Brainstorming today at 5:15 - 10-15-2026.mp4 | mp4 | 2026-10-17 15:44 | — |

## Comentarios
### 2026-10-19 10:35 · Cristian Berrío
Phase 4 is live (pushed and published Oct 19)

Everything below is published at formation-foundations.lovable.app. Everything is internal. Nobody was invited, no logins were created, and no emails or texts went out. Testing used demo users, and the test data was removed afterwards.

A. Admin home. Leaders, Catechists and Staff cards sit under the stats. They show live counts and open their section.

B. Leaders
Drag and drop people between groups, or back to "Not in a group". It works with a mouse, on a phone (press and hold) and with the keyboard (Space). The Move menu is still there. Only the person you drag moves.
Each group card shows a red Needs leader badge when it has no leader, and its name opens the group page: contacts, last 3 classes, needs chips, a hangout log, a prayer list and leader notes. You can also copy contacts or download an Excel there.
Needs chips: convalidation, annulment, baptism certificate, sponsor, documents. Never case notes or form answers.
Hangout log: date and who came.
On the Leaders tab, each leader shows their last check-in and a checklist of their own Pending items. It uses the same items as the Pending tab, so ticking one ticks both.
Counters come from live data. Suggest groups was not changed.

Groups now match your sheet (OCIA-Leader-Groups.xlsx, Oct 19)
7 groups, 66 people:
College A (10), College B (10), Young adults A (8), Young adults B (7): need a leader
College C (10): Morgan
Engaged & married (10): Christo
Adults 30+ (11): Kat. This is 1 over the cap of 10.
Andrew Mier and the 2 minors have no group.
The 10 people who came to only 1 class are no longer in a group. They are still on the Sacraments list.
Anais and Brenda don't have a group yet.

C. People
Tabs in your order: Admin · Staff · Catechist · Leader.
The Adults category is gone. Facilitators now sit under Catechist. Every role is kept.
Father Ben is in Admin. This is a category only, with no new access.
Our own admin logins are in a separate tab labelled "Internal admin · name pending", which the parish never sees.
Anyone whose role doesn't fit a tab yet is under "To confirm" (today only Deacon Gary).
Names open the person's profile across Reports, Rites, Events, Groups, Registrations, Outbox, Team and Outreach. A login with no person on file opens a basic profile.

D. Staff. The section is named Staff. Its tabs are Holidays 2027, Directory and two "Soon" tabs (Profile, Posts). Import staff list in Directory is ready for your Excel: drag the file in or click to choose it, then preview and confirm. Each person gets the Staff category, with no invite and no login. Nothing has been imported yet.

E. Catechists. The directory has Programs, Language and Notes for all 25 people, from 08-Catechist-Directory. Christo, Anais, Morgan and Brenda are Catechist + Leader, and Kat is Facilitator + Leader. There are no duplicates.

F. Polish
EN/ES switch in the Admin header. It covers the menu, home, Leaders (with the group page), People and Staff. The other admin screens are still English.
All uploads accept drag and drop or click.
Changed screens were checked on a phone-size screen with no sideways scrolling.

Still needed from you
The staff Excel.
A name for the internal admin group.
The right spelling of "Kori" (not in the system yet, so not added).
Deacon Gary's role.
Leaders for the 4 open groups.

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-16-86e3rgkv1-propose-ocia-leader-groups-leaders-email-admin-changes|Propose OCIA leader groups, leaders email, Admin changes]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-05-86e3k18rn-adults-and-leaders-dashboards-people-onboarding|Adults and Leaders dashboards, People onboarding]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-13-86e3pxguj-reconcile-ocia-attendance-registrations-withdrawals|Reconcile OCIA attendance, registrations, withdrawals]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-12-86e3pck95-2027-holiday-voting-link-for-staff|2027 holiday voting link for staff]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-16-86e3rj6c8-propuestas-cambios-en-el-dashboard|Propuestas cambios en el dashboard]]
