---
name: pdf-extractor
description: |
  Extract PDF pages to faithful markdown using Gemini Vision.
  WHEN to use: User wants to extract content from a PDF file, convert pages to markdown,
  get text from scanned or image-heavy PDFs, or prepare document content for further processing.
  WHEN NOT to use: Creating new PDFs, editing existing PDFs, or slide deck extraction (use pptx-extractor).
argument-hint: <path-to-pdf>
---

# PDF Extractor Skill

Extracts PDF pages to faithful markdown recreations using Gemini 2.5 Pro vision.

Handles pages that contain scanned text, images of diagrams, screenshots, and other visual
content that can't be extracted by text-only PDF parsing.

---

## Pipeline

1. **pdftoppm** renders individual page PNGs at 300 DPI
2. **Gemini 2.5 Pro** processes each page image individually for:
   - Faithful markdown recreation (every word, not summaries)
   - ASCII spatial layout
   - Visual element descriptions (images, charts, figures, diagrams)

## Usage

```bash
# Full document extraction (output goes to <pdf_name>/ next to the source file)
python .claude/skills/pdf-extractor/scripts/extract_pdf.py <file.pdf>

# Specific pages only
python .claude/skills/pdf-extractor/scripts/extract_pdf.py <file.pdf> --pages 1-5,10,15

# Custom output location
python .claude/skills/pdf-extractor/scripts/extract_pdf.py <file.pdf> -o <custom_dir>

# Dry run (no API calls)
python .claude/skills/pdf-extractor/scripts/extract_pdf.py <file.pdf> --dry-run
```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--output-dir, -o` | `<pdf_name>/` next to source | Output directory |
| `--pages, -p` | all | Page range (e.g., `1-5,10`) |
| `--model, -m` | `gemini-2.5-pro` | Gemini model |
| `--dpi` | `300` | Image rendering DPI |
| `--workers, -w` | `5` | Max parallel Gemini API calls |
| `--dry-run` | off | Preview without API calls |

## Output Structure

One folder per page, each containing its own files:

```
<pdf_stem>/
├── index.md                # Document overview with page list
├── metadata.json           # Page count, extraction status
├── page_01/
│   ├── page_01.png         # Rendered page image
│   ├── content.md          # Faithful markdown recreation
│   ├── layout.md           # ASCII spatial layout
│   └── visual_elements.md  # Image/graphic descriptions
├── page_02/
│   └── ...
```

## Dependencies

- `google-genai` - Gemini API
- `poppler-utils` - PDF to PNG conversion (pdftoppm, pdfinfo)

## Environment

```bash
export GEMINI_API_KEY="your-api-key"
```

Or use a `.env` file (auto-detected in current or parent directories).
