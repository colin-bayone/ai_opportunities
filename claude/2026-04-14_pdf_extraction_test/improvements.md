# extract_pdf.py — Planned Improvements

Baseline script is working (text + XHTML output, matching talent_ai logic).
These are changes to make before tackling the 1,064-page Cisco document.

## ⚠ Implementation Order Warning

**Do NOT implement these individually.** Several items have dependencies and conflicts:

- **#1 (Markdown format) depends on #4 (Markdown tables)** — no point building Markdown output with `[TABLE]` blocks still in it. These must ship together.
- **#1 and #3 (Chunked processing) interact** — Markdown output with a document header and `## Page N` structure needs to be designed with chunked/streaming writes in mind. Building it as a single in-memory string first, then retrofitting chunking, means rework.
- **#7 (Table deduplication) affects #1 and #4** — how tables render in Markdown depends on whether we keep inline text, structured blocks, or one-or-the-other. Must decide dedup strategy before finalizing table format.

**Plan:** Finalize the full design across all items, then implement once. Do not build incrementally.

## 1. Markdown Output Format

Replace the `=====` page separators with proper Markdown structure:

```markdown
# Document Title (from filename or PDF metadata)

---

## Page 1

Content here...

### Tables

| Col A | Col B | Col C |
|-------|-------|-------|
| data  | data  | data  |

---

## Page 2

...
```

**Why:** Navigable structure. Editors and renderers give you a clickable TOC from the `## Page N` headers. Much more useful than raw text with separator lines.

## 2. Progress Reporting

Print per-page progress so long extractions don't look hung:

```
Page 12/1064 (1.1%) — 3 tables found
Page 13/1064 (1.2%)
...
```

Update every page, or at minimum every 10 pages. Include a running timer.

## 3. Chunked Processing

**Decision:** Try without chunking first. Use progress reporting (#2) plus streaming writes (append each page as processed). Test on the 1,064-page Cisco document — if memory or performance is actually a problem, add chunking then. Don't pre-engineer it.

**Additional feature:** Add `--start-page` and `--end-page` (or `--pages 50-100`) CLI arguments for extracting a specific page range. This is useful regardless of chunking — user decides. Acceptable that Markdown structure won't have full document context when using a partial range.

## 4. Table Formatting in Markdown

**Decision:** Markdown tables replace inline text for the table region — no duplication. Confirmed by testing: table duplication inflated Rivian output by 74%.

Convert the current `[TABLE ... ]` / `[/TABLE]` format to proper Markdown tables:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
```

Use the first row as headers if it looks like a header row (heuristic: shorter text, distinct from data rows). Fall back to no-header table if ambiguous. This is tightly coupled with #1 (Markdown format) and #7 (deduplication) — implement together.

## 5. PDF Metadata Extraction

**Decision:** Pull metadata from the PDF via `doc.metadata` (title, author, creation date, subject). Include it at the top of the Markdown output AND write it as a separate `metadata.json` or `metadata.md` file within the output subfolder (#6). Both — not one or the other.

## 6. Output Subfolder Convention

Output files should go into a subfolder named `<filename>_PDF_extraction_<date>_<hhmmss>` rather than cluttering the same directory as the input PDF. The script should create this automatically.

## 7. Table Deduplication

**Decision:** Markdown tables replace inline text — suppress spatial text lines that fall within a table's bounding box. Implementation uses bbox coordinates from table extraction to filter overlapping text lines.

**Caution:** Must test carefully before committing. The bbox filtering could accidentally strip non-table content that overlaps a table region. Test with the Rivian RFP first (known baseline: 0.83% diff without tables) and verify no content is lost before applying to the Cisco guide.

Verified baseline: after stripping `[TABLE]` blocks and separators, extracted content matched manual copy-paste within 0.83%. Table duplication inflated output by 74%.

## 8. Deferred: Splitting Large Documents

**Status:** Deferred. Not worrying about this until it comes up as an actual problem. The page range flag from #3 may make this unnecessary in practice.

For very large documents, consider an option to split output into multiple files (e.g., one per chapter or per N pages). Not needed for baseline but worth considering if the Cisco guide produces a 2MB+ text file that's unwieldy to work with.
