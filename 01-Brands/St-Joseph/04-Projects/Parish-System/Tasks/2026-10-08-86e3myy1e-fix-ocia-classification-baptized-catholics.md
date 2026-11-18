---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3myy1e"
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

# Fix OCIA classification logic so baptized Catholics are no longer counted as OCIA across all dashboards

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 5 🍁

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3myy1e](https://app.clickup.com/t/86e3myy1e) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | — |
| Creada | 2026-10-08 12:26 |
| Actualizada | 2026-10-12 10:23 |
| Cerrada | 2026-10-12 10:23 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis pidió corregir en la fuente la regla de clasificación para que los católicos bautizados no se cuenten como OCIA en ningún dashboard, conteo, reporte o formulario (145 personas en un solo grupo OCIA, 49 de ellas católicas bautizadas). Cristian entregó el 8 de octubre un grupo nuevo, Adult Sacraments (Sacramentos para Adultos), con 49 personas, y OCIA quedó en 96 (25 + 65 + 6), sin perder registros, asistencia ni historial; el enrutamiento desde el OCIA Candidate Form y el paso automático al verificar un bautismo dudoso como católico quedaron automáticos, y los ritos OCIA excluyen a Adult Sacraments. Este año Adult Sacraments sigue en la misma clase OCIA. Pendiente al último comentario: que la versión se publique en Lovable para verlo en el sitio en vivo (los datos ya estaban actualizados).

## Descripción
## Objective
Rework the sacraments grouping logic in the St. Joseph Formation app so **baptized Catholics are never classified as OCIA**, and fix every dashboard, count, report and form that depends on that classification.

**Rule:** OCIA only applies to people who have **not** been baptized Catholic and are entering the faith. If someone was baptized Catholic, they are **not** OCIA.
## Context
On the Groups page (`/admin/formation`), the **Sacraments (OCIA)** section currently lumps everyone into one OCIA group (145 people), including **49 Baptized Catholic**. That's wrong. The section description even says "Catholics completing sacraments" are a subgroup of OCIA.

![](https://t9017418223.p.clickup-attachments.com/t9017418223/6b78c700-4899-43b8-b0a3-73f936824d6b/image.png)

Current breakdown shown in the OCIA card:
*   49 Baptized Catholic → **not OCIA**, must move to a separate group (e.g. Adult Sacraments / Adult Confirmation, Catholics completing First Communion and/or Confirmation)
*   25 Baptized, other Christian → OCIA (Profession of Faith / reception into full communion)
*   65 Unbaptized → OCIA (Baptism)
*   6 Baptism doubtful or unknown → OCIA, pending verification

Expected result: OCIA shows \~96 people (25 + 65 + 6), and the 49 baptized Catholics show in their own non-OCIA adult sacraments group.

Requested by Luis in [https://app.clickup.com/t/86e3jryaj?comment=90170260424422](https://app.clickup.com/t/86e3jryaj?comment=90170260424422).
## To Keep in Mind
*   Fix the logic at the source (classification rule / data model), not just the label in the UI.
*   Audit **every** place that reads OCIA status: Dashboard, Groups, People, Registrations, Sacraments, Rites, Reports, Communications, Payments, Forms ("2026-2027 OCIA Candidate Form"), and the Adults/Leaders dashboards.
*   Update the Sacraments section description copy so it no longer says Catholics completing sacraments are part of OCIA.
*   Rites tied to OCIA (Rite of Acceptance, Rite of Election, Scrutinies, etc.) must not include baptized Catholics.
*   Migrate the existing 49 records to the new group without losing registrations, payments, catechist assignments or history.
*   "Baptism doubtful or unknown" stays in OCIA until verified; once verified as Catholic baptism, the person should automatically move out of OCIA.
*   Registration forms: a person who answers "baptized Catholic" should be routed to the non-OCIA group automatically.
*   Test: counts on every dashboard should add up (OCIA + Catholic adult sacraments = previous 145) and no baptized Catholic should appear anywhere labeled OCIA.

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| image.png | png | 2026-10-08 12:26 | Luis Torres |

## Comentarios
### 2026-10-08 16:01 · Cristian Berrío
✅ Done: baptized Catholics are no longer counted as OCIA

Context
On the Groups page, the Sacraments (OCIA) section had everyone in one OCIA group: 145 people. That included 49 baptized Catholics.

Problem
OCIA is only for people entering the faith. Someone baptized Catholic is not OCIA, so every count, list and dashboard that said "OCIA 145" was wrong.

Solution
• There is a new group called Adult Sacraments (Sacramentos para Adultos) for baptized Catholics completing First Communion and/or Confirmation. It is not OCIA.
• OCIA now has 96 people: 25 baptized in another church, 65 unbaptized, and 6 whose baptism is doubtful or unknown. Those 6 stay in OCIA until the baptism is verified.
• Adult Sacraments has 49 people. 96 + 49 = 145, so nobody was lost.
• The 49 kept everything: registration, answers, attendance and history. They also have the same catechists.
• This year Adult Sacraments still sits in the same OCIA class (same day, same QR), and their attendance counts the same way. Next year they can have their own class times.
• It is automatic from now on:
– Someone who answers "baptized Catholic" on the OCIA Candidate Form goes straight to Adult Sacraments.
– If a doubtful baptism is verified as Catholic, the person moves out of OCIA by themselves.
– The system does not let anyone put a non-Catholic in Adult Sacraments.
• OCIA rites (Acceptance, Sending, Election, Scrutinies, Easter Vigil) never include Adult Sacraments people.

How to see it, step by step
Go to formation-foundations.lovable.app/admin and sign in.
In the menu, click Groups. Under Sacraments there are now two cards:
– OCIA · 96 people, split into 25 / 65 / 6
– Adult Sacraments · 49 people, all "Baptized Catholic", with "Meets with the OCIA class"
Click Open group on Adult Sacraments. The People tab shows the 49 people, and the Schedule tab says it meets with the OCIA class.
In the menu, click Sacraments. The top cards show OCIA 96 and Adult Sacraments 49. The subgroups appear in two rows (OCIA and Adult Sacraments), and each person has a label saying which one they are in.
Go back to the Dashboard. The Sacraments card reads "96 OCIA · 49 Adult Sacraments".
In the menu, click Rites, then Who receives what. OCIA and Adult Sacraments are listed separately. If you open an OCIA rite (for example a Scrutiny), the Adult Sacraments box does not appear.

To test the automatic move without touching real people
Use the demo at formation-foundations.lovable.app/demo (made-up people: OCIA 50 · Adult Sacraments 30).
Open Sacraments and pick someone whose baptism says "doubtful" or "unknown". Change the baptism to Baptized Catholic and save. The person moves to Adult Sacraments on their own.

Note: the live site shows all of this once the latest version is published in Lovable. The data is already updated.

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjca-module-4-sacraments-ocia|Module 4: Sacraments (OCIA)]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-05-86e3k18rn-adults-and-leaders-dashboards-people-onboarding|Adults and Leaders dashboards, People onboarding]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-13-86e3pxguj-reconcile-ocia-attendance-registrations-withdrawals|Reconcile OCIA attendance, registrations, withdrawals]]
