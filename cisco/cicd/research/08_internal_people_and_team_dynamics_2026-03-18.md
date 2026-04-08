# 08 - Internal Meeting: People and Team Dynamics

**Source:** /cisco/cicd/source/internal_team_meeting_2026-03-18.txt
**Source Date:** 2026-03-18 (First internal team briefing)
**Document Set:** 08 (Internal team meeting — Colin, Saurav, Askari)
**Pass:** Team profiles, dynamics, and management style

---

## Source Context

This is the first meeting where Colin briefs his offshore delivery team — Saurav Kumar Mishra and Askari Sayed — on the Cisco CI/CD engagement. Colin joins approximately 4 minutes into the call; the first few minutes are Saurav and Askari chatting privately. The meeting runs approximately 1 hour 25 minutes. It is recorded on Teams. The transcript is speech-to-text and contains phonetic artifacts ("Altadeck" = Ultratech, "Askavi" = Askari, "Escar" / "Scari" = Askari, "Devakar" = Divakar).

This document focuses on the people present — who they are, how they behave, what can be inferred about their capabilities and engagement level — and on how Colin operates as a manager.

---

## 1. Saurav Kumar Mishra

**Role:** Offshore team member, already partially briefed by Colin before this meeting.

### What the transcript reveals

- **Prior context with Colin.** Saurav has had at least one earlier conversation with Colin about the engagement. He references this explicitly: "I already had like a small bit of this with you earlier — for him I think it's like totally new from the start to end." He has also seen documents that Colin shared previously and has been exposed to the CI/CD pipeline diagram. He has a head start on Askari.

- **Hardware status.** Has both the BayOne laptop and the Cisco laptop. Colin confirms this at the top of the meeting. Saurav is therefore hardware-ready to begin work.

- **Technical engagement level: high.** Saurav asks the most questions of anyone in the meeting. He drives into specifics:
  - Asks about the "commit from users" arrow in the CICD diagram and whether that is the same as the developer blue box or a separate code source. This is a good architectural question that forces Colin to explain the broken workflow where managers bypass the normal PR process.
  - Asks whether the developers or managers can select which gates run. This leads to a detailed walkthrough of the CDT vs. gates problem.
  - Asks about SDK availability for the DeepSight/Atlas platform.
  - Raises the stale unit test problem — what happens to old unit tests when a new function changes business logic? Colin validates this as exactly the right question and uses it to explain the need for state-aware unit testing.
  - Asks whether the issue of engineers not knowing why PRs are stuck is "a process problem" that BayOne should not be solving. Colin agrees but explains how AI gives them cover to address process problems under the AI banner.
  - Notes the token cost implications of scale: "even if they are like random checks just running, suppose one check takes around just suppose 100 tokens and we are running it 10 times a day for 750 people — that's a lot of tokens too."
  - Suggests using Claude Code (via "Co work on Cloud for Chrome") for the Cisco training sessions.
  - Asks whether they can use BayOne accounts for Claude on the Cisco device. Practical, shows he is thinking about the actual logistics of doing work.

- **Personality and rapport.** Comfortable with Colin. Jokes about Colin's Paint drawings ("I thought you would have drawn that"). Uses casual language. Responds to the Big Brother concern about developer KPI monitoring with "I don't know how I should feel about that thing" — an honest, slightly edgy reaction that Colin handles well by clarifying there is no surveillance intent. Expresses genuine enthusiasm: "Looking forward to it, yeah."

- **Pre-meeting behavior.** Before Colin joins, Saurav makes small talk with Askari. He asks about Askari's previous organization and seems to already know Askari was working at Ultratech. He also references sharing documents with Askari previously: "It should be the one for which I've shared the documents." This suggests Saurav has already been acting as a bridge between Colin and Askari, forwarding materials.

- **Assessment.** Saurav presents as an engaged, technically curious team member who is comfortable asking questions and pushing back. He is not passive. His questions are architecturally sound and show he has actually read the materials. He will likely be productive early.

---

## 2. Askari Sayed

**Role:** Offshore team member, brand new to the engagement. This is his first substantive exposure to the Cisco project.

### What the transcript reveals

- **Background.** Colin references asking Askari about the 10-million-line codebase during his interview, which confirms Askari was specifically screened for this engagement. Later in the meeting, Askari reveals his background: he was the lead AI engineer at Ultratech Cement. He holds a master's degree in data science (not stated in transcript but provided in the prompt context). He built a voice assistant using Wolfram Alpha named "Jarvis" for his bachelor's project, which won first place in his college, and he describes it as "one of my best projects I've made so far." He still has the codebase from 6-7 years ago.

- **Current situation at Ultratech.** Before Colin joins, Askari describes Ultratech as being in crisis. The transcript renders the company name as "Altadeck" — this is Ultratech Cement, one of India's largest cement manufacturers. The crisis is a supply chain disruption: "all our shipments are struck in the different Middle East area." The specific commodities affected are coal and petcoke, which are essential inputs for cement plant operations: "If you don't have a coal and petcoke, we cannot run our plants only. If the plant go shut down, Ultratech goes down." Askari describes it as ongoing and worsening: "every day there is something new is happening." He is doing "firefighting every day." He says it does not look like it will end soon and will "affect many people."

  **Implication:** Askari is still at Ultratech at the time of this meeting (March 18). He appears to be in a transitional state — he has been issued a Cisco laptop but does not yet have a BayOne laptop. His BayOne laptop shipped the day of this meeting (confirmed by Askari: "I just got update from Vinayak that it got shipped today"). He is not yet fully onboarded to BayOne.

- **Hardware status.** Cisco laptop only. BayOne laptop shipped March 18, not yet received. This means Askari cannot work on BayOne systems until the laptop arrives. Colin acknowledges this but proceeds with the briefing anyway: "good thing is I'll be able to talk through today because the important thing is..."

- **Technical engagement level: moderate but growing.** Askari asks fewer questions than Saurav but the ones he asks are substantive:
  - Asks whether they are building "a complete end to end platform from scratch with the custom plugins, custom connectors." Colin corrects this — they are extending VS Code, not building from zero.
  - Asks a synthesizing question about the overall goal: "So we have to build an agentic flow which is going to analyze the build image, find a bug and suggest a developer to fix the bug or AI is going to fix it by itself by writing the codes — is it what we are trying to achieve?" This shows he is following the thread and trying to construct a mental model, even though this is his first exposure.
  - Confirms experience with GitHub Enterprise: "Yeah, work with it."
  - Toward the end, notes "this is all much like too much information in this session" — honest self-assessment about information overload.

- **Personality.** Polite, somewhat more formal than Saurav. Says "makes sense" frequently as an acknowledgment. Shares the Jarvis voice assistant story with genuine enthusiasm and some pride. Responds positively to Colin's Marvel references. Says he is "looking forward to work with you and team" at closing.

- **Pre-meeting behavior with Saurav.** Askari and Saurav have a rapport already. Askari asks Saurav whether this is the same CI/CD project they discussed before. Saurav says no, it is the one related to "switch" (likely NX-OS/Nexus, which is the networking hardware). Askari then asks about "the one which about regarding the Java files," which may reference Saurav sharing Cisco code artifacts previously. This exchange shows they have been talking independently before Colin formalized the team.

- **Assessment.** Askari is starting from behind — he does not have BayOne hardware, has not seen the full document set, and is still actively employed at Ultratech dealing with a crisis. His technical background (lead AI engineer, data science masters) positions him well for the AI-heavy aspects of the engagement. His engagement level during the meeting is solid given that everything is new to him. He will need more ramp time than Saurav.

---

## 3. Colin Moore — Management Style and Leadership Approach

This meeting is the richest source in the library for understanding how Colin manages a team. The following observations are all first-person, drawn directly from his words and behavior during the briefing.

### 3a. Team Selection and Identity

Colin emphasizes that he chose this team deliberately: "I chose this team very specifically." He frames the team as a BayOne team first, not a Cisco team: "I'm trying to do something different with this team. Usually whenever we do engagements, we say like, oh, they're a part of the client team. I'm like, no, no, no, you're a part of the BayOne team first and then we just happen to be doing this client project." He says directly to both: "I want you to feel that way too."

This is a significant departure from how BayOne typically handles client engagements (per Set 04's discussion of dysfunction). Colin is building loyalty and identity around himself and BayOne, not around Cisco.

### 3b. Ground Rules — Explicit and Numbered

Colin sets four explicit rules:

1. **Do Cisco work on Cisco hardware.** But this is immediately softened with nuance: prototyping on BayOne hardware is fine, API keys will never be detected, and the constraint is directional — "Stuff can go onto your Cisco laptop, but stuff should not be coming off of your Cisco laptop onto your BayOne laptop." He warns that Cisco monitors file transfers on Cisco machines: "any files that you send forward or backward out of that laptop are gonna get looked at because we are a client to them." The practical message: be smart, don't transfer large code files out of Cisco systems, and use common sense.

2. **Interact directly with Cisco — as peers.** Colin explicitly tells Saurav and Askari to see themselves as peers to VP-level and senior director-level Cisco staff: "See yourself as their peer. You're the person that they're hiring to tell them what the heck to do because they don't know." He uses the analogy of how you might talk to a father figure — respectful debates are fine, but some things you just do not say. He specifically addresses the Srinivas relationship: "I will take no hold backs on arguing with him, but always do it respectfully. Always take him and understand he's in charge of his practice."

3. **Use Webex for Cisco communications; Teams for internal.** All Cisco-side communication moves to Webex. Internal team meetings stay on Teams (for recording capability). Colin had created a Teams channel but will set up Webex teams once accounts are ready. This is a practical dual-platform constraint, not a preference.

4. **Escalate early.** "If you're having a problem or if you feel like you're getting behind, please tell me ASAP." Colin ties this to the April 30 renewal timeline and the need to show progress. He frames escalation as a trust-building opportunity, not a failure signal: "client contracts, the way that they work for the most part is if you can prove yourself early on in the beginning, you will have a rock solid relationship for the whole full duration." He says explicitly: "it's never bothering me."

### 3c. Communication Style

- **Uses analogies and metaphors extensively.** Father figure analogy for client relationships. Car upgrade analogy for pricing. "Screw the CDT" for manager behavior. "Raw chicken on the sandwich" (carried from Set 04, not used here but characteristic).
- **Self-deprecating about his tools.** Jokes about his MS Paint drawings. Shares openly that he would run through compliance trainings at his old job with multiple monitors while eating lunch — not telling them to do that, but winking hard.
- **Demystifies the client.** Repeatedly normalizes what could be intimidating: "don't get freaked out about the size" (10M LOC). "This is dreams. I ask this every day from Claude" (about the chat interface). "None of them are real" (DeepSight apps). He strips away Cisco's self-image as a uniquely complex enterprise: "They like to think they have the hardest problems in the world. I disagree."
- **Strategic transparency.** Shares his internal strategy openly with the team. He tells them he is trying to build a relationship with Srinivas through DeepSight: "my point here is definitely take a look at the recording" and "if we put applications on the screen for him, big or small, even if they're not related to the project, that guy will love us." He shares the GitHub Actions rejection as a political reality, not a technical one. He shares that he does not believe phase one will be done by April 30 — but the goal is to show progress and have a plan.
- **Inclusive meeting behavior.** He says explicitly: "I am not the type that says, you know, hey, only I talk at meetings." He promises dress rehearsals before senior meetings but wants both team members participating in VP-level calls.

### 3d. Cultural Sensitivity

At the end of the meeting, Askari raises that Eid might fall on Friday and he would need to take leave. Colin's response is immediate and accommodating: "Oh, that's right. That's right." He does not hesitate or create friction. He reschedules the next meeting to Thursday instead, and goes further: "I don't want to hold you to the holiday calendar, the optional one, without you being fully onboarded yet." He explains the optional vs. fixed holiday system will be covered after full onboarding. This is handled naturally, without performative statements.

### 3e. Commitment to Team Knowledge Infrastructure

Colin introduces his approach to knowledge management as a team benefit, not an administrative burden. He describes:
- Recording all internal meetings on Teams
- Extracting transcripts and processing them through Claude Code skills
- Creating GitHub issues from meeting transcripts automatically
- Building a "blockchain style" knowledge chain where each meeting produces a knowledge document and a bridge document linking to the previous state
- Setting up a repository for all materials

He frames this as a commitment: "that's my kind of commitment to both of you. There's going to be a lot of information thrown around. It's going to be really tough to get our minds wrapped around all of it at once."

### 3f. Internal Tooling Sharing

Colin mentions several BayOne-internal capabilities:
- **Jarvis** — the codename for BayOne's internal automation project using Airflow + Azure + Claude Code skills
- **Airflow** — running and available, with Azure access, for recurring background tasks
- **TalentAI** — referenced as the platform where the transcript processing skill currently lives (Askari does not yet know what TalentAI is; Saurav gave him "a brief description")
- **Tanuja** — mentioned as another team member who could handle internal automation tasks

---

## 4. Team Dynamics

### 4a. Saurav and Askari Pre-Meeting

The first 4 minutes of the call are Saurav and Askari talking without Colin. Key observations:

- They already have a rapport. The conversation is casual and friendly.
- Saurav asks about progress on something Askari was working on at his previous organization — "the what do you call Katie you were giving in your last organization" (likely a KT or knowledge transfer). This suggests they had discussed Askari's Ultratech work before.
- Askari shares the Ultratech crisis candidly with Saurav. There is no guardedness.
- They reference having discussed the project previously: Askari asks "is this the same project of the CICD that one which you discussed with me?" and references "the one which about regarding the Java files." They have been communicating independently.

### 4b. Engagement Asymmetry

Saurav is significantly more active than Askari throughout the meeting. This is expected — Saurav has prior context, already has both laptops, and has already been briefed by Colin once. Askari is receiving everything cold. Askari's "too much information" comment near the end is honest and appropriate for someone encountering all of this for the first time.

### 4c. Colin's Information Distribution

Colin is the sole source of information in this meeting. Neither Saurav nor Askari contribute any information about the Cisco engagement itself — they are purely receiving. This is a one-directional briefing, not a working session. The team has not yet done any work on the engagement.

### 4d. No Tension or Friction

There are no disagreements, no awkward moments, and no signs of interpersonal friction. The closest thing to pushback is Saurav's Big Brother comment about KPI monitoring, which Colin defuses cleanly.

---

## 5. Other Team Members Referenced (Not Present)

### Srikar
- Not present. Not yet onboarded. Expected "next week" (week of March 24). Colin says he "definitely will be here next week."

### Namita
- Not present. H1B transfer issues. Colin expects her "definitely before the end of the month" (March) but adds: "They keep telling me next week, but I don't believe it."
- Described as the Airflow expert: "she did that for a job for eight years, so she's very well equipped on this."

### Tanuja
- Mentioned once in passing. Positioned as someone who could handle internal BayOne automation tasks so as not to burden the Cisco delivery team.

### Vinayak
- Mentioned by Askari as the person who informed him the BayOne laptop shipped. Likely a BayOne operations/logistics person.

---

## 6. Hardware and Readiness Summary

| Person | BayOne Laptop | Cisco Laptop | Status |
|--------|--------------|--------------|--------|
| Saurav | Yes | Yes | Hardware-ready. Has prior briefing context. |
| Askari | Shipped Mar 18, not received | Yes | Can access Cisco systems but not BayOne systems. Still transitioning from Ultratech. |
| Srikar | Unknown | Unknown | Not yet onboarded. Expected week of Mar 24. |
| Namita | Unknown | Unknown | H1B transfer pending. Expected before end of March (Colin skeptical). |
