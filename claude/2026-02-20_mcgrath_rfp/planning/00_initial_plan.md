# McGrath RFP Response - Initial Plan

**Session:** 2026-02-20
**Lead:** Colin Moore (Director of AI, BayOne Solutions)
**Coordinator Session:** This one (quarterback)

---

## Project Objective

BayOne Solutions is responding to McGrath RentCorp's Managed Services Provider RFP. Goal: Win the contract by positioning BayOne as a strategic partner (not just a staffing vendor) with insider advantage (5 embedded resources).

---

## Source Documents

| Document | Content | Status |
|----------|---------|--------|
| MacgrathSummary 1.pdf | Strategic intel from contractor calls + Mae Roberts notes | Plaintext extracted |
| McGrath RFP Analysis BayOne.pdf | Neha's comprehensive analysis (timeline, SWOT, strategies) | Plaintext extracted |
| McGrath RFP Questions BayOne.pdf | 20 draft questions with internal rationale | Plaintext extracted |

**PDF Verification Needed:** Confirm plaintext captures all content (graphics, tables, formatting)

---

## RFP Question Strategy (Critical Constraints)

1. **Don't reveal strategy to competitors** - Questions are public; competitors read them too
2. **Position as knowledgeable partner** - Better questions = better partner signal
3. **Balance specificity** - Not too vague (looks uninformed), not too specific (reveals approach)
4. **Colin reviews all questions** - This balance requires human judgment

---

## Coordination Model

```
┌─────────────────────────────────────┐
│  This Session (Quarterback)         │
│  - Coordinates work                 │
│  - Reviews outputs                  │
│  - Makes decisions with Colin       │
│  - Synthesizes into final outputs   │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┬──────────────┬──────────────┐
    ▼          ▼          ▼              ▼              ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────────┐ ┌────────────┐
│Session │ │Session │ │Session │ │  Session   │ │  Session   │
│   A    │ │   B    │ │   C    │ │     D      │ │     E      │
│PDF     │ │Question│ │Gap     │ │  Refine    │ │ Competitor │
│Verify  │ │Catalog │ │Analysis│ │  Improve   │ │   Risk     │
└────────┘ └────────┘ └────────┘ └────────────┘ └────────────┘
```

---

## Phased Approach

### Phase 1: Foundation (Current)
- [x] Create session structure
- [x] Create output folder structure
- [ ] Verify PDF→plaintext completeness (Session A)
- [ ] Catalog existing questions in structured format (Session B)
- [ ] Build initial knowledge base

### Phase 2: Analysis
- [ ] Gap analysis - what questions haven't we asked? (Session C)
- [ ] Refine/improve existing questions (Session D)
- [ ] Competitor risk assessment - which questions reveal too much? (Session E)

### Phase 3: Synthesis
- [ ] Colin review of all analysis
- [ ] Finalize question list
- [ ] Prepare submission-ready document

### Phase 4: Skill Development
- [ ] Document workflow patterns that worked
- [ ] Capture feedback (positive/negative) throughout
- [ ] Design reusable RFP skill

---

## Knowledge Base Strategy (Blockchain Style)

**Principle:** Version rather than overwrite. Each knowledge base snapshot is a point-in-time record.

**Location:** `mcgrath/knowledge_base/`

**Naming Convention:**
- `kb_v01_<date>_<description>.md` - Initial version
- `kb_v02_<date>_<description>.md` - After new info integrated
- etc.

**Current State File:** `mcgrath/knowledge_base/CURRENT.md` - Always points to latest version

---

## Output Locations

| Type | Location | Purpose |
|------|----------|---------|
| Working files | `claude/2026-02-20_mcgrath_rfp/` | Planning, progress, decisions |
| Handoff prompts | `claude/2026-02-20_mcgrath_rfp/handoffs/` | Instructions for other sessions |
| Knowledge base | `mcgrath/knowledge_base/` | Versioned reference docs |
| Questions | `mcgrath/questions/` | RFP question iterations |
| Analysis | `mcgrath/analysis/` | Gap analysis, competitor risk, etc. |

---

## Session Handoff Protocol

Each handoff prompt must include:
1. **Context** - What we're doing, why it matters
2. **Specific task** - Exactly what this session should produce
3. **Input files** - Exactly which files to read
4. **Output format** - Where to put results, how to structure them
5. **Boundaries** - What NOT to do (stay focused)

---

## Feedback Tracking (For Skill Development)

Location: `claude/2026-02-20_mcgrath_rfp/issues_and_improvements/`

Track:
- What worked well (patterns to encode in skill)
- What didn't work (anti-patterns to avoid)
- Where human judgment was essential (can't automate)
- Coordination friction points
