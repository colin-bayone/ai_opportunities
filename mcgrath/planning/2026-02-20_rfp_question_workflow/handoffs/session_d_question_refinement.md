# Session D: Question Refinement

**Purpose:** Improve the wording, clarity, and strategic positioning of existing questions

---

## Context

BayOne Solutions is submitting RFP questions to McGrath RentCorp TODAY. We have 20 questions drafted. Your job: make them better — clearer, more strategic, better positioned.

**Key insight from the source documents:** BayOne wants to be seen as a strategic partner, not a staffing vendor. Our 5 embedded resources give us insider advantage. Questions should subtly reinforce this positioning.

**Critical constraint:** Questions are public — competitors read them. Improvements should NOT reveal more about our strategy. If anything, refinements should make questions MORE neutral while still getting us the information we need.

---

## Your Task

Review each of the 20 questions and assess:

1. **Clarity** — Is the question unambiguous? Will MGRC understand exactly what we're asking?
2. **Positioning** — Does the question make us look like a sophisticated partner?
3. **Efficiency** — Could we combine questions or ask more in fewer words?
4. **Neutrality** — Does the wording reveal our concerns or preferences?
5. **Actionability** — Will the answer actually help us (or is it just nice-to-know)?

For questions that need improvement, provide:
- The original question
- The refined version
- What changed and why

---

## Input Files

**Primary:**
1. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/question_catalog_v01.md` — Full question catalog with rationale

**Supporting context:**
2. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/McGrath RFP Analysis BayOne_plaintext.txt` — RFP context
3. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/MacgrathSummary 1_plaintext.txt` — Strategic positioning goals

---

## Output

Create a single file:
**`/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/refinement_recommendations.md`**

Structure:
```markdown
# Question Refinement Recommendations

**Date:** [date]
**Analyzed by:** Session D

## Executive Summary
[2-3 sentences: Overall quality assessment. How many need changes?]

## Questions Requiring No Changes
[List question numbers that are already well-crafted]

Q1, Q3, Q7... — These are clear, well-positioned, and neutral.

## Questions with Minor Refinements

### Q#: [Short title]
**Original:** [full original question]
**Refined:** [improved version]
**Changes:** [What changed and why]
**Impact:** [Clarity / Positioning / Neutrality / Efficiency]

## Questions with Significant Refinements

### Q#: [Short title]
**Original:** [full original question]
**Refined:** [improved version]
**Changes:** [What changed and why]
**Impact:** [Clarity / Positioning / Neutrality / Efficiency]
**Risk Note:** [If refinement changes sensitivity level]

## Questions to Consider Removing
[Any questions that are redundant, low-value, or risky]

### Q#: [Short title]
**Original:** [full question]
**Reason to Remove:** [Why this question may not be worth asking]
**Alternative:** [If applicable, what to ask instead]

## Consolidation Opportunities
[Questions that could be combined]

| Questions | Combined Version | Benefit |
|-----------|-----------------|---------|
| Q# + Q# | [merged question] | [fewer questions, same info] |

## Positioning Enhancements
[Specific wording changes that better position BayOne as strategic partner]

## Summary of Recommended Changes

| Question | Action | Priority |
|----------|--------|----------|
| Q1 | No change | — |
| Q2 | Minor refinement | Medium |
| ... | ... | ... |
```

---

## Refinement Principles

1. **Shorter is usually better** — Concise questions are easier to answer
2. **One question, one topic** — Avoid compound questions that get partial answers
3. **Specific > vague** — "What is the monthly ticket volume?" beats "Can you tell us about volumes?"
4. **Neutral framing** — Ask "Is X acceptable?" not "We prefer X — is that okay?"
5. **Professional tone** — Match the formality of an enterprise RFP

---

## Sensitivity Watch

The catalog flags these as medium-sensitivity:
- Q8 (multi-MSP vs single provider) — reveals potential consortium approach
- Q9 (incumbent advantage weighting) — directly signals incumbent status
- Q18 (hybrid pricing model) — reveals pricing preference
- Q19 (multi-year pricing model) — reveals Year 1 aggressive pricing strategy

Consider whether refinements can reduce sensitivity while preserving the question's value.

---

## Boundaries

- DO NOT identify new questions to add (that's Session C's job)
- DO NOT assess overall competitor risk (that's Session E's job)
- DO NOT make final decisions — provide recommendations for Colin's review
- ONLY refine existing questions

---

## When Done

Save your recommendations to the specified location. The coordinator will review with Colin and decide which refinements to accept.
