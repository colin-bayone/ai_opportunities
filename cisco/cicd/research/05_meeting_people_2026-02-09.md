# 05 - Meeting: People (CICD-Relevant Only)

**Source:** /cisco/cicd/source/meeting_guhan_selva_2026-02-09.txt
**Source Date:** 2026-02-09 (Cisco campus meeting, primarily EPNM-focused)
**Document Set:** 05 (Guhan/Selva meeting -- light treatment for CICD)
**Pass:** People relevant to CICD engagement

---

## Source Context

This is an in-person meeting at the Cisco campus during Colin's two-week Bay Area trip (weeks of February 9 and 16, planned in Set 03). The meeting is primarily about the EPNM/UI conversion opportunity -- a separate engagement tracked in `cisco/epnm_ems/`. This file extracts only the people and relationship signals relevant to the CICD engagement.

The transcript is a speech-to-text capture of a conference room conversation. Quality is uneven -- "Mecha" is likely Mahesh, "sheen" = screen, "goat" = Go (programming language), "HGPD" = ChatGPT, "GTO" = CTO. The meeting includes small talk, logistics about room setup, WebEx connectivity struggles, and scheduling for a follow-up session later that afternoon.

**Meeting setup:** Venkat arranged this introduction (confirmed in Set 04: "I put in a good word with Guhan"). The meeting that Set 04 predicted -- "just you, Guhan and Venkat" -- appears to have materialized as Colin meeting Guhan in person, with Selva (BayOne) facilitating.

---

## People Identified

### 1. Guhan

**Role:** Cisco executive or senior engineering leader with $7M in R&D funding. Manages a large distributed team (Israel, India, and likely Bay Area). Reports to or is a peer of Venkat. This meeting confirms he is the person Set 04 identified as the major expansion opportunity.

**What this source tells us:**

- Guhan is physically present in this meeting and is the Cisco-side host. He speaks with authority about platform strategy, product management priorities, and team consolidation -- this is not someone relaying decisions, this is the decision-maker.
- He travels extensively: Sweden, India (December/January), upcoming trips to Israel, Europe. He has "a large team" in Israel -- "very hardworking, very smart folks" -- that he has not visited in five years. He also has a team member ("my cut") who is described as being "everywhere at all given times" traveling between India, Sweden, Israel, and Europe.
- He frames the EPNM/UI conversion problem in terms that directly parallel the CICD engagement's context: legacy code, customer resistance to change, competing internal initiatives that need consolidation, and the challenge of deciding where to invest limited engineering time.
- He describes himself as managing 45-50 million lines of code across 6-8 parts, spanning multiple generations of platform evolution (gen A to gen E and beyond). This is the broader codebase context that both the EPNM and CICD engagements sit within.
- He values strategic thinking over implementation: "Given your title and your experience, I think it's not just about implementing. What is the right direction? What is the right way to go about it?" He explicitly asks Colin for consulting, not just delivery.
- He is trying to bring structure to his organization: "I'm trying to build a catalog of things that are happening and have a structured way through Jira... trying to bring certain process... we have been trying to get some order, some method to madness." This maps directly to the same organizational discipline problems that plague the CICD engagement's target environment.
- He defers priority decisions to product management: "The product has prioritized, which is important. Because everything at this point seems to be priority... We've got to have 10 priorities and run behind everything, all the 10." He wants to "enforce some decisions" on product management to prioritize properly before committing BayOne resources.
- He is open to Colin exploring his broader team's work even before formal engagement: "If your team has time, I have time... they can explain what is happening around so that you can also... the choices are there then you can pick." He invites Colin to shadow his teams to understand what is happening and help weigh in on priorities.
- He reacts positively when Colin begins presenting the code modernization methodology: "I'm sorry to interrupt you, but this seems definitely interesting. I want to understand, are you going to add a knowledge graph? And all those things, right?" He stops the presentation to ask for a deeper session, scheduling a follow-up the same afternoon.

**Signals for CICD:**

- **Guhan's $7M R&D budget is the expansion path.** Set 04 identified this as the largest opportunity. This meeting confirms Guhan is real, engaged, and interested. His interest is primarily EPNM/modernization, but his organizational challenges (consolidation, prioritization, method to madness) are identical to the problems the CICD engagement addresses at a smaller scale.
- **"Method to madness" is a shared pain.** Guhan describes trying to bring order to competing team initiatives, catalog work in Jira, and enforce prioritization. This is exactly the problem space where CICD improvements (standardized pipelines, automated testing, deployment discipline) provide structural answers. If the CICD engagement succeeds in Anand's group, the "method to madness" framing is how it could expand into Guhan's larger organization.
- **He wants consulting, not just execution.** His explicit request for strategic guidance ("what is the right direction?") aligns with Colin's positioning as a consulting partner, not a staff augmentation vendor. This is the same positioning Colin has used in CICD conversations.

---

### 2. Selva

**Role:** BayOne account or relationship manager. Facilitates the meeting logistics, manages scheduling, and acts as the intermediary between Colin and Cisco stakeholders.

**What this source tells us:**

- Selva is physically present in the meeting and handles the practical logistics: finding conference rooms, connecting to WebEx, managing calendar conflicts, coordinating with Guhan on follow-up scheduling.
- He knows Guhan's calendar and team dynamics: "I'll look at your calendar... You won't be able to find it. It's very difficult." He manages the relationship at the operational level.
- He is the one who confirms meeting times and offers to introduce Colin to Guhan's team members: "We love that. He's got, he's here for the next two weeks and we're going to be here pretty much in and out."
- He refers to Colin in the third person when talking to Guhan ("He's here for the next two weeks"), positioning Colin as the BayOne resource being deployed.
- His role in this meeting appears similar to Zahra's role with Anand/Venkat -- he is the relationship holder, Colin is the technical substance.

**Signals for CICD:**

- Selva is a BayOne account person managing the Guhan relationship specifically. He does not appear in prior CICD research (Sets 01-04). His presence suggests BayOne has assigned dedicated account coverage for the Guhan expansion opportunity, separate from Zahra's management of the Anand/Venkat relationship.
- If Guhan's broader organization includes teams adjacent to the CICD engagement, Selva would be the BayOne person to coordinate cross-pollination between the two engagements.

---

### 3. Mahesh (transcribed as "Mecha")

**Role:** Cisco internal person who suggested BayOne to Guhan for the EPNM/UI work.

**What this source tells us:**

- Guhan opens the substantive portion of the meeting by saying: "Mecha did chat with me about one of the things that we could do, and there was some interesting opportunities that we had to accelerate some area." This means Mahesh initiated the conversation about using BayOne.
- This aligns with Set 03's identification of Mahesh as a Cisco internal champion sympathetic to BayOne. In Set 03, Mahesh was quoted telling Rahul daily that Abhay should have chosen BayOne. Here, Mahesh is actively brokering introductions -- he has moved from passive sympathy to active advocacy.

**Signals for CICD:**

- Mahesh is now confirmed as an active BayOne advocate inside Cisco, not just a sympathetic bystander. He connects to both the EPNM and potentially the CICD orbits. If Mahesh is close to Guhan's organization, success in either engagement reinforces BayOne's position through Mahesh's advocacy.
- The Set 03 gap ("Is Mahesh connected to Anand's organization?") remains unresolved, but his connection to Guhan is now confirmed.

---

### 4. Varel

**Role:** Cisco team lead. Manages the UI-focused team that would handle the EPNM screen conversion work.

**What this source tells us:**

- When Colin asks whether Varel would be involved, Guhan confirms: "Yeah, one idea is Varel's team, which is the... the one he said was the one that referred to the UI." Varel's team handles the UI layer.
- Colin says he just met with "Salva" (likely Selva, or possibly a separate person) "the other day, actually." The context suggests Colin has already been making rounds at Cisco during his Bay Area trip.

**Signals for CICD:**

- Varel is EPNM-specific and not directly relevant to the CICD engagement. However, knowing that Guhan's organization includes Varel's UI team and Meryl's agentic platform team helps map the organizational structure. The CICD engagement (Anand/Srinivas) sits elsewhere in the org chart but may share infrastructure or platform dependencies with Varel's and Meryl's teams.

---

### 5. Meryl

**Role:** Cisco leader building an agentic AI platform. Separate from Varel's UI team, also under Guhan's umbrella.

**What this source tells us:**

- Guhan identifies two areas of work under his purview: (1) the UI conversion (Varel's team) and (2) the agentic platform (Meryl's team). When Colin asks about Meryl, Guhan says: "The agency platform is being built by Meryl. And I checked with her on what she needs something there at this point."
- Colin reveals he has already been in contact with Meryl: "Meryl and I were supposed to have a follow-up conversation as well."
- **The critical CICD connection:** Colin says directly: "She mentioned that I talked about what we're doing with CICD. She said it's somewhat relevant to us." This is the only direct mention of CICD in the meeting. Meryl acknowledges CICD has some relevance to her agentic platform work but characterizes it as "somewhat" -- not a primary fit.
- Meryl is based in New York, not in the Bay Area. She is traveling and will not be available the following week. Colin and the group discuss scheduling a separate connection.

**Signals for CICD:**

- **Meryl is the bridge between the EPNM and CICD conversations.** She is the only person in this meeting who has directly referenced the CICD engagement, and she characterized it as "somewhat relevant" to her work. This is a weak but real connection point.
- Her agentic platform work could eventually benefit from the same CI/CD pipeline improvements being built for Anand's team. If BayOne succeeds in standardizing CI/CD practices for Anand/Srinivas, the methodology could be extended to Meryl's platform team as a natural expansion.
- She is aware of Colin and has engaged with him independently. This means BayOne has touchpoints across at least three Cisco organizations: Anand/Srinivas (CICD), Varel (UI), and Meryl (agentic platform), all connected through Guhan.

---

### 6. Colin Moore

**Role:** BayOne Director of AI. Same role as Sets 01-04.

**What this source adds (incremental):**

- This is Colin's first in-person meeting with Guhan. He positions himself as a consulting partner with deep technical experience, not a vendor selling staff: "I'm our Director of AI... my focus has always been high reliability systems. Determinism in AI, things that you can actually trust and are transparent."
- He introduces the CICD engagement naturally as context for his Cisco experience: "We had a couple of things at Cisco. One that we have right now that we're, I think, about to start this work is on CI-CD side." He then pivots to the code modernization topic as more relevant to Guhan's needs.
- He positions himself as a consulting partner explicitly: "It's as much for me a solution as it is consulting in a way. Because our job can't just be to do solutions. Because if I do that, I'm not really being a good partner to you. I have to help you think about what comes next."
- He demonstrates strong rapport-building with Guhan. The meeting starts with small talk about travel, and by the end, Guhan has interrupted Colin's presentation to schedule a deeper afternoon session -- a strong engagement signal.
- He references his Coherent experience: ~40,000 employees, 60-person team, Center of Excellence for AI, data-com/telecom domain ("less about where Cisco is, but I at least understand enough to be conversational").
- He describes his methodology for code modernization as starting with "simplification" and building a knowledge graph -- Guhan interrupts excitedly at this point.

**Signals for CICD:**

- Colin's positioning in this meeting carries directly into CICD. The "high reliability systems," "determinism in AI," and "consulting not just solutions" framing is the same posture he uses with Anand's team. Success in this meeting reinforces his credibility across all Cisco engagements.
- He mentions CICD unprompted as one of the things BayOne is already doing at Cisco. This establishes CICD as real, ongoing work -- not a theoretical proposal. Guhan hears that Colin is already embedded at Cisco, which adds credibility to the expansion conversation.
- His ability to pivot from CICD (Anand's scope) to code modernization (Guhan's scope) in a single conversation demonstrates the cross-selling potential that BayOne leadership has been pursuing.

---

## People Referenced But Not Present

| Person | Prior Set Role | Status in Set 05 |
|--------|---------------|-------------------|
| Anand | CICD sponsor, budget holder (Sets 01-04) | Not mentioned. This meeting is Guhan's world, not Anand's. |
| Srinivas | CICD technical lead (Sets 01-04) | Not mentioned. |
| Venkat | VP who brokered this introduction (Set 04) | Not present in the room but his advocacy is the reason this meeting exists. |
| Zahra | BayOne account lead (Set 04) | Not mentioned. Selva appears to manage the Guhan relationship separately. |
| Rahul | BayOne senior leadership (Sets 02-04) | Not mentioned by name, though the trip to Bay Area was planned with him in Set 03. |
| Sarang | Former BayOne resource at Cisco (Sets 02-04) | Not mentioned. |

---

## Relationship Map Update (CICD-Relevant Additions from Set 05)

```
Cisco Side                                       BayOne Side
----------                                       -----------
Venkat (VP)                                      Selva (account, manages Guhan relationship)
  |                                                |
  +-- Anand (CICD sponsor)                       Zahra (account, manages Anand/Venkat)
  |     +-- Srinivas (CICD tech lead)              |
  |                                              Colin Moore (Director of AI)
  +-- Guhan ($7M R&D)                              + now has direct rapport with Guhan
        +-- Mahesh (internal champion, active)      + CICD work mentioned as existing credential
        +-- Varel (UI team -- EPNM)                 + code modernization pitched to Guhan
        +-- Meryl (agentic platform)
              + "CICD somewhat relevant" <---------- weak link to CICD engagement
```

---

## Gaps Remaining

1. **Selva's exact role at BayOne.** Is he an account manager, delivery lead, or another function? His relationship to Zahra and the Anand/Venkat track is unclear.
2. **Mahesh's organizational position.** Confirmed as connected to Guhan. Still unknown whether he is connected to Anand/Srinivas (the CICD group).
3. **Meryl's follow-up with Colin.** The conversation about CICD being "somewhat relevant" was mentioned but not explored. The nature of the relevance is undefined.
4. **Guhan's reporting relationship to Venkat.** Set 04 said Venkat introduced Guhan. This meeting does not clarify whether Guhan reports to Venkat or is a peer. The 45-50M lines of code and $7M R&D budget suggest significant organizational scope.
