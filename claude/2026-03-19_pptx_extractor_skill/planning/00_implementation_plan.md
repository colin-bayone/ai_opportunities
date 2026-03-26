# PPTX Extractor Skill - Implementation Plan

## Skill Location

`.claude/skills/pptx-extractor/`

```
.claude/skills/pptx-extractor/
├── SKILL.md              # Skill definition (triggers, rules)
└── scripts/
    └── extract_pptx.py   # Single script, does everything
```

## Why One Script

The pipeline is linear and self-contained. No phases, no hooks, no multi-agent orchestration. One PPTX in, organized folder out. Splitting it into multiple scripts adds complexity with no benefit.

## Pipeline (what extract_pptx.py does)

### Step 1: Split PPTX into individual slides
- Use python-pptx to create N single-slide PPTX files in a temp directory
- Also extract speaker notes per slide via python-pptx (`.slides[i].notes_slide`)
- Also extract basic structural metadata (title text, shape counts, image counts)

### Step 2: Send each slide to Gemini 2.5 Pro individually
- For each single-slide PPTX file, send to Gemini with `types.Part.from_bytes()`
- MIME type: `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- Three prompts per slide (or one combined prompt returning structured sections):

**Prompt asks for:**
1. **Markdown recreation** - Faithful reproduction of all visible content
2. **ASCII layout** - Spatial representation of how elements are arranged on the slide
3. **Visual element descriptions** - What images, screenshots, diagrams, charts, icons are present

### Step 3: Write organized output
```
<output_dir>/
├── index.md                # Deck overview, slide list with titles
├── slides/
│   ├── slide_01.md         # Faithful markdown recreation
│   ├── slide_01_layout.txt # ASCII layout
│   ├── slide_02.md
│   ├── slide_02_layout.txt
│   └── ...
└── metadata.json           # Per-slide: title, speaker notes, graphic descriptions, shape counts
```

### Step 4: Clean up temp files

## CLI Interface

```bash
python3 extract_pptx.py <file.pptx> --output-dir <dir> [--slides 1-5,10] [--model gemini-2.5-pro] [--dry-run]
```

- `--slides` - Optional slide range (same parser as process_document.py page ranges)
- `--model` - Defaults to `gemini-2.5-pro`
- `--dry-run` - Show slide count, titles, and what would be processed
- JSON output to stdout (same pattern as existing scripts)

## Key Implementation Details

### Splitting with python-pptx
```python
from pptx import Presentation
from pptx.util import Emu

def split_pptx(file_path, temp_dir):
    prs = Presentation(file_path)
    slide_files = []
    for i, slide in enumerate(prs.slides):
        # Create new presentation with same dimensions
        new_prs = Presentation()
        new_prs.slide_width = prs.slide_width
        new_prs.slide_height = prs.slide_height
        # Copy slide layout and content
        # ... (python-pptx slide copying logic)
        out_path = temp_dir / f"slide_{i+1:02d}.pptx"
        new_prs.save(out_path)
        slide_files.append(out_path)
    return slide_files
```

**Important caveat:** python-pptx doesn't have a native "copy slide" API. The approach is:
- Option A: Use python-pptx's XML manipulation to copy slide XML between presentations
- Option B: Use python-pptx to export slide content + LibreOffice to render to PNG, then send images to Gemini
- Option C: Send the full PPTX to Gemini but request only one specific slide per call

**Recommended: Option C first, Option B as fallback.** Sending the full PPTX but prompting "analyze ONLY slide N" is simplest and avoids the slide-copying complexity. If Gemini doesn't respect the single-slide instruction reliably, fall back to rendering PNGs via LibreOffice.

### Gemini Prompt (per slide)

```
Analyze slide {N} of this PowerPoint presentation. Ignore all other slides.

Provide THREE sections:

## Markdown Content
Recreate the complete visible content of this slide in markdown.
Include all text, bullet points, tables, and data exactly as shown.
Do NOT summarize. Capture everything faithfully.

## ASCII Layout
Show the spatial arrangement of elements on this slide using ASCII art.
Indicate where titles, text blocks, images, and graphics are positioned.
Use box-drawing characters and labels.

## Visual Elements
List and describe every image, screenshot, diagram, chart, icon, or graphic on this slide.
For screenshots of text, transcribe the text content.
For diagrams, describe the structure and relationships shown.
For charts, describe the type and data represented.
```

### Speaker Notes Extraction
```python
def get_speaker_notes(slide):
    if slide.has_notes_slide:
        notes_slide = slide.notes_slide
        return notes_slide.notes_text_frame.text
    return None
```

### Metadata Structure
```json
{
  "source_file": "deck.pptx",
  "total_slides": 43,
  "slides_processed": 43,
  "model": "gemini-2.5-pro",
  "slides": [
    {
      "number": 1,
      "title": "Introduction",
      "speaker_notes": "Welcome everyone...",
      "visual_elements": ["Company logo (top-right)", "Background gradient image"],
      "shape_count": 5,
      "image_count": 2,
      "has_table": false,
      "has_chart": false
    }
  ]
}
```

## Dependencies

- python-pptx (installed)
- google-genai (installed via RFP skill)
- python-dotenv (optional, for .env loading)

## Rate Limiting Consideration

43 slides = 43 Gemini API calls. Add a small delay between calls (0.5s) to avoid rate limiting, and print progress to stderr so the user sees it moving.

## Verification

1. Run `--dry-run` on a test PPTX to confirm slide counting and title extraction
2. Run on 2-3 slides first (`--slides 1-3`) to verify output quality
3. Run full deck and inspect output folder structure
4. Confirm speaker notes appear in metadata.json
5. Confirm ASCII layouts are present and reasonable
