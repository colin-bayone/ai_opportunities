# 10 — Open Questions and Risks

**Purpose of this document:** Everything the transcripts explicitly flag as unresolved, plus the risks the engagement has surfaced that the execution session should watch for. Questions here are for the execution session to hold in mind as it works, raising to Colin when the code or the research files do not resolve them. Risks are for the execution session to anticipate and avoid.

All items trace to a specific source in the research library.

---

## 1. Open Questions — Product and Scope

### 1.1 Exact column set for the Alarms table
**Source:** Set 07 walkthrough (`research/07_meeting_product_walkthrough_faults_2026-04-06.md`).
**Status:** Walkthrough confirmed columns exist and a column picker is on the right side but did not enumerate the actual column list.
**How to resolve:** Read the EPNM alarms code. If not clear, raise to Jenis through Colin.

### 1.2 Complete left-menu enumeration for Device Details
**Source:** Set 07 walkthrough.
**Status:** System summary, device details, chassis and enrollment were mentioned. Others were referenced as "and other left-menu items" without enumeration.
**How to resolve:** Read the EPNM Device Details code. If not clear, raise to Akhil through Colin.

### 1.3 Complete action list for Device 360
**Source:** Set 07 walkthrough.
**Status:** Device Console was named. "Different different actions" were referenced without enumeration.
**How to resolve:** Read the EPNM Device 360 code. If not clear, raise to Akhil through Colin.

### 1.4 Interface 360 structure
**Source:** Set 07 walkthrough.
**Status:** Unclear whether Interface 360 has the same tab structure as Device 360 or a different interface-specific layout.
**How to resolve:** Read the EPNM Interface 360 code.

### 1.5 Bulk-import CSV schema
**Source:** Set 07 walkthrough.
**Status:** A sample CSV is downloadable. Required columns, optional columns, and validation rules were not described.
**How to resolve:** Download the sample CSV (once access is provisioned) and review the EPNM import validation logic.

### 1.6 Device-add wizard step-by-step breakdown
**Source:** Set 07 walkthrough.
**Status:** IP address as the first step, then SNMP / Telnet / HTTP / HTTPS credentials in subsequent steps. Step count and field-by-step detail not fully captured.
**How to resolve:** Read the EPNM device-add wizard code.

### 1.7 State-management scheduling UI
**Source:** Set 07 walkthrough.
**Status:** "Schedule maintain state" and "schedule managed state" actions exist. UI controls (time picker, scheduling semantics) not described.
**How to resolve:** Read the EPNM scheduling UI code.

### 1.8 Chassis View interactivity reimplementation status
**Source:** Set 07 walkthrough. Implicit in the 80-90 percent backend coverage figure.
**Status:** Whether the interactive Chassis View component (module slot state clicks, port state interactions, hardware hierarchy drill-down) is part of the 80 percent reimplemented in EMS or part of the approximately 10-20 percent gap was not confirmed.
**How to resolve:** Read both EPNM ChassisView and the EMS equivalent. If there is no EMS equivalent, this becomes a gap item requiring Selva's decision.

### 1.9 Database-bypassing operations
**Source:** Set 07 walkthrough. Ramkrishna said "in most of the cases, it won't directly go to the [device]. It reads from the database."
**Status:** Some operations do query devices directly. Which operations is unknown.
**How to resolve:** Read the EPNM application code for direct device queries.

### 1.10 Syslog UI layout, filtering, and relationship to alarms / events
**Source:** Set 07 walkthrough.
**Status:** Syslogs are a third data type. No UI detail was provided.
**How to resolve:** Read the EPNM syslog code.

### 1.11 Advanced filter structure (alarms)
**Source:** Set 07 walkthrough.
**Status:** Quick filter and advanced filter exist. Criteria, operators, saved filter capabilities, date / time range semantics were not described.
**How to resolve:** Read the EPNM alarms advanced filter code.

### 1.12 Severity-based row coloring
**Source:** Set 07 walkthrough.
**Status:** Not discussed. EPNM alarms almost certainly have severity-based visual cues; details are not captured.
**How to resolve:** Read the EPNM alarms table styling.

### 1.13 Cross-navigation between alarms, events, and syslogs
**Source:** Set 07 walkthrough.
**Status:** Not described. Tabs, separate left-nav entries, or contextual links are all possible.
**How to resolve:** Read the EPNM fault management navigation code.

### 1.14 Real-time update mechanism for alarms
**Source:** Set 07 walkthrough.
**Status:** How new alarms appear in the table (auto-refresh, polling, push, server-sent events) was not discussed.
**How to resolve:** Read the EPNM alarms client-side update logic. Check for corresponding EMS backend support before replicating.

### 1.15 Expandable row content details
**Source:** Set 07 walkthrough.
**Status:** Every alarm row is expandable and contains "general information" and other detail. Exact fields, lazy-loading behavior, and data source were not enumerated.
**How to resolve:** Read the EPNM alarms row expansion code.

### 1.16 Full alarm action set beyond Clear
**Source:** Set 07 walkthrough.
**Status:** Clear alarms was confirmed. Other actions "similar to the network devices" were referenced without enumeration. Typical fault-management actions (acknowledge, annotate, assign, suppress, create trouble ticket) are unknown for this product.
**How to resolve:** Read the EPNM alarms toolbar and context menu code.

### 1.17 Time-based filtering on events
**Source:** Set 07 walkthrough.
**Status:** "Past 8 hours" and "all events" were named. Full preset list, custom range support, and calendar picker support were not described.
**How to resolve:** Read the EPNM events filter code.

### 1.18 Relationship between the most-recent-events popup and the full events page
**Source:** Set 07 walkthrough.
**Status:** Both exist. Whether they show the same data with different filters or different data sources is unclear.
**How to resolve:** Read the EPNM events code.

---

## 2. Open Questions — Architecture and Technology

### 2.1 Exact EMS backend repository names
**Source:** Set 07 walkthrough.
**Status:** Frontend repos (Infra UI, Common UI, EMS UI) were named. Corresponding backend repositories exist but were not enumerated. EMS Assurance was referenced as the fault backend.
**How to resolve:** Confluence page or Akhil's email with code pointers.

### 2.2 Shell app loading mechanism
**Source:** Set 07 walkthrough.
**Status:** How Infra UI loads EMS UI feature pages (micro-frontend, lazy-loaded Angular modules, or a monolithic Angular build) was not described.
**How to resolve:** Read the Infra UI repo. Check the routing configuration and module federation setup if any.

### 2.3 Common UI consumption pattern
**Source:** Set 07 walkthrough.
**Status:** How Common UI is consumed by EMS UI (npm package, Git submodule, or built together) is unclear.
**How to resolve:** Read the EMS UI `package.json` and build configuration.

### 2.4 Harbor versus Magnetic relationship
**Source:** Set 07 walkthrough. Praveen said "Harbor and Magnetic design system."
**Status:** Whether these are two separate systems, two layers of one system (Harbor as the component library and Magnetic as the broader Cisco design language, or vice versa), or something else is unclear.
**How to resolve:** Read the design system integration in Common UI. Confirm with Akhil if necessary.

### 2.5 Toggle state persistence mechanism
**Source:** Not discussed. The Set 08 conversion patterns research proposed `localStorage` as the POC default.
**Status:** Per-user (persisted in backend), per-session, or per-browser (localStorage) has not been agreed. For POC, `localStorage` is a reasonable default per the research.
**How to resolve:** Implement using localStorage for POC. Flag the decision to Selva for the product phase.

### 2.6 Go services scope on the EMS backend
**Source:** Set 07 walkthrough. Ramkrishna: "There are areas, at least on the device management side, and there are Go services running at the back end."
**Status:** Which specific endpoints are Go versus Spring Boot is not mapped. Whether the Angular frontend calls Go services directly or only through Spring Boot is unclear. Whether gRPC is used for inter-service communication is unknown.
**How to resolve:** Read the backend endpoint definitions. This is contextual — the POC does not call Go directly.

### 2.7 The approximate 10-20 percent backend gap, for POC screens specifically
**Source:** Set 07 walkthrough. Ramkrishna's "at least 80 percent" framing.
**Status:** Which specific EPNM features for Inventory and Fault Management are missing from EMS is unknown. Gap analysis is part of the POC work.
**How to resolve:** Discover through code deep dive (work item B1). Flag to Selva per item E1 handling.

### 2.8 Test suite format and repository location
**Source:** Set 07 walkthrough.
**Status:** Cisco's existing test infrastructure covers seven categories and thousands of cases, with data-driven coverage. Specific test framework, test-case format, and repository paths were not named.
**How to resolve:** Request from Cisco engineering team (action item B3 / Set 07 action item 12) or search the Confluence page.

### 2.9 Integration points for API testing of the classic UI
**Source:** Set 07 walkthrough (testing discussion).
**Status:** Because the classic UI calls the existing EMS backend, API-level testing of the integration points between the Angular classic UI and the EMS APIs was not explicitly discussed.
**How to resolve:** Execution-session-driven decision, in coordination with Colin.

---

## 3. Open Questions — Access and Operations

### 3.1 Specific AD groups needed
**Source:** Set 07 walkthrough.
**Status:** Akhil referred to "a few groups" without enumeration.
**How to resolve:** Resolved during AD provisioning (work item A1). Akhil or the Cisco team names them when enrolling Colin.

### 3.2 VM provisioning timeline
**Source:** Set 07 walkthrough.
**Status:** No firm date was committed. Ramesh offered to facilitate but a specific provisioning date was not set.
**How to resolve:** Follow-up through Selva or Ramesh. Escalate if delayed.

### 3.3 Recurring sync meeting cadence and time slot
**Source:** Set 07 walkthrough.
**Status:** Daily versus weekly and the specific time slot were not agreed. The India / EST overlap constraint is narrow (8:00 AM to 12:30 PM EST).
**How to resolve:** Selva or Aadit sets up. BayOne should be flexible within the overlap window.

### 3.4 Specific US contact for VM provisioning
**Source:** Set 07 walkthrough. Ramkrishna alluded to US-based resources; Ramesh was flagged as the best facilitator.
**Status:** The specific person or team who actually provisions the VMs was not named.
**How to resolve:** Ramesh or Selva through follow-up.

### 3.5 Confluence page access for Colin
**Source:** Set 07 walkthrough.
**Status:** A Confluence page was assembled and Akhil walked Colin through it live. Whether Colin has independent access (versus viewing during a walkthrough) was not confirmed.
**How to resolve:** Try to access. Raise to Selva if blocked.

### 3.6 Neha's access status
**Source:** Set 07 walkthrough.
**Status:** Whether Neha needs Cisco accounts, repository access, or AD group membership was not explicitly discussed.
**How to resolve:** Neha and Colin coordinate with Selva.

### 3.7 The "Cerny" message from Set 03
**Source:** `research/03_meeting_next_steps_2026-03-25.md`.
**Status:** An informal end-of-meeting comment (after Guhan had departed) referenced a message from someone sounding like "Cerny" about another team working in this area. Never resolved.
**How to resolve:** Colin may or may not have resolved this informally since. If it resurfaces, it becomes a scope question.

---

## 4. Open Questions — Testing

### 4.1 Who provides the existing test suites and how
**Source:** Set 07 walkthrough.
**Status:** Colin asked for access and run-through. No specific person was assigned the delivery. Praveen, Akhil, and Jenis are the likely contacts.
**How to resolve:** Follow up through Selva.

### 4.2 Customer-specific profile testing inclusion
**Source:** Set 07 walkthrough.
**Status:** Whether these are in scope for the POC versus the full engagement was not discussed.
**How to resolve:** Explicit ask to Selva. Default assumption: deferred to the full engagement.

### 4.3 Scale testing inclusion for the classic UI
**Source:** Set 07 walkthrough.
**Status:** Whether scale testing applies to the POC classic UI was not discussed.
**How to resolve:** Explicit ask to Selva. Default assumption: deferred.

### 4.4 QA dashboard validation
**Source:** Set 07 walkthrough.
**Status:** Whether the Cisco team will actively review the QA dashboard during the POC or treat it as a passive artifact was not established. Dashboard visibility itself was deferred to the full engagement.
**How to resolve:** Colin aligns with Selva as the POC approaches closeout.

### 4.5 Migration and upgrade testing for the toggle feature itself
**Source:** Set 07 walkthrough.
**Status:** Not discussed. Whether the classic-view toggle needs explicit migration testing between EMS releases is an open question.
**How to resolve:** Deferred to the full engagement unless specifically raised.

---

## 5. Open Questions — AI Compliance and Tooling

### 5.1 DeepSite / DeepSeek formal status at Cisco
**Source:** 2026-04-06 walkthrough. Colin referenced DeepSite (or DeepSeek) as another Cisco-context AI tool.
**Status:** Formal status (approved, restricted, under evaluation) not specified.
**How to resolve:** If relevant for any reason, ask Selva or Ramesh. Not relevant if the tool is not needed for the POC (POC uses Claude Code and local LangGraph only).

### 5.2 Claude Code data flow specifics
**Source:** 2026-04-06 walkthrough.
**Status:** Whether Cisco has a private Claude instance, whether code is sent to Anthropic under an enterprise agreement, or some other arrangement is not specified.
**How to resolve:** Treat the Cisco-issued Claude Code as the approved tool and do not use alternatives. If the exact data flow matters, ask Ramesh.

### 5.3 Library approval process mechanism
**Source:** 2026-04-06 walkthrough.
**Status:** Colin stated libraries must be approved first. Specific approval process and time-to-response were not described.
**How to resolve:** Route library asks through Colin.

### 5.4 LangGraph eventual hosting
**Source:** 2026-04-06 walkthrough. Colin: "for the moment, my Cisco-issued laptop."
**Status:** If LangGraph moves off the laptop, it moves to Cisco server or VM, not to an external cloud. Specific plan not set.
**How to resolve:** Not an immediate POC decision.

### 5.5 Cross-engagement tool sharing
**Source:** 2026-04-06 walkthrough.
**Status:** Whether the NX-OS CI/CD engagement and the EPNM-to-EMS engagement share tooling or environments is not specified.
**How to resolve:** Default assumption: separate environments. Cross-sharing requires specific approval.

---

## 6. Risks

Risks are not the same as open questions. These are things that could go wrong and require proactive attention.

### 6.1 Backend regression affects both views simultaneously
**Source:** Selva in the 2026-03-25 scope reframe meeting. Direct quote: "Any service change we have — we are in the critical release path, which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way."
**Mitigation:** Treat any backend touchup as a high-care change. Narrow the change to the smallest viable scope. Route through Selva before making any backend change, even narrow ones. Verify regression behavior in both views before declaring the change complete.

### 6.2 Undocumented legacy behavior in EPNM
**Source:** Set 08 research. No design documentation exists (confirmed by Selva in Set 02).
**Mitigation:** Agent-driven code exploration is the primary pattern. Expect quirks in sorting, filtering, data transformation, and device-type-specific logic buried in widget code. Preserve rather than "clean up" — fidelity to EPNM behavior is the acceptance bar.

### 6.3 Pub/sub dependency web in EPNM
**Source:** Set 08 research.
**Mitigation:** Catalog all `topic.publish` and `topic.subscribe` calls early. The contracts are invisible from the code structure but are essential for the classic view to reproduce EPNM behavior faithfully.

### 6.4 Classic UI tests will not carry over from EPNM
**Source:** 2026-04-06 walkthrough. Jenis raised this; Praveen expanded; Colin confirmed the replica work will happen in the full engagement.
**Mitigation:** Do not assume existing EPNM UI tests protect the classic view. Internal unit testing for the POC is the minimum; Playwright-based equivalence verification is the POC's functional check.

### 6.5 Cross-timezone coordination delay
**Source:** Narrow India / EST overlap (8:00 AM to 12:30 PM EST).
**Mitigation:** Default to async through the WebEx team space and email. Batch questions. Use the recurring sync for decisions that must be synchronous. Do not let time-zone friction convert into a multi-day resolution cycle for small questions.

### 6.6 Pricing model inconsistency with reframed scope (internal only)
**Source:** Documented flag across the research library (Sets 04 and 06).
**Relevance to the execution session:** This is an internal BayOne commercial matter, not something the execution session addresses. The scope the execution session delivers against is the scope in this handoff package — two screens, UX overlay, backend untouched. Any commercial recalibration is Colin's.

### 6.7 Access provisioning stalling the engagement
**Source:** Hardware provisioning itself took roughly five weeks versus an initial 1-2 week estimate (Sets 01 through 03). AD group and VM provisioning have no firm dates as of Set 07.
**Mitigation:** Active follow-up through Colin. Escalate through Selva if the delay threatens the POC work.

### 6.8 Scope creep via "while we're at it"
**Source:** Implicit risk in any POC that sits inside a larger engagement.
**Mitigation:** The scope is two screens. Any expansion (even "small" suggestions from the Cisco team) gets flagged to Colin before acting. Selva will be the arbiter.

### 6.9 Accidental customer-visible AI references
**Source:** Customer-transparency principle throughout the engagement.
**Mitigation:** Commit messages, code comments, UI text, and PR descriptions should read as standard Cisco engineering output. No mention of prompts, agents, models, AI tooling, or LangGraph in customer-facing artifacts. Colin is the final gate.

### 6.10 Tool sprawl
**Source:** AI compliance constraints.
**Mitigation:** Claude Code and local LangGraph only. No "it would be nice if I could use X" decisions. Route all tool questions through Colin.

### 6.11 The 20 percent backend gap is larger than expected for one of the POC screens
**Source:** Ramkrishna's "at least 80 percent" framing. The gap is not enumerated.
**Mitigation:** Discover through the code deep dive (work item B1). If a screen turns out to have significant missing backend support, raise to Selva rather than trying to build around it. Per Praveen's guidance, the answer is to add the missing capability to the EMS backend over time, not to bring EPNM's backend forward.

### 6.12 Interpretation drift from the 2026-04-06 meeting
**Source:** The walkthrough is the most technically dense meeting and established many specifics. Transcripts are speech-to-text and have errors.
**Mitigation:** Trust the screenshots for attendee names. Trust the Confluence page for repo lists. When the transcript is ambiguous, defer to the code over the transcript. When both the transcript and the code are ambiguous, raise to the relevant tech lead through Colin.

---

## 7. What to Do With This List

The execution session should treat sections 1 through 5 as a living backlog of questions to resolve while working. Most will resolve naturally through code reading. Some will need to be raised.

Section 6 (risks) is a checklist to revisit at key decision points: when opening a new screen's conversion, when a library question arises, when a backend change seems necessary, when preparing the POC demonstration, when writing a commit message that is about to be pushed.

If the execution session encounters an item not on this list that feels material, add it to this document or raise to Colin. The handoff docs are not static; updates during the POC should be expected.
