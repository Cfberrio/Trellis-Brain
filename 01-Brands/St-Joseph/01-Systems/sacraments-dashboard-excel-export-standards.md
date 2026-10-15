---
brain_note_id: "note:72affe35-2a2a-4b84-ab62-4358c6119ce0"
canonical_key: "sacraments-excel-export-standards"
brand_id: "st_joseph"
---
# Sacraments Dashboard Excel Export Standards

## Canonical Statement

- **rule**: The Sacraments Excel export must group participants by status in the following order: Registered & attending, Attending, not registered, Registered, not attending, No class yet, and Status not set.
- **process**: Excel exports from the Sacraments page must respect active dashboard filters, include a summary tab with export metadata, and use the suffix '-filtered' in the filename when filters are applied.
- **rule**: Export formatting must include frozen header rows, active Excel filters on all columns, alternating row shading, and no merged cells to ensure sorting and filtering functionality.
- **rule**: Within each participation status group in the export, names must be sorted alphabetically by last name.

## Evidence Log

- 2026-10-15T21:34:02.282Z — `clickup:86e3r1g9k`
  - `e1` (source_body): Improve readability with bold, contrasting headers, frozen header rows, sensible column widths, wrapped long text, consistent alignment and alternating row shading. Keep the data range filterable without merged cells or decorative rows breaking sorting and filtering.
  - `e2` (source_child): People are grouped by status in this order: Registered & attending → Attending, not registered → Registered, not attending → No class yet → Status not set... names are sorted by last name inside each group... The download follows the page filters. It only includes the people shown on screen.

## Provenance

- Source: `clickup` `86e3r1g9k`
- Source hash: `49ce5cd8b9675db1777b4c53f5f5929401f8128feaf3553d143e0eeb4a6d5816`
- Observed at: 2026-10-15T21:34:02.282Z
- Agent run: `cc50a6a4-da76-467e-aaca-0f06e4987f2b`
- Validation run: `bfad4fe1-6170-44c1-b5f0-253e3ca3b556`
