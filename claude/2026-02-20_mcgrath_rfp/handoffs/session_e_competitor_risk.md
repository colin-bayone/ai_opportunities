# Session E: Competitor Risk Assessment

**Purpose:** Assess which questions reveal too much to competitors or position us poorly

---

## Context

BayOne Solutions is submitting RFP questions to McGrath RentCorp TODAY. **All submitted questions are visible to all bidders.** Your job: evaluate each question through a competitor's eyes.

BayOne's situation:
- 5 people already embedded at McGrath (insider advantage)
- Positioning as strategic partner, not staffing vendor
- May not have deep bench in all 10 solution areas
- Considering consortium approach for gaps

Competitors likely include:
- Large MSPs (Infosys, Wipro, Cognizant) — more resources, offshore leverage
- Specialized Oracle/Salesforce partners — deeper technical expertise
- Regional MSPs — relationship-focused, similar to BayOne

---

## Your Task

For each of the 20 questions, assess:

1. **Information leakage** — What does this question reveal about BayOne?
2. **Competitive advantage given** — Could a competitor use this to strengthen their bid?
3. **Positioning impact** — Does this make us look strong or weak?
4. **Counter-intelligence** — What might competitors ask that we should anticipate?

Focus especially on the 4 medium-sensitivity questions flagged in the catalog:
- Q8: Multi-MSP vs single provider
- Q9: Incumbent advantage weighting
- Q18: Hybrid pricing model
- Q19: Multi-year pricing model

---

## Input Files

**Primary:**
1. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/question_catalog_v01.md` — Full catalog with sensitivity ratings

**Supporting context:**
2. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/McGrath RFP Analysis BayOne_plaintext.txt` — SWOT, win strategy
3. `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/MacgrathSummary 1_plaintext.txt` — BayOne's position and risks

---

## Output

Create a single file:
**`/home/cmoore/programming/cisco_projects/cicd/mcgrath/analysis/competitor_risk_assessment.md`**

Structure:
```markdown
# Competitor Risk Assessment

**Date:** [date]
**Analyzed by:** Session E

## Executive Summary
[2-3 sentences: Overall risk level of our question set. Key concerns.]

## Risk Rating Summary

| Risk Level | Count | Questions |
|------------|-------|-----------|
| Low | # | Q1, Q2, ... |
| Medium | # | Q8, Q9, ... |
| High | # | (hopefully none) |

---

## High-Risk Questions (Action Required)

### Q#: [Short title]
**Question:** [full text]
**What It Reveals:** [specific information leaked]
**How Competitors Could Use This:** [concrete example]
**Recommendation:** Remove / Reword / Accept Risk
**If Rewording:** [suggested alternative]

---

## Medium-Risk Questions (Review Recommended)

### Q#: [Short title]
**Question:** [full text]
**What It Reveals:** [specific information leaked]
**How Competitors Could Use This:** [concrete example]
**Mitigation Options:**
1. [Option A]
2. [Option B]
**Recommendation:** [action + rationale]

---

## Low-Risk Questions (No Action Needed)

[Brief table or list confirming these are safe]

| Question | Why It's Safe |
|----------|---------------|
| Q1 | Any MSP would ask this |
| Q2 | Standard scoping question |
| ... | ... |

---

## Competitor Counter-Intelligence

### What competitors might learn from our questions:
1. [Insight they could gain]
2. [Insight they could gain]

### Questions competitors might ask that we should anticipate:
1. [Question] — What this reveals about them
2. [Question] — What this reveals about them

### How our questions compare to what sophisticated competitors likely ask:
[Assessment of whether we look more/less sophisticated]

---

## Strategic Positioning Assessment

### Questions that make us look STRONG:
- Q#: [Why it positions us well]
- Q#: [Why it positions us well]

### Questions that make us look WEAK:
- Q#: [Concern and mitigation]

### Questions that signal our incumbent advantage appropriately:
- Q#: [Assessment]

### Questions that might undermine our "strategic partner" positioning:
- Q#: [Concern]

---

## Final Recommendations

### Must Change:
[Questions requiring immediate attention]

### Should Change:
[Questions worth improving if time permits]

### Accept As-Is:
[Questions where risk is acceptable given information value]

### Remove Entirely:
[Questions where risk outweighs value]
```

---

## Competitor Mindset Guidance

When assessing each question, ask yourself:
- "If I were Wipro/Infosys, what would I learn from this?"
- "If I were a specialized Oracle partner, how would I react?"
- "Does this question make BayOne look like a serious MSP or a staffing shop?"

Remember: The goal is NOT to ask bland questions. Good questions show sophistication. The goal is to avoid revealing strategic weaknesses or approach details that competitors could exploit.

---

## Boundaries

- DO NOT suggest new questions (that's Session C's job)
- DO NOT refine question wording (that's Session D's job)
- DO NOT make final decisions — provide risk assessment for Colin's review
- ONLY assess competitive risk and positioning impact

---

## When Done

Save your assessment to the specified location. The coordinator will review with Colin and decide on any changes needed before submission.
