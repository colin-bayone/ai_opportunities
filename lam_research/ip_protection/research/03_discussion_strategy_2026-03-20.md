# 03 - Discussion: Strategy and Positioning

**Source:** /lam_research/ip_protection/source/prior_discussion_strategy_2026-03-20.md (and 1 related file)
**Source Date:** 2026-03-20 (Working discussion between Colin Moore and Claude)
**Document Set:** 03 (Prior Working Discussion)
**Pass:** Consolidated strategy and positioning from 2 source documents

---

## Deliverable Structure: Two Separate Documents

### Document 1: Problem Restatement

The first document is a pure listening exercise. It restates Lam's problem using Mikhail's language and structure: the two swim lanes, detection versus redaction, self-help search versus escalation entry, the over-restriction cycle, the feedback loop vision, the infrastructure landscape, and the technical challenge (false positive rates, spelling variations across fab identifiers).

No solutions. No proposals. No technology names. This document exists to pass one specific gate.

**Brad's gate:** "Repeat back to us there's a very clear understanding in what we're trying to solve." This is the explicit credibility test from Set 02. Brad said on the call that they have heard it before from other vendors. If BayOne cannot articulate the problem better than Lam can articulate it themselves, BayOne does not earn the right to propose solutions.

This is the "we've heard it before" test. Passing it requires demonstrating that BayOne absorbed the nuance, not just the headline problem statement.

### Document 2: Preliminary Approach

The second document opens with a brief summary of the problem restatement (a concise reference, not a repeat of Document 1) and then presents specific features and capabilities BayOne would propose:

- Hybrid architecture: deterministic matching where patterns are known, AI-based classification where context matters
- Unified control plane concept
- Ingestion-first philosophy
- Application-by-application migration strategy
- Enterprise tools strategy (Purview, Azure AI Foundry)
- Dashboard and governance visibility

### The Reframe Happens in Document 2, Not Document 1

Document 1 uses Lam's framing. Document 2 corrects the framing from a position of authority, without ever telling Lam they are wrong.

**The technical reality Lam is missing:** Detection is a necessary precondition for redaction. You cannot redact what you have not identified. Redaction is an additional step after detection, not a separate capability. The fact that Mikhail frames these as two separate business cases reveals that Lam has no technical concept of how a detection-action pipeline actually works.

**How Document 2 handles this:** It does not take Lam to school. It does not say "you are wrong." It presents a unified pipeline where detection feeds into action, and Mikhail's "two swim lanes" naturally become two modes of the same system: real-time at ingestion versus batch on historical data. The reframe is implicit in the architecture, not stated as a correction.

### Critical Framing for Document 2

These are explicitly preliminary ideas and planning that would need to be:

1. Refined with Lam (their input on priorities, constraints, specific applications)
2. Refined internally after a true discovery phase with a technical team (the Daniel call and beyond)

This is not a final proposal. It is a starting point for the follow-up meeting where Brad said they would discuss "approaches with trade-offs."

---

## Brad's "Repeat Back" Gate

Brad's gate is the single most important checkpoint in the engagement process. From Set 02, Brad controls the room, redirects speakers, and has been burned by prior vendors. His explicit instruction was for BayOne to demonstrate understanding before proposing anything.

Document 1 satisfies this gate. Document 2 is only earned after Document 1 proves BayOne listened.

The risk of combining both into one document is that it reads as "we heard your problem, and here is our product" -- which is the exact vendor pattern Brad has scar tissue from.

---

## Scope Discipline

### What the Deliverables Focus On

Solely the problem statement within Brad's team:

- Customer IP detection and protection across their document and knowledge systems
- The two use cases Mikhail presented (even though Document 2 reframes the approach)
- The ingestion pipeline, control plane, and historical data cleanup

### What Gets Mentioned Only in Passing

- "This architecture can naturally enable other AI activities once the immediate issue is solved."
- "If that is of interest strategically, we can discuss when the team is ready."
- Stop there. Do not elaborate. Do not list examples. Do not pitch growth.

### Why This Discipline Is Non-Negotiable

Mikhail was dismissive of anything beyond the stated use cases during the discovery call. Brad explicitly said "we don't want to introduce noise in our business case." Colin was redirected on the call for exactly this kind of scope expansion (the IAM tangent that earned Brad's "Is that clear, Colin?").

The future potential is real and massive. Anuj's instinct to "boil the ocean" is correct from a capability standpoint. But the presentation must be laser-focused on what was asked. The proposal must not repeat the mistake from the discovery call.

The rule: earn the right to expand later by delivering on the immediate ask first.

---

## The Dashboard Is a Feature, Not a Differentiator

### What It Actually Covers

The dashboard is not just AI adoption metrics. It encompasses:

- Business value and usage of all tools
- Visibility into which tools to focus on and expand
- A unified interface for requesting new data sources or functionality
- Platform-level governance and audit

### Positioning

The dashboard is a fundamental component of the control plane, not a sales differentiator to lead with. It exists because a unified platform naturally generates this data.

Do not oversell it as a unique BayOne innovation. Frame it as: "Of course you get this, because that is what a properly built platform gives you." Presenting it as a headline feature signals that BayOne does not understand the difference between a feature and a selling point.

---

## IT and Security Stakeholders

### Colin's Operating Position

It does not matter whether IT or security has veto power over Brad's initiative. BayOne will simply work with them. The technical team will make it clear quickly if they are constrained by IT or security decisions.

### Client-Facing Rule

Nothing in a customer-facing document should suggest that Lam is incompetent or that their organizational structure is flawed. This applies across the board:

- Do not question Brad's authority in writing
- Do not suggest their org structure is broken
- Do not imply IT should have been involved from the start
- If IT needs to be brought in, frame it as: "We would welcome the opportunity to collaborate with your IT team to align on infrastructure requirements" -- not "We need to verify whether Brad actually controls this"

This is a diplomatic constraint, not a strategic one. The assessment of Brad's authority and IT's role is internal knowledge (captured in Sets 02 and 02a). The deliverables reflect respect for Lam's organizational decisions as presented.

---

## The "Gen AI Stance" Is a Drastic Overreaction, Not a Principled Position

### What Mikhail Said on the Call

Lam avoided generative AI because of "unstructured output."

### Colin's Assessment

Mikhail is a business user who encountered the term "unstructured output" and does not understand what it means technically. Language models are fully capable of producing structured output (JSON, classification labels, binary decisions). Even unstructured output can be parsed into structured format. The concern is technically nonsensical.

### What Actually Happened at Lam

Lam did not arrive at a principled "we do not want generative AI" stance. What happened was:

1. A poorly executed internal proof of concept without actual AI expertise
2. Results that did not meet expectations (20% false positive rate, which is out-of-the-box baseline performance)
3. A drastic overreaction to those bad results
4. A business-level misattribution of the failure to the technology rather than the implementation

This is the same pattern identified in Set 02 (What Was Tried): the prior approaches were fundamentally wrong, not incrementally improvable.

### How to Handle in the Deliverables

- Do not frame this as "overcoming their Gen AI objections"
- Do not try to convince them generative AI is safe
- Simply present the hybrid approach. The AI components do what they do.
- If someone asks "is this generative AI?", the answer is: "We use the right tool for each part of the problem -- deterministic matching where patterns are known, AI-based classification where context matters."
- Let the results speak. If the system works, no one will object to the underlying technology.

The goal is not to win a philosophical argument about generative AI. The goal is to solve the problem. The technology selection follows from the problem requirements, not from a position paper on AI categories.

---

## The Control Plane Is a Custom Solution, Never a Product

### What It Is

A custom build for Lam, tailored to their environment, their data sources, and their specific needs. This is a consulting engagement: "We will come in, get this set up for you, and we are more than happy to provide long-term support and build off of this."

### What It Is Not

- Not a product sitting in BayOne's back pocket ready to deploy
- Not an out-of-the-box solution
- Not a one-size-fits-all platform
- Not something BayOne already has that magically solves any problem

### Language Discipline

Always call it a "solution," never a "product." The framing is: "A tailor-made solution using the same methodology and blueprint as has been applied at previous customers." Every client's environment is drastically different. The methodology is reusable; the implementation is custom.

Using "product" language triggers the vendor pattern that Brad has scar tissue from. "Product" implies a thing you buy off the shelf. "Solution" implies expertise applied to a specific problem.

### Reusability Is Internal, Not Client-Facing

When Colin architects and builds this, he will build it to be reusable (good engineering practice). But that is an internal BayOne benefit. It is never positioned to the client as "we have a pre-built thing."

The only scenario where this becomes product-like is if Lam wants BayOne to maintain it long-term as a managed service. That is a conversation for later, not for the proposal.

---

## Prior Work as Credibility Without Overpromising

### Engagements to Reference

Colin has built similar architectures for:

- **Coherent Corp** -- massive global enterprise, many teams across finance, engineering, sales, service, manufacturing
- **A retail customer** -- Salesforce-based, completely different stack
- **An Oracle Cloud customer** -- different cloud, different use case

### How to Use These References

Each engagement was custom. The pattern and expertise transfer; the code does not. These references establish that Colin has done this before, in different environments, with different constraints. They do not promise that Lam's solution will be the same as any prior engagement.

The credibility claim is: "We have built unified control planes across diverse enterprise environments." The claim is not: "We have a solution we have deployed three times."

---

## Competitive Positioning Against Accenture

### What We Know from Set 02a

Accenture was the prior partner who failed on the text classification work. The 20% false positive rate, the 17% after fine-tuning, and the 1,000+ hour labeling exercise that was paused -- this is Accenture's work product (or work product from a period when Accenture was involved).

### How to Handle

- Do not name Accenture in any deliverable or proposal
- Do not reference the prior work as a failure by a specific vendor
- Frame the prior approach as a "common but brittle pattern": applying generic Named Entity Recognition (NER) to a domain-specific problem where the entities (semiconductor customer names, fab identifiers, process parameters) are not in any model's training data
- Position BayOne's approach as starting from the domain, not from the model. The distinction is: "We build the detection strategy around your specific data, not around a pre-trained model's capabilities."

This frames the failure as methodological (the approach was wrong) rather than vendor-specific (Accenture was incompetent). It is more credible, less petty, and less likely to trigger defensiveness from anyone at Lam who was involved in selecting or managing the prior engagement.

---

## Agentic AI: Solve the Use Case, Do Not Upsell

### Current Positioning

Agentic AI is one part of a potential solution for the specific use case at hand. It is not:

- A growth platform pitch
- A "this can expand to other initiatives" lead
- A reason to sound like BayOne is pursuing more than what was asked

### Why This Constraint Exists

Mikhail was dismissive in the transcript about anything beyond the two use cases. He actively redirected Colin when the scope expanded. Pitching "growth potential" and "agentic AI platform" will trigger the exact pushback that occurred on the discovery call.

### What BayOne Can Say

- A minor point, almost in passing: "This architecture can naturally expand to other initiatives once this immediate problem is solved."
- Nothing more. The proposal focuses on their stated problem.
- Provide examples in passing to Lam of what is possible, but do not make it a section or a selling point.

The word "agentic" does not need to appear in any client-facing material. If the architecture includes agentic components, they are described by what they do ("automated classification and routing," "continuous monitoring and escalation"), not by what category of AI they belong to.

---

## Summary of Positioning Rules

These rules emerge from the discovery call dynamics (Set 02), the internal debrief (Set 02a), and the strategy discussion captured here:

1. **Earn the right to propose.** Document 1 (problem restatement) must pass Brad's gate before Document 2 (approach) is credible.
2. **Stay in scope.** Only address the two stated use cases. Expansion is mentioned once, in passing, with no elaboration.
3. **Solution, not product.** Every reference to what BayOne will build uses solution language. The control plane is custom for Lam, not a pre-built platform.
4. **Do not fight the Gen AI stance.** Present the hybrid approach. Let results speak. Do not try to convince anyone that generative AI is safe.
5. **Do not name competitors.** Frame prior failed approaches as a common methodological pattern, not a vendor failure.
6. **Respect organizational authority in writing.** Internal assessments of Brad's control, IT's role, and Mikhail's technical depth stay internal. Deliverables reflect respect for Lam's decisions as presented.
7. **Dashboard is table stakes.** It is a natural feature of a properly built platform, not a selling point.
8. **Prior work is credibility, not a promise.** Methodology transfers, implementations do not.
9. **Agentic AI solves the problem at hand.** It is not a growth pitch. The word "agentic" may not need to appear at all.
10. **Preliminary framing.** Document 2 is explicitly a starting point for discussion, not a final proposal. It requires refinement with Lam and a true discovery phase.