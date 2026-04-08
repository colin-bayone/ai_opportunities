# 03 - Discussion: Technical Approach (Round 3)

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)
**Context:** Second round of Q&A follow-up

---

## 1. Dashboard, Reporting, and Governance Framework

### Architecture Decision: Built Into the Control Plane

The metrics/insights layer is a **dashboard and reporting module built directly into the control plane**, not a separate system. This gives leadership visibility into:

- **Governance metrics:** Rejection rates, flagged content patterns, compliance trends
- **Usage metrics:** How much people are actually using the tools -- super valuable to leadership because right now, with fragmented systems, there is no possible way they are tracking usage and understanding actual business value
- **User behavior insights:** Known offenders, repeat flagging, training gap identification
- **Business value demonstration:** The tools' actual impact, not just a guess with leadership support

### Data Layer, Not Dashboard Lock-In

The underlying data is stored regardless of how it's consumed. Multiple consumption options:

- **BayOne-built dashboard** within the control plane (default offering)
- **Integration with existing BI tools** (Tableau, Power BI, whatever Lam uses) -- completely fine
- **BayOne builds the dashboard using their tools** -- also fine

Colin's philosophy: "It's just data. If we store it, it doesn't really matter if we're building the dashboard or if they are, or if we are for them with their tools. It's all the same."

### The Selling Point

This goes beyond governance into **business intelligence about AI tool adoption**. Leadership currently has no visibility into whether their RAG applications are actually delivering value. The control plane solves this as a side effect of existing there. This is a cohesive, holistic solution -- not just a filter bolted onto a chatbot.

---

## 2. AI Classification Speed: Async Queue with Synchronous UX

### Architecture: Queue for Robustness, Not for Batching

The processing architecture is an **async queue**, but the user experience is effectively synchronous:

- The queue exists for robustness (scalability, retry logic, fault tolerance)
- In practice, the queue never actually forms -- documents process in seconds
- Leverages Azure for scale

### User Experience

- User clicks upload
- Upload screen appears ("uploading...")
- While the upload screen is showing, all processing runs (deterministic checks, AI classification)
- If clean: document enters the knowledge base, user proceeds
- If rejected: user gets a message back with specifics -- in the UI, via notification, whatever the system supports

### The "2-5 Seconds" Requirement Needs Clarification

Colin wants to understand the actual motivation behind Mikhail's 2-5 second requirement:

- **If it's 2-5 seconds for the upload itself:** No problem. The processing happens during the upload UX. User doesn't even perceive a delay.
- **If it's 2-5 seconds to start doing RAG on the document:** That's a different constraint entirely. Even ChatGPT takes more than 2 seconds between uploading a document and being ready for RAG queries on it. Speed optimization is possible but we need to understand the actual use case.

### Document-Type-Aware Processing

The best approaches are NOT one-size-fits-all. The system should be aware of document types:

- **Excel file:** Processed differently than a PDF or a transcript. Different patterns, different extraction.
- **Known offender users:** If a user has a history of uploading flagged content, apply greater scrutiny. Normal checks still run, but the AI layer can apply elevated attention.
- **Content type routing:** Different document types route to different processing pipelines within the same queue.

---

## 3. What to Extract from Daniel (Technical Call)

### Questions Already Identified by Colin

From the meeting and this discussion, the specific things we need from the technical lead:

**On prior technical work:**
- What models were actually used? (Beyond "Transformers, SpaCy, Azure AI" -- specific architectures, versions, configurations)
- Who did the work? Internal team, Accenture, or both?
- What was the golden standard / ground truth they were testing against?
- What was the testing methodology? (How were false positives measured? What was the test set?)
- How is the current system deployed? (Infrastructure, pipeline, serving)
- What exactly did the prior approach look like end-to-end?

**On Accenture's involvement:**
- What deliverables did Accenture produce?
- How was the problem statement given to Accenture? (Was it well-scoped or vague?)
- Did Lam give Accenture enough information to succeed, or was it set up to fail?
- This is critical: we need to make sure we don't fall into the same trap if the problem is on the client side (insufficient context, unclear requirements) rather than the solution side.

**On the applications:**
- Top 3 most important RAG-like applications, described at a technical level
- What systems do these applications touch?
- What data sources feed them?
- Are they truly unique, or are they variations of the same architecture?

**On organizational reality:**
- What is the actual governance structure today? (Not Brad's version -- the technical reality)
- How do IT and cybersecurity factor in?
- Brad says he owns everything, but does he actually have authority over IT decisions? Business owners love to say they own things, and Brad does not strike Colin as someone who should be trusted with IT decisions given the state of their current approach.
- We need to verify Brad's claimed ownership so we don't get hamstrung later if IT or security has veto power.

**On infrastructure:**
- What Azure services are they actually paying for?
- What's on-prem vs. cloud today?
- What's the data volume? (Documents per day, tickets per day, searches per day)

---

## 4. Competitive Positioning Against Prior Work

### The Approach: Diplomatic but Clear

**Do NOT:** Call out Accenture by name or throw shade at another company.

**Do:** Position the prior approach as a known pattern with known limitations:

- "Our understanding of the prior approach" -- acknowledge it was tried
- Frame it as a **common but brittle pattern**: custom model training for classification is well-understood but fragile. It requires extensive training content, becomes very static, and cannot respond to dynamic, robust conditions.
- If it was to be successful, it would need a massive labeled dataset and continuous maintenance -- which is exactly what their 1,000+ hour estimate revealed.

### Why the Hybrid Approach Is Better

- **Cost and speed advantage of deterministic systems** (known patterns match instantly, zero false positives on exact matches)
- **Power and flexibility of AI-based systems** for contextual analysis, not just NLP but agentic AI and capabilities built into Azure AI Foundry
- **Enterprise tools from the start** because we're thinking strategically beyond one problem statement

### Colin's Caveat

He does not want to commit to "why my hybrid approach is correct" without knowing more technical details from the Daniel call. But based on what we've heard, the directional positioning is solid. The proposal should say: "from what we've heard, this approach addresses the specific failure modes described" -- not "your prior approach was wrong."

### The Strategic Value Proposition

The value BayOne brings is NOT "we can build a better classifier." It's:
- We are thinking about this strategically for them, not just solving one problem
- Enterprise tools, unified governance, visibility, and scalability
- A platform that grows with them, not a point solution that breaks when requirements change

---

## 5. Application-by-Application Migration: Governance Gap Is Pre-Existing

### The Reality

Yes, during migration there is a period where some applications are on the new platform and some aren't. Yes, this creates a governance gap. But:

**The governance gap already exists today.** Lam has 6+ search systems, no unified data lake, no unified governance, and over-restriction as a blunt instrument. Moving one application to the new system doesn't make the gap worse -- it makes one piece of it better.

### Why Not Big Bang

A massive all-at-once transition would:
- Unnecessarily delay everything
- Prevent early testing and validation
- Require coordinating across all applications simultaneously
- Be the "revolutionary" approach that Brad explicitly rejected

The application-by-application approach is:
- Evolutionary (Brad's word)
- Enables early testing
- Reduces risk
- Each migration reduces the remaining workload proportionally

### Shared Data Sources Reduce Marginal Effort

Colin's key insight: these RAG applications likely do NOT have truly unique data sources. As more applications come online in the new system, the workload decreases proportionally because the data sources are shared. The first application is the hardest. Each subsequent one is easier.

### Reject Ad-Hoc Per-App Customization

Colin explicitly rejects trying to build custom solutions for each individual Q&A bot:
- That's duplication of effort
- Not worth our time
- The whole point of the control plane is that it's a unified architecture
- New applications get pulled into the existing platform, not given bespoke treatment

We can help Lam plan new system integrations to pull additional applications into the architecture, but the architecture itself doesn't change per app.
