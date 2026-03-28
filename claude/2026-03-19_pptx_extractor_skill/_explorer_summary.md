# Session Summary: 2026-03-19_pptx_extractor_skill

## Client/Opportunity
**BayOne Internal / Tooling** — PPTX extraction skill using Gemini 2.5 Pro vision

## Purpose
Develop a Claude Code skill that extracts PowerPoint presentations into faithful markdown using Gemini vision. Splits PPTX into individual slides, sends each to Gemini for visual interpretation, produces structured markdown with spatial layout diagrams and visual element descriptions. Includes full production extractions of 2 decks.

## File Tree
```
2026-03-19_pptx_extractor_skill/
  goals/
    00_requirements.md                          (4.2K)  Skill spec: PPTX -> slides -> Gemini 2.5 Pro -> markdown.
                                                        Why vision: handles screenshots, diagrams beyond XML.
                                                        Output: faithful markdown, ASCII layout, metadata, notes.
  planning/
    00_implementation_plan.md                   (8.5K)  Technical blueprint. 3 options evaluated:
                                                        A: python-pptx XML (complex)
                                                        B: LibreOffice -> PNG -> Gemini
                                                        C: Full PPTX -> Gemini with slide filter (simplest)
                                                        Recommended: Option C. CLI interface spec. Rate limiting.
  research/
    debug_parse.py                              (1.6K)  Debug: sends slide 21 PNG to Gemini, dumps raw response
    test_option_b.py                            (2.8K)  Test Option B: slide PNG -> Gemini 2.5 Pro
    test_option_c.py                            (2.9K)  Test Option C: full PPTX -> Gemini with slide filter
    slide_05_test_output.md                     (18K)   Sample extraction: BayOne Service Offerings slide.
                                                        Faithful markdown + ASCII 2x3 grid + 8 icon descriptions.
    slide_images/
      slide-05.png                              (850K)  Test slide screenshot
      WIP_Managed_Services_Support_Proposal.pdf (~10MB) PDF reference
    test_output/                                (3 slides extracted from 43-slide deck)
      index.md                                  (800B)  Index for 3 extracted slides
      metadata.json                             (2.1K)  Per-slide metadata, all extraction_success: true
      slide_04/ slide_05/ slide_06/             (4 files each: content.md, layout.md,
                                                        visual_elements.md, slide_XX.png)
  source/
    BayOne-Overview-Ariat-GCC-Feb-2026_COLIN_EDITS/
      index.md                                  (2.8K)  19/21 slides extracted from Ariat deck
      metadata.json                             (8.5K)  Per-slide metadata
      slide_01/ through slide_19/               (4 files each: content.md, layout.md,
                                                        visual_elements.md, slide_XX.png)
    MGRC Managed Services Proposal/
      index.md                                  (3.8K)  32/32 slides extracted from McGrath deck
      metadata.json                             (38K)   Complete metadata for all 32 slides
      slide_01/ through slide_32/               (4 files each: content.md, layout.md,
                                                        visual_elements.md, slide_XX.png)
    (5 PPTX source files)
      BayOne-Overview-Ariat-GCC-*.pptx          (2.1MB) 21 slides
      MGRC Managed Services Proposal.pptx       (5.8MB) 32 slides
      MGRC Managed Services Proposal v3 2.pptx  (5.2MB) Alternate version
      WIP_Managed_Services_Support_Proposal.pptx (4.2MB) 43 slides
      WIP_PC_*_0322 2.pptx                      (4.0MB) Alternate version
```

## Key Deliverables
1. **Requirements + implementation plan** — 3 options evaluated, Option C recommended
2. **3 test scripts** — proving feasibility of image-based and PPTX-based extraction
3. **Production extraction: Ariat deck** — 19/21 slides (90%) faithfully extracted
4. **Production extraction: McGrath deck** — 32/32 slides (100%) faithfully extracted
5. **Standardized output format** per slide: content.md + layout.md (ASCII) + visual_elements.md + PNG

## Cross-References
- **Ariat deck:** `BayOne-Overview-Ariat-GCC-Feb-2026_COLIN_EDITS.pptx` (21 slides, for folder #14)
- **McGrath deck:** `MGRC Managed Services Proposal.pptx` (32 slides, for `mcgrath/`)
- **Skill target:** `.claude/skills/pptx-extractor/`
- **Dependencies:** python-pptx, Pillow, google-genai (Gemini 2.5 Pro)

## Suggested Home
`claude/` or `tooling/` — internal skill development.

## Summary Statistics
- **Total files:** 150+ (95 markdown, 55 PNGs, 3 JSON, 3 Python, 5 PPTX)
- **Total size:** ~300 KB markdown + ~30 MB images + ~21 MB PPTX
- **Slides extracted:** 72+ (19 Ariat + 32 McGrath + 3 test + 18 misc)
- **Extraction success rate:** ~95%
- **Model:** Gemini 2.5 Pro exclusively
