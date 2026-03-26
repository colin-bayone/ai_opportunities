# RFP Questions Skill - Complete Architecture

**Date:** February 23, 2026
**Status:** APPROVED - Ready for generation

---

## Skill Identity

```yaml
name: rfp-questions
description: |
  Develops clarifying questions for RFP responses with competitive risk awareness.
  WHEN to use: User mentions RFP questions, Q&A development, proposal clarifications,
  or wants help improving RFP question lists for competitive bidding.
  WHEN NOT to use: General proposal writing, non-RFP questions, internal Q&A.
argument-hint: [client-name]
```

---

## File Structure

```
.claude/skills/rfp-questions/
├── SKILL.md                              # Coordinator workflow (~400 lines)
├── scripts/
│   ├── scaffold_project.py               # Create folder structure
│   ├── check_previous_phases.py          # Verification logic (used by hook)
│   └── generate_outputs.py               # HTML/CSV/Markdown generation
└── references/
    ├── phase_requirements.md             # Required artifacts per phase
    ├── handoff_templates.md              # Session A-J handoff templates
    ├── competitive_strategy.md           # Domain knowledge on RFP Q&A risks
    └── bayone_html_template.md           # HTML/CSS design spec for output

.claude/agents/
├── rfp-source-verifier.md                # Session A (Sonnet)
├── rfp-question-cataloger.md             # Session B (Sonnet)
├── rfp-gap-analyzer.md                   # Session C (Opus)
├── rfp-refinement-analyzer.md            # Session D (Opus)
├── rfp-competitor-assessor.md            # Session E (Opus)
├── rfp-final-risk-reviewer.md            # Session G (Opus)
├── rfp-duplicate-checker.md              # Session H (Sonnet)
├── rfp-depth-checker.md                  # Session I (Sonnet)
└── rfp-document-generator.md             # Session J (Opus)

.claude/hooks/
└── rfp-questions-compliance.py           # Stop hook - Check Previous Phases
```

---

## 6-Phase Workflow

### Phase 1: SETUP

**Actions:**
1. Ask user for client name and RFP context
2. Scaffold project folder via script
3. Verify source documents exist (user provides)
4. Initialize state.json
5. Create `.active` marker file

**Gate:** `phase_01_setup/source_verification.md` exists

### Phase 2: CATALOG & ANALYSIS (Agent Teams - Parallel)

**Agents spawned:**
| Agent | Session | Model | Task |
|-------|---------|-------|------|
| source-verifier | A | Sonnet | Verify PDFs/docs complete, create document map |
| question-cataloger | B | Sonnet | Extract questions, assign IDs, categorize |
| gap-analyzer | C | Opus | Find topic/depth/risk gaps, suggest questions |
| refinement-analyzer | D | Opus | Review questions for competitive signals |
| competitor-assessor | E | Opus | Holistic competitor-view risk assessment |

**Gate:** All 5 analysis artifacts exist in `phase_02_analysis/`

### Phase 3: INTERACTIVE REVIEW (Coordinator - Sequential)

**Actions:**
1. Present gaps 3-5 at a time, wait for decisions
2. Present refinements 3-5 at a time, wait for decisions
3. Present risk items, wait for decisions
4. Record EVERY decision explicitly
5. Update consolidated_questions_v02.md

**Gate:** `phase_03_review/review_decisions.md` exists, decisions logged in state.json

### Phase 4: QUALITY CHECKS (Agent Teams - Parallel)

**Agents spawned:**
| Agent | Session | Model | Task |
|-------|---------|-------|------|
| final-risk-reviewer | G | Opus | Holistic review of full set post-decisions |
| duplicate-checker | H | Sonnet | Find semantic duplicates, suggest consolidations |
| depth-checker | I | Sonnet | Verify questions appropriately detailed for RFP Q&A |

**Gate:** All 3 quality artifacts exist in `phase_04_quality/`

### Phase 5: USER APPROVAL

**Actions:**
1. Present final question list summary
2. Surface any remaining concerns from Phase 4
3. Ask for EXPLICIT approval
4. Record in state.json: `approved: true`

**Gate:** state.json contains `approved: true`

### Phase 6: DOCUMENT GENERATION (User Choice)

**Actions:**
1. **ASK USER** what outputs they want:
   - Final markdown (always generated)
   - HTML review document (optional)
   - CSV export (optional)
2. **OFFER** Big4 skill invocation for content review/polish
3. Generate selected outputs via document-generator agent
4. Remove `.active` marker

**Gate:** `phase_06_outputs/final_questions.md` exists (plus selected formats)

---

## Session Folder Structure

```
.rfp-questions/<client-name>/
├── .active                                    # Marker for hook scoping
├── orchestration/
│   └── state.json                             # Survives compaction
├── phase_01_setup/
│   └── source_verification.md
├── phase_02_analysis/
│   ├── source_verification_report.md          (Session A)
│   ├── question_catalog_v01.md                (Session B)
│   ├── gap_analysis.md                        (Session C)
│   ├── refinement_recommendations.md          (Session D)
│   └── competitor_risk_assessment.md          (Session E)
├── phase_03_review/
│   ├── review_decisions.md
│   └── consolidated_questions_v02.md
├── phase_04_quality/
│   ├── final_risk_review.md                   (Session G)
│   ├── duplication_check.md                   (Session H)
│   └── depth_check.md                         (Session I)
├── phase_05_approval/
│   └── (state.json check only - no artifact)
└── phase_06_outputs/
    ├── final_questions.md
    ├── rfp_questions_review.html              (if requested)
    └── rfp_questions.csv                      (if requested)
```

---

## state.json Schema

```json
{
  "client_name": "McGrath",
  "rfp_name": "MSP RFP 2026",
  "session_folder": ".rfp-questions/mcgrath-msp-2026",
  "current_phase": "review",
  "completed_phases": ["setup", "analysis"],
  "what_we_are_building": "36 clarifying questions for MSP RFP",
  "competitive_context": "BayOne is smaller bidder vs large embedded MSPs",
  "source_documents": [
    "rfp_plaintext.md",
    "integration_list.xlsx"
  ],
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
      "item": "Q13",
      "type": "revision",
      "decision": "accepted",
      "reason": "removed strategic signal",
      "timestamp": "2026-02-23T14:30:00Z"
    }
  ],
  "gaps_reviewed": 12,
  "gaps_accepted": 8,
  "gaps_modified": 2,
  "gaps_rejected": 2,
  "critical_learnings": [
    "Large MSPs have embedded teams who get answers internally",
    "RFP Q&A is public - competitors see every question"
  ],
  "approved": false,
  "requested_outputs": ["markdown", "html", "csv"],
  "big4_review_requested": true,
  "agent_mode": "teams"
}
```

---

## Agent Definitions Summary

| Agent | Model | permissionMode | Tools |
|-------|-------|----------------|-------|
| rfp-source-verifier | Sonnet | plan | Read, Glob, Grep |
| rfp-question-cataloger | Sonnet | plan | Read, Glob, Grep |
| rfp-gap-analyzer | Opus | plan | Read, Glob, Grep |
| rfp-refinement-analyzer | Opus | plan | Read, Glob, Grep |
| rfp-competitor-assessor | Opus | plan | Read, Glob, Grep |
| rfp-final-risk-reviewer | Opus | plan | Read, Glob, Grep |
| rfp-duplicate-checker | Sonnet | plan | Read, Glob, Grep |
| rfp-depth-checker | Sonnet | plan | Read, Glob, Grep |
| rfp-document-generator | Opus | plan | Read, Glob, Grep |

All workers are **read-only**. They write their analysis to specified output files, but the coordinator handles all file management decisions.

---

## Stop Hook Logic

```python
# .claude/hooks/rfp-questions-compliance.py

# 1. Check for marker file
marker = find_marker(".rfp-questions/*/.active")
if not marker:
    sys.exit(0)  # Not an rfp-questions session, allow

# 2. Read state.json
state = read_state(marker.parent / "orchestration/state.json")
current_phase = state["current_phase"]

# 3. Define phase requirements
PHASE_REQUIREMENTS = {
    "setup": ["phase_01_setup/source_verification.md"],
    "analysis": [
        "phase_02_analysis/source_verification_report.md",
        "phase_02_analysis/question_catalog_v01.md",
        "phase_02_analysis/gap_analysis.md",
        "phase_02_analysis/refinement_recommendations.md",
        "phase_02_analysis/competitor_risk_assessment.md"
    ],
    "review": ["phase_03_review/review_decisions.md"],
    "quality": [
        "phase_04_quality/final_risk_review.md",
        "phase_04_quality/duplication_check.md",
        "phase_04_quality/depth_check.md"
    ],
    "approval": [],  # Checked via state.json
    "outputs": ["phase_06_outputs/final_questions.md"]
}

# 4. Verify all PREVIOUS phases complete
for phase in phases_before(current_phase):
    for artifact in PHASE_REQUIREMENTS[phase]:
        if not exists(marker.parent / artifact):
            print(f"Missing artifact: {artifact}", file=sys.stderr)
            print(f"Complete Phase {phase} before proceeding.", file=sys.stderr)
            sys.exit(2)  # Block

# 5. Special check for approval phase
if current_phase in ["outputs"] and not state.get("approved"):
    print("User approval required before generating outputs.", file=sys.stderr)
    sys.exit(2)

sys.exit(0)  # All checks passed
```

---

## Integration Points

### Big4 Skill Integration

In Phase 6, after user selects outputs:

```markdown
## Output Options

1. Final Markdown - Always generated
2. HTML Review Document - Professional BayOne design
3. CSV Export - For spreadsheet import

Would you also like me to invoke the **big4 skill** to review and polish
the question phrasing before final generation? This acts like a Big Four
consultant review to prevent misfires and improve clarity.

[Yes / No / Skip to generation]
```

If yes, invoke big4 skill with the consolidated questions, then proceed with generation.

### SessionStart Hook (Context Survival)

On session start, if `.active` marker exists:
1. Read state.json
2. Output critical context to Claude
3. Resume from current_phase

---

## Key Patterns from McGrath Session

### What Worked
- Incremental presentation (3-5 items)
- Full original text in revision notes
- Explicit decision confirmation
- Version control on question documents

### Anti-Patterns to Avoid
- Dumping all findings at once
- Truncating original questions
- Assuming "sounds good" = approval
- Pre-filtering gaps (human must see all)

---

## Settings.local.json Entries

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/.claude/hooks/rfp-questions-compliance.py",
            "timeout": 10000
          }
        ]
      }
    ]
  },
  "permissions": {
    "allow": [
      "Bash(python3 $CLAUDE_PROJECT_DIR/.claude/skills/rfp-questions/scripts/*)"
    ]
  },
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```
