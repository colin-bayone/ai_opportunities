# Phase 2 Session 1: Skill Structure & SKILL.md Patterns

## Executive Summary

1. **Skills are modular capability packages** consisting of a required `SKILL.md` file with YAML frontmatter and markdown instructions, plus optional supporting directories (`scripts/`, `references/`, `assets/`).

2. **Two frontmatter fields are required**: `name` (max 64 chars, lowercase letters/numbers/hyphens only) and `description` (max 1024 chars, determines auto-triggering).

3. **Progressive disclosure architecture** minimizes context usage: metadata loads at startup (~100 tokens), SKILL.md body loads on trigger (<5k tokens recommended), bundled resources load on-demand.

4. **Slash commands merged into skills** (v2.1.3, late 2025): `.claude/commands/` files still work but new development should use skills for full feature access.

5. **Skill triggering relies on LLM reasoning**, not algorithmic matching—description quality directly determines auto-invocation accuracy. The WHEN + WHEN NOT description pattern improves reliability.

6. **Key invocation controls**: `disable-model-invocation: true` prevents auto-triggering; `user-invocable: false` hides from slash menu but allows model invocation.

7. **Agent Skills is an open standard** (December 2025) adopted by both Anthropic and OpenAI, hosted at https://agentskills.io/specification.

---

## Sources Consulted

| Source | URL | Type | Notes |
|--------|-----|------|-------|
| Claude Code Docs - Skills | https://code.claude.com/docs/en/skills | Official | Primary reference, comprehensive |
| Claude API Docs - Overview | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | Official | Agent Skills architecture |
| Claude API Docs - Best Practices | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | Official | Authoring guidelines |
| Anthropic Skills GitHub | https://github.com/anthropics/skills | Official | Repo structure, examples |
| Skill-Creator SKILL.md | https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md | Official | Reference implementation |
| Agent Skills Specification | https://agentskills.io/specification | Official | Open standard spec |
| Anthropic Engineering Blog | https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills | Official | Design philosophy |
| Claude Code Docs - Subagents | https://code.claude.com/docs/en/sub-agents | Official | Context fork, delegation |
| Deep Dive Blog | https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/ | Community | Technical internals |
| Mikhail Shilkov Blog | https://mikhail.io/2025/10/claude-code-skills/ | Community | Invocation mechanism |
| Scott Spence Blog | https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably | Community | Activation patterns |

---

## Detailed Findings

### Skill Directory Structure

Skills are self-contained folders with a standardized organization:

```
skill-name/
├── SKILL.md              # REQUIRED: Main skill file with frontmatter + instructions
├── scripts/              # Optional: Executable Python/Bash automation
│   └── helper.py         # Claude invokes via Bash tool
├── references/           # Optional: Documentation loaded into context on demand
│   └── FORMS.md          # Text files read via Read tool
├── assets/               # Optional: Templates and static files
│   └── template.html     # Referenced by path, not loaded into context
└── LICENSE.txt           # Optional: License information
```

**Key Principles:**

1. **Only SKILL.md is required** - everything else is optional
2. **Always use `{baseDir}` placeholder** for file references - never hardcode paths
3. **Keep references one level deep** from SKILL.md to ensure complete file reads
4. **Match directory name to skill name** - validation may enforce this

**Skill Discovery Locations** (priority order, higher overrides lower):
1. Enterprise/managed settings (organization-wide)
2. CLI flags (`--agents` JSON)
3. User settings (`~/.claude/skills/` or `~/.config/claude/skills/`)
4. Project settings (`.claude/skills/`)
5. Plugin directories (`<plugin>/skills/`)
6. Built-in skills

**Monorepo Support:** Skills in nested `.claude/skills/` directories within subdirectories are automatically discovered.

**Live Reload:** Skills from `--add-dir` directories integrate with live change detection without session restart.

---

### SKILL.md Format

Every SKILL.md file has two parts:

```markdown
---
name: skill-name
description: What the skill does and when to use it
---

# Skill Name

[Markdown instructions Claude follows when skill is active]

## Section 1
...

## Section 2
...
```

**Structure Guidelines:**

1. **Keep SKILL.md under 500 lines** (~5000 words) to optimize context
2. **Use imperative language** ("Analyze code for...") not second-person
3. **Structure with headers, lists, code blocks** for parseability
4. **Include concrete examples** where workflows aren't obvious
5. **Move detailed content to references/** and link to it
6. **Add table of contents** for files exceeding 100 lines

**Content Types:**

| Type | Purpose | Example |
|------|---------|---------|
| Reference content | Knowledge integrated into current work | Conventions, patterns, domain expertise |
| Task content | Step-by-step workflows for specific actions | Build processes, deployment procedures |

---

### Frontmatter Fields

#### Required Fields

| Field | Constraints | Purpose |
|-------|-------------|---------|
| `name` | 1-64 chars, lowercase alphanumerics and hyphens only, no leading/trailing/consecutive hyphens | Creates the `/slash-command` and unique identifier |
| `description` | Non-empty, max 1024 chars, no XML tags | Tells Claude when to auto-invoke; write in third person |

**Invalid `name` patterns:**
- Uppercase characters: `MySkill`
- Leading hyphen: `-my-skill`
- Trailing hyphen: `my-skill-`
- Consecutive hyphens: `my--skill`
- Reserved words: `anthropic`, `claude`

#### Optional Fields - Invocation Control

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `disable-model-invocation` | Boolean | `false` | When `true`, prevents Claude from auto-triggering; skill only available via `/name` |
| `user-invocable` | Boolean | `true` | When `false`, hides from slash menu but still allows model invocation |
| `argument-hint` | String | none | Shows expected parameters in autocomplete (e.g., `[issue-number] [priority]`) |

**Invocation Matrix:**

| disable-model-invocation | user-invocable | Result |
|--------------------------|----------------|--------|
| false | true | Default: auto-invoke + manual invoke |
| true | true | Manual only via `/name` |
| false | false | Auto-invoke only (background knowledge) |
| true | false | Effectively disabled |

#### Optional Fields - Execution Context

| Field | Type | Values | Purpose |
|-------|------|--------|---------|
| `context` | String | `fork` | Isolates execution in separate subagent context |
| `agent` | String | `Explore`, `Plan`, `general-purpose` | Specifies subagent type when using `context: fork` |
| `model` | String | `sonnet`, `opus`, `haiku`, `inherit`, or full model ID | Override model during skill execution |
| `mode` | Boolean | `true` | Categorizes as a "mode command" modifying behavior |

**Note on `context: fork`:** There's a known issue (GitHub #17283) where `context: fork` and `agent:` fields may be ignored when skill is invoked via Skill tool.

#### Optional Fields - Tool Access

| Field | Type | Purpose |
|-------|------|---------|
| `allowed-tools` | String (space/comma-delimited) | Pre-approved tools without per-use approval |

**Tool Specification Syntax:**

```yaml
# Simple - permit all actions for tool
allowed-tools: Read, Write, Grep

# Scoped - permit matching calls only
allowed-tools: Bash(git status:*), Bash(npm:*)

# Wildcard - permit all operations for command
allowed-tools: Bash(gh *)

# Skill invocation
allowed-tools: Skill(analyzer), Skill(builder *)
```

**Known Limitations:**
- `allowed-tools` only works in Claude Code CLI, not Agent SDK
- There are reported bugs where permissions may not be enforced (GitHub #14956, #18837)

#### Optional Fields - Metadata

| Field | Type | Purpose |
|-------|------|---------|
| `license` | String | License identifier or reference |
| `version` | String | Version tracking (e.g., `1.0.0`) |
| `compatibility` | String | Environment requirements (max 500 chars) |
| `metadata` | Object | Key-value pairs for additional properties |

#### Complete Frontmatter Example

```yaml
---
name: code-reviewer
description: Reviews code for security vulnerabilities, performance issues, and best practice violations. Use when the user asks for code review, security audit, or wants feedback on implementation quality.
license: MIT
version: 1.2.0
allowed-tools: Read, Grep, Glob
disable-model-invocation: false
user-invocable: true
argument-hint: [file-path]
model: opus
---
```

---

### Skill Triggering

#### How Triggering Works

1. **Startup**: System loads all skill metadata (name, description) into context (~100 tokens per skill)
2. **User message**: Claude receives user request
3. **Skill matching**: Claude uses LLM reasoning (not algorithmic matching) to determine relevance
4. **Skill invocation**: Claude calls Skill tool with skill name
5. **Context expansion**: Full SKILL.md body injected into conversation
6. **Execution**: Claude follows skill instructions with access to bundled resources

**Critical insight:** Claude uses pure language model reasoning to match intent against descriptions. There is no embedded matching algorithm.

#### Message Injection Pattern

When a skill executes, two messages are injected:

**Message 1** (visible to user):
```xml
<command-message>The "pdf" skill is loading</command-message>
<command-name>pdf</command-name>
```

**Message 2** (hidden, sent to Claude):
```
[Full skill prompt with instructions, workflows, output formats]
```

#### Description Writing for Optimal Triggering

**The WHEN + WHEN NOT Pattern** (84% activation vs 20% baseline):

```yaml
description: >
  Analyzes database schemas and generates migration scripts.
  Auto-invoke when user mentions database changes, schema updates,
  or migration planning. Do NOT load for general SQL queries
  or data analysis tasks unrelated to schema modifications.
```

**Best Practices:**

1. **Be specific about trigger conditions** - list exact keywords and scenarios
2. **Explicitly exclude non-matches** - state when NOT to invoke
3. **Use third person** - "Generates reports" not "You generate reports"
4. **Include action verbs** - describe what the skill does
5. **Max 1024 characters** - be concise but comprehensive

**Anti-Patterns:**

- Vague descriptions: "Helper for various tasks"
- Missing trigger conditions: "Processes data"
- Overly broad: "Use for any coding task"

#### Known Activation Challenges

Simple instruction patterns like "If the prompt matches skill keywords, use Skill(name)" often fail (~20% success). Solutions:

1. **Forced Eval Hook** (84% success): Requires Claude to explicitly evaluate each skill before proceeding
2. **Hooks-based activation**: Use `PreUserMessage` hooks for conditional skill loading
3. **Explicit user invocation**: Use `/skill-name` for guaranteed activation

---

### Skills vs Commands vs Agents

#### Evolution Timeline

- **Pre-2025**: Slash commands (`.claude/commands/`) were separate from skills
- **October 2025**: Agent Skills released as unified capability system
- **December 2025**: Agent Skills published as open standard (agentskills.io)
- **Late 2025 (v2.1.3)**: Slash commands merged into skills system
- **January 2026**: Same format adopted by OpenAI for Codex CLI and ChatGPT

#### Comparison Matrix

| Aspect | Skills | Slash Commands (Legacy) | Subagents |
|--------|--------|-------------------------|-----------|
| Location | `.claude/skills/name/SKILL.md` | `.claude/commands/name.md` | `.claude/agents/name.md` |
| Invocation | Auto + `/name` | `/name` only | Auto via Task tool |
| Context | Shared (or forked) | Shared | Always isolated |
| Frontmatter | Full feature set | Limited | Full feature set |
| Supporting files | `scripts/`, `references/`, `assets/` | None | None (but has skills field) |
| Token efficiency | Lazy-loaded | Inserted every time | Separate context |

#### When to Use Each

**Use Skills for:**
- Domain-specific knowledge that shouldn't bloat CLAUDE.md
- Reusable workflows with supporting files
- Capabilities that benefit from auto-triggering
- Document generation with templates

**Use Slash Commands (Legacy) for:**
- Simple one-off commands (these still work)
- Quick prototypes before converting to skills

**Use Subagents for:**
- Self-contained tasks with verbose output
- Operations requiring different tool/permission restrictions
- Tasks suitable for cheaper models (Haiku)
- Parallel research or exploration

**Use CLAUDE.md for:**
- Always-loaded project context
- Coding conventions that apply everywhere
- Team-wide instructions

#### Migration Path

```
Legacy command: .claude/commands/review.md
    becomes
Skill: .claude/skills/review/SKILL.md
```

Both `/review` work identically. Legacy files continue working indefinitely, but new development should use skills for:
- Auto-loading capability
- Frontmatter configuration
- Supporting file directories
- Bundled scripts

---

### Skill Invocation Patterns

#### Manual Invocation

```
/skill-name                    # No arguments
/skill-name argument           # Single argument
/skill-name arg1 arg2 arg3     # Multiple arguments
```

#### Argument Access

| Variable | Contains |
|----------|----------|
| `$ARGUMENTS` | Everything after command name |
| `$ARGUMENTS[0]` or `$0` | First positional argument |
| `$ARGUMENTS[1]` or `$1` | Second positional argument |
| `$N` | Nth positional argument |

**Example SKILL.md:**

```yaml
---
name: migrate-component
argument-hint: [component] [from-framework] [to-framework]
---

Migrate the $0 component from $1 to $2.
```

Usage: `/migrate-component SearchBar React Vue`

#### Dynamic Context with Shell Execution

The `!`command\`\` syntax executes shell commands at skill load time:

```markdown
## Current Branch
!`git branch --show-current`

## Recent Commits
!`git log --oneline -5`
```

Output is inserted into skill content before Claude processes it.

#### Programmatic Invocation

From within SKILL.md instructions:
```markdown
After analysis, invoke the `reporter` skill to generate the final document.
```

---

## Patterns Catalog

### Pattern 1: Reference Knowledge

**Description:** Injects domain expertise into conversation without step-by-step workflow

**When to use:** Coding conventions, API documentation, style guides

**Example:**
```yaml
---
name: api-conventions
description: Company API design standards. Load when designing endpoints or reviewing API code.
disable-model-invocation: false
user-invocable: false
---

# API Design Standards

## Naming Conventions
- Use plural nouns for collections: `/users`, `/orders`
- Use kebab-case: `/user-profiles`
...
```

### Pattern 2: Task Workflow

**Description:** Step-by-step process for completing a specific task

**When to use:** Build processes, deployment, code generation

**Example:**
```yaml
---
name: deploy-staging
description: Deploy application to staging environment. Use when user mentions staging deployment or release preparation.
disable-model-invocation: true
allowed-tools: Bash(git *), Bash(docker *)
---

# Staging Deployment

## Prerequisites
- [ ] All tests passing
- [ ] Version bumped

## Steps
1. Build Docker image: `docker build -t app:staging .`
2. Push to registry: `docker push registry/app:staging`
...
```

### Pattern 3: Script Automation

**Description:** Offload computational work to bundled scripts

**When to use:** Data transformations, file processing, complex calculations

**Example:**
```yaml
---
name: pdf-processor
allowed-tools: Bash(python3 *)
---

# PDF Processing

Use the bundled script to extract content:

```bash
python3 {baseDir}/scripts/extract_pdf.py "$INPUT_FILE"
```

Parse the JSON output and present findings to user.
```

### Pattern 4: Template-Based Generation

**Description:** Fill templates with generated content

**When to use:** Document generation, code scaffolding

**Example:**
```yaml
---
name: proposal-generator
---

# Proposal Generator

1. Read template from `{baseDir}/assets/proposal-template.html`
2. Gather requirements from user
3. Fill placeholders: {{CLIENT_NAME}}, {{PROJECT_SCOPE}}, {{TIMELINE}}
4. Write completed proposal to user-specified location
```

### Pattern 5: Forked Context Specialist

**Description:** Run skill in isolated subagent for clean separation

**When to use:** Verbose operations, different tool restrictions

**Example:**
```yaml
---
name: security-scanner
context: fork
agent: general-purpose
model: opus
allowed-tools: Read, Grep, Glob
---

# Security Analysis

Analyze codebase for vulnerabilities. Return findings as structured JSON.
Do not modify any files.
```

### Pattern 6: Wizard-Style Workflow

**Description:** Multi-phase task with user confirmation between steps

**When to use:** Complex operations requiring validation

**Example:**
```yaml
---
name: database-migration
disable-model-invocation: true
---

# Database Migration Wizard

## Phase 1: Analysis
Analyze current schema and proposed changes. Present summary to user.

**STOP and wait for user confirmation before proceeding.**

## Phase 2: Generation
Generate migration scripts. Show user the SQL.

**STOP and wait for user approval.**

## Phase 3: Execution
Apply migrations to target database.
```

### Pattern 7: Progressive Reference Loading

**Description:** Keep SKILL.md lean, load details on demand

**When to use:** Large documentation, mutually exclusive contexts

**Example:**
```yaml
---
name: error-handler
---

# Error Handling

Load the appropriate reference based on error type:
- For HTTP errors: Read `{baseDir}/references/HTTP_ERRORS.md`
- For Database errors: Read `{baseDir}/references/DB_ERRORS.md`
- For Auth errors: Read `{baseDir}/references/AUTH_ERRORS.md`
```

### Pattern 8: Validation-Execute Pattern

**Description:** Verify conditions before destructive operations

**When to use:** Batch operations, deletions, external API calls

**Example:**
```yaml
---
name: batch-processor
---

# Batch Processing

## Pre-Validation
1. Generate list of items to process
2. Show user the complete list
3. Wait for explicit approval

## Execution
Only after approval, process each item and log results.

## Post-Validation
Verify all items processed successfully. Report any failures.
```

---

## Recency Notes

### Changes in 2025

| Date | Change |
|------|--------|
| October 2025 | Agent Skills initial release |
| December 2025 | Open standard published at agentskills.io |
| December 18, 2025 | Organization-level skill deployment shipped |
| Late 2025 (v2.1.3) | Slash commands merged into skills |

### Changes in 2026

| Date | Change |
|------|--------|
| January 2026 | OpenAI adopts Agent Skills format for Codex CLI |
| January 2026 | SkillsMP directory reaches 96,751+ skills |
| February 2026 | Current documentation reflects unified system |

### Deprecated Patterns

1. **Separate commands directory**: Still works but skills preferred
2. **`when_to_use` field**: Undocumented, may be deprecated; use `description`
3. **Windows-style paths**: Use forward slashes only

### Known Issues (February 2026)

1. `allowed-tools` may not be enforced (GitHub #18837)
2. `context: fork` may be ignored in Skill tool invocation (GitHub #17283)
3. `argument-hint` with brackets can cause TUI hang (GitHub #22161)
4. Auto-activation reliability varies (~20-84% depending on technique)

---

## Recommendations for Skill-Forge

Based on this research, skill-forge should implement:

### Core Requirements

1. **Generate valid SKILL.md** with required `name` and `description` fields
2. **Enforce naming constraints**: lowercase, alphanumerics, hyphens, 1-64 chars
3. **Create standard directory structure**: `SKILL.md` + optional `scripts/`, `references/`, `assets/`
4. **Use `{baseDir}` placeholder** for all file references

### Description Generation

1. **Apply WHEN + WHEN NOT pattern** for optimal triggering
2. **Include action verbs** and specific trigger conditions
3. **Stay under 1024 characters**
4. **Use third person**

### Frontmatter Handling

1. **Support all documented fields** (see Frontmatter Fields section)
2. **Default sensible values**: `disable-model-invocation: false`, `user-invocable: true`
3. **Validate field constraints** (character limits, allowed values)

### Content Generation

1. **Keep SKILL.md under 500 lines**
2. **Use progressive disclosure** - link to reference files for details
3. **Include concrete examples**
4. **Structure with headers and code blocks**

### Advanced Features

1. **Support `context: fork`** for isolated execution
2. **Handle `allowed-tools`** with proper syntax
3. **Generate argument handling** with `$ARGUMENTS` and `$N` variables
4. **Bundle scripts** in `scripts/` directory with proper invocation patterns

### Validation

1. **Check name format** against regex: `^[a-z0-9]+(-[a-z0-9]+)*$`
2. **Verify description non-empty** and under 1024 chars
3. **Warn about known issues** (auto-activation reliability, context fork limitations)

---

## Appendix: Full Frontmatter Field Reference

```yaml
---
# REQUIRED
name: skill-name                    # 1-64 chars, lowercase alphanumeric + hyphens
description: >                      # 1-1024 chars, triggers auto-invocation
  What the skill does and when Claude should use it.

# INVOCATION CONTROL
disable-model-invocation: false     # true = manual /name only
user-invocable: true                # false = hide from slash menu
argument-hint: [arg1] [arg2]        # autocomplete hint

# EXECUTION CONTEXT
context: fork                       # fork = run in subagent
agent: Explore                      # Explore | Plan | general-purpose
model: opus                         # sonnet | opus | haiku | inherit | model-id
mode: true                          # categorize as mode command

# TOOL ACCESS
allowed-tools: Read, Grep, Bash(git *) # pre-approved tools

# METADATA
license: MIT                        # license identifier
version: 1.0.0                      # version tracking
compatibility: Claude Code >=2.0   # environment requirements (max 500 chars)
metadata:                           # arbitrary key-value pairs
  author: Team Name
  category: development
---
```
