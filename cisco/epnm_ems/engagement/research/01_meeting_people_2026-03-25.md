# 01 - Meeting: People

**Source:** `source/guhan_selva_3_25_2026.txt`
**Source Date:** 2026-03-25 (POC Proposal Discussion)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused on people identification, roles, sentiment, and dynamics

---

## Attendees

### Guhan (Cisco)

- **Role:** Senior leader on the EPNM/EMS product line. Framed the problem, set expectations, drove the conversation.
- **Observed behavior:** Opened the meeting with a thorough walkthrough of the business problem. Spoke first and longest in the initial framing. Used "we" language throughout, indicating ownership of the decision to pursue this path. Gave Colin room to present but asked pointed follow-up questions.
- **Key concern:** Domain-level functionality gaps. Asked directly: "How do you make sure there's no domain gap or no functionality gap?" This was the most probing technical question on the call. He wants assurance that conversion is faithful, not just cosmetically similar.
- **Sentiment:** Positive and engaged. Receptive to the approach Colin presented. Wants this to succeed because it serves a business need (moving customers from EPNM to EMS). Sees the POC as a tool to justify additional resources internally: "if we have to also get the additional resources for this, which we will have to work through, this will help."
- **Decision authority:** Appears to be the primary decision-maker for this initiative. Set the 4-week timeline. Directed team availability expectations.
- **Key quote (paraphrased):** "We need to move those customers. The idea is to move all the customers from EPNM into EMS."

### Selva (Cisco)

- **Role:** Engineering or product leader, closer to the technical implementation. Knows what has and has not been ported to EMS.
- **Observed behavior:** Spoke second, added technical specificity to Guhan's framing. Clarified the "vertical" nature of the work: "If something was not brought in the front-end, the corresponding back-end is also not working." Suggested focusing on screens NOT yet brought into EMS to maximize value.
- **Key contribution:** Reframed the exercise from "convert old to new" to "bring missing functionality into EMS end-to-end." This is a sharper, more actionable scope. Suggested looking at missing reports as a concrete starting point.
- **Sentiment:** Practical, solution-oriented. Not skeptical but also not effusive. Wants the exercise to be useful: "just to add more value to this exercise, we will focus on the ones that we've not brought in yet."
- **Expectations of Colin:** Expects Colin to work independently after receiving context. "Hopefully you'll be able to, once we get the context right, you'll be able to move ahead on your own to do this analysis and come back."
- **Team availability note:** Made it clear the team is on critical platform work and cannot dedicate significant time. Context will be provided, but Colin runs independently with periodic checkpoints.

### Colin Moore (BayOne Solutions)

- **Role:** Director of AI, BayOne's technical lead for this engagement. Presenting the POC proposal and methodology.
- **Observed behavior:** Had prepared the proposal before the meeting. Shared his screen to walk through prepared questions, noting many had already been answered by Guhan's opening. Pivoted smoothly to ask targeted follow-ups rather than reading from a script.
- **Technical presentation:** Explained the toolchain (Claude Code for exploration, LangGraph agent swarm for deeper work), the agent architecture (architect, engineer, foreman, judge), the blockchain documentation approach, and Playwright for automated testing. Used analogies ("bringing the army approach versus one soldier") to make abstract concepts concrete.
- **Positioning:** Framed the POC as an investment BayOne is making: "sometimes the proof is in the pudding." Committed to working on Cisco hardware with Cisco-licensed AI tools without hesitation. Did not oversell or make timeline promises beyond what was discussed.
- **Sentiment:** Confident, enthusiastic ("this is the fun part for us"), respectful of Cisco's security requirements.

### Additional BayOne Participant (likely Rahul or team member)

- **Role:** Brief interjection near the end regarding hardware timeline. Mentioned there's a call in the evening to get a firm date on the Cisco laptop delivery.
- **Observed behavior:** Supportive, logistical. Committed to expediting the hardware process.
- **Key statement (paraphrased):** "We're going to get an answer on the hardware today. There's a call in the evening... we're going to try to speed that process up."

---

## Dynamics

- **Guhan led, Selva refined.** Guhan set the strategic frame (customers need this, it's business-impacting). Selva added operational precision (which screens, what "vertical" means, team bandwidth).
- **Colin was well-prepared.** Having the proposal pre-written earned credibility. The fact that Guhan's opening answered many of Colin's prepared questions was noted positively by Colin and demonstrated alignment.
- **Trust signals:** Guhan explicitly asked Colin to use Cisco-licensed tools, and Colin agreed immediately and enthusiastically. No friction on security. Guhan also indicated willingness to help Colin get set up with licenses, which suggests investment in the relationship.
- **Independence expected.** Both Guhan and Selva emphasized that Colin should work independently after initial context is provided. The team is busy. Periodic checkpoints, not continuous support.
- **POC as internal leverage.** Guhan sees the POC output as something he can use to secure more resources. This means the deliverables need to be demo-ready and visually compelling, not just technically sound.
