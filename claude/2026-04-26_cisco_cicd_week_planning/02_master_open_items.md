# Master Open Items List

**Scope:** Every open or unresolved action item across the entire Cisco CI/CD engagement history (Team Sets 01 through 15, Main Sets 06 through 15) PLUS every item Srinivas specifically requested in Main Set 15.
**Format:** Master list. No per-person assignments yet. That step comes later.
**Sources:**
- `cisco/cicd/team/tracking/action_items.md` (147 items, filtered to open/unresolved)
- `cisco/cicd/team/tracking/decisions.md` (63 decisions; cross-checked for open implications)
- `cisco/cicd/team/tracking/blockers.md` (active blockers chain)
- `cisco/cicd/team/research/14b_expectations_and_outstanding_actions_2026-04-24.md` (status categorization for items 1-136)
- `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/srini_MOM.txt` (Wednesday Apr 22 Srinivas MOM, Colin absent)
- `cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt` (Friday Apr 24 transcript)
- `cisco/cicd/research/15_meeting_summary_2026-04-24.md` (Srinivas's Main Set 15 explicit asks)
- `cisco/cicd/research/15_meeting_access_unblocked_and_deliverables_2026-04-24.md` (Srinivas's deployment target definition)
- `cisco/cicd/research/15_meeting_cicd_app_integration_and_skills_2026-04-24.md` (skills inventory, regression workstream)
- `cisco/cicd/research/15_meeting_deployment_form_decision_2026-04-24.md` (per-user + group concept architecture)
- `cisco/cicd/research/15_meeting_build_track_and_pr_dependencies_2026-04-24.md` (Bazel + GitHub dependency graphs, PR backout use case)
- `cisco/cicd/research/14_meeting_mom_decomposition_2026-04-22.md` (Wednesday MOM Set 14)
- `cisco/cicd/research/13_meeting_open_items_and_scope_updates_2026-04-20.md` (Set 13 carry-forward)

---

## A. Items Srinivas Explicitly Asked For in Main Set 15

These are the items that have to be done because Srinivas asked for them on the most recent call. They are the highest-priority items by definition and they shape everything else.

### A1. Monday weekly status one-pager

GitHub markdown file in the CI/CD repository. Single page. Mermaid where it helps. Tasks in flight, next-Friday target, decision prompt for him to drive scope adjustment. Tracked via the issues list in the same repository. Srinivas's words: "what is the birthday view of the entire summary, right?"

### A2. CI/CD application running on ADS by Friday May 1

Application live on the ADS server. Static FAQ for environmental issues plus dynamic answers via CAT MCP. Both routes feed the same chat user interface. Srinivas's words: "you should be able to bring up the CACD app on your idea server, plug in the CAT MCP and these questions behind it so that the user asks a question in the chat box that I was showing you here that you should be able to get an answer for either dynamic or static, both."

### A3. Static FAQ from prior Q&A data

Build the static FAQ portion of the answer set from the existing answers-by-the-user data. Srinivas's words: "we need to first create a static fat least because not everything is dynamic. Dynamic part is in the cat recipe. Static part is there are some environmental issues and whatnot that is already there in the answers by the user."

### A4. CAT MCP plugged into the CI/CD app

CAT MCP integrated as the dynamic-answer path inside the CI/CD application. Four tools identified, NX repo access now unblocked by Srinivas himself.

### A5. Service-Application-Platform-style backend

Backend designed so that two frontends can plug into it: the CI/CD app chat interface and a WebEx bot in the NX-OS CI pipeline. Srinivas's words: "if you can design the backend as an SAP, then technically we can plug in the UI and plug in as a part of the comp itself."

### A6. WebEx bot deployed on NX-OS CI pipeline

Same backend as the CI/CD app. DeepSight-aware bot in the NX-OS CI WebEx space. User can ask questions in NX-OS CI and get the same routing.

### A7. LLM via circuit API initially

Shared circuit key in the interim. Mid-week conversation between Colin and Srinivas to design how the shared key gets distributed without compromise. Migrates to per-user DeepSight credentials when DeepSight is issued.

### A8. All skills committed to main CI/CD repository

SME-KB is not the destination. The Cisco MCP vault is being constructed on the main CI/CD repository. BayOne pushes there.

### A9. ds agent init pattern for skill distribution

Each user runs `ds agent init` to pull current skills from the main CI/CD repository and install locally. No Codex admin coordination needed.

### A10. PR-to-PR commit attribution dependency mapping (visual)

Build track deliverable. Bazel out-of-box dependency graphs are the substrate. GitHub PR-commit dependency mapping visual is the next-week target. Builds on the call graph from Justin (partial, to be expanded).

### A11. Regression protection workstream

UI-based automation (Playwright) plus backend validation. Modular and adapter-based for cross-app reuse. Srinivas's explicit ask in Main Set 15. The core artifact must be standalone with any application-specific concerns built as an adapter layer ("if I pick the deliverables, it has to be standalone, meaning I should be able to plug and play other places"). Same pattern applies to backend validation. New workstream added to scope.

### A12. Security key rotation pattern (deferred but on the list)

Srinivas raised the static-key-no-rotation concern. Colin offered three patterns (GitHub secrets, Azure Key Vault, Open Web UI). Framed as "add to your list, not urgent." Stays on the master list but is not a this-week item.

### A13. Per-user personalization with group concept (deployment form decision, Main Set 15)

CI/CD app dashboard filters to the logged-in user's own pull requests by default via the existing CI/CD app user session. Manager roll-up runs through the existing Cisco "group concept" feature: a manager configures their own group via the group API, the dashboard pulls group membership from the Cisco directory at view-load time, and aggregates members' pull request data on demand. No central poller. No central compute. Srinivas's words: "it is never a CI-CD app to do whatever you want." BayOne consumes the group API; Srinivas committed to share the API details ("we can tell you what is the group API").

### A14. On-demand pull plus low-frequency dashboard refresh (no central poller)

Mode 1: on-demand pull per pull request triggered by user interest. Mode 2: low-frequency (~30-minute) dashboard refresh per user session. Calibrated to two ceilings: Cisco compute constraint (no spare GPU capacity) and shared per-hour API rate limit on the upstream pull request data source. Colin's words: "we'll make it very low frequency, like half an hour or something." Architectural decision; constrains every subsequent component design this week.

### A15. PR backout dependency intelligence (PR-to-PR graph use case)

Srinivas restated the PR backout use case in Main Set 15 in the most concrete form to date. Ten PRs in a build, one fails, a developer commits a fix on top of another PR, that fix causes a downstream issue, the release lead needs to know which other PRs depend on the one being backed out before pulling it. The PR dependency graph (per A10) must support this specific user workflow. The release-lead "are you okay with three PRs?" question is the validation lens. Bazel out-of-box dependency graphs plus GitHub PR dependency information are the substrates; visual artifact is next-week deliverable.

### A16. Skills inventory documentation in CI/CD repo

Colin committed in Main Set 15 to publish the full skills inventory as documentation in the CI/CD repository. Three skills named in the meeting (Apache eCharts, WebEx bot creation, NXOS issue categorization). Fourth skill not named; needs identification before documentation goes in. Closes a Main Set 14 commitment and gives Cisco visibility into the BayOne delivery footprint.

### A17. NX issue category skill productionized for real-time insights (Wednesday Apr 22 MOM, Directive 2)

The nxos-issue-categorizer skill (built in Team Sets 11-12) needs continued development to enable real-time insights for admin/manager users. Elevates the skill from one-time analysis to continuous monitoring. Srinivas asked for this in Wednesday's MOM-only meeting that Colin missed. Already partially captured in B2 ("Issue categorization skill + dashboard productization") but worth surfacing as a Srinivas-explicit ask, not just an engagement-history item.

### A18. Multi-MCP orchestration architecture (Wednesday Apr 22 MOM, Directives 3 and 4)

Beyond CAT, identify and integrate additional MCPs for other issue categories (Directive 3, sequence: later). Architecture pattern: a main agent routes user messages to the relevant MCP, performs tool calls, returns real-time responses (Directive 4). Each issue category has associated MCPs. Srinivas asked for this in Wednesday's MOM. Not on the current master list. The CAT MCP integration in A4 is the first concrete instance of this pattern.

## B. Open Items From the Engagement History (Team Sets 01-14)

These are items that were assigned across Team Sets 01-14 and remain open or unresolved per Set 14b's catalog. Filtered to remove items that are DELIVERED, SUPERSEDED with no remaining work, or otherwise closed. Status notes are from Set 14b unless updated by Main Set 15.

### B1. Access provisioning and tooling

- **DCN Switching tenant for permanent ADS** (item 3, BLOCKED). Colin owns via item 122. Mahaveer escalation in flight; Anand backup. Three weeks of follow-up have not produced a functional tenant selection in the portal. Status as of Friday EOD: Mahaveer follow-up was scheduled, outcome not yet documented in the chain.
- **CN-SJC-STANDALONE bundle membership** (item 25, PARTIAL). Rolled into the Mahaveer escalation. Open.
- **Pulse and Scribbler access** (items 6, 23 BLOCKED then SUPERSEDED). Effectively closed with the Pulse/Scribbler scope deferral at Main Set 13. No further work needed.
- **Codex / Copilot access via appstore.cisco.com** (item 40). Open for whoever still does not have it. Vaishali and Tanuja excluded (no hardware).
- **DeepSight access on Cisco laptop** (item 131, IN PROGRESS). Srikar pursuing via support ticket. Open.
- **DeepSight credentials for LLM** (Set 15 forward). Coming after demo. Per Main Set 15: "after demo."
- **MCP viewer app for testing external MCPs** (Main Set 13 announcement, Main Set 15 confirmation). Coming soon as playground. Open.
- **NX repository commit-approval-tracking access** (item 124 prerequisite, RESOLVED in Main Set 15 by Srinivas's personal commitment to add user IDs himself). Operationally open until Colin sends user IDs and Srinivas runs the add. Critical-path item.

### B2. Build log and CI/CD application work

- **CD nightly build log visibility, composite vs individual files** (item 57, STALE). Justin has not shown CD logs. Open.
- **Log-snapshot automation script** (item 58, HAND-WAVED). Idea acknowledged, no script produced. Open.
- **Sample and organize log library** (item 59, STALE). Dependency on Vaishali hardware plus no independent progress. Open.
- **Read-only access to main-branch real-run logs on NFS** (item 60, PARTIAL). Now blocking CAT MCP execution under Srikar's ownership. Open.
- **Star-schema data model for CI/CD traceability** (item 61, DELIVERED NARROW). Architecture directional rather than rigorous. Likely needs refinement once data flows through it. Open if the Friday May 1 deployment surfaces gaps.
- **CAT MCP gap analysis vs 12 top-level categories** (item 123, PARTIAL). Four tools identified, gap analysis not yet produced. Open. Now executable with NX repo access committed.
- **Git LFS error on NX-OS repository** (item 124, IN PROGRESS). Justin documentation in hand. Open.
- **Full CI/CD job dependency graph (PR-level)** (item 134, IN PROGRESS). Bazel command received. PR-level equivalent still being determined. Open. Aligns with Srinivas A10 and A15 above.
- **Call graph expansion** (Main Set 15). Justin has done partial call graph work. BayOne to expand and "build into a process" so it produces consistent output as the codebase evolves. Third axis of build track work alongside Bazel build dependency graph and GitHub PR dependency graph. Open.
- **Issue categorization skill + dashboard productization** (Main Set 15 status). Complete on main CI/CD repo. To be productized for real-time via the user-session CI/CD app pattern. Open.
- **DCN tools repo improvements: agent.md, skills, grep-based fallback scripts** (item 106, DELIVERED NARROW for recommendation, verification by Namita open). Saurav recommended; Namita to verify current state of `build_error_analysis.md` location and propose patch. Open.
- **DCN tools retry-mechanism clarification** (items 96, 97, 98, PARTIAL). Open question whether the tool runs build + applies fix + diff, or only generates diff. Saurav and Namita disagreed; not resolved via code inspection or via Justin call to a documented answer. Open.

### B3. WebEx bot work

- **WebEx bot deployment on temp ADS with Podman container** (Main Set 15 status). Complete on webex-skills branch, deployable on temp ADS. Open until deployed.
- **Bot compliance policy navigation (registration plus user-cap conflict with 300-user NxOS group)** (item 54). Open until bot is actually deployed and registered.
- **Branch merge strategy resolved as merge-into-main** (Main Set 15). All four skills on the webex-skills branch get merged into the main CI/CD repository. SME-KB is a separate concern. Refactor later once Cisco's MCP vault structure is announced. Operationally open until merge happens.
- **Wall-E bot stranded on dead Podman container** (item 102, DELIVERED NARROW). Architecture work continued on BayOne laptop but the Wall-E bot prototype is stranded. Open until Saurav rebuilds on new hardware (gates on item B5 hardware).

### B4. Documentation, sharing, accountability cadence

- **Documentation sharing in team chat (Mahaveer ADS docs, Justin Git LFS docs)** (item 126, IN PROGRESS, expected today). Open.
- **Formal GitHub issue tracking starts Monday Apr 27** (item 128). Structural inflection point. Open by definition until executed.
- **24-hour update expectation operationalized** (item 129). Open and ongoing.
- **AI tools used aggressively, no manual research** (item 130). Open and ongoing. Methodology now transferred per Set 15.
- **GitHub Enterprise feature research (Actions, Connect, packages, hooks)** (item 120). Open. Two-week target from Set 10.
- **Recurring meetings on team and individual calendars** (item 73). Open, status not recently updated.

### B5. Saurav-specific carryforward items

- **Saurav laptop replacement / SAL buy** (items 28, 31, 74, 75, 84-87). Hardware ticket INC10796337. Status: Saurav working on BayOne hardware while Cisco machine is in repair. Loaner from Cisco Delhi was not confirmed. Open until Cisco hardware is back or SAL Mac is bought. Saurav also owes the lost-work redo (item 86) once hardware lands.
- **MCP endpoint design thinking** (item 121). Ongoing, 3-4 week runway. Open.

### B6. Personnel and policy items from Set 15

- **Client Data Handling Policy distribution** (item 137). Sent. Status: 3 of 6 signed copies received. Pending signatures from the remaining team members.
- **Vaishali and Tanuja direct communication on observer-mode rationale** (item 146). Open early next week.
- **Hold Vaishali and Tanuja in observer mode through Friday May 1 hardware-landing target** (item 144). Open through May 1.
- **Direct accountability conversation with Srikar** (item 142). Status: planned today or Monday. Open.
- **Anand call questioning Cisco-side technical leadership diplomatically** (item 143). Status: planned today. Open as of this drafting.

### B7. Cross-cutting team items

- **Court-case framing for adversarial-party interactions** (item 147). Standing rule. Open and ongoing.
- **Methodology kit packaging for BayOne AI practice** (item 145). Near-term. Open.
- **Singularity-related skill maintenance** (no specific item but Set 15 referenced packaging). Open.

## C. Items Specifically From Main Set 15 Forward Action Items

These were called out in the Main Set 15 access-unblocked file as forward action items. Some overlap with section A above.

- Colin sends NX repo user IDs to Srinivas (today/tonight, gate for B2 NX repo access)
- Colin meets Mahaveer for ADS (today, B1 first item)
- Colin escalates to Anand if ADS unresolved by EOD (today)
- Cisco-side CI/CD app deployment Monday by Anupma backend (Cisco owns this; BayOne integration depends on it; deploys with Jenkins pipeline, staging controller, production controller already wired so BayOne focuses only on business logic)
- Mid-week Colin/Srinivas conversation on shared circuit key distribution (A7)
- Asynchronous unblocking via WebEx space (operational pattern, not a discrete item)
- BayOne consumes the Cisco-supplied environment from Monday onward; no Jenkins pipeline standup work
- Test CAT MCP behavior in the MCP viewer playground when it goes live (operational pattern; the viewer is the validation surface for any external MCP before integration into the application backend)

## C2. Wednesday Apr 22 Srinivas MOM-Only Items (Colin Absent)

These items came out of the Wednesday Apr 22 Srinivas sync that Colin did not attend. The MOM was written by Srikar and Namita. Some overlap with sections A and B above; surfaced separately here so the Wednesday-channel commitments are not lost.

- **CAT category to CAT MCP cross-check connection** (Directive 1). Connect the first workflow (CAT category issues) to the CAT MCP, conduct cross-check, establish an intermediate reply system, then integrate the WebEx bot to respond to CAT issues. Priority: deploy and let users provide feedback. Operationalizes A2-A6 with the CAT-first sequencing.
- **NX issue category skill productionized for real-time** (Directive 2; mirrored as A17 above).
- **Construct or identify MCPs for other issue categories** (Directive 3, sequence: later; mirrored as A18 above).
- **Main agent orchestrates user message to relevant MCP** (Directive 4; mirrored as A18 above).
- **Upload all skills to CI/CD repo** (Directive 5; mirrored as A8 above).
- **One slide for next meeting on open items and access** (Directive 6). Delivered Friday Apr 24; consumed in Main Set 15. Closed but worth noting it traced to a Wednesday MOM directive that the team executed without Colin.
- **Knowledge graph deferred long-term, dependency graph immediate priority** (Namita's section). Srinivas's words via Namita's MOM: "we could work towards knowledge graph but doesn't want to hold the project to start on the effort. So current priority is to leverage dependency graph to ensure progress." Knowledge graph stays on the long-term roadmap as the "graph type theme" Colin used in Main Set 15 to keep it on the map without committing to a current-quarter delivery.
- **GitHub repo for all documentation, design, architecture, and source code** (Namita's section). Srinivas committed in Wednesday MOM to share a GitHub repo BayOne uses for all documentation and code changes. Operationally now overlapping with the main CI/CD repo decision in Main Set 15. The .md format requirement applies to all learning, design, and architecture documents.
- **Justin question: full-job dependency graph (vs per-step)** (Namita's MOM P.S.). Per-build-step Bazel graphs already exist; Namita asked Justin for the full CI/CD build job graph. Tracked under item 134 in section B2 above.

## D. Items Surfaced for Decision (Not Yet Owned)

These are open questions where Srinivas owns the answer or where BayOne needs Srinivas input before owning the action.

- **XPR reference** (mentioned by Srinivas, may be announced next week; affects skill organization). Track for next-week announcement.
- **Shared circuit key distribution mechanism** (mid-week conversation pending). Both sides have input.
- **Group API details** (Srinivas committed to share). BayOne needs the group API contract to wire the manager roll-up dashboard view per A13. Open until Srinivas shares.
- **MCP vault structure announcement** (Srinivas indicated "next week or something" in Main Set 15). Affects how skills are organized once the vault is ready. BayOne pushes to main CI/CD repo in the interim and refactors later when announced.
- **MCP viewer app launch timing** (Srinivas previewed in Main Set 15; not yet live). BayOne should plan to validate CAT MCP behavior in the viewer once available.
- **Justin and Devakar coordination on parallel disk-based dependency work** (Main Set 15). Srinivas owns this himself ("I'll talk to Justin maybe"). BayOne tracks for any direction change but does not act. Open at Srinivas level.
- **Deployment semantics question (item 132)**: what does "deployed by next Friday" mean? RESOLVED in Main Set 15 by the deployment target definition. Closed.
- **Branch merge strategy (item 133)**: WebEx-skills branch merge vs feature accumulation. RESOLVED in Main Set 15 (merge into main CI/CD repo). Operationally open until merge happens; tracked under B3.

## D2. Items Implied by Main Set 13 and 14 That Remain Open

These commitments surfaced in earlier Srinivas meetings but were not converted to action items in the tracker. Surfaced here to ensure they are not lost.

- **Date-snapshot semantics for the chat categorizer** (Main Set 13 Srinivas guidance). Srinivas's exact words: "take the date snapshots, that way you do not have to redo the same dates again. If you have consumed the old data, you can only consume the new data in the consecutive two times." Affects how the categorizer service handles incremental processing. Open as a design constraint for the categorizer productization in B2.
- **Reusable categorizer service framing** (Main Set 13). Colin committed to building the categorizer as a reusable modular service layer applicable across projects, not a one-shot report. Open as a design constraint for the productization work.
- **Modular and pluggable test for every BayOne deliverable** (Main Set 13 reinforcement). Srinivas restated and reinforced this principle in Main Set 15 with the deliverable/adapter framing. Standing rule, open and ongoing.
- **Wednesday user-issue taxonomy deliverable** (Main Set 13 Wednesday Apr 22 deadline). Delivered via the Wednesday MOM-only meeting per C2 above. Closed but traced for completeness.
- **DeepSight reports access at read level** (Main Set 13). Confirmed as adequate for current phase by Srinivas's procedural question. Code execution and repository code access remain longer-term gates. Open in the deeper sense; closed at the read-only-reports level.

## E. The Bare-Minimum Floor for This Week

Per Colin's framing, the temporary ADS deployment is a bare-minimum target the team should be able to do this week with very minimal effort. It is its own document at `03_temp_ads_minimum_bar.md` because the framing matters (this is the floor, not the ceiling). Failure to land this by Friday is not acceptable.

## Exclusion rules (governance)

Exclusion rules for what does and does not appear on this list are documented at `10_exclusion_rules.md` in this session folder. That file is the source of truth.
