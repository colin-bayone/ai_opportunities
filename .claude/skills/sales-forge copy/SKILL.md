---
name: sales-forge
description: |
  Builds sales proposals, engagement materials, and pitch decks for BayOne Solutions opportunities.
  WHEN to use: User mentions sales proposal, engagement prep, sales pitch, sales deck, new opportunity,
  client proposal, or wants to prepare materials for a prospect meeting.
  WHEN NOT to use: Internal documentation, technical specs not for clients, or non-sales content creation.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*), Task, WebSearch, WebFetch
---

# Sales-Forge

Build compelling sales proposals, pitch decks, and engagement materials from raw context.

## Hard Rules

1. Always create organized folder structure before generating deliverables
2. Research unfamiliar technologies/terms using the sales-research agent
3. Follow BayOne design specs for all HTML output (see `{baseDir}/references/bayone-design-spec.md`)
4. Never fabricate client information - ask if unclear
5. Proposals are proposal-led, not discovery-led (show we did the homework)
6. Check Playwright dependencies before PDF conversion

## Workflow Phases

### Phase 0: Setup

Before first use, verify dependencies:
```bash
python3 {baseDir}/scripts/check_dependencies.py
```

If dependencies missing, run:
```bash
python3 {baseDir}/scripts/install_dependencies.py
```

### Phase 1: Context Ingestion

When user provides context (emails, transcripts, documents):

1. Read all provided source materials
2. Extract and organize:
   - **People**: Names, titles, roles, reporting structure
   - **Company**: Client name, industry, size
   - **Project**: What they're trying to do, timeline, budget hints
   - **Pain points**: Problems they've mentioned
   - **Technical terms**: Technologies, tools, acronyms to research

3. Ask clarifying questions if critical info is missing

### Phase 2: Research

For unfamiliar technologies or terms, spawn the sales-research agent:

```
Use the Task tool with subagent_type="sales-research" to research: [list of terms]
```

The research agent will return concise definitions suitable for a glossary.

### Phase 3: Structured Documentation

Create engagement folder following this structure:

```
{client-name}/
├── 00_index.md              # Navigation hub
├── context/                 # Source materials (user provides)
│   └── additional*/         # Additional context folders as needed
├── project/                 # Current state documents
│   ├── 00_project_overview.md
│   ├── 01_glossary.md
│   ├── 02_pain_points.md
│   ├── 03_scope_and_scale.md
│   └── 04_engagement_timeline.md
├── planning/                # Strategy and approach
│   ├── 00_bayone_positioning.md
│   └── 01_open_questions.md
├── stakeholders/            # People and relationships
│   └── 00_people_directory.md
├── research/                # Investigation materials
└── deliverables/            # Final outputs (proposals, slides)
```

**Document Guidelines:**
- Use snake_case with two-digit prefixes
- Keep each document focused on one topic
- Cross-reference related documents
- Update 00_index.md as documents are created

### Phase 4: User Interview / Strategy

Before generating deliverables, clarify:

1. **Deliverable type**: Proposal (single document) or slides (deck)?
2. **Audience**: VP level? Technical? Executive?
3. **Key message**: What's the one thing they should remember?
4. **Positioning**: What makes BayOne right for this?
5. **Call to action**: What do we want them to do next?

Use AskUserQuestion tool for quick clarification when needed.

### Phase 5: Deliverable Generation

#### For Proposals (Single HTML Document)

Follow the pattern from `{baseDir}/references/proposal-template.md`:
- Cover page with gradient
- Numbered sections (01, 02, 03...)
- Tables for structured data
- Highlight boxes for key points
- Print-optimized CSS

#### For Slide Decks (Multiple HTML Files)

Each slide is a separate HTML file. Follow the pattern from `{baseDir}/references/slide-template.md`:
- One HTML file per slide
- Full-viewport design
- Consistent header/footer
- Print CSS for PDF export

**Slide vs Document HTML Differences:**
- **Slides in HTML**: Decorative border, gradient background container, centered on page
- **Slides in PDF**: Full-bleed, no decorative container, content fills the page
- **Documents**: Same appearance in HTML and PDF

### Phase 6: PDF Conversion

Convert HTML to PDF using Playwright:

```bash
python3 {baseDir}/scripts/html_to_pdf.py <input.html> <output.pdf> [--mode slide|document]
```

**Modes:**
- `document` (default): Standard margins, flows across pages
- `slide`: Each HTML file becomes one full-page slide, landscape orientation

For slide decks, convert each HTML file separately then combine if needed.

### Phase 7: Adaptation

When user provides new information:
1. Identify which documents need updates
2. Update affected documents
3. Note changes in engagement timeline
4. Regenerate deliverables if already created

## Output Formats

| Type | Files | Use Case |
|------|-------|----------|
| Proposal | Single HTML + PDF | Formal proposal document |
| Slide Deck | Multiple HTML + PDFs | Presentation / pitch |
| Documentation Only | Markdown files | Prep work, no deliverable yet |

## Scripts

| Script | Purpose |
|--------|---------|
| `check_dependencies.py` | Verify Playwright is installed |
| `install_dependencies.py` | Install Playwright and browser |
| `html_to_pdf.py` | Convert HTML to PDF |

## References

| Reference | Content |
|-----------|---------|
| `bayone-design-spec.md` | BayOne visual identity and CSS patterns |
| `proposal-template.md` | Proposal HTML structure |
| `slide-template.md` | Slide HTML structure |
| `folder-structure.md` | Standard engagement folder layout |

## Example Session

```
User: I have a new opportunity with Acme Corp. Here are some emails...
[provides context]

Claude: I'll start by reading these materials and setting up an engagement folder.
[creates acme-corp/ folder structure]
[extracts people, project details, pain points]
[spawns research agent for unfamiliar terms]

User: Here's more context from a call yesterday.
[provides additional materials]

Claude: I'll integrate this new information.
[updates relevant documents]

User: I think we're ready for a proposal.

Claude: Before I generate the proposal, a few questions:
- Who's the primary audience?
- What's the key message?
[user answers]

Claude: Generating the proposal now.
[creates deliverables/01_proposal.html]
[converts to PDF]
```
