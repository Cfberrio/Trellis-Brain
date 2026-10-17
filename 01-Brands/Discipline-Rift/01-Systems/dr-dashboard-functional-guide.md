---
brain_note_id: "note:7951b8cd-7d3a-44ef-893a-de7bbc9ddf4f"
canonical_key: "dr-dashboard-functional-guide"
brand_id: "discipline_rift"
---
# DR Dashboard Functional Guide

## Canonical Statement

- **definition**: The Discipline Rift Dashboard is a central administration panel used to manage school sports programs, schedules, coaches, student registrations, and parent communication (Email/SMS).
- **fact**: The system hierarchy is organized into Schools, Services (sports programs), Sections (specific schedules), and Sessions (individual classes).
- **process**: The dashboard automates session creation based on repetition patterns (weekly, bi-weekly, monthly) and handles automated reminders for coach attendance and student absences.
- **fact**: The platform integrates with GoHighLevel (GHL) for CRM synchronization and uses Supabase for secure, role-based administrator access.
- **process**: Marketing features include personalized Email/SMS campaigns using variables (e.g., {studentName}) and a newsletter module with multiple SMTP server options.

## Evidence Log

- 2026-10-17T18:47:04.872Z — `clickup_doc_page:8cqnrff-21357/8cqnrff-29057`
  - `e1` (source_body): Es un panel de administración (dashboard) donde el equipo de DisciplineRift gestiona todo su negocio de programas deportivos escolares: las escuelas, los programas (voleibol, tenis, pickleball), los horarios de prácticas, los entrenadores, los estudiantes inscritos, la comunicación con los padres
  - `e2` (source_body): Conceptos clave que debes conocer... Escuela | Servicio / Programa | Sección | Sesión | Inscripción | Staff / Entrenador | Padre / Tutor
  - `e3` (source_body): el sistema crea solo todas las clases individuales (cada lunes y miércoles de ese rango). No hay que escribirlas una por una.
  - `e4` (source_body): Recordatorios automáticos: detecta qué coaches no han registrado la asistencia de hoy y les envía un recordatorio... detecta estudiantes que faltaron y avisa amablemente a sus padres.
  - `e5` (source_body): Sincronización con GoHighLevel (GHL): Esta sección copia los contactos de los padres desde DisciplineRift hacia GHL.
  - `e6` (source_body): La identidad se valida con un servicio profesional en la nube (Supabase), igual que hacen los bancos y apps modernas.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21357/8cqnrff-29057`
- Source hash: `39898f9385abed5735c199154ab9893962a96d05ceecab8c2193eca817f92393`
- Observed at: 2026-10-17T18:47:04.872Z
- Agent run: `c964272b-053c-4e2f-89ac-620cb6322b56`
- Validation run: `ca074516-2c7a-4b27-8a44-387934834bc9`
