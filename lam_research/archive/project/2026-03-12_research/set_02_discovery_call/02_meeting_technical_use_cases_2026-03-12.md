# 02 - Meeting: Technical Use Cases (Deep Dive)

**Source:** `source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on use cases

---

## 1. Framing: The Troubleshooting Workflow as Foundation

Mikhail explicitly frames the entire discussion around a troubleshooting workflow, which he draws on the whiteboard. The workflow has three stages:

1. **Self-help** -- user searches knowledge bases and AI tools to find answers independently
2. **Ask for help** -- user reaches out to a specific community or experts
3. **Escalate** -- structured troubleshooting with more experts involved

This workflow is the scaffolding for the two use cases. Mikhail: "I'm using the troubleshooting as the workflow is self-help, where you use the search tools or you use the AI tools to search for things, right? To see if you can seek the answers, if not, you go into export help, and then you go and what we call escalate, or it's more of a structured troubleshooting, more experts are being involved."

The business goal spanning both use cases: "overall, what we're trying to achieve, we're trying to achieve productivity, right? We're trying to make sure we can bubble up as much information as possible without violating customer IP, without violating our IP as well, so that people can solve problems."

Brad adds the cost and customer dimension: "This is very very costly. You're right when you're in this phase. Also, it's effects customer trust, other things. So the goal is to drive this down and drive this up."

The desired trajectory is to strengthen self-help (drive usage up) so that ask-for-help/escalate (expensive, slow) gets driven down. The feedback loop is critical: once problems are solved through escalation, those solutions should feed back into the self-help knowledge base. But this feedback loop is blocked precisely because the escalation data contains unstructured, potentially IP-violating content that cannot safely be fed into the general population search.

---

## 2. The Over-Restriction Problem

This is the foundational context for both use cases. Brad introduces it directly: "our current mode of operation is we over restrict."

Mikhail elaborates: "what we're doing, we're putting policies in place, which basically creates hard barriers. Because we're saying, OK, we don't know if this document contains IP. We're just going to, by default, assume that it does. We don't want to risk it, right? So it's more that's where over restriction starts coming in."

Brad acknowledges the trade-off explicitly: "Which is not a bad thing in the larger scheme of things, especially with the IP lens effect, right? Because it could lead to a lot more loss or other trade." But then: "True, but we're also knowing that we're limiting the productivity, the capability, because we don't share that much."

### Concrete example of over-restriction killing productivity

Mikhail provides a concrete scenario: "if document three has the path to solution, but you only can look at Intel documents and this sits in a Samsung space, you're not going to see that."

This means: a field engineer working on an Intel problem cannot see a solution that was documented in a Samsung context, even though the solution itself may be entirely generic and non-IP-bearing. The customer segmentation walls block cross-pollination of troubleshooting knowledge.

### Over-restriction also limits AI training

Mikhail: "this also limits to what data we can train our AI agents on, right? Or our AI mobs, not agents, but our models on because, hey, if this source is restricted and we cannot control whether this data could be trained for general public, we're not going to pass the source to the model to train them because we don't want to assume that additional risk."

So the over-restriction has a compounding effect: it blocks human search AND it blocks the ability to train AI models that could further improve productivity.

### Over-restriction as silo creation

Brad describes how the response to uncertainty creates further fragmentation: "sometimes we'll say, okay, this type of information lives in this, and we'll just take a little search on it. But the thing is, is now you have a seven or an eight. You're at nine, so you're just creating silos of what you think is the right information to serve through that. And then again, it's another form of restricting."

They have **six different search tools** (Mikhail: "we don't have a single search for it. We have six search formulas"), and the over-restriction philosophy has led to fragmentation where different knowledge pools are siloed across different systems.

---

## 3. Use Case 1: Self-Help Search

### What it is

The first use case concerns the search phase of troubleshooting. When a user searches for solutions across knowledge bases, customer-confidential information (CI documents, proprietary procedures, etc.) may exist in the results. The challenge: surface relevant results without exposing customer IP across customer boundaries.

Mikhail frames it: "How do we, in the search area, are able to produce meaningful results, removing customer confidential information?"

### The data landscape

- **Mostly unstructured data.** Mikhail: "Majority of the data that we're concerned with today for this discussion is unstructured data. So it lives inside documents. It could live inside the meeting transcripts. It could live in the procedures or a problem test."
- **Some metadata exists** in certain areas to identify customers or flag content, but coverage is not 100%. Mikhail: "we do have in some areas metadata to identify the customer or to identify something. It's not 100%."
- **No single data lake.** Multiple databases and search systems, each with different segmentation. Mikhail: "because we have many search tools and ways of getting information, some of the databases or some of the stuff is segmented and different. So there is not one, you could say data lake or something like that."

### What "sensitive" means in this context

Sensitive information in the search use case is primarily **customer-identifiable information** -- data that would reveal which customer (Intel, Samsung, Micron, etc.) a particular problem, solution, or procedure relates to. This includes:

- **Customer names** (direct mentions)
- **Fab identifiers** (e.g., "Fab 11", "F11", "Fab-11", "Fab space 11" -- Mikhail notes the many variant spellings)
- **File names** that contain customer identifiers
- **Site-specific details** that could be traced back to a customer
- **Customer-proprietary process information** embedded in troubleshooting documents

Brad specifies the initial target fields: "the reason is we want to promote those couple of fields, right? Let's say customer name, file name. Sometimes those are just enough."

But Mikhail insists on discussing it conceptually rather than field-by-field: "that's why I want to talk conceptually, rather than specific systems, because we have, in some areas we have a single source, in some areas we have many, many different systems."

### The customer trust dimension

Samsung (and other customers) trust Lam that their data is not cross-shared. Mikhail: "what we say in Samsung, which really means in-lab employees, but that still, Samsung trusts us that it's not cross-shared, right? Because there could be like, oh, Samsung solved that problem, but that could be very proprietary."

### Current access model in search

Today, customer segmentation is enforced at the system level. Mikhail gives the ticketing example: "If a person at Micron is going to open a ticket, people that identify as part of being Micron will be able to see and search all those tickets. So that exists today in our tool. What doesn't exist at Samsung person opens a ticket... nobody at Micron able to see that ticket."

The aspiration: if you could reliably strip customer-identifiable information from solutions, those solutions could be made available to the general population, massively expanding the searchable knowledge base.

### Relationship to the redaction approach

For Use Case 1, the technique is primarily about **redaction** -- processing stored content to remove customer-identifiable information so it can be surfaced more broadly. This is the "heavy-handed" approach that can take more time, is accuracy-focused, and where over-redacting is initially acceptable.

Mikhail explicitly ties it: "this space we're right over-redacting. So if we over-redact less, we already have success." In other words, the bar for success in the search use case is lower: if they can move from blanket restriction to targeted redaction (even if sometimes too aggressive), that's already a win because it opens up previously invisible knowledge.

### Desired end-state for Use Case 1

The goal is to take content that is currently fully restricted (invisible to cross-customer searches) and make it available to the general population by stripping customer-identifying information. The end-state vision:

- Documents that contain solutions are processed to remove customer identifiers
- The cleaned content becomes searchable across customer boundaries
- Engineers working on Intel problems can find solutions that originated in Samsung contexts (and vice versa), but without ever knowing which customer the solution came from
- AI models can be trained on this cleaned data, further improving self-help capabilities
- The feedback loop from escalation back into self-help becomes functional

---

## 4. Use Case 2: Ask for Help / Escalation

### What it is

The second use case concerns the entry points where users create tickets, ask questions, and interact with experts. When someone asks for help, the way they describe their problem can itself expose customer IP. Additionally, once data enters the escalation flow, it accumulates unstructured content (answers, transcripts, attachments) that may contain IP.

Mikhail: "the way you ask a question could present an IP risk if an Intel person asks the question in a way that exposes Intel's IP and a Samsung person [can see it]."

### The real-world violation rate

Brad provides a striking data point about how common policy violations are: "when we started this project, I'm like, how many tickets is gonna take me to find policy violation? Seven. Seven's ticket, there was already concept-renade [a confidential violation]."

This underscores the human factor: people violate IP policies not out of malice but out of convenience. Mikhail: "We're trying to protect against the human factor."

### Concrete example of the problem

Mikhail gives a specific scenario: "if a person at Micron is going to open a ticket... they could say, hey, I'm on my phone, Fab11, and I have this issue with this tool, and we don't want them to say micrograph-11. We just want to know what you're talking about."

The desired behavior: "If I say, hey, I have an issue with the Sun's eye tool, generic enough." They want people to describe problems generically -- tool type, symptom, behavior -- without customer-specific identifiers.

### Two sub-approaches within Use Case 2

Mikhail explicitly separates Use Case 2 into two distinct technical challenges:

#### Sub-approach A: Detection at Entry (Real-Time)

**Purpose:** Notify the user in real-time that they may be violating customer confidentiality policy as they enter information.

**Key characteristics:**
- **Not blocking, just notifying.** Mikhail: "let's start not enforcing the policy, but let's notify you to potentially could be violating. Still leave it up to the users to say, yes, I am. No, I'm not."
- Brad: "Because we're never going to get it accurate enough, or we can 100% block it from entry."
- **Real-time performance requirement.** Mikhail: "this has to run within UI, whatever is UI standards, two to five seconds max."
- **Extremely sensitive to false positives.** Mikhail: "we're much more sensitive in this space to false positives rather than over-redacting... Because this is real time. These are notifications that go to the users."
- **False positive tolerance: below 1% end state.** Mikhail: "we needed this number to be way below 1% end state."
- **The 20% false positive problem.** Their tested models produced roughly 20% false positive rate per ticket, which is "absolutely unacceptable." Mikhail: "If every fifth thing I say, hey, you possibly have a violation, then you're like, no, I don't. People are just not going to trust it. And if you constantly give auditors notifications, say, a possible violation, they're also going to not trust your system. They're going to turn off these notifications."
- **"Big brother approach."** Mikhail uses this phrase: "it's more about the big brother approach. How fast you can get to detect and notify the user that they would have possible violation of customer confidential information."
- **Detection only -- no redaction at this stage.** Mikhail: "In this case, we're not doing redaction. We're just doing detection and we're stopping there. We're letting users know that they might have issues and that we stop with the detection."

#### Sub-approach B: Batch Redaction After Entry

**Purpose:** Once data has entered the system (problem statements, answers, transcripts, attachments), perform heavier analysis to detect and redact customer-identifiable information so the data can be fed back into the general knowledge base.

**Key characteristics:**
- **Not performance-sensitive.** Mikhail: "this could run an hour" (contrasted with the 2-5 second real-time requirement).
- **Accuracy-focused over speed.** Mikhail: "one is not performance focused. One is more accuracy focused."
- **Over-redacting is acceptable initially.** Success is defined as reducing blanket restriction to targeted (even aggressive) redaction.
- **Multiple modalities.** Brad raises the complexity: "in some cases, if it's inside a picture or like the OCR picture, you're still going to just retrieve the document rather than..." This implies the batch redaction needs to handle text, images (OCR), potentially transcripts, and attachments.
- **Detection plus action.** Mikhail: "it's still a detection, but a different type of detection and what you do with that." The batch process detects sensitive content and then takes action (redact, restrict, flag).
- **Fallback to restriction.** Mikhail: "in some instances, either say, I can't redact and I'm going to redact, or no, I can't redact even though I detect this. So you're still going to restrict the document." If redaction isn't possible (e.g., IP embedded in an image), the document stays restricted rather than being released with IP intact.
- **Enables the feedback loop.** The ultimate purpose is to clean escalation data so it can be fed back into self-help: "once we're able to build that confidence, then we can open these tickets up to general population, where today we're very segmented."

### Mikhail's explicit framing of detection vs. redaction

Mikhail draws a clear line between these two: "in both cases, in this case, in this case, it's detection. It's just one is not performance focused. One is more accuracy focused. The other one is good enough, less false positive performance focus."

He also insists these are separate swim lanes: "When we say small piece and MVP, I would expect them not being jumbled together, but they could be separate swim lanes." They can inform each other ("They can agree with each other") but should be developed and evaluated independently.

---

## 5. Performance Requirements (Consolidated)

### Detection at Entry (Real-Time)

| Requirement | Target |
|---|---|
| Response time | 2-5 seconds max (UI standards) |
| False positive rate | Well below 1% end state |
| Current false positive rate | ~20% per ticket (unacceptable) |
| Action on detection | Notify user, do not block |
| Scope | Text fields at entry points (problem statements, descriptions) |
| Mode | Real-time, per-submission |

### Batch Redaction (Post-Entry)

| Requirement | Target |
|---|---|
| Processing time | Can take up to an hour; not performance-sensitive |
| Accuracy priority | High -- accuracy over speed |
| Over-redaction tolerance | Acceptable initially; success = less restriction than blanket approach |
| Action on detection | Redact where possible; restrict document if redaction not feasible |
| Scope | All content in escalation flow (text, images/OCR, transcripts, attachments) |
| Mode | Batch processing of stored data |

---

## 6. What Has Been Tried

Mikhail provides specifics on previous technical attempts, which contextualizes both use cases.

### MLOps + Model Training

They set up MLOps on Azure cloud and tried three models:
1. **Transformers model** (unspecified which)
2. **spaCy** (NLP library, likely NER-based approach)
3. **Azure AI model** (unspecified which)

They passed training data to these models. Results: "those models were trained with global data as well, not just our data, we were hitting the rate of false positives of around 20% per ticket."

Fine-tuning improved this marginally: "the fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."

Colin's assessment of this result: "when I heard 20%... that's pretty much out-of-the-box chat GPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all." Mikhail confirms: "the fine-tuning actually went from 20% to 17% today, exactly."

### Rule-Based Models

They started exploring rule-based approaches but hit the variant spelling problem. Mikhail: "something like a fab could be spelled many different ways, right? So there were ones, they're the accuracy basically created because the data is unstructured. Some people put a micro 11, some put F11, some put PAP space 11, PAP dash 11."

The maintenance burden was also cited: "we know that we can actually put all these permutations in a rule-based models, but now we're policing this non-stop every day as new things come up."

### Labeling Exercise Assessment

They evaluated doing a full labeling exercise to create structured training data: "it was over a thousand man hours just to get the labeling up and then continuous maintenance, so that was fairly expensive activity."

They haven't ruled it out: "doesn't mean we don't want to do it, all I'm saying is with looked at the labeling activity." The framing is: if the use case proves valuable enough, "maybe a thousand hours is just peanuts compared to the productivity gains we could gain by opening this up."

### Deliberate avoidance of generative AI

Mikhail makes a notable statement about their technology choices: "one thing I don't want us to limit is to just LLMs and generative AI... we actually have not used generative AI to prove any use cases, not because of unstructured data, but because of unstructured output. If it does mean we can't, all I'm saying is we decided to go with something more definitive that can tell us redact, don't redact, rather than at a structured output that LLMs typically produce."

This reveals a philosophical preference for deterministic outputs (yes/no redaction decisions) over probabilistic generative outputs, though they acknowledge LLMs could potentially be prompted for structured output.

---

## 7. Infrastructure and Platform Context

This directly affects feasibility and approach for both use cases.

### Current state: Extreme heterogeneity

Mikhail's response to questions about the technology stack: "anything you can think of is because again, these are not free systems. Some of it on-prem, some of it is on cloud, some of it is eventually gonna move to cloud, some of it is Lam GPT so we still have open and like the GPT models within Lam, some of it is again cloud but bots. So anything you can think of most likely this is a hazard."

Critically: "These are not two, three systems. I'm not describing a single system or three systems. These are flows."

### Aspirational direction

Mikhail: "we do want to focus on cloud first going forward. So that's our plan. And again, I don't want to dive into technical, but we also want to focus on microservice architecture long term."

### Data entry mechanisms

Multiple ways data enters the system, relevant for both use cases:
- Standard procedures and documents (uploaded or stored)
- User-entered problem statements in ticketing systems
- Responses and answers from experts
- **Microsoft Teams meeting transcripts** automatically attached to tickets (Mikhail: "if they schedule out of the system, Microsoft Teams meeting transcripts, it's transcribed and it's automatically attached to the ticket")
- Images and OCR content within documents

### Search tools

Six different search tools/formulas exist. No unified search. Different tools search different knowledge pools with different access restrictions.

### Internal AI capabilities

They have "Lam GPT" -- internal deployment of GPT models. They also use Co-Pilot (which uses GPT models internally). The AI ecosystem is diverse.

---

## 8. Existing Access Controls and IAM

Relevant context for how use cases interact with identity.

### What exists today

- **Customer-based segmentation** in the ticketing system. Micron-associated users see Micron tickets; Samsung users see Samsung tickets; cross-visibility is blocked.
- **ASM (Access Security Manager or similar)** governs access to certain sensitive areas. Brad: "We do have ASM that governs access to certain things, right? So like our escalate flow area."
- Users can **manually restrict** entire tickets or specific attachments, but not individual entry fields. Brad: "a user can make a conscious decision to restrict the entire ticket and or attachments by attachments, but not by all the different entry fields."
- **Employee type restrictions:** Contractors, LSPs (Licensed Service Providers), and employees have different access levels. Trade-restricted employees and those in embargo countries have specific flags and identifiable attributes (different colored badges).
- **Role and work center attributes** exist but are not "super robust." Brad: "I wouldn't say it's super robust. I'm going to say we do have attributes around some of that stuff."

### What's in progress

- Enterprise IAM (Identity Access Management) program has been active for about two years, making progress but not yet mature. Brad: "The company's working on getting to more of an IAM identity access management. And so that's an active program that's been going on probably for about two years."

### Mikhail's boundary-setting on IAM

Mikhail deliberately separates the IAM / access-based-filtering problem from the two use cases he's presenting. When the BayOne team asks about role-based access, Mikhail redirects: "I just want to caution against that... what we're describing is actually a completely different use case that I didn't present, which is, yeah, when it's restricted, how do you solve that? I don't think we need to focus on that."

His reasoning: the redaction/detection use cases are about cleaning content so it CAN be shared broadly, not about controlling WHO sees what. The IAM problem is orthogonal. If redaction works, the content becomes safe for general consumption regardless of who's looking.

---

## 9. Relationship Between the Two Use Cases

### Shared goal

Both use cases serve the same ultimate objective: unlock productivity by enabling knowledge sharing across customer boundaries without violating IP.

### Different positions in the workflow

- Use Case 1 (Self-Help Search) operates on **stored content** -- documents, procedures, historical solutions. The redaction happens in batch on existing data.
- Use Case 2 (Ask for Help / Escalation) operates on **live content** -- data as it's being created and as it flows through the escalation process.

### The feedback loop connecting them

The critical link: Use Case 2's batch redaction is what enables Use Case 1. Once escalation data is cleaned through heavy-handed detection and redaction (Use Case 2, Sub-approach B), that cleaned data can be fed into the self-help search knowledge base (Use Case 1). Mikhail: "more heavy-handed detection and redaction so we can safely feed this into the general with the ultimate goal of dragging this down" (referring to driving down escalation volume).

Without the redaction pipeline from Use Case 2, the self-help knowledge base (Use Case 1) remains starved of cross-customer solutions, and the over-restriction problem persists.

### Mikhail's insistence on separation

Despite their connectedness, Mikhail explicitly wants them treated as separate swim lanes for MVP purposes: "When we say small piece and MVP, I would expect them not being jumbled together, but they could be separate swim lanes."

---

## 10. Technology and Approach Openness

### Not married to AI

Brad is emphatic: "I know AI is a very sexy word, but it's also a meaningless word, and not married to any specific AI technologies, LLM, machine learning, or anything like that, it doesn't have to be an AI."

He acknowledges a preference: "Preference on AI? Sure, because your kind of ceiling goes up with AI, what you can do afterwards."

### Open to any approach

Brad: "we are open to any and all approaches by also understanding what are the trade offs and what are the, you know, outcomes that we can expect with those."

### Evolutionary, not revolutionary

Brad: "we're not expecting to be revolutionary and right out of it. Evolutionary is absolutely fine."

### Incremental proof approach

Brad repeatedly emphasizes starting small and proving incrementally: "We want these things that we can chunk them down, prove these things, and then kind of determine, because not everything may work, right?"

And: "similar to what we did last year, we would try those incremental steps to see proving out that we get those things."

### Rapid prototyping preferred

Brad: "this is where I think we want to get to some rapid prototyping. I mean, we don't want these things to take months and years, right?"

---

## 11. Colin's Unified Control Plane Recommendation

Colin (BayOne) makes a significant architectural recommendation during the discussion that is worth capturing as it may shape the proposed approach.

Colin argues for a common control plane across applications: "there has to be commonality between these applications. The good thing with that is about 95% of a rack application is identical. The only thing that really changes is maybe some strategy for ingestion, maybe the end use case is a little bit different, but the actual architecture fundamentally is relatively the same."

His key point about ingestion: "The whole problem is that whenever you make information known or available to AI, that's how information comes in. That ingestion part is so critical because even if information comes out, you shouldn't have to redact anything if this part actually worked. It's not possible. It can't create that from nothing."

Colin argues the biggest bang for the buck is at the ingestion point: "making sure that entry point is very robust, that is where the biggest bang for your buck is going to be here for sure. It's easier than you would think if you can have that common control plane."

Warning about fragmentation: "The more diverse and the less governance that's over that space, the worse this gets and it gets worse over time."

Brad's response to this framing is positive: "we are open to any and all approaches."

---

## 12. Priorities Between the Two Use Cases

### Brad's stated MVP focus

Brad mentions wanting to focus on specific fields first: "we want to promote those couple of fields, right? Let's say customer name, file name. Sometimes those are just enough." This suggests the initial target is narrow: can we reliably detect/redact just customer names and file names that contain customer identifiers?

### Mikhail's framing of MVP scope

Mikhail confirms starting small: "the reason is we want to promote those couple of fields, right? Let's say customer name, file name." But he also states: "if you can't get those correct, and you can't redact or do whatever we're trying to do with those, you can't escape, right?" -- meaning if you can't solve the simple case (customer name, file name), there's no point tackling the harder cases.

### Implicit prioritization

While no explicit "do Use Case X first" statement is made, the structure of the conversation implies:
1. **Detection at entry (Use Case 2A)** is the most immediately painful because of the 20% false positive problem and the user-facing nature of the failure.
2. **Batch redaction (Use Case 2B / feeds Use Case 1)** is the higher long-term value because it unlocks the feedback loop and opens the knowledge base.
3. Both should proceed as **parallel but separate swim lanes**.

### Proving the concept on narrow fields first

The strategy appears to be: prove that customer name and file name can be reliably detected/redacted in a small scope, then expand to broader content types. Mikhail: "We want to start small and prove incrementally that we can solve certain things."

---

## 13. Specific Scenarios and Edge Cases Mentioned

### The spelling variant problem (Fab identifiers)

Mikhail provides detailed examples of how a single entity can be spelled many ways: "something like a fab could be spelled many different ways... Some people put a micro 11, some put F11, some put PAP space 11, PAP dash 11." This is a direct challenge for both rule-based detection and ML-based detection.

### Mobile entry

Mikhail mentions: "they could say, hey, I'm on my phone, Fab11, and I have this issue with this tool." This implies that entry points include mobile interfaces where users may be even more abbreviated and inconsistent in their typing.

### Teams meeting transcripts auto-attached to tickets

When an escalation meeting is scheduled through the system via Microsoft Teams, the transcript is automatically transcribed and attached to the ticket. This is a significant entry point for unstructured, potentially IP-containing content that the user has no opportunity to manually review before it enters the system.

### OCR content in images

Brad raises the case of IP embedded in images: "in some cases, if it's inside a picture or like the OCR picture, you're still going to just retrieve the document rather than..." This implies that for image-based content, redaction may not be feasible and the fallback is document-level restriction.

### The auditor fatigue problem

Mikhail describes how false positives don't just annoy users -- they also create fatigue for auditors: "if you constantly give auditors notifications, say, a possible violation, they're also going to not trust your system. They're going to turn off these notifications." This is a dual audience problem: both end users and compliance auditors are consumers of detection outputs.

### Policy violation found in 7th ticket

Brad's anecdote about finding a policy violation in the 7th ticket he checked demonstrates the prevalence of the problem and the gap between policy and practice. People routinely include customer-identifiable information in tickets.

---

## 14. What BayOne Was Asked to Do Next

Brad frames the ask: "We know it's very complex. We know there's probably not going to be a one-on-one end-all thing, but if we could, you know, understand what those approaches are, those trade-offs are, that's where we want to kind of take the next steps."

Specifically they want:
1. **Different perspectives** on approaches -- they don't want to hear "I have a technology solution that can solve that." They want trade-off analysis.
2. **Incremental proof points** -- chunk things down, prove them, determine what works.
3. **Rapid prototyping** -- not months-and-years timelines.
4. **A follow-up meeting** with broader technical team. Brad: "in the follow up, we would have others here to look at the different approaches, trade-offs, Q&A."

Mikhail adds a critical requirement for clarity: "we want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve, right? And so that's critically important."

---

## 15. Organizational Notes Relevant to Use Cases

- **Brad owns end-to-end:** product, engineering, and execution. "I own the entire thing."
- **Three functions:** Business/Program (Brad), Product (Mikhail), Technical (Daniel). They assemble scrum teams from these functions.
- **Initial focus is on systems they own.** Mikhail: "our initial focus is to prove out this case within our systems. If we can prove out success, you can start branching out to other places."
- **Not a typical engagement model.** Mikhail: "what if we decide to go there, it's not gonna be me like writing user stories requirements. I'm gonna have somebody as part of my team, you're gonna, your team is gonna be working with, it's not gonna be like did for the pod working because that was a pilot, that was the only reason. That's not a standard mode of operation."
- The follow-up meeting will include a broader set of people, including more technical stakeholders.
