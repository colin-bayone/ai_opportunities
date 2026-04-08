# 09 - Internal Meeting: People and Team Dynamics

**Source:** /cisco/cicd/source/internal_team_meeting_2026-03-30.txt
**Source Date:** 2026-03-30 (Full team briefing)
**Document Set:** 09 (Internal team meeting — Colin, Saurav, Askari, Srikar)
**Pass:** Team profiles, new members, and dynamics

---

## Source Context

This is the second internal team briefing on the Cisco CI/CD engagement, 12 days after the first (Set 08, March 18). The meeting runs approximately 1 hour 24 minutes. Colin Moore is joined by Saurav Kumar Mishra, Askari Sayed, and — for the first time — Srikar. This is the first meeting with four of the five team members present. Namita remains absent pending H1B completion. The transcript is speech-to-text and contains phonetic artifacts ("Scotty" / "Sridhar" = Srikar, "Golin" = Colin, "Vanessa" = a misrender when Colin addresses Saurav, "Askavi" / "Ashika" = Askari, "Altadeck" = Ultratech, "Bevin" = BayOne).

This document focuses on the people — who is new, what can be inferred about them, how the team dynamics have evolved since Set 08.

---

## 1. Srikar — New Team Member

**Role:** On-site team member, Bay Area based, will be physically present at Cisco's campus alongside Namita.

### What the transcript reveals

- **Location.** San Francisco Bay Area. Recently moved to the US (approximately two years). Previously based in Bangalore. Colin confirms: "she'll be with you in in person in the Cisco offices in California" when discussing Namita joining Srikar on-site.

- **Background.** Srikar introduces himself: "I previously worked as a AI engineer and before that like I worked on computer vision systems." He does not elaborate on specific employers or projects during this meeting. His self-description is brief and modest compared to Saurav and Askari's introductions.

- **Meeting with Colin the prior week.** Colin says: "Srikar, we got to spend some time together in person last week." This confirms an in-person meeting occurred during the week of March 23-27, consistent with the Set 08 expectation that Srikar would be onboarded that week.

- **Hardware status.** Has a Cisco laptop. Does not yet have a BayOne laptop. Colin confirms: "Srikar, you only have Cisco hardware, not Bay one hardware just yet." Srikar says he needs to meet Rahul (Bobbili) — "tomorrow, maybe, maybe tomorrow or Wednesday, so I'll be getting it back as well." This means as of March 30, Srikar has been on the team for approximately one week but is still missing BayOne hardware. He can join the Teams meeting as a guest but does not have a BayOne email account. Colin notes: "he has a Cisco e-mail, not a Bay one e-mail" and that "your Bay one account will be resolved in a couple of days."

- **Time zone accommodation.** Colin opens with an apology: "Srikar, my sincere apologies to you. I know it is super early for you." The meeting is at approximately 2:00 PM EST, which is 7:00 AM PST. Srikar's response is gracious: "No problem. I was actually waiting. You informed me on the Friday, right? So I was, uh, prepared and waiting." Colin immediately commits to adjusting future meeting times: "probably 11 EST or 8:00 AM PST will be our sweet spot for meeting. So going forward, I'll adjust the meeting."

- **Engagement level during the meeting.** Srikar speaks less than Saurav or Colin. His contributions are short and confirmatory ("Yeah," "Right, yes," "OK, got it"). He does ask one substantive question: when Askari raises GitHub's AI agent platform for code review, Srikar asks a clarifying question — "So the one you mentioned, this will come after raising a PR or before raising a PR?" — which prompts a useful exchange where Saurav explains the blue box (pre-PR, local) versus the green box (post-PR, GitHub). This shows Srikar is following the architecture discussion and thinking about placement of capabilities in the pipeline.

- **Openness to collaboration.** At the end of the meeting, Srikar volunteers his availability explicitly: "I'm open to like anytime like when you are whenever you are want to connect respect of the time like I'm I'm open to like be on the call anytime later at night or early morning also works for me." This is a strong signal of engagement and willingness.

- **Assessment.** Srikar is quiet but present. He does not ask many questions, but the one he does ask is targeted and shows comprehension. He is new to the team, new to the US (two years), and joined this meeting at 7:00 AM his time without complaint. The combination of Bay Area location, AI/computer vision background, and willingness to be on-site at Cisco makes him strategically valuable for the discovery phase. His personality appears agreeable and accommodating. Whether he will be as vocal as Saurav in engineering discussions remains to be seen — this was his first group meeting and he may have been deferring.

---

## 2. Namita — Status Update

Namita is still not present. Colin provides an update:

- **H1B process.** "Our final person that is on this team, she's just finishing up her H1B process. So it took her a couple extra days than we had anticipated, even with us expediting that process." This confirms the H1B transfer is taking longer than expected, consistent with Colin's skepticism in Set 08 ("They keep telling me next week, but I don't believe it").

- **Expected timeline.** "She'll get involved with everything, uh, probably starting next week." This pushes Namita's start to the week of April 6. In Set 08 (March 18), Colin expected her "definitely before the end of the month" (March). She has slipped by at least one week.

- **Physical location.** Colin confirms she will be on-site at Cisco with Srikar: "she'll be with you in in person in the Cisco offices in in California."

- **Expertise reiterated.** Colin describes her as "the resident airflow expert" and adds: "her background was in in in Airflow itself as well as Apache Kafka." He also calls her "an Agentic AI specialist." The 8-year Airflow experience first mentioned in Set 08 is referenced indirectly through the framing of her as the Airflow anchor for the team.

- **Discovery role.** Colin assigns Namita (alongside Srikar) to the structured discovery phase because they are local: "the burden will primarily fall on myself, Srikar and Namita. The reason being, Srikar and Namita will be on site on Cisco's campus, and since they're local, they have that capability to be there in person for meetings."

---

## 3. Saurav Kumar Mishra — Evolution from Set 08

Saurav continues to be the most active team member after Colin.

- **Pre-meeting behavior.** Saurav opens the call before Colin arrives, greeting Srikar and Askari. He takes a casual leadership role: "Let's wait a couple of minutes for Colin." This mirrors the Set 08 pattern where Saurav and Askari chatted before Colin joined.

- **Technical engagement.** Saurav's questions and contributions in this meeting are more solution-oriented than in Set 08:
  - Raises the question of whether Cisco developers already use agentic coding tools (Claude Code, Codex, Cursor). This leads to a useful discussion about GitHub Copilot being the only tool available to most Cisco developers.
  - Asks about the impact of work trees on PR velocity metrics — pointing out that baseline measurements will shift if tools change developer behavior.
  - Continues to connect architecture to real tooling: suggests that branch health notifications could be "background automated process based on the different type of notification" using Airflow.
  - Proposes adding the Singularity skill to a scheduler on "cool work" (Claude Code cowork) so it runs automatically after meetings, which Colin redirects to the Jarvis plan.
  - Asks practical logistics questions: where to complete the GitHub Enterprise training, whether DeepSight requires training before building on it.

- **Rapport with team.** Saurav responds to Srikar's introduction warmly: "really looking forward to working with you." His self-introduction references approximately one year at BayOne and "3 plus years of experience building AIML solutions. Mainly it was regarding document intelligence and business process automations and before that I have been like involved and working for as like freelancer for around two years."

- **Assessment.** Saurav has clearly progressed from Set 08. He is no longer just asking questions to understand the engagement — he is contributing solution ideas and thinking about operational workflow. He references Talent AI and Django Forge from his internal BayOne work, confirming he has hands-on experience with the tooling patterns Colin is bringing to this engagement.

---

## 4. Askari Sayed — Evolution from Set 08

Askari is notably quieter in this meeting than in Set 08.

- **Participation level.** Askari speaks only a few times in the entire meeting. His introduction to Srikar is brief: five years' experience, three in "and around" (likely analytics), two in "proper ML side, modeling side," currently lead AI engineer at Ultratech Cement ("Ultradex Cement" in transcript), master's in data science and big data analytics.

- **One substantive contribution.** Askari raises the question about GitHub's AI agent platform for automated code review and test generation: "recently if we'll see the GitHub has launched its own agent AI platform correct, which automatically verify and do all the sanity checks and generate the test cases." He asks whether they can "utilize that and on top of that you know build our own like on own customizable agent AI." This is a relevant point that leads to the copilot quality discussion.

- **Assessment.** Askari's reduced participation could reflect several things: he may still be absorbing (the "too much information" reaction from Set 08 may apply here too), the meeting is late in his time zone, or he may be more comfortable contributing in smaller settings. He has not had an opportunity to demonstrate hands-on work yet. His one contribution shows he is tracking industry developments (GitHub's agent AI platform) and thinking about integration strategies.

---

## 5. Colin Moore — Management and Communication

### 5a. Time Zone Management

Colin demonstrates acute awareness of the multi-timezone challenge. The meeting starts at approximately 2:00 PM EST / 7:00 AM PST / late evening IST. He immediately apologizes to Srikar for the early Pacific time and commits to adjusting: "11 EST or 8:00 AM PST will be our sweet spot." For the India-based team members, he discusses Monday/Wednesday/Friday or Monday/Wednesday/Thursday cadence, noting: "I know Friday will get late for Askari and and Saurav, we might do Monday, Wednesday, Thursday, so that way we don't have to kill your weekend off." He also suggests Friday meetings could be "a shorter one so everyone can get a reasonable start to the the weekend."

### 5b. Sales Training Absence

Colin discloses that he was unavailable the prior week: "there was a sales training last week where essentially they for all purposes, made us put our phones in a metal box and said you can't touch them for a week." He describes himself as "characteristic" (likely meant "uncharacteristic" or the transcript garbled it) in being offline. He immediately reaffirms his commitment: "I'm finally back EST. This is my number one priority to get this project on the road and ready to go."

### 5c. Emphasis on Flat Team Structure

Colin devotes significant time to establishing that engineering discussions should be argumentative: "I've never in my life had an engineering team that hasn't argued at some point. So I'm warning all of you. Everyone is smart here as long as we're all respectful of each other. I don't care if it gets heated." He explicitly warns against passivity: "the worst thing to do is also to just not say anything, just be passive. That's also a bad thing when it's just one person steamrolling everyone." He frames architecture decisions as collaborative: "I haven't used anything specific that is for us to think through and have discussions on this week itself." The only veto criterion he sets is production-readiness: "I only shut things down if they're not going to be production oriented." He gives Ollama as an example — with 750 developers committing around the clock, a local model will not scale.

### 5d. Team Identity Reinforcement

Colin repeats the team-first framing from Set 08: "I had the luxury of picking everyone kind of by hand for this project." He emphasizes complementary skills: "everyone on this team has a lot of crossover with what you know, which is a good thing, but you also kind of each bring something unique to the table." He asks team members to "get to know one another, to know what the strengths are."

### 5e. Intern Anecdote

Colin tells a story about a former intern who, after five days on the job, proposed "increasing annual revenue" as a transformative company idea. The purpose is to caution against flagging deficiencies in Srinivas's DeepSight platform without sufficient context: "make sure you know you're putting the time in on your end before you say this is not good or this is really good." He immediately softens it: "I know everyone's far beyond that in this group, but needs to be said."

---

## 6. Team Dynamics

### 6a. Four of Five Present

This is the first meeting with the near-complete team. The dynamic is noticeably different from Set 08's two-person briefing. Colin does most of the talking (as expected for a briefing), but three people are now receiving rather than two. Saurav remains the primary questioner. Srikar contributes sparingly. Askari contributes once substantively. There is no interpersonal friction.

### 6b. Saurav as Informal Bridge

Saurav continues the pattern observed in Set 08 of acting as an informal bridge. He opens the meeting, manages small talk, and in the body of the meeting, explains the blue box vs. green box distinction to Srikar when Askari's question creates ambiguity about where AI code review fits. Colin does not have to intervene — Saurav fills the gap.

### 6c. On-Site vs. Offshore Split

The team now has a clear split:
- **On-site (Bay Area):** Srikar (active), Namita (pending)
- **Offshore (India):** Saurav, Askari

Colin assigns discovery responsibility primarily to the on-site team: "the burden will primarily fall on myself, Srikar and Namita." He asks Saurav and Askari to "communicate any questions you might want to have answered at a reasonable clip" and route them through the on-site team members for in-person resolution. This creates a relay dynamic where the offshore team generates questions and the on-site team gets them answered.

### 6d. No Pre-Meeting Private Conversation

Unlike Set 08, there is no extended pre-meeting conversation between Saurav and Askari before Colin joins. The pre-meeting is just greetings (Saurav greets Srikar and Askari, Srikar says "Hey, Sarah. Good evening."). Colin joins at approximately 2:35 and the meeting begins. This may be because Srikar's presence as a new person changed the dynamic, or simply because Colin joined faster this time (2.5 minutes vs. 4 minutes in Set 08).

---

## 7. Hardware and Readiness Summary (Updated from Set 08)

| Person | BayOne Laptop | Cisco Laptop | BayOne Email | Status |
|--------|--------------|--------------|-------------|--------|
| Saurav | Yes | Yes | Yes | Fully hardware-ready. Most engaged questioner. Approaching one year at BayOne. |
| Askari | Yes (received since Mar 18) | Yes | Yes | Hardware-ready. Quiet in this meeting. Still listed at Ultratech in his intro. |
| Srikar | No (meeting Rahul Mar 31 or Apr 1) | Yes | No (Cisco email only) | On-site Bay Area. Missing BayOne hardware and email. Can join Teams as guest only. Expected resolution in "a couple of days." |
| Namita | Unknown | Unknown | Unknown | H1B pending. Expected to join week of April 6. Will be on-site Bay Area with Srikar. |
| Colin | Yes | Yes | Yes | Back from sales training. EST time zone. |
