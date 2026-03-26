---
name: pptx-extractor
description: |
  Extract PowerPoint slides to faithful markdown using Gemini Vision.
  WHEN to use: User wants to extract content from a PPTX file, convert slides to markdown,
  get text from screenshot-heavy slide decks, or prepare slide content for HTML recreation.
  WHEN NOT to use: Creating new PowerPoint files, editing existing slides, or HTML generation.
argument-hint: <path-to-pptx>
---

# PPTX Extractor Skill

Extracts PowerPoint slides to faithful markdown recreations using Gemini 2.5 Pro vision.

Handles slides that contain screenshots of text, images of diagrams, and other visual content
that can't be extracted by parsing PPTX XML alone.

---

## Pipeline

1. **python-pptx** extracts structural metadata and speaker notes
2. **LibreOffice headless** converts PPTX to PDF
3. **pdftoppm** renders individual slide PNGs at 300 DPI
4. **Gemini 2.5 Pro** processes each slide image individually for:
   - Faithful markdown recreation (every word, not summaries)
   - ASCII spatial layout
   - Visual element descriptions (images, charts, icons, screenshots)

## Usage

```bash
# Full deck extraction (output goes to <pptx_name>/ next to the source file)
python .claude/skills/pptx-extractor/scripts/extract_pptx.py <file.pptx>

# Specific slides only
python .claude/skills/pptx-extractor/scripts/extract_pptx.py <file.pptx> --slides 1-5,10,15

# Custom output location
python .claude/skills/pptx-extractor/scripts/extract_pptx.py <file.pptx> -o <custom_dir>

# Dry run (no API calls)
python .claude/skills/pptx-extractor/scripts/extract_pptx.py <file.pptx> --dry-run
```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--output-dir, -o` | `<pptx_name>/` next to source | Output directory |
| `--slides, -s` | all | Slide range (e.g., `1-5,10`) |
| `--model, -m` | `gemini-2.5-pro` | Gemini model |
| `--dpi` | `300` | Image rendering DPI |
| `--workers, -w` | `5` | Max parallel Gemini API calls |
| `--dry-run` | off | Preview without API calls |

## Output Structure

One folder per slide, each containing its own files:

```
<pptx_stem>/
├── index.md                # Deck overview with slide list
├── metadata.json           # Titles, speaker notes, shape counts
├── slide_01/
│   ├── slide_01.png        # Rendered slide image
│   ├── content.md          # Faithful markdown recreation
│   ├── layout.md           # ASCII spatial layout
│   └── visual_elements.md  # Image/graphic descriptions
├── slide_02/
│   └── ...
```

## Dependencies

- `python-pptx` - PPTX structure and speaker notes
- `google-genai` - Gemini API
- `libreoffice-impress` - PPTX to PDF conversion
- `poppler-utils` - PDF to PNG conversion (pdftoppm)

## Environment

```bash
export GEMINI_API_KEY="your-api-key"
```

Or use a `.env` file (auto-detected in current or parent directories).
