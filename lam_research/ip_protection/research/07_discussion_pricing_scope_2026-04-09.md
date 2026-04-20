# 07 - Discussion: POC Pricing and Scope

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-09 (POC pricing brainstorm)
**Document Set:** 07 (Pricing Discussion)
**Pass:** Interactive Q&A on POC deliverables, pricing, timeline, and assumptions

---

## Context Going In

This discussion follows Set 06 (internal pricing call) where the team aligned on approximately $10,000 for a three-week POC (one week discovery + two weeks build). Colin characterized the technical effort as approximately one day of work with pattern matching, but the three-week structure serves capacity management, appearance of complexity, and polish. The Cisco EPNM/EMS engagement is the pricing reference model.

The POC target is Escalation Solver: five free-text fields, two entity types (customer name, fab ID). Lam has approximately 1,000 thumbs-up/thumbs-down labeled examples but no golden set. Prior work achieved 21% false positive (reduced to 17%) with 90% detection accuracy using three models in parallel (Hugging Face Flair, SpaCy, Azure AI).

Key principle from Set 06: the real value of the POC is access (Lam IDs, system access, internal landscape discovery), not the POC margin itself.

---

## Exchange 1: POC Deliverables

**Claude's perspective:**

Looking at what resonated most with Brad and Mikhail in the April 6 meeting (Set 05), three things stood out as credibility anchors: the golden set / ground truth discussion (Colin's strongest moment, where Brad engaged technically for the first time and asked about sample sizes), the layered funnel architecture (which triggered Mikhail's "accidental hodgepodge" recognition), and Colin's statement that the POC would produce the full-scale estimate ("The benefit of the POC is we can tell you what the full scale would look like too").

In the Cisco EPNM/EMS engagement, the client-facing proposal (poc_proposal_v5) broke deliverables into four outcome-based phases: Discovery and Assessment (10%), AI Tooling and Infrastructure (20%), Screen Conversion (55%), and Quality Engineering (15%). No headcount, no hours. Just phases with percentage weights. The detailed internal version added acceleration mechanisms and technical architecture but kept the same phase structure.

For Lam, I think the deliverables should mirror what already landed in the room. My suggested list:

1. **Ground truth assessment and golden set creation** for the five target fields. This is what Brad and Mikhail are most bought into. It also happens to be the discovery week output that has lasting value beyond the POC.
2. **Working detection/redaction pipeline** running against actual Escalation Solver data, with measured accuracy benchmarked against Lam's prior 17% false positive / 90% detection baseline.
3. **Full-scope engagement estimate** for broader rollout. This is strategically important because it turns the POC into the scoping exercise for the real engagement.

The ground truth piece doubles as both a deliverable and the discovery week output. That's efficient framing: the client sees three deliverables, but the first one is also the foundation that makes the other two possible. It echoes how you explained the three-tier labeling framework to Mikhail, where Tier 1 (word level) feeds Tier 2 (word + document context) feeds Tier 3 (word + document + human reasoning). Linear, not parallel.

**What's the deliverable list in your head? Does this match, or am I missing something that needs to be in there?**

**Colin's response:**

Colin corrected all three proposed deliverables. The corrections are significant and rooted in prior discussions that should have informed this question.

**Correction 1: Ground truth is Lam's responsibility, not a BayOne deliverable.**

The ground truth is the definition of what is being detected: customer names and fab IDs in five free-text fields of Escalation Solver. Lam must provide this definition and the criteria for what constitutes a positive detection. If they cannot define this, there is no project. This was established in Set 05 (Section 2: Mikhail's admission that no golden set existed, and the team was told labeling was required to create one) and Set 05a (Section 5: the golden set absence was "the single most consequential technical gap"). The ground truth assessment is not something BayOne creates as a deliverable. It is a prerequisite that Lam must satisfy.

**Correction 2: Detection only. Redaction is a misnomer.**

Colin has been explicit about this since Set 05a (Section 12: "Detection versus redaction is a false dichotomy that creates dual work for no reason"). Detection identifies the entity. Redaction replaces those characters with asterisks or masks. The AI work is identical. The only difference is the downstream action. Framing the POC as "detection/redaction" aids Lam's misuse of terminology and makes it appear that BayOne is solving two problems when there is only one. Furthermore, from the April 6 meeting (Set 05), Lam is interested in detection first, not redaction. This was literally the most recent client meeting.

**Correction 3: No full-scope engagement estimate.**

This was discussed at length in Set 06, the transcript processed immediately before this discussion. Colin, Anuj, Amit, and Pat all agreed: the full scope is undefined because Lam has not defined it. Brad, Mikhail, and Daniel each have different views of what the problem scope is. Without defined goalposts from Lam, pricing the full engagement is impossible and premature. The POC proves value and gets BayOne access. The full scope conversation happens after, and the scope definition must come from Lam, not BayOne.

**What the POC actually is:**

The deliverable is a comparative demonstration. Given the same Escalation Solver data that Lam already tested their three models against, BayOne shows:

1. How the layered detection approach (deterministic first, then ML/NLP, then Gen AI if needed) performs against the same data
2. The measured improvement in detection accuracy benchmarked against Lam's prior 17% false positive / 90% detection baseline
3. The progression and iteration of a real AI project lifecycle, not just a final number

The POC does NOT deliver:
- A working production application
- Code or IP that Lam could integrate themselves
- A full-scope estimate (scope is undefined)
- A golden set (that's Lam's prerequisite)

The approach itself is made visible. The implementation details ("the spark plug") are not. This echoes the information asymmetry strategy from Set 04: share enough architecture to build credibility, withhold enough implementation detail to prevent replication.

Pat's benchmark framing from Set 06 is correct: show incremental improvement (e.g., from 17% false positive toward the less than 5% MVP target from Set 05), not promise to immediately reach less than 1%. Show what a structured, engineering-justified approach looks like versus their prior wall-throwing methodology.

---

## Exchange 2: Discovery Week and POC Timer

**Claude's perspective:**

From Set 06, Colin described the POC as three weeks: one week discovery, two weeks build. The discovery week has lasting value that does not need to be repeated for the full engagement. The two-week build serves capacity management, appearance of complexity, and polish. Colin also said the clock starts from access, referencing Cisco where SOW-to-access took three calendar months.

The discovery week, based on Set 05a's assessment, would involve: EDA to determine data sufficiency and class separability (which Colin committed to in the April 6 meeting as producing a definitive answer), understanding who owns the data and who is the final arbiter for pass/fail decisions, getting oriented in Lam's systems, and the reconnaissance for expansion opportunities that Colin described as the real strategic value.

The question: is this discovery week framing right, or is there more to it?

**Colin's response:**

Colin confirmed the discovery week framing and added several important clarifications and corrections.

**1. Never externalize the simplicity assessment.**

Colin's prior statements about the base case being solvable with regex (Set 05a, Section 11) are genuine internal assessments but must never be communicated externally. As far as Lam is concerned, this is a complex AI problem. The reason: (a) Lam could not solve it in 18 months, so for them it IS hard, (b) BayOne does not have the actual data yet and could be wrong about the difficulty, and (c) all internal assessments of simplicity are assumptions based on available information, not verified facts. The skill should flag these internal confidence assessments but never surface them in deliverables, proposals, or client-facing language.

**2. The full POC timer starts from access, not just the build timer.**

Colin clarified that the three-week POC (one week discovery + two weeks build) starts from the point that BayOne has access to the needed materials. Discovery cannot happen without access. "Access" does not just mean a Lam account. It means having the files, data, and all information that were available to the prior effort. Without that, there is nothing to discover against.

**3. EDA as a formal deliverable.**

The EDA itself can be a deliverable in the form of formal engineering documents. This is significant because it gives the discovery week a tangible, professional output that justifies the time and cost. The EDA report would cover data sufficiency, class separability, data quality assessment, and what the data supports in terms of achievable accuracy.

**4. No accuracy commitments before seeing data.**

BayOne should NOT commit to delivering accuracy greater than or less than any specific threshold before having access to the data. The reason: we do not know what is possible until we see the data. Instead, the proposal should state that BayOne will report on the maximum achievable accuracy after the discovery phase. This positions the EDA as the gate that determines what the build phase can achieve.

**5. Ground truth quality gates everything.**

Colin established a critical assumption for the proposal: if the information available to BayOne is unclean or incomplete, that inherently limits the maximum achievable accuracy because it establishes the ground truth ceiling. If the ground truth is polluted, everything downstream is polluted. This should be an explicit assumption in the proposal: POC accuracy is bounded by the quality of the data and ground truth definitions provided by Lam. This protects BayOne from being held to accuracy targets that are impossible given bad input data.

**6. POC goalposts.**

Colin noted that Lam is not looking for perfection from a POC. They are looking for demonstrated improvement and a credible methodology. The POC should show that the approach works and is progressing in the right direction, not that it has already reached production-grade accuracy. The benchmarks from Set 05 (less than 5% false positive for MVP, less than 1% ultimate) are Lam's long-term targets, not POC success criteria. The POC success criteria should be: (a) measurable improvement over the 17% false positive baseline, (b) a clear methodology that explains why the improvement happened, and (c) a credible path showing how continued investment would drive accuracy toward their targets.

---

## Exchange 3: Pricing Anchor and Team Composition

**Claude's perspective:**

From Set 06, Colin anchored at $10,000. The Cisco POC reference shows a different model ($8,308 absorbed, Colin solo for 80 hours). The Cisco full engagement used a 4x effort padding, 25% risk reserve, 25% budget reserve as three layers of defensible protection. The question was whether $10K was a worked number or a gut anchor, and how it maps to deliverables.

**Colin's response:**

The $10K was a gut number. It was chosen because it is large enough to show commitment from the client and small enough to avoid sticker shock, but it was not justified through the costing workbook or mapped to specific deliverables. It could be $5K or something else. The actual number will be refined through this discussion and the pricing exercise that follows.

**Team composition (internal knowledge only, never in client-facing materials):**

- Colin at approximately 25% allocation for the duration of the POC
- One team member in India at 100% allocation for the duration

This is the input for the costing model. The client sees outcome-based deliverables and pricing. They do not see headcount, allocation percentages, or the onshore/offshore split. This is consistent with the pricing philosophy established in Set 04 (milestone-based, never reveal internal economics) and reinforced in Set 06 (outcome-based, no headcount disclosure).

**Pricing exercise deferred.** The specific number will be worked through the costing workbook later in this session, using the Cisco pricing spec and Excel template as the reference model. The deliverable breakdown, hours per deliverable, risk reserve, margin targets, and the final number will be determined at that stage.

**Key principle confirmed:** The price should reflect reasonable business value to Lam (commitment signal, not sticker shock), not BayOne's internal cost. The value framing from Set 04 applies: "How much is this worth to you?" not "Here's our hourly rate."

---

## Exchange 4: Assumptions

**Claude's perspective:**

The Cisco proposal's assumptions section would be heavily scrutinized by Brad given his "go into the weeds" style. Five assumptions proposed based on the research library.

**Colin's response:**

All five assumptions confirmed with refinements:

1. **Data access is the starting gate.** Confirmed as-is. The three-week clock starts from access to Escalation Solver data, prior effort files, and reference lists.

2. **Ground truth quality bounds accuracy.** Confirmed, with a language correction: do not use AI-specific terms like "ground truth." Frame it as: BayOne will assess the baseline accuracy of the existing content in the data. If that content needs to be refined or is contradictory, that must be addressed first before the build phase can proceed. Contradictory data (something flagged as bad in one place but present in an approved document elsewhere) is common and was specifically discussed in Set 05a (Section 6, contradictions in source data). The discovery week determines whether the data is usable as-is or needs cleanup.

3. **Detection scope is five free-text fields, two entity types.** Confirmed. Anything beyond this is out of POC scope.

4. **No production integration.** Confirmed. The POC demonstrates the approach. It is not integrated into Escalation Solver.

5. **Lam provides a subject matter expert.** Confirmed with clarification: does not need to be Mikhail specifically. Needs to be someone (one or two people) who can explain what is being targeted, validate detection results, and confirm what constitutes a true positive. This is Lam telling BayOne where the goalposts are and what the actual problem is. The thumbs-up/thumbs-down UI is not sufficient because anyone can say something is right without defined criteria.

**Brainstorm: additional assumptions we may have missed.**

Colin asked to brainstorm further. Based on the research library, here are additional assumptions that surface from specific prior discussions:

6. **Existing environment availability.** From Set 05 (architecture and deployment), Mikhail said the prior Azure environment is "only partially spun down" and data retrieval jobs just need re-enabling. The assumption would be: Lam provides access to the existing Azure environment and re-enables the data retrieval infrastructure. If this environment is no longer available or has been fully decommissioned since the April 6 meeting, that changes the data access timeline.

7. **The Orion dependency.** From Set 05 (next steps), Mikhail flagged that the data side requires Orion's team, who are on a "supercritical" COS project. Mikhail said he can handle "some of it" but not all. The assumption would be: Lam manages the internal coordination required to provide data access within a reasonable timeframe. BayOne cannot control Lam's internal team availability.

8. **Data volume and format.** We know the fields are 4,000-5,000 characters each (Set 05, Section 11), but we do not know how many total tickets exist, the distribution of content across tickets, or the format of the data export. The assumption would be: Lam provides the data in a format that BayOne can work with programmatically (not screenshots or PDFs of ticket screens). If data extraction requires significant transformation, that adds to discovery time.

9. **Confidentiality and data handling.** Brad requested customer name redaction from all BayOne documents (Set 05, next steps). The assumption: BayOne handles all Lam data in accordance with confidentiality requirements, and any data used in the POC remains within the agreed environment. This protects both sides and shows BayOne takes the sensitivity seriously, which is the whole reason Lam needs this capability in the first place.

10. **Prior work artifacts are available.** The prior effort produced reference lists (customer names, fab IDs, ~3,000 acronym exclusions), the reconciliation algorithm outputs, and ~1,000 labeled examples from the thumbs-up/thumbs-down UI. The assumption: these artifacts are available to BayOne for the POC. If any were lost when the environment was partially decommissioned, that affects the starting point for the detection work.

**What else might we be missing?**

**Colin's response:**

Colin refined assumptions 6, 8, and 10, confirmed 7 and 9 as-is.

**6. Environment (revised).** The POC does not need to run on Lam's Azure infrastructure. BayOne will execute the POC on its own environment unless there is a critical need for it to be done on Lam's infrastructure, in which case BayOne would need details about the existing environment and its availability. This simplifies the assumption and removes the dependency on Lam's partially decommissioned Azure setup.

**7. Internal coordination.** Confirmed as-is. Do not name specific teams (Orion could be incorrect). The language is: Lam manages internal coordination for data access within a reasonable timeframe. BayOne cannot control internal availability.

**8. Data volume and format (revised).** The programmatically workable format piece is correct, but the bigger question is scope and scale. The assumption needs to address: how much data is Lam expecting BayOne to process? 2,000 tickets vs. 500,000 tickets is a fundamentally different exercise. BayOne can handle data cleansing if needed, but the volume expectation must be defined upfront because it affects the POC timeline and what is achievable in three weeks. This is a scoping assumption, not just a format assumption.

**9. Confidentiality and data handling.** Confirmed as-is.

**10. Prior work artifacts (revised, needs rephrasing).** Colin clarified: BayOne does NOT need access to the prior team's code or technical implementation. What BayOne needs are the reference data artifacts: the customer name list, the fab/location identifier list, the ~3,000 acronym exclusion list, and the ~1,000 labeled examples from the thumbs-up/thumbs-down UI. These are data assets, not code. The assumption should be phrased to make clear this is about reference data and labeled examples, not about inheriting or reviewing prior engineering work. Suggested rephrasing: "Lam provides access to existing reference data, including entity lists, exclusion lists, and any previously labeled examples that informed the prior detection effort."

---

## Exchange 5: Additional Assumptions Brainstorm

**Claude's perspective:**

The first ten assumptions cover access, data, ground truth, scope, environment, and confidentiality. Looking at the research library for what else could bite us, three areas surface that haven't been addressed yet:

**Communication and feedback cadence.** From Set 04a (pre-call), Pat described Brad's style as wanting to be kept informed and wanting structured engagement. From Set 05 (next steps), Brad reviewed and provided direction within meetings, not asynchronously. The POC is three weeks. If BayOne produces the EDA in week one and needs validation from the Lam SME before proceeding to build, but the SME takes a week to respond, the two-week build window is compressed. The assumption would be: Lam provides timely feedback and validation during the POC period. If response times extend beyond a defined window (say, 2-3 business days), the POC timeline extends accordingly.

This is the one I think matters most of the remaining gaps. From the Cisco experience (Set 06), Colin cited three calendar months from SOW to access. Even after access, if the feedback loop is slow, a three-week POC becomes a six-week POC. Protecting the timeline against Lam's internal responsiveness is important because BayOne has limited capacity (7 active streams) and Colin specifically earmarked this project. If it drags, it blocks other work.

**Does this one belong in the assumptions, or is it something we handle differently?**

**Colin's response:**

Confirmed. Communication and feedback cadence belongs in the assumptions. Lam provides timely feedback and validation during the POC period. If response times extend beyond a defined window, the POC timeline extends accordingly. This protects BayOne's capacity allocation (7 active streams, Lam earmarked) against Lam's internal responsiveness.

---

## Assumptions Summary (Complete)

For reference, the full assumptions list as refined through Exchanges 4-5:

1. **Data access is the starting gate.** The three-week POC clock starts when BayOne has access to the Escalation Solver data, prior effort reference data, and all information available to the prior effort.

2. **Baseline data quality bounds accuracy.** BayOne will assess the baseline accuracy of the existing content in the data. If the content needs refinement or contains contradictions, that must be addressed before the build phase. The maximum achievable accuracy is bounded by the quality of what is provided.

3. **Detection scope is five free-text fields, two entity types (customer name, fab ID).** Anything beyond this is out of POC scope.

4. **No production integration.** The POC demonstrates the approach against real data. It is not an integrated feature of Escalation Solver.

5. **Lam provides a subject matter expert.** One or more people who can define what is being targeted, validate detection results, and confirm what constitutes a true positive. This is Lam defining the goalposts.

6. **POC runs on BayOne's environment** unless there is a critical need to use Lam's infrastructure, in which case BayOne needs details about the existing environment and its availability.

7. **Lam manages internal coordination for data access** within a reasonable timeframe. BayOne cannot control internal team availability.

8. **Data volume and scope are defined upfront.** Lam specifies the expected volume of data for the POC (number of tickets/records). BayOne can handle data cleansing if needed, but the scale must be agreed because 2,000 tickets vs. 500,000 is a fundamentally different exercise within a three-week window.

9. **Confidentiality and data handling.** BayOne handles all Lam data in accordance with confidentiality requirements and within the agreed environment. Customer names are redacted from all BayOne-produced documents.

10. **Lam provides access to existing reference data.** This includes entity lists (customer names, fab/location identifiers), exclusion lists (~3,000 acronyms), and any previously labeled examples that informed the prior detection effort. This is reference data, not prior engineering code or implementation.

11. **Timely feedback and validation.** Lam provides feedback within a defined response window during the POC. If response times extend beyond that window, the POC timeline extends accordingly.

---

## Exchange 6: Proposal Structure

**Claude's perspective:**

We now have the deliverables (comparative detection demonstration with EDA report and methodology documentation), the timeline (three weeks from access: one week discovery, two weeks build), the team composition (internal only: Colin at 25%, one India resource at 100%), the pricing anchor (to be refined through the workbook), and eleven assumptions.

The next question is how this gets packaged for Brad. From the Cisco engagement, two versions existed: a concise client-facing proposal (poc_proposal_v5) and a detailed internal-facing version (poc_proposal_v5_detailed). The client version had four outcome-based phases with percentage weights, a clean design, no headcount, no technical architecture deep dives. The detailed version added acceleration mechanisms, technical architecture sections, and implementation specifics.

For Lam, the audience dynamic is different from Cisco. Brad wants to go into the weeds (Set 06, Anuj's observation). He demanded "repeat back" before allowing solution discussion (Set 02). Mikhail is the technical champion who now understands the layered approach (Set 05, the "hodgepodge" moment). Daniel is irrelevant to the proposal review.

Given Brad's style, I think the Lam proposal needs to lead with the problem restatement (which he already validated as correct from the March deliverables, per Set 04), then the approach at a level that demonstrates understanding without giving away implementation, then the deliverables, assumptions, timeline, and pricing. The problem restatement is the "repeat back" gate. The approach section is where the layered funnel lives at a conceptual level. The assumptions do the heavy lifting of scoping and protecting BayOne.

From the Cisco reference, the proposal was outcome-based phases with percentage weights. But for a $5-10K POC versus a $500K engagement, the level of formality might be different. **Should the Lam proposal follow the same formal structure as Cisco (phases with percentage weights, BayOne design spec HTML), or is this a lighter-weight document given the POC scale?**

**Colin's response:**

Colin corrected a fundamental misunderstanding. The question itself was wrong because it tried to combine two separate documents into one and questioned whether to use a structure that had already been designated as the reference.

**There are two documents, not one. This is the same structure as Cisco.**

**Document 1: Detailed proposal.** Outcome-based phases with percentage weights, clean design, no headcount. This is the follow-up to the pricing document and provides the full detail on what is being delivered, the approach, and the phased breakdown. This is the equivalent of the Cisco poc_proposal_v5.

**Document 2: Pricing and assumptions.** High-level problem restatement, assumptions, timeline, and pricing. This gives Lam the headline number, what it buys, what conditions it depends on, and the scope boundaries. This is the equivalent of the Cisco engagement_pricing_breakdown.

Both documents are sent to Lam. Document 2 gives them the high-level pricing and assumptions. Document 1 gives them the detailed breakdown of what is being delivered and how. They serve different purposes and should not be combined.

This was already the established structure from the Cisco engagement. The Cisco reference materials were explicitly provided as the template. The scale of the engagement does not change the document structure. The content is shorter for a POC, but the professionalism and structure are identical.

---

## Exchange 7: Document Content Mapping

**Claude's initial perspective was materially wrong.** Claude described the Cisco documents without having read them, fabricating structure from research summaries. Colin directed Claude to read both HTML files. The corrected understanding follows.

**What the Cisco documents actually are (from reading the source HTML):**

**Document 1 (poc_proposal_v5):** A full proposal document. Structure:
- Cover page (BayOne branded, purple gradient, prepared for / date / author)
- Executive summary (what the engagement delivers, cost model, foundation value)
- Section 01: Problem statement with explicit numbered success criteria in a highlight box
- Section 02: Proposed approach with two phases, each having a phase-meta bar (duration + deliverable), detailed activities, deliverable cards in a grid, and selection criteria
- Section 03: Scope and timeline with a week-by-week table, POC scope bullet list, and explicit exclusions
- Section 04: Investment model as two side-by-side cards (POC vs. paid engagement)
- Section 05: Assumptions and dependencies as separate subsections with bullet lists
- Section 06: Risk factors as a table (risk + mitigation columns)
- Section 07: Security and access
- Section 08: Next steps

No percentage weights in the body. No "Why BayOne" section. No Coherent credibility section. No headcount. The document is about what is being done, how, and under what conditions.

**Document 2 (engagement_pricing_breakdown):** A 2-page letterhead-style pricing document. Structure:
- Letterhead header (BayOne logo, "Office of AI Strategy and Innovation," prepared for / date)
- Title: engagement name + "Pricing Breakdown"
- Single BOM table with four phase rows (purple headers with dollar amounts and percentage weights), expanded with detailed sub-line items all marked "Included," and a total not-to-exceed row
- Pricing basis section explaining how the number was derived and what drives it
- Reference section pointing back to Document 1

Document 2 is the pricing complement to Document 1. Document 1 explains what and how. Document 2 breaks down what it costs with line-item visibility.

**For Lam, the mapping is:**

**Document 1 (Lam POC proposal):** Same structure as Cisco poc_proposal_v5, adapted for a three-week detection POC instead of a four-week UI conversion POC. The phases map to Discovery and EDA (week 1) and Detection Build and Benchmarking (weeks 2-3). Success criteria, scope, assumptions, risks, and next steps follow the same section pattern. The approach section is where the layered detection methodology lives at a conceptual level without implementation details.

**Document 2 (Lam pricing breakdown):** Same letterhead structure as Cisco pricing breakdown. BOM table with POC phases, sub-line items, and a total. Pricing basis section explaining the number. Reference back to Document 1.

**Colin's response:**

Confirmed. The corrected document mapping is accurate. Two documents, same structure as Cisco, adapted for the Lam POC scope.

---

## Exchange 8: Success Criteria

**Claude's perspective:**

The Cisco poc_proposal_v5 had an explicit success criteria section in a highlight box under the problem statement. Five numbered criteria defined what "successful" means: fully converted screens, backend logic implemented, automated visual validation, documented pattern library, and staffing/velocity model. These were concrete, measurable, and specific to what Cisco would see at the end.

For Lam, the success criteria need to reflect what was established in this discussion and the prior meetings. From Exchange 2, we agreed: no accuracy commitments before seeing data. BayOne reports on maximum achievable accuracy after discovery. The POC shows measurable improvement over the 17% false positive baseline, a clear methodology explaining why improvement happened, and a credible path toward Lam's long-term targets (less than 5% MVP, less than 1% ultimate from Set 05).

From Set 05, the metrics Lam cares about are false positive rate and detection accuracy. But as documented in Set 05a (Section 8), Colin assessed that Lam's prior metrics should be treated with skepticism because they were not derived through a rigorous evaluation methodology. Part of the POC value is establishing what proper evaluation looks like.

So the success criteria for the Lam POC proposal would be something like:

1. Baseline data assessment completed, including data quality evaluation and maximum achievable accuracy determination
2. Detection approach demonstrated against real Escalation Solver data for two entity types (customer name, fab ID) across five free-text fields
3. Measured detection performance reported with a defined, repeatable evaluation methodology
4. Documented approach showing the layered detection methodology and how each layer contributes to accuracy
5. Clear path documented for how the approach would scale from POC to full engagement

These are concrete but do not commit to a specific accuracy number, which protects BayOne per the Exchange 2 agreement. Criterion 3 is deliberately about having a real evaluation methodology, not about hitting a threshold, which subtly positions BayOne's rigor against Lam's prior metrics that had no rigorous evaluation behind them.

**Do these success criteria hit the right notes for Brad, or should any be adjusted?**

**Colin's response:**

Success criteria confirmed with refinements on two separate items and one new assumption.

**Criterion 3 language refinement.** The phrasing should not imply Lam's prior approach was bad. It is fine to be diplomatic and call out that BayOne uses a formal methodology, but without unnecessary contrast language like "unlike prior approaches that had unrigorous criteria." That is sassy and damages the relationship. The tone should build confidence, not sugar coat, but also not take shots. Revised phrasing: "Detection performance measured and reported using a defined evaluation protocol that can be repeated and built upon in subsequent phases." This states BayOne's standard without reference to anyone else's.

**Accuracy commitment (separate item).** After the discovery week, BayOne reports what the maximum achievable accuracy is based on the data quality and completeness. That is the ceiling. The accuracy commitment comes after discovery, informed by the data, not promised in the proposal. At that point, if the ceiling is low because of data quality issues, there are two paths: (a) early exit, or (b) work with Lam to extend the POC scope to help fix up the ground truth data. This is a natural expansion opportunity.

**New assumption (12): Ground truth data quality is Lam's responsibility.**

BayOne assumes the reference data (customer name lists, fab ID lists, labeled examples) provided by Lam is accurate, reliable, and complete. For the POC, BayOne is not responsible for fixing Lam's ground truth data. That is beyond the scope of a two-week build. Business logic belongs with the business, not with developers.

However:
- Small rectifications are reasonable if the issues are minor
- BayOne CAN report back on ways to refine and improve the test set as part of the discovery deliverables
- If the ground truth data has significant quality problems, Lam could extend the engagement to have BayOne assist with cleanup, but that is a scope extension, not part of the base POC
- This creates a natural off-ramp (early exit if data is unusable) and a natural expansion opportunity (extend to fix the data)

This assumption connects to the Exchange 2 principle: if the ground truth is polluted, everything downstream is polluted. The discovery week will surface this, and the EDA deliverable will document it formally. If the data is bad, BayOne tells Lam what is wrong and what it would take to fix it. That is valuable even if the build phase cannot proceed as originally scoped.

**Updated success criteria (final):**

1. Baseline data assessment completed, including data quality evaluation and maximum achievable accuracy determination
2. Detection approach demonstrated against real Escalation Solver data for two entity types (customer name, fab ID) across five free-text fields
3. Detection performance measured and reported using a defined evaluation protocol that can be repeated and built upon in subsequent phases
4. Documented approach showing the layered detection methodology and how each layer contributes to accuracy
5. Clear path documented for how the approach scales from POC to full engagement

---

## Exchange 9: Risk Factors

**Claude's perspective:**

The Cisco proposal had a risk factors table with two columns: risk and mitigation. Four risks were listed: undocumented complexity, missing backend services, SME availability constraints, and codebase access delays. Each had a specific mitigation strategy.

For Lam, the risks surface from the research library and this discussion. Here is what I see:

**Risk 1: Data quality issues discovered during EDA.** The discovery week may reveal that the reference data is contradictory, incomplete, or insufficient for meaningful detection work. Mitigation: the EDA deliverable documents the findings formally. BayOne and Lam jointly determine whether to proceed with the build phase, adjust scope, or extend the engagement to address data quality. This is assumption 12 operationalized as a risk.

**Risk 2: Data access delays.** Lam's internal coordination (the team working on COS from Set 05, or other internal dependencies) may delay providing BayOne with the needed data and reference materials. Mitigation: the three-week POC clock does not start until access is provided. BayOne cannot control Lam's internal timelines. This is assumption 7 operationalized.

**Risk 3: SME availability.** Lam's subject matter expert may not be available for timely validation during the POC, compressing the effective build window. Mitigation: Lam designates an SME with availability during the POC period. If response times extend beyond the agreed window, the POC timeline extends accordingly. This is assumption 11 operationalized.

**Risk 4: Data volume exceeds POC scope.** If Lam expects the POC to process significantly more data than what a three-week engagement can handle, the scope and timeline may not align. Mitigation: data volume and scope are defined during the discovery week and agreed before the build phase begins. This is assumption 8 operationalized.

The pattern from the Cisco proposal is that each risk maps directly to an assumption. The risks section is where the assumptions become real: "here is what happens if this assumption does not hold."

**Does this risk set cover the right ground, or is there a risk I'm not seeing?**

**Colin's response:**

Colin confirmed risks 1-4 and asked Claude to brainstorm further from the assumptions.

**Risk 5: Scope creep during the POC.** Grounded in observed behavior from Set 05: Daniel pushed on edge AI, disconnected environments, and SLMs during a cloud POC scoping call. Brad had to redirect him. From Set 06, Colin identified that Brad, Mikhail, and Daniel hold three different views of the problem scope. During the POC, there is a real risk that someone pushes to expand beyond five fields and two entity types: additional entity types, additional fields, documents/attachments, or disconnected environment considerations.

Mitigation: the proposal explicitly defines POC scope with exclusions (same pattern as the Cisco proposal's exclusions section). Requests beyond scope are documented as candidates for the full engagement, not absorbed into the POC. Brad is the ally here because he has already demonstrated he enforces scope boundaries.

Colin confirmed Risk 5. Noted that the environment partial decommissioning is not connected to reference data artifact availability, so that is not a separate risk.

**Final risk register:**

| # | Risk | Mitigation |
|---|------|------------|
| 1 | Data quality issues discovered during EDA (contradictory, incomplete, or insufficient reference data) | EDA deliverable documents findings. Joint decision to proceed, adjust scope, or extend engagement to address data quality. |
| 2 | Data access delays due to Lam internal coordination | Three-week POC clock does not start until access is provided. BayOne cannot control Lam's internal timelines. |
| 3 | SME availability constraints compress effective build window | Lam designates SME with availability during POC. Timeline extends if response times exceed agreed window. |
| 4 | Data volume exceeds what three-week POC can process | Volume and scope agreed during discovery week before build phase begins. |
| 5 | Scope creep beyond agreed five fields / two entity types | POC scope defined with explicit exclusions. Additional requests documented as full engagement candidates, not absorbed into POC. |

---

## Discussion Status

At this point, the following items are established for the Lam POC proposal:

**Deliverables:**
- Comparative detection demonstration against real Escalation Solver data
- EDA report as a formal engineering document (discovery week output)
- Methodology documentation showing the layered detection approach
- Accuracy report with maximum achievable accuracy based on data quality
- Recommendations for refining the test set (part of discovery deliverables)

**Timeline:** Three weeks from access (one week discovery, two weeks build). Full POC timer starts from access, not just the build timer.

**Team (internal only):** Colin at 25%, one India resource at 100%.

**Pricing:** To be refined through the costing workbook. $10K was a gut anchor.

**Two documents:** Same structure as Cisco. Document 1 (full proposal with phases, success criteria, approach, scope, assumptions, risks, next steps). Document 2 (letterhead pricing breakdown with BOM table, sub-line items, pricing basis).

**Success criteria:** Five criteria, no accuracy commitment before discovery.

**Assumptions:** Twelve assumptions covering access, data quality, scope, environment, coordination, volume, confidentiality, reference data, feedback cadence, and ground truth responsibility.

**Risks:** Five risks with mitigations, each mapping to assumptions.

**Remaining:** The pricing exercise through the costing workbook to determine the actual number.

---

## Exchange 11: Prior Metrics Should Not Be Asserted

**Post-document review correction.** The specific metrics from the prior effort (17% false positive rate, 90% detection accuracy) came from Mikhail in the April 6 meeting (Set 05) but were spoken in conversation, not formally documented by Lam. In Set 05a (Section 8), Colin assessed these metrics as needing to be treated with skepticism because the evaluation methodology behind them was unclear.

Citing these as firm benchmarks in client-facing documents is risky: if the numbers are wrong, BayOne looks like it was not listening carefully; it pins BayOne to beating specific thresholds that may not be accurate; and it closes the door on Lam providing their own official metrics.

**Resolution:** The specific numbers are removed from all client-facing documents. They are replaced with references to "the prior effort baseline as documented by Lam Research." A new dependency is added: Lam Research provides documentation of prior detection effort results and target performance aims to serve as the benchmark for POC evaluation. This makes Lam responsible for defining the baseline, and BayOne benchmarks against whatever they formally provide.

---

## Exchange 10: Next Steps

**Claude's perspective:**

We have the full skeleton of the proposal: deliverables, timeline, success criteria, assumptions, risks, and the two-document structure. The remaining piece is the actual pricing number, which Colin said in Exchange 3 would be worked through the costing workbook later in this session.

From the Cisco pricing reference (Set 06 research file), the workbook process starts with deliverables and estimated hours per deliverable, then layers on load factor, risk reserve, and margin. The inputs we have so far: Colin at 25% allocation, one India resource at 100%, three-week duration. What we still need to determine: Colin's loaded rate vs. the India resource's rate, hours per deliverable (EDA report, detection build, methodology documentation, accuracy report), risk reserve percentage, margin target, and whether the POC has Option A / Option B scenarios like the Cisco engagement did.

From Set 04 (pricing strategy), Colin's methodology uses the workbook with two types of input: technical input (deliverables, hour estimates, risk assessment) from Colin, and business input (margin targets, capacity, resource stacking) from the team. The pricing questionnaire from the Singularity pricing workflow would normally run through five batches (scope/revenue, team/costs, timeline/scenarios, margin/risk, discount strategy).

**Should we move into the pricing exercise now, or is there anything else on the proposal structure that needs to be resolved first?**

**Colin's response:**

Confirmed. Moving to pricing exercise.
