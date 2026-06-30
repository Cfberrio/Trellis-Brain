---
brand: Discipline-Rift
area: systems
note_type: project
status: active
canonical: true
used_for_ai: true
owner: Domis
last_updated: 2026-06-19
sensitivity: internal
hub_role: migration-hub
aliases:
  - DR Backend Migration
  - DR Lovable Migration
---

# DR Backend Migration (Supabase viejo → Lovable Cloud)

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Systems-Home|DR Systems Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/DR-Shared-Entities-and-Integrations|DR Shared Entities and Integrations]]
- [[01-Brands/Discipline-Rift/01-Systems/DR-Operational-Flows|DR Operational Flows]]
- [[01-Brands/Discipline-Rift/01-Systems/Parent-App-Home|DR Parent App Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Coach-Portal-Home|DR Coach Portal Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Admin-Operations-App-Home|DR Admin Operations App Home]]

## What this is
Migración del backend de Discipline Rift desde el Supabase viejo (`tdyyjoyotvzgbeowtlfv`, "Program Website") hacia **Lovable Cloud** (Supabase por debajo). Doc técnico detallado vive en el repo local: `~/Documents/DISCIPLINERIFT/DR-Migration-Plan.md` + `migration/*.sql`. Esta nota es el resumen canónico en el vault.

## Decisión de arquitectura (2026-06-19)
**Monolito, un dominio:** `disciplinerift.com` con todo separado por rutas en UN solo proyecto Lovable:
- `/` → sitio marketing
- `/admin` → reemplaza el backend admin (admindr.disciplinerift.com)
- `/coach` → reemplaza la app de coach
- portal parent → ruta
- Una sola DB Cloud, acceso por rol vía RLS.

**IDs:** Lovable nuevo `DISCIPLINERIFT` = `d555121b-31c3-4c00-96a8-7ac15612143e` (workspace `2CH8YJC1AgAWMYWp2SCc`). Supabase viejo ref `tdyyjoyotvzgbeowtlfv`. DB Cloud nueva: **aún no prendida** (se revisa el DDL primero).

## Modelo de auth (resuelto, verificado en data)
- Todos loguean por **email + OTP**. Roles en tabla `user_role` (data, no allowlist).
- Verificado en viejo: `parent.parentid` == `auth.users.id` en 664/674 (98.5%); `staff.id` == `auth.users.id` en 22/24. **El login ya está linkeado por UUID.**
- **Migración clave:** se copia `auth.users` viejo→nuevo preservando el UUID → los ~674 padres NO se re-registran (entran con email+OTP y el sistema los reconoce, ven a sus hijos).
- Coach: Domis los crea en Users (Lovable). Admin: `admin@disciplinerift.com` (cambiar password tras setup).

## Cambios de DB principales
- snake_case en todo; renames: `staff`→`coach`, `assistance`→`attendance`, `Newsletter`→`newsletter`, `Drteam`→`coach_application`, `Partners_Program`→`partners_program`.
- State machines (enums): payment (Stripe webhook = fuente verdad), enrollment, attendance (present/absent/late/excused).
- Multi-brand día 1: tabla `brand` (DR/OEV/RV/CTS) + `brand_id`.
- Skills & Tiers reales (`tier`/`skill`/`student_skill_status`) → desbloquea feature de padres.
- Coupon mejorado, waitlist, cart multi-hijo.
- Anti-sobreventa: `seat_hold` + `reserve_seat()` con row-lock (REG1).
- Idempotencia webhooks (`webhook_event`), audit_log + consent (menores), job_registry.
- RLS por rol (parent ve su familia, coach su equipo, admin todo), índices en todos los FKs, soft-delete `deleted_at`.

## Seguridad — corregir
- 🔴 RLS off en ~20 tablas PII (se activa en Fase D, tras ETL).
- 🔴 Secretos en texto plano en `cron.job` (x-dr-secret, Bearer GHL, anon JWT) → rotar + Vault al cutover.
- ⚠️ Buckets `resume`/`attachements` públicos → privados + signed URLs.
- ⚠️ RPC SECURITY DEFINER ejecutables por anon → invoker/revoke.
- ⚠️ OTP expiry inconsistente → fijar 10 min. Leaked-password protection ON. Upgrade Postgres.

## Plan por fases
- **Fase A** — Diseño esquema limpio (DDL) — ✅ escrito (`01_schema.sql`), pendiente revisión.
- **Fase B** — RLS diseñado (`02_rls.sql`) — ✅ escrito, se activa en Fase D.
- **Fase C** — ETL viejo→nuevo (`03_etl.sql`) + migrar auth.users — ⏭️ siguiente.
- **Fase D** — Validar + activar RLS + testear por rol.
- **Fase E** — Recrear automatización: 7 edge functions, crons (+ `release_expired_holds` cada 5min), triggers de negocio, secrets→Vault, webhooks GHL/Meta/Claude.
- **Fase F** — Cutover: apuntar web/integraciones al nuevo, rotar secretos viejos.

## Inventario viejo (verificado 2026-06-19)
23 tablas · 17 funciones · **7 edge functions** · **3 cron jobs activos** · 3 buckets. (El doble-trigger de Newsletter y el cron roto del plan original YA estaban arreglados.)

## Backlog diferido (Fase 2/3)
notification_preferences · session_note · contenido marketing editable · referral · comms templates/send_log · payments upgrade · certificados desde skills. Detalle: `migration/DEFERRED-phase-2-3.md` en el repo.

## Estado / próximo paso
DDL (schema + RLS) escrito y aprobado en concepto. **Próximo:** escribir el ETL (`03_etl.sql`) — mapeo viejo→nuevo + migrar `auth.users` con UUID intacto. NO prender la DB hasta validar. Documentar sobre la marcha aquí.


---

## ✅ Migración core EJECUTADA (2026-06-19)
DB Lovable prendida (`d555121b`). Schema + data + auth + RLS aplicados y validados vía Lovable MCP (postgres_fdw del nuevo al viejo, luego limpiado).

- **Schema:** 33 tablas · 9 enums · 39 funciones · 4 brands (DR/OEV/RV/CTS).
- **Auth:** 763 auth.users migrados con UUID intacto + 763 identities. **674/674 padres con login + rol** (9 pre-creados con su parentid + 1 reconciliado por email). 22 coaches con login (faltan 2 por crear).
- **Data:** todas las tablas 1:1 vs viejo (parent 674, student 794, enrollment 1320, payment 1168, attendance 3528, message 951…). **Cero huérfanos** (integridad referencial perfecta).
- **RLS:** 33/33 tablas ON con políticas por rol.

### Falta (Fase E + F)
- Recrear 7 edge functions + triggers de negocio + crons (incl `release_expired_holds` 5min) + secrets a Vault.
- Crear admin `admin@disciplinerift.com` + rol admin. Crear 2 coaches sin auth.
- Buckets privados (resume/attachements). Construir las apps por rutas (/admin, /coach, parent).
- Cutover + rotar secretos viejos (x-dr-secret, Bearer GHL, anon JWT) + password DB vieja.


## ✅ Fase E avanzada — automatización (2026-06-19)
Proyecto nuevo Supabase ref `hvgcxtawrditxvgvqfxb`. Edge base `https://hvgcxtawrditxvgvqfxb.supabase.co/functions/v1/`.

- **7 edge functions deployadas** (vía agente Lovable), adaptadas al schema nuevo + mejoradas, dormidas hasta poner secrets: dr_ghl_newsletter, dr_ghl_registered, dr_ghl_abandoned_cron, get_reminders_t24, ghl-sms-cleanup, meta-webhook, ghl-sms-draft.
- **Triggers** newsletter→edge y payment(paid)→edge (leen DR_EDGE_SECRET del Vault, no hardcoded). **increment_student_level** portado (dispara con status='paid').
- **4 crons**: release_expired_holds */5 (activo ya), dr_ghl_abandoned_cron */30, ghl_sms_draft_dr */2, ghl_sms_cleanup_dr 9am.
- **Admin** operativo: admin@disciplinerift.com (rol admin). Todos los coaches con login.

### Falta para activar
- Poner secrets en Lovable (Project Settings → Secrets): DR_EDGE_SECRET (ya generado) + GHL token/webhooks + Anthropic key + Meta/IG tokens. Lista: `migration/SECRETS-shopping-list.md`.
- SEC3 buckets privados. Construir apps por rutas (/admin, /coach, parent). Fase F cutover.


## ✅ Storage + SEC3 + automatización LIVE (2026-06-19)
- **Automatización LIVE:** Domis puso 6 secrets (DR_EDGE_SECRET, ANTHROPIC, GHL token + 3 webhooks). Newsletter probado end-to-end (trigger→edge→GHL 200). 6/7 functions operativas. Solo Meta/IG dormido.
- **Storage migrado:** buckets nuevos (team-logo público, resume/attachements privados) + RLS. 81 logos + 37 adjuntos copiados old→new (resumes eran base64 en DB). 0 archivos rotos, 0 refs al viejo. SEC3 cerrado.

### BACKEND = COMPLETO
schema + data + auth + RLS + automatización + storage. **Falta:** construir apps frontend (/admin, /coach, parent), secrets Meta/IG, Fase F cutover (dominio + rotar secretos viejos + borrar proyecto viejo).
