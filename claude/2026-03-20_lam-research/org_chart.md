# Lam Research Engagement - Org Chart

**Last Updated:** 2026-03-20 (from document set 02a - internal debrief)

This is a living document. It always reflects the most current understanding of all people involved in this engagement. For historical tracking of when information was learned, see the per-set people documents in `research/`.

---

## Lam Research

### Bradley Estes ("Brad")
- **Title:** Managing Director, Knowledge & Advanced Services
- **Role in Engagement:** Primary point of contact, decision maker, room controller
- **Ownership:** Owns the entire vertical end-to-end: business case, product definition, ideation, execution. Has business, program, product, and technical functions under him.
- **Background:** Progressed from Product Support Manager to Senior Director of Knowledge Management
- **Focus:** Knowledge governance, information governance, product support
- **Sentiment:** Controlled, deliberate, structured. Keeps meetings focused. Pushes back diplomatically but directly when boundaries are crossed ("Is that clear, Colin?"). Has been burned by vendors before ("we've heard it before"). Not interested in being sold to -- demands demonstrated understanding before solutions. Values clarity, incrementalism, speed of iteration. Technology agnostic.
- **Key Quote:** "We don't want to have the discussion right now about, oh, I've got a technology solution that can solve that. We want a very, because we've heard it before, we want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve."
- **Working Style:** Will NOT write user stories himself. Assigns team members. Previous "pod" model was a pilot, not standard. Expects structured engagement with his team handling requirements.
- **Known Since:** Set 01 (call prep), significantly deepened in Set 02 (meeting)

### Mikhail Krivenko
- **Title:** Head of Product (in Brad's organization)
- **Role in Engagement:** Technical problem presenter, scope guardian, product lead
- **Responsibilities:** Product management, IT design, product order -- both ideation and execution
- **Sentiment:** Pragmatic, detail-oriented, methodical. Framework-first communicator. Remarkably honest about knowledge limits ("I don't know what that even means"). Firm on scope boundaries. Very clear on the detection vs. redaction distinction. Focused on outcomes, not technology names. Comfortable correcting both BayOne and Brad when needed.
- **Key Quote:** "20% is absolutely unacceptable number, right? We can't live with that."
- **Relationship to Brad:** Functions as a unit with Brad but in distinct roles. Brad sets rules and guards boundaries; Mikhail delivers substance. Defers to Brad on organizational questions but leads the technical presentation independently.
- **Known Since:** Set 01 (call prep), significantly deepened in Set 02 (meeting)

### Daniel (last name unknown)
- **Title:** Technical Lead (in Brad's organization)
- **Role in Engagement:** Technical counterpart to Mikhail. Not present in discovery call, confirmed for follow-up meeting.
- **Org Structure:** "Daniel, program. Me [Mikhail], product." Together they form scrum teams with Brad's business function.
- **Sentiment:** Not yet met directly.
- **Significance:** Gatekeeper to technical depth. Brad and Mikhail handle business/product framing; technical deep dives require Daniel.
- **Known Since:** Set 01 (call prep), confirmed in Set 02 (meeting)

### Christian (last name unknown)
- **Title:** Unknown (part of Brad's team)
- **Role in Engagement:** Not present on the call. Owns a specific slide/document Mikhail was looking for at the start.
- **Known Since:** Set 02 (meeting, mentioned only)

### Monica (last name unknown)
- **Title:** Unknown (part of Brad's broader team)
- **Role in Engagement:** Not on this call. Brad referenced: "you only met three people, but you know, Monica was blessed."
- **Known Since:** Set 02 (meeting, mentioned only)

### Jason Callahan
- **Title:** CISO
- **Role in Engagement:** Not directly involved. His public security posture shapes Lam's culture.
- **Public Quote:** "We are operating from the zero-trust point of view. But we all share intellectual property. Fundamentally, we as security people don't trust encryption."
- **Sentiment:** Security-sophisticated, zero-trust philosophy
- **Known Since:** Set 01 (call prep, public reference only)

---

## BayOne Solutions

### Colin Moore
- **Title:** Director of AI (introduced himself as "head of AI")
- **Role in Engagement:** Technical lead
- **Relevant Experience:** Coherent Corp (same semiconductor equipment industry), defense primes (Raytheon, Northrop Grumman), AI governance for 40K+ users, detection/redaction systems, shadow AI programs, ITAR/CMMC/DFARS/NIST 800-171
- **Meeting Performance:** Strongest moment was the 20%/ChatGPT diagnosis ("that's pretty much out-of-the-box ChatGPT"). Unified control plane concept also landed well. Got redirected once by Brad/Mikhail when veering into IAM territory. Tendency toward verbosity and solution-drift, but recovered well after redirection.
- **Known Since:** Set 01

### Anuj Sehgal
- **Title:** VP of Sales
- **Role in Engagement:** Senior sales lead for the Lam opportunity. Drives commercial strategy, relationship management, deal progression. Not on the discovery call but debriefed immediately after.
- **Style:** High-energy, strategically sharp, blunt internally but measured externally. Controls the tempo of the sales process. Assigns action items, manages travel logistics, sequences next steps. Land-and-expand thinker.
- **Relationship to Zahra:** Appears senior to her. Makes strategic deal decisions. Zahra handled initial connection; Anuj quarterbacking the opportunity.
- **Key insight:** Sees Lam as a massive embed opportunity modeled after what Deloitte/Capgemini have done there for years. Knows the competitive landscape.
- **Known Since:** Set 02a (internal debrief)

### Pratik Sharda / "Pat" (possibly "Pradeep" in speech-to-text)
- **Title:** Unknown
- **Role in Engagement:** Team member. Active participant on the call. Asked questions about ingestion, identity management, scaling approaches. Designated as follow-up contact for extracting specifics from Lam.
- **Meeting Performance:** Colin: "Pat was awesome, this meeting." Concise, normalizing contributions. Almost over-talked at one point but self-corrected. Made one factual error about tool maturity (Colin flagged for coaching). Trusted execution partner.
- **Note:** "Pradeep" in the debrief transcript is most likely a speech-to-text artifact for "Pratik." The conversational flow treats "email Pat" and "ask Pradeep" as the same instruction.
- **Known Since:** Set 01, active participation confirmed in Set 02, reviewed in Set 02a

### Surej KP
- **Title:** Unknown
- **Role in Engagement:** Team member. May have been present but did not speak or was not attributed in transcript.
- **Known Since:** Set 01

### Amit Grover
- **Title:** Delivery
- **Role in Engagement:** Delivery lead. May have been present but did not speak or was not attributed in transcript.
- **Known Since:** Set 01

### Zahra
- **Title:** Sales
- **Role in Engagement:** Initial connection/sales. Not present on the discovery call.
- **Note:** Friction noted around communication and scheduling for this opportunity. Raised internally.
- **Known Since:** Prior context (opportunity catalog)

---

## Relationship Map

- **Brad controls everything.** Single decision-maker with full ownership of business, product, program, and technical. No cross-org approvals needed for initial work. Matrix dependencies exist for systems his org doesn't own, but initial scope is within his domain.
- **Brad -> Mikhail -> Daniel** is the chain. Brad sets rules, Mikhail delivers substance, Daniel handles technical depth. They assemble scrum teams across these three functions.
- **Brad has been burned before.** Previous vendor/consultant experiences left scar tissue. He explicitly tests whether BayOne can "repeat back" the problem before allowing solution discussion. This is the gate.
- **The org is self-contained** for initial scope. Complexity comes later when branching to systems they don't own.
- **Anuj is the deal driver.** VP of Sales, quarterbacking the commercial strategy. He controls the sales tempo and sequences Colin's technical work with client-facing milestones. Zahra handled the initial connection; Anuj owns the deal now.
- **BayOne sales friction** with Zahra around communication/scheduling is a background issue, separate from the technical engagement.
- **Competitive landscape:** Deloitte and Capgemini are long-term embedded incumbents at Lam. Accenture was the prior partner who attempted the text classification work and failed. BayOne's model is to replicate the embed-and-expand approach with superior technical delivery.
- **Next engagement point:** Follow-up meeting with Daniel, broader Lam team, and potentially more BayOne technical staff. BayOne presents approaches with trade-offs. Gated by whether Lam provides tool specifics in response to Pat's follow-up email.
