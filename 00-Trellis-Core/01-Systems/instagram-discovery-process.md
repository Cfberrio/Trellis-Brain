---
brain_note_id: "note:5b393872-de29-4bee-bb6d-18410d44d5c8"
canonical_key: "instagram-discovery-process"
brand_id: "trellis_core"
---
# Instagram-Discovery-Process

## Canonical Statement

- **process**: Instagram discovery process: Use Claude Code with Apify MCP (DeepMine Reels Search for recent content, Instagram Search Scraper for baseline). Filter by date window, deduplicate by shortcode, and validate permalinks. Prioritize recent content (postedAt within window) over scrape date.
- **fact**: DeepMine Reels Search is more effective for recent Instagram discovery than standard Instagram Search Scraper for technical/niche topics.

## Evidence Log

- 2026-10-24T16:39:14.445Z — `clickup:86e3v9jnn`
  - `e1` (source_body): Piloto ejecutado de punta a punta: 5 runs, USD 0.525 de gasto real, ganador DeepMine. ... B trajo 39 Reels, el 100% dentro de la ventana, y 12 útiles (7 de valor alto). A trajo 42 posts, 6 en ventana y 4 útiles.

- 2026-10-27T02:10:39.145Z — `clickup:86e3v9jnn` (validation `ca7a7cff-2829-4d20-89cc-0225e13f17d2`)
  - `e1` (source_child): Piloto ejecutado de punta a punta: 5 runs, USD 0.525 de gasto real, ganador DeepMine. ... B trajo 39 Reels, el 100% dentro de la ventana, y 12 útiles (7 de valor alto). A trajo 42 posts, 6 en ventana y 4 útiles.
- **process**: Instagram discovery process: Use Claude Code with Apify MCP (DeepMine Reels Search for recent content, Instagram Search Scraper for baseline). Filter by date window, deduplicate by shortcode, and validate permalinks. Prioritize recent content (postedAt within window) over scrape date.
- **fact**: DeepMine Reels Search is more effective for recent Instagram discovery than standard Instagram Search Scraper for technical/niche topics, yielding higher precision and relevance within a 30-day window.

- 2026-10-27T18:46:30.632Z — `clickup:86e3v9jnn` (validation `be972d39-cf56-4eb0-8eed-868af5d43ac9`)
  - `e1` (source_child): Piloto ejecutado de punta a punta: 5 runs, USD 0.525 de gasto real, ganador DeepMine. ... B trajo 39 Reels, el 100% dentro de la ventana, y 12 útiles (7 de valor alto). A trajo 42 posts, 6 en ventana y 4 útiles.
  - `e2` (source_body): Stack recomendado: plugin Apify para Claude Code → MCP de Apify → Actor DeepMine Reels Search (descubrimiento reciente) → Apify Reel Scraper solo para enriquecer → skill local para evaluar.
- **process**: Instagram discovery process: Use Claude Code with Apify MCP (DeepMine Reels Search for recent content, Instagram Search Scraper for baseline). Filter by date window, deduplicate by shortcode, and validate permalinks. Prioritize recent content (postedAt within window) over scrape date.
- **fact**: DeepMine Reels Search is more effective for recent Instagram discovery than standard Instagram Search Scraper for technical/niche topics, yielding higher precision and relevance within a 30-day window.

## Provenance

- Source: `clickup` `86e3v9jnn`
- Source hash: `8fdebc15794d49b19725e3f08f1bd54198e1a8082ec7b260ab891ac199d95e1e`
- Observed at: 2026-10-24T16:39:14.445Z
- Agent run: `32dd1cce-aeb2-4bc9-a31b-ed2277276617`
- Validation run: `387ecda4-851f-445a-a752-8a808fb724cb`
