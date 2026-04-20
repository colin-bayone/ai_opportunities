# Proposed Build Log Analysis Architecture — Review and Revision

**Date:** 2026-04-16
**Participants:** Colin Moore, Claude
**Source artifact:** `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/Proposed Build Log Analysis Architecture — Blocks 1–7.html`
**Purpose:** Capture the architectural review discussion before rebuilding Namita's diagram as a polished Mermaid deliverable. The goal is to make the architecture correct, defensible, and aligned with BayOne AI practice principles before presenting to Srinivas's team at Cisco.

---

## Context

Namita produced an initial architecture diagram for the Cisco CI/CD build log analysis pipeline as an inline SVG. The diagram covers eight blocks: NFS ingestion, parsing and chunking, three-tier error classification (deterministic / ML / LLM), auto-fix with PR, star-schema storage, and an MCP interface, plus external feeds (MySQL build metadata, Git/GitHub APIs, a Bazel docs scraper).

The diagram has layout problems as an SVG and will be rebuilt in Mermaid.js. Before rebuilding, the architecture itself was reviewed for correctness.

---

## Namita's Source Diagram — Block Summary

- **B1 NFS Ingestion** — Bazel CI+CD logs from NFS; batched 15–30 min or event-driven (decision pending).
- **B2 Parsing and Chunking** — regex + NLP chunking, semantic chunk boundaries, NLP summarization "to shrink text prior to tier 2/3 calls." Critical given 300K–500K line files.
- **B3 / Tier 1 Rule-Based** — Deterministic detection using a Bazel error code registry, regex, and error description lookup. No AI.
- **B4 / Tier 2 NLP/ML** — Specialized small model, error category / issue type, semantic similarity matching, confidence scoring. Invoked when T1 can't resolve.
- **B5 / Tier 3 LLM** — Root cause investigation, fix suggestion generation, summary generation. Only when T1 + T2 can't resolve.
- **B5.1 Auto-Fix & PR** — Consumes outputs from B3/B4/B5. Generates code patch, branches/commits via Git, opens a PR, triggers build verification. Human review gate mandatory.
- **B6 Structured Storage** — Star schema: `build_analysis_facts` (fact) + `dim_builds`, `dim_errors`, `dim_repos`, `dim_branches`, `dim_log_files`.
- **B7 MCP Tool Interface** — Query + action tools for downstream agents: query results, trace error → commit/PR, fetch fix suggestions, live Git/GitHub lookups.
- **External feeds** — Bazel Docs Scraper (feeds T1 registry), MySQL build metadata (correlates with B1), Git/GitHub APIs (SHA lookup, PR state).

---

## Colin's Architectural Principles

These principles govern all architectural decisions on this engagement:

1. **Simplest, least complex way first — always.** Don't design for hypothetical future complexity.
2. **Deterministic before ML, ML before LLM.** Regex is nanoseconds, ML is tens of milliseconds, LLM is seconds + dollars. The cost gradient is the entire reason tiering exists.
3. **Most efficient and least compute-heavy solution first — always.**
4. **Rejects and regex matching as the first line of defense.** Deterministic early-out is what makes the rest of the pipeline affordable at scale.

---

## Issues Identified in Namita's Diagram

### 1. Tier routing contradiction

**Issue:** Namita's diagram shows three arrows from B2 directly into T1 ("known errors"), T2 ("contextual"), and T3 ("complex"), *and* shows dashed "unresolved" escalation arrows from T1→T2→T3. These are two contradictory routing models. If B2 classifies complexity upfront, the cascade is meaningless. If the cascade is the real design, the B2-to-T2/T3 shortcuts should not exist.

**Resolution:** Every error enters at T1. Escalation to T2, then T3, happens only when the prior tier cannot resolve. The B2→T2 and B2→T3 shortcuts are removed. B2 does not classify complexity.

**Rationale:** This matches Colin's deterministic-first principle. Even if B2 could guess "this looks complex," sending it straight to T3 incurs LLM cost for something that might have been a known error. T1 is cheap enough that sending everything through it is the right default.

### 2. NLP in Block 2 is a layering violation

**Issue:** Namita specified three NLP-adjacent activities in B2:
- NLP chunking (break file into logical units)
- Semantic chunk boundaries (a restatement of chunking)
- NLP summarization "to shrink text prior to tier 2/3 calls"

All of these are expensive operations performed *before* tier routing. Colin called this "ass backwards" — you're paying NLP costs on errors that T1 would have resolved for free.

**Resolution:**
- **Chunking stays in B2, but deterministic.** Logs have structural markers (timestamps, phase delimiters, error prefixes). No NLP required to segment 500K-line files into analyzable units.
- **NLP summarization moves into T3 (LLM tier).** Summarization only has value when the LLM is actually invoked. It becomes a preamble step inside T3, not a preemptive step in B2.
- **"Semantic chunk boundaries" is redundant** with deterministic chunking and is dropped.

**Rationale:** This preserves the cost gradient. Cheap operations upstream, expensive operations only when needed.

### 3. B5.1 is mis-positioned as a sub-block of B5

**Issue:** "Auto-Fix & PR" is remediation, not classification. It consumes outputs from all three tiers. Numbering it "5.1" makes it look like an appendage of Tier 3, which will confuse reviewers.

**Resolution:** Promote to its own block. The rebuild uses:
- B1 Ingest
- B2 Parse
- B3 Classify (with three internal tiers shown visually)
- B4 Remediate (formerly 5.1)
- B5 Storage
- B6 Serve

### 4. Storage writers — Claude's original framing was wrong; corrected

**Claude's original (incorrect) concern:** T1, T2, T3, and B5.1 all point at B6 in Namita's diagram. Claude read this as four writers contending for the same fact table, with race conditions, update ambiguity, and schema ownership issues.

**Colin's correction:** The architecture is an **inverted-pyramid cascade**. Each error is caught at exactly one tier:
- Error enters T1.
- If T1 catches it → T1 writes the classification row, done.
- If T1 misses → falls through to T2. If T2 catches → T2 writes the classification row, done.
- If T2 misses → falls through to T3. T3 writes the classification row.

Each error produces **exactly one classification row**, written by whichever tier caught it. No tier ever writes for an error that another tier already owns. The cascade is self-regulating by construction.

B5.1 (remediation) writes to a **separate remediation / PR table**, joined to the classification row by `error_id`. Different table, different writer, no contention.

**Actual storage model:**
- **Classification fact table** — one row per error, written by T1, T2, or T3 (mutually exclusive). All three tiers write the same schema. No races, no ambiguity.
- **Remediation table** — written by B5.1, keyed by `error_id`. Joined to the classification row at read time when remediation context is needed.

**The append-only event-log idea is abandoned** — it was Claude over-engineering for a non-problem. The simple cascade + separate remediation table is correct and cleaner.

**Lesson recorded:** Do not pattern-match parallel-processing concerns onto a cascade. A funnel is exclusive by design.

### 5. Bazel Docs Scraper as the T1 source

**Issue:** Scraping Bazel HTML docs is brittle. Doc structure changes break the scraper.

**Resolution:** Replace with an **Error Catalog Service** informed by two sources:
- **Historical record** from Cisco's own build logs (what errors they actually hit)
- **Known error catalogs from Bazel releases** (version-locked, refreshed on Bazel upgrade)

Colin's note: Bazel version doesn't change frequently at Cisco, so the version-lock cost is low. The catalog service is presented as informed-and-seeded rather than exhaustively-live. Not a battle to fight in the current diagram; the important thing is the architecture supports it.

### 6. No orchestration, error handling, or observability layer

**Issue:** A production architecture document without these is incomplete. Reviewers will flag it.

**Resolution:** **Apache Airflow wraps the whole pipeline.** Cisco already uses Airflow, so this is free adoption. Airflow gives DAG topology, retries, DLQ, SLA monitoring, and observability hooks. Shown as a cross-cutting layer in the diagram.

### 7. No feedback loop for novel errors

**Issue (raised by Claude):** When T3's LLM handles a genuinely novel error and a human approves the PR in B4, that is a high-value signal. Without a feedback loop, the T1 catalog stays static and "novel" volume grows over time, slowly eroding the cost savings of tiering.

**Resolution:** Add an explicit dashed edge `B4 approved fix → T1 catalog (promote)`. When B4's PR is human-approved, the error pattern is promoted into the T1 catalog (or T2 training data, depending on pattern shape) so the next occurrence hits the cheap path.

---

## Issues Claude Raised That Were Conceded After Colin's Feedback

### Star schema is over-engineered

**Claude's original concern:** Star schema signals OLAP emphasis, but the MCP workload is lookup-heavy.

**Colin's correction:** Star schema is standard dimensional modeling. Fact table of events + dimension tables of entities fits both lookup (trace error → commit) and aggregation (error rates over time) access patterns. Not over-engineered — it's how you properly model this kind of data.

**Claude position:** Concession accepted. Star schema stays.

### Pull exhaustive error catalog live as a background service is "easy"

**Colin's original framing:** Not much work to pull a complete list of Bazel error codes + permutations as a live service.

**Claude's pushback:** Bazel doesn't publish a formal error-catalog API. The canonical source is error strings in Bazel's Java/Go source code. Realistic sourcing options: (a) parse Bazel source per release, (b) derive from historical logs, (c) hybrid seed-and-grow. It's a sub-project, not a flag to flip.

**Resolution:** Colin agreed not to fight this battle today. Catalog service is positioned as informed by historical record + Bazel release catalogs. Acknowledged sub-project, scoped realistically for Srinivas conversation.

---

## Diagram Style Corrections

These are presentation corrections that affect the rebuild.

1. **"Block" is wasted space.** Use `B1`, `B2`, `B3` prefixes or numbered steps. Do not spell out "Block 1" etc.
2. **Tier labels should be visual, not typographic.** Color, vertical stacking, and a one-word functional label ("Deterministic," "ML / NLP," "LLM") convey tier identity without the word "Tier."
3. **Purple palette** (BayOne brand) — the document is a BayOne deliverable, not a slide. Mermaid purple theme variables from `mermaid_design_standards.md`.

---

## Revised Topology (To Build)

### Main pipeline (top to bottom or left to right)

1. **B1 Ingest** — NFS watch, batched 15–30 min. Event-driven listed as future option (pending).
2. **B2 Parse** — Deterministic chunking (timestamp / phase delimiter / error prefix). No NLP. No summarization.
3. **Classify** (single entry at T1, cascade via dashed "unresolved" arrows):
   - T1 Deterministic (regex + catalog lookup)
   - T2 ML / NLP (classification, confidence scoring)
   - T3 LLM (root cause, fix suggestion; NLP summarization only happens here, as a preamble)
4. **B4 Remediate** — Consumes outputs from T1/T2/T3. Code patch, Git branch/commit, PR, build verification trigger, human review gate.
5. **B5 Storage** — Star schema with two related tables:
   - **Classification fact table** — one row per error, written by whichever tier caught it (T1, T2, or T3). Mutually exclusive by cascade.
   - **Remediation table** — written by B4, keyed by `error_id`. Joined to classification at read time.
6. **B6 Serve** — MCP tools for agents; optional hooks for analytics / alerting.

### External feeds

- **Error Catalog Service** (replaces Bazel docs scraper) → T1. Informed by historical Cisco logs + Bazel release catalogs.
- **MySQL build metadata** → B1 (correlate) and B5 (dimensions).
- **Git / GitHub APIs** → B4 (PR creation), B6 (live lookups).

### Cross-cutting

- **Apache Airflow** wraps the pipeline end-to-end. Provides orchestration, retries, DLQ, SLA monitoring, observability.

### Feedback edges

- **B4 approved fix → T1 catalog (promote)** — dashed edge labeled "promote to catalog." Closes the novel-error feedback loop.

---

## Open / Pending Items

- **Ingestion mode decision** (batched vs event-driven) — mark as pending in the diagram, same as Namita's.
- **CI vs CD log format differentiation** — Namita flagged this; TBD whether the pipeline splits for CI vs CD or unifies. Out of scope for this diagram rebuild; mark pending.
- **Error Catalog Service build effort** — scoped for later conversation with Srinivas; acknowledge in block-by-block notes.

---

## Status

- Review complete.
- Revised topology agreed.
- Ready to rebuild as Mermaid diagram in BayOne purple palette at `cisco/cicd/deliverables/proposed_architecture_mermaid_2026-04-16.html`.
- Colin to confirm any final adjustments before build.
