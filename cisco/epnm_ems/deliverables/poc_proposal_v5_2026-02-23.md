# EPNM to EMS UI Conversion: Proof-of-Concept Proposal

**Prepared by:** BayOne Solutions
**Author:** Colin Moore, Director of AI
**Date:** February 2026
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

**AI-Assisted Conversion Tooling**

For this proof-of-concept, BayOne will use Cisco-provided Claude Code with purpose-built skills and sub-agents for exploration and conversion work. This approach provides structured automation with appropriate human oversight at POC scale, where patterns are still being discovered and validated.

The workflow models how experienced engineering teams approach conversion systematically:

- **Analysis:** Each EPNM screen is examined holistically, mapping data flows from UI through service layer, identifying backend dependencies, and determining EMS service integration points. Where gaps exist, they are documented immediately.

- **Planning:** Based on analysis, implementation is planned by identifying specific translation patterns (such as Dojo widget structures to Angular component equivalents), flagging areas requiring custom logic, and designing component structure and service integration.

- **Execution:** Conversion proceeds with sub-tasks for component implementation, service integration, and test creation. Work is coordinated through structured handoffs rather than ad-hoc effort.

- **Validation:** A quality gate reviews output against specification, validates behavioral equivalence, and catches gaps before they propagate. Work can be halted and redirected if standards are not met.

The tooling has access to capabilities beyond conversation: codebase search, static analysis, prototype implementation, and test execution. Each step produces documented outputs that inform subsequent work and enable traceability.

For larger engagements beyond the POC, BayOne employs a LangGraph-based multi-agent architecture. This enables fully autonomous coordination across parallel work streams, with agents dynamically spawning sub-tasks and self-managing gap resolution. The foundations established during the POC transfer directly to this scaled model.

**Pattern Library and Knowledge Base**

As exploration and conversion proceed, BayOne builds a comprehensive knowledge base specific to this codebase: a traceable, continuously refined understanding of the system that grows with every screen analyzed.

The knowledge base captures:

- **Conversion patterns:** Documented mappings between EPNM constructs and EMS equivalents, including nuances and edge cases discovered during implementation
- **Test coverage:** Unit tests and validation cases for edge cases uncovered during conversion, ensuring patterns are verified before reuse
- **Gap inventory:** What functionality exists in EPNM, what exists in EMS, and where gaps remain
- **Backend status:** Which services are already implemented in EMS and which require new development
- **Dependency mapping:** Cross-dependencies between frontend and backend, as well as interlinkages between features that affect conversion sequencing

Example pattern mappings (illustrative; actual patterns will be identified during codebase exploration):

| EPNM Pattern | EMS Equivalent | Notes |
|--------------|----------------|-------|
| Dojo DataGrid with server-side paging | Angular Material table with paginated API | May require endpoint modification |
| Dojo Dialog with form validation | Angular Material dialog with reactive forms | Validation rules migrate to form validators |
| Direct service injection | HTTP client with RxJS | Service calls become observable streams |
| Dojo publish-subscribe event handling | Angular event emitters or RxJS subjects | Requires scope consideration for memory management |

This knowledge base expands with each screen converted, maintaining historical traceability so decisions and discoveries remain accessible. Patterns are captured at an abstract level, so lessons learned from one category of screen (such as reports) accelerate work on similar screens in that category. As the knowledge base grows, the tooling can also revisit earlier work to apply newly discovered patterns, ensuring consistency across the converted codebase.

**Visual Validation**

BayOne will use Playwright for automated visual testing throughout conversion:

- Capture baseline screenshots and interaction flows from EPNM
- Compare against converted EMS screens at each stage
- Flag visual regressions automatically
- Generate side-by-side comparison reports

This approach catches discrepancies early and provides confidence that functional equivalence has been achieved.

**Gap Documentation**

Some EPNM functionality may not convert cleanly. Potential gaps include:

- New EMS microservices that do not yet exist
- API extensions required to support legacy interaction patterns
- UX modifications where exact replication is not feasible

BayOne will document these gaps explicitly. Cisco can decide whether to address gaps during the POC or defer them to subsequent engagement phases.

Final human review complements the automated validation throughout. When AI-assisted processes miss something, the miss tends to be categorical: a whole class of functionality rather than scattered individual items. This makes human review effective at catching gaps that automated checks might overlook, and any newly identified patterns can be applied retroactively across prior work.

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

- **Cost to Cisco:** None. This represents BayOne's investment in demonstrating capability.
- **Staffing:** Single senior BayOne resource
- **Execution:** Sequential, building infrastructure concurrently
- **Outcome:** Demonstrated conversion capability, documented patterns, estimation model, foundation for scale

### Paid Engagement (Upon Cisco Approval)

- **Staffing:** Team scale based on timeline requirements
- **Execution:** Parallel streams using established patterns and trained agents
- **Foundation:** All infrastructure developed during POC (knowledge graph, pattern library, custom agents, validation infrastructure)
- **Velocity:** Multiplicative improvement over POC baseline

The codebase analysis, custom agents, and conversion patterns developed during the POC remain available for any subsequent engagement. A paid engagement would not require repeating this foundational work.

---

## Acceleration Mechanism

The four-week POC duration does not extrapolate linearly to full-scale conversion. The POC front-loads infrastructure investment that does not repeat for subsequent screens: codebase exploration, pattern identification, agent development, workflow design, and tooling setup all happen once.

Once this infrastructure is in place, per-screen work becomes predictable. The POC establishes a baseline velocity under the slowest possible execution mode: single resource, sequential work, infrastructure still being developed. Any estimate derived from this baseline is inherently conservative. Additional team members and the LangGraph multi-agent architecture provide linear or better improvements to delivery velocity; projections based on POC performance therefore represent a reliable floor rather than an optimistic target. BayOne is prepared to discuss staffing and timeline projections after the exploration phase, when analysis provides the data needed for accurate estimation.

### One-Time Infrastructure Investment

| Work | Output |
|------|--------|
| Codebase exploration | Knowledge graph mapping architecture, dependencies, and patterns |
| Pattern identification | EPNM-to-EMS conversion library specific to this codebase |
| Agent development | Custom LangGraph agents tuned to this architecture, encoding discovered patterns and edge cases |
| Workflow design | Validated conversion process with quality gates |
| Tooling setup | Playwright test infrastructure, CI integration, comparison reporting |

This infrastructure is developed during the POC at BayOne's investment.

### Per-Screen Work

| Activity | First Screen | Subsequent Screens |
|----------|--------------|-------------------|
| Pattern discovery | Extensive | Minimal (patterns already cataloged) |
| Agent tuning | Significant | Incremental (agents already trained) |
| Implementation | Discovery-driven | Application of known transformations |
| Validation | Establish baselines | Execute existing comparisons |
| Gap identification | Novel findings | Variations on documented gaps |

The first screen carries the full weight of infrastructure development. The second screen benefits from all prior work. By the third screen, execution follows established patterns rather than requiring discovery.

---

## Technical Context

### EPNM Architecture

EPNM is a monolithic Java application with a Dojo and JavaScript frontend. After more than 15 years of evolution, the system exhibits characteristics typical of mature enterprise platforms:

- **Tight coupling** between UI components and backend services. Dojo widgets frequently embed business logic or make direct service calls that assume monolithic deployment.
- **Implicit contracts** between layers. The frontend relies on backend behaviors that are not formalized as APIs; these are implementation details that have remained stable over time.
- **Accumulated complexity** from years of feature additions, workarounds, and institutional knowledge embedded within the codebase.

The frontend combines Dojo, JavaScript, and some Angular components. Dojo's widget system, declarative markup, and data binding patterns do not have direct Angular equivalents and require semantic translation rather than syntactic conversion.

For example, Dojo widgets manage their own lifecycle and state in ways that must be mapped to Angular's component model and dependency injection system, and Dojo's module loading approach differs from Angular's ES6 module structure. These are tractable challenges, but they require understanding the intent behind existing code rather than mechanically transforming syntax.

### EMS Architecture

EMS is a microservices-based platform with an Angular frontend. The architecture assumes:

- **Service boundaries** that do not exist in EPNM. A single monolithic service call may need to orchestrate multiple microservices in the EMS context.
- **Explicit API contracts** between frontend and backend. Angular components consume well-defined REST endpoints rather than implicit contracts.
- **Reactive state management** patterns. Angular's approach using RxJS and observables differs fundamentally from Dojo's data stores and publish-subscribe mechanisms.

### Vertical Integration Requirements

As noted during discovery discussions, if a frontend capability does not exist in EMS, the supporting backend logic typically does not exist either. This conversion effort therefore requires vertical work: extracting complete functional slices from one architecture and reimplementing them in another.

For each screen, the conversion process requires:

1. **Data flow analysis** from UI interaction through service layer to data access
2. **Backend logic identification** including business rules, validation, aggregation, and transformation
3. **EMS service mapping** where equivalent microservices exist, or gap documentation where they do not
4. **Angular UI implementation** following EMS conventions and integrating with appropriate services
5. **Behavioral validation** to ensure functional equivalence for end users

BayOne has executed similar conversions across technology stacks including C# to Rust, Spring to Go, and thick-client to web architectures. The methodology described in this proposal reflects that experience.

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

1. **Hardware delivery:** BayOne will confirm the date and notify Cisco immediately upon receiving access
2. **Initial context:** If Cisco's team can identify candidate screens before code access is available, Phase 1 conversations can begin early
3. **Repository access:** Once hardware is ready, BayOne will require access to EPNM and EMS codebases
4. **Kickoff:** Brief synchronization to align on priorities and introduce BayOne to relevant SMEs

BayOne will deliver preliminary analysis within the first two weeks of repository access. Screen selection will follow collaboratively, with conversion execution proceeding immediately thereafter.
