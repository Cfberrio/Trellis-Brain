---
brand: Trellis-Core
area: system
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: curated
sensitivity: internal
last_updated: 2026-09-09
up:
  - "[[00-Trellis-Core/Trellis-Home]]"
---

# Obsidian Setup

## Parent
- [[00-Trellis-Core/Trellis-Home|Trellis Home]]

## Purpose
Dejar tu Obsidian igual al del resto del equipo: mismos plugins, mismos colores, mismos íconos.

Son 4 pasos y toma unos 5 minutos. No hay que editar ningún archivo a mano.

---

## Paso 1 — Bajá el vault

```
git pull
```

Esto ya te trae las notas **y** la configuración lista para aplicar.

---

## Paso 2 — Instalá los plugins

En Obsidian: **Settings → Community plugins → Browse**.

Buscá cada uno por nombre, **Install** y después **Enable**:

| Plugin | Autor |
|---|---|
| Local REST API | Adam Coddington |
| Breadcrumbs | SkepticMystic |
| Juggl | Emile van Krieken |
| Excalidraw | Zsolt Viczian |
| Advanced Canvas | Developer-Mike |
| Portals | samaraliwarsi |
| myBrain | CarlB01 |

> **Local REST API**: entrá a sus ajustes y generá tu propia API key. Es personal, no se comparte con nadie.

---

## Paso 3 — Cerrá Obsidian y corré el prompt

**Primero cerrá Obsidian completo con `Cmd+Q`** (o `Ctrl+Q` en Windows). No alcanza con cerrar la ventana.

> Esto no es opcional. Con Obsidian abierto, los plugins reescriben su propia configuración encima de la nueva y no se aplica nada. No aparece ningún error: simplemente no funciona.

Ahora abrí **Claude Code** en la carpeta del vault y pegá esto:

```
Aplicá la configuración de Obsidian de este vault siguiendo el mapa que está en
00-Trellis-Core/Obsidian-Config/INSTALL.md. Seguí ese archivo al pie de la letra
y mostrame la tabla de validación al final.
```

Esperá a que termine.

---

## Paso 4 — Abrí Obsidian y revisá

- [ ] En el panel de Portals, el primer tab es una **casa** y muestra todas las carpetas
- [ ] Los tabs de las marcas tienen íconos de colores (trofeo, queso, carpa...)
- [ ] En el explorador de archivos, las carpetas tienen emoji y color
- [ ] El color de la interfaz (botones, links) es verde azulado

**¿Algo no aparece?** Andá a **Settings → Community plugins**, apagá y prendé ese plugin. Con eso se resuelve casi siempre.

**¿Sigue sin aparecer?** Cerrá Obsidian con `Cmd+Q` y volvé a correr el prompt del Paso 3.

---

## Cómo usar lo nuevo

**Portals** — Es el panel de tabs de la izquierda. Cada tab muestra **solo su carpeta**: si entrás al tab de una marca, ves esa marca sola. Para ver el vault completo usá el tab de la **casa**. No está roto, funciona así.

**Advanced Canvas** — En un canvas, seleccioná un nodo y vas a ver dos desplegables nuevos:
- **Trellis Role** — pinta el nodo según su función (Brand Core, System, Communication, Evidence, Project, Operations, DNA, AI)
- **Trellis Link** — tipa las flechas como Parent, Child o Related, igual que la jerarquía de Breadcrumbs

**Excalidraw** — Los dibujos se guardan como notas `.md` normales, así que viajan por git como cualquier otra nota. Nadie tiene que exportar ni adjuntar nada.

**Juggl** — Colorea cada nota según su campo `brand`. Si una nota sale gris, es porque tiene el `brand` mal escrito o vacío.

---

## Si querés cambiar algo

La configuración vive en `00-Trellis-Core/Obsidian-Config/`. Si editás algo ahí y hacés push, al resto del equipo le llega con el próximo `git pull` (y aplicando el prompt del Paso 3 de nuevo).

Los colores de cada marca están en esos archivos y son los mismos en el grafo, el explorador, los canvas y Portals. Si agregás una marca nueva, mantené ese criterio.
