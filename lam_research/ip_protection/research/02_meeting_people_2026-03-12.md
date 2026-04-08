# 02 - Meeting: People

**Source:** /lam_research/ip_protection/source/lam_discovery_call_2026-03-12.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** People identification and dynamics

---

## Present on the Call

### Bradley Estes ("Brad")
- **Title:** Managing Director, Knowledge and Advanced Services (from Set 01)
- **Role on This Call:** Room controller, boundary setter, decision maker
- **What He Owns:** "I own the entire thing. I am the business case, the product definition, the ideation, and the execution." Has business, program, product, and technical functions under him.
- **Behavior Observed:**
  - Set the call format and enforced it: Lam presents, then Q&A
  - Explicitly demanded understanding before solutions: "We don't want to have the discussion right now about, oh, I've got a technology solution that can solve that... we've heard it before."
  - Redirected Colin when he veered into IAM territory: "I don't think that's like, that is a separate use case... I just want to caution against that." Then directly: "Is that clear, Colin?"
  - Values incrementalism: "we want to start small and prove incrementally"
  - Technology agnostic: "I know AI is a very sexy word, but it's also a meaningless word... not married to any specific AI technologies"
  - Provided context on org scope: "you only met three people, but you know, Monica was blessed"
  - Clear about engagement model: "it's not gonna be me like writing user stories requirements. I'm gonna have somebody as part of my team... that was a pilot, that was the only reason. That's not a standard mode of operation."
- **Sentiment:** Controlled, deliberate, structured. Has been burned by vendors before. Not interested in being sold to. Tests whether BayOne can repeat back the problem before allowing solution discussion.

### Mikhail Krivenko
- **Title:** Head of Product (in Brad's organization)
- **Role on This Call:** Technical problem presenter, scope guardian
- **What He Does:** "I'm a head of product in Brad's organization. So on the product management, I do IT design and the product order. So both ideation and execution part of the process."
- **Behavior Observed:**
  - Led the entire whiteboard problem presentation independently
  - Remarkably honest about knowledge limits: "You're not talking to a technical audience here" and "I don't know what that even means" (re: Azure AI Foundry)
  - Very precise on the detection vs. redaction distinction: clearly separated the two business cases and their different requirements
  - Firm on scope boundaries: corrected Pat/Colin when discussion drifted
  - Named specific models tried: Transformers, SpaCy, Azure AI model
  - Provided the 20% false positive rate data and the fine-tuning result (down to 17%)
  - Described the 1,000+ hour labeling exercise that was paused
  - Explained why GenAI was not tried: "unstructured output" concern
- **Sentiment:** Pragmatic, detail-oriented, methodical. Framework-first communicator. Comfortable correcting both BayOne team and Brad when needed.

### Pratik Sharda / "Pat"
- **Role on This Call:** Active participant, asked questions about ingestion, identity management, scaling
- **Behavior Observed:**
  - Asked about data lake and ingestion patterns
  - Raised identity and access management as relevant to the problem
  - Made comments about the general AI ecosystem (guardrails not tested for production, etc.)
  - Contributed to the technical discussion on detection approaches
  - Colin's assessment from debrief: "Pat was awesome, this meeting"
- **Note:** Likely the same person as "Pradeep" in the debrief transcript (speech-to-text artifact)

### Colin Moore (BayOne)
- **Title:** Introduced himself as "head of AI here at Bay One"
- **Role on This Call:** Technical lead
- **Behavior Observed:**
  - Strong opening: connected Coherent experience (same semiconductor industry) to Lam's problem
  - Strongest moment: diagnosing 20% false positive rate as "pretty much out-of-the-box ChatGPT" which landed well
  - Unified control plane concept resonated: "there has to be commonality between these applications"
  - Got redirected by Brad/Mikhail when veering into IAM territory (Brad: "Is that clear, Colin?")
  - Showed knowledge of ITAR/CMMC/DFARS regulatory environment
  - Tendency toward verbosity and solution-drift, but recovered after redirection

### Not Present But Referenced

- **Daniel** - Technical Lead in Brad's org. "Daniel, program. Me [Mikhail], product." Confirmed for the follow-up meeting.
- **Christian** - Owns a specific slide/document Mikhail was looking for at the start of the call.
- **Monica** - Part of Brad's broader team. Brad referenced: "you only met three people, but you know, Monica was blessed."

## Org Structure Revealed

Brad -> Mikhail (product) -> Daniel (program/technical). Together they form scrum teams. Brad owns the entire vertical end-to-end. No cross-org approvals needed for initial work. Matrix dependencies exist for systems they do not own, but initial scope is within Brad's domain.
