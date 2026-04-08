# 03 - Meeting: July Timeline and Costing Discussion

**Source:** /cisco/epnm_ems/source/guhan_selva-3-25-2026.txt
**Source Date:** 2026-03-25 (POC Proposal Discussion and Scope Refinement)
**Document Set:** 03 (Third meeting, scope clarification and next steps)
**Pass:** Focused deep dive on timeline exploration and costing considerations

---

## 1. Venkat's July Mention: Exploring What Is Realistic

Venkat raised the possibility of July during the conversation. This was not a demand or a deadline. He was exploring what is achievable, testing the boundaries of what the timeline could look like if things went well:

> "I think Velkatt was telling if he can even do it in the current release, which is going out in July. That will be the best."

This statement came from Selva, paraphrasing what Venkat had communicated. The framing is aspirational — "if he can even do it" and "that will be the best" — not directive. Venkat wanted to understand whether the current release cycle (July) could absorb this work, not to impose it as a requirement.

Colin's response acknowledged July as not out of the question, but immediately grounded it in practical constraints:

> "So for us, I don't think July is out of the question. I do think that, you know, it's the matter of the costing for it too, for, you know, beyond what we do for the, for this MPP. But July demand for the whole thing. That's where it becomes a budget question more than anything."

Key elements of Colin's framing:
- July is possible in principle — he did not dismiss it
- The feasibility depends on costing and budget appetite, not on technical impossibility
- He explicitly called it "a budget question more than anything"
- He distinguished between the POC scope (the current effort) and the full engagement ("beyond what we do for this MPP")

## 2. Full Scope: 200-250 Workflow Screens

Colin referenced the total scope of the engagement beyond the POC:

> "But there's I think in total 200, 250 screens, or workflow screens that will have you going, something like that."

This number was stated as an approximation ("something like that"), suggesting it came from earlier conversations or Cisco's own internal estimates. It was not contested by Selva or Guhan. This is the total number of screens that would need the classic-view treatment — the full engagement scope, not the POC scope.

The POC scope remains 2-3 representative screens, as discussed earlier in the meeting. The 200-250 number is the universe of work that would follow if the POC proves the approach.

## 3. Parallelizable Work and Cost-Timeline Tradeoff

Colin made a significant strategic point about how the work scales after the POC:

> "Now the good thing with that is, like I said, it's very parallelizable, it's a fun word, parallelizable work where we can have a lot of streams going. For instance, for me it's like I would have a person dedicated to just the QAQE agents, you know, and I would have a person doing this subset of screens, doing that batch, moving on to the next. I can get more done with more people in parallel."

He then explicitly linked this to the cost-timeline tradeoff:

> "Yes, that increases the shorter-term cost, but that gets you where you want to be faster. And it gets you there comfortably, so it's not like we're delivering on June 31st or June 30th for a July 1st deadline."

This framing is important: Colin was signaling that a July target is achievable if Cisco is willing to invest in more parallel resources. He was not promising July — he was explaining the lever that makes July possible (more people, higher short-term cost, but faster delivery). He also emphasized the quality angle: "comfortably" means not a last-minute scramble.

## 4. Colin's Deliberate Restraint on Numbers

Colin was intentional about not getting into specific cost figures during this meeting:

> "And I won't throw numbers around today, but at the same time, just think about it because that way we can start looking for people early on our side."

This is a carefully calibrated statement. He:
- Declined to price the engagement on the spot
- Asked Cisco to "think about it" — seeding the budget conversation for a future discussion
- Pivoted immediately to the operational concern of resource availability

## 5. Early Resource Mobilization: India Team

Colin's suggestion to start looking for India resources early was directly tied to avoiding a lag period between the POC and the full engagement:

> "So if we want to get some India resources to help accelerate this, if we do want to shoot for July, we can get a head start so we don't have a lag period after this initial deliverable is done."

The logic chain:
1. The POC will take a defined period (Colin previously suggested roughly four weeks)
2. After the POC, if Cisco wants to proceed to the full 200-250 screens, BayOne will need to staff up
3. Finding and onboarding India resources takes time
4. If they wait until after the POC to start recruiting, there will be a dead period where no work is happening
5. Starting the search early (during the POC) eliminates that gap

This is also a soft sell — Colin was signaling that BayOne has India delivery capability, which affects the cost structure favorably and aligns with Cisco's own India-based team structure. Selva had confirmed earlier: "I'm expecting that the team will be in India, by the way, Colin."

## 6. Selva's Concern: Server-Side Changes and the Critical Release Path

Selva raised a significant constraint about backend modifications:

> "We will not have any way now to go either way. So any changes to the current server, because the current server is also getting updated. Next three months of coding is going to happen."

This statement reveals:
- The EMS server-side code is actively being developed for the same July release
- Server-side changes introduce risk to the critical path — if something breaks, both the new UI and the classic UI could be affected
- Selva framed this as a stability concern: "we will have a non-usable or a buggy new UI under classic UI"
- The next three months (roughly April through June 2026) are an active coding period for the server

Earlier in the meeting, Guhan had set the baseline expectation:

> "We don't want to rewrite the back-end services. So that can keep me honest. Because that's a lot of work. If we write all the back-end again, then we have to maintain two different versions. We're not staffed. It's not the right way to do it."

However, Guhan also acknowledged that some backend work would be necessary:

> "One thing is, for example, in the older UI, we might have given him ability to look at things with a different lens... So this means that there may be slight touch up to the back end to do that filtering. That's the kind of thing we expect."

And Selva reinforced this nuance:

> "Sometimes you may need to go touch the back end to do this particular API. Since we are not presenting a certain information in a certain way, I'm not having a corresponding back-end API. So you may need to do that corresponding thing to make it happen."

The tension here is clear:
- Some backend API adjustments may be needed to support the classic view
- But the server is in active development for the July release
- Any backend changes carry risk of destabilizing the release
- This is an unresolved constraint that will need to be navigated screen by screen

## 7. POC's Dual Purpose: Demonstration and Cost Estimation

Selva articulated the two outcomes expected from the POC:

> "So there can be another outcome of this. So one has to demonstrate it for two, three screens. Second one is to, you put it in your document very clearly, that second one is also to cost out what it takes to do the whole thing."

Colin had set this up earlier when he described how the POC would generate the data needed for scoping the full engagement:

> "What I'll find out from this, even beyond the 2-3 screens, I'll find out the general complexity of the other screens, too. So that's what I meant when I said the representative sample. I'll be able to figure out what the effort level was needed, what the customization level was needed on these, and map that out, see what the outliers are, figure out what that time would take to say for sure before I even start talking to you about doing it in July, you know, can we realistically do this?"

The POC therefore serves as:
1. **Proof of concept** — Demonstrate the classic-view conversion on 2-3 screens with working toggle
2. **Cost estimation model** — Provide empirical data on effort-per-screen that can be extrapolated to the full 200-250 screen scope

Colin also explained why the POC timing should not be linearly extrapolated:

> "Don't think if I say like it'll take us three weeks to do this, that that's three weeks for three screens, because that's just... kind of that initial front loading of getting everything set up, understanding everything, discoveries wrapped in there too."

And later, when Selva asked for clarification:

> "On your earlier comment, I didn't quite catch, are you saying that initially it takes more time and then the subsequent ones will be even faster?"

Colin confirmed:

> "Yes, yes, by far. So typically what we see, and this is the first, it's almost like this exponential decay cycle truly, even the time-wise, the first time is us, first of all, understanding the problem. So there's that onboarding period for us."

This exponential decay model is central to how BayOne will price the full engagement: the POC establishes the baseline cost including one-time setup, and subsequent screens are progressively cheaper. This is the data that the POC's second purpose will produce.

## 8. Confidence Level Discussion

Selva asked directly about confidence:

> "What is your confidence level that we can do this automated AI way without having to burn lots of resources?"

Colin's answer:

> "Very high. Very high. I think one of the goals that I would have for this depends upon how comfortable everyone is. I know there's other initiatives at Cisco to go to what we'd say is like 100% AI generated code. This is a very good one where maybe not at first can we say that because at first we're going to need to pass a manual oversight of this. Once we have a pattern established, this starts to take off."

He qualified the confidence:
- High confidence in the approach overall
- Not claiming 100% automation from day one
- Manual oversight is needed in the early phase
- Once patterns are established, the AI-driven approach accelerates
- Referenced Cisco's own interest in AI-generated code as contextual alignment

## 9. Open Questions and Unresolved Points

### Budget and Pricing
- No numbers were discussed. Colin deliberately deferred this. The cost conversation will happen after the POC produces empirical data on effort-per-screen.
- The budget question is the primary gate for whether July is realistic for the full scope.

### Server-Side Risk Management
- How will backend API adjustments be handled without destabilizing the July release? No process was established for this.
- Who approves backend changes? Guhan owns the architecture, but Selva's concern about the critical release path suggests there is a governance layer that has not been discussed.

### Resource Planning Timeline
- Colin suggested starting to look for India resources early, but no specific trigger or timeline was set for when that search would begin.
- The POC has not formally started yet — next steps are domain expert sessions scheduled for the following week.

### Scope of "Full Thing"
- The 200-250 screen number was mentioned but not broken down. No categorization of screen complexity, no identification of which screens might require backend changes versus pure UI work.
- The "representative sample" approach during the POC is intended to address this, but it depends on which screens are selected for the POC covering enough diversity.

### Product Management Sign-Off
- Selva mentioned: "At some point we will work with the product management to see if this is good enough or we have to do more." Product management has not been involved in these discussions yet.

### July: Full Scope or Partial?
- It remains unclear whether "July" means all 200-250 screens or a meaningful subset. Colin's framing ("July demand for the whole thing") suggests he understood it as the full scope, but this was not explicitly confirmed or denied by Selva.

## 10. Timeline Reconstruction

Based on statements in this meeting, the implied timeline is:

| Phase | Timeframe | Activity |
|-------|-----------|----------|
| Domain expert sessions | Early next week (late March / early April 2026) | Cisco India team walks Colin through specific screens, code access, and expected outcomes |
| POC execution | ~4 weeks after access (April-May 2026) | 2-3 screens converted with local toggle, cost model developed |
| Scoping discussion | After POC delivery (May-June 2026) | Cost proposal for full engagement, resource plan, timeline options |
| Full engagement (if July) | June-July 2026 | Parallel streams, India resources, multiple screen batches |

The July target, if pursued, would require the POC to complete quickly, the scoping discussion to happen fast, and India resources to already be identified and available. Colin's early-mobilization suggestion was designed to compress the gap between POC completion and full engagement kickoff.
