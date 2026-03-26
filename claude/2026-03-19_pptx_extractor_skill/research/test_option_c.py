#!/usr/bin/env python3
"""
Test Option C: Send full PPTX to Gemini, ask for only slide 5.
Tests whether Gemini 2.5 Pro can focus on a single slide from a 43-slide deck.
"""

import json
import os
import sys
from pathlib import Path

# Load .env
try:
    from dotenv import load_dotenv
    for candidate in [Path.cwd() / ".env"] + [p / ".env" for p in Path.cwd().parents]:
        if candidate.exists():
            load_dotenv(candidate)
            break
except ImportError:
    pass

from google import genai
from google.genai import types

PPTX_PATH = Path("claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal.pptx")
SLIDE_NUM = 5
MODEL = "gemini-2.5-pro"

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"Reading {PPTX_PATH} ({PPTX_PATH.stat().st_size / 1024 / 1024:.1f} MB)...", file=sys.stderr)
    pptx_bytes = PPTX_PATH.read_bytes()

    prompt = f"""Analyze ONLY slide {SLIDE_NUM} of this PowerPoint presentation. Ignore all other slides completely.

Provide THREE clearly separated sections:

## Markdown Content
Recreate the complete visible content of slide {SLIDE_NUM} in markdown.
Include all text, bullet points, tables, and data exactly as shown.
Do NOT summarize. Capture every word faithfully.
Use proper markdown formatting (headers, lists, bold, etc.) to match the slide structure.

## ASCII Layout
Show the spatial arrangement of elements on slide {SLIDE_NUM} using ASCII art.
Indicate where titles, text blocks, images, and graphics are positioned relative to each other.
Use box-drawing characters and labels.
Show approximate proportions.

## Visual Elements
List and describe every image, screenshot, diagram, chart, icon, or graphic visible on slide {SLIDE_NUM}.
For each visual element, provide:
- Type (photo, icon, diagram, chart, screenshot, logo, etc.)
- Position on slide (top-left, center, bottom-right, etc.)
- Description of what it depicts
- If it contains text, transcribe that text

Be thorough and faithful. This is for document archival, not summarization."""

    print(f"Sending to {MODEL} - requesting slide {SLIDE_NUM} only...", file=sys.stderr)

    mime_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation"

    response = client.models.generate_content(
        model=MODEL,
        contents=[
            types.Part.from_bytes(data=pptx_bytes, mime_type=mime_type),
            prompt
        ]
    )

    print(f"Response received. Length: {len(response.text)} chars", file=sys.stderr)

    # Write output
    output_path = Path("claude/2026-03-19_pptx_extractor_skill/research/slide_05_test_output.md")
    output_path.write_text(f"# Test: Option C - Slide {SLIDE_NUM} Extraction\n\n"
                           f"**Model:** {MODEL}\n"
                           f"**Source:** {PPTX_PATH.name}\n"
                           f"**Slide:** {SLIDE_NUM}\n\n---\n\n"
                           f"{response.text}\n")

    print(f"Output written to {output_path}", file=sys.stderr)
    print(json.dumps({"success": True, "chars": len(response.text), "output": str(output_path)}))


if __name__ == "__main__":
    main()
