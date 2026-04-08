# 02 - Meeting: Infrastructure and Access (Deep Dive)

**Source:** /lam_research/ip_protection/source/lam_discovery_call_2026-03-12.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on infrastructure, systems, and access management

---

## 1. System Landscape: Extreme Fragmentation

### The Core Statement

When Colin asked whether the infrastructure is "all on Azure," Mikhail's response was emphatic and revealing:

> "Oh my God. This is like ever like anything you can make up is because again, these are not free systems. Some of it on-prem, some of it is on cloud, some of it is eventually going to move to cloud, some of it is LamGPT so we still have OpenAI like the GPT models within Lam, some of it is again cloud but bots so anything you can think of most likely this is a hazard. Because these are not two, three systems."

This is as close to "total chaos" as a product leader will voluntarily admit in a discovery call. The key elements:

- **On-prem systems** exist and are still active
- **Cloud systems** exist separately
- **Migration in progress** -- some on-prem systems are "eventually going to move to cloud" (no timeline given)
- **LamGPT** -- an internal deployment of GPT models running within Lam's environment
- **Copilot** -- referenced separately from LamGPT, indicating Microsoft Copilot is also deployed (Colin confirmed: "in the Copilot, we're really talking OpenAI model, right? Because Copilot using GPT models")
- **Cloud-based bots** -- additional AI/automation tooling in the cloud
- These are described as "flows" not "systems" -- meaning the data moves through multiple platforms within a single workflow

### The "Flows Not Systems" Distinction

Mikhail explicitly corrected the framing away from discrete systems:

> "These are not two, three systems. I'm not describing a single system or three systems. These are flows."

This is significant. It means the fragmentation is not just about having multiple applications -- it is about data moving through heterogeneous environments within a single business process. A troubleshooting ticket might originate in one system, get transcribed in Microsoft Teams, attach to a ticket in another system, get searched via yet another tool, and feed results back through a different interface.

### Aspirational Direction

Mikhail stated a forward-looking preference:

> "We do want to focus on cloud first going forward. So that's our plan. And again, I don't want to dive into technical, but we also want to focus on microservice architecture long term."

He immediately tempered this:

> "Whether we do or not, let's say these solutions, that's a different thing, but that's our kind of aspirational goal to focus on."

**Interpretation:** Cloud-first and microservices are the stated architectural direction, but Mikhail is candid that current reality does not match this aspiration. The word "aspirational" is doing a lot of work here.

---

## 2. Search Tools and Knowledge Fragmentation

### Six Search Systems

Mikhail stated directly:

> "We don't have a single search for it. We have six search formulas."

This is why he insisted on discussing the problem "conceptually, rather than specific systems":

> "Because we have, in some areas we have a single source, in some areas we have many, many different systems."

### No Unified Data Lake

When Colin asked whether there was "one unified place" for the knowledge base layer, Mikhail's answer was unambiguous:

> "Because we have many search tools and ways of getting information, some of the databases or some of the stuff is segmented and different. So there is not one, you could say data lake or something like that."

He acknowledged this could change:

> "That doesn't mean that that's not in the future."

But immediately explained why the current state persists:

> "But as of right now, because of the over-restriction, sometimes we'll say, okay, this type of information lives in this, and we'll just take a little search on it."

### Siloing as a Consequence of Search Fragmentation

The fragmentation is self-reinforcing. As Mikhail described it, the over-restriction drives segmentation, which creates silos, which limits what data AI models can be trained on:

> "But the thing is, is now you have a seven or an eight. You're at nine, so you're just creating silos of what you think is the right information to serve through that. And then again, it's another form of restricting."

And the downstream effect on AI:

> "This also limits to what data we can train our AI agents on, right? Or our AI models, not agents, but our models on because, hey, if this source is restricted and we cannot control whether this data could be trained for general public, we're not going to pass the source to the model to train them because we don't want to assume that additional risk."

**Key insight:** The fragmentation is not just an infrastructure problem -- it is a data availability problem that directly constrains Lam's ability to build and train AI solutions. The six search systems, the lack of a data lake, and the over-restriction policies all feed into a cycle where knowledge is locked away in silos.

---

## 3. Data Ingestion Patterns

### Multiple Entry Points, No Clean Answer

When Pat asked "how do things actually get into the system," Mikhail was candid that there is no neat architecture:

> "There are so many systems because we have procedures. So keep this in mind. There's many ways... I'm not going to be able to give you a very neat answer how things get in."

### Specific Ingestion Channels Identified

Despite the caveat, several channels were described or implied:

1. **Standard procedures and documents** -- "the majority of our concerns is with our procedures and documents." These are pre-existing reference material. How they enter the system was not specified, but they are stored across the fragmented landscape.

2. **Microsoft Teams meeting transcripts** -- described in the escalation workflow: "if they schedule out of the system, Microsoft Teams meeting, it's transcribed and it's automatically attached to the ticket." This is an automatic ingestion path. Speech-to-text transcripts get attached to tickets without human review for IP content.

3. **User-entered problem statements** -- when a technician opens a ticket, they type free-text describing the problem. Mikhail gave a vivid example: "this is an unstructured data entered by people in their problem statement. They could say, hey, I'm on my phone, Fab 11, and I have this issue with this tool, and we don't want them to say [customer-specific fab name]. We just want to know what you're talking about."

4. **User-uploaded document attachments** -- users can "actually upload" documents to tickets. These can be individually restricted by the user but there is no automated screening at upload time.

5. **Responses to problem statements** -- experts answering questions also enter unstructured text, which feeds back into the knowledge base.

6. **Feedback loop from escalation back to self-help** -- once a problem is solved through escalation, the intent is to feed the solution back into the self-help search layer so future users find it without escalating. This is the ingestion pattern that is currently blocked by the IP problem: "we can't fool and build this feedback loop and take unstructured data that we know is restricted, or potentially could be restricted, and feed it into the general training area."

### The Ingestion Control Problem

Colin made a strong statement about the importance of ingestion-side controls:

> "The whole problem is that whenever you make information known or available to AI, that's how information comes in. That ingestion part is so critical because even if information comes out, you shouldn't have to redact anything if this part actually worked. It's not possible. It can't create that from nothing."

> "Making sure that entry point is very robust, that is where the biggest bang for your buck is going to be here for sure. It's easier than you would think if you can have that common control plane."

Mikhail partially agreed but noted that some ingestion controls already exist -- the problem is they are blunt:

> "Some of this is already built into our system. So that part is already there, but that's what's causing over-restriction because we only have that information, so we have to indiscriminately restrict on these things rather than saying very specific pieces of information."

---

## 4. Unstructured Data as the Primary Challenge

### Explicit and Repeated Emphasis

Mikhail stated multiple times that unstructured data is the core problem:

> "Majority of the data that we're concerned with today for this discussion is unstructured data. So it lives inside documents. It could live inside the meeting transcripts. It could live in the procedures or a problem statement."

When Colin asked whether numeric/scientific data (machine learning territory) or textual data (Gen AI territory) was the priority:

> "I'm going to say unstructured is probably the initial. Yeah, because all the entry points are unstructured, right? It's procedures that are written, people putting the problem statements in place, people responding to the problem statements, et cetera, et cetera."

### Metadata Exists but Is Incomplete

There is some metadata in the system:

> "Mostly unstructured, though we do have in some areas metadata to identify the customer or to identify something. It's not 100%."

This means partial tagging exists -- some documents carry customer identifiers or other metadata -- but coverage is inconsistent. This is not a clean structured environment with missing tags; it is a fundamentally unstructured environment with occasional metadata attached.

### The Labeling Problem

The labeling effort required to make the unstructured data tractable for ML approaches was estimated and paused:

> "If it were to use ML models what it would take us to label, go through labeling exercise, it was over a thousand man hours just to get the labeling up and then continuous maintenance."

Mikhail did not dismiss labeling permanently:

> "Doesn't mean we don't want to do it. All I'm saying is we've looked at the labeling activity... that's one of the reasons we're kind of limited to fields to see if we can prove out."

The implication: if the two-field proof of concept (customer name, file name) succeeds, a broader labeling investment might be justified. But the thousand-hour estimate was enough to defer it.

---

## 5. Identity and Access Management (IAM)

### Current State: In Progress, Not Robust

Brad provided the most direct assessment of IAM maturity:

> "The company's working on getting to more of an IAM, Identity Access Management. And so that's an active program that's been going on probably for about two years. We're making progress there but I wouldn't say that it's like super robust."

He hedged further:

> "I'm going to say, I wouldn't say it's super robust. I'm going to say we do have attributes around some of that stuff."

### What IAM Currently Provides

Brad described what currently exists:

- **Work center identification:** "We identify people by the work center."
- **Role identification:** "And the role" -- but this was qualified as incomplete.
- **Some user attributes:** "We do have attributes around some of that stuff."

### What IAM Does Not Yet Provide

Brad was explicit:

> "We don't have an enterprise-wide IAM thing yet. I'm not saying the company, I mean, I know the company's working on it, but it's not something easily transformed."

The IAM program has been underway for approximately two years but has not reached the level of maturity needed to solve the access control problem at enterprise scale.

### Mikhail's View of IAM's Future Relevance

Mikhail acknowledged that IAM will eventually help:

> "I think where the IAM part of it is, right, the Identity Access Management, if it's working, I think it will eventually come to the place where it's going to help quite a bit for the problem. I think in the future more help."

But this is explicitly future-tense. IAM is not currently a lever that can be pulled to address the IP protection problem.

---

## 6. ASM (Access Security Management)

### What ASM Governs

Brad described ASM as a more mature but narrower system:

> "We do have ASM that governs access to certain things, right? So like our escalate flow area, right?"

Specific ASM capabilities in the escalation system:

> "We even have the capability in there that a user can make a conscious decision to restrict the entire ticket and/or attachments by attachments. But not by all the different entry fields. They can do the whole thing, and then it's restricted, or they can [restrict] specific documents that they may actually upload."

### ASM Limitations

Brad was clear about what ASM does not cover:

> "ASM... doesn't govern everything. It only governs certain things that it's actually tied to, which is our more sensitive areas, that it's been a hard [requirement]."

So ASM provides granular access control in specific high-sensitivity areas (like the escalation system) but is not an enterprise-wide solution. It is a point solution deployed where the risk was judged highest.

### The Gap Between ASM and Enterprise IAM

The picture that emerges: ASM handles the most sensitive areas with ticket-level and attachment-level restrictions. IAM is the broader enterprise effort that has been underway for two years but is not yet robust. Between the two, there is a significant coverage gap where the default behavior is over-restriction via policy rather than technical controls.

---

## 7. Employee Categories and Access Tiers

### Categories Explicitly Named

Brad enumerated the employee categories relevant to the access model:

> "Whether you're an employee or you're a contractor, right, or you're an LSP, licensed service provider."

And additional restriction layers:

> "We do have certain restrictions even if you're a Lam employee. So if you're a trade restricted employee or you're in an embargo country, there is restrictions based on your location."

### Full Category List

1. **Blue badge employees** -- full Lam employees, broadest access. Brad: "if you're a Lam blue badge employee, you have [access]... now again, there's different philosophies on that."
2. **Contractors** -- restricted relative to full employees.
3. **LSPs (Licensed Service Providers)** -- a distinct category from contractors, with their own restriction level.
4. **Trade-restricted employees** -- Lam employees who carry trade restrictions; they "have a different colored badge."
5. **Embargo country employees** -- Lam employees located in embargoed countries, with location-based restrictions.

### How Restricted Employees Are Identified

Brad indicated that trade-restricted employees have system-level markers:

> "Those people are flagged in our system that have an identifiable flag that they are a TRI employee or something like that. They even have a different colored badge. There's some attribute there that can be keyed off of, right, or that can be leveraged."

This means there are existing system attributes for at least the most restricted categories. The question is whether these attributes are consistently applied and whether they are available to downstream systems for automated access decisions.

### The Over-Access Problem for Blue Badge Employees

Brad gave a telling example about the looseness of access for unrestricted employees:

> "In our engineering system. I'm an office worker. I have access to all our drawings and schematics. Do I use them? Do I access them? No. So why do I have access? Well, I do have access, but I don't ever use my access, right?"

And the philosophical debate it creates:

> "So there's discussions in the company about, well, we shouldn't give access to people that never need access to this stuff. Why do they have blanket access, right? But it's just an old [way of doing things]."

Brad categorized this as a future concern, not a current priority:

> "Those are old philosophies or the old ways of like doing things. So we do want to put those in place and later is more like an evolution. But it's not something that is a major issue to solve now. That's more of just like tightening things up later and just getting better at some of this."

---

## 8. The Over-Restriction Mechanics

### How Over-Restriction Works in Practice

Brad and Mikhail described the mechanism clearly. The core logic is:

> "We don't know if this document contains IP. We're just going to, by default, assume that it does. We don't want to risk it, right? So it's more that's where over-restriction starts coming in."

Or as Brad put it:

> "When in doubt, we just restrict it."

### Concrete Example: Cross-Customer Knowledge Sharing

Mikhail provided a specific example of how this plays out:

> "If document three has the path to solution, but you only can look at Intel documents and this sits in a Samsung space, you're not going to see that."

And the customer trust dimension:

> "What we say in Samsung, which really means in-lab employees, but that still, Samsung trusts us that it's not cross-shared, right? Because there could be like, oh, Samsung solved that problem, but that could be very proprietary."

### The Escalation System Example

In the ticket system specifically:

> "A person at Micron is going to open a ticket, people that identify as part of being Micron will be able to see and search all those tickets. So that exists today in our tool. What doesn't exist... a Samsung person opens a ticket. Nobody at Micron [is] able to see that ticket, because they will be able to identify there is a possibility [of IP exposure]."

### Consequences of Over-Restriction

Brad acknowledged the costs directly:

> "We're also knowing that we're limiting the productivity, the capability, because we don't share that much."

And in broader business terms:

> "This is very, very costly. When you're in this phase, also, it affects customer trust, other things."

Mikhail was equally direct:

> "This also limits to what data we can train our AI agents on... if this source is restricted and we cannot control whether this data could be trained for general public, we're not going to pass the source to the model to train them because we don't want to assume that additional risk."

### Over-Restriction as a Self-Reinforcing Cycle

The pattern described in the meeting:
1. Data enters the system unstructured and potentially containing IP
2. Because there is no reliable way to detect/redact IP, the default is to restrict access
3. Restricted access creates siloed search tools and databases
4. Siloed data cannot be used to train AI models
5. Without AI models, there is no automated way to detect/redact IP
6. Return to step 2

This is the fundamental cycle that the engagement is being asked to break.

---

## 9. The Ticket-Level Data Flow

### How a Ticket Moves Through the System

Synthesizing from multiple statements across the meeting, here is the data flow for a single troubleshooting ticket:

1. **Self-help search** -- technician searches across available knowledge bases (limited by customer restrictions). Six different search tools, fragmented databases.
2. **Ask for help** -- if self-help fails, technician opens a ticket. They enter a free-text problem statement. This is an unstructured text entry point. Example: "I'm on my phone, Fab 11, and I have this issue with this tool."
3. **Expert engagement** -- ticket is routed to an expert community. Experts may have a Microsoft Teams meeting, which is automatically transcribed and attached to the ticket.
4. **Escalation** -- if the initial expert community cannot resolve, the ticket escalates to structured troubleshooting with more experts involved.
5. **Resolution** -- the answer is captured in the ticket.
6. **Feedback loop (aspirational)** -- the resolved ticket feeds back into the self-help knowledge base so future technicians can self-serve.

Step 6 is where the IP problem creates the hardest block. The feedback loop cannot function safely without reliable detection and redaction, so knowledge stays locked in restricted tickets.

---

## 10. Specific Systems and Tools Mentioned

| System/Tool | What Was Said | Context |
|---|---|---|
| **LamGPT** | "We still have OpenAI like the GPT models within Lam" | Internal deployment of GPT models, part of the fragmented landscape |
| **Copilot** | "In the Copilot, we're really talking OpenAI model" | Microsoft Copilot deployment; Colin confirmed it runs GPT models |
| **Six search tools** | "We have six search formulas" | No specific names given; described conceptually rather than by system name |
| **Microsoft Teams** | Transcription automatically attached to tickets | Used for expert troubleshooting calls in the escalation workflow |
| **Azure cloud** | MLOps deployed on Azure cloud for model training | Hosted the Transformers/SpaCy/Azure AI model experiments |
| **On-prem systems** | "Some of it on-prem" | Still active, no migration timeline specified |
| **Cloud-based bots** | "Some of it is again cloud but bots" | Additional automation layer, not further specified |
| **ASM** | Access security management for sensitive areas | Controls ticket-level and attachment-level access in the escalation system |
| **IAM (in progress)** | Identity Access Management program | Two years in, not enterprise-wide yet |
| **Engineering system** | Contains "all our drawings and schematics" | Brad's example of over-broad access for blue badge employees |
| **Escalation ticket system** | Customer-segmented visibility | Users can see tickets only for their assigned customer; manual restriction of whole ticket or individual attachments is possible |

---

## 11. Colin's "Unified Control Plane" Argument

Colin made an extended case for a common architectural layer across the fragmented systems:

> "There has to be commonality between these applications. The good thing with that is about 95% of a redaction application is identical. The only thing that really changes is maybe some strategy for ingestion, maybe the end use case is a little bit different, but the actual architecture fundamentally is relatively the same."

> "If you want to put your lasso around a lot of things at the org, you know, taking that snowball approach, pick the things that are the highest impact for you first, absolutely good way to start. But overall, you don't want to keep things so fragmented because you're going to end up trying to play whack-a-mole with this."

And the ingestion-first argument:

> "Making sure that entry point is very robust, that is where the biggest bang for your buck is going to be here for sure. It's easier than you would think if you can have that common control plane. The more diverse and the less governance that's over that space, the worse this gets and it gets worse over time."

**Brad's reception of this argument was not explicitly positive or negative.** He did not push back, but he also did not endorse it. Mikhail's earlier insistence that the two business cases (detection and redaction) be treated as "separate swim lanes" may be in tension with a unified control plane approach, or it may simply reflect a preference for scoped MVP work.

---

## 12. What Lam Does Not Own

Mikhail noted that the scope includes systems outside Brad's direct control:

> "Of course, there is, of course, matrix pieces. We do have some systems within this flow that we don't own."

But the initial engagement is scoped to their own systems:

> "Our initial focus is to prove out this case within our systems. If we can prove out success, you can start branching out to other places."

This means the MVP scope is limited to Brad's org-owned systems, but the broader problem includes systems owned by other parts of Lam. Cross-org system integration would be a future phase, not a first engagement concern.

---

## 13. Open Questions and Unresolved Points

1. **Which six search tools?** Mikhail referenced "six search formulas" but deliberately kept the discussion conceptual. The specific tools were never named. This information is needed for any technical architecture work.

2. **LamGPT architecture.** Is LamGPT running on-prem or in Lam's cloud tenant? How is it integrated with the search tools? What data does it have access to? None of this was specified.

3. **Copilot deployment scope.** Is Copilot deployed broadly or to specific teams? What data sources does it connect to? Is it governed by the same over-restriction policies?

4. **On-prem system specifics.** Which systems remain on-prem? What is the migration timeline? Are these part of the six search tools or separate?

5. **Microsoft Teams transcript handling.** Transcripts are "automatically attached to the ticket." Is there any review step? Any filtering? This is a direct IP ingestion risk channel with no apparent controls described.

6. **ASM coverage scope.** ASM governs "certain things" in "more sensitive areas." Which systems exactly? Is the escalation ticket system the only one, or are there others?

7. **IAM roadmap.** Two years in, not robust. What is the planned timeline for enterprise-wide IAM? Would the IP protection solution need to integrate with or anticipate the IAM rollout?

8. **Contractor and LSP access details.** Brad listed the categories but did not specify how contractor and LSP access differs from blue badge in practice. Are they on different systems entirely, or the same systems with different permission levels?

9. **Cloud provider specifics.** Azure was mentioned for the ML experiments. Is Azure the primary cloud provider for all cloud workloads, or are multiple providers in use?

10. **The engineering system access question.** Brad raised the example of office workers having access to drawings and schematics as a philosophical issue for later. But if the IP protection solution needs to account for who should have access to what, this "later" problem may need to be addressed sooner.

11. **Transcript cuts off.** The meeting transcript ends mid-sentence as Mikhail is about to answer Colin's question about "high value targets" -- which specific platform or use case would be most impactful to tackle first. This answer was not captured.

---

## 14. Summary: The Infrastructure Picture

Lam Research's infrastructure reality for this engagement is defined by fragmentation, partial governance, and defensive over-restriction:

- **No unified data layer.** Six or more search systems, databases segmented by customer and restriction level, on-prem and cloud mixed, no data lake.
- **Multiple AI deployments.** LamGPT (internal GPT), Microsoft Copilot, cloud bots -- each presumably with their own data access patterns and restrictions.
- **IAM immature.** Two-year-old program, not enterprise-wide, not robust. User attributes exist for the most restricted categories (trade-restricted, embargo country) but general identity and access management is not solved.
- **ASM point solution.** Effective in the escalation system for ticket-level and attachment-level restrictions, but not a general-purpose access control framework.
- **Unstructured data dominant.** Documents, transcripts, problem statements, procedures -- all text, all potentially containing customer-identifiable information, all lacking consistent metadata.
- **Over-restriction as the default.** In the absence of reliable detection and redaction, everything is assumed to contain IP and restricted accordingly. This throttles productivity, limits AI training data, and creates a self-reinforcing cycle of knowledge fragmentation.
- **Cloud-first aspiration.** Stated preference for cloud and microservice architecture going forward, but current reality is far from that aspiration.

Any technical solution must work within this fragmented, partially governed, aspiration-reality-gap environment -- or must propose a path toward the architectural coherence that does not yet exist.
