---
name: talent-docs-skill
description: |
  Guide for building and populating the TalentAI Help Center documentation system. This skill should be used when implementing help center issues (#1038-#1042), writing user documentation, or uploading content to Azure Blob Storage. Supports PARALLEL ASYNC SWARM execution with multiple agents exploring, writing, reviewing, and uploading simultaneously. Covers Django app setup, Phoenix templates, markdown rendering with Python-Markdown and Pygments.
---

# TalentAI Help Center Documentation Skill

This skill provides comprehensive guidance for building the TalentAI Help Center - a user-facing documentation system for recruiters and non-technical staff.

## Key Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| `markdown` | >= 3.10.0 | Markdown → HTML rendering |
| `pygments` | >= 2.19.2 | Code syntax highlighting |

**Install:**
```bash
poetry add markdown pygments
```

**Usage:**
```python
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

md = markdown.Markdown(
    extensions=[
        'tables',
        'fenced_code',
        TocExtension(permalink=True, toc_depth=3),
        CodeHiliteExtension(css_class='highlight', guess_lang=False),
        'sane_lists',
    ],
    output_format='html5'
)

html = md.convert(markdown_content)
toc = md.toc  # Table of contents HTML
```

## Parallel Agent Swarm Architecture

This skill supports **parallel async execution** using multiple specialized agents working simultaneously. This dramatically speeds up documentation generation.

### Swarm Agents

| Agent | Purpose | Parallelism |
|-------|---------|-------------|
| `help-docs-orchestrator` | Coordinates entire swarm | 1 (main) |
| `help-docs-explorer` | Explores apps for features | Up to 10 |
| `help-docs-writer` | Writes documentation articles | Up to 10 |
| `help-docs-critic` | Reviews for quality/style | Up to 10 |

### Execution Waves

```
WAVE 1: Exploration (Parallel)
├── Explorer: recruitment/candidates/
├── Explorer: recruitment/jobs/
├── Explorer: recruitment/emails/
├── Explorer: recruitment/calendar_app/
├── Explorer: recruitment/analytics/
├── Explorer: core/accounts/
└── Explorer: intelligence/
    [Wait for all to complete]
           │
           ▼
WAVE 2: Writing (Parallel)
├── Writer: getting-started/welcome.md
├── Writer: candidates/search-basics.md
├── Writer: candidates/filters.md
├── Writer: jobs/creating.md
└── ... (up to 10 parallel)
    [Wait for all to complete]
           │
           ▼
WAVE 3: Review (Parallel)
├── Critic: getting-started/welcome.md
├── Critic: candidates/search-basics.md
└── ... (up to 10 parallel)
    [Approved → Upload, Rejected → Rework]
           │
           ▼
WAVE 4: Upload
└── Batch upload to Azure Blob Storage
```

### Spawning Parallel Agents

To spawn multiple agents in parallel, use multiple Task tool calls in a **single message**:

```python
# Spawn 5 explorers in parallel
Task(subagent_type="help-docs-explorer", prompt="Explore recruitment/candidates/...")
Task(subagent_type="help-docs-explorer", prompt="Explore recruitment/jobs/...")
Task(subagent_type="help-docs-explorer", prompt="Explore recruitment/emails/...")
Task(subagent_type="help-docs-explorer", prompt="Explore recruitment/calendar_app/...")
Task(subagent_type="help-docs-explorer", prompt="Explore recruitment/analytics/...")
```

Claude Code executes these **simultaneously**, not sequentially. Maximum 10 parallel.

### Using the Orchestrator

For full documentation generation (Issue #1042), spawn the orchestrator:

```
Task tool:
  subagent_type: "help-docs-orchestrator"
  model: opus
  prompt: |
    Generate complete TalentAI Help Center documentation.

    Apps to cover:
    - recruitment/candidates/
    - recruitment/jobs/
    - recruitment/emails/
    - recruitment/calendar_app/
    - recruitment/analytics/
    - core/accounts/
    - intelligence/ (AI features)

    Use parallel swarm execution:
    1. Spawn explorers in parallel (up to 10)
    2. Spawn writers in parallel based on findings
    3. Spawn critics to review all articles
    4. Upload approved articles to Azure

    Reference: .claude/skills/talent-docs-skill/
```

## Quick Reference

### Key Paths

```
help_center/                              # Django app
help_center/services/blob_reader.py       # Azure blob access
help_center/services/markdown_renderer.py # Markdown → HTML
help_center/services/navigation.py        # Nav structure

# Design references
claude/2026-01-07_docs_help_center/design_drafts/04_phoenix_enhanced.html
claude/2026-01-07_docs_help_center/design_drafts/05_phoenix_home.html
claude/2026-01-07_docs_help_center/planning/01_architecture.md

# Swarm agents
.claude/agents/help-docs-orchestrator.md
.claude/agents/help-docs-explorer.md
.claude/agents/help-docs-writer.md
.claude/agents/help-docs-critic.md
```

### Azure Blob Structure

```
docs/                        # Azure blob container
├── _nav.yaml                # Navigation structure
├── index.md                 # Home page content
├── getting-started/
│   ├── welcome.md
│   └── quick-start.md
├── candidates/
│   ├── search-basics.md
│   └── filters.md
└── [other sections...]
```

### URL Structure

- `/docs/` → Home page (index.md)
- `/docs/getting-started/` → getting-started/index.md
- `/docs/candidates/search-basics/` → candidates/search-basics.md

## Implementation Issues

| Issue | Description | Status |
|-------|-------------|--------|
| #1038 | Core Django App Setup | Foundation |
| #1039 | Azure Blob Storage Integration | Storage |
| #1040 | Markdown Rendering Service | Rendering |
| #1041 | Phoenix-Themed Templates | UI |
| #1042 | Generate Documentation Content | **Swarm** |

## Content Writing Guidelines (Summary)

**Target Audience:** Recruiters, hiring managers (non-technical)

**Voice:** Friendly, clear, helpful - like a knowledgeable colleague

**Structure:**
```markdown
# [Task-Oriented Title]

[1-2 sentence overview]

## How to [Do the Thing]

1. Go to **Candidates > Search**
2. Click **Filters**
3. Select your criteria
4. Click **Apply**

## Pro Tips

- **Start broad** - Begin with fewer filters
- **Save searches** - Reuse your filter combinations

## Common Questions

**Q: Why no results?**
A: Your filters might be too restrictive.
```

**Formatting:**
- **Bold** for UI elements: **Save**, **Cancel**
- `Code` for shortcuts: `Ctrl+K`
- Numbered lists for procedures
- Bullet lists for options

**DON'T:** Use jargon, passive voice, technical terms

**DO:** Use "you", active voice, recruiter examples

## Azure Upload

### Single File
```bash
az storage blob upload \
  --account-name $AZURE_STORAGE_ACCOUNT_NAME \
  --container-name docs \
  --name "candidates/filters.md" \
  --file filters.md
```

### Batch Upload
```bash
az storage blob upload-batch \
  --account-name $AZURE_STORAGE_ACCOUNT_NAME \
  --destination docs \
  --source ./docs-staging/
```

### Using the Script
```bash
.claude/skills/talent-docs-skill/scripts/upload_docs.sh filters.md candidates/filters.md
```

## TalentAI Branding

```css
/* Purple-to-pink gradient */
.docs-brand-name .text-accent {
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.btn-bayone {
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
    color: #ffffff;
}
```

## Reference Files

For detailed information:
- `references/architecture.md` - Full technical architecture
- `references/content_guidelines.md` - Detailed writing guidelines
- `references/navigation_structure.md` - Complete nav.yaml template

## Anthropic Multi-Agent Patterns

This skill implements patterns from [Anthropic's Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system):

- **Orchestrator-Worker Pattern:** Lead agent coordinates specialized workers
- **Parallel Tool Calling:** Multiple agents execute simultaneously
- **Isolated Context Windows:** Each agent has its own 200k context
- **Result Synthesis:** Orchestrator collects and synthesizes findings

Key insight: "Token usage explains 80% of variance in performance." Parallel execution with isolated contexts dramatically improves quality and speed.

## Sources

- [Anthropic Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Claude Code Subagents Documentation](https://code.claude.com/docs/en/sub-agents)
- [Parallel Coding Agents](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/)
- [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
