# Phase 3 Session 4: Cross-Cutting Patterns

## Executive Summary

1. **Settings use explicit allow-list pattern** - Permissions whitelist specific tools with domain/command prefix restrictions (e.g., `WebFetch(domain:github.com)`, `Bash(python3:*)`)

2. **Commands and skills have significant overlap** - `/django-issue` is a massive 830-line command that duplicates skill functionality; `/django-forge` and `/extract-issues` are thin wrappers that just invoke their corresponding skills

3. **Prompts folder is underutilized** - Contains only kickoff templates meant for copy-paste, not proper Claude Code prompts; one file is empty

4. **YAML frontmatter is universal but inconsistent** - All skills use `name:` and `description:` but format varies (single-line vs multi-line, trigger phrases sometimes included)

5. **Agent orchestration is the dominant pattern** - 7 of 9 skills spawn sub-agents; the most sophisticated skills (airflow, azure, talent-docs) use parallel async swarm execution

6. **Hard rules/constraints sections are common but named inconsistently** - "Hard Rules", "Hard Constraints", "Core Philosophy", "Critical Reminders" all serve the same purpose

7. **Reference documentation and scripts are well-organized** - Consistent `references/` and `scripts/` subdirectory pattern across skills

---

## Files Analyzed

### Settings
- `.claude/settings.local.json`

### Commands (4 files)
- `.claude/commands/django-issue.md` (831 lines)
- `.claude/commands/agentic-django-issue.md` (251 lines)
- `.claude/commands/django-forge.md` (69 lines)
- `.claude/commands/extract-issues.md` (56 lines)

### Prompts (2 files)
- `.claude/prompts/django-forge-kickoff.md` (57 lines)
- `.claude/prompts/django-forge-pr-review.md` (empty - 1 line)

### Other Skills (9 SKILL.md files)
- `.claude/skills/airflow-skill/SKILL.md` (287 lines)
- `.claude/skills/azure-expert-skill/SKILL.md` (704 lines)
- `.claude/skills/docker-expert-skill/SKILL.md` (202 lines)
- `.claude/skills/django-database-query-skill/SKILL.md` (554 lines)
- `.claude/skills/github-issue-creator-skill/SKILL.md` (776 lines)
- `.claude/skills/concept-tutor-skill/SKILL.md` (359 lines)
- `.claude/skills/brainstorm-skill/SKILL.md` (255 lines)
- `.claude/skills/talent-docs-skill/SKILL.md` (292 lines)
- `.claude/skills/meeting-git-issue-extractor/SKILL.md` (586 lines)

---

## Detailed Analysis

### Settings Patterns

**Structure:**
```json
{
  "permissions": {
    "allow": [...],
    "deny": [],
    "ask": []
  }
}
```

**Permission Types Found:**
| Permission Type | Example | Purpose |
|-----------------|---------|---------|
| Full tool | `WebSearch` | No restrictions |
| Domain-scoped WebFetch | `WebFetch(domain:github.com)` | Limit to specific domains |
| Command-prefix Bash | `Bash(mkdir:*)` | Allow specific command patterns |

**Domains Whitelisted:**
- companieslogo.com
- github.com
- raw.githubusercontent.com
- agentskills.io
- platform.claude.com
- www.anthropic.com
- claude.com
- leehanchung.github.io

**Bash Commands Whitelisted:**
- `mkdir:*`
- `python3:*`
- `curl:*`

**Observations:**
- Empty `deny` and `ask` arrays indicate permissive defaults
- No environment variable definitions in settings
- Settings focus on web access and file creation permissions

---

### Commands Analysis

| Command | Lines | Purpose | Relationship to Skills |
|---------|-------|---------|------------------------|
| `django-issue` | 831 | 8-phase Django implementation workflow | **Standalone** - Complete workflow, doesn't invoke skill |
| `agentic-django-issue` | 251 | Multi-agent Django workflow | **Duplicate** - Essentially same as django-forge concept |
| `django-forge` | 69 | Invoke django-forge skill | **Wrapper** - Just invokes skill with hard rules reminder |
| `extract-issues` | 56 | Invoke meeting-git-issue-extractor | **Wrapper** - Just invokes skill |

**Command Structure Patterns:**

1. **Frontmatter:**
   ```yaml
   ---
   description: Short description
   argument-hint: <issue-number or description>
   ---
   ```

2. **Content Organization:**
   - Massive standalone workflows (django-issue: 8 phases, detailed checklists)
   - OR thin wrappers that invoke skills with reminders

**Key Finding: django-issue vs django-forge**
- `django-issue` is a massive standalone command with complete workflow
- `django-forge` is a wrapper that invokes the skill
- Both accomplish similar goals - redundancy exists

---

### Prompts Pattern

**Purpose:** Copy-paste kickoff templates for sessions, NOT traditional prompt engineering

**Content of django-forge-kickoff.md:**
- Template for invoking Django Forge skill
- Agent usage table
- Non-negotiable rules reminder
- Git push permission instructions

**Content of django-forge-pr-review.md:**
- Empty (just newline)

**Key Finding:** The prompts folder serves as a "canned instructions" repository, not as reusable prompt templates in the technical sense. This pattern is underutilized and could be merged into commands or skills.

---

### Cross-Skill Patterns

#### Common Sections Across Skills

| Section | Occurrence | Purpose |
|---------|------------|---------|
| YAML Frontmatter | 9/9 | Name, description, triggers |
| Hard Rules/Constraints | 7/9 | Forbidden behaviors, safety |
| When to Use | 8/9 | Trigger conditions |
| Workflow/Phases | 7/9 | Step-by-step process |
| Agent Tables | 5/9 | Sub-agent definitions |
| Example Session | 5/9 | Interaction demonstrations |
| References mention | 6/9 | Documentation pointers |

#### Frontmatter Patterns

**Format 1: Simple (3 skills)**
```yaml
---
name: concept-tutor
description: Single line description...
---
```

**Format 2: Multiline with pipe (6 skills)**
```yaml
---
name: azure-expert-skill
description: |
  Multi-line description
  with more details...
---
```

**Inconsistencies:**
- Some include trigger phrases in description, some don't
- Some include `(project)` tag, some don't
- No version information in any skill

#### Hard Rules Section Naming

| Skill | Section Name |
|-------|--------------|
| airflow-skill | "Hard Constraints" |
| azure-expert-skill | "Hard Rules" |
| docker-expert-skill | "Safety Rules" |
| django-database-query-skill | "Critical: NEVER ASSUME!" |
| github-issue-creator-skill | (embedded in steps) |
| concept-tutor-skill | "Core Philosophy" |
| brainstorm-skill | "Core Philosophy" |
| talent-docs-skill | (embedded) |
| meeting-git-issue-extractor | "Hard Rules" |

#### Agent Orchestration Patterns

**Skills Using Sub-Agents:**

| Skill | # Agents | Execution Pattern |
|-------|----------|-------------------|
| airflow-skill | 10 | Sequential with some parallel |
| azure-expert-skill | 9 | Parallel waves |
| talent-docs-skill | 4 | Parallel async swarm (waves) |
| meeting-git-issue-extractor | 4 | Parallel exploration, sequential issues |
| github-issue-creator-skill | 3 (optional) | Sequential analyzer->author->reviewer |

**Skills NOT Using Sub-Agents:**
- docker-expert-skill (suggests research sub-agents)
- django-database-query-skill (recommends db-analyst agent setup)
- concept-tutor-skill (pure conversational)
- brainstorm-skill (pure conversational)

#### Directory Structure Patterns

**Standard Structure (observed):**
```
skill-name/
├── SKILL.md              # Main skill file (ALL skills)
├── references/           # Documentation (7/9 skills)
├── scripts/              # Utility scripts (5/9 skills)
├── templates/            # Issue/doc templates (2/9 skills)
├── agents/               # Sub-agent definitions (2/9 skills)
└── examples/             # Example files (1/9 skills)
```

**Variations:**
- Some skills define agents inline in SKILL.md
- Some skills point to `.claude/agents/` (shared location)
- Template locations vary (templates/ vs inline)

---

### Skill Catalog

| Skill | Type | Complexity | Unique Features |
|-------|------|------------|-----------------|
| airflow-skill | Domain Expert | HIGH | 10 specialized agents, workflow patterns A-E, quality gates, 3.x specific |
| azure-expert-skill | Domain Expert | HIGH | 9 sub-agents, session folders, lessons_learned.md, VNet awareness rules |
| docker-expert-skill | Domain Expert | MEDIUM | Diagnostics scripts, modern syntax enforcement, BuildKit focus |
| django-database-query-skill | Utility | MEDIUM | Schema cataloging, reference files, template scripts, anti-assumption rules |
| github-issue-creator-skill | Process | HIGH | Templates, SOC2 compliance, narration guidelines, explicit permission gates |
| concept-tutor-skill | Educational | LOW | Teaching patterns only, no execution, progressive complexity |
| brainstorm-skill | Conversational | LOW | Discussion only, no execution, Socratic method |
| talent-docs-skill | Content Gen | HIGH | Parallel async swarm, wave execution, multiple agents per wave |
| meeting-git-issue-extractor | Process | HIGH | 8 phases, state.json resumption, per-issue approval workflow |

**Skill Type Categories:**
1. **Domain Expert** (3): Deep knowledge of specific technology
2. **Process** (2): Multi-phase workflows with checkpoints
3. **Utility** (1): Focused tool for specific task
4. **Educational** (1): Teaching/explanation only
5. **Conversational** (1): Discussion/brainstorming only
6. **Content Generation** (1): Document creation with parallel execution

---

## Good Patterns (Keep)

### 1. YAML Frontmatter with name/description
Every skill has this, providing consistent metadata for skill discovery.

### 2. Hard Rules/Constraints Sections
Explicit forbidden behaviors prevent dangerous actions:
```markdown
## Hard Rules
1. **NEVER run destructive commands without explicit permission**
2. **NEVER batch commands** - Execute ONE command at a time
3. **If a command fails, STOP and THINK**
```

### 3. Reference Documentation Organization
Consistent `references/` subdirectory pattern:
- `references/lessons_learned.md` (azure)
- `references/questionnaire_approach.md` (airflow)
- `references/operations_guide.md` (django-database-query)

### 4. Session Folder Patterns
State management through dated folders:
```
claude/<YYYY-MM-DD>_<topic>/
├── orchestration/state.json
├── agents/
├── research/
└── source/
```

### 5. Agent Tables with Purpose and Model
Clear agent definitions:
```markdown
| Agent | Purpose | Model |
|-------|---------|-------|
| DAG Builder | Generate production-ready code | Opus |
| DAG Polisher | Interactive review | Opus |
```

### 6. Example Sessions
Concrete interaction patterns showing expected behavior.

### 7. "Never Do" Explicit Constraints
Clear anti-patterns:
- "Never mention Claude, Claude Code, or AI"
- "Never add Co-Authored-By attribution"
- "Never assume database credentials"

### 8. Scripts in Standardized Location
Utility scripts in `scripts/` subdirectory with descriptive names.

### 9. Permission Gates Before Destructive Actions
Pattern of requiring explicit user approval:
```markdown
**WAIT FOR EXPLICIT PERMISSION**
**NEVER run `gh issue create` without explicit user permission.**
```

### 10. Workflow Visualization
ASCII diagrams showing multi-phase processes:
```
WAVE 1: Exploration (Parallel)
├── Explorer: recruitment/candidates/
├── Explorer: recruitment/jobs/
    [Wait for all to complete]
           │
           ▼
WAVE 2: Writing (Parallel)
```

---

## Outdated Patterns (Update)

### 1. Inconsistent Frontmatter Format
**Current:**
- Some use `|` for multiline description
- Some include trigger phrases, some don't
- No version tracking

**Recommended:**
```yaml
---
name: skill-name
version: 1.0.0
description: |
  Description here...
triggers:
  - "keyword 1"
  - "keyword 2"
---
```

### 2. Missing Model Recommendations
Some skills don't specify which Claude model to use for agents. Best practice from airflow-skill and azure-expert-skill is to always include model in agent tables.

### 3. No Version Information
Skills don't track when they were last updated or what version they are. This makes maintenance difficult.

### 4. Prompts Folder Underutilized
Currently contains only copy-paste templates. Should either:
- Be deprecated and merged into commands
- OR be expanded with proper prompt engineering templates

### 5. Commands Duplicating Skills
The `/django-issue` command is 831 lines and could be a skill. The `/django-forge` and `/extract-issues` commands are just wrappers - this indirection is unnecessary.

### 6. Lessons Learned Not Universal
Only azure-expert-skill has a `lessons_learned.md` pattern. This self-improving pattern should be in all domain expert skills.

---

## Inconsistencies Found

### 1. Description Format Variation
| Skill | Format | Includes Triggers |
|-------|--------|-------------------|
| airflow-skill | multiline | Yes |
| azure-expert-skill | multiline | Yes (in description) |
| docker-expert-skill | single line | Yes |
| django-database-query-skill | single line | Yes |
| github-issue-creator-skill | single line | Yes (partial) |
| concept-tutor-skill | single line | Yes |
| brainstorm-skill | single line | Yes |
| talent-docs-skill | multiline | Yes |
| meeting-git-issue-extractor | single line | Yes (partial) |

### 2. Agent Definition Location
- Some skills define agents inline in SKILL.md
- Some point to `.claude/agents/` (shared location)
- Some have local `agents/` subdirectory

### 3. Hard Rules Section Naming
- "Hard Rules" (2 skills)
- "Hard Constraints" (1 skill)
- "Safety Rules" (1 skill)
- "Core Philosophy" (2 skills)
- "Critical Reminders" (1 skill)
- Embedded in steps (2 skills)

### 4. Reference Path Format
- Some use full paths: `.claude/skills/github-issue-creator-skill/references/...`
- Some use relative paths: `references/...`
- Some use skill-relative: `See references/ directory`

### 5. Template Location
- `templates/` subdirectory (github-issue-creator-skill)
- Inline in SKILL.md (others)
- `scripts/` with template suffix (django-database-query-skill)

### 6. State Management
- Some skills use `state.json` (meeting-git-issue-extractor)
- Some use session folders without explicit state (azure-expert-skill uses agent_logs/)
- Some have no state management (simpler skills)

---

## Recommendations for Skill-Forge

### 1. Standardize Frontmatter Schema
```yaml
---
name: skill-name           # Required: lowercase, hyphenated
version: 1.0.0            # Required: semver
description: |            # Required: multiline preferred
  Main description here.
triggers:                 # Required: array of trigger phrases
  - "create a DAG"
  - "convert to Airflow"
model: opus              # Optional: default model for skill
type: domain-expert      # Optional: category
---
```

### 2. Create Standard Skill Template
Skill-forge should generate skills with these sections:
1. Frontmatter (standardized)
2. Overview (1-2 paragraphs)
3. When to Use This Skill
4. Hard Rules (if applicable)
5. Workflow/Process (with phase diagram)
6. Agent Definitions (if multi-agent)
7. Reference Documentation
8. Example Session
9. Related Skills

### 3. Standardize Directory Structure
```
skill-name/
├── SKILL.md              # Main skill definition
├── references/           # Documentation files
│   └── *.md
├── scripts/              # Utility scripts
│   └── *.py, *.sh
├── templates/            # Reusable templates
│   └── *.md
└── examples/             # Example files
    └── *.md
```

### 4. Migrate Redundant Commands to Skills
- `/django-issue` -> Should be a skill or deprecated in favor of django-forge
- `/agentic-django-issue` -> Duplicate, should be removed
- `/django-forge` -> Keep as thin wrapper OR remove and invoke skill directly
- `/extract-issues` -> Keep as thin wrapper OR remove

### 5. Deprecate or Repurpose Prompts Folder
Options:
- **Deprecate:** Move kickoff templates into skill references
- **Repurpose:** Create proper prompt engineering templates
- **Merge:** Add "kickoff" section to each skill's SKILL.md

### 6. Add Version Tracking
Skills should track:
- Version number (semver)
- Last updated date
- Changelog or update history

### 7. Implement Universal Lessons Learned
Pattern from azure-expert-skill should be standard:
```markdown
## Self-Learning Protocol
When errors occur:
1. Document in lessons_learned.md
2. Update skill if pattern is common
3. Create GitHub issue for review
```

### 8. Standardize Agent Table Format
Always include:
| Agent | Purpose | Model | Async |
|-------|---------|-------|-------|

### 9. Consistent Reference Paths
Use skill-relative paths in SKILL.md:
- `references/filename.md` (not full paths)
- Full paths only when referencing across skills

### 10. Session State Standard
For stateful skills, standardize on:
```json
{
  "session_id": "uuid",
  "created_at": "timestamp",
  "current_phase": "phase-name",
  "completed_phases": [],
  "metadata": {}
}
```

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total files analyzed | 15 |
| Settings files | 1 |
| Commands | 4 |
| Prompts | 2 (1 empty) |
| Skills | 9 |
| Skills with sub-agents | 5 |
| Skills with parallel execution | 3 |
| Average SKILL.md length | 446 lines |
| Longest SKILL.md | github-issue-creator-skill (776 lines) |
| Shortest SKILL.md | docker-expert-skill (202 lines) |

---

## Cross-Reference: Skill Capabilities

### Skills That Spawn Agents
- airflow-skill
- azure-expert-skill
- talent-docs-skill
- meeting-git-issue-extractor
- github-issue-creator-skill (optional)

### Skills That Use Session Folders
- azure-expert-skill
- meeting-git-issue-extractor
- talent-docs-skill

### Skills That Are Pure Conversation
- concept-tutor-skill
- brainstorm-skill

### Skills That Enforce Safety Gates
- azure-expert-skill (destructive commands)
- github-issue-creator-skill (issue creation)
- meeting-git-issue-extractor (issue creation)
- docker-expert-skill (prune commands)

### Skills That Reference External Documentation
- github-issue-creator-skill (references/)
- airflow-skill (references/)
- azure-expert-skill (references/)
- docker-expert-skill (references/)
- django-database-query-skill (references/)
