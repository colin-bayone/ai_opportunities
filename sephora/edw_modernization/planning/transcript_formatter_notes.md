# Note: Transcript Formatter Script

**Date:** 2026-04-02
**Status:** Build quick script now, integrate into singularity skill later

## Problem

Speech-to-text transcript files often arrive as a single giant line with no line breaks. This makes them unreadable by the Read tool (which works line-by-line) and forces workarounds like bash or reading the entire file at once (which hits token limits on long transcripts).

## Solution

Simple Python script that splits on speaker timestamps and sentence boundaries to produce a readable multi-line file. Does not modify the original (source files are never modified per blockchain methodology). Creates a new `_formatted.txt` file alongside the original.

## TODO

- [x] Build script at `sephora/edw_modernization/planning/format_transcript.py`
- [x] Test on Mani meeting 1 transcript
- [ ] After codebase exploration is complete, integrate into singularity skill at `.claude/skills/singularity/scripts/format_transcript.py`
- [ ] Add to singularity skill documentation as a preprocessing step for source materials
