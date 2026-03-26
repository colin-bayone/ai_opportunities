#!/usr/bin/env python3
"""
Estimate token count for a file using character count / 4.

Usage:
    python estimate_tokens.py <file_path>
    python estimate_tokens.py <file_path> --warn-threshold 5000
"""

import argparse
import json
import sys
from pathlib import Path


def estimate_tokens(content: str) -> int:
    """Estimate token count as character count / 4."""
    return len(content) // 4


def main():
    parser = argparse.ArgumentParser(description="Estimate token count for a file")
    parser.add_argument("file_path", help="Path to file to analyze")
    parser.add_argument(
        "--warn-threshold",
        type=int,
        default=5000,
        help="Token threshold for warning (default: 5000)",
    )
    args = parser.parse_args()

    file_path = Path(args.file_path)

    if not file_path.exists():
        print(json.dumps({"error": f"File not found: {file_path}"}))
        sys.exit(1)

    content = file_path.read_text()
    char_count = len(content)
    token_estimate = estimate_tokens(content)
    line_count = len(content.splitlines())

    result = {
        "file": str(file_path),
        "characters": char_count,
        "lines": line_count,
        "estimated_tokens": token_estimate,
        "threshold": args.warn_threshold,
        "exceeds_threshold": token_estimate > args.warn_threshold,
    }

    if token_estimate > args.warn_threshold:
        result["warning"] = (
            f"File exceeds recommended {args.warn_threshold} tokens. "
            f"Consider moving content to references/. "
            f"Note: References are loaded on-demand and may not always be called."
        )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
