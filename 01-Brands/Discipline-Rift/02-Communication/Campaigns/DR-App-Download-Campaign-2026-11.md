---
brand: Discipline-Rift
area: communication
subarea: campaigns
note_type: campaign
status: draft
canonical: false
used_for_ai: true
source_type: derived
source_reference: "Propuesta 2026-11-23 sobre roadmap app aprobado por Luis (ClickUp doc COMMS DR 8cqnrff-27437 pág. 4). Copia en repo disciplinerift/docs/proposals/2026-11-23-app-download-campaign.md"
owner: Luis
last_updated: 2026-11-23
sensitivity: internal
hub_role: leaf
audience: parent
channel: [email]
up:
  - "[[01-Brands/Discipline-Rift/02-Communication/Communication-Home]]"
related:
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Marketing-Email-Language-Guide]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Campaigns/DR-Marketing-Email-History-Index]]"
---

# Campaña "Descarga la app" — v2

**Fecha:** 23-nov-2026 · **Redacta:** Cristian · **Aprueba:** Luis
**Base:** roadmap aprobado por Luis (doc Comunicaciones pág. 4) + [[DR-Marketing-Email-Language-Guide|guía de lenguaje]] construida con los correos reales de GHL ago–nov 2026 y los 14 principios de edición de Luis.
**v2 vs v1:** quitado el correo de prueba social (Luis saca las "proof stacks" del correo), quitados los 2 botones iPhone/Android (regla: una acción puesta dos veces), cada correo < 100 palabras de cuerpo (techo de Luis: 230), frases fijas de los correos reales, firma y remitente Coach Luis.

---

## 1. Cadencia (la de Luis, 29-oct)

| Día | Fecha propuesta | Canal | A quién | Ángulo |
| --- | --- | --- | --- | --- |
| D1 | Lun 5-ene-2027 | Correo | Todos los padres de la temporada | La app ya está |
| D3 | Mié 7-ene | Correo | Sin tag `dr_app` | "You can ask." (coach directo) |
| D6 | Sáb 10-ene | Correo | Sin `dr_app` | Los dos padres en la misma página |
| D9 | Mar 13-ene | SMS | Sin `dr_app` | Link directo |
| D12 | Vie 16-ene | Correo | Sin `dr_app` | Fecha real: Early Spring empieza la semana del 25-ene |

Hora: 7:30 PM Orlando. Remitente: `Discipline Rift <coachluis@disciplinerift.com>`.

**Botón único:** `GET THE APP` → una página `disciplinerift.com/get-app` que abre App Store o Google Play según el teléfono (falta construirla, ver §4). Debajo del botón, texto chico: "iPhone and Android".

---

## 2. Decisiones para Luis

1. **Audiencia:** el 5-ene Winter ya terminó. Propuesta: inscritos Early Spring 2027 + pagados Winter 2026.
2. **Sin garantía 100% en esta campaña:** va a padres ya inscritos (regla de 9-nov: no mostrar el refund a inscritos).
3. **Label del botón:** "GET THE APP" (sigue la lógica de "REGISTER": verbo + acción real).

---

## 3. Textos

Merge: `{{contact.first_name}}`. Footer estándar en todos (guía §2).

### D1 — La app ya está (todos) · 97 palabras de cuerpo

**Subject:** The Discipline Rift app is here
**Preview:** Your child's team, coach and schedule, on your phone.
**Hero:** Your team, in your pocket.

`[GET THE APP]` · iPhone and Android

Hi {{contact.first_name}},

Before the new season starts, we have something for you.

The Discipline Rift app puts your child's team on your phone.

**Message the coach.**
Send a message and get a notification when the coach answers.

**See every practice.**
After every practice, the coach posts an update with the skill taught, the progress made, and what the team will work on next.

**Know what's next.**
Practice reminders the day before, and the coach's note for the next practice.

Logging in takes a minute. Use the email you registered with and we send you a 6-digit code. No password.

`[GET THE APP]`

See you at practice!
Coach Luis
Founder, Discipline Rift

---

### D3 — "You can ask." (sin `dr_app`) · 71 palabras de cuerpo

**Subject:** How was practice? Now you can ask the coach
**Preview:** One message, straight to your child's coach.
**Hero:** A direct line to the coach.

`[GET THE APP]` · iPhone and Android

Hi {{contact.first_name}},

If "How was practice?" only ever gets you "Fine," now you have more to go on.

In the Discipline Rift app you can read the coach's update after every practice and message the coach directly. When the coach answers, you get a notification.

Running late, a question about the schedule, or your child is home sick? You can ask.

`[GET THE APP]`

Use the email you registered with. We send you a 6-digit code.

See you at practice!
Coach Luis
Founder, Discipline Rift

---

### D6 — Los dos padres (sin `dr_app`) · 70 palabras de cuerpo

**Subject:** Both parents, same updates
**Preview:** Add a second parent in the app and share the team.
**Hero:** The whole family on the team.

`[GET THE APP]` · iPhone and Android

Hi {{contact.first_name}},

What happens when the other parent does the pickup and you have the coach's message?

In the Discipline Rift app you can add a second parent. You both see the same coach updates, the same schedule and the same messages from the coach.

1. Get the app and log in with your email.
2. Add the second parent from your account.
3. They get an invite and join your family.

`[GET THE APP]`

See you at practice!
Coach Luis
Founder, Discipline Rift

> Nota: verificar el texto del paso 2 contra la pantalla real antes de enviar.

---

### D9 — SMS (sin `dr_app`) · 1 segmento

> Hi {{contact.first_name}}! Coach Luis here. Message your child's coach and see every practice update in the Discipline Rift app: disciplinerift.com/get-app

(Estilo del SMS Fall→Winter de oct: "Hi X! …", corto, con exclamación.)

---

### D12 — Antes de Early Spring (sin `dr_app`) · 59 palabras de cuerpo

**Subject:** Early Spring starts the week of January 25
**Preview:** Set up the app before the first practice.
**Hero:** Ready before the first practice.

`[GET THE APP]` · iPhone and Android

Hi {{contact.first_name}},

The new season starts the week of January 25.

Get the Discipline Rift app now, and the first practice reminder, the coach's update and the coach's messages land on your phone from day one.

Log in with the email you registered with. We send you a 6-digit code.

`[GET THE APP]`

If something doesn't work, just reply here or call (407) 614-7454.

See you at practice!
Coach Luis
Founder, Discipline Rift

---

## 4. Qué falta para enviar

| Falta | Dueño |
| --- | --- |
| Luis aprueba textos + 3 decisiones (§2) | Luis |
| Página `/get-app` que redirige a la tienda según el teléfono | Cristian |
| Confirmar que el tag `dr_app` ya aparece en GHL | Cristian |
| Verificar en la app real: update por práctica, nota del coach, invitar 2do padre (iOS y Android) | Cristian |
| HTML con el diseño de los correos de sep–oct (azul #0497F7, hero, 2 botones) | Cristian |
| Pasar textos por `dr-brand-guardian` | Cristian |
| Actualizar doc Comunicaciones el día que se active | Cristian |
