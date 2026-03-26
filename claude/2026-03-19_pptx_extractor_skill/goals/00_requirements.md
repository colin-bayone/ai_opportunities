# PPTX Extractor Skill - Requirements

## Objective

Standalone Claude Code skill that extracts PowerPoint content into faithful markdown recreations, one slide at a time, using Gemini 2.5 Pro for visual interpretation.

## Why Gemini (not just XML parsing)

Some slides contain screenshots of text, images of diagrams, and other visual content that can't be extracted by parsing PPTX XML alone. Gemini Vision handles these faithfully.

## Core Requirements

1. **Split first, process individually** - Break a PPTX into single-slide PPTX files, then send each one to Gemini separately. Small context = faithful output.
2. **Faithful markdown recreation** - Archive-grade, not summaries. Every word, every table, every bullet.
3. **ASCII layout recreation** - Separate file per slide showing spatial layout structure.
4. **Slide metadata** - Describe what images, graphics, screenshots, and diagrams are on each slide.
5. **Speaker notes** - Extract and include if present.
6. **Organized output folder** - index.md, per-slide markdown, per-slide ASCII layout, metadata.json.

## Model

Gemini 2.5 Pro (`gemini-2.5-pro`) - not Flash.

## Downstream Use

The markdown output will be used to create HTML slide decks. This skill is extraction only - no HTML generation.

## Known Context

- python-pptx 1.0.2 already installed
- Pillow 11.3.0 already installed
- LibreOffice not installed (may install if needed for PNG rendering)
- Existing RFP skill scripts at `.claude/skills/rfp-questions/scripts/` provide proven patterns for Gemini integration
