# Singularity — Self-Containment and Structural Pattern Reference

**Audience:** Claude orchestrator session on the Cisco machine, building a forge-pattern skill for EPNM-to-EMS issue-driven work.
**Source skill:** /home/cmoore/programming/ai_opportunities/.claude/skills/singularity/
**Purpose:** This is the canonical example of a self-contained skill in this repository. Use it as the structural template for the EPNM forge skill. Pair with files 01-04 (DjangoForge analysis) for the workflow logic.

---

## 1. The Complete Frontmatter (Verbatim)

The entire YAML frontmatter from `/home/cmoore/programming/ai_opportunities/.claude/skills/singularity/SKILL.md` (lines 1-17):

```yaml
---
name: singularity
description: |
  Organizes consulting engagements from raw transcripts and context into structured research libraries, client deliverables, and pricing models.
  WHEN to use: new client opportunity, transcript processing, engagement prep, proposal creation, pricing model, discovery organization.
  WHEN NOT to use: internal project work, code implementation, non-consulting tasks.
user-invocable: true
argument-hint: [new|continue|process|deliver|price|discuss]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*), WebSearch, WebFetch, Task
hooks:
  Stop:
    - hooks:
        - type: "command"
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/singularity/scripts/singularity_stop.py"
          timeout: 10000
          statusMessage: "Verifying singularity workflow..."
---
```

### Frontmatter Keys (Every Key, Documented)

| Key | Value | Purpose |
|---|---|---|
| `name` | `singularity` | Skill identifier; matches folder name. |
| `description` | Multi-line block | Two-part trigger: "WHEN to use" / "WHEN NOT to use". This is what the harness routes against. |
| `user-invocable` | `true` | Skill can be invoked as `/singularity` directly by the user. |
| `argument-hint` | `[new\|continue\|process\|deliver\|price\|discuss]` | Hint shown to the user about argument forms. Pipe-separated alternatives in square brackets. |
| `allowed-tools` | `Read, Write, Edit, Glob, Grep, Bash(python3:*), WebSearch, WebFetch, Task` | Comma-separated tool list. Note `Bash(python3:*)` constrains Bash to python3 invocations. `Task` is the agent-spawn tool. |
| `hooks` | Map keyed by hook event name | Inline hook declarations. Defines a Stop hook here. |

---

## 2. How Hooks Are Declared in the Frontmatter

Singularity declares ONE hook: a `Stop` hook. The full structure:

```yaml
hooks:
  Stop:
    - hooks:
        - type: "command"
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/singularity/scripts/singularity_stop.py"
          timeout: 10000
          statusMessage: "Verifying singularity workflow..."
```

### Structure Breakdown

- **Top-level `hooks:` map.** Keyed by hook event name. The known event types in Claude Code: `Stop`, `SessionStart`, `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `SubagentStop`, `PreCompact`, `Notification`. Singularity uses only `Stop`.
- **`Stop:` is a list.** The outer item is a *matcher group*; matcher groups can carry filters (e.g., tool-name matchers for PreToolUse). For Stop, no matcher is needed because there is nothing to match against.
- **Each matcher group has its own `hooks:` list.** This is the inner array that contains the actual hook commands. Yes — the keyword `hooks` appears twice in the path: once as the top-level frontmatter key, once nested inside the matcher group.
- **Each hook entry has four fields:**
  - `type: "command"` — the only documented type; runs a shell command.
  - `command: "..."` — the command string.
  - `timeout: 10000` — milliseconds. 10000 = 10 seconds. The hook is killed if it exceeds this.
  - `statusMessage: "..."` — a message shown to the user while the hook runs. Should be short and active-voice.

### Path Resolution at Runtime

The command uses **`$CLAUDE_PROJECT_DIR`** as the root anchor:

```
python3 $CLAUDE_PROJECT_DIR/.claude/skills/singularity/scripts/singularity_stop.py
```

`$CLAUDE_PROJECT_DIR` is the absolute path to the project root that the user is working in (the `cwd` Claude Code was launched from). At runtime the harness expands this env var and the python interpreter receives an absolute path. This is the **correct way** to reference skill-internal scripts: it is portable across machines and cwd changes.

### Other Hook Types Singularity Could Have Used (Not Currently Used)

For reference when designing the EPNM skill — these are the patterns Singularity does NOT use but could be added with the same structure:

```yaml
hooks:
  SessionStart:
    - hooks:
        - type: "command"
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/<name>/scripts/inject_state.py"
          timeout: 5000
          statusMessage: "Loading skill state..."
  PreToolUse:
    - matcher: "Write"           # only fires on Write tool calls
      hooks:
        - type: "command"
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/<name>/scripts/guard_writes.py"
          timeout: 5000
  PostToolUse:
    - matcher: "Edit"
      hooks:
        - type: "command"
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/<name>/scripts/post_edit_check.py"
          timeout: 5000
```

The `matcher:` field on the matcher group is a tool-name filter (only relevant for PreToolUse / PostToolUse). For Stop, there is no matcher because Stop fires unconditionally at end-of-turn.

---

## 3. The Folder Layout

Top-level layout of `/home/cmoore/programming/ai_opportunities/.claude/skills/singularity/`:

```
singularity/
├── SKILL.md                  (the skill definition + frontmatter, 481 lines)
├── references/               (loaded on demand by SKILL.md flows; behavior + domain rules)
├── scripts/                  (executable Python scripts; one is the stop hook)
├── gold_standards/           (canonical "what good looks like" examples)
│   ├── charts/               (HTML chart examples)
│   ├── deliverables/         (HTML deliverable examples + bridge_document_example.md)
│   └── presentations/        (subfolders per presentation type, each with full deck + README)
├── templates/                (fill-in-the-blank starters)
├── layout_examples/          (HTML slide layout examples; loaded for presentation generation)
├── mermaid_shape_library/    (HTML reference pages for mermaid diagram capabilities)
└── worked_examples/          (full end-to-end engagement examples)
    ├── cisco_team/           (sub-singularity worked example)
    └── lam_research/         (full engagement worked example)
```

### What Each Directory Contains

**`references/`** — 29 markdown files, all behavioral or domain rules. Naming convention: `<topic>.md` (no numeric prefix, no date). Loaded **on demand** by specific flows in SKILL.md (e.g., Flow 4 loads `deliverables_pipeline.md`, `anti_patterns.md`, `professional_standards.md`). One file (`hard_rules.md`) is mandatory-on-every-invocation.

Files (verbatim list):
```
agent_architecture.md            (how Task agents are spawned and prompted)
anti_patterns.md                 (writing patterns to avoid)
bayone_design_spec.md            (HTML/CSS design system)
bayone_team.md                   (team bios, used in deliverables)
blockchain_methodology.md        (append-only research rule)
complete_structure.md            (full engagement folder structure)
deliverables_pipeline.md         (markdown-first → HTML → review pipeline)
document_processing.md           (multi-pass transcript processing)
enforcement_architecture.md      (the Proof via Artifact pattern)
folder_structure.md              (canonical folder layout + naming)
hard_rules.md                    (16 behavioral rules; mandatory on every invocation)
health_check_methodology.md      (audit checklist for Flow 8)
inventory_design.md              (auto-inventory generation design)
mermaid_design_standards.md      (mermaid color palette + standards)
mermaid_flowchart_learnings.md   (mermaid lessons learned)
mermaid_shape_library.md         (quick-reference shape menu)
mermaid_svg_scaling_research.md  (SVG scaling research notes)
nested_singularity.md            (sub-singularity pattern)
people_tracking.md               (per-set people files + org_chart pattern)
playwright_screenshot_research.md (screenshot research notes)
presentation_design_language.md  (21-rule slide design spec)
pricing_workflow.md              (pricing questionnaire and process)
professional_standards.md        (writing standards: no em dashes, etc.)
reorganization_guide.md          (how to reorganize an engagement)
sales_forge_merger.md            (history: singularity replaces sales-forge)
session_continuity.md            (session handoff pattern)
skill_ecosystem.md               (sibling skills relationship)
team_meeting_processing.md       (team meeting processing rules)
tracking_folder_pattern.md       (tracking/ folder update rules)
```

**`scripts/`** — Five Python scripts. Naming convention: snake_case verbs. The stop hook is `singularity_stop.py` (skill-namespaced filename so it does not collide with other skills' stop hooks).
```
flag_ai_patterns.py        (linter for AI writing anti-patterns)
format_transcript.py       (formats raw speech-to-text transcripts before reading)
generate_inventory.py      (auto-regenerates engagement inventory; called by stop hook)
html_to_pdf.py             (converts deliverable HTML to PDF)
singularity_stop.py        (THE STOP HOOK)
```

**`gold_standards/`** — Three subfolders (`charts/`, `deliverables/`, `presentations/`), each containing real-quality reference outputs. Used as **structural** reference, not fill-in-the-blanks. SKILL.md explicitly says "read for style and structure" not "copy". Each subfolder has a `README.md` orienting the reader. `deliverables/` has 27 files (mostly HTML, plus `bridge_document_example.md` and the README).

**`templates/`** — Three files. Used as fill-in-the-blank starters:
```
ProjectCostingTemplate.xlsx     (binary; Excel pricing template)
excel_template_prompt.md        (prompt for Claude-in-Excel session)
methodology_template.md         (the 00_methodology_*.md research file template)
```

**`layout_examples/`** — Nine HTML files demonstrating slide layout patterns + `README.md`. Mandatory pre-read before presentation generation (SKILL.md Flow 7 hard-gates this). Files are named by layout type (`agenda.html`, `chevron_flow_detail.html`, `closing.html`, `grid_takeaway.html`, `profile.html`, `split_concept.html`, `three_column.html`, `title.html`).

**`mermaid_shape_library/`** — Eight numbered HTML files demonstrating every mermaid capability. Loaded together when generating diagrams. Numeric prefix orders the read order (01_classic_shapes through 08_diagram_types_gallery).

**`worked_examples/`** — Two engagements. `lam_research/` shows the full engagement structure (org_chart, source/, research/, planning/, decisions/, deliverables/, progress/). `cisco_team/` shows the sub-singularity pattern (research/, source/, tracking/, planning/, documents/, cross_reference.md, README.md).

---

## 4. Self-Containment Status

**Singularity passes the self-containment audit cleanly.** Use it as the model.

| Check | Status | Evidence |
|---|---|---|
| Hooks defined inside the skill (frontmatter)? | YES | `SKILL.md` frontmatter declares the Stop hook. No reference to `settings.json` for hook wiring. |
| Scripts bundled inside the skill? | YES | All five scripts live in `singularity/scripts/`. The hook command is `$CLAUDE_PROJECT_DIR/.claude/skills/singularity/scripts/singularity_stop.py`. |
| References inside the skill? | YES | All 29 reference markdown files in `singularity/references/`. SKILL.md never references files outside `.claude/skills/singularity/`. |
| Templates inside the skill? | YES | `singularity/templates/` includes the markdown methodology template and the Excel binary. |
| Gold standards inside the skill? | YES | `singularity/gold_standards/` is fully bundled. |
| External skill dependencies (cross-skill references)? | NO | SKILL.md mentions sibling skills (`/big4`, `/pptx-extractor`, `/pdf-extractor`) only as offers to the user. No file-level dependencies. **Hard Rule 10** explicitly forbids cross-skill file dependencies. |

**Hard Rule 10 (verbatim from SKILL.md line 34):**
> 10. **Self-contained skill.** All reference files, templates, and assets live within `.claude/skills/singularity/`. No external dependencies. All reference files, templates, and company context live within `.claude/skills/singularity/`. All rationale, rules, and references must be inside this directory. Never cross-reference session folders, engagement folders, or external paths as authoritative sources from within the skill definition.

**This is the model for the EPNM forge skill.** Everything the skill needs — hooks, scripts, references, templates, examples — lives under `.claude/skills/<skill-name>/`. The only external path the skill writes to or reads from at runtime is `$CLAUDE_PROJECT_DIR/<engagement-folder>/`, which is the user's working data, not part of the skill.

---

## 5. Stop Hook Implementation Pattern

### Script Location
`/home/cmoore/programming/ai_opportunities/.claude/skills/singularity/scripts/singularity_stop.py` (261 lines).

### High-Level Logic (What It Verifies)

The hook is the enforcement engine for the **Proof via Artifact** pattern. It:

1. Reads JSON from stdin (Claude Code passes hook context via stdin).
2. Loop-prevention: exits 0 immediately if `data.get("stop_hook_active")` is true.
3. Locates the active engagement by globbing for `research/00_methodology_*.md` (one, two, and three levels deep from cwd).
4. If no engagement found → exits 0 (legitimate "no work in progress" state).
5. Otherwise picks the most recently modified engagement and walks a checklist:
   - **Check 1:** `org_chart.md` exists if research has progressed beyond methodology (>1 research file).
   - **Check 2:** Per-set summary completion (each set NN has a `NN_summary_*.md` file ≥200 chars, OR is the highest-numbered set with a `.set_NN_in_progress` marker).
   - **Check 3:** `references/hard_rules.md` exists in the skill folder.
   - **Check 4:** Presentation references exist (spec, layout examples, gold standard) **if** presentation HTML exists in the engagement.
   - **Check 5:** `references/nested_singularity.md` exists **if** sub-singularity folders exist.
   - **Check 6:** Chart HTML files contain `class="back-btn"` if `presentations/*/charts/` exists.
6. If any issue found: prints all issues to stderr and exits with code 2.
7. If clean: auto-runs `generate_inventory.py` against the engagement (best-effort; failures swallowed) and exits 0.

### How It Handles "Skill Not Active" Cases

**The hook is skill-scoped via the frontmatter declaration.** Because it lives in the skill's frontmatter, the harness only registers the hook when `singularity` is the active skill in the session. There is no marker file scoping mechanism in this script.

**Additionally**, the hook self-degrades gracefully:
- No engagement folder found → exit 0 (line 134-136).
- `find_skill_dir` returns None → exit 0 (line 169-170).

Combined: the hook is genuinely safe — it only enforces when there is something to enforce.

### Exit Code Semantics

```
0  = OK, proceed (or no work to verify)
2  = BLOCKING ERROR; Claude must fix and re-attempt
```

Exit code 2 is the documented Claude Code mechanism for surfacing the stderr message back to Claude as feedback. Claude then sees the error and is forced to address it before its next response.

### "Proof via Artifact" Pattern (from `references/enforcement_architecture.md`)

> Every required step produces an artifact. The stop hook checks that all required artifacts exist. Missing artifacts block progression with exit code 2. This is the same pattern used in django-forge-v2, proven across dozens of issue implementations. It is deterministic, not behavioral. Claude cannot skip a step because the hook catches the missing artifact regardless of what Claude decided to do.

Key principles (lifted verbatim from `enforcement_architecture.md`):

1. **Artifacts, not transcripts.** Never parse the conversation transcript. Artifacts are reliable proof.
2. **Section headers, not phrases.** Match `## Transcription` not "transcription note".
3. **Pattern matching, not hardcoded filenames.** Match `*_summary_*.md`, not `01_meeting_summary_2026-03-12.md`.
4. **Minimum size checks.** Require minimum char counts (50-200 depending) so empty placeholders fail.
5. **Skill-scoped hooks.** Defined in frontmatter so hook only fires when skill active.
6. **Loop prevention.** Always check `stop_hook_active` first.

### Script Skeleton (Reusable)

```python
#!/usr/bin/env python3
import json, sys
from pathlib import Path

def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active", False):
        sys.exit(0)
    cwd = Path(data.get("cwd", "."))

    # Locate active workspace via marker file
    markers = list(cwd.glob("**/<marker-pattern>"))
    if not markers:
        sys.exit(0)

    issues = []
    # ...checks...
    if issues:
        print("Skill workflow check:\n- " + "\n- ".join(issues), file=sys.stderr)
        sys.exit(2)
    sys.exit(0)

if __name__ == "__main__":
    main()
```

---

## 6. How Agents Are Dispatched

### Agent Prompt Template (Verbatim from SKILL.md lines 200-239)

```
You are writing a detailed decomposition document from a meeting transcript.
Read the transcript, then write one focused output file.

**Your focus:** [ONE SPECIFIC TOPIC - e.g., "Technical use cases and requirements"]

**Read this file:** /<client_name>/<opportunity_name>/source/<transcript_filename>

**Context from the topic map (so you know what to look for):**
[BULLET POINTS from the topic map for this specific topic]

**What to capture in exhaustive detail:**
- Quote or closely paraphrase key statements. Do not summarize. Decompose.
- Capture specific numbers, names, technical details, and claims.
- Note who said what when it matters for context.
- Flag open questions or unresolved points.

**IMPORTANT: Speech-to-text transcript quality.**
This transcript is speech-to-text and full of transcription errors. Use common sense:
- "concept-renade" = "confidential violation"
- "lamb GPT" = "LamGPT"
- "Spacey" = "SpaCy"
- "on pram" = "on-prem"
- "brass beam" = "Brad's team"
- "compiler" = "Copilot"
- "Gapsium" / "Kaptima" = "Capgemini"
Infer intended meaning from context. Do not take mangled words at face value.

**Write your output to:** /<client_name>/<opportunity_name>/research/<set>_<type>_<topic>_<date>.md

**Use this header format:**
# <Set Number> - <Source Type>: <Topic>

**Source:** /<client_name>/<opportunity_name>/source/<transcript_filename>
**Source Date:** <date> (<context>)
**Document Set:** <set number> (<description>)
**Pass:** Focused deep dive on <topic>

---
```

### Spawn Pattern: Single Message, Multiple Tool Calls

From `references/agent_architecture.md`:

```
// Spawn all 5 agents in ONE message
Agent(topic1_prompt)
Agent(topic2_prompt)
Agent(topic3_prompt)
Agent(topic4_prompt)
Agent(topic5_prompt)
```

All Task tool calls go in **one assistant message** to maximize parallelism. The harness runs them concurrently.

### Permissions Handling

**`mode: "bypassPermissions"`** is set on every agent spawn. This is a Task-tool option that lets the agent write files without per-write user approval prompts. It works in concert with the project-level Write permission (see Mandatory Startup below).

### How Agents Write Their Output

Agents **write directly to the engagement folder**. The agent prompt includes the exact target path. Hard Rule 4 (SKILL.md line 28):

> 4. **Agents write their own files.** Deep-dive and research agents write directly to the engagement folder. Use `mode: "bypassPermissions"`. Never fall back to writing in the main session if an agent fails. Report the failure and ask how to proceed.

### What An Agent Receives in Its Prompt

Six required elements (from `references/agent_architecture.md`):

1. The transcript path (agent reads it itself; the main session does not pre-extract).
2. The topic focus (exactly one topic per agent).
3. Context from the topic map (bullet points from the main session's Pass 1 work).
4. Exhaustive detail instructions ("Quote or closely paraphrase. Don't summarize, decompose.").
5. Speech-to-text warning + concrete example mappings.
6. Exact output file path + header template.

### Agent Description Field

Each agent gets a short, descriptive name in the Task `description` field:
```
description: "Deep dive: technical use cases"
description: "Deep dive: what was tried"
description: "Deep dive: infrastructure and access"
```

### Agent Failure Handling

> If an agent fails to write a file:
> - Do NOT fall back to writing the file in the main session. The user explicitly rejected this pattern.
> - Do NOT attempt to extract agent output from temp files with scripts.
> - Report the failure and ask the user how to proceed.

---

## 7. References Organization

**Location:** `.claude/skills/singularity/references/`
**Count:** 29 files
**Naming convention:** `<topic>.md` — no numeric prefix, no date suffix. Topical names so they can be referenced by SKILL.md flows by name.

### Categorized List

**Behavioral / always-loaded:**
- `hard_rules.md` — 16 behavioral rules with violation protocols. Mandatory every invocation. Stop hook verifies existence.

**Workflow rules:**
- `blockchain_methodology.md` — append-only research doc rule
- `document_processing.md` — multi-pass transcript processing
- `agent_architecture.md` — Task agent spawn pattern + prompts
- `session_continuity.md` — handoff between Claude sessions
- `enforcement_architecture.md` — the Proof via Artifact pattern + hook design

**Structure / organization:**
- `folder_structure.md` — canonical engagement folder layout
- `complete_structure.md` — extended structure reference
- `nested_singularity.md` — sub-singularity pattern
- `people_tracking.md` — dual people-tracking system (per-set + org_chart)
- `inventory_design.md` — auto-inventory generation
- `tracking_folder_pattern.md` — tracking/ folder update rules
- `team_meeting_processing.md` — internal team meeting processing
- `reorganization_guide.md` — how to reorganize an existing engagement
- `health_check_methodology.md` — Flow 8 audit checklist

**Domain / company context:**
- `bayone_team.md` — BayOne team bios for deliverables
- `bayone_design_spec.md` — HTML/CSS design system
- `sales_forge_merger.md` — history of merger from sales-forge
- `skill_ecosystem.md` — sibling skill relationships

**Writing standards:**
- `professional_standards.md` — writing rules (no em dashes, etc.)
- `anti_patterns.md` — patterns to avoid

**Pricing:**
- `pricing_workflow.md` — questionnaire and process
- `deliverables_pipeline.md` — markdown-first → HTML pipeline

**Presentation:**
- `presentation_design_language.md` — 21-rule slide spec
- `mermaid_design_standards.md` — palette + standards
- `mermaid_shape_library.md` — quick reference
- `mermaid_flowchart_learnings.md` — lessons learned
- `mermaid_svg_scaling_research.md` — research notes
- `playwright_screenshot_research.md` — research notes

### Loading Pattern

References are not auto-loaded. Each Flow in SKILL.md explicitly says **"Load references: ..."** with absolute paths. Example from Flow 4:

```
**Load references:** `.claude/skills/singularity/references/deliverables_pipeline.md`,
`.claude/skills/singularity/references/anti_patterns.md`,
`.claude/skills/singularity/references/professional_standards.md`
```

This is the model for the EPNM forge skill: name your references topically (no numbering), reference them by absolute path inside SKILL.md flows, and explicitly list which to load per flow.

---

## 8. Templates Organization

**Location:** `.claude/skills/singularity/templates/`
**Count:** 3 files
**Pattern:** Fill-in-the-blank starters that are copied or used as content seeds when creating engagement artifacts.

| File | Type | Used By |
|---|---|---|
| `methodology_template.md` | Markdown | Flow 1 (New Engagement). Copied to `<engagement>/research/00_methodology_<date>.md` with client name and opportunity description filled in. |
| `excel_template_prompt.md` | Markdown | Flow 5 (Pricing). Used as a prompt for a Claude-in-Excel session. |
| `ProjectCostingTemplate.xlsx` | Binary | Flow 5 (Pricing). The actual Excel costing template. |

### Template Content Pattern

The methodology template uses `<PLACEHOLDER>` markers for substitution:
```markdown
# Decomposition Methodology

**Established:** <DATE>
**Engagement:** <CLIENT_NAME> - <OPPORTUNITY_DESCRIPTION>

---

## Blockchain Style Documentation
...
```

Templates are explicitly **NOT** considered gold standards or authoritative references. They are starters that get instantiated per engagement.

---

## 9. The Mandatory-Startup Pattern (Verbatim from SKILL.md lines 67-81)

> ## Mandatory Startup: Permission and Rules Check
>
> **Every invocation, before ANY work, run these checks in order.**
>
> 1. Read `.claude/settings.local.json`
> 2. Verify `Write($CLAUDE_PROJECT_DIR/**)` exists in `permissions.allow`
> 3. Verify `WebSearch` exists in `permissions.allow`
> 4. If either is missing:
>    - Tell the user: "Singularity requires agents to write files autonomously and research agents to search the web. I need to add `Write($CLAUDE_PROJECT_DIR/**)` and/or `WebSearch` to the permissions. May I do that?"
>    - If approved, add the permission
>    - If declined, explain the skill cannot function and stop
> 5. Read `.claude/skills/singularity/references/hard_rules.md`
> 6. If the file does not exist, stop and tell the user: "The behavioral hard rules file is missing. It must exist at `.claude/skills/singularity/references/hard_rules.md` for the skill to function."

### Why This Pattern Works for the EPNM Skill

- **Step 1-4 (permission check):** Verifies the user's environment can support agent-driven writes BEFORE any work that requires them. The check is not buried in a flow; it is the first thing the skill does on every invocation.
- **Step 5-6 (hard rules read):** Forces the rules into context every invocation. The stop hook reinforces this by failing if `hard_rules.md` is missing.
- **Hard gate:** Each step must succeed before proceeding. Failure stops the session with a specific, actionable user prompt.

This is the model for the EPNM forge skill's startup. Adapt the permission set (the EPNM skill might need GitHub or Bash permissions instead of/in addition to Write+WebSearch) but keep the structure.

---

## 10. The "Ask Before Writing" Pattern

This is enforced via prose in SKILL.md and reinforced by Hard Rule B7 in `references/hard_rules.md`. There is no programmatic enforcement of this pattern in the stop hook (the hook checks artifacts that result from the pattern, not the pattern itself).

### Where It Lives in SKILL.md

**Hard Rule 3 (line 27):**
> 3. **Ask, do not assume.** Always propose file lists and get user approval before writing research docs or spawning agents. The user controls what gets created. Different meetings warrant different breakdowns.

**Flow 3 step 4-5 (transcript processing):**
> 4. **Pass 1 continued: Topic map.** Identify major topics. Write topic map with proposed deep-dive files AND rationale for why each needs its own file. Present to user.
> 5. **Ask user.** Get approval on the file list. User may adjust, add, or remove files.

### Where It Lives in `references/hard_rules.md`

**Rule B6 (Do not reinvent proven structure):** When the user has pointed to a reference structure, replicate it. Do not ask whether to use it.

**Rule B7 (Align on structure before producing documents):**
> Before producing any non-trivial deliverable, propose an outline or structural plan and get user approval. This applies to HTML documents, markdown deliverables, proposals, summaries, and presentations. Skipping to production wastes the user's time reviewing work that may be structurally wrong. The outline step is non-negotiable for anything substantial.

### Enforcement Strength

- **Text only.** The skill relies on Claude reading and following the rule.
- **Indirect hook reinforcement:** The stop hook does not block on "did you ask?" but it DOES block on "did the produced artifacts have the required structure / minimum content?". So if Claude skips the asking step and writes garbage, the hook catches the symptom.
- **Behavioral rule violation protocol** (`hard_rules.md` lines 43-52): If the user calls out a violation, Claude must stop, re-read `hard_rules.md`, acknowledge the rule by number, and correct course.

For the EPNM forge skill, consider adding programmatic enforcement: a marker file like `.plan_approved` written when the user approves the plan, and a PreToolUse hook on Write that blocks writes to specific folders unless the marker exists.

---

## 11. What Patterns the EPNM Forge Skill Should Carry Directly

### Lift Verbatim (Copy as-is, adapt only the skill name)

- **Frontmatter Stop hook structure** — the entire `hooks: Stop:` block. Change only the script path:
  ```yaml
  hooks:
    Stop:
      - hooks:
          - type: "command"
            command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/<epnm-forge>/scripts/<epnm_forge>_stop.py"
            timeout: 10000
            statusMessage: "Verifying <epnm-forge> workflow..."
  ```
- **Folder layout** — `references/`, `scripts/`, `gold_standards/`, `templates/`, `worked_examples/`. Add other top-level folders (`layout_examples/`, `mermaid_shape_library/`) only if the skill produces visual artifacts of those types.
- **Mandatory Startup section** in SKILL.md — same six-step structure (permission check → rules read), with adjusted permission set for the EPNM workflow.
- **Stop hook script skeleton** — the loop-prevention check, the `data = json.load(sys.stdin)` pattern, the marker-glob discovery, the issues-list/exit-2 reporting, the auto-degrade-on-no-workspace pattern.
- **Proof via Artifact principle** — every required step produces an artifact; hook verifies artifacts exist, not transcripts.
- **Self-containment Hard Rule** — the explicit prose forbidding cross-skill file dependencies.
- **Agent prompt template structure** — six required elements (target path, focus, context, detail instructions, format guidance, output path + header). Adapt the actual prompt text to the EPNM domain.
- **Single-message agent dispatch** — all parallel Task calls in one message.
- **`mode: "bypassPermissions"`** on every agent spawn.

### Lift With Adaptation

- **References organization** — topical filenames, no numeric prefix. Adapt the actual file set to the EPNM domain. Carry forward `hard_rules.md` (always-loaded), `enforcement_architecture.md` (designer-facing doc), and a domain-rules equivalent of `blockchain_methodology.md`.
- **Templates organization** — fill-in-the-blank starters with `<PLACEHOLDER>` markers. The EPNM skill will need its own templates (issue spec template, PR description template, etc.).
- **Gold standards organization** — three subfolders by output type (charts/deliverables/presentations for Singularity). EPNM will likely have different output types: e.g., `gold_standards/issues/`, `gold_standards/prs/`, `gold_standards/code/`.
- **Worked examples** — at least one full end-to-end example. Singularity has `worked_examples/lam_research/`. The EPNM skill should have a comparable worked example showing one issue from intake to merged PR.
- **Hard Rules behavioral file** — keep the format (numbered B1-BN, "Why" footnotes, violation protocol). Replace the Singularity-specific rules with EPNM-specific ones (e.g., never push to main without review, always run tests before declaring done).

### Singularity-Specific (DO NOT lift to the EPNM skill)

- **Multi-pass transcript processing methodology.** Specific to consulting transcript work; not applicable to issue-driven engineering.
- **Blockchain-style append-only research docs.** Conceptually adjacent (immutable history) but the specific numbering convention (`01`, `02`, `02a`, `01-02_changes_*`) is for chronological meeting events, not for engineering artifacts.
- **Speech-to-text correction list** in agent prompts. Replace with engineering-specific guidance (e.g., framework version awareness, library freshness checks).
- **The eight Flows** (New / Continue / Process Source / Deliver / Price / Discuss / Present / Audit). The EPNM skill will have its own flows; adapt the **structure** (numbered flows with explicit "Questions to ask" / "Actions" / "Load references" sections) but not the content.
- **People tracking + org_chart pattern.** Specific to client engagements with named individuals. The EPNM skill cares about authors and reviewers, not about org-chart-style tracking.
- **Set-completion logic** in the stop hook. The EPNM skill will have a different completion notion (e.g., "issue has explore.md, plan.md, implementation, tests, PR" rather than per-set summary docs). Reuse the **mechanism** (group artifacts by prefix, require minimum content) but redefine the **groups**.
- **Mermaid + presentation libraries.** Only relevant if the EPNM skill produces visual deliverables, which is unlikely for issue-driven dev work.
- **Sub-singularity pattern.** The "nested skill instance" pattern is unusual. Most engineering workflows do not need it. Skip unless a clear use case emerges.

---

## Closing Note for the Receiving Session

Singularity's strength is that **it is auditable from the outside**. A reader who has never used the skill can:

1. Read SKILL.md and understand the rules and flows.
2. Look at the frontmatter and know exactly what hook fires when.
3. Read the stop hook script and know exactly what is verified.
4. Walk `worked_examples/lam_research/` and see the methodology in practice.
5. Read `references/enforcement_architecture.md` and understand the design philosophy.

Pursue the same property in the EPNM forge skill. If a future maintainer cannot answer "what does this skill do, and what guarantees does it enforce?" by reading the skill folder alone, the self-containment is broken.
