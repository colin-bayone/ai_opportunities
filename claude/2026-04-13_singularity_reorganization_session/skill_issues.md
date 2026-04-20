# Skill Issues: Singularity Reorganization Session (2026-04-13)

Issues encountered and patterns observed during a session that reorganized four engagement folders (cisco/epnm_ems, sephora, lam_research, tailored_brands) into Singularity format. These notes complement the per-engagement skill_notes.md files and are intended to inform future updates to the singularity skill itself.

---

## Source Material Handling

### Format Transcripts Before Reading Them (Critical Failure Pattern)

**Corrected 2026-04-13.** During the cisco/epnm_ems reorganization, when a new transcript arrived (`selva_and_team_4-6-2026.txt`), Claude attempted to read the raw single-line file directly through the Read tool. The user caught it: "Did you just try to read a single line transcript without running it through the script that we put together?" This wasted tokens on an unreadable wall-of-text and produced no useful comprehension.

The same pattern repeated when the March 25 transcript was provided — Claude went to read it before formatting.

**Rule for the skill:** When any new source transcript arrives in source/, the FIRST action is to format it with `format_transcript.py`. No exceptions. The skill should enforce this as a mandatory pre-step before any Read operation on a source file. Reading raw single-line transcripts produces poor comprehension and burns tokens.

### Verify Before Assuming Files Are Identical

**Corrected 2026-04-13.** After finding two files with similar names and the same byte size, Claude assumed they were duplicates based on a high-level diff that showed they were "99 bytes different — probably trivial." The user pushed back: "You can't just read and say that it's 99 bytes bigger and therefore it's trivial. You need to actually see what's actually different there." Claude then attempted a `diff` with `fold` that produced a malformed comparison and persisted in trying clever approaches instead of just reading both files.

The user finally said: "Just read the fucking files; they're not that long; it's not that hard. I recommend processing them with the script first."

**Rule for the skill:** When comparing two source files for substantive content differences, the correct approach is: format both files with the script, read both files in their entirety, and report the actual differences. Hash comparison is fine for confirming identity. Byte-size comparison is NOT a substitute for content comparison. Clever shell pipelines (diff + fold) for token efficiency often fail and waste more tokens than just reading the files.

### Never Keep Duplicate Files As "Alternates"

**Corrected 2026-04-13.** After confirming two files were essentially identical, Claude proposed keeping the new one "as an alternate copy" alongside the original. The user shut this down immediately: "I specifically said no, do not keep two versions of the same file as an alternate. That is stupid. If they are the same, keep one version only."

**Rule for the skill:** Source folders should contain ONE copy of each unique source material. If a file is functionally identical to an existing one, delete the duplicate. Do not preserve "alternates" or "in case we need them later." Duplicates create future confusion about which version is authoritative.

---

## Decision Presentation

### Decisions Need Context, Not Just Names

**Corrected 2026-04-13.** Multiple times in the session, Claude asked the user to make decisions about files without showing the file paths or content summaries. Example: "What about the CEO and Venkat files?" The user responded: "I have no idea what they are because you just said 'CEO and backend files'. You didn't tell me a path or a URL, and you didn't tell me what content was contained inside. How the hell would I randomly know two random files that you couldn't even be bothered to give me the file name for in a folder? That you don't even tell me where it is."

**Rule for the skill:** When presenting a decision to the user about how to handle a file or folder, ALWAYS include:
1. The full path to the file
2. The file size
3. A brief summary of the actual content (not inferred from filename — read it)
4. Why the decision is needed
5. The proposed options with explicit recommendations

Vague references like "the pricing docs" or "the CEO file" assume the user has the same context Claude has. They don't. The Read tool exists for a reason — use it before asking for decisions.

---

## Reorganization-Specific Patterns

### Singularity Skill Did Not Cover Reorganization Use Case

**Observed 2026-04-13.** The skill was built for greenfield engagements: starting with a blank folder, adding source materials, processing chronologically. It did not have guidance for the much more common case of reorganizing folders that already had partial structure, mixed Singularity and non-Singularity content, or content that needed to be archived versus integrated.

A separate `reorganization_guide.md` was written and saved to `.claude/skills/singularity/references/` to document the four engagement states (A: never touched, B: partial, C: complete needs validation, D: multi-project) and the four-phase approach (explore and map, archive and structure, process source materials, validate).

**Rule for the skill:** The reorganization guide should be officially incorporated into the skill, possibly as a Flow 7 ("Reorganize an existing engagement folder") in the main SKILL.md. The skill should detect existing folder state and route to the appropriate flow rather than always assuming a greenfield engagement.

### Deliverables vs Presentations vs Planning Distinctions Are Unclear

**Observed 2026-04-13.** During the lam_research validation, the user noted: "I think there is right now some confusion among the singularity folders about what goes in deliverables versus what goes in presentations." Investigation found that some HTML files in `deliverables/` were actually internal (not client-facing), and there was no clear rule for what distinguished a "deliverable" from a "presentation."

The working rule we settled on:
- **deliverables/** = Client-facing documents (multi-page, narrative, sent to client or shared internally as polished artifacts)
- **presentations/** = Slide decks (individual slides meant to be presented/walked through)
- **planning/** = Internal-only documents (meeting summaries for BayOne use, prep notes, session handoffs)

**Rule for the skill:** The folder_structure.md reference should explicitly define these distinctions with examples. The Flow 4 (Create Deliverable) prompt should also ask whether the document is client-facing or internal, and route to the appropriate folder. Currently the skill assumes everything in deliverables/ is client-facing.

### Stop Hook Fires During Normal Mid-Set Processing

**Observed 2026-04-13.** The Singularity stop hook flagged "no summary document found" multiple times during the session, including during legitimately mid-set processing (after writing the people file but before completing the deep dives and summary). This is expected behavior given the rule that summaries must always be the last file, but it produces noise during normal workflow.

**Rule for the skill:** The stop hook could be smarter about distinguishing "user is done with the session and forgot a summary" from "user is mid-set and the summary is coming." One option: skip the warning if the most recent file in research/ is dated within the current session (suggesting active processing). Another option: only fire the warning if no file in research/ has been modified within some recent window. As-is, the warning is correct but noisy.

---

## Process Patterns

### Run File Comparisons Before Archiving

**Observed 2026-04-13.** During the sephora reorganization, the temptation was to move 124 files of pre-Singularity meeting analysis (`2025-02-25_andrew-meeting-prep/`) directly to archive without checking what was unique. The user's instruction was important: "Don't just randomly throw things into archive, because I think there is right now some confusion among the singularity folders about what goes in deliverables versus what goes in presentations."

The actual investigation found 16 unique items (stakeholder dossiers, relationship analysis, action tracking) that should be preserved into the active project before archiving. A naive "move to archive" would have lost this content.

**Rule for the skill:** Before archiving any folder during a Phase 4 cleanup, run a comparison agent that identifies (a) source materials already captured in the active project, (b) source materials that are unique and need to be moved into the active project, and (c) derived analysis that is superseded by the active research library. Archive only what is fully accounted for. This is documented in the reorganization_guide.md but should also be a hard step in the Flow 7 (Reorganize) workflow.

### Split Reorganization Into Validate vs Process Phases

**Observed 2026-04-13.** The most common reorganization pattern is a project that is already mostly-Singularity but has gaps (missing session handoff, unformatted source files, empty pricing folder, source files added since last processing). For these, full reprocessing is wasteful — the right action is targeted gap-filling.

The reorganization guide includes a State C validation checklist (12 items) for this. It worked well for sephora/edw_modernization (10/12 PASS) and lam_research/ip_protection (10/12 PASS). The two failures in both cases were the same: empty pricing folder and missing session handoff.

**Rule for the skill:** The validation checklist in the reorganization guide should become a runnable check, not just a reference. A script could verify each item programmatically and report PASS/FAIL/N/A. This would let the user run validation regularly without invoking a full agent.

---

## Reference Documents Created During This Session

| File | Purpose |
|------|---------|
| `.claude/skills/singularity/references/reorganization_guide.md` | Complete guide for reorganizing existing engagement folders into Singularity format. Covers four states, four phases, and worked examples. |
| `.claude/skills/singularity/scripts/format_transcript.py` | Script to format single-line speech-to-text transcripts into readable multi-line files. Was previously living in sephora/edw_modernization/planning/ and was promoted into the skill. |

---

## Work Completed This Session

| Folder | State | Result |
|--------|-------|--------|
| cisco/epnm_ems | A (never touched) | Full reorganization — 57 research docs across 8 sets |
| sephora | D (multi-project) | Validated 2 Singularity projects, archived 5 legacy folders, copied 16 unique items into active project |
| lam_research | D (single project + legacy) | Validated ip_protection, consolidated 8 legacy items into project, archived rest |
| tailored_brands | A (never touched) | Full reorganization — 7 research docs in 1 set |
