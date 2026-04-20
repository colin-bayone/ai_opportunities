# CI/CD Engagement Primer — April 16, 2026

**Prepared for:** Srinivas Pitta
**Prepared by:** Colin Moore, BayOne AI Practice
**Covering:** Team progress and findings since the April 10 meeting
**Purpose:** Structure tomorrow's meeting productively

---

## Summary

Since our last meeting on April 10, the team has focused on three areas: analyzing user pain points from the NxOS CI workflow channel, deepening our understanding of the build log infrastructure, and exploring the WebEx API for meeting and chat integration. This document captures what we learned, what we built, and what we need to discuss.

---

## 1. Pain Point Analysis — NxOS CI Workflow Channel

The team scraped and categorized messages from the NxOS CI workflow WebEx space. The dataset spans approximately three years (April 2023 through March 2026) and contains over 4,200 actionable messages across 25 categories.

### Top Issue Categories by Volume

| Category | Messages | % of Total |
|----------|----------|-----------|
| Bug/Error | 463 | 10.9% |
| Question/Help Request | 460 | 10.9% |
| Infrastructure/Deployment Problem | 410 | 9.7% |
| Test Failure | 396 | 9.4% |
| Code Review | 349 | 8.2% |

[CHART: category_distribution.png — embed in HTML]

### Response Time and Coverage

For resolvable issue categories, we measured average first response time and what percentage of threads received any reply.

| Category | Avg Response | Median | Response Coverage |
|----------|-------------|--------|------------------|
| Blocker/Dependency | 12 min | 7 min | 44% |
| QA/Testing Issue | 46 min | 5 min | 39% |
| Infrastructure/Deployment | 249 min (~4 hrs) | 20 min | 61% |
| Bug/Error | 263 min (~4.4 hrs) | 51 min | 49% |
| Test Failure | 321 min (~5.4 hrs) | 44 min | 46% |
| Question/Help Request | 440 min (~7.3 hrs) | 13 min | 34% |

[CHART: 6_avg_first_response_time.png — embed in HTML]

### Key Findings

1. **Two-thirds of help requests receive no response.** Question/Help Request is the highest-volume category tied with Bug/Error, yet only 34% of threads get any reply. Engineers are asking for help and receiving silence.

2. **Build failures take half a workday to get first acknowledgment.** Bug/Error and Test Failure threads average 4 to 5 hours before a first response. At the 90th percentile, engineers wait over 10 hours.

3. **Explicit blockers get resolved in minutes.** When an issue is specifically flagged as a blocker, the average first response time drops to 12 minutes. The team responds when urgency is communicated. The gap is in identifying what should be escalated.

4. **Channel volume has tripled over three years.** Weekly message volume has grown from 20-40 messages per week in 2023 to 60-120 in 2026. The manual triage approach is not scaling with the growing engineering organization.

### Recommendation

This data suggests the highest-impact first target for AI-driven triage is the Question/Help Request category: high volume, lowest response coverage, and longest average wait. An automated system that can surface relevant documentation, link to known solutions, or route questions to the right person would address the single largest gap in the current workflow.

---

## 2. Build Log Infrastructure — What We Learned

The team met with Justin Joseph (April 8 and April 9) and gained hands-on access to the build log system. The following was verified through direct observation and discussion.

### Build System Landscape

- Two build systems: Gmake (nx_main branch, legacy, being phased out) and Bazel (nx_dev branch, current focus)
- Two build types: CI builds (developer PRs) and CD builds (official nightly)
- CI and CD builds have different NFS paths, different log formats, and different retention policies

### Log Infrastructure Details

| Attribute | CI Builds | CD Builds |
|-----------|----------|----------|
| NFS path pattern | `/auto/paw-sjc-scratch/paw-logs/{uuid}/...` | `/auto/ins-bld-tools/branches/{branch}/nexus/logs/{tag}` |
| Path discovery | UUID extracted from PR metadata | Predictable from branch + build tag |
| Retention (success) | Deleted at PR merge | 2 weeks |
| Retention (failure) | 3-5 days | 5 years |
| Triage entry point | No build_log.html | build_log.html available |

- 13 distinct Bazel error log types, organized per image/stage (nxos64, nxos64_msx, linecardimages, core_64_n9000, etc.)
- 40+ individual log files per build in a flat directory structure
- Build metadata (build number, status, timestamps) stored in MySQL; logs stored separately on NFS

### Existing Automation Review

The team reviewed the existing build repair automation pipeline (PR #642 on DCN/tools) at the code level. The pipeline consists of 7 components:

1. `analyze_and_fix_build.py` — entry point, parses build_log.html for :STATUS: lines, routes to Gmake or Bazel workflow
2. `automated_workflow.py` (Gmake) and `automated_bazel_workflow.py` (Bazel) — two parallel paths
3. `find_earliest_error_log.py` (Gmake) and `bzl_error_report.py` (Bazel) — error extraction
4. `BUILD_ERROR_ANALYSIS_NO_BUILD.md` — Codex prompt for fix generation
5. Verification builds with up to 3 retries
6. Email notification with git diff

**Identified limitations:**
- Error extraction captures only a subset of available context (mtime-based file selection, backward scan stops at ARCH lines)
- No persistence of analysis results across runs (workspace files overwritten each attempt)
- No traceability from a fix back to the root cause that motivated it
- Gmake path rebuilds all targets on every retry (Bazel correctly tracks remaining failures only)
- Hard-coded absolute paths throughout (fragile to infrastructure changes)
- The `error_output` parameter is accepted but never passed to the Codex prompt

The Bazel workflow is the more mature path and serves as the better foundation for improvement.

---

## 3. Proposed Architecture — Build Log Analysis Pipeline

Based on the current-state review and the technical understanding gained, the team has drafted a proposed end-to-end architecture for the build log analysis system. This is initial thinking; several decisions are pending.

[EMBED: Namita's 7-block SVG diagram from proposed architecture HTML]

### Architecture Overview (8 Blocks)

**Block 1 — NFS Ingestion:** Reads Bazel CI/CD logs from NFS. Proposal: start with 15-30 minute batched polling, revisit once build cadence patterns are confirmed.

**Block 2 — Parsing and Chunking:** Regex parsing for uniform log formats, NLP-based chunking for varied formats. NLP summarization reduces text volume before any Tier 2/3 processing to control token cost.

**Block 3 (Tier 1) — Rule-Based Detection:** Deterministic error matching using the Bazel error code registry and regex patterns. No AI. Fast path, low cost. Expected to handle the majority of known errors.

**Block 4 (Tier 2) — NLP/ML Classification:** Specialized small model for errors that Tier 1 cannot match. Semantic similarity, confidence scoring. Invoked only on escalation from Tier 1.

**Block 5 (Tier 3) — LLM Analysis:** Root cause investigation and fix suggestion generation for novel or compound errors. Invoked only when Tiers 1 and 2 cannot resolve.

**Block 5.1 — Auto-Fix and PR:** Generates code patches, opens PRs with root cause summaries, triggers build verification. Human review gate is mandatory on all PRs.

**Block 6 — Structured Storage:** Star schema design with a fact table (`build_analysis_facts`, one row per error per build) and dimension tables (`dim_builds`, `dim_errors`, `dim_repos`, `dim_branches`, `dim_log_files`). Provides commit-level traceability that does not exist in the current system.

**Block 7 — MCP Tool Interface:** Exposes all analysis results to downstream agents and users via MCP tools. Query analysis results, trace errors to commits/PRs, fetch fix suggestions, pull build failure summaries, and correlate with live Git/GitHub state.

### Pending Decisions

- Ingestion mode: batched polling vs event-driven/realtime (Block 1)
- CI vs CD log format differences need hands-on verification (Block 2)
- Availability of labeled datasets for the Tier 2 ML model (Block 4)
- Fix delivery mechanism: PR comment, new branch/PR, or email (Block 5.1)

---

## 4. WebEx Integration — What We Learned

### Chat Scraping (Task 1)
- A working WebEx scraper was built and deployed into the team's own WebEx space. It captures full message history with structured fields (timestamp, author, email, bot flag, text, files, thread parent), stores to PostgreSQL, and supports per-room scoping and deduplication.
- The NxOS CI workflow channel scrape (Section 1 above) was performed using this capability.

### Meeting Recording Extraction (Task 2)
- A working extraction tool was built that retrieves transcripts, summaries, action items, and audio from WebEx meetings via the API.
- **Key constraint discovered:** The WebEx API restricts recording/transcript access to meeting owners. A regular attendee cannot extract these artifacts via API. This impacts the automation architecture for Task 2.
- For meetings where the team is the organizer, the API path works. For broader automation across the organization, either admin-scoped tokens or an alternative approach (such as audio-file-based transcription) would be needed.

---

## 5. Open Questions for Discussion

1. **Scope clarification for WebEx work.** The team has built both a chat scraper and a meeting recording extractor. Should the focus remain on the NxOS CI workflow channel specifically, or should this be generalized for the broader set of WebEx spaces?

2. **Relationship to existing work.** The team observed the Nexus T agent in the NxOS CI workflow space. How does our work relate to that effort? Should we be collaborating with that team, building on their work, or focusing on a different aspect of the problem?

3. **Fix delivery preference.** For the build log analysis pipeline, when AI generates a fix: should the system comment on the existing PR, open a new PR with the fix, or notify via another channel? The current Justin workflow uses email; the proposed architecture includes a PR-based approach with human review.

4. **Tiered processing — data for the ML model.** The proposed architecture includes a Tier 2 ML model for error classification. Does the team have access to labeled datasets of past build errors and their resolutions? If not, should Tier 2 initially use pre-trained models or unsupervised approaches?

5. **Batch vs realtime for log ingestion.** For CI builds (where developers are waiting), is near-realtime processing expected? For CD nightly builds, is batch processing on a 15-30 minute cycle acceptable?

---

## 6. Access Items Requiring Action

| Item | First Requested | Current Status | What Is Needed |
|------|----------------|---------------|---------------|
| DeepSight platform access | ~4 weeks ago | No access | Direct grant from platform owner |
| Pulse/Scribble repository access | April 9 | Repo links not yet provided; naming confusion between "Scribble" and "Scrubber" in GitHub | Direction to the repo owner to share exact links and grant access |
| Permanent ADS machine | April 3 (tenant), April 11 (bundle) | Tenant approved by Mahaveer but not reflected in portal. Bundle (CN-SJC-STANDALONE) is sequential — can only be added after ADS machine is provisioned. | Namita following up with Mahaveer on the tenant portal issue per Srinivas's guidance (April 16). |

The team has temporary ADS access (4-week lease, RHEL8) which enables current work, but permanent access is needed for sustained development. All environment setup and tooling configuration done on temporary machines would need to be repeated every 4 weeks.

---

## Companion Materials Available

The following are available as separate files if deeper review is desired:

1. **Current-state architecture diagram** — Interactive HTML showing Justin's existing 7-component build repair pipeline with annotated limitations (expandable detail per component)
2. **NxOS CI workflow analysis — full dataset** — CSV with categorized messages, response times, and thread structure
3. **Log type mapping** — Complete catalog of all 13 Bazel error log types with CI/CD differentiation, NFS paths, and retention policies
4. **WebEx API endpoint reference** — Verified endpoints for chat scraping and meeting recording extraction
