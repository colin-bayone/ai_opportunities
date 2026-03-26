# RFP Question Development Skill — Builder Handoff

**Date:** February 23, 2026
**From:** Colin Moore / Claude session
**To:** Claude session building the skill
**Purpose:** Everything you need to build the RFP Question Development skill

---

## Quick Start

1. **Read the requirements doc first:** `01_skill_requirements_v2.md` in this same folder
2. **Understand the core challenge:** RFP Q&A is public - competitors see every question
3. **Key architecture:** Coordinator + Worker sessions (not one monolithic flow)

---

## What This Skill Does

Helps consulting teams develop clarifying questions for RFP responses. The workflow:

1. Verify source documents are complete
2. Catalog existing questions with metadata
3. Identify gaps in RFP coverage
4. Review questions for competitive risks
5. Walk human through findings one-by-one
6. Run quality checks (duplicates, depth)
7. Generate outputs (markdown, HTML, CSV)

---

## Critical Design Decisions Already Made

### 1. Multi-Session Architecture
**Decision:** Use coordinator + worker sessions, NOT a single long session.
**Why:** The coordinator maintains human relationship. Workers do focused tasks without context overhead.
**Implementation:** Use Task tool to spawn workers with structured handoffs.

### 2. Incremental Presentation
**Decision:** Present findings 3-5 items at a time, never dump everything.
**Why:** Humans get overwhelmed. Quality decisions require focus.
**Implementation:** Always ask "ready to continue?" before showing more.

### 3. Explicit Decision Recording
**Decision:** Every human decision must be explicitly confirmed and logged.
**Why:** "Sounds good" is ambiguous. Need clear audit trail.
**Implementation:** Confirm back, then write to decisions file.

### 4. No Pre-Filtering
**Decision:** Worker sessions present ALL findings. Human decides what matters.
**Why:** If AI pre-filters, human can't see what was excluded.
**Implementation:** Boundaries in handoffs say "present ALL, do NOT filter."

### 5. File Versioning
**Decision:** Never overwrite question documents. Use version suffixes.
**Why:** Human may want to go back. Need recovery path.
**Implementation:** `_v01`, `_v02`, `_v03`, then `final_`.

---

## The 10 Sessions Explained

| Session | Type | Purpose | Runs When |
|---------|------|---------|-----------|
| A | Worker | Verify source docs complete | Phase 1 (parallel with B) |
| B | Worker | Catalog questions with metadata | Phase 1 (parallel with A) |
| C | Worker | Find gaps in RFP coverage | Phase 2 (after A+B) |
| D | Worker | Find competitive risks in questions | Phase 2 (parallel with C, E) |
| E | Worker | Assess full set from competitor view | Phase 2 (parallel with C, D) |
| F | Coordinator | Interactive review with human | Phase 3 (sequential) |
| G | Worker | Final holistic risk review | Phase 4 (after F) |
| H | Worker | Check for duplicate questions | Phase 4 (parallel with G, I) |
| I | Worker | Check question depth appropriate | Phase 4 (parallel with G, H) |
| J | Worker | Generate HTML, CSV, final markdown | Phase 5 (last) |

---

## Handoff Template

Every worker session needs this structure:

```
CONTEXT: [What we're doing, why it matters, competitive positioning]

TASK: [Exactly what to produce]

INPUT FILES:
- [Exact path 1]
- [Exact path 2]

OUTPUT: [Exact path and expected structure]

FORMAT: [Tables, sections, etc.]

BOUNDARIES:
- Do NOT [thing they shouldn't do]
- Do NOT [another thing]
- Present ALL [findings] - human decides
```

See Appendix A in the requirements doc for complete examples.

---

## File Structure to Create

```
project_root/
├── source/           # User provides these
├── questions/        # Skill creates/updates these
├── analysis/         # Worker session outputs
├── decisions/        # Human decision log
└── knowledge_base/   # Glossary, reference
```

---

## Key Learnings from the McGrath Session

These are things we discovered while actually doing this work:

### 1. Question Simplification
Some questions were too detailed for RFP Q&A. We had a "depth check" pass that identified 4 questions to simplify. This became Session I.

### 2. Revision Notes Matter
When showing revised questions, always show the FULL original text. Truncating the original frustrated the human because they couldn't compare properly.

### 3. Justification Clarity
Internal justifications ("Critical for cost modeling") are different from what you'd show the client. The skill tracks both but only exports the appropriate version.

### 4. HTML Output Requirements
The human wanted Big Four consulting quality. This means:
- Professional design (BayOne spec: purple gradient, Inter font)
- Print-optimized for 8.5" x 11"
- No emojis, no excessive formatting
- Table headers must be consistent (we had a CSS bug where column classes overrode header styles)

### 5. Multiple Sync Points
We had 5 different question documents that needed to stay in sync. Any update required updating all 5. The skill should track document dependencies and prompt for sync.

---

## Anti-Patterns We Hit

| What Happened | Why It Was Bad | How to Avoid |
|---------------|----------------|--------------|
| Dumped 12 gaps at once | Human overwhelmed | Batch 3-5, ask to continue |
| Truncated original questions | Human couldn't compare | Always show full text |
| CSS class specificity bug | Headers looked wrong | Test HTML output carefully |
| Assumed "sounds good" meant approval | Decision not recorded | Always confirm explicitly |
| Forgot to update one of 5 docs | Documents drifted | Track dependencies |

---

## Testing the Skill

### Minimum Viable Test
1. Give it an RFP document and 5-10 existing questions
2. Verify it catalogs questions correctly
3. Verify it identifies at least one gap
4. Verify it presents findings incrementally
5. Verify it records a decision when human approves something

### Full Test
1. Complete workflow from source verification to HTML output
2. Verify all file dependencies are tracked
3. Verify version control works (can recover previous state)
4. Verify HTML meets design spec
5. Verify CSV imports cleanly to Excel/Sheets

---

## Reference Files

In the McGrath project, you can find:

| File | What It Shows |
|------|---------------|
| `questions/rfp_questions.csv` | Final CSV output format |
| `questions/rfp_questions_review.html` | Final HTML output (BayOne design) |
| `knowledge_base/glossary.md` | Example glossary structure |

These are real outputs from the McGrath session and show the expected quality level.

---

## Questions the Skill Should Handle

The skill should be able to handle these user requests:

- "I have an RFP and some draft questions, help me improve them"
- "Review these questions for competitive risk"
- "What gaps do we have in our question coverage?"
- "Generate an HTML version of the questions"
- "Export the questions as CSV"
- "I want to revise Q13, show me the options"
- "Go back to the previous version of the questions"

---

## What Success Looks Like

A successful skill will:

1. **Not overwhelm the human** - Incremental presentation, clear navigation
2. **Maintain strategic awareness** - Every output considers competitor visibility
3. **Track everything** - Decisions, versions, dependencies
4. **Produce professional outputs** - HTML that looks like Big Four quality
5. **Be recoverable** - Human can always go back to previous state

---

## Final Notes

The requirements document (`01_skill_requirements_v2.md`) is comprehensive. This handoff document is meant to give you the "why" behind the decisions and the practical learnings from actually doing this work.

The McGrath RFP session took multiple hours with many iterations. The skill should make this a 30-60 minute process for future RFPs.

Good luck building it.

---

*End of Handoff Document*
