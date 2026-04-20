# 04e - Namita Deliverable: Proposed Build Log Analysis Architecture (Blocks 1-7)

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/Proposed Build Log Analysis Architecture — Blocks 1–7.html
**Source Date:** 2026-04-16 (proposed architecture, created after Set 04 team sync)
**Document Set:** 04e (supplementary to Set 04, individual team member deliverable)
**Pass:** Full decomposition of Namita's proposed future-state architecture

---

## Overview

This is Namita's proposed end-to-end architecture for the build log analysis pipeline, presented as an SVG diagram with block-by-block notes. It implements Colin's three-tier inverted pyramid approach (Set 03) within a complete pipeline from NFS ingestion through MCP tool interface. The subtitle explicitly marks this as "Initial thinking; details pending log format verification."

This is the **future state** diagram — the third of Colin's three-diagram framework (Set 04: current state, problems/recommendations, future state). Combined with her earlier current-state diagram (Set 02c), Namita has now produced two of the three architecture views Colin defined.

The diagram was created using Claude Code on Namita's machine (file path: `Users/namitamane/Documents/bayone_cisco/output/`).

---

## Architecture: 8 Blocks + 2 External Systems

### Block 1 — NFS Ingestion
- **Input:** Bazel logs (both CI and CD builds)
- **Mode options:** Batched (15-30 min polling) or event-driven/realtime via filesystem watcher
- **Features:** Scheduled poll or watcher, manifest + checksum for integrity
- **Proposal:** Start with 15-30 min batching to match current build cadence; revisit once queue patterns and SLA targets are confirmed
- **Status:** Decision pending on batch vs realtime

### Block 2 — Log Parsing and Chunking
- **Purpose:** Structured extraction from raw log files
- **Approach:** Regex parsing for uniform formats, NLP-based chunking for varied formats
- **Key feature:** NLP summarization to shrink text prior to Tier 2/3 calls (token cost control)
- **Semantic chunk boundaries** for meaningful segmentation
- **Critical constraint:** 300K-500K line files require aggressive size reduction before any AI processing
- **Status:** Pending CI vs CD format verification

### Block 3 (Tier 1) — Rule-Based Error Detection
- **Type:** Deterministic, no AI
- **Approach:** Bazel docs error code registry + regex/pattern matching + error description lookup
- **Speed:** Fast path, low cost
- **Expected outcome:** Handles the majority of errors
- **Fed by:** Bazel Docs Scraper (separate utility that populates the error code registry)

### Block 4 (Tier 2) — NLP/ML Contextual Classification
- **Type:** Invoked only when Tier 1 cannot resolve
- **Approach:** Specialized small ML model for error category/issue type classification
- **Features:** Semantic similarity matching, confidence scoring
- **Target:** Contextual, non-trivial errors

### Block 5 (Tier 3) — LLM Complex Analysis
- **Type:** Invoked only when Tiers 1 and 2 cannot resolve
- **Approach:** Root cause investigation, fix suggestion generation, summary generation
- **Target:** Novel and compound errors only
- **Escalation flow:** Explicit from T1 → T2 → T3, shown with dashed arrows labeled "unresolved"

### Block 5.1 — Auto-Fix and PR
- **Consumes:** Outputs from all three tiers (fix context flows from B3, B4, B5)
- **Actions:** Generate code patch (diff), branch + commit via Git, open PR with root cause + fix, trigger build verification
- **Critical gate:** Human review gate on PR — mandatory, shown as an explicit badge
- **Status feedback:** PR results (merged/rejected/build pass) flow back to Block 6 storage
- **Note:** "Builds on Justin's POC approach" — explicitly acknowledges existing work

### Block 6 — Structured Storage (Star Schema)
- **Design:** Star schema with relational database
- **Fact table:** `build_analysis_facts` — one row per error per build
- **Dimension tables:** `dim_builds`, `dim_errors`, `dim_repos`, `dim_branches`, `dim_log_files`
- **Persists:** Summaries, suggested fixes, confidence scores, SHA hashes, PR numbers
- **Does NOT persist:** Full commit diffs and PR comments (queried live from Git/GitHub APIs)
- **Key property:** Commit-level traceability — every analysis result traces back to a specific commit and PR

### Block 7 — MCP Tool Interface
- **Purpose:** Agentic AI access layer
- **Tools exposed:** Query analysis results, trace error to commit/PR, fetch fix suggestions, pull build failure summaries, live Git/GitHub API lookups, CI/CD build status
- **Consumers:** Downstream agents and users via DeepSight

### External Systems (Side Inputs)
- **MySQL Build Metadata** — build ID, timestamp, status. Correlates with Block 1 ingestion.
- **Git/GitHub APIs** — commits, diffs, PR review state (live). Feeds Block 6 via SHA lookup.
- **Bazel Docs Scraper** — Populates Tier 1 error code registry. Separate utility.

---

## Data Flow Summary

```
NFS Logs → B1 (Ingest) → B2 (Parse/Chunk) → [known errors] → B3 Tier 1 (Rules)
                                             → [contextual]  → B4 Tier 2 (NLP/ML)
                                             → [complex]     → B5 Tier 3 (LLM)
                                                                    ↓
B3/B4/B5 all feed → B5.1 (Auto-Fix + PR) → B6 (Star Schema Storage)
B3/B4/B5 also feed classification results directly → B6
B6 → B7 (MCP Tools) → Downstream agents/users
```

The tiered escalation is one-directional: T1 → T2 → T3. Each tier records its confidence score. Errors that T1 resolves never touch T2 or T3.

---

## Pending Decisions (Explicitly Marked in Diagram)

1. **Batch vs realtime for Block 1** — Namita proposes starting with 15-30 min batching
2. **CI vs CD format verification** — Parsing strategy depends on whether CI and CD log formats differ
3. **Log format verification** — Need to confirm format consistency across build types and timeframes
4. **Architecture review** — Marked as pending overall

---

## Design Strengths

1. **Colin's three-tier approach fully implemented.** The inverted pyramid from Set 03 is realized as Blocks 3, 4, 5 with explicit escalation paths and confidence scoring at each tier.

2. **Star schema for storage.** This is a mature data modeling choice. The fact-dimension pattern enables flexible analytics (slice by build, by error type, by repo, by branch, by log file) without denormalization.

3. **MCP as the consumption layer.** Block 7 directly addresses Srinivas's requirement that all data sources be exposed via MCPs. The architecture ends at the MCP interface, making it a complete DeepSight integration story.

4. **Human review gate is explicit.** Block 5.1 shows the human-in-the-loop requirement as a mandatory gate, not an optional feature. This aligns with the Set 04 discussion about never letting AI autonomously commit fixes.

5. **Traceability is built in.** Every analysis result in Block 6 traces to a commit SHA and PR number. This directly addresses the "no traceability" limitation identified in the current-state architecture (Set 02c).

6. **Token cost management.** Block 2 includes NLP summarization specifically to reduce text before Tier 2/3 calls. This addresses Srinivas's inference cost concern.

7. **Bazel Docs Scraper as a separate utility.** Tier 1's effectiveness depends on a comprehensive error code registry. Making this a separate component that feeds Tier 1 is the right separation of concerns.

---

## Comparison to Current State (Set 02c)

| Aspect | Current State (Justin) | Proposed (Namita) |
|--------|----------------------|-------------------|
| Error extraction | Subset only (mtime-based, backward scan) | Three-tier with explicit escalation |
| Persistence | None (workspace files overwritten) | Star schema with fact + 5 dimension tables |
| Traceability | None (email has diff but no link to error) | SHA + PR number on every analysis row |
| Fix delivery | Email summary (make) or email always (Bazel) | PR with human review gate |
| Retry logic | Make: all targets; Bazel: remaining only | Not explicitly addressed (noted as "pending") |
| MCP integration | None | Block 7 as dedicated MCP tool interface |
| Token optimization | None (full error context to Codex) | NLP summarization in Block 2 + tiered escalation |
| Build metadata | MySQL (read-only, basic) | MySQL correlation + star schema for analysis |

---

## Significance for Srinivas Prep

This diagram is a strong candidate for inclusion in the Srinivas prep. It shows:
1. The team has moved from "understanding the problem" to "designing the solution"
2. The architecture implements every principle Srinivas values: reusable (MCP layer), optimized (tiered to minimize LLM usage), extensible (star schema enables future analytics)
3. It acknowledges Justin's existing work ("builds on Justin's POC approach") rather than dismissing it
4. Pending items are honestly marked — the team is not pretending to have all answers
