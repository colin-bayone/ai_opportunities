# Sales-Forge Merger: Capability Mapping

## Purpose

This document maps every sales-forge capability to its equivalent in singularity, identifies gaps, and specifies what needs to be added to singularity to fully replace sales-forge.

Sales-forge will be deprecated once singularity is working. This is the blueprint for that transition.

---

## Phase-by-Phase Mapping

### Sales-Forge Phase 1: Context Gathering → Singularity: Source Processing + Research Decomposition

| Sales-Forge Creates | Singularity Equivalent | Status |
|---|---|---|
| `00_index.md` (navigation hub) | Not needed. Singularity uses summary docs per set and the reading order in the methodology doc. The blockchain structure IS the index. | **Drop** |
| `stakeholders/00_people_directory.md` | `/<client_name>/<opportunity_name>/org_chart.md` (living doc) + per-set people files in `/<client_name>/<opportunity_name>/research/` | **Covered** (superior: dual system) |
| `project/00_project_overview.md` | Captured in Set 01 research docs (e.g., `01_call_prep_situational_context_<date>.md`). The summary doc for each set serves as the overview at that point in time. | **Covered** (superior: chronological, not static) |
| `project/01_glossary.md` | Not explicitly created. Technical terms are captured in context within research docs. | **Gap - see below** |
| `project/02_pain_points.md` | Captured in research deep dives (e.g., `02_meeting_technical_use_cases_<date>.md`, `02_meeting_what_was_tried_<date>.md`). Pain points are documented in context, not extracted into a separate file. | **Covered** (superior: pain points in context with full detail) |
| `project/03_scope_and_scale.md` | Captured in research deep dives. Scope emerges across multiple docs. | **Covered** |
| `project/04_engagement_timeline.md` | The blockchain itself IS the timeline. Each set is a chronological event. Bridge documents capture what changed between events. | **Covered** (superior: the structure is the timeline) |
| `planning/00_bayone_positioning.md` | Captured in discussion sets (Set 03 type). Strategy and positioning are documented as working discussions. | **Covered** (superior: captures the reasoning, not just the conclusion) |
| `planning/01_open_questions.md` | `/<client_name>/<opportunity_name>/decisions/` folder. Open questions tracked here. Also captured in discussion docs and information request deliverables. | **Covered** |

#### Gap: Glossary

Sales-forge creates a glossary of key terms and definitions, with web research for unfamiliar technologies. Singularity does not have an explicit glossary mechanism.

**Resolution:** Add an optional `/<client_name>/<opportunity_name>/planning/glossary_<date>.md` file. Created when the engagement involves unfamiliar technology or domain-specific terminology. Not required for every engagement. The skill should offer to create it when it encounters terms that need definition during source processing.

---

### Sales-Forge Phase 2: Strategy Development → Singularity: Discussion Sets

| Sales-Forge Does | Singularity Equivalent | Status |
|---|---|---|
| Interactive Q&A about goals, positioning, unique angle | Discussion sets in `/<client_name>/<opportunity_name>/research/`. Example: `03_discussion_strategy_and_deliverables_<date>.md` | **Covered** (superior: captured as append-only research) |
| "What does BayOne want from this engagement?" | Discussion topic, captured in research | **Covered** |
| "What's our unique angle or credibility?" | Discussion topic, captured in research | **Covered** |
| "Who has decision-making authority?" | Org chart + people docs. Authority is tracked per person. | **Covered** |
| "What are the client's explicit asks vs. implicit needs?" | Research deep dives capture both. Discussion sets analyze the gap. | **Covered** |
| "What's the competitive landscape?" | Org chart relationship map section. Also captured in debrief docs (02a type). | **Covered** |
| Updates `planning/00_bayone_positioning.md` | Discussion docs capture positioning decisions with full reasoning. | **Covered** (superior: reasoning preserved) |

**No gaps.** Singularity's discussion mode fully covers sales-forge's strategy development. The difference is that singularity preserves the reasoning chain (why we chose this positioning) rather than just the conclusion.

---

### Sales-Forge Phase 3: Deliverable Creation → Singularity: Deliverables Pipeline

| Sales-Forge Does | Singularity Equivalent | Status |
|---|---|---|
| Asks: what type of deliverable? | Singularity asks the same question. Deliverables are user-directed. | **Covered** |
| Asks: title, subtitle, audience? | Same interaction pattern. | **Covered** |
| Generates proposal HTML from template | Singularity drafts markdown first, then generates HTML using gold standard patterns and the design spec. | **Covered** (superior: markdown source of truth + HTML formatting) |
| Generates individual slide HTML files | **Slide generation moves to a separate slide skill.** Singularity can invoke it. Output goes to `/<client_name>/<opportunity_name>/presentations/`. | **Covered via sibling skill** |
| Standard proposal structure (Cover → Challenge → Approach → Capabilities → Engagement → Why BayOne → Next Steps) | Singularity supports multiple deliverable types, not just proposals. The structure varies by deliverable type (problem restatement, information request, preliminary approach, formal proposal). Gold standards define the patterns. | **Covered** (superior: multiple deliverable types, not one fixed structure) |
| Uses `proposal-template.html` with placeholder variables | Singularity uses the gold standard files in `.claude/skills/singularity/assets/design/gold_standards/` as references, plus the design spec. Not a fill-in-the-blanks template. Deliverables are crafted, not templated. | **Covered** (superior: crafted from research, not templated) |

**Key difference:** Sales-forge uses a single proposal template with placeholder variables (`{{TITLE}}`, `{{CLIENT}}`, etc.) and fills it in. Singularity writes content from the research library and formats it using the design spec and gold standards as style references. This produces more natural, engagement-specific documents rather than template-shaped output.

---

### Sales-Forge Phase 4: Refinement and Export → Singularity: Quality Review + Export

| Sales-Forge Does | Singularity Equivalent | Status |
|---|---|---|
| Present deliverable for feedback | Same interaction pattern. | **Covered** |
| Iterate based on input | Same interaction pattern. | **Covered** |
| Convert to PDF via `html_to_pdf.py` | Script moves to `.claude/skills/singularity/scripts/html_to_pdf.py`. Same capability. | **Covered** |
| No quality review step | Singularity can invoke the big4 skill for quality review before finalizing. | **Singularity is superior** |

---

### Sales-Forge: Handling New Information → Singularity: Append-Only

| Sales-Forge Does | Singularity Equivalent | Status |
|---|---|---|
| Read new source material | Same. New source goes to `/<client_name>/<opportunity_name>/source/`. | **Covered** |
| Identify what's new vs. duplicate | Bridge documents explicitly capture what changed. | **Covered** (superior: changes are documented, not silently merged) |
| Update relevant documentation | New information gets a NEW document set (append-only). Old docs are never edited. | **Covered** (superior: history preserved) |
| Surface key changes to user | Bridge documents and summaries surface changes. | **Covered** |

---

### Sales-Forge: Research Capabilities → Singularity: Research Agents

| Sales-Forge Does | Singularity Equivalent | Status |
|---|---|---|
| WebSearch for unfamiliar technologies | Same capability. Singularity can use WebSearch directly or spawn research agents. | **Covered** |
| Task tool with `research-agent` for deep dives | Same capability. | **Covered** |
| Add findings to glossary | Add findings to `/<client_name>/<opportunity_name>/planning/glossary_<date>.md` (new, see gap above). | **Covered with gap fix** |

---

### Sales-Forge: BayOne Context → Singularity: `.claude/context/`

| Sales-Forge Does | Singularity Equivalent | Status |
|---|---|---|
| Hardcoded team: Colin, Zahra, Neha, Rahul | `.claude/context/bayone_team.md` - living document, grows with the team. | **Covered** (superior: not hardcoded, shared across skills) |
| Hardcoded positioning statements | `.claude/context/bayone_positioning.md` - living document, evolves over time. | **Covered** (superior: not hardcoded, shared across skills) |

---

## What Singularity Adds Beyond Sales-Forge

These are capabilities singularity has that sales-forge does not:

1. **Blockchain methodology** - Append-only, chronological, immutable research record
2. **Multi-pass transcript processing** - Each topic gets a focused read, not a single sweep
3. **Parallel agent execution** - 5+ agents processing a transcript simultaneously
4. **Dual people tracking** - Per-event snapshot + living org chart
5. **Bridge documents** - Explicit "what changed" between events
6. **Pricing workflow** - Full questionnaire, Excel handoff, correction prompts
7. **Multiple deliverable types** - Not just proposals (problem restatements, information requests, technical approaches, follow-up emails)
8. **Session continuity** - Handoff docs, skill notes, methodology anchors
9. **Quality review integration** - big4 skill for polishing
10. **Sibling skill awareness** - pptx-extractor, pdf-extractor, slide skill, big4

---

## Additions to Singularity Spec

Based on this analysis, the following need to be added to the singularity spec:

### 1. Glossary (Optional File)

Add to `03_folder_structure_and_naming.md`:

- `/<client_name>/<opportunity_name>/planning/glossary_<date>.md` as an optional file
- Created when the engagement involves unfamiliar technology or domain-specific terms
- Populated during source processing when unfamiliar terms are encountered
- Updated (not append-only) as new terms are discovered
- Research agents can be spawned to look up definitions

### 2. Strategy Discussion as Standard Set

Add to `02_document_processing_workflow.md`:

When the research library is sufficiently built (typically after 2+ document sets), the skill should proactively offer a strategy discussion covering:
- What does BayOne want from this engagement?
- What is the unique angle or credibility?
- Who has decision-making authority on the client side?
- What are the explicit asks vs. implicit needs?
- What is the competitive landscape?

This is captured as a standard discussion set and feeds directly into deliverable creation.

### 3. Deliverable Type Catalog

Add to `06_deliverables_pipeline.md`:

Expand the deliverable types section with the full catalog of what singularity can produce, with gold standard references for each:

| Deliverable Type | Gold Standard | When to Use |
|---|---|---|
| Problem restatement | `problem_restatement.html` | After discovery, to demonstrate understanding before proposing solutions |
| Information request | `information_request.html` | When specific information is needed from the client to proceed |
| Preliminary approach | `preliminary_approach.html` | Initial solution direction, explicitly framed as preliminary |
| Formal proposal (concise) | `poc_proposal_v5.html` | Scoped engagement with pricing, timeline, and deliverables |
| Formal proposal (detailed) | `poc_proposal_v5_detailed.html` | Extended version with deeper technical justification |
| Follow-up email | (markdown only) | After meetings, to maintain momentum and request next steps |
| Resource plan | `resource_plan_for_cisco.html` (silver) | Staffing and team structure documents |

### 4. Web Research During Source Processing

Add to `02_document_processing_workflow.md`:

During source processing, if the skill encounters unfamiliar technologies, companies, or domain-specific concepts, it should:
1. Flag them to the user
2. Offer to research via WebSearch or research agents
3. Add findings to the glossary if one exists
4. Incorporate context into the relevant research docs

### 5. Proposal Template as Reference (Not Fill-in-the-Blanks)

Clarify in `06_deliverables_pipeline.md`:

The `proposal_template.html` in `.claude/skills/singularity/assets/templates/` is a **structural reference**, not a fill-in-the-blanks template. It shows the standard section order and CSS patterns for proposals. Deliverables are written from the research library using the design spec and gold standards as style guides, not by populating template placeholders.

---

## Deprecation Plan for Sales-Forge

1. **Phase 1:** Build singularity with all capabilities mapped above
2. **Phase 2:** Run singularity on 2-3 real engagements to validate
3. **Phase 3:** Once validated, update sales-forge's SKILL.md trigger to redirect: "This skill has been replaced by singularity. Invoke /singularity instead."
4. **Phase 4:** After confirmation period, archive sales-forge

Sales-forge's assets that move to singularity:
- `assets/templates/proposal-template.html` → `.claude/skills/singularity/assets/templates/proposal_template.html`
- `scripts/html_to_pdf.py` → `.claude/skills/singularity/scripts/html_to_pdf.py`
- `references/bayone-design-spec.md` → `.claude/skills/singularity/assets/design/bayone_design_spec.md` (to be updated by the design spec session)

Sales-forge's assets that move to the slide skill:
- `assets/templates/slide-cover-template.html`
- `assets/templates/slide-content-template.html`
- `references/slide-format.md`
- `scripts/html_to_pdf.py` (copy, both skills get it)
