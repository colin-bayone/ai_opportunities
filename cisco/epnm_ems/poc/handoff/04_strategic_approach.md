# 04 — Strategic Approach

**Purpose of this document:** The conversion approach as articulated across the engagement meetings, at the level the transcripts established. What strategies are in scope, what principles guide the work, what methodological elements Cisco has endorsed. Not prescriptive on specific implementation choices beyond what the transcripts committed to.

---

## 1. The Core Strategic Framing

The POC is a UX overlay, not a conversion. The approach rebuilds the visual and interaction model of EPNM in Angular, places that rebuild behind a toggle inside the EMS build, and points it at the existing EMS backend. The strategic win is fidelity without duplication: customers see the experience they know, operators get a transition period, Cisco avoids maintaining two backends, and renewal revenue flows as customers move from EPNM to EMS under the comfort bridge the toggle provides.

Guhan synthesized the approach in one sentence: "It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel."

Selva's metaphor: "Take that UX and that experience, marry it with the backend that's already there in the system."

---

## 2. Visual and Interaction Fidelity is the Target

Colin framed the approach to the Cisco team directly: "So really we'll keep it exactly, visually speaking, and UX speaking identical to this EPNM use case. But Selva, as you said, map everything to the new backend."

Fidelity covers three dimensions:

1. **Visual fidelity.** EPNM colors (blue and white), typography, spacing, layout, and visual component style. The classic view should look like EPNM to a customer who has used EPNM for years.
2. **Interaction fidelity.** Clicks, navigation paths, filter behavior, row-expand semantics, toggle positions, tab structures, and workflow steps should match EPNM. If a user opens the Network Devices screen and clicks a device name, the same information should appear in the same layout it appeared in EPNM.
3. **Functional fidelity.** Actions that change state (adding a device, clearing an alarm, scheduling a maintenance window) should have the same effect in the classic view as in EPNM, using the EMS backend as the effector.

The acceptance test that follows from this (Guhan): "Final test will be to show the same thing comes up everywhere." Same action in either view. Same result.

---

## 3. The Exponential Decay / Front-Loading Principle

Colin explicitly set this expectation with Selva in the scope reframe meeting: "This does grow exponentially. So when it starts out, I think we'd said it would just be me working on this for the POC, but it's still fine. That is the slowest it will ever be."

Colin's mental model:

- The first screen (or first batch of screens) is slowest. Environment setup, codebase exploration, architectural understanding, agent development, pattern establishment, and initial discovery all happen up front and are not repeated.
- Every subsequent screen benefits from the compounding of what was built earlier. Components already converted can be reused. Patterns already established can be applied. Agents already tuned to the codebase move faster.
- Per-screen time decays exponentially toward a steady-state rate as the infrastructure matures.
- Linear extrapolation ("if N screens take X weeks, then 10N screens take 10X weeks") significantly overestimates the work. Colin warned against this explicitly: "Don't think if I say like it'll take us three weeks to do this, that that's three weeks for three screens, because that's just kind of that initial front loading."

The execution session does not need to prove the decay mechanics during the POC. It does need to build the foundation well enough that the decay actually materializes in the full engagement that follows. Poorly-chosen patterns on the first screens make the second, third, and fiftieth screens harder, not easier.

---

## 4. The Venn Diagram Approach to Feature Mapping

Selva asked Colin how the project would identify functionality that existed in one product but not the other. Colin's answer: "So that's what I call almost like a Venn diagram. And our goal would be a perfect circle overlap, at least for the areas that the customers care about."

The mental model:

- One circle is EPNM functionality.
- The other circle is EMS functionality.
- The overlap is functionality available in both.
- The target is a perfect circle overlap for the areas customers care about — not for the total feature set. Full feature parity across every historical EPNM capability is not required. Customer-relevant parity is.

For the POC, the Venn diagram is drawn just for Inventory and Fault Management. Agent-driven codebase exploration surfaces what exists in EPNM for each screen, what exists in EMS, and where the gaps are. Gaps relevant to the two screens either get narrow API-level touchups (if small) or get flagged to Selva (if larger).

Colin also framed the practical efficiency of the agent-driven mapping: "Rather than trying to set up all these calendar meetings with the team and bogging everyone down, now with agents, we just go and explore."

---

## 5. Priority Order Versus Diversity Order

Colin raised a planning consideration in the scope reframe meeting: when sequencing work across multiple screens, two different orderings are useful:

- **Priority order.** Screens customers use most. Guhan's criterion. For the POC this is Faults and Inventory by design.
- **Diversity order.** Screens covering the widest range of UI patterns — tables, detail / form views, topology / graph views, popups, 360 views. Diversity order helps agents learn more edge cases early, which accelerates later screens.

The two orderings are not in conflict for the POC; both screens in scope are high priority and also represent distinct pattern families (Inventory spans tables, detail views, nested popups, and chassis visualization; Fault Management adds time-windowed events, correlated alarms, and expandable rows). Diversity is already built into the POC scope.

For the full engagement that follows the POC, the question of whether to order by priority or diversity is a planning decision to raise with Selva. For the POC, it does not apply.

---

## 6. Parallelizable Workflow for Post-POC Scale

Colin described the scaling model to Selva: "This is a very parallelizable workflow. So once the foundation is there, once those agents are there, it's really just a matter of having people on our side to continue to run this and be the quality checkers."

Colin's proposed stream model for post-POC scale:

| Stream | Focus | Personnel |
|--------|-------|-----------|
| QA / QE agents | Build and run automated verification agents | One dedicated person |
| Screen batch A | Convert a subset of screens using established patterns | One person |
| Screen batch B | Convert another subset of screens | One person |
| Additional batches | Further subsets | Additional people |

This is not POC work. It matters only to the extent that the POC's output enables parallel streams afterward. If the patterns Colin establishes are reusable and well-documented, the parallel scaling is straightforward. If not, the scaling falters.

---

## 7. Automated QA and QE — In and Out of POC Scope

### What is in POC scope

Colin's stated POC testing approach (from the 2026-04-06 walkthrough):

- Enough testing to guarantee existing functional equivalency for the two screens.
- Internal unit testing complete before declaring the POC done.
- Awareness of Cisco's existing regression suites, even if not full integration with them.

### What is deferred to the full engagement

- Full agentic QA with Playwright agents that drive Playwright like a user would — clicking around, trying different options, combining exploratory behavior with deterministic testing workflows.
- Dashboard visibility for the Cisco team. Colin committed to a dashboard showing the tests, which agents ran, what they observed, and their conclusions — "the good, the bad, and the ugly." This is deferred scope.
- Coverage gap analysis: identifying holes in existing test suites.
- Creation of replica test cases for the Angular-based classic UI.
- Integration with Cisco's existing seven-category test infrastructure (functional, scale, end-to-end, UI, API, migration, upgrade).
- Data-driven test creation across the full device configuration matrix.

### The verification principle for POC

Colin's approach for the POC: user-persona Playwright agents trained on the EPNM interface exercise the classic view and verify that actions produce the same results as equivalent actions in the new EMS UX. This is the minimum functional equivalence check. Full agentic gap analysis is deferred.

Selva on the approach: "That would be great too." The team endorsed the direction.

---

## 8. Four-Agent Architecture (from BayOne Methodology)

Colin's methodology presentation in Set 01 included the LangGraph agent swarm model: architect, engineer, foreman, and judge. Set 02 reinforced the judge agent as the meta-analytical layer for gap detection. Set 05a (Venkat positioning notes) confirmed this framing is consistent with how Venkat describes the approach internally at Cisco.

Roles:
- **Architect.** Plans conversion at the structural level. Analyzes existing code, proposes conversion shape, identifies patterns.
- **Engineer.** Generates code from the architect's plan.
- **Foreman.** Coordinates execution, sequences work, manages dependencies between sub-agents.
- **Judge.** Meta-analyzes quality. Reviews test coverage, identifies categorical gaps, flags inconsistencies.

Guhan's directness on gap detection in Set 02: "How do you ensure no domain or functionality gap?" Colin's four-layer response — judge agent, Playwright visual comparison, peer-to-peer agent gap analysis with autonomous sub-agent spawning, human categorical review — remains the quality-assurance frame.

The detail of how the four agents are implemented is not specified by Cisco; it is the execution session's domain. Cisco endorses the pattern; Cisco does not prescribe the implementation.

---

## 9. Customer-Transparent Output

Across multiple meetings, a recurring principle: customers never see the AI. Guhan referenced this in Set 01. It is reinforced in Venkat's positioning (Set 05a) as "100 percent AI-generated code" as the internal narrative. What ships to customers is code; what Cisco tells customers is the classic view feature works as expected.

Practically this means: commit messages, documentation, code comments, and UI text should read as standard Cisco engineering output. Nothing about prompts, agents, models, or AI tooling leaks into customer-visible artifacts. Colin is the gatekeeper for this discipline.

Colin's qualifier in the scope reframe meeting: at the POC stage, "we're going to need to pass a manual oversight of this. Once we have a pattern established, this starts to take off." The full 100-percent-AI-generated framing is an aspiration; the POC starts with manual oversight and graduates toward it.

---

## 10. The Four-Phase Lifecycle (Product-Level, Not POC-Level)

For context only. The broader product strategy Cisco is executing:

1. **Current state.** EMS ships new UX only. Customers resist.
2. **Classic view toggle shipped.** The feature this POC prototypes. Customers can switch.
3. **Transition period.** Customers use classic as a comfort bridge.
4. **Classic view deprecated.** New UX becomes the only view.

The POC proves the pattern works on two screens. The product team then scales the pattern across the surface (200-250 workflow screens) and manages the phase-out timeline with customers. The execution session's work stays inside Phase 2: deliver the two-screen toggle in a way that demonstrates the pattern and sets up the scaling.

---

## 11. Discovery Is Agent-Driven, Not Meeting-Driven

Colin's framing: "We're very good at that. So we won't need much hand holding once we have access to the code base. We go and have exploration happen. Even on this, I said we kind of build our own kind of map of the application. So we understand a lot more without having to ask SMEs. So we try to make that as painless as it can be. The only time we'll ask questions is if things contradict each other or things aren't in alignment or logically speaking."

The working pattern:
- Read the codebase with agents first.
- Build an internal map of the application.
- Identify gaps, inconsistencies, or ambiguities.
- Only then bring specific, targeted questions to the Cisco team.

This protects the Cisco team's bandwidth (they are on critical release work) and keeps BayOne's questions high-signal. It also means the execution session should not default to asking Selva or the tech leads when a question comes up; the first move is almost always to look at the code.

---

## 12. What the Execution Session Should Not Change Without Going Back to Colin

The following are positions Colin has committed to with Cisco in transcripts. Any deviation needs to be raised back to Colin, not changed unilaterally by the execution session:

- The scope is two screens.
- The toggle is local per screen for the POC.
- The default view on login is the classic view.
- The classic UI uses the existing EMS backend unchanged (except narrow API touchups).
- The output is production-quality code.
- Cisco hardware, Cisco-issued accounts, Cisco-issued Claude Code, and local LangGraph are the only tools.
- Customers never see the AI.
- Functional equivalence is the acceptance bar.
- The four-agent pattern (architect / engineer / foreman / judge) is the internal BayOne methodology Cisco has endorsed.
