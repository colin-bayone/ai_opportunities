#!/usr/bin/env python3
"""
SOW Document Render Script

Combines YAML data with Jinja2 template to produce HTML.
Optionally generates PDF via the Playwright utility.

Usage:
    # Render HTML only
    python3 render_sow.py data.yaml output.html

    # Render HTML and generate PDF
    python3 render_sow.py data.yaml output.html --pdf

    # Use custom template
    python3 render_sow.py data.yaml output.html --template custom-template.html

    # Specify total pages (for screen footer display)
    python3 render_sow.py data.yaml output.html --total-pages 12
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    print("Error: Jinja2 not installed. Run: pip install jinja2")
    sys.exit(1)


def load_yaml(yaml_path: Path) -> dict:
    """Load and parse YAML data file."""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def count_page_divs(html: str) -> int:
    """Count the number of <div class="page"> elements in rendered HTML."""
    # Match <div class="page"> or <div class="page cover-page"> etc.
    pattern = r'<div\s+class="[^"]*\bpage\b[^"]*"'
    matches = re.findall(pattern, html)
    return len(matches)


def render_template(template_path: Path, data: dict, total_pages: int = None) -> str:
    """Render Jinja2 template with YAML data."""
    template_dir = template_path.parent
    template_name = template_path.name

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )

    template = env.get_template(template_name)

    # First render pass (with placeholder for total_pages if not specified)
    render_data = {**data, 'total_pages': total_pages or '??'}
    html = template.render(**render_data)

    # If total_pages wasn't specified, count page divs and re-render
    if total_pages is None:
        calculated_pages = count_page_divs(html)
        render_data['total_pages'] = calculated_pages
        html = template.render(**render_data)

    return html


def generate_pdf(html_path: Path, pdf_path: Path, script_dir: Path) -> bool:
    """Generate PDF using the Playwright utility."""
    playwright_script = script_dir.parent / 'html_to_pdf_playwright.py'

    if not playwright_script.exists():
        print(f"Warning: Playwright script not found at {playwright_script}")
        print("PDF generation skipped. Run manually with html_to_pdf_playwright.py")
        return False

    try:
        result = subprocess.run(
            ['python3', str(playwright_script), str(html_path), str(pdf_path)],
            capture_output=True,
            text=True,
            cwd=script_dir.parent
        )

        if result.returncode == 0:
            print(f"PDF generated: {pdf_path}")
            return True
        else:
            print(f"PDF generation failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"PDF generation error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Render SOW document from YAML data and Jinja2 template',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        'yaml_file',
        type=Path,
        help='Path to YAML data file'
    )

    parser.add_argument(
        'output_html',
        type=Path,
        help='Path for output HTML file'
    )

    parser.add_argument(
        '--template', '-t',
        type=Path,
        default=None,
        help='Path to Jinja2 template (default: sow-template.html in same directory)'
    )

    parser.add_argument(
        '--pdf', '-p',
        action='store_true',
        help='Also generate PDF using Playwright utility'
    )

    parser.add_argument(
        '--total-pages',
        type=int,
        default=None,
        help='Total page count for footer (auto-calculated if not specified)'
    )

    args = parser.parse_args()

    # Resolve paths
    script_dir = Path(__file__).parent.resolve()
    yaml_path = args.yaml_file.resolve()
    output_path = args.output_html.resolve()

    # Default template path
    if args.template:
        template_path = args.template.resolve()
    else:
        template_path = script_dir / 'sow-template.html'

    # Validate inputs
    if not yaml_path.exists():
        print(f"Error: YAML file not found: {yaml_path}")
        sys.exit(1)

    if not template_path.exists():
        print(f"Error: Template file not found: {template_path}")
        sys.exit(1)

    # Load YAML data
    print(f"Loading data from: {yaml_path}")
    data = load_yaml(yaml_path)

    # Render template
    print(f"Rendering template: {template_path}")
    html = render_template(template_path, data, args.total_pages)

    # Write output HTML
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTML generated: {output_path}")

    # Generate PDF if requested
    if args.pdf:
        pdf_path = output_path.with_suffix('.pdf')
        generate_pdf(output_path, pdf_path, script_dir)

    print("Done.")


if __name__ == '__main__':
    main()
