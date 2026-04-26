# Table of Contents

## Foundation Documents

- `about.md` — What this documentation is, what it covers, who it is for, how it is structured.
- `rules.md` — Authoring rules that govern all chapters. Contributors read before adding content.
- `contents.md` — This document. Table of contents and session state.

## Chapters

Chapter numbering is stable once a chapter is in place. New chapters are appended with the next available number. Chapter titles may be refined as the material is written.

| # | Title | Status |
|---|---|---|
| 1 | Discovery | Draft complete |
| 2 | Engagement Context and Research Library Architecture | Draft complete |
| 3 | Handoff Package Assembly | Draft complete |
| 4 | Codebase Analysis Through Structural Artifacts | Draft complete |
| 5 | The Parallel Investigation Pattern | Draft complete |
| 6 | Cross-Repository Synthesis and Mapping | Draft complete |
| 7 | Flag Surfacing and Policy Review | Draft complete |
| 8 | Handoff and Execution Preparation | Draft complete |
| 9 | Scope Discipline as a Working Practice | Draft complete |
| 10 | Uncertainty Management and the Observation–Conclusion Boundary | Draft complete |

The chapter list above is a planning sketch. New chapters may be added as additional phases or disciplines surface in the writing, and the sketch above may be reorganized once the full arc is drafted. The table reflects the current working plan.

## Current State

**Last updated:** 2026-04-22 (end of drafting session, early evening).

**What exists:**
- Three foundation documents: `about.md`, `rules.md`, `contents.md`.
- All ten chapters have a complete first draft on disk.

**What was accomplished in this documentation session:**
- Foundation documents produced.
- Rule 13 (mandatory parallel-agent production workflow with write-capability pilot verification) codified.
- Write-capability pilot verified on disk.
- The reference transcript covering the central working phase was read in full.
- All ten chapters were drafted through three waves of parallel-agent production (Wave 1: chapters 1–3; Wave 2: chapters 4–6; Wave 3: chapters 7–10), reviewed in the main thread for rule compliance between waves, and corrected where violations appeared. Corrections applied: one tool-name reference in Chapter 1 cleaned to the rule-2 alternative; one framework-terminology phrasing in Chapter 3 softened to pure descriptive form; two line-count citations in Chapter 6 rewritten to remove metric claims while preserving the surrounding narrative.

**What a subsequent session would pick up on:**
- A second-pass review of the full set for cross-chapter consistency — shared terminology, transition paragraphs between chapters flowing cleanly, avoiding unintended duplication of content across the cross-cutting chapters (9 and 10) and the phase chapters (3 through 8).
- Any edits the engagement lead requests after reviewing the drafts.
- Optional additions: an introduction/preface document, a glossary, or a reader's map summarizing which chapters to read for different use cases (an internal contributor onboarding onto a similar engagement; a customer-team reader wanting an overview of the methodology; a reader focused on a specific discipline).
- If new engagement activity produces material the documentation should incorporate (an execution-phase retrospective, for example), a new chapter can be appended and the table above updated.

**State notes for continuity:**
- Rule 13 is mandatory. Any session that finds its agents cannot write autonomously stops and flags to the user immediately; no workaround is permitted.
- Wave-based production (two to four parallel chapters per wave) was the pattern used and worked reliably. A subsequent session revising the set can use the same pattern or work single-chapter-at-a-time depending on the scope of changes.
- When a chapter references another chapter (for example, Chapter 5 references Chapter 3, Chapter 10 references Chapter 9), cross-chapter-consistency review should confirm the reference still fits after any revision.
- Common compliance pitfalls encountered during Waves 1–3 and worth watching in future work: tool names leaking in (rule 2), specific line-counts or byte-sizes being cited alongside file paths (rule 3), and "the session" or "the drafting session" slipping into neutral-voice prose (rule 11). A pre-review grep pass against these patterns is a cheap safety check.
