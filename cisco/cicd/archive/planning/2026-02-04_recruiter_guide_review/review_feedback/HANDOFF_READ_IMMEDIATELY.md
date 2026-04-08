# STOP - Read This Before Doing Anything Else

I had another Claude session review your work on the recruiter guides. They found problems.

**UPDATE (after all 4 guides approved):** Add CrewAI to the Agentic AI Engineer guide. See "Final Update Required" section at the bottom.

Before you make any more changes, read the feedback documents in this folder:

```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-04_recruiter-guides/review_feedback/
```

## Read These Files In Order

1. **01_critical_feedback.md** - Detailed critique of what's wrong and what needs fixing
2. **02_validation_checklist.md** - Checklist to validate every guide before showing me
3. **03_search_string_reference.md** - Properly constructed search strings for all 4 roles

## What You Need To Do

1. Read all three documents completely
2. Fix the Senior AI Solutions Engineer and Automation Engineer guides based on the feedback
3. Run both guides through the validation checklist
4. Show me the corrected guides
5. Do not proceed to AI Engineer or Agentic AI Engineer until I approve the first two

## Key Issues Found

- AI pair programming should be a **MUST-HAVE**, not a strong signal
- Copilot is NOT equivalent to Claude Code/Cursor - make this distinction explicit
- Search strings need to be tiered (Layer 1/2/3) and actually tested
- Screening questions need weak/good answer indicators that a non-technical recruiter can use
- No arbitrary company lists or VC jargon
- Some technical terms still lack plain-language explanations

Do not argue with the feedback. Read it, understand it, fix it.

---

## Final Update Required

**After all 4 guides are approved**, add CrewAI to the Agentic AI Engineer recruiter guide:

### Location
`/claude/2026-02-02_resource-planning/deliverables/job_descriptions/recruiter_guides/recruiter_guide_agentic_ai_engineer.html`

### Changes Required

1. **Synonym Groups** - Add CrewAI to the "Agentic Patterns" group:
   ```
   (LangGraph OR CrewAI OR "function calling" OR "tool calling" OR "tool use" OR autonomous)
   ```

2. **Tech Stack Keywords** - Add CrewAI to Nice-to-Have (Bonus Points):
   ```
   <span class="tag-secondary">CrewAI</span>
   ```

3. **Search Strings** - Optionally add CrewAI to Layer 2:
   ```
   ... AND (LangGraph OR CrewAI OR "function calling" OR "tool calling" ...
   ```

### Why
CrewAI is a legitimate multi-agent framework with real production adoption. It's appropriate for the Agentic AI Engineer role which builds autonomous systems.
