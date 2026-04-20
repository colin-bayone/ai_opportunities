# Group A Design: Markdown Output + Table Formatting + Table Deduplication

Covers improvements #1, #4, and #7 as a unified implementation.

## Problem

Each page is currently processed in two independent passes — text extraction gives all text (including text inside tables), and table extraction gives structured table data. These get concatenated via `[TABLE]` blocks, resulting in table content appearing twice. Output uses `=====` separators instead of navigable Markdown. Table duplication inflated the Rivian RFP output by 74%.

## Research Findings

PyMuPDF has **no native way** to separate table text from body text. `page.get_text()` returns ALL text including table cell content. `page.find_tables()` extracts tables independently. The only way to classify text as "inside a table" is spatial bbox intersection using `pymupdf.Rect.intersects()`.

However, **`Table.to_markdown()`** is built into PyMuPDF — no need to write our own Markdown table renderer.

## Simplified Approach (Colin's feedback)

Don't over-engineer deduplication. The baseline extraction already captures everything — the duplication is just the `[TABLE]` blocks being appended. Instead of trying to surgically remove table text from the body:

1. **Main Markdown file:** Text extracted with spatial ordering (naturally includes table cell text as part of page flow), formatted with `## Page N` headers. No `[TABLE]` blocks appended. This is the clean, readable output.
2. **Separate tables file:** All structured table data dumped to its own file using PyMuPDF's built-in `Table.to_markdown()`. Nothing is lost — it's just in a separate file.

This avoids all bbox filtering risk entirely. The main file has clean text with table content inline (as it appears when you read the page). The tables file has the structured version for anyone who needs columns/rows.

### Why this is better than bbox filtering

- No risk of accidentally suppressing non-table content
- No coordinate geometry or tolerance tuning
- Nothing is discarded — just separated
- The main output matches what you'd get from a manual copy-paste (proven: 0.83% match)

### Optional future enhancement

If we later want the main Markdown to have proper pipe tables *instead of* inline text, we can revisit bbox intersection at that point. `pymupdf.Rect.intersects()` exists for that purpose. But it's not needed for a correct, complete extraction.

## Document Structure (Improvement #1)

```markdown
# Rivian RFP_DWS Managed Services Support2

> **Source:** Rivian RFP_DWS Managed Services Support2.pdf
> **Pages:** 33 | **Tables:** 46
> **Extracted:** 2026-04-14 17:40

---

## Page 1

Content from page 1...

---

## Page 2

More content here. Table cell text appears naturally as part of
the page flow, just as it would if you copy-pasted from the PDF.

Content continues...

---

## Page 3
```

## Tables File Structure

Separate file (`tables.md` or `tables.json`) in the output subfolder:

```markdown
# Tables: Rivian RFP_DWS Managed Services Support2

## Page 5

### Table 1 (default detection, high confidence)

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |

### Table 2 (lines_based detection, medium confidence)

| Col A | Col B |
|-------|-------|
| data  | data  |

## Page 12

### Table 1 (default detection, high confidence)

...
```

## Output Subfolder Contents

```
<filename>_PDF_extraction_<date>_<hhmmss>/
├── <filename>.md          ← main Markdown output (text with page headers)
├── tables.md              ← all structured tables, organized by page
├── metadata.md            ← PDF metadata (title, author, dates, etc.)
└── <filename>.xhtml       ← XHTML output (existing format, kept for compatibility)
```

## Code Changes Required

- Stop appending `[TABLE]` blocks in `_enhance_text_with_tables` — remove that call entirely from the main flow
- Replace `=====` page separators with `## Page N` headers and `---` dividers
- Add document header with metadata blockquote
- New: `_extract_tables_to_file(doc, output_path)` — iterate pages, call `table.to_markdown()`, write organized tables file
- New: `_extract_metadata(doc)` — pull `doc.metadata`, write to file and document header
- New: auto-create output subfolder with naming convention
- Keep XHTML extraction as-is (separate output, no changes needed)

## Testing Plan

1. Run against Rivian RFP
2. Compare main Markdown non-whitespace char count against manual copy-paste baseline (32,545 chars) — should be within 1%
3. Verify tables file contains all 46 tables
4. Spot-check a few pages visually for readability
