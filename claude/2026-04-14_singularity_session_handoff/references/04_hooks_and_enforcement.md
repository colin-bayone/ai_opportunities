# 04 - Hooks and Enforcement Architecture

**Date:** 2026-04-14
**Scope:** Complete reference for the hook and enforcement system built into the Singularity skill during the April 2026 multi-day session. Covers the design philosophy, implementation details, current coverage, known gaps, behavioral rule enforcement, and recommendations for future sessions.

---

## 1. Design Philosophy: Proof via Artifact

The enforcement architecture is built on a single principle: **every required step produces an artifact, and the stop hook checks that all required artifacts exist.** Missing artifacts block progression with exit code 2.

This is deterministic enforcement, not behavioral enforcement. The system does not parse conversation transcripts or rely on Claude remembering to do something. Instead, each mandatory workflow step writes a file (or updates a file) at a known path. The stop hook then verifies that those files exist. If they do not, Claude cannot proceed.

The distinction matters because behavioral instructions ("always read the spec before generating slides") are routinely violated. Artifact checks ("if presentation HTML exists, the spec file must also exist") cannot be circumvented regardless of what Claude decides to do in a given turn.

---

## 2. The django-forge-v2 Reference Pattern

The enforcement architecture was modeled on the django-forge-v2 skill located at `/home/cmoore/programming/claude-plugins/plugins/django-tools/skills/django-forge-v2/`. That skill demonstrates the pattern at scale with:

- **8 phases**, each with defined artifact requirements documented in `references/phase_requirements.md`
- **A Stop hook** that walks backward through all previous phases, checking that every required artifact exists
- **A PreToolUse hook** that blocks forbidden operations in real time (not just after the fact)
- **A SessionStart hook** that re-injects context from `state.json` after conversation compaction
- **A marker file** (`.active`) that scopes the hooks to fire only when the skill is in use

The key lessons carried forward from django-forge-v2 into Singularity:

1. Artifacts, not transcripts. Never parse the conversation to check if a step happened.
2. Section headers, not phrases. When checking content within artifacts, match structural headers rather than specific wording.
3. Pattern matching, not hardcoded filenames. Match `*_summary_*.md` rather than a specific filename with a specific date.
4. Minimum size checks. An empty file is not a valid artifact. Require minimum character counts to prevent placeholder files from passing.
5. Skill-scoped hooks. The stop hook is defined in the skill's frontmatter so it only fires when Singularity is active.
6. Loop prevention. Always check `stop_hook_active` at the top to prevent infinite recursion.

---

## 3. Exit Code Protocol

The stop hook uses a three-value exit code scheme:

| Exit Code | Meaning | Effect |
|-----------|---------|--------|
| 0 | All checks passed | Claude proceeds normally |
| 2 | Blocking error detected | Claude is blocked; the error message is fed back as feedback |
| (any other) | Unexpected failure | Treated as a non-blocking error |

When exit code 2 fires, the error message printed to stderr tells Claude exactly what artifact is missing and what action to take. Claude must then produce the missing artifact before it can continue. This creates a deterministic enforcement loop: skip a step, get blocked, fix it, proceed.

---

## 4. Hook Definitions in SKILL.md Frontmatter

The SKILL.md frontmatter defines the following hooks:

```yaml
hooks:
  Stop:
    - hooks:
        - type: "command"
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/singularity/scripts/singularity_stop.py"
          timeout: 10000
          statusMessage: "Verifying singularity workflow..."
```

Currently, only the **Stop hook** is defined. There are no PreToolUse, SessionStart, or other hook types configured. The Stop hook fires after every Claude response and runs the Python verification script with a 10-second timeout.

Because the hook is defined in the skill's frontmatter (not in global settings), it is automatically scoped to fire only when the Singularity skill is active. This means it does not interfere with other skills or non-skill sessions. No `.active` marker file is needed, unlike the django-forge-v2 pattern.

---

## 5. What the Stop Hook Currently Checks

The stop hook script (`scripts/singularity_stop.py`) performs 6 checks:

### Check 1: Org Chart Existence

- **Artifact:** `{engagement_root}/org_chart.md`
- **Condition:** Only fires if more than 1 research file exists in `research/` (meaning research has progressed beyond the initial methodology document)
- **Error message:** Instructs Claude to create the org chart after processing the first source material

### Check 2: Summary Document Existence

- **Artifact:** `research/*_summary_*.md` (glob pattern)
- **Condition:** Only fires if more than 1 research file exists but no summary files are found
- **Error message:** States that each document set must end with a summary file

### Check 3: Hard Rules File Existence

- **Artifact:** `.claude/skills/singularity/references/hard_rules.md`
- **Condition:** Always checked on every invocation
- **Error message:** States the file must exist and be read at the start of every invocation

### Check 4: Presentation Design References Gate

This is a compound check with three sub-checks, all gated on the presence of presentation HTML files in the engagement:

- **4a - Design language spec:** Checks that `.claude/skills/singularity/references/presentation_design_language.md` exists
- **4b - Slide examples:** Checks that `.claude/skills/singularity/assets/slide_examples/` exists and contains at least one `.html` file
- **4c - Gold standard deck:** Checks that `.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/` exists

If any of these are missing and presentation HTML has been generated, the hook blocks.

### Check 5: Sub-Singularity References Gate

- **Artifact:** `.claude/skills/singularity/references/nested_singularity.md`
- **Condition:** Only fires if the engagement contains nested methodology files at `*/research/00_methodology_*.md` (indicating a sub-singularity exists)
- **Error message:** States the nested singularity reference must exist

### Check 6: Chart Back Button Verification

- **Artifact:** `class="back-btn"` string in chart HTML files
- **Condition:** Scans all `presentations/*/charts/*.html` files
- **Error message:** Identifies the specific chart file missing the back button element
- **Notable:** This is the only check that inspects file content rather than just verifying existence

### Engagement Discovery

Before running any checks, the script discovers the active engagement by globbing for `*/research/00_methodology_*.md` and `*/*/research/00_methodology_*.md` from the current working directory. It selects the most recently modified methodology file and derives the engagement root from it. If no methodology files exist (indicating no active engagement), the script exits 0 without checking anything.

### Loop Prevention

The first thing the script does is check `data.get("stop_hook_active", False)`. If true, it exits 0 immediately. This prevents the stop hook from triggering itself recursively when Claude responds to a hook-generated error message.

---

## 6. What the Stop Hook Does NOT Check (Known Gaps)

The path verification audit conducted on 2026-04-13 identified several gaps:

### Gap 1: No Mermaid Validation

The stop hook does not verify that mermaid design standards (`references/mermaid_design_standards.md`) or the shape library (`assets/mermaid_shape_library/`, 8 HTML files) were consulted when chart HTML files contain mermaid diagrams. The assets exist and are referenced in the SKILL.md Flow 7 instructions, but no artifact check enforces their use. Charts with mermaid diagrams can be generated without the shape library ever being read.

### Gap 2: Gold Standard Check is Presentation-Only

The gold standards directory contains non-presentation gold standards (information request, preliminary approach, POC proposal, problem restatement, knowledge transfer), but the stop hook only validates the presentation gold standard path. Deliverable HTML generation (Flow 4) is not gated by the stop hook against any deliverable-specific gold standards.

### Gap 3: No Deliverable Design Spec Gate

When generating HTML deliverables (Flow 4), the BayOne design spec at `assets/design/bayone_design_spec.md` is supposed to be read. The stop hook does not verify this. The instruction exists only as a behavioral rule in the SKILL.md Flow 4 section.

### Gap 4: No Content Quality Checks on Slides

Check 6 verifies back buttons exist in chart pages, but there is no analogous check for slide content quality. The SKILL.md specifies that all cards must use bullet formatting (`.items`/`.item` pattern), but the stop hook does not scan for this. The "Planned Checks" in the enforcement architecture document mention this as a future addition.

### Gap 5: No Transcript Formatting Verification

Behavioral rule B3 requires that raw transcripts be formatted with `format_transcript.py` before reading. The stop hook does not verify whether a formatted version exists alongside raw source files. This remains purely behavioral enforcement.

### Gap 6: Bridge Document Existence

The SKILL.md mandates bridge documents (`research/<from>-<to>_changes_<date>.md`) between document sets. The stop hook does not check for their existence when multiple document sets exist.

---

## 7. The Mandatory Startup Gate: hard_rules.md

### The Pattern

Every Singularity invocation, before any work proceeds, must execute a two-part startup check:

1. **Permission check:** Read `.claude/settings.local.json` and verify that `Write($CLAUDE_PROJECT_DIR/**)` and `WebSearch` exist in `permissions.allow`. If missing, request permission to add them. If declined, stop.
2. **Hard rules read:** Read `.claude/skills/singularity/references/hard_rules.md`. If the file does not exist, stop and inform the user.

The stop hook (Check 3) enforces that the hard rules file exists. However, the stop hook cannot enforce that the file was actually read. The "must read before proceeding" instruction is behavioral. The existence check is the deterministic backstop: if someone deletes the file, the hook catches it.

### What hard_rules.md Contains

The file contains 16 behavioral rules (B1 through B16), each derived from a specific violation that occurred during a prior session. Every rule includes:

- The rule statement
- The reasoning (why this rule exists)
- When the violation occurred and was corrected

The rules cover:

| Rule | Topic |
|------|-------|
| B1 | One question at a time in interactive discussion |
| B2 | No unilateral filtering during exploration |
| B3 | Format transcripts before reading |
| B4 | Read reference documents before describing them |
| B5 | Verify proposals against the research library |
| B6 | Do not reinvent proven structure |
| B7 | Align on structure before producing documents |
| B8 | Decisions require full context (paths, content, rationale) |
| B9 | Do not declare work done prematurely |
| B10 | Paraphrase and improve, do not record verbatim |
| B11 | Verify before assuming files are identical |
| B12 | No duplicate source files |
| B13 | Provide full context and framing when raising items |
| B14 | Check language standards across all documents |
| B15 | Bring perspective to brainstorming, do not interview |
| B16 | Confirm before executing after multiple corrections |

Rules B8, B11, B12, and B16 were added during the April 13 session. The file is a living document that grows as new behavioral failures are identified and codified.

---

## 8. The Rule Violation Protocol

The hard_rules.md file defines a mandatory protocol for when a rule violation is identified. When the user indicates a rule has been violated (through phrases like "you broke a rule," "that violates," "we already discussed this," or similar):

1. **Stop current work immediately.** Do not continue the violating approach.
2. **Re-read hard_rules.md** before responding.
3. **Acknowledge the specific rule violated** by number (e.g., "That violated B2").
4. **Correct course** based on the rule, then continue.

The re-read requirement is critical. It forces Claude to ground its next action in the full rule set rather than in the same pattern that produced the violation. Without the re-read, Claude tends to apologize and then repeat a variant of the same mistake.

---

## 9. What Worked Well With Enforcement This Session

### Artifact-Based Checks Are Reliable

The presentation design references gate (Check 4) consistently prevented slide generation from proceeding without the design language spec, example slides, and gold standard deck being present. This is the most complex multi-artifact check in the stop hook, and it functioned correctly across multiple engagement contexts (Lam Research and Cisco CICD both have presentations).

### The Chart Back Button Check Caught Real Issues

Check 6 inspects actual HTML content for the `class="back-btn"` element. This is the only content-level check in the current hook, and it works because the check is simple, deterministic, and binary (the string is either present or it is not).

### Skill-Scoped Hooks Eliminated Cross-Contamination

By defining the stop hook in the SKILL.md frontmatter rather than in global settings, the hook only fires during Singularity sessions. This avoids the problem that plagued earlier approaches where hooks would fire during unrelated work and cause confusion.

### The Hard Rules File as Living Documentation

The pattern of codifying every behavioral correction into a numbered rule, with the violation date and reasoning, created an increasingly comprehensive behavioral specification. Starting from zero rules and ending with 16 over the course of the multi-day session demonstrates the value of treating behavioral failures as bugs to be documented rather than one-off corrections.

### Exit Code 2 Feedback Loop

When the stop hook blocks with exit code 2, the error message is specific enough that Claude can self-correct without user intervention. The messages include the file path, the expected artifact, and the corrective action. This turns enforcement from a wall into a guide.

---

## 10. What Did Not Work (Behavioral Violations Despite Codification)

### Rules Were Violated After Being Written Down

Multiple behavioral rules were violated even after they were codified in hard_rules.md. The pattern is consistent: Claude reads the rules at session start, follows them for a while, and then reverts to default behavior as the conversation grows longer and the rules drift out of the active context window.

Specific examples from this session:

- **B8 (Decisions require full context):** Claude continued to present file decisions without full paths, content summaries, or rationale even after B8 was written. This required multiple corrections in the same session.
- **B9 (Do not declare work done prematurely):** Claude continued to use closing language ("you're all set," "good luck") during active work.
- **B16 (Confirm before executing after multiple corrections):** This rule was created because Claude was corrected three times on the enforcement approach and then immediately started executing without confirming the agreed plan. The rule was necessary because the pattern of "correct, correct, correct, execute without confirmation" is a deep default behavior.

### Behavioral Rules Cannot Be Enforced Deterministically

The fundamental limitation is that the stop hook can only verify artifacts. It cannot verify behavior. Rules like "ask one question at a time" (B1), "format transcripts before reading" (B3), or "verify proposals against the research library" (B5) describe process requirements that do not have a clean artifact signature. The stop hook cannot tell whether Claude asked one question or five in a given response.

### Context Window Decay

Behavioral rules lose effectiveness as the conversation grows. The hard_rules.md file is read at session start and exists in the context window, but as the conversation extends (especially during long transcript processing or iterative deliverable work), the rules effectively fall out of Claude's active attention. This is not a hook problem; it is a fundamental context window limitation.

### The "Read Before Describing" Problem

B4 (read reference documents before describing them) is particularly difficult to enforce because Claude's training data includes descriptions of many common document structures. Claude can produce a plausible-sounding description of a document's structure without reading it, and the stop hook has no way to detect this. Only user vigilance catches these violations.

---

## 11. Recommendations for the Next Session

### 11.1 Add Content-Level Checks Where Feasible

The back button check (Check 6) proves that content-level verification works when the check is simple and deterministic. Extend this pattern to:

- **Bullet formatting in slides:** Check for `.items` and `.item` CSS classes in presentation HTML files. If cards exist without bullet formatting, block.
- **Document header format:** Check that research documents start with the required header structure (`# <Set Number>`, `**Source:**`, `**Source Date:**`, `**Document Set:**`, `**Pass:**`).
- **Mermaid references:** If chart HTML contains `class="mermaid"`, verify that the mermaid design standards file and shape library exist.

### 11.2 Add Deliverable Gold Standard Gate

Mirror Check 4 (presentation references gate) for deliverables. If HTML files exist in `deliverables/`, verify that the BayOne design spec exists at `assets/design/bayone_design_spec.md` and that the appropriate gold standard for the deliverable type is present. The gold standard directory already contains type-specific examples.

### 11.3 Add Bridge Document Check

If the engagement has more than one document set (more than one distinct set number prefix in `research/`), verify that bridge documents (`*_changes_*.md`) exist for consecutive sets. This is currently a behavioral instruction in SKILL.md with no artifact enforcement.

### 11.4 Consider a PreToolUse Hook

The django-forge-v2 pattern includes a PreToolUse hook that can block forbidden operations in real time (before they happen, not after). Singularity currently has no PreToolUse hook. Potential uses:

- Block writing to `source/` directories (source files should never be modified)
- Block writing presentation HTML without the design language spec having been read in the current session (would require a session state tracker)
- Block writing research documents without the required header format

### 11.5 Consider a SessionStart Hook

A SessionStart hook could re-inject the hard_rules.md content after conversation compaction events. This would address the context window decay problem by ensuring the rules are re-read when the context is trimmed, not just at the start of the session.

### 11.6 Re-Read hard_rules.md at the Start of Every Session

This is already mandated in the SKILL.md startup sequence, but it bears emphasizing in handoff documentation. The new session should begin with a fresh read of the rules file, and the session operator should verify that the read actually occurred (check for the read tool call in the first few turns).

### 11.7 Track Rule Violation Frequency

Consider adding a lightweight tracking mechanism (a markdown file in `planning/` or a comment at the bottom of hard_rules.md) that records how often each rule is violated per session. This data would help prioritize which behavioral rules are candidates for conversion to artifact-based enforcement and which are holding as behavioral instructions.

### 11.8 Increase Stop Hook Timeout if Checks Grow

The current timeout is 10 seconds. With 6 checks, this is adequate. If content-level checks are added (scanning HTML files for patterns, verifying header formats across research documents), the script may need more time, especially on engagements with many files. Monitor execution time and increase the timeout if checks are added.

---

## 12. File Reference

| File | Purpose |
|------|---------|
| `.claude/skills/singularity/SKILL.md` | Skill definition with hook frontmatter and mandatory startup sequence |
| `.claude/skills/singularity/scripts/singularity_stop.py` | The stop hook script (6 checks) |
| `.claude/skills/singularity/references/hard_rules.md` | 16 behavioral rules, mandatory read at session start |
| `.claude/skills/singularity/references/enforcement_architecture.md` | Design document explaining the proof-via-artifact pattern |
| `claude/2026-04-13_mermaid_research/path_verification_HOOK.md` | Path verification audit of the stop hook (2026-04-13) |
