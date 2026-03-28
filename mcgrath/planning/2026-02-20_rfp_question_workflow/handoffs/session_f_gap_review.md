# Session F: Gap Analysis Review (Interactive)

**Purpose:** Walk Colin through the gap analysis findings one topic at a time

---

## Context

BayOne Solutions is submitting RFP questions to McGrath RentCorp today. Session C produced a gap analysis identifying areas where we have no questions or insufficient coverage. Your job: walk Colin through each gap **one at a time** so he can decide which ones to pursue.

Colin is the Director of AI at BayOne. He will have specific guidance on AI/automation topics.

---

## Critical Instructions

**DO NOT dump walls of text.** Present one gap at a time. Wait for Colin's response before moving to the next.

Format for each gap:
1. Name the gap (one line)
2. Why it matters (2-3 sentences max)
3. The suggested question from the analysis
4. Ask: "Want to add this, modify it, or skip?"

Only after Colin responds, move to the next gap.

---

## Input File

**`/home/cmoore/programming/cisco_projects/cicd/mcgrath/analysis/gap_analysis.md`**

This contains:
- 6 topic gaps (areas with zero questions)
- 5 depth gaps (areas touched but not deep enough)
- 5 risk gaps (uncertainties not probed)
- Competitive intelligence gaps

---

## Your Task

1. Start by asking Colin which category he wants to review first (topic gaps, depth gaps, risk gaps, or competitive intel gaps)
2. Present gaps one at a time within that category
3. For each gap, get his decision: add / modify / skip
4. Track decisions as you go
5. When done with a category, ask if he wants to continue to the next

---

## Output

When Colin is done reviewing, create:
**`/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/gap_decisions.md`**

Structure:
```markdown
# Gap Review Decisions

**Date:** [date]
**Reviewed by:** Colin Moore

## Questions to Add
[List questions Colin approved, with his modifications if any]

## Skipped Gaps
[List gaps Colin chose not to pursue, with brief reason if given]
```

---

## Boundaries

- DO NOT present multiple gaps at once
- DO NOT make decisions for Colin
- DO NOT rush through — let him guide the pace
- ONLY facilitate the review; he decides what to add
