# 03 — Objectives and Scope

**Purpose of this document:** The exact POC scope as established by the Cisco engineering team. What is in, what is out, what defines done. No extrapolation. If a detail is not confirmed in the transcripts, it is flagged as open rather than invented.

---

## 1. Objective Stated in One Sentence

Rebuild the EPNM classic UI for two specific functional areas (Inventory and Fault Management) in Angular, inside the EMS build, behind a local per-screen toggle that defaults to the classic view on login and flips to the existing EMS UX when toggled, with every screen reading from and writing to the existing EMS backend unchanged.

---

## 2. The Two Screens

### 2.1 Inventory (POC Part 1)

The Inventory target spans four distinct UI surfaces, confirmed by Akhil in the 2026-04-06 walkthrough:

#### Network Devices
- A list / table view of devices.
- Reachable from: left navigation → Inventory → Network Devices. Also reachable from Device Management → Network Devices.
- Left filter panel with filter categories: All devices (default), filter by device type, filter by locations, filter by group and sites.
- Device-add workflow: multi-step wizard requiring IP address, protocol credentials (SNMP, Telnet, HTTP, HTTPS, and others). The exact wizard step count and field-by-step breakdown was not fully enumerated in the walkthrough and is an open item.
- Bulk import: download a sample CSV template, populate it, upload the CSV.
- Basic table operations: edit, delete.
- Device state operations: set to admin state, set to maintain state, set to manage state, schedule maintain state, schedule managed state, disable handler inventory.
- Additional toolbar actions: export device, new box certificate, OEM commands.

#### Device Details
- Reached by clicking the device name (rendered as a hyperlink) in the Network Devices table.
- Layout: left panel shows the Chassis View (visual of the physical device). Main content area shows a view selected from a left-side menu.
- Left-menu views observed in the walkthrough: system summary view, device details, chassis and enrollment, and other items that were not fully enumerated. Full enumeration is an open item.
- Content covers both the physical device (hardware modules, chassis layout, ports) and logical configurations (routing and other software-defined configurations). Ramkrishna described this as "the physical aspects of the device and also the configurations such as the routing and other logical configurations on the device."

#### Chassis View
- Rendered on the left side of the Device Details screen.
- Visual representation of the physical device showing modules and ports.
- Device images in EMS are application assets, not Oracle BLOBs as in EPNM: "For the new UI, it is part of the application, not stored in Oracle and all."
- Whether the chassis view interactive component (module slot state, port state interactions, hardware hierarchy clicks) has been fully reimplemented on the EMS side was not confirmed during the walkthrough. This is an open item and may fall into the approximately 10-20 percent backend gap.

#### Device 360
- A popup / overlay view of a single device's context.
- Launched via an info icon in the Network Devices table. Also launchable from other screens: alarms, other 360-style windows.
- Tabs: Alarms (associated alarms for the device), Modules (hardware modules / components), Interfaces (clicking an interface launches a nested Interface 360), Location, Recent changes.
- Actions menu includes Device console and others (full list not captured).
- An alarms popup is accessible from Device 360.

#### Interface 360 (nested)
- Launched from the Interfaces tab inside Device 360.
- A second-level 360 view inside a 360 view. This nesting pattern must be reproduced in the Angular rebuild.
- Whether Interface 360 has the same tab structure as Device 360 or a different interface-specific layout was not enumerated.

### 2.2 Fault Management (POC Part 2)

Selva drew the delineation in the walkthrough: "Just to put some delineation, Colin, whatever we covered earlier is part one of the POC, like the inventory device, like that's target for the POC. This is part two, and this is a different area."

#### Alarms Table
- Navigation: Monitor → Alarms and Events.
- Same table component pattern as Network Devices. The common table pattern is part of the Common UI repository in EMS.
- Columns: not enumerated in the walkthrough. Column picker is present on the right side. Full column set is an open item.
- Quick filter: text-based search across visible columns. Typed into an input at the top of the table.
- Advanced filter: structured multi-criteria filtering. Exact criteria, operators, date / time range selection, and saved filter capabilities were not fully described.
- Table actions: clear alarms (confirmed by Jenis — a write operation against the alarm backend, not just display). Other actions described as "similar to the network devices" (edit, delete, bulk operations, export, state management).
- Expandable rows: every row can be expanded inline to reveal additional detail. Expanded content includes "general information" and other detail fields. Exact fields and lazy-loading behavior are open items.
- Correlated alarms: multiple related alarms grouped under a root cause. Jenis: "Correlated alarms. I think that we showed the 360 view." Viewable from at least two places: the alarms table itself and within the Device 360 alarms tab. Visual representation (tree, grouped rows, correlation panel) was not described.

#### Events
Akhil described a multi-layered events interface:
- A "most recent events" popup accessible from the alarms screen.
- Time-based presets including "past 8 hours" and "all events." Full preset list and custom range support are open items.
- An events page as a secondary full-page table, separate from the alarms table.
- The relationship between the popup and the full page (same data with different filters versus different data sources) was not explicitly discussed.

#### Syslogs
- A third fault-management data type alongside alarms and events.
- No specific UI layout, filter behavior, or relationship-to-alarms details were provided in the walkthrough. This is genuinely under-documented and will require the execution session to examine the EPNM code directly.

#### Cross-navigation
How users move between alarms, events, and syslogs views (tabs, separate left-nav entries, contextual links) was not captured in the walkthrough.

#### Real-time update mechanism
How the alarms table refreshes when new alarms arrive (auto-refresh, polling, server-sent events, push) was not discussed.

---

## 3. What the Classic View Must Look Like

Akhil confirmed the visual target: the classic view must reproduce the EPNM look and feel. EPNM's theme is blue and white. The classic view's default state on login is the EPNM theme — left menu, page layout, colors, typography all rendering like the legacy Dojo-based EPNM. When the user toggles to the new UX, the page flips to the Magnetic design system (the current EMS visual language).

Customer perception is the success bar: a customer using the classic view should recognize it as the EPNM experience they know. Colin's commitment: "So really we'll keep it exactly, visually speaking, and UX speaking identical to this EPNM use case."

---

## 4. What the Toggle Must Do

- Local per screen. Each of the screens in scope gets its own embedded toggle control. There is no global user-settings toggle in the POC.
- Default on login is the classic view. Toggle flips to the new UX. Toggling back returns to the classic view.
- The toggle changes the visual presentation only. Both views call the same EMS backend APIs and should produce identical functional results.
- The global toggle — a user preference that changes the entire application experience at once — is explicitly deferred to the product phase. Selva: "When we finally do the product, we may do it somewhere globally in the user setting or somewhere where they say, and then the whole experience is going to be classic. So that we'll worry about later."

How the toggle state is managed (per-browser-session, per-user persisted, URL parameter) was not specified in the walkthrough. This is an open item for the execution session to decide or raise.

---

## 5. What the Backend Integration Must Do

The classic UI calls the existing EMS backend. No backend reimplementation. Guhan was emphatic: "We are not trying to reboot the backend from older, right? That's not something what we want him to do." Praveen confirmed: "We don't want this old backend to be brought over... when we bring over this classic look, you want that UI to talk to the new backend that exists on the next generation."

### The narrow exception

Selva described the one acceptable backend change: "In the older UI, we might have given him ability to look at things with a different lens. And we sometimes may or may not have that... this means that there may be slight touchup to the backend to do that filtering." This is API-level: add a filter parameter, widen or narrow a query scope, adjust a response field. Anything larger is out of scope.

### The server-side risk to be aware of

Selva flagged the critical release path: "Any changes to the current server, because the current server is also getting updated. With no changes to the backend preferably, because any service change we have — we are in the critical release path, which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way." Any backend touchup must be done with extra care because a regression could break both views simultaneously.

### The 80 percent backend coverage and the gap

Ramkrishna stated that approximately 80 percent of EPNM backend functionality has been reimplemented in EMS. The remaining approximately 10-20 percent is a gap to be analyzed. Colin committed: "There will be a gap analysis. So we'll look for, you know, if there's anything critical that's missing and then those things that maybe, you know, that 10% that's remaining that might not be migrated or might not be compatibly migrated, we'll be able to flag that."

For the POC specifically, gap analysis applies only to the screens in scope. For Inventory and Fault Management, what has and has not been reimplemented on the EMS side must be identified. Items that are missing on the EMS backend but needed for POC functional equivalence fall into one of two paths:
- If the gap is narrow (API shape differences, missing filter parameter), the narrow API touchup exception applies.
- If the gap is broader (entire backend capability missing), Praveen's guidance applies: "We need to consider adding equivalent functionality in the new [product] rather than just bringing over the whole old thing. That's too bulky to bring here and that's not the approach we're taking." Flag to Selva rather than proceed.

---

## 6. Where the Classic UI Code Lives

Undecided. Akhil offered two options: "I mentioned about this particular EMS UI, UI is our repository, right? Maybe you can create a folder and for now you can add it out there, or you can create a separate repository also. It's up to you all. You can think about it and come up with your plan, then we can review it."

The constraint is firm: "It has to be part of the new EMS build." Wherever the classic UI code lives, it must build as part of EMS and must support toggling into and out of the existing EMS UX.

Colin owes a proposal on this decision. Action item 10 in the Set 07 action list.

---

## 7. What Defines "Done" for the POC

From the transcripts, these are the explicit completion criteria:

1. **Two screens converted.** Inventory (Network Devices, Device Details, Chassis View, Device 360, Interface 360) and Fault Management (alarms table with filtering and correlated alarms, events interface, syslogs).
2. **Toggle works on each screen.** Each of the in-scope screens has its own embedded local toggle. Default state on login is the classic view. Toggling flips to the existing EMS UX. Toggling back returns to the classic view.
3. **Classic UI code builds as part of EMS.** Whether located in a subfolder of the EMS UI repository or in a new dedicated repository, the code must integrate into the EMS build pipeline.
4. **Functional equivalence demonstrated.** The same action in both views produces the same result against the same EMS backend. Guhan: "Final test will be to show the same thing comes up everywhere." Colin stated the verification approach: Playwright-driven user-persona agents that exercise the classic view against the new view and confirm matching outcomes.
5. **Internal unit testing complete.** Colin: "If there's, let's say, for instance, unit tests that are missing, that will be even internally to us before I come back to you and say, OK, we're done with the POC."
6. **Gap analysis documented for the scoped screens.** Items in the remaining 10-20 percent backend gap that are relevant to the two screens identified and flagged.
7. **Code organization plan proposed.** Colin owes a plan on where the classic UI code should live. This should be agreed with the Cisco team before being locked in.
8. **POC-grade quality is production-grade code.** Selva: "It's going to be product of product. It's not a prototype." The classic view will ship to customers after the POC. The code must be production-ready, not sketch-quality.

---

## 8. What is Explicitly NOT in Scope for the POC

From the transcripts, the following are explicitly deferred, whether to the full engagement or to Cisco's own roadmap:

- **Backend reimplementation.** Guhan repeated twice.
- **Global toggle (user setting).** Selva: "That we'll worry about later."
- **UX team involvement.** Explicitly not part of the POC. The UX team blesses the final design in the product phase.
- **Full agentic QA with dashboard visibility for the Cisco team.** Colin deferred this explicitly to the full engagement.
- **Coverage gap analysis on Cisco's existing test suites.** Colin: "For the agentic part for the gap analysis, that probably will wait till the full engagement, just because that will take some time and that'll make the POC drag out."
- **Replica of Cisco's existing UI test cases for the Angular classic UI.** Jenis raised this; Praveen expanded the expectation; Colin confirmed the replica work will happen — but in the full engagement, not the POC.
- **Full regression suite integration.** Deferred.
- **Data-driven test case creation covering the full device configuration matrix.** Deferred.
- **Customer-specific profile testing.** Not discussed for POC scope.
- **Scale testing for the classic UI.** Not discussed for POC scope.
- **Migration and upgrade testing for the toggle feature itself.** Not discussed.
- **Screens beyond Inventory and Fault Management.** The full product surface is 200 to 250 workflow screens. Only the two listed functional areas are in the POC.

---

## 9. What the Execution Session Needs to Decide or Raise

- Exact column set for the alarms table.
- Exact left-menu enumeration for Device Details.
- Full action list for Device 360 beyond Device Console.
- Interface 360 structure (same tabs as Device 360 or different).
- Bulk-import CSV schema: required columns, optional columns, validation rules.
- State-management scheduling UI: time-picker and scheduling controls for "schedule maintain state" and "schedule managed state."
- Chassis View interactivity: whether the interactive component is part of the 80 percent reimplemented on EMS or part of the gap.
- Which operations bypass the database and query devices directly (the "in most cases" exception Ramkrishna mentioned).
- Syslog UI layout and filtering behavior.
- Advanced filter structure for the alarms table.
- Severity-based row coloring in the alarms table.
- Cross-navigation patterns between alarms, events, and syslogs.
- Real-time update mechanism for alarms.
- Time-based filtering granularity on events (full preset list, custom ranges, calendar picker).
- Expandable row content: exact fields, layout, data source, lazy loading behavior.
- Relationship between the "most recent events" popup and the full events page (same data with different filters, or different data sources).
- Severity handling, acknowledgement workflow, annotation, assignment, suppression, trouble-ticket creation — the full action set on alarms beyond "clear alarms."

These items are captured in more complete form in `10_open_questions_and_risks.md`.
