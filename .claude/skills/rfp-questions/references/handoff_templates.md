# Agent Handoff Templates

This document contains the handoff templates for each worker agent session. Use these templates when spawning agents to ensure consistent, high-quality outputs.

---

## Contents

1. [Session A: Source Verification](#session-a-source-verification)
2. [Session B: Question Cataloging](#session-b-question-cataloging)
3. [Session C: Gap Analysis](#session-c-gap-analysis)
4. [Session D: Refinement Analysis](#session-d-refinement-analysis)
5. [Session E: Competitor Assessment](#session-e-competitor-assessment)
6. [Session G: Final Risk Review](#session-g-final-risk-review)
7. [Session H: Duplication Check](#session-h-duplication-check)
8. [Session I: Depth Check](#session-i-depth-check)
9. [Session J: Document Generation](#session-j-document-generation)

---

## Session A: Source Verification

**Agent:** rfp-source-verifier
**Model:** Sonnet

```
## Context
You are verifying source documents for an RFP question development session.

Client: {client_name}
RFP: {rfp_name}
Session folder: {session_folder}

## Task
1. Read all provided source documents
2. Verify plaintext extraction is complete (no truncation)
3. Identify all sections with page/row references
4. Flag any sections that appear incomplete
5. Create a document map

## Input Files
- RFP: {rfp_path}
- Questions: {questions_path}
- Supplementary: {supplementary_paths}

## Output
Write your findings to:
{session_folder}/phase_02_analysis/source_verification_report.md

Use the format specified in your agent instructions.

## Boundaries
- Do NOT analyze content for gaps (Session C handles that)
- Do NOT evaluate question quality (Session D handles that)
- Only verify document completeness and readability
```

---

## Session B: Question Cataloging

**Agent:** rfp-question-cataloger
**Model:** Sonnet

```
## Context
You are cataloging existing RFP questions with metadata for analysis.

Client: {client_name}
RFP: {rfp_name}
Session folder: {session_folder}

## Task
1. Extract each question from the source document
2. Assign unique ID (Q1, Q2, Q3...)
3. Identify which RFP section each relates to
4. Categorize by topic
5. Note any existing justifications

## Input Files
- Questions document: {questions_path}
- RFP (for section references): {rfp_path}

## Output
Write your findings to:
{session_folder}/phase_02_analysis/question_catalog_v01.md

Use the format specified in your agent instructions.

## Boundaries
- Do NOT evaluate quality (Session D handles that)
- Do NOT suggest changes (Session D handles that)
- Do NOT identify gaps (Session C handles that)
- Catalog ONLY - structure what exists
```

---

## Session C: Gap Analysis

**Agent:** rfp-gap-analyzer
**Model:** Opus

```
## Context
You are identifying gaps in RFP question coverage.

Client: {client_name}
RFP: {rfp_name}
Competitive context: {competitive_context}
Session folder: {session_folder}

## Task
1. Map RFP sections to existing questions
2. Identify sections with ZERO questions (Topic Gaps)
3. Identify questions that could go deeper (Depth Gaps)
4. Identify risks/uncertainties not probed (Risk Gaps)
5. Suggest a question for each gap with justification

## Input Files
- RFP: {rfp_path}
- Question catalog: {session_folder}/phase_02_analysis/question_catalog_v01.md
- Source verification: {session_folder}/phase_02_analysis/source_verification_report.md

## Output
Write your findings to:
{session_folder}/phase_02_analysis/gap_analysis.md

Use the format specified in your agent instructions.

## Boundaries
- Do NOT revise existing questions (Session D handles that)
- Do NOT pre-filter gaps based on importance
- Present ALL gaps found - human decides what to include
```

---

## Session D: Refinement Analysis

**Agent:** rfp-refinement-analyzer
**Model:** Opus

```
## Context
You are reviewing existing questions for competitive risks.

Client: {client_name}
RFP: {rfp_name}
Competitive context: {competitive_context}
Session folder: {session_folder}

CRITICAL: RFP Q&A is PUBLIC. Every question you ask, every competitor sees.
Questions can reveal what you don't know, what you're worried about, and your strategy.

## Task
1. Review each question for competitive signals
2. Flag questions that reveal strategy
3. Flag questions that reveal gaps/weaknesses
4. Flag questions with problematic wording
5. Suggest revised wording where appropriate

## Input Files
- Question catalog: {session_folder}/phase_02_analysis/question_catalog_v01.md
- RFP: {rfp_path}

## Output
Write your findings to:
{session_folder}/phase_02_analysis/refinement_recommendations.md

Use the format specified in your agent instructions.

## Boundaries
- Focus on competitive risk, NOT content quality
- Do NOT add new questions (Session C handles gaps)
- For each flagged question, ALWAYS provide full original text
```

---

## Session E: Competitor Assessment

**Agent:** rfp-competitor-assessor
**Model:** Opus

```
## Context
You are evaluating the FULL question set from a competitor's perspective.

Client: {client_name}
RFP: {rfp_name}
Competitive context: {competitive_context}
Session folder: {session_folder}

Imagine you are a competitor reviewing our Q&A submission.
What would you learn about us?

## Task
1. Review full question set from competitor perspective
2. Identify patterns that reveal strategy
3. Identify questions that expose weaknesses
4. Assign risk levels (Low/Medium/High)
5. Recommend keep/modify/remove for flagged items

## Input Files
- Question catalog: {session_folder}/phase_02_analysis/question_catalog_v01.md
- Refinement analysis: {session_folder}/phase_02_analysis/refinement_recommendations.md
- Gap analysis: {session_folder}/phase_02_analysis/gap_analysis.md

## Output
Write your findings to:
{session_folder}/phase_02_analysis/competitor_risk_assessment.md

Use the format specified in your agent instructions.

## Boundaries
- This is a HOLISTIC review - look at the full set, not just individual questions
- Focus on what competitors would INFER
- Consider patterns across multiple questions
```

---

## Session G: Final Risk Review

**Agent:** rfp-final-risk-reviewer
**Model:** Opus

```
## Context
You are performing a final holistic review AFTER human decisions have been made.

Client: {client_name}
RFP: {rfp_name}
Session folder: {session_folder}

By this point:
- Gaps have been reviewed and some accepted as new questions
- Refinements have been reviewed and some questions revised
- Removals have been decided
- The consolidated question list reflects all decisions

## Task
1. Review the FULL updated question set as a whole
2. Look for emergent patterns that weren't visible before
3. Check if multiple questions together reveal more than each alone
4. Flag any remaining concerns
5. Provide final risk assessment

## Input Files
- Consolidated questions: {session_folder}/phase_03_review/consolidated_questions_v02.md
- Review decisions: {session_folder}/phase_03_review/review_decisions.md
- Original competitor assessment: {session_folder}/phase_02_analysis/competitor_risk_assessment.md

## Output
Write your findings to:
{session_folder}/phase_04_quality/final_risk_review.md

Use the format specified in your agent instructions.

## Boundaries
- Do NOT re-litigate individual decisions from Phase 3
- Focus on emergent patterns from the COMBINATION of changes
- Be concise - this is a final check, not a deep dive
```

---

## Session H: Duplication Check

**Agent:** rfp-duplicate-checker
**Model:** Sonnet

```
## Context
You are checking for duplicate or overlapping questions.

Client: {client_name}
Session folder: {session_folder}

## Task
1. Compare each question against all others
2. Identify semantic duplicates (same question, different wording)
3. Identify partial overlaps (one question subsumes another)
4. Suggest consolidations where appropriate

## Input Files
- Consolidated questions: {session_folder}/phase_03_review/consolidated_questions_v02.md

## Output
Write your findings to:
{session_folder}/phase_04_quality/duplication_check.md

Use the format specified in your agent instructions.

## Boundaries
- Flag duplicates ONLY - do NOT remove questions
- A question that BUILDS ON another is NOT a duplicate
- Different dimensions of the same topic are NOT duplicates
```

---

## Session I: Depth Check

**Agent:** rfp-depth-checker
**Model:** Sonnet

```
## Context
You are checking questions for appropriate depth level.

Client: {client_name}
Session folder: {session_folder}

RFP Q&A has a specific purpose:
- Clarify RFP ambiguities
- Gather information for accurate pricing
- Level the playing field

Questions that are too detailed belong in oral presentations.
Questions that are too vague won't elicit useful responses.

## Task
1. Review each question for appropriate depth
2. Flag questions too granular for RFP Q&A
3. Flag questions too vague to get useful answers
4. Suggest simplifications or expansions where needed

## Input Files
- Consolidated questions: {session_folder}/phase_03_review/consolidated_questions_v02.md

## Output
Write your findings to:
{session_folder}/phase_04_quality/depth_check.md

Use the format specified in your agent instructions.

## Boundaries
- Focus on DEPTH appropriateness, not content quality or risk
- Suggest specific rewording, not just "simplify"
- When simplifying, preserve the core information need
```

---

## Session J: Document Generation

**Agent:** rfp-document-generator
**Model:** Opus

```
## Context
You are generating final deliverables for the completed question set.

Client: {client_name}
RFP: {rfp_name}
Session folder: {session_folder}
Requested formats: {formats}  # e.g., ["markdown", "html", "csv"]

## Task
1. Read the final consolidated question list
2. Read all review decisions and metadata
3. Generate requested output formats

## Input Files
- Consolidated questions: {session_folder}/phase_03_review/consolidated_questions_v02.md
- State: {session_folder}/orchestration/state.json
- Review decisions: {session_folder}/phase_03_review/review_decisions.md

## Output
Write outputs to:
- {session_folder}/phase_06_outputs/final_questions.md (always)
- {session_folder}/phase_06_outputs/rfp_questions_review.html (if html requested)
- {session_folder}/phase_06_outputs/rfp_questions.csv (if csv requested)

Use the formats specified in your agent instructions and the HTML template
in references/bayone_html_template.md.

## Boundaries
- Generate ONLY the formats requested by user
- Follow templates exactly - do not improvise styling
- Include ALL questions from the consolidated list
- Ensure HTML is print-ready at 8.5" x 11"
```
