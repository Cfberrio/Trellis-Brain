---
brain_note_id: "note:10e051f1-a0ba-413e-bf82-e84742e1acb5"
canonical_key: "dr-dashboard-guide"
brand_id: "discipline_rift"
---
# Discipline Rift Dashboard Guide

## Canonical Statement

- **definition**: The DisciplineRift Dashboard is a central administration panel used to manage school sports programs, including schools, services (volleyball, tennis, pickleball), practice schedules, coaches, student registrations, and parent communication.
- **fact**: The system uses a hierarchical data structure: School > Service/Program > Section (schedule) > Session (individual class) > Enrollment > Staff > Parent.
- **process**: The dashboard automates session creation based on repetition patterns (weekly, bi-weekly, monthly) and handles automated reminders for coach attendance and student absences.
- **fact**: The platform integrates with GoHighLevel (GHL) for CRM synchronization and uses Supabase for secure administrator-only authentication.

## Evidence Log

- 2026-10-17T15:52:14.817Z — `clickup_doc_page:8cqnrff-21297/8cqnrff-28777`
  - `e1` (source_body): Es un panel de administración (dashboard) donde el equipo de DisciplineRift gestiona todo su negocio de programas deportivos escolares: las escuelas, los programas (voleibol, tenis, pickleball), los horarios de prácticas, los entrenadores, los estudiantes inscritos, la comunicación con los padres
  - `e2` (source_body): Conceptos clave que debes conocer... Escuela, Servicio / Programa, Sección, Sesión, Inscripción, Staff / Entrenador, Padre / Tutor.
  - `e3` (source_body): el sistema crea solo todas las clases individuales (cada lunes y miércoles de ese rango). No hay que escribirlas una por una.
  - `e4` (source_body): Recordatorios automáticos: detecta qué coaches no han registrado la asistencia de hoy y les envía un recordatorio... detecta estudiantes que faltaron y avisa amablemente a sus padres.
  - `e5` (source_body): Sincronización con GoHighLevel (GHL): Esta sección copia los contactos de los padres desde DisciplineRift hacia GHL.
  - `e6` (source_body): La identidad se valida con un servicio profesional en la nube (Supabase)... solo las personas previamente registradas como administradores pueden entrar.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21297/8cqnrff-28777`
- Source hash: `bed5a2684a150629f4b374dbdd085e7fac038e347eea6c5b8ab13108035abbc2`
- Observed at: 2026-10-17T15:52:14.817Z
- Agent run: `07ecfe11-26d1-4ad2-aeea-0044cbe05661`
- Validation run: `c1adc79d-69ac-4244-b3ea-45b1711f4bf9`
