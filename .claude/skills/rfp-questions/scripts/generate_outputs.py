#!/usr/bin/env python3
"""
Generate RFP question outputs in multiple formats.

Usage: python generate_outputs.py --session-folder <path> --formats markdown,html,csv

Generates final question documents based on the consolidated question list.
"""

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path


def read_state(session_folder: Path) -> dict:
    """Read state.json."""
    state_path = session_folder / "orchestration" / "state.json"
    with open(state_path) as f:
        return json.load(f)


def read_questions(session_folder: Path) -> str:
    """Read the consolidated questions file."""
    # Try different possible locations
    candidates = [
        session_folder / "phase_03_review" / "consolidated_questions_v02.md",
        session_folder / "phase_03_review" / "consolidated_questions_v01.md",
        session_folder / "phase_02_analysis" / "question_catalog_v01.md",
    ]

    for path in candidates:
        if path.exists():
            return path.read_text()

    raise FileNotFoundError("No question file found")


def parse_questions(content: str) -> list[dict]:
    """Parse questions from markdown format into structured data."""
    questions = []

    # Simple regex-based parsing - may need adjustment based on actual format
    # This is a basic implementation; the actual parsing may be more complex

    # Pattern to match question blocks
    pattern = r'###\s+Q(\d+)\s*\n(.*?)(?=###\s+Q\d+|\Z)'

    matches = re.findall(pattern, content, re.DOTALL)

    for num, block in matches:
        q = {
            "number": int(num),
            "text": "",
            "type": "Original",
            "section": "",
            "rfp_reference": "",
            "rfp_location": "",
            "justification": ""
        }

        # Parse fields from block
        for line in block.strip().split('\n'):
            if '|' in line and 'Field' not in line and '---' not in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 2:
                    field, value = parts[0], parts[1]
                    field_lower = field.lower()

                    if 'question' in field_lower:
                        q["text"] = value
                    elif 'type' in field_lower:
                        q["type"] = value
                    elif 'category' in field_lower or 'section' in field_lower:
                        q["section"] = value
                    elif 'reference' in field_lower:
                        q["rfp_reference"] = value
                    elif 'location' in field_lower:
                        q["rfp_location"] = value
                    elif 'justification' in field_lower:
                        q["justification"] = value

        if q["text"]:
            questions.append(q)

    return questions


def generate_markdown(questions: list[dict], state: dict, output_path: Path) -> None:
    """Generate final markdown document."""
    client = state.get("client_name", "Client")
    rfp = state.get("rfp_name", "RFP")

    lines = [
        f"# RFP Clarifying Questions - {client}",
        "",
        f"**RFP:** {rfp}",
        f"**Prepared by:** BayOne Solutions",
        f"**Date:** {datetime.now().strftime('%B %d, %Y')}",
        f"**Total Questions:** {len(questions)}",
        "",
        "---",
        ""
    ]

    # Group by section
    sections = {}
    for q in questions:
        section = q.get("section", "General")
        if section not in sections:
            sections[section] = []
        sections[section].append(q)

    # Generate sections
    for section_name, section_questions in sections.items():
        lines.append(f"## {section_name}")
        lines.append("")

        for q in section_questions:
            lines.append(f"### Q{q['number']}")
            lines.append("")
            lines.append(f"**Question:** {q['text']}")
            lines.append("")
            lines.append(f"**Type:** {q['type']}")
            lines.append("")
            lines.append(f"**RFP Reference:** {q['rfp_reference']}")
            lines.append("")
            if q['rfp_location']:
                lines.append(f"**RFP Location:** {q['rfp_location']}")
                lines.append("")
            lines.append(f"**Justification:** {q['justification']}")
            lines.append("")
            lines.append("---")
            lines.append("")

    output_path.write_text('\n'.join(lines))
    print(f"Generated: {output_path}")


def generate_csv(questions: list[dict], state: dict, output_path: Path) -> None:
    """Generate CSV export."""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # Header
        writer.writerow([
            "#", "Type", "Section", "Question",
            "RFP Reference", "RFP Location", "Justification"
        ])

        # Data rows
        for q in questions:
            writer.writerow([
                q['number'],
                q['type'],
                q['section'],
                q['text'],
                q['rfp_reference'],
                q['rfp_location'],
                q['justification']
            ])

    print(f"Generated: {output_path}")


def generate_html(questions: list[dict], state: dict, output_path: Path, template_path: Path = None) -> None:
    """Generate HTML document following BayOne design spec."""
    client = state.get("client_name", "Client")
    rfp = state.get("rfp_name", "RFP")
    counts = state.get("question_counts", {})

    # Group by section
    sections = {}
    for q in questions:
        section = q.get("section", "General")
        if section not in sections:
            sections[section] = []
        sections[section].append(q)

    # Build HTML (inline template for self-containment)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{client} - RFP Clarifying Questions</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #0f172a;
      --accent: #a855f7;
      --purple-dark: #5b21b6;
      --text: #334155;
      --text-light: #64748b;
      --border: #e2e8f0;
      --bg-subtle: #f8fafc;
      --white: #ffffff;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text);
      line-height: 1.5;
      font-size: 14px;
      background: var(--white);
    }}
    .cover {{
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px;
      background: linear-gradient(135deg, #2e1065 0%, #4c1d95 50%, #6d28d9 100%);
      color: var(--white);
    }}
    .cover h1 {{ font-size: 44px; font-weight: 700; margin-bottom: 24px; }}
    .cover-subtitle {{ font-size: 20px; color: rgba(255,255,255,0.8); margin-bottom: 48px; }}
    .cover-meta {{ display: flex; gap: 48px; padding-top: 48px; border-top: 1px solid rgba(255,255,255,0.15); }}
    .cover-meta-item label {{ font-size: 11px; color: rgba(255,255,255,0.5); text-transform: uppercase; }}
    .cover-meta-item span {{ font-size: 15px; font-weight: 500; }}
    .container {{ max-width: 1000px; margin: 0 auto; padding: 48px 40px; }}
    .summary-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 40px; }}
    .summary-stat {{ text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(124,58,237,0.06), rgba(168,85,247,0.04)); border-radius: 8px; }}
    .summary-stat .value {{ font-size: 28px; font-weight: 700; color: #7c3aed; }}
    .summary-stat .label {{ font-size: 11px; color: var(--text-light); text-transform: uppercase; }}
    .section-header {{ display: flex; align-items: center; gap: 12px; margin: 32px 0 16px; padding-bottom: 8px; border-bottom: 2px solid var(--purple-dark); }}
    .section-num {{ font-size: 11px; font-weight: 700; color: white; background: var(--purple-dark); padding: 4px 10px; border-radius: 4px; }}
    .section-title {{ font-size: 18px; font-weight: 700; }}
    .q-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
    .q-table th {{ text-align: left; padding: 8px 10px; background: #5b21b6; color: white !important; font-size: 10px; text-transform: uppercase; }}
    .q-table td {{ padding: 10px; border-bottom: 1px solid var(--border); vertical-align: top; }}
    .q-table tr:nth-child(even) {{ background: var(--bg-subtle); }}
    .badge {{ display: inline-block; padding: 2px 6px; border-radius: 3px; font-size: 9px; font-weight: 600; text-transform: uppercase; }}
    .badge-original {{ background: #e0e7ff; color: #3730a3; }}
    .badge-revised {{ background: #fef3c7; color: #92400e; }}
    .badge-new {{ background: #d1fae5; color: #065f46; }}
    .footer {{ text-align: center; padding: 32px; border-top: 1px solid var(--border); margin-top: 40px; }}
    @media print {{
      @page {{ size: 8.5in 11in; margin: 0.4in; }}
      .cover {{ height: 10in; page-break-after: always; }}
    }}
  </style>
</head>
<body>
  <div class="cover">
    <div class="cover-content">
      <div style="font-size: 12px; letter-spacing: 3px; text-transform: uppercase; color: #e879f9; margin-bottom: 24px;">RFP Clarifying Questions</div>
      <h1>{client} {rfp}</h1>
      <p class="cover-subtitle">{len(questions)} questions for Q&A submission</p>
      <div class="cover-meta">
        <div class="cover-meta-item"><label>Prepared For</label><br><span>{client}</span></div>
        <div class="cover-meta-item"><label>Submitted By</label><br><span>BayOne Solutions</span></div>
        <div class="cover-meta-item"><label>Date</label><br><span>{datetime.now().strftime('%B %d, %Y')}</span></div>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="summary-grid">
      <div class="summary-stat"><div class="value">{len(questions)}</div><div class="label">Total Questions</div></div>
      <div class="summary-stat"><div class="value">{counts.get('original', 0)}</div><div class="label">Original</div></div>
      <div class="summary-stat"><div class="value">{counts.get('revised', 0)}</div><div class="label">Revised</div></div>
      <div class="summary-stat"><div class="value">{counts.get('new', 0)}</div><div class="label">New</div></div>
    </div>
'''

    # Generate sections
    section_num = 1
    for section_name, section_questions in sections.items():
        html += f'''
    <div class="section-header">
      <span class="section-num">{section_num:02d}</span>
      <span class="section-title">{section_name}</span>
    </div>
    <table class="q-table">
      <thead><tr><th>#</th><th>Type</th><th>Question</th><th>RFP Reference</th><th>Justification</th></tr></thead>
      <tbody>
'''
        for q in section_questions:
            badge_class = f"badge-{q['type'].lower()}"
            html += f'''        <tr>
          <td style="font-weight: 600; color: var(--accent);">{q['number']}</td>
          <td><span class="badge {badge_class}">{q['type']}</span></td>
          <td>{q['text']}</td>
          <td style="font-size: 12px;">{q['rfp_reference']}</td>
          <td style="font-size: 12px;">{q['justification']}</td>
        </tr>
'''
        html += '      </tbody>\n    </table>\n'
        section_num += 1

    html += '''
    <div class="footer">
      <div style="font-size: 18px; font-weight: 700;">Bay<span style="color: #a855f7;">One</span> Solutions</div>
      <p style="font-size: 12px; color: var(--text-light);">Confidential</p>
    </div>
  </div>
</body>
</html>
'''

    output_path.write_text(html)
    print(f"Generated: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate RFP question outputs")
    parser.add_argument("--session-folder", required=True, help="Path to session folder")
    parser.add_argument("--formats", default="markdown", help="Comma-separated formats: markdown,html,csv")

    args = parser.parse_args()

    session_folder = Path(args.session_folder)
    formats = [f.strip().lower() for f in args.formats.split(",")]

    # Read state
    try:
        state = read_state(session_folder)
    except Exception as e:
        print(f"Error reading state: {e}", file=sys.stderr)
        sys.exit(1)

    # Read questions
    try:
        content = read_questions(session_folder)
        questions = parse_questions(content)
    except Exception as e:
        print(f"Error reading questions: {e}", file=sys.stderr)
        sys.exit(1)

    if not questions:
        print("Warning: No questions parsed from input file", file=sys.stderr)

    # Output directory
    output_dir = session_folder / "phase_06_outputs"
    output_dir.mkdir(exist_ok=True)

    # Generate requested formats
    if "markdown" in formats:
        generate_markdown(questions, state, output_dir / "final_questions.md")

    if "csv" in formats:
        generate_csv(questions, state, output_dir / "rfp_questions.csv")

    if "html" in formats:
        generate_html(questions, state, output_dir / "rfp_questions_review.html")

    print(f"\nGenerated {len(formats)} output(s) in {output_dir}")


if __name__ == "__main__":
    main()
