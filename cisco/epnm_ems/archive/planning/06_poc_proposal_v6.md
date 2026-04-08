# EPNM to EMS UI Conversion: Proof-of-Concept Proposal

**Prepared by:** BayOne Solutions
**Author:** Colin Moore, Director of AI
**Date:** March 2026
**For:** Guhan, Selva, Cisco EMS Team

---

## Executive Summary

BayOne Solutions proposes a four-week proof-of-concept engagement to demonstrate AI-assisted conversion of EPNM screens to the EMS platform. This engagement will deliver 2-3 fully converted screens, including both frontend UI and supporting backend logic, using a methodology designed to accelerate with each subsequent screen.

BayOne is providing this proof-of-concept at no cost to Cisco. The infrastructure developed during this engagement (codebase analysis, custom conversion agents, validated patterns) will serve as the foundation for any subsequent paid engagement. This approach allows Cisco to evaluate BayOne's capabilities against actual codebase requirements before committing to a larger engagement.

---

## Problem Statement

Cisco seeks to migrate functionality from EPNM to EMS. This migration presents architectural complexity beyond typical UI modernization efforts, requiring extraction of tightly-coupled functionality from a monolithic system and re-implementation within a microservices architecture.

### Success Criteria

This proof-of-concept will be considered successful if:

1. Two to three representative screens are fully converted and functional in the EMS environment
2. Backend logic supporting these screens is implemented or integrated with existing EMS services
3. Automated visual validation confirms behavioral equivalence with EPNM
4. A documented pattern library enables estimation of remaining conversion scope
5. A staffing and velocity model supports planning for full-scale engagement

---

## Proposed Approach

### Phase 1: Exploration and Onboarding

**Duration:** Approximately two weeks from code access
**Deliverable:** Analysis document with categorized screens and recommended POC candidates

Before conversion work begins, BayOne will conduct systematic codebase analysis using AI-assisted exploration to develop a structured understanding of the EPNM architecture.

**Codebase Analysis**

BayOne will use Claude Code for initial exploration, mapping module boundaries, identifying service dependencies, tracing data flows, and cataloging UI patterns. This analysis will produce:

- Screen inventory and categorization (data entry forms, dashboards, reports, configuration wizards, real-time monitoring views)
- Dependency graphs identifying which screens share backend services
- Complexity indicators distinguishing screens with heavy cross-dependencies from relatively self-contained ones
- Pattern identification documenting recurring UI structures and their backend correlates

**Collaborative Screen Selection**

Cisco's team possesses context that cannot be derived from code analysis alone: which screens customers prioritize, which have been historically problematic, and which represent typical versus edge-case complexity.

BayOne proposes that Cisco SMEs identify candidate screens based on business priority, with BayOne validating technical feasibility based on codebase analysis. This shared ownership of scope decisions protects both parties: Cisco is not bound by assumptions made without business context, and BayOne is not committed to screens that prove to be outliers.

**Selection Criteria**

Ideal POC candidates are screens that:

- **Represent** the broader conversion challenge rather than edge cases
- **Are sufficiently self-contained** to convert without extensive system dependencies
- **Do not yet exist in EMS** so this work adds value rather than duplicating effort
- **Are complex enough** to demonstrate meaningful capability

BayOne cannot make informed recommendations until codebase exploration is complete. The exploration phase will surface dependencies, gaps, and complexity factors that are not visible from documentation or discussion alone. Some findings will require Cisco's input and direction before screen selection can be finalized. BayOne will recommend 2-3 screens with supporting rationale; Cisco will review these recommendations, provide guidance on any flagged gaps, and select which screens proceed to Phase 2.

### Phase 2: Conversion, Testing, and Acceptance

**Duration:** Approximately two weeks from screen selection
**Deliverable:** Working screens in EMS, documented conversion patterns, estimation model

BayOne will use Cisco-provided Claude Code with purpose-built skills and sub-agents for conversion work. The workflow follows a structured approach: analysis, planning, execution, and validation, with each step producing documented outputs. As conversion proceeds, BayOne builds a pattern library specific to this codebase that accelerates subsequent screen conversions.

Visual validation uses Playwright for automated testing, capturing baseline screenshots from EPNM and comparing against converted EMS screens to confirm functional equivalence.

Where EPNM functionality does not convert cleanly (missing EMS services, API gaps, UX constraints), BayOne will document these gaps explicitly for Cisco to address during or after the POC.

---

## Scope and Timeline

### POC Scope

- **Screens:** 2-3 representative screens, selected collaboratively following Phase 1 analysis
- **Depth:** End-to-end conversion including backend logic, not limited to UI translation
- **Validation:** Automated visual comparison, functional testing, gap documentation
- **Deliverables:** Working code, documented patterns, estimation model for remaining screens

### Timeline

**Total Duration:** Four weeks from code access

| Week | Phase | Activities |
|------|-------|------------|
| 1-2 | Exploration and Onboarding | Codebase analysis, screen categorization, candidate selection with Cisco team |
| 3-4 | Conversion, Testing, and Acceptance | Convert selected screens, develop pattern library, validate and document |

The timeline begins upon receipt of repository access. Some Phase 1 activities (initial conversations with Cisco SMEs regarding screen priorities, understanding categorization criteria) can proceed before hardware delivery.

### Exclusions

- **Additional screens beyond agreed scope.** BayOne will provide an estimation model for extrapolation, but the POC itself is bounded to 2-3 screens.
- **New EMS backend services.** If a screen requires backend functionality that does not exist in EMS, BayOne will document the gap. Building new microservices falls within paid engagement scope.
- **Production deployment.** POC deliverables consist of working code demonstrated in a development or test environment.

---

## Investment Model

### Proof-of-Concept (This Proposal)

- **Cost to Cisco:** None
- **Deliverables:** 2-3 fully converted screens, pattern library, gap documentation, estimation model
- **Foundation:** Codebase analysis, conversion agents, and validation infrastructure developed at BayOne's investment

### Paid Engagement (Upon Cisco Approval)

- **Model:** Outcome-based engagement
- **Scope:** Determined collaboratively based on POC findings and Cisco priorities
- **Foundation:** All POC infrastructure transfers directly
- **Estimation:** Reliable projections available after Phase 1 analysis

---

## Assumptions and Dependencies

### Assumptions

1. EPNM and EMS codebases are accessible via standard repository mechanisms
2. Cisco SMEs will be available for periodic consultation during Phase 1 (estimated 2-3 hours total)
3. EMS development environment is available for deployment and validation
4. Selected POC screens have existing backend services in EMS or gaps can be documented and deferred

### Dependencies

1. Cisco hardware delivery (laptop in progress)
2. Repository access provisioning
3. Cisco approval of screen selection following Phase 1 analysis

---

## Risk Factors

| Risk | Mitigation |
|------|------------|
| Selected screens have undocumented complexity | Phase 1 analysis and collaborative selection reduce this risk; scope adjustments possible with mutual agreement |
| Backend services do not exist in EMS | Gap documentation is an explicit deliverable; building new services is out of scope for POC |
| SME availability constraints | Phase 1 can extend if necessary; this does not affect Phase 2 timeline once screens are selected |
| Codebase access delays | Phase 1 conversations can begin prior to repository access |

---

## Security and Access

Per prior discussions:

- All work will be performed on Cisco hardware (laptop delivery in progress)
- All AI tooling will use Cisco-licensed instances (Claude via Cisco-approved channels)
- No code will leave Cisco infrastructure
- NDA is already executed

BayOne is already onboarded for the CI/CD engagement with Anand's team. The same security posture applies to this engagement.

---

## Next Steps

1. **Hardware delivery:** Expected on 3/18
2. **Initial context:** If Cisco's team can identify candidate screens before code access is available, Phase 1 conversations can begin early
3. **Repository access:** Once hardware is ready, BayOne will require access to EPNM and EMS codebases
4. **Kickoff:** Brief synchronization to align on priorities and introduce BayOne to relevant SMEs

BayOne will deliver preliminary analysis within the first two weeks of repository access. Screen selection will follow collaboratively, with conversion execution proceeding immediately thereafter.
