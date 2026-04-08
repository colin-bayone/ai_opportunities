# 03 - Campus Visit: Cross-Engagement Insights

**Source:** /cisco/cicd/source/meeting_cisco_campus_epnm_and_internal_2026-01-15.txt
**Source Date:** ~2026-01-15 (Cisco campus visit during Jan 9-20 trip)
**Document Set:** 03 (Cisco campus visit -- EPNM-focused, light treatment for CICD)
**Pass:** Cisco culture, BayOne positioning, and lessons learned relevant to CICD

---

## The $500K Loss: BayOne's Prior Cisco Failure

This is the most strategically important item in this transcript for the CICD engagement. Rahul shares the story directly with Colin during their one-on-one conversation.

### What Happened

- BayOne won a project at Cisco prior to the current QA/testing engagement that Amit presented in the case study session.
- The project was structured as a fixed-scope engagement.
- **The scope was not defined.** Rahul states this explicitly: "the scope was not defined."
- There were "too many interdependencies" and "the roadblocks were too much."
- BayOne was "just learning through the process" -- they did not understand the environment or the work before committing.
- After six to eight months of effort, "they pulled the plug, and we were happy to get the pulled the plug, because it was not going anywhere."
- BayOne lost approximately $500,000 on this project.

### What BayOne Learned

Rahul states the lesson as a firm organizational rule: **"In today's world, if somebody comes to us and says the scope is not defined, we are not signing for a fixed scope project. Then we are only signing for a time and material. We are not working. And in your time, if you are unsure about the scope, you're not signing up."**

This is a binary decision rule:
- Defined scope --> Fixed-price is possible
- Undefined scope --> Time and material only, or do not engage

### Why This Matters for CICD

The CICD engagement has several parallels to the failed project:

1. **Scope ambiguity.** Set 01 lists six use cases (A through F), of which only A, E, and F are named. Use cases B, C, and D remain undefined. The starting focus (A+F) is clearer, but the overall engagement scope is not fully defined.
2. **Environmental complexity.** Set 02 documented Cisco's dysfunctional development practices (code pasting in WebEx, no proper GitHub usage, non-standard workflows). This mirrors the "too many interdependencies" and "roadblocks" that killed the prior project.
3. **Learning curve.** Set 02 noted that standard CI/CD practitioners would get "lost almost immediately" in Srinivas's domain. The prior project also involved BayOne "just learning through the process."

The $500K loss validates BayOne's decision (reflected in Set 01 and Set 02) to start with a discovery phase and operate on a quarterly budget with time-and-material flexibility rather than committing to fixed deliverables up front. It also explains why Rahul is cautious about scope commitments -- this is not theoretical risk management but a lesson paid for at considerable cost.

### Timeline Implication

Rahul says the successful QA/testing engagement (Amit's case study) came **after** the $500K failure: "But when we went on to the second project, we were much more cautious, we were much more structured, we did not fail." This means BayOne has been through at least two engagement cycles with Cisco -- one catastrophic failure and one multi-year success. The CICD engagement would be a third attempt at a new type of work within Cisco.

---

## Cisco Vendor Selection Dynamics

### Relationships Trump Capabilities

Rahul and Colin discuss a pattern that emerges across multiple Cisco engagements:

- **The Abhay story.** A Cisco decision-maker named Abhay selected a competing vendor over BayOne because "he had known the person that was at the other agency. He had known them from some past work." BayOne put its "best work forward" but lost to the personal relationship. Mahesh (another Cisco person) reportedly told Rahul daily that Abhay should have chosen BayOne.
- **The case study session reinforces this.** Amit notes that several of BayOne's largest engagements started from relationships, not competitive RFPs: "this started off now with the relationship, right?" He describes how the testing engagement began through an existing relationship and expanded through demonstrated capability.
- **Rahul's explicit statement:** "We had a heart cell. I think most of the time we got it because we had prior relationships. People trusted. Mahesh equivalent in those companies who could vouch for us."

**Implication for CICD:** The CICD engagement already has Anand as a relationship-based sponsor. Protecting and deepening this relationship is more important than technical proposal quality. Conversely, any expansion within Cisco (to the VP's broader budget, to adjacent groups) will require building new internal champions -- BayOne cannot assume that success in Anand's group will automatically open doors elsewhere.

### First Engagement Penalty

Rahul articulates a clear pattern for BayOne's position at Cisco:

> "While we start cheering these ones, right, they are not busy, we are not, in their mind, they don't know us that we have these capabilities. So we'll be always competing against somebody. Always, right? Getting a first success or second success will always be a longer cycle, will be a more frustration cycle. They might not, we will win some, we'll lose some. But once we start winning it, it will create repetitive success for us to get it."

This maps directly to the CICD engagement's dynamics:
- BayOne is still in the "first success" phase with Anand's group
- The $100K/quarter budget (Set 02) is a trust-building allocation, not a reflection of the work's value
- Success here unlocks a "repetitive success" cycle with "this VP [who] has a lot of budget" (Set 02)

### Risk Tolerance Varies by Customer

The discussion reveals that Cisco's risk appetite is shaped by prior experience:

> "When they are trying to solve a problem, they will go where they have the most confidence or the least risk. No one wants to get burned."

Rahul uses BayOne's own client relationships as the counter-example: "if coherent has to get some resources offshore, we are there trying, right? Because we have built that complex." The CICD engagement sits in the "unproven" category, which means Cisco will default to conservative scope, conservative budget, and high scrutiny.

---

## BayOne's Managed Services Playbook (Relevant to CICD Positioning)

The case study session reveals a replicable pattern that informs how BayOne could position the CICD engagement for stickiness and growth:

### The Testing Engagement Arc

1. **Entry via relationship.** BayOne got in the door through existing connections.
2. **Started with staff augmentation adjacent work.** Even though it ran as "fixed capacity," the initial scope was operational testing support.
3. **Introduced process and tooling.** BayOne brought in TestRail, standardized test case management, introduced regression automation, and established reporting cadences.
4. **Built trust through transparency.** Weekly appearances/reports: "we will report back to you every week, we watched what the team has done last week, how many bugs they have reported, how many new bugs they have created."
5. **Shifted to biweekly reporting.** As trust grew, the reporting frequency decreased, signaling increased autonomy.
6. **Customer stopped questioning team composition.** "They've never come and asked, okay, I mean, why is somebody going in, why is somebody going out." BayOne achieved true managed services status.
7. **Expanded scope organically.** From testing into CMS content management and development activities.
8. **Team became irreplaceable.** "Getting rid of it, it's very difficult for anybody when they hire somebody to replace you."

### Application to CICD

The CICD engagement could follow this same arc:
- Enter through the discovery phase (already planned)
- Introduce process improvements (CI/CD workflows, GitHub practices, Airflow orchestration)
- Establish visibility through regular reporting
- Demonstrate value through measurable outcomes (cycle time reduction, deployment frequency, error reduction)
- Gradually shift from project-based to managed-services model
- Expand from A+F use cases into B, C, D, E

The case study session explicitly positions this as BayOne's standard playbook. Amit describes it as moving from "3 and 11 to fixed capacity to minus 1" -- a progression from staff augmentation to fixed capacity to fully managed operations.

---

## Colin's Code Modernization Presentation

Colin presented code modernization capabilities during the internal session. The specific content is EPNM-related and tracked in `cisco/epnm_ems/`, but the presentation itself has CICD relevance:

- **It demonstrated BayOne's AI-enhanced delivery capabilities.** Someone reacted to the visual quality: "This looks great. Did you do a lot of these things inside custom? There's a lot of visual polish to this that I haven't seen from most of our slide decks." Colin's ability to produce polished, differentiated materials is an asset for CICD proposals and client presentations.
- **It positioned BayOne as having code modernization depth.** Even though the CICD engagement is about pipeline automation (not code rewriting), demonstrating modernization expertise adds credibility. Cisco's codebase is legacy and poorly structured (Set 02); understanding modernization patterns is directly relevant.
- **It was part of the sales enablement effort.** BayOne is systematically building a library of case studies and capabilities presentations. The CICD engagement, once started, should generate its own case study material for the same internal audience.

---

## Pricing and Commercial Insights

### Fixed Price vs. Time and Material

The transcript contains an extended discussion about engagement pricing models, triggered by the case study Q&A. Key points relevant to CICD:

- **Discovery-first is standard BayOne practice.** Amit describes the approach: "We'll start a while you engage. We'll do a discovery phase for three weeks to six weeks time. And by the end of that discovery, we'll know whether we are in a position to give you an estimate."
- **Story points can anchor managed services.** One BayOne customer engagement runs on story-point-based delivery: "we set up this managed services model for one of our customers. And that is based on the story points that we have to deliver." This model could work for CICD if BayOne establishes a sprint cadence.
- **RFP-stage work disadvantages BayOne.** Rahul notes: "from our standpoint, we have the size of the company we are. If it's already got to RFP stage, we're already on the back." The CICD opportunity is valuable precisely because it came through relationship, not RFP.
- **The gray area is BayOne's sweet spot.** Rahul: "for us, there are that gray area where people are confused, they don't know about it. They can't really come up with a clear score because the product isn't started. That's the best work for us to get engaged." The CICD engagement fits this description -- Cisco knows they have pipeline problems but does not have a defined solution.

### Pricing Sensitivity at Cisco

From the broader discussion about winning and losing deals:

- "The pricing was great, so ours was like second return, I guess then, and then you'll be servicing." -- BayOne's pricing was competitive in at least one Cisco context.
- "If they are very confident that they will be able to deliver very good high quality work and all of that, but the pricing is not matching, it's not moving." -- Some Cisco groups are price-sensitive even when quality is demonstrated.
- "Some customers have seen who have a lot of, like they want quality at any cost." -- Other Cisco groups prioritize quality over cost.

Identifying which category Anand's group falls into is important for the CICD pricing strategy. Set 02's $100K/quarter budget suggests cost-consciousness, but this could also reflect trust-building conservatism rather than price sensitivity.

---

## BayOne Organizational Dynamics

### Colin's Bandwidth is Being Actively Managed

Rahul tells Colin directly: "keep looking for the right people who can take off your work. That's more important. Because if you get any of these [deals] which you have been involved with, then you will be scrambling between talent AI and delivering that and additional sales costs that you have to get into."

Colin responds by describing how he has started delegating more to his team: "I tried to say I'm going to reorganize my time. For the team, I tried to give people a little bit more responsibility and ownership of specific things. That's been going well."

**CICD implication:** Colin is the only person at BayOne with the technical depth to lead CICD discovery and design. If the engagement launches while he is still deeply involved in Talent AI and other Cisco opportunities, his attention will be divided. Rahul is aware of this and pushing Colin to build a support structure, but it is not yet in place.

### Strategic Hires Planned

Rahul mentions: "We are making some strategic hires or talking to two people whom we want to bring on board to help us walk through this journey more easily, smoother."

These hires appear to be for BayOne's AI practice broadly, not specifically for CICD. But if they materialize, they could free Colin's bandwidth or provide additional senior resources for Cisco engagements.

### February Bay Area Trip

Rahul asks Colin to come to the Bay Area for two weeks in February (weeks of the 9th and 16th). This trip would include:
- The AQO event on February 19-20
- "Important discussions" during the week of February 9
- In-person time with Rahul before Rahul travels to India on the 16th

This trip is likely where CICD discovery planning, Cisco relationship-building, and EPNM positioning would all converge. Colin's physical presence at both the BayOne Bay Area office and the Cisco campus during this window is a significant investment of time.

---

## Fact vs. Interpretation

| Item | Fact (stated in transcript) | Interpretation (inferred) |
|------|---------------------------|--------------------------|
| $500K loss on prior Cisco project | Rahul states the amount and timeline (6-8 months) directly | This is likely the same engagement or the same Cisco group where Gaurav and/or Sarang were later placed |
| Scope was not defined | Rahul states this as the root cause | BayOne did not push back on scope ambiguity before committing to fixed price |
| Post-failure, BayOne succeeded | Rahul says the QA engagement that followed was "much more cautious, much more structured" | The $500K lesson directly produced BayOne's current discovery-first, T&M approach |
| Mahesh wanted BayOne selected | Rahul quotes Mahesh's daily comments | Mahesh may still be an active contact who could support CICD or other Cisco opportunities |
| Abhay chose vendor on personal relationship | Rahul and Colin discuss this directly | Relationship-based selection is the norm at Cisco, not the exception |
| Colin's code modernization presentation was visually polished | Attendee comment captured in transcript | Colin's presentation capabilities differentiate BayOne from typical offshore/staffing vendors |
| Two strategic hires being pursued | Rahul states this directly | These hires are for BayOne's AI practice, timing and relevance to CICD uncertain |
| February two-week trip planned | Rahul requests, Colin agrees | This trip will serve multiple purposes: CICD, EPNM, Talent AI, internal meetings |
