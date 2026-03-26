---
name: sales-forge
description: |
  Strategic sales engagement preparation and proposal generation for BayOne consulting opportunities.
  WHEN to use: User mentions new client opportunity, engagement prep, proposal creation, sales deck, client presentation, or needs to organize discovery information for a sales pursuit. Also auto-invoke when user provides client emails, meeting transcripts, or context for a new engagement.
  WHEN NOT to use: Existing project work, technical implementation, internal documentation, or non-sales activities.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*), WebSearch, WebFetch, Task
---

# Sales Forge

Strategic engagement preparation and proposal generation for BayOne consulting opportunities.

## Overview

This skill guides the full lifecycle from raw context (emails, transcripts, notes) through structured documentation to polished deliverables (proposals or slide decks).

**Output Formats:**
- **Proposal**: Single multi-section HTML document (e.g., AI acceleration proposal)
- **Slides**: Individual HTML files per slide (e.g., capabilities deck)

---

## Workflow Phases

### Phase 1: Context Gathering

**Objective:** Ingest all available information and organize into structured documentation.

**Standard Documentation Set:**

Create a project folder at the location user specifies (default: same level as source context). Generate these documents:

| Document | Purpose |
|----------|---------|
| `00_index.md` | Navigation hub with quick links |
| `stakeholders/00_people_directory.md` | Names, titles, org structure, relationships |
| `project/00_project_overview.md` | What the engagement is about |
| `project/01_glossary.md` | Key terms and definitions (research if needed) |
| `project/02_pain_points.md` | Problems, opportunities, blockers |
| `project/03_scope_and_scale.md` | Quantified metrics, timeline, scale |
| `project/04_engagement_timeline.md` | Chronological history of interactions |
| `planning/00_bayone_positioning.md` | How we position ourselves |
| `planning/01_open_questions.md` | Gaps to fill, questions to answer |

**Actions:**
1. Read all source documents provided by user
2. Extract people, roles, and organizational relationships
3. Research unfamiliar terms/technologies using WebSearch
4. Create structured documentation in parallel where possible
5. Use Task tool with `research-agent` for technology deep dives

**STOP after Phase 1:** Present summary of what was captured. Ask if user has additional context before proceeding.

---

### Phase 2: Strategy Development

**Objective:** Understand user's goals, positioning, and approach.

**Key Questions to Explore:**
- What does BayOne want from this engagement? (Staffing? Solutions? Advisory?)
- What's our unique angle or credibility?
- Who has decision-making authority?
- What are the client's explicit asks vs. implicit needs?
- What's the competitive landscape?

**Actions:**
1. Review documented pain points and opportunities
2. Interview user about goals if not clear from context
3. Help brainstorm positioning if needed
4. Update `planning/00_bayone_positioning.md` with strategy
5. Identify key messages for deliverable

**STOP after Phase 2:** Confirm strategic direction before creating deliverables.

---

### Phase 3: Deliverable Creation

**Objective:** Generate polished client-facing documents.

**Before starting, ask:**
1. What type of deliverable? (Proposal / Slides / Both)
2. What's the title and subtitle?
3. Who is the audience? (VP level? Technical? Executive?)
4. Any specific sections or content to include?

#### For Proposals

Single HTML document with multiple sections. Follow BayOne design spec.

**Standard Structure:**
1. Cover page with title, subtitle, client name, date
2. Executive summary / The Challenge
3. Our Approach
4. Capabilities mapped to their needs
5. Proposed Engagement (phased approach)
6. Why BayOne
7. Next Steps
8. Footer

**Reference:** `{baseDir}/references/bayone-design-spec.md`

#### For Slides

Individual HTML files, one per slide. Each slide is self-contained.

**Standard Structure:**
- `01_cover.html` - Title slide
- `02_challenge.html` - Problem statement
- `03_approach.html` - Our methodology
- `04_XX.html` - Content slides
- `NN_next_steps.html` - Call to action

**Reference:** `{baseDir}/references/slide-format.md`

---

### Phase 4: Refinement and Export

**Actions:**
1. Present deliverable to user for feedback
2. Iterate based on input
3. Convert to PDF if requested using `{baseDir}/scripts/html_to_pdf.py`

---

## Handling New Information

When user provides additional context mid-workflow:
1. Read the new source material
2. Identify what's new vs. duplicate
3. Update relevant documentation (don't overwrite—edit existing files)
4. Surface key changes to user
5. Adjust strategy if new info changes the picture

---

## Research Capabilities

For unfamiliar technologies, companies, or domains:
- Use WebSearch for current information
- Use Task tool with `research-agent` for deep dives
- Add findings to glossary document
- Cite sources where relevant

---

## BayOne Context

**Core Team:**
- Colin Moore - Director of AI (technical lead, subject matter expert)
- Zahra Syed - Director, Strategic Accounts (sales lead)
- Neha Malhotra - Head of Recruiting (staffing)
- Rahul - President

**Positioning:**
- Not just a staffing firm—strategic AI and data engineering partner
- Colin's experience at Coherent provides credibility for BI/data migrations
- Proposal-led conversations, not blank-slate discovery
- Tool-agnostic, honest brokers

---

## File References

- Design specification: `{baseDir}/references/bayone-design-spec.md`
- Slide format guide: `{baseDir}/references/slide-format.md`
- PDF conversion script: `{baseDir}/scripts/html_to_pdf.py`

---

## Quick Start Examples

**User provides emails about new opportunity:**
```
"Here are some emails about a new Sephora opportunity: [path]"
→ Phase 1: Read emails, create documentation structure, research technologies
→ Phase 1 complete, ask for additional context
```

**User wants to create proposal:**
```
"Let's create a proposal for Sephora"
→ Confirm Phase 1+2 complete
→ Ask about format, title, audience
→ Generate HTML proposal
```

**User provides new info mid-stream:**
```
"Here's another document: [path]"
→ Read, identify new info, update relevant docs, surface changes
```
