# Outline: Discovery Session Document (April 6)

**Purpose:** On-screen reference for the Lam call. High-level talking points with supporting detail available if needed. Not a presentation deck, not a homework assignment.

---

## Section 1: The Problem

### 1.1 The Core Challenge
- Lam services competing customers (TSMC, Samsung, Intel, Micron) simultaneously
- Years of field service, troubleshooting, and escalation work have built a deep internal knowledge base
- The knowledge itself is largely generic and transferable across customers, but it is contaminated with customer-identifiable information (customer names, fab identifiers, site-specific details)
- Because there is no reliable way to separate the generic knowledge from the customer-specific information, everything is restricted by default
- The result: Lam's own engineers cannot access solutions that already exist within the organization

### 1.2 The Business Impact
- Support efficiency and productivity are throttled by the inability to share knowledge safely
- Problems that have already been solved get re-escalated because the solutions are locked behind customer restrictions
- The troubleshooting workflow (self-help, ask for help, escalate) is designed to drive resolution at the lowest tier, but the feedback loop from escalation back to self-help is broken. Cleaned solutions cannot re-enter the general knowledge base.
- This costs time, money, and customer trust

### 1.3 Use Cases Under Discussion
- Two high-level use cases have been identified, both tied to the troubleshooting workflow:
  - **Enabling self-help search** by processing stored content to remove customer-identifiable information so the underlying technical knowledge can be surfaced across customer boundaries
  - **Protecting escalation entry points** by detecting potential customer IP at the point of data entry and notifying users before the information enters the system
- These are broad, high-level use cases. The specific applications, data types, and workflows involved have not yet been defined. That is part of what this session is for.

### 1.4 The Infrastructure Landscape
- Highly heterogeneous environment: on-prem, cloud, in-migration, internal AI deployments, cloud bots
- No unified data lake. Data is fragmented across many systems with different segmentation and access models.
- 6+ search systems covering different knowledge pools
- Aspiration toward cloud-first and microservice architecture

---

## Section 2: Where We Are Today

### 2.1 What We Have Established
- Shared understanding of the problem (confirmed by Lam team)
- Two clear use cases with different technical requirements
- Knowledge of prior approaches and their limitations

### 2.2 Discovery Areas for This Session
- Understanding the technical landscape in more depth
- Identifying a concrete starting point for proof of concept scope
- Learning from what has been tried: what worked, what did not, and why
- Defining what a successful outcome looks like for the team

---

## Section 3: Prior Work

Understanding what was tried, what it was tried on, and what it was supposed to accomplish. We keep this conversational and at a high level. We do not need to dive deep into model architectures. The goal is to understand the application context, not audit the ML pipeline.

### 3.1 What Was Tried and What Was It For?
- What specific application was the prior effort running against?
- What was that application supposed to do? What business problem was it solving?
- How does the detection/redaction capability help that application function better?
- What approaches were used? (ask in passing, don't interrogate)
- What did not work, and why was it not acceptable?

### 3.2 What Does Success Look Like?
- Not in terms of percentages or response times (those were off-the-cuff numbers)
- What was the prior effort supposed to deliver as an outcome?
- What would have made the team say "this is working, let's keep going"?
- Help them articulate: how does solving this change what the application can do for its users?

---

## Section 4: Selecting the POC Target

This is the pivotal section. We must leave this call with a named application, or we cannot move forward.

### 4.1 Same Application or Different?
- Is the application from the prior work still the right starting point?
- Or is there a different, more impactful application the team would rather focus on?
- Either answer is fine, but we need a specific one

### 4.2 If They Need Help Choosing
- The business team is best positioned to identify impact, but some signals that can help:
  - Which application is the most critical to daily operations?
  - Which one has the most users?
  - Which one is the largest and most mature?
- Alternatively, if BayOne is given a catalog of applications or further conversations with the engineering team, we can help identify the right target
- What does not work: a generic, application-less "just detect stuff and we'll feed it documents" framing. That is not a POC, that is a science experiment with no business context.

### 4.3 Going Deep on the Selected Application
- What it does, who uses it, where it sits in the troubleshooting workflow
- What data sources feed into it
- What types of content are most likely to contain customer-identifiable information
- What "sensitive" looks like in this application's specific context
- Data volume: how much content, how often
- Technical environment: Azure, on-prem, or hybrid? What services are in use?
- Architecture: how data enters, how it is stored, how it is served
- Existing pipelines, middleware, or infrastructure
- Any reusable artifacts from prior work

### 4.4 Representative Data
- Examples of content that should be flagged (failure cases from this application)
- Examples of clean content (gold standard)
- Coverage across data types if the application ingests multiple formats
- Sanitized or synthetic examples are acceptable if security constraints prevent sharing real data

---

## Section 5: An Approach That Works

High-level overview of what a proven approach looks like, drawn from BayOne's experience at Coherent and similar environments. Not a final plan. An example of what works, adapted to what we know about Lam's environment so far.

### 5.1 The Hybrid Architecture
- Deterministic layer for known patterns (customer names, fab identifiers, spelling variations) using enterprise tools like Microsoft Purview. Zero false positives on known entities because it is exact matching and curated dictionaries, not probabilistic AI.
- AI classification layer for contextual sensitivity where patterns alone cannot reach. Hosted on Azure AI Foundry for scalability and manageability.
- Both layers unified through a common data plane hosted in Azure, integrated with IAM, RBAC, and compliance controls that IT departments can manage and trust.

### 5.2 Why Azure Is the Best-Case Scenario
- Most cost-effective and scalable approach
- Auto-scales, maintains, and is accessible to IT teams to manage directly
- Compliance integration with identity and access management out of the box
- This is the approach that worked at Coherent, and BayOne has tried it the other ways too
- Custom or on-prem deployments are possible and can succeed, but the maturity remains at POC level. They live and breathe and die as prototypes. Azure deployments grow into production systems that the organization owns and operates.
- The same architecture can work on-prem if required, but Azure is definitively the right way to do this for long-term value

### 5.3 What This Means for Lam
- This is not a product. It is a custom solution built on Lam's own Azure environment using proven methodology.
- BayOne builds it, Lam's team can maintain and extend it
- The architecture is designed so that once the first application is solved, expanding to additional applications follows the same pattern with decreasing effort
- Framing: a solution that empowers the team to own and operate the capability, not a dependency on a vendor

### 5.4 Reading the Room: Infrastructure Collaboration
- Azure is the best case, but it requires access to corporate Azure infrastructure
- If the team is funding this independently and operating separately from IT, that shapes the deployment model
- Understanding the collaboration potential with IT early allows us to scope the approach correctly
- We can work with whatever the reality is, but knowing the reality upfront prevents surprises later

---

## Section 6: Continuing the Conversation

- Summarize what was discussed and what was learned
- Identify any remaining gaps
- Propose concrete follow-up actions with owners
- Timeline for BayOne to come back with a scoped proposal based on today's inputs
