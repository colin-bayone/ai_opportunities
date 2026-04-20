# 02c - Namita Deliverable: Build Repair Architecture Diagrams

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/build_architecture_with_limitations.html and build_fix_architecture_light.html
**Source Date:** 2026-04-15 (shared in team chat: "current architectural diagram" at 8:34 PM, "architecture with limitations" at 8:37 PM)
**Document Set:** 02c (supplementary to Set 02, individual team member deliverable)
**Pass:** Full decomposition of Namita's architecture analysis of Justin's build repair automation pipeline

---

## Document Overview

These are two interactive HTML visualizations of Justin's current build error auto-fix pipeline. Both are well-designed, animated, and technically detailed. They represent the most thorough code-level analysis of Justin's PR #642 produced by anyone on the BayOne team.

- **build_architecture_with_limitations.html** — "Current-state architecture" view. A vertical flowchart showing 8 pipeline stages from data sources through email notification, with 7 expandable limitation annotations.
- **build_fix_architecture_light.html** — "System architecture" deep dive. An interactive card-based view with 7 components, each expandable to show key behaviors and risks. Includes detailed verification loop internals for both Make and Bazel paths, plus a 9-step end-to-end flow summary.

**Important observation:** The specificity of these diagrams — naming exact functions, parameters, file paths, error handling gaps, and code patterns — indicates Namita has read Justin's actual code, not just summarized verbal descriptions. She is referencing function names like `run_codex_analysis()`, `find_earliest_error_log()`, `bzl_error_report.py`, `build_bazel_command()`, and parameters like `error_output` that only appear in source code. This means she has accessed and reviewed the code in PR #642 or the repository itself.

---

## Pipeline Architecture (7 Stages)

### Stage 1: Data Sources

| Source | Contents | Access |
|--------|----------|--------|
| **NFS logs** | `build_log.html`, `error.log.*` files | Via ADS machines |
| **MySQL metadata** | Build tags, branch info | Build portal backend |
| **Build portal** | Build status, LOC, sanity results | `ibn-sw-bld7-1:8000` (internal server) |
| **workflow_common.py** | Shared utilities: git diff, email, WIT workspace management | In the codebase |

**New detail:** The build portal runs on `ibn-sw-bld7-1:8000`, an internal Cisco server. This is the first time the server hostname has been documented.

### Stage 2: Triage and Routing

**Script:** `analyze_and_fix_build.py`

**Behavior:**
- Parses `build_log.html` for `:STATUS:` lines
- Build passed → exit 0 (no action)
- `sdk_build_n9k` failed → manual investigation email (not automated)
- `nxos64_parallel` failed → route to automation
- Branch `nx_dev` → Bazel workflow; other branches → Make workflow

**Risks identified:**
- Duplicate `:STATUS:` lines are not deduplicated (can create duplicate task entries)
- Branch routing is hard-coded (only `nx_dev` uses Bazel)
- Failure detection depends entirely on `:STATUS:` line format

### Stage 3: Workflow Scripts (Two Parallel Paths)

| Path | Script | Build System | Key Detail |
|------|--------|-------------|------------|
| **Make** | `automated_workflow.py` | gmake | WIT workspace creation, 3 retry attempts |
| **Bazel** | `automated_bazel_workflow.py` | Bazel | BEP JSON parsing, structured retry state tracking |

### Stage 4: Error Extraction

**Make path:** `find_earliest_error_log.py`
- Scans directory for `error.log.images*` files, sorts by modification time
- Finds `Error 1` lines, walks backward for `error:` context
- Deduplicates prior error lines across occurrences
- Output modes: text, JSON, or compiler-style
- **Limitation:** "Earliest" based on mtime, which may not represent the actual first failure. Backward scan stops at `ARCH` lines (log-format specific). Only scans immediate directory.

**Bazel path:** `bzl_error_report.py`
- Parses BEP (Build Event Protocol) JSON for build status, root cause, failed labels
- Scans raw log for failure regions independently
- Classifies errors: compilation, linker, analysis, RBE (Remote Build Execution), generic
- Extracts target/object names from "Compiling...failed" lines
- Prioritizes remote execution failures to the front
- JSON output structure: `failed_targets`, `failed_objects`, `unique_errors`
- **Limitation:** BEP parsing silently swallows all exceptions. Heavy regex heuristics may miss nonstandard compiler output. `get_error_logs_streaming()` scans the whole file (not truly streaming).

### Stage 5: Prompt Context

**Prompt file:** `BUILD_ERROR_ANALYSIS_NO_BUILD.md`
- Core rule: run automatically, do not prompt user, NO builds
- Parse compiler errors into: file, line, column, type, symbol
- Search related symbols and read surrounding code
- Infer root cause and choose minimal fix strategy
- Generate and apply patch, verify with grep/git diff only
- Includes walkthrough examples: duplicate function, deprecated macro

**Context files:** `tools/current_errors.txt` and `tools/current_errors.json`
- In-workspace only, overwritten each retry
- **Limitation:** No structured persistence of analysis results across runs. No database.

**Risks:**
- References stale tool names (`grep_search`, `replace_string_in_file`)
- Error log location says `build_XX_error.log` but workflows use `current_errors.txt`
- Mixes "generate patch" and "edit files directly" mental models

### Stage 6: AI Analysis (Codex/LLM)

- Analyzes errors, edits source in workspace, produces patchable changes
- No build commands (verification is separate)
- **Limitation:** Receives only a subset of errors. The `error_output` parameter is accepted by `run_codex_analysis()` in both workflows but is never actually used — the Codex prompt does not receive this data.
- **Risk:** Codex runs with `--sandbox danger-full-access` flag in the Bazel workflow

### Stage 7: Verification Builds (Up to 3 Attempts)

**Make verification loop:**
1. `run_build()` — Load VBE module from `config.files/vbe.mk`
2. `gmake -j16 <target>` — Run per target, log each separately
3. Summarize results — Count passed vs failed
4. Decision: All pass?
   - **Pass:** Collect git diff → write `success_email.txt` → send email
   - **Fail:** Extract fresh errors → rewrite `current_errors.txt` → rerun Codex → loop back
   - **Exhaust (3 attempts):** Exit code 1, NO email sent

**Bazel verification loop:**
1. `run_bazel_builds()` — from standalone dir, restore cwd in finally
2. `build_bazel_command()` — `.so/.bin/.klm` targets get `_all` suffix
3. Build ONLY remaining failed targets, log per target per attempt
4. Decision: All remaining pass?
   - **Pass:** Stop retrying
   - **Fail:** `analyze_retry_failures()` → re-parse with `bzl_error_report.py` → update `attempt_history` → append to `bazel_build_history.log` → rerun Codex → loop back
   - **Always (regardless of outcome):** Generate `bazel_build_email.txt` with attempt history → send email

**Critical difference:** Make rebuilds ALL original targets on every retry (wastes time, obscures per-target progress). Bazel correctly tracks remaining targets and only rebuilds failures. This is the single most important architectural difference between the two paths.

### Stage 8: Notification

- Email summary with git diff, attempt history, latest error context
- Sent whether pass or fail (Bazel path)
- Make path: email on success only, no email on exhaustion
- **Limitation:** No traceability from fix back to root cause. Cannot link a specific patch to the error that motivated it.

---

## Complete Limitations Inventory (7 Items)

| # | Limitation | Component | Impact |
|---|-----------|-----------|--------|
| 1 | **Subset errors** | `find_earliest_error_log.py`, `bzl_error_report.py` | Only a fraction of available error context reaches the LLM. Mtime-based selection may miss the real first failure. |
| 2 | **No persistence** | `tools/current_errors.txt/.json` | Analysis results exist only during a single run. No database. Nothing queryable after the session ends. No historical error patterns. |
| 3 | **No traceability** | Email output | Cannot link patch → error block → root cause. Post-hoc analysis impossible. |
| 4 | **Make retries all** | `automated_workflow.py` | Rebuilds full target list on every retry instead of just failures. Wastes time, obscures progress. Bazel does this correctly. |
| 5 | **Unused parameter** | `run_codex_analysis()` | `error_output` param accepted but never passed to Codex prompt. Reduces AI context quality. |
| 6 | **Hard-coded paths** | Multiple files | `BZL_ERROR_REPORT`, WIT binary path, mail script path, `NODEJS_HOME` all absolute. Fragile to infrastructure changes. |
| 7 | **Tag selection bug** | `workflow_common.py` | `find_latest_build_tag()` sorts ascending and returns first match — likely returns oldest tag, not newest. |

---

## Additional Risks from Detailed View

| Component | Risk |
|-----------|------|
| `analyze_and_fix_build.py` | Failure detection depends entirely on `:STATUS:` line format. If format changes, automation silently breaks. |
| `automated_workflow.py` | Proceeds even if `find_earliest_error_log()` fails to find errors. |
| `automated_bazel_workflow.py` | `--use-existing-workspace` flag skips checkout entirely. |
| `bzl_error_report.py` | BEP parsing silently swallows ALL exceptions (errors hidden). |
| `BUILD_ERROR_ANALYSIS_NO_BUILD.md` | References stale tool names that may not exist in current Codex. |

---

## End-to-End Flow (9 Steps)

1. Detect failing task from `build_log.html`
2. Triage: manual handling vs automation
3. Route to Make or Bazel workflow by branch
4. Create/reuse WIT workspace, checkout failing tag
5. Extract structured error context from logs
6. Feed context + prompt to Codex for code patches
7. Run verification builds externally
8. If failures remain → re-extract errors → re-run Codex → retry **(up to 3 times)**
9. Collect git diff and send summary email

---

## Significance for BayOne's Architecture Proposal

Namita's analysis provides the technical foundation for Colin's three-tier approach (Set 01 Decision #4: "do not commit to architecture until logs are inspected firsthand"). With this analysis, the team now has:

1. **A documented baseline.** Every component of Justin's current pipeline is named, its behavior described, and its limitations cataloged. The team can now propose specific improvements to specific components rather than vague "rearchitecture."

2. **Clear improvement targets.** The 7 limitations map directly to engineering work: add persistence (database), add traceability (error→fix linking), fix the subset extraction problem, fix the tag selection bug, remove hard-coded paths, add error-output to the Codex prompt, and fix the Make retry behavior.

3. **The Bazel vs Make comparison as a wedge.** The Bazel workflow is demonstrably better engineered (tracks remaining targets, uses structured JSON, maintains attempt history). This positions BayOne to say: "The Bazel path is the right model. Let us bring the rest of the system up to that standard and add what is missing."

4. **Evidence of code-level understanding.** When Colin presents to Srinivas, he can reference specific function names, specific bugs (the `error_output` parameter that is accepted but never used), and specific architectural gaps. This demonstrates BayOne has done real discovery, not surface-level observation.
