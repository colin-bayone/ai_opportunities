# Kickoff: Compliance Enforcement

Use this when you need deterministic rules that Claude must follow.

---

## Example Prompt

```
We have a problem: Claude keeps forgetting our rules.

We've told it in CLAUDE.md:
- Never commit directly to main
- Always run tests before committing
- Never modify .env files
- Always include ticket number in commit messages

But it still sometimes skips these. I need something that FORCES compliance, not just suggests it. I don't care if it slows things down - correctness matters more.

Can you help me create hooks that enforce these rules? I want hard blocks, not warnings.
```

---

## What This Demonstrates

- User has experienced "LLM skips steps" problem
- Wants deterministic enforcement over probabilistic compliance
- Understands the trade-off (slower but correct)
- Pure hooks use case - may not even need a full skill
- Skill-forge should:
  - Validate this is a hooks-only solution (no SKILL.md needed)
  - Create PreToolUse hooks for:
    - Block `git commit` if on main branch
    - Block `git commit` if tests haven't run in session
    - Block Write/Edit to `.env*` files
  - Create UserPromptSubmit or Stop hook to verify ticket number
  - Explain exit code 2 pattern and stderr feedback
  - Place hooks at `.claude/hooks/` with settings.json config
