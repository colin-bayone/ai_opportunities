# Deliverable Completion Plan

**Document:** preliminary_approach_2026-04-14
**Status:** In progress. Phase 1 complete. Ready for Phase 2 (apply all revisions).
**Last Updated:** 2026-04-14

---

## Current State

- First draft HTML exists (needs revision)
- Architecture content document exists (approved direction, ready to integrate)
- Architecture mermaid diagram drafted
- Round 1 feedback captured and documented
- Gap analysis complete, Colin reviewed and decided on all 40 items (33 included, 5 excluded, 2 skipped)
- Revised outline exists with all structural decisions made
- Title decided: "An Agentic Platform for Quality Engineering"

## Completed Work

### Phase 1: Parallel Research (DONE)

| Task | Status | Output |
|------|--------|--------|
| Mermaid architecture diagram | DONE | `planning/architecture_diagram_draft_2026-04-14.md` |
| Gap analysis | DONE | `planning/gap_analysis_preliminary_approach_2026-04-14.md` |
| Gap analysis decisions | DONE | `research/03_discussion_gap_analysis_decisions_2026-04-14.md` |

---

## Phase 2: Apply All Revisions to HTML (NEXT)

Apply in this order. Each step is discrete and reviewable.

### Step 2a: Cover Page
- Update title to "An Agentic Platform for Quality Engineering"
- Update cover label to "AGENTIC QUALITY ENGINEERING"
- Source: Round 1 feedback, Gap #24

### Step 2b: Table of Contents
- Add after cover page, before Section 01
- Simple navigation listing all section names
- Source: Round 1 feedback, Gap #27

### Step 2c: Section 01 — Problem Summary Rewrite
- Rewrite opening paragraph: industry framing, not Sephora-specific claim (Gap #23)
- Add disclaimer paragraph: current understanding, subject to refinement (Gap #22)
- Add mid-2026 timeline as urgency context (Gap #21)
- Add localization testing as a cross-cutting requirement or in QE card (Gap #4)
- Add A/B testing variant handling in the common requirements area (Gap #1)
- Distinguish nonprod (pre-release validation) from production (anomaly detection) in common requirements (Gap #2)
- Add AI mandate since August 2025 as context (Gap #13, MEDIUM but fits naturally here)
- Expand AMP model context: explain why it matters for testing velocity (Gap #34)
- Add ADA compliance testing as a noted gap the platform architecture supports (Gap #5)
- Sharpen QE card: frame velocity achievement as strategic context, not compliment (Gap #14)

### Step 2d: Section 02 — Full Architecture Rewrite
- Replace entire section with architecture content draft (Gap #30)
- Integrate mermaid diagram showing the five layers
- Add non-destructive guardrails and sandbox escalation (Gap #3)
- Add A/B variant handling in how the platform operates across environments (Gap #1)
- Add production anomaly detection as a distinct operational mode (Gap #2)
- Strengthen codebase mapping / state graph concept in Layer 1 (Gap #6)
- Add recursive downstream dependency coverage model (Gap #7)
- Reframe the unified hub concept (was "control panel"): centralized visibility for all teams and leadership, reduces need for multiple applications, saves time, lessens technical debt (Gap #26, REFRAMED)
- Add bidirectional feedback in confidence scoring (approvals lower threshold, corrections raise it) (Gap #8)
- Add edge case feedback loop as a learning mechanism, not just diagnostic (Gap #9)
- Add QE leads transition to decision-makers as design context for observability (Gap #15)
- Add build-vs-buy alignment: architecture designed for ownership and personalization (Gap #18)
- Add "system autonomy" vs "autonomous systems" distinction (Gap #36)
- Add framework as growth bottleneck insight (Gap #32)
- Add Airflow reference for scheduled test execution (Gap #40)
- List breadth of MCP connectors (Figma, Canva, WordPress) (Gap #38)
- Remove Progressive Buildout (moves to Section 05) (Gap #25)

### Step 2e: Section 03 — Technical Foundation Updates
- Add MCP server as a Sephora organizational requirement, not just a Figma detail (Gap #10)
- Strengthen "practice like we play" proof point (Gap #19)
- Add tool maturity threshold (v1.0 minimum) to the battle-tested framing (Gap #17)
- Add human consistency insight (automated systems can exceed human consistency at scale) (Gap #31)
- Ensure web application / unified hub details are present in the stack table row

### Step 2f: Section 04 — Engagement Models
- Change layout from 3-column to horizontal stacked cards (Gap #28)
- Remove "Outcome-based, not headcount-based" highlight box (Gap #29)

### Step 2g: Section 05 — Implementation Pathway
- Add Progressive Buildout content (moved from Section 02) (Gap #25)
- Add common knowledge base initiative as future exploration area (Gap #16)
- Add expanding quality mandate as future context (Gap #37)

### Step 2h: Section 06 — Preliminary Framing
- No major changes needed

### Step 2i: End of Document
- Add standalone callout for Open WebUI / organizational AI portal collaboration (Gap #33)

---

## Phase 3: Review

| Step | Action |
|------|--------|
| 3a | Colin reviews revised HTML in browser |
| 3b | Address any Round 2 feedback |
| 3c | Offer /big4 quality review before finalizing |

---

## Decision Log

| Decision | Date | Notes |
|----------|------|-------|
| Title: "An Agentic Platform for Quality Engineering" | 2026-04-14 | Cover label: AGENTIC QUALITY ENGINEERING |
| Architecture: five-layer model | 2026-04-14 | Deterministic Automation, Saved Playbooks, Agentic Exploration, Review and Confidence, Observability |
| Problem Summary: industry framing, not Sephora-specific | 2026-04-14 | Do not put words in their mouth |
| Engagement models: horizontal layout | 2026-04-14 | Three-col too narrow |
| Remove outcome-based callout box | 2026-04-14 | Unnecessary, deviates from gold standard |
| Control panel reframed as unified hub | 2026-04-14 | Not removed. Reframed: centralized visibility for all teams and leadership, reduces multiple apps, lessens technical debt |
| Progressive buildout moves to Section 05 | 2026-04-14 | Delivery strategy, not architecture |
| Gap analysis: 33 items included, 5 excluded, 2 skipped | 2026-04-14 | See `research/03_discussion_gap_analysis_decisions_2026-04-14.md` for full decisions |
| Content production = lowest hanging fruit, not highest impact | 2026-04-14 | Sequencing already correctly framed in draft. QE or UI/UX for holistic impact; firm recommendation after deeper dive. |

---

*This is a working document. Updated as work progresses.*
