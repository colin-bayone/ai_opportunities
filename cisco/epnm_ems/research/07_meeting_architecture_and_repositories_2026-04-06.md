# 07 - Meeting: Architecture and Repository Structure

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting)
**Pass:** Focused deep dive on architecture and repository structure

---

## 1. Two-Product Landscape

The meeting confirmed the two-product architecture that has been discussed in prior sessions:

- **EPNM** (Evolved Programmable Network Manager) -- the legacy/current product, built on a Dojo-based frontend framework with an Oracle database backend.
- **EMS** (Element Management System) -- the next-generation product, part of **CNC** (Crosswork Network Controller). Built on Angular with a Postgres backend.

Pradeep framed the relationship: "There is a data model where the data is abstracted. And then the various applications -- when I say applications within the product -- you will have an inventory component, there will be a topology component, there will be a fault component, so on and so forth, service level component. All of them will consume that data from the database."

The key distinction for this engagement: EPNM functionality was not directly "migrated" to EMS. As the team clarified: "It's not exactly migrated in a way. Things got reimplemented. Some of it, at least 80% of it, is there in the other product, as in the newer product."

---

## 2. EPNM Repositories (Legacy Side)

Akhil walked through the EPNM repository structure. The EPNM codebase is organized across multiple repositories by functional area:

### 2.1 PI Framework Repository
- **Name:** PI Framework (referenced as "core framework in Dojo")
- **Purpose:** Core UI framework for EPNM, written in Dojo
- **Description:** Contains "the prime UI and the framework UI, Dojo based"
- The transcript refers to this as the foundational framework layer

### 2.2 Wireless Framework Repository
- **Name:** Wireless Framework / Wireless Repos
- **Purpose:** Contains wireless-specific UI and framework code
- **Description:** Referenced alongside PI Framework as part of the EPNM frontend stack

### 2.3 Assembly Repository
- **Name:** Assembly Repo
- **Purpose:** Contains inventory-related UI screens
- **Description:** "Inventory screens are part of the assembly repo"
- Akhil noted: "Assembly is on the UI side"
- Additional repos also contain inventory-related items (not named individually)

### 2.4 ChassisView Repository
- **Name:** ChassisView Repo
- **Purpose:** Contains the chassis visualization component
- **Description:** "ChassisView is coming from the ChassisView repo"
- This renders the physical device images and chassis layout views seen in the device details screen

### 2.5 Fault Management Repositories
- **Name:** Referenced as "fault management EPA wireless repo" and "fault" (likely EPA = EPNM Assurance)
- **Purpose:** Fault/alarm management backend and frontend
- **Description:** Akhil noted that fault management spans backend and frontend: "The fault is on the backend... it's backend and frontend, and assembly is on the UI side"
- "EMS Assurance" was also mentioned as "back end side" -- this may be the EMS-side equivalent

### 2.6 Complete Repository List
Akhil referenced an external link for the complete EPNM repository list: "You can find out your complete repository list in this link also." This link was shared in the meeting materials/chat but is not captured in the transcript text.

---

## 3. EMS Repositories (New Generation Side)

The EMS architecture follows a three-layer repository model. Akhil explained this clearly:

### 3.1 Infra UI (Shell App)
- **Name:** Infra UI Repository
- **Purpose:** The shell application -- top-level application container
- **What it contains:** "This header and the top menu and other infrastructure UI components is coming from Infra UI repository"
- **Architecture role:** This is the outermost layer. It provides the application shell that all other modules load into. The shell app renders:
  - Header bar
  - Top navigation menu
  - Infrastructure-level UI components (login, layout frame, etc.)

### 3.2 Common UI (Shared Components)
- **Name:** Common UI Repository
- **Purpose:** Shared/reusable UI components consumed across EMS
- **What it contains:** Akhil gave a concrete example: "If you look at this card, right? These cards and the tables and these things are called common components. So this common component is part of this common UI."
- **Architecture role:** Component library layer. Sits between the shell app and feature pages. Contains:
  - Card components
  - Table components
  - Common UI widgets and patterns
  - Shared design patterns from Harbor/Magnetic design system

### 3.3 EMS UI (Feature Pages)
- **Name:** EMS UI Repository
- **Purpose:** Feature-specific pages for EMS functionality
- **What it contains:** "All these EMS related pages like Praveen mentioned about software image management and other things, other pages is part of this repo"
- **Architecture role:** This is the feature layer where specific product functionality lives:
  - Software image management
  - Inventory views
  - Fault management views
  - Device management pages
  - All EMS-specific feature screens

### 3.4 Backend Repositories
- Referenced as "corresponding" backend repositories alongside the frontend repos
- Akhil mentioned: "Back-end party, yeah, this is a corresponding... Postgres... backend"
- The backend repo names were not explicitly stated in the transcript, but they exist as counterparts to the frontend repos

---

## 4. Shell App Architecture

The shell app pattern is central to understanding how EMS is structured:

```
+--------------------------------------------------+
|  Infra UI (Shell App)                            |
|  - Header, top nav, infrastructure components    |
|  +--------------------------------------------+  |
|  |  Common UI (Shared Components)             |  |
|  |  - Cards, tables, design system widgets    |  |
|  |  +--------------------------------------+  |  |
|  |  |  EMS UI (Feature Pages)              |  |  |
|  |  |  - Inventory, Fault, SIM, etc.       |  |  |
|  |  +--------------------------------------+  |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
```

Key statement from Akhil: "EMS is kind of like built on top of shell app. So when I say shell app means this header and the top menu and other infrastructure UI components is coming from Infra UI repository."

The pattern Akhil described for how the classic UI code should integrate: "We also use the underlying Crosswork Common UI, right, and that pattern should be picked up from the existing port."

---

## 5. Frontend Technology Stack

### 5.1 EPNM Frontend (Legacy)
- **Framework:** Dojo (legacy version)
- **Description:** "EPNM UI is a Dojo based framework"
- **Theming:** "The theming is kind of a blue and white kind of thing"
- **Architecture:** Likely MVC pattern. Colin noted: "If this is MVC architecture, I'm assuming for the old application, because it was on Dojo, we'll get that mapped out."

### 5.2 EMS Frontend (New Generation)
- **Framework:** Angular 21 (latest version)
- **Design System:** Harbor and Magnetic design system
  - Akhil: "If you look at the Crosswork UI, we have a Magnetic design system. So it's a design system called Harbor and Magnetic design system you're using."
- **Branding:** Crosswork UI design language
- **Description:** "Crosswork UI is pretty much on Angular stack, latest Angular 21 is used here"

---

## 6. Backend Technology Stack

### 6.1 EPNM Backend
- **Database:** Oracle
- **Data collection:** SNMP, CLI (referred to as "ECLI" in transcript) for device polling
- **Pattern:** Devices are polled, data is parsed, stored in Oracle, then consumed by application components
- Pradeep's description: "The information is collected, parsed, and there is a data model where the data is abstracted."

### 6.2 EMS Backend
- **Database:** PostgreSQL ("There's Postgres in the new product. We've gotten rid of Oracle dependency.")
- **Primary framework:** Spring Boot ("Mostly Spring Boot, yes")
- **Additional services:** Go services for certain areas
  - Pradeep clarified: "Somewhere... based application is being used. There are areas, at least on the device management side, and there are Go services running at the back end."
- **API layer:** REST APIs serve the Angular frontend
- **Device images:** Stored in the application itself, not in the database. ("For the new UI, it is part of the application, not stored in Oracle and all.")

### 6.3 Backend Reimplementation (Not Migration)
The team emphasized that the EMS backend is not a direct migration from EPNM:
- ~80% of EPNM functionality has been reimplemented in EMS
- ~10-20% gap remains
- The classic UI (POC deliverable) must connect to the new EMS backend, not bring over the old EPNM backend
- Selva: "We don't want this old back end to be brought over... when we bring over this classic look, you want that UI to talk to the new backend that exists on the next generation."

---

## 7. Where Should New Classic UI Code Live?

This was a key architectural question raised by Colin during the meeting:

### 7.1 The Question
Colin asked: "If there's a case where there might not be a UI element that exists in repository B on the EMS side, what do you want us to do there? Do you want us to keep it kind of off? Or do you want us to add in those UI elements there? So for instance, you have the old UI elements from EPNM in the EPNM repo. Where do you want the, let's say the old version that's connected to the new backend, where would you like those to live?"

### 7.2 The Answer (Partially Open)
Akhil's response: "So your point is like when you're rewriting in Angular, so where do you want to keep the code?... I mentioned about this particular EMS UI, UI is our repository, right? Maybe you can create a folder and for now you can add it out there, or you can create a separate repository also. It's up to you all. You can think about it and come up with your plan, then we can review it."

### 7.3 The Constraint
There was one firm constraint: "It has to be part of the new EMS build. Yeah, this is the art of this. And then you should be able to toggle and then realize it."

### 7.4 The Agreed Approach
Colin proposed a collaborative approach: "Organization-wise, yeah, I'd like to work with the team on that."

Two options emerged:
1. **New folder within EMS UI repo** -- Create a folder within the existing EMS UI repository for classic UI components
2. **Separate repository** -- Create a standalone repository for classic UI code

The decision was deferred, with Colin to propose a plan for team review.

---

## 8. The Toggle Mechanism

The toggle between classic (EPNM-style) and current (EMS/Magnetic) UI is a core deliverable:

- Akhil: "The default, once I log into the Crosswork UI, the default will be showing the EPNM theme. Basically the left menu and the other area should be... the EPNM current feel should be shown instead of Magnetic."
- Toggle behavior: "Once I suppose I have a toggle button somewhere in the UI, once I toggle it to EMS UI, then the current design should be shown."
- Default state: EPNM classic view is the default after login
- Toggle target: Switch to current EMS/Magnetic design
- Implementation: Colin's team can propose the toggle mechanism

---

## 9. Data Architecture Pattern

The data flow for both products follows the same fundamental pattern:

```
Network Devices
    |
    | (SNMP, CLI polling)
    v
Data Collection & Parsing
    |
    v
Database (Oracle for EPNM / Postgres for EMS)
    |
    v
Application Components (Inventory, Topology, Fault, etc.)
    |
    v
UI Rendering
```

Key clarification from the meeting:
- Colin: "This application reads from isn't necessarily the device directly, but instead this application reads from Oracle. Is that right?"
- Team response: "In most of the cases, it won't directly go to the [device]. It reads from the database, correct."
- Same pattern applies to EMS, just with Postgres instead of Oracle

---

## 10. Repository Access

Access to repositories is controlled through Cisco internal groups:

- Akhil: "It is basically controlled through [Cisco] groups. So when we can get that activated... a few groups we have to enable this access. So once after that, he can seamlessly access all the repos."
- Selva confirmed: "It's part of your any engagement here. We're not allowed to use Cisco code on anything that's outside of our... I mean, they're approved AI tools that we get access to is the only thing that we use on our code."
- Action item: Akhil or team to get Colin's Cisco ID added to the appropriate groups for repository access

---

## 11. Open Questions

### Architecture Questions
1. **Exact backend repo names for EMS** -- The frontend repos (Infra UI, Common UI, EMS UI) were named clearly, but the corresponding backend repository names were not explicitly stated
2. **Shell app loading mechanism** -- How does the Infra UI shell app load the EMS UI feature pages? Is this micro-frontend, lazy-loaded modules, or a monolithic Angular build?
3. **Common UI consumption pattern** -- Is Common UI consumed as an npm package, a Git submodule, or built together with EMS UI?
4. **Harbor vs. Magnetic** -- Are these two separate design systems, or layers of one system? Akhil mentioned both: "a design system called Harbor and Magnetic design system"
5. **Where the toggle state is managed** -- Is the toggle per-user (persisted in backend), per-session, or per-browser?

### Code Organization Questions
6. **Classic UI folder structure** -- Decision pending: new folder in EMS UI repo vs. separate repo. Colin to propose plan.
7. **Shared component reuse** -- How much of Common UI can the classic view reuse vs. needing its own components to match EPNM styling?
8. **EPNM theming in Angular** -- The classic view needs "blue and white" EPNM theming within an Angular app that uses Harbor/Magnetic. How to handle theme coexistence?

### Backend Gap Questions
9. **The 10-20% functionality gap** -- Which specific EPNM backend features are not yet reimplemented in EMS? This determines where classic UI screens might not have data sources.
10. **Go services scope** -- Which specific areas use Go vs. Spring Boot on the EMS backend? Is there a pattern to when Go is used?

### Access Questions
11. **Complete repository list link** -- Referenced in meeting but not captured in transcript. Need to obtain this link.
12. **Cisco group access timeline** -- How long does it take to get Colin's ID added to the required Cisco groups for repo access?
