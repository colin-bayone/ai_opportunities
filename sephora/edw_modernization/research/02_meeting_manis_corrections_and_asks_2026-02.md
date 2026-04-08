# 02 - Meeting: Mani's Corrections and Engagement Requirements

**Source:** /sephora/edw_modernization/source/mani_transcript2_formatted.txt
**Source Date:** 2026-02 (Colin's First Meeting with Mani)
**Document Set:** 02 (Mani Meeting 2)
**Pass:** Focused deep dive on Mani's corrections, requirements, and engagement asks

---

## 1. The Critical Framing Correction: "This Is Not Migration, This Is Re-Engineering"

This is the single most important correction Mani made during the meeting. Colin opened with a summary of his understanding (lines 1-16), which was generally well-received, but Mani immediately and emphatically corrected the framing around what this initiative actually is.

**Colin's opening summary (lines 3-16) described:**

- A "three year EDW project to migrate from some legacy on-prem" infrastructure over to Databricks
- Reports in Cognos and SSAS cubes being "migrated over to something like ThoughtSpot and Tableau"
- Pipelines "migrated" from DataStage to Databricks pipelines
- Cognos being retained during transition
- A semantic layer that needs to be "created and formed"
- Pain points around the scale of the "migration"

Colin used the word "migrate" or "migration" repeatedly in this summary. He was deliberately staying high-level ("not going into any detail intentionally here, just want to make sure I'm on the right track" --- line 16).

**Mani's validation followed by correction (lines 17-34):**

Mani first validated: "You summarized it very well on here. I think you understood it very well" (lines 18-19). But then he delivered the critical correction:

> "Not everything is being translated to [Tableau]. And this is not a migration initiative. This is completely re-engineering [initiative]. That's one thing that we are making very clear, and that's why [we] are not calling this migration [but] modernization." (lines 20-23)

He then explained the distinction with precision (lines 24-27):

> "If it is migrated, it's lift-and-shift, or it's moving the data from here to there, or it is moving something from one place to another place. But in this particular context, it's not just migration. We have to re-engineer that. We have to re-engineer and rewire [these] things." (lines 24-27)

**What Mani is communicating:**

- The word "migration" implies lift-and-shift --- taking existing logic, reports, and pipelines and moving them as-is from one platform to another. That is NOT what Sephora is doing.
- "Modernization" is the correct term because they are fundamentally re-engineering the underlying architecture, not just porting code.
- This distinction is not semantic nitpicking --- it reflects the actual scope and complexity of the work. Re-engineering means rethinking how things are built, not just where they run.
- Mani said "that's one thing we are making very clear" --- this is a deliberate, organization-wide framing choice, likely reinforced in how the project is communicated to leadership and stakeholders.

**Implication for all future deliverables:** Every document, proposal, and conversation must use "modernization" or "re-engineering" --- never "migration." This is a term Mani has clearly drawn a line around.

## 2. Correction: Front End (Cognos) Is Being Retained, Not Replaced

Mani clarified that the front-end reporting layer --- specifically Cognos --- is being retained in most cases. Colin's summary had implied a more wholesale transition to ThoughtSpot and Tableau.

**Mani's correction (lines 28-33):**

> "In some cases, like most cases, we are trying to retain the front end of it, which is, if it is Cognos, it will remain in Cognos. There is a desire to move to ThoughtSpot or Tableau, but that's not something that we are pursuing. So right, the change management is not --- it's not so resistant. That's why [we're] keeping [it]." (lines 28-32)

**What this means:**

- The Cognos front end stays. Users continue to interact with the same reporting interface they know.
- There is a "desire" to move to ThoughtSpot or Tableau eventually, but that is explicitly NOT being pursued as part of this initiative.
- The rationale is change management: by keeping the front end the same, they avoid user resistance and reduce the scope of organizational change.
- The re-engineering happens underneath --- the data platform, pipelines, and architecture change, but the user-facing reporting layer remains familiar.
- This is a deliberate strategic choice, not a limitation. It reduces risk and keeps the focus on the data platform transformation.

**Implication for the proposal:** BayOne's AI-assisted approach should focus on the data layer re-engineering (pipelines, business logic, data transformations), not on front-end reporting tool migration. The Cognos interface is staying.

## 3. Mani's Stance on Semantic Layer: Pragmatism Over Perfection

Colin raised the semantic layer question directly (lines 128-131), asking whether common data definitions across the organization were well-established.

**Mani's response was nuanced and pragmatic (lines 132-161):**

> "Semantically, we need to check with [Grishi] on this." (line 132)

He then gave his own view:

> "Semantically, in my view, we are not going to address that everything as a one shot... It's virtually an ongoing effort. And we are not going to go to, you know, [put] too much effort in having common definitions, common [terminology]. Even [I'll attest], you know, it. But if that kind of slows down our work in this, then we will not [pursue] that." (lines 134-138)

And more directly:

> "We have to keep [making] progress. That's important. It's good to have a semantic layer. [But] if that [semantic layer is] slowing us down, then we [will] just go ahead and [do] the engineering implementation." (lines 140-143)

**Then the Grishi caveat (lines 145-149):**

> "I would say from my point of view, [but] Grishi, of course, [may] see differently. [I] would let [Grishi] design these things. If she feels [she's] good to define the layer and actually [build] the physical parts of the semantic layer, what exactly has to go into those things? If she feels confident that she can do this and she can [execute on] it and even if it slows down --- [I'd] probably [allow] that." (lines 145-149)

**What this reveals about decision dynamics:**

- Mani's personal philosophy is progress over perfection. He would rather keep the modernization moving than get bogged down defining a perfect semantic layer.
- However, Grishi has the authority to make a different call. If Grishi is confident she can define and build the semantic layer without derailing the timeline, Mani would defer to her judgment.
- This tells us Grishi is the technical decision-maker on architecture and implementation approach. Mani sets the strategic direction and pace expectations, but Grishi owns the execution decisions.
- Mani explicitly named the risk: "That's exactly where people get carried away. People get into a platform and they will get too much into defining that versus losing the visibility of the outside layer" (lines 156-157). He has clearly seen semantic layer efforts derail modernization projects before.

**Mani's confidence in the team (lines 159-160):**

> "I think actually Grishi and Andrew would be good to do it. They have the right people to do that."

This is an endorsement of Grishi and Andrew Ho's capabilities on the semantic layer question specifically.

**Implication for the proposal:** Do not lead with semantic layer as a major AI opportunity. Mani views it as a potential trap. If BayOne proposes AI-assisted semantic layer work, frame it as an accelerator that prevents the slowdown Mani fears --- not as a standalone workstream that adds scope.

## 4. Validation: "Your Approach Looks Good"

After Colin presented his slide deck (lines 186-293), Mani gave explicit validation.

**Mani's response (lines 294-296):**

> "Your approach all looks good. This is exactly what the thing is right now --- [how we're] approaching [and] progressing. Finance is the first thing that [we] have taken." (lines 294-296)

This is significant because:

- Mani confirmed that Colin's AI-assisted modernization approach aligns with how Sephora is already thinking about the problem.
- He confirmed the sequencing: finance is the first category track.
- The validation was unqualified --- "all looks good" --- with no caveats or corrections on the approach itself.

## 5. The "Unique Value" Question

Immediately after validating the approach, Mani pushed for differentiation (line 297):

> "I'm trying to understand what is the value or unique thing that you want to present here." (line 297)

This is a direct challenge: if the approach is aligned with what they are already doing, what does BayOne specifically bring that they do not already have?

**Colin's answer focused on two things (lines 298-314):**

1. **Experience:** "Have you done this before? We know the pain points. We know where things [get stuck]. We also know the balance is tough to find. And sometimes it does exist internally. But unfortunately, if it's [only] internal, that does take people [away from other work]." (lines 300-306). Colin positioned BayOne's differentiation as having lived through a similar re-engineering effort and knowing where the pitfalls are.

2. **AI-first integrated approach:** "What we can do differently than most is we can work with [your] teams. Because [we have] AI as [a core] strategy. So you don't want to [create] silos... If there's already ongoing initiatives at the company, what we can do, even with these [AI]-assisted items, we can work with them [alongside]. We can [integrate] with [existing efforts] so that this becomes kind of a unified platform for you --- you're not creating silos while you're trying to solve a modernization." (lines 310-314)

**Mani's follow-up (line 316):**

> "Are you more [proposing] that you can [deliver] the specific [work] or you can [staff for] it?"

Mani is asking a clarifying question: is BayOne proposing to deliver a specific AI solution, or to provide staff/resources? This suggests he wants to understand the engagement model --- are you a solutions partner or a staffing partner?

**Colin's answer (line 317):** "Yes, that's right" --- affirming both. BayOne can do either or both.

## 6. The Case Studies Ask

Mani asked directly for proof of prior work (line 319):

> "But you've done something similar to this --- do [you] have any case studies or examples?"

Colin confirmed and offered to show them immediately (lines 320-325), but Mani was out of time. Colin committed to sending case studies after the meeting.

**What Colin planned to send (lines 336-341):**

- A Snowflake case study (described as "more architecture" and implying the customer "gives a lot more freedom in that way than [Databricks] does, which is both a benefit and a curse")
- A Databricks case study focused on "building the custom connectors and helping to do that"

**Implication:** Mani expects tangible proof that BayOne has executed similar re-engineering work before. Abstract capabilities pitches will not suffice. The case studies need to demonstrate hands-on delivery, not just consulting advice.

## 7. The "Specific Category Example" Ask

Mani made a concrete request for the proposal (lines 344-348):

> "[Take] a specific example with certain assumptions --- approximately [what would be] the [timeline]. Cost [would] depend upon the [scope] of it and then the [specifics]." (lines 346-348)

**What Mani is asking for:**

- Pick a specific category (e.g., one of the report tracks like supply chain or merchandising)
- Make stated assumptions about the scope
- Provide an estimated timeline for completing that category
- Cost estimates that are tied to the scope

He is not asking for a vague "it depends" proposal. He wants a concrete, tangible example: "For category X, assuming Y reports of Z complexity, we estimate A timeline at B cost." This is how he evaluates whether BayOne can actually execute.

**Which category to target:** Colin asked Mani about this directly (lines 365-376). Mani noted that finance "has already progressed" and would be "almost done" in another 20-odd days (lines 369-370). He suggested supply chain or merchandising as possibilities, noting that merchandising involves stakeholders including Grishi and Michael (lines 374-377). The specific category was not definitively chosen in the meeting --- Mani indicated Colin should "check with Grishi" and coordinate through her.

## 8. The "Three Options" Instruction

Mani gave explicit, specific guidance on proposal structure (lines 378-383, 449-453):

> "Come up with some options, I would say. One option is for you to take it entirely. Second [option, the] same piece to work [but where you do] the architecture and design [while the] team [handles implementation] --- [the team is a] table [of] people coming from [different places] --- there are people from [the data] platform, there are people from [the engineering] team. So people coming from different angles and places. So, the architectural design is kind of done by the [team], and then you can take [the] implementation." (lines 378-382)

And later:

> "Let me see that we do 3 options. Don't over [do it] --- like 7 options, that would be too much. Maybe just [restrict] to maybe 3 options. And then maybe like one type of [category] would go for [one] option, another category for another option." (lines 449-452)

**What Mani is prescribing:**

1. **Option 1: Full ownership** --- BayOne takes the category end-to-end (architecture, design, and implementation)
2. **Option 2: Implementation only** --- Sephora's cross-functional team (data platform, engineering, etc.) does the architecture and design; BayOne takes the implementation
3. **Option 3: Implied** --- Likely a lighter-touch or hybrid model (given the flexibility discussion that follows)

**The "different category per option" instruction:** Mani suggested that each option could apply to a different category. So Option 1 might be applied to merchandising, Option 2 to supply chain, and Option 3 to a third category. This way the proposal demonstrates versatility and gives Mani multiple entry points to engage.

**The "don't give me seven options" directive:** Mani explicitly does not want a complex, exhaustive proposal. Three options. Keep it focused. This signals that he values clarity and decisiveness over comprehensiveness.

## 9. The "Investment" Ask: Skin in the Game

Mani asked for something beyond a standard rate-card proposal (lines 394-396):

> "I would love seeing [that] with what kind of investment that you can do... [It's] not [just] a [standard engagement], but [I want to see] what kind of investment that you guys can do. So if you can bring that point of view also in the proposal, that would be good." (lines 394-396)

**What "investment" means in this context:**

- Mani is asking BayOne to put skin in the game. He does not want a pure time-and-materials proposal where all the risk sits with Sephora.
- "Investment" likely means one or more of: discounted pilot rates, upfront work at BayOne's cost to prove value, a fixed-price component where BayOne absorbs overrun risk, or a shared-risk model where compensation is partially tied to outcomes.
- Zahra (BayOne) had also previously framed a confidence-building approach (lines 385-391): "One is to build your confidence because I know we're new to you... if there's something smaller that would be still useful to you, then we could do to start, even if that's at [our cost]."
- Mani's response to this was the investment ask --- he is receptive to the confidence-building framing but wants to see it formalized in the proposal.

**Implication:** The proposal must include a clear statement of BayOne's investment --- what BayOne is willing to put on the line to earn the engagement. This is a trust-building mechanism for a new relationship.

## 10. Flexibility in Engagement Models

Mani raised this unprompted (lines 442-448):

> "In the model, kind of a different model, you need some flexibility also. We, even if we go like a [staffing model], not everybody wants full-time. And we can bring in people for a couple of hours to go --- you know, we have --- it's very flexible, more of it. So I would love if [in your proposal you show] those options --- see what kind of flexibility that you can have." (lines 442-448)

**What Mani is asking for:**

- Not all positions need to be full-time dedicated resources. Some roles may only need a few hours per week.
- He wants to see that BayOne can accommodate flexible staffing --- fractional engagement, part-time specialists, on-demand expertise.
- "Not everybody wants full-time" could refer to both the client's budget constraints and the nature of certain roles (e.g., a senior architect providing guidance 10 hours/week rather than being embedded full-time).
- This should be reflected in the "three options" --- different engagement models with different levels of commitment and flexibility.

**Implication:** The proposal should not assume full-time-equivalent staffing across the board. Show models that range from embedded full-time resources to fractional/part-time specialists. This flexibility may also be part of BayOne's differentiation.

## 11. Mani's Description of the Project Organization and Roadmap

While not a direct "ask," Mani provided significant detail about how the modernization is organized, which constrains what BayOne can propose.

**Category-by-category approach (lines 66-113):**

- There are thousands of reports. They cannot be changed "in one shot" (line 66).
- They are approaching it "track by track" and "category by category" (lines 67-68).
- Categories include: Finance, Supply Chain, Merchandising, Stores, and others (line 70).
- Finance is the first track taken. Within finance, they have figured out which reports to sunset and which to re-engineer (lines 86-88).
- Other categories (like merchandising) "would not come [forward] yet" --- they are next in the roadmap (lines 89-90).
- There is a defined roadmap: "Which category comes first? Which category comes next? Which category [comes] third? That part has been figured out" (lines 99-101).
- The first three tracks are in progress. Remaining tracks (also three) have not started and will go through the same detailed scoping process when their turn comes (lines 104-106).

**Architectural patterns are established (lines 73-84, 107-108):**

- The target is Databricks (line 75).
- They know the sources (line 76).
- Accelerators from Databricks and Databricks partners are being evaluated (lines 77-78).
- The team has spent "the last couple of months" assessing which tools work best for different use cases (lines 81-82).
- "The architectural [pattern] is not going to change. Those parts are very well established" (lines 107-108).
- The same patterns will be applied to each new category as it comes up --- merchandising, supply chain, stores (lines 109-112).

**The team structure (lines 119-125):**

- Databricks has "a seat at the table," Microsoft has "a seat at the table," the data platform team has "a seat at the table" (lines 119-121).
- Important stakeholders are represented from across the organization (line 122).
- "This is the core team. This team establishes what's right to do, how to do it" (lines 124-125).
- Mani is "very [confident] about" the team --- they have 5-6+ years of institutional knowledge and know the reports "in and out" (lines 93-96).

**Implication for the proposal:** BayOne is entering a well-organized initiative with established patterns, a clear roadmap, and a strong core team. The proposal should position BayOne as augmenting this structure, not replacing or redirecting it. Any AI-assisted approach must plug into the existing category-by-category methodology and respect the architectural decisions already made.

## 12. Existing AI Tool Usage

Colin asked about existing AI tools (line 164). Mani's answer (lines 167-171):

> "Definitely, the team is using AI to accelerate. What exact tools they're using --- [there are certain] tools that they use, and also [Low is Australia] and other tools that they are using. Those two are really something that comes to my head right now. More details [Grishi] might have already told you." (lines 167-171)

The speech-to-text is garbled here, but the key signals are:

- The team IS already using AI tools (this is not greenfield AI adoption).
- Mani could not name the specific tools off the top of his head --- he deferred to Grishi for details.
- At least two specific tools are in use. One likely reference is to Databricks' built-in AI capabilities; the other is unclear from the transcript.

**Implication:** Colin needs to understand the existing AI tooling landscape from Grishi before proposing anything that might overlap or conflict.

## 13. Timeline and Logistics Signals

**Proposal delivery timeline (lines 398-418):**

- Zahra (BayOne) suggested presenting the proposal in person the following week.
- Mani said "next week is not a good time" --- it is a short week with a "huge off-site" on Wednesday/Thursday (lines 403-411).
- They agreed on "the week after" (lines 413-414).
- Mani explicitly said he wants to attend and "get the first-time view" and provide "feedback and inputs" (lines 416-417).
- Zahra acknowledged this would give them time to "build this, bring a structure to this" and then they can "review" (line 418-419).

**In-person presence (lines 422-441):**

- Colin is based in Pittsburgh, Pennsylvania (line 422).
- BayOne committed to having "somebody here local" (line 425) --- between Zahra and Neha, there will be "physical presence consistently every week" (line 439).
- Mani was receptive to in-person meetings. Colin offered flexibility: "If you prefer remote, I can be remote. If you would like in person, I [enjoy] the sunny weather" (lines 431-432).

**Implication:** The proposal needs to be ready approximately two weeks after this meeting. The presentation should be in-person with Mani present.

## 14. Decision-Making and Budget Signals

While Mani did not state a budget number, several signals emerged:

- **Mani has decision authority** but wants Grishi involved: "I would [like to] come and [attend] that meeting. I [want] to get the first-time view and [provide] feedback and inputs" (lines 416-417). He is positioning himself as the decision-maker who reviews and approves, with Grishi handling technical evaluation.
- **The category-based approach implies incremental budgeting:** Each track/category likely has its own budget or is approved incrementally. This is consistent with the "three options" structure --- each option could correspond to a different category with a different budget level.
- **"Investment" framing suggests budget sensitivity:** Mani's ask for BayOne to show "skin in the game" suggests that getting budget approval for an unproven new partner may require BayOne to reduce the client's financial risk upfront.
- **Finance track is nearly complete** (20-odd more days per line 369), so the next category is the real target. BayOne's proposal should be timed to catch the beginning of the next track.

## 15. Colin's Presentation Content (for context)

Colin presented a slide deck (lines 186-293) covering:

1. **The challenge:** Thousands of reports, tribal knowledge embedded in legacy systems, SMEs stretched thin, manual validation is slow (lines 196-209)
2. **AI opportunity #1 --- Pattern detection and clustering:** Using traditional ML combined with generative AI to group similar reports, reduce cognitive load on SMEs, enable batch processing rather than report-by-report review (lines 213-228)
3. **AI opportunity #2 --- Code analysis and business logic surfacing:** Automated extraction of business logic from legacy code, dependency mapping, identifying consolidation opportunities, reducing the report footprint (lines 232-246)
4. **AI opportunity #3 --- Automated mapping and validation:** Deterministic systems for validation rather than purely LLM-based approaches, pattern-based quality assurance, reusable templates (lines 247-257)
5. **Staffing support:** BayOne can supplement the team for ongoing BAU (business-as-usual) work that gets squeezed during modernization (lines 259-264)
6. **Engagement approach:** Proposed a pilot on the finance track (already well-defined) or an unstarted track, to prove the AI-assisted approach before scaling (lines 267-278)

Mani's "all looks good" response (line 294) validated this presentation content in its entirety.

## 16. Zahra's Confidence-Building Framing

Zahra (BayOne) introduced a two-tier proposal concept (lines 385-391):

> "From the proposal standpoint, I can give you maybe 2 different types of proposals... One is to build your confidence because I know we're new to you... if there's something smaller that would be still useful to you, then we could do to start, even if that's at [our cost]... And if there's a bigger scope as well, we can address that." (lines 385-391)

This sets up the "investment" conversation and directly led to Mani's skin-in-the-game ask. Zahra effectively opened the door, and Mani walked through it by saying he wants to see BayOne's investment commitment formalized in the proposal.

## 17. Post-Meeting Reaction

The transcript captures a brief, unguarded moment after Mani left the call (lines 466-470):

> "God, it is such a good fucking day. That was so good. That slide was [done] two minutes before." (lines 467-469)

This indicates:

- Colin and the BayOne team (likely Zahra) felt the meeting went extremely well.
- The slide deck was prepared last-minute ("two minutes before"), yet Mani validated the approach.
- The team's confidence level is high coming out of this meeting.

---

## Summary: Mani's Complete Ask List for the Proposal

| # | Ask | Details |
|---|-----|---------|
| 1 | **Case studies/examples** | Proof of prior similar work. Snowflake architecture case and Databricks connector case mentioned. |
| 2 | **Specific category example** | Pick a category, state assumptions, provide estimated timeline and cost. |
| 3 | **Three options (not seven)** | Different engagement models, potentially mapped to different categories. Full ownership, implementation-only, and a third hybrid/flexible model. |
| 4 | **Investment/skin in the game** | Show what BayOne is willing to invest upfront to earn the engagement. Not a pure T&M proposal. |
| 5 | **Flexibility in staffing** | Not all roles need full-time. Show fractional/part-time/on-demand options. |
| 6 | **Unique value differentiation** | Answer "what is the unique thing you bring?" with specifics, not generalities. |
| 7 | **Use "modernization" not "migration"** | Language discipline across all materials. This is re-engineering, not lift-and-shift. |
| 8 | **In-person presentation** | Deliver approximately two weeks after this meeting, with Mani present. |
