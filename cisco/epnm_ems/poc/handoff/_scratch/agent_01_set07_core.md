# Agent 01 Extraction: Set 07 Core Material

Source documents (all from the April 6, 2026 technical walkthrough meeting):

1. 07_meeting_architecture_and_repositories_2026-04-06.md
2. 07_meeting_product_walkthrough_inventory_2026-04-06.md
3. 07_meeting_product_walkthrough_faults_2026-04-06.md
4. 07_meeting_ai_compliance_and_tooling_2026-04-06.md

---

## 1. Architecture Overview

### 1.1 Two-Product Landscape

Two products are in scope for understanding the engagement context [from 07_meeting_architecture_and_repositories]:

- **EPNM (Evolved Programmable Network Manager):** the legacy / current product. Built on a Dojo-based frontend framework with an Oracle database backend.
- **EMS (Element Management System):** the next-generation product, part of **CNC (Crosswork Network Controller)**. Built on Angular with a PostgreSQL backend.

Pradeep framed the overall relationship: "There is a data model where the data is abstracted. And then the various applications, when I say applications within the product, you will have an inventory component, there will be a topology component, there will be a fault component, so on and so forth, service level component. All of them will consume that data from the database."

The team clarified that EPNM was not directly migrated to EMS: "It's not exactly migrated in a way. Things got reimplemented. Some of it, at least 80% of it, is there in the other product, as in the newer product."

### 1.2 EPNM Architecture (Legacy)

- Frontend framework: **Dojo (legacy version)** [from 07_meeting_architecture_and_repositories; 07_meeting_product_walkthrough_inventory]
- Theming: blue and white
- Likely MVC pattern (Colin's assumption, not confirmed by Cisco): "If this is MVC architecture, I'm assuming for the old application, because it was on Dojo, we'll get that mapped out."
- Database: Oracle
- Data collection from devices via SNMP and CLI (CLI was rendered as "ECLI" in transcript but is CLI)
- Device images: historically stored in Oracle (the old pattern)

### 1.3 EMS Architecture (New Generation)

Frontend stack [from 07_meeting_architecture_and_repositories; 07_meeting_product_walkthrough_inventory]:

- Framework: **Angular 21** (latest). "Crosswork UI is pretty much on Angular stack, latest Angular 21 is used here."
- Design system: **Harbor and Magnetic design system** ("a design system called Harbor and Magnetic design system you're using").
- Branding: Crosswork UI design language.

Backend stack:

- Database: **PostgreSQL**. "There's Postgres in the new product. We've gotten rid of Oracle dependency."
- Primary framework: **Spring Boot** ("Mostly Spring Boot, yes").
- Additional services: Go services in certain areas. Pradeep: "There are areas, at least on the device management side, and there are Go services running at the back end."
- API layer: REST APIs serve the Angular frontend.
- Device images: stored in the application itself, not in the database. "For the new UI, it is part of the application, not stored in Oracle and all."

### 1.4 Shell App Layering (EMS)

The EMS frontend follows a three-layer shell-app model [from 07_meeting_architecture_and_repositories]:

1. **Infra UI (Shell App)** — outermost layer. Provides application shell, header bar, top navigation menu, and infrastructure-level UI components (login, layout frame).
2. **Common UI** — middle layer. Shared / reusable component library (cards, tables, common widgets, shared design patterns from Harbor / Magnetic).
3. **EMS UI** — innermost layer. Feature-specific pages (software image management, inventory views, fault management views, device management, etc.).

Akhil: "EMS is kind of like built on top of shell app. So when I say shell app means this header and the top menu and other infrastructure UI components is coming from Infra UI repository."

Akhil also indicated that the classic UI should follow this layered pattern: "We also use the underlying Crosswork Common UI, right, and that pattern should be picked up from the existing port."

### 1.5 Data Flow Pattern (Both Products)

The data flow pattern is the same in both products; only the database differs [from 07_meeting_architecture_and_repositories; 07_meeting_product_walkthrough_inventory]:

Network Devices -> (SNMP, CLI polling) -> Data Collection and Parsing Layer -> (abstracted data model) -> Oracle Database (EPNM) or PostgreSQL (EMS) -> Application components (Inventory, Topology, Fault, Service Level, Performance Monitoring, Software Image Management) -> UI Rendering (Dojo in EPNM, Angular in EMS).

Srama explained the steps in the inventory demo: "After you add a device, you give the credentials. You tell how to collect this information by using SNMP, [and] CLI. You can [configure] those credentials aspect. So the information is collected, parsed, and there is a data model where the data is abstracted."

On read direction, Colin asked whether the application reads from devices or from the database. The answer: "In most of the cases, it won't directly go to the [device]. It reads from the database, correct." The qualifier "in most of the cases" implies that some operations may query devices directly.

---

## 2. Repository Inventory — EPNM

All entries from 07_meeting_architecture_and_repositories unless otherwise noted. Akhil walked through this structure.

### 2.1 PI Framework Repository
- Role: core UI framework for EPNM, written in Dojo.
- Contents: "the prime UI and the framework UI, Dojo based."
- Described as the foundational framework layer.

### 2.2 Wireless Framework Repository (Wireless Repos)
- Role: contains wireless-specific UI and framework code.
- Referenced alongside PI Framework as part of the EPNM frontend stack.

### 2.3 Assembly Repository
- Role: contains inventory-related UI screens.
- Akhil: "Inventory screens are part of the assembly repo"; "Assembly is on the UI side."
- The faults walkthrough confirmed that fault management UI code also lives in the assembly repo: "the fault is on the backend... it's backend and frontend, and assembly is on the UI side" [from 07_meeting_product_walkthrough_faults].
- Additional unnamed repos also contain inventory-related items.

### 2.4 ChassisView Repository
- Role: contains the chassis visualization component.
- Akhil: "ChassisView is coming from the ChassisView repo."
- Renders the physical device images and chassis layout seen in the device details screen.

### 2.5 Fault Management Repositories
- Referenced as "fault management EPA wireless repo" and "fault" (EPA is likely EPNM Assurance).
- Akhil indicated fault management spans both backend and frontend: "The fault is on the backend... it's backend and frontend, and assembly is on the UI side."
- Janice appears to own the fault management backend ("Janice's backend") [from 07_meeting_product_walkthrough_faults].
- A reference to "EPA wireless repo" suggests some fault management logic may exist in a wireless-specific repository.

### 2.6 Complete Repository List
- Akhil referenced an external link containing the complete EPNM repository list: "You can find out your complete repository list in this link also." The link was shared in meeting materials / chat but is not captured in the transcript text.

---

## 3. Repository Inventory — EMS

### 3.1 Infra UI Repository (Shell App)
- Role: shell application, top-level container.
- Contents: "This header and the top menu and other infrastructure UI components is coming from Infra UI repository."
- Provides: header bar, top navigation menu, infrastructure-level UI (login, layout frame).

### 3.2 Common UI Repository (Shared Components)
- Role: shared / reusable UI components consumed across EMS.
- Akhil: "If you look at this card, right? These cards and the tables and these things are called common components. So this common component is part of this common UI."
- Contents: card components, table components, common UI widgets, shared design patterns from Harbor / Magnetic.

### 3.3 EMS UI Repository (Feature Pages)
- Role: feature-specific EMS pages.
- Akhil: "All these EMS related pages like Praveen mentioned about software image management and other things, other pages is part of this repo."
- Contents: software image management, inventory views, fault management views, device management pages, all EMS-specific feature screens.

### 3.4 Backend Repositories
- Corresponding backend repositories exist alongside the frontend repos.
- Akhil: "Back-end party, yeah, this is a corresponding... Postgres... backend."
- The backend repo names were not explicitly stated in the transcript.
- **EMS Assurance** is referenced as the EMS-side fault / alarm / event backend ("EMS assurance is also back inside") [from 07_meeting_product_walkthrough_faults].

---

## 4. Inventory Screens Walkthrough

All material in this section is from 07_meeting_product_walkthrough_inventory. Walkthrough was primarily led by Akhil, with contributions from Srama and Praveen.

### 4.1 POC Inventory Scope Modules

Akhil enumerated the modules in scope for POC Part 1:

1. Network Devices (list / table view)
2. Device Details (detailed view of a single device)
3. Interface 360 (popup / overlay view with device alarms, modules, interfaces)
4. Fault Management (POC Part 2, covered separately)

"These are the scope of the modules which we identified. One is the network devices and device details and interface 360 and then fault management."

### 4.2 Network Devices Screen

**Navigation / entry:**
- Dashboard is the landing screen after login.
- Path: Left navigation -> Inventory -> Network Devices.
- Also accessible via Device Management -> Network Devices. Akhil: "So you can see there is already a device management network devices also."

**Filtering panel (left side):**
- "Right now it is filtered by all devices. You can filter by device type and locations."
- Filter options observed: All devices (default), Filter by device type, Filter by locations, Filter by group and sites.

**Device add workflow:**
- Multi-step wizard ("step forward").
- Single device add requires: IP address, protocol credentials (SNMP, Telnet, HTTP, HTTPS, "et cetera").
- Akhil: "Here you can add a device. Once you click on add a device, you have to enter the IP address and other details. So there is a step forward here. SNMP, Telnet, HTTP, HTTPS, et cetera."

**Bulk import:**
- Download a sample CSV template, populate it with device details, upload the CSV.
- Akhil: "Also, there is a bulk import. You can download the sample CSV and then also you can add the details and have a bulk import also."

**Table functionality:**
- Basic operations: "edit, delete, and all these are supported."

**Device state management operations:**
- Set to admin state
- Set to maintain state
- Set to manage state
- Schedule maintain state (time-based scheduling)
- Schedule managed state (time-based scheduling)
- Disable handler inventory

Akhil: "Then we have admin state set to maintain state. Also, we have a set to manage state. Schedule the [maintain] state, schedule managed state, disable the handler inventory."

**Additional toolbar actions:**
- Export device (export device data)
- New box certificate (certificate management)
- OEM commands (vendor-specific command execution)

### 4.3 Device 360

- Launched via info icon in network devices table; also launchable from multiple other places (alarms view, other windows).
- Akhil: "It can be launched from different places like alarms here other different windows we can open it."

**Tabs / sections inside Device 360:**
- Alarms (associated alarms for the device)
- Modules (hardware modules / components)
- Interfaces (clicking an interface launches a nested Interface 360 view)
- Location (physical location information)
- Recent changes (change history)

**Nested Interface 360 pattern:**
- "From interface you can [open], again it will launch one more 360 view."
- This second-level popup (360 inside 360) must be replicated in the Angular rewrite.

**Device 360 actions menu:**
- Device console (direct console access)
- Multiple other actions ("different different actions")

**Alarms popup from Device 360:**
- "Again if you see alarms there is a different pop-up also here."

### 4.4 Device Details

- Accessed by clicking the device name (rendered as a hyperlink) in the network devices table.
- Akhil: "You can click on this device name type is a hyperlink once you click here the left hand side you will see that chassis view."

**Layout:**
- Left panel: Chassis view (visual of the physical device).
- Main content area: multiple views from a left menu.

**Left-menu views observed (Srama):**
- System summary view
- Device details
- Chassis and enrollment
- Other left-menu items (not fully enumerated)

**What Device Details represents (Srama):**
- "Basically, all this is information we collect from an individual network device. After you add a device, you give the credentials. You tell how to collect this information by using SNMP, [and] CLI. You can [configure] those credentials aspect. So the information is collected, parsed, and there is a data model where the data is abstracted."
- Shows both physical and logical aspects: "What you see here is the physical aspects of the device and also the configurations such as the routing and other logical configurations on the device."
- Physical aspects: hardware components, chassis layout, modules, ports.
- Logical aspects: routing configurations, other software-defined configurations.

### 4.5 Chassis View

- Rendered on the left side of Device Details.
- Visual representation of the physical device hardware showing modules and ports.
- Device images in EMS are application assets, not database BLOBs. Team: "For the new UI, it is part of the application, not stored in Oracle and all."
- Whether the chassis view interactive component (module slots, port states, hardware hierarchy interactions) has been fully reimplemented in EMS was not confirmed (flagged as open).

### 4.6 Toggle Defaults and Theme Behavior for Inventory

- Default state after login: classic EPNM look and feel (blue / white, legacy layout).
- After toggling: Magnetic design system (current EMS visual language).
- Toggle switches the entire visual experience, not individual components.
- Akhil: "The default, once I log into the Crosswork UI, the default will be showing the EPNM theme. Basically the left menu and the other area should be [the EPNM] current [look and] feel should be shown instead of Magnetic."

---

## 5. Faults Screens Walkthrough

All material in this section is from 07_meeting_product_walkthrough_faults. Walkthrough led by Akhil with contributions from Janice (fault management domain), Praveen, and Ramesh.

### 5.1 Navigation

- EPNM path: **Monitor -> Alarms and Events**.
- Akhil: "From monitor, you can go to the alarms and events. This is fault management."

### 5.2 Alarms Table

- Same table component pattern as the network devices table: "So you can see the alarms here. And it's on the table actions similar to the network devices."
- The common table pattern is part of the Common UI repository.

**Table actions:**
- "Clear alarms" confirmed by Janice. This is a write operation against the alarm management backend, not just display.
- Other actions described as "similar to the network devices" (edit, delete, bulk operations, export, state management).

**Column behavior:**
- Column configuration / picker is present on the right side.
- Akhil: "And there are different columns here in the right hand side also."
- Exact column set was not enumerated in the walkthrough.

### 5.3 Correlated Alarms

- Janice: "Correlated alarms. I think that we showed the 360 view."
- Alarms can be correlated: multiple related alarms grouped under a root cause.
- Correlated alarms are viewable from at least two places: the alarms table itself (via correlation relationships shown in the grid) and within the Device 360 alarms tab.

### 5.4 Events

Akhil: "From here there is a different pop-up most recent events and then there is all events eight hours past eight hours then there is an events page a secondary table."

This describes a multi-layered events interface:

1. **Most recent events pop-up** — accessible from the alarms screen; a quick-access pop-up (modal or panel).
2. **Time-based filtering** — at least one preset: "past eight hours." An "all events" option exists.
3. **Events page (secondary table)** — a full-page events table separate from the alarms table.

### 5.5 Syslogs

- Akhil: "And then we have syslogs."
- Syslogs are a third data type within fault management, alongside alarms and events.
- No additional detail on syslog UI layout was provided in the transcript.

### 5.6 Filtering

Akhil: "All the table we have a quick filter and advance filter."

- **Quick filter:** text-based search across visible columns; typed into a text input at the top of the table.
- **Advanced filter:** structured, multi-criteria filtering with column-specific criteria, logical operators, date / time range selection, saved filter presets, and compound conditions.
- **Events time-based presets** are a separate control from quick / advanced filter (e.g., "past 8 hours," "all events").

### 5.7 Expandable Rows

- Akhil: "And also there is expandable in the [table] every row has expandable data as information, general information, things like that." (transcript originally rendered this as "PC every day row", paraphrased here).
- Every row can be expanded inline to reveal additional detail.
- Expanded content includes general information and other detail fields.

### 5.8 Faults Toggle Behavior

- Default state after login: Monitor -> Alarms and Events screens render with EPNM classic look and feel (blue / white, Dojo-style table components).
- Toggled state: same screens rendered with Magnetic design system.
- Both states connect to the same EMS backend (assurance module). Only the presentation layer changes.

---

## 6. Backend Status

[Primarily from 07_meeting_architecture_and_repositories and 07_meeting_product_walkthrough_inventory]

### 6.1 Reimplementation, Not Migration

- "It's not exactly migrated in a way. Things got reimplemented. Some of it, at least 80% of it, is there in the other product, as in the newer product."
- The backend was rebuilt for EMS rather than ported from EPNM.

### 6.2 The 80% Figure

- Cisco team stated "at least 80%" of EPNM backend functionality has been reimplemented in EMS.
- The qualifier "at least" suggests this is conservative.
- The remaining gap is approximately 10-20% (Colin referenced "10% that's remaining").

### 6.3 What the POC Must Do About the Backend

- Selva: "We don't want this old back end to be brought over... when we bring over this classic look, you want that UI to talk to the new backend that exists on the next generation."
- Praveen: "We don't want this old backend to be brought over. You're right, right? The functionalities, like when [Srama] said 80, 90% is there, and then you have [the new] product. They have an equivalent backend implemented, and that's how the new UI is talking to the [backend]. So when we bring over this classic look, you want that UI to talk to the new backend that exists on the next generation."
- Colin confirmed: "So really we'll keep it exactly, visually speaking, and UX speaking identical to this EPNM use case. But Selva, as you said, map everything to the new backend. So that's very clear for me."

### 6.4 Gap Handling

- Praveen on gap handling: "In the instance where potentially the new backend is not there, then... We need to consider adding equivalent functionality in the new [product] rather than just bringing over the whole old thing. That's too bulky to bring here and that's not the approach we're taking."
- Colin: "There will be a gap analysis. So we'll look for, you know, if there's anything critical that's missing and then those things that maybe, you know, that 10% that's remaining that might not be migrated or might not be compatibly migrated, we'll be able to flag that."

### 6.5 Database

- EMS uses PostgreSQL. Oracle has been fully eliminated: "We've gotten rid of Oracle dependency."
- The database migration is already complete in EMS. The POC does not need to migrate data or schema from Oracle to PostgreSQL.

### 6.6 Selva's EMS Functional Scope Summary

- "EMS is the terminology you would keep hearing, element management system, where you have the inventory, the fault, the performance monitoring, topology links, software image management, the underlay configurations, so on and so forth. So that functionality is what we provide in EMS and a subset of what we have in EPNM."
- Critical qualifier: EMS is "a subset of what we have in EPNM." Even with 80%+ reimplementation, EMS does not yet have full feature parity with EPNM.

### 6.7 Fault Management Backend Status

- **EMS Assurance** exists as the fault / alarm / event backend in EMS ("EMS assurance is also back inside") [from 07_meeting_product_walkthrough_faults].
- The fault management backend in EMS is part of the ~80% already reimplemented.

---

## 7. AI Compliance Rules

All material in this section is from 07_meeting_ai_compliance_and_tooling. The discussion was initiated by Selva on behalf of Ramesh.

### 7.1 Ramesh's Concerns

Ramesh asked about:
1. Tool identity (what specific AI tools are used).
2. Compliance status (are those tools Cisco-approved).
3. Architecture (local vs. cloud-based; if cloud-based, is Cisco code exposed externally).
Ramesh cited Claude Code and Cursor as examples he was familiar with.

### 7.2 Hardware and Account Rules

Colin's explicit commitments:
- All work performed on **Cisco hardware**.
- All accounts are **Cisco-issued**.
- Colin: "Every single thing we do for this will be done number one on Cisco hardware and number two with Cisco-issued accounts."

### 7.3 Approved AI Tools for This Engagement

Two tools only:

1. **Claude Code (Cisco-issued).** Cisco has procured and authorized this tool at the enterprise level; BayOne uses it through Cisco's provisioning.
   - Colin: "So for us, what that looks like from an architecture perspective is Claude Code -- we use for development. We'll use the Cisco-issued Claude Code."
2. **LangGraph (local execution).** Runs on Colin's Cisco-issued laptop. No external cloud dependency.
   - Colin: "Number two, for the actual deployment, that is LangGraph, and that is local. So that is also living and breathing on, for the moment, my Cisco-issued laptop."
   - The phrase "for the moment" signals possible future move to a Cisco server / VM, but local execution would remain the architectural property.

### 7.4 Explicit Negation of Third-Party Tools

- Colin: "We won't bring in any kind of external third-party or cloud-based tools aside from the Cisco-provided Claude Code for this."

### 7.5 Code Exposure Controls

- Selva reiterated Cisco policy: "It's part of any engagement here. We're not allowed to use Cisco code on anything that's outside of our... I mean, the approved AI tools that we get access to is the only thing that we use on our code."
- Repository access itself is controlled through Cisco internal groups. Akhil: "It is basically controlled through [Cisco] groups. So when we can get that activated... a few groups we have to enable this access. So once after that, he can seamlessly access all the repos." [from 07_meeting_architecture_and_repositories]
- Action item: Akhil or team to add Colin's Cisco ID to the appropriate groups.

### 7.6 Gatekeeper Model

- Colin: "So I'm kind of the master gatekeeper. Of course for the POC, it's just me. But even if we choose to go with the full-scale engagement, still that same gatekeeping will be there."
- Colin: "But yes, absolutely strictly Cisco-issued. And there's no way for my team to override that."

### 7.7 Transparency Commitment

- Colin: "We'll be very transparent about what we're using and how we're using it."

### 7.8 Precedent Cited

- The NX-OS CI/CD pipeline engagement with Cisco (contacts named: Srinivas Pita and Anand Singh) is the operational precedent. Colin: "We are currently active. Me and about four other people are active on a different project for Cisco. That's the NX-OS CI/CD pipeline work."
- "For that work, we already have certain things Cisco-provisioned for us."

### 7.9 DeepSeek Reference

- Colin referenced DeepSeek as part of demonstrating compliance awareness: "Even things like DeepSeek right now -- we're also helping out certain of us with DeepSeek as well. So we have good understanding of what AI compliance looks like at Cisco."
- DeepSeek's formal status at Cisco (approved, restricted, under evaluation) was not stated in the transcript.

### 7.10 Staffing and Compliance Scaling

- For the POC, only Colin is working on the project.
- For the full-scale engagement, additional team members would be "effectively Cisco employees for the duration of the engagement, all NDA signed, all other items taken care of on Cisco side."
- The security model scales: every BayOne team member gets the same treatment (Cisco hardware, Cisco-issued accounts, Cisco-approved tools only).

---

## 8. Tooling Constraints

[Primarily from 07_meeting_ai_compliance_and_tooling, with a repository access element from 07_meeting_architecture_and_repositories]

### 8.1 Library Installation Gate

- Colin: "Even the libraries that are used -- those are not able to be touched unless we get those approved first."
- Software supply chain is gated: Python libraries, npm packages, and other dependencies require approval before installation.
- The specific approval mechanism (formal Cisco change management process vs. BayOne-internal control) and approval time-to-response were not described.
- For the POC (Colin only), this is self-governed.

### 8.2 Network / Cloud Restrictions

- No external third-party cloud-based tools are permitted.
- LangGraph must run locally (Cisco-issued laptop), not on external cloud infrastructure.
- Claude Code is permitted only via Cisco's enterprise provisioning.

### 8.3 Repository Access Gating

- Repository access is enabled via Cisco internal groups; Colin's Cisco ID must be added to the required groups before he can access the repos [from 07_meeting_architecture_and_repositories].

### 8.4 Code Residency

- All code must remain on Cisco hardware (reaffirmed commitment from February 9, 2026 discovery meeting per Section 9 of the source document).
- No downloading code to personal machines under any circumstances.

### 8.5 NDA Status

- NDA already signed prior to this meeting.

---

## 9. Verbatim Scope Commitments

### 9.1 Akhil — Scope of the Rewrite

- "The first part is we want to rewrite in Angular the [inventory] screens and the same look, bring the same look and feel what we have in [EPNM] by rewriting in Angular."
- "EPNM is written in Dojo legacy, Dojo and the legacy basically framework."

### 9.2 Akhil — Modules in Scope

- "These are the scope of the modules which we identified. One is the network devices and device details and interface 360 and then fault management."

### 9.3 Akhil — Toggle Behavior

- "Once they toggle to the EMS and from that default UI, we can toggle back to the EMS UI. So basically introduce a theme toggle and default will be [EPNM] UI default and then you can toggle back to the EMS UI."
- "The default, once I log into the Crosswork UI, the default will be showing the EPNM theme. Basically the left menu and the other area should be [the EPNM] current [look and] feel should be shown instead of Magnetic."
- "Once I suppose I have a toggle button somewhere in the UI, once I toggle it to EMS UI, then the current design should be shown."

### 9.4 Akhil — Where Classic UI Code Lives (Partially Open)

- "So your point is like when you're rewriting in Angular, so where do you want to keep the code?... I mentioned about this particular EMS UI, UI is our repository, right? Maybe you can create a folder and for now you can add it out there, or you can create a separate repository also. It's up to you all. You can think about it and come up with your plan, then we can review it."

### 9.5 Firm Constraint on Build Integration

- "It has to be part of the new EMS build. Yeah, this is the art of this. And then you should be able to toggle and then realize it."

### 9.6 Akhil — Pattern Reuse

- "We also use the underlying Crosswork Common UI, right, and that pattern should be picked up from the existing port."

### 9.7 Selva — POC Part 1 vs. Part 2 Delineation

- "Just to put some delineation, Colin, whatever we covered earlier is part one of the POC, like the inventory device, like that's target for the POC. This is part two, and this is a different area."

### 9.8 Selva — Classic UI Must Talk to New Backend

- "We don't want this old back end to be brought over... when we bring over this classic look, you want that UI to talk to the new backend that exists on the next generation."

### 9.9 Selva — EMS Functional Scope

- "EMS is the terminology you would keep hearing, element management system, where you have the inventory, the fault, the performance monitoring, topology links, software image management, the underlay configurations, so on and so forth. So that functionality is what we provide in EMS and a subset of what we have in EPNM."

### 9.10 Selva — Cisco AI Tools Policy

- "It's part of any engagement here. We're not allowed to use Cisco code on anything that's outside of our... I mean, the approved AI tools that we get access to is the only thing that we use on our code. Which you are aware of and you mentioned."

### 9.11 Praveen — No Old Backend Brought Over

- "We don't want this old backend to be brought over. You're right, right? The functionalities, like when [Srama] said 80, 90% is there, and then you have [the new] product. They have an equivalent backend implemented, and that's how the new UI is talking to the [backend]. So when we bring over this classic look, you want that UI to talk to the new backend that exists on the next generation."

### 9.12 Praveen — Gap Handling

- "In the instance where potentially the new backend is not there, then... We need to consider adding equivalent functionality in the new [product] rather than just bringing over the whole old thing. That's too bulky to bring here and that's not the approach we're taking."

### 9.13 Ramesh — Staffing for POC

- "So presently, it will be only you working on the project?" (Colin confirmed yes for the POC.)

### 9.14 Colin — Visual Fidelity and Backend Mapping

- "So really we'll keep it exactly, visually speaking, and UX speaking identical to this EPNM use case. But Selva, as you said, map everything to the new backend. So that's very clear for me."

### 9.15 Colin — Gap Analysis Commitment

- "There will be a gap analysis. So we'll look for, you know, if there's anything critical that's missing and then those things that maybe, you know, that 10% that's remaining that might not be migrated or might not be compatibly migrated, we'll be able to flag that."

### 9.16 Colin — Both Cases Clear

- "On my side, I think the two cases here are clear. The code is clear."

---

## 10. Open Items

### 10.1 Architecture Open Items [from 07_meeting_architecture_and_repositories]
1. Exact backend repo names for EMS (the frontend repos Infra UI / Common UI / EMS UI are named; backend counterparts exist but were not named).
2. Shell app loading mechanism: how does Infra UI load EMS UI feature pages (micro-frontend, lazy-loaded modules, or monolithic Angular build)?
3. Common UI consumption pattern: npm package, Git submodule, or built together with EMS UI?
4. Harbor vs. Magnetic: two separate design systems or layers of one?
5. Toggle state management: per-user (persisted in backend), per-session, or per-browser?

### 10.2 Code Organization Open Items
6. Classic UI folder structure decision pending: new folder inside EMS UI repo vs. separate repo. Colin to propose plan.
7. Shared component reuse: how much of Common UI can the classic view reuse vs. needing its own components to match EPNM styling?
8. EPNM theming in Angular: how to handle coexistence of blue / white EPNM theme with Harbor / Magnetic in the same Angular app.

### 10.3 Backend Gap Open Items
9. Which specific EPNM backend features are not yet reimplemented in EMS (the 10-20% gap)?
10. Go services scope: which specific areas use Go vs. Spring Boot on the EMS backend? Is there a pattern?

### 10.4 Access Open Items
11. Complete EPNM repository list link: referenced in meeting, not captured in transcript.
12. Cisco group access timeline: how long to add Colin's ID to the required groups for repo access.

### 10.5 Inventory Walkthrough Open Items [from 07_meeting_product_walkthrough_inventory]
13. Full enumeration of Device Details sub-screens in the left menu.
14. Complete list of Device 360 actions (beyond "device console").
15. ChassisView data source: whether the interactive chassis view component has been reimplemented in EMS or falls into the ~20% gap.
16. Which operations bypass the database and query devices directly (the "in most cases" exception).
17. Exact step count of the device add wizard and field-by-step breakdown.
18. Bulk import CSV schema: required columns, optional columns, validation rules.
19. State management scheduling UI: time-picker and scheduling controls for "schedule maintain state" and "schedule managed state."
20. Interface 360 structure: same tabs as Device 360 or a different interface-specific layout.

### 10.6 Fault Management Walkthrough Open Items [from 07_meeting_product_walkthrough_faults]
21. Exact columns in the alarms table (not enumerated).
22. Visual representation of correlated alarms (tree hierarchy, grouped rows, correlation panel).
23. Syslog UI layout, filtering, and relationship to alarms / events views.
24. Real-time update mechanism for alarms (auto-refresh, polling, push).
25. Expandable row content: exact fields, layout, data source, lazy loading.
26. Advanced filter fields for fault management: criteria, operators, saved filter capabilities.
27. Cross-navigation between alarms, events, and syslogs.
28. Time-based filtering granularity on events: full preset list, custom ranges, calendar-picker.
29. Severity-based row coloring in alarms table.
30. Full action set beyond "clear alarms" (acknowledge, annotate, assign, suppress, create trouble ticket).
31. Relationship between "most recent events" pop-up and the full events page: same data with different filters, or different data sources.
32. Which EMS assurance backend APIs correspond to each fault management view.

### 10.7 AI Compliance and Tooling Open Items [from 07_meeting_ai_compliance_and_tooling]
33. DeepSeek formal status at Cisco (approved, restricted, under evaluation).
34. Claude Code data flow specifics: whether Cisco has a private Claude instance, whether code is sent to Anthropic servers under an enterprise agreement, or some other arrangement.
35. Library approval process mechanism and time-to-response.
36. LangGraph eventual hosting: if it moves off the laptop, to what (Cisco server / VM vs. cloud instance)?
37. Ramesh's ongoing oversight role vs. one-time due diligence.
38. Cross-engagement tool sharing between NX-OS CI/CD and EPNM-to-EMS engagements.
