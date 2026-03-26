# Kickoff: Help Me Understand

Use this when you're new to skills or unsure what's possible.

---

## Example Prompt

```
I keep doing the same repetitive tasks when reviewing PRs:

- Check if tests pass
- Look for common security issues
- Verify the PR follows our coding standards
- Make sure migrations are included if models changed

I'm tired of remembering all these steps. I heard skills can help but I don't know where to start. What are my options?
```

---

## What This Demonstrates

- User has a pain point but no solution in mind
- Describes workflow, not technical requirements
- Perfect candidate for Step 0 option 1 ("I need help understanding what's possible")
- Skill-forge should:
  - Explain that this could be a skill with agents (parallel reviewers)
  - Suggest hooks for enforcement (Stop hook to verify all checks done)
  - Ask clarifying questions about which parts need determinism vs flexibility
  - Help them discover they might want multiple agents working together
