#!/usr/bin/env python3
"""
Format single-line speech-to-text transcripts into readable multi-line files.

Takes a transcript that's one giant line and splits it by:
1. Speaker timestamps (e.g., "Colin Moore   0:45" or "Saurav Kumar Mishra   1:02:05")
2. Sentence boundaries (periods, question marks, exclamation marks)

Creates a new file with _formatted suffix. Never modifies the original.

Usage:
    python format_transcript.py <input_file>
    python format_transcript.py <input_file> <output_file>
"""

import re
import sys
from pathlib import Path


def format_transcript(text: str) -> str:
    """Split a single-line transcript into readable lines."""

    # Pattern for speaker timestamps like "Colin Moore   0:45" or "Saurav Kumar Mishra   1:02:05"
    # Also handles "Transcript" header and "stopped transcription" footer
    speaker_pattern = re.compile(
        r'(?='  # lookahead so we don't consume the match
        r'(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s{2,}\d+:\d{2}(?::\d{2})?)'  # Name   timestamp
        r'|(?:^Transcript$)'  # "Transcript" header
        r'|(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+stopped transcription)'  # "X stopped transcription"
        r')'
    )

    # First pass: split on speaker turns
    parts = speaker_pattern.split(text)

    lines = []
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Check if this is a speaker line (Name   timestamp)
        speaker_match = re.match(
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s{2,}(\d+:\d{2}(?::\d{2})?)$',
            part.split('.')[0].strip() if '.' not in part[:60] else ''
        )

        # Try to separate speaker header from their speech
        full_speaker_match = re.match(
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s{2,}\d+:\d{2}(?::\d{2})?)\s*(.*)',
            part,
            re.DOTALL
        )

        if full_speaker_match:
            speaker_line = full_speaker_match.group(1).strip()
            speech = full_speaker_match.group(2).strip()

            lines.append('')  # blank line before speaker
            lines.append(speaker_line)

            if speech:
                # Split speech into sentences
                sentences = split_sentences(speech)
                for sentence in sentences:
                    sentence = sentence.strip()
                    if sentence:
                        lines.append(sentence)
        else:
            # No speaker header, just split into sentences
            sentences = split_sentences(part)
            for sentence in sentences:
                sentence = sentence.strip()
                if sentence:
                    lines.append(sentence)

    return '\n'.join(lines).strip() + '\n'


def split_sentences(text: str) -> list[str]:
    """Split text on sentence boundaries while keeping the punctuation."""
    # Split on sentence-ending punctuation followed by a space and uppercase letter
    # or followed by a space and common sentence starters
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

    result = []
    for part in parts:
        # Also split on very long runs (>300 chars) at comma boundaries
        if len(part) > 300:
            subparts = re.split(r'(?<=,)\s+', part)
            current = ''
            for sp in subparts:
                if len(current) + len(sp) > 250 and current:
                    result.append(current.strip())
                    current = sp
                else:
                    current = current + ' ' + sp if current else sp
            if current:
                result.append(current.strip())
        else:
            result.append(part)

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python format_transcript.py <input_file> [output_file]")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: {input_path} does not exist")
        sys.exit(1)

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_name(
            input_path.stem + '_formatted' + input_path.suffix
        )

    text = input_path.read_text(encoding='utf-8')
    formatted = format_transcript(text)
    output_path.write_text(formatted, encoding='utf-8')

    # Stats
    original_lines = text.count('\n') + 1
    new_lines = formatted.count('\n') + 1
    print(f"Formatted: {input_path.name}")
    print(f"  Original: {original_lines} lines, {len(text)} chars")
    print(f"  Formatted: {new_lines} lines, {len(formatted)} chars")
    print(f"  Output: {output_path}")


if __name__ == '__main__':
    main()
