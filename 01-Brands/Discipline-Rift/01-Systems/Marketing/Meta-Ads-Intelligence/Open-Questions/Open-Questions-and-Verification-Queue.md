---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — secciones 'Open questions' de knowledge/experts/*.md + knowledge/research-questions.md + VIDEO-MANIFEST.json"
repo_path: domains/ads/meta/intelligence
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/open-questions
  - discipline-rift
aliases:
  - "Preguntas abiertas y cola de verificación"
  - "Open Questions and Verification Queue"
  - "Qué falta en Meta Ads Intelligence"
---

# Preguntas abiertas y cola de verificación

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (el backlog formal A1–S2)]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Experiments|DR Meta Ads Experiments]]

---

> [!abstract] Para qué existe esta nota
> Todo sistema de investigación acumula deuda: cosas que se afirmaron y no se verificaron, corpus que no se terminó, auditorías que se pospusieron. Esta nota la lista completa, sin maquillar. **Si algo de aquí resulta ser distinto de lo supuesto, hay notas que cambian.**

---

## 1. Bloqueantes antes de tocar la cuenta de DR

Estas cinco se resuelven **antes** de cualquier cambio, no después.

| # | Qué verificar | Por qué bloquea | Dónde nació |
|---|---|---|---|
| **1** | **¿Existe Pixel? ¿Existe CAPI?** El grep de `fbq` / `Conversions API` en los dos repos de DR dio **cero resultados** — pero la corrección posterior estableció que **ausencia de código no prueba ausencia de integración** viva o de partner | Decide el objetivo de campaña (Wave 1A) y decide si la rama Leads→Website es siquiera construible | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget\|Wave 1B]] · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Run-2026-08-13-C1-C2-C3-C4\|parche C1–C4]] |
| **2** | **¿El bug de subida de presupuesto (2026-08-03) es real y sigue vivo?** Reportado por un operador con más de 1.400 cuentas, no confirmado por Meta, auto-reportado, y por su propia cuenta no le pegó a todas las cuentas | **Prioridad máxima: chequear antes de que DR suba cualquier presupuesto** | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Ben-Heath\|Ben Heath]] · claim BH-P3-16 |
| **3** | **La redefinición de atribución click-through / engage-through (abril 2026)** | Si se confirma, **cualquier ventana de medición de DR que cruce abril 2026 es discontinua** — no se puede comparar antes con después | Ben Heath · BH-P3-08 → verificar contra [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Optimization-Goals-and-Attribution\|Meta oficial]] |
| **4** | **¿Cuál es el volumen semanal real de DR de los eventos candidatos de optimización, por metro?** | **Todo lo estructural del corpus resuelve sobre ese número y no está en archivo.** Sin él, la discusión de estructura es teórica | Ben Heath · pregunta 4 de su corpus · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget\|Wave 1B]] |
| **5** | **¿Está el ajuste "reach more people likely to respond" en la cuenta de DR, y está activado?** | Es el único ajuste nombrado que **rompería la garantía de zona atendible** de DR | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-3-Audience-and-Measurement\|Wave 3]] · Ben Heath BH-P3-10 |

---

## 2. Verificaciones contra documentación de Meta

| # | Afirmación externa | Qué hay que hacer |
|---|---|---|
| 2.1 | **Andromeda se publicó el 2 dic 2024** (post de ingeniería de Meta leído en cámara) con rollout de ~1 año | Confirmarlo contra fuente primaria. **Resolvería la disputa de fechas del panel contra un documento**, no contra opiniones |
| 2.2 | **Agrupación por entity ID** | Sin verificar contra documentación |
| 2.3 | **Tope de 150 anuncios por ad set** | Sin verificar |
| 2.4 | **¿Meta ofrece un conversion lift study al nivel de gasto de DR?** | Determina si la capa 4 de medición de Wave 3 es siquiera accesible |
| 2.5 | **Discrepancia en la herramienta de creative testing**: la UI en vivo dice "5" anuncios, la documentación de primera mano dice "2–7" | Re-capturar y fechar |

---

## 3. Corpus sin terminar

**148 videos · 1.044.019 palabras.** Detalle por experto y los 9 IDs pendientes de Holiday: [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura]].

| Experto | Pendiente | Condición al retomarlo |
|---|---|---|
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Nick-Theriot\|Nick Theriot]] | 79 videos · 348.908 palabras | El siguiente por tamaño; el más barato de cerrar |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Andrew-Faris\|Andrew Faris]] | 60 videos · 628.633 palabras | Programa de entrevistas: **cada claim debe nombrar al hablante real**. Contrastar contra Holiday, en especial `UTgZcAbxHSw` (bid cap vs cost cap) |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Taylor-Holiday\|Taylor Holiday]] | 9 videos · 66.478 palabras | Por título parecen ecommerce y contenido de agencia — pero eso es predicción, no resultado |

---

## 4. Trabajo de síntesis pendiente

| Entregable | Qué falta |
|---|---|
| `CLAIM-AUDIT.md` | Auditar los **26 claims previos derivados de video** contra el corpus completo. Los dos casos ya auditados demostraron errores de atribución reales |
| `RUN-REPORT.md` de Phase 3 | Reporte de ejecución de la revisión completa |
| `CROSS-EXPERT-FINDINGS.md` | Hallazgos organizados **por pregunta de investigación**, no por experto — hoy la síntesis vive dispersa en 16 notas |
| Cola de validación de plataforma | Lista formal de qué claims esperan verificación contra Meta |
| Índice de videos para presentar | Cubriendo los ocho expertos con corpus |
| Reconciliar `sources-index.json` y `experts.yaml` | **Diferido a propósito** hasta el final de la corrida completa, para hacerlo en una sola pasada. Hoy los dos archivos no reflejan el estado de Phase 3 |

> [!warning] La deferral que hay que tener presente
> `sources-index.json` y `experts.yaml` **no están sincronizados con Phase 3**. Si alguien los lee como estado actual, va a subestimar el corpus. Se arreglan en una sola pasada cuando cierren los 148 videos.

---

## 5. Huecos estructurales del conocimiento

1. **Ningún miembro del panel opera un negocio como DR.** Ralph Burns es lo más cercano en amplitud fuera de ecommerce; Loomer en escala; Heath en formato local/multi-ubicación. Ninguno de los tres es DR.
2. **La evidencia local de competidores es delgada por construcción**: 16 anuncios de 2 familias, y 11 de esos 16 son un programa de bebés fuera de la banda de edad de DR.
3. **Cero DR TEST RESULT.** El sistema entero está en nivel hipótesis. Ninguna regla operativa probada existe todavía, y no puede existir hasta que corra algo en la cuenta.
4. **¿Hay un creador de actividades juveniles o audiencia de padres en el mercado de Orlando a precio viable?** Los anuncios de partnership son la recomendación convergente más fuerte del panel y **DR no tiene ninguna evidencia sobre la oferta local**.

---

## 6. La mitad del proyecto que no está construida

La investigación externa es la **Mitad 1**. Termina en hipótesis de DR, nunca en prueba.

La **Mitad 2** —no construida— valida y corrige esas hipótesis con los resultados propios de DR, sobre tres ejes que hay que chequear, nunca asumir:

- **AUDIENCIA** — ¿los anuncios están llegando a la gente correcta?
- **MENSAJE** — ¿el creativo produce la respuesta buscada en esa audiencia?
- **ESTRUCTURA** — ¿la arquitectura se comporta como predijo la investigación?

```text
investigación → hipótesis DR → campaña → datos reales de DR
   → diagnóstico de audiencia + mensaje + estructura → cambio controlado
   → DR TEST RESULT → mejor decisión siguiente
```

**El proyecto no está completo cuando existe un playbook.** Está completo cuando un sistema repetible chequea los tres ejes contra los datos propios de DR y mejora las campañas con el tiempo.
