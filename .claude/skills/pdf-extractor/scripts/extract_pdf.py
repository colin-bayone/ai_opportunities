#!/usr/bin/env python3
"""
PDF Extractor - Faithful page-by-page markdown extraction using Gemini Vision.

Renders each PDF page to a PNG image, then sends each page in parallel to
Gemini 2.5 Pro for faithful markdown recreation, ASCII layout, and visual
element descriptions.

Usage:
    python extract_pdf.py <file.pdf> [--pages 1-5,10] [--model gemini-2.5-pro] [--dry-run]
    python extract_pdf.py <file.pdf> --output-dir <custom_dir>  # override default output location

Environment:
    GEMINI_API_KEY - Required for Gemini API access (can be in .env file)

Dependencies:
    - google-genai (Gemini API)
    - pdftoppm (poppler-utils, for PDF to PNG conversion)

Output (created next to the source PDF by default):
    <pdf_stem>/
    ├── index.md
    ├── metadata.json
    ├── page_01/
    │   ├── page_01.png
    │   ├── content.md
    │   ├── layout.md
    │   └── visual_elements.md
    ├── page_02/
    │   └── ...
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def load_env():
    """Load environment variables from .env file if available."""
    try:
        from dotenv import load_dotenv
        env_path = Path.cwd() / ".env"
        if not env_path.exists():
            for parent in Path.cwd().parents:
                candidate = parent / ".env"
                if candidate.exists():
                    env_path = candidate
                    break
        if env_path.exists():
            load_dotenv(env_path)
    except ImportError:
        pass


load_env()


def check_gemini_available() -> bool:
    """Check if Gemini SDK is available."""
    try:
        from google import genai
        return True
    except ImportError:
        return False


def get_gemini_client():
    """Initialize Gemini client."""
    from google import genai
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    return genai.Client(api_key=api_key)


def check_system_deps() -> list[str]:
    """Check for required system dependencies. Returns list of missing deps."""
    missing = []
    if not shutil.which("pdftoppm"):
        missing.append("pdftoppm (apt install poppler-utils)")
    return missing


def get_pdf_page_count(file_path: Path) -> int:
    """Get PDF page count using pdfinfo if available, fallback to byte counting."""
    if shutil.which("pdfinfo"):
        try:
            result = subprocess.run(
                ["pdfinfo", str(file_path)],
                capture_output=True, text=True, timeout=10
            )
            for line in result.stdout.splitlines():
                if line.startswith("Pages:"):
                    return int(line.split(":")[1].strip())
        except Exception:
            pass

    # Fallback: byte-level counting
    content = file_path.read_bytes()
    count = content.count(b"/Type/Page") + content.count(b"/Type /Page")
    return max(count, 1)


def parse_page_range(page_spec: str, max_pages: int) -> list[int]:
    """Parse page specification like '1-5,10,15-20' into list of page numbers."""
    if not page_spec:
        return list(range(1, max_pages + 1))

    pages = set()
    for part in page_spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = int(start)
            end = min(int(end), max_pages)
            pages.update(range(start, end + 1))
        else:
            page_num = int(part)
            if page_num <= max_pages:
                pages.add(page_num)

    return sorted(pages)


def extract_page_images(pdf_path: Path, output_dir: Path, pages: list[int], dpi: int = 300) -> dict[int, Path]:
    """Extract specific pages from PDF as PNG images using pdftoppm."""
    output_dir.mkdir(parents=True, exist_ok=True)
    page_images = {}

    for page_num in pages:
        prefix = output_dir / f"page_{page_num:02d}"
        result = subprocess.run(
            [
                "pdftoppm", "-png",
                "-f", str(page_num), "-l", str(page_num),
                "-r", str(dpi),
                str(pdf_path), str(prefix)
            ],
            capture_output=True, text=True, timeout=60
        )

        if result.returncode != 0:
            print(f"  Warning: pdftoppm failed for page {page_num}: {result.stderr}", file=sys.stderr)
            continue

        # pdftoppm names output as prefix-NN.png
        expected = prefix.parent / f"{prefix.name}-{page_num:02d}.png"
        final = prefix.parent / f"page_{page_num:02d}.png"

        if expected.exists():
            expected.rename(final)
            page_images[page_num] = final
        else:
            # Try to find whatever pdftoppm created
            candidates = list(prefix.parent.glob(f"{prefix.name}*.png"))
            if candidates:
                candidates[0].rename(final)
                page_images[page_num] = final
            else:
                print(f"  Warning: No PNG created for page {page_num}", file=sys.stderr)

    return page_images


def process_page_with_gemini(
    client,
    image_path: Path,
    page_num: int,
    model: str = "gemini-2.5-pro"
) -> dict:
    """Send a single page image to Gemini for extraction."""
    from google.genai import types

    image_bytes = image_path.read_bytes()

    prompt = f"""You are analyzing page {page_num} of a PDF document, rendered as an image.

Provide THREE clearly separated sections:

## Markdown Content
Recreate the complete visible content of this page in markdown.
Include all text, headings, bullet points, tables, footnotes, and data exactly as shown.
Do NOT summarize. Capture every word faithfully.
Use proper markdown formatting (headers, lists, bold, tables, etc.) to match the document structure.
Preserve paragraph breaks and section structure.

## ASCII Layout
Show the spatial arrangement of elements on this page using ASCII art.
Indicate where headings, text columns, images, tables, sidebars, headers, and footers are positioned.
Use box-drawing characters and labels.
Show approximate proportions.

## Visual Elements
List and describe every image, screenshot, diagram, chart, figure, logo, or graphic visible on this page.
For each visual element, provide:
- Type (photo, icon, diagram, chart, screenshot, logo, figure, table, etc.)
- Position on page (top-left, center, bottom-right, etc.)
- Description of what it depicts
- If it contains text, transcribe that text
- If it has a caption or figure number, include that

Be thorough and faithful. This is for document archival, not summarization."""

    try:
        response = client.models.generate_content(
            model=model,
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                prompt
            ]
        )
        return {"success": True, "text": response.text, "page_num": page_num}

    except Exception as e:
        return {"success": False, "text": f"Error processing page {page_num}: {str(e)}", "page_num": page_num}


def parse_gemini_response(text: str) -> dict:
    """Parse Gemini response into markdown, layout, and visual elements sections.

    Only splits on our three known section headers, not arbitrary ## headers
    that Gemini may use inside the markdown content itself.
    """
    sections = {"markdown": "", "layout": "", "visual_elements": ""}

    # Only match our specific section headers, not any ## in the content
    section_pattern = re.compile(
        r'^## (?:Markdown Content|ASCII Layout|Visual Elements)\s*$',
        re.MULTILINE
    )
    matches = list(section_pattern.finditer(text))

    for i, match in enumerate(matches):
        header = match.group(0).strip().lower()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()

        if "markdown" in header:
            sections["markdown"] = content
        elif "ascii" in header or "layout" in header:
            sections["layout"] = content
        elif "visual" in header:
            sections["visual_elements"] = content

    # If parsing failed, put everything in markdown
    if not any(sections.values()):
        sections["markdown"] = text

    return sections


def write_outputs(
    output_dir: Path,
    source_name: str,
    total_pages: int,
    processed_pages: dict,
    page_images: dict[int, Path],
    model: str,
) -> dict:
    """Write all output files: one folder per page, each with its own files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    files_created = []

    for page_num in sorted(processed_pages.keys()):
        result = processed_pages[page_num]
        sections = parse_gemini_response(result["text"])

        # Create per-page folder
        page_dir = output_dir / f"page_{page_num:02d}"
        page_dir.mkdir(parents=True, exist_ok=True)

        # Copy page image into its folder
        if page_num in page_images:
            dest = page_dir / f"page_{page_num:02d}.png"
            shutil.copy2(page_images[page_num], dest)
            files_created.append(str(dest))

        # raw.md - always save the complete Gemini response, no parsing
        raw_path = page_dir / "raw.md"
        raw_path.write_text(result["text"])
        files_created.append(str(raw_path))

        # content.md - faithful markdown recreation
        content_path = page_dir / "content.md"
        content = f"# Page {page_num}\n\n"
        content += sections["markdown"]
        content += f"\n\n---\n*Source: {source_name}, Page {page_num} of {total_pages}*\n"
        content_path.write_text(content)
        files_created.append(str(content_path))

        # layout.md - ASCII spatial layout
        layout_path = page_dir / "layout.md"
        layout = f"# Page {page_num} - Spatial Layout\n\n"
        layout += sections["layout"]
        layout += "\n"
        layout_path.write_text(layout)
        files_created.append(str(layout_path))

        # visual_elements.md - image/graphic descriptions
        visual_path = page_dir / "visual_elements.md"
        visual = f"# Page {page_num} - Visual Elements\n\n"
        visual += sections["visual_elements"]
        visual += "\n"
        visual_path.write_text(visual)
        files_created.append(str(visual_path))

    # Write metadata.json
    metadata = {
        "source_file": source_name,
        "total_pages": total_pages,
        "pages_processed": len(processed_pages),
        "model": model,
        "pages": [
            {
                "number": page_num,
                "extraction_success": processed_pages[page_num]["success"],
            }
            for page_num in sorted(processed_pages.keys())
        ],
    }

    metadata_path = output_dir / "metadata.json"
    metadata_path.write_text(json.dumps(metadata, indent=2))
    files_created.append(str(metadata_path))

    # Write index.md
    index_lines = [
        f"# {source_name}\n",
        f"**Total Pages:** {total_pages}",
        f"**Pages Extracted:** {len(processed_pages)}",
        f"**Model:** {model}\n",
        "## Pages\n",
    ]

    for page_num in sorted(processed_pages.keys()):
        folder = f"page_{page_num:02d}"
        index_lines.append(
            f"- **Page {page_num:02d}**\n"
            f"  - [Content](./{folder}/content.md) "
            f"| [Layout](./{folder}/layout.md) "
            f"| [Visual Elements](./{folder}/visual_elements.md) "
            f"| [Image](./{folder}/page_{page_num:02d}.png)"
        )

    index_lines.append(f"\n---\n*Extracted by PDF Extractor*\n")

    index_path = output_dir / "index.md"
    index_path.write_text("\n".join(index_lines))
    files_created.insert(0, str(index_path))

    return {"files_created": files_created}


def main():
    parser = argparse.ArgumentParser(
        description="Extract PDF pages to markdown using Gemini Vision"
    )
    parser.add_argument("file_path", help="Path to PDF file")
    parser.add_argument("--output-dir", "-o", default=None,
                        help="Output directory (default: <pdf_name>/ next to source file)")
    parser.add_argument("--pages", "-p", default=None,
                        help="Page range to process (e.g., '1-5,10')")
    parser.add_argument("--model", "-m", default="gemini-2.5-pro",
                        help="Gemini model to use (default: gemini-2.5-pro)")
    parser.add_argument("--dpi", type=int, default=300,
                        help="DPI for page image rendering (default: 300)")
    parser.add_argument("--workers", "-w", type=int, default=5,
                        help="Max parallel Gemini API calls (default: 5)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be processed without calling API")

    args = parser.parse_args()

    file_path = Path(args.file_path).resolve()

    # Default output dir: same parent as PDF, folder named after the file
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = file_path.parent / file_path.stem

    # Validate input
    if not file_path.exists():
        print(json.dumps({"error": f"File not found: {file_path}"}))
        sys.exit(1)

    if file_path.suffix.lower() != ".pdf":
        print(json.dumps({"error": f"Not a PDF file: {file_path.suffix}"}))
        sys.exit(1)

    # Check system dependencies
    missing = check_system_deps()
    if missing and not args.dry_run:
        print(json.dumps({"error": "Missing system dependencies", "missing": missing}))
        sys.exit(1)

    # Check Gemini availability
    if not args.dry_run and not check_gemini_available():
        print(json.dumps({"error": "google-genai not installed", "fix": "pip install google-genai"}))
        sys.exit(1)

    # Get page count
    print(f"Reading {file_path.name}...", file=sys.stderr)
    total_pages = get_pdf_page_count(file_path)
    print(f"  {total_pages} pages, {file_path.stat().st_size / 1024 / 1024:.1f} MB", file=sys.stderr)

    # Parse page range
    pages_to_process = parse_page_range(args.pages, total_pages)

    # Dry run
    if args.dry_run:
        print(json.dumps({
            "dry_run": True,
            "file": str(file_path),
            "total_pages": total_pages,
            "pages_to_process": pages_to_process,
            "output_dir": str(output_dir),
            "model": args.model,
            "dpi": args.dpi,
            "workers": args.workers,
        }, indent=2))
        sys.exit(0)

    # Create temp directory for intermediate files
    with tempfile.TemporaryDirectory(prefix="pdf_extract_") as temp_dir:
        temp_path = Path(temp_dir)

        # Step 1: Extract page images
        print(f"Extracting {len(pages_to_process)} page images at {args.dpi} DPI...", file=sys.stderr)
        page_images = extract_page_images(file_path, temp_path / "images", pages_to_process, args.dpi)
        print(f"  {len(page_images)} images extracted", file=sys.stderr)

        if not page_images:
            print(json.dumps({"error": "No page images were extracted"}))
            sys.exit(1)

        # Step 2: Process pages with Gemini in parallel
        client = get_gemini_client()
        processed_pages = {}
        total = len(page_images)
        completed = 0

        print(f"Processing {total} pages with Gemini ({args.workers} parallel workers)...", file=sys.stderr)

        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    process_page_with_gemini, client, page_images[page_num], page_num, args.model
                ): page_num
                for page_num in sorted(page_images.keys())
            }

            for future in as_completed(futures):
                page_num = futures[future]

                try:
                    result = future.result()
                    processed_pages[page_num] = result
                    completed += 1
                    status = "ok" if result["success"] else "FAILED"
                    print(
                        f"  [{completed}/{total}] Page {page_num} - {status} ({len(result['text'])} chars)",
                        file=sys.stderr, flush=True
                    )
                except Exception as e:
                    completed += 1
                    processed_pages[page_num] = {
                        "success": False,
                        "text": f"Error: {str(e)}",
                        "page_num": page_num,
                    }
                    print(
                        f"  [{completed}/{total}] Page {page_num} - EXCEPTION: {e}",
                        file=sys.stderr, flush=True
                    )

        # Step 3: Write organized output
        print(f"Writing output to {output_dir}...", file=sys.stderr)
        output_info = write_outputs(
            output_dir, file_path.name, total_pages,
            processed_pages, page_images, args.model
        )

    # Summary
    successful = sum(1 for r in processed_pages.values() if r["success"])
    failed = len(processed_pages) - successful

    result = {
        "success": True,
        "file": str(file_path),
        "total_pages": total_pages,
        "pages_processed": len(processed_pages),
        "pages_successful": successful,
        "pages_failed": failed,
        "output_dir": str(output_dir),
        "files_created": output_info["files_created"],
    }

    print(json.dumps(result, indent=2))
    print(f"\nDone! {successful}/{len(processed_pages)} pages extracted successfully.", file=sys.stderr)


if __name__ == "__main__":
    main()
