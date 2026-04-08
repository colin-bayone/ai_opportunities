#!/usr/bin/env python3
"""
HTML to PDF Converter with Proper Footer Support

Uses Playwright's displayHeaderFooter feature to render footers
correctly on every printed page - solving the position:absolute footer
problem that breaks with browser print.

Usage:
    python3 html_to_pdf_playwright.py <input.html> [output.pdf]

Options:
    --no-footer         Disable footer
    --footer-left       Left footer text (default: "Confidential")
    --footer-right      Right footer text (supports {page} and {pages} placeholders)
    --margin-top        Top margin (default: 0.75in)
    --margin-bottom     Bottom margin (default: 1in)
    --margin-left       Left margin (default: 0.75in)
    --margin-right      Right margin (default: 0.75in)
    --footer-font       Footer font family (default: "'Times New Roman', Times, serif")

Examples:
    # Basic conversion with default Confidential / Page X of Y footer
    python3 html_to_pdf_playwright.py SOW.html SOW.pdf

    # Custom footer text
    python3 html_to_pdf_playwright.py SOW.html SOW.pdf --footer-left "Draft" --footer-right "Page {page}"

    # No footer
    python3 html_to_pdf_playwright.py SOW.html SOW.pdf --no-footer
"""

import argparse
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright


def convert_html_to_pdf(
    input_path: str,
    output_path: str = None,
    footer_left: str = "Confidential",
    footer_right: str = "Page {page} of {pages}",
    footer_font: str = "'Times New Roman', Times, serif",
    no_footer: bool = False,
    margin_top: str = "0.75in",
    margin_bottom: str = "1in",
    margin_left: str = "0.75in",
    margin_right: str = "0.75in",
):
    """
    Convert HTML to PDF using Playwright with proper footer support.

    The key insight: Playwright's displayHeaderFooter renders headers/footers
    OUTSIDE the page content area, on every physical page. This solves the
    problem where CSS position:absolute footers end up in the middle of content
    when browser print paginates differently than expected.
    """

    input_path = Path(input_path).resolve()

    if output_path is None:
        output_path = input_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path).resolve()

    # Footer HTML templates
    # These use Playwright's special CSS classes that get replaced with actual values
    # See: https://playwright.dev/python/docs/api/class-page#page-pdf

    footer_template = ""
    if not no_footer:
        # Parse footer_right to replace {page} and {pages} with Playwright's special classes
        right_html = footer_right.replace("{page}", '<span class="pageNumber"></span>')
        right_html = right_html.replace("{pages}", '<span class="totalPages"></span>')

        footer_template = f'''
        <div style="width: 100%; font-size: 10px; font-family: {footer_font};
                    padding: 0 0.75in; display: flex; justify-content: space-between;
                    border-top: 1px solid #ccc; padding-top: 5px; margin-top: 5px;">
            <span>{footer_left}</span>
            <span>{right_html}</span>
        </div>
        '''

    # CSS to inject - hides the HTML-based footers since Playwright will add its own
    # Lets Playwright handle pagination naturally (no forced page breaks)
    hide_html_footers_css = '''
    <style>
        /* Hide HTML-based footers - Playwright's displayHeaderFooter handles this */
        .page-footer {
            display: none !important;
        }
        /* Remove screen-only styling, let content flow naturally */
        .page {
            width: auto !important;
            min-height: auto !important;
            height: auto !important;
            box-shadow: none !important;
            margin: 0 !important;
            padding: 0.3in 0 !important;
            border: none !important;
            page-break-after: auto !important;
            page-break-inside: auto !important;
        }
        /* Cover page needs special handling - it should be its own page */
        .cover-page {
            page-break-after: always !important;
            padding-top: 1.5in !important;
            padding-bottom: 1in !important;
            text-align: center;
        }
        /* Keep tables and signature blocks together when possible */
        table, .signature-block, .totals-section {
            page-break-inside: avoid;
        }
        /* Keep headers with their following content */
        h2, h3, h4 {
            page-break-after: avoid;
        }
    </style>
    '''

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the HTML file
        page.goto(f'file://{input_path}')

        # Inject CSS to hide HTML-based footers
        page.add_style_tag(content=hide_html_footers_css.replace('<style>', '').replace('</style>', ''))

        # Wait for any fonts/images to load
        page.wait_for_load_state('networkidle')

        # Generate PDF with proper footer support
        pdf_options = {
            'path': str(output_path),
            'format': 'Letter',  # 8.5" x 11"
            'print_background': True,
            'margin': {
                'top': margin_top,
                'bottom': margin_bottom,
                'left': margin_left,
                'right': margin_right,
            },
        }

        if not no_footer:
            pdf_options['display_header_footer'] = True
            pdf_options['header_template'] = '<span></span>'  # Empty header
            pdf_options['footer_template'] = footer_template

        page.pdf(**pdf_options)

        browser.close()

    print(f"Created: {output_path}")
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Convert HTML to PDF with proper footer support using Playwright",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument("input", help="Input HTML file")
    parser.add_argument("output", nargs="?", help="Output PDF path (optional)")
    parser.add_argument("--no-footer", action="store_true", help="Disable footer")
    parser.add_argument("--footer-left", default="Confidential", help="Left footer text")
    parser.add_argument("--footer-right", default="Page {page} of {pages}",
                        help="Right footer text ({page} and {pages} are replaced)")
    parser.add_argument("--margin-top", default="0.75in", help="Top margin")
    parser.add_argument("--margin-bottom", default="1in", help="Bottom margin")
    parser.add_argument("--margin-left", default="0.75in", help="Left margin")
    parser.add_argument("--margin-right", default="0.75in", help="Right margin")
    parser.add_argument("--footer-font", default="'Times New Roman', Times, serif",
                        help="Footer font family (default: 'Times New Roman', Times, serif)")

    args = parser.parse_args()

    try:
        convert_html_to_pdf(
            args.input,
            args.output,
            footer_left=args.footer_left,
            footer_right=args.footer_right,
            footer_font=args.footer_font,
            no_footer=args.no_footer,
            margin_top=args.margin_top,
            margin_bottom=args.margin_bottom,
            margin_left=args.margin_left,
            margin_right=args.margin_right,
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
