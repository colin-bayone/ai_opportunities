
```

**Decision Recording:** After each human decision, record in `decisions/review_decisions.md`:
```markdown
| Item | Decision | Rationale | Timestamp |
|------|----------|-----------|-----------|
| Q13 Revision | Accepted | Removes strategic signal | 2026-02-23 14:30 |
```

---

### Session G: Final Risk Review

**Purpose:** Re-evaluate the complete question set after human decisions, looking for patterns across the full set.

**Inputs:**
- Updated question list (incorporating all decisions from Session F)
- Original competitor risk assessment (from Session E)
- Decision log (from Session F)

**Tasks:**
1. Review the FULL question set as a whole (not individual questions)
2. Look for emergent patterns that weren't visible in individual review
3. Check if multiple questions together reveal more than each alone
4. Flag any remaining concerns
5. Provide final risk assessment

**Output:** `analysis/final_risk_review.md`
```markdown
## Final Risk Review

### Overall Assessment
[Low/Medium/High] - [Summary]

### Pattern Analysis
- No concerning patterns detected
- OR: Questions Q3, Q9, Q15 together reveal timeline concerns

### Remaining Concerns
[List any items that should be reconsidered]

### Recommendation
Proceed with submission / Recommend additional review of [specific items]
```

**Boundaries:** This is a holistic review. Do NOT re-litigate individual decisions from Session F.

---

### Session H: Duplication Check

**Purpose:** Identify questions that overlap or could be consolidated.

**Inputs:**
- Final question list (after Session F decisions)

**Tasks:**
1. Compare each question against all others
2. Identify semantic duplicates (same question, different wording)
3. Identify partial overlaps (one question subsumes another)
4. Suggest consolidations where appropriate

**Output:** `analysis/duplication_check.md`
```markdown
## Duplication Check

### Duplicates Found
| Question A | Question B | Overlap Type | Recommendation |
|------------|------------|--------------|----------------|
| Q7 | Q11 | Partial | Consolidate into Q7 |

### Consolidation Suggestions
[Specific wording for consolidated questions]

### Clean List
[No duplicates found / X duplicates identified]
```

**Boundaries:** Flag duplicates only. Do NOT remove questions without human approval.

---

### Session I: Depth Appropriateness Check

**Purpose:** Ensure questions are appropriately detailed for an RFP Q&A context.

**Inputs:**
- Final question list
- RFP document (to understand complexity of topics)

**Tasks:**
1. Review each question for appropriate depth
2. Flag questions that are too granular (should be asked in orals/follow-up)
3. Flag questions that are too vague (won't get useful answers)
4. Suggest simplifications or expansions where needed

**Output:** `analysis/depth_check.md`
```markdown
## Depth Appropriateness Check

### Too Granular (Save for Orals)
| Question | Issue | Recommendation |
|----------|-------|----------------|
| Q14 | Asks for specific hourly breakdown | Simplify to "general staffing approach" |

### Too Vague (Won't Get Useful Answer)
| Question | Issue | Recommendation |
|----------|-------|----------------|
| Q22 | "Tell us about your environment" | Add specific aspects to address |

### Appropriate Depth
[X of Y questions are appropriately scoped]
```

**Boundaries:** Focus on RFP context appropriateness. Do NOT evaluate strategic value (Session D/E handle that).

---

### Session J: Document Generation

**Purpose:** Produce final deliverables in multiple formats.

**Inputs:**
- Final approved question list
- All analysis documents
- Decision log

**Tasks:**
1. Generate final markdown document with all questions
2. Generate HTML version (following BayOne design spec)
3. Generate CSV for spreadsheet import
4. Generate summary statistics

**Outputs:**

1. `questions/final_questions.md` - Clean list for submission
2. `questions/rfp_questions_review.html` - Formatted HTML for review
3. `questions/rfp_questions.csv` - CSV export
4. `questions/submission_summary.md` - Statistics and notes

**HTML Requirements:**
- Follow BayOne design spec (purple gradient, Inter font)
- Include cover page with RFP name, date, question count
- Table format with columns: #, Type, Section, Question, RFP Reference, Justification
- Print-optimized for 8.5" x 11"

**CSV Requirements:**
- Headers: #, Type, Section, Question, RFP Reference, RFP Location, Justification
- Properly escaped for Excel/Google Sheets import

---

## Part 3: Presentation and Interaction Guidelines

### 3.1 Incremental Presentation

**Core Principle:** Never dump large amounts of information on the human at once.

**Rules:**
1. Present findings in digestible chunks (3-5 items max per batch)
2. Always ask "ready to continue?" or "want to see more?"
3. Offer navigation choices ("gaps next, or refinements?")
4. Summarize before diving into details

**Good Example:**
```
"I found 12 gaps total. Here are the 3 highest-priority ones:
[Shows 3 gaps]
Want to review these before seeing the rest?"
```

**Bad Example:**
```
"Here are all 12 gaps I found:
[Dumps all 12 gaps at once]"
```

### 3.2 Decision Confirmation

**Every decision must be explicitly confirmed:**

```
Human: "Accept that revision"
Coordinator: "Confirmed: Q13 revised to remove specific split example.
             Recording decision. Next item?"
```

**Never assume:**
- Silence means approval
- "Sounds good" means "implement it"
- Partial feedback means full approval

### 3.3 Progress Tracking

**Maintain visible progress throughout:**

```
"Progress: 4 of 12 gaps reviewed
- 2 accepted as new questions
- 1 modified before accepting
- 1 rejected (save for orals)

8 gaps remaining. Continue?"
```

### 3.4 Error Recovery

**If human seems confused or frustrated:**
1. Stop current flow
2. Summarize where we are
3. Offer to restart section or skip ahead
4. Never argue or over-explain

---

## Part 4: File Management and Dependencies

### 4.1 Directory Structure

```
project_root/
├── source/
│   ├── rfp_original.pdf
│   ├── rfp_plaintext.md
│   ├── integration_list.xlsx
│   └── strategic_intel.md
├── questions/
│   ├── question_catalog_v01.md
│   ├── consolidated_questions_v01.md
│   ├── consolidated_questions_v02.md  (after revisions)
│   ├── final_questions.md
│   ├── rfp_questions_review.html
│   └── rfp_questions.csv
├── analysis/
│   ├── source_verification_report.md
│   ├── gap_analysis.md
│   ├── refinement_recommendations.md
│   ├── competitor_risk_assessment.md
│   ├── final_risk_review.md
│   ├── duplication_check.md
│   └── depth_check.md
├── decisions/
│   ├── review_decisions.md
│   └── session_log.md
└── knowledge_base/
    └── glossary.md
```

### 4.2 Version Control

**Question documents use version suffixes:**
- `_v01` = Initial catalog
- `_v02` = After gap additions
- `_v03` = After refinements
- `final_` = Approved for submission

**Never overwrite without versioning.** If human wants to go back, previous versions must exist.

### 4.3 Dependency Chain

```
source/rfp_plaintext.md
        ↓
    Session A (verify) + Session B (catalog)
        ↓
    questions/question_catalog_v01.md
        ↓
    Session C (gaps) + Session D (refinements) + Session E (risk)
        ↓
    analysis/*.md files
        ↓
    Session F (human review)
        ↓
    questions/consolidated_questions_v02.md + decisions/review_decisions.md
        ↓
    Session G (final risk) + Session H (duplicates) + Session I (depth)
        ↓
    analysis/final_*.md files
        ↓
    Session J (document generation)
        ↓
    questions/final_questions.md + .html + .csv
```

---

## Part 5: Output Formats

### 5.1 Markdown Format

```markdown
## RFP Clarifying Questions - [Client Name]

**Prepared by:** [Company]
**Date:** [Date]
**Total Questions:** [Count]

---

### Section 1: Scope & Transition Planning

#### Q1
**Question:** [Full text]
**Type:** Original | New | Revised
**RFP Reference:** [Section] / [Subsection]
**RFP Location:** [Page/Row]
**Justification:** [Why we ask this]

---
```

### 5.2 HTML Format

Follow BayOne design spec:
- Purple gradient cover (#2e1065 to #6d28d9)
- Inter font family
- Table with sticky headers
- Print margins for 8.5" x 11"
- No emojis

### 5.3 CSV Format

```csv
"#","Type","Section","Question","RFP Reference","RFP Location","Justification"
"1","Original","Scope & Transition","[Question text]","MGRC Environment","Page 12","[Justification]"
```

---

## Part 6: Anti-Patterns and Errors to Avoid

### 6.1 Workflow Anti-Patterns

| Anti-Pattern | Why It's Bad | Correct Approach |
|--------------|--------------|------------------|
| Coordinator does deep analysis | Loses focus, fills context | Delegate to worker sessions |
| Batching unrelated decisions | Overwhelms human | One topic at a time |
| Pre-filtering gaps | Human can't see what was excluded | Present ALL, let human filter |
| Assuming approval | Decisions not recorded | Explicit confirmation always |
| Overwriting files | Can't recover previous state | Version everything |

### 6.2 Question Development Anti-Patterns

| Anti-Pattern | Example | Why It's Bad |
|--------------|---------|--------------|
| Revealing strategy | "We're concerned about timeline..." | Competitors see this |
| Specific examples | "...one MSP for Salesforce, another for Oracle..." | Shows your thinking |
| Aggressive positioning | "How will incumbent knowledge be weighted?" | Signals desperation |
| Compound questions | "What is X and also Y and how does Z?" | Won't get clear answer |
| Questions answered in RFP | Asking about something clearly stated | Looks like you didn't read it |

### 6.3 Session Handoff Anti-Patterns

| Anti-Pattern | Why It's Bad | Correct Approach |
|--------------|--------------|------------------|
| Vague task description | Worker doesn't know what to produce | Specific task + output format |
| Missing file paths | Worker can't find inputs | Exact paths always |
| No boundaries | Worker does too much or too little | Explicit "do NOT" list |
| Missing context | Worker makes wrong assumptions | Include strategic context |

---

## Part 7: Domain Knowledge - RFP Strategy

### 7.1 The Public Q&A Challenge

**Key insight:** RFP Q&A submissions are typically published to ALL bidders. Every question you ask, every competitor sees.

**Implications:**
- Questions reveal what you don't know
- Questions reveal what you're worried about
- Questions reveal your strategy
- Sophisticated competitors analyze your questions

### 7.2 Large vs. Small Bidder Dynamics

**Large MSPs (100-200 embedded people):**
- Already know answers from internal relationships
- Use Q&A to clarify minor points
- Don't reveal strategy because they don't need to ask

**Small/Mid-size Bidders:**
- Need Q&A to gather critical information
- Every question is a calculated risk
- Must get information without revealing gaps

### 7.3 Question Categories by Risk

| Category | Risk Level | Notes |
|----------|------------|-------|
| Standard operational questions | Low | "What's the ticket volume?" - everyone asks |
| Clarification on RFP text | Low | "Section 3.2 says X, can you confirm?" |
| Process questions | Low | "What's the evaluation timeline?" |
| Staffing/resource questions | Medium | Could reveal your model |
| Commercial/pricing questions | Medium-High | Could reveal your strategy |
| Capability questions | High | "Do you require X?" reveals you lack X |
| Strategic questions | High | "Are you open to Y?" reveals your preference |

### 7.4 Neutralizing Techniques

**Instead of:** "We're concerned about the aggressive timeline..."
**Ask:** "Is there flexibility in the go-live date based on transition complexity?"

**Instead of:** "We don't have Oracle Fusion expertise..."
**Ask:** "What level of Oracle Fusion certification is required vs. preferred?"

**Instead of:** "We want to split the work with a partner..."
**Ask:** "Does MGRC have a preference between single-provider and multi-provider models?"

---

## Part 8: Glossary of Terms

| Term | Definition |
|------|------------|
| **Coordinator Session** | The main Claude session that orchestrates workflow and interacts with the human |
| **Worker Session** | A focused sub-session that performs a specific analysis task |
| **Handoff** | The structured information passed from coordinator to worker |
| **Gap Analysis** | Identifying RFP areas not covered by existing questions |
| **Refinement** | Improving existing questions (usually for competitive safety) |
| **Competitive Signal** | Information revealed to competitors through questions |
| **Topic Gap** | An RFP section with zero questions |
| **Depth Gap** | A question that could probe deeper |
| **Risk Gap** | An uncertainty or risk not addressed by any question |

---

## Appendix A: Example Handoff Templates

### Gap Analysis Handoff
```
CONTEXT: We're preparing RFP questions for [Client] [Opportunity].
[Company] is a [size] bidder competing against [competitor context].

TASK: Analyze the existing questions and identify gaps in RFP coverage.
For each gap found, suggest a question.

INPUT FILES:
- RFP: /path/to/rfp_plaintext.md
- Questions: /path/to/question_catalog_v01.md
- Intel: /path/to/strategic_intel.md (if exists)

OUTPUT: Create /path/to/analysis/gap_analysis.md with sections:
- Topic Gaps (RFP sections with no questions)
- Depth Gaps (questions that could go deeper)
- Risk Gaps (uncertainties not probed)

FORMAT: Use tables with columns: Gap | RFP Section | Suggested Question | Why We Ask

BOUNDARIES:
- Do NOT revise existing questions (Session D handles that)
- Do NOT pre-filter gaps based on importance
- Present ALL gaps found - human decides what to include
- Do NOT make strategic judgments about competitors
```

### Refinement Analysis Handoff
```
CONTEXT: We're preparing RFP questions for [Client] [Opportunity].
[Company] is a [size] bidder. Questions are PUBLIC - all competitors see them.

TASK: Review existing questions for competitive risks and suggest refinements.

INPUT FILES:
- Questions: /path/to/question_catalog_v01.md
- Intel: /path/to/strategic_intel.md (if exists)

OUTPUT: Create /path/to/analysis/refinement_recommendations.md with sections:
- Questions Requiring Revision (with original, issue, suggested, risk level)
- Questions to Consider Removing (with original, issue, recommendation)

BOUNDARIES:
- Focus on competitive risk, NOT content quality
- Do NOT evaluate whether questions are good/useful
- Do NOT add new questions (Session C handles that)
- Flag ALL concerns - human decides what to act on
```

---

## Appendix B: Decision Log Template

```markdown
# RFP Question Review - Decision Log

**Project:** [Client] [Opportunity]
**Reviewer:** [Name]
**Date:** [Date]

## Session Summary
| Category | Reviewed | Accepted | Modified | Rejected |
|----------|----------|----------|----------|----------|
| Gaps | 12 | 8 | 2 | 2 |
| Refinements | 4 | 3 | 1 | 0 |
| Removals | 2 | 1 | 0 | 1 |

## Detailed Decisions

### Gap Decisions
| ID | Gap | Decision | Notes |
|----|-----|----------|-------|
| G1 | Compliance coverage | Accepted | Added as Q29 |
| G2 | DR/BCP details | Modified | Simplified wording |
| G3 | Audit frequency | Rejected | Save for orals |

### Refinement Decisions
| ID | Question | Decision | Notes |
|----|----------|----------|-------|
| R1 | Q13 (Multi-MSP) | Accepted | Removed specific example |
| R2 | Q31 (Pricing model) | Modified | Further neutralized |

### Removal Decisions
| ID | Question | Decision | Notes |
|----|----------|----------|-------|
| X1 | Q9 (Incumbent advantage) | Accepted | Too aggressive |
| X2 | Q15 (Timeline concern) | Rejected | Keep but modify |
```

---

*End of RFP Question Development Skill Requirements v2.0*
