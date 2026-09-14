# Obsidian-Config — mapa de instalación

Instrucciones para Claude Code. Las personas no necesitan leer este archivo:
ellas siguen [[00-Trellis-Core/Obsidian-Setup]].

## Requisito previo

Obsidian debe estar **cerrado** antes de escribir nada. Verificar con `pgrep -x Obsidian`.
Si está abierto, detenerse y avisar: el plugin sobrescribe su propio `data.json` al
guardar y se pierde toda la configuración sin ningún error visible.

## Mapa de archivos

Rutas relativas a la raíz del vault. Origen → destino.

| Origen | Destino | Modo |
|---|---|---|
| `00-Trellis-Core/Obsidian-Config/appearance.json` | `.obsidian/appearance.json` | merge |
| `00-Trellis-Core/Obsidian-Config/snippets/*.css` (6) | `.obsidian/snippets/` | copiar |
| `00-Trellis-Core/Obsidian-Config/plugins/advanced-canvas.json` | `.obsidian/plugins/advanced-canvas/data.json` | merge |
| `00-Trellis-Core/Obsidian-Config/plugins/portals.json` | `.obsidian/plugins/portals/data.json` | merge |
| `00-Trellis-Core/Obsidian-Config/plugins/excalidraw-overrides.json` | `.obsidian/plugins/obsidian-excalidraw-plugin/data.json` | merge |
| `00-Trellis-Core/Obsidian-Config/plugins/juggl-graph.css` | `.obsidian/plugins/juggl/graph.css` | copiar |
| `00-Trellis-Core/Obsidian-Config/plugins/mybrain.json` | `.obsidian/plugins/mybrain/data.json` | merge |
| `00-Trellis-Core/Obsidian-Config/plugins/mybrain-patch.sh` | `.obsidian/plugins/mybrain/main.js` | ejecutar |

**merge** = mantener las claves que ya existan en el destino y sobrescribir solo las
que vienen en el origen. Nunca reemplazar el archivo entero: `portals.json` y
`excalidraw-overrides.json` son fragmentos parciales a propósito.

**copiar** = escribir el archivo tal cual.

**ejecutar** = correr `bash <origen>` desde la raíz del vault. El script es idempotente:
si ya está aplicado no hace nada. Si falla con "source changed upstream", myBrain
cambió su código y el patch hay que revisarlo a mano antes de seguir; reportarlo.
Hay que volver a ejecutarlo después de cada actualización de myBrain (la
actualización pisa `main.js`).

## Por qué myBrain lleva patch

myBrain indexa los destinos de `up` / `down` / `related` por el texto literal del
wikilink (`01-brands/.../brand-home`) pero los busca por nombre de nota (`brand-home`).
Este vault escribe todos los enlaces de jerarquía con ruta completa, así que sin el
patch ninguna nota se clasifica como Parent / Child / Friend. El patch hace que
indexe por el último segmento de la ruta, igual que el lado de búsqueda.

Mapeo de cuadrantes myBrain ↔ campos Breadcrumbs (en `mybrain.json`):

| Cuadrante myBrain | Campo frontmatter | Notas |
|---|---|---|
| Parents (arriba) | `up` | explícito en 718 notas |
| Children (abajo) | `down` | explícito en 48; el resto se infiere del `up` inverso (igual que Breadcrumbs) |
| Friends (izquierda) | `related` | explícito en 621 |
| Siblings (derecha) | — | automático: notas que comparten el mismo parent |

`same` / `next` / `prev` existen en Breadcrumbs pero el vault no los usa (0 notas);
myBrain no tiene cuadrante para ellos, se dejan fuera.

Si la carpeta de un plugin no existe, ese plugin no está instalado: saltear ese
archivo y reportarlo al final.

## Prohibido

No tocar `.obsidian/plugins/obsidian-local-rest-api/` por ningún motivo. Contiene la
API key y la clave privada de cada persona, que son individuales y no se comparten.

## Validación al terminar

1. Todos los JSON escritos parsean.
2. Los 6 snippets existen en `.obsidian/snippets/` y los 6 nombres están listados en
   `enabledCssSnippets` dentro de `.obsidian/appearance.json`.
3. Toda ruta de carpeta referenciada en `spaces`, `customIcons` y `customColors` de
   Portals existe en el vault (excepto `/`, que es la raíz).
4. `grep -c 'u.split("/").pop()' .obsidian/plugins/mybrain/main.js` devuelve `1`.

Reportar en una tabla qué se aplicó, qué se salteó y por qué.
