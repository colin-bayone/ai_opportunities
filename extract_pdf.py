#!/usr/bin/env python3
"""
Standalone PDF text extraction script.

Ported from talent_ai/intelligence/extraction/services/document_converter.py.
Strips all Django dependencies — takes a PDF file path in, writes structured output.

Uses PyMuPDF (fitz) as primary extractor with pdfplumber as fallback.

Usage:
    python3 extract_pdf.py <pdf_file_path>
    python3 extract_pdf.py <pdf_file_path> --pages 10-50
    python3 extract_pdf.py <pdf_file_path> --start-page 5 --end-page 20

Output (in auto-created subfolder):
    <pdf_name>.md       — Markdown with ## Page N headers (main output)
    tables.md           — all structured tables, organized by page
    metadata.md         — PDF metadata (title, author, dates)
    <pdf_name>.xhtml    — semi-structured XHTML with page comments
"""

import sys
import os
import io
import html
import re
import time
import json
import argparse
from datetime import datetime
from typing import List, Dict, Any, Optional

# PDF processing libraries
try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False


# ---------------------------------------------------------------------------
# Text cleaning helpers (from document_converter.py)
# ---------------------------------------------------------------------------

def _fix_pymupdf_characters(text: str) -> str:
    """Fix PyMuPDF character corruption issues including ligatures and artifacts."""
    if not text:
        return text

    corrections = {
        'ﬀ': 'ff',
        'ﬁ': 'fi',
        'ﬂ': 'fl',
        'ﬃ': 'ffi',
        'ﬄ': 'ffl',
        'ﬆ': 'st',
        'Ɵ': 'ti',
        'ƞ': 'tf',
        'ƫ': 'tti',
        'Ɨ': 'I',
        'ɨ': 'i',
        '�': 'ti',
    }

    corrected_text = text
    for corrupt_char, correct_char in corrections.items():
        corrected_text = corrected_text.replace(corrupt_char, correct_char)

    corrected_text = corrected_text.replace('CiƟzen', 'Citizen')

    return corrected_text


def _clean_text_content(text: str) -> str:
    """Clean text content by fixing Unicode issues, HTML entities and merging standalone bullets."""
    if not text:
        return text

    text = _fix_pymupdf_characters(text)
    text = text.replace('\uf0b7', '• ')
    text = html.unescape(text)

    bullet_chars = ['•', '·', '▪', '▫', '◦', '‣', '⁃', '○', '●', '▸', '▶', '►', '✓', '✔', '–', '—', '*', '+', 'o']

    lines = text.split('\n')
    merged_lines = []
    i = 0

    while i < len(lines):
        current_line = lines[i]
        stripped = current_line.strip()

        if len(stripped) == 1 and stripped in bullet_chars:
            next_content = None
            j = i + 1
            while j < len(lines):
                if lines[j].strip():
                    next_content = lines[j]
                    break
                j += 1

            if next_content:
                merged_lines.append(f"{stripped} {next_content.strip()}")
                i = j + 1
            else:
                merged_lines.append(current_line)
                i += 1
        else:
            merged_lines.append(current_line)
            i += 1

    result = '\n'.join(merged_lines)
    lines = result.split('\n')
    lines = [line.rstrip() for line in lines]

    cleaned_lines = []
    empty_count = 0

    for line in lines:
        if not line.strip():
            empty_count += 1
            if empty_count <= 2:
                cleaned_lines.append('')
        else:
            empty_count = 0
            cleaned_lines.append(line)

    while len(cleaned_lines) > 1 and not cleaned_lines[0].strip():
        cleaned_lines.pop(0)

    while len(cleaned_lines) > 1 and not cleaned_lines[-1].strip():
        cleaned_lines.pop()

    return '\n'.join(cleaned_lines)


# ---------------------------------------------------------------------------
# Text extraction (PyMuPDF primary path)
# ---------------------------------------------------------------------------

def _extract_text_with_proper_ordering(page) -> str:
    """Extract text with proper spatial ordering to fix content placement issues."""
    blocks = page.get_text("dict", flags=0)

    text_lines = []

    for block in blocks['blocks']:
        if 'lines' in block:
            for line in block['lines']:
                bbox = line['bbox']
                text_parts = []
                for span in line['spans']:
                    if span['text'].strip():
                        text_parts.append(span['text'])

                if text_parts:
                    full_text = ' '.join(text_parts).strip()
                    text_lines.append({
                        'text': full_text,
                        'top': bbox[1],
                        'left': bbox[0],
                        'bottom': bbox[3]
                    })

    line_tolerance = 5
    text_lines.sort(key=lambda x: (round(x['top'] / line_tolerance) * line_tolerance, x['left']))

    return '\n'.join(line['text'] for line in text_lines)


# ---------------------------------------------------------------------------
# Table extraction
# ---------------------------------------------------------------------------

def _is_duplicate_table(new_table, existing_tables: List[dict]) -> bool:
    """Check if a table is a duplicate based on bbox overlap."""
    if not hasattr(new_table, 'bbox') or new_table.bbox is None:
        return False

    new_bbox = new_table.bbox

    for existing in existing_tables:
        if existing.get('bbox') is None:
            continue

        existing_bbox = existing['bbox']

        overlap_x = max(0, min(new_bbox[2], existing_bbox[2]) - max(new_bbox[0], existing_bbox[0]))
        overlap_y = max(0, min(new_bbox[3], existing_bbox[3]) - max(new_bbox[1], existing_bbox[1]))

        if overlap_x > 0 and overlap_y > 0:
            new_area = (new_bbox[2] - new_bbox[0]) * (new_bbox[3] - new_bbox[1])
            existing_area = (existing_bbox[2] - existing_bbox[0]) * (existing_bbox[3] - existing_bbox[1])
            overlap_area = overlap_x * overlap_y

            if (overlap_area / new_area > 0.7) or (overlap_area / existing_area > 0.7):
                return True

    return False


def _extract_tables_comprehensive(page, page_num: int) -> List[dict]:
    """Extract tables using multiple strategies for maximum accuracy."""
    tables = []

    # Strategy 1: Default PyMuPDF detection
    try:
        default_tables = page.find_tables()
        for idx, table in enumerate(default_tables):
            table_data = {
                'page': page_num,
                'table_id': f"p{page_num}_default_t{idx + 1}",
                'extraction_method': 'default',
                'data': table.extract(),
                'bbox': table.bbox,
                'confidence': 'high',
                'markdown': table.to_markdown(),
            }
            tables.append(table_data)
    except Exception:
        pass

    # Strategy 2: Lines-based detection (for bordered tables)
    try:
        lines_tables = page.find_tables(
            vertical_strategy='lines',
            horizontal_strategy='lines'
        )
        for idx, table in enumerate(lines_tables):
            if not _is_duplicate_table(table, [t for t in tables if t['extraction_method'] == 'default']):
                table_data = {
                    'page': page_num,
                    'table_id': f"p{page_num}_lines_t{idx + 1}",
                    'extraction_method': 'lines_based',
                    'data': table.extract(),
                    'bbox': table.bbox,
                    'confidence': 'medium',
                    'markdown': table.to_markdown(),
                }
                tables.append(table_data)
    except Exception:
        pass

    # Strategy 3: Mixed approach (lines vertical, text horizontal)
    try:
        mixed_tables = page.find_tables(
            vertical_strategy='lines',
            horizontal_strategy='text',
            snap_tolerance=3.0
        )
        for idx, table in enumerate(mixed_tables):
            if not _is_duplicate_table(table, tables):
                table_data = {
                    'page': page_num,
                    'table_id': f"p{page_num}_mixed_t{idx + 1}",
                    'extraction_method': 'mixed_lines_text',
                    'data': table.extract(),
                    'bbox': table.bbox,
                    'confidence': 'medium',
                    'markdown': table.to_markdown(),
                }
                tables.append(table_data)
    except Exception:
        pass

    return tables


# ---------------------------------------------------------------------------
# pdfplumber fallback
# ---------------------------------------------------------------------------

def _extract_tables_pdfplumber(page, page_num: int) -> List[dict]:
    """Extract tables using pdfplumber."""
    tables = []
    try:
        raw_tables = page.extract_tables()
        for idx, table_data in enumerate(raw_tables):
            if table_data:
                # Build markdown manually for pdfplumber tables
                md_lines = []
                for row_idx, row in enumerate(table_data):
                    cleaned = [str(c).strip().replace('\n', ' ') if c else '' for c in row]
                    md_lines.append('| ' + ' | '.join(cleaned) + ' |')
                    if row_idx == 0:
                        md_lines.append('| ' + ' | '.join(['---'] * len(cleaned)) + ' |')
                markdown = '\n'.join(md_lines)

                table_info = {
                    'page': page_num,
                    'table_id': f"p{page_num}_pdfplumber_t{idx + 1}",
                    'extraction_method': 'pdfplumber_default',
                    'data': table_data,
                    'bbox': None,
                    'confidence': 'medium',
                    'markdown': markdown,
                }
                tables.append(table_info)
    except Exception:
        pass
    return tables


# ---------------------------------------------------------------------------
# Metadata extraction
# ---------------------------------------------------------------------------

def _extract_metadata(doc, filename: str) -> Dict[str, Any]:
    """Extract PDF metadata from the document."""
    raw = doc.metadata or {}
    return {
        'filename': filename,
        'title': raw.get('title', '') or '',
        'author': raw.get('author', '') or '',
        'subject': raw.get('subject', '') or '',
        'creator': raw.get('creator', '') or '',
        'producer': raw.get('producer', '') or '',
        'creation_date': raw.get('creationDate', '') or '',
        'mod_date': raw.get('modDate', '') or '',
        'total_pages': len(doc),
    }


def _write_metadata_file(metadata: Dict[str, Any], output_dir: str,
                         pages_extracted: int, tables_found: int,
                         start_page: Optional[int], end_page: Optional[int]) -> str:
    """Write metadata to a standalone file."""
    path = os.path.join(output_dir, 'metadata.md')
    lines = [
        f"# Extraction Metadata",
        f"",
        f"## Source Document",
        f"",
        f"- **Filename:** {metadata['filename']}",
        f"- **Title:** {metadata['title'] or '(none)'}",
        f"- **Author:** {metadata['author'] or '(none)'}",
        f"- **Subject:** {metadata['subject'] or '(none)'}",
        f"- **Creator:** {metadata['creator'] or '(none)'}",
        f"- **Producer:** {metadata['producer'] or '(none)'}",
        f"- **Creation Date:** {metadata['creation_date'] or '(none)'}",
        f"- **Modified Date:** {metadata['mod_date'] or '(none)'}",
        f"- **Total Pages:** {metadata['total_pages']}",
        f"",
        f"## Extraction Details",
        f"",
        f"- **Extracted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Pages Extracted:** {pages_extracted}",
        f"- **Tables Found:** {tables_found}",
    ]

    if start_page or end_page:
        lines.append(f"- **Page Range:** {start_page or 1}–{end_page or metadata['total_pages']}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    return path


# ---------------------------------------------------------------------------
# Tables file
# ---------------------------------------------------------------------------

def _write_tables_file(all_tables: List[dict], filename: str, output_dir: str) -> str:
    """Write all structured tables to a separate Markdown file."""
    path = os.path.join(output_dir, 'tables.md')
    lines = [
        f"# Tables: {filename}",
        f"",
        f"Total tables extracted: {len(all_tables)}",
        f"",
    ]

    current_page = None
    for table in all_tables:
        if table['page'] != current_page:
            current_page = table['page']
            lines.append(f"---")
            lines.append(f"")
            lines.append(f"## Page {current_page}")
            lines.append(f"")

        lines.append(f"### {table['table_id']} ({table['extraction_method']}, {table['confidence']} confidence)")
        lines.append(f"")
        lines.append(table.get('markdown', '(no markdown available)'))
        lines.append(f"")

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    return path


# ---------------------------------------------------------------------------
# XHTML extraction (kept from baseline for compatibility)
# ---------------------------------------------------------------------------

def _extract_text_with_proper_ordering_for_xhtml(page) -> str:
    """Extract text using block-level spatial ordering for XHTML output."""
    blocks = page.get_text("dict", flags=0)
    text_blocks = []

    for block in blocks['blocks']:
        if 'lines' in block:
            block_lines = []
            for line in block['lines']:
                line_text = ' '.join(span['text'] for span in line['spans'] if span['text'].strip())
                if line_text:
                    block_lines.append(line_text)

            if block_lines:
                text_blocks.append({
                    'text': '\n'.join(block_lines),
                    'top': block['bbox'][1],
                    'left': block['bbox'][0]
                })

    text_blocks.sort(key=lambda x: (round(x['top'] / 10) * 10, x['left']))

    return '\n\n'.join(block['text'] for block in text_blocks)


def _convert_text_to_xhtml_paragraphs(text: str) -> str:
    """Convert plain text to xHTML paragraphs."""
    xhtml_paragraphs = []
    for line in text.split('\n'):
        line = line.strip()
        if line:
            escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            xhtml_paragraphs.append(f"<p>{escaped_line}</p>")

    return '\n'.join(xhtml_paragraphs)


def _standardize_bullets_universal(content: str) -> str:
    """Convert all bullet symbols to big bullets."""
    bullet_symbols = ['•', '▪', '▫', '◦', '‣', '⁃', '✓', '✅', '⚫', '◯', '○']
    for symbol in bullet_symbols:
        content = content.replace(symbol, '●')

    content = re.sub(r'●\s*([^\s])', r'● \1', content)
    content = re.sub(r'●\s*●+', '●', content)

    return content


def _clean_xhtml_content(html_content: str) -> str:
    """Clean HTML/xHTML content."""
    if not html_content:
        return html_content

    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    html_content = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#(?:\d+|x[0-9a-fA-F]+));)', '&amp;', html_content)

    entity_replacements = {
        '&#x25cf;': '•',
        '&#x2013;': '–',
        '&#x2014;': '—',
        '&#x2022;': '•',
        '&nbsp;': ' ',
    }

    for entity, replacement in entity_replacements.items():
        html_content = html_content.replace(entity, replacement)

    html_content = re.sub(r'<(i|b|em|strong)>\s*</\1>', '', html_content)
    html_content = re.sub(r'[ \t]+', ' ', html_content)
    html_content = re.sub(r'\n\s*\n+', '\n', html_content)
    html_content = re.sub(r'\s+([.,:;!?])', r'\1', html_content)

    html_content = _standardize_bullets_universal(html_content)

    html_content = re.sub(r'<p>[✅●•]\s*</p>', '', html_content)
    html_content = re.sub(r'<p>• [✅●•]\s*', '<p>• ', html_content)

    return html_content


def _create_xhtml_wrapper(content: str, title: str) -> str:
    """Create XHTML wrapper document."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>Extracted Document - {title}</title>
</head>
<body>
{content}
</body>
</html>"""


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------

def extract_pdf(pdf_path: str, start_page: Optional[int] = None,
                end_page: Optional[int] = None) -> None:
    """
    Extract text, tables, metadata, and XHTML from a PDF file.

    Output goes into an auto-created subfolder next to the input PDF.
    """
    if not os.path.isfile(pdf_path):
        print(f"ERROR: File not found: {pdf_path}")
        sys.exit(1)

    if not HAS_PYMUPDF and not HAS_PDFPLUMBER:
        print("ERROR: No PDF processing libraries available. Install pymupdf or pdfplumber.")
        sys.exit(1)

    filename = os.path.basename(pdf_path)
    base_name = os.path.splitext(filename)[0]
    parent_dir = os.path.dirname(os.path.abspath(pdf_path))

    # Create output subfolder
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    output_dir_name = f"{base_name}_PDF_extraction_{timestamp}"
    output_dir = os.path.join(parent_dir, output_dir_name)
    os.makedirs(output_dir, exist_ok=True)

    print(f"Reading: {pdf_path}")
    with open(pdf_path, 'rb') as f:
        pdf_content = f.read()
    print(f"File size: {len(pdf_content) / (1024 * 1024):.1f} MB")
    print(f"Output:  {output_dir}/")

    # Open document to get total page count and metadata
    doc = fitz.open(stream=pdf_content, filetype="pdf")
    total_pages = len(doc)
    metadata = _extract_metadata(doc, filename)

    # Resolve page range
    first_page = max(1, start_page or 1)
    last_page = min(total_pages, end_page or total_pages)

    if first_page > total_pages:
        print(f"ERROR: start-page {first_page} exceeds document length ({total_pages} pages)")
        doc.close()
        sys.exit(1)

    pages_to_process = last_page - first_page + 1
    range_label = f"{first_page}–{last_page}" if (first_page > 1 or last_page < total_pages) else "all"
    print(f"Pages:   {total_pages} total, extracting {pages_to_process} ({range_label})")

    # --- Markdown extraction (streaming write) ---
    print(f"\n--- Markdown Extraction ---")
    md_path = os.path.join(output_dir, f"{base_name}.md")
    all_tables = []
    total_chars = 0
    extraction_start = time.time()

    with open(md_path, 'w', encoding='utf-8') as md_file:
        # Document header
        header = f"# {base_name}\n\n"
        header += f"> **Source:** {filename}  \n"
        header += f"> **Pages:** {total_pages} total"
        if range_label != "all":
            header += f" (extracting {range_label})"
        header += f"  \n"
        header += f"> **Extracted:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        md_file.write(header)

        for page_num in range(first_page, last_page + 1):
            page = doc[page_num - 1]  # fitz uses 0-based indexing

            # Extract text
            if HAS_PYMUPDF:
                raw_text = _extract_text_with_proper_ordering(page)
            else:
                # pdfplumber fallback would need a separate open — skip for now
                raw_text = ""

            clean_text = _clean_text_content(raw_text)

            # Extract tables
            if HAS_PYMUPDF:
                page_tables = _extract_tables_comprehensive(page, page_num)
            else:
                page_tables = []
            all_tables.extend(page_tables)

            # Write page to file (no table duplication — tables go to separate file)
            md_file.write(f"\n---\n\n## Page {page_num}\n\n")
            md_file.write(clean_text)
            md_file.write("\n")
            total_chars += len(clean_text)

            # Progress reporting
            pages_done = page_num - first_page + 1
            pct = pages_done / pages_to_process * 100
            elapsed = time.time() - extraction_start
            tables_on_page = len(page_tables)
            table_note = f" — {tables_on_page} table{'s' if tables_on_page != 1 else ''}" if tables_on_page else ""
            print(f"  Page {page_num}/{last_page} ({pct:.0f}%){table_note}  [{elapsed:.1f}s]",
                  flush=True)

    doc.close()

    elapsed_total = time.time() - extraction_start
    print(f"\nMarkdown:     {total_chars:,} chars, {pages_to_process} pages [{elapsed_total:.1f}s]")
    print(f"Written to:   {md_path}")

    # --- Tables file ---
    if all_tables:
        print(f"\n--- Tables ---")
        tables_path = _write_tables_file(all_tables, filename, output_dir)
        print(f"Tables:       {len(all_tables)} tables extracted")
        print(f"Written to:   {tables_path}")
    else:
        print(f"\nNo tables found.")

    # --- Metadata file ---
    print(f"\n--- Metadata ---")
    meta_path = _write_metadata_file(metadata, output_dir, pages_to_process,
                                      len(all_tables), start_page, end_page)
    print(f"Written to:   {meta_path}")

    # --- XHTML extraction ---
    print(f"\n--- XHTML Extraction ---")
    xhtml_result = _extract_xhtml(pdf_content, filename, first_page, last_page)

    if xhtml_result['success']:
        xhtml_path = os.path.join(output_dir, f"{base_name}.xhtml")
        with open(xhtml_path, 'w', encoding='utf-8') as f:
            f.write(xhtml_result['xhtml'])
        print(f"XHTML:        {xhtml_result['metadata'].get('xhtml_length', 0):,} chars")
        print(f"Written to:   {xhtml_path}")
    else:
        print(f"ERROR: XHTML extraction failed: {xhtml_result.get('error')}")

    print(f"\nDone. All output in: {output_dir}/")


def _extract_xhtml(pdf_content: bytes, filename: str,
                   first_page: int, last_page: int) -> Dict[str, Any]:
    """Extract xHTML from PDF using PyMuPDF for a given page range."""
    if not HAS_PYMUPDF:
        return {'xhtml': '', 'metadata': {}, 'success': False, 'error': 'PyMuPDF not available'}

    try:
        doc = fitz.open(stream=pdf_content, filetype="pdf")
        xhtml_content = []

        for page_num in range(first_page, last_page + 1):
            page = doc[page_num - 1]
            xhtml_text = _extract_text_with_proper_ordering_for_xhtml(page)
            xhtml_cleaned = _clean_text_content(xhtml_text)
            xhtml_paragraphs = _convert_text_to_xhtml_paragraphs(xhtml_cleaned)
            xhtml_content.append(f"<!-- Page {page_num} -->\n" + xhtml_paragraphs)

        doc.close()

        raw_xhtml = '\n'.join(xhtml_content)
        cleaned_xhtml = _clean_xhtml_content(raw_xhtml)
        final_xhtml = _create_xhtml_wrapper(cleaned_xhtml, filename)

        return {
            'xhtml': final_xhtml,
            'metadata': {
                'file_name': filename,
                'file_type': 'pdf',
                'pages': len(xhtml_content),
                'processor': 'PyMuPDF',
                'xhtml_length': len(final_xhtml)
            },
            'success': True,
            'error': None
        }

    except Exception as e:
        return {'xhtml': '', 'metadata': {}, 'success': False, 'error': str(e)}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_page_range(pages_str: str):
    """Parse a page range string like '10-50' into (start, end)."""
    if '-' in pages_str:
        parts = pages_str.split('-', 1)
        return int(parts[0]), int(parts[1])
    else:
        page = int(pages_str)
        return page, page


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract text, tables, and metadata from PDF files.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 extract_pdf.py document.pdf
  python3 extract_pdf.py document.pdf --pages 10-50
  python3 extract_pdf.py document.pdf --start-page 5 --end-page 20
        """
    )
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('--pages', type=str, default=None,
                        help='Page range to extract (e.g., 10-50 or 5)')
    parser.add_argument('--start-page', type=int, default=None,
                        help='First page to extract (1-based)')
    parser.add_argument('--end-page', type=int, default=None,
                        help='Last page to extract (1-based)')

    args = parser.parse_args()

    start = args.start_page
    end = args.end_page

    if args.pages:
        start, end = parse_page_range(args.pages)

    extract_pdf(args.pdf_path, start_page=start, end_page=end)
