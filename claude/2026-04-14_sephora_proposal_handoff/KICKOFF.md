# Kickoff: Sephora QE Proposal - Diagram Fix and Final Review

Copy this into a new Claude Code session in the `ai_opportunities` repository.

---

## Context

A previous session built a complete deliverable package for a Sephora QE preliminary approach. The content is done and approved. The one remaining problem is that mermaid diagrams in the architecture detail companion document do not scale to fill the page when printed. This consumed 3+ hours without resolution due to repeated failed attempts and poor decision-making.

## Step 1: Read the handoff

Read `claude/2026-04-14_sephora_proposal_handoff/HANDOFF.md` in full. It contains:
- Complete inventory of all files and their status
- The exact diagram scaling problem and what was tried
- What the research says should work
- What NOT to do (critical behavioral guidance)
- Colin's content feedback and approval status

## Step 2: Read the research

Read these three files. They contain the actual technical knowledge needed to solve the problem:
1. `sephora/qa_qe_playwright/planning/mermaid_svg_scaling_research_2026-04-14.md` - why mermaid SVGs do not scale (inline max-width)
2. `sephora/qa_qe_playwright/planning/svg_scaling_browser_research_2026-04-14.md` - how SVG viewBox/width/height/CSS interact
3. `sephora/qa_qe_playwright/planning/mermaid_flowchart_learnings_2026-04-14.md` - the working mermaid pattern

## Step 3: Read the mermaid shape library

Read all 8 HTML files in `claude/2026-04-13_mermaid_research/shape_library/` to understand mermaid capabilities. The previous session was told to read all 8 and only read 3. Read all of them.

## Step 4: Diagnose in DevTools first

Open `sephora/qa_qe_playwright/deliverables/architecture_detail_v2_2026-04-14.html` in Chrome. Use DevTools to inspect the rendered SVG elements. Understand what attributes mermaid actually set. Experiment with CSS in DevTools to find the combination that makes the SVG fill the available height when printed. The charts are tall and narrow - HEIGHT is the dimension that matters, not width.

Do NOT edit any files until you have confirmed a working approach in DevTools and explained it to me.

## Step 5: After the diagram fix

Once diagrams are fixed:
1. Ask Colin to review `technical_foundation_2026-04-14.html` 
2. Apply the same diagram fix to `technical_foundation_2026-04-14.html` if it has the same issue
3. The three files to send to Vaibhav are listed in the handoff document

## Critical Rules

- Do NOT make decisions without asking. The previous session repeatedly made unilateral decisions that wasted hours.
- Do NOT create experiment files, prototypes, or scratchpad scripts without permission.
- Do NOT run all charts when testing. Run ONE until it works.
- Do NOT conflate viewport size with print output size.
- Ask questions when unsure. The previous session charged ahead repeatedly instead of asking.
