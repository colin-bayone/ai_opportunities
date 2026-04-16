# 02 - Meeting: Infrastructure & Access (Deep Dive)

**Source:** `source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on infrastructure and IAM

---

## 1. Infrastructure Stack and Platform Landscape

### 1.1 Colin's Direct Question About Infrastructure

Colin asked a direct question: "Is there like a stack that this is deployed on? When I say stack, I'm not talking about development stack, but more like infrastructure stack. So I heard co-pilot. So is this all on Azure? Is that true? Or is there multiple platforms that this is deployed on?"

### 1.2 Mikhail's Response - The "Everything" Answer

Mikhail's response was emphatic and revealing:

> "Oh my God. This is like ever like anything you can make up is because again, these are not free systems. Yeah, right some of it on pram some of it is on cloud some of it is eventually gonna move to cloud some of it is lamb GPT so we still have Open and like the GPT models within lamb some of it is again cloud but bots so anything you can think of most likely this is a hazard."

Key breakdown of what exists:
- **On-premises systems** - some current systems run on-prem
- **Cloud systems** - some are already cloud-based
- **Systems in migration** - some "eventually gonna move to cloud"
- **LamGPT** - GPT models hosted within Lam's own infrastructure
- **Cloud bots** - some bot-based solutions on cloud
- **Legacy systems** - implied by the sheer diversity ("these are not free systems" meaning these are not greenfield, they are inherited/ accumulated systems)

Mikhail explicitly framed the problem as not about discrete systems but about flows: "Because these are not two, three systems. I'm not describing a single system or three systems. These are flows. These are flows."

### 1.3 Cloud-First Aspiration

Immediately after describing the fragmented current state, Mikhail stated the directional aspiration:

> "But we do want to focus on cloud first going forward. So that's our plan."

### 1.4 Microservice Architecture Aspiration

Mikhail also articulated a longer-term architectural vision:

> "And again, I don't want to dive into technical, but we also want to focus on microservice architecture long term. Whether we do or not, let's say these solutions, that's a different thing, but that's our kind of aspirational goal to focus on."

Key nuance: He qualified this as "aspirational" and acknowledged uncertainty about whether it will actually happen ("whether we do or not"). This was not presented as a committed roadmap item but as directional thinking.

---

## 2. The Data Fragmentation Problem

### 2.1 No Unified Data Lake

Colin asked directly: "Is there one unified place or is this kind of broken up by each application?"

Mikhail's response confirmed fragmentation:

> "Because we have many search tools and ways of getting information, some of the databases or some of the stuff is segmented and different. So there is not one, you could say data lake or something like that."

He then added that a unified data lake is not off the table for the future: "So there doesn't mean that that's not in the future."

### 2.2 Six-Plus Search Systems

Mikhail explicitly stated the scale of search fragmentation:

> "We have six search formulas."

He used this as the reason to discuss the problem conceptually rather than system-by-system: "So that's why I want to talk conceptually, rather than specific systems, because we have, in some areas we have a single source, in some areas we have many, many different systems."

No specific search system names were given during the call. The six-plus search tools were referenced as a class, not individually enumerated.

### 2.3 Fragmentation Creating Silos

Brad and Mikhail described how the fragmentation itself produces knowledge silos:

> "But the thing is, is now you have a seven or an eight. You're at nine, so you're just creating silos of what you think is the right information to serve through that. And then again, it's another form of restricting."

The implication: each new restricted search creates another silo, compounding the problem rather than solving it. The number growing from six to seven to eight to nine represents the creep of fragmented search tools over time.

### 2.4 The Over-Restriction Problem - Specific Examples

**Example 1 - Cross-customer knowledge blocking:**
> "If document three has the path to solution, but you only can look at Intel documents and this sits in a Samsung space, you're not going to see that."

This is a concrete illustration: a field technician working on an Intel problem cannot access a Samsung ticket that contains the solution, even though the underlying technical knowledge may have nothing customer-proprietary about it.

**Example 2 - AI training data limitations:**
Mikhail explicitly connected over-restriction to AI capability:
> "And this also limits to what data we can train our AI agents on, right? Or our AI mobs, not agents, but our models on because, hey, if this source is restricted and we cannot control whether this data could be trained for general public, we're not going to pass the source to the model to train them because we don't want to assume that additional risk."

Over-restriction therefore has a cascading effect: it prevents not just human access to knowledge, but also prevents AI models from being trained on that knowledge.

**Example 3 - Escalation ticket visibility:**
> "What doesn't exist [is that if a] Samsung person opens a ticket... nobody at Micron [is] able to see that ticket, because they will be able to identify there is a possibility [of IP exposure]."

Even when a Samsung ticket's solution would help a Micron technician, the entire ticket is invisible.

**Example 4 - Policy violations are common:**
Brad provided a striking anecdote about how quickly violations surface:
> "When we started this project, I'm like, how many tickets is gonna take me to find policy violation? Seven. Seven's ticket, there was a... already concept-renade."

By the seventh ticket examined, a policy violation (customer confidential information in the wrong place) was found.

---

## 3. Data Types and Data Flows

### 3.1 Unstructured vs. Structured Data

Mikhail was emphatic that the primary concern is unstructured data:

> "Majority of the data that we're concerned with today for this discussion is unstructured data. So it lives inside documents. It could live inside the meeting transcripts. It could live in the procedures or a problem test."

He acknowledged some structured metadata exists: "Though we do have in some areas metadata to identify the customer or to identify something. It's not 100%."

### 3.2 How Data Enters the Systems

Colin asked how things get into the system. Mikhail's response catalogued multiple ingestion paths:

1. **Standard procedures** - written documents uploaded or created
2. **Problem statements** - free-text entries by users describing issues (e.g., "I'm on my phone, Fab11, and I have this issue with this tool")
3. **Responses to problem statements** - expert answers entered as free text
4. **Teams meeting transcriptions** - automatically captured and attached to tickets
5. **Document uploads** - files attached to escalation tickets
6. **OCR images** - pictures/diagrams that contain embedded text

Mikhail explicitly said he cannot give a neat answer:
> "I'm not going to be able to give you a very neat answer how things get in, because yes, the majority of our concerns is with our procedures and documents. But in this case, this is an unstructured data entered by people in their problem statement."

### 3.3 Teams Meeting Transcription Workflow

A specific workflow was described for escalation:

> "For example, when you're in escalation flow, we actually have if they schedule out of the system, Microsoft Teams meeting, it's transcribed and it's automatically attached to the ticket."

This means:
- Escalation tickets can trigger Teams meetings
- Those meetings are scheduled "out of the system" (from the ticketing system)
- Microsoft Teams auto-transcribes the meeting
- The transcription is automatically attached back to the originating ticket
- This transcription is unstructured data that could contain customer-identifiable information

### 3.4 The Feedback Loop

Mikhail described a critical data flow aspiration - a feedback loop:

> "There is the feedback loop, because we want to actually drive down the usage of these systems by doing what? Once the problem statement and the answer is identified, we feed this always back so next time people come in, they self-help and they don't have to ask the question."

The problem: this feedback loop requires taking unstructured data from escalation tickets and feeding it into the general self-help knowledge base. But that data may contain customer-identifiable information, which prevents the feedback loop from functioning:

> "The problem with that, all of this is unstructured data. So even if the user was identified, it doesn't help us because long term it has to feed into more general population."

This is the core tension: productivity requires opening up data, but IP/customer protection requires restricting it. The feedback loop is blocked by the over-restriction problem.

---

## 4. Identity and Access Management (IAM)

### 4.1 Current IAM State

Brad gave the most direct assessment of IAM maturity:

> "I wouldn't say it's super robust. I'm going to say we do have attributes around some of that stuff. The company's working on getting to more of an IAM identity access management. And so that's an active program that's been going on probably for about two years. We're making progress there but I wouldn't say that it's like super robust."

Key facts:
- IAM program has been active for approximately two years
- Progress is being made but the system is not "super robust"
- It is a company-wide initiative, not limited to Brad's org
- Not yet enterprise-wide in coverage

### 4.2 User Identification Attributes

Users are identified by two primary attributes. Mikhail and Brad confirmed:

> "We identify people by the work center. And the role."

Mikhail was cautious about overstating the sophistication:
> "I'm going to say we do have attributes around some of that stuff."

### 4.3 Employee Categories and Restrictions

Brad outlined the employee taxonomy and associated restrictions:

**By employment type:**
- **Lam employees** (blue badge) - broadest access
- **Contractors** - have restrictions associated with their status
- **LSPs (Licensed Service Providers)** - also have restrictions

**By trade restriction status:**
- **Trade Restricted Individuals (TRI)** - employees flagged in the system who have specific restrictions
- TRI employees "even have a different colored badge"
- "There's some attribute there that can be keyed off of, right, or that can be leveraged"

**By geography:**
- **Embargo country employees** - "If you're a trade restricted employee or you're in an embargo country, there is restrictions based on your location"

Brad's exact language:
> "So we do have, whether you're an employee or you're a contractor, right, or you're an LSP, licensed service provider. So the difference... So there is restrictions associated with those, okay? We do have certain restrictions even if you're a land employee. So if you're a trade restricted employee or you're in an embargo country, there is restrictions based on your location. But you do have people in those regions that are restricted, but those people are flagged in our system that have an identifiable flag that they are a TRI employee or something like that, they even have a different colored badge."

### 4.4 The Over-Provisioning Problem

Brad gave a candid example of access being too broad in some areas while over-restricted in others:

> "In our engineering system. I'm an office worker. I have access to all our drones and schematics. Do I use them? Do I access them? No. So why do I have access? Well, I do have access, but I don't ever use my access, right? So there's discussions in the company about, well, we shouldn't give access to people that never need access to this stuff. Why do they have blanket access, right? But it's just an old... Right. Those are old philosophies or the old ways of like doing things."

He characterized tightening this as evolutionary, not urgent:
> "So we do want to put those in place and later is more like an evolution. But it's not something that is a major issue to solve now. That's more of just like tightening things up later and just getting better at at some of this."

### 4.5 ASM (Access Security Manager)

Brad described ASM as a partial solution:

> "We do have ASM that governs access to certain things, right? So like our escalate flow area, right?"

**What ASM can do:**
- Governs access to certain applications/ areas (specifically mentioned: the escalation flow area)
- Allows users to make conscious decisions to restrict entire tickets
- Allows users to restrict specific attachments on tickets

**What ASM cannot do:**
- Does not restrict individual entry fields within tickets (only whole ticket or attachment level)
- Does not govern everything - only "certain things that it's actually tied to"
- Is not enterprise-wide

Brad's exact framing:
> "And we even have the capability in there that a user can make a conscious decision to restrict the entire ticket and or attachments by attachments, but not by all the different entry fields. They can do the whole thing, and then it's restricted, or they can specific documents that they may actually upload. So I think ASM, but it doesn't govern everything. It only governs certain things that it's actually tied to, which is our more sensitive areas, that it's been a hard idea. But we don't have an enterprise-wide IAM thing yet."

### 4.6 Customer Data Segmentation

The current segmentation model works at the customer level for ticket visibility:

> "If a person at Micron is going to open a ticket, people that identify as part of being Micron will be able to see and search all those tickets. So that exists today in our tool."

The inverse is also enforced:
> "What doesn't exist [is that if a] Samsung person opens a ticket... nobody at Micron [is] able to see that ticket."

Important clarification from Mikhail: the people opening tickets are Lam employees working at customer sites, not customers themselves:
> "And again, land employee, not Samsung, because these are internal tools. But Samsung, nobody at Micron able to see that ticket, because they will be able to identify there is a possibility."

So the segmentation model is:
- Lam employee assigned to Micron -> can see Micron tickets
- Lam employee assigned to Samsung -> can see Samsung tickets
- Cross-visibility is blocked (Micron-assigned cannot see Samsung tickets and vice versa)
- This is "internal tools" - customer employees do not directly access these systems

---

## 5. AI and ML Tools in Use

### 5.1 LamGPT

Mikhail mentioned LamGPT in passing when describing the infrastructure landscape:

> "Some of it is lamb GPT so we still have Open and like the GPT models within lamb."

This indicates:
- LamGPT is an internal deployment of GPT models
- It runs within Lam's own infrastructure (not a SaaS subscription to OpenAI directly)
- It uses OpenAI's GPT models (the transcript says "Open and like the GPT models")
- It is one of many AI tools in the environment

No further details were provided about LamGPT's specific use cases, deployment architecture, or which GPT model version is in use.

### 5.2 Copilot Usage

Copilot was mentioned in context of the Microsoft ecosystem. When Colin asked about the stack, someone (likely Pat or Rahul) noted:

> "From an AI perspective, in the compiler, we're really talking open AI model, right? Because compiler using GPT models, right? They don't use open AI. I should not say that. That doesn't sound right. They use GPT models inside."

This confirms:
- Microsoft Copilot is in use at Lam
- Copilot uses GPT models internally
- There was some confusion/correction about whether to say "OpenAI" vs "GPT models" - the speaker corrected themselves to say Copilot uses GPT models

### 5.3 What Has Been Tried - ML/AI Experiments

Mikhail detailed the specific models and approaches tried:

**Models tested:**
1. **Transformers model** - named explicitly
2. **Spacy** - named explicitly
3. **Azure AI model** - named explicitly
4. A possible fourth model (Mikhail said "I don't remember the third" implying there were more)

**Infrastructure for ML experiments:**
> "We put MLOps in place, and we've tried training a few models."
> "It was a cloud-based MLOps put on Azure cloud, but the model was, like I said, Azure AI model, space and transformers."

So the MLOps pipeline was on Azure cloud, even though the broader infrastructure is heterogeneous.

**Results:**
- False positive rate of approximately 20% per ticket ("20% of tickets ended up with 20% false positive rate")
- Fine-tuning improved it only marginally: "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."
- Target: "way below 1% end state"
- Colin's assessment: "When I heard 20%... that's pretty much out-of-the-box chat GPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all."

**Rule-based approaches also tried:**
> "We've started trying rule-based models, but we haven't gotten far because, again, something like a fab could be spelled many different ways, right?"

Example of the problem: a single concept like "Fab 11" could appear as "Micro 11," "F11," "PAP space 11," "PAP dash 11," etc. Rule-based models require constant maintenance to account for new permutations.

### 5.4 Generative AI vs. Machine Learning Distinction

Mikhail made an important strategic distinction:

> "One thing I don't want us to limit is to just LLMs and generative AI. So for example... some of the things we've actually tested was more with machine learning rather than generative AI. We actually have not used generative AI to prove any use cases, not because of unstructured data, but because of unstructured output."

His reasoning:
> "We decided to go with something more definitive that can tell us redact, don't redact, rather than at a structured output that LLMs typically produce. I know it's prompt, you can make it structured, but there's limits to that as well."

This is a significant design philosophy: they chose ML over Gen AI for the redaction/detection use case specifically because ML gives binary outputs (redact/don't redact) while LLMs give probabilistic, unstructured outputs.

### 5.5 Technology Agnosticism

Brad explicitly stated they are not wedded to AI as the approach:

> "I do want to also stress, I know AI is a very sexy word, but it's also a meaningless word. And not married to any specific AI technologies, LLM, machine learning, or anything like that, it doesn't have to be an AI."

He acknowledged AI's advantages but kept the door open:
> "Preference on AI? Sure, because your kind of ceiling goes up with AI, what you can do afterwards, because other solutions are very important solutions."

---

## 6. Azure and Microsoft Stack Components

### 6.1 Confirmed Microsoft/Azure Elements

- **Microsoft Teams** - in use for escalation meetings, with auto-transcription
- **Microsoft Copilot** - in use, running GPT models
- **Azure Cloud** - used for MLOps pipeline
- **Azure AI model** - one of the models tested for redaction/detection

### 6.2 Colin's Question About Azure Services

Colin asked specifically: "Are you using Azure AI Foundry for the cloud side?"

Mikhail's response was frank about the limits of his technical knowledge:
> "You're not talking to a technical audience here. But to an extent, I'm able to represent."

He did not confirm or deny Azure AI Foundry or Azure Purview usage. The technical details beyond what he could represent would need to come from Daniel or other technical team members in a follow-up meeting.

---

## 7. Colin's "Unified Control Plane" Suggestion

### 7.1 The Suggestion

Colin made a strategic recommendation mid-conversation:

> "Just to be honest, because I had to do the same thing and there's no way to do this unless you have some kind of a common control plane. And what I mean by that is there has to be commonality between these applications."

He elaborated on the concept:
> "The good thing with that is about 95% of a rack application is identical. The only thing that really changes is maybe some strategy for ingestion, maybe the end use case is a little bit different, but the actual architecture fundamentally is relatively the same. But if you want to, you know, kind of put your lasso around a lot of things at the org, you know, taking that snowball approach, you know, pick the things that are the highest impact for you first, absolutely good way to start."

He warned against continued fragmentation:
> "But overall... You don't want to keep things so fragmented because you're going to end up trying to, you know, play whack-a-mole with this. I say that from experience."

And made the case for unified ingestion:
> "There has to be some kind of a unified control plane for how information gets in and how information gets out."

He then specifically argued that ingestion is where the biggest impact lies:
> "The whole problem is that whenever you make information known or available to AI, that's how information comes in. That ingestion part is so critical because even if information comes out, you shouldn't have to redact anything if this part actually worked. It's not possible. It can't create that from nothing... Making sure that entry point is very robust, that is where the biggest bang for your buck is going to be here for sure. It's easier than you would think if you can have that common control plane."

### 7.2 How It Was Received

Colin then asked directly about appetite:
> "Maybe from the standpoint of what's the appetite for something like that? If you were to say for the applications they have internally, is it something where we can pick the top end of them or is it something where we would have capability to say, we can give you a very nice integratable place where things can get stripped out early so that they're stored right the first time because then you don't even have to worry about downstream."

Brad's response was open and receptive:
> "So to answer your question, Paul [Colin], and I think you were asking there is, we are open to any and all approaches by also understanding what are the trade offs and what are the outcomes that we can expect with those, right?"
> "I think anything and everything as Miquel was saying is on the table."

However, Mikhail then added a cautionary note about scope:

> "I just want to caution against that... I just want to make sure we're not introducing noise in our business case."

He wanted to keep the discussion focused on the two specific use cases (detection at entry, redaction on stored data) rather than broadening to the full access management question. He acknowledged Colin's point but wanted to maintain focus:

> "Some of this is already built into our system. So that part is already there, but that's what's causing over restriction because we only have that information, so we have to indiscriminately restrict on these things rather than saying very specific pieces of information."

---

## 8. The Labeling Problem

### 8.1 Scale of Labeling Effort

Mikhail quantified the labeling effort that was assessed:

> "One of the things we looked at for example if it were to use ML models what it would take us to label go through labeling exercise it was over a thousand man hours just to get the labeling up and then continuous maintenance."

This was described as "fairly expensive activity" but not ruled out:
> "Doesn't mean we don't want to do it all I'm saying is [we] looked at the labeling activity to do exactly what you're saying, but that's one of the reasons we're kind of limited to fields to see if we can prove out."

The strategic calculus:
> "And if we say, yeah, this case is where all the things sit, maybe a thousand hours is just peanuts compared to the productivity gains we could gain by opening this up."

### 8.2 The Two-Field MVP

Brad referenced the MVP scope being limited to two data fields:

> "What I think we want to prove out, or we tried to prove out in our initial, correct if I'm wrong, account, was just really about two attributes or two data fields, right? Because if you can't get those correct, and you can't redact or do whatever we're trying to do with those, you can't escape, right?"

The two fields were identified as: **customer name** and **file name** (sometimes called "company"):
> "We want to promote those couple of fields, right? Let's say customer name, file name. Sometimes those are just enough."

---

## 9. System Ownership and Scope

### 9.1 Systems Owned vs. Not Owned

Mikhail acknowledged that some systems in the flow are outside their org's ownership:

> "Of course, there is, of course, matrix pieces. We do have some systems within this flow that we don't own. But our initial focus is to prove out this case within our systems."

Strategy: prove the approach within owned systems first, then expand:
> "If we can prove out success, you can start branching out to other places."

### 9.2 Brad's Organizational Scope

Brad's organization owns the end-to-end pipeline for this initiative:

> "Brad owns both product, engineer, and kills that guy. I own the entire thing."
> "I have everything from business, program, product, to technical."

Team structure: Brad (business/product), Daniel (technical), with scrum teams assembled across the three functions (business, program, product, technical).

---

## 10. Performance Requirements

### 10.1 Detection at Entry Point - Real-Time

For the detection use case (notifying users of potential policy violations as they enter data):

> "This is real time, right? How fast you can get... to detect and notify the user that they would have possible violation of customer confidential information."
> "This has to run... within UI, whatever is UI standards, two to five seconds max, right."

### 10.2 Redaction on Stored Data - Batch

For the redaction use case (cleaning stored data to enable broader access):

> "This could run an hour."

The performance distinction is critical: detection must be sub-5-seconds; redaction can be batch-processed over longer timeframes.

### 10.3 False Positive Sensitivity

For detection (real-time notifications):
> "We're much more sensitive in this space to false positives rather than over-redacting... because this is real time. These are notifications that go to the users."
> "If every fifth thing I say, hey, you possibly have a violation, then you're like, no, I don't. People are just not going to trust it."

For redaction (stored data cleanup):
> "In this space we're right over-redacting. So if we over-redact less, we already have success."

Target: below 1% false positive rate for detection.

---

## 11. Summary of Named Systems and Technologies

| System/Technology | Context | Status |
|---|---|---|
| Microsoft Teams | Meeting scheduling and auto-transcription in escalation flow | In use |
| Microsoft Copilot | AI assistance using GPT models | In use |
| LamGPT | GPT models hosted within Lam infrastructure | In use |
| Azure Cloud | MLOps pipeline hosting | In use (for ML experiments) |
| Azure AI model | One of models tested for redaction | Tested, paused |
| Spacy | NLP model tested for redaction | Tested, paused |
| Transformers model | ML model tested for redaction | Tested, paused |
| ASM (Access Security Manager) | Governs access to sensitive areas (escalation flow) | In use, limited scope |
| MLOps pipeline | Cloud-based on Azure | In use |
| 6+ search tools | Multiple search interfaces across different data silos | In use |
| Rule-based models | Attempted for detection/redaction | Tried, abandoned due to maintenance burden |

---

## 12. Key Gaps Identified in This Conversation

1. **No unified data lake** - data fragmented across many systems
2. **No enterprise-wide IAM** - program in progress (~2 years) but not robust
3. **ASM covers only specific areas** - not enterprise-wide access governance
4. **No common control plane** for data ingestion/output (Colin's recommendation)
5. **No successful AI/ML solution for redaction** - all attempts paused at ~17-20% false positive rates
6. **Labeling effort estimated at 1,000+ person-hours** with ongoing maintenance
7. **No ability to feed escalation data back into self-help** due to IP contamination risk
8. **Six-plus separate search systems** creating knowledge silos
9. **Over-restriction is the default** - organizational philosophy when in doubt
10. **Specific system names for search tools were not disclosed** - Mikhail deliberately stayed conceptual
