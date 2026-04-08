# 02 - Meeting: Business Opportunity (Deep Dive)

**Source:** `source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on business opportunity and engagement

---

## 1. Brad's Ownership Structure and Engagement Scope

Brad owns the entire vertical end-to-end. This is stated explicitly and unambiguously in the meeting:

- **Brad (direct quote):** "I own the entire thing... I am the business case, the product definition, the ideation, and the openness. I've been in my organization. I have everything from business, program, product, to technical."
- **Mikhail clarified the structure:** "Brad owns both product, engineer, and kills that guy." (likely "builds" - transcription artifact)
- **Three functional pillars under Brad:** Daniel handles the technical function, someone handles program, and Brad (with Mikhail) handles product. "So between the three functions, we put scrum teams together."
- **Broader team exists but wasn't present:** "You only met three people, but... even some of the people, but yes, end to end, with a brass [Brad's] beam [team]."

**What this means for engagement scope:** BayOne is dealing with a single decision-maker who controls business case, product definition, ideation, AND execution. There is no need to navigate between business stakeholders and engineering stakeholders -- Brad is both. This simplifies the engagement significantly because:
1. No alignment gap between "the business" and "the builders"
2. Brad can authorize work, define scope, and resource it from within his own org
3. No cross-organizational approvals needed for initial work (though matrix dependencies exist for some systems they don't own)

**Matrix caveat:** Brad acknowledged: "Of course, there is, of course, matrix pieces. We do have some systems within this flow that we don't own. But our initial focus is to prove out this case within our systems." This means Brad can greenlight work within his domain, but expanding to org-wide would require other stakeholders.

---

## 2. How Brad Described the Ideal Engagement Approach

Brad was very explicit about what he wants and does not want from the engagement. Key statements, closely paraphrased:

### Rapid prototyping, not long projects
- "We want to get to some rapid prototyping. I mean, we don't want these things to take months and years, right? We want these things that we can chunk them down, prove these things, and then kind of determine, because not everything may work, right?"
- "Similar to what we did last year, we would try those incremental steps to see proving out that we get those things."

### Evolutionary, not revolutionary
- "And we're not expecting to be revolutionary and right out of it. Evolutionary is absolutely fine."
- Colin's response to this: "That's super helpful because I will tell you the biggest barrier to this for most organizations is absolutely that kind of appetite to change."

### Technology agnostic -- not married to AI
- "I also want to stress, I know AI is a very sexy word, but it's also a meaningless word, and not married to any specific AI technologies, LLM, machine learning, or anything like that, it doesn't have to be an AI."
- "Preference on AI? Sure, because your kind of ceiling goes up with AI, what you can do afterwards, because other solutions are very important solutions. But I just want to make sure that that message is clear, right? It doesn't have to be."
- Mikhail reinforced this: "One thing I don't want us to limit is to just LLMs and generative AI."

### Open to any and all approaches, with trade-offs explained
- "We are open to any and all approaches by also understanding what are the trade-offs and what are the outcomes that we can expect with those."
- "Anything and everything... is on the table. We think and we believe that we can, I don't know, CNF, pilot, POC, whatever fancy word you want to use, right? And prove that that is the right approach to start to address those challenges and problems."

### Start small, prove incrementally
- "We want to start small and prove incrementally that we can solve certain things."
- "We're starting very, very small."
- On fields to start with: "That's why we're kind of limited to fields to see if we can prove out." (referring to customer name and file name as initial targets)

---

## 3. The "Pod" Reference

Brad made a very specific distinction about how a previous engagement worked versus how future work would work:

- **Brad (direct quote):** "I want to be really clear like... it's not gonna be me like writing user stories requirements. I'm gonna have somebody as part of my team, you're gonna... your team is gonna be working with, it's not gonna be like did for the pod working because that was a pilot that was the only reason. That's not a standard mode of operation."

**Analysis:** The "pod" appears to reference a previous pilot engagement (likely with BayOne or another vendor) where the working model was more embedded/collaborative -- possibly Brad or his team directly writing user stories and working in a tightly coupled "pod" structure with the vendor. Brad is explicitly saying:
1. That was a one-time pilot arrangement
2. It is NOT how things will work going forward
3. His team will handle user stories and requirements internally
4. BayOne's team would work with designated members of Brad's team, not with Brad directly on requirements

This is an important structural signal: the engagement model will be more traditional (Brad's team defines requirements, vendor team executes) rather than an embedded pod model.

---

## 4. What Brad Explicitly Said About NOT Writing User Stories

This was stated clearly and with emphasis:

- "I want to be really clear like it... if we decide to go there, it's not gonna be me like writing user stories requirements. I'm gonna have somebody as part of my team."

**Implication for BayOne:** Do not propose an engagement model where Brad is expected to be hands-on writing requirements or user stories. He will assign team members for that. BayOne needs to be prepared to work with Brad's designated team members (likely Daniel and others) for the day-to-day technical and requirements work. Brad is the strategic decision-maker and approval authority, not the working-level collaborator.

---

## 5. The ROI Framing: Escalation Costs, Feedback Loop, Knowledge Enrichment

Brad and Mikhail laid out a clear ROI framework built around the troubleshooting workflow: Self-Help -> Ask for Help (Expert Help) -> Escalate.

### Cost structure
- **Brad (direct quote):** "When you're over here [escalation], this is very, very costly."
- Escalation affects: cost, customer trust, other downstream impacts
- **The goal is to shift volume leftward:** "The goal is to drive this down [escalation] and drive this up [self-help]... theoretically, you will never get here [zero escalation]. The goal is to get here [self-help] and drive it [escalation] down."

### The feedback loop vision
This is central to the business case. The vision is cyclical:

1. Problems enter the system through self-help, expert help, or escalation
2. Once a problem is solved (at any tier), the problem statement AND the answer should feed back into the self-help knowledge base
3. Next time someone encounters the same problem, they find the answer at the self-help level without escalating
4. This progressively reduces escalation volume and cost

**The blocker to the feedback loop:** The feedback loop cannot be built until IP/redaction is solved. Brad and Mikhail stated this clearly:
- "Until we have confidence, we can't fool [fully] build this feedback loop and take unstructured data that we know is restricted, or potentially could be restricted, and feed it into the general training area."
- The unstructured data problem is the gate: even if the user who entered the data is identified, "it still doesn't tell us if here there is data that they shouldn't be putting."

### Predictive analysis as eventual ROI multiplier
- Pat (Raquel) mentioned: "That's actually the ROI on the ML, KI, all of that is predictive analysis. Because once the root cost analysis of, let's say, 10, 100,000, the data points come in, then it predicts it in the very first layer itself."
- This suggests a longer-term vision where enough data flowing through the feedback loop enables predictive troubleshooting at the self-help tier.

### Over-restriction as current cost
- **Brad:** "Our current mode of operation is we over restrict... And by doing that, we know that we're limiting because we're limiting the knowledge, the information."
- **Mikhail:** "True, but we're also knowing that we're limiting the productivity, the capability, because we don't share that much."
- Example: "If document three has the path to solution, but you only can look at Intel documents and this sits in a Samsung space, you're not going to see that."
- This over-restriction also limits what data can be used to train AI models: "This also limits to what data we can train our AI agents on... because, hey, if this source is restricted and we cannot control whether this data could be trained for general public, we're not going to pass the source to the model."

---

## 6. Every Next Step Mentioned

### Follow-up meeting
- Brad stated clearly a follow-up meeting would happen: "The follow up meeting that we would have on this."
- **Who will be there:** "We'll bring in a broader set of folks."
- **Why this meeting was smaller:** "We just wanted to make sure we had focus on the problem, the kind of challenging, kind of so forth. So we had clarity around that."
- **What the follow-up meeting is for:** "In the follow up, we would have others here to look at the different approaches, trade-offs, Q&A, those types of things, because then we bring in other folks."
- Colin confirmed: "We can connect folks, too."
- Pat acknowledged: "Everyone else has a day job... so my day job is this. I get to focus on this."

### Technical connection
- There was agreement that Colin would connect with Daniel (Brad's technical lead) for deeper technical discussion: "I just want to make sure that Colin had some more technical aspects to it."

### High-value targets question (asked but answer cut off)
- Colin asked: "From your perspective, let's talk like high value targets for this. If we had the initial... where would we be best to focus? Is there like a specific platform that you're looking at right now or use case internally?"
- Mikhail began answering: "Two things. Number one, one of the things we wanted to..."
- **The transcript cuts off here.** The answer to this critical question is not captured.

---

## 7. Deal Signals: Real vs. Exploratory

### Strong signals this is real (not just exploratory)

1. **Previous pilot already happened:** "Similar to what we did last year, we would try those incremental steps." They have already worked with BayOne (or a vendor) in a pod structure. This is a continuation, not a cold start.

2. **Brad owns the full stack:** He doesn't need to sell this internally to another group. He IS the business case, product definition, ideation, and execution owner.

3. **Specific technical history:** They've already tried multiple ML approaches (Transformers, Spacey, Azure AI model), invested in MLOps, done labeling estimation (1,000+ man hours), and know specific false positive rates (20% down to 17%). This is not theoretical exploration -- they've spent real resources already.

4. **Clear articulation of what didn't work and why:** The 20% false positive rate, the 1,000-hour labeling estimate, the rule-based approach limitations with spelling variations. They know exactly where they've hit walls.

5. **Brad is asking for "high value targets":** He asked Colin directly where to focus first. This is a buying signal -- he's asking BayOne to help prioritize, which means he's thinking about actually doing it.

6. **Evolutionary appetite confirmed:** Brad explicitly said revolutionary isn't expected. This lowers the risk of scope paralysis.

7. **Brad's team structure is ready:** He has product, program, and technical functions that can "put scrum teams together." The organizational infrastructure for execution exists.

8. **They want BayOne's outside perspective:** "We're also looking for feedback because we can't be the only company that have this... also interested to get a different perspective on where and how we should approach."

### Caution signals

1. **"We've heard it before":** Brad said explicitly: "We don't want to have the discussion right now about, oh, I've got a technology solution that can solve that. We want a very, because we've heard it before, we want people to be, we want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve." This implies previous vendors have jumped to solutions without understanding the problem. BayOne needs to demonstrate deep problem understanding first.

2. **No budget discussion in the transcript:** No dollar figures, no quarterly allocation, no headcount numbers were mentioned. This is notable for its absence.

3. **No timeline discussed:** No dates, no sprints, no "we need this by Q3." The urgency is implied by the escalation cost problem but not explicitly stated.

4. **Complexity acknowledged repeatedly:** "We know it's very complex. We know there's probably not going to be a one-on-one end-all thing." This could mean realistic expectations or could mean the problem is so big they keep studying it without acting.

---

## 8. Brad's "High Value Targets" Question and the Answer

Colin asked the question near the end of the meeting: "From your perspective, let's talk like high value targets for this. If we had the initial, let's say you call it, like you said, whatever fancy word, three letter word we wanna call it, where would we be best to focus? Is there like a specific platform that you're looking at right now or use case internally? I know there's a lot of different systems and tools. What would be the most impactful for you if we were to tackle it immediately?"

Mikhail began to respond: "Two things. Number one, one of the things we wanted to..."

**The transcript cuts off here.** The answer -- which would have been critical for proposal scoping -- is lost. This needs to be recovered in the follow-up meeting or a separate conversation.

---

## 9. Budget, Timeline, and Resources

**Budget:** Not mentioned anywhere in the transcript. No dollar figures, no quarterly allocations, no references to approved budgets or budget requests.

**Timeline:** Not explicitly discussed. The only temporal references are:
- "We don't want these things to take months and years" (anti-pattern, not a timeline)
- "Similar to what we did last year" (previous pilot was in 2025)
- The IAM program has been going on "probably for about two years"

**Resources:** Brad indicated his team has the following available:
- Product function (Mikhail and Brad)
- Program function (someone unnamed)
- Technical function (Daniel)
- Scrum teams can be assembled from these functions
- "You only met three people" -- broader team exists
- Brad will assign team members to work with BayOne; he won't be writing user stories himself

**Labeling cost reference:** Mikhail mentioned "over a thousand man hours" for the labeling exercise they evaluated. This gives a sense of the scale they're operating at, but it's framed as a cost they were trying to avoid, not a budget they spent.

---

## 10. How Brad Framed the Relationship with BayOne

Brad's framing positions BayOne as a **consultant/advisory partner**, not a pure vendor or a staff augmentation resource:

- **Seeking outside perspective:** "We're also looking for feedback because we can't be the only company that have this or are experiencing these types of challenges. So also interested to get a different perspective on where and how we should approach."
- **Expertise expected:** Brad asked Colin for "high value targets" -- where to focus. This is asking for strategic advisory input, not just execution capacity.
- **Understanding before solutioning:** "We want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve." This positions BayOne as needing to earn credibility through demonstrated understanding.
- **Not embedded pod going forward:** The previous pod model was a pilot. Future engagement will be more structured: Brad's team defines, BayOne's team executes/advises.

Colin positioned BayOne/himself as bringing:
- Relevant direct experience: "I came from... Coherent, from laser semiconductors and advanced materials side of the house"
- IP protection expertise: "managing IP, the exact same problem... I think we have a good grip on"
- Specific domain credentials: ITAR, CMMC, DFARs, China operations, AI Center of Excellence
- AI leadership: "I'm our head of AI here at Bay One"

---

## 11. "We've Heard It Before" and What It Implies

Brad's statement: "We don't want to have the discussion right now about, oh, I've got a technology solution that can solve that. We want a very, because we've heard it before, we want people to be, we want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve, right? And so that's critically important."

**What this implies:**
1. **Other vendors have pitched them.** Brad has been through at least one (likely multiple) rounds of vendors proposing AI solutions before fully understanding the problem.
2. **Those engagements likely disappointed.** The emphasis on "we've heard it before" carries a tone of skepticism or fatigue with premature solutioning.
3. **The bar for BayOne is "repeat the problem back."** Before any proposal or solution discussion, Brad wants to see that BayOne can articulate the problem as well as his team can. This is a trust-building gate.
4. **Solutioning too early is a disqualifier.** If BayOne comes back with "here's our AI platform that solves this," they will likely lose credibility.
5. **The right move:** Come back with a problem decomposition document that demonstrates deep understanding, THEN propose approaches with trade-offs.

---

## 12. The "Repeat Back" Requirement

Brad made this a specific ask, not a passing comment:

- "We want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve, right? And so that's critically important. Then we can figure out, okay, what are the approaches we can take to actually prove those things out."

**The sequence Brad expects:**
1. BayOne demonstrates understanding of the problem (repeat back)
2. THEN approaches and trade-offs can be discussed
3. THEN incremental proof/prototyping can begin

This is a gating sequence. Step 1 must be completed before steps 2-3 are even on the table.

---

## 13. Internal Stakeholders Beyond Brad's Team

### Mentioned as needing to be involved
- **Daniel** (Brad's technical lead) -- not present in this meeting, will be in the follow-up: "We'll bring in a broader set of folks."
- **Broader team members** -- "You only met three people" -- others exist and will be brought in for the follow-up meeting.
- **Monica** was mentioned by name as part of the broader team: "Monica was blessed [part of the team]."

### Systems they don't own
- Brad acknowledged: "We do have some systems within this flow that we don't own." Those system owners would eventually need to be involved if the solution expands beyond Brad's domain.

### Enterprise-level stakeholders
- IAM (Identity Access Management) program is an active 2-year company-wide initiative. Brad's work would eventually intersect with this.
- Engineering systems access discussions are happening at a broader company level (the example about office workers having access to drawings and schematics).

### Not mentioned but likely relevant
- Security/compliance team (given the IP sensitivity)
- Customer-facing teams (since customer trust is part of the ROI argument)
- IT infrastructure team (given the diverse tech stack)

---

## 14. Risk Signals and Concerns

### Risks expressed by Brad/Mikhail (their concerns about the problem)

1. **False positive sensitivity:** "We're much more sensitive in this space to false positives rather than over-redacting... If every fifth thing I say, hey, you possibly have a violation, then you're like, no, I don't. People are just not going to trust it." The 20% false positive rate killed their previous ML approach. They need "way below 1% end state."

2. **Unstructured data complexity:** "Majority of the data that we're concerned with today for this discussion is unstructured data. So it lives inside documents. It could live inside the meeting transcripts. It could live in the procedures or a problem test."

3. **Spelling/format variation:** Rule-based models struggled because "a fab could be spelled many different ways... Some people put a micro 11, some put F11, some put PAP space 11, PAP dash 11."

4. **Infrastructure fragmentation:** "Anything you can think of most likely [the infrastructure] has... because these are not two, three systems... some of it on prem, some of it is on cloud, some of it is eventually gonna move to cloud, some of it is Lam GPT." Six different search systems exist.

5. **Previous ML results were disappointing:** Transformers, Spacey, and Azure AI model all produced ~20% false positive rates. Fine-tuning only improved to 17%. This is effectively out-of-the-box performance.

### Risks for BayOne (concerns about the engagement)

1. **No budget discussion:** The absence of any budget conversation is notable. It could mean budget exists and isn't worth discussing yet, or it could mean budget hasn't been secured.

2. **Complexity could stall action:** Despite Brad's stated appetite for rapid prototyping, the problem is genuinely complex. Multiple previous attempts have stalled or failed. There's a risk of analysis paralysis.

3. **"We've heard it before" skepticism:** Previous vendor experiences have created a trust deficit. BayOne must navigate this carefully.

4. **Transcript cut off at the critical question:** The "high value targets" answer -- which would scope the initial engagement -- is missing. BayOne is proceeding without knowing Brad's top priority targets.

5. **The pod model is explicitly off the table:** BayOne cannot propose an embedded working model. They need to be prepared to work in a more arm's-length structure with Brad's designated team members.

6. **Enterprise IAM is a parallel workstream:** Solutions that depend on robust identity management may be premature given the 2-year-old IAM program is "not super robust" yet.

---

## 15. Colin's Advisory Input During the Meeting

Colin made several substantive contributions that positioned BayOne's expertise:

### Unified control plane recommendation
- "There has to be commonality between these applications... about 95% of a redaction application is identical. The only thing that really changes is maybe some strategy for ingestion."
- "If you want to... put your lasso around a lot of things at the org... overall, you don't want to keep things so fragmented because you're going to end up trying to play whack-a-mole with this."
- "Making sure that entry point is very robust, that is where the biggest bang for your buck is going to be here for sure."

### Ingestion-first philosophy
- "Redaction on the output tends to be, like you said, very heavy... doing it on ingestion... if you can have that unified kind of layer first, that's what's going to help you the most out of anything we can talk about."
- "Even if information comes out, you shouldn't have to redact anything if this part [ingestion] actually worked."

### Assessment of previous ML results
- "When I heard 20%... that's pretty much out-of-the-box ChatGPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all."
- Mikhail confirmed: "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."

### Questions that demonstrated understanding
- Asked about the infrastructure stack (Azure, on-prem, etc.)
- Asked about governance and shadow IT concerns
- Asked about regional restrictions and compliance (ITAR-adjacent thinking)
- Distinguished between Gen AI (unstructured text) and ML (numeric/scientific data) use cases

---

## 16. Two Distinct Business Cases Identified

Mikhail was very deliberate about separating these:

### Business Case 1: Self-Help Search Enablement
- **Problem:** Over-restricted search results limit productivity
- **Current state:** Six different search systems, segmented data, restrictive access policies
- **Goal:** Enable broader search results by redacting/removing customer-confidential information rather than restricting entire documents
- **Approach:** Detection and redaction (heavier, not real-time)
- **Success metric:** "If we over-redact less, we already have success"
- **Sensitivity:** Accuracy-focused; some over-redaction is acceptable

### Business Case 2: Expert Help / Escalation Entry Point
- **Problem:** Users entering customer-identifiable information into problem statements and tickets
- **Current state:** Samsung employees can't see Micron tickets and vice versa; restricts cross-pollination of solutions
- **Goal:** Detect potential policy violations at entry point; notify users in real-time
- **Approach:** Real-time detection (not redaction); "big brother approach"
- **Performance requirement:** "Two to five seconds max" -- must be within UI standards
- **Sensitivity:** False-positive-focused; 20% false positive rate was unacceptable; target is "way below 1%"
- **Key distinction from Case 1:** "This is not about redaction. This is about detection."

Mikhail emphasized these should be treated as separate swim lanes: "When we say small piece and MVP, I would expect them not being jumbled together, but they could be separate swim lanes."

---

## 17. What Was NOT Discussed

Notable absences from the conversation:

1. **Competitive landscape** -- No mention of other vendors currently being evaluated alongside BayOne
2. **Budget or procurement process** -- No discussion of how work would be contracted, purchased, or funded
3. **Success criteria beyond false positive rates** -- No KPIs, no business metrics tied to dollar savings
4. **Data volume** -- No mention of how many documents, tickets, or searches are processed
5. **Regulatory requirements** -- No mention of specific regulatory frameworks (SOC2, ISO, etc.) that might constrain solutions
6. **Timeline or urgency** -- No deadlines, no "we need this by" statements
7. **Decision-making process** -- No mention of who approves vendor selection or engagement terms beyond Brad
8. **Contract structure** -- No discussion of how a POC or pilot would be structured commercially

---

## 18. Summary: Engagement Readiness Assessment

**Readiness level:** High, with specific gates to clear.

**What makes this ready:**
- Single decision-maker with full ownership (Brad)
- Previous pilot experience with vendor engagement model
- Clear problem articulation with specific technical history
- Stated appetite for rapid prototyping and evolutionary approach
- Technology-agnostic stance (no religion about AI vs. non-AI)
- Follow-up meeting already planned with broader team

**Gates to clear:**
1. Demonstrate problem understanding ("repeat back") before proposing solutions
2. Recover the "high value targets" answer from the cut-off transcript
3. Connect Colin with Daniel for technical depth
4. Understand budget and timeline in the follow-up meeting
5. Propose an engagement model that is NOT the pod model -- structured, with Brad's team owning requirements

**Recommended BayOne approach for follow-up:**
- Lead with a problem decomposition document (the "repeat back")
- Present approaches with trade-offs for both business cases separately
- Propose small, time-boxed proof work on the highest-value target (once identified)
- Position the unified control plane / ingestion-first philosophy as a strategic differentiator
- Do NOT lead with technology or product pitches
