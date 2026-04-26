# Enforcement Architecture

## The Pattern

**Every required step produces an artifact. The stop hook checks that all required artifacts exist. Missing artifacts block progression with exit code 2.**

This is the same pattern used in django-forge-v2, proven across dozens of issue implementations. It is deterministic, not behavioral. Claude cannot skip a step because the hook catches the missing artifact regardless of what Claude decided to do.

---

## How It Works

### 1. Required Steps Produce Artifacts

Each mandatory step in the workflow writes a file (or updates a file) at a known path. The artifact is the proof that the step happened. Examples:

- Mandatory startup reads `hard_rules.md` and the permission check reads `settings.local.json` — these are gated steps where the skill stops if the condition is not met.
- Processing a transcript produces people files, deep-dive files, and a summary — the stop hook checks that summaries exist.
- Creating a presentation requires reading the design language spec and examples — the stop hook checks that the spec and examples exist.

### 2. The Stop Hook Verifies Artifacts

The stop hook fires every time Claude finishes a response. It:

1. Identifies the active engagement (by finding `research/00_methodology_*.md`)
2. Walks through a checklist of required artifacts
3. For each artifact: checks existence and optionally minimum content size
4. If any required artifact is missing: prints the issue to stderr and exits with code 2
5. Exit code 2 blocks Claude and feeds the error message back as feedback

### 3. Exit Code 2 Is the Enforcement Mechanism

- Exit 0 = everything is fine, proceed
- Exit 2 = blocking error, Claude cannot proceed until the issue is resolved
- The error message tells Claude exactly what is missing
- Claude must then go produce the missing artifact before continuing

---

## Applying This to Singularity

### Current Checks (in `scripts/singularity_stop.py`)

| Check | Artifact | Condition |
|-------|----------|-----------|
| Methodology exists | `research/00_methodology_*.md` | After engagement created |
| Org chart exists | `org_chart.md` | After research has started (>1 research file) |
| Per-set summary completion | `research/<NN>_summary_*.md` (≥200 chars) per set | Every set except the most recent must be closed with a summary. The most recent set is exempt if `research/.set_<NN>_in_progress` marker exists. |
| Hard rules file exists | `references/hard_rules.md` | Always |
| Presentation spec exists | `references/presentation_design_language.md` | If presentation HTML exists |
| Slide examples exist | `layout_examples/*.html` | If presentation HTML exists |
| Gold standard deck exists | `gold_standards/presentations/team_status_update/` | If presentation HTML exists |
| Sub-singularity reference exists | `references/nested_singularity.md` | If sub-singularity folders exist |
| Chart back buttons | `class="back-btn"` in chart HTML | If `charts/` subfolder exists |

### Set Completion Logic

Research files are grouped by set prefix (`01`, `02`, `03`, ...). Letter suffixes (`01a`, `01b`) roll up to their parent set. Bridge documents (`01-02_changes_*.md`) and the methodology document (`00_methodology_*.md`) are excluded from set grouping.

For each set:
- **Closed:** a summary file `<NN>_summary_*.md` exists with ≥200 characters of content.
- **In progress:** summary is missing AND a marker file `research/.set_<NN>_in_progress` exists AND the set is the highest-numbered one. Exempt from the check.
- **Unclosed (violation):** summary missing AND either no marker OR not the most recent set. The hook fails.

Markers are created at the start of a set (right after the people file is written) and deleted at the end (after the summary is written). This is documented in Flow 3 of `SKILL.md`.

### Planned Checks

| Check | Artifact | Condition |
|-------|----------|-----------|
| Hard rules file exists | `references/hard_rules.md` | Always (every invocation) |
| Chart back buttons | `class="back-btn"` in chart HTML | If `charts/` subfolder exists |
| Bullet formatting in slides | `.items` pattern in card HTML | If presentation HTML exists |
| Sub-singularity methodology | `*/team/research/00_methodology_*.md` | If sub-singularity folders exist |
| Gold standard exists | `gold_standards/presentations/team_status_update/` | If presentation HTML exists |

---

## Key Principles

1. **Artifacts, not transcripts.** Never parse the conversation transcript to check if a step happened. Transcripts are fragile (format changes, spacing). Artifacts are reliable proof.

2. **Section headers, not phrases.** When checking content within artifacts, match section headers (`## Transcription`) rather than specific phrases ("transcription note"). Headers are structural; phrases are stylistic.

3. **Pattern matching, not hardcoded filenames.** Match `*_summary_*.md` rather than `01_meeting_summary_2026-03-12.md`. Numbers vary; the suffix is the stable identifier.

4. **Minimum size checks.** An empty file is not a valid artifact. Require minimum character counts (50-200 depending on the artifact type) to prevent placeholder files from passing the check.

5. **Skill-scoped hooks.** The singularity stop hook is defined in the skill's frontmatter, so it only fires when singularity is active. It does not interfere with other skills or non-skill sessions.

6. **Loop prevention.** Always check `stop_hook_active` at the top of the hook. If true, exit 0 immediately to prevent infinite recursion.

---

## Reference Implementation

The django-forge-v2 skill at `/home/cmoore/programming/claude-plugins/plugins/django-tools/skills/django-forge-v2/` demonstrates this pattern with:

- 8 phases, each with defined artifact requirements (`references/phase_requirements.md`)
- A stop hook that walks backward through all previous phases checking artifacts
- A PreToolUse hook that blocks forbidden operations in real time
- A SessionStart hook that re-injects context from `state.json` after compaction
- A marker file (`.active`) that scopes the hooks to only fire when the skill is in use
