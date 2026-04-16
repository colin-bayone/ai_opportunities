# 03 - Discussion: Strategy & Deliverables

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)
**Context:** Final round of Q&A -- positioning, client management, and deliverable structure

---

## 1. The Dashboard Is a Feature, Not a Differentiator

### What It Covers
Not just AI adoption metrics, but:
- Business value and usage of all tools
- Which tools to focus on and expand
- A unified place for people to request new data sources or functionality
- "Sky's the limit" -- this is a platform feature, not a bolt-on

### Positioning
This is a **fundamental component** of the control plane, not a sales differentiator to lead with. It exists because a unified platform naturally generates this data. Don't oversell it as a unique BayOne innovation -- frame it as "of course you get this, because that's what a properly built platform gives you."

---

## 2. IT/Security Stakeholders: Practical, Not Political

### Colin's Position
It doesn't really matter if IT or security has veto power. We'll just work with them. The technical team will tell us pretty quickly if they're hamstrung.

### Client-Facing Rule
**Do NOT put anything in a customer-facing document that would suggest Lam is incompetent.** This applies across the board:
- Don't question Brad's authority in writing
- Don't suggest their org structure is broken
- Don't imply IT should have been involved from the start
- If IT needs to be brought in, frame it as "we'd love to collaborate with your IT team to align on infrastructure" -- not "we need to verify whether Brad actually controls this"

---

## 3. Agentic AI: Solve the Use Case, Don't Upsell

### Current Positioning
Agentic AI is one part of a potential solution for the specific use case at hand. It is NOT:
- A growth platform pitch
- A "this can expand to other initiatives" lead
- A reason to sound like we're going for more than what was asked

### Why This Matters
Mikhail was fairly dismissive in the transcript about anything beyond the two use cases. He actively redirected Colin when the scope expanded. Pitching "growth potential" and "agentic AI platform" will trigger the exact pushback we saw on the call.

### What We Can Say
- A very minor point, almost in passing: "this architecture can naturally expand to other initiatives once this immediate problem is solved"
- Nothing more. The proposal focuses on their stated problem. Period.
- Provide examples in passing to Lam of what's possible, but do not make it a section or a selling point

---

## 4. The "Gen AI Stance" Is Not Real

### What Mikhail Actually Said
Mikhail said they avoided generative AI because of "unstructured output." Colin's assessment: Mikhail is a business user who came across the term "unstructured output" and does not understand what it means.

### The Reality
- Language models are fully capable of giving structured output (JSON, classification labels, binary decisions)
- Even if output is unstructured, it can always be parsed into structured format
- The concern is "completely nonsensical" from a technical standpoint

### What Actually Happened
Lam did NOT have a principled "we don't want gen AI" stance. They had:
1. A poorly executed internal POC without actual AI expertise
2. Results that didn't meet expectations (20% false positive = out-of-the-box baseline)
3. A drastic overreaction to those bad results
4. A business-level misattribution of the failure to the technology rather than the implementation

### How to Handle in the Proposal
- Do NOT frame this as "overcoming their Gen AI objections"
- Do NOT try to convince them Gen AI is safe
- Simply present the hybrid approach. The AI components do what they do. If someone asks "is this generative AI?", the answer is "we use the right tool for each part of the problem -- deterministic matching where patterns are known, AI-based classification where context matters"
- Let the results speak. If the system works, no one will object to the underlying technology.

---

## 5. Deliverable Structure: Two Separate Documents

### Document 1: Problem Restatement
- Demonstrates that BayOne listened and understood
- This is Brad's explicit gate: "repeat back to us there's a very clear understanding in what we're trying to solve"
- Should cover: the two use cases, the over-restriction problem, the feedback loop vision, the technical challenge (false positive rates, spelling variations), and the infrastructure landscape
- Pure problem articulation. No solutions. No proposals. No technology names.
- This satisfies the "we've heard it before" test. If we can articulate their problem better than they can, we've earned the right to propose solutions.

### Document 2: Preliminary Approach
- Includes a brief summary of the problem restatement (not a repeat -- a concise reference)
- Then: specific features and capabilities we would propose
- Hybrid architecture: deterministic + AI layers
- Unified control plane concept
- Ingestion-first philosophy
- Application-by-application migration strategy
- Enterprise tools strategy (Purview, Azure AI Foundry)
- Dashboard and governance visibility

### Critical Framing for Document 2
These are explicitly **preliminary ideas and planning** that would need to be:
1. Refined with Lam (their input on priorities, constraints, specific applications)
2. Refined internally after a true discovery phase with a technical team (the Daniel call and beyond)

This is NOT a final proposal. It's a starting point for the follow-up meeting where Brad said they'd discuss "approaches with trade-offs."
