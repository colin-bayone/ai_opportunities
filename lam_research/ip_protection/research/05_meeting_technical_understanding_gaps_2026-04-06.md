# 05 - Meeting: Technical Understanding Gaps (Internal Assessment)

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** Internal assessment of technical understanding levels and credibility

**WARNING: Internal only. Candid assessments. Do not share with Lam Research.**

---

## Daniel Harrison (Lam) -- The "Technical Counterpart" Who Was Not Technical

### Role vs. Contribution

Daniel was brought into this meeting as the engineering counterpart to Mikhail's product function. Brad described the purpose of Daniel's presence as providing "the technical side" that the first meeting lacked. Daniel's actual contribution was to derail and confuse the discussion with a fixation on disconnected, air-gapped, and Small Language Model (SLM) topics that had no relevance to the conversation at hand.

His self-introduction set the tone: "I'm more on the information gathering side today as opposed to being in contribution, just unless I see anything egregious." That was the most accurate thing he said all meeting. He contributed almost nothing of technical value.

### The Edge AI Fixation

Daniel's first substantive interjection came before Colin had even finished the problem restatement slide. The conversation was about proving the core use case -- detection and redaction of sensitive information in enterprise text fields, hosted on Azure. Daniel immediately pushed it sideways:

> "Are we only focused on the enterprise implementation or are we considering offline or small language models?"

Brad had to redirect: "We're going to prove the use case first." Daniel did not accept this:

> "If we're not bringing it up as, hey, this is where we see ourselves five, 10 years from now..."

He then followed up with a stream of disconnected assertions about SLMs, model parity, and air-gapped environments:

> "The thing that I'm trying to piece together is that when we talk about large language model to small language model parity or collaboration and what parameters exist within each of them, if we have the ability of saying, hey, the LLM that we're potentially using to support this business case enables this other possibility..."

This is not a coherent technical statement. "Parameters exist within each of them" is vague to the point of meaninglessness. "LLM to SLM parity or collaboration" is a phrase that sounds technical but describes nothing specific. He was word-assembling, not reasoning.

Colin had to directly correct him: "Only thing I'm going to add is you're already saying LLM is a solution. Machine learning is still on the table. We don't have to use LLM." This was a polite way of saying: you are jumping to implementation choices before we have even defined whether this is an ML, NLP, rule-based, or LLM problem.

### The Fundamental Misunderstanding

Daniel does not understand the difference between model architecture and deployment topology. His mental model conflates:
- **Where a model runs** (cloud, on-prem, air-gapped edge device)
- **What kind of model it is** (LLM, SLM, NLP model, rule-based system)
- **How a model is trained** (fine-tuning, pre-training, custom training)

He treated these as interchangeable, as if choosing to deploy on an air-gapped device automatically meant you needed an SLM, and choosing an enterprise cloud deployment automatically meant LLM. This is not how any of this works. You can run an LLM on-prem. You can run a rule-based system in the cloud. The deployment target does not determine the model architecture.

When Colin explained the three deployment scenarios (air-gapped, true on-prem server, cloud hyperscaler), Daniel responded:

> "I have a different definition for that when I think about our customer fabs and Edge AI and small language models. So that's what I think of as on-premises."

Mikhail had to clean this up for him: "That is not on-prem versus Azure. That's to me disconnected environment, right? That's fab-specific deployments." Even Mikhail, who is not an AI practitioner, understood the distinction that Daniel did not.

### The Clean Room Tangent

Later, Daniel attempted to connect the IP protection problem to customer clean room environments and data extraction:

> "Getting data out and then loading it into a large language model is still possible. I think the small language model would come in if you prove to the customer that you don't have the recipe, their yield data, very sensitive IP stuff that's been cleansed, that you're just taking the tool data that can be shared."

Mikhail again had to redirect: "You're talking about structured data because rest of the data today could be easily segregated out of the data you don't need machine learning. This is for unstructured data."

Daniel was conflating the general data security problem in semiconductor fabs (structured tool data, yield data) with the specific NER/redaction problem for unstructured text in the Escalation Solver application. These are completely different problems with completely different solutions. The fact that Mikhail -- the product manager, not the engineering lead -- had to correct the engineering lead on the scope of the technical problem says everything about where Daniel's understanding actually sits.

### The AI Foundry Comment

Daniel's one attempt at specific technical knowledge:

> "I know that AI Foundry has compatibility with Edge AI and these small language models."

This is a generic statement that could be assembled from reading a Microsoft marketing page. It contributed nothing to the discussion. AI Foundry is a deployment and orchestration platform; saying it "has compatibility" with SLMs is like saying "Azure has compatibility with running code." It is true, it is obvious, and it demonstrates no deeper understanding.

### Assessment

Daniel is a 30-year software engineering veteran who has no AI/ML literacy. His contributions were uniformly disruptive -- he introduced topics that were out of scope, used terminology he did not understand, and had to be corrected by both Colin and Mikhail on basic distinctions. Pat's pre-call assessment ("I don't have a lot of high hopes for Daniel's AI knowledge") was generous.

**Communication implication:** Do not direct technical AI content at Daniel. He will not evaluate it accurately, and he may derail discussions by mapping everything back to the clean room / air-gapped / SLM framework that he is comfortable with but that does not apply to the POC. Route technical content through Mikhail instead. Daniel's value is in the software engineering infrastructure layer -- deployment environments, Kubernetes, data pipelines -- not in model selection or ML methodology.

---

## Pratik / Pat (BayOne) -- The Boundary of the Relationship Manager Role

### Where He Added Value

Pat performed his in-room proxy role well. He re-asked questions when the Lam side went vague, pushed for confirmation on the POC target, and maintained flow when Colin was constrained by the remote format. These are his strengths: room management, relationship continuity, and ensuring Colin's questions do not get dropped.

He also correctly pushed for specificity on the POC application choice: "Was there a particular criteria and process you followed on shortlisting? Was it accuracy, safety?" This is good sales hygiene -- get the client to articulate their own decision criteria so you can map your proposal to it.

### Where He Overstepped

Pat repeatedly ventured into technical territory where he lacked understanding, and Colin had to work around or implicitly disagree with what he said.

**Benchmarking assertion:** When discussing the 18-month-old prior work, Pat injected:

> "The assumption is also the performance that you're referring to, based on what you were benchmarking in the, at least in this space, AI space overall, and Colin would talk about more of the benchmarking changes every day. So yesterday's benchmarking is not included."

This is word salad. "Yesterday's benchmarking is not included" is not a meaningful statement. "Benchmarking changes every day" is an oversimplification that misrepresents how model evaluation works. Benchmarks do not change daily. Model releases happen on a periodic cadence, and benchmark methodology is relatively stable. Pat was trying to frame the 18-month gap as making the prior work obsolete, which has a kernel of truth, but his articulation of why was technically incoherent.

Mikhail politely corrected the framing: "It wasn't really a benchmarking that we're looking for. It's setting up a baseline, more than anything." Mikhail understood the distinction between benchmarking (comparing models against each other on standardized tasks) and baseline establishment (understanding where your own system performs) better than Pat did.

**Training approaches word dump:** Pat attempted to explain training concepts:

> "The trainings have improved in the last few years. They are now, earlier it used to be just training of data, labeling and all. Now they're calling it pre-training, post-training. So for example, this thumbs up and down, which is already there that you mentioned in your UI, it's kind of an aspect of the post-training where you can improve on it."

This conflates multiple concepts incorrectly. "Pre-training" refers to the initial large-scale training of a foundation model on massive corpora. "Post-training" encompasses RLHF (Reinforcement Learning from Human Feedback), instruction tuning, and alignment work done after pre-training. A thumbs-up/thumbs-down UI for reviewing individual detections is not "post-training" in any meaningful sense. It is user feedback collection that could feed into fine-tuning, retraining, or simply quality monitoring -- none of which are "post-training" as the term is used in the field.

This is dangerous because it makes a simple concept (user feedback loop) sound more sophisticated than it is, and it simultaneously misuses technical terminology in front of a client who is trying to learn this vocabulary. If Mikhail or Daniel later repeats "post-training" in the wrong context because Pat taught them the wrong definition, that creates confusion downstream.

**The "tool" Colin already has assertion:** Pat multiple times tried to boost credibility by referencing Colin's prior work:

> "We have done it internally for V1 itself. We have our own tool. Colin has already well done a lot of interface. So I want to make sure there is synergy there as well."

This is vague enough to be harmless, but it is also vague enough to be unhelpful. "V1 itself," "our own tool," "a lot of interface" -- none of these phrases communicate anything specific. They are credibility filler, not information.

**The semiconductor rarity claim:** Pat's assertion about the uniqueness of the problem:

> "This use case, the similarity of what you're in within the semiconductor domain. I can name, there would be less than 50 enterprise-level organizations who would need this problem statement."

NER and sensitive data detection are not semiconductor-specific problems. They are horizontal concerns that apply to healthcare, finance, legal, defense, and every regulated industry. The specific patterns to detect are domain-specific (fab IDs, customer tool names), but the problem class is universal. Framing this as rare makes Lam feel special, which is good salesmanship, but it is technically misleading and could come back to bite if Lam discovers that every large enterprise has the same problem.

### Assessment

Pat is valuable as a relationship manager and in-room coordinator. When he stays in that lane, he is effective. The problem surfaces when he fills silence with technical-sounding statements that are imprecise or wrong. Colin cannot correct Pat in front of the client without undermining the team's credibility, so he has to absorb the cost of Pat's misstatements and work around them. This was visible multiple times in this meeting.

**Communication implication:** In future meetings, Pat should be briefed to avoid technical assertions about model training, benchmarking, or architecture. His value is in redirecting vague answers, managing room dynamics, and reinforcing Colin's questions -- not in explaining AI concepts. If a technical question comes up that Colin has not addressed, Pat's response should be "Colin, do you want to take that?" not an attempt at a technical answer.

---

## Mikhail Krivenko (Lam) -- The Turning Point

### What Changed from the First Meeting

In the first meeting (Set 02), Mikhail provided a high-level overview of the problem but stayed generic. The internal debrief (Set 02a) characterized him as "not technical." That assessment was wrong, or at least incomplete.

In this meeting, Mikhail demonstrated something more important than technical depth: genuine intellectual honesty about what went wrong. This is rare in enterprise settings where people who led failed initiatives typically defend their decisions or blame external factors.

### The "Accidental Hodgepodge" Moment

This was the single most revealing moment of the meeting. After Colin laid out the layered architecture approach (deterministic layer, then ML/NLP, then GenAI as the final gate), Mikhail immediately mapped it to what they had done:

> "So we just literally picked like a hodgepodge of stuff and then stuck a regex on top of that as well."

Colin confirmed: "It's everyone does it." But Mikhail pressed further:

> "So we just basically accidentally picked literally every single thing, one of each."

This was not performance. This was not someone nodding along to be polite. Mikhail heard the explanation of why a structured, linear, gate-based approach matters, and he immediately understood that their approach -- running three models in parallel with a reconciliation algorithm -- was architecturally unsound. He did not defend it. He did not qualify it. He named it: "accidental hodgepodge."

Then he explicitly separated himself from the decision: "I wasn't the one picking it. I'm coming in from the business side of things. I'm just confirming what I just heard like Colin talked about and I like picked up on some of the acronyms."

This is a person who understands he is not an ML expert, is not pretending to be one, and is actively trying to learn the right framing so he can make better decisions going forward.

### The Labeling Discussion -- Substantive Engagement

When Colin explained the golden set concept, Mikhail provided the most specific and useful data of the entire meeting:

> "So we didn't have a golden set because we were told, or at least I was told, that we have to do the labeling to create that set."

This is an honest admission that they were told labeling was necessary, took that at face value, estimated 1,000+ hours, and stopped. He is not defending the decision. He is reporting what happened.

He then described what they actually did instead -- loading customer lists, acronym exclusion lists, and fab location lists as proxies for proper labeled data. This is exactly the kind of pragmatic workaround that a product manager would drive: we cannot afford the ideal approach, so here is what we can afford. The fact that it did not work is not surprising, but the fact that Mikhail understands why it did not work now (after Colin's explanation) is significant.

### The Three-Tier Labeling Follow-Up

When Colin presented the three tiers of labeling (word-level, word-plus-document-context, word-plus-document-plus-human-rationale), Mikhail immediately identified where they stood:

> "We don't have tier 3. We'd be definitely tier 1 first."

And when Brad asked about the statistical sample size needed, Mikhail returned to practical ground:

> "We actually still do have already a UI which actually gives you a thumbs up, thumbs down if the system is doing it properly or not. So the extension of is it true or not, it's already built in. How much of that data do we have to go through?"

This is the right question. Not "what is the theory," but "we have this infrastructure already, how do we leverage it toward what you are describing."

### The Rule-Based Combination Flagging

Brad suggested that a combination of elements (customer name plus fab ID appearing together) should trigger flags. Mikhail built on this with practical intuition:

> "If you have like customer name on itself it's not such a bad thing if there's nothing else with it. If you have fab ID it's probably fine. Once you start to stick things together is where you start to get into the issue."

Then he proposed the specific approach:

> "Having some type of rule around, hey, if any of these show up in any combination of two or three or something like that, you gotta flag it."

This is not an ML concept. This is someone with product and business domain knowledge proposing exactly the kind of deterministic-layer logic that Colin's architecture starts with. Mikhail independently arrived at the first layer of Colin's proposed approach through business intuition alone. That is a strong signal.

### Assessment

Mikhail's credibility went up substantially in this meeting. He is not an AI practitioner and does not pretend to be one. What he is: the person who lived through the failed attempt, understands what went wrong at a conceptual level now that it has been explained properly, and has the practical domain knowledge to validate whether a proposed approach makes sense for Lam's actual data and workflows.

He is also the person who will champion BayOne's approach internally. When he says "we accidentally picked a hodgepodge," he is giving himself and his team permission to try a different approach. That is organizational buy-in that no slide deck can create.

**Communication implication:** Mikhail is the primary technical audience. Not because he is the most technical, but because he is the most honest about what he does and does not understand, and he has the organizational position to translate technical recommendations into business decisions. Technical explanations should be framed at a conceptual level with practical anchoring to Lam's specific data -- he responds to that. Avoid jargon-heavy framing; he picks up on acronyms and maps them correctly, but he does it through pattern recognition, not prior expertise.

---

## Brad (Lam) -- Unexpectedly Strong Intuition

### The "Layers of an Onion" Origin

Brad used this phrase first. Not Colin. When the discussion was moving toward what approach to take, Brad's framing set the direction:

Colin adopted it explicitly: "This goes back to what Brad was saying earlier and where I kept saying like layers of an onion."

This matters because it means Brad arrived at the meeting with an intuitive sense that the solution is not monolithic -- that there are graduated stages of filtering, each with different cost and complexity profiles. He did not have the technical vocabulary, but the architectural intuition was already there.

### Asking for Technical Depth on the Golden Set

The most unexpected moment from Brad was when Colin explained the known-good / known-bad concept. Brad did not accept the high-level version. He pushed:

> "I do want a little bit more technical answers. I'm actually more specifically about this good bad, right? We use the five fields, right, to see if this fab ID and the customer name is present."

Then he asked the specific question that led to Colin's strongest explanation:

> "When you say known good or known bad, what are you talking about? Because data and information come in all different types of forms. Could you give me some context in what would be a good known good, and a good known bad type of content?"

This is a senior business leader asking for specifics, not accepting hand-waving, and framing the question in terms of his own domain (the five fields, the fab ID, the customer name). He is not asking a theoretical question. He is asking: show me what this looks like with our data.

This also suggests Brad has been burned by consultants who speak in generalities. He knows the difference between a confident-sounding explanation and one that maps to his actual problem.

### Scope Management

Brad was decisive on the air-gapped / edge question that Daniel kept pushing:

> "Focus on the cloud for the primary use case, but discussions in future thinking about how to achieve parity between those air-gapped files as well."

One sentence. Clear scope boundary. Future compatibility noted. Move on. This is effective executive direction, and it was delivered in the context of Daniel's extended tangent having consumed meeting time unnecessarily.

Brad also caught that Colin's slides were not in the pre-shared materials: "Colin, what you're going through here, we don't have, right?" This is someone who prepared for the meeting and noticed the gap. Minor, but it signals attentiveness.

### The Customer Name Redaction Request

Brad asked BayOne to remove customer names from all shared documents:

> "Remove the customer names, just multiple customers. They'll call out those specifically. And if these documents go broader, which they probably will at some point, we want to redact any specific customer names out of it."

Colin's response: "Easy first redaction project for us."

This was a good moment. Brad is signaling that document governance matters to him personally, and Colin's light response acknowledged the irony (we are being asked to do IP protection, and the first ask is to redact our own documents) while also showing it is trivial for BayOne to do.

### Assessment

Brad is smarter than his title suggests. His contributions were precise, his questions showed genuine engagement, and his scope management was effective. He is not technical in the ML/AI sense, but his intuition about layered complexity, his demand for concrete examples, and his decisive scoping all indicate someone who will evaluate BayOne's proposal on substance, not on slides.

The Set 02a debrief framed Brad primarily as the economic buyer. That is true, but this meeting revealed he is also an engaged evaluator who will push back on vagueness. The proposal needs to be specific and grounded in Lam's actual data, not generic consulting language.

**Communication implication:** Brad respects specificity and distrusts generalities. Every claim in the proposal should be anchored to something from his actual environment -- the Escalation Solver, the five fields, the 21% false positive rate, the 1,000-hour labeling estimate. When Brad asks a question, answer it concretely with an example from his domain, not with an analogy. The giraffe/car analogy worked for the golden set explanation, but Brad's follow-up showed he wanted it mapped back to his specific fields immediately after.

---

## Colin (BayOne) -- Where Credibility Was Built

### The Golden Set Explanation -- Strongest Moment

Colin's explanation of the golden set, ground truth, and labeling tiers was the high point of the meeting. It landed for three reasons:

1. **He directly addressed the 1,000-hour labeling fear.** Mikhail said they were told labeling would take over 1,000 man-hours and that was cost-prohibitive. Colin reframed labeling as bucketing, not pixel-level tagging: "Labeling doesn't always have to mean what we were talking about for computer vision, which is image, tag, human being has to sit there and waste their time. For the most part, we're talking about bucketing."

2. **He gave Brad the concrete depth Brad asked for.** The three tiers (word only, word plus document context, word plus document plus human rationale) were structured, specific, and immediately applicable. Mikhail could place himself on the scale ("We'd be definitely tier 1 first"). Brad could see the effort gradient.

3. **He set a ceiling that explained the failure.** "The output limit of your model is limited to the accuracy of whatever you gave it, and if that's a small set, or if it's not labeled, you're proportionally limited as to what the accuracy of that system can be." This is a clean technical explanation for why the prior attempt hit 21% false positives -- not because the models were bad, but because the input data was insufficient. It gave Mikhail an explanation that was not a criticism of his team.

### The Layered Architecture -- Compressed by Time But Effective

Colin did not get to present the full architecture in detail due to Brad's 2:30 hard stop. But what he did present landed. The key structural insight -- that the prior approach ran models in parallel and voted, whereas the correct approach is a linear pipeline where each layer narrows the problem -- was clearly communicated. Mikhail's "accidental hodgepodge" reaction confirmed it landed.

Colin also connected the approach to his own production system: "For myself, at Coherent, this was something that 40,000 people are using every day. And that's something that also got deployed to aerospace and defense." This is not a slide claim. This is a specific reference to a working system at scale in a similar regulated environment.

### Handling Daniel's Tangents

Colin managed Daniel's edge AI fixation without alienating him and without conceding scope. His response pattern was consistent:
- Acknowledge the concern ("Sure, I can talk to that")
- Redirect to the current scope ("I'll get to that, it's about slide six")
- Provide a brief, definitive technical answer ("There's no actual reason to use small language models unless you're doing on-prem")
- Close the loop ("So what I would say is for the POC's sake, tell me what you want me to shoot for")

He did not get drawn into debating SLM architecture or air-gapped deployment models. He answered Daniel's concern with a framework (three deployment scenarios), got Brad to make the scoping call, and moved on.

### The One Correction That Mattered

When Daniel said "you're already saying LLM is a solution," Colin corrected immediately and cleanly:

> "Only thing I'm going to add is you're already saying LLM is a solution. Machine learning is still on the table. We don't have to use LLM. Totally just right. So this is my product. We haven't really zeroed in. Is it LLM? Is it only machine learning? Is it even just rule-based stuff, right? Maybe we don't even go either of those routes. All of that is on the table."

This was important because it positioned Colin as the person who is not selling a particular technology -- he is diagnosing the problem and selecting the right tool. In a room where Daniel was fixating on SLMs and Pat was throwing around benchmarking language, Colin's insistence on starting from the problem, not the solution, was a credibility marker.

### What Was Lost to Time Pressure

The Azure section of Colin's presentation was not shown in detail. The full architecture slide got compressed. The exploratory data analysis (EDA) commitment -- that BayOne would analyze the data first to determine sample size needs rather than guessing -- was mentioned but not elaborated.

These are not critical losses for this meeting, but the proposal needs to cover them. The Lam side left without seeing the full technical picture, which means the proposal is doing double duty: it is both a commercial document and the technical depth that the meeting did not have time to deliver.

### Assessment

Colin gained credibility with Mikhail and Brad in this meeting. His explanations were concrete, his corrections were respectful, and his technical framing gave Lam a vocabulary for understanding what went wrong that does not blame anyone. The golden set explanation is the moment they will remember.

**Communication implication:** The proposal should lead with the approach and methodology that Colin presented, anchored to the specific Lam data points (Escalation Solver, five text fields, 21% false positive rate, existing thumbs-up/thumbs-down UI). Colin's credibility is built on specificity and production experience, not on slides. Keep that pattern.

---

## Amit (BayOne) -- Generic Contributions

### What He Said

Amit's primary contributions were around benchmarking context and training approaches. He provided background framing for why the 18-month gap matters and tried to contextualize the prior work within the broader AI landscape.

His most specific contribution was the compliment framing:

> "I just want to also compliment I think the team and Brad overall like you already 18 months ago tried it out so you really compared to some all the other organization that is scaled to have not been even still figuring out."

This is relationship management, not technical contribution. It is fine in the moment but does not advance the technical discussion.

### The "Post-Training" Comment

As noted in Pat's section, Amit's adjacent comment about pre-training and post-training was technically imprecise. He also added:

> "It's not as heavy as you may think of making that data, like what we are good at. Only thing is the definition itself."

This is a correct high-level point (the labeling burden is not as heavy as Lam fears), but Amit did not provide the specifics to back it up. Colin did that later with the three-tier labeling framework.

### The Semiconductor Rarity Argument

Amit echoed Pat's framing about the semiconductor space being unique:

> "The reason for that is this use case, the similarity of what you're in within the semiconductor domain. I can name, there would be less than 50 enterprise-level organizations who would need this problem statement."

As noted earlier, this is salesmanship, not technical analysis. NER for sensitive data is a universal enterprise problem. The semiconductor framing makes Lam feel their problem is special, which helps emotionally but is not technically accurate.

### Assessment

Amit's contributions were supportive but not substantive. He reinforced points that Colin made more precisely, and he added relationship-management commentary that kept the tone positive. His role in the room was not to be the technical expert, so the generic nature of his contributions is not a failure -- it is just a reflection of his function.

**Communication implication:** Amit's value in future meetings is as the delivery assurance presence -- the person who signals that BayOne has the operational capacity to execute. He should not be the person explaining training methodology or model architecture. Let him handle execution timeline, resource commitment, and operational logistics.

---

## Summary: Credibility Ledger

| Person | Credibility Direction | Key Reason |
|--------|----------------------|------------|
| **Daniel Harrison** | Down significantly | Every technical contribution was either incorrect, out of scope, or had to be corrected by someone else in the room. Did not fulfill the "technical counterpart" role. |
| **Pat (Pratik)** | Stable with caveats | Performed the proxy/wingman role well. Overstepped on technical topics with imprecise or wrong assertions that Colin had to absorb without correcting. |
| **Mikhail Krivenko** | Up significantly | Demonstrated intellectual honesty, practical domain knowledge, and the ability to absorb new technical framing and immediately apply it to his own context. The "accidental hodgepodge" moment was genuine understanding. |
| **Brad** | Up moderately | Showed better technical intuition than expected. Asked for specific depth. Made decisive scoping calls. Will evaluate the proposal on substance. |
| **Colin** | Up with Mikhail and Brad | Golden set explanation was the credibility anchor. Layered architecture framing converted Mikhail. Handled Daniel's tangents without friction. |
| **Amit** | Neutral | Supportive but generic. No technical errors, but no technical depth either. |

---

## Forward Communication Strategy

| Stakeholder | How to Communicate |
|-------------|-------------------|
| **Mikhail** | Primary technical audience. Use conceptual framing with concrete Lam examples. He learns by mapping new information to what he already knows. Give him the vocabulary to champion the approach internally. |
| **Brad** | Every claim needs an anchor to his data. Do not hand-wave. He will ask follow-up questions, and he will notice if the answer is generic. Lead with the specific numbers from his environment. |
| **Daniel** | Do not engage on SLM / air-gapped / edge topics unless specifically scoped. If he raises it, acknowledge and redirect to Brad for scoping decisions. His technical questions on AI topics will consume time without advancing the engagement. Engage him on software infrastructure, deployment environments, and Kubernetes -- that is where his 30 years of experience actually applies. |
| **Pat** | Brief him before meetings to stay in the relationship/room-management lane. Give him specific talking points he can repeat accurately rather than letting him improvise on technical topics. |
| **Amit** | Execution assurance. Timeline, resources, operational capacity. Keep him in that frame. |
