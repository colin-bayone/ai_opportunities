# Django Forge Skill - Design Decisions

This document captures the design decisions made during skill creation for reference and future modifications.

## Origin

Created on January 2, 2026 after extensive research into:
- Existing skills (meeting-git-issue-extractor, phoenix-theme-skill, github-issue-creator)
- Multi-agent coordination patterns (blackboard, Agent-as-a-Judge)
- Claude Code Task tool and subagent capabilities
- User preferences for implementation workflow

## Key Design Decisions

### 1. Multi-Agent Implementation Swarm

**Decision:** Use a 4-role swarm architecture (Architect, Engineer, Foreman, Judge) instead of a single implementation agent.

**Rationale:**
- Implementation is the heaviest phase - shouldn't be a single bottleneck
- Separation of concerns: planning vs design vs execution vs evaluation
- Quality gates via Judge prevent poor code from accumulating
- Parallel execution via Foreman maximizes throughput
- User requested this pattern explicitly

### 2. Hybrid Planning (Architect + Engineer vs Planner)

**Decision:** Use separate Architect + Engineer for HIGH complexity issues, combined Planner for MEDIUM/LOW.

| Complexity | Approach | Rationale |
|------------|----------|-----------|
| HIGH | Separate | Maximum thoroughness for complex work |
| MEDIUM | Combined | Good balance of quality and efficiency |
| LOW | Combined | Don't over-engineer simple fixes |

**User confirmed:** Hybrid approach selected per user feedback.

### 3. Model Selection

| Agent | Model | Rationale |
|-------|-------|-----------|
| All Explorers | Opus | Complex reasoning for codebase understanding |
| Architect | Opus | Strategic decomposition requires depth |
| Engineer | Opus | Technical design needs sophistication |
| Planner | Opus | Combined role needs full capability |
| Foreman | Opus | Coordination complexity |
| Code Workers | Opus | Best code quality (user request) |
| Test Workers | Sonnet | Good balance for tests |
| Judge | Opus | Nuanced evaluation with detailed feedback |
| Git Handler | Haiku | Simple operations |

**User confirmed:** Opus for code, Sonnet for rest.

### 4. Worker Communication (Blackboard Pattern)

**Decision:** Agents communicate via markdown/JSON files in `.django-workflow/issue-{number}/`.

**Rationale:**
- File-based communication is debuggable and auditable
- User can inspect any file at any time
- Supports resumption (files persist)
- No complex message passing infrastructure needed
- Research shows 13-57% performance improvement over coordinator-only patterns

### 5. User Escalations

**Decision:** ALL blocked tasks escalate to user (never auto-skip).

**Rationale:**
- User explicitly requested maximum control
- Stuck tasks need human judgment
- Prevents silent failures
- Maintains transparency

### 6. Loop Prevention Guardrails

**Decision:** Multiple guardrails to prevent infinite rework loops:
1. Max 3 rework iterations per task
2. Repetitive output detection (>90% similar = blocked)
3. Token budget: 100k per task
4. Time budget: 30 min per task (conceptual)

**Rationale:**
- Research identified infinite loops as major risk
- External enforcement is more reliable than self-governance
- Multiple guardrails provide defense in depth

### 7. Models Before Queries (Hard Rule)

**Decision:** model-explorer MUST complete before any code worker writes query code.

**Rationale:**
- User explicitly stated this requirement
- N+1 queries are common Django mistake
- Understanding models prevents incorrect relationships
- Proper select_related/prefetch_related requires model knowledge

### 8. HTMX Over JavaScript (Hard Rule)

**Decision:** Always prefer HTMX patterns over JavaScript.

**Rationale:**
- User explicitly stated this requirement
- Project uses HTMX throughout
- Simpler, more maintainable
- OOB swaps handle complex updates
- WebSockets via Channels for real-time

### 9. Library Freshness Requirements

**Decision:** Third-party libraries must:
- Be updated within 1 year of current date
- Have version >= 1.0.0

**Rationale:**
- User explicitly stated this requirement
- Unmaintained libraries are risky
- Pre-1.0 libraries aren't production-ready
- Scripts provided for validation

### 10. Current Date Context for Research

**Decision:** Always get current date before web searches, include year in search terms.

**Rationale:**
- User noted Claude often returns outdated content
- Web searches should be time-aware
- Scripts provided: `get_current_date.py`

### 11. Smart Explorer Selection

**Decision:** Skill decides which explorers to run based on issue type.

| Issue Type | Explorers |
|------------|-----------|
| Database/Models | model (required), view, test |
| Backend only | model (required), view, test |
| UI/Templates | model, view, template, test |
| Full-stack | ALL |

**User confirmed:** Skill decides based on issue type.

### 12. Question Limits

**Decision:** Max 3 questions per message to user.

**Rationale:**
- From meeting-git-issue-extractor pattern
- User explicitly appreciates this limit
- Prevents overwhelming users
- Forces prioritization

### 13. Wave-Based Parallel Execution

**Decision:** Tasks execute in waves based on dependencies.

```
Wave 1: Tasks with no dependencies (parallel)
Wave 2: Tasks depending on Wave 1 only (parallel)
Wave N: Integration tasks
```

**Rationale:**
- Maximizes parallelism where possible
- Respects dependencies
- Clear execution model
- Up to 10 concurrent workers per wave (Claude Code limit)

### 14. Judge Evaluation Criteria

**Decision:** Judge evaluates on:
1. Functional correctness
2. Pattern compliance
3. Test coverage
4. Code quality (N+1 queries, etc.)
5. Security
6. Scope adherence

**Severity levels:**
- CRITICAL: Must fix (security, broken functionality)
- MAJOR: Should fix (patterns, quality)
- MINOR: Nice to fix (style)

**Rationale:**
- Comprehensive quality gates
- Clear severity levels guide rework priority
- Matches github-issue-creator-skill patterns

## Integration Points

### With Existing Skills

| Skill | Integration |
|-------|-------------|
| meeting-git-issue-extractor | Session folder patterns, state management, user interaction |
| phoenix-theme-skill | UI component catalog, Playwright testing |
| github-issue-creator-skill | Best practices references, issue templates |

### With Existing Agents

| Agent | Reused |
|-------|--------|
| docs-explorer | Used for Phase 2 |
| git-operations-handler | Used for Phase 8 |
| django-implementation-planner | Pattern reference |

## Additional Decisions (User Feedback Session)

### 15. Reference Materials Strategy

**Decision:** Copy all best practices from github-issue-creator-skill/references/ AND use web search.

**Rationale:**
- Comprehensive reference docs already exist
- Web search validates/updates with modern practices
- Both approaches together ensure quality

### 16. Traffic Controller Agent

**Decision:** Create dedicated traffic-controller agent for workflow compliance.

**Rationale:**
- Ensures proper role following
- No Claude attribution in git
- Draft PRs created properly
- Separates workflow concerns from code quality (Judge)

### 17. Session Start Protocol

**Decision:** ALWAYS ask user for context before starting.

**Hard rules:**
1. Ask if user has anything to share first
2. Offer folder creation options
3. Offer git worktree option
4. Wait for user context

### 18. User Override Capability

**Decision:** All major decisions shown to user with override option.

**Rationale:**
- User said "Transparency is key"
- User should control their workflow
- Architect/Engineer choice can be overridden
- Explorer selection can be overridden

### 19. Sequential Presentation

**Decision:** Present complex information sequentially, not all at once.

**Rationale:**
- User said "don't overwhelm them"
- Phase by phase presentation
- Wait for acknowledgment
- Better user experience

### 20. Enhanced Quality Gates

**Decision:** Comprehensive quality checks before presenting to user:

| Check | Description |
|-------|-------------|
| SOC2 | Security compliance |
| Idempotency | Operations can be repeated safely |
| DRY | No code duplication |
| No truncation | Complete implementations only |
| No hacky workarounds | Proper solutions only |
| Tests pass | All tests must pass |
| No Claude attribution | Never in git |

### 21. Skill Integrations

**Decision:** Integrate with:
- github-issue-creator-skill (for generating new issues)
- git-worktrees-skill (for isolated development)

**Rationale:**
- Scope creep items become new issues
- Worktrees keep main branch clean

### 22. Research Agent

**Decision:** Create research-agent that uses web search with current date context.

**Rationale:**
- Validates reference docs against modern practices
- Uses get_current_date.py for time-aware searches
- Combines static docs + live research

## Future Considerations

1. **Parallel branches:** Could multiple issues be worked simultaneously?
2. **Learning from Judge feedback:** Could common issues be prevented?
3. **Metrics dashboard:** Track rework rates, common failures
4. **Integration tests:** End-to-end skill testing

## Session That Created This Skill

Research and design performed on 2026-01-02.

Files created in: `claude/2026-01-02_django-forge/`
- `research/00_research_findings.md`
- `research/01_library_requirements.md`
- `research/02_skill_architecture.md`
- `research/03_implementation_swarm_architecture.md`
- `research/04_additional_requirements.md` - User feedback (TO IMPLEMENT)

## Implementation Status

### Created
- SKILL.md (needs update with new requirements)
- agents/architect.md
- agents/engineer.md
- agents/planner.md
- agents/foreman.md
- agents/code-worker.md
- agents/test-worker.md
- agents/judge.md (needs enhancement)
- agents/model-explorer.md
- scripts/get_current_date.py
- scripts/check_library_freshness.py
- scripts/state_manager.py

### To Create
- agents/view-explorer.md
- agents/template-explorer.md
- agents/codebase-explorer.md
- agents/research-agent.md
- agents/traffic-controller.md
- references/ (copy from github-issue-creator-skill)

### To Update
- SKILL.md - Add all new requirements
- agents/judge.md - Add comprehensive quality gates
