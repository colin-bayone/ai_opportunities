# Session B: Question Catalog

**Purpose:** Create a structured catalog of existing RFP questions for analysis

---

## Context

BayOne Solutions is responding to McGrath RentCorp's MSP RFP. We have 20 draft questions already prepared (in `McGrath RFP Questions BayOne_plaintext.txt`). Before we can analyze gaps, refine questions, or assess competitor risk, we need these questions in a structured format.

You are one of several Claude sessions working on this project. Your job is narrow and specific: catalog the questions, nothing more.

---

## Your Task

Read the questions document and create a structured catalog that extracts:

1. **Question ID** - Q1, Q2, etc. (as in source)
2. **Category** - The category grouping from the source
3. **RFP Tab/Section** - Where in the RFP this question references
4. **Question text** - The actual question (submission-ready version)
5. **Internal rationale** - Why we're asking (the italic text)
6. **Strategic purpose** - Classify each: Scope clarity / Evaluation intel / Pricing protection / Competitive signal / Risk mitigation
7. **Information sensitivity** - Does this question reveal anything about our approach? (None / Low / Medium / High)

---

## Input Files

**Primary:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/McGrath RFP Questions BayOne_plaintext.txt`

**Supporting context (read for background, don't catalog):**
- `McGrath RFP Analysis BayOne_plaintext.txt` - Understand the RFP context
- `MacgrathSummary 1_plaintext.txt` - Understand BayOne's position

---

## Output

Create a single file:
**`/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/question_catalog_v01.md`**

Structure:
```markdown
# McGrath RFP Questions - Catalog v01

**Date:** [date]
**Cataloged by:** Session B
**Source:** McGrath RFP Questions BayOne_plaintext.txt

## Summary Statistics
- Total questions: 20
- By category: [count per category]
- By strategic purpose: [count per purpose]
- Sensitivity distribution: [count per level]

---

## Category 1: Scope & Transition Planning

### Q1: [Short title]
- **RFP Reference:** [Tab/Section/Row]
- **Question:** [Full question text]
- **Internal Rationale:** [Why we're asking]
- **Strategic Purpose:** [Classification]
- **Sensitivity:** [None/Low/Medium/High] - [Brief explanation]

### Q2: [Short title]
[Same structure]

---

## Category 2: Evaluation & Selection Criteria
[Continue pattern]

---

## Observations

[Any patterns you notice - which categories are heavy/light, which have high sensitivity, etc. Keep factual, not strategic recommendations.]
```

---

## Classification Guidance

**Strategic Purpose:**
- **Scope clarity** - Helps us understand what we're bidding on
- **Evaluation intel** - Helps us understand how we'll be judged
- **Pricing protection** - Reduces our financial risk
- **Competitive signal** - Shows our expertise to McGrath
- **Risk mitigation** - Protects us contractually

**Information Sensitivity:**
- **None** - Any MSP would ask this
- **Low** - Slightly reveals our thinking but not problematic
- **Medium** - Reveals a specific concern or approach
- **High** - Could give competitors strategic advantage

---

## Boundaries

- DO NOT suggest new questions
- DO NOT recommend removing questions
- DO NOT modify question wording
- DO NOT provide strategic recommendations
- ONLY catalog and classify what exists

---

## When Done

Save your catalog to the specified location. The coordinator session will use this for subsequent analysis sessions.
