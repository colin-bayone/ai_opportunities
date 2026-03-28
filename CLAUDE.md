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

- **`sephora/`** — EDW Modernization engagement (largest, most structured). Has its own `00_index.md` navigation file. 7 related session folders in `claude/`.
- **`cisco/`** — CI/CD consulting engagement (NX-OS pipeline improvement) + EPNM-to-EMS UI conversion (separate engagement). 6 related session folders.
- **`mcgrath/`** — RFP response (managed services). `rfp_docs/` contains the source RFP, analysis, and developed questions. Slide deck rebuild in `claude/`.
- **`ariat/`** — India GCC setup (scaling 30→200 people, 18 months). Primary opportunity: managed testing transformation. Has `00_index.md`. 3 related session folders.
- **`lam_research/`** — IP protection / NER-redaction for $17B semiconductor company. Discovery complete March 2026. Has `00_index.md`. 2 related session folders.
- **`tailored_brands/`** — Discovery meeting prep for Men's Wearhouse / Joseph A. Bank parent ($75M tech investment, QA gaps).
- **`zeblock/`** — Zeblok partnership exploration. Executive summary HTML deliverables.
- **`bayone/`** — Internal BayOne AI practice materials: `processes/` (AI lead qualification framework), `positioning/` (capabilities deck, portfolio catalog), `hiring/` (Technical Manager JD). Has `00_index.md`.

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
