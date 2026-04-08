#!/usr/bin/env python3
"""
Playwright script to capture screenshots of HTML documents for visual review.

Supports multiple viewport modes and overlapping captures for long pages.
Respects Claude API limit: max 8000px on any dimension.
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import sys

# HTML documents to review
DOCUMENTS = [
    # Meeting 1 (CI/CD Kickoff with Anand/Srini/Divakar)
    "meeting1_anand_srini_divakar/00_meeting_breakdown.html",
    "meeting1_anand_srini_divakar/01_speaker_notes.html",
    "meeting1_anand_srini_divakar/02_sentiment_and_relationship.html",
    # Meeting 2 (Regression Testing with Rama)
    "meeting2_rama/00_meeting_breakdown.html",
    "meeting2_rama/01_crossover_analysis.html",
    "meeting2_rama/02_speaker_notes.html",
    "meeting2_rama/03_sentiment_and_relationship.html",
]

BASE_DIR = Path(__file__).parent
SCREENSHOTS_DIR = BASE_DIR / "screenshots"

# Claude API limit
MAX_DIMENSION = 8000

# Viewport modes
MODES = {
    "portrait": {
        "width": 1020,
        "height": 1320,
        "description": "8.5x11 print document ratio",
    },
    "landscape_4x3": {
        "width": 1280,
        "height": 960,
        "description": "Standard 4:3 screen",
    },
    "landscape_hd": {
        "width": 1920,
        "height": 1080,
        "description": "16:9 HD screen",
    },
}

DEFAULT_MODE = "portrait"
DEFAULT_OVERLAP = 200  # pixels of overlap between consecutive captures


def validate_dimensions(width: int, height: int) -> bool:
    """Check that dimensions respect the 8000px API limit."""
    if width > MAX_DIMENSION:
        print(f"ERROR: Width {width}px exceeds {MAX_DIMENSION}px limit")
        return False
    if height > MAX_DIMENSION:
        print(f"ERROR: Height {height}px exceeds {MAX_DIMENSION}px limit")
        return False
    return True


def capture_screenshots(
    doc_indices: list[int] | None = None,
    mode: str = DEFAULT_MODE,
    overlap: int = DEFAULT_OVERLAP,
):
    """
    Capture screenshots of specified documents.

    Args:
        doc_indices: List of document indices to capture (None = all)
        mode: Viewport mode - 'portrait', 'landscape_4x3', or 'landscape_hd'
        overlap: Pixels of overlap between consecutive captures
    """
    if mode not in MODES:
        print(f"ERROR: Unknown mode '{mode}'. Available: {list(MODES.keys())}")
        return

    viewport = MODES[mode]
    vp_width = viewport["width"]
    vp_height = viewport["height"]

    # Validate viewport dimensions
    if not validate_dimensions(vp_width, vp_height):
        print("Fix viewport dimensions in MODES config")
        return

    SCREENSHOTS_DIR.mkdir(exist_ok=True)

    # If no indices specified, capture all
    if doc_indices is None:
        doc_indices = list(range(len(DOCUMENTS)))

    # Calculate scroll step (viewport height minus overlap)
    scroll_step = vp_height - overlap
    if scroll_step <= 0:
        print(f"ERROR: Overlap ({overlap}px) must be less than viewport height ({vp_height}px)")
        return

    print(f"Mode: {mode} ({vp_width}x{vp_height}) - {viewport['description']}")
    print(f"Overlap: {overlap}px, Scroll step: {scroll_step}px\n")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for idx in doc_indices:
            if idx < 0 or idx >= len(DOCUMENTS):
                print(f"Skipping invalid index: {idx}")
                continue

            doc_path = DOCUMENTS[idx]
            html_file = BASE_DIR / doc_path

            if not html_file.exists():
                print(f"File not found: {html_file}")
                continue

            # Create page with configured viewport
            page = browser.new_page(viewport={"width": vp_width, "height": vp_height})

            # Load the HTML file
            page.goto(f"file://{html_file.absolute()}")

            # Wait for fonts and styles to load
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(500)

            # Get total page height
            page_height = page.evaluate("document.body.scrollHeight")

            # Generate base screenshot filename
            base_name = doc_path.replace("/", "_").replace(".html", "")

            print(f"{doc_path}")
            print(f"  Page height: {page_height}px")

            if page_height <= vp_height:
                # Single screenshot - page fits in viewport
                screenshot_path = SCREENSHOTS_DIR / f"{base_name}.png"
                page.screenshot(path=str(screenshot_path), full_page=True)
                print(f"  Captured: {screenshot_path.name}")
            else:
                # Multiple screenshots with overlap
                num_captures = ((page_height - vp_height) // scroll_step) + 2
                print(f"  Capturing {num_captures} screenshots with {overlap}px overlap")

                for i in range(num_captures):
                    y_offset = i * scroll_step

                    # Don't scroll past the end
                    max_scroll = page_height - vp_height
                    if y_offset > max_scroll:
                        y_offset = max_scroll

                    # Skip if we've already captured this position
                    if i > 0 and y_offset >= max_scroll and (i - 1) * scroll_step >= max_scroll:
                        break

                    # Scroll to position
                    page.evaluate(f"window.scrollTo(0, {y_offset})")
                    page.wait_for_timeout(150)

                    screenshot_path = SCREENSHOTS_DIR / f"{base_name}_{i + 1:02d}.png"
                    page.screenshot(path=str(screenshot_path), full_page=False)
                    print(f"  Captured: {screenshot_path.name} (y={y_offset})")

            page.close()

        browser.close()

    print(f"\nScreenshots saved to: {SCREENSHOTS_DIR}")


def print_usage():
    """Print usage information."""
    print("Usage: python screenshot_capture.py [options] [doc_indices...]")
    print()
    print("Options:")
    print("  --mode MODE      Viewport mode (default: portrait)")
    print("  --overlap PX     Overlap between captures in pixels (default: 200)")
    print("  --list           List available documents and modes")
    print()
    print("Examples:")
    print("  python screenshot_capture.py                    # All docs, portrait mode")
    print("  python screenshot_capture.py 0                  # First doc only")
    print("  python screenshot_capture.py --mode landscape_4x3 0 1")
    print("  python screenshot_capture.py --overlap 300 0")


def print_list():
    """List available documents and modes."""
    print("Documents:")
    for i, doc in enumerate(DOCUMENTS):
        print(f"  {i}: {doc}")
    print()
    print("Modes:")
    for name, config in MODES.items():
        print(f"  {name}: {config['width']}x{config['height']} - {config['description']}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print_usage()
        sys.exit(0)

    if "--list" in args:
        print_list()
        sys.exit(0)

    # Parse arguments
    mode = DEFAULT_MODE
    overlap = DEFAULT_OVERLAP
    indices = []

    i = 0
    while i < len(args):
        if args[i] == "--mode" and i + 1 < len(args):
            mode = args[i + 1]
            i += 2
        elif args[i] == "--overlap" and i + 1 < len(args):
            overlap = int(args[i + 1])
            i += 2
        else:
            try:
                indices.append(int(args[i]))
            except ValueError:
                print(f"Unknown argument: {args[i]}")
                print_usage()
                sys.exit(1)
            i += 1

    # Run capture
    capture_screenshots(
        doc_indices=indices if indices else None,
        mode=mode,
        overlap=overlap,
    )
