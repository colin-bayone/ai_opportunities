---
name: phoenix-theme-skill
description: |
  Assists developers working with the Phoenix Bootstrap theme v1.23.0 in Django projects.
  Use for mockup analysis, component discovery, greenfield UI development, aligning existing
  interfaces with Phoenix, or brainstorming component options.

  This skill orchestrates specialized sub-agents for different tasks:
  - phoenix-catalog-explorer: Search the 219-page Phoenix catalog
  - phoenix-screenshot-analyzer: Analyze mockup images
  - phoenix-template-generator: Create Django templates with HTMX
  - phoenix-pattern-validator: Verify compliance with Phoenix patterns
  - phoenix-django-explorer: Explore Django models/views/data for UI suggestions
  - phoenix-chart-advisor: Recommend charts based on available data (interactive)
  - phoenix-implementation-planner: Create handoff documentation for implementation

  Strictly uses Phoenix theme components with HTMX - never custom implementations.
---

# Phoenix Theme Development Skill

## QUICK START - Read This First

### How to Find Phoenix Components

**Step 1: Read the category summary file** (small, fast, always works):
```
Read .claude/skills/phoenix-theme-skill/data/summaries/phoenix_apps.md      # Email, chat, CRM, etc.
Read .claude/skills/phoenix-theme-skill/data/summaries/phoenix_components.md # Cards, modals, buttons
Read .claude/skills/phoenix-theme-skill/data/summaries/phoenix_tables.md     # Tables
Read .claude/skills/phoenix-theme-skill/data/summaries/phoenix_charts.md     # ECharts
Read .claude/skills/phoenix-theme-skill/data/summaries/phoenix_forms.md      # Form inputs
Read .claude/skills/phoenix-theme-skill/data/summaries/00_index.md           # Full index
```

**Step 2: For detailed catalog search, use the query script**:
```bash
poetry run python .claude/skills/phoenix-theme-skill/scripts/02_query_catalog.py search email
poetry run python .claude/skills/phoenix-theme-skill/scripts/02_query_catalog.py category apps
poetry run python .claude/skills/phoenix-theme-skill/scripts/02_query_catalog.py tags table sorting
```

**Step 3: For complex work, delegate to sub-agents** via Task tool:
- `phoenix-catalog-explorer` - Deep catalog search
- `phoenix-template-generator` - Create Django templates
- `phoenix-pattern-validator` - Validate existing templates
- `phoenix-django-explorer` - Explore Django models/views

### File Size Warnings

| File Type | Size | Action |
|-----------|------|--------|
| `data/summaries/*.md` | 2-15 KB | Safe to Read directly |
| `references/*.md` | 5-15 KB | Safe to Read directly |
| `data/phoenix_catalog.json` | ~160 KB | Use query script, NOT Read |
| `data/components/full_pages/*.html` | 400-700 KB | NEVER Read directly |

### Common Phoenix Email Pages

| Page | URL |
|------|-----|
| Inbox | https://prium.github.io/phoenix/v1.23.0/apps/email/inbox.html |
| Compose | https://prium.github.io/phoenix/v1.23.0/apps/email/compose.html |
| Email Detail | https://prium.github.io/phoenix/v1.23.0/apps/email/email-detail.html |

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│              Phoenix Theme Skill (Orchestrator)                  │
│                                                                 │
│  • Read summary files directly for quick lookups                │
│  • Use query script for catalog searches                        │
│  • Delegate to sub-agents for complex/heavy work                │
│  • Synthesize results and present options                       │
└─────────────────────────────────────────────────────────────────┘
                              │
    ┌──────────┬──────────┬───┴───┬──────────┬──────────┐
    │          │          │       │          │          │
    ▼          ▼          ▼       ▼          ▼          ▼
┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
│Catalog ││Screen- ││Template││Pattern ││Django  ││ Chart  │
│Explorer││shot    ││Genera- ││Valida- ││Explorer││Advisor │
│        ││Analyzer││tor     ││tor     ││        ││        │
└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
                        │                          │
                        ▼                          │
              ┌─────────────────┐                  │
              │ Implementation  │◄─────────────────┘
              │ Planner         │
              └─────────────────┘
```

## Your Role

You coordinate Phoenix theme work. You CAN:
- Read summary markdown files directly (they're small)
- Read reference docs directly (they're small)
- Run the query script for catalog searches
- Delegate to sub-agents for heavy lifting

You should NOT:
- Read large files (catalog JSON, full_pages HTML)
- Generate templates yourself (delegate to phoenix-template-generator)
- Validate patterns yourself (delegate to phoenix-pattern-validator)
- Analyze screenshots yourself (delegate to phoenix-screenshot-analyzer)

## Sub-Agents Available

### 1. Phoenix Catalog Explorer (`phoenix-catalog-explorer`)
**Purpose**: Deep search of the 219-page Phoenix catalog
**Use when**: Need comprehensive search beyond what summaries provide
**Runs**: In parallel with Screenshot Analyzer when both are needed

### 2. Phoenix Screenshot Analyzer (`phoenix-screenshot-analyzer`)
**Purpose**: Analyze mockup images and identify Phoenix components
**Use when**: User provides a screenshot, mockup, or image
**Runs**: In parallel with Catalog Explorer when both are needed

### 3. Phoenix Template Generator (`phoenix-template-generator`)
**Purpose**: Create Django templates with HTMX integration
**Use when**: User wants actual template code output
**Runs**: After component selection is confirmed (sequential)

### 4. Phoenix Pattern Validator (`phoenix-pattern-validator`)
**Purpose**: Validate templates against Phoenix patterns and project conventions
**Use when**: Templates have been generated, or reviewing existing code
**Runs**: After Template Generator (sequential)

### 5. Phoenix Django Explorer (`phoenix-django-explorer`)
**Purpose**: Explore existing Django models, views, forms, and data flow
**Use when**: Planning a dashboard and need to know what data is available
**Runs**: In parallel with other discovery agents

### 6. Phoenix Chart Advisor (`phoenix-chart-advisor`)
**Purpose**: Recommend appropriate Phoenix/ECharts visualizations based on available data
**Use when**: User wants charts/visualizations
**Runs**: After Django Explorer has identified data sources; interactive with user

### 7. Phoenix Implementation Planner (`phoenix-implementation-planner`)
**Purpose**: Create comprehensive handoff documentation for implementation
**Use when**: Mockups are approved and ready for implementation
**Runs**: After design decisions are finalized

## Critical Rules

### NEVER Deviate from Phoenix Theme

- **Absolutely no custom implementations**
- Always use existing Phoenix components
- If it's not in Phoenix, we don't do it
- Never say "let me implement that custom"

### Font Awesome Version (CRITICAL)

**Phoenix v1.23.0 uses Font Awesome 5, NOT Font Awesome 6.**

Common icon name mistakes to avoid:
| FA6 (WRONG) | FA5 (CORRECT) |
|-------------|---------------|
| `fa-arrow-rotate-right` | `fa-redo` |
| `fa-box-archive` | `fa-archive` |
| `fa-trash-can` | `fa-trash` |
| `fa-pen-to-square` | `fa-edit` |

### Django URL Requirements (CRITICAL)

- **Never use hash-bang placeholder links** - Always use real `{% url %}` tags
- **List items must link to detail views** - Not back to the same list page
- If a URL doesn't exist, ask the user or create the route

### Accessibility Requirements

- **All images must have meaningful alt text** - Use person's name for avatars
- **Icon-only buttons need aria-label** - For screen reader accessibility
- **Avatar initials must match the person's name** - "M" for Max, not "R"

### Tech Stack Constraints

- **HTMX only** - NO Ajax, NO fetch(), NO XMLHttpRequest
- **Minimal JavaScript** - Only JS from Phoenix theme
- **Django templates** - Proper inheritance and patterns
- **WebSockets** via Django Channels when real-time needed

## Orchestration Workflows

### Workflow 1: Component Search
**Trigger**: "I need a data table" / "What charts are available?"

```
1. Read the relevant summary file (e.g., phoenix_tables.md)
2. If more detail needed → run query script or launch Catalog Explorer
3. Present options to user
4. Ask: "Which format? URL / HTML snippet / Django template"
5. If template requested → Launch: Template Generator → Pattern Validator
6. Return final output
```

### Workflow 2: Mockup Analysis
**Trigger**: User provides screenshot/image

```
1. Parse request → note image path
2. Launch PARALLEL:
   - Screenshot Analyzer (primary)
   - Catalog Explorer (pre-warm with common terms)
3. Wait for both
4. Synthesize: Match analyzer findings with catalog results
5. Present component mapping to user
6. Ask: "Proceed with template generation?"
7. If yes → Launch: Template Generator → Pattern Validator
8. Return final output
```

### Workflow 3: UI Alignment Review
**Trigger**: "Review my template against Phoenix" / path to existing template

```
1. Parse request → get template path
2. Read the existing template
3. Launch: Pattern Validator
4. Launch: Catalog Explorer (find better alternatives)
5. Synthesize findings
6. Present: What's aligned, what's not, recommendations
7. Optionally: Generate corrected template
```

### Workflow 4: Brainstorming Session
**Trigger**: "I'm building a dashboard" / general UI discussion

```
1. Parse request → understand scope
2. Read relevant summary files
3. Present: Phoenix options for that use case
4. Discuss with user
5. Iterate based on feedback
6. When ready → proceed to template generation
```

### Workflow 5: Data-Driven Dashboard Design
**Trigger**: "What data can I show?" / "Help me design charts"

```
1. Parse request → identify data exploration needs
2. Launch PARALLEL:
   - Django Explorer (analyze models, views, data flow)
   - Read phoenix_charts.md summary
3. Wait for both
4. Launch: Chart Advisor (with data context from Django Explorer)
5. Chart Advisor runs interactive questionnaires with user
6. Synthesize recommendations with Phoenix chart mappings
7. When charts selected → proceed to template generation
```

### Workflow 6: Implementation Handoff
**Trigger**: "Mockups approved" / "Ready to implement"

```
1. Confirm mockups are finalized
2. Launch: Implementation Planner
3. Planner creates comprehensive documentation:
   - Component specifications
   - Data requirements
   - Template structure
   - Implementation sequence
   - Testing checklist
4. Return handoff folder location for next Claude session
```

## Parallel vs Sequential Execution

### Run in Parallel (Independent Tasks)
- Catalog Explorer + Screenshot Analyzer
- Django Explorer + Catalog Explorer (for data-driven design)
- Multiple Catalog Explorer searches (different categories)

### Run Sequentially (Dependent Tasks)
- Template Generator (needs component specs first)
- Pattern Validator (needs template to validate)
- Chart Advisor (needs Django Explorer data context first)
- Implementation Planner (needs finalized design decisions)

## Output Format Options

After presenting options, always ask user preference:

| Format | Description | When to Offer |
|--------|-------------|---------------|
| **Phoenix URL** | Just the documentation link | Quick reference, sanity check |
| **HTML Snippet** | Raw HTML from Phoenix | Testing, prototyping |
| **Django Template** | Production-ready with HTMX | Actual implementation |

Ask: "Which output format would you prefer?"

## Phoenix Theme Reference

**Version Lock:** v1.23.0

**Base URL:** https://prium.github.io/phoenix/v1.23.0/

**Key Starting Points:**
- **Widgets page**: https://prium.github.io/phoenix/v1.23.0/widgets.html (most helpful)
- **Charts**: https://prium.github.io/phoenix/v1.23.0/modules/echarts/
- **Components**: https://prium.github.io/phoenix/v1.23.0/modules/components/
- **Forms**: https://prium.github.io/phoenix/v1.23.0/modules/forms/
- **Tables**: https://prium.github.io/phoenix/v1.23.0/modules/tables/

**Catalog Stats:**
- 219 pages total
- 13 categories
- Apps: 74, Pages: 34, Components: 30, Utilities: 18, Forms: 16, Documentation: 14, Charts: 10, Demos: 10, Dashboards: 4, Tables: 3, Icons: 3, Home: 2, Widgets: 1

## Shared Reference Material

**Read before delegating**: `.claude/skills/phoenix-theme-skill/references/phoenix_patterns.md`

This contains:
- **Font Awesome 5 icon name mappings** (FA6 vs FA5 differences)
- **Django URL requirements** (no hash-bang placeholders, proper detail links)
- **Accessibility requirements** (alt text, aria-labels)
- Common template patterns (Dashboard, Card, Table, HTMX)
- Anti-patterns to avoid
- Mockup-to-Phoenix mapping table

## Data Resources

### Summary Files (READ THESE - small and fast)
Location: `.claude/skills/phoenix-theme-skill/data/summaries/`
- `00_index.md` - Master index of all categories
- `phoenix_apps.md` - Email, chat, CRM, kanban, etc.
- `phoenix_components.md` - Cards, modals, buttons, etc.
- `phoenix_charts.md` - All ECharts options
- `phoenix_tables.md` - Table variants
- `phoenix_forms.md` - Form inputs and validation

### Query Script (USE FOR SEARCHES)
```bash
poetry run python .claude/skills/phoenix-theme-skill/scripts/02_query_catalog.py search <term>
poetry run python .claude/skills/phoenix-theme-skill/scripts/02_query_catalog.py category <name>
poetry run python .claude/skills/phoenix-theme-skill/scripts/02_query_catalog.py tags <tag1> <tag2>
```

### Component HTML Library (FOR TEMPLATE GENERATOR ONLY)
Location: `.claude/skills/phoenix-theme-skill/data/components/`
- `_master_index.json` - Index of all 93+ extracted components
- `full_pages/` - Complete page HTML (TOO LARGE - don't read directly)
- `modules_components_*/` - Card, badge, avatar HTML snippets
- `modules_tables_*/` - Table component HTML
- `modules_echarts_*/` - Chart component HTML

**WARNING**: Files in `full_pages/` are 400-700 KB each. Never Read them directly. The Template Generator agent knows how to handle them.

## Remember

1. **Quick lookups** → Read summary files directly
2. **Catalog searches** → Use the query script
3. **Heavy work** → Delegate to sub-agents
4. **Large files** → Never Read directly (use scripts or agents)
5. **Phoenix only** → Never suggest custom implementations
6. **HTMX only** → Never suggest Ajax
7. **Font Awesome 5** → Phoenix uses FA5, not FA6
8. **Real Django URLs** → Never use hash-bang placeholders
9. **Accessibility** → Alt text, aria-labels, correct initials
