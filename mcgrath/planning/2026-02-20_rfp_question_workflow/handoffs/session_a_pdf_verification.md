# Session A: PDF Verification

**Purpose:** Ensure plaintext extractions capture all content from source PDFs

---

## Context

BayOne Solutions is responding to McGrath RentCorp's MSP RFP. We have three source PDFs and their plaintext extractions (simple copy/paste from PDFs). Before we build our knowledge base, we need to verify the plaintext is complete.

You are one of several Claude sessions working on this project. Your job is narrow and specific: verify completeness, nothing more.

---

## Your Task

Read each PDF and compare to its plaintext counterpart. Identify:

1. **Missing text** - Any content in the PDF not in the plaintext
2. **Missing structure** - Tables, lists, or formatting lost in extraction
3. **Graphics/diagrams** - Any visual content that needs description
4. **Garbled text** - OCR errors, encoding issues, or corruption

---

## Input Files

**Location:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/`

| PDF | Plaintext |
|-----|-----------|
| MacgrathSummary 1.pdf | MacgrathSummary 1_plaintext.txt |
| McGrath RFP Analysis BayOne.pdf | McGrath RFP Analysis BayOne_plaintext.txt |
| McGrath RFP Questions BayOne.pdf | McGrath RFP Questions BayOne_plaintext.txt |

---

## Output

Create a single file:
**`/home/cmoore/programming/cisco_projects/cicd/mcgrath/analysis/pdf_verification_report.md`**

Structure:
```markdown
# PDF Verification Report

**Date:** [date]
**Verified by:** Session A

## Summary
[Overall assessment: Complete / Minor issues / Significant gaps]

## Document 1: MacgrathSummary 1
- **Completeness:** [Complete / Incomplete]
- **Missing content:** [List or "None"]
- **Graphics/diagrams:** [Describe any, or "None"]
- **Issues:** [Any problems found]

## Document 2: McGrath RFP Analysis BayOne
[Same structure]

## Document 3: McGrath RFP Questions BayOne
[Same structure]

## Recommendations
[Any follow-up actions needed]
```

---

## Boundaries

- DO NOT analyze the content strategically
- DO NOT suggest RFP answers or approaches
- DO NOT create additional files beyond the report
- DO NOT modify the source files
- ONLY verify completeness and report findings

---

## When Done

Save your report to the specified location. The coordinator session will review and integrate your findings.
