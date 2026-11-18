---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "https://app.clickup.com/t/86e3ercb4"
owner: Cristian
last_updated: 2026-11-17
sensitivity: internal
related_systems:
  - clickup
  - st-joseph-connect
  - lovable
  - supabase
related_notes:
  - "[[01-Brands/St-Joseph/00-Brand-Core/Brand-Home]]"
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Timeline]]"
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Decisions-Log]]"
hub_role: system-hub
tags:
  - st-joseph
  - parish-system
---

# St. Joseph Parish System: Project Home

## Parent
- [[01-Brands/St-Joseph/00-Brand-Core/Brand-Home|St. Joseph Brand Home]]

## Qué es
Sistema parroquial propio de St. Joseph Catholic Church (Orlando), propiedad de la parroquia. Reemplaza Microsoft Forms, Gravity Forms, Excel, USBs, links de Gift Central y el calendario compartido de Outlook. Fases acordadas en la propuesta del 30 sep 2026: P1 Events & Retreats, P2 Adult Formation & OCIA ("Sacraments" en pantallas de staff), P3 Weekly Schedule & Check-In, y luego las áreas Future.

- Código: [GitHub Cfberrio/st.-joseph-connect](https://github.com/Cfberrio/st.-joseph-connect) (TanStack Start + Lovable Cloud/Supabase)
- App publicada: https://formation-foundations.lovable.app (horarios públicos en `/schedule/ocia-adults`, `/schedule/aff-en`, `/schedule/aff-es`)
- ClickUp: tarea madre [Build and roll out the St. Joseph parish system](https://app.clickup.com/t/86e3ercb4). El trabajo semanal cuelga de las tareas OCT 5, OCT 19, NOV 2 y NOV 9 en DEV › CB › Cristian.
- Personas clave: Luis Torres (pide y aprueba), Cristian Berrío (construye), Fr. Benjamin Lehnertz (párroco), Mary, Kori, Wendy y los líderes de grupos pequeños.

Esta nota y sus hijas se exportaron de ClickUp el 2026-11-17. Las notas de tarea copian literalmente la descripción, los adjuntos (solo su lista) y todos los comentarios con sus respuestas. Las credenciales se redactaron y el doc CREDENTIALS no se copió.

## Children
### Navegación
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Timeline|Línea de tiempo]]: qué pasó y cuándo
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Decisions-Log|Registro de decisiones]]: decisiones fechadas de Luis y del equipo

### Docs de ClickUp
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Docs/Discovery-Notes|Discovery Notes]] (25 sep, corregidas 2 oct)
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Docs/OCIA-Team-Game-Plan-Road-to-Sunday-10-25|OCIA Team Game Plan: Road to Sunday 10/25]] (15 oct, restricted)

### Reuniones y reportes (evidencia)
- [[01-Brands/St-Joseph/03-Evidence/Meetings/2026-10-02-SyncUp-Notes-Dev|SyncUp 2026-10-02]]: revisión del dashboard
- [[01-Brands/St-Joseph/03-Evidence/Meetings/2026-10-14-SyncUp-Notes-Dev|SyncUp 2026-10-14]]: follow-ups y Outreach
- [[01-Brands/St-Joseph/03-Evidence/Meetings/2026-10-16-SyncUp-Notes-Dev|SyncUp 2026-10-16]]: People, roles, líderes (restricted)
- [[01-Brands/St-Joseph/03-Evidence/Reports/2026-10-11-Sunday-Session-Sign-In-Report|Sunday Session Sign-In Report, 11 oct]] (restricted)
- [[01-Brands/St-Joseph/03-Evidence/Reports/Humble-Hungry-Smart|Humble, Hungry, Smart]]: material de equipo; falta confirmar con Luis que es de St. Joseph

### Espacio ClickUp ST JOSEPH
- [[01-Brands/St-Joseph/05-Operations/ClickUp-Space/ST-JOSEPH-Space-Overview|ST JOSEPH Space Overview]]: 6 listas, 5 formularios y 102 registros (restricted)

### Tareas
**Programa base (tarea madre + 15 subtareas, OCT 5 🍁)**

| Tarea | Estado | Creada | Qué se hizo |
|---|---|---|---|
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3ercb4-build-and-roll-out-the-st-joseph-parish-system\|Build and roll out the parish system]] | aprobado | 2026-09-25 | Tarea madre: todos los módulos construidos al 2 oct, con datos reales cargados |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj25-knowledge-transfer-with-johanna\|Knowledge transfer with Johanna]] | aprobado | 2026-09-25 | Traspaso hecho; importadas 509 asistencias, 46 catequistas y 140 de la lista maestra |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj2r-get-access-parish-email-database-calendar-catechist-excel\|Get access]] | aprobado | 2026-09-25 | Correo de Luis; Excel de catequistas, lista maestra y MS Forms recibidos |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj5v-data-model-and-architecture\|Data model & architecture]] | aprobado | 2026-09-25 | Esquema en supabase/migrations, RLS, auditoría |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj6r-module-1-registration-engine\|Module 1 Registration]] | aprobado | 2026-09-25 | Constructor de formularios, Candidate Form v2, 13 formularios web |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj7p-module-2-payments-and-reconciliation\|Module 2 Payments]] | aprobado | 2026-09-25 | Stripe Checkout + webhook, CSV de Gift Central, "To reconcile" |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etj9x-module-3-attendance-qr-check-in-absence-rules\|Module 3 Attendance]] | aprobado | 2026-09-25 | Check-in QR, reglas de ausencias, cumplimiento de padres |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjca-module-4-sacraments-ocia\|Module 4 Sacraments]] | aprobado | 2026-09-25 | G1/G2/G3, bautismo, casos de matrimonio, documentos, llamadas |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjd0-module-5-catechist-scheduling\|Module 5 Catechist scheduling]] | aprobado | 2026-09-25 | Dentro de Schedule desde el 2 oct |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjea-module-6-communications-reminders-weekly-reports\|Module 6 Communications]] | aprobado | 2026-09-25 | Outbox con envío manual; correo a Wendy |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjjr-module-7-branding-bilingual-ui-launch-training\|Module 7 Branding & launch]] | aprobado | 2026-09-25 | Marca y páginas móviles; staff solo en inglés |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjg6-module-8-facilities-and-room-calendar\|Module 8 Rooms]] | aprobado | 2026-09-25 | Salones como recursos, reglas de N-ésimo martes |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-09-25-86e3etjgz-retreats-pilot-emmaus-silent-retreat-never-alone\|Retreats pilot]] | aprobado | 2026-09-25 | Retiros de octubre importados como "To reconcile" |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-02-86e3j53x0-apply-oct-2-review-corrections\|Oct 2 review corrections]] | aprobado | 2026-10-02 | 10 correcciones de la revisión del 2 oct (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-02-86e3j54f1-reconcile-every-project-record-sept-24-to-oct-1\|Reconcile records Sept 24–Oct 1]] | aprobado | 2026-10-02 | 18 conflictos resueltos; mensaje de 14 preguntas para la parroquia |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-02-86e3j6va7-inline-contact-status-and-notes-on-ocia-list\|Inline contact status & notes]] | aprobado | 2026-10-02 | Estado de contacto y notas en línea |

**OCT 5 🍁**

| Tarea | Estado | Creada | Qué se hizo |
|---|---|---|---|
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-05-86e3k18rn-adults-and-leaders-dashboards-people-onboarding\|Adults & Leaders dashboards]] | aprobado | 2026-10-05 | Dashboards Admin People, Leaders y Adults (/me) con Learning |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-08-86e3myy1e-fix-ocia-classification-baptized-catholics\|Fix OCIA classification]] | aprobado | 2026-10-08 | Adult Sacraments (49 bautizados) separado de OCIA (96) |

**OCT 19 🪪**

| Tarea | Estado | Creada | Qué se hizo |
|---|---|---|---|
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-12-86e3pck95-2027-holiday-voting-link-for-staff\|2027 holiday voting]] | aprobado | 2026-10-12 | /vote y /admin/staff (Staff space) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-13-86e3px9da-guide-kori-through-stripe-setup\|Stripe setup guide for Kori]] | aprobado | 2026-10-13 | Guía en PDF para la cuenta Stripe de la parroquia |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-13-86e3pxguj-reconcile-ocia-attendance-registrations-withdrawals\|Reconcile OCIA attendance & withdrawals]] | aprobado | 2026-10-13 | Asistencia del 11 oct importada; Archive/Restore y Move (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-15-86e3qxu4z-clickup-outreach-feature-in-st-joseph\|Outreach board]] | aprobado | 2026-10-15 | /admin/outreach + /contact; 22 FOLLOW UP en Replied |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-15-86e3r1g9k-fix-sacraments-excel-export\|Sacraments Excel export]] | aprobado | 2026-10-15 | Export por Participation status con Summary |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-15-86e3r2c1h-sacramental-challenges-leaders-guide\|Leaders' guide (draft)]] | aprobado | 2026-10-15 | Borrador en PDF de 30 páginas con 12 casos anonimizados (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-16-86e3rgkv1-propose-ocia-leader-groups-leaders-email-admin-changes\|Leader groups proposal]] | aprobado | 2026-10-16 | Propuesta aprobada el 17 oct; fase 4 publicada el 19 oct |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-17-86e3rvdtb-implement-phase-4-admin-dashboard-changes\|Phase 4 Admin dashboard]] | aprobado | 2026-10-17 | Tarjetas en home, tablero de grupos, People con pestañas, Staff, catequistas |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-16-86e3rj698-pendientes-para-correo-de-leaders\|Leaders email]] | aprobado | 2026-10-16 | Texto del correo a líderes listo; no consta su envío |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-16-86e3rj6c8-propuestas-cambios-en-el-dashboard\|Dashboard proposal (FACT)]] | aprobado | 2026-10-16 | Solo el PDF adjunto |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-21-86e3uf6kw-subgrupos-de-matrimonio-en-excel-de-sacramentos\|Marriage subgroups in Excel]] | aprobado | 2026-10-21 | Columna "Marriage case" y tabla en Summary |

**NOV 2 🥩**

| Tarea | Estado | Creada | Qué se hizo |
|---|---|---|---|
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-30-86e3xd8fn-one-qr-code-per-session\|One QR per session]] | aprobado | 2026-10-30 | Enlace fijo /checkin/&lt;code&gt;; fin de la rotación |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-30-86e3xfq3y-update-sacrament-small-groups-breakdown\|Small groups breakdown]] | aprobado | 2026-10-30 | Workbook v3: 10 grupos, 93 personas (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-09-86e3zwmjy-print-ready-attendance-qr-pdf\|Attendance QR PDF]] | aprobado | 2026-11-09 | Botón Download PDF bajo Show QR |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-10-86e402hde-joes-bros-bbq-food-and-beverage-sign-up\|Joe's Bros BBQ sign-up]] | aprobado | 2026-11-10 | SignUpGenius con 8 slots (Fraternity) |

**NOV 9 🎋**

| Tarea | Estado | Creada | Qué se hizo |
|---|---|---|---|
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-30-86e3xd8fp-manual-attendance-oct-22-adult-faith-formation\|Oct 22 AFF manual attendance]] | realizado | 2026-10-30 | Hoja en papel ingresada; 3 nombres confirmados el 13 nov (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-05-86e3z12vb-reconcile-ocia-attendance-claims\|Reconcile OCIA attendance claims]] | realizado | 2026-11-05 | Reclamos por correo y WhatsApp conciliados; nueva política el 13 nov (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-11-86e40b6ap-ocia-registration-forms-update-past-registrants\|OCIA Candidate Form import]] | aprobado | 2026-11-11 | 179 respuestas (130 personas) importadas; flujo de 5 estados construido (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-11-86e40cv5h-mary-fr-ben-conversation-software-changes\|Mary / Fr. Ben → One Plan]] | realizado | 2026-11-11 | Un solo grupo Sacraments, equipos, expediente del líder, co-líderes (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-13-86e40v9gn-pdf-record-per-person-ocia-adult-formation\|PDF intake records]] | aprobado | 2026-11-13 | Paso 1: 104 expedientes OCIA en PDF (restricted) |
| [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-13-86e40ve5a-draft-ocia-follow-up-emails-in-outlook\|OCIA follow-up drafts]] | aprobado | 2026-11-13 | 33 borradores en el Outlook de ltorres@, sin enviar |

## Pendientes abiertos (según el último comentario de cada tarea)
- **Publicar y desplegar.** Publicar en Lovable lo que esté pendiente y desplegar el envío de correo (`send-queued-emails`, `send-login-code`). Esto lo hace Cristian.
- **Asistencia.** El plan del punto 5 de [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-11-05-86e3z12vb-reconcile-ocia-attendance-claims|86e3z12vb]] espera el OK de Luis: programadas vs. asistidas, lista de quienes pasan el 50 % y páginas de sesión. De los 79 que pasan el 50 %, 58 nunca asistieron. Falta pedir a Kat las fotos del 8 y 9 nov.
- **Líderes.** Faltan los emails de Jeremie, Tyler (también su apellido) y Alfred y Rebecca Tripodo. Adults 30+ B sigue sin líder y el equipo de iniciación no tiene nombre. Las invitaciones a líderes, las alertas, las preguntas a Fr. Ben y los temas menores están en espera.
- **Correos.** Luis revisa y envía los 33 borradores. Elizabeth Rodriguez no tiene email. Hay que decidir qué pasa con David Colon y Karen Reyes.
- **Expedientes PDF.** No consta entregado el paso 2 (botón "Download intake (PDF)" en el perfil).
- **Sitio parroquial.** El enlace OCIA debe apuntar al formulario de la app y hay que poner `/contact` en la web.
- **Staff y People.** Faltan el Excel de staff, el nombre del grupo admin interno, la ortografía de "Kori" y el rol de Deacon Gary.
- **Guía de líderes.** Falta la revisión de Fr. Benjamin y corregir la Pascua 2027 en el calendario (es el 28 mar).
- **Infraestructura.** Faltan las cuentas Apple Developer y Google Play, un archivo de muestra de Camino y decidir entre el calendario de salones propio y Outlook (Brandon / Visionary).
- **Preguntas a la parroquia.** El mensaje de 14 preguntas de [[01-Brands/St-Joseph/04-Projects/Parish-System/Tasks/2026-10-02-86e3j54f1-reconcile-every-project-record-sept-24-to-oct-1|86e3j54f1]] no tiene fecha de envío.
- **Fraternity BBQ.** Luis tiene que definir el acceso a SignUpGenius y pasar el correo de Miguel. Falta el formulario de voluntarios.

## Related
- [[01-Brands/St-Joseph/01-Systems/platform-dashboard-roles-and-learning-modules|Platform dashboard roles and learning modules]]
- [[01-Brands/St-Joseph/05-Operations/SOPs/Mens-Worship-Night-Coordination|SOP: Men's Worship Night coordination]]
