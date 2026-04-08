# Methodology Details: AI-Assisted Conversion Workflow

**Reference Document for POC Proposal**
**March 2026**

---

## AI-Assisted Conversion Tooling

For this proof-of-concept, BayOne will use Cisco-provided Claude Code with purpose-built skills and sub-agents for exploration and conversion work. This approach provides structured automation with appropriate human oversight at POC scale, where patterns are still being discovered and validated.

The workflow models how experienced engineering teams approach conversion systematically:

- **Analysis:** Each EPNM screen is examined holistically, mapping data flows from UI through service layer, identifying backend dependencies, and determining EMS service integration points. Where gaps exist, they are documented immediately.

- **Planning:** Based on analysis, implementation is planned by identifying specific translation patterns (such as Dojo widget structures to Angular component equivalents), flagging areas requiring custom logic, and designing component structure and service integration.

- **Execution:** Conversion proceeds with sub-tasks for component implementation, service integration, and test creation. Work is coordinated through structured handoffs rather than ad-hoc effort.

- **Validation:** A quality gate reviews output against specification, validates behavioral equivalence, and catches gaps before they propagate. Work can be halted and redirected if standards are not met.

The tooling has access to capabilities beyond conversation: codebase search, static analysis, prototype implementation, and test execution. Each step produces documented outputs that inform subsequent work and enable traceability.

For larger engagements beyond the POC, BayOne employs a LangGraph-based multi-agent architecture. This enables fully autonomous coordination across parallel work streams, with agents dynamically spawning sub-tasks and self-managing gap resolution. The foundations established during the POC transfer directly to this scaled model.

---

## Pattern Library and Knowledge Base

As exploration and conversion proceed, BayOne builds a comprehensive knowledge base specific to this codebase: a traceable, continuously refined understanding of the system that grows with every screen analyzed.

The knowledge base captures:

- **Conversion patterns:** Documented mappings between EPNM constructs and EMS equivalents, including nuances and edge cases discovered during implementation
- **Test coverage:** Unit tests and validation cases for edge cases uncovered during conversion, ensuring patterns are verified before reuse
- **Gap inventory:** What functionality exists in EPNM, what exists in EMS, and where gaps remain
- **Backend status:** Which services are already implemented in EMS and which require new development
- **Dependency mapping:** Cross-dependencies between frontend and backend, as well as interlinkages between features that affect conversion sequencing

### Example Pattern Mappings

(Illustrative; actual patterns will be identified during codebase exploration)

| EPNM Pattern | EMS Equivalent | Notes |
|--------------|----------------|-------|
| Dojo DataGrid with server-side paging | Angular Material table with paginated API | May require endpoint modification |
| Dojo Dialog with form validation | Angular Material dialog with reactive forms | Validation rules migrate to form validators |
| Direct service injection | HTTP client with RxJS | Service calls become observable streams |
| Dojo publish-subscribe event handling | Angular event emitters or RxJS subjects | Requires scope consideration for memory management |

This knowledge base expands with each screen converted. Patterns are captured at an abstract level, so lessons learned from one category of screen (such as reports) accelerate work on similar screens, and newly discovered patterns can be applied retroactively for consistency.

---

## Categorical Pattern Recognition

When AI-assisted processes miss something, the miss tends to be categorical: a whole class of functionality rather than scattered individual items. This makes human review effective at catching gaps that automated checks might overlook, and any newly identified patterns can be applied retroactively across prior work.
