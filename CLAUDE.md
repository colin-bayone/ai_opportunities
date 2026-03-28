# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **sales and consulting knowledge base** for BayOne Solutions' AI practice, managed by Colin Moore (Director of AI). It contains client opportunity research, meeting transcripts, proposals, RFP responses, deliverables, and session archives — not a software project with build/test/lint commands.

## Repository Structure

The repo is organized by **client/opportunity** at the top level, with a shared resources directory:

- **`ai_docs/`** — BayOne company-wide reference materials: capabilities, use cases, Colin's profile, and session guides. These are source-of-truth documents used across opportunities.
- **`specs/`** — BayOne design system (`bayone-design-spec.md`) and branded HTML templates. All client-facing HTML deliverables should follow this design spec (Big Four consulting aesthetic, purple brand palette).
- **`claude/`** — Claude Code session archive. Date-prefixed subdirectories contain session outputs (slides, analyses, skill prototypes). `SESSIONS/` holds exported conversation transcripts. `_cleaned` suffix = processed by `clean_claude_transcript.py`.

### Client Directories

Each client directory follows a similar pattern of `context/` (source materials), `project/` or `docs/` (structured knowledge), `planning/` (strategy), and `deliverables/` (outputs):

- **`sephora/`** — EDW Modernization engagement (largest, most structured). Has its own `00_index.md` navigation file.
- **`cisco/`** — CI/CD consulting engagement.
- **`mcgrath/`** — RFP response (managed services). `rfp_docs/` contains the source RFP, analysis, and developed questions.
- **`zeblock/`** — Zeblok partnership exploration. Executive summary HTML deliverables.
- **`tailored_brands/`** — Meeting transcripts from discovery calls.

## Key Files

- **`clean_claude_transcript.py`** — Standalone Python script that strips code-snippet lines from exported Claude Code transcripts, producing `_cleaned.txt` versions. Usage: `python clean_claude_transcript.py <transcript_file>`
- **`specs/bayone-design-spec.md`** — Full CSS design system for branded HTML documents. Reference this when creating any client-facing HTML deliverable.
- **`ai_docs/bayone_capabilities.md`** — Comprehensive capabilities list. Reference when positioning BayOne for new opportunities.
- **`ai_docs/colin-moore-profile4.md`** — Colin's professional profile for proposals and bios.

## Working Conventions

- Client-facing HTML deliverables use the BayOne design spec (purple palette, Big Four consulting style). See `specs/bayone-design-spec.md`.
- Session work products go in `claude/` with date-prefixed directory names (`YYYY-MM-DD_description`).
- Source materials (emails, transcripts, meeting notes) go in each client's `context/` directory.
- Structured knowledge extraction goes in `project/` or `docs/` subdirectories with numbered filenames for ordering.
- The `sephora/` directory uses `00_index.md` as a navigation hub — maintain this pattern if adding similar index files to other clients.
