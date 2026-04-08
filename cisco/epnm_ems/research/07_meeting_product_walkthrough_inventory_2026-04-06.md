# 07 - Meeting: Product Walkthrough -- Inventory

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting)
**Pass:** Focused deep dive on inventory screen walkthrough

---

## Overview

This document captures every detail of the live product walkthrough of the EPNM inventory screens conducted on April 6, 2026. This was the first time BayOne saw the product in action. All prior meetings (Sets 01-06) discussed the product abstractly -- architecture, scope, pricing, strategy. This meeting was the first live demonstration with Cisco's engineering tech leads present.

The walkthrough was led primarily by **Akhil** (tech lead), with commentary and supplementary context from **Srama** (tech lead) and **Praveen** (engineering lead). **Selva** provided the overarching narrative framing. Colin Moore attended as the BayOne technical lead who will execute the POC.

The inventory walkthrough constitutes **Part 1** of the POC scope. Fault management (covered in a separate document) constitutes Part 2. Akhil explicitly drew this distinction during the demo:

> "Just to put some delineation, Colin, whatever we covered earlier is part one of the POC, like the inventory device, like that's target for the POC. This is part two, and this is a different area."

---

## Meeting Context: What Was Known Before vs. What This Meeting Added

Before this walkthrough, BayOne understood the conceptual landscape: two products (EPNM and EMS), different architectures (monolithic vs. microservices), different frontends (Dojo vs. Angular), a customer requirement for legacy UI fidelity, and a POC scoped to specific screens. But BayOne had never seen the screens themselves, never observed the actual workflow, and never experienced the interaction model.

Praveen (Cisco engineering lead) opened the meeting by asking directly how much exposure BayOne had:

> "Is the team here from day one exposed to EPNM? Have you seen the product, have you accessed the functionality, the server, the user guide, or any other recordings of material, how much you are exposed to both the products, EPNM and CNC?"

Colin's answer was candid:

> "The real answer is not too much. I think we've talked with Selva and Guhan at a high level about the apps. We have not seen them yet. And that was actually one of the things that I wanted to, it was part of my initial request, of course, was to see maybe, you know, EPNM and EMS both in action. We understand the architecture, we understand what the business case is and what the, you know, what we're trying to do in good detail. But the actual usage of the apps, which is, of course, the most important thing to make sure we can have some functional equivalency when we do the transition, that remains."

This meeting closed that gap for the inventory domain.

---

## Pre-Walkthrough: Prepared Resources

Before beginning the live demo, Akhil (or a team member -- the transcript attributes this to the demonstrating speaker, likely Akhil given the flow) pointed out that Cisco's team had already staged reference materials:

- **User guide** -- available for both EPNM and EMS for deeper self-study
- **API documentation** -- added alongside the user guide
- **Recordings of EPNM device onboarding and network devices** -- pre-recorded walkthroughs
- **Recordings of EMS inventory and detailed views** -- pre-recorded walkthroughs

The speaker noted:

> "There is a user guide which is added here and similar in EMS... Then there is API documentation also added here. So I think our team has added some recordings so we can also go through the EPNM device onboarding and network devices. So that recording is added here. So similar way, EMS inventory and detailed views, recordings also added."

These materials were referenced as available on a Confluence page that the team had prepared.

---

## The EPNM UI: Legacy Technology Framing

Before logging into the system, Akhil provided the technology context. EPNM's UI is built on **Dojo**, specifically characterized as a legacy framework:

> "EPNM is written in Dojo legacy, Dojo and the legacy basically framework."

The stated objective for the POC is to **rewrite these screens in Angular** while preserving the identical look and feel:

> "The first part is we want to rewrite in Angular the [inventory] screens and the same look, bring the same look and feel what we have in [EPNM] by rewriting in Angular."

The toggle mechanism was described explicitly: once the rewritten screens exist, users will be able to switch between the classic (EPNM-style) experience and the modern EMS experience:

> "Once they toggle to the EMS and from that default UI, we can toggle back to the EMS UI. So basically introduce a theme toggle and default will be [EPNM] UI default and then you can toggle back to the EMS UI."

---

## POC Scope: Modules Identified

Akhil listed the specific modules in scope for the POC before beginning the demo:

1. **Network Devices** (list/table view)
2. **Device Details** (detailed view of a single device)
3. **Interface 360** (popup/overlay view with device alarms, modules, interfaces)
4. **Fault Management** (covered separately -- Part 2)

> "These are the scope of the modules which we identified. One is the network devices and device details and interface 360 and then fault management."

---

## Walkthrough: Network Devices Screen

### Login and Navigation

Akhil logged into the EPNM UI server. The **dashboard** is the landing screen after login. From the dashboard, the left navigation panel provides the path to inventory:

> "You see the left nav where inventory and network device. This is the screen we are talking about. Network devices. This comes under device management."

The navigation hierarchy observed:
- **Left navigation panel** -> **Inventory** -> **Network Devices**
- Also accessible via: **Device Management** -> **Network Devices**

Akhil noted that both paths exist:

> "So you can see there is already a device management network devices also."

### Filtering Panel (Left Side)

Once the Network Devices screen loaded, the left side of the screen displays a **filtering panel**:

> "If you look at the left side, there is a... Right now it is filtered by all devices. You can filter by device type and locations."

The filtering options observed:
- **All devices** (default view)
- **Filter by device type**
- **Filter by locations**
- **Filter by group and sites** (mentioned later in the walkthrough)

### Device Add Functionality

The Add Device workflow was demonstrated as a multi-step form:

> "Here you can add a device. Once you click on add a device, you have to enter the IP address and other details. So there is a step forward here. SNMP, Telnet, HTTP, HTTPS, et cetera."

**Single device add** requires:
- IP address
- Protocol credentials: SNMP, Telnet, HTTP, HTTPS (and potentially others -- "et cetera")
- The interface uses a step-by-step wizard flow ("step forward")

**Bulk import** is also supported:

> "Also, there is a bulk import. You can download the sample CSV and then also you can add the details and have a bulk import also."

The bulk import workflow: download a sample CSV template, populate it with device details, upload the CSV.

### Table Functionality

The network devices are displayed in a table with standard operations:

> "Then there is a basic table functionality like edit, delete, and all these are supported."

### Device State Management

Several device state management operations are available from the network devices screen:

> "Then we have admin state set to maintain state. Also, we have a set to manage state. Schedule the [maintain] state, schedule managed state, disable the handler inventory."

Operations observed:
- **Set to admin state**
- **Set to maintain state**
- **Set to manage state**
- **Schedule maintain state** (time-based scheduling)
- **Schedule managed state** (time-based scheduling)
- **Disable handler inventory**

### Additional Actions

> "And also there is export device, the new box certificate, OEM commands."

Actions available from the network devices toolbar:
- **Export device** (export device data)
- **New box certificate** (certificate management)
- **OEM commands** (vendor-specific command execution)

---

## Walkthrough: Device 360

### Launching Device 360

Device 360 is a popup/overlay view that can be launched from **multiple places** throughout the application. The first method demonstrated was via the info icon on the network devices table:

> "So you can click on this info icon, it will open device 360. And this device 360 can be launched from multiple places, so this is one of the places."

It was also noted that Device 360 can be launched from:
- The alarms view
- Various other windows throughout the application

> "It can be launched from different places like alarms here other different windows we can open it."

### Device 360 Content

The Device 360 popup contains multiple tabs and information sections:

> "Where you can see that alarms, modules, interfaces. From interface you can [open], again it will launch one more 360 view."

Observed tabs/sections within Device 360:
- **Alarms** (associated alarms for the device)
- **Modules** (hardware modules/components)
- **Interfaces** (network interfaces -- clicking an interface launches a nested Interface 360 view)
- **Location** (physical location information)
- **Recent changes** (change history)

### Nested 360 Views

A significant UX pattern: from within Device 360, clicking an interface launches an **Interface 360** view -- a second-level popup:

> "From interface you can [open], again it will launch one more 360 view."

This nesting pattern (360 inside 360) will need to be replicated in the Angular rewrite.

### Actions from Device 360

The Device 360 view includes an **actions menu**:

> "And there is also an action here, you can go to device console and we have different different actions available here."

Observed actions:
- **Device console** (direct console access)
- Multiple other actions (described as "different different actions")

### Alarms Popup from Device 360

From the alarms section within Device 360, there is an additional popup view for alarm details:

> "Again if you see alarms there is a different pop-up also here."

---

## Walkthrough: Device Details

### Navigation to Device Details

Device Details is accessed by clicking on the **device name** in the network devices table. The device name is rendered as a hyperlink:

> "You can click on this device name type is a hyperlink once you click here the left hand side you will see that chassis view."

### Device Details Layout

The Device Details screen has two primary areas:

**Left panel:** Chassis view (visual representation of the physical device)

**Main content area:** Multiple views accessible from a left menu:
- **System summary view**
- **Device details**
- **Chassis and enrollment** (and other left menu items)

Srama added context:

> "We have a system summary view, device details, and other left menu's [options like] chances [chassis] and enrollment."

### What Device Details Shows

Srama provided the definitive explanation of what this screen represents:

> "Basically, all this is information we collect from an individual network device. After you add a device, you give the credentials. You tell how to collect this information by using SNMP, [and] CLI. You can [configure] those credentials aspect. So the information is collected, parsed, and there is a data model where the data is abstracted."

The Device Details view shows **both physical and logical aspects** of the device:

> "What you see here is the physical aspects of the device and also the configurations such as the routing and other logical configurations on the device."

Physical aspects: hardware components, chassis layout, modules, ports
Logical aspects: routing configurations, other software-defined configurations

---

## Data Flow Architecture

### How Data Gets Into the System

Srama described the complete data flow during the device details portion of the walkthrough. This is the most technically significant architectural explanation provided in the meeting.

**Step 1: Device discovery and credential setup.** When a device is added, the administrator provides credentials and specifies which protocols to use for data collection. The protocols mentioned explicitly are **SNMP** and **CLI**.

**Step 2: Data collection.** The system uses the configured protocols to query the network devices. SNMP polling and CLI commands retrieve device state, configuration, and inventory information.

**Step 3: Parsing and abstraction.** The raw data from devices is collected, parsed, and stored in a **data model** where it is abstracted:

> "The information is collected, parsed, and there is a data model where the data is abstracted."

**Step 4: Database storage.** In EPNM, this abstracted data is stored in **Oracle**:

> "All of them will consume that data from the database, Oracle is the database here."

**Step 5: Application consumption.** Multiple application components within the product consume data from the database. The application does not typically query devices directly at runtime:

> "And then the various applications, when I say applications within the product, you will have an inventory component, there will be a topology component, there will be a fault component, so on and so forth, service level component. All of them will consume that data from the database."

**Step 6: Business functions.** Each application component uses the data for its specific purpose:

> "They either use it for the business application, visualization, monitoring, configuration, troubleshooting, so on and so forth."

### Diagram: EPNM Data Flow

```
Network Devices
    |
    | (SNMP / CLI queries)
    v
Data Collection & Parsing Layer
    |
    | (abstracted data model)
    v
Oracle Database (EPNM) / PostgreSQL (EMS)
    |
    +---> Inventory Component
    +---> Topology Component
    +---> Fault Component
    +---> Service Level Component
    +---> Performance Monitoring
    +---> Software Image Management
    |
    v
UI Rendering (Dojo in EPNM / Angular in EMS)
```

### Application Reads from Database, Not Devices

Colin asked a clarifying question to confirm the data flow direction:

> "So where this application reads from isn't necessarily the device directly, but instead this application reads from Oracle. Is that right? Or is it reading from both or situationally?"

The answer was definitive:

> "In most of the cases, it won't directly go to the [device]. It reads from the database correct."

The qualifier "in most of the cases" suggests there may be edge cases where the application does query devices directly (perhaps for real-time console access or on-demand operations), but the standard operational pattern is database-first.

---

## Database Migration: Oracle to PostgreSQL

### The Change

A critical architectural fact was revealed during this exchange. Colin, having confirmed that EPNM reads from Oracle, was about to ask about database compatibility when the Cisco team preempted:

> "By the way, there's no [Oracle] in the new product. There's Postgres in the new product. We've gotten rid of Oracle dependency."

This is a significant simplification for the conversion work. Oracle is a proprietary, licensed database with its own SQL dialect, PL/SQL stored procedures, and operational complexity. PostgreSQL is open-source. The removal of Oracle dependency in EMS means:

1. No Oracle licensing costs or dependencies in the new product
2. PostgreSQL's SQL dialect is more standard
3. The new backend already has its own data access layer built for PostgreSQL

Colin's reaction confirmed this was welcome news:

> "Even easier, then. That's good."

### Implications for the POC

The database migration is **already complete** in EMS. The POC does not need to migrate data or schema from Oracle to PostgreSQL. Instead, the POC's classic UI rewrite will consume data from the PostgreSQL-backed EMS APIs. The old EPNM backend (Oracle-based) is not being carried forward.

Praveen explicitly clarified this point:

> "We don't want this old backend to be brought over. You're right, right? The functionalities, like when [Srama] said 80, 90% is there, and then you have [the new] product. They have an equivalent backend implemented, and that's how the new UI is talking to the [backend]. So when we bring over this classic look, you want that UI to talk to the new backend that exists on the next generation."

Colin confirmed understanding:

> "So really we'll keep it exactly, visually speaking, and UX speaking identical to this EPNM use case. But Selva, as you said, map everything to the new backend. So that's very clear for me."

---

## Backend Migration Status: The 80% Figure

### What Has Been Reimplemented

Colin asked the direct question about backend migration status:

> "Between EPNM and EMS? Is that functionality, in terms of the backend, already moved over? Or is that something that's still pending to query the devices?"

The answer established a critical quantitative benchmark:

> "It's not exactly migrated in a way. Things got reimplemented. Some of it, at least 80% of it, is there in the other product as in the newer product."

Key distinctions in this statement:

1. **Not migrated -- reimplemented.** The backend was not ported from EPNM; it was rebuilt for EMS. This is consistent with what was established in Meeting 02 (the monolithic architecture cannot be directly ported).

2. **At least 80%.** The speaker estimated that 80% or more of the backend functionality already exists in EMS. This means the majority of the data access, business logic, and API layers that a classic UI would need to call are already present.

3. **"At least."** The qualifier suggests 80% is a conservative estimate. The actual number may be higher.

### What This Means for the POC

For the POC screens (inventory and fault management), the implication is that most of the backend APIs the classic UI will need to call already exist in EMS. The POC is primarily a frontend conversion with API mapping -- not a backend development project for the majority of functionality.

However, the remaining ~20% of backend functionality that has not been reimplemented represents the gap analysis work that Colin referenced:

> "There will be a gap analysis. So we'll look for, you know, if there's anything critical that's missing and then those things that maybe, you know, that 10% that's remaining that might not be migrated or might not be compatibly migrated, we'll be able to flag that."

(Note: Colin said "10%" here, likely rounding from the "80-90%" stated by the Cisco team, suggesting 10-20% is the remaining gap.)

### Where Backend Gaps Exist

Praveen addressed what happens when the new backend does not have equivalent functionality:

> "In the instance where potentially the new backend is not there, then... We need to consider adding equivalent functionality in the new [product] rather than just bringing over the whole old thing. That's too bulky to bring here and that's not the approach we're taking."

This confirms the design principle: when a gap is found, new code is written for EMS rather than extracting old code from EPNM. The monolithic EPNM backend is explicitly ruled out as a source of transplanted code.

---

## Image Storage

### How Device Images Are Stored

Colin asked specifically about the device images (chassis views, asset type images) that appear in the EPNM UI:

> "On the old EPNM system, there was that view that had, let's say, like pictures, images for the actual network devices. So for those ones, are those actually stored in the application? Are those being sourced from Oracle? And if so, where do those live now for the new application?"

Colin noted that in Oracle-based systems, images are sometimes stored directly in the database (as BLOBs):

> "I know sometimes in Oracle, those are stored natively within Oracle itself and then pulled into the application at runtime, or maybe they're just built into the application."

The answer was clear:

> "For the new UI, it is part of the application, not stored in Oracle and all."

**Images are stored as application assets in EMS, not in the database.** This means the chassis view images, device type icons, and other visual assets are bundled with the application code, not retrieved from PostgreSQL at runtime. This simplifies the frontend conversion -- images are static assets that can be referenced directly without database queries.

---

## Selva's EMS Functional Scope Summary

Selva provided a comprehensive summary of what EMS covers, reinforcing the scope of the element management domain:

> "EMS is the terminology you would keep hearing, element management system, where you have the inventory, the fault, the performance monitoring, topology links, software image management, the underlay configurations, so on and so forth. So that functionality is what we provide in EMS and a subset of what we have in EPNM."

EMS functional areas confirmed:
- **Inventory** (device management, device details)
- **Fault** (alarms, events, syslogs)
- **Performance monitoring**
- **Topology and links**
- **Software image management**
- **Underlay configurations**

The critical qualifier: EMS is described as **"a subset of what we have in EPNM."** Even with 80%+ reimplementation, EMS does not yet have full feature parity with EPNM.

---

## Colin's Assessment During the Walkthrough

After seeing the inventory screens live for the first time, Colin gave an on-the-spot assessment that is worth capturing:

> "This is great. I actually feel pretty good about this as we're going."

Specifically on the UI conversion complexity:

> "For the new interface, because I think that's probably where the next questions that I'd have, and I can wait for those until later. So new interface, definitely new stack. From a UI perspective, this is going to be great, because this is nice and clean."

On the popup/modal patterns:

> "The pop-up windows, the modal dialogues that are coming, those will be fine. And I think that's very clear as to what everything does."

On sub-screens and nested views:

> "We'll be able to fully map out from one screen, even if there's, let's call them sub-screens within a screen. For instance, whenever that pop-up was showing, that we can definitely do."

On Device 360:

> "For the 360, that won't be a problem."

This assessment is significant because it is the first time the person who will execute the POC has seen the actual product. His reaction -- that the screens are "nice and clean" and the conversion is feasible -- is a positive signal for POC confidence.

---

## EPNM Design System vs. EMS Design System

The Cisco team described the visual theming differences between the two products:

**EPNM:** Blue and white color scheme

> "If you look at the [EPNM] theming is kind of a blue and white kind of thing."

**EMS (Crosswork UI):** Uses the **Harbor** and **Magnetic** design system

> "If you look at the Crosswork UI, we have a magnetic design system. So it's a design system called Harbor and magnetic design system."

The Crosswork UI (which includes EMS) runs on **Angular 21**:

> "Crosswork UI is pretty much on Angular stack, latest Angular 21 is used here."

### The Toggle Behavior

The desired toggle behavior was described in more detail:

> "The default, once I log into the Crosswork UI, the default will be showing the [EPNM] theme. Basically the left menu and the other area should be [the EPNM] current [look and] feel should be shown instead of magnetic."

This clarifies the toggle design:
- **Default state after login:** Classic EPNM look and feel (blue/white, legacy layout)
- **After toggling:** Modern EMS/Magnetic design system
- The toggle switches the entire visual experience, not individual components

---

## Open Questions from the Inventory Walkthrough

### 1. Exact List of Device Details Sub-Screens

The walkthrough showed "system summary view, device details, and other left menu options" but did not enumerate every sub-screen in the device details left menu. A full inventory of all device details sub-screens is needed for the POC scope.

### 2. Which Device 360 Actions Exist

Akhil mentioned "different different actions available" in the Device 360 action menu but did not enumerate them beyond "device console." The complete action list needs to be documented from the application or user guide.

### 3. ChassisView Data Source

Images are confirmed as application assets in EMS. However, the chassis view itself is more than images -- it includes interactive elements showing module slots, port states, and hardware hierarchy. Whether the chassis view component has been reimplemented in EMS, or whether this falls into the ~20% gap, was not stated.

### 4. "In Most Cases" Database Reads

The confirmation that the application reads from the database "in most of the cases" implies exceptions exist. What operations bypass the database and query devices directly? This matters for the classic UI rewrite because those operations would need different API patterns.

### 5. Device Add Wizard Step Count

The add-device wizard was described as having a "step forward" pattern with SNMP, Telnet, HTTP, HTTPS credentials. The exact number of steps in the wizard and which fields appear on each step were not enumerated in the demo.

### 6. Bulk Import CSV Schema

The bulk import feature uses a downloadable CSV template. The schema of that CSV (required columns, optional columns, validation rules) was not discussed. This will need to be understood for the POC conversion.

### 7. State Management Scheduling

"Schedule maintain state" and "schedule managed state" imply a time-picker or scheduling UI within the network devices screen. This scheduling sub-feature was not demonstrated in detail.

### 8. Interface 360 vs. Device 360

The demo showed that Interface 360 launches from within Device 360. Whether Interface 360 has the same tabs and structure as Device 360, or a different layout specific to interfaces, was not clarified.

---

## Cross-Reference: How This Meeting Resolves Prior Questions

### From Set 02 (2026-02-20): "What does the EPNM UI actually look like?"

Now answered. The EPNM UI has been seen live for the first time. It features a dashboard landing page, left navigation panel, filterable device tables, popup Device 360 views, nested Interface 360 views, and a multi-step device add wizard. The overall design language is blue and white with a clean, utilitarian layout.

### From Set 02 (2026-02-20): "Are the functionality gaps purely vertical?"

Reinforced. Srama's description of the data flow (SNMP/CLI -> parsing -> data model -> Oracle -> application components) shows that the architecture is indeed vertically integrated. However, the 80% backend reimplementation figure is new information that significantly narrows the expected gap for the POC screens.

### From Set 02 (2026-02-20): "What database does EMS use?"

Now answered definitively. EMS uses **PostgreSQL**. Oracle has been completely eliminated. This was stated as a deliberate design choice: "We've gotten rid of Oracle dependency."

### From Set 03 (2026-03-25): "What are the specific screens for the POC?"

Now answered. The POC Part 1 covers: Network Devices list, Device 360, Device Details (including chassis view). POC Part 2 covers fault management (alarms, events, syslogs).

---

## Key Terminology from This Walkthrough

| Term | Meaning |
|------|---------|
| **Network Devices** | The primary inventory list screen showing all managed devices in a filterable table |
| **Device 360** | A popup overlay showing a device's alarms, modules, interfaces, location, and recent changes -- launchable from multiple places in the application |
| **Interface 360** | A nested popup launched from within Device 360, showing details for a specific network interface |
| **Device Details** | The full-page detailed view of a single device, including chassis view, system summary, and configuration information |
| **Chassis View** | Visual representation of the physical device hardware, showing modules and ports |
| **Admin State** | A device lifecycle state (administrative control) |
| **Maintain State** | A device state indicating maintenance mode |
| **Managed State** | A device state indicating active management |
| **Data Model** | The abstracted representation of device data, parsed from SNMP/CLI responses and stored in the database |
| **Harbor / Magnetic** | Cisco's design system used by Crosswork UI / EMS (the modern visual language) |
| **Dojo** | The legacy JavaScript UI framework used in EPNM |
| **Angular 21** | The current version of Angular used in the EMS/Crosswork UI frontend |
| **Theme Toggle** | The proposed UI control that switches between classic (EPNM-style) and modern (Magnetic) visual experiences |

---

## Summary of What Was Seen

This walkthrough provided BayOne's first direct exposure to the EPNM inventory screens. The key takeaways for POC execution:

1. **The screens are well-structured and clean.** Colin's assessment that the UI is "nice and clean" suggests the conversion will not require reverse-engineering complex or tangled layouts.

2. **The data flow is database-centric.** The application reads from the database in most cases, not from devices directly. This means the classic UI only needs to call EMS APIs that read from PostgreSQL -- no need to replicate device polling logic.

3. **80%+ of the backend already exists in EMS.** The majority of APIs the classic UI needs are already implemented.

4. **Images are application assets.** No database retrieval needed for device images in the new system.

5. **Oracle is gone.** The PostgreSQL migration is complete. No Oracle compatibility concerns.

6. **The popup/modal pattern is consistent.** Device 360 and Interface 360 follow a consistent overlay pattern that can be implemented as reusable Angular components.

7. **The toggle defaults to classic.** The desired behavior is that the EPNM-style UI is the default experience, with the option to switch to the modern Magnetic design system.
