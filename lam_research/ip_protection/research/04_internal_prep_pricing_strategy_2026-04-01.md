# 04 - Internal Prep: Pricing Strategy

**Source:** /lam_research/ip_protection/source/internal_anuj_amit_pratik_colin_04-01-2026.txt
**Source Date:** 2026-04-01 (Internal BayOne prep call)
**Document Set:** 04 (Internal Prep Call)
**Pass:** Focused deep dive on pricing, costing, and commercial strategy

---

## 1. The Costing Workbook

Colin introduced a costing workbook he built for formal project costing. He described it as his own methodology, not derived from the Blue Sheet framework, but from his experience with corporate-style projects. He positioned it as solving a recurring problem: "There's so many people that need to give some level of input to the costing conversation. It helps to make it less work for everyone. And finally puts it to one place."

### 1.1 Workbook Structure

The workbook has multiple tabs, with a design principle that inputs are concentrated in just two tabs (Personnel and Project Inputs), and every other tab auto-calculates from those inputs. Colin explicitly stated: "Anything that's not yellow is not an input field. Yellow is input." Blue-shaded fields throughout the workbook are calculated values that cannot be edited.

**Tab 1 -- Instructions**
A dedicated instruction sheet as the first page of the workbook.

**Tab 2 -- Personnel**
- Working locations (configurable, selectable)
- Rates: annual or hourly, base rate
- Loaded costs calculated per resource
- Allocation percentages to the project (for shared resources -- e.g., Colin might be less than 100% allocated overall but 100% during a POC phase)
- Defaults and summary section

Colin noted the allocation feature is important for shared resources: "If I'm on a project, let's say, I'm not 100% on the project, maybe for the POC, but not overall. But this lets us calculate for that."

**Tab 3 -- Project Inputs**
This tab is deliverables-based, not headcount-based. Key fields include:
- Project details (reflected through the entire workbook -- "You don't have to change things through projects. Easy, simple.")
- Resource summary (auto-calculated from Personnel tab -- "This is not able to be touched. This is strictly a calculation coming from the personnel tab.")
- Auto-calculated monthly team burn at peak
- Working hours assumption per fully loaded person per month and annually
- Engagement parameters: revenue opportunity framing
- **Deliverables section:** Number/quantity of deliverables, and estimated hours per deliverable with tooling. Colin stated: "If you can think about things as deliverables, what is the amount or quantity of deliverables and what's the hours estimated with the tooling for those deliverables."
- **Risk reserve:** A buffer included as a safety net, described as "not lost cost for us, but just an extra padding on top of our margin." Colin explained the purpose: "Even if we say we're making 40% margin, great. Well, what happens if I needed to go buy more expensive resources? I don't want to tap into that margin because that can make an engagement go negative really quick. So what do I do? I put in a risk buffer of 20% from the get-go, which is essentially 20% added on to the sunken cost for the resources and the time as well."
- POC items section
- Travel inclusion (simple toggle or entry)
- Hardware and consumables, monthly subscriptions, one-time equipment costs -- all factored in
- **Margin settings:** Threshold targets through engagements, used as labels/references throughout the worksheet

**Tab 4 -- POC (Dedicated)**
A separate tab for POC costing with configurable billing treatment:
- Billed to the client
- Absorbed by BayOne
- Covered by salaried resources (e.g., Colin -- "Technically it doesn't cost us anything. Technically, you can't really say that it's billable because it's not. But this comes from the client.")
- Effort hours input (e.g., 80 hours), which auto-calculates duration and all downstream details

**Tab 5 -- Scenarios**
Supports multiple engagement scenarios (e.g., Scenario A and Scenario B). Duration of engagement is configurable. Allows staggered resource starts (e.g., a person starting at month two, with the workbook automatically adjusting calculations). Produces a summary table with:
- Revenue
- Base costs by phase
- Loaded costs
- Margin on loaded costs (both dollar and percentage)
- **Discount analysis:** Shows how much negotiation room exists. Colin described: "How much wiggle room do you have to leverage for negotiation? So you can see over here, this safe or below floor here with the loaded cost with the risk reserve in mind, you could offer them up to a 15% discount before you would not meet your margin threshold."
- Bird's eye comparison of Scenario A vs. Scenario B

**Tab 6 -- Throughput Comparison**
Colin called this "the most exciting" tab. It addresses the core estimation problem: "The tough thing is to say, how much time will this actually take?"

How it works:
- Starts with known number of deliverables and average time per deliverable (can be granular or broad -- "We don't even have to be ballpark in that same realm, but we don't have to be close")
- Everyone gets the same available hours per month (calculated field)
- Shows total team capacity, minimum hours, safe hours to deliver
- Risk reserve buffer applied
- Calculates team capacity utilization (e.g., "My team is at 41.4% capacity, aka we are in real good shape. Probably could trim off a resource if we wanted to.")

**Productivity multiplier column** -- This is the differentiating feature. Not all workers are equal:
- Junior person: **0.25** multiplier
- Mid-level person: **1.0** baseline ("Like a mid-level person baseline. No one amazing, no one bad, but just normal.")
- Senior person: **2.0** multiplier

This allows scenario modeling: "You can play around with what would this project look like if I had a team of five juniors versus a team of two seniors or maybe a hybrid team. How does that costing work and how does that impact you?" If a resource is underperforming mid-project, their multiplier can be adjusted to see the risk impact, and "all these things on the sheet update accordingly."

### 1.2 Workbook Design Philosophy

The workbook requires two types of input, divided by role:
1. **Technical input (Colin):** Deliverables definition, hour estimates per deliverable, risk assessment based on technical complexity or unknowns
2. **Business input (team):** Margin targets, available capacity, resource stacking across projects

Amit's reaction was strongly positive: "This is fantastic... this provides much more detail than we want at times. This is very good actually." He asked Colin to share it so he could review and suggest adjustments.

---

## 2. The Cisco Example (Live Reference Project)

Colin walked the team through a real, recently submitted engagement using the costing workbook -- the Cisco EPNM-to-EMS UI conversion project. This served as a concrete demonstration of the methodology.

### 2.1 Scoping Approach

Suresh asked Colin how long the conversion work would take per screen. Colin's internal estimate was approximately **2 hours per screen** at full pace. But when asked about his confidence level, Colin said: "I don't know. I haven't seen their code yet. I have no clue."

Instead of quoting 2 hours or even a modest buffer at 3 hours, Colin quoted **8 hours per screen** -- a 4x multiplier on his internal estimate. His rationale: "Because at the end of the day, all that we're going to do is deliver faster. And with solutions, they're not trying to do this at the lowest cost because, frankly, they would do it in-house if that was the case or they'd go for a commercial solution if it existed."

The deliberate padding was strategic, not deceptive: "You notice I didn't put it to three. I put it to eight."

### 2.2 Costing Parameters

- **250 screens** to convert
- **8 hours estimated per screen** (padded from ~2 hours realistic)
- **25% risk reserve** on top: "Which means that if this number fluctuates up by 25%, or even this number fluctuates up by 25%, we're still okay."
- **Two scenarios modeled:**
  - Scenario A: July delivery (compressed, ~3 months) -- Colin refused to offer any discount: "No situation where we're offering any discount, if that's the case."
  - Scenario B: December delivery (standard, ~8 months) -- Standard pricing with discount room
- **30% margin as the hard floor** for the December scenario
- **Result: $500K SOW**

### 2.3 Safety Net Layering

Colin emphasized the cumulative protection built into the numbers: "I've already said it's four times as much effort on my end. We had to do the screens that I know is probably realistic. On top of that, I threw an extra 25%. And on top of that, I have an extra 25% in my budget in case I need to hire more people to do this."

The layers are:
1. **4x effort padding** (2 hours realistic, quoted at 8)
2. **25% risk reserve** on top of the padded hours
3. **25% budget reserve** for potential additional hiring

If none of these buffers are consumed: "We end up walking away about 75%, 80% margin. And it's all defensible to them."

Defensibility is key. If the client asks why the price is what it is: "Well, we took this, we took this, we took this" -- each layer has a legitimate justification.

---

## 3. Milestone-Based Pricing and Procurement Avoidance

### 3.1 Outcome-Based, Not Headcount-Based

Colin articulated a clear philosophy of milestone-based pricing that deliberately obscures internal resource economics. The core framing: "Rather than you saying based on headcount, you don't need to know the headcount. You don't need to know. If it takes me one person, if it takes me 100, that's my business, not yours. You need to know how much the deliverable outcome is worth to you in the timeline that you want to be delivered."

The client's only negotiation levers are:
1. Ask for a discount
2. Accept a longer delivery timeline
3. Reduce scope

### 3.2 Keeping Procurement Away from Rates

Colin cited Suresh's explicit advice: "Keep their procurement teams the heck away from headcounts and even that amount of hours per deliverable." The risk is that procurement will "try to say, I'm going to divide that, and here's the hourly rate, and we're going to negotiate on that."

The countermeasure: "We can cut it out entirely by just saying, how much is this worth to you? And if this is way off base more than you were thinking, OK, we can see about delivering it at a slower pace or reducing scope."

No disclosure of:
- Offshore vs. onshore resource mix
- Number of resources
- Hourly rates
- Hours per deliverable (to procurement)

Colin stated: "We don't need to even tell them, this is offshore people, onshore people. It'll be purely outcome-based."

### 3.3 Value-Based Pricing Philosophy

The overarching pricing philosophy Colin articulated: **"How much is this worth to you?"** -- not "here's our hourly rate." This shifts the negotiation from cost-plus to value-based. The client is buying an outcome and a timeline, not labor hours.

---

## 4. POC Pricing Philosophy

### 4.1 Never Free

Amit raised the POC pricing issue directly and with conviction: "We should not do a free pilot at all, which I'm feeling we should definitely ask for whatever, even if it's a marginal cost dollar. We should tell them that it's going to cost a little bit... some value should be attached."

The strategic rationale: "If we say we'll do a free pilot, then they might be enticed to do the same pilot with other players also." Free POCs create a perverse incentive for the client to run parallel free evaluations with multiple vendors, extracting value without commitment.

Amit cited industry precedent: "That's one of the reasons Accenture, PwC, or any of these Deloitte's, they do POCs, they do pay because they don't want to keep doing POCs and not being paid and just keep solving problems."

### 4.2 POC as Gateway, Not Giveaway

The discussion framed the POC as the first of two scoping exercises:
1. **Immediate scope of work:** The POC itself, narrowly defined
2. **Broader picture estimation:** "Once we know what that one looks like, we have a good estimate of what the others do. So then the scope of work is just that times time or times effort, if they want to get it done faster."

Colin used a Roman building metaphor: "Almost think of it like pillars in a Roman building. This is just the first column, which is this first project."

The workbook's dedicated POC tab supports this with flexible billing treatment (billed, absorbed, or salaried resource coverage), ensuring even internal-cost POCs are tracked and valued.

### 4.3 Deferred Payment as Alternative

Amit mentioned deferred payment as an acceptable alternative to free: "We can do a defer payment if they want, but some value should be attached." The principle is that the client must have financial skin in the game, even if the timing of payment is flexible.

---

## 5. Lam Research Budget Perception and Urgency

### 5.1 Lam Has No Cost Framework

Colin identified a critical strategic advantage: Lam Research has no internal baseline for what this type of work should cost. The evidence was their mention of "1,000 man hours" for data labeling in an earlier meeting.

Colin's assessment: "They have no idea how much this is worth or how much it's not worth, which is an advantage for us. If they say, like, oh, a thousand man hours to label data, they have no clue what they're talking about. A thousand man hours would be an exceptional amount of money with very little actual value at the end."

He compared it to resume inflation: "They threw out 1,000, and I'm like, it's like on a person's resume. I improved efficiency by 90%. I know you didn't. If you did, you wouldn't be applying for this job. It's a round number because someone told you metrics are good."

Amit reinforced the point, noting that 1,000 man hours could mean 10, 20, or more people, and that "data labeling and managing that team is the biggest entire thing of the training of the model itself." Without knowing database size, number of documents, and redaction requirements, neither side can estimate accurately -- but critically, "the good thing is neither do they."

### 5.2 The "T Mode" Argument

Colin made a forceful case that Lam is in what he called "T mode" -- an existential, must-do situation rather than an optional or convenient project. He noted pushback from Anand on this characterization but stood firm.

Colin's reasoning: "They're unique because they handle their competitor's data. They have TSMC data. So they can't have a screw up here. They are effectively shutting off AI for that duration. So they don't really have a choice but to do this as soon as they can, or risk otherwise exposing information."

The commercial implication is direct: "If it's expensive, it's expensive. It's a safety cost. It's not like a normal business, like this is convenient, nice to have. It's like, make sure we don't end up in a courtroom because our internal tools leaked customer or competitor information."

This reframes the budget conversation entirely. It is not a discretionary technology investment -- it is a risk mitigation imperative. Colin positioned this as meaning Lam's price sensitivity should be lower than a typical engagement.

### 5.3 Scope-First Approach to Budgeting

Colin advocated for determining scope before discussing budget: "Budgets actually for me, it's like secondary almost. Because this is one where... they don't have an option."

The proposed sequence:
1. Get a concrete, narrowed scope from the upcoming meeting (the "entry point")
2. Use the costing workbook to calculate what that scope should cost
3. Present the number to Lam
4. Let them react -- "They can either say, oh my god, or they can say, yeah, sounds good, because we're a manufacturing company. We've got money to spend."

Amit agreed but wanted the team to be prepared with hypothetical numbers: "Can [we] play with this to come up with a hypothetical scenario? In case the conversations come around, you tell us what the number is and they are like, we tell them something." Colin suggested waiting until after Monday's meeting to have a concept of scope before running scenarios in the workbook.

---

## 6. Information Control as Commercial Strategy

### 6.1 Solution Opacity

A major theme running through the pricing discussion was deliberate information asymmetry. Colin described a layered approach to what gets shared with Lam:

**What to share:** The overall architecture, the hybrid deterministic/AI approach, the Cohere case study, the end-state vision (unified data plan). Colin stated: "I will sound intentionally like I'm giving away all the detail."

**What to withhold:** The implementation specifics that make it actually work. Colin called these "the spark plug that actually makes it work in practice" and "secret ingredients." His confidence in sharing the architecture: "Technically speaking, I have confidence that they can give this to anyone else, and they won't be able to deliver it."

**Why share at all:** To gain credibility with the technical team (Daniel Harrison) and to set questions that competitors cannot answer well: "It's almost like an RFP, but we're intentionally asking hard questions that we can answer great, but we know other people are going to fall over on."

### 6.2 Costing Opacity

The pricing approach mirrors the solution approach. The client sees:
- Milestone-based deliverables with associated costs
- Timeline options with corresponding price points
- Discount thresholds

The client does not see:
- Internal hourly rates
- Resource mix (onshore/offshore)
- Headcount
- Hours-per-deliverable breakdowns
- Margin calculations
- Risk reserve percentages

Amit reinforced this: "We should not give them if it's going to take us a day or a month. We need to gauge what their appetite is as well."

### 6.3 Off-the-Shelf Tool Pricing Awareness

Colin revealed an interesting detail about the deterministic layer of the solution: standard tools like Microsoft Purview could handle the PII redaction portion for approximately **$7/month per user**. Setup would take roughly **1.5 hours** by someone with the right expertise.

His explicit instruction: "The trick is they don't need to know that it's $7 a month and that it would take someone like us to set up for an hour and a half. They don't need to know that. They just need to know that this is one part of a much grander solution."

This is positioned not as deception but as proper solution framing -- the off-the-shelf component is genuinely one part of a larger custom engagement, but the client does not need visibility into the cost breakdown of individual components.

---

## 7. Key Pricing Principles (Summary)

Drawing from the full discussion, Colin's pricing methodology for the Lam engagement follows these principles:

1. **Scope first, budget second.** Get a concrete entry-point project defined before discussing numbers.
2. **Deliverables-based, not time-and-materials.** Price by outcome, not by hour or headcount.
3. **Pad aggressively but defensibly.** Use conservative estimates (4x in the Cisco case), then add risk reserves on top.
4. **Layer your safety nets.** Effort padding, risk reserve, and budget reserve are three distinct protection mechanisms.
5. **Never reveal internal economics.** Procurement should not see hourly rates, headcounts, or resource mix.
6. **Frame as value, not cost.** "How much is this worth to you?" positions the engagement as an investment, not an expense.
7. **POC must cost something.** Even marginal cost prevents multi-vendor free POC shopping.
8. **Exploit the client's lack of baseline.** Lam has no internal reference for what this should cost, which provides pricing power.
9. **Leverage existential urgency.** Lam handles competitor data (TSMC) -- this is risk mitigation, not optional enhancement.
10. **Maintain information asymmetry.** Share enough architecture to build credibility; withhold enough implementation detail to prevent replication.
