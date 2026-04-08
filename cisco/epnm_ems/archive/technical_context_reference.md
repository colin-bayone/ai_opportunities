# Technical Context: EPNM and EMS Architectures

**Reference Document for POC Proposal**
**February 2026**

---

## EPNM Architecture

EPNM is a monolithic Java application with a Dojo and JavaScript frontend. After more than 15 years of evolution, the system exhibits characteristics typical of mature enterprise platforms:

- **Tight coupling** between UI components and backend services. Dojo widgets frequently embed business logic or make direct service calls that assume monolithic deployment.
- **Implicit contracts** between layers. The frontend relies on backend behaviors that are not formalized as APIs; these are implementation details that have remained stable over time.
- **Accumulated complexity** from years of feature additions, workarounds, and institutional knowledge embedded within the codebase.

The frontend combines Dojo, JavaScript, and some Angular components. Dojo's widget system, declarative markup, and data binding patterns do not have direct Angular equivalents and require semantic translation rather than syntactic conversion.

For example, Dojo widgets manage their own lifecycle and state in ways that must be mapped to Angular's component model and dependency injection system, and Dojo's module loading approach differs from Angular's ES6 module structure. These are tractable challenges, but they require understanding the intent behind existing code rather than mechanically transforming syntax.

---

## EMS Architecture

EMS is a microservices-based platform with an Angular frontend. The architecture assumes:

- **Service boundaries** that do not exist in EPNM. A single monolithic service call may need to orchestrate multiple microservices in the EMS context.
- **Explicit API contracts** between frontend and backend. Angular components consume well-defined REST endpoints rather than implicit contracts.
- **Reactive state management** patterns. Angular's approach using RxJS and observables differs fundamentally from Dojo's data stores and publish-subscribe mechanisms.

---

## Vertical Integration Requirements

If a frontend capability does not exist in EMS, the supporting backend logic typically does not exist either. This conversion effort therefore requires vertical work: extracting complete functional slices from one architecture and reimplementing them in another.

For each screen, the conversion process requires:

1. **Data flow analysis** from UI interaction through service layer to data access
2. **Backend logic identification** including business rules, validation, aggregation, and transformation
3. **EMS service mapping** where equivalent microservices exist, or gap documentation where they do not
4. **Angular UI implementation** following EMS conventions and integrating with appropriate services
5. **Behavioral validation** to ensure functional equivalence for end users

---

## Relevant Experience

BayOne has executed similar conversions across technology stacks including C# to Rust, Spring to Go, and thick-client to web architectures. The methodology described in the POC proposal reflects that experience.
