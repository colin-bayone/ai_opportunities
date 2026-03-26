# Kickoff: Multi-Agent Workflow

Use this when you need multiple specialized agents working together.

---

## Example Prompt

```
I need to build a "feature-implementation" skill that coordinates multiple agents:

1. A planner agent that breaks down the feature into tasks
2. An explorer agent that researches the codebase for patterns to follow
3. Multiple worker agents that implement different parts in parallel
4. A reviewer agent that checks the work before completion

The planner and explorer should be cheap and fast (read-only).
The workers need to edit files.
The reviewer should be thorough (maybe Opus?).

Workers don't need to talk to each other - they just report back.
But I want the reviewer to block completion if quality isn't met.

How do I set this up?
```

---

## What This Demonstrates

- User understands they need agents but wants guidance on configuration
- Clear roles with different requirements (model selection matters)
- Mix of read-only and write agents (permission modes)
- Subagents pattern (workers report back, no inter-agent communication)
- Quality gate via hooks (reviewer blocks completion)
- Skill-forge should:
  - Confirm subagents over Agent Teams (no inter-agent communication needed)
  - Help with model selection (haiku for explorer, sonnet for workers, opus for reviewer)
  - Set up permission modes (plan for explorer, acceptEdits for workers)
  - Create Stop hook for the reviewer's quality gate
