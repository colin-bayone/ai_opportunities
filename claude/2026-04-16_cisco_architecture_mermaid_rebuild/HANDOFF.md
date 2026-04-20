# Handoff: Cisco Build Log Analysis Architecture — Mermaid Rebuild

**Date:** 2026-04-16
**Author:** Colin Moore + Claude (session)
**Status:** Both diagrams complete and approved by Colin

---

## What This Handoff Covers

Namita produced an initial SVG architecture diagram for the Cisco CI/CD build log analysis pipeline. Colin and Claude reviewed it, corrected several architectural issues, and rebuilt it as **two polished Mermaid.js HTML deliverables** in the BayOne design system.

This handoff explains what was built, which file to use when, and the architectural decisions baked in — so a future session picking up this work doesn't re-derive everything or accidentally regress the corrections.

---

## The Two Deliverables

Both files live in `cisco/cicd/deliverables/` and are cross-linked (each has a button in the header pointing at the other).

### 1. Top-to-Bottom (Vertical) — **PRIMARY CHOICE**

**Path:** `cisco/cicd/deliverables/proposed_architecture_mermaid_tb_2026-04-16.html`

- Portrait orientation (8.5 × 11 print)
- 1200 px max-width container
- Main pipeline flows top to bottom: B1 → B2 → B3 Classify → B4 → B5 → B6
- B3 Classification Cascade subgraph stacks the three tiers vertically inside
- External feeds (CATALOG, MYSQL, GIT) positioned around the main flow
- GIT anchored near the bottom via invisible `B5 ~~~ GIT` edge + lengthened `GIT ---> B6`
- **This is the version to use for presentations / printed handouts.** Colin confirmed this one.

### 2. Left-to-Right (Horizontal) — Alternate

**Path:** `cisco/cicd/deliverables/proposed_architecture_mermaid_2026-04-16.html`

- Landscape orientation (11 × 8.5 print)
- 1600 px max-width container
- Same content, same architecture — horizontal arrangement
- Built first as a reference layout; kept for optionality

---

## Architecture as Depicted (What's Actually in the Diagram)

The diagrams show the **corrected** architecture — not Namita's original. Every element below reflects a decision made during the review and is defensible.

### Main Pipeline

1. **B1 · Ingest** — NFS watch of Bazel CI+CD logs. Batched 15–30 min (marked pending). Event-driven retained as future option.
2. **B2 · Parse** — Deterministic chunking only (timestamps, phase delimiters, error prefixes). **No NLP. No summarization.** This is a deliberate correction of Namita's original, which put NLP summarization upstream of the tiers.
3. **B3 · Classification Cascade** — Inverted-pyramid cascade with three tiers:
   - **Tier 1 · Deterministic** — regex + catalog lookup. Handles the bulk of errors at negligible cost.
   - **Tier 2 · ML / NLP** — specialized small model, confidence scoring. Receives only what T1 can't resolve.
   - **Tier 3 · LLM** — root cause analysis, fix suggestion. Receives only novel or compound errors.
   - Cascade is **mutually exclusive**: each error is caught at exactly one tier. The thick `==>` arrows with "if unresolved · escalate" labels make this visually unambiguous.
4. **B4 · Remediate** — Auto-Fix + PR. Consumes classification from whichever tier caught the error. Generates patch, branches, commits, opens PR, triggers build verification, **mandatory human review gate**.
5. **B5 · Storage** — Star schema. Two tables: **classification fact** (1 row per error, written by whichever tier caught it) and **remediation** (keyed by `error_id`, written by B4). Joined at read time.
6. **B6 · Serve** — MCP tools + analytics hooks. Read-path separated from writes; MCP reads from derived views.

### External Feeds

- **Error Catalog Service** — Replaces Namita's brittle "Bazel Docs Scraper." Sourced from Bazel release catalogs (version-locked, low-frequency refresh) + historical Cisco logs. Grows via the `B4 approved fix → CATALOG` feedback edge.
- **MySQL Build Metadata** — build id / timestamp / status, feeds B1 for correlation.
- **Git / GitHub APIs** — commits, diffs, PR review state. Feeds B4 (PR creation) and B6 (live lookups).

### Cross-Cutting

- **Apache Airflow** — Wraps the full pipeline. Provides orchestration, retries, DLQ, SLA monitoring, observability. Represented as a styled banner directly above the diagram card (not a mermaid subgraph — that caused layout issues).

### Feedback Loop

- `B4 approved fix → Error Catalog Service` (dashed edge labeled "promote approved fix") — closes the novel-error loop. When the LLM handles a genuinely novel error and a human approves the PR, the pattern is promoted into the T1 catalog so the next occurrence hits the cheap path.

---

## What Was Corrected vs Namita's Original (Do Not Regress)

| Issue in Namita's diagram | Correction in the rebuild |
|---|---|
| B2 had direct arrows to T1, T2, T3 (contradicting the cascade) | B2 feeds only the CLASSIFY subgraph; cascade is the single routing model |
| NLP chunking / semantic boundaries / summarization all in B2 | B2 is deterministic-only; summarization (if needed) is inside T3 — but the explicit bullet was removed because an LLM doesn't need NLP preprocessing to summarize |
| B5.1 positioned as sub-block of Tier 3 | Promoted to B4 Remediate; it consumes from all tiers |
| Four components (T1/T2/T3/B5.1) shown writing to B6 — Claude initially flagged this as a race / ambiguity problem | **Colin corrected Claude**: the cascade is mutually exclusive, so exactly one tier writes per error. B4 writes to a separate remediation table. No race. See `cisco/cicd/planning/proposed_architecture_review_2026-04-16.md` section 4 for the full discussion. |
| Bazel Docs Scraper as T1 source | Error Catalog Service (hybrid source: Bazel releases + historical logs) |
| No orchestration layer | Apache Airflow banner wraps the pipeline |
| No feedback loop | `B4 → CATALOG` edge promotes approved fixes |

### What Claude Originally Got Wrong (and Colin Corrected)

- **"Star schema is over-engineered"** — It isn't. It's standard dimensional modeling and fits the access patterns. Claude withdrew the concern.
- **"Four writers to B6 creates race conditions"** — Wrong framing. The cascade is exclusive by construction. Do not reintroduce the event-log / append-only framing that Claude had briefly proposed; it was abandoned.
- **Changed MySQL cylinder to rectangle and B6 hexagon to rectangle to make them resize** — Unauthorized reshape. Colin instructed to **resize without reshaping**. The final implementation uses a post-render `getBBox()` + SVG `transform="translate … scale … translate"` with `vector-effect="non-scaling-stroke"` on the path/polygon elements. **Do not change the shapes.**

---

## Technical Notes (If You Need to Edit)

### File Structure

- Both files are fully self-contained HTML — no external assets beyond CDN (Inter font, FontAwesome 6, Mermaid 11).
- BayOne design system is inlined in `<style>`. Purple palette from `.claude/skills/singularity/references/bayone_design_spec.md`.
- Mermaid source is inside `<pre class="mermaid">`. The diagram renders via `mermaid.run({ querySelector: '.mermaid' })` in the bottom `<script>` block.

### Mermaid Config

- `useMaxWidth: false` (we control sizing ourselves via CSS + post-render viewBox recalc)
- `htmlLabels: true` (required for FontAwesome icons and `<b>` / `<br/>` formatting)
- `wrappingWidth: 600`, `rankSpacing: 60–70`, `nodeSpacing: 40–50`
- Theme: base with purple palette overrides

### Post-Render JavaScript (Critical)

The `renderDiagram()` function does three important things after `mermaid.run()`:

1. **Node title styling** — Every `<b>` inside a node is restyled as a boxed title bar (white background, stroke-matched border, tight margin). Rect heights are grown by +20 px to accommodate.
2. **Custom shape resizing** —
   - MySQL node (cylinder, path element) gets a horizontal scale-1.4x transform around its center, with `vector-effect: non-scaling-stroke` to preserve stroke thickness
   - B6 Serve node (hexagon, polygon element) gets a vertical scale-1.35x transform around its center, same stroke preservation
3. **ViewBox recalculation** — `getBBox()` on the SVG, then a tight viewBox with 24 px padding. This ensures the diagram fills the container width without excessive whitespace.

If you modify node content and a node overflows its shape, increase the growth constant (currently +20) rather than reintroducing the height-growth / title-bar-padding guessing from earlier iterations.

### Print Styles

- `@page` size matches orientation (11×8.5 for LR, 8.5×11 for TB)
- Colors forced via `print-color-adjust: exact`
- Page breaks avoided on `.diagram-card`, `.note-card`, etc.
- Diagram scales via SVG's natural aspect ratio + `max-width: 100%`

### CSS Classes That Matter

- `.diagram-group` — wrapper giving the airflow banner + card a shared shadow (visual connection)
- `.airflow-banner` — styled banner above the card; font-size 15 px, weight 600, icon 22 px
- `.mermaid .node foreignObject div` — forces 13 px / 600 weight on all node text
- `.mermaid .node rect, .mermaid .node polygon { rx: 8 }` — rounded corners

---

## Supporting Documents

| Document | Purpose |
|---|---|
| `cisco/cicd/planning/proposed_architecture_review_2026-04-16.md` | Full architecture review discussion — every issue Claude raised, how Colin responded, what was agreed. **Read this before making architectural changes.** |
| `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/Proposed Build Log Analysis Architecture — Blocks 1–7.html` | Namita's original SVG diagram (preserved for reference) |
| `.claude/skills/singularity/references/mermaid_design_standards.md` | Purple-palette theme variables used here |
| `.claude/skills/singularity/references/mermaid_flowchart_learnings.md` | Lessons from Sephora work — especially the title-bar post-render pattern |
| `.claude/skills/singularity/references/mermaid_svg_scaling_research.md` | Why `useMaxWidth: false` + custom viewBox recalc |

---

## Open / Pending Items (Explicit in the Diagram)

These are flagged in the diagram and in the block-by-block notes. A future session may resolve them:

1. **Ingestion mode** — batched 15–30 min vs event-driven. Diagram shows B1 with dashed border (`class B1 pending`). Recommended start: batched. Revisit after queue patterns are known.
2. **CI vs CD log differentiation** — Namita flagged this; may warrant splitting the pipeline. Not resolved; called out in the notes section.
3. **Error Catalog Service scoping** — Sourcing from Bazel source / historical logs / promoted fixes is a sub-project, not a flag-flip. Scope with Srinivas.

---

## Known Constraints / What Not to Do

- **Don't wrap the pipeline in a mermaid subgraph for Airflow.** That approach overlapped content with the multi-line subgraph title. The HTML banner above the card is the correct representation.
- **Don't restructure cross-edges at the individual-tier level** (i.e., `T1 → B4`, `T2 → B4`, `T3 → B4`). That produced 8 cross-subgraph edges and scrambled the cascade layout. The aggregated approach (`CLASSIFY → B4`) is what keeps T1 → T2 → T3 stacked vertically.
- **Don't change MySQL or B6 shapes** to make them resize. The post-render scaling on path/polygon with `non-scaling-stroke` works cleanly. Colin explicitly instructed preservation of the cylinder and hexagon.
- **Don't add NLP to B2** under any framing. Colin was emphatic: deterministic-first, cheap upstream. NLP belongs in Tier 2 only.

---

## Immediate Next Steps (Probable)

1. Embed the TB diagram (or a rendered image export) into the Srinivas primer deck (`cisco/cicd/deliverables/srinivas_primer_2026-04-16.html`) or reference it from there.
2. Prepare a brief talking-script that walks Srinivas's team through: the inverted-pyramid cost argument → the Error Catalog Service → the human review gate on B4 → the feedback loop.
3. Resolve the ingestion mode decision once queue patterns are understood.

---

## Contact Points

- Architecture decisions and rationale: see `cisco/cicd/planning/proposed_architecture_review_2026-04-16.md`
- Namita (original author): owns the first-pass architecture; any substantive structural change should be discussed with her
- Colin: final call on architecture correctness and BayOne positioning
