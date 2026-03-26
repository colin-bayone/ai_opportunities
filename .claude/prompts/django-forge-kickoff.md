# Django Forge Session Kickoff

Copy and paste this when starting a Django Forge session:

---

Use your Django Forge skill to implement issue #960.
We had used this skill to implement this issue in the past, but it clearly missed critical workflow items like the traffic controller and git operations handler agent. Let's be extra careful with this and get it right this time. 

**Before you start:**
- Read and understand the entire workflow in SKILL.md
- At each step, self-check that you are following the workflow correctly
- If unsure, re-read the relevant section before proceeding

**Non-negotiable rules:**
- Create the worktree FIRST
- Create state.json IMMEDIATELY after session folder
- Create a DRAFT PR after your FIRST file edit (not at the end)
- At each checkpoint, STOP and verify every box before proceeding
- Follow the phases in order - no shortcuts, even for LOW complexity

**USE YOUR SUB-AGENTS - If you're not spawning agents, you're doing it wrong.**

Available agents you SHOULD be using:

| Agent | When to Use |
|-------|-------------|
| `git-operations-handler` | ALL git operations (branch, commit, PR) - always |
| `traffic-controller` | Workflow compliance checking - always |
| `docs-explorer` | Documentation exploration - always |
| `model-explorer` | Database/model work |
| `view-explorer` | Views/services/URLs |
| `template-explorer` | UI/template changes |
| `codebase-explorer` | Cross-cutting patterns |
| `architect` + `engineer` | Planning (HIGH complexity) |
| `planner` | Planning (MEDIUM/LOW complexity) |
| `foreman` + `code-worker` + `test-worker` | Implementation (HIGH complexity) |
| `judge` | Quality evaluation (HIGH, optional MEDIUM) |
| `playwright-quick` | Fast UI verification, screenshots, pass/fail (default for most UI changes) |
| `playwright-tester` | Comprehensive UI testing with detailed reports (complex multi-page flows) |
| `research-agent` | Web search for best practices |

Use agents when the workflow calls for them. Don't skip agent steps to "save time."

**Playwright Testing (MANDATORY for UI changes):**
- **Python changes = Server restart required** (views.py, models.py, etc.)
- Ask user if dev server is running (on correct port!) BEFORE invoking Playwright
- Default to `playwright-quick` for most cases
- Use `playwright-tester` for complex multi-step workflows
- Write script to file first, then run it (transparency for debugging)
- Screenshots with FULL ABSOLUTE PATHS must be shared with user
- Report must include: what was tested, URLs, output, screenshot links

Read the skill carefully. Follow it precisely. Self-check constantly. I will reject sloppy work.

**Git Push Permissions:**
Only I am allowed to push. Any time you need to push, hand off to me with the push command as a one-liner, I will run it and then revert back to you. Do you understand?