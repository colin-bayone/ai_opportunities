#!/usr/bin/env python3
"""
HTML to PDF Converter for BayOne Documents

Converts HTML documents (proposals and slides) to PDF format.
Uses either Chrome/Chromium headless or WeasyPrint depending on availability.

Usage:
    python html_to_pdf.py <input.html> [output.pdf]
    python html_to_pdf.py <input_dir> [output.pdf]  # Merge multiple slide files

Options:
    --engine chrome|weasyprint|auto    Force rendering engine (default: auto, prefers chrome)
    --merge                            Merge multiple HTML files into single PDF
    --landscape                        Inject 16:10 landscape page sizing for slides

Flag selection by use case (what callers should pass):
    Single deliverable (proposal, problem restatement, info request, briefing):
        python html_to_pdf.py deliverable.html
        # No flags. Defaults to auto engine, portrait letter, the deliverable's
        # own @page CSS controls layout.

    Multi-slide presentation deck (BayOne 16:10 slides):
        python html_to_pdf.py slides_dir/ deck.pdf --merge --landscape
        # --merge combines every *.html in the directory in filename sort order.
        # --landscape is REQUIRED for slide decks because Chrome's print-to-pdf
        # has no native landscape flag and the slide HTML does not include @page
        # CSS. Without --landscape the slides render on portrait letter paper
        # with massive whitespace.

    Single slide preview (one HTML file from a deck):
        python html_to_pdf.py 03_architecture.html preview.pdf --landscape
        # --landscape only. No --merge needed for a single file.

    Force a specific engine:
        Add --engine chrome or --engine weasyprint to any of the above.

Implementation notes:
    Chrome headless does not have a direct landscape flag for --print-to-pdf.
    When --landscape is passed, this script injects an @page rule into a temp
    copy of the HTML (sized 11.5in x 7.1875in to match the BayOne 16:10 slide
    aspect ratio) and points Chrome at the temp file. Originals are not modified.
    Slide navigation buttons (.slide-nav) are hidden in print via the same
    injection so they do not appear in the PDF.

    External fonts and icons (Inter via Google Fonts, Font Awesome via CDN) need
    time to load before Chrome snapshots the page. The --virtual-time-budget and
    --run-all-compositor-stages-before-draw Chrome flags are always passed (no
    user-facing flag controls them) so icons and webfonts render in every PDF.

    Merge uses pypdf.PdfWriter.append (current API). Falls back to PyPDF2
    PdfMerger if only the older library is installed. PdfMerger was removed
    from pypdf in 5.x, so do not rely on importing it from pypdf in new code.
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# CSS injected into temp HTML copies when --landscape is passed.
# Sized to match the BayOne 16:10 slide aspect (1100px wide / 1.6 = 687.5px tall).
# 11.5in x 7.1875in produces an exact 16:10 page that the slide fills edge to edge
# with no whitespace. Slide navigation buttons are hidden in print.
LANDSCAPE_PAGE_CSS = """
<style id="bayone-pdf-page-sizing">
@page { size: 11.5in 7.1875in; margin: 0; }
@media print {
  body { padding: 0 !important; min-height: 0 !important; background: transparent !important; }
  .slide { width: 100% !important; max-width: none !important; }
  .slide-nav { display: none !important; }
}
</style>
"""


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


def _inject_landscape_css(src_html: Path) -> Path:
    """Write a temp copy of src_html with the landscape page CSS injected.

    The temp file is placed alongside the source so relative asset paths
    (images/, charts/, etc.) continue to resolve. Caller is responsible
    for unlinking the returned path when done.
    """
    content = src_html.read_text()
    if "</head>" in content:
        content = content.replace("</head>", LANDSCAPE_PAGE_CSS + "</head>", 1)
    else:
        content = LANDSCAPE_PAGE_CSS + content
    dest = src_html.parent / f"_pdftmp_{src_html.name}"
    dest.write_text(content)
    return dest


def chrome_to_pdf(html_path: str, pdf_path: str, landscape: bool = False):
    """Convert HTML to PDF using Chrome headless.

    When landscape=True, the source HTML is copied to a temp file with an
    injected @page rule sized to the BayOne 16:10 slide aspect. The original
    HTML is not modified.
    """
    chrome = find_chrome()
    if not chrome:
        raise RuntimeError("Chrome/Chromium not found. Install Chrome or use --engine weasyprint")

    src = Path(html_path).resolve()
    tmp_html = None
    if landscape:
        tmp_html = _inject_landscape_css(src)
        target = tmp_html
    else:
        target = src

    html_url = f"file://{target}"

    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-software-rasterizer",
        # Allow time for CDN fonts (Google Fonts, Font Awesome) and other
        # network assets to load before Chrome snapshots the page. Without
        # these flags, Chrome prints before icons and webfonts render.
        "--virtual-time-budget=15000",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        "--print-to-pdf-no-header",
        html_url,
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Chrome error: {result.stderr}", file=sys.stderr)
            raise RuntimeError(f"Chrome PDF conversion failed")
    finally:
        if tmp_html is not None:
            tmp_html.unlink(missing_ok=True)

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
    """Merge multiple PDFs into one.

    Tries pypdf first (current API uses PdfWriter.append, since PdfMerger was
    removed in pypdf 5.x). Falls back to PyPDF2 (which still ships PdfMerger
    through 3.x) for older environments.
    """
    # pypdf >= 5.x: use PdfWriter, which has an append() method that accepts
    # paths or file-like objects.
    try:
        from pypdf import PdfWriter
        writer = PdfWriter()
        for pdf_path in pdf_paths:
            writer.append(str(pdf_path))
        with open(output_path, "wb") as f:
            writer.write(f)
        return output_path
    except ImportError:
        pass

    # Older fallback path: PyPDF2's PdfMerger.
    try:
        from PyPDF2 import PdfMerger
    except ImportError:
        raise RuntimeError(
            "Neither pypdf nor PyPDF2 is installed. Run: pip install pypdf"
        )

    merger = PdfMerger()
    for pdf_path in pdf_paths:
        merger.append(str(pdf_path))
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
        help="Inject 16:10 landscape page sizing (required for slide decks)"
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
