# RFP Skill Requirements - Captured from McGrath Session

**Date:** February 20, 2026
**Source:** Colin Moore observations during McGrath RFP work

---

## Workflow Pattern (What Worked)

### Multi-Session Architecture
- **Coordinator session** = quarterback, doesn't do deep analysis itself
- **Specialized sessions** = focused tasks with clear boundaries
- Sessions A-H each had single responsibility
- Parallel execution where no dependencies exist

### Session Handoff Protocol
Must include:
1. Context — what we're doing, why it matters
2. Specific task — exactly what to produce
3. Input files — exact paths
4. Output format — where to put results, structure
5. Boundaries — what NOT to do

### Document Organization
- **Session folder** (`claude/<date>_<topic>/`) = working files, planning, tracking
- **Output folder** (`mcgrath/`) = human-readable deliverables
- Keep them separate — don't mix internal tracking with deliverables

### Versioning Approach
- "Blockchain style" — version rather than overwrite
- `v01`, `v02` naming for iterations
- Consolidated docs when synthesizing multiple inputs

---

## Presentation Style (Critical)

### What NOT to Do
- Don't dump walls of text
- Don't batch multiple unrelated decisions
- Don't invent constraints user didn't ask for (e.g., "top 5")
- Don't rush through findings

### What TO Do
- Present one topic at a time
- Wait for user response before moving on
- Let user guide priority and depth
- Be conversational, not report-style
- Ask "want to see X or Y first?"

---

## RFP Question Strategy (Domain Knowledge)

### Core Principle
Ask questions that seem obvious but don't give competitors advantage.

### Competitive Context to Understand
- Larger MSPs have 100-200 people embedded
- They get answers through internal channels, not RFP Q&A
- Smaller bidder (BayOne) is at information disadvantage
- RFP questions are public — all competitors see them

### The Balance
1. Questions that enlighten US for strong proposal
2. Don't reveal our gaps or strategy
3. Look standard/obvious even when strategic
4. If large MSPs already know it, asking levels the field

### Question Assessment Criteria
- "Would a 200-person embedded team already know this?"
- Does this reveal BayOne's strategy or gaps?
- Does this position us well (shows sophistication)?
- Could this expose gaps in competitors' thinking?

### What to Avoid in Questions
- Specific examples that reveal our thinking (e.g., "Salesforce first, then Oracle")
- Pricing preferences that show commercial strategy
- Direct signals of incumbent status
- Questions that imply we lack capability

---

## Session Types Needed for RFP Skill

| Session Type | Purpose | Output |
|--------------|---------|--------|
| PDF Verification | Ensure plaintext extraction is complete | Verification report |
| Question Catalog | Structure existing questions with metadata | Structured catalog |
| Gap Analysis | Find uncovered areas | Gap list with suggested questions |
| Refinement | Improve wording, reduce sensitivity | Revision recommendations |
| Competitor Risk | Assess what questions reveal | Risk assessment |
| Interactive Review | Walk human through findings one-by-one | Decisions document |
| Final Risk Review | Full competitive lens with context | Final clearance |
| Duplication Check | Find overlap/redundancy | Consolidation recommendations |

---

## Artifacts Needed

| Artifact | Purpose | Location |
|----------|---------|----------|
| Question Catalog | Structured view of all questions | `questions/` |
| Gap Decisions | Human decisions on what to add | `questions/` |
| Refinement Decisions | Human decisions on rewording | `questions/` |
| Consolidated Questions | All questions with justifications | `questions/` |
| Final Submission List | Clean version for submission | `questions/` |
| Glossary | Terms, acronyms, people lookup | `knowledge_base/` |
| Risk Assessments | Competitive risk analysis | `analysis/` |
| Progress Tracker | Session status tracking | Session folder |
| Feedback Log | What worked/didn't work | Session folder |

---

## Human Judgment Points (Can't Automate)

1. **Final question selection** — which gaps to fill
2. **Rewording decisions** — accept/modify/reject refinements
3. **Removing questions** — too risky vs valuable
4. **Strategic positioning** — how aggressive to be
5. **Domain expertise input** — AI/automation topics, etc.
6. **Competitor risk tolerance** — what's acceptable to reveal

---

## Errors Made This Session (Anti-Patterns)

1. Dumped synthesis as wall of text instead of incremental
2. Invented "top 5" constraint not requested
3. Didn't read Session G output before summarizing it
4. Didn't track decisions in files as we went (had to backfill)
5. Didn't log skill requirements throughout (doing it now as backfill)
6. Used jargon without explanation ("Big Bang")

---

## Things That Worked Well

1. Parallel session execution (A+B, then C+D+E)
2. Clear handoff documents with boundaries
3. Separate coordinator from worker sessions
4. Session F interactive review (one topic at a time)
5. Colin's strategic insight captured and used in Session G handoff
6. Glossary as reusable knowledge base artifact
7. Consolidated doc with justifications before final clean version

---

## Skill Trigger Phrases

When user says things like:
- "RFP questions"
- "bid response"
- "clarifying questions for RFP"
- "vendor questions"
- "proposal questions"

---

## CRITICAL: File Dependency Tracking

**Issue discovered:** When updating questions after depth check, only updated FINAL_submission_questions.md. Left these out of sync:
- existing_questions.md
- new_questions.md
- all_questions_organized.md
- consolidated_questions_v02.md

**Root cause:** No system to track which files contain the same data and must be updated together.

**Requirements for skill:**
1. **Dependency map** — Track which files contain overlapping content
2. **Update propagation** — When one file changes, identify all related files
3. **Single source of truth** — Consider having ONE canonical source, others generated from it
4. **Sync check** — Before completing a task, verify all related files are in sync

**Possible approaches:**
- Maintain a `file_dependencies.md` that maps relationships
- Use a "source → derived" model where derived docs are regenerated, not edited
- Add checksums or version tags to related sections

---

## Open Questions for Skill Design

1. How to handle different RFP sizes (20 questions vs 100)?
2. Should glossary be auto-generated or human-curated?
3. How to persist competitive context across sessions?
4. Should there be a "question quality score" metric?
5. How to handle RFP-specific domain knowledge (healthcare vs tech vs govt)?
6. **How to track file dependencies and prevent sync drift?**

---

## Additional Feedback (Late Session)

### Missing: "Too Deep in the Weeds" Check
- Some questions may be too specific/granular
- Need a session type that scrutinizes whether questions are appropriately scoped
- Not all questions need to be highly detailed — some should stay high-level

### Missing: RFP Document References
- Each question should cite the specific RFP section/row it relates to
- Helps reviewers understand context
- Original questions doc had this ("MGRC Environment / MGRC Overview", "Specific Requirements / OCI, Row 48")
- This got lost in consolidation — need to preserve it

### Document Organization Issues
- Consolidated doc still hard to scan for new vs existing
- Justifications too short — don't explain enough
- Need multiple views:
  1. **Existing questions only** (with revisions called out at top)
  2. **New questions only**
  3. **Well-organized combined view** (better grouping/formatting)

### Missing: Review of Existing Questions
- We reviewed gaps, refinements, and competitive risk
- But never systematically reviewed the original 20 questions for quality
- Skill should include this as an explicit step

### Depth Appropriateness Findings (Session I)
- 32 of 36 questions were at the right depth
- 4 questions were too granular (Q17, Q19, Q26, Q27)
- **Pattern:** Security/compliance questions asked for audit-level specifics (SAQ type, pen testing frequency, specific certifications)
- **Rule for skill:** Questions about security/compliance should stay high-level in Q&A. Audit details come during due diligence.
- **Simplification principle:** Remove example lists from questions (e.g., "Oracle Fusion certified, Salesforce Admin certified") — makes us look like we're checking boxes

### Depth Calibration by Question Type
| Type | Appropriate Depth |
|------|-------------------|
| Scope/volume questions | Detailed (we need numbers) |
| Evaluation criteria | High-level (just want weights) |
| Commercial/pricing | Open-ended (flexibility, not specifics) |
| Security/compliance | High-level (scope, not audit specifics) |
| Technical architecture | Detailed (we need to staff appropriately) |

### Implication for Skill
- Multiple document outputs, not just one consolidated doc
- RFP references are metadata that must be preserved
- "Depth appropriateness" check is a distinct review type
- Original question review should happen before gap analysis
- Auto-flag questions that include example lists — often too granular
