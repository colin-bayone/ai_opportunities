# Phase 3 Session 1: django-forge Skill Deep Dive

**Research Date:** 2026-02-11
**Research Focus:** Exhaustive analysis of django-forge skill architecture, 14-agent swarm, scripts, and reference organization
**Files Analyzed:** 1 SKILL.md, 14 agents, 4 scripts, 2 reference files, + Phase 2 research for comparison

---

## Executive Summary

1. **django-forge is the most sophisticated skill in the codebase** - A 14-agent implementation swarm with 8 workflow phases, state persistence, and comprehensive quality gates. At ~950 lines, the SKILL.md approaches the recommended limit but uses progressive disclosure effectively.

2. **The swarm follows a "Blackboard Pattern"** where agents communicate through shared markdown/JSON files in `.django-workflow/issue-{n}/`, enabling resumption, auditability, and parallel execution without complex message passing.

3. **Smart complexity-based routing** selects the appropriate planning approach: HIGH complexity → separate Architect + Engineer agents; MEDIUM/LOW → combined Planner agent.

4. **Strong alignment with Phase 2 best practices** including progressive disclosure, subagent isolation, script-based deterministic operations, and WHEN + WHEN NOT description patterns.

5. **Four key patterns to adopt for skill-forge**: (1) Wave-based parallel execution with dependency tracking, (2) Judge/Quality gate pattern for output validation, (3) State persistence via JSON for resumption, (4) Explorer parallelization for context gathering.

6. **Gaps identified**: Missing `context: fork` and `model` frontmatter fields that official docs recommend; some agents exceed recommended complexity (foreman.md at 340+ lines could benefit from splitting).

---

## SKILL.md Architecture Analysis

### Structure Overview

The SKILL.md (~950 lines) is well-organized with clear sections:

```
├── Frontmatter (name, description only)
├── Table of Contents (for navigation)
├── What Is django-forge? (overview)
├── 8 Workflow Phases (detailed process)
├── Agent Catalog (summary of all 14)
├── Orchestration Protocol (coordination)
├── Resource Catalog (scripts, references)
├── Examples
└── Hard Rules
```

### Frontmatter Analysis

**Current:**
```yaml
---
name: django-forge
description: |
  Multi-agent skill for end-to-end GitHub issue implementation...
---
```

**Alignment with Best Practices:**
| Field | Present | Best Practice | Assessment |
|-------|---------|---------------|------------|
| `name` | Yes | Required, lowercase + hyphens | Compliant |
| `description` | Yes | WHEN + WHEN NOT pattern | Partial - has triggers but no exclusions |
| `model` | No | Recommended for Opus-requiring skills | Missing |
| `context: fork` | No | Optional but useful for isolation | Missing |
| `allowed-tools` | No | Pre-approve common tools | Missing |

**Recommendation:** Add:
```yaml
model: opus
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(git:*)
```

### Progressive Disclosure Implementation

The skill implements progressive disclosure effectively:

**Tier 1 (Always loaded):** ~100 token frontmatter
**Tier 2 (On skill invocation):** ~950 line SKILL.md - at the upper limit (500 lines recommended)
**Tier 3 (On-demand):**
- `references/design_decisions.md` (336 lines)
- `references/django_best_practices.md` (184 lines)
- Scripts (zero context cost until executed)

**Assessment:** Good overall but SKILL.md could be pruned. The "Hard Rules" section (68 lines) could move to a reference file since it's enforcement knowledge not orchestration flow.

### 8-Phase Workflow Architecture

| Phase | Name | Agents Involved | Description |
|-------|------|-----------------|-------------|
| 1 | Setup | git-operations-handler | Create session folder, init state |
| 2 | Documentation | docs-explorer, research-agent | Gather references, check library freshness |
| 3 | Exploration | model/view/template/codebase-explorer | Parallel codebase analysis |
| 4 | Planning | Architect+Engineer OR Planner | Task decomposition based on complexity |
| 5 | Approval | traffic-controller | User reviews plan |
| 6 | Implementation | Foreman → code-worker(s) + test-worker(s) → Judge | Wave-based execution |
| 7 | Testing | playwright-tester | E2E verification |
| 8 | Git | git-operations-handler, traffic-controller | Commit, PR creation |

**Strengths:**
- Clear phase boundaries with explicit completion criteria
- Complexity-aware routing (HIGH vs MEDIUM/LOW)
- Quality gates at multiple points (Phase 5 approval, Phase 6 Judge)
- Resumption support through state persistence

**Potential Issues:**
- 8 phases may be overkill for simple issues - consider "fast path" for LOW complexity
- No explicit timeout handling documented (guardrails mentioned in design_decisions.md but not SKILL.md)

---

## Agent Swarm Analysis (14 Agents)

### Agent Inventory

| Agent | Lines | Model | Async | Primary Tools | Role |
|-------|-------|-------|-------|---------------|------|
| architect | 193 | Opus | No | Read, Grep, Glob | Strategic task decomposition |
| code-worker | 234 | Opus | Yes | Read, Edit, Write, Grep, Glob, Bash | Implementation |
| codebase-explorer | 215 | Opus | Yes | Read, Glob, Grep | Cross-cutting pattern discovery |
| engineer | 178 | Opus | No | Read, Grep, Glob | Technical design after Architect |
| foreman | 343 | Opus | No | Read, Write, Task | Worker coordination |
| judge | 274 | Opus | No | Read, Glob, Grep, Bash | Quality evaluation |
| model-explorer | 236 | Opus | Yes | Read, Glob, Grep | Django model analysis |
| planner | 165 | Opus | No | Read, Grep, Glob | Combined Architect+Engineer for MEDIUM/LOW |
| playwright-tester | 235 | Opus | Yes | Read, Write, Bash, Glob | E2E testing |
| research-agent | 187 | Opus | Yes | WebSearch, WebFetch, Bash | Time-aware documentation research |
| template-explorer | 256 | Opus | Yes | Read, Glob, Grep | Django template/HTMX analysis |
| test-worker | 198 | Sonnet | Yes | Read, Edit, Write, Grep, Glob, Bash | Test creation |
| traffic-controller | 216 | Opus | No | Read, Grep, Glob | Workflow compliance enforcement |
| view-explorer | 364 | Opus | Yes | Read, Glob, Grep | View/service/URL analysis |

**Total Lines:** ~3,094 across 14 agents

### Agent Architecture Patterns

#### Pattern 1: Parallel Explorers
```
Phase 3 spawns explorers in parallel:
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ model-      │  │ view-       │  │ template-   │  │ codebase-   │
│ explorer    │  │ explorer    │  │ explorer    │  │ explorer    │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
       │                │                │                │
       └────────────────┴────────────────┴────────────────┘
                                │
                        Orchestrator collects
```

**Key Insight:** All explorers are Async=Yes and read-only. They write findings to `{session_path}/exploration/` as markdown files. This is textbook subagent usage per Phase 2 research.

#### Pattern 2: Complexity-Based Planning Fork
```
                    ┌─────────────────┐
                    │ Assess          │
                    │ Complexity      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
          HIGH           MEDIUM           LOW
              │              │              │
              ▼              └──────┬───────┘
     ┌────────────┐                 │
     │ Architect  │                 ▼
     └─────┬──────┘         ┌────────────┐
           │                │ Planner    │
           ▼                │ (combined) │
     ┌────────────┐         └────────────┘
     │ Engineer   │
     └────────────┘
```

**Assessment:** Smart optimization. HIGH complexity gets thoroughness (two-pass); MEDIUM/LOW gets efficiency (single combined agent).

#### Pattern 3: Wave-Based Implementation (Foreman Pattern)
```
Foreman receives task list with dependencies:
Task 1: No deps → Wave 1
Task 2: No deps → Wave 1
Task 3: Depends on 1 → Wave 2
Task 4: Depends on 1,2 → Wave 2
Task 5: Depends on 3,4 → Wave 3

Wave 1 (parallel):
├── code-worker → Task 1 → Judge
└── code-worker → Task 2 → Judge

Wave 2 (after Wave 1 complete):
├── code-worker → Task 3 → Judge
└── code-worker → Task 4 → Judge

Wave 3 (after Wave 2 complete):
└── code-worker → Task 5 → Judge
```

**foreman.md Analysis (343 lines - largest agent):**

Key sections:
1. Task State Management (pending/in_progress/complete/approved/rejected/blocked)
2. Worker Pool Management (max 5 concurrent, avoid contention)
3. Judge Integration (APPROVED/REWORK/BLOCKED verdicts)
4. Rework Loop (max 3 iterations per task)
5. Completion Aggregation

**Concern:** At 343 lines, foreman.md is complex. Consider splitting coordination logic from state management.

#### Pattern 4: Judge Quality Gate
```
For each completed task:
┌──────────────┐
│ code-worker  │ completes task
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ Judge evaluates:                                          │
│  1. Functional correctness                                │
│  2. Pattern compliance (models before queries, HTMX)      │
│  3. Test coverage                                         │
│  4. Code quality (N+1 queries, DRY)                       │
│  5. Security                                              │
│  6. Scope adherence                                       │
└──────────────────────────┬───────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    APPROVED          REWORK            BLOCKED
         │                 │                 │
    Continue         Return to         Escalate to
    to next          code-worker       user
    wave             (max 3x)
```

**Key Judge Features:**
- Severity levels: CRITICAL (must fix), MAJOR (should fix), MINOR (nice to fix)
- Detailed rework instructions on rejection
- Fresh eyes evaluation (independent of worker context)
- Token budget awareness (fails if worker used >100k tokens)

### Agent Prompt Template Analysis

All agents follow a consistent template structure:
```markdown
You are the [ROLE NAME] agent for django-forge.

Session folder: {session_path}
Issue number: {issue_number}
Issue title: {issue_title}

## Your Role
[Purpose statement]

## Context
### Issue Requirements
{issue_body}

### Previous Work
{findings from earlier phases}

## Your Task
[Specific instructions]

## Output Format
[Expected output structure with example]

## Hard Rules
[Non-negotiable constraints]
```

**Assessment:** Excellent consistency. Template variables (`{session_path}`, etc.) enable dynamic context injection.

### Agent Model Selection Analysis

| Model | Agents | Use Case |
|-------|--------|----------|
| Opus | 13/14 | Complex reasoning, code generation, evaluation |
| Sonnet | 1/14 (test-worker) | Sufficient for test generation |

**Comparison to design_decisions.md intent:**
> "Opus for code, Sonnet for rest"

**Assessment:** Partial implementation. design_decisions.md suggested Sonnet for test workers, which is implemented. However, Judge and explorers could potentially use Sonnet for cost savings - explorers do read-only analysis, and Judge does evaluation not generation.

---

## Script Integration Analysis

### Script Inventory

| Script | Lines | Purpose | Execution Context |
|--------|-------|---------|-------------------|
| check_library_freshness.py | 240 | Validate 3rd-party library currency | Phase 2 (research-agent) |
| get_current_date.py | 77 | Time-aware context for web searches | Phase 2 (research-agent) |
| playwright_template.py | 247 | Reference Playwright patterns | Phase 7 (playwright-tester) |
| state_manager.py | 328 | Session state CRUD operations | All phases |

### check_library_freshness.py Analysis

**Purpose:** Enforce library freshness requirements:
1. Must have been updated within 1 year
2. Must be version >= 1.0.0 (production-ready)
3. Must have active maintenance

**Implementation:**
- Uses `gh api` to check GitHub releases and commits
- Parses version strings for semver comparison
- Returns APPROVED/REJECTED with rationale

**Best Practice Alignment:**
- Script provides deterministic validation (LOW degrees of freedom - appropriate for fragile operations)
- Output is structured JSON (easy for LLM to parse)
- No dependencies beyond Python stdlib + gh CLI

**Example Usage:**
```bash
python check_library_freshness.py django-htmx --github adamchainz/django-htmx
```

### get_current_date.py Analysis

**Purpose:** Provide time-aware context for web searches and library checks

**Why This Exists:** Per design_decisions.md:
> "User noted Claude often returns outdated content. Web searches should be time-aware."

**Implementation:**
```python
context = {
    "current_date": now.strftime("%Y-%m-%d"),
    "current_year": now.year,
    "one_year_ago": one_year_ago.strftime("%Y-%m-%d"),
    "search_context": f"in {now.year}",
}
```

**Assessment:** Simple, focused script. research-agent uses this to append current year to search queries.

### playwright_template.py Analysis

**Purpose:** Reference implementation for Playwright testing patterns

**Key Patterns Documented:**
1. **Direct URL auth** (NOT clicking login buttons)
2. **Cookie verification** after auth
3. **JavaScript click** for hidden elements
4. **State-based waits** (NOT arbitrary timeouts)

**Critical Code Pattern:**
```python
# CORRECT: Navigate directly to auth endpoint
await page.goto(f"{BASE_URL}/accounts/dev/auto-login/?email={email}")

# WRONG: Clicking login buttons
# page.locator('text=Sign In').click()  # DON'T DO THIS
```

**Assessment:** Excellent use of scripts for encoding project-specific patterns. This prevents playwright-tester from guessing at auth patterns.

### state_manager.py Analysis

**Purpose:** CRUD operations for session state persistence

**State Structure:**
```json
{
  "session_id": "uuid",
  "issue_number": 123,
  "issue_title": "Feature X",
  "complexity": "MEDIUM",
  "current_phase": "implementation",
  "completed_phases": ["setup", "documentation", "exploration", "planning", "approval"],
  "phase_data": { ... },
  "user_decisions": [ ... ],
  "conflicts_resolved": [ ... ],
  "tasks": [ ... ],
  "implementation_stats": {
    "total_tasks": 5,
    "tasks_approved": 3,
    "tasks_reworked": 1,
    "total_rework_count": 2
  }
}
```

**CLI Operations:**
- `init` - Create new session
- `load` - Read session state
- `advance` - Move to next phase
- `status` - Get current state summary
- `list` - Show all existing sessions

**Assessment:** This is the "Blackboard" implementation - central state that all agents read/write via file operations rather than message passing.

### Script Best Practice Alignment

| Best Practice (Phase 2) | Implementation | Assessment |
|------------------------|----------------|------------|
| Self-contained (stdlib only) | Yes - no pip dependencies | Excellent |
| Clear input/output | Yes - CLI args, JSON output | Excellent |
| Cross-platform paths | Yes - forward slashes | Excellent |
| Script code never enters context | Yes - only output consumed | Excellent |
| Plan-Validate-Execute pattern | Partial - no explicit validation script | Could add |

---

## Reference File Organization

### Reference Inventory

| File | Lines | Purpose |
|------|-------|---------|
| design_decisions.md | 336 | Skill creation rationale, user decisions captured |
| django_best_practices.md | 184 | Django-specific checklist for Judge evaluation |

### design_decisions.md Analysis

**Purpose:** Captures the "why" behind skill design choices. Valuable for:
- Future maintainers understanding rationale
- Users understanding expected behavior
- Debug sessions when behavior seems wrong

**Key Sections:**
1. Origin and research sources
2. 22 numbered design decisions with rationale
3. Integration points with other skills
4. Implementation status (created/to-create)

**Assessment:** Excellent documentation practice. However, this is meta-documentation about the skill itself, not runtime reference content. Consider whether this belongs in references/ or a separate `docs/` directory.

### django_best_practices.md Analysis

**Purpose:** Checklist for Judge agent to evaluate code quality

**Coverage:**
- Models (field definitions, methods, Meta options)
- Views (CBV/FBV patterns, query optimization)
- Forms
- URLs
- Templates
- Security
- Testing
- Migrations
- Performance
- Code organization
- Anti-patterns

**Assessment:** Good checklist format. Judge agent can systematically verify each category.

### Reference Organization Best Practices Alignment

| Best Practice (Phase 2) | Implementation | Assessment |
|------------------------|----------------|------------|
| One level deep from SKILL.md | Yes | Compliant |
| Domain-organized | Partial - only 2 files | Adequate for scope |
| Table of contents for >100 lines | No | Should add |
| Clear loading signals in SKILL.md | Yes | Good |

---

## Comparison to Phase 2 Best Practices

### SKILL.md Structure

| Best Practice | django-forge | Assessment |
|--------------|--------------|------------|
| Keep under 500 lines | 950 lines | Exceeds - consider splitting |
| Required name/description | Present | Compliant |
| WHEN + WHEN NOT description | Partial WHEN | Should add WHEN NOT |
| Use {baseDir} placeholder | Uses {session_path} etc | Appropriate adaptation |
| Table of contents | Present | Excellent |
| Imperative language | Yes | Compliant |

### Agent Configuration

| Best Practice | django-forge | Assessment |
|--------------|--------------|------------|
| Name: lowercase + hyphens | Yes | Compliant |
| Description: meaningful | Yes | Good auto-delegation triggers |
| Tools: restricted appropriately | Mostly | Explorers correctly limited to read-only |
| Model: specified | In prompt, not frontmatter | Should formalize |
| permissionMode | Not specified | Could add for workers |

### Script Integration

| Best Practice | django-forge | Assessment |
|--------------|--------------|------------|
| Deterministic operations use scripts | Yes | Excellent (date, freshness) |
| Scripts don't enter context | Yes | Proper execution model |
| Plan-Validate-Execute | Partial | Could strengthen |
| JSON output for structure | Yes | Easy parsing |

### Progressive Disclosure

| Best Practice | django-forge | Assessment |
|--------------|--------------|------------|
| 3-tier loading | Implemented | Good |
| References one level deep | Yes | Compliant |
| Conditional loading signals | Yes | Clear directives |
| Long refs have TOC | No | Should add |

### Context Management

| Best Practice | django-forge | Assessment |
|--------------|--------------|------------|
| Subagent isolation for research | Yes (explorers) | Excellent |
| Shared memory via files | Yes (blackboard) | Excellent |
| Minimize main context pollution | Yes | Findings stay in files |

---

## Key Patterns to Adopt for skill-forge

### Pattern 1: Blackboard Communication

**What:** Agents communicate through shared files rather than message passing

**Why:**
- Debuggable (can inspect files)
- Resumable (state persists)
- No complex coordination infrastructure
- Agents remain stateless

**Implementation:**
```
.django-workflow/issue-{n}/
├── orchestration/
│   └── state.json          # Central state
├── exploration/
│   ├── model_findings.md   # From model-explorer
│   ├── view_findings.md    # From view-explorer
│   └── template_findings.md # From template-explorer
├── implementation/
│   └── completed-work/     # Worker outputs
└── testing/
    └── test_results.md     # Playwright output
```

### Pattern 2: Complexity-Based Routing

**What:** Different agent combinations based on task complexity

**Why:**
- HIGH complexity needs thoroughness
- LOW complexity needs speed
- One-size-fits-all wastes resources or misses quality

**Implementation:**
```python
if complexity == "HIGH":
    spawn(architect)
    spawn(engineer)  # After architect completes
else:
    spawn(planner)   # Combined agent
```

### Pattern 3: Wave-Based Parallel Execution

**What:** Execute independent tasks in parallel, respecting dependencies

**Why:**
- Maximizes throughput
- Respects task ordering
- Up to 10 concurrent agents (Claude Code limit)

**Implementation:**
```
Wave 1: [Task A, Task B] - parallel, no deps
         ↓
Wave 2: [Task C, Task D] - parallel, depend on Wave 1
         ↓
Wave 3: [Task E] - depends on Wave 2
```

### Pattern 4: Judge Quality Gate

**What:** Independent evaluation agent reviews all outputs

**Why:**
- Fresh eyes catch issues worker missed
- Consistent quality standards
- Prevents poor code from accumulating
- Detailed rework instructions

**Verdicts:**
- APPROVED → Continue
- REWORK → Return to worker (max 3x)
- BLOCKED → Escalate to user

### Pattern 5: Explorer Parallelization

**What:** Launch multiple read-only explorers simultaneously

**Why:**
- Exploration is embarrassingly parallel
- Each explorer has isolated context
- Findings merge via files
- 2-3x faster than sequential

**Example:**
```javascript
// Launch all in single message (parallel execution)
Task({ subagent_type: "model-explorer", ... })
Task({ subagent_type: "view-explorer", ... })
Task({ subagent_type: "template-explorer", ... })
```

### Pattern 6: State Persistence for Resumption

**What:** JSON state file tracks workflow progress

**Why:**
- Sessions can resume after interruption
- User can see progress at any time
- Enables "continue from where we left off"

**State Fields:**
```json
{
  "current_phase": "implementation",
  "completed_phases": ["setup", "docs", "exploration", "planning"],
  "tasks": [...],
  "user_decisions": [...]
}
```

---

## Gaps and Recommendations

### Missing Elements

1. **Frontmatter Fields:**
   - Add `model: opus` (skill requires Opus)
   - Add `allowed-tools` for common operations
   - Consider `context: fork` for isolation

2. **SKILL.md Length:**
   - At 950 lines, exceeds 500-line recommendation
   - Move "Hard Rules" section to reference file
   - Move detailed output format examples to references

3. **Table of Contents in References:**
   - django_best_practices.md (184 lines) needs TOC
   - design_decisions.md (336 lines) needs TOC

4. **Description WHEN NOT Pattern:**
   ```yaml
   description: |
     Multi-agent skill for end-to-end GitHub issue implementation.
     Use when user provides a GitHub issue number or asks to implement
     a Django feature/bugfix. Do NOT use for documentation tasks,
     code review without implementation, or non-Django projects.
   ```

5. **Fast Path for LOW Complexity:**
   - Current workflow has 8 phases for all issues
   - LOW complexity could skip exploration and use minimal planning

6. **Timeout/Budget Enforcement:**
   - design_decisions.md mentions 100k token budget per task
   - Not enforced in agent prompts
   - Consider adding explicit budget instructions

### Potential Improvements

1. **Model Cost Optimization:**
   - Explorers could use Sonnet (read-only analysis)
   - traffic-controller could use Haiku (simple checks)
   - Judge evaluation might work with Sonnet

2. **foreman.md Complexity:**
   - At 343 lines, largest agent file
   - Consider splitting: `foreman-coordinator.md` + `foreman-state.md`

3. **Validation Script:**
   - Add `validate_plan.py` for pre-approval checks
   - Currently user approval is only gate before implementation

4. **Hook Integration:**
   - Could add PreToolUse hook for Edit operations
   - Run lint/format automatically

---

## Conclusion

django-forge represents a mature, well-architected multi-agent skill that demonstrates best practices for:

1. **Agent Coordination:** Blackboard pattern with file-based communication
2. **Quality Control:** Judge pattern for independent evaluation
3. **Efficiency:** Parallel explorers, wave-based implementation
4. **Flexibility:** Complexity-based routing
5. **Persistence:** State management for resumption

For skill-forge, the key takeaways are:

1. **Structure matters:** The 8-phase workflow provides clear boundaries
2. **Separation of concerns:** Each agent has one job
3. **Files over messages:** Blackboard pattern simplifies coordination
4. **Quality gates:** Judge pattern prevents accumulation of issues
5. **Pragmatic model selection:** Opus for code, Sonnet where sufficient

The skill demonstrates that complex multi-agent workflows can be implemented within Claude Code's skill framework, using the Task tool for subagent spawning and markdown files for inter-agent communication.

---

## Files Analyzed

### SKILL.md
- `/home/cmoore/programming/cisco_projects/cicd/.claude/skills/django-forge/SKILL.md`

### Agents (14)
- `agents/architect.md` (193 lines)
- `agents/code-worker.md` (234 lines)
- `agents/codebase-explorer.md` (215 lines)
- `agents/engineer.md` (178 lines)
- `agents/foreman.md` (343 lines)
- `agents/judge.md` (274 lines)
- `agents/model-explorer.md` (236 lines)
- `agents/planner.md` (165 lines)
- `agents/playwright-tester.md` (235 lines)
- `agents/research-agent.md` (187 lines)
- `agents/template-explorer.md` (256 lines)
- `agents/test-worker.md` (198 lines)
- `agents/traffic-controller.md` (216 lines)
- `agents/view-explorer.md` (364 lines)

### Scripts (4)
- `scripts/check_library_freshness.py` (240 lines)
- `scripts/get_current_date.py` (77 lines)
- `scripts/playwright_template.py` (247 lines)
- `scripts/state_manager.py` (328 lines)

### References (2)
- `references/design_decisions.md` (336 lines)
- `references/django_best_practices.md` (184 lines)

### Phase 2 Research (for comparison)
- `phase2_session1_skill_structure.md`
- `phase2_session2_agents_subagents.md`
- `phase2_session4_scripts_context.md`
