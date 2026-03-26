# Phase 2 Session 4: Scripts, Context & Progressive Disclosure

**Research Date:** 2026-02-11
**Scope:** External research only - official documentation, GitHub repos, and web sources
**Focus:** Best practices for scripts, context management, and progressive disclosure in Claude Code

---

## Executive Summary

1. **Progressive Disclosure is the Core Architecture** - Skills implement a 3-tier loading pattern: metadata (~100 tokens) → SKILL.md (<5k tokens) → bundled resources (on-demand). This filesystem-based approach means unused content consumes zero tokens.

2. **Scripts vs LLM: Degrees of Freedom** - Match instruction specificity to task fragility: High freedom (text) for flexible tasks, Medium freedom (pseudocode/parameterized scripts) for guided operations, Low freedom (exact scripts) for fragile/deterministic operations like database migrations.

3. **Context Window is a Shared Resource** - Every token competes with conversation history. Skills should assume Claude is intelligent and only provide context Claude lacks. Challenge each piece of information: "Would removing this cause Claude to make mistakes?"

4. **Subagents for Context Isolation** - Each subagent gets its own 200K token context window. Use them for research/investigation to keep main context clean. Teams using subagents correctly see 2-3x productivity gains.

5. **CLAUDE.md Should Be "Ruthlessly Pruned"** - Keep to 50-60 lines maximum. Use `/docs` folder for domain-specific gotchas, custom agents for specialized domains, and automated tools for enforceable rules.

6. **Reference Files: One Level Deep** - All reference files should link directly from SKILL.md. Avoid nested references as Claude may partially read files and miss complete information.

7. **Settings Hierarchy is Strict** - Enterprise policies → CLI flags → Local project → Shared project → User settings. Higher scopes always override lower ones; no user setting can override a managed policy.

---

## Sources Consulted

| Source | URL | Type | Notes |
|--------|-----|------|-------|
| Anthropic Official Blog | https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills | Official | Core skills architecture announcement |
| Claude Platform Docs - Best Practices | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | Official | Comprehensive authoring guide |
| Claude Platform Docs - Overview | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | Official | Skills architecture overview |
| Claude Platform Docs - Compaction | https://platform.claude.com/docs/en/build-with-claude/compaction | Official | Context compaction behavior |
| GitHub anthropics/skills | https://github.com/anthropics/skills | Official | Reference implementations |
| GitHub skill-creator SKILL.md | https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md | Official | Meta-skill for creating skills |
| Lee Hanchung Deep Dive | https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/ | Analysis | Technical architecture analysis |
| Mikhail Shilkov Skills Internals | https://mikhail.io/2025/10/claude-code-skills/ | Analysis | Structure and invocation patterns |
| Progressive Disclosure Blog | https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/ | Practitioner | Four-layer architecture for CLAUDE.md |
| Claude Code Docs - Settings | https://code.claude.com/docs/en/settings | Official | Settings hierarchy and permissions |
| Claude Code Docs - Sub-agents | https://code.claude.com/docs/en/sub-agents | Official | Subagent patterns |
| Claude Code Docs - Hooks | https://code.claude.com/docs/en/hooks | Official | Hook lifecycle events |
| GitHub PreCompact Hook Issue | https://github.com/anthropics/claude-code/issues/17237 | Feature Request | Context preservation strategies |
| VentureBeat Skills Article | https://venturebeat.com/technology/how-anthropics-skills-make-claude-faster-cheaper-and-more-consistent-for-business-workflows/ | Press | Business context and benefits |
| Various eesel.ai guides | https://www.eesel.ai/blog/ | Practitioner | Multiple practical guides |

---

## Detailed Findings

### Script Integration

#### Directory Structure

Skills bundle scripts in a `scripts/` directory within the skill folder:

```
skill-name/
├── SKILL.md
├── scripts/
│   ├── validate_form.py
│   ├── extract_data.py
│   └── helper.sh
├── references/
│   └── api-docs.md
└── assets/
    └── template.docx
```

#### Python Script Patterns

Python scripts are the primary scripting mechanism. Key patterns:

1. **Self-Contained Scripts** - Use only built-in libraries when possible to avoid dependency issues
2. **Clear Input/Output** - Scripts receive arguments via command line, output via stdout
3. **Error Handling** - Provide helpful error messages, not stack traces
4. **Cross-Platform** - Use forward slashes in paths (`scripts/helper.py`, not `scripts\helper.py`)

Example from codebase-visualizer skill:
```bash
python ~/.claude/skills/codebase-visualizer/scripts/visualize.py .
```

#### Bash Script Patterns

Bash scripts for simpler operations or orchestration:

1. **Permission Patterns** - Skills can pre-approve bash commands via `allowed-tools` frontmatter (e.g., `Bash(git:*)`)
2. **Wildcards for Granular Control** - `Bash(npm:*)` permits only npm operations
3. **Chain Commands** - Use `&&` for sequential operations with dependencies

#### How Skills Invoke Scripts

Scripts are invoked via the Bash tool. Critical distinction:

- **Script code never enters context** - Only the script's output consumes tokens
- **Explicit execution intent** - SKILL.md must clearly state whether to execute or read:
  - Execute: "Run `analyze_form.py` to extract fields"
  - Reference: "See `analyze_form.py` for the extraction algorithm"

#### Script Input/Output Patterns

**Input Methods:**
- Command-line arguments for simple inputs
- Stdin for structured data (JSON)
- File paths for document processing
- Environment variables for configuration

**Output Patterns:**
- Stdout for results (consumed as tool response)
- JSON for structured data
- Exit codes for success/failure (0 = success, non-zero = failure)
- Stderr for error messages

**Plan-Validate-Execute Pattern:**
For complex batch operations:
1. Create a structured plan file (e.g., `changes.json`)
2. Validate with a script before execution
3. Execute only after validation passes
4. Verify the output

This catches errors early and provides clear debugging feedback.

---

### When Scripts vs LLM

#### Decision Criteria: Degrees of Freedom

The fundamental principle is matching instruction specificity to task characteristics:

| Freedom Level | When to Use | Implementation | Example |
|--------------|-------------|----------------|---------|
| **High** | Multiple valid approaches, context-dependent decisions, heuristic guidance | Text-based instructions | Code review: analyze structure, check for bugs, suggest improvements |
| **Medium** | Preferred pattern exists, some variation acceptable, configuration affects behavior | Pseudocode or scripts with parameters | Report generation with customizable templates |
| **Low** | Exact sequence required, fragile operations, error-prone steps | Specific scripts, few/no parameters | Database migrations that must run in exact order |

#### Analogy: Robot on a Path

"Think of Claude as a robot exploring a path":
- **Narrow bridge with cliffs** → Specific guardrails needed (low freedom, exact scripts)
- **Open field, no hazards** → General direction sufficient (high freedom, text instructions)

#### Fragile Operations Requiring Scripts

Operations where scripts are essential:

1. **Database Migrations** - Must run in exact sequence
2. **File System Operations** - Bulk rename, move, delete operations
3. **Data Transformations** - Complex computations better expressed in code
4. **Form Field Extraction** - Deterministic parsing of structured documents
5. **Validation Operations** - Checking data integrity, schema compliance
6. **Build/Deploy Steps** - CI/CD-like workflows with dependencies

#### Determinism Requirements

Use scripts when you need:
- **Reproducible results** - Same input always produces same output
- **No hallucination risk** - Critical data must be accurate
- **Audit trails** - Operations must be logged consistently
- **Error recovery** - Clear rollback procedures

#### LLM is Better For

- Intent matching and skill selection
- Workflow orchestration and decision-making
- Contextual adaptation based on user requirements
- Complex reasoning tasks
- Natural language generation
- Code review and analysis

---

### Progressive Disclosure

#### 3-Tier Loading Architecture

**Level 1: Metadata (Always Loaded)**
- YAML frontmatter only: `name` and `description`
- Cost: ~100 tokens per skill
- Purpose: Enable Claude to decide when to invoke each skill
- Implementation: Aggregated into `<available_skills>` section in Skill tool description (limited to 15,000 characters)

**Level 2: Full Instructions (Triggered Loading)**
- Complete SKILL.md body
- Cost: Under 5,000 tokens (recommended under 500 lines)
- Purpose: Detailed procedural knowledge, workflows, best practices
- Loaded when: Claude determines the skill matches user intent

**Level 3: Bundled Resources (As-Needed Loading)**
- Additional files in references/, scripts/, assets/
- Cost: Zero until accessed
- Purpose: Specialized documentation, reference data, templates
- Loaded when: Explicitly referenced during skill execution

#### How to Structure for Progressive Loading

**Pattern 1: High-Level Guide with References**
```markdown
# SKILL.md

Quick-start content here (under 500 lines)

For form-filling operations, see `reference/FORMS.md`
For API details, see `reference/API.md`
For usage examples, see `reference/EXAMPLES.md`
```

**Pattern 2: Domain-Specific Organization**
```
bigquery-skill/
├── SKILL.md (overview)
└── reference/
    ├── finance.md
    ├── sales.md
    ├── product.md
    └── marketing.md
```

**Pattern 3: Conditional Details**
Show basic content inline, link advanced topics separately. Use `<details>` tags for deprecated methods or historical context.

#### Critical Constraint: One Level Deep

**All reference files should link directly from SKILL.md.**

Avoid nested references. Claude may partially read files when encountering nested references, missing complete information.

```
GOOD:
SKILL.md → reference/api.md
SKILL.md → reference/forms.md

BAD:
SKILL.md → reference/index.md → reference/api.md
```

#### Token Budget Considerations

- **SKILL.md body**: Keep under 500 lines for optimal performance
- **Reference files over 100 lines**: Include table of contents at top so Claude sees full scope during partial reads
- **Available skills section**: Limited to 15,000 characters total
- **Scripts**: Code never loads into context; only output consumes tokens
- **Assets**: Referenced by path only; never loaded into context

#### When to Put Content Inline vs References

**Inline in SKILL.md:**
- Core workflow steps (always needed)
- Critical constraints and warnings
- Primary examples
- Quick-start instructions

**In Reference Files:**
- Domain-specific variations
- Advanced/edge cases
- Deprecated patterns (use `<details>` tags)
- Comprehensive API documentation
- Large example sets

---

### Context Management

#### Context Window as Shared Resource

"The context window is a public good." Every token competes with:
- System prompts
- Conversation history
- Other skills' metadata
- Tool results
- User messages

Key principle: Challenge each piece of information by asking:
1. "Does Claude already know this?"
2. "Would removing this cause Claude to make mistakes?"

#### How to Minimize Context Usage

1. **Assume Claude's Intelligence** - Only provide context Claude lacks
2. **Use Progressive Disclosure** - Load information only when needed
3. **Scripts Over Generated Code** - Script output consumes fewer tokens than having Claude write and execute code
4. **Clear Context Between Tasks** - Use `/clear` or start new sessions
5. **Monitor Context Meter** - `/compact` proactively at 70% capacity

#### Subagent Context Isolation

Each subagent operates with:
- Own 200K token context window
- Custom system prompt
- Specific tool access
- Independent permissions

**Key Benefits:**
- Prevents context pollution
- Verbose output stays in subagent context
- Only relevant summary returns to main conversation
- Teams see 2-3x productivity gains with proper subagent use

**Token Efficiency Pattern:**
```
Main Context: Clean implementation discussion
    └── Subagent 1: Test exploration (verbose output contained)
    └── Subagent 2: Documentation research (verbose output contained)
    └── Subagent 3: Codebase analysis (verbose output contained)
```

**Shared Memory Pattern:**
Instead of passing massive contexts between agents, use markdown files as shared memory. This trick alone cut token usage by 50-60% in reported cases.

#### Subagent Limitations

- Cannot spawn other subagents
- Work in isolation with no direct awareness of other subagents
- Main agent must wait for all reports before synthesizing
- Maximum ~10 parallel subagents (additional are queued)

#### Compaction Behavior

**Auto-Compact Trigger:** ~95% capacity (or 25% remaining)

**How It Works:**
1. System detects input tokens exceed threshold
2. Claude generates conversation summary
3. Compaction block contains the summary
4. Response continues with compacted context

**Manual Control:**
- `/compact` - Trigger manually
- `/compact only keep X` - Custom preservation instructions
- `Esc + Esc` or `/rewind` - Partial compaction from checkpoint

**Customizing via CLAUDE.md:**
```markdown
When compacting, always preserve:
- Full list of modified files
- Test commands used
- Key architectural decisions
```

#### PreCompact Hook for Context Preservation

**Status:** Feature requested but not fully implemented (Issue #17237)

**Proposed Capability:**
- `PreCompact` hook fires before summarization begins
- Receives: messages_to_compact, current_summary, session_id, cwd
- Can output: inject_into_summary, extracted_data

**Current Workarounds:**
- SessionEnd hooks to parse transcripts
- Manual compaction with preservation instructions
- Writing critical info to files before compaction

---

### Reference Files

#### references/ Directory Patterns

Location within skill:
```
skill-name/
├── SKILL.md
├── references/
│   ├── api-docs.md
│   ├── schema.json
│   ├── examples.md
│   └── troubleshooting.md
```

**Content Types:**
- Markdown documentation
- JSON schemas
- Configuration templates
- Example collections
- Domain-specific guides

#### How to Organize References

**By Domain:**
```
references/
├── finance.md
├── sales.md
├── product.md
└── marketing.md
```

**By Function:**
```
references/
├── api.md
├── forms.md
├── validation.md
└── examples.md
```

**By Complexity:**
```
references/
├── quickstart.md
├── advanced.md
└── troubleshooting.md
```

#### Linking from SKILL.md

**Explicit References:**
```markdown
For form-filling operations, see `references/forms.md`
For API details, consult `references/api.md`
```

**Conditional Loading:**
```markdown
If extracting tables → see `references/tables.md`
If working with images → see `references/images.md`
```

**Signal File Purpose:**
Provide enough context that Claude knows WHEN to load:
```markdown
`references/forms.md` - Use when filling PDF forms or extracting form fields
`references/api.md` - Use when making API calls to external services
```

#### Index Files Patterns

For reference directories with many files, consider an index:

```markdown
# references/index.md

## Available References

| File | When to Use |
|------|-------------|
| forms.md | PDF form filling operations |
| api.md | External API integration |
| validation.md | Data validation rules |
```

**Important:** Keep index as the ONLY intermediary - all docs should still be one level from SKILL.md via the index.

#### Table of Contents in Long References

For reference files exceeding 100 lines:
```markdown
# API Reference

## Contents
1. Authentication
2. Endpoints
3. Error Codes
4. Rate Limits
5. Examples

---

## 1. Authentication
...
```

This ensures Claude sees the full scope even during partial reads.

---

### CLAUDE.md Patterns

#### What Goes in CLAUDE.md

**Essential Content Only (~50-60 lines):**

1. **Project Overview** (2-3 sentences)
   - What the project is
   - Tech stack summary
   - High-level architecture

2. **Essential Commands**
   - Dev server: `pnpm dev`
   - Tests: `pnpm test`
   - Lint: `pnpm lint:fix`
   - Build: `pnpm build`

3. **Critical Constraints**
   - Must-follow patterns
   - Security requirements
   - Breaking change warnings

4. **Pointers to Docs**
   - "IMPORTANT: Read relevant docs below before starting any task"
   - "For complex usage, see `docs/X.md`"

#### Project vs User Level

| Location | Scope | Use Case |
|----------|-------|----------|
| `~/.claude/CLAUDE.md` | All projects | Personal preferences, global patterns |
| `./CLAUDE.md` | Current project | Team standards, project-specific |
| `./CLAUDE.local.md` | Current project, not committed | Personal project overrides |
| `./subdir/CLAUDE.md` | Subdirectory | Monorepo-specific instructions |

**Hierarchical Loading:**
1. Home directory (`~/.claude/CLAUDE.md`)
2. Project root (`./CLAUDE.md`)
3. Individual directories (on demand)

#### Keeping It Focused ("Ruthlessly Pruned")

**The Litmus Test:**
For each line, ask: "Would removing this cause Claude to make mistakes?"
If not, cut it.

**Anti-Patterns to Avoid:**
- Embedding entire files (use references instead)
- Negative-only instructions ("Never use X" without alternative)
- Basic concepts Claude already knows
- Time-sensitive information
- Excessive examples

**Prefer Automated Enforcement:**
If a tool can enforce it, don't write prose about it:
- ESLint for code style
- TypeScript for type safety
- Prettier for formatting
- Husky for pre-commit checks

#### Integration with Skills

**@Import Syntax:**
```markdown
@README.md - Project overview
@package.json - Available npm commands
```

**Skills Reference:**
```markdown
For specialized tasks, Claude can use skills in `.claude/skills/`
```

**CLAUDE.md + Skills Division:**
- CLAUDE.md: What applies to ALL work in this project
- Skills: Specialized knowledge for specific task types

---

### Settings Integration

#### settings.json Patterns

**Location Hierarchy (highest to lowest priority):**
1. Enterprise Managed (`C:\Program Files\ClaudeCode\managed-settings.json` or system paths)
2. Command-Line Flags (session only)
3. Local Project (`.claude/settings.local.json`)
4. Shared Project (`.claude/settings.json`)
5. Global User (`~/.claude/settings.json`)

**Basic Structure:**
```json
{
  "permissions": {
    "allow": ["Bash(git:*)", "Read", "Write"],
    "deny": ["Bash(rm -rf *)"],
    "ask": ["Bash(npm:*)"]
  },
  "env": {
    "MY_API_KEY": "value"
  },
  "hooks": {
    "PreToolUse": [...]
  }
}
```

#### Permissions Integration

**Permission Modes:**
- `allow` - Automatic execution (no prompt)
- `ask` - Prompt user for confirmation
- `deny` - Block execution

**Rule Evaluation Order:**
1. Deny rules first
2. Then ask rules
3. Then allow rules
4. First matching rule wins

**Wildcard Patterns:**
```json
{
  "allow": [
    "Bash(git:*)",
    "Bash(npm:*)",
    "Read",
    "Write"
  ]
}
```

#### Environment Variables

**Setting via settings.json:**
```json
{
  "env": {
    "ANTHROPIC_API_KEY": "sk-...",
    "MY_SERVICE_URL": "https://api.example.com"
  }
}
```

**Key Variables:**
- `ANTHROPIC_API_KEY` - API authentication
- `CLAUDE_CODE_SUBAGENT_MODEL` - Model for subagents
- `HTTPS_PROXY` - Corporate proxy
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` - Disable telemetry

**API Key Priority:**
Environment variable API keys are prioritized over authenticated subscriptions. Set `ANTHROPIC_API_KEY` only if you want to use pay-as-you-go billing.

#### Scope Hierarchy (Managed, Project, User, Local)

| Scope | Location | Override Behavior |
|-------|----------|-------------------|
| Managed | System paths | Cannot be overridden |
| CLI Flags | Command line | Override user/project |
| Local Project | `.claude/settings.local.json` | Override shared/user |
| Shared Project | `.claude/settings.json` | Override user |
| User | `~/.claude/settings.json` | Base defaults |

**Enterprise Lock-Down:**
When `allowManagedPermissionRulesOnly: true` is set in enterprise settings:
- Only managed-level permission rules take effect
- User and project-level allow/ask/deny arrays are ignored
- Prevents permission escalation beyond organization policy

---

### Token Efficiency Patterns

#### Minimizing Context Usage

1. **Progressive Disclosure** - Load only what's needed
2. **Scripts Over Code Generation** - Output vs full code
3. **Subagent Delegation** - Isolate verbose operations
4. **Reference Files** - Don't embed, reference
5. **Focused CLAUDE.md** - 50-60 lines max

#### When to Load vs Not Load

**Load Immediately:**
- Core workflow instructions
- Critical constraints
- Error handling guidance

**Load On-Demand:**
- Domain-specific details
- Advanced patterns
- Historical context
- API documentation

**Never Load:**
- Content Claude already knows
- Enforceable rules (use tooling)
- Time-sensitive information
- Redundant examples

#### Fan-Out Patterns

**Parallel Subagent Dispatch:**
```
Main Agent
    ├── Research Agent 1 (component A)
    ├── Research Agent 2 (component B)
    ├── Research Agent 3 (component C)
    └── Collect and synthesize results
```

**Codebase Exploration:**
- Primary agent lists all functions/files
- Spin up subagent for each to analyze
- Final agent assembles into documentation

**Bulk Operations:**
- Primary agent greps for all instances
- Spin up subagent per file for replacements
- Each subagent has small, safe context

#### Scoped Investigation

**The "Core Trio" Pattern:**
- Product-manager agent: Define user stories
- UX-designer agent: Propose user flows
- Engineer agent: Outline technical plan

**Model Optimization:**
Set `CLAUDE_CODE_SUBAGENT_MODEL` to use cheaper models for subagent work:
- Main session: Opus for complex reasoning
- Subagents: Sonnet for focused tasks

---

## Patterns Catalog

### Pattern 1: Script-Based Validation Loop

**Description:** Use scripts to validate operations before and after execution

**When to Use:**
- Form filling operations
- Data transformations
- Any operation where errors are costly

**Example:**
```markdown
## Form Filling Workflow

1. Run `scripts/analyze_form.py` to extract field structure
2. Review extracted fields in output
3. Create field mapping in `data/mapping.json`
4. Run `scripts/validate_mapping.py` to verify
5. Only if validation passes, run `scripts/fill_form.py`
6. Run `scripts/verify_output.py` to confirm
```

---

### Pattern 2: Domain-Organized References

**Description:** Organize reference files by domain for selective loading

**When to Use:**
- Multi-domain skills
- Large reference sets
- Teams with specialized knowledge areas

**Example:**
```
references/
├── index.md (table of contents)
├── finance.md
├── sales.md
├── engineering.md
└── legal.md
```

SKILL.md references:
```markdown
Determine the domain of the request:
- Financial data → see `references/finance.md`
- Sales metrics → see `references/sales.md`
- Technical specs → see `references/engineering.md`
```

---

### Pattern 3: Degrees of Freedom Matching

**Description:** Match instruction specificity to task fragility

**When to Use:** Always - this is a fundamental principle

**Example:**
```markdown
## Task-Specific Instructions

### Code Reviews (High Freedom)
Analyze the code for bugs, style issues, and improvements.
Use your judgment on what to highlight.

### Report Generation (Medium Freedom)
Use the template in `assets/report-template.md`
Customize sections based on available data.
Required sections: Summary, Findings, Recommendations.

### Database Migration (Low Freedom)
Execute EXACTLY these commands in order:
1. `python scripts/backup_db.py`
2. `python scripts/migrate_v2.py`
3. `python scripts/verify_migration.py`
DO NOT proceed if any step fails.
```

---

### Pattern 4: Progressive CLAUDE.md Architecture

**Description:** Four-layer architecture for token-efficient context

**When to Use:** All projects using Claude Code

**Example:**
```
Layer 1: CLAUDE.md (50 lines, always loaded)
Layer 2: /docs folder (loaded on reference)
Layer 3: .claude/agents/ (loaded via Task tool)
Layer 4: Automated tools (ESLint, TypeScript, Prettier)
```

CLAUDE.md structure:
```markdown
# Project Name

Brief overview (2-3 sentences)

## Commands
- `pnpm dev` - Start dev server
- `pnpm test` - Run tests

## Stack
React, TypeScript, PostgreSQL

## IMPORTANT
Read relevant docs before starting any task:
- `docs/patterns.md` - Project patterns
- `docs/gotchas.md` - Known issues
```

---

### Pattern 5: Subagent Research Delegation

**Description:** Use subagents for research to preserve main context

**When to Use:**
- Codebase exploration
- Documentation research
- Test execution with verbose output
- Log analysis

**Example:**
```markdown
## Codebase Analysis Workflow

1. Dispatch parallel subagents:
   - Agent 1: Explore `src/components/`
   - Agent 2: Explore `src/services/`
   - Agent 3: Explore `src/utils/`

2. Each agent returns summary only

3. Main agent synthesizes findings

4. Verbose exploration output never enters main context
```

---

### Pattern 6: PreToolUse Hook Enforcement

**Description:** Use hooks to enforce standards before tool execution

**When to Use:**
- Code style enforcement
- Security checks
- Mandatory formatting

**Example Configuration:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "match": ["Write", "Edit"],
        "pattern": "*.py",
        "command": "black ${file}"
      }
    ],
    "PreToolUse": [
      {
        "match": ["Bash"],
        "pattern": "rm -rf *",
        "action": "deny"
      }
    ]
  }
}
```

---

### Pattern 7: Table of Contents for Long References

**Description:** Add navigation for files over 100 lines

**When to Use:**
- Reference files > 100 lines
- Complex API documentation
- Multi-section guides

**Example:**
```markdown
# API Reference

## Contents
1. [Authentication](#authentication)
2. [Endpoints](#endpoints)
3. [Error Codes](#error-codes)
4. [Rate Limits](#rate-limits)
5. [Examples](#examples)

---

## Authentication
...
```

---

### Pattern 8: Shared Memory via Files

**Description:** Use markdown files as inter-agent shared memory

**When to Use:**
- Multi-agent workflows
- Long-running investigations
- Cross-session continuity

**Example:**
```markdown
## Workflow

1. Agent A writes findings to `scratch/findings.md`
2. Agent B reads `scratch/findings.md` for context
3. Final agent synthesizes from `scratch/*.md`

Token savings: 50-60% vs passing context between agents
```

---

## Recency Notes

### What Changed in 2025/2026

**October 2025:**
- Agent Skills officially announced (Oct 16, 2025)
- Skills available across Claude.ai, Code, and API

**December 2025:**
- Agent Skills published as open standard for cross-platform portability (Dec 18, 2025)

**September 2025:**
- "Context editing" and "memory tool" announced
- Automatic clearing of stale tool calls
- Completion buffer prevents mid-operation compaction

**2026 Updates:**
- Compaction now available on Claude Opus 4.6 with `compact-2026-01-12` beta header
- Windows enterprise settings path updated to `C:\Program Files\ClaudeCode\managed-settings.json` (v2.1.2)
- PreToolUse hooks can now modify tool inputs before execution (v2.0.10)

### Deprecated Patterns

- ~~Time-sensitive deprecation dates~~ → Use "Old patterns" sections with collapsed details
- ~~Windows backslash paths~~ → Always use forward slashes for cross-platform compatibility
- ~~Old Windows managed settings path~~ → Use new `C:\Program Files\ClaudeCode\` path

---

## Recommendations for Skill-Forge

Based on this research, skill-forge should implement:

### 1. Progressive Disclosure from Day One
- Always generate 3-tier structure: metadata → SKILL.md → references/
- Enforce 500-line limit on SKILL.md with automatic suggestions to split

### 2. Degrees of Freedom Framework
- Ask users about task fragility during skill creation
- Suggest text vs pseudocode vs exact scripts based on answers
- Include examples of each freedom level in templates

### 3. Reference Organization Patterns
- Generate references/ directory by default
- Enforce one-level-deep linking
- Auto-generate table of contents for files > 100 lines
- Create index.md for skills with 3+ reference files

### 4. Script Integration Templates
- Provide Python and Bash script templates
- Include plan-validate-execute pattern template
- Show input/output patterns clearly
- Include error handling boilerplate

### 5. Context Efficiency Guidance
- Show estimated token counts during creation
- Warn when SKILL.md exceeds 300 lines (suggest splitting at 500)
- Suggest subagent patterns for complex operations
- Include shared-memory file patterns

### 6. Settings Integration
- Generate appropriate permissions in settings.json
- Show allowed-tools patterns for scripts
- Include hook templates for common enforcement needs

### 7. Testing/Iteration Workflow
- Include evaluation structure in templates
- Provide test-across-models checklist
- Include observation patterns for navigation analysis

### 8. Anti-Pattern Detection
- Warn about nested references
- Flag Windows-style paths
- Detect unclear execution intent for scripts
- Check for assumed package availability
