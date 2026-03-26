# Agent Teams Token Cost Clarification

> **Research Date:** 2026-02-11
> **Purpose:** Verify official Anthropic numbers on Agent Teams vs subagent token costs
> **Finding:** The "~5x per teammate" estimate is NOT official. Official figure is **7x for plan mode**.

---

## Official Anthropic Statement

From the official Claude Code documentation at [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs):

> **"Agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode, because each teammate maintains its own context window and runs as a separate Claude instance."**

This is the **only official multiplier** provided by Anthropic.

---

## What We Know (Official)

### 1. Agent Teams Token Consumption Calculation

| Fact | Source | Status |
|------|--------|--------|
| 7x more tokens than standard sessions (plan mode) | [Claude Code Costs Docs](https://code.claude.com/docs/en/costs) | **Official** |
| Token usage scales with number of active teammates | [Claude Code Costs Docs](https://code.claude.com/docs/en/costs) | **Official** |
| Token usage scales with how long each teammate runs | [Claude Code Costs Docs](https://code.claude.com/docs/en/costs) | **Official** |
| "Token usage is roughly proportional to team size" | [Claude Code Costs Docs](https://code.claude.com/docs/en/costs) | **Official** |
| Each teammate maintains its own context window | [Claude Code Agent Teams Docs](https://code.claude.com/docs/en/agent-teams) | **Official** |

### 2. What's NOT Provided Officially

| Missing Information | Status |
|---------------------|--------|
| Multiplier for Agent Teams in implementation mode (non-plan) | **Not documented** |
| Specific multiplier for subagents vs single session | **Not documented** |
| Formula for calculating Agent Team costs | **Not documented** |
| Comparison formula: subagents vs Agent Teams | **Not documented** |

---

## Is the "~5x per teammate" Estimate Accurate?

**No official source confirms this.**

### Where did "~5x" come from?

Community blog posts (not official Anthropic documentation):

| Source | Quote | Official? |
|--------|-------|-----------|
| [Addy Osmani's Blog](https://addyosmani.com/blog/claude-code-agent-teams/) | "A 5-person team uses roughly 5x the tokens of a single session" | **No** |
| [alexop.dev](https://alexop.dev/posts/from-tasks-to-swarms-agent-teams-in-claude-code/) | "token cost is real (~5x per teammate)" | **No** |
| Various Medium posts | Similar estimates | **No** |

### What does this mean?

The "~5x per teammate" appears to be a **community rule-of-thumb** derived from:
- Basic math: N teammates = ~Nx tokens (each has separate context)
- Practical observation, not official documentation

The **official 7x figure** is specifically for **plan mode**, which involves more context loading per teammate.

---

## Subagent Token Costs (Official)

Anthropic provides **no specific multiplier** for subagent token costs vs single sessions.

### What IS documented:

From [Claude Code Costs Docs](https://code.claude.com/docs/en/costs):

> "Running tests, fetching documentation, or processing log files can consume significant context. Delegate these to subagents so the verbose output stays in the subagent's context while only a summary returns to your main conversation."

> "For simple subagent tasks, specify model: haiku in your subagent configuration."

### Interpretation:

- Subagents can **reduce** main conversation costs by isolating verbose output
- Subagent costs depend on: model used (Haiku vs Sonnet vs Opus), task complexity, context accumulated
- **No official comparison multiplier to Agent Teams**

---

## Agent SDK Cost Model

From [Claude Agent SDK Cost Tracking Docs](https://platform.claude.com/docs/en/agent-sdk/cost-tracking):

> Costs are **"additive by token consumption rather than by system complexity"**

This confirms:
- No special multiplier surcharge for multi-agent systems
- You pay for tokens consumed, regardless of architecture
- Agent Teams cost more because each teammate is a separate Claude instance with its own context

---

## Corrected Understanding

### Agent Teams Cost Model

```
Agent Teams Cost = Sum of (each teammate's token consumption)
                 = ~Nx base cost where N = number of teammates

Plan Mode Overhead = 7x standard session (official)
Implementation Mode = Not documented (likely lower than 7x)
```

### Subagent Cost Model

```
Subagent Cost = Individual subagent token consumption
              = Depends on model (Haiku cheaper than Sonnet)
              + Depends on task scope

Total Cost = Main session + Sum of (all subagent sessions)
           = Additive, no special multiplier
```

### Key Difference

| Factor | Subagents | Agent Teams |
|--------|-----------|-------------|
| Context isolation | Yes - results summarized back | Yes - fully independent |
| Multiple instances | Yes | Yes |
| Communication overhead | None (report-back only) | Yes (inter-agent messaging) |
| Official multiplier | None provided | 7x in plan mode |

---

## What Anthropic DOES Say About Costs

Direct quotes from official documentation:

### On Agent Teams ([code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)):

> "Agent teams use significantly more tokens than a single session."

> "For research, review, and new feature work, the extra tokens are usually worthwhile. For routine tasks, a single session is more cost-effective."

> "Keep teams small. Each teammate runs its own context window, so token usage is roughly proportional to team size."

> "Clean up teams when work is done. Active teammates continue consuming tokens even if idle."

### On Subagents ([code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)):

> "Control costs by routing tasks to faster, cheaper models like Haiku"

---

## Summary

| Question | Answer |
|----------|--------|
| Is there an official token multiplier for Agent Teams? | **Yes: 7x in plan mode** |
| Does the 7x apply to all Agent Team usage? | **No: only "when teammates run in plan mode"** |
| Is the "~5x per teammate" accurate? | **Unconfirmed: community estimate, not official** |
| Is there an official subagent multiplier? | **No: not documented** |
| How are multi-agent costs calculated? | **Additive: sum of all token consumption** |

---

## Recommendation

For skill-forge documentation and estimates:

1. **Use official 7x figure** for Agent Teams in plan mode
2. **Use "roughly proportional to team size"** for general Agent Teams estimates
3. **Do not cite "~5x per teammate"** as an official figure
4. For subagents, state: "costs depend on model selection and task scope; use Haiku for simple tasks"
5. Clarify that all multi-agent costs are **additive token consumption**

---

## Sources

| Source | URL | Authority |
|--------|-----|-----------|
| Claude Code Costs Documentation | https://code.claude.com/docs/en/costs | **Official Anthropic** |
| Claude Code Agent Teams Documentation | https://code.claude.com/docs/en/agent-teams | **Official Anthropic** |
| Claude Code Subagents Documentation | https://code.claude.com/docs/en/sub-agents | **Official Anthropic** |
| Claude Agent SDK Cost Tracking | https://platform.claude.com/docs/en/agent-sdk/cost-tracking | **Official Anthropic** |
| Addy Osmani Blog | https://addyosmani.com/blog/claude-code-agent-teams/ | Community |
| alexop.dev Blog | https://alexop.dev/posts/from-tasks-to-swarms-agent-teams-in-claude-code/ | Community |
