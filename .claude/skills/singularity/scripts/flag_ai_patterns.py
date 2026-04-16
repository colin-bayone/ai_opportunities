#!/usr/bin/env python3
"""
AI Pattern Flagger - Deterministic pre-scan for quality auditor agent.

Scans a document for common AI writing anti-patterns and outputs flagged
locations for the quality auditor agent to investigate.

Usage:
    python3 flag_ai_patterns.py <file_path>

Output: JSON with flagged items for agent consumption.
"""

import json
import re
import sys
from pathlib import Path


def flag_patterns(file_path: Path) -> dict:
    """Scan file for AI anti-patterns and return flagged locations."""

    content = file_path.read_text()
    lines = content.split('\n')

    flags = []

    # Pattern definitions with severity hints
    patterns = [
        # High priority - almost always problematic
        {
            "name": "contrastive_isnt",
            "regex": r"isn't\s+(?:just\s+)?(?:about\s+)?[\w\s]+[,;]\s*it(?:'s|\s+is)",
            "severity": "high",
            "description": "Contrastive framing: 'isn't X, it's Y'"
        },
        {
            "name": "contrastive_not",
            "regex": r"(?:This|It|That)\s+is\s+not\s+(?:just\s+)?(?:about\s+)?[\w\s]+[,;—]\s*it(?:'s|\s+is)",
            "severity": "high",
            "description": "Contrastive framing: 'not X, it's Y'"
        },
        {
            "name": "more_than_its",
            "regex": r"more\s+than\s+(?:just\s+)?(?:a\s+)?[\w\s]+[,;—]\s*it(?:'s|\s+is)",
            "severity": "high",
            "description": "Contrastive framing: 'more than X, it's Y'"
        },

        # Medium priority - often problematic, needs context
        {
            "name": "isnt_word",
            "regex": r"\bisn't\b",
            "severity": "medium",
            "description": "Contraction 'isn't' - check for contrastive framing"
        },
        {
            "name": "just_word",
            "regex": r"\bjust\b",
            "severity": "medium",
            "description": "Word 'just' - often filler or minimizing"
        },
        {
            "name": "it_is_phrase",
            "regex": r"\bit\s+is\b",
            "severity": "medium",
            "description": "Phrase 'it is' - check for vague reference or contrastive setup"
        },
        {
            "name": "more_than_phrase",
            "regex": r"\bmore\s+than\b",
            "severity": "medium",
            "description": "Phrase 'more than' - check for contrastive framing"
        },

        # Lower priority - context dependent
        {
            "name": "rhetorical_question",
            "regex": r"^[^#].*\?\s*$",
            "severity": "low",
            "description": "Line ends with question mark - may be rhetorical"
        },
        {
            "name": "its_contraction",
            "regex": r"\bit's\b",
            "severity": "low",
            "description": "Contraction 'it's' - verify not part of contrastive frame"
        },
    ]

    for line_num, line in enumerate(lines, 1):
        # Skip code blocks and headers
        if line.strip().startswith('```') or line.strip().startswith('#'):
            continue

        for pattern in patterns:
            matches = list(re.finditer(pattern["regex"], line, re.IGNORECASE))
            for match in matches:
                flags.append({
                    "line": line_num,
                    "column": match.start() + 1,
                    "pattern": pattern["name"],
                    "severity": pattern["severity"],
                    "description": pattern["description"],
                    "matched_text": match.group(),
                    "line_content": line.strip(),
                    "context": get_context(lines, line_num - 1, 1)
                })

    # Deduplicate overlapping flags on same line
    flags = deduplicate_flags(flags)

    # Sort by severity then line number
    severity_order = {"high": 0, "medium": 1, "low": 2}
    flags.sort(key=lambda x: (severity_order[x["severity"]], x["line"]))

    return {
        "file": str(file_path),
        "total_lines": len(lines),
        "total_flags": len(flags),
        "high_severity": len([f for f in flags if f["severity"] == "high"]),
        "medium_severity": len([f for f in flags if f["severity"] == "medium"]),
        "low_severity": len([f for f in flags if f["severity"] == "low"]),
        "flags": flags
    }


def get_context(lines: list, index: int, window: int) -> str:
    """Get surrounding lines for context."""
    start = max(0, index - window)
    end = min(len(lines), index + window + 1)
    context_lines = []
    for i in range(start, end):
        prefix = ">>> " if i == index else "    "
        context_lines.append(f"{i+1:4d}{prefix}{lines[i]}")
    return "\n".join(context_lines)


def deduplicate_flags(flags: list) -> list:
    """Remove lower-severity duplicates when higher-severity pattern matches same text."""
    # Group by line
    by_line = {}
    for flag in flags:
        line = flag["line"]
        if line not in by_line:
            by_line[line] = []
        by_line[line].append(flag)

    result = []
    for line_flags in by_line.values():
        # If we have high severity, skip medium/low that overlap
        high = [f for f in line_flags if f["severity"] == "high"]
        if high:
            result.extend(high)
            # Add non-overlapping medium/low
            for f in line_flags:
                if f["severity"] != "high":
                    overlaps = any(
                        f["column"] >= h["column"] and
                        f["column"] < h["column"] + len(h["matched_text"])
                        for h in high
                    )
                    if not overlaps:
                        result.append(f)
        else:
            result.extend(line_flags)

    return result


def format_for_agent(results: dict) -> str:
    """Format results as markdown for agent consumption."""
    output = []
    output.append(f"# AI Pattern Scan Results")
    output.append(f"")
    output.append(f"**File:** {results['file']}")
    output.append(f"**Total Flags:** {results['total_flags']}")
    output.append(f"- High severity: {results['high_severity']}")
    output.append(f"- Medium severity: {results['medium_severity']}")
    output.append(f"- Low severity: {results['low_severity']}")
    output.append(f"")

    if results['total_flags'] == 0:
        output.append("No patterns flagged. Proceed with holistic review.")
        return "\n".join(output)

    output.append("## Flagged Items")
    output.append("")
    output.append("Review each item below. The script flags potential issues;")
    output.append("use judgment to determine if each is actually problematic.")
    output.append("")

    current_severity = None
    for flag in results['flags']:
        if flag['severity'] != current_severity:
            current_severity = flag['severity']
            output.append(f"### {current_severity.upper()} Severity")
            output.append("")

        output.append(f"**Line {flag['line']}:** {flag['description']}")
        output.append(f"```")
        output.append(flag['context'])
        output.append(f"```")
        output.append(f"Matched: `{flag['matched_text']}`")
        output.append("")

    return "\n".join(output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 flag_ai_patterns.py <file_path> [--json]", file=sys.stderr)
        sys.exit(1)

    file_path = Path(sys.argv[1])
    output_json = "--json" in sys.argv

    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    results = flag_patterns(file_path)

    if output_json:
        print(json.dumps(results, indent=2))
    else:
        print(format_for_agent(results))


if __name__ == "__main__":
    main()
