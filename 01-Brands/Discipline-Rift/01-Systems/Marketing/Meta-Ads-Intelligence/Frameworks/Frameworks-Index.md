---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: index
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/wave-*.md (5 frameworks, 2026-08-13 / 2026-08-14)"
repo_path: domains/ads/meta/intelligence/output
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: index
tags:
  - meta-ads
  - meta-ads/framework
  - meta-ads/index
  - discipline-rift
aliases:
  - "Frameworks — índice"
  - "Waves 1A-3"
  - "Meta Ads Frameworks"
---

# Frameworks — índice de las cinco olas

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (el backlog que estas olas responden)]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-Structure-Full-Method|Método completo de estructura DR]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas]]

---

> [!danger] Nivel de conocimiento de las cinco: **DR HYPOTHESIS**
> Construidas sobre PLATFORM FACT + EXTERNAL PRACTITIONER CLAIM + hechos de contexto de DR.
> **Nada aquí está probado para DR.** Ninguna campaña, ad set, anuncio, presupuesto, targeting, placement, Pixel ni CAPI ha sido modificado o creado.

Las olas se encadenan: cada una hereda los supuestos de la anterior por escrito y entrega un contrato de entrada a la siguiente. Ninguna podía empezar sin que la previa entregara sus supuestos.

```text
1A objetivo/evento → 1B volumen/presupuesto → 2A arquitectura → 2B creativo → 3 audiencia/medición
```

---

## Wave 1A — Objetivo y evento de optimización

[[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1A-Objective-and-Optimization-Event|Abrir framework]] · Preguntas **A1** (objetivo) · **A2** (evento de optimización) · **A3** (calidad vs cantidad) · 2026-08-13, revisado v2 el mismo día

**Resultado:** el objetivo quedó **condicional, no cerrado**. Sales→Website es la lectura actual; Leads→Website depende de requisitos que DR no ha auditado.

Cuatro cosas siguen sin establecerse y **las cuatro deciden el objetivo**: dónde se completa el registro; con qué frecuencia; si existe CAPI; y si hay un CRM con etapas de registro que pueda sincronizar de vuelta.

> [!bug] Esta ola pasó por una corrección de seis errores materiales
> La v1 tenía seis errores de interpretación que la auditoría encontró y la v2 corrigió — entre ellos que **sí existe** una palanca de calidad del lado de plataforma para embudos web (lo que reabrió el objetivo Leads y eliminó la respuesta única de v1), que el gating de datos de menores **no es permisible como estaba diseñado** bajo los Business Tools Terms, y que **el objetivo de una campaña publicada no se puede cambiar en absoluto** — requiere campaña nueva. La lista completa está al inicio de la nota.

---

## Wave 1B — Volumen y viabilidad de presupuesto

[[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget|Abrir framework]] · Preguntas **B1** (volumen de eventos) · **B2** (viabilidad de presupuesto) · **B3** (aprendizaje a bajo volumen) · 2026-08-13

**El hallazgo que más cambió el proyecto** salió de una inspección read-only del frontend de DR y del repo de automatización:

- Registro y pago **se completan online en la misma sesión** (Supabase escribe `parent/student/enrollment` en el paso 4, Stripe Checkout en el paso 6).
- **Supabase es el único sistema de registro.** No hay CRM separado.
- **No existe implementación de Pixel ni de Conversions API en el código.** Se buscó `fbq`, `facebook pixel`, `Conversions API`, `CAPI` en ambos repos: cero resultados.

Eso es más fuerte que "salud de CAPI desconocida": la infraestructura base de tracking para Meta **parece ausente, no solo sin verificar**. Consecuencia directa: la rama Leads→Website **no es construible hoy**, y la ola opera sobre **Sales → Website**.

Sobre el umbral de 50: la condición real de salida del aprendizaje es *"deliver stably"*; los ~50 eventos son la descripción de Meta de cuándo eso **suele** pasar — no una regla, no un acantilado. Y entregar por debajo del umbral **no es una penalización**: el costo es menos estabilidad y normalmente mayor CPA, no descalificación.

---

## Wave 2A — Arquitectura de campaña

[[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2A-Campaign-Architecture|Abrir framework]] · Preguntas **C1** (número de campañas) · **C2** (dónde va el presupuesto) · **C3** (separar testing y scaling) · **C4** (disparadores de revisión) · 2026-08-14

```text
Campañas:                 1
Rol de la campaña:        una sola campaña de adquisición — sin división de roles
Ad sets:                  1 (estado actual, no un techo)
Presupuesto:              se queda a nivel ad set — hoy no hay razón para moverlo
Testing vs scaling:       sin campañas separadas
Confianza:                C1 ALTA · C2 MEDIA (bajo riesgo) · C3 ALTA · C4 MEDIA
```

**La salida más valiosa de esta ola es una prohibición, no una construcción.** Toda elaboración disponible a nivel campaña —segunda campaña, campaña de escala, campaña de retargeting, asignación de presupuesto a nivel campaña— o exige una condición que DR no cumple, o divide señal que DR no tiene.

Y un matiz honesto sobre C2: **con un solo ad set la decisión de dónde va el presupuesto es casi inerte**. Los criterios de Meta para elegir entre los dos modos son todos comparaciones *entre* ad sets, y no hay un segundo ad set que comparar.

---

## Wave 2B — Método creativo operativo

[[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Abrir framework]] · Preguntas **D1** · **D2** · **D3** · **D4** · 2026-08-14

```text
Dónde entra la creatividad:  al ad set existente. No construir un segundo ad set para testear
Creativos por ronda:         2–3, como HIPÓTESIS INICIAL de baja complejidad — no un óptimo probado
Cómo entran:                 toda la ronda en UNA sola sesión de edición (un reinicio de aprendizaje,
                             no N). La creatividad es lo único que cambia esa sesión
Cadencia:                    sin calendario fijo y SIN umbral universal de días. Se revisa cuando el
                             período fue técnicamente limpio y hay entrega suficiente para clasificar
Regla de corte:              cuatro tipos de kill — técnico, de política, dominado, downstream
Regla de conservación:       se conserva por defecto mientras el anuncio sea NOT_EVALUABLE
Sin gasto:                   árbol de diagnóstico de 5 ramas ANTES de juzgar el creativo
```

Lo importante: **"no hay evidencia suficiente" es un veredicto válido y esperado, no un fracaso.** Ausencia de evidencia no es evidencia de debilidad. Y la entrega desigual entre anuncios es comportamiento **documentado como normal** por Meta —el *breakdown effect*—, no un veredicto sobre el creativo.

---

## Wave 3 — Audiencia, geografía, atribución y medición

[[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-3-Audience-and-Measurement|Abrir framework]] · Preguntas **E1** · **E2** · **E3** · **G1** · **G2** · 2026-08-14

```text
Audiencia:      Advantage+ audience con Ubicación como CONTROL DURO
                Sin intereses / detailed targeting. Edad mínima adulta como control
                "Reach more people likely to respond" = OFF — es el único ajuste nombrado
                que rompería la garantía de zona atendible de DR
Controles duros: Ubicación · edad mínima (comprador adulto) · EXCLUSIONES de custom audience
Geo:            UN ad set con la UNIÓN de radios cerrados alrededor de cada campus activo
                — no una selección de ciudad completa, y no un ad set por colegio
Targeting vs mensaje: los AJUSTES imponen geografía atendible y comprador adulto.
                El MENSAJE califica colegio, deporte, edad, formato, horario y precio.
                La creatividad provoca autoselección; NO puede imponer ni verificar nada
Atribución:     modelo estándar · 7 días clic · 1 día visualización · engage-through OFF
                7 días clic es la ventana MÁS LARGA que Meta ofrece hoy para conversiones web
                — es un techo de plataforma, no una convención copiada
Medición:       4 capas — 1 entrega · 2 creativo/mensaje · 3 respuesta calificada · 4 registro pagado
```

**Múltiples ubicaciones en un ad set no son múltiples ad sets.** Ese es el punto que evita fragmentar la señal por colegio. La verdad del negocio vive en la base de datos de DR, no en el reporte de Meta — Meta mide publicidad, no es el libro contable.

---

## Cómo se usan estas cinco

1. Para **ejecutar**, no leas las olas: lee [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-Structure-Full-Method|el método completo]] o el [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|Playbook]].
2. Para **entender por qué** una decisión es esa, entra a la ola correspondiente: cada una trae la evidencia y **qué observación la desmentiría**.
3. Para **reabrir** una decisión, revisa los disparadores de revisión de C4 y el `stop_condition` de la pregunta en el [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|backlog]].
