# Chapter 1 — Discovery

## Overview

Discovery is the phase of work that precedes the central recorded execution phase of the engagement. It encompasses everything that had to happen before a disciplined handoff package could be assembled: first contact, scoping conversations, proposal iteration, methodology presentation, relationship-building, a consequential scope reframe, technical context-gathering, and the initial architectural walkthrough with the Cisco engineering team. Discovery produced the strategic shape of the work, the technical orientation necessary to operate inside Cisco's product surface, and the behavioral commitments that defined how the work would be executed.

The chapter treats discovery as a single coherent grouping rather than a sequence of granular phases. The substance of discovery is what it produced, not the calendar mechanics by which it was produced. What follows is an account of that substance: the customer problem, the reframes that locked the final scope, the two products in view, the strategic posture taken, the quality-assurance posture articulated, the working-model constraints accepted, the architectural walkthrough with the engineering team, and the behavioral commitments that emerged.

## How the Engagement Began

Contact with Cisco came through an internal referral. A Cisco engineering leader in the Provider Connectivity area had expressed interest in an AI-accelerated approach to a long-standing user-interface problem on one of the organization's flagship network-management products. A referral source inside Cisco identified BayOne's AI practice as a plausible partner, and a first meeting was arranged on-site at Cisco offices.

The first meeting was exploratory. The tone was collegial. Conversation moved organically from introductions into the business problem. The Cisco side described a legacy network-management product with customers who were resistant to a new user experience on its modernized successor. The framing offered at first contact was already oriented toward an AI-accelerated alternative to traditional staffing: the Cisco engineering leader explicitly rejected the approach of staffing ten engineers for a year as the means of reproducing missing functionality, and asked whether an agent-driven development posture could do the work faster, at quality, and with strategic guidance rather than raw implementation labor.

During that first meeting the engagement model was sketched: a proof-of-concept delivered on Cisco-issued hardware, under Cisco's AI-compliance regime, with one BayOne technical lead running the work end-to-end. A second meeting was scheduled for later the same day with a Cisco team lead, so that the technical details underneath the business framing could be explored more deeply. That same-day follow-up established a pattern that persisted through discovery: the Cisco side was action-oriented and willing to accelerate, provided BayOne could match the pace with substantive material.

The POC was framed as an investment rather than a commercial transaction. Commercial mechanics around that framing are out of scope for this documentation; what matters methodologically is that discovery could proceed with a tight focus on technical outcomes without commercial negotiation consuming the working time.

## The Customer Problem

The problem the customer brought to the table was not a missing-feature problem. It was a user-experience problem with operational and commercial consequences.

Customers running the legacy network-management product had roughly a decade of accumulated operator muscle memory on its user interface. Network operations teams had trained on the legacy experience, built integrations around it, and adopted workflows that assumed its specific visual and interaction patterns. When Cisco shipped a modernized replacement with a redesigned user experience on a newer technology stack, operator reaction was negative. Multiple customer escalations surfaced asking for a transition path back to the legacy experience, at least for some release window while operators acclimated to the new one.

The customer framing was explicit. Operators did not want to learn an entirely new interface on the same timeline they were being asked to adopt new underlying product behavior. The request was for the option to toggle between the classic and the modern experience for a release or two — long enough to absorb the operational change without also absorbing the interaction-model change. Over time, the modern experience would become the only experience, and the classic view would be deprecated. The classic view was explicitly temporary: a comfort bridge, not a permanent dual experience.

There was a commercial dimension underneath the user-experience framing. Cisco wanted customers to migrate to the modernized product for renewal and roadmap reasons. Without a comfort bridge, customers resisted the migration. With a comfort bridge, customers could move onto the new product and gradually absorb the new interface on a schedule their operators could tolerate. The classic view toggle is, in that sense, a migration mechanism as much as it is a user-experience accommodation. Retirement of the legacy product depends on customers being willing to move; customers are willing to move if they are not forced to change every habit simultaneously.

Discovery established this framing clearly enough that every downstream scope and design decision could be evaluated against it. The POC is not a novelty exercise. It is a fidelity exercise in service of a migration strategy.

## The Products in View

Two products anchor the engagement. Discovery established what each one is, how they relate, and where the POC sits inside that relationship.

### EPNM — Evolved Programmable Network Manager

EPNM is Cisco's long-standing network-management product. Customers have been running it for roughly a decade. Its frontend is built on the Dojo 1.x framework; the backend is a Java monolith; the database is Oracle. The product collects device information from the network through SNMP and CLI polling, parses that information into an internal data model, persists it to Oracle, and renders it through Dojo- and Dijit-based user-interface components. The visual theme is blue-and-white. The product spans inventory, topology, fault management, service-level reporting, performance monitoring, software-image management, and related functional areas.

EPNM's codebase is distributed across several repositories that together implement the product surface:

```
EPNM (conceptual repository layout)
├── Prime framework (Dojo-based core framework)
├── Wireless framework
├── Assembly (inventory UI)
├── ChassisView
└── Fault management (including wireless fault repositories)
```

The legacy codebase is the source of truth for the product's behavior. No design documentation covering EPNM's user interface exists in a form that can substitute for the code itself. Over a decade of sustained development, the code has undergone what the Cisco team described as "surgery" — repeated modification in place — which rules out any direct port of files from one codebase to another as a viable conversion strategy. Conversion work, where it happens at all, is against the observable behavior of the running application, with the code as the reference.

### EMS and Crosswork Network Controller

The modernized product is referred to as EMS, the Element Management System component of Cisco's Crosswork Network Controller platform. EMS uses Angular 21 on the Harbor and Magnetic design system for its frontend, a Spring Boot primary backend with some Go services on the device-management side, and PostgreSQL instead of Oracle. Oracle has been fully eliminated from EMS; device images are stored as application assets rather than database BLOBs.

EMS follows a three-layer shell-app model:

```
EMS UI (feature pages)
  └── Common UI (shared reusable components: cards, tables, widgets)
        └── Infra UI (outer shell: header, navigation, login, layout frame)
```

EMS was not migrated from EPNM. It was independently reimplemented on the newer stack. The two products cover overlapping conceptual territory — inventory, faults, events, device management — with different user experiences, different technology stacks, and different backends. Backends are not shared.

A figure reported during the architectural walkthrough puts approximately eighty percent of the legacy backend's functionality as having been reimplemented on the EMS stack. The remaining ten to twenty percent represents a gap whose specifics are expected to emerge during implementation-level investigation. Gap detection is accordingly built into the POC as a first-class concern rather than a late-phase surprise.

### How the Two Products Relate to the POC

The POC targets the overlap: areas of functionality that exist in EPNM and also exist in EMS, where the difference between the two is primarily visual and interaction-level rather than functional. Two screens are in scope for the POC — Inventory and Fault Management. Both areas exist in both products. The POC rebuilds the EPNM-style user experience in Angular and wires it to the EMS backend, rather than reimplementing missing EPNM functionality on the EMS side.

## The Scope Evolution

One of the most important outcomes of discovery was a scope reframe that changed the fundamental shape of the work. Earlier conversations had treated the engagement as a full-stack vertical conversion: for each missing area of functionality in the modernized product, the POC would port the legacy frontend and backend together onto the new stack. The opening framing was oriented around missing reports and missing device coverage, with the premise that where a frontend screen was absent, the corresponding backend capability was also absent.

That framing was explicitly reversed in a subsequent working meeting. The Cisco operational counterpart opened the conversation by acknowledging that the earlier framing had not been clear, and corrected the direction: the POC's target areas already existed in the modernized product. They had a backend. They had a user interface. What had changed between the legacy and the modernized product was the user experience — the visual design, the interaction patterns, the workflow — not the underlying capability.

The implication of the reframe was decisive. The POC was not a conversion of missing functionality. The POC was a user-experience overlay on screens that already existed in the modernized product. The backend was off-limits. The frontend was the subject.

The reframe settled several questions at once:

- **Included.** A classic-view toggle on existing modernized-product screens. A frontend rebuild that reproduces the legacy user experience in the modern stack. Wiring of the rebuilt user interface to the existing backend services of the modernized product.
- **Excluded.** Backend reimplementation. The decision was stated emphatically on the Cisco side. Two reasons were cited explicitly: the effort required, and the maintenance burden of carrying two backends forward. A narrow exception was allowed for API-level touchup — widening or narrowing a query scope, adding a filter parameter, similar surgical adjustments on the backend where the existing service boundary was slightly off for the classic-view needs. Anything larger than narrow API adjustment was out of scope.
- **Excluded.** Missing functionality work. The POC was no longer about filling gaps in the modernized product. Coverage gaps between the legacy and modern products were acknowledged to exist and would be a focus of the larger engagement, but were not the POC's concern.

A single-sentence synthesis from the Cisco side captured the reframe: the POC is forking the user interface; the backend is consistent between the two variants; the difference is the look and feel.

The scope reframe locked the final shape of the POC. Everything downstream in discovery — the architectural walkthrough, the technical research, the handoff-package design — took the reframe as its anchor. The classic view is a UX overlay. The backend is not rewritten. Two screens are in scope. The toggle is per-screen for the POC. The classic view is the default on login.

### The Two-Screen Scope

The scope reframe confirmed two screens — Inventory and Fault Management — as the POC target. During the architectural walkthrough with the Cisco engineering team, each screen was mapped to a concrete set of sub-screens.

```
POC Scope
├── Inventory (Part 1)
│   ├── Network Devices list
│   ├── Device Details
│   │   ├── Chassis View (left pane)
│   │   └── Left-menu sub-views
│   │       ├── System Summary
│   │       ├── Device Details
│   │       ├── Chassis
│   │       └── Enrollment
│   ├── Device 360
│   │   └── Tabs: Alarms, Modules, Interfaces, Location, Recent Changes
│   └── Interface 360 (nested, launched from the Interfaces tab of Device 360)
└── Fault Management (Part 2)
    ├── Alarms table
    │   ├── Columns, quick filter, advanced filter
    │   ├── Expandable rows
    │   ├── Clear-alarm action
    │   ├── Correlated alarms
    │   └── 360-view link
    ├── Most-recent-events popup
    ├── Full events page (past-eight-hours default window)
    └── Syslogs
```

Inventory was designated Part 1. Fault Management was designated Part 2. The delineation is substantive rather than cosmetic — the two areas have different visual languages in the legacy product, different data sources in the modern product, and different behavioral expectations around real-time updates, filtering, and correlation. Treating them as two parts ensured that scope remained legible throughout execution and that acceptance could be evaluated per area.

## Strategic Approach

Several strategic commitments emerged during discovery. They are the posture that made the rest of the work coherent, and they are the posture the execution phase inherits.

### Fidelity Over Novelty

The target is not a new user experience. The target is faithful reproduction of the legacy user experience on the modern technology stack. An operator should not be able to tell, looking at the classic view, whether they are using the original legacy application or the reproduced classic view inside the modern product. Visual pattern, interaction pattern, workflow shape — all reproduced. The bar is deliberately not creativity, and deliberately not improvement. It is faithfulness. Any urge to "fix" a legacy pattern during conversion is treated as an expansion of scope and is resisted on that basis.

Fidelity over novelty is a discipline. It aligns the work with the customer problem (operator comfort during a transition period) rather than with implementer preference. It simplifies acceptance testing (both views, same backend, same observable result on identical inputs). It forecloses unproductive design debates during execution.

### Customer Transparency

The POC is produced using AI-assisted development, but the artifact customers see is the classic view itself. The method of production is not customer-facing. Customer communication about the transition — how it works, when it will be available, what the toggle does — is Cisco's to handle. BayOne does not communicate with end customers. This boundary simplifies the engagement and keeps narrative control with the product owner.

### Comfort Bridge Framing

The classic view is explicitly a comfort bridge. It exists to ease a migration, not to become a permanent dual experience. An external analogy was used during discovery to anchor this framing: the pattern seen in productivity applications and consumer banking applications where a new user experience ships alongside an old one, with a toggle allowing users to defer the transition on their own schedule, and the old experience eventually removed. The lifecycle the classic view toggle serves is a four-stage arc: the current state with the new experience only and resistant customers; the target state with the toggle shipped; the transition period during which customers use the bridge; and the end state with the classic view deprecated and removed.

This framing matters methodologically because it constrains the ambition of the work. The classic view does not need to evolve. It does not need feature development. It needs to be faithful, stable, and quietly retirable. Scope decisions are evaluated against that eventual deprecation — anything that would make the classic view harder to remove later is counted as a negative.

### Exponential-Decay Reasoning on Conversion Effort

A reasoning pattern articulated during discovery shaped the expectations around how the work would scale from the POC into the larger engagement. Agent-driven conversion work has an up-front investment cost that is not proportional to the scope of the first output. Environment setup, pattern establishment, library installation, shared component extraction, service-layer adapters, the theme-toggle infrastructure itself — these are largely one-time costs that the first converted screens bear, and that subsequent screens inherit.

As a consequence, the effort per screen is not linear. Early screens are slow. Subsequent screens are progressively faster because they reuse established infrastructure and reuse patterns already mapped between the two technology stacks. The decay is roughly exponential: the curve flattens as the set of infrastructure decisions stabilizes, after which additional screens are incremental applications of the established patterns rather than fresh investments.

The methodology consequence of this reasoning is twofold. First, the POC scope is chosen so that meaningful infrastructure is established during the POC itself — not so small that infrastructure never gets exercised, and not so large that the POC consumes scale work. Second, linear extrapolation from POC duration to larger-engagement duration is explicitly cautioned against. The POC is a disproportionately front-loaded effort; scaling projections must account for the decay curve.

## Quality Assurance Posture

Quality assurance was treated as a first-class concern from the first working meeting. The Cisco side raised, directly and repeatedly, the question of how domain gaps and functionality gaps would be detected and surfaced. The answer articulated during discovery had several layers and is the posture the rest of the work inherits.

### Multi-Layer Verification

Verification is not a single activity. It is a stack of activities, each of which catches different kinds of deviation:

1. **Meta-analysis of test coverage by a judge layer.** A layer whose responsibility is evaluating whether the test coverage produced by the implementation work is itself sufficient — covering the right behaviors, exercising the right edge cases, detecting its own gaps.
2. **Visual comparison that works without a running application.** Automated visual testing that can evaluate rendered output of the classic view against reference images of the legacy application. Not contingent on having both applications live side by side; functions against captured references.
3. **Peer-to-peer gap analysis between autonomous agents.** Multiple agents exchanging observations about coverage and surfacing disagreements as candidate gaps. Autonomous sub-agent spawning is part of the pattern — when an agent identifies a zone that requires deeper investigation, the investigation is delegated to a focused sub-agent rather than absorbing the parent agent's attention.
4. **Human categorical review as the last line of defense.** Not line-by-line review of code. Categorical review — does the produced output, at the level of screen behavior, match the expected behavior of the legacy product. Reserved for items the preceding layers cannot be trusted to catch.

### Gap Detection as a First-Class Concern

The eighty-percent reimplementation figure for the modernized product's backend is not a number to be taken on faith during implementation. The ten-to-twenty-percent gap is where implementation risk concentrates. Gap detection — surfacing where a legacy screen depends on behavior the modern backend does not yet support — is part of the POC's deliverable scope, not an afterthought handled if time permits. The posture articulated during discovery is that gaps are surfaced quickly, documented cleanly, and treated as information for the Cisco side to act on rather than as problems to be worked around silently. Silent workarounds are explicitly rejected. Honest surface of uncertainty is explicitly required.

### POC-Scoped Testing Versus Engagement-Scoped Testing

A distinction was drawn during the architectural walkthrough that affects how the POC's quality-assurance commitments are structured. The full Cisco testing infrastructure covers seven categories — functional, scale, end-to-end, UI, API, migration, upgrade — with thousands of data-driven test cases across device types and configurations. The existing UI tests are not transferable to the classic view: the DOM is different under Angular, the selectors will not match, and Dojo-specific patterns do not survive the rebuild. Replicating the existing UI test suite for the classic view is acknowledged as necessary work, but belongs to the larger engagement, not the POC.

The POC's testing scope is narrower: enough automated testing to guarantee functional equivalence between the classic view and the modern view on the two screens, plus internal unit testing before the POC is declared complete. Full agentic QA infrastructure, dashboard visibility, and coverage-gap instrumentation are deferred to the larger engagement. The distinction preserves discipline. The POC's testing demonstrates the approach without consuming scale work.

## Working Model

Discovery established the operating constraints under which the work would actually be performed. These constraints shaped every methodology decision that followed.

### Constrained Customer-Team Bandwidth

The Cisco engineering team is resourced on a critical release path for their own product. They cannot invest significant synchronous time in the POC. The working model accepted during discovery is that BayOne operates independently after initial context transfer, with periodic checkpoints for progress and clarification. Questions are batched rather than nibbled at. Working sessions are efficient. Asynchronous coordination is the default; synchronous calls are scheduled into the narrow overlap window between time zones only when a decision genuinely requires it.

The practical consequence is that the engagement cannot depend on calendar meetings for information. Information has to be extracted from artifacts — the repositories themselves, documentation the team has prepared, recordings and pointers they provide — and turned into a working reference that the execution phase can consume. The research-and-reference-building practice that appears later in the methodology is a direct response to this constraint.

### Asynchronous Coordination

The WebEx team space established during discovery is the primary asynchronous channel. Email is a secondary channel for code pointers, repository links, and artifacts that need a retrievable record. A recurring synchronous cadence was planned but scoped to decisions and clarifications, not routine status.

### Agent-Driven Codebase Exploration Over Calendar Meetings

A central methodology posture emerged during discovery: when a question about the codebase can be answered by reading the codebase, reading the codebase is the first move, not scheduling a meeting. Codex — the AI-assisted development tool — is used to explore, analyze, and produce structured references for both products. Meetings are reserved for decisions, clarifications, and things the code genuinely does not answer (design intent, historical context, future direction). This posture aligns with the bandwidth constraint on the customer side and with the exponential-decay reasoning on conversion effort: investment in structured codebase exploration early pays off throughout execution.

### Library-Install Gating

Library installations on the Cisco machine are gated. One authorized gatekeeper approves each library addition. This is not a bureaucratic overlay — it is part of the AI-compliance posture. Third-party dependencies are the most common vector for both security exposure and for quiet scope expansion. Gating them forces each addition to be justified, which keeps the dependency tree narrow and keeps the classic view's build-time footprint inside the existing modernized-product build.

### AI-Compliance Constraints

The Cisco side operates under specific constraints for how AI tools may be used on their code. Discovery surfaced and accepted these constraints as non-negotiable:

- All work is performed on the Cisco machine. The engagement is treated as single-venue. No transfer of information off the Cisco machine.
- Cisco-issued AI tools only. Two tools are approved: the Cisco-issued Codex build for development, and a locally-running orchestration framework for multi-agent coordination. No external cloud AI tools.
- Cisco-issued accounts only. Personal accounts and personal licenses are not permitted.
- Non-disclosure agreement in place.
- Repository access is provisioned through Active Directory groups, gated by Cisco's standard access-control mechanisms.

These constraints were accepted without friction because they were a precondition for the engagement to happen at all. The methodological consequence is that all of the work described later in the documentation — the repository analysis, the handoff package, the execution preparation — had to be designed to operate under these constraints from the first line of code.

## The Architectural Walkthrough

The architectural walkthrough with the full Cisco engineering team was the point at which the conceptual framing established in earlier working sessions met the running products and the actual repositories. It was the first time both products were observed running, the first time the repository layouts were mapped, and the first time the AI-compliance posture was ratified collectively with the engineering team that would be working alongside the POC.

The walkthrough was attended by the engineering leads responsible for Inventory, Fault Management, architecture, compliance, and test — together with the operational counterpart on the Cisco side and the engagement team on the BayOne side. The structure of the session was presentation followed by repository traversal: the lead for each area walked through the relevant user-interface screens in the running product, then opened the corresponding repository and explained the code layout.

### Confirmation of Scope

The two screens in scope — Inventory and Fault Management — were each walked through on the live product. Sub-screen inventory was confirmed to match the scope captured earlier: Network Devices list, Device Details with Chassis View and left-menu sub-views, Device 360 with its tab set, and Interface 360 as a nested 360 inside Device 360 for the Inventory area; alarms table with filters and expandable rows, correlated alarms and clear-alarm action, a most-recent-events popup, a full events page with the past-eight-hours default window, and syslogs for the Fault Management area.

### Repository Layout

The repository layouts for both products were traversed during the walkthrough. The legacy product's repositories were identified: the Prime framework repository for the Dojo-based core, the wireless framework repository, the assembly repository containing the inventory user interface, the ChassisView repository, and the fault-management repositories. The modernized product's repositories follow the three-layer shell-app structure: the infra-UI repository for the outer shell, the common-UI repository for shared components, and the EMS-UI repository for feature-specific pages. A set of supporting backend repositories — Spring Boot services, Go services on the device-management side — sit behind the user-interface layer.

### Shell-App Architecture

The three-layer shell-app model of the modernized product was explained in detail during the walkthrough. The classic view must integrate into this model. The specific question of where the classic-view code lives — inside the EMS-UI repository as a subtree, or as a separate repository loaded by the shell — was left as a decision for the execution preparation phase, with a commitment on the BayOne side to produce a code-organization proposal for review.

### Backend Coverage

The approximately-eighty-percent backend reimplementation figure was stated during the walkthrough. The remaining gap is acknowledged to exist. Characterizing that gap screen-by-screen is part of the POC's work. The figure is treated as an observation (the team's own assessment of where they are) rather than a validated conclusion (a coverage audit has not been performed in the form the POC would require). Treating the figure with observational discipline rather than treating it as a firm contract is part of the quality-assurance posture.

### Default View and Toggle Behavior

Two behavioral commitments were confirmed during the walkthrough that govern how the classic view appears to users:

- **Default on login is the classic theme.** Once logged into the Crosswork user interface, the default rendering is the legacy blue-and-white, Dojo-style layout. The toggle flips the page to the modernized Magnetic-designed appearance. This is the reverse of a naive expectation. It aligns with the comfort-bridge framing: operators opening the product land first in the experience they recognize.
- **Toggle is per-screen for the POC.** Each targeted screen has its own embedded toggle control. The global, product-level toggle — a user-setting preference that flips the entire application at once — is explicitly deferred to the larger engagement. The POC demonstrates the approach; the product-phase work generalizes it.

### Action Items

The walkthrough produced a set of action items covering access provisioning (Active Directory group membership, VM provisioning for an inventory-ready legacy environment and a development-ready modern environment), communication setup (the WebEx team space), documentation review (the Confluence page the Cisco team prepared with user guides, API documentation, meeting recordings, and the repository list), and substantive deliverables (the code-organization proposal on the BayOne side, the code-pointer and repository-link email on the Cisco side, identification of the regression suite relevant to the two screens, and a recurring sync cadence). The action items sit across both sides and establish the interface between the two teams for the execution phase.

## Core Behavioral Commitments

Discovery produced a small number of behavioral commitments that structure the work. They are not implementation details. They are the rules under which implementation decisions are made.

- **No backend rewrites.** The classic view consumes the same REST APIs the modernized user interface consumes. Presentation-layer differences are adapted on the client side through display adapters, not backend changes. A narrow exception for API-level touchup — a filter parameter added, a query scope adjusted — is permitted where the existing service boundary is slightly off for the classic-view needs. Anything larger is out of scope and must be surfaced before acting.
- **Classic view is the default on login.** Users land first in the legacy-style experience. The modernized appearance is behind the toggle.
- **Toggle is per-screen for the POC.** Global toggle behavior is explicitly deferred. The POC demonstrates the pattern; the pattern generalizes later.
- **Production-quality code is the bar.** The POC is not a prototype in the throwaway sense. The classic-view feature will ship to customers. The code produced during the POC must be production-grade from the start. The POC demonstrates the approach on two screens before scaling; it does not produce disposable work that scale must rewrite.
- **Functional equivalence is the acceptance test.** Both views share the same backend. The same action in either view must produce the same result. Acceptance testing validates this.
- **Fidelity, not improvement.** The classic view reproduces the legacy experience faithfully. Design improvements — even ones that would plainly help an end user — are counted as scope expansion and resisted.
- **Honest surface of uncertainty.** Gaps, ambiguities, and points where the reference material is thin are surfaced cleanly to the Cisco side. Silent workarounds are rejected.

## The Outcome of Discovery

Discovery concluded with the engagement in a state where the handoff package could be assembled. Concretely, discovery produced the following outputs that the next phase consumed directly:

- A clear statement of the customer problem and the strategic role of the classic view inside Cisco's migration plans.
- A locked POC scope — two screens, classic-view toggle on the modernized product, backend untouched, production-quality code.
- A characterization of both products sufficient for the execution phase to orient: technology stacks, repository layouts, shell-app structure, backend coverage level.
- A quality-assurance posture: multi-layer verification, gap detection as a first-class concern, POC-scoped testing distinguished from engagement-scoped testing.
- A working model accepted by both sides: constrained customer-team bandwidth, asynchronous coordination as the default, agent-driven codebase exploration as the first move, library-install gating, single-venue AI compliance.
- A set of behavioral commitments binding on the work: no backend rewrites, classic-view default on login, per-screen toggle, production-quality output, fidelity over novelty, honest surface of uncertainty.
- An action-item set covering access provisioning, communication setup, documentation review, and substantive deliverables that would be worked in parallel with the handoff-package preparation.

At this point the engagement had enough context, enough scope discipline, and enough alignment between the two sides to pivot from discovery and scoping into the production of a structured handoff package. The orientation was complete. The shape of the work was agreed. The constraints were understood. What remained was to produce, in a form the execution phase could consume directly, the assembled context that discovery had generated — the structured reading of both products' repositories, the cross-product mapping, the conversion-pattern reference, the numbered handoff documents, and the primers that would let the execution sessions start work without re-deriving the reasoning behind the scope. That production is the subject of the next chapter.
