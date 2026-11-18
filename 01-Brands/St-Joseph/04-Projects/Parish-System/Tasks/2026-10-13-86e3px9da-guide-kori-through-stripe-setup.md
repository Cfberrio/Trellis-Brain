---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3px9da"
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

# Guide Kori through Stripe setup for parish registrations

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 19 🪪

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3px9da](https://app.clickup.com/t/86e3px9da) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | — |
| Creada | 2026-10-13 14:20 |
| Actualizada | 2026-10-15 12:16 |
| Cerrada | 2026-10-15 12:16 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis pidió guiar a Kori para que cree, verifique y conecte al banco de la parroquia la cuenta de Stripe a nombre de la parroquia, invitando a Luis como Administrator (sin compartir contraseñas), como base para mover registros y pagos a la plataforma. Se decidió no mover la inscripción actual de hombres (ya tenían el link de GiveCentral) y lanzar las próximas inscripciones en la plataforma. Cristian adjuntó el 13 de octubre la guía en PDF (St-Joseph-Stripe-Setup-Guide.pdf). Los dos checklists (configuración de Kori y lo que se necesita de la parroquia) aparecen completos en ClickUp y la tarea quedó aprobada el 15 de octubre; no hay comentarios que confirmen cada punto por separado.

## Descripción
## Objective
Get the parish's own Stripe account created, verified, and connected to the parish bank account, with us invited in so we can wire it to the registration platform. Kori does the setup (she owns the bank and identity info), we only need team access. This is the foundation for moving parishioner registrations + payments onto our platform.
## Context
Source: [https://app.clickup.com/t/86e3p6vdw?comment=90170262042136](https://app.clickup.com/t/86e3p6vdw?comment=90170262042136)

**Today's process is fully manual:** Father announces → Johanna makes an Outlook Forms QR → people register (no payment prompt) → Carly chases the form, copies emails, emails everyone for payment → Wendy sends the payments roster → Carly reconciles both lists by hand and re-emails whoever hasn't paid. GiveCentral doesn't connect to anything and went down this week, so even the payment link fails.

**Where we're headed:** one QR → one page to register and pay → paid people drop off the pending list automatically → admin sends unpaid reminders with one click. Money goes Stripe → parish bank.

**Decision:** we are NOT moving the current men's registration (they already got the GiveCentral link, a second link would confuse them). We're getting everything set up so the _next_ registrations launch on our platform fresh.

* * *

## Step by step for Kori (about 20 to 30 min)
Have ready: parish legal name + EIN, parish address and phone, the parish bank routing + account number (or online banking login), and the personal info of the person authorized to represent the parish (name, date of birth, home address, last 4 of SSN).
1. **Sign up.** Go to [stripe.com](http://stripe.com) → **Start now**. Use an official parish email (ideally a shared office address, not a personal one, so the account doesn't leave with one person).
2. **Confirm your email** from the message Stripe sends.
3. **Click "Activate payments"** on the dashboard.
4. **Business type:** choose **Nonprofit organization**. Enter the legal name _exactly_ as it appears on IRS paperwork, plus the EIN and parish address.
5. **Industry:** pick **Religious organizations**. Website: the parish website.
6. **Representative:** the authorized person enters their own details. Stripe requires this to verify the account. We never see it.
7. **Public details:** set the **statement descriptor** (what shows on people's bank statements) to something recognizable like the parish name. Add the parish office phone and support email.
8. **Bank account:** connect the parish account where the money should land. Use instant login or enter routing + account number.
9. **Turn on two-step verification** (Settings → Personal details → Security).
10. **Invite us:** Settings → **Team and security** → **Invite member** → enter Luis's email ([grouptrellis@gmail.com](mailto:grouptrellis@gmail.com)) → role **Administrator**. ⚠️ Please don't send us a password. The invite gives us what we need, and Kori can remove us any time.
11. **Optional but worth it:** Stripe offers reduced processing fees for nonprofits. Email Stripe support with the parish's nonprofit documentation to apply.

When it's done, Stripe shows the account as **active** with payouts enabled. Send Luis a quick note that it's finished.

* * *

## What we need from the parish
*   Stripe team invite (Administrator) sent to Luis
*   Confirmation the account is verified and payouts are on
*   Parish bank account connected and verified (Kori only, we never touch bank details)
*   Statement descriptor approved (the name parishioners will see on their statements)
*   Access to the **official parish email** so registration confirmations come from the parish, not from us (a shared mailbox or send permission, whatever IT approves)
*   Pricing sign-off: men's registration is **$100** (normally $185)
*   OK to create a **CCM** discount code for anyone with financial difficulty
*   Parish logo file for the registration page
*   Who on staff gets admin access to the paid/unpaid view (Carly at minimum)
## To Keep in Mind
*   **Never collect logins or bank details over email or chat.** Team invite only. If someone offers a password, decline it.
*   The account must be in the **parish's** name with the parish's EIN, not Trellis Fields or Discipline Rift, so the money goes straight to the parish.
*   Catholic parishes are often covered under the diocese's group tax exemption, not their own IRS letter. If Stripe asks for nonprofit proof, Kori may need the diocese's group ruling letter or the parish's listing in the Official Catholic Directory.
*   Stripe may ask for extra documents (bank letter, ID photo) during verification. That's normal. Kori just uploads them.
*   Don't build anything on the WordPress site. This is a standalone page reached by QR, a temporary fix until the bigger platform decision is made.
*   Keep this simple for staff: one link, one QR. Nothing that feels like "another tool."

## Checklists
### Kori: Stripe setup
- [x] Create Stripe account with official parish email
- [x] Invite Luis as Administrator
- [x] (Optional) Apply for nonprofit pricing
- [x] Complete business verification (nonprofit, legal name, EIN)
- [x] Set statement descriptor + support contact
- [x] Connect parish bank account
- [x] Turn on two-step verification

### What we need from the parish
- [x] Stripe invite accepted
- [x] Account active, payouts enabled
- [x] Official parish email access for confirmations
- [x] $100 price approved
- [x] CCM discount code approved
- [x] Parish logo
- [x] Admin users for paid/unpaid view confirmed

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| St-Joseph-Stripe-Setup-Guide.pdf | pdf | 2026-10-13 17:34 | Cristian Berrío |

## Comentarios
### 2026-10-13 17:34 · Cristian Berrío
St-Joseph-Stripe-Setup-Guide.pdf

(Adjunto en el comentario: St-Joseph-Stripe-Setup-Guide.pdf)

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj7p-module-2-payments-and-reconciliation|Module 2: Payments & reconciliation]]
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-05-86e3k18rn-adults-and-leaders-dashboards-people-onboarding|Adults and Leaders dashboards (pendiente: Stripe a nombre de la parroquia)]]
- Solicitud original en la semana OCT 19 🪪: [86e3p6vdw](https://app.clickup.com/t/86e3p6vdw?comment=90170262042136)
