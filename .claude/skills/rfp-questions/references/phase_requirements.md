# Phase Requirements Reference

This document defines the **required artifacts** for each phase. The Stop hook verifies these artifacts exist before allowing progression to the next phase.

---

## Contents

0. [Phase 0: Document Ingestion](#phase-0-document-ingestion)
1. [Phase 1: Setup](#phase-1-setup)
2. [Phase 2: Catalog & Analysis](#phase-2-catalog--analysis)
3. [Phase 3: Interactive Review](#phase-3-interactive-review)
4. [Phase 4: Quality Checks](#phase-4-quality-checks)
5. [Phase 5: User Approval](#phase-5-user-approval)
6. [Phase 6: Document Generation](#phase-6-document-generation)
7. [state.json Schema](#statejson-schema)

---

## Phase 0: Document Ingestion

**Gate:** Ingested documents must exist before Phase 1 can use them.

| Artifact | Path | Min Size | Description |
|----------|------|----------|-------------|
| Ingestion Index | `ingested/index.md` | 50 chars | Master inventory of processed documents |

**This phase is OPTIONAL** - only required when source documents need visual processing (PDFs, Excel, images).

**Content requirements for ingested/index.md:**

```markdown
# Document Ingestion Index

## Documents Processed

| Document | Type | Pages/Sheets | Output Folder |
|----------|------|--------------|---------------|
| rfp_document.pdf | PDF | 45 pages | ingested/rfp_document/ |
| integration_list.xlsx | Excel | 3 sheets | ingested/integration_list/ |

## Processing Notes
- [Any issues or special handling noted]

## Status
Ingestion complete: Yes
```

**Per-document requirements:**

For each processed document, must have:
- `ingested/<doc_name>/index.md` - Document overview
- `ingested/<doc_name>/page_XX.md` or `sheet_XX.md` - Content files

**state.json updates:**
- `ingestion_complete: true`
- `ingested_documents` array populated
- `completed_phases` includes "ingestion"

**Scripts used:**
- `scripts/scan_documents.py` - Inventory source folder
- `scripts/process_document.py` - PDF/image processing via Gemini
- `scripts/process_excel.py` - Excel processing via openpyxl + Gemini

**Environment requirements:**
```bash
export GEMINI_API_KEY="your-api-key"
pip install google-genai openpyxl
```

---

## Phase 1: Setup

**Gate:** All setup artifacts must exist before Phase 2.

| Artifact | Path | Min Size | Description |
|----------|------|----------|-------------|
| Source Verification | `phase_01_setup/source_verification.md` | 50 chars | Confirmation that source documents are complete |

**Content requirements for source_verification.md:**

```markdown
# Source Document Verification

## Documents Provided
- [ ] RFP: <path>
- [ ] Existing Questions: <path>
- [ ] Supplementary: <path>

## Document Status
| Document | Status | Issues |
|----------|--------|--------|
| [name] | Complete/Incomplete | [description] |

## Readiness
[Ready to proceed / Blocked by issues]
```

**Additional requirements:**
- state.json initialized with client_name, rfp_name
- .active marker file created
- Folder structure scaffolded

---

## Phase 2: Catalog & Analysis

**Gate:** All 5 analysis artifacts must exist before Phase 3.

| Artifact | Path | Min Size | Description |
|----------|------|----------|-------------|
| Source Report | `phase_02_analysis/source_verification_report.md` | 100 chars | Document map from Session A |
| Question Catalog | `phase_02_analysis/question_catalog_v01.md` | 200 chars | Structured questions from Session B |
| Gap Analysis | `phase_02_analysis/gap_analysis.md` | 200 chars | Coverage gaps from Session C |
| Refinement Recommendations | `phase_02_analysis/refinement_recommendations.md` | 100 chars | Risk analysis from Session D |
| Competitor Assessment | `phase_02_analysis/competitor_risk_assessment.md` | 200 chars | Holistic risk from Session E |

**Session A output structure:**
- Document list with status
- Section breakdown with page/row references
- Any issues found

**Session B output structure:**
- Question count by category
- Each question with ID, text, category, RFP reference
- Category index

**Session C output structure:**
- Coverage summary table
- Topic gaps with suggested questions
- Depth gaps with suggested questions
- Risk gaps with suggested questions

**Session D output structure:**
- Risk level summary
- Questions requiring revision with full original, issue, suggested revision
- Questions to consider removing
- Low/no risk questions list

**Session E output structure:**
- Overall risk profile
- Pattern analysis
- High/medium/low risk items
- Questions that strengthen position

---

## Phase 3: Interactive Review

**Gate:** Review decisions must be recorded before Phase 4.

| Artifact | Path | Min Size | Description |
|----------|------|----------|-------------|
| Review Decisions | `phase_03_review/review_decisions.md` | 50 chars | Log of all human decisions |

**Content requirements for review_decisions.md:**

```markdown
# Review Decisions Log

## Summary

| Category | Reviewed | Accepted | Modified | Rejected |
|----------|----------|----------|----------|----------|
| Gaps | 12 | 8 | 2 | 2 |
| Refinements | 5 | 3 | 1 | 1 |
| Removals | 2 | 1 | 0 | 1 |

## Decision Log

| # | Item | Type | Decision | Notes | Timestamp |
|---|------|------|----------|-------|-----------|
| 1 | Gap 1 | New Question | Accepted | Added as Q29 | 2026-02-23 14:30 |
| 2 | Q13 | Revision | Accepted | Removed strategic signal | 2026-02-23 14:35 |
```

**state.json updates:**
- `review_decisions` array populated
- `gaps_reviewed`, `gaps_accepted`, etc. counts updated
- Question counts updated

**Optional but expected:**
- `phase_03_review/consolidated_questions_v02.md` - Updated question list

---

## Phase 4: Quality Checks

**Gate:** All 3 quality artifacts must exist before Phase 5.

| Artifact | Path | Min Size | Description |
|----------|------|----------|-------------|
| Final Risk Review | `phase_04_quality/final_risk_review.md` | 100 chars | Holistic review from Session G |
| Duplication Check | `phase_04_quality/duplication_check.md` | 50 chars | Overlap analysis from Session H |
| Depth Check | `phase_04_quality/depth_check.md` | 50 chars | Depth analysis from Session I |

**Session G output structure:**
- Review context (counts before/after)
- Overall assessment
- Patterns resolved
- New patterns checked
- Remaining concerns (if any)
- Final recommendation

**Session H output structure:**
- Summary (exact/semantic duplicates, overlaps)
- Duplicates found with details
- Partial overlaps with analysis
- Clean questions list

**Session I output structure:**
- Summary (appropriate/too granular/too vague)
- Too granular questions with suggested simplifications
- Too vague questions with suggested expansions
- Appropriate depth questions confirmation

---

## Phase 5: User Approval

**Gate:** Explicit user approval must be recorded in state.json.

| Artifact | Path | Min Size | Description |
|----------|------|----------|-------------|
| (state.json check) | - | - | `approved: true` in state.json |

**Verification:**
```python
if state.get("approved", False):
    return True
```

**What must be presented to user:**
- Final question count by type and category
- Summary of quality check findings
- Any remaining concerns
- Explicit approval request

**NEVER assume approval. ALWAYS wait for explicit "yes", "approved", "proceed".**

---

## Phase 6: Document Generation

**Gate:** Final markdown must exist.

| Artifact | Path | Min Size | Description |
|----------|------|----------|-------------|
| Final Questions | `phase_06_outputs/final_questions.md` | 200 chars | Complete question document |

**Optional outputs (based on user selection):**
- `phase_06_outputs/rfp_questions_review.html` - Professional HTML
- `phase_06_outputs/rfp_questions.csv` - Spreadsheet export

**Completion:**
- Remove `.active` marker
- Set `workflow_complete: true` in state.json

---

## state.json Schema

Critical fields that must be populated:

```json
{
  "client_name": "McGrath",
  "rfp_name": "MSP RFP 2026",
  "session_folder": ".rfp-questions/mcgrath",
  "current_phase": "review",
  "completed_phases": ["setup", "analysis"],
  "what_we_are_building": "36 clarifying questions for MSP RFP",
  "competitive_context": "BayOne is smaller bidder vs large embedded MSPs",
  "source_documents": ["rfp_plaintext.md", "integration_list.xlsx"],
  "existing_questions_count": 20,
  "question_counts": {
    "original": 16,
    "revised": 3,
    "new": 17,
    "removed": 1,
    "total": 36
  },
  "review_decisions": [
    {
      "item": "Gap 1",
      "type": "new_question",
      "decision": "accepted",
      "notes": "Added as Q29",
      "timestamp": "2026-02-23T14:30:00Z"
    }
  ],
  "gaps_reviewed": 12,
  "gaps_accepted": 8,
  "gaps_modified": 2,
  "gaps_rejected": 2,
  "critical_learnings": [
    "Large MSPs have embedded teams who get answers internally"
  ],
  "approved": false,
  "requested_outputs": ["markdown", "html", "csv"],
  "big4_review_requested": false,
  "workflow_complete": false,
  "agent_mode": "teams"
}
```

---

## Verification Commands

To manually verify phase completion:

```bash
# Check Phase 1
ls -la .rfp-questions/*/phase_01_setup/

# Check Phase 2
ls -la .rfp-questions/*/phase_02_analysis/

# Check Phase 3
cat .rfp-questions/*/phase_03_review/review_decisions.md

# Check Phase 4
ls -la .rfp-questions/*/phase_04_quality/

# Check approval
cat .rfp-questions/*/orchestration/state.json | python -m json.tool | grep approved

# Check Phase 6
ls -la .rfp-questions/*/phase_06_outputs/
```
