# DjangoForge v2 — Scripts and Hooks Deep-Dive

**Audience:** Claude orchestrator session on the Cisco machine.
**Source skill:** /home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/
**Purpose:** Operational reference for the compliance enforcement layer. Pair with the anatomy audit (file 01) and the workflow document (file 02).

---

## 0. Important Discovery About Hook Location

The DjangoForge v2 SKILL.md frontmatter does **not** declare hooks inline. The frontmatter only contains `name`, `description`, and `argument-hint`. The hooks are implemented as separate scripts under `~/.claude/hooks/` and registered in `~/.claude/settings.local.json` (or `~/.claude/settings.json` for project-scoped registration).

The scripts that implement the v2 hook layer:

```
/home/cmoore/programming/talent_ai/.claude/hooks/
├── django-forge-v2-pretooluse.py        (PreToolUse, matcher: Bash)
├── django-forge-v2-sessionstart.sh      (SessionStart, source: compact)
└── django-forge-v2-stop.py              (Stop)
```

All three implement the **skill-marker pattern**: each one early-exits with status 0 unless `<main_repo>/.django-forge-v2/.active` exists. This means hooks are globally registered but scoped per-session via a marker file the skill creates on activation and deletes on completion. This is the v2 mechanism that lets the skill "turn its enforcement on and off" without modifying settings.json each time.

The orchestrator session on the Cisco machine, when designing an EPNM-equivalent, should plan to:
1. Place the hook scripts under `~/.claude/hooks/` (or a project `.claude/hooks/` folder).
2. Register them in `settings.local.json` with the appropriate event types.
3. Have the skill drop a marker file (e.g. `.epnm-forge/.active`) on activation, and have each hook check for that marker first.

---

## 1. trace_dependencies.py — Line-by-Line Walkthrough

### 1.1 Purpose

**Plain English:** When a GitHub issue depends on prior issues (and those depend on still earlier issues), this script walks the chain to produce an ordered list of issues to read first. It also supports a date-cutoff alternative for cases where the dependency graph is implicit (everything since project epoch). It exists to **prevent the bad pattern of "just grab the most recent N issues"** — a heuristic that produced incorrect context in the v1 skill.

**Technical:** A CLI utility that interrogates GitHub via the `gh` CLI, parses issue bodies for dependency markers (`Depends on #N`, `Blocked by #N`, `After #N`, `Requires #N`, `Prerequisite: #N`), and emits either a topologically ordered (root-first) JSON list of issue numbers via recursive traversal, or a chronologically sorted (oldest-first) list of issues created after a given date.

### 1.2 Inputs

**CLI arguments:**

```python
parser.add_argument("--method", choices=["recursive", "date", "auto"], required=True)
parser.add_argument("--issue", type=int, help="Starting issue number (for recursive/auto)")
parser.add_argument("--after", help="Date cutoff in YYYY-MM-DD format (for date method)")
parser.add_argument("--output", choices=["json", "text"], default="json")
```

- `--method recursive --issue 1190` → walk dependencies starting at #1190
- `--method date --after 2026-01-01` → all issues created after the date
- `--method auto --issue 1190` → try recursive; if no deps found, return single-issue list

**Environment:**
- Inherits `GH_TOKEN` / GitHub CLI auth from caller. Script does not read env vars directly.
- Requires `gh` CLI in `PATH` and an authenticated session in the current repo.

**Files read:** None. All input comes from `gh` API responses parsed as JSON.

### 1.3 Outputs

**stdout (JSON mode, default):** A single JSON array of integers, e.g. `[905, 1185, 1190]`.

**stdout (text mode):** One line per issue, formatted `#NNN`.

**stderr:** Status messages — method used, count of issues found, errors fetching individual issues. Designed to be captured separately from the machine-readable stdout.

**Exit codes:** Only `0` is emitted on success. `argparse` will exit non-zero on invalid arguments. The script does not treat `gh` failures as fatal — it logs to stderr and falls back where possible.

### 1.4 Key Functions, Annotated

**`run_gh_command(args)` — gh wrapper:**

```python
def run_gh_command(args: list[str]) -> dict | list | None:
    try:
        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout) if result.stdout.strip() else None
    except subprocess.CalledProcessError as e:
        print(f"Error running gh command: {e.stderr}", file=sys.stderr)
        return None
    except json.JSONDecodeError:
        return None
```

Single point of integration with `gh`. All `gh` calls return parsed JSON or `None`. Failure is non-fatal — caller decides what to do with `None`.

**`extract_dependencies(issue_body)` — regex parser:**

```python
patterns = [
    r'[Dd]epends\s+on\s+#(\d+)',
    r'[Bb]locked\s+by\s+#(\d+)',
    r'[Aa]fter\s+#(\d+)',
    r'[Rr]equires\s+#(\d+)',
    r'[Pp]rerequisite[s]?\s*:\s*#(\d+)',
]
dependencies = set()
for pattern in patterns:
    matches = re.findall(pattern, issue_body)
    for match in matches:
        dependencies.add(int(match))
return sorted(list(dependencies))
```

This is the convention enforcement: dependency relationships in issue bodies must use one of these five textual forms. The set is sorted before returning so ordering is deterministic. Note that the script does NOT parse GitHub's native "Linked Issues" field (the cross-reference graph) — only free-text patterns. This is a deliberate choice: it forces issue authors to write dependencies explicitly in prose where humans (and Claude reading the issue) will see them.

**`trace_recursive(issue_number, visited)` — depth-first walker with cycle detection:**

```python
def trace_recursive(issue_number: int, visited: set[int] = None) -> list[int]:
    if visited is None:
        visited = set()
    if issue_number in visited:
        return []
    visited.add(issue_number)

    issue_data = run_gh_command([
        "issue", "view", str(issue_number),
        "--json", "number,title,body"
    ])
    if not issue_data:
        print(f"Could not fetch issue #{issue_number}", file=sys.stderr)
        return [issue_number]

    body = issue_data.get("body", "")
    dependencies = extract_dependencies(body)

    result = []
    for dep in dependencies:
        if dep not in visited:
            result.extend(trace_recursive(dep, visited))
    result.append(issue_number)  # Add current AFTER deps -> roots first
    return result
```

Key correctness points:
- `visited` set prevents infinite loops on cyclic dependency graphs.
- Current issue is appended **after** recursing into deps, producing root-first order suitable for "read these in order" guidance.
- If `gh issue view` fails for an issue, it is included alone (degraded mode rather than crash).

**`trace_date_based(after_date)` — server-side date filter:**

```python
def trace_date_based(after_date: str) -> list[int]:
    issues = run_gh_command([
        "issue", "list",
        "--state", "all",
        "--search", f"created:>{after_date}",
        "--limit", "200",
        "--json", "number,title,createdAt"
    ])
    if not issues:
        return []

    def parse_date(issue):
        created_str = issue.get("createdAt", "")
        try:
            return datetime.fromisoformat(created_str.replace('Z', '+00:00'))
        except ValueError:
            return datetime.min.replace(tzinfo=timezone.utc)

    issues.sort(key=parse_date)
    print(f"Found {len(issues)} issues created after {after_date}", file=sys.stderr)
    return [issue["number"] for issue in issues]
```

Filter happens server-side via the GitHub search API (`--search "created:>DATE"`). `--limit 200` is described in a comment elsewhere as "a safety net, not the primary filter." Output is sorted oldest-first, matching the consumption pattern (read history forward).

**`auto_trace(issue_number)` — fallback chain:**

```python
def auto_trace(issue_number: int) -> list[int]:
    result = trace_recursive(issue_number)
    if len(result) > 1:
        print(f"Method: Recursive chain (found {len(result)} issues)", file=sys.stderr)
        return result
    print(f"Method: Single issue (no dependencies found)", file=sys.stderr)
    return result
```

Always tries recursive first. If that returns only the input issue, it just returns that. There is a comment "Could extend to check for related PRs, labels, etc." indicating planned enhancement — not currently implemented.

### 1.5 When Invoked in the Workflow

Per SKILL.md Phase 3 (Codebase Exploration), the dependency trace is run at the start of "Read Related PRs Deeply." The skill text:

> "From issue text and dependency chain, identify all related PRs."

The recursive trace is the canonical way to derive that list. The script is invoked manually by Claude as a Bash call — there is no hook that fires it automatically.

### 1.6 Failure Behavior

Non-zero exit only on argparse errors. All `gh` failures are logged to stderr; the script continues with degraded results (single-issue lists, empty lists). This is a deliberate choice — Claude can see the stderr noise and decide whether to retry.

The script does not raise; it does not produce alarming exit codes that would propagate upward. The compliance value is in **what it refuses to do** — there is no code path that returns a "top N" or "most recent" result regardless of relationship to the input issue.

### 1.7 External Dependencies

- Python 3.10+ (uses `list[int]`, `dict | list | None` PEP 604 union types).
- `gh` CLI in `PATH`, authenticated.
- Standard library only: `argparse`, `json`, `re`, `subprocess`, `sys`, `datetime`.

No third-party Python packages required. Self-contained.

### 1.8 The "Recursive Chain OR Date-Based" Pattern — Where Implemented

SKILL.md states v2 supports only two retrieval methods. The script is the implementation:

| Pattern | Function | Activation |
|---|---|---|
| Recursive chain | `trace_recursive()` | `--method recursive` or `--method auto` |
| Date-based | `trace_date_based()` | `--method date` |

There is **no third method**, and the PreToolUse hook (see Section 3.1) actively blocks the third method ("top N" via `gh issue list --limit 50`). The pair — script that only knows the two valid methods, plus hook that blocks the invalid one — is the enforcement.

### 1.9 Adaptation Guidance for EPNM-to-EMS

**Reusable as-is:** The structure of the script — argparse interface, gh wrapper, regex-based dependency extraction, recursive walker, date-based fallback — transfers cleanly.

**Adaptations needed:**

1. **Issue tracker.** The Cisco engagement may use Jira or an internal tracker rather than GitHub. Replace the `gh` CLI with the appropriate Jira REST call (or `jira-cli`). The function shape stays the same: `run_tracker_command(args) -> dict | list | None`.

2. **Dependency markers.** The five regex patterns are GitHub-issue-body-text conventions. Cisco teams may use Jira link types (`is blocked by`, `depends on` as native Jira link relationships) which require a different fetch path — read the linked-issues array rather than parsing prose.

3. **Multi-repo dimension.** EPNM-to-EMS spans 14 repos. The recursive walker may need to track which repo a given issue lives in (currently it assumes one repo, the cwd). Consider extending the visited set from `set[int]` to `set[tuple[repo, issue_id]]`.

4. **Date epoch.** The default project epoch in DjangoForge is `2026-01-01` (Search Architecture start). The Cisco equivalent should use the EPNM-to-EMS project kickoff date.

---

## 2. verify_branch_sync.sh — Line-by-Line Walkthrough

### 2.1 Purpose

**Plain English:** Before we look at code to plan an issue, make sure our local copy is up to date with what's on the remote. If a colleague merged something five minutes ago, we need to pull it before reasoning about "what the code looks like" — otherwise our Issue vs Reality check is wrong.

**Technical:** A bash script that fetches the remote, compares `HEAD` to `@{upstream}` via `git rev-parse` and `git merge-base`, and exits with code 2 (the Claude Code "blocking error" code) if the local branch is behind or has diverged from the remote.

### 2.2 Inputs and Outputs

**Input:** Single optional positional argument — the path of the worktree to check. Defaults to the current directory.

```bash
WORKTREE_PATH="${1:-.}"
cd "$WORKTREE_PATH"
```

**Output:** Human-readable text to stdout describing what was checked and the verdict. The final line is always `STATUS: PASS` or `STATUS: FAIL`.

**Exit codes:**

| Code | Meaning |
|---|---|
| 0 | Branch is current (up to date, ahead, or no upstream) |
| 1 | Script error (set by `set -euo pipefail` on unexpected failure) |
| 2 | Branch is behind remote OR diverged from remote |

### 2.3 Checks Performed

```bash
set -euo pipefail
WORKTREE_PATH="${1:-.}"
cd "$WORKTREE_PATH"

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
git fetch --quiet
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse "@{upstream}" 2>/dev/null || echo "")
```

After fetching, the script captures three SHAs:
- `LOCAL` — the SHA at HEAD of the local branch.
- `REMOTE` — the SHA at HEAD of the upstream tracking branch (empty if no upstream configured).
- `BASE` — `git merge-base HEAD "@{upstream}"`, the most recent common ancestor.

Decision matrix:

```bash
if [[ -z "$REMOTE" ]]; then
    # No upstream configured -> PASS with warning
elif [[ "$LOCAL" == "$REMOTE" ]]; then
    # Up to date -> PASS
elif [[ "$LOCAL" == "$BASE" ]]; then
    # Local is the merge-base -> we are strictly behind -> FAIL exit 2
elif [[ "$REMOTE" == "$BASE" ]]; then
    # Remote is the merge-base -> we are strictly ahead -> PASS
else
    # Neither is the merge-base -> diverged -> FAIL exit 2
fi
```

### 2.4 What "Synced" Means Here

**PASS conditions:**
- `LOCAL == REMOTE` — strict equality, nothing new on either side.
- `REMOTE == BASE` — local has commits the remote doesn't, but remote has nothing new (ahead is fine because we will push later).
- No upstream branch configured (script cannot know, assumes PASS with a warning).

**FAIL conditions:**
- `LOCAL == BASE` — remote has commits we don't have. We are behind. Must `git pull`.
- Neither equals BASE — both sides have unique commits. Must `git pull --rebase` to reconcile.

Note that "ahead" passes because the script's job is to ensure the planning step happens against current code; having unpushed local commits doesn't violate that.

### 2.5 When It Runs

Invoked in Phase 1 of the workflow, after worktree creation, as documented in SKILL.md:

```bash
.claude/skills/django-forge-v2/scripts/verify_branch_sync.sh
```

The Stop hook (Section 3.3) requires `phase_01_setup/branch_sync_verified.md` to exist before any later phase can complete. So in practice, Claude must run this script and write a file documenting the result before moving to Phase 2.

### 2.6 Failure Mode

When exit 2:
1. `set -euo pipefail` and the explicit `exit 2` cause the parent shell to see the failure.
2. The script prints to stdout an explicit remediation:
   ```
   You must pull the latest changes before proceeding:
     git pull
   This ensures Issue vs Reality comparison is against current code.
   STATUS: FAIL (behind remote)
   ```
3. Claude receives the failure and must remediate (run `git pull` or `git pull --rebase`) and re-run the script.
4. The Stop hook will continue to block phase progression because `branch_sync_verified.md` will not have been written with success content.

### 2.7 Environment Requirements

- Bash 4+ (`[[ ]]`, `${1:-.}`).
- `git` 2.0+ with `@{upstream}` syntax support.
- A configured remote tracking branch (otherwise the script passes with a warning rather than failing).
- Network access to the git remote for `git fetch`.

### 2.8 Adaptation Guidance for EPNM-to-EMS

**Reusable as-is:** The git-level comparison logic transfers cleanly. The exit-code contract (0 / 2) and the human-readable output format are language-agnostic.

**Adaptations needed:**

1. **Multi-repo extension.** EPNM-to-EMS spans **14 repos**. The current script checks one. The Cisco equivalent should iterate over the 14 repos and check each `agentic UI conversion` branch (or whatever the active integration branch is named) against `develop` (or the canonical base branch for that repo).

   Pseudocode shape:
   ```bash
   FAILED_REPOS=()
   for repo in /home/cmoore/cisco/epnm-repos/*; do
       (cd "$repo" && verify_one_repo "$repo") || FAILED_REPOS+=("$repo")
   done
   if [ ${#FAILED_REPOS[@]} -gt 0 ]; then
       echo "FAIL: ${#FAILED_REPOS[@]} repos out of sync"
       printf '  - %s\n' "${FAILED_REPOS[@]}"
       exit 2
   fi
   ```

2. **Branch naming.** The DjangoForge script uses whatever branch is checked out. The Cisco equivalent likely needs to verify a specific branch is checked out (e.g., `agentic-ui-conversion`) and that base reference (likely `develop` rather than `main`) is current. Consider adding required-branch and required-base parameters.

3. **Output artifact.** DjangoForge expects `phase_01_setup/branch_sync_verified.md` to exist (see Stop hook). The Cisco equivalent should produce an analogous artifact, possibly listing the per-repo status so the Stop hook can verify all 14 are current.

---

## 3. Hooks — Implementation Detail

The DjangoForge v2 hooks are not declared in SKILL.md frontmatter. They are external scripts. This section documents each one as if the orchestrator session needs to register the equivalents in `~/.claude/settings.local.json` for the Cisco machine.

### 3.1 PreToolUse Hook — `django-forge-v2-pretooluse.py`

**Hook type:** `PreToolUse`
**Matcher:** `Bash` (only checks Bash tool calls)
**Trigger:** Every time Claude attempts a Bash call while the skill marker exists.
**Command:** `python3 /home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-pretooluse.py`
**Recommended timeout:** 10 seconds.

**Status message / decision protocol:** On block, the hook writes a JSON object to stdout:

```python
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": " | ".join(violations)
    }
}
print(json.dumps(output))
sys.exit(0)
```

It does not use exit code 2 — instead it uses the structured `permissionDecision: deny` mechanism so Claude sees a permission denial rather than a tool error.

**What it enforces:**

The hook reads the proposed Bash command and runs three checks. Each check is a function returning either `None` (no violation) or a string (violation message).

**Check 1 — sed prohibition:**

```python
def check_sed_command(command: str) -> str | None:
    if re.search(r'\bsed\b', command):
        return "Use the Edit tool instead of sed. Django-forge-v2 prohibits sed."
    return None
```

Rationale per SKILL.md Hard Rule 2: "No sed command - Use Edit tool. PreToolUse hook blocks sed." sed is hard to audit and easy to misuse for in-place file mutation that bypasses the structured Edit tool.

**Check 2 — Python replace patterns:**

```python
patterns = [
    r'python.*-c.*\.replace\(',
    r'python.*-c.*re\.sub\(',
    r"python.*-c.*open\(.*write",
]
```

Catches one-liner Python invocations that mutate files. Same rationale as sed — these bypass the Edit tool's structured changes. SKILL.md Hard Rule 4: "No Python replace scripts without permission."

**Check 3 — arbitrary retrieval:**

```python
if 'gh issue list' in command and '--limit' in command:
    limit_match = re.search(r'--limit\s+(\d+)', command)
    if limit_match:
        limit = int(limit_match.group(1))
        if limit >= 10 and limit % 5 == 0:
            return f"Arbitrary retrieval detected (--limit {limit})..."
```

Heuristic: limits ≥ 10 that are round multiples of 5 (10, 15, 20, 25, 50, 100) are treated as arbitrary "top N" pulls. Limits like 7 or 13 (idiosyncratic, presumably specific) pass through. This is the enforcement counterpart to the trace_dependencies.py script.

**Skill-marker gate (front of hook):**

```python
marker = main_repo / ".django-forge-v2" / ".active"
if not marker.exists():
    sys.exit(0)  # Skill not active, don't block
```

This is the universal "is the skill active?" check. The hook is global but only fires when the skill has marked itself active.

**Failure mode:** Returns `permissionDecision: deny` with a human-readable reason. The user (orchestrator) sees the denial and the reason. Bash call does not execute.

**Reusable as-is:** The skill-marker pattern and the JSON-deny output mechanism transfer directly.

**Adaptations for EPNM:**
- Drop the `sed` rule? Likely keep — same rationale applies to Java/TypeScript editing.
- Drop the Python-replace rule? Replace with **JavaScript replace patterns** (e.g., `node -e "...replaceAll..."` ) and Java-equivalent in-place mutations.
- Replace `gh issue list --limit` with the equivalent retrieval check for whatever issue tracker Cisco uses.
- Marker path becomes `.epnm-forge/.active` (or whatever the skill is named).

### 3.2 SessionStart Hook — `django-forge-v2-sessionstart.sh`

**Hook type:** `SessionStart`
**Trigger condition:** Source equals `compact` (i.e., session is resuming after auto-compaction).
**Command:** `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-sessionstart.sh`
**Recommended timeout:** 30 seconds (involves multiple subprocess calls and a Python heredoc).

**Status message / output mechanism:** The hook writes plain text to stdout. Anything written is **injected into the conversation context** at session resume — this is the re-injection mechanism.

**What it does:**

1. Reads the JSON input from stdin to extract `cwd` and `source`.
2. Early-exit if `source != "compact"`.
3. Resolve the main repo path via `git rev-parse --git-common-dir` (worktree-aware).
4. Check skill marker `<main_repo>/.django-forge-v2/.active`. Early-exit if missing.
5. Walk all `.django-forge-v2/issue-*/orchestration/state.json` files looking for one whose `worktree_path` matches the current worktree (multi-session aware).
6. Read that session's state.json and emit a formatted context block.

**Re-injected context format:**

```
============================================================
DJANGO-FORGE-V2 SESSION RESUMED AFTER COMPACTION
============================================================

Issue: #1190 - <title>

Current Phase: implementation
Completed Phases: setup, docs, codebase, planning, approval

BUILDING: Boolean group UI for JobDivaCandidateSearch
NOT BUILDING: CandidateHybridSearch modifications

Files being modified:
  - integrations/jobdiva/search/group_converter.py
Files NOT to touch:
  - recruitment/candidates/services/hybrid_search.py

CRITICAL LEARNINGS:
  * Issue text was OUTDATED - written before PRs 1356/1377/1407 merged
  * JobDivaCandidateSearch is the NEW system, not CandidateHybridSearch

Implementation Status (Wave 2):
  Completed: TASK-001, TASK-002, TASK-003
  Pending: TASK-004, TASK-005

User Decisions Recorded:
  - plan_approved: True

Agent Mode: teams

Session Folder: /home/.../.django-forge-v2/issue-1190

============================================================
Read state.json for full context. Continue from current phase.
============================================================
```

**What is "compaction"?**

When a Claude Code session approaches its context window limit, the harness automatically compacts older messages — replacing them with a summary. This is lossy. The "what we are NOT building" warnings, the "files NOT to touch" lists, and the "issue text was OUTDATED" learnings are exactly the kind of disambiguating context that gets summarized away first.

**Why is this needed for forge workflows?**

Forge sessions are long. Implementation of a HIGH-complexity issue can span 200,000+ tokens of context across exploration, planning, judging, and rework. Compaction during such a session, without re-injection, would cause Claude to forget the load-bearing constraints — which then leads to the kind of "drift back to outdated issue text" failure that motivated v2.

The re-injection lets Claude treat compaction as if a new fully-informed session was just started — state.json is the durable source of truth, and the hook reads it back every time the harness compacts.

**Failure mode:** Exit 0 silently if no skill marker, no matching session, or unparseable state. This is correct: if the session has no forge context to re-inject, the hook should be a no-op.

**Reusable with adaptation:** The pattern (state.json + compact-source-detection + stdout re-injection) is fully transferable. The adaptations are cosmetic:
- State.json schema changes (add per-repo status, branch-per-repo, EPNM-specific fields).
- Marker path changes.
- The "BUILDING / NOT BUILDING" framing transfers verbatim — equally important for UI conversion work where it is easy to mistake one Angular component for another.

### 3.3 Stop Hook — `django-forge-v2-stop.py`

**Hook type:** `Stop`
**Trigger condition:** Fires whenever Claude's turn ends.
**Command:** `python3 /home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-stop.py`
**Recommended timeout:** 30 seconds.

**What it does:**

1. Reads stdin JSON, checks `stop_hook_active` to avoid recursion.
2. Resolves main repo and current worktree (worktree-aware via `git rev-parse --git-common-dir`).
3. Checks skill marker. Exit 0 if absent.
4. Locates the active session by matching `state.json:worktree_path` to the current worktree.
5. Reads `current_phase` from state.json.
6. Determines all phases that come **before** the current phase.
7. For each prior phase, checks that the required artifacts exist and meet minimum size.
8. If any artifacts are missing, prints a workflow violation to stderr and exits 2.

**The phase artifact map (the contract):**

```python
{
    "setup": {
        "files": [
            "phase_01_setup/issue_fetched.json",
            "phase_01_setup/worktree_created.md",
            "phase_01_setup/branch_sync_verified.md",
        ],
        "min_size": 50,
    },
    "docs": {
        "files": ["phase_02_docs/docs_findings.md"],
        "min_size": 100,
    },
    "codebase": {
        "files": [
            "phase_03_codebase/codebase_state.md",
            "phase_03_codebase/issue_vs_reality.md",
        ],
        "min_size": 200,
    },
    "planning": {
        "files": [
            "phase_04_planning/task-manifest.md",
            "phase_04_planning/technical-design.md",
        ],
        "min_size": 100,
    },
    "approval": {
        "files": [],
        "min_size": 0,
        "check_state": "user_approved",
    },
    "implementation": {
        "files": [],
        "min_size": 0,
        "check_judge_evaluations": True,
    },
    "testing": {
        "files": ["phase_07_testing/test_results.md"],
        "min_size": 50,
    },
    "git": {
        "files": [
            "phase_08_git/pr_description.md",
            "phase_08_git/final_commit.md",
        ],
        "min_size": 50,
    },
}
```

Two phases use non-file checks:

**Approval check:**

```python
for decision in state.get("user_decisions", []):
    if isinstance(decision, dict):
        if decision.get("decision") == "plan_approved" and decision.get("value"):
            approved = True
            break
    elif isinstance(decision, str):
        if decision == "plan_approved":
            approved = True
            break
if not approved:
    issues.append("User approval not recorded in state.json")
```

The approval gate is a state.json field, not a file. This forces Claude to write state.json explicitly when the user approves, rather than confabulating "they said yes."

**Implementation judge-evaluation check:**

```python
if artifacts.get("check_judge_evaluations"):
    completed_tasks = state.get("completed_tasks", [])
    judge_dir = session_dir / "phase_06_implementation" / "judge-evaluations"
    if completed_tasks:
        if not judge_dir.exists():
            issues.append("Missing judge-evaluations/ folder")
        else:
            for task in completed_tasks:
                eval_file = judge_dir / f"judge_evaluation_{task}.md"
                if not eval_file.exists():
                    issues.append(f"Missing judge evaluation for {task}")
```

Every task marked completed in state.json must have a corresponding `judge_evaluation_TASK-NNN.md` file. This forces the "every task gets reviewed" workflow rule — Claude cannot mark a task done without the Judge agent evaluating it.

**Failure output (exit 2):**

```python
print("DJANGO-FORGE-V2 WORKFLOW VIOLATION", file=sys.stderr)
print("=" * 40, file=sys.stderr)
print(f"Cannot proceed with phase '{current_phase}'.", file=sys.stderr)
print("Previous phases have missing artifacts:", file=sys.stderr)
print("", file=sys.stderr)
for issue in all_issues:
    print(issue, file=sys.stderr)
print("", file=sys.stderr)
print("Complete these artifacts before continuing.", file=sys.stderr)
sys.exit(2)
```

**What exit code 2 does in Claude Code:**

In the Claude Code Stop-hook protocol, exit 2 is a **blocking error** that prevents the session from ending its turn cleanly. The stderr message is fed back into the conversation as feedback to Claude. So on exit 2 the orchestrator session sees:

> "DJANGO-FORGE-V2 WORKFLOW VIOLATION
> Cannot proceed with phase 'planning'.
> Previous phases have missing artifacts:
> Phase 'codebase' incomplete:
>   - Missing: phase_03_codebase/issue_vs_reality.md"

And must remediate. This is the "hooks with exit code 2 instead of relying on text saying MUST" mechanism mentioned in SKILL.md.

**Reusable with adaptation:**

The gate-checker pattern transfers fully. Adaptations:
- Phase list and artifact map change to reflect EPNM workflow phases.
- "Approval" pattern (state-based gate) transfers verbatim.
- "Judge evaluation" pattern transfers if Cisco equivalent uses a Judge agent; if not, drop or replace with a different per-task validation.

---

## 4. The Compliance Enforcement Model — Synthesis

### 4.1 Violations the System Catches

| Violation | Catch mechanism | Phase |
|---|---|---|
| Skipping setup (worktree, branch sync) | Stop hook misses `branch_sync_verified.md` | Any phase after setup |
| Skipping docs reading | Stop hook misses `docs_findings.md` | Any phase after docs |
| Skipping Issue vs Reality check | Stop hook misses `issue_vs_reality.md` | Any phase after codebase |
| Planning without spec artifacts | Stop hook misses `task-manifest.md` or `technical-design.md` | Any phase after planning |
| Implementing without user approval | Stop hook misses `plan_approved` in state.json | Implementation onward |
| Marking task done without Judge eval | Stop hook misses `judge_evaluation_TASK-X.md` | Implementation onward |
| Skipping testing | Stop hook misses `test_results.md` | Git phase |
| Using sed | PreToolUse hook denies | Any time |
| Using Python replace | PreToolUse hook denies | Any time |
| Arbitrary "top 50 issues" | PreToolUse hook denies | Any time |
| Branch out of sync at start | `verify_branch_sync.sh` exits 2 | Setup phase |
| Outdated context after compaction | SessionStart hook re-injects state.json | Any time after compaction |

### 4.2 What the User / Orchestrator Experiences

**On a Stop-hook violation (exit 2):**
The session does not end Claude's turn. Instead, Claude receives the stderr message as feedback and must address the listed missing artifacts before the next stop attempt succeeds. From the user's terminal, they see Claude continue working — writing the missing files — rather than completing.

**On a PreToolUse denial:**
The Bash call returns a permission-denied response with the violation reason. Claude sees the denial inline like any other permission failure and must take a different approach (use Edit instead of sed, etc.).

**On the `verify_branch_sync.sh` exit 2:**
Claude sees a failed bash invocation with explicit remediation in stdout. It runs `git pull` and re-runs the script.

**On SessionStart re-injection:**
Invisible to the user. Claude resumes mid-conversation but with the state.json context block injected at the top of the new context window, re-establishing the load-bearing facts.

### 4.3 Why "Hooks With Exit Code 2" Beats "Text Saying MUST"

In v1, compliance was enforced only by SKILL.md text saying "MUST do X". The model could and did skip steps under load — long contexts, complex issues, compaction events all eroded the constraint.

In v2, compliance is enforced by external code. The hook is not part of Claude's reasoning loop — it runs in the harness and physically prevents progression. Claude cannot decide to ignore it. The exit-code-2 mechanism translates the file system state ("these artifacts exist or do not") directly into "this turn cannot end." It is the difference between a sign that says "do not enter" and a locked door.

The trade-off is rigidity: legitimate edge cases that need to bypass a phase require either skill-level awareness of the bypass or temporary marker removal. DjangoForge v2 accepts this rigidity in exchange for the failure modes it eliminates.

---

## 5. The SessionStart Re-injection Pattern

### 5.1 What is Compaction?

Claude Code maintains a conversation history. When that history exceeds the context window of the model in use, the harness invokes auto-compaction: older turns are replaced with a model-generated summary, freeing tokens. The session continues with the summarized history plus all recent messages.

The trigger is internal to the harness; Claude doesn't initiate it and may not even notice it happening mid-turn. The session's `source` field becomes `compact` after such a compaction event.

### 5.2 Why It Breaks Forge Workflows

Forge work depends on accumulated decisions and warnings:
- "We chose JobDivaCandidateSearch, not CandidateHybridSearch."
- "Issue text says X but PRs 1356/1377 actually merged Y."
- "Do not modify hybrid_search.py."
- "Wave 2 contains TASK-004 and TASK-005."

The summarizer model has no special knowledge of which sentences are load-bearing. A summary like "discussed implementation approach for issue #1190" elides every one of those facts. After compaction, Claude resuming the session might happily start editing `hybrid_search.py` because the prohibition was summarized away.

### 5.3 The Re-injection Mechanism

```
[User opens new turn in compacted session]
    ↓
[Harness fires SessionStart hook with source="compact"]
    ↓
[Hook reads .django-forge-v2/issue-N/orchestration/state.json]
    ↓
[Hook prints structured context block to stdout]
    ↓
[Harness injects stdout content into the conversation]
    ↓
[Claude sees the re-established context at the start of the new turn]
    ↓
[Claude continues with full constraint awareness]
```

The state.json file is the canonical durable store. It is updated at every phase transition and every meaningful user decision. The hook just renders state.json as conversation context.

### 5.4 The Re-injected Content Structure

Reproduced in Section 3.2. Key fields surfaced:
- Issue number and title
- Current phase and completed phases list
- "BUILDING" and "NOT BUILDING" statements (the disambiguating constraints)
- Files being modified vs. files NOT to touch
- Critical learnings list (free-form, captures the hard-won realizations)
- Implementation wave status (completed and pending tasks)
- User decisions (plan_approved, etc.)
- Agent mode (teams vs legacy)
- Session folder absolute path

### 5.5 Adaptation for EPNM-to-EMS

**Reusable with adaptation:**

The state-driven re-injection pattern transfers entirely. The state.json schema needs additions for the EPNM context:

```json
{
  "engagement": "epnm-to-ems",
  "current_phase": "...",
  "completed_phases": [...],
  "ui_conversion_target": "Page X / Workflow Y",
  "what_we_are_converting": "...",
  "what_we_are_NOT_converting": "...",
  "repos_in_scope": ["repo1", "repo2", ...],
  "branch_per_repo": {
    "repo1": "agentic-ui-conversion",
    "repo2": "agentic-ui-conversion"
  },
  "files_being_modified_per_repo": {...},
  "files_NOT_to_touch_per_repo": {...},
  "angular_to_react_decisions": [...],
  "critical_learnings": [...],
  "user_decisions": [...]
}
```

The 14-repo dimension expands the schema substantially. Otherwise the pattern is identical.

---

## 6. Adaptation Summary Table

| Asset | Status | Adaptation |
|---|---|---|
| `trace_dependencies.py` recursive walker | Reusable with adaptation | Swap `gh` for Cisco issue tracker; extend visited-set for multi-repo. |
| `trace_dependencies.py` date-based mode | Reusable with adaptation | Swap query API; update default epoch date. |
| `trace_dependencies.py` regex patterns | Reusable as-is | Keep the five "Depends on / Blocked by / After / Requires / Prerequisite" patterns; they are convention, not Django-specific. |
| `verify_branch_sync.sh` single-repo logic | Reusable as-is | Pure git logic, transfers cleanly. |
| `verify_branch_sync.sh` invocation | Reusable with adaptation | Wrap in a multi-repo iterator that checks 14 repos against `develop`. |
| PreToolUse `sed` block | Reusable as-is | Same rationale applies to any language. |
| PreToolUse `python -c replace` block | Reusable with adaptation | Add equivalents for `node -e`, `npm exec`, in-place Java tooling. |
| PreToolUse arbitrary-retrieval block | Reusable with adaptation | Update from `gh issue list --limit` to whatever Cisco issue tracker exposes. |
| PreToolUse skill-marker gate | Reusable as-is | Change marker path from `.django-forge-v2/.active` to `.epnm-forge/.active`. |
| Stop hook phase-artifact map | Reusable with adaptation | Replace Django phase contract with EPNM phase contract; keep the structural pattern. |
| Stop hook approval-state check | Reusable as-is | The state.json `user_decisions` pattern transfers cleanly. |
| Stop hook judge-evaluation check | Reusable with adaptation | Keep if using a Judge agent; replace with appropriate per-task validation otherwise. |
| Stop hook worktree-aware session matching | Reusable as-is | Multi-worktree support is an absolute requirement for parallel UI conversions. |
| SessionStart compaction-source detection | Reusable as-is | The `source == "compact"` filter is harness-defined and language-agnostic. |
| SessionStart re-injection format | Reusable with adaptation | Render the new EPNM-specific state.json fields (per-repo branch status, conversion target, etc.). |
| Skill-marker activation pattern (`.active` file) | Reusable as-is | Universal pattern for skill-scoped global hooks. |
| 8-phase workflow | Django-specific (structurally) | The structural pattern (artifact-per-phase, gate per phase) transfers; phase content is rewritten for EPNM. |
| Worktree mandatory rule | Reusable as-is | Multi-repo Cisco work needs worktrees more than single-repo Django work. |

---

## 7. Files Referenced

Absolute paths used throughout this document:

- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/SKILL.md`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/scripts/trace_dependencies.py`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/scripts/verify_branch_sync.sh`
- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-pretooluse.py`
- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-sessionstart.sh`
- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-stop.py`
- `/home/cmoore/programming/talent_ai/.claude/settings.local.json` (where hooks would normally be registered; see Section 0 — note that the django-forge-v2 hooks are present as scripts but NOT currently registered in this settings file).

---
