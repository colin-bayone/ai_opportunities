---
name: big4
description: |
  Transform rough or internal documents into professional Big Four consulting quality.
  Catches AI writing anti-patterns, colloquial language, and formatting violations.
  Manual invocation only via /big4.
disable-model-invocation: false
user-invocable: true
argument-hint: [document-path]
allowed-tools: Read, Write, Edit, Glob, Grep, Task, WebSearch, WebFetch
---

# Big4: Professional Document Polish

Transform internal or rough documents into polished, client-ready materials that read like Big Four consulting deliverables.

## Hard Rules

1. NEVER modify the original document. Create versioned copies (v2, v3, etc.)
2. ALWAYS read source materials (transcripts, context docs) before critiquing
3. ALWAYS create session folder structure before any work
4. ALWAYS update state.json when transitioning phases
5. NEVER skip phases. The Stop hook enforces this.
6. Preserve ALL substantive content. Style changes only, not substance removal.

## Session Setup

When invoked, first create the session folder structure:

```
claude/<date>_big4_<topic>/
├── state.json              # Phase tracking
├── source/                 # Original documents, transcripts
├── research/               # Transcript analysis, web research
└── planning/               # Critique, rewrites, comparisons
```

Initialize state.json:
```json
{
  "current_phase": "setup",
  "topic": "<description>",
  "original_document": "<path>",
  "created": "<timestamp>"
}
```

## Phases

### Phase 1: Setup

1. Create session folder structure
2. Copy or link original document to `source/`
3. Identify any supporting materials (transcripts, context docs)
4. Update state.json: `"current_phase": "setup"`

**Required artifacts:** Session folder exists, source documents present

### Phase 2: Source Analysis

1. Spawn `transcript-reader` agent to deeply read all source materials
2. Document findings in `research/source_analysis.md`
3. Capture: key claims, technical details, stakeholder quotes, context
4. Update state.json: `"current_phase": "source_analysis"`

**Required artifacts:** `research/source_analysis.md` (minimum 500 characters)

### Phase 3: Critique

1. Read the document to be polished section by section
2. Apply anti-pattern detection (read `.claude/skills/big4/references/anti_patterns.md`)
3. Apply professional standards (read `.claude/skills/big4/references/professional_standards.md`)
4. Produce comprehensive critique in `planning/critique.md`
5. Update state.json: `"current_phase": "critique"`

**Critique document must include:**
- Issue categories with specific line references
- Examples of each violation
- Concrete fix recommendations
- Overall verdict (PASS / FAIL / NEEDS REVISION)

**Required artifacts:** `planning/critique.md` (minimum 1000 characters)

### Phase 4: Rewrite

1. Create rewritten version preserving original filename with version suffix
2. Save to `planning/<original_name>_v2.md` (or v3, v4 as needed)
3. Apply ALL fixes identified in critique
4. Maintain all substantive content from original
5. Update state.json: `"current_phase": "rewrite"`

**Required artifacts:** `planning/*_v2.md` or higher version

### Phase 5: Comparison

1. Compare original vs rewritten version
2. Verify no substantive content was removed
3. Document all changes in `planning/version_comparison.md`
4. Update state.json: `"current_phase": "comparison"`

**Comparison document must include:**
- Content preservation verification table
- List of changes made (with rationale)
- Confirmation that substance was preserved

**Required artifacts:** `planning/version_comparison.md` (minimum 500 characters)

### Phase 6: Compliance

1. Check rewritten document against project style guide (CLAUDE.md if present)
2. Verify all anti-patterns removed
3. Document in `planning/style_compliance.md`
4. Update state.json: `"current_phase": "compliance"`

**Required artifacts:** `planning/style_compliance.md`

### Phase 7: Quality Audit

1. Run the pattern flagging script on the rewritten document:
   ```bash
   python3 .claude/skills/big4/scripts/flag_ai_patterns.py planning/<document>_vN.md
   ```
2. Save script output to `planning/pattern_scan.md`
3. Spawn `quality-auditor` agent with the document and scan results
4. Agent produces `planning/quality_audit.md` with final verdict
5. Update state.json: `"current_phase": "quality_audit"`

**Quality Audit must include:**
- Review of each flagged item (OK or ISSUE)
- Additional issues found beyond script flags
- Overall verdict (PASS / FAIL / NEEDS REVISION)

**Required artifacts:** `planning/quality_audit.md` (must contain "Verdict: PASS")

If verdict is FAIL or NEEDS REVISION, return to Phase 4 (Rewrite) and iterate.

### Phase 8: Complete

1. Update state.json: `"current_phase": "complete"`
2. Present final document location to user
3. Summarize key changes made

## Optional: Refinement Iterations

After Phase 6, user may request additional refinements:

1. User provides feedback on specific issues
2. Document feedback in `planning/refinement_feedback_N.md`
3. Create new version (v3, v4, etc.)
4. Re-run comparison and compliance checks

For technical research during refinement:
- Spawn `web-researcher` agent for framework/technology research
- Document findings in `research/`

## Agent Usage

**transcript-reader:** Always spawn for Phase 2 source analysis
```
Use the transcript-reader agent to deeply analyze all documents in source/
```

**web-researcher:** Spawn when technical verification needed
```
Use the web-researcher agent to research [specific framework/technology]
```

**quality-auditor:** Always spawn for Phase 7 quality audit
```
First run: python3 .claude/skills/big4/scripts/flag_ai_patterns.py <document_path>
Then spawn quality-auditor agent with the document and scan results
```

## State Transitions

The Stop hook verifies all previous phases are complete before allowing current phase work.

| Current Phase | Hook Verifies |
|---------------|---------------|
| setup | Nothing (first phase) |
| source_analysis | setup artifacts |
| critique | setup + source_analysis |
| rewrite | setup + source_analysis + critique |
| comparison | setup + source_analysis + critique + rewrite |
| compliance | all previous phases |
| quality_audit | all previous phases |
| complete | all previous phases (including quality_audit with PASS verdict) |

## References

Load these as needed during critique:
- `.claude/skills/big4/references/anti_patterns.md` - AI writing patterns to catch
- `.claude/skills/big4/references/professional_standards.md` - Big Four quality standards
