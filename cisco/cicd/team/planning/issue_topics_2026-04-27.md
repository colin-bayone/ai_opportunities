# Issue Topics for the Week of 2026-04-27

**Status:** Topics only. Bodies are not drafted in this file. These are the discrete pieces of work that will become GitHub issues on the BayOne and Cisco trackers Colin announced in the Team Set 16 prep call.

**Critical-path target:** Friday May 1 deployment (CICD app on ADS, WebEx bot on the NX-OS pipeline, both wired to a shared backend with a static FAQ path sourced from the NX-OS wiki and a dynamic FAQ path sourced from CAT MCP cache request data).

**Already done (not issues):**
- Client Data Handling Policy signed by both Srikar and Namita (gating mechanism per Team Set 15 decision #58, fully in effect)
- First NX GitHub login completed by both Srikar and Namita (Anupma's hard prerequisite for the lead-only group access that gates CAT MCP execution)

These two items came up repeatedly in the Set 14 to Set 16 chain. They are no longer outstanding and do not appear below.

**Sequencing principle:** Each issue is sized for a 24-hour update artifact and ordered so that completion of one unblocks the next. Day-to-day GitHub issue tracking begins this week per Team Set 14 decision; 24-hour updates are the cadence per Team Set 14 item #129.

---

## Srikar Madarapu

Track: skills, CAT MCP, FAQ, WebEx bot back-end logic.

### 1. CAT MCP dynamic answer path: end-to-end implementation

The single largest issue on Srikar's plate this week. Srikar drives the analysis Colin had hoped any of the team could drive.

Inputs:
- Srikar's own analysis documents (to be dropped at `/cisco/cicd/team/source/week_2026-04-27/day_2026-04-27/srikar/`)
- Anupma's live walkthrough captured in Main Set 16: `cisco/cicd/research/16_meeting_cat_mcp_pr_mapping_resolution_2026-04-27.md`. Confirms the CAT cache request structure already contains the PR mapping plus rich metadata (branch, submitter, bug ID, SHA, sub-initiator, all checks). Reachable from any PR's Checks tab as the cache request creation check.

Output:
- End-to-end happy path: PR ID arriving in chat -> CAT cache request data lookup -> structured response back to chat. No UI work in scope; the path needs to function end to end against the live NX repo.
- Captures the pivot away from the assumed PR-to-CAT mapping table to the cache-request data path.
- Handles any Git LFS clone friction encountered along the way as part of this issue (not its own issue).

Critical-path linkage: this is the dynamic answer half of Friday's deliverable. Without this, the CICD app and WebEx bot have only static answers.

### 2. Static FAQ wiring from the NX-OS wiki

Replaces the prior chat-pattern-analysis approach for the static FAQ source. Srinivas redirected the static-FAQ source to the existing NX-OS wiki in Main Set 16. Anupma confirmed the wiki already contains PR workflows, FAQs, and the startup guide.

Inputs:
- NX-OS wiki link (Divakar committed to share it in the WebEx engagement space; landing today / tomorrow)

Output:
- Bot answers static questions from wiki content for the canonical happy path (e.g., "how do I commit my code") via wiki scrape and indexing.
- Acceptance: bot returns wiki-sourced answers for at least three representative static questions identified in the Set 16 unanswered-chat analysis.

External dependency: blocked until Divakar shares the wiki link.

### 3. Chat-to-wiki feedback loop

Pairs with issue 2. Srinivas accepted Colin's feedback-loop proposal in Main Set 16: chat-discovered static answers proposed as GitHub issues to the wiki repo for human review before merge.

Output:
- Mechanism that detects a chat fix not present in the wiki, opens a GitHub issue against the wiki repo proposing the wiki entry.
- Acceptance: at least one issue is opened against the wiki repo from a chat-resolved exchange the bot processes.

External dependency: assumes the wiki link is in hand and the static FAQ path from issue 2 is functioning.

### 4. Static-vs-dynamic breakdown chart for last six months of unanswered NX-OS chat questions

Deliverable Colin owes Srinivas from the Main Set 16 exchange. Reframes Colin's earlier all-time-resolved analysis into the breakdown Srinivas actually asked for: among unanswered questions, which are static (no DB lookup, answer is well-known) versus dynamic (need DB lookup, e.g., PR-stuck queries).

Inputs:
- Existing nxos-issue-categorizer skill output and dashboard
- The "static" semantic clarification from Main Set 16 (no-DB-required, not point-in-time-frozen)

Output:
- Six-month toggle on the existing dashboard chart
- Static-vs-dynamic classification of the unanswered subset across the last six months
- Link sent to Srinivas

Acceptance: Srinivas can use the chart to identify the highest-volume static pain points first.

### 5. WebEx Bot Builder skill: capture IT, policy, and audit references

Set 16 produced the most complete picture to date of the WebEx bot deployment process at Cisco: the Cisco bot registry portal, the audit and approval flow, the deployment under DSA Atlas (also referred to as DSR Class) generic user ID, the form fields and business justification expectations, the relationship between bot lifecycle and Cisco MyID continuity, and the still-pending bot compliance criteria thread.

Output:
- The WebEx Bot Builder skill is updated to encode this knowledge so any future bot can be built in the BayOne plus Cisco environment without rediscovery.
- Includes the policy references, the case-number-and-form-template handoff pattern, the per-app generic user ID principle from Srinivas, and the open-question list (compliance criteria from Cisco IT).

This is documentation work, sized for one to two days. Not on the Friday critical path but high leverage for the practice.

---

## Namita Ravikiran Mane

Track: build logs, PR commit attribution, dependency graph; peer-leadership posture for Srikar (Team Set 15 decision #60, ongoing posture, not separately tracked).

### 1. PR-to-PR dependency mapping deliverable applying the Friday parallel-agent methodology

Direct execution of the work Colin transferred during the 90-minute Friday Colin-Namita 1:1 (Team Set 15). The methodology coaching session is captured in `cisco/cicd/team/research/15_1on1_research_methodology_coaching_2026-04-24.md`. Namita is expected to have read that file. The deliverable is the work she was supposed to have read it for.

Inputs:
- The methodology transfer captured in the file above (parallel general-purpose agents in Claude Code, prompts that specify attributes not outcomes, SQLite mention to signal system-building intent, current date in prompts, do not over-specify platform or version, markdown file output rather than chat output, rules.md scaffolding alongside research outputs, single-agent query validation before scaling to parallel)
- GitHub SBOM (Software Bill of Materials) feature on the NX repo
- Bazel built-in dependency commands (Justin documented; the command path is built into Git Enterprise rather than a custom Cisco tool, per Main Set 16 reframe)
- Team Set 15 action item #140 (this deliverable was flagged as one-week-overdue by Colin; the methodology transfer was the unblock)

Output:
- A structured markdown artifact set (research folder layout per the methodology), end-to-end PR-to-PR dependency mapping for the NX repo, validated against at least one known recent release-lead PR backout case (the Main Set 13 use case).
- Includes a `rules.md` capturing the methodology choices made.

Critical-path linkage: this feeds the build-failure analysis MCP endpoint scope and the release-lead PR backout use case Srinivas grounded the architecture in (Main Set 13). Not on Friday's deliverable critical path but is the highest-priority backlog item for Namita personally.

### 2. After issue 1 lands: pair with Srikar on his active issues

Posture, not a separate tracked issue. Namita supports Srikar's CAT MCP, static FAQ wiring, and chat-to-wiki feedback loop work. Specific paired-work units may be carved out at standup if a clear hand-off exists. WebEx bot research itself is not in this list (going to Saurav).

---

## Source folder for Colin to drop Srikar's CAT MCP documents

Path: `/cisco/cicd/team/source/week_2026-04-27/day_2026-04-27/srikar/`

The folder is created and has a README explaining what goes there. Drop the documents Srikar shared regarding the CAT MCP dynamic answer path in that folder. Treat as source material; do not modify.

---

## Cross-reference

- Critical-path framing: `cisco/cicd/deliverables/weekly_status_2026-04-27_v3_table.md`
- Main Set 16 outcomes feeding these issues: `cisco/cicd/research/16_summary_2026-04-27.md` plus the eight deep-dive files in the same folder
- Friday parallel-agent methodology coaching for Namita: `cisco/cicd/team/research/15_1on1_research_methodology_coaching_2026-04-24.md`
- Team Set 16 prep call that announced the GitHub issue tracking infrastructure: `cisco/cicd/team/research/16_summary_2026-04-27.md`
