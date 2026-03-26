# EPNM to EMS UI Conversion: POC Proposal

**Prepared by:** Colin Moore, Director of AI, BayOne Solutions
**Date:** February 2026
**For:** Guhan, Selva, Cisco EMS Team

---

## Executive Summary

BayOne proposes a four-week proof-of-concept to demonstrate AI-assisted conversion of EPNM screens to EMS. We will convert 2-3 representative screens end-to-end- UI and backend logic- using a methodology that accelerates with each screen converted.

This POC is an investment we're making at our cost. The infrastructure we build during the POC- codebase analysis, custom conversion agents, validated patterns- becomes the foundation for any subsequent engagement. We're not asking you to take our word that this works; we're proving it on your actual codebase.

---

## The Technical Challenge

This is not a skinning exercise. EPNM and EMS represent fundamentally different architectural paradigms, and the conversion requires extracting functionality from a tightly-coupled monolith and re-implementing it within a microservices context.

### EPNM Architecture (Legacy)

EPNM is a monolithic Java application with a Dojo/JavaScript frontend. After 15+ years of evolution, it exhibits the characteristics typical of long-lived enterprise systems:

- **Tight coupling** between UI components and backend services. Dojo widgets often embed business logic or make direct service calls that assume monolithic deployment.
- **Implicit contracts** between layers. The frontend relies on backend behaviors that aren't formalized as APIs- they're implementation details that happen to work.
- **Accumulated complexity** from years of feature additions, workarounds, and undocumented tribal knowledge baked into the code.

The frontend mix of Dojo, vanilla JavaScript, and some Angular creates additional complexity. Dojo's widget system, declarative markup, and data binding patterns have no direct Angular equivalents- they require semantic translation, not syntactic conversion.

### EMS Architecture (Modern)

EMS is microservices-based with an Angular frontend. The architecture assumes:

- **Service boundaries** that don't exist in EPNM. What was a single monolithic service call may need to orchestrate multiple microservices.
- **API contracts** between frontend and backend. Angular components consume well-defined REST endpoints, not the implicit contracts EPNM relies on.
- **Different state management** patterns. Angular's reactive approach (RxJS, observables) differs fundamentally from Dojo's data stores and pub/sub mechanisms.

### Why This Is Vertical Work

When Selva noted that "if the frontend doesn't exist, the backend doesn't either," he identified the core challenge. This isn't about translating UI markup- it's about extracting vertical slices of functionality from one architecture and reimplementing them in another.

For each screen, we need to:

1. **Understand the data flow** from UI interaction through service layer to data access
2. **Identify backend logic** that must migrate- business rules, validation, aggregation, transformation
3. **Map to EMS patterns** where equivalent microservices exist, or flag gaps where they don't
4. **Implement the Angular UI** following EMS conventions and integrating with the appropriate services
5. **Validate behavioral equivalence** to ensure customers get the same experience

The challenge isn't that this is impossible- we've done similar conversions before (C# to Rust, Spring to Go, thick-client to web). The challenge is doing it efficiently at scale. That's where the methodology matters.

---

## Our Approach

### Phase 1: Exploration and Screen Selection

**Duration:** ~1 week from code access
**Deliverable:** Analysis document with categorized screens and recommended POC candidates

Before converting anything, we need to understand the codebase. This isn't just reading documentation (which, as you noted, is sparse). It's systematic analysis using AI-assisted exploration to build a knowledge graph of the EPNM architecture.

**Codebase Analysis:**

We use Claude Code for initial exploration- mapping module boundaries, identifying service dependencies, tracing data flows, and cataloging UI patterns. This produces a structured understanding of:

- Screen inventory and categorization (data entry forms, dashboards, reports, configuration wizards, real-time monitoring)
- Dependency graphs showing which screens share backend services
- Complexity indicators- screens with heavy cross-dependencies vs. relatively self-contained ones
- Pattern identification- recurring UI structures and their backend correlates

**Collaborative Screen Selection:**

Your team knows things we can't learn from code alone: which screens customers care most about, which have been historically problematic, which represent typical vs. edge-case complexity.

We propose that your SMEs identify candidate screens based on business priority, and we validate feasibility based on our analysis. This shared ownership of scope decisions protects both parties- you're not bound by our blind guesses, and we're not committed to screens that turn out to be outliers.

**Selection Criteria:**

For POC candidates, we're looking for screens that are:

- **Representative** of the broader conversion challenge, not edge cases
- **Self-contained enough** to convert without pulling in half the system
- **Not yet in EMS** so this work adds value rather than duplicating effort
- **Complex enough** to demonstrate real capability, not trivial wins

We'll recommend 2-3 screens with rationale. You decide which ones proceed to Phase 2.

### Phase 2: Conversion and Validation

**Duration:** ~3 weeks from screen selection
**Deliverable:** Working screens in EMS, documented conversion patterns, estimation model

This is where we prove the approach on real code.

**The Agent Architecture:**

For conversion work at this scale, Claude Code alone isn't enough. We use a LangGraph-based agent swarm that models how experienced engineering teams actually work:

- **Architect Agent:** Analyzes the EPNM screen holistically. Maps data flows, identifies backend dependencies, determines what EMS services to integrate with (or what gaps exist). Produces a conversion specification.

- **Engineer Agent:** Takes the specification and plans implementation. Identifies specific Dojo→Angular translation patterns, flags areas requiring custom logic, designs the component structure and service integration.

- **Foreman Agent:** Orchestrates execution. Spawns worker sub-agents for specific tasks- component implementation, service integration, test creation. Manages parallel work streams and coordinates handoffs.

- **Judge Agent:** Quality gate. Reviews output against the specification, validates behavioral equivalence, catches gaps before they propagate. Can halt work and redirect if something's wrong.

These agents have access to tooling beyond conversation- they can grep codebases, run static analysis, prototype implementations, execute tests. They coordinate through structured handoffs, not just chat.

**Pattern Library:**

As we convert screens, we build a pattern library specific to EPNM→EMS conversion:

| EPNM Pattern | EMS Equivalent | Notes |
|--------------|----------------|-------|
| Dojo DataGrid with server-side paging | Angular Material table + paginated API | Requires endpoint modification |
| Dojo Dialog with form validation | Angular Material dialog + reactive forms | Validation rules migrate to form validators |
| Direct service injection | HTTP client + RxJS | Service calls become observable streams |
| Dojo pub/sub event handling | Angular event emitters / RxJS subjects | Scope considerations for memory leaks |

This library starts small and grows with each screen converted. By screen 3, we're not discovering patterns- we're applying known transformations.

**Visual Validation:**

We use Playwright for automated visual testing throughout conversion:

- Capture baseline screenshots and interaction flows from EPNM
- Compare against converted EMS screens at each stage
- Flag visual regressions automatically
- Generate side-by-side comparison reports

This catches discrepancies early and gives you confidence that "same experience" actually means the same experience.

**Gap Analysis:**

Not everything will convert cleanly. Some EPNM functionality may require:

- New EMS microservices that don't exist yet
- API extensions to support legacy interaction patterns
- UX compromises where exact replication isn't feasible

We document these explicitly. You decide whether to address gaps during the POC or defer them. Either way, you have a clear picture of what "full conversion" actually requires.

---

## The Flywheel Effect

A natural question: if 2-3 screens take 4 weeks, does that mean 100 screens take 150 weeks?

No. The POC is front-loaded with one-time work that doesn't repeat.

### One-Time Investment (Happens Once)

| Work | What It Produces |
|------|------------------|
| Codebase exploration | Knowledge graph mapping architecture, dependencies, patterns |
| Pattern identification | EPNM→EMS conversion library specific to your codebase |
| Agent development | Custom LangGraph agents tuned to your architecture, encoding discovered patterns and edge cases |
| Workflow design | Validated conversion process with quality gates |
| Tooling setup | Playwright test infrastructure, CI integration, comparison reporting |

This work happens during the POC. It's the investment we're making for free.

### Per-Screen Work (Repeats, But Faster)

| Work | First Screen | Later Screens |
|------|--------------|---------------|
| Pattern discovery | Heavy | Minimal- patterns already cataloged |
| Agent tuning | Significant | Incremental- agents already trained |
| Implementation | Guided by discovery | Apply known transformations |
| Validation | Establish baselines | Run existing comparisons |
| Gap identification | Novel findings | Variations on known gaps |

The first screen carries the full weight of infrastructure buildout. The second screen benefits from everything learned. By screen 3, we're executing against established patterns, not discovering them.

### The Math

During the POC, I'm working solo and sequentially. That's the slowest possible execution mode- but it's appropriate for establishing the foundation.

Once patterns are locked and agents are trained:

- **Parallel execution** becomes possible. Multiple team members can run the same playbook simultaneously without stepping on each other.
- **Per-screen velocity** improves dramatically. Pattern application is faster than pattern discovery.
- **Quality remains consistent.** The judge agent and validation infrastructure enforce standards regardless of who's executing.

The POC establishes a baseline velocity under worst-case conditions (solo, sequential, building infrastructure). A staffed engagement multiplies that baseline.

---

## Scope and Timeline

### POC Scope

- **Screens:** 2-3 representative screens, selected collaboratively after Phase 1 analysis
- **Depth:** End-to-end conversion including backend logic, not just UI translation
- **Validation:** Automated visual comparison, functional testing, gap documentation
- **Deliverables:** Working code, documented patterns, estimation model for remaining screens

### Timeline

**Total:** 4 weeks from code access

| Week | Phase | Activities |
|------|-------|------------|
| 1 | Exploration | Codebase analysis, screen categorization, candidate selection with your team |
| 2-4 | Conversion | Convert selected screens, build pattern library, validate and document |

The timer starts when I have repository access. Some Phase 1 work- initial conversations with your SMEs about screen priorities, understanding your categorization criteria- can happen before the laptop arrives.

### What's Not Included

- **Screens beyond the agreed 2-3.** We'll provide an estimation model to extrapolate, but the POC itself is bounded.
- **New EMS backend services.** If a screen requires backend functionality that doesn't exist in EMS, we document the gap. Building new microservices is paid engagement scope.
- **Production deployment.** POC deliverables are working code demonstrated in a dev/test environment.

---

## Investment Model

### POC (This Proposal)

- **Cost to Cisco:** Zero. This is our investment to prove capability.
- **Staffing:** Colin solo
- **Execution:** Sequential, building infrastructure as we go
- **Outcome:** Demonstrated conversion, documented patterns, estimation model, foundation for scale

### Paid Engagement (If You Proceed)

- **Staffing:** Team scale based on timeline requirements
- **Execution:** Parallel streams using established patterns and trained agents
- **Foundation:** Everything built during POC- knowledge graph, pattern library, custom agents, validation infrastructure
- **Velocity:** Multiplicative improvement over POC baseline

The POC isn't just a demo. It's heavy lifting that becomes the foundation for real work. The codebase analysis, the custom agents, the conversion patterns- that infrastructure doesn't disappear. If you proceed, you're not starting from zero.

---

## Security and Access

Per our discussion:

- All work happens on Cisco hardware (laptop in progress)
- All AI tooling uses Cisco-licensed instances (Claude via Cisco's approved channels)
- No code leaves Cisco infrastructure
- NDA already executed

I'm already onboarded for the CI/CD engagement with Anand's team. The same security posture applies here.

---

## Next Steps

1. **Laptop arrival:** I'll confirm the date and notify you immediately when I have access
2. **Initial context:** If your team can identify candidate screens before I have code access, we can start Phase 1 conversations early
3. **Code access:** Once hardware is ready, I'll need repository access to EPNM and EMS codebases
4. **Kickoff:** Brief sync to align on priorities and introduce me to the relevant SMEs

I'll have a preliminary analysis within the first week of access. From there, we'll select screens together and execute.

---

**Questions?** Happy to discuss any aspect of this proposal. The approach is proven- we've done similar conversions on codebases ranging from legacy .NET to embedded C++. The specifics always vary, but the methodology scales.
