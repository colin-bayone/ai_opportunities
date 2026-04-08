# Lam Research IP Protection - Org Chart

**Last Updated:** 2026-04-06 (from document sets 01, 02, 02a, 03, 04, 04a, 05, 05a)

This is a living document. It always reflects the most current understanding of all people involved in this engagement. For historical tracking of when information was learned, see the per-set people documents in research/.

---

## Lam Research

### Bradley Estes ("Brad")
- **Title:** Managing Director, Knowledge and Advanced Services
- **Role in Engagement:** Primary point of contact, decision maker, room controller
- **Ownership:** Owns the entire vertical end-to-end: business case, product definition, ideation, execution. Has business, program, product, and technical functions under him. No cross-org approvals needed for initial scope.
- **Background:** Progressed from Product Support Manager to Senior Director of Knowledge Management
- **Focus:** Knowledge governance, information governance, product support
- **Sentiment:** Controlled, deliberate, structured. Keeps meetings focused. Pushes back diplomatically but directly when boundaries are crossed ("Is that clear, Colin?"). Has been burned by vendors before ("we've heard it before"). Not interested in being sold to. Demands demonstrated understanding before solutions. Values clarity, incrementalism, speed of iteration. Technology agnostic.
- **Key Quote:** "We don't want to have the discussion right now about, oh, I've got a technology solution that can solve that. We want a very, because we've heard it before, we want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve."
- **Working Style:** Will NOT write user stories himself. Assigns team members. Previous "pod" model was a pilot, not standard operating mode. Expects structured engagement with his team handling requirements.
- **Known Since:** Set 01 (call prep), significantly deepened in Set 02 (meeting), assessed in Set 02a (debrief)

### Mikhail Krivenko
- **Title:** Head of Product (in Brad's organization)
- **Role in Engagement:** Technical problem presenter, scope guardian, product lead
- **Responsibilities:** Product management, IT design, product order, both ideation and execution
- **Sentiment:** Pragmatic, detail-oriented, methodical. Framework-first communicator. Remarkably honest about knowledge limits ("I don't know what that even means"). Firm on scope boundaries. Focused on outcomes, not technology names. Comfortable correcting both BayOne and Brad when needed.
- **Key Quote:** "So we just basically accidentally picked literally every single thing, one of each." (Set 05, recognizing the prior approach was fundamentally unsound)
- **Set 05 Development:** Revealed as the actual technical driver of the prior ML work (not Daniel). Named Presidio models, described the 12-to-5-to-3 model selection, explained the reconciliation algorithm, described the on-prem Kubernetes deployment. Had a genuine recognition moment where he understood the prior approaches were fundamentally wrong. Engaged substantively on the labeling discussion. Credibility was gained with him. He is the person on the Lam side who will understand and champion the approach.
- **Relationship to Brad:** Functions as a unit with Brad but in distinct roles. Brad sets rules and guards boundaries; Mikhail delivers substance. Defers to Brad on organizational questions but leads the technical presentation independently.
- **Known Since:** Set 01 (call prep), significantly deepened in Set 02 (meeting), credibility milestone in Set 05

### Daniel Harrison
- **Title:** Director of Engineering, GFSO area
- **Role in Engagement:** Engineering counterpart to Mikhail. Covers all products Mikhail manages on the product side, except services.
- **Org Structure:** "Daniel, program. Me [Mikhail], product." Together they form scrum teams with Brad's business function.
- **Experience:** Approximately 30 years in software development. Test automation, QA, software architecture. Every role on development teams except UX. Approximately 10 years at Lam Research.
- **Current Work:** Working with BayOne's Philippines team on knowledge management engagement. .NET stack.
- **Set 05 Performance:** Self-described as "more on the information gathering side." Primary contribution was pushing on disconnected/air-gapped/edge AI environments for customer fabs. Did not drive or contribute to the prior ML work discussion. Appears to not understand model hosting or the distinction between model architecture and deployment topology. The least useful and least clear participant on the April 6 call.
- **Assessment:** Daniel is a software engineering leader, not an AI/ML resource. Communication with his team should be calibrated accordingly. His edge AI concerns are legitimate for future phases but were premature and distracting in the POC scoping context.
- **Known Since:** Set 01 (call prep), confirmed Set 02, background Set 04, first met Set 05

### Christian (last name unknown)
- **Title:** Unknown (part of Brad's team)
- **Role in Engagement:** Not present on the call. Owns a specific slide/document Mikhail was looking for at the start.
- **Known Since:** Set 02 (meeting, mentioned only)

### Monica (last name unknown)
- **Title:** Unknown (part of Brad's broader team)
- **Role in Engagement:** Not on the discovery call. Brad referenced: "you only met three people, but you know, Monica was blessed."
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
- **Role in Engagement:** Technical lead, solution architect
- **Relevant Experience:** Coherent Corp (same semiconductor equipment industry), defense primes (Raytheon, Northrop Grumman), AI governance for 40,000+ users, detection/redaction systems, shadow AI programs, ITAR/CMMC/DFARS/NIST 800-171
- **Meeting Performance:** Strongest moment was the 20%/ChatGPT diagnosis ("that's pretty much out-of-the-box ChatGPT"). Unified control plane concept also landed well. Got redirected once by Brad/Mikhail when veering into IAM territory. Tendency toward verbosity and solution-drift, but recovered well after redirection.
- **Technical Vision (from Set 03):** Hybrid deterministic + AI architecture, ingestion-first philosophy, unified control plane, application-by-application migration
- **Known Since:** Set 01

### Anuj Sehgal
- **Title:** VP of Sales
- **Role in Engagement:** Senior sales lead, deal driver. Not on the discovery call but debriefed immediately after. Controls the commercial strategy and sales tempo.
- **Style:** High-energy, strategically sharp, blunt internally but measured externally. Land-and-expand thinker.
- **Strategy:** Sees Lam as a massive embed opportunity modeled after Deloitte/Capgemini's long-term presence. "Start small, embed, scale."
- **Relationship to Zahra:** Appears senior to her. Zahra handled initial connection; Anuj quarterbacking the opportunity.
- **Known Since:** Set 02a (internal debrief)

### Pratik Sharda / "Pat" (also "Pradeep" in speech-to-text)
- **Title:** Unknown (functions as account lead / senior consultant for Lam)
- **Role in Engagement:** Colin's in-room proxy and tactical wingman. Declared: "My ultimate customer is not Brad or Mikhail or Daniel today, it's you [Colin]." Backs Colin up when answers get vague. Multi-year relationship with Brad's team (CSBG). Deep knowledge of Lam internal politics (CSBG vs. GIS split).
- **Meeting Performance:** "Pat was awesome, this meeting" (Set 02). Continues to be the person who pushes Lam for specifics when they stay general.
- **Strategic Value:** Understands the CSBG/GIS political landscape, Brad's direct funding model, and the new CIO's vendor rationalization. This context is not available from any other BayOne team member.
- **Known Since:** Set 01, active participation confirmed Set 02, reviewed Set 02a, strategic role clarified Set 04a

### Surej KP
- **Title:** Unknown
- **Role in Engagement:** Team member. May have been present but did not speak or was not attributed in transcript.
- **Known Since:** Set 01

### Amit Grover
- **Title:** Delivery Lead
- **Role in Engagement:** Delivery management, operational bridge to current Lam-BayOne engagement (Philippines team). First substantive participation in Set 04.
- **Value to Engagement:** Has direct working knowledge of Daniel Harrison and Lam's current technical environment from the existing Philippines team engagement. Provides operational intelligence that a cold vendor would not have.
- **Set 04 Contributions:** Provided intel on Daniel's background, flagged .NET stack and Test Complete exploration, questioned the 1,000-hour labeling estimate's realism, received the costing workbook for scenario modeling.
- **Known Since:** Set 01 (listed), active participation in Set 04 (internal prep)

### Zahra
- **Title:** Sales
- **Role in Engagement:** Initial connection/sales. Not present on the discovery call.
- **Note:** Friction noted around communication and scheduling. Raised internally.
- **Known Since:** Prior context (opportunity catalog)

---

## Relationship Map

- **Brad controls everything.** Single decision-maker with full ownership of business, product, program, and technical. No cross-org approvals needed for initial work. Matrix dependencies exist for systems his org does not own, but initial scope is within his domain.
- **Brad -> Mikhail -> Daniel** is the chain. Brad sets rules, Mikhail delivers substance, Daniel handles technical depth. They assemble scrum teams across these three functions.
- **Brad has been burned before.** Previous vendor/consultant experiences (likely including Accenture/Capgemini) left scar tissue. He explicitly tests whether BayOne can "repeat back" the problem before allowing solution discussion. This is the gate.
- **The org is self-contained** for initial scope. Complexity comes later when branching to systems they do not own.
- **Anuj is the deal driver.** VP of Sales, quarterbacking the commercial strategy. He controls the sales tempo and sequences Colin's technical work with client-facing milestones.
- **BayOne sales friction** with Zahra around communication/scheduling is a background issue, separate from the technical engagement.
- **Competitive landscape:** Deloitte and Capgemini are long-term embedded incumbents at Lam. Accenture was the prior partner who attempted the text classification work and failed. BayOne's model is to replicate the embed-and-expand approach with superior technical delivery.
- **Next engagement point:** Proposal delivery by Friday April 10, 2026. Brad reviews following week, decision by approximately April 17. SOW/legal approximately one week. POC on Escalation Solver approximately two weeks from data access. Orion dependency for some data access (critical COS project). Brad requested customer name redaction from all BayOne documents.
