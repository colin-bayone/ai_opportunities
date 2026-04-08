# 06 - Discussion: Pricing Breakdown Strategy

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-02
**Document Set:** 06 (Pricing Breakdown Discussion)
**Context:** Guhan asked for a breakdown of the $500K pricing. Internal team (Surej, Zahra, Neha) coordinating response. Informed by Sets 03 (March 25 scope reframe), 04 (pricing strategy), and 05 (CEO call).
**Note:** Originally numbered Set 03 in a prior system. Renumbered to Set 06 during Singularity reorganization (2026-04-07).

---

## Trigger

Guhan reached out asking: "Thanks for the estimate from Colin. Would like to know how this was priced at 500k. Please suggest."

Internal Teams chat:
- **Zahra:** Guhan reached out asking for a breakdown of the $500K
- **Surej (CEO):** Share breakdown as three buckets: POC, Tool Build, and Conversion of all screens
- **Neha:** Asked if numbers are accurate
- **Colin:** Will prepare the sheet with breakdown

## What Guhan Is Actually Asking

He is not pushing back on the price. He is asking for justification he can use internally, likely for procurement or for Venkat/Arun to approve. He needs a story that explains why $500K is the right number, not a spreadsheet to negotiate against.

## Strategic Decision: Bill of Materials, Not Effort Sheet

**Agreed approach:** Present the $500K as a bill of materials with four work phases, each with included items described as deliverables. This keeps pricing outcome-based while showing composition.

**What we are NOT providing:**
- Effort hours
- Headcount
- Per-person rates
- Blended rates
- Timeline-to-cost mapping

**Why:** Exposing any of these gives procurement levers to negotiate the rate down. The only levers we want available are:
- Exclude a feature (reduces scope AND price)
- Extend the timeline (changes delivery option, not price)
- Take more work off our plate (reduces scope AND price)

Every lever reduces scope if it reduces price. No lever reduces price while keeping scope.

## Four-Bucket Breakdown

Expanded from Surej's three-bucket suggestion to four, adding QE as its own category.

### Bucket 1: Discovery and Codebase Analysis (10% / $50,000)

This is the foundation. Everything downstream depends on it.

**Included:**
- Systematic EPNM architecture mapping using AI-assisted exploration
- Module boundary identification and service dependency tracing
- Complete screen inventory with complexity classification
- Data flow analysis from UI through service layer to data access
- EMS integration point identification and gap analysis
- Conversion pattern identification and documentation
- Collaborative screen prioritization with Cisco SMEs
- Architecture review document with findings and recommendations

**Why it matters:** Without this, conversion is guesswork. This phase produces the knowledge base that makes everything after it possible. The codebase has 15+ years of accumulated complexity with limited documentation. This is the phase where we build the understanding that doesn't exist on paper.

### Bucket 2: AI Tooling and Agent Development (20% / $100,000)

This is the investment that enables 100% AI-generated code. It is proprietary BayOne IP built specifically for this codebase.

**Included:**
- Purpose-built conversion agents tuned to EPNM/EMS architecture patterns
- Dojo-to-Angular component translation engine with semantic understanding
- Monolith-to-microservices service extraction patterns
- Automated visual validation pipeline (Playwright-based, screen-level comparison)
- Conversion pattern library (reusable, grows with each screen converted)
- Persistent knowledge base capturing codebase structure, patterns, and edge cases
- Agent coordination framework for parallel conversion streams

**Why it matters:** This is what makes the project viable at this price point. Without custom tooling, this would be a manual conversion project at 3-4x the cost and timeline. The tooling encodes institutional knowledge about THIS codebase, not generic conversion rules. Every screen converted makes the tooling smarter for the next one.

### Bucket 3: Screen Conversion and Integration (55% / $275,000)

The core delivery. 240 to 260 screens converted end-to-end so that customers transitioning from EPNM experience no disruption to their existing workflows.

**The conversion challenge (from Guhan and Selva's own framing):**
- EPNM and EMS are fundamentally different architectures: monolithic Java/Dojo vs. microservices Java/Angular. Code cannot be transplanted. As Guhan stated, if it were that simple, Cisco's internal team would have solved it already.
- The EPNM codebase has undergone significant modification ("surgery on the older core") during EMS development, meaning the original code is not in a clean, extractable state.
- The work is vertical: where a screen has not been brought into EMS, the supporting backend logic also does not exist in EMS. This is not a UI reskinning exercise.
- Documentation is limited. Understanding the functionality of each screen requires AI-assisted code exploration, not document review.
- Customer expectation is full functional equivalence: same visualization, same operations, same interaction patterns. The customer should not be able to distinguish the converted EMS experience from the original EPNM experience.

**Included:**
- Frontend UI conversion: Dojo widget structures, declarative markup, and data binding patterns translated to Angular component model, dependency injection, and ES6 module structure. Semantic translation, not syntactic find-and-replace.
- Backend logic extraction: business rules, validation logic, data aggregation, and transformation logic identified in the EPNM monolith and re-implemented for EMS microservices boundaries. Service calls that were implicit in the monolith become explicit API contracts in EMS.
- EMS service integration: connecting converted screens to existing EMS endpoints. Where EMS services support the functionality, integration is direct. Where gaps exist, they are documented with specific recommendations.
- Data flow preservation: tracing each screen's data path from UI interaction through service layer to data access, ensuring the complete flow is functionally equivalent in EMS.
- Reactive state management adaptation: Dojo's data stores and publish-subscribe patterns mapped to Angular's RxJS observables and event emitters, with attention to scope and memory management.
- Per-screen functional equivalence verification against EPNM baseline behavior.
- Gap documentation: explicit documentation of any EPNM functionality that cannot be converted because the corresponding EMS microservice does not yet exist. These gaps are documented with enough detail for Cisco's team to build the missing services if desired.
- Targeted backend integration work where EMS services need minor adaptation to support converted screens. This covers service adaptation, not new service development (per the assumption that EMS backend infrastructure is substantially in place).
- Conversion pattern capture: each completed screen enriches the pattern library, accelerating subsequent conversions. Patterns are captured at an abstract level so lessons from one screen category (reports, dashboards, configuration wizards) apply across similar screens.

**Why it matters:** This is work that Cisco's team has done manually for prior screen migrations, but the remaining backlog is too large to complete with the existing team's bandwidth. Guhan described this as unanticipated work that is nonetheless critical for product. BayOne's AI-assisted methodology makes the full conversion feasible at a fraction of the manual effort and timeline.

### Bucket 4: Quality Engineering and Validation (15% / $75,000)

Continuous quality assurance integrated throughout, not a separate phase at the end.

**Included:**
- Continuous generative AI-driven QE embedded in the development cycle
- Automated visual validation: side-by-side EPNM vs. EMS screen comparison for every converted screen
- Automated regression testing across all converted screens (catches regressions when later changes affect earlier work)
- Integration testing with the EMS environment to verify end-to-end functionality
- Functional equivalence verification: ensuring converted screens behave identically to EPNM for end users
- Domain-specific validation: element management operations, network topology, inventory workflows
- Final acceptance validation and stakeholder review support
- Defect resolution and stabilization during the acceptance period

**Why it matters:** QE is not a gate at the end. It runs continuously. The AI-driven approach means testing scales with the conversion work rather than becoming a bottleneck. If anything is missed, the failure mode is categorical (a whole class of functionality), which makes it detectable in human review.

## Percentage Split Rationale

| Bucket | % | $ | Rationale |
|---|---|---|---|
| Discovery | 10% | $50,000 | Foundation work. Essential but bounded. One-time investment. |
| Tooling | 20% | $100,000 | Proprietary IP. What makes the project viable at this price. |
| Conversion | 55% | $275,000 | The bulk deliverable. 240-260 screens, full-stack. |
| QE | 15% | $75,000 | Continuous quality. Not optional, not separable from conversion. |

## Negotiation Defense

If procurement pushes on any bucket:

| Push | Response |
|---|---|
| "Can we skip discovery?" | Discovery is what prevents expensive surprises during conversion. Skipping it means converting blind. |
| "Can we reduce tooling?" | The tooling is what enables 100% AI-generated code. Without it, this becomes a manual conversion project at 3-4x the cost and timeline. |
| "Can we reduce QE?" | QE is integrated throughout development, not a separate phase. Reducing it means accepting lower confidence in functional equivalence. |
| "Can we do fewer screens?" | Yes. Reducing the screen count proportionally reduces the Conversion bucket. Discovery and Tooling remain the same (they're one-time). |
| "Can we extend the timeline for a lower price?" | Timeline extension changes the delivery option (July vs. Q4). It does not change the total effort or price. |

## Format Decision

The breakdown should be presented as a clean document, not a spreadsheet. Format:
- One page or close to it
- Same BayOne letterhead as the pricing proposal
- Four sections, each with the phase name, dollar amount, percentage, and included items
- Professional, not granular enough to negotiate individual lines

## Open Items

- Need to confirm with Surej that four buckets (not three) is acceptable
- Need to determine delivery format: email attachment (PDF) or direct in Teams?
- Should this reference the original pricing proposal or stand alone?
- Neha asked "are these numbers accurate?" -- need to confirm she has the right numbers before the breakdown goes out
