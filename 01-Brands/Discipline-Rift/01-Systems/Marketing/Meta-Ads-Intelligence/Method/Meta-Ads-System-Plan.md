---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/PLAN.md"
repo_path: domains/ads/meta/intelligence/PLAN.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/method
  - discipline-rift
aliases:
  - "Meta Ads System Plan"
  - "Plan Meta Ads Intelligence"
---

# Meta Ads Intelligence — Plan ajustado al repo

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Operating-Rules|Reglas de operación del dominio]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-How-To-Use|Cómo usar el sistema]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitors-Index|Competidores — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/PLAN.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Fecha:** 13 de agosto de 2026
**Marca activa:** Discipline Rift (única por ahora)
**Ubicación:** `domains/ads/meta/intelligence/`

---

## 0. Qué cambia respecto al plan original

El plan original está bien pensado, pero asume un repo vacío. Este repo ya tiene la mitad construida. Estos son los recortes y por qué.

| Plan original | Ajuste | Razón |
|---|---|---|
| Repo nuevo `dr-ads-intelligence` en GitHub | Vive en `domains/ads/meta/intelligence/` | Repo separado pierde el loop con `data/raw/` de Meta y con las skills fase 2/3 que ya corren. El valor está en cruzar lo que hacen los demás con lo que muestra nuestra propia cuenta. |
| `src/ingest.ts` + `normalize.ts` + `analyze.ts` + `validate.ts` + `compare.ts` + `publish.ts` | 3 skills de Claude Code | Claude Code ya es el LLM y ya orquesta. Escribir TypeScript que llame a la API de Claude es construir un segundo sistema para hacer lo que este ya hace. |
| `ANTHROPIC_API_KEY` en `.env` | No se usa | Los tokens ya están cubiertos por la sesión. Una API key aparte es una factura nueva sin capacidad nueva. |
| `APIFY_TOKEN` en `.env` + apify-client | Apify MCP, ya conectado en `.mcp.json` | Ya está autenticado por OAuth. No hay que gestionar token. |
| `npm install apify-client @anthropic-ai/sdk dotenv yaml zod` | Nada que instalar | Sin código, sin dependencias, sin `package.json`. |
| Apify Google Search Scraper para discovery | `WebSearch` nativo | Discovery de artículos y videos por keyword sale gratis con la herramienta nativa. Apify se reserva para lo que la herramienta nativa no puede: Ad Library, transcripts de Reels, transcripts de YouTube. |
| `apify/website-content-crawler` para artículos | `WebFetch` nativo | Mismo motivo. Gratis y suficiente para blogs y landing pages. |
| `config/dr-context.md` nuevo | Reusar `domains/ads/meta/discipline-rift/CLAUDE.md` | Ese archivo ya define avatar, oferta real, los 3 deliverables, claim rules y lenguaje prohibido. Escribir un segundo contexto de DR garantiza que se desincronicen. |
| Dos sistemas de scoring (30 pts y 14 pts) | Uno solo: 14 pts | El plan tenía los dos. Se queda el de 14. |
| Schedules + webhooks de Apify desde el principio | Manual, revisión mensual | Automatizar antes de saber si el output sirve es gastar en algo que quizá no queremos repetir. |
| Ad Library como Fase 9 / Fase 16 | Ad Library como **pilar 1** | Corrección de prioridad: el objetivo es extraer lo que corren los demás. La biblioteca de expertos es soporte, no el centro. |

**Lo que se mantiene íntegro del plan original:** el schema de claims, la verificación contra documentación oficial de Meta, el consensus engine, la capa de aplicabilidad a DR, el scoring, el control de recencia, y la lista de lo que NO vamos a hacer.

---

## 1. Qué es esto y qué NO es

**Ya tenemos** `domains/ads/meta/discipline-rift/` — fases 1-2-3. Eso mira **nuestra propia cuenta**: extrae, diagnostica, produce SOP de rehab.

**Esto es lo contrario:** mira **hacia afuera**.

```
discipline-rift/     →  qué está pasando en NUESTRA cuenta
intelligence/        →  qué están corriendo LOS DEMÁS + qué dice Meta + qué dicen expertos
```

Son dominios separados a propósito. No se tocan los archivos de fases 1-3.

El punto de unión es uno solo y es el que da el valor:

```
intelligence/output/dr-playbook.md
        ↓
   se lee como input en la fase 3 (campaign rehab)
        ↓
   los cambios propuestos dejan de ser "lo que dice el diagnóstico"
   y pasan a ser "lo que dice el diagnóstico + lo que ya funciona afuera"
```

---

## 2. Los dos pilares

### Pilar 1 — Competitor Ad Extraction (prioridad)

Sacar de Meta Ad Library los anuncios que corren competidores y marcas análogas, y detectar patrones:

- oferta visible
- hook de primeros 3 segundos
- ángulo (conveniencia, precio, seguridad, resultado, identidad)
- CTA
- formato (video / imagen / carousel)
- **días que lleva corriendo el anuncio** ← la señal más importante
- cuántas variaciones tiene activas la misma marca
- landing page a la que mandan

**Por qué "días corriendo" es la señal:** Ad Library no da gasto ni conversiones para anuncios comerciales normales. Pero un anuncio que lleva 90 días activo casi seguro está funcionando — nadie quema presupuesto tres meses en un creative muerto. Longevidad es el proxy de performance disponible públicamente.

Lo que NO vamos a afirmar: cuánto venden, cuánto gastan, cuál es su CPA. Ad Library no lo da y inventarlo destruye la credibilidad del sistema.

### Pilar 2 — Public Knowledge (soporte)

Expertos públicos + documentación oficial de Meta, para saber si un patrón que vemos es táctica válida o vicio heredado.

Sin este pilar, el pilar 1 se convierte en "copiemos al competidor" — que es exactamente cómo se propagan las malas prácticas.

---

## 3. Estructura de carpetas

```
domains/ads/meta/intelligence/
│
├── CLAUDE.md                       # contexto del dominio (reglas de operación)
├── PLAN.md                         # este archivo
├── README.md
│
├── config/
│   ├── competitors.yaml            # marcas a vigilar en Ad Library
│   ├── experts.yaml                # 4-6 expertos, no más
│   └── keywords.yaml               # queries de discovery
│
├── inbox/
│   └── urls.json                   # cualquiera del equipo pega una URL aquí
│
├── data/
│   ├── raw/                        # dumps crudos de Apify (fecha + fuente)
│   └── index.json                  # URLs ya procesadas → dedup
│
├── competitors/
│   ├── ads/                        # un .md por marca vigilada
│   └── patterns.md                 # patrones repetidos entre marcas
│
├── knowledge/
│   ├── official-meta/              # documentación oficial resumida
│   ├── experts/                    # un .md por experto
│   └── topics/                     # un .md por tema (consenso + conflictos)
│
└── output/
    ├── dr-playbook.md              # ← el archivo maestro
    ├── experiments.md              # ← lo que hay que probar
    └── briefs/
        └── YYYY-MM-DD-brief.md     # brief periódico
```

Sin base de datos. Markdown + JSON + Git es suficiente y hace el historial auditable con `git log`.

---

## 4. Las 3 skills

Siguen la convención que ya usa el repo (`ads-meta-dr-phase1-extract`, etc.).

### `ads-meta-intel-adlib` — Competitor sweep

**Input:** `config/competitors.yaml`
**Proceso:** Apify Ad Library actor → dump a `data/raw/` → extracción de patrones
**Output:** `competitors/ads/<marca>.md` + `competitors/patterns.md`

Cada anuncio queda registrado así:

```yaml
advertiser:
ad_id:
first_seen:
days_running:
format:            # video | image | carousel
hook:              # primera línea / primeros 3s
offer:
angle:
cta:
landing_page:
active_variations: # cuántas versiones corre la misma marca
captured_at:
```

Y el output agregado responde: qué ángulos sobreviven más tiempo, qué ofertas se repiten entre marcas independientes, qué formato domina, qué hooks se repiten.

### `ads-meta-intel-ingest` — Conocimiento público

**Input:** `inbox/urls.json` o una URL suelta
**Proceso:** detecta el tipo de fuente y enruta

```
instagram.com/reel  → Apify (caption + transcript)
youtube.com/watch   → Apify (metadata + subtítulos)
facebook.com/ads/library → deriva a ads-meta-intel-adlib
cualquier otra      → WebFetch nativo
```

**Output:** claims estructurados en `data/raw/` + actualiza `knowledge/experts/<nombre>.md`

Antes de procesar, chequea `data/index.json`. Si la URL ya está, se detiene. No se procesa nada dos veces.

### `ads-meta-intel-playbook` — Validación + adaptación a DR

**Input:** todo lo anterior + `domains/ads/meta/discipline-rift/CLAUDE.md` + últimos outputs de fase 2
**Proceso:**

1. Agrupa claims por tema
2. Contrasta cada claim contra `knowledge/official-meta/` → `SUPPORTED / PARTIALLY_SUPPORTED / CONFLICTING / OUTDATED / INSUFFICIENT_EVIDENCE`
3. Compara entre expertos → consenso y desacuerdos
4. Cruza con `competitors/patterns.md` → ¿lo que dicen coincide con lo que corren?
5. Traduce a DR: local, on-campus, padres de kids 6-12, KPI real = registro completado
6. Puntúa (ver §6)

**Output:** `output/dr-playbook.md` + `output/experiments.md`

La pregunta que este archivo debe responder en una pantalla:

> Si hoy tuviéramos que reconstruir las campañas de DR, ¿qué haríamos y por qué?

---

## 5. Actors de Apify — verificado en Store hoy

### Ad Library

| Actor | Precio | Nota |
|---|---|---|
| `apify/facebook-ads-scraper` | $0.0058 / anuncio | Oficial de Apify, 31.8k usuarios, rating 4.19. Default seguro. |
| `brilliant_gum/facebook-ads-library-scraper` | $0.015 / anuncio | El único que reporta explícitamente **días corriendo**. Más caro pero da la señal que más nos importa. |
| `memo23/facebook-ads-library-scraper-ppe` | $0.0005 / result + $0.05 start | Schema más rico, incluye reach EU. Barato a volumen. |

**Decisión:** arrancar con `apify/facebook-ads-scraper` (oficial, estable). Si el campo de duración no viene utilizable, probar `brilliant_gum`. La skill debe tener un adapter — nunca depender del formato exacto de un actor de terceros.

**Costo estimado del sweep mensual:** 15 competidores × 40 anuncios = 600 anuncios ≈ **$3.50/mes** con el actor oficial. El free tier de Apify ($5/mes de crédito) cubre el MVP entero.

### Instagram y YouTube

`apify/instagram-scraper` para Reels. Para YouTube usar un actor con subtítulos. En ambos casos, adapter propio: el output se normaliza al mismo schema antes de tocar nada más.

---

## 6. Scoring — una sola escala

```
Meta oficial lo respalda        0-3
Varios expertos coinciden       0-3
Publicación reciente            0-2
Relevante para DR               0-3
Calidad de evidencia            0-3
                        TOTAL: 14
```

```
12-14 → HIGH PRIORITY   (adoptar)
 8-11 → TEST            (experimento con control)
 5-7  → WATCH           (registrar, no actuar)
 0-4  → IGNORE
```

Todo claim guarda `published_at`, `captured_at`, `last_verified_at`. Sin fecha, no entra.

---

## 7. Qué NO se toca

- Los tres skills de Google Ads OEV (`google-ads-phase*`)
- Los tres skills de Meta DR (`ads-meta-dr-phase*`)
- `domains/ads/meta/discipline-rift/` — data, output, scripts, CLAUDE.md
- Raíz del repo

Todo lo nuevo vive dentro de `domains/ads/meta/intelligence/` y en tres archivos de skill nuevos.

**Un arreglo pendiente:** `.claude/rules/ads/meta.md` dice *"Scaffold stage. No active pipeline yet"*. Eso quedó desactualizado — el pipeline de DR lleva meses corriendo. Hay que corregirlo y añadir la sección de intelligence.

---

## 8. Orden de construcción

### Sprint 1 — Competitor sweep (el que da valor primero)

1. Escribir `config/competitors.yaml` con las marcas reales a vigilar
2. Crear skill `ads-meta-intel-adlib`
3. Correr un sweep contra 5 competidores
4. Revisar: ¿los patrones que salen sirven para decidir algo?

**Criterio de corte:** si el output del sweep no cambia ninguna decisión de creative, el sistema no se construye más.

### Sprint 2 — Conocimiento público

5. `config/experts.yaml` — 4-6 personas
6. Crear skill `ads-meta-intel-ingest`
7. Procesar 15 fuentes: 5 Reels, 5 YouTube, 5 artículos
8. Poblar `knowledge/official-meta/` con la documentación oficial

### Sprint 3 — Playbook

9. Crear skill `ads-meta-intel-playbook`
10. Generar el primer `dr-playbook.md` y `experiments.md`
11. Correr el primer experimento en la cuenta real

### Sprint 4 — Cierre del loop

12. Conectar `dr-playbook.md` como input opcional de `ads-meta-dr-phase3-campaign-rehab`
13. Registrar resultados reales de los experimentos en `output/`

### Sprint 5 — Solo si los sprints 1-4 demostraron valor

14. Discovery recurrente con WebSearch
15. Cadencia programada

---

## 9. Cadencia

| Ritmo | Qué | Cómo |
|---|---|---|
| Cuando aparece algo | Alguien pega URL en `inbox/urls.json` | Manual |
| Mensual | Competitor sweep + regenerar playbook | Se engancha al ciclo mensual que ya corre en `social-metrics` |
| Trimestral | Revisar documentación oficial de Meta por cambios | Manual |

Nada diario. El conocimiento de plataforma no cambia todos los días y procesarlo a diario solo produce ruido.

---

## 10. Primera prueba real

15 fuentes de conocimiento + 5 competidores. Y responder:

1. ¿Los patrones de competidores sirven para decidir un creative concreto?
2. ¿Puedo rastrear cada afirmación hasta su fuente?
3. ¿El sistema distingue opinión de experto vs. regla oficial de Meta?
4. ¿Detecta cuando un experto contradice a Meta?
5. ¿Traduce correctamente ecommerce → programa local after-school?
6. ¿Los experimentos que propone son experimentos que realmente queremos correr?

Si la respuesta a la 1 y la 6 es no, no se sigue construyendo.

---

## 11. Límites

- Solo información pública. Nada de cursos pirateados, contenido privado, paywalls, ni evasión de logins.
- Ad Library no da gasto ni conversiones de anuncios comerciales normales. No se infiere ninguna de las dos.
- Longevidad de un anuncio es un proxy, no una métrica. Se etiqueta como proxy.
- Una estrategia de ecommerce no se copia a DR sin marcarla como `applicability: high | medium | low` y `modification_required: yes | no`.
- No guardar transcripts que nadie va a convertir en decisión.
- Si el sistema solo produce material de lectura, falló.

---

## Bottom line

El plan original construye una máquina de investigación desde cero. Este repo ya tiene la mitad: el LLM, el scraper, el contexto de marca, la data real de la cuenta, y las skills que convierten diagnóstico en SOP.

Lo que falta es la mirada hacia afuera y el archivo que responde qué hacer.

Eso son tres skills y una carpeta. No un repo, no un pipeline de TypeScript, no una API key nueva.
