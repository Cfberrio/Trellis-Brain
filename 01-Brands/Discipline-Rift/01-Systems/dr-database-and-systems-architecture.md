---
brain_note_id: "note:c032b9c4-cdde-4ddb-a062-dcc674013b28"
canonical_key: "dr-database-systems-architecture"
brand_id: "discipline_rift"
---
# DR Database and Systems Architecture

## Canonical Statement

- **fact**: The Discipline Rift database was migrated in June 2026 to a secure architecture using Row Level Security (RLS) to ensure parents and coaches only access their own data.
- **rule**: The system prevents overbooking (overselling) by temporarily reserving a spot for a few minutes once a parent begins the payment process.
- **process**: Automated workflows include syncing registrations to GoHighLevel (CRM), abandoned cart reminders, and AI-generated SMS draft responses for the team to review.
- **fact**: Attendance tracking is standardized into four states: present, absent, late, and justified.
- **fact**: Sensitive documents like coach resumes and student media are stored in private folders with temporary access permissions rather than public links.

## Evidence Log

- 2026-10-17T18:51:32.400Z — `clickup_doc_page:8cqnrff-21637/8cqnrff-29397`
  - `e1` (source_body): Mudamos toda la información de Discipline Rift (padres, estudiantes, equipos, pagos, asistencia, mensajes…) de una casa vieja y desordenada a una casa nueva, ordenada y con seguridad de verdad
  - `e2` (source_body): esto NO es solo “esconder botones”. Es un candado real en la base de datos. Aunque alguien intente colarse, la base de datos le niega el acceso a lo que no es suyo.
  - `e3` (source_body): Cuando un papá empieza a pagar, el sistema le aparta el cupo por unos minutos. Si el equipo está lleno, avisa “lleno” en vez de venderlo dos veces. Adiós sobreventa.
  - `e4` (source_body): Newsletter → CRM: Cuando alguien se suscribe, lo manda al sistema de marketing (GoHighLevel). ... Borradores de SMS con IA: Lee mensajes sin responder y prepara un borrador con inteligencia artificial para que el equipo revise.
  - `e5` (source_body): La asistencia ahora distingue: presente, ausente, tarde, justificado (antes solo “sí/no”).
  - `e6` (source_body): Los documentos sensibles (currículums de coaches, fotos/videos del chat de menores) ahora están en carpetas privadas — solo se abren con un permiso temporal, no son públicas.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21637/8cqnrff-29397`
- Source hash: `2bf42cbad2d5335ffb032954c055ca44dc5c5901a8966088178764c1e83680d0`
- Observed at: 2026-10-17T18:51:32.400Z
- Agent run: `fe2e4992-a7ac-4ec9-ab25-2d0214b5ba76`
- Validation run: `c0501e05-ea4b-48b4-b234-7440ad42ee3d`
