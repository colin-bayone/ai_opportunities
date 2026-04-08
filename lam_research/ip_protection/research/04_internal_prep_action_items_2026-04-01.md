# 04 - Internal Prep: Action Items and Deliverables

**Source:** /lam_research/ip_protection/source/internal_anuj_amit_pratik_colin_04-01-2026.txt
**Source Date:** 2026-04-01 (Internal BayOne prep call)
**Document Set:** 04 (Internal Prep Call)
**Pass:** Focused deep dive on action items, deliverables, and logistics

---

## Meeting Logistics: Monday April 6th with Lam Research

### The Lam Meeting

- **Date:** Monday, April 6, 2026
- **Duration:** 1.5 hours
- **Lam Attendee:** Daniel Harrison (Senior Director, technical manager; currently works with BayOne's Philippines team; approximately 10 years at Lam; described as having done "everything under the sun" technically except AI/ML expertise)
- **Format:** In-person at Lam's location

### BayOne Attendance

| Person | Attendance | Notes |
|--------|-----------|-------|
| Anuj | In-person, confirmed | Will attend at Lam's location |
| Colin | Likely remote | Travel constraints; team (12 people) struggles when Colin is in Pacific time zone; management pushing back on travel; Colin acknowledges in-person is better for dynamics and body language reading but cannot commit for the 6th |
| Amit | Not explicitly confirmed for Monday meeting | Needs to be ready with costing scenarios |
| Pratik | Not explicitly discussed for Monday | On the call but attendance at Lam not addressed |

### Internal Sync Before the Lam Meeting

- **Monday sync call:** Colin committed to scheduling one ("I'll put one for Monday already, so that we are fresh on what we're going to do")
- **Friday check-in option discussed:** Amit asked whether the team should connect Friday or Monday; Colin said either works; team left it that a Monday sync was confirmed, with Friday as optional if anything comes up ("In case we think of anything tomorrow, then we can also do that by day")
- Colin's assessment: not much additional prep needed before Monday because "we actually already did a lot of the legwork already"

---

## Action Items

### Colin - Owner

| Action Item | Timeline | Status/Notes |
|-------------|----------|--------------|
| Polish the question list for Daniel | Before Monday meeting | Colin has an existing list of technical questions; plans to "condense these down" so verbal questions are detailed but written materials stay high-level; described as taking "all three seconds" |
| "Crest up" the presentation details | Before Monday meeting | Take existing materials and polish them for presentation; Colin described this as light-touch work on already-completed materials |
| Share the costing workbook with Amit | Before Monday (ideally by Friday) | Colin demonstrated the workbook on the call; Amit requested access to review and play with it |
| Schedule the Monday sync call | Before Monday | Colin committed: "I'll put one for Monday already" |
| Structure the 1.5-hour meeting | Before Monday | Colin outlined the structure during this call (see Meeting Structure section below) |

### Amit - Owner

| Action Item | Timeline | Status/Notes |
|-------------|----------|--------------|
| Review and play with the costing workbook | Between receiving it and Monday meeting | Amit to create hypothetical scenarios so numbers are ready "in case the conversations come around" during the Lam meeting; Amit said: "I would just want to take a look at it... suggest some inputs" |
| Be prepared with costing scenarios | By Monday meeting | If scope conversations happen during the meeting, Amit should be ready to discuss what the numbers look like |

### Anuj - Owner

| Action Item | Timeline | Status/Notes |
|-------------|----------|--------------|
| Attend Monday meeting in person | April 6 | Confirmed attendance at Lam's location |
| Provide context on Daniel Harrison during the meeting | April 6 | Anuj has firsthand knowledge of Daniel from interviews and discussions; described Daniel's background and current work |

### Team - General

| Action Item | Timeline | Status/Notes |
|-------------|----------|--------------|
| Think of additional items by Friday | By Friday April 4 | Colin left the door open: "In case we think of anything tomorrow, then we can also do that" |
| No new material creation needed | N/A | Colin's assessment: existing materials are sufficient; only polish needed |

---

## Existing Deliverables (Already Shared with Lam)

### 1. Problem Restatement / "What We Understood" Document
- **Status:** Already shared with Lam; Lam confirmed it was correct ("they said we understood it correctly")
- **Purpose for Monday:** Colin plans to restate the problem at the start of the meeting as a credibility-establishing move ("restating the problem to them, doing that quickly, high level, allowing for them to ask questions... that establishes part one of credibility, which is these guys understand")
- **Note:** This is described as two separate documents: (a) the discovery steps that were shared, and (b) the "what we understood" document

### 2. Preliminary Technical Approach / Solution Architecture
- **Status:** Exists in some form; Colin walked through it on the call
- **Content includes:**
  - Two-layer architecture: deterministic layer (off-the-shelf tools like Microsoft Purview for PII/role-based redaction) plus custom AI layer for domain-specific IP protection
  - "Unified data plan" concept as the end-state vision
  - Enterprise tools integration (credential/access management, governance, visibility)
  - Emphasis on building on Lam's existing systems rather than introducing new platforms
- **Intentional information management:** Colin described deliberately making this look comprehensive while omitting the "spark plug" implementation details that make it actually work in practice; the approach is designed so that even if Lam shares it with competitors, those competitors cannot replicate it without the missing expertise

### 3. Cohere Case Study / Reference Experience
- **Status:** Colin has this ready to present verbally
- **Content:** BayOne (specifically the AI practice) did this exact type of IP protection project for Cohere "from the earlier days of AI when things were a lot less defined"
- **Purpose for Monday:** Establish technical credibility by showing prior experience with the same problem, and note that Cohere's case was actually more complex (involving China and international business considerations versus Lam's US-based employee scope)

---

## Deliverables to Prepare or Finalize

### 1. Polished Question List for Daniel
- **Owner:** Colin
- **Status:** Draft exists; needs condensing and reformatting
- **Key questions to ask Daniel (identified during this call):**
  - What was tried technically in-house? What was the specific scope of that effort?
  - What failed and why? What was the outcome?
  - What are the success criteria? (Reference: Mikheil mentioned 97% accuracy in under 5 seconds on a prior call -- is that a need, a want, or a dream?)
  - Gauge in-house capability without explicitly asking ("understand what their in-house capability is like without explicitly asking the question")
  - Assess whether they perceive this as an easy or hard problem
  - What tools/technologies are in their current stack? (.NET confirmed for current engagement; TestComplete being explored for testing automation)
  - Competition: are other vendors being evaluated, or is it just BayOne?
  - Timeline: how urgently do they need this?
  - What is the specific application or entry point they want to start with?

### 2. Costing Workbook
- **Owner:** Colin (created); Amit (to review and run scenarios)
- **Status:** Built and demonstrated on this call; used for the Cisco engagement already; needs to be shared with Amit
- **Description:** Multi-tab Excel workbook for project costing:
  - **Instructions tab:** First page with guidance
  - **Personnel tab (input):** Working locations, annual/hourly rates, base rates, loaded costs per resource, project allocation percentages, productivity multipliers (junior = 0.25, mid = 1.0, senior = 2.0)
  - **Project Inputs tab (input):** Number of deliverables, estimated hours per deliverable, risk reserve percentage, POC items, travel, hardware/consumables, monthly subscriptions, one-time equipment costs, margin thresholds and targets
  - **POC tab:** Dedicated tab for proof-of-concept costing; can designate costs as billed to client, absorbed by BayOne, or covered by salaried resources
  - **Scenario tabs:** Support for multiple scenarios (e.g., Scenario A vs. B with different timelines)
  - **Comparison tab:** Bird's eye view across scenarios
  - **Throughput tab:** Calculates team capacity, minimum/safe hours, risk reserve impact on capacity; allows "what if" modeling (team of 5 juniors vs. 2 seniors vs. hybrid)
  - **Key principle:** Only yellow cells are inputs; blue cells are calculated; changes propagate through entire workbook from the two input tabs
  - **Margin/discount logic:** Shows maximum discount before hitting margin floor; accounts for risk reserve on top of margin
- **For Lam specifically:** Cannot be populated until scope is defined in the Monday meeting; Amit should prepare hypothetical scenarios so the team is ready if the conversation turns to numbers

### 3. Meeting Presentation Materials
- **Owner:** Colin
- **Status:** Existing materials need light polish ("crest them up")
- **Content:** Problem restatement, Cohere experience, preliminary approach, question list
- **Note:** Materials are intentionally designed to share enough to establish credibility while withholding implementation specifics

---

## Agreed Meeting Structure for Monday (1.5 Hours)

Colin outlined the following structure, which the team endorsed:

### Phase 1: Establish Credibility (Opening)
1. **Restate the problem** -- High level, quickly, allow questions; demonstrates "these guys understand"
2. **Present Cohere experience** -- "Here's a company just like you with the exact same constraints and even more complicated"; cover what was tried, what did not work, why a hybrid solution was the right fit
3. **Present preliminary approach** -- Show the deterministic + custom AI two-layer architecture; present the "rosy picture" of the unified data plan end-state; intentionally appear to give comprehensive detail while omitting critical implementation specifics

### Phase 2: Discovery Questions (Target ~45 Minutes)
4. **Technical questioning** -- Go through the question list; this is the primary purpose of the meeting since it was set up based on BayOne's request for more technical understanding
5. **Key extractions needed:**
   - What was tried before and why it failed
   - Specific application or entry point (force them past ambiguity)
   - In-house perception of problem difficulty
   - Competition landscape
   - Success criteria definition
   - Scope boundaries

### Phase 3: Scoping and Next Steps (Closing)
6. **Give a "teaser"** of the potential solution tied back to their answers
7. **Steer toward concrete outcomes:** scope, timeline, budget appetite
8. **Goal:** Leave with enough information to produce a proposal; avoid needing another meeting ("the goal out of the next is the actionable outcome from there... what we need is the amount, date, time, how quickly they want to do")
9. **If costing comes up:** Have Amit's hypothetical scenarios ready; do not disclose headcount or hourly rates; frame as outcome-based/deliverable-based pricing

---

## Strategic Decisions Made on This Call

### Pricing Strategy
- **Outcome-based pricing, not headcount-based:** "You don't need to know the headcount... you need to know how much the deliverable outcome is worth to you in the timeline that you want"
- **Keep procurement away from hourly rates:** Per Suresh's advice from the Cisco engagement, avoid giving procurement teams any basis to calculate per-person rates
- **No free pilot:** Team agreed unanimously; Amit emphasized this strongly ("we should not do a free pilot at all"); even a marginal cost is acceptable; deferred payment is an option; rationale: free POC invites competitors to also do free POCs
- **Risk reserve built into costing:** 20-25% buffer on top of margin to cover unknowns
- **Leverage urgency:** Lam handles competitor data (specifically TSMC data); an IP leak is a legal/courtroom risk, not a convenience issue; this limits their ability to negotiate on price or delay

### Information Sharing Strategy
- **Share enough to establish credibility, withhold implementation specifics:** "Not give enough that they can actually move up on their own"
- **Remind of NDA/non-disclosure obligations** when sharing technical details
- **Assume Lam may share materials with competitors:** Design all shared materials so that even if forwarded, competitors cannot replicate the approach
- **Ask questions that double as competitive barriers:** "It's almost like an RFP, but we're intentionally asking hard questions that we can answer great, but we know other people are going to fall over on"
- **Do not disclose solution timeline or level of effort:** Gauge their appetite first; if they want a large engagement, scope it accordingly; if they want small, "let's give them enough, they can have to go, but if we give them enough, then we have some revenue"
- **Do not discuss the solution in detail:** Focus on what it will cost and how long it will take, not how it works

### What Lam Will Likely Ask (Based on Past Experience)
- Anuj warned: "They want to give out less and ask more" -- expect them to deflect questions and instead ask "What have you done? What is the industry doing? What do you think?"
- Anuj noted: "They are not very clear on what they want" -- expect continued ambiguity on scope
- Amit noted: Lam (especially Brad) always wants to know what others are doing, what industry experience BayOne brings from other customers
- Amit suggested: Be prepared to discuss off-the-shelf tool landscape (and why none are sufficient for a custom solution)

---

## Desired Outcomes from the Monday Meeting

The team explicitly agreed on these objectives:

1. **Competition intelligence:** Find out if BayOne is the only vendor or if others are being evaluated
2. **Concrete timeline:** When does Lam need this done? How urgent is it?
3. **Concrete project scope:** Get them to commit to a specific application or entry point rather than the broad "constellation" of possibilities; ideally point to what they tried before as the starting scope
4. **Scoping for proposal:** Enough detail to produce an SOW; two types of scoping: (a) immediate scope of work for the entry point, (b) broader estimate across all applications based on the first one as a template ("this is just the first column... once we know what that one looks like, we have a good estimate of what the others do")
5. **Budget appetite:** Gauge what their expectations are without directly asking
6. **Daniel's technical perspective:** What was done before, why it failed, what his team's capabilities are
7. **Actionable next step:** Ideally a signed-off SOW or at minimum a paid POC; avoid another open-ended meeting

---

## Open Items and Risks

| Item | Risk/Concern | Mitigation |
|------|-------------|------------|
| Colin may not attend in person | Loses the in-person dynamic advantage that Anuj specifically values ("the dynamics shift quite a bit... the nuances are there") | Anuj attending in person partially mitigates; Colin acknowledged the importance and is trying to resolve travel constraints |
| Lam may still be ambiguous on scope | Cannot cost or propose without a defined scope | Question list designed to force specificity; Colin plans to extract scope during the meeting |
| Lam may share materials with competitors | Could enable a competitor to undercut BayOne | All materials designed to appear comprehensive while omitting critical implementation details |
| Lam may try to do it in-house | If they feel the problem is solvable, they may attempt it internally | Present enough complexity to demonstrate that this requires specialized expertise |
| Costing workbook needs scope inputs | Cannot produce real numbers without scope from Monday meeting | Amit to prepare hypothetical scenarios; real numbers will follow after Monday |
| Team size for this engagement undefined | Cannot allocate resources without scope | Costing workbook supports scenario modeling; will be populated post-Monday |
| No formal Friday sync scheduled | Could miss prep window | Monday sync confirmed; Friday left as informal option if something comes up |
