# Singularity Skill Extension: Master To-Do List

**Session:** 2026-04-10 (created), 2026-04-13 (organized)
**Goal:** The singularity skill produces work at the quality of the Srinivas deck and the team sub-singularity on command, without substantial problems, on the first try.
**Scope:** Everything in this document gets done. Not a pick-list. The phases are ordered by dependency and value, but every item is committed.

---

## Overview

This to-do list now has six phases, expanded after the 2026-04-13 synthesis (`claude/singularity_feedback/2026-04-13_round_01/00_synthesis.md`). Phase 0 codifies the recurring failure patterns and Hard Rules as the first priority because these have been violated multiple times and block quality output. Phases 1-5 continue as before.

| Phase | Focus | Status |
|-------|-------|--------|
| 0 | Hard Rules and Recurring Failure Prevention | Not started |
| 1 | Gold Standard Establishment | Not started |
| 2 | Nested Singularity Pattern Codification | Not started |
| 3 | Presentation Design Language Hardening | Not started |
| 4 | SKILL.md Integration and Stop Hook Updates | Not started |
| 5 | Mermaid Diagram Polish (visual refinement) | Saved for last |

---

## Phase 0: Hard Rules and Recurring Failure Prevention

**Why first:** The synthesis documented 15 named failure patterns. The skill must enforce these before any new work proceeds. Items here go at the top of SKILL.md as Hard Rules, loaded every invocation.

### 0.1 Create a "Hard Rules" Section at the Top of SKILL.md

- [ ] Add a "Hard Rules — Read Every Invocation" section immediately after the frontmatter
- [ ] This section lists the rules from synthesis §1 (Hard Rules) as numbered, terse, non-negotiable items
- [ ] Each rule gets a one-sentence statement and a reference to where the rationale/longer form lives
- [ ] Include all 15 rules from synthesis §1.1 through §1.15

### 0.2 Codify One-Question-at-a-Time Rule (Recurring Failure #1)

- [ ] **CRITICAL - RECURRING FAILURE:** Synthesis §1.1 + §15.14
- [ ] Add as Hard Rule #1 in SKILL.md: "Ask one question at a time in discussion or clarification contexts. Never present multiple open questions in a single response. If multiple questions exist, pick the most critical one and ask it; queue the rest for follow-up turns."
- [ ] Update Flow 6 (Discussion) to explicitly remove "max 5 questions per batch" language and replace with single-question-per-turn
- [ ] The max-5 rule still applies to written transcript-processing follow-ups where the user can answer in writing; clarify the distinction in both places
- [ ] Apply to Flow 7 (Present) when asking about deck structure, audience, topics
- [ ] Apply anywhere the skill asks clarifying questions

### 0.3 Codify No-Unilateral-Filtering Rule (Recurring Failure #2)

- [ ] **CRITICAL - RECURRING FAILURE:** Synthesis §1.2 + §15.15
- [ ] Add as Hard Rule #2 in SKILL.md: "When the user instructs Claude to explore, inventory, catalog, or search for something, Claude must present the full inventory to the user and await direction before reading, filtering, or prioritizing. Do not use terms like 'most important,' 'most relevant,' 'the key ones,' or 'let me focus on' during inventory presentation unless the user has already provided filtering criteria."
- [ ] Apply to any exploration task: file discovery, transcript cataloging, cross-engagement search, research library review
- [ ] Corollary: if exploration finds items Claude did not previously know about, surface those items first and flag them as new discoveries

### 0.4 Codify Format-Transcripts-First Rule

- [ ] Synthesis §1.3 + §15.10
- [ ] Add as Hard Rule: "When any new raw transcript arrives in source/, the FIRST action is to format it with `format_transcript.py`. No exceptions. Reading raw single-line transcripts is forbidden."
- [ ] Stop hook could verify: if any `.txt` file in a source/ folder was read in this session before it was formatted, flag as violation

### 0.5 Codify Read-Reference-Docs-Before-Describing Rule

- [ ] Synthesis §1.4 + §15.2
- [ ] Add as Hard Rule: "Never describe the structure or content of a reference document without having read it in the current session. Research agent summaries are not substitutes for reading the source."
- [ ] Apply especially to deliverables that will be replicated (getting structure wrong means building the wrong thing)

### 0.6 Codify Use-What-Is-Already-Known Rule

- [ ] Synthesis §1.5 + §15.1
- [ ] Add as Hard Rule: "Before proposing any deliverable, plan, or solution component during Flow 6 (Discussion), verify the proposal against the research library. If a prior set addressed the topic, the proposal must be consistent."
- [ ] The worst failure mode is proposing something the research library contradicts — it undermines confidence in the whole system

### 0.7 Codify Do-Not-Reinvent-Proven-Structure Rule

- [ ] Synthesis §1.6 + §15.3
- [ ] Add as Hard Rule: "When a prior engagement has an established document structure that the user has pointed to as a reference, replicate that structure. Do not ask whether to use it. Do not propose alternatives."

### 0.8 Codify Align-on-Structure-Before-Producing Rule

- [ ] Synthesis §1.7 + §15.8
- [ ] Add as Hard Rule: "Before producing any non-trivial deliverable, propose an outline or structural plan and get user approval. This applies to HTML documents, markdown deliverables, proposals, and summaries."

### 0.9 Codify Decisions-Need-Context Rule

- [ ] Synthesis §1.8 + §15.13
- [ ] Add as Hard Rule: "When presenting a decision to the user about how to handle a file or folder, ALWAYS include: full path, file size, brief content summary (read the file — do not infer from filename), why the decision is needed, proposed options with explicit recommendations."

### 0.10 Codify Do-Not-Declare-Work-Done-Prematurely Rule

- [ ] Synthesis §1.9 + §15.4
- [ ] Add as Hard Rule: "Never declare a task complete, wish the user good luck, or offer closing sentiments unless the user has explicitly said the work is finished. Default posture: more work remains."

### 0.11 Codify Paraphrase-Not-Verbatim Rule

- [ ] Synthesis §1.10 + §15.5
- [ ] Add as Hard Rule: "When capturing user input into research documents, paraphrase into professional prose. Preserve substance, improve clarity. Remove filler, conversational artifacts, and hyperbole."

### 0.12 Codify Verify-Before-Assuming-Files-Identical Rule

- [ ] Synthesis §1.11 + §15.11
- [ ] Add as Hard Rule: "Hash comparison confirms identity. Byte-size comparison does not. When in doubt, format both files and read both in full."

### 0.13 Codify No-Duplicate-Alternates Rule

- [ ] Synthesis §1.12 + §15.12
- [ ] Add as Hard Rule: "Source folders contain ONE copy of each unique file. No duplicates, no alternates, no backups 'in case we need them later.'"

### 0.14 Codify Full-Context-and-Framing Rule

- [ ] Synthesis §1.13 + §15.7
- [ ] Add as Hard Rule: "When raising a topic for discussion, provide full context (what was said, who said it, what it means technically), offer Claude's own perspective and analysis, then ask the user for their take. Terse prompts like 'Item X: Topic. What do you think?' are inadequate."

### 0.15 Codify Check-All-Documents-Not-Just-Flagged Rule

- [ ] Synthesis §1.14 + §15.9
- [ ] Add as Hard Rule: "When anti-patterns are identified in a deliverable, scan the entire document for the same patterns. When a problem is found in one client-facing document, check all client-facing documents. Do not rely on grep alone — read each end to end."

### 0.16 Codify Bring-Perspective-to-Brainstorming Rule

- [ ] Synthesis §1.15 + §15.6
- [ ] Add as Hard Rule: "In brainstorming and discussion mode, Claude brings substantive perspective, proposals, and analysis. Asking the user to direct the next topic without offering insight is interviewing, not brainstorming. Each exchange leads with Claude's perspective and ends with a focused question — never with 'what do you want to discuss next?'"

### 0.17 Add a Hard Rules Proof Check to the Stop Hook

- [ ] After Phase 0 rules are codified in SKILL.md, extend the stop hook to verify the rules section exists and has expected content
- [ ] This is a low-cost structural check that catches accidental removal during SKILL.md edits

---

## Phase 1: Gold Standard Establishment

**Why first:** Downstream references and Flow 7 instructions will point to these gold standards. They need to exist before the references and flows can reference them.

### 1.1 Copy Srinivas Presentation as Gold Standard

- [ ] Create `.claude/skills/singularity/assets/design/gold_standards/presentations/` directory
- [ ] Copy the full Srinivas deck to `.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/`
  - [ ] `00_title.html`
  - [ ] `01_assigned_items_status.html`
  - [ ] `02_discovery_findings_build.html`
  - [ ] `02a_build_ecosystem_diagram.html`
  - [ ] `03_discovery_findings_webex.html`
  - [ ] `04_items_for_discussion.html`
  - [ ] `05_access_status.html`
  - [ ] `06_next_steps.html`
  - [ ] `charts/build_log_ecosystem.html`
- [ ] Write a `README.md` in `gold_standards/presentations/srinivas_status/` explaining what each slide demonstrates: bullets, navigation, status badges, split panels, definition bars, dedicated diagram slide, access status, takeaways, and mermaid integration with full-screen viewer
- [ ] Update `deliverables_pipeline.md` table (if it references gold standards for presentations) to add the presentation gold standard row

### 1.2 Copy Team Sub-Singularity as Worked Example

- [ ] Create `.claude/skills/singularity/references/worked_example_team/` directory
- [ ] Copy `cisco/cicd/team/` contents into it, matching the pattern of the existing `references/worked_example/` (Lam Research)
  - [ ] `source/` with the transcript
  - [ ] `research/` with all 6 files (00 methodology, 01 people/action_items/blockers/technical_discussion/summary)
  - [ ] `tracking/` with action_items.md, blockers.md, decisions.md
  - [ ] `planning/` (can be empty)
  - [ ] `documents/` (can be empty)
  - [ ] `cross_reference.md`
- [ ] Scrub or redact any sensitive internal BayOne details that should not be in the skill asset (e.g., specific individual critiques, internal politics commentary)
- [ ] Write a `README.md` at `worked_example_team/README.md` explaining what this demonstrates: separate numbering chain, team meeting passes, tracking folder dual model, cross-reference to main chain

### 1.3 Copy Build Log Ecosystem Diagram as Chart Gold Standard

- [ ] Create `.claude/skills/singularity/assets/design/gold_standards/charts/` directory
- [ ] Copy `charts/build_log_ecosystem.html` as `gold_standards/charts/example_ecosystem_diagram.html`
- [ ] This serves as the reference for standalone full-screen chart files (back button, theme variables, layout structure)

---

## Phase 2: Nested Singularity Pattern Codification

**Why second:** This is a fundamental structural addition. It needs its own reference files because it is too large for inline inclusion in SKILL.md. The SKILL.md will load these files when the flow is invoked.

### 2.1 Create `references/nested_singularity.md`

- [ ] Source material: `claude/2026-04-10_singularity_nested_design/00_exploration_and_design.md` (extract into skill-appropriate form)
- [ ] Sections to include:
  - [ ] What a sub-singularity is (conceptually)
  - [ ] When to create one (team operations, parallel workstreams, vendor evaluation, discovery sub-tracks)
  - [ ] Folder structure template (source, research, tracking, documents, planning, cross_reference.md)
  - [ ] Numbering rules (independent chain, no relation to parent)
  - [ ] Tracking folder (always created, contents optional)
  - [ ] Documents folder (formatted outputs like HTML reports)
  - [ ] Cross-reference file format (by set number and by topic thread)
  - [ ] Rules: one level of nesting, parent org chart is master, convergence flows upward
  - [ ] How to add a new sub-singularity to an existing engagement
  - [ ] Reference to worked example at `references/worked_example_team/`

### 2.2 Create `references/team_meeting_processing.md`

- [ ] Scope: how to process team standup / team-with-counterpart transcripts through a sub-singularity
- [ ] Standard passes (ordered):
  - [ ] People and dynamics (first file, always)
  - [ ] Action items and assignments (including status of prior-set items)
  - [ ] Blockers, dependencies, escalations
  - [ ] Decisions made and rationale
  - [ ] Technical discussion (only when substantive technical content exists)
  - [ ] Summary (last file, always)
- [ ] How this differs from client-meeting processing in `document_processing.md`
- [ ] Tracking documents to update after processing:
  - [ ] `tracking/action_items.md` format (open, completed, blocked tables)
  - [ ] `tracking/blockers.md` format (active, resolved tables)
  - [ ] `tracking/decisions.md` format (numbered log with rationale)
- [ ] Cross-reference update after each set
- [ ] Bridge documents for team chains (same rules as parent chain: write after two sets exist)

### 2.3 Create `references/tracking_folder_pattern.md`

- [ ] Scope: living operational documents alongside blockchain research
- [ ] Concept: dual model (blockchain audit trail + tracking dashboard)
- [ ] Rules:
  - [ ] Tracking files are living (editable, updated after each research set)
  - [ ] Research files remain immutable and contain the per-meeting record
  - [ ] Every tracking update references the source set
  - [ ] Tracking folder is always created, even if empty at start
- [ ] Templates (copy from `cisco/cicd/team/tracking/` formats)
- [ ] When tracking files are appropriate vs. not (operational sub-singularities yes, pure research sub-singularities can leave them empty)

### 2.4 Update `references/folder_structure.md`

- [ ] Add section: "Sub-Singularity Folder Structure"
- [ ] Add the `documents/` folder description to the sub-singularity template
- [ ] Add the `tracking/` folder description
- [ ] Add the `cross_reference.md` file description
- [ ] Note: main engagement folders do not automatically get a `documents/` folder; that is sub-singularity specific for now
- [ ] Add an example filesystem tree showing `cisco/cicd/` with the team sub-singularity inside

### 2.5 Update `references/complete_structure.md`

- [ ] Add sub-singularity folder structure alongside the main engagement structure
- [ ] Update the "What Lives Where: Decision Guide" table with sub-singularity rows

### 2.6 Update `references/blockchain_methodology.md`

- [ ] Add note: the same blockchain rules apply within each sub-singularity
- [ ] Cross-reference to `nested_singularity.md` for sub-singularity-specific details

---

## Phase 3: Presentation Design Language Hardening

**Why third:** The design language spec exists but is missing the rules we learned through feedback. Without these, fresh sessions will repeat our mistakes.

### 3.1 Update `references/presentation_design_language.md` with Explicit Rules

- [ ] Add rule: "Bullet formatting (.items/.item pattern) is the default for all card bodies, not paragraph text. Paragraphs are acceptable only for short lead paragraphs or takeaway summaries."
- [ ] Add rule: "Navigation (prev/next/home) is mandatory on every slide in a multi-slide deck. First slide has prev disabled. Last slide has next disabled. Home always points to slide 00."
- [ ] Add rule: "When a section has 4+ substantive points or status indicators, give it its own slide rather than cramming into an existing slide."
- [ ] Add rule: "Large diagrams go on their own dedicated slide (02a style), not embedded within content slides."
- [ ] Add rule: "No individual names in slide content. Presenter name is allowed only on the title and closing slides."
- [ ] Add rule: "No direct quotes from any person in any slide."
- [ ] Add rule: "Diplomatic framing for any issue. Problems are presented as 'alignment needed' or 'items for discussion,' not as conflicts or criticisms."
- [ ] Add rule: "Architectural ideas are framed as preliminary or exploratory, not as finalized plans, unless explicitly confirmed."
- [ ] Add rule: "Content must use specific details from the source material. Vague corporate language is a failure mode."
- [ ] Add rule: "Error on more slides rather than dense slides. Density reduces readability."
- [ ] Add a "Common Failure Modes" subsection listing each rule's violation symptoms and how to avoid them

### 3.2 Add the Bullet Item Pattern to the Component Library Section

- [ ] Document the `.items` / `.item` CSS classes explicitly as a component
- [ ] Include CSS snippet
- [ ] Include HTML snippet with bold lead + description pattern
- [ ] Note: bold lead phrase sets the key fact, description elaborates

### 3.3 Add the Slide Navigation Pattern to the Component Library Section

- [ ] Document the `.slide-nav` CSS and HTML as a component
- [ ] Include the full CSS and HTML
- [ ] Include the link-chain rules (first: prev disabled, last: next disabled, home: always slide 00)

### 3.4 Add "Dedicated Diagram Slide" Pattern

- [ ] Document the pattern used in 02a_build_ecosystem_diagram.html
- [ ] Layout: standard header, title + lead centered, diagram fills the content area, "Open full-screen diagram" link, footer
- [ ] When to use: diagram has 4+ nodes, multiple subgraphs, or detail that cannot compress into a compact inline render

### 3.5 Reference the Gold Standard in the Spec

- [ ] Add a section near the top: "Gold Standard Reference"
- [ ] Point to `assets/design/gold_standards/presentations/srinivas_status/`
- [ ] Describe briefly what each slide in the gold standard demonstrates
- [ ] Instruct: before generating a new deck, read the gold standard to see the design language applied end-to-end

---

## Phase 4: SKILL.md Integration and Stop Hook Updates

**Why fourth:** SKILL.md loads the references. All the references need to exist first.

### 4.1 Add Sub-Singularity Section to SKILL.md

- [ ] Location: between Flow 6 (Discussion) and Sibling Skills table
- [ ] Section title: "Sub-Singularities"
- [ ] Brief overview (3-5 sentences) of what sub-singularities are and when to use them
- [ ] List the three main use cases: team operations, parallel workstreams, vendor evaluation
- [ ] Instruct: load `references/nested_singularity.md` and `references/team_meeting_processing.md` and `references/tracking_folder_pattern.md` when creating or processing a sub-singularity
- [ ] Reference the worked example at `references/worked_example_team/`

### 4.2 Update Flow 3 (Process Source Material) in SKILL.md

- [ ] Add branch: if the source material is an internal team meeting, consider routing to a team sub-singularity instead of the main chain
- [ ] Ask the user: "Is this an internal team meeting (should go in `team/`) or a client meeting (should go in the main chain)?"
- [ ] If sub-singularity does not yet exist, offer to create it using the nested_singularity methodology
- [ ] If it exists, process into the sub-singularity's research chain using team_meeting_processing.md passes

### 4.3 Update Flow 7 (Present) in SKILL.md

- [ ] Update the mandatory pre-generation reading to include the gold standard: spec + 3+ examples + the Srinivas gold standard deck
- [ ] Add explicit process step: "Propose the slide list with descriptions and get user approval before generating any HTML"
- [ ] Add explicit rule set from Phase 3.1 (bullets default, nav mandatory, no names, diplomatic framing, specific content, preliminary language for unfinalized ideas)
- [ ] Add step: "If a diagram is needed, propose a chart file in `charts/` and a dedicated diagram slide (02a style). Do not embed diagrams in content slides."
- [ ] Reference `assets/design/gold_standards/charts/example_ecosystem_diagram.html` for the chart file pattern

### 4.4 Update Flow 1 (New Engagement) in SKILL.md

- [ ] Add option: "Does this engagement include team operations that should have a team sub-singularity from the start?"
- [ ] If yes, create the team/ sub-singularity folder structure at engagement creation time
- [ ] Write the team `00_methodology.md` using the team_meeting_processing.md approach

### 4.5 Hook Noise Reduction During Mid-Set Processing

- [ ] Synthesis §14.2 + S2
- [ ] Stop hook currently fires "no summary document found" during legitimate mid-set processing
- [ ] Proposed fix options:
  - Skip warning if most recent file in research/ is dated within current session
  - Only fire warning if no file in research/ has been modified within some recent window
- [ ] Pick one approach and implement
- [ ] (The Hard Rules enforcement items that used to live at 4.5 have been moved to Phase 0 where they belong as priority work)

### 4.6 Update the Stop Hook

- [ ] Add check: if sub-singularity folders exist (detected by `*/team/research/00_methodology_*.md` or similar), verify `references/nested_singularity.md` exists
- [ ] Add check: if presentation HTML exists, verify the gold standard at `assets/design/gold_standards/presentations/srinivas_status/` exists
- [ ] Add check: if `charts/` subfolder exists inside a presentation folder, verify each chart file has a back button element (regex match for `class="back-btn"`)
- [ ] Add check: if presentation HTML contains cards without the `.items` pattern (bullet class) AND has more than N words in a card description, flag as potential paragraph-in-card violation (heuristic)

### 4.7 Update `references/skill_ecosystem.md`

- [ ] Update the presentation slide skill row to point to Flow 7 (it currently may still reference the TBD slide skill)
- [ ] Add row for the nested singularity / team sub-singularity pattern
- [ ] Add note about the gold standard deck availability

### 4.8 Update `references/sales_forge_merger.md` if needed

- [ ] Remove or update any remaining references to "Slide skill (TBD)"
- [ ] Note that slide templates that were planned for the TBD slide skill are now codified in the design language spec and the gold standard

### 4.9 Add Reorganization Flow to SKILL.md

- [ ] Synthesis §13 + S2
- [ ] The `reorganization_guide.md` exists in `references/` but is not yet an official flow in SKILL.md
- [ ] Add Flow 8 (or appropriate number): "Reorganize an existing engagement folder"
- [ ] Flow detects existing folder state (A, B, C, D) and routes to the appropriate phase of the reorganization guide
- [ ] Include the State C validation checklist as a runnable step
- [ ] Consider: can the validation checklist become a script for programmatic verification rather than agent-based judgment?

### 4.10 Flow 4 (Create Deliverable) Asks Client-Facing vs Internal

- [ ] Synthesis §6.3 + S2
- [ ] Current behavior: skill assumes everything in deliverables/ is client-facing
- [ ] Update Flow 4 to ask: "Is this document client-facing or internal-only?"
- [ ] If internal: route to planning/ instead of deliverables/
- [ ] Update folder_structure.md to explicitly define the distinction with examples

### 4.11 Decision on Worked Example Refresh

- [ ] Synthesis §16.7
- [ ] The `worked_example/planning/skill_notes.md` has been marked as frozen-in-time (2026-03-20 snapshot)
- [ ] Question: should the worked example ever be refreshed to a newer snapshot, or remain frozen to preserve a specific teaching moment?
- [ ] If refreshed: when and how? Which version becomes the new snapshot?
- [ ] Colin to decide, then execute

---

## Phase 5: Mermaid Diagram Polish (Saved for Last)

**Why last:** Current mermaid functionality works. The remaining work is visual polish (colors, shapes, professional aesthetic). Explicitly deferred until Phases 1-4 are complete.

### 5.1 Mermaid Design Standards Document

- [ ] Create `references/mermaid_design_standards.md`
- [ ] Goal statement: professional, highly polished, robust diagrams for architecture, application workflows, decision trees, data flows
- [ ] Color palette standards:
  - [ ] Subgraph cluster colors (e.g., blue for code/build, yellow for storage, red for legacy/POC, green for proposed, purple for AI/ML, orange for external)
  - [ ] Node fill + stroke combinations within each cluster family
  - [ ] Edge label backgrounds
  - [ ] Emphasis patterns (how to highlight critical paths)
- [ ] Shape conventions:
  - [ ] Rounded rectangles for services/apps
  - [ ] Rhombus for decisions
  - [ ] Cylinders for databases
  - [ ] Subgraph clusters for logical grouping
- [ ] Line style conventions:
  - [ ] Solid for current/confirmed flows
  - [ ] Dashed for proposed/future flows
  - [ ] Thicker for primary paths, thinner for secondary
- [ ] Typography:
  - [ ] Inter font family via themeVariables
  - [ ] fontSize: 13px for standalone full-screen, 11px for compact inline
  - [ ] Bold for node titles in multi-line nodes, regular for descriptions
- [ ] Layout conventions:
  - [ ] graph TB for top-to-bottom hierarchies
  - [ ] graph LR for sequential processes
  - [ ] When to use each
- [ ] nodeSpacing, rankSpacing, curve style recommendations

### 5.2 Mermaid Chart Gold Standards

- [ ] Create a suite of gold standard chart files in `assets/design/gold_standards/charts/`
- [ ] Each gold standard covers a distinct diagram type:
  - [ ] `example_architecture_diagram.html` (enterprise architecture with clusters, Azure/cloud components, on-prem systems)
  - [ ] `example_workflow_diagram.html` (sequential application workflow with decision points)
  - [ ] `example_ecosystem_diagram.html` (existing — the Cisco build log ecosystem; review and polish)
  - [ ] `example_data_flow_diagram.html` (data pipeline with transformations)
  - [ ] `example_decision_tree.html` (branching logic with outcomes)
- [ ] Each gold standard demonstrates the color palette and shape conventions from 5.1
- [ ] Each includes the back button, the theme initialization, and the layout pattern

### 5.3 Embedded Chart Pattern Documentation

- [ ] Add section to `references/presentation_design_language.md` (or a dedicated `references/mermaid_integration.md`): "Embedded Chart with Full-Screen Viewer"
- [ ] Content: both the inline compact version and the standalone full-screen file must exist together
- [ ] The slide embeds a compact version
- [ ] The `charts/` subfolder holds the full-screen version
- [ ] The link pattern: `<a class="diagram-link" href="charts/name.html" target="_blank">Open full-screen diagram</a>`
- [ ] The full-screen file has the back button
- [ ] When the diagram has fewer than X nodes: compact inline is acceptable
- [ ] When the diagram has X+ nodes or subgraph clusters: dedicated diagram slide is required, with the full-screen version in `charts/`
- [ ] Code examples for both patterns

### 5.4 Mermaid Theme Initialization Reference

- [ ] Create `references/mermaid_theme.md` (or include as a section in mermaid_design_standards.md)
- [ ] Standard theme variables for slides (blue palette)
- [ ] Standard theme variables for long-form documents (purple palette from the Sephora architecture diagram)
- [ ] CSS overrides for SVG text mode (rounded corners, edge label backgrounds)
- [ ] Fallback error message pattern

### 5.5 Update Flow 7 to Use Mermaid Standards

- [ ] After all mermaid gold standards exist, update Flow 7 mandatory reading to include `mermaid_design_standards.md` when the deck will include diagrams
- [ ] Update the stop hook to verify mermaid gold standards exist when charts/ subfolder is present

### 5.6 Polish the Existing Srinivas Chart

- [ ] Revisit `cisco/cicd/presentations/srinivas_status_2026-04-10/charts/build_log_ecosystem.html` with the new standards
- [ ] Apply color palette, shape conventions, line style
- [ ] Propagate polish to the gold standard copy

---

## Cross-Cutting Process Rules (Apply to All Phases)

- [ ] After completing each sub-item, update this document with a status checkmark
- [ ] After completing each sub-section, update `02_skill_improvements_tracker.md` to move items from pending to completed
- [ ] When a new pattern or rule is discovered during the work, add it to the appropriate phase as a new sub-item immediately
- [ ] Do not mark a phase complete until every sub-item is complete
- [ ] After Phase 4 completes, test the skill end-to-end by running a fresh invocation that produces both a sub-singularity and a presentation
- [ ] After Phase 5 completes, test by generating a new diagram from scratch using the standards

---

## Open Questions (Colin to Resolve)

Drawn from synthesis §16 and open_questions document. Each blocks or informs specific items above.

- [ ] **Q1: `client/` folder concept** — Separate sub-singularity, alias for presentations/, or broader concept with transcripts/notes/presentations from client-facing events? Needed for `folder_structure.md` update (affects Phase 2.4).
- [ ] **Q2: Gold standard treatment for deliverables** — Should end-to-end gold standard treatment (like Srinivas deck) also be applied to: problem restatement + info request + preliminary approach as a chain? Formal proposal with pricing? Team status presentation chain showing tracking evolution?
- [ ] **Q3: Depth of methodology enforcement** — Balance of behavioral instructions vs deterministic hook checks. Is current balance right? More checks? Fewer?
- [ ] **Q4: When to offer vs enforce sub-singularity creation** — Always offer at engagement creation? Only when asked? Detect automatically (2+ team meetings implies one)?
- [ ] **Q5: Cross-engagement learning** — Is there a case for a cross-engagement knowledge layer the skill consults? Or is that scope creep?
- [ ] **Q6: Backup and recovery** — If a blockchain file is accidentally modified or deleted, is there a recovery pattern? Should there be?
- [ ] **Q7: Worked example skill_notes refresh policy** — Should the frozen-in-time snapshot ever be refreshed? If so, when and how is the new snapshot chosen?
- [ ] **Q8: Hook noise fix choice** — For mid-set processing hook noise, pick: skip warning if recent file dated within session, OR only fire if no file modified within window.

---

## Success Criteria

Phase 1-4 complete means a fresh Claude session, given only this prompt: "Here's a transcript of my team meeting and a PDF from my team. I need a status deck for my client meeting tomorrow." should produce:

1. A team sub-singularity set with people, action items, blockers, decisions, technical discussion, and summary
2. Updated tracking documents
3. A proposed slide list shared with the user for approval
4. After approval, a complete multi-slide HTML deck with:
   - Proper navigation
   - Bullet formatting throughout
   - Diplomatic framing
   - Specific content drawn from the source material
   - Access status (if applicable) on its own slide
   - Any diagrams on their own dedicated slides with full-screen viewer
5. Quality matching the Srinivas deck

Phase 5 complete means the same prompt produces visually polished, professional-grade diagrams in addition to all of the above.
