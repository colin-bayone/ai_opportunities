# Skill-Forge Version Tracking

## Current Version

| Field | Value |
|-------|-------|
| **Last Updated** | 2026-03-28 |
| **Last Researcher** | skill-forge-updater (parallel research agents) |
| **Claude Code Version** | v2.1.86 (Mar 27, 2026) |
| **Features Covered Through** | March 2026 |
| **Staleness Threshold (days)** | 30 |

## Update History

### 2026-03-28 — Research Update (Automated)
- **Scope**: Full research covering v2.1.0 (Jan 7) through v2.1.86 (Mar 27)
- **References Created**: `2026-03-28_new_features_update.md` covering all new features
- **Key New Features**: Hook system grew 14→26+ events, HTTP hooks, conditional `if` field, skill description cap 250 chars, `effort`/`initialPrompt`/`paths:` frontmatter, worktree isolation, named agents with SendMessage, `auto` permission mode, `/batch` command, plugin system matured, remote/cloud execution, 1M context Opus 4.6, Sonnet 4.6
- **Research Method**: 4 parallel research agents (core features, agents, skills/hooks, infrastructure)

### 2026-02-11 — Initial Creation
- **Scope**: Full research across 4 phases
- **References Created**: 8 files covering skill structure, agents/subagents, hooks, scripts/context, and local patterns
- **Key Features Documented**: Agent Teams, Async Subagents, MCP Tool Search, Skills Hot Reload, Enhanced Hooks, Opus 4.6 (200K context), Fast Mode
- **Models Documented**: Opus 4.6, Sonnet 4, Haiku 4.5

## Known Gaps (Auto-Detected or Manually Noted)

_Updated by the skill-forge-updater agent or manually. Each entry notes the date detected and resolution status._

### Open Gaps

- **2026-03-28**: SKILL.md workflow sections not yet updated for new frontmatter fields (effort, initialPrompt, paths)
- **2026-03-28**: Existing references (2026-02-11_*) contain some outdated info (e.g., 1024 char description limit, 200K context) — not yet corrected inline
- **2026-03-28**: Plugin distribution workflow not yet documented in skill-forge (user sharing across projects)

### Addressed Gaps (Historical Record)

_These gaps were detected during the 2026-03-28 staleness analysis and are now covered in `references/2026-03-28_new_features_update.md`._

- **2026-03-28** (ADDRESSED): Agent tool replaced Task tool as primary spawning mechanism
- **2026-03-28** (ADDRESSED): Worktree isolation (`isolation: "worktree"`) for agents
- **2026-03-28** (ADDRESSED): Named agents with SendMessage for direct communication
- **2026-03-28** (ADDRESSED): 1M context window for Opus 4.6 (was 200K)
- **2026-03-28** (ADDRESSED): Sonnet 4.6 model released
- **2026-03-28** (ADDRESSED): Remote triggers and Cron scheduling tools
- **2026-03-28** (ADDRESSED): Task management tools (TaskCreate/TaskUpdate) separated from Agent
- **2026-03-28** (ADDRESSED): `auto` permission mode added
- **2026-03-28** (ADDRESSED): Write permission patterns for agent file-writing
- **2026-03-28** (ADDRESSED): NotebookEdit for Jupyter support
- **2026-03-28** (ADDRESSED): EnterPlanMode/ExitPlanMode, EnterWorktree/ExitWorktree tools
- **2026-03-28** (ADDRESSED): Hook system grew from 14 to 26+ events
- **2026-03-28** (ADDRESSED): New hook handler type: HTTP (`"type": "http"`)
- **2026-03-28** (ADDRESSED): Conditional hook `if` field
- **2026-03-28** (ADDRESSED): Skill description cap reduced from 1024 to 250 characters
- **2026-03-28** (ADDRESSED): New skill frontmatter: effort, initialPrompt, paths, disallowedTools, maxTurns
- **2026-03-28** (ADDRESSED): `/batch` command for codebase-wide parallel changes
- **2026-03-28** (ADDRESSED): `managed-settings.d/` drop-in directory for enterprise
- **2026-03-28** (ADDRESSED): Auto-memory system with MEMORY.md

## How Updates Work

1. **Automatic staleness check**: When skill-forge is invoked, `scripts/check_staleness.py` compares the current date against `Last Updated` above
2. **If stale (>30 days)**: User is prompted to run the `skill-forge-updater` agent
3. **The updater agent**: Spawns parallel research agents that write findings directly to `references/`
4. **After update**: This VERSION.md is updated with the new date and coverage summary
5. **Enforcement**: `skill-forge-preflight.py` Stop hook blocks generation if checks weren't run
