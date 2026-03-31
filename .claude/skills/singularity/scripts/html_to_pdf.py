#!/usr/bin/env python3
"""
HTML to PDF Converter for BayOne Documents

Converts HTML documents (proposals and slides) to PDF format.
Uses either Chrome/Chromium headless or WeasyPrint depending on availability.

Usage:
    python html_to_pdf.py <input.html> [output.pdf]
    python html_to_pdf.py <input_dir> [output.pdf]  # Merge multiple slide files

Options:
    --engine chrome|weasyprint    Force specific rendering engine
    --merge                       Merge multiple HTML files into single PDF
    --landscape                   Use landscape orientation (for slides)

Examples:
    # Single proposal
    python html_to_pdf.py proposal.html

    # Slide deck (merges all HTML files)
    python html_to_pdf.py slides/ deck.pdf --merge --landscape
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def find_chrome():
    """Find Chrome/Chromium executable."""
    candidates = [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        # macOS
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        # Windows (WSL paths)
        "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe",
        "/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    ]

    for candidate in candidates:
        if shutil.which(candidate):
            return candidate
        if os.path.isfile(candidate):
            return candidate

    return None


def chrome_to_pdf(html_path: str, pdf_path: str, landscape: bool = False):
    """Convert HTML to PDF using Chrome headless."""
    chrome = find_chrome()
    if not chrome:
        raise RuntimeError("Chrome/Chromium not found. Install Chrome or use --engine weasyprint")

    # Resolve to absolute path with file:// protocol
    html_path = Path(html_path).resolve()
    html_url = f"file://{html_path}"

    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-software-rasterizer",
        f"--print-to-pdf={pdf_path}",
        "--print-to-pdf-no-header",
    ]

    if landscape:
        # Chrome doesn't have a direct landscape flag for print-to-pdf
        # The HTML should use @page { size: landscape } in CSS
        pass

    cmd.append(html_url)

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Chrome error: {result.stderr}", file=sys.stderr)
        raise RuntimeError(f"Chrome PDF conversion failed")

    return pdf_path


def weasyprint_to_pdf(html_path: str, pdf_path: str):
    """Convert HTML to PDF using WeasyPrint."""
    try:
        from weasyprint import HTML
    except ImportError:
        raise RuntimeError("WeasyPrint not installed. Run: pip install weasyprint")

    HTML(filename=html_path).write_pdf(pdf_path)
    return pdf_path


def merge_pdfs(pdf_paths: list, output_path: str):
    """Merge multiple PDFs into one."""
    try:
        from pypdf import PdfMerger
    except ImportError:
        try:
            from PyPDF2 import PdfMerger
        except ImportError:
            raise RuntimeError("PyPDF2/pypdf not installed. Run: pip install pypdf")

    merger = PdfMerger()
    for pdf_path in pdf_paths:
        merger.append(pdf_path)

    merger.write(output_path)
    merger.close()
    return output_path


def get_html_files(input_path: str) -> list:
    """Get list of HTML files from path (file or directory)."""
    path = Path(input_path)

    if path.is_file():
        return [str(path)]

    if path.is_dir():
        # Sort by filename to maintain slide order (01_cover.html, 02_challenge.html, etc.)
        html_files = sorted(path.glob("*.html"))
        return [str(f) for f in html_files]

    raise ValueError(f"Path not found: {input_path}")


def convert(
    input_path: str,
    output_path: str = None,
    engine: str = "auto",
    merge: bool = False,
    landscape: bool = False
):
    """Main conversion function."""

    html_files = get_html_files(input_path)

    if not html_files:
        raise ValueError(f"No HTML files found in {input_path}")

    # Determine output path
    if output_path is None:
        if len(html_files) == 1:
            output_path = str(Path(html_files[0]).with_suffix(".pdf"))
        else:
            output_path = str(Path(input_path) / "output.pdf")

    # Select engine
    if engine == "auto":
        if find_chrome():
            engine = "chrome"
        else:
            engine = "weasyprint"

    print(f"Using engine: {engine}")

    # Single file conversion
    if len(html_files) == 1 and not merge:
        if engine == "chrome":
            result = chrome_to_pdf(html_files[0], output_path, landscape)
        else:
            result = weasyprint_to_pdf(html_files[0], output_path)

        print(f"Created: {result}")
        return result

    # Multiple files - convert each then merge
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_files = []

        for i, html_file in enumerate(html_files):
            tmp_pdf = os.path.join(tmpdir, f"{i:03d}.pdf")
            print(f"Converting: {html_file}")

            if engine == "chrome":
                chrome_to_pdf(html_file, tmp_pdf, landscape)
            else:
                weasyprint_to_pdf(html_file, tmp_pdf)

            pdf_files.append(tmp_pdf)

        print(f"Merging {len(pdf_files)} PDFs...")
        result = merge_pdfs(pdf_files, output_path)
        print(f"Created: {result}")
        return result


def main():
    parser = argparse.ArgumentParser(
        description="Convert BayOne HTML documents to PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument("input", help="Input HTML file or directory of slides")
    parser.add_argument("output", nargs="?", help="Output PDF path (optional)")
    parser.add_argument(
        "--engine",
        choices=["auto", "chrome", "weasyprint"],
        default="auto",
        help="Rendering engine (default: auto)"
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge multiple HTML files into single PDF"
    )
    parser.add_argument(
        "--landscape",
        action="store_true",
        help="Use landscape orientation"
    )

    args = parser.parse_args()

    try:
        convert(
            args.input,
            args.output,
            engine=args.engine,
            merge=args.merge,
            landscape=args.landscape
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
