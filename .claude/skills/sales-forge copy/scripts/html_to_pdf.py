#!/usr/bin/env python3
"""
Convert HTML to PDF using Playwright.

Usage:
  python3 html_to_pdf.py <input.html> <output.pdf> [--mode document|slide]

Modes:
  document - Standard document with margins, portrait orientation (default)
  slide    - Full-bleed slide, landscape orientation, no margins

Examples:
  python3 html_to_pdf.py proposal.html proposal.pdf
  python3 html_to_pdf.py slide_01.html slide_01.pdf --mode slide
"""

import sys
import argparse
from pathlib import Path


def convert_to_pdf(input_path: str, output_path: str, mode: str = "document"):
    """
    Convert HTML file to PDF.

    Args:
        input_path: Path to input HTML file
        output_path: Path for output PDF file
        mode: 'document' or 'slide'
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: playwright not installed")
        print("Run: python3 install_dependencies.py")
        sys.exit(1)

    input_file = Path(input_path).resolve()
    output_file = Path(output_path).resolve()

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Configure PDF options based on mode
    if mode == "slide":
        pdf_options = {
            "path": str(output_file),
            "format": "Letter",
            "landscape": True,
            "print_background": True,
            "margin": {
                "top": "0",
                "right": "0",
                "bottom": "0",
                "left": "0"
            }
        }
    else:  # document
        pdf_options = {
            "path": str(output_file),
            "format": "Letter",
            "landscape": False,
            "print_background": True,
            "margin": {
                "top": "0.4in",
                "right": "0.4in",
                "bottom": "0.4in",
                "left": "0.4in"
            }
        }

    print(f"Converting: {input_file.name}")
    print(f"Mode: {mode}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the HTML file
        page.goto(f"file://{input_file}")

        # Wait for fonts to load
        page.wait_for_load_state("networkidle")

        # Small delay for any animations/transitions
        page.wait_for_timeout(500)

        # Generate PDF
        page.pdf(**pdf_options)

        browser.close()

    print(f"Output: {output_file}")
    print("Done!")


def convert_slides_batch(input_dir: str, output_dir: str):
    """
    Convert all HTML slides in a directory to PDFs.

    Args:
        input_dir: Directory containing HTML slide files
        output_dir: Directory for output PDFs
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    html_files = sorted(input_path.glob("*.html"))

    if not html_files:
        print(f"No HTML files found in {input_dir}")
        sys.exit(1)

    print(f"Found {len(html_files)} slides to convert")
    print()

    for html_file in html_files:
        pdf_file = output_path / f"{html_file.stem}.pdf"
        convert_to_pdf(str(html_file), str(pdf_file), mode="slide")
        print()

    print(f"Converted {len(html_files)} slides to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert HTML to PDF using Playwright",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Single document:
    python3 html_to_pdf.py proposal.html proposal.pdf

  Single slide:
    python3 html_to_pdf.py slide_01.html slide_01.pdf --mode slide

  Batch slides:
    python3 html_to_pdf.py slides/ output/ --batch
"""
    )

    parser.add_argument("input", help="Input HTML file or directory (with --batch)")
    parser.add_argument("output", help="Output PDF file or directory (with --batch)")
    parser.add_argument(
        "--mode",
        choices=["document", "slide"],
        default="document",
        help="Conversion mode (default: document)"
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Batch convert all HTML files in input directory"
    )

    args = parser.parse_args()

    if args.batch:
        convert_slides_batch(args.input, args.output)
    else:
        convert_to_pdf(args.input, args.output, args.mode)


if __name__ == "__main__":
    main()
