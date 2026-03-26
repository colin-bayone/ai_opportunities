# Skill-Forge Research Index

**Session:** 2026-02-11_skill-forge-creation
**Purpose:** Research for building a new skill-forge skill to replace skill-creator

---

## Research Documents

### Phase 1: New Feature Research (Dec 2025 - Feb 2026)

| File | Contents | Lines |
|------|----------|-------|
| `00_claude_code_december_2025_features.md` | 28 major feature categories from Dec 2025 | ~1500 |
| `01_claude_code_jan_feb_2026_features.md` | All Jan/Feb 2026 features including Agent Teams | ~1200 |
| `02_skill_creator_comprehensive_breakdown.md` | Complete breakdown of Anthropic's skill-creator | ~800 |
| `claude_agent_sdk_research.md` | Agent SDK, subagents vs teams, patterns | ~600 |

---

## Key New Features Summary (Dec 2025 - Feb 2026)

### Revolutionary Features

1. **Agent Teams / Peer-to-Peer Agents** (Feb 6, 2026)
   - True peer-to-peer collaboration (not hierarchical)
   - Shared task list with dependency tracking
   - Direct messaging between teammates
   - Enable: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

2. **Async Subagents** (Dec 10, 2025)
   - Background execution with wake-up mechanism
   - Ctrl+B to move subagent to background
   - Parallel task execution

3. **MCP Tool Search** (Jan 2026)
   - Lazy loading for MCP tools
   - 95% context window savings
   - 49% → 74% accuracy improvement

4. **Skills Hot Reload** (Jan 7, 2026)
   - Immediate changes without restart
   - Real-time testing and iteration

5. **Hooks System Enhanced**
   - PreToolUse, PostToolUse, Stop, Setup events
   - Type options: command, prompt, agent
   - Async hooks support

### Infrastructure Changes

- **LSP Integration** (Dec 21, 2025): 900x performance improvement
- **Claude Code 2.1.0** (Jan 7, 2026): 1,096 commits
- **Opus 4.6** (Feb 2026): 1M context window
- **Fast Mode** (Feb 2026): 2.5x faster output

### Important Patterns

- **Subagents vs Agent Teams**: Subagents for sequential/dependent work, Teams for parallel/independent
- **Progressive Disclosure**: 3-tier loading (metadata → SKILL.md → resources)
- **Context as Public Good**: Minimize token usage, challenge every inclusion
- **Verification-First**: Always provide tests/screenshots for self-verification

---

## Skill Creation Key Insights

### From skill-creator Analysis

1. **Structure**: SKILL.md + optional scripts/, references/, assets/
2. **Triggering**: Description field must contain ALL "when to use" info
3. **Freedom Levels**: High (text) → Medium (pseudocode) → Low (scripts)
4. **Progressive Disclosure**: Only load what's needed, when needed
5. **6-Step Process**: Understand → Plan → Initialize → Edit → Package → Iterate

### New Capabilities to Leverage

- **Hooks in Skills**: PreToolUse/PostToolUse for guardrails
- **Agent-based hooks**: Spawn subagents for complex verification
- **Skills can specify tools**: `allowed-tools` frontmatter
- **Skills can spawn subagents**: Via Task tool patterns
- **Hot reload**: Test changes instantly

---

## Documents from Claude Code Official Docs

The claude-code-guide agent provided comprehensive documentation on:

- Subagents & Task tool (built-in types, custom creation, tool control)
- Hooks system (all events, handler types, configuration)
- Skills architecture (structure, frontmatter, invocation control)
- Agent Teams & multi-agent patterns
- MCP integration
- Configuration files & settings
- Async operations & scripting
- Permissions & security
- Best practices

This is captured in the research agent outputs above.

---

## Next Steps

1. **Phase 2**: Research best practices (accounting for recency)
2. **Phase 3**: Investigate local .claude/ skills, agents, scripts
3. **Sync**: Discuss findings and plan skill-forge architecture
