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

**merge** = mantener las claves que ya existan en el destino y sobrescribir solo las
que vienen en el origen. Nunca reemplazar el archivo entero: `portals.json` y
`excalidraw-overrides.json` son fragmentos parciales a propósito.

**copiar** = escribir el archivo tal cual.

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

Reportar en una tabla qué se aplicó, qué se salteó y por qué.
