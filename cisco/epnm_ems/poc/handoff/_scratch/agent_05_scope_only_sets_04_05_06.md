# Agent 05 - Scope-Only Extraction from Sets 04, 05, 05a, 06, 06a, 06b, 06c

Source files read (all seven):

1. research/04_discussion_pricing_strategy_2026-03-26.md
2. research/05_internal_call_pricing_decisions_2026-03-30.md
3. research/05a_notes_venkat_positioning_2026-03-30.md
4. research/06_discussion_pricing_breakdown_2026-04-02.md
5. research/06a_discussion_pricing_refinement_language_2026-04-02.md
6. research/06b_gap_analysis_breakdown_vs_transcripts_2026-04-02.md
7. research/06c_gap_resolution_decisions_2026-04-02.md

Commercial content (rates, headcount cost calculations, margin figures, discount levers, monetary amounts) has been filtered out per instructions.

---

## 1. Scope-Relevant Content from Set 04

Source: 04_discussion_pricing_strategy_2026-03-26.md

- The scope reframe from Set 03 (March 25) established the work as a "classic view toggle" rather than full-stack conversion. Set 04 explicitly flags that prior language describing "250+ screens converted, full-stack, end-to-end" and "full vertical slice (UI + backend)" was written before that reframe was absorbed and "may need recalibration." The toggle or overlay approach is noted as "likely less effort per screen than full-stack vertical conversion."
- POC is positioned as part of the overall engagement, not a separate phase. Scope of the POC is described as "2-3 screens + pattern foundation" and is intended to begin the engagement.
- Open technical item flagged: the POC is expected to calibrate the per-screen effort estimate with real data.
- Open operational item flagged: engagement start date depends on hardware arrival from Cisco.
- Open client-side item flagged: specific July interest (specific date and customer expectation) not yet confirmed.

## 2. Scope-Relevant Content from Set 05

Source: 05_internal_call_pricing_decisions_2026-03-30.md

- Operational positioning decision: bound the scope clearly with written assumptions and include a change-request clause. Scope discipline is the mechanism for protecting the engagement, rather than number inflation.
- Named people and roles:
  - Rahul: BayOne CEO, gave guidance on scope bounding and change-request approach.
  - Venkat: senior Cisco leader characterized by Rahul as "more like a doer, not somebody whose own strategy." Rahul advised identifying the person senior to Venkat to build higher-level relationships.
- Sephora precedent cited as confidence signal for AI-assisted conversion methodology: after POC, a conversion took 2 minutes with 97% accuracy on production. This informs how the execution session should speak about AI-assisted conversion confidence, though it is a cross-engagement data point, not an EPNM/EMS commitment.
- No POC-screen technical detail added in this set.

## 3. Scope-Relevant Content from Set 05a (Venkat positioning)

Source: 05a_notes_venkat_positioning_2026-03-30.md

- Venkat's role: senior Cisco leader above Guhan. Positioned as an internal sponsor / advocate for BayOne. His advocacy is described as a strategic asset beyond the Guhan and Selva relationship.
- Sponsorship signal: Venkat used the EPNM-to-CNC UI migration as his own example when describing where AI-driven modernization fits. He treats this engagement as a showcase for the AI-generated code narrative.
- NRE funding context: Venkat confirmed NRE funding is the funding mechanism for partner work in the Provider Connectivity area, which is Guhan's team. This is the funding path backing the engagement.
- Positioning language for the execution session: Venkat explicitly recommended BayOne position itself as an "AI-driven engineering partner" with "100% AI-generated code capability" as the key differentiator. He framed this as "the closer you are to 100% AI-generated code, the stronger the story." The execution session should align the POC narrative (how the toggle feature was built) with this 100% AI-generated code positioning.
- Human-role framing that complements the 100% AI-generated code claim: prompt engineering, architecture design, code review, debugging, test topology optimization, solution design. This is the language used when referring to what humans on the engagement do.
- Geographic talent advice is excluded per instructions.

## 4. Scope-Relevant Content from Set 06 (including 06a, 06b, 06c)

### Set 06 - scope and positioning items

Source: 06_discussion_pricing_breakdown_2026-04-02.md

- Named people and roles:
  - Guhan: Cisco, asked for a breakdown of the engagement value; audience for internal justification (likely to Venkat, Arun, or procurement). Not pushing back on price; needs a defensible story.
  - Selva: Cisco, paired with Guhan on scope framing.
  - Surej: BayOne CEO, suggested a three-bucket structure (POC, Tool Build, Conversion of all screens). Team expanded to four buckets.
  - Zahra: BayOne, coordinating Cisco-facing response.
  - Neha: BayOne, coordinating internal team response.
- Scope composition the engagement is presented as (four work phases, to be used as the operating structure, not the pricing structure):
  1. Discovery and Codebase Analysis
  2. AI Tooling and Agent Development
  3. Screen Conversion and Integration
  4. Quality Engineering and Validation
- Scope boundary statements that affect POC framing:
  - "240 to 260 screens converted end-to-end so that customers transitioning from EPNM experience no disruption to their existing workflows." (Note: this language coexists with the Set 03 classic view toggle reframe; the handoff must not silently resolve the conflict.)
  - "EPNM and EMS are fundamentally different architectures: monolithic Java/Dojo vs. microservices Java/Angular." Guhan's own framing: "if it were that simple, Cisco's internal team would have solved it already."
  - The EPNM codebase has undergone "surgery on the older core" during EMS development. The original code is not in a clean, extractable state.
  - Where a screen has not been brought into EMS, the supporting backend logic also does not exist in EMS. Explicitly flagged as "not a UI reskinning exercise."
  - Customer expectation: "same visualization, same operations, same interaction patterns." Customer "should not be able to distinguish the converted EMS experience from the original EPNM experience."
  - Gap documentation is an explicit deliverable for EPNM functionality where no corresponding EMS microservice exists. These gaps are documented in enough detail for Cisco to build missing services.
  - Backend work is framed as "service adaptation, not new service development," under the assumption that EMS backend infrastructure is substantially in place.
- Scope levers defined for procurement conversations (operational positioning):
  - Reducing screen count proportionally reduces the Conversion bucket; Discovery and Tooling remain as one-time investments.
  - Timeline extension changes the delivery option, not total effort.
  - No lever reduces price while preserving scope.

### Set 06a - refinement language

Source: 06a_discussion_pricing_refinement_language_2026-04-02.md

- Commitment language relevant to the execution session: discovery is positioned as "calibration, not re-pricing." Any adjustment flows through the change request process already in the proposal. Refinement is not renegotiation.
- Operational positioning for the execution session: the engagement is characterized as conservative estimation absent code access. Once the codebase is accessible, findings will be shared proactively, and significant changes go through the formal change-request process.
- No new POC-screen technical detail.

### Set 06b - gap analysis items with scope-shaping content

Source: 06b_gap_analysis_breakdown_vs_transcripts_2026-04-02.md

Scope-shaping items (filter passes pricing content, keeps scope and operational detail):

- Estimation model as a discovery deliverable. Guhan explicitly wants conversion-velocity data he can use for customer-facing delivery commitments ("if we are able to do 10 screens in 10 days, we can do 17 in 17 days, some sort of estimation we can do based on this"). Implication for POC: velocity data from the POC is a client-facing artifact, not just internal calibration.
- Running instances of EPNM and EMS will be provided "when we get to that stage" (Selva). Discovery requires access to the live applications, not only the code.
- Identification of what has already been ported vs. what remains in EPNM only. Selva stated "there are some screens we have already brought in functionality with a new UI." Scope must distinguish existing EMS work from gaps to avoid duplicated effort. Selva also directed the effort to "focus on the ones that we've not brought in yet."
- UX preservation, not UX redesign. Prior porting involved UX redesign, and some customers rejected the new UX. The current effort explicitly preserves the EPNM experience because customers want it. This is directly load-bearing for a classic-view toggle POC.
- Customer-transparent equivalence as the success standard. Guhan: "from a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything."
- Agent architecture is a four-agent model (architect, engineer, foreman, judge) with peer-to-peer communication. The judge agent is called out specifically for gap detection and quality enforcement.
- Methodology progression: Claude Code for initial exploration, scaling to LangGraph for deeper work. Two-tier tooling approach.
- Knowledge persistence described as "almost a blockchain documentation style" - persistent append-only knowledge that grows with each screen.
- Test coverage gap analysis: Colin told Guhan "if they're identified as gaps, even if we already have tests written, maybe we need new tests. Maybe there's not some written that should have been written in the past." The judge agent identifies where tests should exist but do not.
- Human-in-the-loop final review. Colin: "the final line of defense is us. So at the end of it, we still have to, as humans, go and review this, do it ourselves." This is an explicit trust commitment positioned alongside the 100% AI-generated code claim, not in contradiction to it.
- Categorical miss detection. Colin's framing: "if anything's missed, it's categorical. It's not like it's a little small thing that can slip through the cracks." Failures are large and detectable.
- Continuous gap analysis described as relentless and continuous ("going back and looking over and over and over again, both during development and at the end").
- Domain-specific validation for element management operations, network topology, inventory workflows. Guhan's biggest concern was domain gaps: "How do we ensure that there's no domain gap or no functionality gap?" Inventory workflows are explicitly named as one of the validation domains. This is directly relevant because Inventory is one of the two POC screens.
- Flywheel / acceleration mechanism: early screens are slower; later screens are faster as patterns and tooling mature. POC conversion rates are therefore conservative relative to steady-state production rates.
- Screen categorization by type: "data entry forms, dashboards, reports, configuration wizards, real-time monitoring views." Reports was specifically called out by Selva as a missing functionality category.

### Set 06c - gap resolution decisions

Source: 06c_gap_resolution_decisions_2026-04-02.md

Decisions that set binding scope and positioning language for the engagement:

- Estimation model explicitly added as a Phase 1 Discovery deliverable. Binding.
- Customer-transparent equivalence language strengthened to "seamless and indistinguishable from the original EPNM interface" and "UX preservation, not UX redesign." Applied to Phase 3 description and Phase 4 visual validation. Binding.
- Human-in-the-loop review: reframed as "architectural oversight and quality verification at every stage of the agentic workflow, with human engineers reviewing all AI-generated output." Positioned alongside 100% AI-generated code, not as a contradiction. Binding.
- Scope boundary resolution: "approximately 240 to 260 screens as identified through collaborative prioritization." Added language: "BayOne will accommodate reasonable variance from this estimate within the engagement. Significant changes to the screen count or complexity beyond what is identified during discovery would be addressed through the change request process." Binding. Added a discovery deliverable: "Inventory of screens already ported to EMS vs. screens remaining in EPNM only, ensuring no duplication of existing work."
- Defensive "protects both parties" language removed entirely and replaced with the reasonable-variance framing above.
- Still pending at end of 06c (not resolved): prominence of flywheel mechanism; where "already ported vs. not" inventory lives; elevation of domain-specific validation; whether test-coverage-gap-analysis is called out in the tooling phase; whether UX preservation vs. redesign is called out explicitly in the breakdown; whether blockchain-style documentation and the four-agent architecture are mentioned in the client-facing breakdown; whether Claude Code to LangGraph progression is surfaced; whether documentation-state-assessment is a separate line item; whether screen categorization by type is expanded; whether categorical-miss-detection is mentioned.

## 5. Open Scope Items Flagged Across These Sets

- Per-screen effort estimate predates the classic-view toggle reframe and has not been recalibrated with code access. (Set 04)
- Engagement start date depends on hardware arrival. (Set 04)
- Specific July customer expectation and specific date not confirmed from Cisco. (Set 04)
- Running instances of EPNM and EMS to be provided "when we get to that stage." Access timing not resolved. (Set 06b)
- Inventory of screens already ported to EMS vs. screens remaining in EPNM only is an explicit discovery deliverable but has not yet been produced. (Set 06c)
- Coexistence of "classic view toggle" framing (Set 03) and "240 to 260 screens converted end-to-end" language (Set 06) is an unreconciled scope articulation that the execution session should be aware of; the POC is only on two screens (Inventory and Fault Management) and the backend is explicitly out of scope for the POC.
- Items still pending at end of 06c (listed above under Set 06c) are unresolved as of the file date. If any are needed for POC framing, they remain open.
- The POC itself was originally described (Set 04) as "80-hour POC, Colin solo, April" covering "2-3 screens + pattern foundation," which predates the current two-screen (Inventory and Fault Management) POC scope that frames this handoff.
