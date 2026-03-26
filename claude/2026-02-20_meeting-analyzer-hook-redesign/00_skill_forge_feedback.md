# Skill-Forge Feedback

Lessons learned from the meeting-analyzer skill that should inform how skill-forge generates skills and hooks.

---

## Hook Design Issues

### 1. Hooks fired globally instead of opt-in

**Problem:** The generated hook scanned ALL `meeting*_*/` folders under `claude/`, firing on every session regardless of whether the skill was being used.

**Fix:** Hooks should use a marker file approach. Skill creates marker at start (e.g., `.meeting-analysis-active`), removes on completion. Hook only fires if marker exists.

### 2. Hardcoded filenames instead of pattern matching

**Problem:** Hook expected exact filenames like `01_speaker_notes.md` and `03_sentiment_and_relationship.md`, but actual numbering varied based on whether optional documents existed.

**Fix:** Use pattern matching for document types: `*_speaker_notes.md`, `*_sentiment*.md`. Numbers can vary; match on the suffix.

### 3. Fragile transcript parsing for workflow verification

**Problem:** Hook searched transcript for JSON strings like `"subagent_type":"Explore"` to verify Explore agent was used. Fragile, format-dependent.

**Fix:** Require workflow steps to produce output files that serve as proof. E.g., Explore agent writes `00_context_discovery.md`. Hook checks file exists.

### 4. Rigid string matching for content validation

**Problem:** Hook searched for exact phrases like "transcription note" or "transcription correction" in documents.

**Fix:** Check for section headers (e.g., `## Transcription`) rather than specific phrases. The section must exist; content can vary.

### 5. Validated historical work from previous sessions

**Problem:** If a previous session created incomplete folders and ran out of context, the hook blocked all future sessions.

**Fix:** Only validate folders created/modified in current session, or only when marker file is active.

---

## Folder Structure Issues

### 6. No dedicated skill output location

**Problem:** Meeting folders were scattered under arbitrary session folders (`claude/<session>/meeting*_*/`). Hard to find, no central location.

**Fix:** Skills that produce artifacts should use a dedicated folder: `./claude/<skill-name>/`. For meeting-analyzer: `./claude/meeting-analyzer/meeting_<topic>_<date>/`.

---

## Workflow Verification Approach

### Recommended pattern for hooks:

1. **Opt-in via marker file** - Hook only fires when skill is active
2. **Proof via output files** - Each required step produces a verifiable artifact
3. **Pattern matching** - Match document types, not exact filenames
4. **Section headers over phrases** - Require structure, allow content flexibility
5. **Session-scoped** - Only validate current work, not historical folders

---

## To Add (as we continue work)

<!-- Add new feedback items here as we discover them -->
