#!/usr/bin/env python3
"""
Document Processor for RFP Questions Skill

Uses Gemini for visual processing of PDFs and images.
Produces page-by-page markdown breakdown (not summaries).

Usage:
    python3 process_document.py <file_path> --output-dir <dir> [--pages 1-5,10]

Environment:
    GEMINI_API_KEY - Required for Gemini API access (can be in .env file)

Output:
    Creates markdown files in output directory:
    - index.md (document overview)
    - page_01.md, page_02.md, etc. (page-by-page content)
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Generator


def load_env():
    """Load environment variables from .env file if available."""
    try:
        from dotenv import load_dotenv
        # Look for .env in current dir and parent dirs
        env_path = Path.cwd() / ".env"
        if not env_path.exists():
            # Try project root (walk up to find .env)
            for parent in Path.cwd().parents:
                candidate = parent / ".env"
                if candidate.exists():
                    env_path = candidate
                    break
        if env_path.exists():
            load_dotenv(env_path)
    except ImportError:
        pass  # dotenv not installed, rely on environment


# Load .env on import
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
            page = int(part)
            if page <= max_pages:
                pages.add(page)

    return sorted(pages)


def get_pdf_page_count(file_path: Path) -> int:
    """Get PDF page count."""
    content = file_path.read_bytes()
    count = content.count(b"/Type/Page") + content.count(b"/Type /Page")
    return max(count, 1)  # At least 1 page


def process_pdf_with_gemini(
    client,
    file_path: Path,
    pages: list[int] | None = None,
    model: str = "gemini-2.0-flash"
) -> Generator[dict, None, None]:
    """
    Process PDF using Gemini's native PDF support.

    Yields page-by-page results with markdown content.
    """
    from google.genai import types

    pdf_bytes = file_path.read_bytes()
    total_pages = get_pdf_page_count(file_path)

    if pages is None:
        pages = list(range(1, total_pages + 1))

    # For native PDF processing, we process the whole document
    # and ask for page-by-page breakdown
    prompt = f"""Analyze this PDF document and provide a page-by-page breakdown.

For EACH page (pages {pages[0]} to {pages[-1]}), provide:

1. Page number
2. Complete text content (preserve formatting, tables, lists)
3. Description of any images, charts, or diagrams
4. Key information or data points

Format your response as:

## Page [N]

### Content
[Full text content of the page]

### Visual Elements
[Description of any images, charts, tables]

### Key Points
- [Important items from this page]

---

Be thorough and complete. Do NOT summarize - capture all content faithfully.
This is for document archival, not summarization."""

    try:
        response = client.models.generate_content(
            model=model,
            contents=[
                types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
                prompt
            ]
        )

        # Parse the response into page chunks
        content = response.text

        # Split by page markers
        page_sections = []
        current_page = None
        current_content = []

        for line in content.split("\n"):
            if line.startswith("## Page "):
                if current_page is not None:
                    page_sections.append({
                        "page": current_page,
                        "content": "\n".join(current_content)
                    })
                try:
                    current_page = int(line.replace("## Page ", "").strip())
                    current_content = [line]
                except ValueError:
                    current_content.append(line)
            else:
                current_content.append(line)

        # Don't forget the last page
        if current_page is not None:
            page_sections.append({
                "page": current_page,
                "content": "\n".join(current_content)
            })

        # If parsing failed, yield the whole thing as page 1
        if not page_sections:
            yield {
                "page": 1,
                "content": content,
                "total_pages": total_pages
            }
        else:
            for section in page_sections:
                section["total_pages"] = total_pages
                yield section

    except Exception as e:
        yield {
            "page": 0,
            "content": f"Error processing PDF: {str(e)}",
            "error": True,
            "total_pages": total_pages
        }


def process_image_with_gemini(
    client,
    file_path: Path,
    model: str = "gemini-2.0-flash"
) -> dict:
    """Process a single image using Gemini vision."""
    from google.genai import types

    image_bytes = file_path.read_bytes()

    # Determine mime type
    suffix = file_path.suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    mime_type = mime_types.get(suffix, "image/png")

    prompt = """Analyze this image and extract all information:

1. **Text Content**: Extract ALL visible text, preserving layout where possible
2. **Visual Elements**: Describe any charts, diagrams, tables, or graphics
3. **Data Points**: List any numbers, dates, or specific data visible
4. **Context**: What type of document or content is this?

Be thorough and complete. This is for document archival, not summarization.
Preserve formatting and structure as much as possible."""

    try:
        response = client.models.generate_content(
            model=model,
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
                prompt
            ]
        )

        return {
            "page": 1,
            "content": response.text,
            "total_pages": 1
        }

    except Exception as e:
        return {
            "page": 1,
            "content": f"Error processing image: {str(e)}",
            "error": True,
            "total_pages": 1
        }


def write_output_files(
    output_dir: Path,
    file_name: str,
    results: list[dict],
    file_type: str
) -> dict:
    """Write processed results to markdown files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    files_created = []

    # Write index file
    index_path = output_dir / "index.md"
    total_pages = results[0].get("total_pages", len(results)) if results else 0

    index_content = f"""# {file_name}

**Type:** {file_type}
**Total Pages:** {total_pages}
**Pages Processed:** {len(results)}

## Contents

"""

    for result in results:
        page_num = result.get("page", 0)
        page_file = f"page_{page_num:02d}.md"
        index_content += f"- [{page_file}](./{page_file}) - Page {page_num}\n"

    index_content += "\n---\n*Processed by RFP Questions Document Ingestion*\n"

    index_path.write_text(index_content)
    files_created.append(str(index_path))

    # Write individual page files
    for result in results:
        page_num = result.get("page", 0)
        page_file = output_dir / f"page_{page_num:02d}.md"

        page_content = f"""# {file_name} - Page {page_num}

{result.get("content", "")}

---
*Source: {file_name}, Page {page_num} of {total_pages}*
"""

        page_file.write_text(page_content)
        files_created.append(str(page_file))

    return {
        "output_dir": str(output_dir),
        "files_created": files_created,
        "pages_processed": len(results)
    }


def main():
    parser = argparse.ArgumentParser(
        description="Process documents using Gemini visual AI"
    )
    parser.add_argument("file_path", help="Path to document (PDF or image)")
    parser.add_argument("--output-dir", "-o", required=True,
                        help="Output directory for markdown files")
    parser.add_argument("--pages", "-p", default=None,
                        help="Page range to process (e.g., '1-5,10')")
    parser.add_argument("--model", "-m", default="gemini-2.5-flash",
                        help="Gemini model to use")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be processed without calling API")

    args = parser.parse_args()

    file_path = Path(args.file_path)
    output_dir = Path(args.output_dir)

    if not file_path.exists():
        print(json.dumps({"error": f"File not found: {file_path}"}))
        sys.exit(1)

    # Check file type
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        file_type = "PDF"
        total_pages = get_pdf_page_count(file_path)
        pages = parse_page_range(args.pages, total_pages)
    elif suffix in (".png", ".jpg", ".jpeg", ".gif", ".webp"):
        file_type = "Image"
        total_pages = 1
        pages = [1]
    else:
        print(json.dumps({
            "error": f"Unsupported file type: {suffix}",
            "supported": [".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp"]
        }))
        sys.exit(1)

    # Dry run - just show what would happen
    if args.dry_run:
        print(json.dumps({
            "dry_run": True,
            "file": str(file_path),
            "file_type": file_type,
            "total_pages": total_pages,
            "pages_to_process": pages,
            "output_dir": str(output_dir),
            "model": args.model
        }, indent=2))
        sys.exit(0)

    # Check Gemini availability
    if not check_gemini_available():
        print(json.dumps({
            "error": "google-genai package not installed",
            "fix": "pip install google-genai"
        }))
        sys.exit(1)

    # Process document
    try:
        client = get_gemini_client()

        if file_type == "PDF":
            results = list(process_pdf_with_gemini(
                client, file_path, pages, args.model
            ))
        else:
            results = [process_image_with_gemini(client, file_path, args.model)]

        # Write output files
        output_info = write_output_files(
            output_dir,
            file_path.name,
            results,
            file_type
        )

        print(json.dumps({
            "success": True,
            "file": str(file_path),
            "file_type": file_type,
            **output_info
        }, indent=2))

    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"Processing failed: {str(e)}"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
