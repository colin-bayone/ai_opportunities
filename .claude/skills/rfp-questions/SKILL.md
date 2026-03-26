---
name: rfp-questions
description: |
  Develops clarifying questions for RFP responses with competitive risk awareness.
  WHEN to use: User mentions RFP questions, Q&A development, proposal clarifications,
  or wants help improving RFP question lists for competitive bidding.
  WHEN NOT to use: General proposal writing, non-RFP questions, internal Q&A.
argument-hint: [client-name]
---

# RFP Question Development Skill

End-to-end workflow for developing clarifying questions for RFP responses with **enforced compliance** and **competitive risk awareness**.

---

## Core Challenge

**RFP Q&A submissions are PUBLIC.** All competitors see every question you ask.

Questions reveal:
- What you don't know
- What you're worried about
- Your strategy and approach
- Your gaps and weaknesses

Large MSPs with 100-200 embedded people already know answers internally. Smaller bidders must use Q&A carefully to gather information without revealing strategy.

---

## Hard Rules

### Compliance Rules

1. **Hooks enforce compliance** - Every phase produces artifacts. Stop hook verifies ALL previous phases complete before progression.

2. **No skipping phases** - The "Check Previous Phases" pattern guarantees workflow compliance.

3. **Marker file scoping** - `.rfp-questions/<client>/.active` ensures hooks only fire for this skill.

### Presentation Rules

4. **Present 3-5 items at a time** - Never dump all findings at once. Always ask "ready to continue?"

5. **Explicit decision recording** - Every human decision must be confirmed back and logged. "Sounds good" is ambiguous.

6. **No pre-filtering** - Present ALL findings. Human decides what matters, not the AI.

7. **Full original text in revisions** - When showing revised questions, show complete original. Never truncate.

### Output Rules

8. **User chooses outputs** - In Phase 6, ASK what formats they want. Don't blindly generate all.

9. **Offer Big4 review** - Before final generation, offer to invoke big4 skill for content polish.

10. **Version control** - Never overwrite question documents. Use `_v01`, `_v02`, then `final_`.

---

## Activation

When this skill is invoked:

1. Create marker file: `.rfp-questions/<client>/.active`
2. This activates skill-scoped hooks
3. Remove marker when workflow completes or user aborts

---

## 7-Phase Workflow

```
Phase 0: DOCUMENT INGESTION (Interactive)
├── Scan source folder for documents
├── Present inventory to user (sizes, types, page counts)
├── Discuss processing strategy per document
├── Process PDFs with Gemini (page-by-page markdown)
├── Process Excel with openpyxl + Gemini (intelligent CSV)
├── NEVER process blindly - always get user consent
└── GATE: ingested/ folder with index.md exists

Phase 1: SETUP
├── Ask user for client name and RFP context
├── Scaffold project folder
├── Verify source documents exist (including ingested/)
├── Initialize state.json
└── GATE: source_verification.md exists

Phase 2: CATALOG & ANALYSIS (Agent Teams - Parallel)
├── Session A: Source verification (Sonnet)
├── Session B: Question cataloging (Sonnet)
├── Session C: Gap analysis (Opus)
├── Session D: Refinement analysis (Opus)
├── Session E: Competitor risk assessment (Opus)
└── GATE: All 5 analysis artifacts exist

Phase 3: INTERACTIVE REVIEW (Coordinator - Sequential)
├── Present gaps 3-5 at a time
├── Present refinements 3-5 at a time
├── Present risk items
├── Record EVERY decision explicitly
└── GATE: review_decisions.md exists

Phase 4: QUALITY CHECKS (Agent Teams - Parallel)
├── Session G: Final holistic risk review (Opus)
├── Session H: Duplication check (Sonnet)
├── Session I: Depth appropriateness check (Sonnet)
└── GATE: All 3 quality artifacts exist

Phase 5: USER APPROVAL
├── Present final question list summary
├── Surface any remaining concerns
├── Get EXPLICIT approval
└── GATE: state.json contains approved: true

Phase 6: DOCUMENT GENERATION (User Choice)
├── ASK user what outputs they want
├── OFFER Big4 skill review
├── Generate selected outputs
├── Remove .active marker
└── GATE: final_questions.md exists
```

---

## Phase 0: Document Ingestion (Detailed)

**This phase runs BEFORE setup when source documents need processing.**

### Step 0.1: Scan Source Folder

```bash
python3 .claude/skills/rfp-questions/scripts/scan_documents.py <session_folder>
```

This produces JSON with:
- File inventory (names, sizes, types)
- Page counts for PDFs
- Sheet info for Excel files
- Processing recommendations

**Present to user:**
> "I found 3 documents in your source folder:
> 1. rfp_document.pdf (2.4 MB, ~45 pages) - Gemini native processing
> 2. integration_list.xlsx (156 KB, 3 sheets) - openpyxl + Gemini
> 3. requirements.png (890 KB) - Gemini vision
>
> Shall I process these? I can do them one at a time or all together."

### Step 0.2: Process Documents (With Consent)

**For PDFs:**
```bash
python3 .claude/skills/rfp-questions/scripts/process_document.py \
  <pdf_path> --output-dir <session>/ingested/<doc_name>/ [--pages 1-10]
```

Options:
- `--pages 1-5,10-15` - Process specific pages
- `--dry-run` - Show what would be processed
- `--model gemini-2.0-flash` - Model selection

**For Excel:**
```bash
python3 .claude/skills/rfp-questions/scripts/process_excel.py \
  <xlsx_path> --output-dir <session>/ingested/<doc_name>/ [--sheets Sheet1]
```

Options:
- `--sheets Sheet1,Sheet2` - Process specific sheets
- `--no-gemini` - Skip AI analysis
- `--dry-run` - Analyze structure only

**For Images:**
```bash
python3 .claude/skills/rfp-questions/scripts/process_document.py \
  <image_path> --output-dir <session>/ingested/<doc_name>/
```

### Step 0.3: Review Ingested Content

After processing, verify with user:
> "I've processed rfp_document.pdf into 45 page files:
> - ingested/rfp_document/index.md (overview)
> - ingested/rfp_document/page_01.md through page_45.md
>
> Want me to show you a sample page to verify quality?"

### Output Structure

```
.rfp-questions/<client>/
├── source/                          # Original documents (user provides)
│   ├── rfp_document.pdf
│   ├── integration_list.xlsx
│   └── requirements.png
└── ingested/                        # Processed documents
    ├── index.md                     # Master inventory
    ├── rfp_document/
    │   ├── index.md
    │   ├── page_01.md
    │   ├── page_02.md
    │   └── ...
    ├── integration_list/
    │   ├── index.md
    │   ├── sheet_data.md
    │   ├── sheet_data.csv
    │   ├── sheet_lookup.md
    │   ├── sheet_lookup.csv
    │   └── relationships.json
    └── requirements/
        ├── index.md
        └── page_01.md
```

### Key Principles

1. **Check size FIRST** - Never blindly process large documents
2. **Get user consent** - Always ask before processing
3. **Page-by-page, not summaries** - Faithful content extraction
4. **Excel intelligence** - Understand relationships, split if needed
5. **Scratchpad experiments** - For tricky documents, create test scripts

### Environment Requirements

```bash
# Required for Gemini processing
export GEMINI_API_KEY="your-api-key"

# Required packages
pip install google-genai openpyxl
```

### Gate

Phase 0 is complete when:
- `ingested/index.md` exists
- User has confirmed ingested content is acceptable
- state.json updated with `ingestion_complete: true`

---

## Phase 1: Setup (Detailed)

### Step 1.1: Gather Context

Ask the user:

> "What client and RFP are we working on? Please provide:
> 1. Client name (for folder naming)
> 2. Brief RFP description
> 3. Your competitive positioning (large bidder, small bidder, incumbent, etc.)
> 4. Where are your source documents?"

### Step 1.2: Scaffold Project

```bash
python3 .claude/skills/rfp-questions/scripts/scaffold_project.py <client-name>
```

This creates:
```
.rfp-questions/<client-name>/
├── .active
├── orchestration/state.json
├── phase_01_setup/
├── phase_02_analysis/
├── phase_03_review/
├── phase_04_quality/
├── phase_05_approval/
└── phase_06_outputs/
```

### Step 1.3: Verify Source Documents

Check that user has provided:
- RFP document (PDF or plaintext)
- Any existing questions
- Supplementary materials (spreadsheets, appendices)

Document in `phase_01_setup/source_verification.md`:
```markdown
# Source Document Verification

## Documents Provided
- [ ] RFP: <path>
- [ ] Existing Questions: <path>
- [ ] Supplementary: <path>

## Readiness
[Ready to proceed / Missing documents]
```

### Step 1.4: Initialize State

```json
{
  "client_name": "...",
  "rfp_name": "...",
  "session_folder": ".rfp-questions/<client>/",
  "current_phase": "setup",
  "completed_phases": [],
  "competitive_context": "...",
  "source_documents": [],
  "agent_mode": "teams"
}
```

---

## Phase 2: Catalog & Analysis

### Agent Teams Mode

Spawn 5 agents in parallel using Agent Teams:

```
Task(subagent_type="rfp-source-verifier", ...)      # Session A
Task(subagent_type="rfp-question-cataloger", ...)   # Session B
Task(subagent_type="rfp-gap-analyzer", ...)         # Session C
Task(subagent_type="rfp-refinement-analyzer", ...)  # Session D
Task(subagent_type="rfp-competitor-assessor", ...)  # Session E
```

Each agent writes to `phase_02_analysis/`:
- `source_verification_report.md` (A)
- `question_catalog_v01.md` (B)
- `gap_analysis.md` (C)
- `refinement_recommendations.md` (D)
- `competitor_risk_assessment.md` (E)

### Handoff Protocol

Every agent handoff includes:
- **Context**: What we're doing, competitive positioning
- **Task**: Exactly what to produce
- **Input Files**: Exact paths to read
- **Output**: Exact path and structure expected
- **Boundaries**: What NOT to do

See `.claude/skills/rfp-questions/references/handoff_templates.md` for complete templates.

### Fallback Mode

If `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` not set:
1. Warn user that Agent Teams is preferred
2. Fall back to sequential subagent execution
3. Wait for each agent to complete before spawning next

---

## Phase 3: Interactive Review

**This is the most critical phase.** The coordinator walks the human through findings.

### Presentation Pattern

```
Coordinator: "Session C found 12 gaps total. Here are the first 3:

1. **Compliance Coverage** (Section 7)
   Suggested: 'Can MGRC provide a calendar of compliance audits...'
   Why We Ask: RFP lists 8 frameworks but only touches PCI.

2. **DR/BCP Details** (Section 4)
   Suggested: 'For critical systems, what are the recovery targets...'
   Why We Ask: Listed as service domain but no details provided.

3. **Documentation State** (Scope of Services)
   Suggested: 'Can MGRC characterize the current state of operational documentation...'
   Why We Ask: Poor documentation means longer KT.

For each: Accept / Modify / Reject / Save for Orals?
Or 'continue' to see more."
```

### Decision Recording

After each decision:

1. Confirm back:
   > "Confirmed: Gap 1 (Compliance) ACCEPTED as Q29. Recording."

2. Update `phase_03_review/review_decisions.md`:
   ```markdown
   | Item | Type | Decision | Notes | Timestamp |
   |------|------|----------|-------|-----------|
   | Gap 1 | Compliance | Accepted | Added as Q29 | 2026-02-23 14:30 |
   ```

3. Update state.json `review_decisions` array

### Progress Tracking

After each batch:
```
"Progress: 5 of 12 gaps reviewed
- 3 accepted as new questions
- 1 modified before accepting
- 1 rejected (save for orals)

7 gaps remaining. Continue?"
```

---

## Phase 4: Quality Checks

Spawn 3 agents in parallel:

```
Task(subagent_type="rfp-final-risk-reviewer", ...)   # Session G
Task(subagent_type="rfp-duplicate-checker", ...)     # Session H
Task(subagent_type="rfp-depth-checker", ...)         # Session I
```

### Session G: Final Risk Review

Reviews the FULL question set as a whole (not individual questions):
- Look for emergent patterns
- Check if multiple questions together reveal more than each alone
- Flag any remaining concerns

### Session H: Duplication Check

- Find semantic duplicates
- Find partial overlaps
- Suggest consolidations

### Session I: Depth Check

- Flag questions too granular for RFP Q&A (save for orals)
- Flag questions too vague (won't get useful answers)
- Suggest simplifications or expansions

---

## Phase 5: User Approval

Present final summary:

```
"We have finalized 36 questions across 6 categories:
- Scope & Transition: 11 questions (6 original, 5 new)
- Evaluation Criteria: 4 questions (2 original, 1 revised, 1 new)
- Staffing: 6 questions (4 original, 2 new)
- Technology: 7 questions (4 original, 3 new)
- Compliance: 1 question (new)
- Commercial: 7 questions (3 original, 2 revised, 2 new)

Quality checks found:
- No concerning patterns (G)
- No duplicates (H)
- 2 questions simplified for appropriate depth (I)

Do you approve this set for document generation?
[Yes / No / Review specific items]"
```

**NEVER assume approval. Wait for explicit "yes", "approved", "proceed".**

---

## Phase 6: Document Generation

### Step 6.1: Ask User What to Generate

```
"What outputs would you like me to generate?

1. **Final Markdown** - Clean question list (always generated)
2. **HTML Review Document** - Professional BayOne design for review/printing
3. **CSV Export** - For spreadsheet import

Select options (e.g., '1, 2' or 'all'): "
```

### Step 6.2: Offer Big4 Review

```
"Would you like me to invoke the **big4 skill** to review and polish
the question phrasing before final generation?

The Big4 skill acts like a Big Four consultant to:
- Prevent misfires in phrasing
- Improve clarity and professionalism
- Catch subtle issues

[Yes / No]"
```

If yes, invoke big4 skill with consolidated questions, then proceed.

### Step 6.3: Generate Outputs

```bash
python3 .claude/skills/rfp-questions/scripts/generate_outputs.py \
  --session-folder .rfp-questions/<client>/ \
  --formats markdown,html,csv
```

Or invoke document-generator agent for complex generation.

### Step 6.4: Cleanup

1. Remove `.active` marker
2. Update state.json: `workflow_complete: true`
3. Inform user where files are located

---

## state.json Schema

Critical fields for context survival:

```json
{
  "client_name": "McGrath",
  "rfp_name": "MSP RFP 2026",
  "session_folder": ".rfp-questions/mcgrath-msp-2026",
  "current_phase": "review",
  "completed_phases": ["ingestion", "setup", "analysis"],
  "ingestion_complete": true,
  "ingested_documents": [
    {"name": "rfp_document.pdf", "pages": 45, "type": "pdf"},
    {"name": "integration_list.xlsx", "sheets": 3, "type": "excel"}
  ],
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
  "review_decisions": [],
  "gaps_reviewed": 12,
  "gaps_accepted": 8,
  "critical_learnings": [
    "Large MSPs have embedded teams who get answers internally"
  ],
  "approved": false,
  "requested_outputs": [],
  "big4_review_requested": false,
  "agent_mode": "teams"
}
```

---

## References

For detailed requirements per phase:
- `.claude/skills/rfp-questions/references/phase_requirements.md`

For agent handoff templates:
- `.claude/skills/rfp-questions/references/handoff_templates.md`

For competitive strategy guidance:
- `.claude/skills/rfp-questions/references/competitive_strategy.md`

For HTML output template:
- `.claude/skills/rfp-questions/references/bayone_html_template.md`

---

## Workflow Completion

When Phase 6 completes:

1. Remove marker file: `.rfp-questions/<client>/.active`
2. Update state.json: `"workflow_complete": true`
3. Inform user: "Documents generated at .rfp-questions/<client>/phase_06_outputs/"

If user aborts mid-workflow:
1. Remove marker file
2. State.json preserves progress for potential resume
3. Partial artifacts remain for reference

---

## Session Start Checklist

Before any work, ALWAYS:

1. **Check for existing session**
   - Look for `.rfp-questions/*/.active` marker
   - If found, offer to resume or start fresh

2. **Ask for context**
   > "Do you have anything to share before we begin? Existing questions, strategic context, concerns?"

3. **Create/verify folder structure**

4. **Create marker file**

5. **Initialize state.json**

6. **Wait for user** before proceeding to analysis
