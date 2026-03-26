# Kickoff: I Know What I Want

Use this when you have a clear vision of the skill you need.

---

## Example Prompt

```
I want to create a skill called "api-docs-generator" that:

1. Reads our Python FastAPI codebase
2. Extracts all endpoint definitions, request/response models, and docstrings
3. Generates OpenAPI-compliant documentation in markdown format
4. Outputs to a docs/ folder with one file per router

It should auto-invoke when I mention "API documentation", "generate docs", or "document endpoints".

It should NOT invoke for general Python questions or non-documentation tasks.

I want a Python script to do the extraction (deterministic), and Claude to handle the markdown formatting (flexible).
```

---

## What This Demonstrates

- Clear skill name and purpose
- Specific trigger conditions (WHEN to use)
- Explicit exclusions (WHEN NOT to use)
- Hybrid approach: scripts for deterministic work, LLM for flexible formatting
- User is ready to jump to Step 1 (Understand) or even Step 2 (Plan)
