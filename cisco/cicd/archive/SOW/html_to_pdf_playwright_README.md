# HTML to PDF Converter with Proper Footer Support

## The Problem

HTML documents with CSS `position: absolute` footers break when printed. The browser reflows content for pagination, but absolutely-positioned elements stay anchored to their original container boundaries, causing footers to appear mid-content.

**This is not a CSS problem**. No CSS can make "repeat this element at the bottom of every physical page" work, because:
1. `position: absolute` is relative to the containing element, not the physical printed page
2. Browser print has no concept of repeating elements per physical page
3. CSS `@page` rules with `@bottom-center` have poor browser support

## The Solution

Playwright's `displayHeaderFooter` feature renders headers/footers at the PDF generation layer, outside the HTML content area, on every physical page. This is the correct abstraction level for solving this problem.

## Prerequisites

```bash
pip install playwright
playwright install chromium
```

## Usage

### Basic Conversion

```bash
python3 html_to_pdf_playwright.py input.html output.pdf
```

Default footer: "Confidential" (left) | "Page X of Y" (right)

### Custom Footer Text

```bash
python3 html_to_pdf_playwright.py input.html output.pdf \
    --footer-left "Draft" \
    --footer-right "Page {page}"
```

Placeholders:
- `{page}` - Current page number
- `{pages}` - Total page count

### No Footer

```bash
python3 html_to_pdf_playwright.py input.html output.pdf --no-footer
```

### Custom Margins

```bash
python3 html_to_pdf_playwright.py input.html output.pdf \
    --margin-top 0.5in \
    --margin-bottom 1.5in \
    --margin-left 1in \
    --margin-right 1in
```

## How It Works

1. **Loads HTML** in headless Chromium via Playwright
2. **Injects CSS** to hide HTML-based `.page-footer` elements
3. **Lets content flow naturally** - removes fixed page heights, lets browser paginate
4. **Special handling for cover page** - forces page break after `.cover-page`
5. **Generates PDF** with Playwright's `display_header_footer=True`
6. **Footer template** uses special Playwright CSS classes:
   - `.pageNumber` - replaced with current page
   - `.totalPages` - replaced with total pages

## Key CSS Injected

```css
/* Hide HTML-based footers - Playwright handles this */
.page-footer { display: none !important; }

/* Let content flow naturally */
.page {
    width: auto !important;
    height: auto !important;
    page-break-after: auto !important;
}

/* Cover page stays on its own page */
.cover-page { page-break-after: always !important; }

/* Keep tables/signatures together */
table, .signature-block { page-break-inside: avoid; }
```

## Example: SOW Document

```bash
# Generate SOW PDF with default Confidential footer
python3 html_to_pdf_playwright.py \
    SOW-Building-Nexus-9000-switches-v3.html \
    SOW-Building-Nexus-9000-switches-v3.pdf
```

## Output

The generated PDF will have:
- Clean pagination based on content length
- Footers at the bottom of every physical page
- Cover page isolated on page 1
- Tables and signature blocks kept together when possible

## Troubleshooting

**Blank pages appearing**: Check for unnecessary `page-break-after: always` rules in the source HTML. The script removes them from `.page` but custom classes may still have them.

**Footer not showing**: Ensure `--no-footer` is not set. Check that the margin-bottom is large enough to accommodate the footer (default 1in).

**Fonts not rendering**: Playwright uses system fonts. If custom fonts are needed, ensure they're loaded via web fonts in the HTML.
