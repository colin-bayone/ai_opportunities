# EPNM-to-EMS UI Conversion - Org Chart

**Last Updated:** 2026-03-26 (from document set 01)

---

## Cisco Systems

### Guhan
- **Title:** VP-level leader (exact title not stated)
- **Role in Engagement:** Primary decision-maker and sponsor for the EPNM-to-EMS UI conversion initiative. Set the strategic direction, timeline, and expectations.
- **Ownership:** Owns the decision to pursue this conversion. Has authority over timeline (set 4-week target) and team allocation. Will use POC output to justify additional resources internally.
- **Background:** Leads the product line that includes both EPNM and EMS. Manages the customer relationship pressure driving this initiative.
- **Sentiment:** Positive, engaged, action-oriented. Wants this to succeed because it directly addresses customer business impact. Asked the most probing technical question on the March 25 call (domain/functionality gaps). Not skeptical of BayOne's approach but wants assurance of completeness.
- **Key Quote (paraphrased):** "We need to move all the customers from EPNM into EMS. The old UI needs to exist."
- **Working Style:** Sets the frame, delegates execution. Expects independent work with periodic checkpoints. Will provide support (licenses, access) but not hand-holding.
- **Known Since:** Set 01 (March 25, 2026 meeting; also present on Feb 9 and Feb 20 calls per prior session materials)

### Selva (Selvan / Srinivas)
- **Title:** Senior Engineering Manager or equivalent
- **Role in Engagement:** Technical and operational lead on the Cisco side. Provides specificity on what has/hasn't been ported, team availability, and technical constraints.
- **Ownership:** Owns the engineering team doing EMS platform work. Determines which functionality is missing and which screens to prioritize. Controls team bandwidth allocation.
- **Background:** Deeply familiar with both EPNM and EMS codebases. Led or participated in prior porting efforts where some screens were brought to EMS with new UX.
- **Sentiment:** Practical, solution-oriented. Not effusive but constructive. Focused on maximizing the value of the exercise by targeting missing functionality rather than re-doing existing work.
- **Key Quote (paraphrased):** "If something was not brought in the front-end, the corresponding back-end is also not working. It's vertical."
- **Working Style:** Adds precision after Guhan sets direction. Expects Colin to work independently after context is provided. Made it clear the team is on critical work and cannot dedicate significant time.
- **Known Since:** Set 01 (March 25, 2026 meeting; also present on Feb 9 and Feb 20 calls per prior session materials)

### Cisco Engineering Team (not yet identified individually)
- **Role:** Will provide context on specific screens and functionality. Will identify candidate screens for conversion.
- **Availability:** On critical platform work. Can provide context but cannot invest significant time.
- **Significance:** Colin will need navigational help from this team ("who to ask for what"). Initial conversations expected before hardware arrives.
- **Known Since:** Set 01 (referenced by Guhan and Selva on March 25 call)

---

## BayOne Solutions

### Colin Moore
- **Title:** Director of AI
- **Role in Engagement:** Technical lead and primary executor for the POC. Will do hands-on coding, analysis, and delivery. Solo for the POC phase, with team ready for scaled engagement.
- **Relevant Experience:** Has executed similar conversions across technology stacks (C# to Rust, Spring to Go, thick-client to web). Built the Claude Code + LangGraph agent swarm methodology used for this engagement.
- **Meeting Performance (March 25):** Well-prepared with proposal pre-written before the call. Many of his prepared questions were answered by Guhan's opening, which he noted and pivoted from smoothly. Presented the methodology confidently using accessible analogies. Committed to Cisco security requirements without hesitation. Positioned the POC as an investment.
- **Known Since:** Set 01

### Additional BayOne Participant (likely Rahul)
- **Title:** President (if Rahul) or team member
- **Role in Engagement:** Logistical support. Committed to expediting hardware delivery timeline.
- **Meeting Performance (March 25):** Brief interjection near end of call. Supportive and action-oriented regarding hardware timeline.
- **Known Since:** Set 01

### BayOne Offshore Team (not yet individually identified)
- **Role:** Ready for beyond-POC engagement. All have signed NDAs and will receive Cisco hardware.
- **Significance:** Colin mentioned this proactively to build confidence that scaling up is ready when needed.
- **Known Since:** Set 01

---

## Related Cisco Stakeholders (Not on This Call)

### Anand
- **Title:** Director (Cisco)
- **Role:** Leads the CI/CD engagement that BayOne is already working on. Colin is already onboarded through Anand's team.
- **Significance:** The existing CI/CD relationship provides the security/NDA foundation that this engagement builds on.
- **Known Since:** Prior engagement context (CLAUDE.md)

### Arun
- **Title:** VP (Cisco)
- **Role:** Senior leadership over the broader initiative.
- **Known Since:** Prior engagement context (CLAUDE.md)

---

## Relationship Map

- **Guhan and Selva** operate as a leadership pair: Guhan sets strategic direction, Selva provides engineering specificity. They appear aligned.
- **Existing CI/CD engagement** (Anand's team) is the bridge that makes this new engagement possible. Same NDA, same security posture, same onboarding.
- **Customer pressure** is the external force driving urgency. Multiple key customers want the legacy UI. This is not a technical initiative, it is business-driven.
- **Internal resource justification:** Guhan explicitly stated the POC output will be used to secure additional resources. The demo quality matters for internal stakeholders beyond this call.
