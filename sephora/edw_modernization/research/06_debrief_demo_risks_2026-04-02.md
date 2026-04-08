# 06 - Debrief: Demo Risks and Known Issues

**Source:** /sephora/edw_modernization/source/saurav-colin_4-2-2026.txt
**Source Date:** 2026-04-02 (Demo Prep Call)
**Document Set:** 06 (Saurav/Colin Demo Prep)
**Pass:** Focused deep dive on demo risks, known issues, and things to avoid

---

## Context

This document catalogs every known issue, risk, and constraint identified during the April 2, 2026 demo prep call between Colin Moore and Saurav Kumar Mishra. The demo is scheduled for later that day (approximately 6:00 PM Colin's time, 3:30 AM Saurav's time on April 3). Colin will present the EDW Modernization agentic pipeline to the Sephora team. Saurav may or may not be available to join given the time zone difference.

---

## Critical: Do NOT Touch During Demo

### 1. Reject and Retry Button
- **Severity:** Critical -- will visibly break the demo if clicked
- **Issue:** The "Reject and Retry" button next to the auto-fix option on the review screen sends the pipeline back through SQL generation, gate checks, config generation, config gate, and validation. The backend execution works correctly and the execution log will show proper processing. However, the DAG animation on the front end breaks: the nodes do not light up correctly on the retry path. Since the front end is built with vanilla HTML/CSS/JavaScript (no React, Vue, or any framework), the DAG state management for re-traversal is fragile.
- **What happens if clicked:** The user sees the DAG screen with incorrect node highlighting. The execution log continues to show correct progress, but the visual representation is misleading.
- **Workaround:** Use "Auto-Fix" instead. Auto-fix performs surgical edits on the generated SQL (analogous to how Claude Code edits files in place) rather than regenerating the full pipeline. It is functionally superior for the review stage and avoids the DAG re-rendering problem entirely.
- **Will it be fixed before demo:** No. This is a fundamental limitation of the frameworkless front end architecture.

### 2. Configuration Dropdowns (Target Platform, Model Selection, Retry Count)
- **Severity:** Moderate -- will not break anything but exposes non-functional UI
- **Issue:** The dropdowns for target platform, model selection, and retry count on the configuration panel are visual placeholders only. They render correctly and "look good" per Saurav, but they do not connect to any backend functionality.
- **What happens if interacted with:** Nothing will happen, which makes it obvious they are non-functional. If a Sephora attendee asks to change the target platform or model, this becomes an awkward moment.
- **Workaround:** Do not interact with these dropdowns during the demo. If asked, position them as future configuration options: "These are where we'll wire in target platform selection and model configuration once we have the MCP connectors to their Cognos environment."
- **Will it be fixed before demo:** No. These are intentional placeholders for future functionality.

### 3. DAG Node Stages (Clicking Individual Stages)
- **Severity:** Low-moderate -- inconsistent behavior
- **Issue:** Saurav added clickable stages on the DAG for previous runs. They contain data, but the display is incomplete. Saurav explicitly said "best not to open these by clicking the stages" because managing the JavaScript for stage-level detail surfacing without a framework became too complex.
- **Workaround:** Do not click individual DAG stage nodes. If detailed stage-level input/output is needed, show it in LangSmith instead, where all data is properly surfaced.
- **Will it be fixed before demo:** No.

---

## Known Bugs

### 4. Zip Download Not Working
- **Severity:** Low -- easy workaround exists
- **Issue:** After the pipeline completes and the user clicks "Approve," the generated artifacts (Spark SQL, deployment YAML, pipeline YAML, HQL) are available for download. The zip/bulk download button does not work. Individual file download buttons do work.
- **Discovery:** Colin tried the zip download during the call and it failed. He then confirmed individual downloads work fine.
- **Workaround:** Download files one at a time using the individual download buttons. During the demo, if showing the download capability, click individual file download buttons only.
- **Will it be fixed before demo:** Not confirmed. Saurav said "I thought these are working, so I just thought that, yeah, maybe zip is also working," suggesting he had not tested it. Low priority given the workaround.

### 5. Advisory Text Body Not Rendering
- **Severity:** Low -- cosmetic issue, data exists
- **Issue:** When auto-fix generates an advisory finding (as opposed to a bug), the review screen shows the advisory badge/label and a "Click to view" prompt, but the advisory text body does not render. Saurav confirmed this is a front-end rendering issue only; the underlying data is present in the state.
- **Workaround:** If the advisory appears during the demo with no visible text, acknowledge it briefly: "The advisory detail is captured in the pipeline state -- we can see the full text in LangSmith." Do not dwell on it.
- **Will it be fixed before demo:** Saurav said "I will fix it. No worries." This is a rendering fix and likely straightforward, but not confirmed complete.

### 6. Pipeline Runs Table Missing on Colin's Database
- **Severity:** High -- blocks the run history page entirely
- **Issue:** The `pipeline_runs` table exists in Saurav's local database but was never created on Colin's Postgres instance. Without it, the run history page (which shows previous pipeline runs with their statuses, timestamps, and run IDs) will not display any data and throws an error.
- **Discovery:** Colin navigated to the run history page during the call and encountered the error. Saurav immediately identified the cause: "I think this pipeline in my system it is present, but maybe I did not set up like a command which can set this up like a pipeline runs table on your end."
- **Workaround:** None until Saurav pushes the fix.
- **Will it be fixed before demo:** Yes. Saurav is adding an auto-create check so the table is created if not present. He is also seeding it with pre-populated demo data (a few passed runs, one pending, one failed) with varied project names. Colin should pull the latest code and run the updated setup before the demo.

### 7. Stage Step Count Overflow
- **Severity:** Very low -- only triggered by repeated reject-and-retry
- **Issue:** The pipeline normally runs through approximately 15 steps to reach human approval. If the user clicks "Reject and Retry" multiple times, the step count grows (Saurav showed examples at 22, 20, 19, 21 steps). When the step count exceeds roughly 15, the step display in the UI becomes visually cluttered and misaligned.
- **Workaround:** Do not use reject-and-retry during the demo (already covered by Issue #1). If auto-fix is used instead, the step count stays within the normal 15-step range plus the fix steps.
- **Will it be fixed before demo:** No, and it does not need to be given the reject-and-retry restriction.

---

## Operational Risks

### 8. API Throttling (Azure 529 Errors)
- **Severity:** High -- could slow the demo significantly
- **Issue:** The pipeline fires multiple LLM calls in parallel at a concurrency of 4. With the current Azure quota of 75K tokens per minute for both Opus and Sonnet, Saurav has been hitting 529 (rate limit) errors. The pipeline handles these gracefully (retries with backoff) but slows down significantly when throttled. Saurav described hitting "a lot of" 529 errors at higher concurrency, which is why he reduced concurrency to 4.
- **Current quota:** 75K tokens per minute for Opus and Sonnet on Azure Foundry
- **Quota request:** Colin submitted requests for a 4-5X increase on both Opus and Sonnet quotas during the call. Approval is uncertain and may not come through before the demo.
- **What happens if throttling occurs:** The pipeline will not break or error out. It will simply run slower. The execution log shows a status indicator when throttling is occurring ("This shows that it is throttling"). Individual stages that normally take seconds could take minutes.
- **Workaround if slow:** 
  - Saurav suggested a cached run approach: "Maybe add a button which can like move through the stages and while you are talking just click through the stages and it will load all the data as it has already processed once and cached once." This was not confirmed as implemented.
  - Colin can narrate over the execution log while stages process, explaining the architecture of each stage.
  - If severely throttled, pivot to LangSmith to show a completed run's waterfall view, which demonstrates the full pipeline execution without needing to wait.
- **What to say if it occurs:** "The pipeline is handling rate limiting from the Azure API -- it retries automatically. In a production deployment, we'd have dedicated throughput provisioned. Let me show you a completed run while this processes."

### 9. Duration Timer Includes Human Wait Time
- **Severity:** Low -- not a bug, but can create a misleading impression
- **Issue:** The total duration displayed at the end of a pipeline run includes all time from start to finish, including the human review step. If Colin spends 10-20 minutes talking through the review findings, explaining the architecture, or answering questions from the Sephora team before clicking approve or auto-fix, that time is added to the total duration.
- **Impact:** Saurav noted the duration on their prep call was "very long" because they were talking during the review step. A duration of 30+ minutes could make the pipeline look slow when the actual processing time was much shorter.
- **Workaround:** Before clicking approve/auto-fix, note the current elapsed time. After the run completes, if the total duration looks inflated, explain: "That total includes the time we spent reviewing the output together. The actual machine processing time was approximately [X] minutes." Alternatively, reference the LangSmith waterfall view, which shows actual processing time per stage without human wait time.

### 10. Same Project Name for All Runs
- **Severity:** Low -- cosmetic, being addressed
- **Issue:** Since the demo has only one use case (inventory periodic), every pipeline run shows the same project name ("inventory periodic" / "daily inventory") in the run history. This makes the run history page look repetitive and does not demonstrate the multi-project capability.
- **Workaround:** Saurav is hardcoding a few different run entries in the database as part of the pipeline_runs table fix (Issue #6). He committed to adding entries with varied project names (e.g., inventory daily, inventory weekly, all SKUs) and mixed statuses (a couple passed, one pending, one failed).
- **Will it be fixed before demo:** Yes, as part of the database seeding in the pipeline_runs fix.

---

## Front End Architecture Constraint

### 11. No Front-End Framework (Vanilla HTML/CSS/JavaScript)
- **Severity:** Background context -- explains the fragility of several other issues
- **Issue:** The entire dashboard UI is built without React, Vue, Angular, or any front-end framework. Saurav described it as "stick with glue." This is not a bug but the root cause of several issues: the DAG animation breaking on retries (#1), the difficulty surfacing stage-level data in DAG nodes (#3), and the advisory text rendering problem (#5).
- **Why it matters for the demo:** Some interactions may feel slightly fragile. The UI looks polished ("It looks like we used a framework, frankly" -- Colin), but edge-case interactions can expose the fragility.
- **What to say if something looks off:** "The front end is a rapid prototype we built to visualize the pipeline. The real power is in the LangGraph backend -- let me show you the LangSmith trace."
- **Positive framing:** Saurav built this in less than a week without a framework and it looks professional. If anyone asks about the technology stack, this is actually impressive for the timeline.

---

## Pre-Demo Checklist (What Saurav Is Fixing)

| Item | Status | Action Required by Colin |
|------|--------|--------------------------|
| Pipeline runs table auto-creation | Saurav adding check | Pull latest code before demo |
| Pre-populated demo run data (varied names/statuses) | Saurav adding seed data | Pull latest code, verify run history page loads |
| Advisory text rendering fix | Saurav said he would fix | Pull latest code, verify advisory text shows |
| Zip download | Not confirmed as being fixed | Plan to use individual downloads |
| Quota increase (Opus + Sonnet) | Colin submitted requests | Check Azure portal for approval before demo |

---

## Demo Interaction Rules

**Safe to click/interact with:**
- "Load Demo Files" button (hardcoded to load the nine correct source files)
- "Start Pipeline" button
- Execution log (read-only, shows real-time agent activity with timers)
- File preview tabs (SQL, YAML, HQL) with syntax highlighting via highlight.js
- "AI Review" button (sends artifacts for audit review)
- "Auto-Fix" button (surgical edit approach, safe and demonstrable)
- "Approve" button (finalizes the run and adds patterns to knowledge base)
- Individual file download buttons
- Previous run selection from run history (if pipeline_runs table is fixed)
- Collapsible panels (configuration panel has a collapse button)
- Progress bar (shows overall pipeline progress)

**Do NOT click/interact with:**
- "Reject and Retry" button (DAG animation breaks)
- Configuration dropdowns (target platform, model, retry count -- non-functional)
- Individual DAG stage nodes (incomplete data surfacing)
- Zip download button (not working)
- Drag and drop file upload area (placeholder only, not functional)

---

## Recovery Playbook: What to Say If Something Goes Wrong

| Scenario | Response |
|----------|----------|
| Pipeline is visibly slow / stalling | "The pipeline is handling API rate limiting. In production, we'd have provisioned throughput. Let me show you a completed run in LangSmith while this processes." |
| DAG animation looks wrong | "Let me pull up the execution log -- you can see the actual pipeline state here. The backend is processing correctly." |
| Advisory text missing | "The advisory data is captured in the pipeline state. We can see the full detail in LangSmith." |
| Run history page is empty/errors | "We're running a fresh instance for this demo. Let me show you the current run instead." |
| Duration looks too long | "That total includes our review time. The actual processing was approximately [X] minutes -- you can see the breakdown in the LangSmith waterfall." |
| A dropdown does nothing when clicked | "Those configuration options are wired in once we connect to the source systems. For the demo, we're running with the default configuration." |
| Any unexpected front-end glitch | "The front end is a visualization layer. The real pipeline runs on LangGraph -- let me show you the LangSmith trace for the full picture." |

---

## Key Insight: LangSmith as the Safety Net

Throughout the call, both Colin and Saurav repeatedly noted that LangSmith contains complete, reliable data for every pipeline run. It shows:
- Waterfall view of all stages with precise timing
- Input/output for every node (blue = LangGraph node level, orange = LLM call level)
- Structured state objects showing deterministic gate results, LLM findings, validation scores
- Full chat thread context for each agent node
- Parallel execution visualization

If anything goes wrong on the front end during the demo, pivoting to LangSmith provides a complete, professionally presented view of the pipeline execution. Saurav himself noted: "Do we even need a UI? Because LangSmith does a better job in my opinion." Colin's response framed the positioning correctly: the UI serves non-technical stakeholders, while LangSmith serves technical stakeholders. Both exist and both work.

LangSmith data appears within 1-2 minutes of a run completing (not real-time during execution). The execution log on the dashboard is the best place to watch real-time progress.
