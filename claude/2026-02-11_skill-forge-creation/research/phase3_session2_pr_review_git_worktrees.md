# Phase 3 Session 2: PR Review + Git Worktrees Skills

## Executive Summary

1. **Hook-based compliance enforcement is a breakthrough pattern** - The `pr-review-workflow-skill` uses exit code 2 to deterministically block PR approval if skill steps weren't completed. This solves the fundamental problem of LLMs "appearing to follow" instructions without actually doing so.

2. **16-step compliance system with logging** - The PR review skill requires 16 logged markers across 3 phases before approval is permitted. Each step must call `log_compliance.sh` to write to `/tmp/pr_N_skill_compliance.log`.

3. **Script-to-LLM balance is well-designed** - Scripts handle deterministic tasks (staleness checking, file classification, template generation) while LLM handles judgment tasks (scope analysis, code review, decision making).

4. **Git worktrees skill is simpler and more utility-focused** - 4 scripts for CRUD operations on worktrees, with extensive safety rules and communication requirements in SKILL.md.

5. **Both skills emphasize "narrate everything"** - Explicit instructions to explain what, why, effect, and risks before running any command. This is a sophisticated UX pattern for building user trust.

6. **AI attribution blocking via hooks** - The `block_ai_attribution.sh` hook prevents Claude's default commit/PR attribution by detecting specific patterns and returning exit code 2.

7. **Cross-skill integration** - The PR review skill calls the git-worktrees skill to create isolated review environments, demonstrating skill composition.

---

## Files Analyzed

### PR Review Workflow Skill
| File | Lines | Purpose |
|------|-------|---------|
| `SKILL.md` | 1,179 | Comprehensive 4-phase workflow with compliance enforcement |
| `scripts/gather_pr_info.sh` | 27 | Fetches PR metadata via `gh` CLI |
| `scripts/prepare_local_env.sh` | 91 | Ensures local main is clean before review |
| `scripts/check_staleness.sh` | 115 | Classifies files as DUPLICATE/MODIFIED/NEW |
| `scripts/classify_files.sh` | 82 | Categorizes files by type (docs, tests, core, etc.) |
| `scripts/log_compliance.sh` | 45 | Writes step markers to compliance log |
| `scripts/generate_review_template.sh` | 101 | Creates approval/changes markdown templates |

### Git Worktrees Skill
| File | Lines | Purpose |
|------|-------|---------|
| `SKILL.md` | 459 | Usage guide with safety and communication rules |
| `scripts/create_worktree.sh` | 230 | Creates worktree with PR/branch support and env setup |
| `scripts/list_worktrees.sh` | 217 | Lists worktrees with JSON and verbose modes |
| `scripts/remove_worktree.sh` | 240 | Safe worktree removal with confirmations |
| `scripts/setup_env.sh` | 229 | Multi-language dependency installation |
| `references/worktree_best_practices.md` | 358 | Comprehensive best practices documentation |

### Hooks
| File | Lines | Purpose |
|------|-------|---------|
| `README.md` | 286 | Architecture docs and extension guide |
| `block_ai_attribution.sh` | 113 | Blocks commits/PRs with Claude attribution |
| `verify_pr_review_compliance.sh` | 152 | Blocks PR approval without skill compliance |

---

## Detailed Analysis

### PR Review Workflow Skill

#### Architecture Overview

The skill is organized into 4 sequential phases, each with specific subagent responsibilities:

```
Phase 1: Pre-Review Analysis
├── Gather PR info (gather_pr_info.sh)
├── Read linked issue (gh CLI)
├── Prepare local env (prepare_local_env.sh)
├── Check staleness (check_staleness.sh)
├── Classify files (classify_files.sh)
└── Scope analysis (LLM judgment)

Phase 2: Code Review
├── Create worktree (git-worktrees-skill integration)
├── Install dependencies (poetry/npm)
├── Load best practices (references/django_best_practices.md)
├── Review core files (LLM analysis)
├── Run tests (Django test runner)
└── Identify issues (LLM judgment)

Phase 3: Decision & Communication
├── Check conflicts (git merge-base)
├── Determine decision (LLM judgment)
├── Generate review (generate_review_template.sh)
└── Submit review (gh pr review)

Phase 4: Post-Approval
├── Notify developer
├── Document learnings
└── Handle dependent PRs
```

#### Compliance Enforcement System

The skill's most innovative feature is its **deterministic compliance enforcement**:

1. **Logging**: After each major step, Claude must run:
   ```bash
   ./scripts/log_compliance.sh <PR_NUMBER> <STEP_MARKER>
   ```

2. **Verification**: When Claude attempts `gh pr review --approve`, the `verify_pr_review_compliance.sh` hook:
   - Extracts PR number from command
   - Reads `/tmp/pr_N_skill_compliance.log`
   - Checks for all 16 required markers
   - Returns exit code 2 if any are missing

3. **Required markers**:
   - Phase 1: 7 markers (GATHER_PR_INFO, READ_LINKED_ISSUE, PREPARE_LOCAL_ENV, CHECK_STALENESS, CLASSIFY_FILES, SCOPE_CHECK, COMPLETE)
   - Phase 2: 7 markers (CREATE_WORKTREE, CHECK_DEPENDENCIES, LOAD_BEST_PRACTICES, REVIEW_CORE_FILES, RUN_TESTS, IDENTIFY_ISSUES, COMPLETE)
   - Phase 3: 2 markers (DETERMINE_DECISION, COMPLETE)

#### Trigger Pattern (from description)

The skill description uses multiple natural language triggers:
- "review PR #123"
- "help me review this pull request"
- "approve PR"
- "check this PR"
- "do a code review on PR"
- "review and approve"

This is a comprehensive trigger set covering various phrasings.

#### Key Instructions

1. **Staleness understanding** (lines 309-355): Extensive documentation on when staleness is critical vs not. This prevents over-reacting to "X commits behind" without context.

2. **Scope creep handling** (lines 381-425): Distinguishes acceptable scope creep (docs, tests) from questionable additions. Explicitly requires user decision for non-trivial scope additions.

3. **Communication rules** (lines 79-137): "NEVER draft a review or approval message without discussing findings first" - explicit instruction to present findings and wait for user direction.

4. **AI attribution prohibition** (lines 897-919): Comprehensive list of forbidden patterns in GitHub content.

---

### Git Worktrees Skill

#### Architecture Overview

Much simpler than PR review - this is a utility skill with 4 CRUD operations:

```
Operations:
├── create_worktree.sh (Create)
├── list_worktrees.sh (Read)
├── remove_worktree.sh (Delete)
└── setup_env.sh (Environment setup utility)
```

#### Safety Policy (Critical Feature)

The skill opens with a **Safety Policy** section (lines 8-33) that defines immutable constraints:
- **NEVER delete branches** - Branch deletion is manual-only
- **NEVER force-push** - No destructive git operations
- **NEVER delete files** - Only worktree directories
- **ALWAYS require confirmation** - Before removing anything

These are framed as "Claude Instructions (CRITICAL)" - direct behavioral constraints.

#### GitHub CLI Rules

Specific instructions to **never specify `--repo`** with `gh` commands (lines 31-34). This addresses a common mistake where Claude adds unnecessary flags.

#### Communication Rules - Narrate Everything

Before running ANY command, Claude must explain (lines 36-57):
1. **What** - The specific command
2. **Why** - The purpose
3. **Effect** - What will change
4. **Risks** - Potential issues

Example provided shows the level of detail expected.

#### Error Handling Rules

Explicit instructions on error handling (lines 61-84):
1. Read the full error message
2. Investigate the actual problem
3. Explain in plain language
4. Propose a fix with user approval

**Anti-pattern explicitly called out**: "WRONG: The script failed. Let me try again with --force."

---

### Script Patterns

| Script | Purpose | Input | Output | Error Handling |
|--------|---------|-------|--------|----------------|
| `gather_pr_info.sh` | Fetch PR metadata | `<PR_NUMBER>` | JSON to stdout, diff to `/tmp/pr_N_diff.txt` | `set -e` (exit on error) |
| `prepare_local_env.sh` | Clean local main | (none) | Status messages to stdout | Exit 1 with descriptive error message for staged changes, merge conflicts |
| `check_staleness.sh` | Classify file staleness | `<PR_NUMBER>` | File status to `/tmp/pr_N_file_status.txt` | `set -e`, graceful handling of missing branches |
| `classify_files.sh` | Categorize files by type | `<PR_NUMBER>` | Category counts + files to `/tmp/pr_N_{docs,infra,tests,migrations,core}.txt` | `set -e`, uses staleness data if available |
| `log_compliance.sh` | Write step markers | `<PR_NUMBER> <MARKER>` | Confirmation to stdout | `set -euo pipefail`, idempotent (skips duplicates) |
| `generate_review_template.sh` | Create review markdown | `<PR_NUMBER> <approval\|changes>` | Template to `/tmp/pr_N_review_{type}.md` | Exit 1 for invalid type |
| `create_worktree.sh` | Create worktree | `<name> [--base, --pr, --no-setup, --path]` | Status messages, colored output | `set -e`, checks for existing directory/branch |
| `list_worktrees.sh` | List worktrees | `[--verbose, --json]` | Table or JSON to stdout | `set -e`, handles offline gracefully |
| `remove_worktree.sh` | Remove worktree | `<name> [-y\|--yes]` | Warnings for uncommitted changes | Requires confirmation unless `--yes`, blocks main worktree removal |
| `setup_env.sh` | Install dependencies | `[--skip-deps, --migrate, --copy-env]` | Status messages | Auto-detects package managers, graceful fallbacks |

#### Common Patterns Across Scripts

1. **Strict error handling**: All scripts use `set -e` (exit on error). Some add `-u` (unset variables) and `-o pipefail`.

2. **Colored output**: ANSI color codes for visual hierarchy (RED for errors, GREEN for success, YELLOW for warnings, BLUE for info).

3. **Help flags**: `-h` and `--help` supported for documentation.

4. **Temp file storage**: All artifacts written to `/tmp/pr_<PR_NUMBER>_*` for easy cleanup.

5. **Repo root discovery**: Scripts navigate to repo root via `$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)`.

6. **Python for JSON parsing**: Uses `python3 -c "import sys, json; ..."` for extracting JSON fields (not `jq` consistently).

---

### Hooks Integration

#### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Skill Execution                          │
│                                                              │
│  Step 1 ──► log_compliance.sh ──► /tmp/pr_N_compliance.log  │
│  Step 2 ──► log_compliance.sh ──► /tmp/pr_N_compliance.log  │
│  ...                                                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   PreToolUse Hook                            │
│                                                              │
│  verify_compliance.sh reads /tmp/pr_N_compliance.log        │
│                                                              │
│  Missing steps? ──► exit 2 ──► ACTION BLOCKED               │
│  All steps OK?  ──► exit 0 ──► Action proceeds              │
└─────────────────────────────────────────────────────────────┘
```

#### block_ai_attribution.sh

**Purpose**: Prevents Claude's default commit/PR attribution from appearing in GitHub.

**Implementation**:
1. Reads command from stdin as JSON
2. Extracts message content from `git commit -m` or `gh pr create --body`
3. Handles both simple `-m "message"` and heredoc `$(cat <<'EOF' ... EOF)` patterns
4. Checks for specific patterns:
   - `noreply@anthropic.com`
   - `generated with [claude code]`
   - Emoji patterns like `robot: Generated with`
5. Returns exit code 2 if found, 0 if clean

**Notable**: Uses targeted patterns (not generic "Claude" or "AI" strings) to avoid false positives.

#### verify_pr_review_compliance.sh

**Purpose**: Blocks PR approval if skill steps weren't completed.

**Implementation**:
1. Reads command from stdin as JSON
2. Extracts PR number from `gh pr review N` pattern
3. Checks for existence of `/tmp/pr_N_skill_compliance.log`
4. Verifies all 16 required markers are present
5. Returns exit code 2 with detailed missing/completed step list if incomplete

**Error messages**: Extremely detailed, telling Claude exactly what's missing and how to fix it.

#### Configuration (from README.md)

Hooks are configured in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "tool == \"Bash\" && tool_input.command matches \"git commit\"",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/block_ai_attribution.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

---

## Good Patterns (Keep)

### 1. Deterministic Enforcement via Exit Codes
The use of exit code 2 to block actions is fundamentally sound. This cannot be bypassed by the LLM - it's enforced by the Claude Code runtime.

**Recommendation**: Skill-forge should support generating compliance logging scripts and verification hooks as a core feature.

### 2. Step-by-Step Compliance Logging
The `log_compliance.sh` pattern is elegant:
- Simple: just writes a marker to a file
- Idempotent: skips duplicates
- Verifiable: external hook can check all markers
- Debuggable: `cat /tmp/pr_N_skill_compliance.log` shows progress

**Recommendation**: This logging pattern should be a standard component in skill-forge.

### 3. Safety Policy as First Section
Git worktrees skill puts safety rules at the top, before any usage instructions. This ensures Claude reads them before operational details.

**Recommendation**: Skill-forge templates should include a Safety Policy section at the top for any skill that modifies files or runs commands.

### 4. Anti-Pattern Examples
Both skills include explicit "WRONG" examples:
- "WRONG: The script failed. Let me try again with --force."
- "Bad: [silently runs all commands]"

**Recommendation**: Include explicit anti-pattern examples in generated skills.

### 5. Narrate-Before-Execute Pattern
Both skills require explaining what, why, effect, and risks before running commands.

**Recommendation**: This should be a standard instruction block in skill-forge output.

### 6. Temp File Organization
Consistent `/tmp/pr_<PR_NUMBER>_*` naming convention for all artifacts.

**Recommendation**: Generate temp file naming conventions based on skill context.

### 7. Cross-Skill Integration
PR review skill calls git-worktrees skill for isolated environment setup.

**Recommendation**: Skill-forge should support declaring skill dependencies.

### 8. Decision Point Communication
Explicit instructions to present options and wait for user direction rather than making decisions unilaterally.

**Recommendation**: For skills with decision points, generate explicit option-presentation templates.

---

## Outdated Patterns (Update)

### 1. Mixed JSON Parsing Approaches
Scripts inconsistently use:
- `jq -r '.field'`
- `python3 -c "import sys, json; print(json.load(sys.stdin)['field'])"`

**Issue**: Inconsistent, harder to maintain, jq not universally available.

**Recommendation**: Standardize on one approach. Current best practice (Feb 2026) is to use `jq` consistently since it's now standard on most systems. Document jq as a dependency.

### 2. Hard-coded Repository Name
Scripts use `REPO_NAME="$(basename "$REPO_ROOT")"` and construct paths like `${REPO_NAME}-${WORKTREE_NAME}`.

**Issue**: Assumes repository naming convention (e.g., "talent_ai").

**Recommendation**: Make repository name configurable or detect from git config.

### 3. No Hook Timeout Handling
Hooks don't have internal timeout logic - rely on external timeout configuration.

**Recommendation**: Scripts should have internal timeout guards for robustness.

### 4. Legacy Emoji in Scripts
Scripts use emoji (e.g., folder:, file:) which may not render in all terminals.

**Issue**: Can break output parsing or display incorrectly.

**Recommendation**: Modern best practice is to make emoji optional via env var like `NO_EMOJI=1`.

### 5. Subagent Pattern Not Using Modern Claude Code Features
The SKILL.md references "subagents" conceptually but doesn't use the actual Task tool subagent_type pattern from Dec 2025 Claude Code updates.

**Recommendation**: Update to use explicit `Task` tool with `subagent_type` for phase delegation.

### 6. No MCP Integration
Skills don't mention MCP servers for external tool integration.

**Recommendation**: Consider MCP-based GitHub integration rather than `gh` CLI for richer error handling.

### 7. References to External URLs
The hooks README references external URLs that may become stale:
- digitalthoughtdisruption.com/...
- docs.anthropic.com/...

**Recommendation**: Include versioned references or embed critical documentation.

---

## Unique Patterns (Consider)

### 1. Staleness Education Section
The PR review skill includes 47 lines (309-355) explaining how to interpret staleness - when it matters, when it doesn't, with concrete examples.

**Why it's unique**: Most skills just say "check staleness." This one teaches the concept.

**Consideration**: Include educational sections for complex concepts that are commonly misunderstood.

### 2. GitHub CLI Version Prerequisites
Lines 150-203 include detailed instructions for upgrading `gh` CLI, including:
- Exact version requirements
- Upgrade commands
- Error pattern recognition
- Explicit "NEVER try to work around this error" instruction

**Why it's unique**: Most skills assume tools are correctly installed.

**Consideration**: Generate prerequisite checks and upgrade instructions for skills with external dependencies.

### 3. Scope Creep Taxonomy
The skill categorizes scope creep into:
- **Always acceptable**: docs, tests, minor cleanup
- **Question user about**: features marked for future, unmentioned functionality
- **Red flags**: Issue asks for 800 lines, PR delivers 2,400

**Why it's unique**: Provides a decision framework rather than just "check for scope creep."

**Consideration**: For skills with judgment calls, provide taxonomies and decision frameworks.

### 4. Confirmation Mode in Non-Interactive Terminals
`remove_worktree.sh` detects `[[ ! -t 0 ]]` (non-interactive) and provides explicit guidance:
- Suggests running manually in terminal
- Documents `--yes` flag with safety warnings
- Explains why confirmation is required

**Why it's unique**: Handles the Claude Code environment where stdin isn't interactive.

**Consideration**: All destructive scripts should handle non-interactive mode gracefully.

### 5. Worktree Best Practices Reference Doc
The 358-line `worktree_best_practices.md` is a standalone reference that could be loaded on demand.

**Why it's unique**: Separates operational instructions (SKILL.md) from educational content (references/).

**Consideration**: Generate separate reference documents for complex topics.

### 6. Hook Extension Guide
The hooks README includes a complete "Extending to Other Skills" section with:
1. Define required steps
2. Create logging script
3. Add logging to skill
4. Create verification hook
5. Configure hook

**Why it's unique**: Makes the compliance pattern reusable.

**Consideration**: Skill-forge should use this exact pattern for skills with enforcement requirements.

---

## Recommendations for Skill-Forge

### Core Features to Include

1. **Compliance Enforcement Generator**
   - Generate `log_compliance.sh` script from step list
   - Generate `verify_*_compliance.sh` hook from required markers
   - Generate hook configuration JSON for `.claude/settings.local.json`

2. **Safety Policy Template**
   - Required section at top of SKILL.md
   - Categories: Never, Always, Requires Confirmation
   - Anti-pattern examples with "WRONG:" prefix

3. **Communication Rules Block**
   - Standard "narrate before executing" instructions
   - Decision point template: "Present options and wait for explicit direction"
   - Progress communication template

4. **Script Generation Standards**
   - `set -euo pipefail` at top
   - Colored output with emoji toggle
   - Help flag (`-h`, `--help`)
   - Consistent argument parsing
   - Temp file naming convention: `/tmp/${skill_name}_${context}_*.txt`

5. **Error Handling Templates**
   - Read full error
   - Investigate cause
   - Explain in plain language
   - Propose fix with approval

### Architecture Patterns

1. **Phase-based workflows**: Generate phase markers and phase-complete tracking

2. **Script vs LLM balance**:
   - Scripts for: data gathering, file manipulation, deterministic checks
   - LLM for: judgment, analysis, communication, decision making

3. **Cross-skill references**: Support `Skill(other-skill)` invocation pattern

4. **Reference documents**: Generate `references/` directory for educational content separate from operational instructions

### Integration Points

1. **Hook system integration**: Generate hook configurations as part of skill installation

2. **Temp file cleanup**: Generate cleanup instructions or scripts

3. **Progress visualization**: Consider generating progress display for multi-step skills

### What NOT to Do

1. **Don't over-engineer simple skills**: Git worktrees skill shows that CRUD utilities don't need compliance enforcement - just safety rules.

2. **Don't assume interactivity**: All scripts must handle non-interactive mode.

3. **Don't hard-code paths**: Use repo root discovery pattern.

4. **Don't mix parsing approaches**: Pick one JSON parser (jq recommended).

---

## Appendix: Line-by-Line Notable Sections

### PR Review SKILL.md

| Lines | Section | Notable Content |
|-------|---------|-----------------|
| 12-67 | Compliance System | Complete compliance architecture documentation |
| 79-137 | Communication Principles | "NEVER draft a review without discussing findings first" |
| 150-203 | GitHub CLI Version | Detailed upgrade instructions |
| 309-355 | Understanding Staleness | 47-line educational section with examples |
| 381-425 | Scope Creep Handling | Taxonomy of acceptable vs questionable additions |
| 897-919 | AI Attribution Prohibition | Comprehensive list of forbidden patterns |

### Git Worktrees SKILL.md

| Lines | Section | Notable Content |
|-------|---------|-----------------|
| 8-33 | Safety Policy | Immutable constraints ("NEVER delete branches") |
| 36-57 | Narrate Everything | What/Why/Effect/Risks framework |
| 61-84 | Error Handling | Anti-pattern: "Let me try again with --force" |
| 340-358 | Shared Git History | Explains worktree architecture |

### Hooks README.md

| Lines | Section | Notable Content |
|-------|---------|-----------------|
| 5-20 | The Problem | "The model can ignore checklists just as easily as original instructions" |
| 22-48 | Architecture | ASCII diagram of compliance flow |
| 121-199 | Extending to Other Skills | 5-step extension guide |
| 232-239 | Exit Codes | Reference table |
