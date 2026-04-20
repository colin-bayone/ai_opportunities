# 02b - Namita Deliverable: Log Type Mapping (Technical Reference)

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/Log Type Mapping.docx
**Source Date:** 2026-04-15 (shared in team chat as "Log Type mapping - details about basic log types, location")
**Document Set:** 02b (supplementary to Set 02, individual team member deliverable)
**Pass:** Full decomposition of Namita's log type classification and NFS structure document

---

## Document Overview

This is a structured Q&A-format document titled "Tasks / Part 1: Log Type Mapping" that systematically answers 6 specific questions about the build log infrastructure. The questions appear to be self-assigned investigative tasks that directly address the open questions from Set 01 about log file organization, types, and access patterns. This is the most detailed technical reference on the build log infrastructure produced by the team to date.

---

## Question 1: All Log Types on ADS Machine

### A. Bazel Logs (nx_dev branch)

**CI Bazel logs (developer PR builds):**

| Log File | Image/Stage |
|----------|-------------|
| `error.log.images^final^bazel^core_64_n9000` | Core 64-bit N9000 |
| `error.log.images^final^bazel^eth_64_n9000` | Ethernet 64-bit N9000 |
| `error.log.images^final^bazel^linecardimages` | Linecard images |
| `error.log.images^final^bazel^nxos64` | NX-OS 64-bit (base) |
| `error.log.images^final^bazel^nxos64_msx` | NX-OS 64-bit MSX |
| `error.log.images^final^bazel^nxos64_noncs` | NX-OS 64-bit non-CS |
| `error.log.images^final^bazel^nxos64_s1` | NX-OS 64-bit S1 |
| `error.log.images^final^bazel^nxos64_s1_dpu` | NX-OS 64-bit S1 DPU |
| `error.log.images^final^nxos64_parallel` | NX-OS 64-bit parallel |

**CD Bazel logs (nightly production builds):**

| Log File | Image/Stage |
|----------|-------------|
| `error.log.images^final^nxos64_imaging` | NX-OS 64-bit imaging |
| `error.log.images^final^nxosvp` | NX-OS VP |
| `error.log.images^final^nxos64v_parallel` | NX-OS 64-bit V parallel |
| `error.log.images^final^nxos64_parallel` | NX-OS 64-bit parallel |
| `error.log.images^final^bazel^nxos64_msx` | NX-OS 64-bit MSX |
| `error.log.images^final^bazel^nxos64_s1_dpu` | NX-OS 64-bit S1 DPU |
| `error.log.images^final^bazel^nxos64_s1` | NX-OS 64-bit S1 |
| `error.log.images^final^bazel^nxos64_noncs` | NX-OS 64-bit non-CS |
| `error.log.images^final^bazel^nxos64` | NX-OS 64-bit (base) |
| `error.log.images^final^bazel^linecardimages` | Linecard images |

**Observations:**
- CI and CD share 6 common log files (the `bazel^` prefixed ones: nxos64_msx, nxos64_s1_dpu, nxos64_s1, nxos64_noncs, nxos64, linecardimages)
- CI has 3 unique log types: `core_64_n9000`, `eth_64_n9000`, `nxos64_parallel`
- CD has 4 unique log types: `nxos64_imaging`, `nxosvp`, `nxos64v_parallel`, `nxos64_parallel`
- File naming uses `^` as path separator (not `/`), suggesting these are flattened representations of a directory hierarchy
- Total distinct Bazel error log types: 13

### B. Gmake Logs (nx_main branch)

Not enumerated in this document. The team's focus is on Bazel per Decision #1.

---

## Question 2: CI vs CD Log Classification

| Category | Source | Description |
|----------|--------|-------------|
| **CI logs** | Developer PRs | Triggered when developers submit pull requests. Build runs against the PR changes. |
| **CD logs** | Official nightly builds | Scheduled production builds that run nightly against the current branch state. |

This confirms the two-track build system. CI and CD logs have different retention policies, different NFS locations, and partially different log file sets.

---

## Question 3: Nightly Build (CD) Log Access and Retention

### CD Nightly Build Logs

| Build Status | Log Location | Retention |
|-------------|-------------|-----------|
| **Success** | `<standalone path>/build/` AND `<standalone path>` | **2 weeks** |
| **Fail** | Copied to `/auto/ins-bld-tools/branches/nx_dev/nexus/logs/` | **5 years** |

### CI Developer PR Build Logs

| Build Status | Log Location | Retention |
|-------------|-------------|-----------|
| **Success** | NFS path embedded in the PR (e.g., `/auto/paw-sjc-scratch/paw-logs/{uuid}/NXOS Build/build/`) | **Deleted after PR merge** |
| **Fail** | NFS path embedded in the PR | **3-5 days** |

**Critical insights:**

1. **Failed CD logs are the permanent record.** They persist for 5 years at the known NFS path under `/auto/ins-bld-tools/branches/`. This is the richest dataset for historical pattern analysis.

2. **Successful CD logs expire in 2 weeks.** If the team wants to analyze passing builds (to understand what "normal" looks like), they need to archive within the 2-week window.

3. **CI success logs are the most ephemeral.** They vanish when the PR merges. For a real-time CI failure analysis system, the pipeline must trigger before merge.

4. **CI failure logs have a 3-5 day window.** This is slightly better than the "about three days" from the PDF document (Set 02a). The 3-5 day range gives a narrow but usable window for batch processing.

5. **CD and CI log NFS paths are different.** CD logs use a predictable path structure based on branch and build tag. CI logs use a UUID-based path embedded in the PR itself, meaning the system must extract the NFS path from the PR metadata to find the logs.

---

## Question 4: Log File Composition

Logs are **NOT composite** (not multiple applications blended into one file). They are organized as:

1. **One folder per build** — named by build tag (e.g., `COV_10_7_0_IDV9_0_201`)
2. **Logs per stage** within each folder, covering these stages:
   - linecard
   - nxos64
   - nxos64_msx
   - nxos64_noncs
   - nxos64_s1
   - nxos64_s1_dpu
   - nxos64_imaging
   - nxos64v_parallel
   - nxosvp

3. **CD builds generate `build_log.html`** — a summary file containing the status of various checks. This is the build-level overview.
4. **CI builds do NOT generate `build_log.html`** — a notable asymmetry. CI builds lack the consolidated status view that CD builds have.

**Architecture implication:** For CI builds, the analysis system must synthesize the build-level status from individual stage logs. For CD builds, `build_log.html` provides a ready-made entry point for triage (check the summary first, then drill into specific stage error logs).

---

## Question 5: The 12-15 Log Files Per Build

Logs are organized **per checks/stage** (not per module, not flat). This answers the Set 01 open question directly.

The 9 stages identified in Question 4 align with the error log file types from Question 1. Each stage produces its own error log, and additional cross-cutting logs (build_log.html, compiler warnings, etc.) exist at the build level.

---

## Question 6: NFS Path Structure

### CD Logs Path Pattern

```
/auto/ins-bld-tools/branches/{branch}/nexus/logs/{tag}
```

**Variables:**
- `{branch}` — e.g., `nx_dev`, `nx_main`
- `{tag}` — build tag, e.g., `COV_10_7_0_IDV9_0_201`

**Example:** `/auto/ins-bld-tools/branches/nx_dev/nexus/logs/COV_10_7_0_IDV9_0_201`

**Log file pattern within the directory:**
```
log_prefix = 'error.log.images^final^bazel'
```

This means log files can be located programmatically: given a branch and build tag, construct the path and glob for files matching the prefix.

### CI Logs Path Pattern

```
/auto/paw-sjc-scratch/paw-logs/{uuid}/NXOS Build/build
```

**Variables:**
- `{uuid}` — unique build identifier (e.g., `5c10425e-3831-11f1-a211-005056a40ab2`)

**Example:** `/auto/paw-sjc-scratch/paw-logs/5c10425e-3831-11f1-a211-005056a40ab2/NXOS Build/build`

**Key difference:** CI logs use UUIDs, not build tags. The UUID must be extracted from the PR metadata or Jenkins build record to locate the logs. This is a more fragile discovery path than CD logs.

---

## Summary of Findings

| Question | Answer |
|----------|--------|
| All log types on ADS? | 13 distinct Bazel error log types across CI and CD, organized by image/stage |
| CI vs CD? | CI = developer PRs, CD = nightly production builds; different retention, different paths |
| Nightly logs accessible from same NFS? | Different base paths. CD: `/auto/ins-bld-tools/branches/`, CI: `/auto/paw-sjc-scratch/paw-logs/` |
| Composite or individual? | Individual per stage. 9 stages. Folder per build. |
| What are the 12-15 files? | Per checks/stage, not per module |
| Path structure? | CD: predictable `{branch}/{tag}`. CI: UUID-based, extracted from PR. |

---

## Architecture Implications for Task 3

1. **Two different log discovery mechanisms needed.** CD logs can be enumerated by constructing paths from branch + tag (available from build portal or MySQL). CI logs require extracting UUIDs from PRs or Jenkins records.

2. **`build_log.html` is the triage entry point for CD builds.** Start with the summary, identify failed stages, then drill into the specific `error.log.images^final^bazel^{stage}` file. CI builds lack this and need a different triage strategy.

3. **Retention drives the processing architecture.** Failed CD logs (5 years) support batch historical analysis. CI failure logs (3-5 days) require near-real-time processing or independent archival. CI success logs (deleted at merge) are effectively inaccessible for historical analysis.

4. **The `^` separator in filenames is a parsing consideration.** File names like `error.log.images^final^bazel^nxos64_s1_dpu` use `^` as a hierarchical separator. A parser can split on `^` to extract: category (error.log), scope (images), status (final), build system (bazel), and stage (nxos64_s1_dpu).

5. **Stage names map directly to hardware/software targets.** The 9 stages (linecard, nxos64, nxos64_msx, etc.) appear to correspond to different NX-OS image targets (different switch hardware, different software variants). Understanding which stages fail most frequently and why would be a high-value analysis.
