# Session C: Gap Analysis

**Purpose:** Identify questions we should be asking but haven't yet

---

## Context

BayOne Solutions is submitting RFP questions to McGrath RentCorp TODAY for an MSP engagement. We have 20 questions already drafted. Your job: identify gaps — important areas or angles we haven't covered.

Session B has already cataloged the existing questions. You will use that catalog plus the source documents to find what's missing.

**Critical constraint:** Questions are public — competitors will read them. Don't suggest questions that reveal our weaknesses or strategic approach. Focus on questions any sophisticated MSP should ask.

---

## Your Task

Analyze the RFP materials and question catalog to identify:

1. **Topic gaps** — Important RFP areas with no questions asked
2. **Depth gaps** — Areas touched superficially that warrant deeper probing
3. **Risk gaps** — Risks/uncertainties in the RFP that we haven't addressed
4. **Competitive intelligence gaps** — Information that would help us win but we're not asking for

For each gap, provide:
- What's missing
- Why it matters (business impact)
- A draft question (if appropriate) or reason why asking might be risky

---

## Input Files

**Primary (read in this order):**
1. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/question_catalog_v01.md` — What we've already asked
2. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/McGrath RFP Analysis BayOne_plaintext.txt` — Full RFP analysis (scope, requirements, timeline)
3. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/MacgrathSummary 1_plaintext.txt` — Strategic intel from contractor calls

---

## Output

Create a single file:
**`/home/cmoore/programming/cisco_projects/cicd/mcgrath/analysis/gap_analysis.md`**

Structure:
```markdown
# RFP Question Gap Analysis

**Date:** [date]
**Analyzed by:** Session C

## Executive Summary
[2-3 sentences: How comprehensive are our current questions? What's the biggest gap?]

## Gap Categories

### Topic Gaps
[Areas in RFP with zero questions]

| RFP Section | Gap Description | Why It Matters | Suggested Question | Risk Level |
|-------------|-----------------|----------------|-------------------|------------|
| ... | ... | ... | ... | Low/Med/High |

### Depth Gaps
[Areas touched but not deeply enough]

| Current Question | What's Missing | Suggested Follow-up | Risk Level |
|------------------|----------------|---------------------|------------|
| Q# ... | ... | ... | Low/Med/High |

### Risk Gaps
[Uncertainties/risks in RFP we haven't probed]

| Risk Area | Potential Impact | Suggested Question | Risk Level |
|-----------|------------------|-------------------|------------|
| ... | ... | ... | Low/Med/High |

### Competitive Intelligence Gaps
[Info that would help us win but we're not asking]

| Information Need | How It Helps Us | Possible Question | Risk of Asking |
|------------------|-----------------|-------------------|----------------|
| ... | ... | ... | ... |

## Priority Recommendations
[Top 5 gaps to address, ranked by importance]

## Gaps We Should NOT Fill
[Questions we considered but rejected because they reveal too much]
```

---

## Sensitivity Guidance

**Risk Level:**
- **Low** — Standard MSP question, reveals nothing
- **Medium** — Shows specific concern or preference
- **High** — Could give competitors strategic advantage

Be especially cautious about questions that would reveal:
- Areas where BayOne lacks capability
- Our pricing strategy or margins
- Specific technical approaches we plan to take
- Concerns about our ability to deliver

---

## Reference: What We've Already Asked (Summary)

From the catalog, our 20 questions cover:
- Category 1: Scope & Transition (6 questions)
- Category 2: Evaluation & Selection (3 questions)
- Category 3: Staffing & Resource Model (4 questions)
- Category 4: Technology & Environment (3 questions)
- Category 5: Commercial & Contractual (4 questions)

Look for gaps WITHIN these categories as well as entirely uncovered areas.

---

## Boundaries

- DO NOT rewrite or critique existing questions (that's Session D's job)
- DO NOT assess competitor risk of existing questions (that's Session E's job)
- DO NOT create final submission-ready questions (just drafts for review)
- ONLY identify gaps and suggest potential questions

---

## When Done

Save your analysis to the specified location. The coordinator will review with Colin and decide which gaps to fill.
