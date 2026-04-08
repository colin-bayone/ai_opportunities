# 05 - Meeting: People

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** People identification and dynamics

---

## Present on the Call

### Daniel Harrison (Lam Research) - First Meeting with Colin
- **Title:** Director of Engineering, GFSO area
- **Scope:** Covers all products that Mikhail manages on the product side, except services
- **Background:** Software development for approximately 30 years. Test automation, QA, software architecture. Every role on software development teams except UX.
- **Self-described role today:** "I'm more on the information gathering side today as opposed to being in contribution, just unless I see anything egregious."
- **Actual contribution:** Pushed hard on disconnected/air-gapped/edge AI environments. Raised clean room and customer fab environments as future scope. Concerned about Small Language Model (SLM) parity with LLMs for future disconnected deployments. Referenced MABC project and E10 data extraction.
- **Key dynamic:** Daniel did NOT drive the prior ML work discussion. That was Mikhail. Daniel's expertise is software engineering, not AI/ML. Pat's pre-call assessment ("I don't have a lot of high hopes for Daniel's AI knowledge") was accurate.
- **Relationship to Mikhail:** "Everything that Mikhail is product managing, basically." Engineering counterpart to Mikhail's product function. They are the two halves of Brad's technical organization.
- **Notable moment:** When Colin asked about the air-gapped question, Daniel pushed back constructively: "If we're not bringing it up as, hey, this is where we see ourselves five, 10 years from now..." He wants architectural compatibility even if it is not in scope for the POC.

### Mikhail Krivenko (Lam Research)
- **Revealed as the actual technical driver of the prior work.** Not Daniel. Mikhail drove the model selection, testing, and evaluation.
- **Technically more knowledgeable than Set 02a debrief suggested.** He named Presidio models, described the 12-to-5-to-3 model selection process, explained the reconciliation algorithm, and described the on-prem Kubernetes deployment. He is not a data scientist, but he is far more technically engaged than "not technical" (the debrief's characterization).
- **Key moment:** When Colin described the layered architecture, Mikhail immediately recognized: "So we just basically accidentally picked literally every single thing, one of each." This was self-aware and showed he understood the problem with their approach once it was explained.

### Bradley Estes (Lam Research)
- **Role this meeting:** Less dominant than the first meeting. Let Mikhail and Daniel drive more of the technical discussion. Intervened on scope boundaries (clean room/air-gap is future, not now) and time management (hard stop at 2:30).
- **Key directive:** "Focus on the cloud for the primary use case, but discussions in future thinking about how to achieve parity between those air-gapped files as well."
- **Action requested:** Remove customer names from all BayOne documents. "If these documents go broader, which they probably will at some point, we want to redact any specific customer names out of it."

### Colin Moore (BayOne)
- **Performance this meeting:** Strong. Covered the problem restatement cleanly, extracted the application name (Escalation Solver), got detailed prior work context from Mikhail, presented the layered architecture credibly, and handled Daniel's edge AI questions without overcommitting.
- **Best moment:** The golden set / ground truth explanation. Brad asked for more technical detail on what "known good" and "known bad" means. Colin's explanation (giraffe vs. car analogy, three tiers of labeling, EDA for sample size) was clear and landed well.
- **Time pressure:** Had to speed through the architecture section when Brad called the 2:30 hard stop. Did not get to cover the Azure section in detail on screen.

### Pratik/Pat (BayOne)
- **In person.** Backed Colin up as planned. Asked follow-up questions on model selection criteria and pushed for clarity on the POC target confirmation.
- **Performed his wingman role.** When Colin's questions got general, Pat rephrased for specificity.

### Anuj Sehgal (BayOne)
- **In person.** Minimal speaking in the transcript. Observing the room dynamics.

### Amit Grover (BayOne)
- **In person.** Contributed context about benchmarking changes and model training approaches. Highlighted that Colin's team has internal tools and competency in this space.

### Not Present But Referenced
- **Orion** - Small team member working on a "supercritical project" (COS). Some data access for the POC will require Orion's attention. Mikhail flagged this as a potential dependency.
- **Renee** - Organized the meeting on Brad's behalf.
