#!/usr/bin/env python3
"""
Clean Claude Code chat transcripts by removing code snippet lines.

This script creates a cleaned copy of exported Claude Code transcripts,
removing the actual code lines shown during Read/Update/Write operations
while preserving the conversation (user questions and Claude's responses).

Usage:
    python clean_claude_transcript.py <transcript_file>

The cleaned output is saved to <original_name>_cleaned.txt

Original file is NEVER modified.
"""

import re
import sys
from pathlib import Path


def is_code_snippet_line(line: str) -> bool:
    """
    Determine if a line is a code snippet from Read/Update operations.

    The key pattern: Code lines from Read/Update start with 6+ spaces
    followed by a digit (the source file line number). Spacing varies
    based on line number length.

    Examples:
        "        4    from django.db"   -> True (8 spaces + single digit)
        "       287 +  if user.pk:"     -> True (7 spaces + 3 digit number)
        "       300 -  )"               -> True (removal marker)
        "● Read(file.py)"               -> False (Claude statement)
        "  ⎿  Read 50 lines"            -> False (tool summary)
        "> user question"               -> False (user input)

    Also matches:
        - Lines that are just "..." between code sections
    """

    # Empty lines - KEEP
    if not line or not line.strip():
        return False

    # Code lines from Read/Update start with 6+ spaces followed by a digit
    # The spacing varies based on line number length (single digit = more spaces)
    # This captures Read/Update code output
    if re.match(r'^\s{6,}\d', line):
        return True

    # Ellipsis lines showing skipped code sections
    stripped = line.strip()
    if stripped == '...':
        return True

    return False


def clean_transcript(input_path: Path) -> tuple[str, int, int]:
    """
    Clean a Claude transcript by removing code snippet lines.

    Returns:
        tuple: (cleaned_content, original_line_count, removed_line_count)
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    removed_count = 0

    for line in lines:
        if is_code_snippet_line(line):
            removed_count += 1
            continue  # Skip this line

        # Keep the line
        cleaned_lines.append(line)

    return ''.join(cleaned_lines), len(lines), removed_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python clean_claude_transcript.py <transcript_file>")
        print("\nThis creates a cleaned copy with code snippets removed.")
        print("Original file is NEVER modified.")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    # Create output filename
    output_path = input_path.parent / f"{input_path.stem}_cleaned{input_path.suffix}"

    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print()

    # Clean the transcript
    cleaned_content, original_count, removed_count = clean_transcript(input_path)

    # Write output (never touch original!)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    kept_count = original_count - removed_count
    reduction_pct = (removed_count / original_count * 100) if original_count > 0 else 0

    print(f"Original lines:  {original_count:,}")
    print(f"Removed lines:   {removed_count:,} ({reduction_pct:.1f}%)")
    print(f"Kept lines:      {kept_count:,}")
    print()
    print(f"✓ Cleaned transcript saved to: {output_path}")


if __name__ == '__main__':
    main()
