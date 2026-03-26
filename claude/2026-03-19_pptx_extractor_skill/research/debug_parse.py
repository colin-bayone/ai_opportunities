#!/usr/bin/env python3
"""Debug: send slide 21 to Gemini and dump raw response to see header format."""

import json
import os
import sys
from pathlib import Path

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

img = Path("claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_21/slide_21.png")
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = """You are analyzing slide 21 of a PowerPoint presentation, rendered as an image.

Provide THREE clearly separated sections:

## Markdown Content
Recreate the complete visible content of this slide in markdown.
Include all text, bullet points, tables, and data exactly as shown.
Do NOT summarize. Capture every word faithfully.
Use proper markdown formatting (headers, lists, bold, etc.) to match the slide structure.

## ASCII Layout
Show the spatial arrangement of elements on this slide using ASCII art.
Indicate where titles, text blocks, images, and graphics are positioned relative to each other.
Use box-drawing characters and labels.
Show approximate proportions.

## Visual Elements
List and describe every image, screenshot, diagram, chart, icon, or graphic visible on this slide.
For each visual element, provide:
- Type (photo, icon, diagram, chart, screenshot, logo, etc.)
- Position on slide (top-left, center, bottom-right, etc.)
- Description of what it depicts
- If it contains text, transcribe that text

Be thorough and faithful. This is for document archival, not summarization."""

response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=[types.Part.from_bytes(data=img.read_bytes(), mime_type="image/png"), prompt]
)

text = response.text
print(f"Total length: {len(text)}", file=sys.stderr)

# Show first 500 chars to see how the response starts
print("=== FIRST 500 CHARS ===")
print(text[:500])
print()

# Show all lines that start with #
print("=== ALL HEADER LINES ===")
for i, line in enumerate(text.split("\n")):
    if line.startswith("#"):
        print(f"  Line {i}: {line!r}")
