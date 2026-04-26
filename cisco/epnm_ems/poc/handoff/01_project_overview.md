# 01 — Project Overview

**Purpose of this document:** The anchor explanation of what this project is, why it exists, what the work is, and who the work is for. Read this first after the index. Every other document in this handoff package is a refinement of material introduced here.

---

## 1. What the Two Products Are

### EPNM (Evolved Programmable Network Manager)

Cisco's long-standing network management product. Customers have been running it for roughly a decade. EPNM is built on a Dojo 1.x frontend framework with a Java monolith backend and an Oracle database. Device information is collected from the network via SNMP and CLI polling, parsed into an internal data model, persisted to Oracle, and rendered by Dojo/Dijit-based UI components. The visual theme is blue and white. The product spans inventory, topology, fault management, service level, performance monitoring, software image management, and related functional areas. EPNM's codebase includes a core framework repository (PI framework, Dojo-based), a wireless framework repository, an assembly repository that contains the inventory UI, a ChassisView repository, and fault management repositories.

### EMS (Element Management System) inside CNC (Crosswork Network Controller)

The next-generation product, part of Cisco's Crosswork Network Controller (CNC) platform. EMS uses an Angular 21 frontend on the Harbor and Magnetic design system, a Spring Boot backend with some Go services on the device-management side, and PostgreSQL instead of Oracle. EMS follows a three-layer shell-app model: Infra UI provides the outer shell (header, top navigation, infrastructure UI, login, layout frame), Common UI provides shared reusable components (cards, tables, common widgets), and EMS UI holds feature-specific pages. The Cisco team characterized EMS as "a subset of what we have in EPNM" — approximately 80 percent (or 80-90 percent) of EPNM backend functionality has been reimplemented in EMS. EMS was not migrated from EPNM; it was independently reimplemented.

### The functional overlap relevant to the POC

Both products cover the same concepts (inventory, faults, events, device management) but with different UX, different technology stacks, and different backends. The backends are not shared. The UX differs significantly because EMS was redesigned with a modern Angular-based visual language, not a port of the EPNM UX.

---

## 2. The Customer Problem That Created This Engagement

Customers who operate EPNM have roughly ten years of muscle memory with its UI. When Cisco shipped EMS with a redesigned UX, customers reacted badly. Multiple customer escalations came back to Guhan's team asking for the option to continue using the classic EPNM experience. Guhan captured the dynamic in his own words: "Our customers are asking that the operators are very used to a 10-year-old product. They can't just like that — one thing, they don't want to learn everything. They're asking us two or three, two releases or something, like a year, like a couple of releases or two or three. So we keep classic and the new."

This is not a complaint about missing features. It is a complaint about the UX change. The operators see EMS's new UX as a productivity tax during the transition period. Customers are asking Cisco for a bridge: let operators keep the familiar EPNM experience while they gradually learn the new one, then phase the classic view out once the new UX becomes the default.

Selva added the commercial lens: "When it comes to renewal, we want the customers to go to this new product and the new thing. We don't want them to stick around with the older one." The classic view toggle is not just customer accommodation. It is a migration mechanism. Cisco wants to retire EPNM and move customers to EMS for renewal revenue purposes, but cannot force the transition without giving operators a comfort bridge.

Guhan described the target end state: "Over time we say okay we're going to take away your old view. This is the only view right now." The classic view is explicitly temporary. Its job is to ease adoption, not to become a permanent dual experience.

---

## 3. The Four-Phase Lifecycle the Classic View Toggle Serves

As articulated by Selva and Guhan together:

1. **Current state.** EMS ships with the new UX only. Customers resist.
2. **Target state (what this engagement delivers).** EMS gets a classic view toggle. Customers can switch to the EPNM-style experience on a screen-by-screen basis during the POC, eventually globally at the product level.
3. **Transition period.** Customers use the classic view as a comfort bridge while their operators gradually adopt the new UX on their own schedule.
4. **End state.** Classic view is deprecated and removed. The new UX becomes the only view.

The Outlook and banking-app analogy was introduced by Selva to anchor this pattern: "We are looking at, you know, like how in Outlook and some of the banking applications, when you change your flow or when you come up with a new UX, they give you the option to toggle and say, I want to continue with the old workflow until I'm comfortable. And then I want to switch to the new thing."

---

## 4. What This POC Actually Is

### It is a UX overlay, not a full-stack conversion

This is the single most important piece of context. The earlier framing of the engagement (Sets 01 and 02 of the research library, roughly February 2026) treated the work as a full-stack vertical conversion of missing EPNM functionality into EMS. That framing was **explicitly reversed** on 2026-03-25 when Selva clarified: "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI. But obviously, it's been redesigned to adopt a new workflow, a new UX and everything."

Selva's metaphor: "Take that UX and that experience, marry it with the backend that's already there in the system." Guhan's version: "It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel."

The POC is a visual and interaction-model fidelity exercise. Rebuild the EPNM UX in Angular, wire it to the existing EMS backend, and ship it inside the EMS build as an alternate theme.

### Two screens are in scope

The POC covers two functional areas, confirmed at the 2026-04-06 walkthrough with the Cisco engineering team:

- **Inventory.** Specifically: the Network Devices list, Device Details (with Chassis View on the left and a left-menu of system summary, device details, chassis and enrollment, and other sub-views), Device 360 (launched from an info icon; tabs for alarms, modules, interfaces, location, recent changes), and Interface 360 (launched from the interfaces tab of Device 360 — a nested 360 view inside a 360 view).
- **Fault Management.** Specifically: the alarms table (with correlated alarms, expandable rows with general information, quick filter and advanced filter, column picker, clear-alarm action), the events interface (most-recent-events popup, past-8-hours default time window, full events page as a secondary table), and syslogs.

Selva drew the delineation explicitly: "Just to put some delineation, Colin, whatever we covered earlier is part one of the POC, like the inventory device, like that's target for the POC. This is part two, and this is a different area." Inventory is Part 1. Fault Management is Part 2.

### The toggle is local per screen for the POC

For the POC, each targeted screen will have its own embedded toggle control. This is deliberately simplified. The product-level global toggle (a user-settings preference that flips the entire application to classic view) is explicitly deferred out of the POC. Selva: "Now, let's say we're going to pick three screens. We're going to have a local toggle on each one — one, each one, another — to keep it simple. Because you're just illustrating the idea."

### Default view on login is the classic theme

Akhil confirmed during the walkthrough that, once logged into the Crosswork UI, the default rendering should be the EPNM theme — blue and white, Dojo-style layout — with the toggle flipping the page to the Magnetic-designed EMS appearance. This is the opposite of what a casual observer might expect. The classic view is the default; the new UX is behind the toggle.

### The backend is explicitly untouched

Guhan was emphatic: "And we don't want to rewrite the backend services. So that can keep me honest. Because that's a lot of work. If we write all the backend again, then we have to maintain two different versions. We're not staffed. It's not the right way to do it." Selva echoed: "Guhan is absolutely right. We're not trying to reboot the backend from older." The only exception is narrow: "Slight touchup to the backend to do that filtering" (adding a filter parameter, widening or narrowing a query scope). Anything larger is out of scope.

The classic UI consumes the same EMS REST APIs that the new UX consumes. Both views hit the same Spring Boot and Go services. Both read from the same PostgreSQL database. Presentation-layer differences are adapted on the client side through display adapters, not backend changes.

### Functional equivalence is the acceptance bar

Guhan's success criterion: "Final test will be to show the same thing comes up everywhere." Perform the same actions in both views. Verify identical results. Because both views share a backend, results must match. This is what acceptance testing validates.

### The POC must be production-quality code

Selva: "It's going to be product of product. It's not a prototype. Eventually it will be product, right?" The classic view feature will ship to customers. POC output must be production-grade. This is a POC in the sense that it demonstrates the approach on two screens before scaling across the full product surface area. It is not a throwaway prototype.

---

## 5. Why Cisco Brought BayOne In

Cisco explicitly rejected the traditional approach of staffing a team of engineers for a year to do the UI conversion. Guhan's framing: "We can't go and rebuild... 45-50 million lines of code... that's not where we want to go." Selva on leadership pressure: "Because you can always see where we are getting direction from the top is 10 screens, now there are 10 people. We are being asked to think differently. And I think we have to. So that's why the AI, your expertise needed."

BayOne is the AI-accelerated alternative. The POC exists to prove that an agent-driven approach can convert the EPNM UX to Angular at a rate that outperforms traditional staffing, with quality guarantees that match or exceed what manual QA would catch. If the POC succeeds on the two chosen screens, the full engagement scales to the rest of the product surface (reported as 200-250 workflow screens in total).

The POC is one person — Colin Moore, BayOne's Director of AI — working solo on both UI and backend (to whatever narrow extent backend work is needed). The full engagement would scale to Colin plus approximately three additional engineers.

---

## 6. Who the Stakeholders Are at a Glance

- **Guhan.** Senior Cisco engineering leader. Decision-maker for this engagement. Leads the Provider Connectivity area. Delegates operational coordination to Selva.
- **Venkat.** Cisco leader above Guhan. Executive sponsor. Advocates for AI-generated code broadly. Exploring whether the work can target a July or August delivery.
- **Selva Subramanian.** Cisco engineering / product lead. Operational counterpart for BayOne. US-based. Runs the working rhythm, schedules sessions, coordinates access, makes day-to-day scope calls.
- **Praveen Kumar Vangala.** Cisco engineering team lead (India-based). Manages the tech leads. Organized the 2026-04-06 walkthrough. Likely the person referred to as "Varel" in the earlier Sets when speech-to-text garbled his name.
- **Cisco tech leads** (India-based unless noted): Akhil Francis (led the product walkthrough), Ramesh Dhashnamoorthy (US-based, asks rigorous AI-compliance and QA questions), Ramkrishna Galla (architecture narrator, senior technical voice), Aadit Vaidyanathan, Jenis Dharmadurai (fault management specifics), Senthilkumar Palaniyandi.
- **Colin Moore.** BayOne Director of AI. Running the POC. Cisco laptop and Cisco ID already issued. Precedent experience on the concurrent NX-OS CI/CD engagement with Srinivas Pita and Anand Singh.
- **Neha Malhotra.** BayOne engagement management. Day-to-day operational partner to Colin.
- **Rahul Bobbili.** BayOne president. Executive oversight, accountability for Colin's responsiveness.
- **Zahra Syed.** BayOne Director, Strategic Accounts. Account-level ownership on the business side.

Detail on all stakeholders, roles, and dynamics is in `07_stakeholders_and_organization.md`.

---

## 7. The Working Model in One Paragraph

The Cisco engineering team is resourced on a critical release path for their own product and cannot invest significant time in the POC. BayOne works independently after initial context transfer, with periodic checkpoints for progress and questions. All work happens on Cisco-issued hardware with Cisco-issued accounts. Only two AI tools are permitted: Cisco-issued Claude Code for development and LangGraph running locally on the Cisco laptop for orchestration. No external cloud AI tools. Library installations are gated through Colin as the single authorized gatekeeper. The Cisco team has prepared a Confluence page with user guides, API documentation, meeting recordings, and the complete repository list, and will add Colin to the Active Directory groups that unlock repository and VM access. Communication day to day runs through a WebEx team space and email; escalations or delays flow through Selva and Neha. Detail in `11_ways_of_working.md` and `08_repositories_access_and_compliance.md`.

---

## 8. What the Execution Session Should Take from This Document

Three things carry through every subsequent decision:

1. The scope is bounded. Two screens. Classic view toggle. Backend untouched. Production-quality output. Any proposal to expand beyond that needs to come back to Colin before acting.

2. The target is not novelty. It is fidelity. The visual and interaction patterns of the EPNM screens must be faithfully reproduced in Angular, themed to look and feel like EPNM, behind the same EMS backend the new UX already calls. A customer should not be able to tell whether the classic view they are using is the original Dojo-based EPNM or the new Angular-based classic view. That is the bar.

3. This POC is the proof point for a much larger engagement, but that engagement is not the execution session's concern. Deliver the two screens, prove the approach, document the patterns cleanly enough that scale is straightforward. Scale is a separate conversation that happens after the POC lands.
