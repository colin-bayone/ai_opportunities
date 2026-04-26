# 09 — Work Items

**Purpose of this document:** The high-level work items at the granularity the transcripts established. No invented tickets. No prescribed methodology for execution inside each item. No timelines. No estimates. No dependencies implied beyond what the transcripts themselves established.

The execution session will decompose each item into concrete code-level steps on arrival. This document is the backlog as Cisco and BayOne have framed it, not a project plan.

---

## How to Use This Document

Each item includes:

- **What it is.** The work item at the level the transcripts stated it.
- **Source.** The meeting or research file where the item originated.
- **What Cisco committed to.** Any Cisco-side responsibilities tied to the item.
- **What BayOne committed to.** Any BayOne-side responsibilities tied to the item.
- **Known inputs.** Files, docs, or meetings the execution session should reference.

Items are ordered roughly by when the execution session is likely to encounter them. Cisco-side access and operational items are listed first because most subsequent work depends on them.

---

## A. Access and Environment Setup

### A1. Active Directory group enrollment for repository access

**What it is.** Colin's existing Cisco ID (`colmoore@cisco.com`) gets added to the AD groups that unlock EPNM and EMS repositories. Specific groups were not enumerated in the walkthrough — Akhil referred to "a few groups."

**Source.** 2026-04-06 walkthrough. Set 07 action item 1.

**Cisco commitment.** Akhil or the Cisco team owns adding Colin to the groups. Aadit will help.

**BayOne commitment.** Confirm access works once provisioning is complete; flag if any expected repo is still inaccessible.

**Known inputs.** Repository list from Akhil's follow-up email and the Confluence page.

---

### A2. VM provisioning — EPNM read-only

**What it is.** A dedicated virtual machine with read-only access to a running EPNM instance. Purpose: exploring the existing classic UI, screen layouts, data flows, and behavior.

**Source.** 2026-04-06 walkthrough. Set 07 action item 6.

**Cisco commitment.** Ramesh (US-based) facilitates. Specific provisioning owner not named.

**BayOne commitment.** Use the VM for reference only. No development or code deployment.

**Known inputs.** None — this is environment setup.

---

### A3. VM provisioning — EMS / CNC development

**What it is.** A dedicated virtual machine for EMS / CNC development. Initially read-only for exploration, then development access with the ability to patch artifact binaries and verify.

**Source.** 2026-04-06 walkthrough. Set 07 action item 7.

**Cisco commitment.** Ramesh facilitates. Specific provisioning owner not named.

**BayOne commitment.** Work on this VM only (no personal machines, no downloads). Follow the access model Ramkrishna described: read-only to start, patching when code is ready.

**Known inputs.** Access to EMS UI, Common UI, Infra UI, and relevant backend repositories.

---

### A4. WebEx team space creation

**What it is.** A WebEx team space for ongoing coordination between BayOne and the Cisco engineering team.

**Source.** 2026-04-06 walkthrough. Set 07 action item 3. Also committed in the 2026-03-25 scope reframe meeting (smaller space between Selva, Colin, and Rahul).

**Cisco commitment.** Aadit or Praveen creates the space. Selva coordinates.

**BayOne commitment.** Neha supplies the BayOne team member list. Colin and the execution session use the space as the primary async channel.

---

### A5. Recurring sync meeting cadence

**What it is.** A recurring sync meeting with the approximately 12 Set 07 attendees. Cadence (daily, weekly) and specific time slot were not agreed in the meeting.

**Source.** 2026-04-06 walkthrough. Set 07 action item 5.

**Cisco commitment.** Selva or Aadit sets up the cadence. India-EST overlap is roughly 8:00 AM to 12:30 PM EST.

**BayOne commitment.** Attend. Colin (or whichever BayOne person is covering) is the primary presenter of progress.

---

### A6. Confluence page review

**What it is.** Colin reviews the Confluence page the Cisco team prepared: user guides, recordings, API docs, repo links.

**Source.** 2026-04-06 walkthrough. Set 07 action item 8.

**Cisco commitment.** Confluence page already prepared. Access provisioning (if separate from repo access) to be confirmed.

**BayOne commitment.** Work through the page and extract the code pointers, API documentation URLs, and recording timestamps that map to the POC screens.

**Known inputs.** Confluence page — specific URL on the meeting invite.

---

### A7. Code pointer email from Akhil

**What it is.** Akhil committed to emailing Colin with specific repository links and code navigation pointers supplementing the Confluence page.

**Source.** 2026-04-06 walkthrough. Set 07 action item 2.

**Cisco commitment.** Akhil.

**BayOne commitment.** Use the email pointers to accelerate the code deep dive in item B1 below.

---

## B. Code Deep Dive and Planning

### B1. Code deep dive and UI mapping for the POC screens

**What it is.** Reading the EPNM code for the Inventory screens (Assembly repo, ChassisView repo, PI framework) and Fault Management (EPA wireless repo and related), and reading the EMS code for the equivalent screens (EMS UI, Common UI, Infra UI). Building an internal map of the application relevant to the two POC functional areas. Identifying Dojo primitives in use, data flow, API call sites, widget composition, and the equivalent EMS REST endpoints.

**Source.** 2026-04-06 walkthrough. Set 07 action item 9. Colin's methodology pattern in Set 02 and Set 03 ("We go and have exploration happen. We build our own kind of map of the application").

**Cisco commitment.** None directly — this is BayOne reading the code.

**BayOne commitment.** Agent-driven exploration. Build the internal application map. Surface questions only when the code does not answer them or when things contradict.

**Known inputs.** Confluence page materials, email code pointers, research library (Set 08 legacy stack and conversion patterns), access to both repositories (once provisioned).

---

### B2. Code organization proposal

**What it is.** A proposal from Colin to the Cisco team on where the classic UI code lives: a subfolder inside the EMS UI repository or a new dedicated repository. Akhil deferred this decision and asked Colin to propose an approach.

**Source.** 2026-04-06 walkthrough. Set 07 action item 10.

**Cisco commitment.** Akhil reviews the proposal and the Cisco team (Selva, Akhil) signs off.

**BayOne commitment.** Colin writes the proposal. Must satisfy the firm constraint that the code builds as part of the EMS build.

**Known inputs.** Proposed folder structure in `06_conversion_patterns_reference.md` Section 8. EMS UI repository layout.

---

### B3. Regression test suite identification

**What it is.** The Cisco engineering team identifies which of their existing regression test suites are applicable to the Inventory and Fault Management POC scope areas. Seven categories of tests exist (functional, scale, end-to-end, UI, API, migration, upgrade), thousands of cases across devices and configurations.

**Source.** 2026-04-06 walkthrough. Set 07 action item 12.

**Cisco commitment.** The engineering team identifies suites. Specific owner not named but Praveen and Ramesh are the most engaged on testing topics.

**BayOne commitment.** Colin asked for access to the existing test suites, the expected run-through, and pointers to what "done" looks like for each area. Use whatever is shared to understand the functional coverage the classic UI must preserve.

---

### B4. Share NX-OS CI/CD testing approach (with Srinivas's permission)

**What it is.** Colin committed to ask Srinivas Pita (NX-OS CI/CD) for permission to share that engagement's testing approach with the EPNM-EMS team as a reference for what BayOne's agentic testing model looks like in practice.

**Source.** 2026-04-06 walkthrough. Set 07 action item 11.

**Cisco commitment.** Srinivas grants or declines permission.

**BayOne commitment.** Colin makes the ask. If permission is granted, the approach is shared with the Cisco EMS team.

---

## C. Classic View Construction — Inventory (POC Part 1)

### C1. Classic view for Network Devices

**What it is.** Angular rebuild of the EPNM Network Devices screen in classic style, wired to the EMS inventory REST APIs. Includes the device list table with left-side filter panel, the multi-step device-add wizard, bulk CSV import, table state operations (set to admin / maintain / manage, schedule maintain / managed, disable handler inventory), and additional toolbar actions (export, new box certificate, OEM commands).

**Source.** 2026-04-06 walkthrough. Selva's delineation: "whatever we covered earlier is part one of the POC, like the inventory device."

**Cisco commitment.** Tech lead availability (Akhil primarily) for questions about layout, fields, filter behavior, and data sources that are not resolvable from the code.

**BayOne commitment.** Apply the per-screen migration checklist from `06_conversion_patterns_reference.md` Section 9.

**Known open items.** Exact device-add wizard field-by-step breakdown. Bulk-import CSV schema (columns, validations). State-management scheduling UI (time picker, scheduling controls). Additional toolbar actions beyond what was demonstrated.

---

### C2. Classic view for Device Details

**What it is.** Angular rebuild of the Device Details screen in classic style: Chassis View on the left, main content area with a left-side menu (system summary, device details, chassis and enrollment, and additional items not fully enumerated). Shows both physical and logical device aspects.

**Source.** 2026-04-06 walkthrough.

**Cisco commitment.** Akhil and Ramkrishna for detail questions about left-menu enumeration, physical-versus-logical rendering choices, and API data mapping.

**BayOne commitment.** Apply the per-screen migration checklist. Coordinate with the Chassis View work item (C3) since they share a screen.

**Known open items.** Complete left-menu enumeration.

---

### C3. Classic view for Chassis View

**What it is.** Angular rebuild of the Chassis View component — the visual representation of the physical device showing modules and ports. Rendered on the left side of Device Details.

**Source.** 2026-04-06 walkthrough.

**Cisco commitment.** Akhil for layout questions. Ramkrishna for questions about which chassis interactions exist on the EMS backend today.

**BayOne commitment.** Apply the per-screen migration checklist. Device images are now application assets in EMS (not Oracle BLOBs), so image delivery is no longer a database concern.

**Known open items.** Whether the interactive chassis view component (module-slot clicks, port state interactions, hardware hierarchy drill-down) has been fully reimplemented on the EMS side. This may fall into the approximately 10-20 percent backend gap and may surface a scope question.

---

### C4. Classic view for Device 360

**What it is.** Angular rebuild of the Device 360 popup. Tabs: Alarms, Modules, Interfaces, Location, Recent changes. Actions menu includes Device Console. Launchable from multiple places (info icon in Network Devices table, alarms, other windows).

**Source.** 2026-04-06 walkthrough.

**Cisco commitment.** Akhil for layout. Jenis for the Alarms tab specifics (cross-cuts with Fault Management).

**BayOne commitment.** Apply the per-screen migration checklist.

**Known open items.** Complete actions menu list beyond Device Console.

---

### C5. Classic view for Interface 360 (nested 360)

**What it is.** Angular rebuild of the Interface 360 popup, launched from the Interfaces tab of Device 360. A 360 view inside a 360 view. The nesting pattern must be preserved.

**Source.** 2026-04-06 walkthrough.

**Cisco commitment.** Akhil for layout questions.

**BayOne commitment.** Apply the per-screen migration checklist. Manage dialog-within-dialog behavior in Angular Material.

**Known open items.** Whether Interface 360 has the same tab structure as Device 360 or a different interface-specific layout.

---

### C6. Classic view styling and theme wiring — Inventory

**What it is.** Apply the EPNM classic theme (blue and white palette, Segoe UI font family, 2px border radius) to the Inventory screens. Wire the theme toggle on each Inventory screen (local per-screen toggle).

**Source.** 2026-04-06 walkthrough. Akhil's confirmation on default theme. 2026-03-25 scope reframe meeting for local-toggle decision.

**Cisco commitment.** None directly.

**BayOne commitment.** Use the CSS custom properties pattern and `ThemeService` from `06_conversion_patterns_reference.md` Section 6. Default state is classic; toggle flips to Magnetic.

---

## D. Classic View Construction — Fault Management (POC Part 2)

### D1. Classic view for Alarms table

**What it is.** Angular rebuild of the Alarms table reached via Monitor → Alarms and Events. Includes the table with column picker, quick filter and advanced filter, expandable rows with general information detail, correlated alarms visualization, clear-alarm action, and the other actions described as "similar to Network Devices."

**Source.** 2026-04-06 walkthrough.

**Cisco commitment.** Jenis for Fault Management specifics. Akhil for the table component pattern (same as Network Devices).

**BayOne commitment.** Apply the per-screen migration checklist.

**Known open items.** Exact column set. Advanced filter criteria, operators, and saved filter capabilities. Severity-based row coloring. Full action set beyond clear-alarm (acknowledge, annotate, assign, suppress, create trouble ticket). Real-time update mechanism for new alarms.

---

### D2. Classic view for correlated alarms

**What it is.** The correlated alarms visualization: multiple related alarms grouped under a root cause. Viewable from at least two places — the alarms table itself and within the Device 360 alarms tab.

**Source.** 2026-04-06 walkthrough. Jenis explicitly: "Correlated alarms. I think that we showed the 360 view."

**Cisco commitment.** Jenis for specifics.

**BayOne commitment.** Decide on the visual rendering (tree hierarchy, grouped rows, correlation panel) — the walkthrough did not describe it. Flag to Jenis if the code does not make the intended rendering clear.

**Known open items.** Visual representation pattern. How correlation relationships are expressed on the API response.

---

### D3. Classic view for Events interface

**What it is.** The multi-layered events interface: most-recent-events popup accessible from the alarms screen, time-based filtering (past 8 hours default, all events, other presets), and a full events page as a secondary table.

**Source.** 2026-04-06 walkthrough.

**Cisco commitment.** Jenis for specifics.

**BayOne commitment.** Apply the per-screen migration checklist.

**Known open items.** Full preset list and custom range support. Relationship between the popup and the full events page (same data with different filters or different data sources). Cross-navigation between alarms, events, and syslogs views.

---

### D4. Classic view for Syslogs

**What it is.** Angular rebuild of the syslogs view — a third data type within fault management, alongside alarms and events. No UI detail was provided in the walkthrough.

**Source.** 2026-04-06 walkthrough (mention only).

**Cisco commitment.** Jenis for specifics if the code does not make the intended layout clear.

**BayOne commitment.** Apply the per-screen migration checklist. The execution session will need to examine the EPNM code directly to understand the intended UI.

**Known open items.** UI layout, filtering behavior, relationship to alarms and events views.

---

### D5. Classic view styling and theme wiring — Fault Management

**What it is.** Apply the EPNM classic theme to the Fault Management screens. Wire the local toggle on each screen.

**Source.** 2026-04-06 walkthrough. 2026-03-25 scope reframe meeting.

**Cisco commitment.** None directly.

**BayOne commitment.** Consistent with item C6. The same `ThemeService` and palette applies.

---

## E. Backend Gap Handling

### E1. Gap analysis for POC-scoped screens

**What it is.** Identification of backend features in EPNM that do not have EMS equivalents within the scope of the Inventory and Fault Management screens. For each gap, classify as narrow (API-level touchup) or broad (needs new EMS backend work).

**Source.** 2026-04-06 walkthrough. Colin's commitment: "There will be a gap analysis. So we'll look for, you know, if there's anything critical that's missing and then those things that maybe, you know, that 10% that's remaining that might not be migrated or might not be compatibly migrated, we'll be able to flag that."

**Cisco commitment.** Selva receives the flags and decides on treatment per Praveen's guidance ("We need to consider adding equivalent functionality in the new product rather than just bringing over the whole old thing").

**BayOne commitment.** Surface findings as the code deep dive (item B1) and the per-screen work items (C and D) progress. Classify and flag.

**Known inputs.** The Set 08 research "API response gaps to watch for" table in `06_conversion_patterns_reference.md` Section 7 (device count in filter panel, alarm summary on device endpoint, export endpoint, bulk-import endpoint, OEM commands, scheduling).

---

### E2. Narrow API touchup execution (if any)

**What it is.** Any narrow API-level backend change identified in E1 and approved by Selva. Examples: adding a filter parameter, widening or narrowing a query scope, adjusting a response field.

**Source.** Selva's explicit allowance: "There may be slight touchup to the backend to do that filtering. That's the kind of thing we expect."

**Cisco commitment.** Selva approves specific changes. Cisco engineering team reviews any PRs against backend repos.

**BayOne commitment.** Keep changes truly narrow. Any regression in the backend affects both views simultaneously because of the critical release path.

---

## F. Verification and Testing

### F1. Functional equivalence verification via Playwright agents

**What it is.** Playwright-driven user-persona agents exercise the classic view against the new EMS view and verify actions produce identical results, because both hit the same backend.

**Source.** 2026-04-06 walkthrough. Colin's approach: "user persona, train an agent to go and know the old interface and then say, try this on the new interface, make sure that everything is matching." Guhan's acceptance test: "Final test will be to show the same thing comes up everywhere."

**Cisco commitment.** Endorses the approach. Selva: "That would be great too."

**BayOne commitment.** Build the Playwright agent suite. Visibility to Cisco during the POC is scoped (full dashboard visibility is deferred to the full engagement).

---

### F2. Internal unit testing

**What it is.** BayOne-internal unit tests covering the classic view components. Colin's explicit commitment: unit tests will be in place before declaring the POC complete.

**Source.** 2026-04-06 walkthrough. Colin: "If there's, let's say, for instance, unit tests that are missing, that will be even internally to us before I come back to you and say, OK, we're done with the POC."

**Cisco commitment.** None directly.

**BayOne commitment.** Unit test coverage for the classic view components.

---

## G. Closeout

### G1. POC demonstration

**What it is.** Demonstrate the classic view toggle working on the two functional areas. Walk through the acceptance test flow: perform the same action in both views, confirm identical results.

**Source.** Guhan (Set 01 through Set 03): the POC is fundamentally about a "working demo." "Can you take that experiment, provide a working code, show us the demo."

**Cisco commitment.** Review the demonstration. Make the call on whether the POC has satisfied the acceptance criteria in `03_objectives_and_scope.md` Section 7.

**BayOne commitment.** Colin delivers the demonstration. Code is production-quality (per Selva's "product of product" framing).

---

### G2. POC documentation and pattern capture

**What it is.** Document the conversion patterns as executed, flagged gaps, and the pattern library that will scale post-POC. This is the "foundation" Colin described as the basis for the exponential decay on subsequent screens.

**Source.** Colin's exponential decay / parallelizable workflow framing in Set 03. Implicit in the premise of a POC that validates a scaling approach.

**Cisco commitment.** Receive the documentation.

**BayOne commitment.** Produce the documentation. The execution session should treat this as a first-class deliverable, not an afterthought.

---

## H. Not in POC Scope (Deferred to Full Engagement)

Listed for clarity. The execution session does not work these during the POC. They are not on this work-item list for execution but are named here so nothing on the list is mistaken for something that should be deferred.

- Full agentic QA with Playwright agents and dashboard visibility.
- Coverage gap analysis against Cisco's existing test suites.
- Creation of replica test cases for the Angular classic UI.
- Full integration with Cisco's seven-category test infrastructure.
- Data-driven test creation across the full device configuration matrix.
- Customer-specific profile testing.
- Scale testing for the classic UI.
- Migration and upgrade testing for the toggle feature itself.
- Global toggle at the product level (user-settings preference).
- UX team involvement (they bless the final design in the product phase).
- Screens beyond Inventory and Fault Management.

---

## Closing Note

This list intentionally stops at the granularity the transcripts established. The execution session will decompose each item into concrete implementation steps on arrival, using the technical references in `06_conversion_patterns_reference.md` and the Set 08 research files. The decomposition is the execution session's judgment call; the items themselves are the scope Cisco and BayOne have set.
