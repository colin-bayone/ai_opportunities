# 08 - Internal Meeting: Briefing Content and Ground Rules

**Source:** /cisco/cicd/source/internal_team_meeting_2026-03-18.txt
**Source Date:** 2026-03-18 (First internal team briefing)
**Document Set:** 08 (Internal team meeting — Colin, Saurav, Askari)
**Pass:** What Colin communicated, how he framed it, and ground rules established

---

## Source Context

This document captures the substance of what Colin communicated to his team during the first internal briefing, how he framed it, and what he chose to include or exclude. Most of the factual content about the engagement was already captured in Sets 01-07. This document focuses on Colin's editorial choices — what he emphasized, what he simplified, what he characterized, and what he omitted entirely.

---

## 1. How Colin Frames the Engagement

### The Opening

Colin does not start with the technical problem. He starts with logistics (hardware check), then ground rules, then people, and only then gets to the technical scope. This ordering is deliberate — he establishes the operating framework before getting into the work itself.

### Framing the Client

Colin consistently demystifies Cisco throughout the briefing:

- **The codebase.** "Are there 10 million lines of code? Maybe. Are there 10 million lines of active code? No, not a chance." He attributes the number to counting duplicates and possibly JAR files. He tells them not to be "freaked out" but also not to take it lightly because of git traffic implications. This is calibrated — he removes the intimidation factor without dismissing the genuine complexity.

- **The team.** "You're working with some really, really good engineers on their team" — but then immediately positions Saurav and Askari as peers, not subordinates: "See yourself as their peer. You're the person that they're hiring to tell them what the heck to do because they don't know."

- **Their problems.** "They like to think they have the hardest problems in the world. I disagree." He frames Cisco's issues as primarily organizational dysfunction dressed up as technical complexity: managers ignoring the CDT, no documentation, no visibility, governance gaps.

- **Their capabilities.** He debunks DeepSight's maturity. The platform looks polished but the applications are "not real" — they are placeholder "coming soon" blocks. He positions this as an opportunity rather than a weakness.

### Framing the Opportunity

Colin frames the engagement as both a delivery obligation and a relationship-building exercise:

- **Deliver on the SOW:** Cover the six use cases, show progress by April 30.
- **Win Srinivas's loyalty:** "If we put applications on the screen for him, big or small, even if they're not related to the project, that guy will love us and we will get business coming out of our ears."
- **Cost optimization as a differentiator:** He plans to tell Srinivas to stop using API keys and switch to Vertex or Azure Foundry for a potential 20x cost reduction. "If I can give you a 20X cost reduction on AI, they're gonna be pretty happy with us."
- **Expansion potential:** He mentions having "four other projects just at Cisco" beyond this engagement.

---

## 2. Coverage of the Six Use Cases

Colin walks through all six problem statements from the SOW. He does not skip any. However, his depth of coverage varies significantly.

### Covered in detail (significant discussion time)

**1. Developer visibility (Blue Box — Problem 1).** Colin breaks this into three sub-dimensions: progress tracking, unit test execution awareness, and current state visibility. He connects this to the 750-developer scale problem and the endless scrum meetings required because there is no tooling-level insight. He also notes the manager KPI desire and preemptively addresses Saurav's Big Brother concern.

**2. Automated debugging of failing unit tests (Blue Box — Problem 2).** Colin frames this as low-hanging fruit that Cisco's traditional developers perceive as "magic" even though tools like Claude Code and Codex already do it. He asks the team to "put your sensibility aside" because the Cisco developers genuinely do not know this is possible.

**3. PR visibility and gate governance (Green Box — Problems 3-4).** This receives the most detailed walkthrough. Colin explains:
- The CDT (Context Driven Testing) system — rule-based test selection by file type
- The 39 review gates — manager-created, inconsistent across teams, unknown to developers
- How the two systems coexist dysfunctionally: most teams use CDT, but a subset of managers bypass it entirely and select gates manually
- The developer's blind spot: developers do not know which gates apply to their commit, get rejected without explanation, and have to wait for their manager to manually explain what failed
- Colin explicitly says CDT is "Srinivas's baby" — a political consideration for how they approach improvements

**4. Self-healing and auto-resume (Red Box — Problem 5).** Colin introduces a three-tier framework not previously documented:
- **Type 1:** RCA only, no action taken. Informational triage.
- **Type 2:** Deterministic action via dashboard. Button-click to retry builds, execute terminal commands. No AI decision-making.
- **Type 3:** AI-driven self-healing. Colin flags this as requiring governance that Cisco has not defined. He recounts asking Cisco "what should AI be able to do?" and getting the answer "just low risk things." He pushed back: "how do you define low risk?" Cisco said "AI will decide." Colin says: "that's a horrible idea. This is production."

  He frames his caution as protecting BayOne: "if we just say OK, you're the boss, you said so, and our AI agent goes and screws up their production deployment, they're gonna come for our heads."

**5. Coverage tracking (Green Box — Problem 6).** Colin ties this back to the CDT discussion. Srinivas claims CDT is mature (2+ years), but Colin reads the contradiction in the data: "he says it's been alive, it's mature for two plus years, and yet people still don't use it... can't actually say that the right test was run. That doesn't make logical sense." He positions the discovery phase as the place to investigate this.

### Covered briefly

**Unit test coverage tracking (Blue Box — Problem 3).** Mentioned as part of the developer box walkthrough. Two dimensions: git diff (what changed) and whether new functions have unit test coverage. Saurav raises the stale unit test problem, which Colin validates and uses to introduce the concept of state-aware unit test structures.

### Not reached

Colin ran out of time before going through the formal plan of attack document. He acknowledges this: "What I'll do is I'll send the documents out to everyone so you can read them at your leisure. So when we meet next, we'll go through what the actual plan of attack is."

---

## 3. Key Contacts — How Colin Characterized Them to the Team

### Srinivas Pitta (Cisco — Director of Engineering)

Colin presents Srinivas with a mix of respect and strategic candor:
- "Our main point of contact for this project"
- Built the DeepSight/Atlas platform — "his baby"
- AI lead for all of Cisco: "for the whole company, he's in charge of things"
- Under competitive pressure internally: "Cisco is a very large company with a lot of very smart people and a lot of people that want to differentiate themselves in AI. So the poor guy's got to always be running as lead on a race where everyone else is running very fast too."
- Needs applications on his platform desperately: "he needs people to use his stuff and he doesn't have anything on the platform"
- Strategic advice: show enthusiasm for DeepSight because "it's like his baby" and "if we do that for him, he'll be a very happy person"

This characterization is accurate to Sets 01-06 but notably kinder in tone than some of the internal discussions in Set 04, where the DeepSight platform received more skeptical treatment.

### Divakar Rayapureddy (Cisco — Build Infrastructure)

- "The owner of this red box" (build automation)
- His team runs Jenkins builds with Bazel as optimizer
- Colin uses Divakar's own example to explain the fire-and-forget problem: "the devocker's example himself was that developers push 5 bug fixes on different branches, but he has no clue as a consolidated view where they're at"
- Presented as a collaborator, not a bureaucratic obstacle (contrast with Set 07, where Divakar was absent from the group chat for 38 of 49 days)

### Anand Singh (Cisco — Senior Director)

- "Srinivasan's boss"
- "Really nice"
- "Still extremely senior at Cisco" — "truly senior in that sense"
- Colin expects periodic meetings with Anand and promises dress rehearsals before those

### Arun Kumar (Cisco — VP)

- Reports to C-suite
- "Super cool to get him on calls. I've met him. He's really, really a nice guy, but definitely very far away from the action."
- Colin raises a question about whether "Arun Kumar" is truly his full name or a transcript artifact from Zahra's notes — shows his attention to detail on Indian naming conventions

### Zahra and Neha (BayOne — Sales)

- Described as "almost like celebrities at Cisco"
- "I don't know what those girls have going on, but I will tell you right now, they walk around Cisco, say hi to everyone under the sun"
- Positioned as intelligence assets: "our eyes and ears that can go and get us information from any team so that we don't have to hunt people down on Webex"
- "They do come from more of a sales and client facing background — think about them as our portal to talk to other people, more so than people that are technically involved with anything"

### Rahul Bobbili (BayOne — "R2")

- Nickname explained: "we call him R2 because our maybe former president Rahul Sharma, he's Rahul"
- "Amazing guy, crazy nice"
- Positioned as the escalation path: "if there's anything that needs escalated, if you have any problems with anything, he can help you out"
- Framed as backup to Colin: "even if I'm not available for some reason, if he is available at all, he's extremely prompt"
- "And I got hit by a bus — he's a good person to reach out to as well"

---

## 4. Ground Rules Established

Four explicit ground rules, documented in detail in the people/dynamics file (08_internal_people_and_team_dynamics). Summary:

1. **Do Cisco work on Cisco hardware.** One-way door — material can go onto Cisco laptop, should not come off it. Prototyping on BayOne hardware is fine. API keys will not be detected.
2. **Interact directly with Cisco as peers.** Respectful but vocal. Colin will not be the sole voice in meetings.
3. **Webex for Cisco communication, Teams for internal.** Dual-platform reality acknowledged and managed.
4. **Escalate early.** Never a bother. Tied to the April 30 renewal and the need to show progress.

---

## 5. Technical Architecture Walkthrough

Colin walks through the CI/CD pipeline using Cisco's own diagram (described as a "big ugly picture"). He covers:

- **Blue Box (Developer):** Local development on laptops. Git commit and push to GitHub. Currently a mystery to management.
- **Green Box (GitHub Enterprise):** PR review, CDT, 39 gates. Hosted on-prem, requires VPN, otherwise identical to standard GitHub.
- **Red Box (Build Infrastructure):** Jenkins + Bazel. Virtual machine builds. Divakar's domain. BayOne will have access to run isolated builds.
- **Airflow:** Orchestrator for all handoffs after the green box. "Everything is being orchestrated through Apache Airflow."
- **Grafana/Prometheus:** Exists only as the out-of-the-box Airflow toggle. Not real dashboards. "When you see this and it looks like they have some analytics and telemetry, think of it as like the most basic out-of-the-box version of that."
- **The broken workflow:** "Commit from users" arrow explained as managers bypassing normal PR flow to manually fix unit test failures and push directly. Colin says this will be corrected as part of the engagement.
- **All on-prem except AI models.** AI models and tools are unrestricted. Cisco will provide cloud accounts (Claude, etc.) via Cisco ID. VS Code is the universal IDE — all developer-facing work must be native to VS Code.

### Constraints explicitly stated
- No external platforms (Cisco builds everything in-house)
- No GitHub Actions (Colin tried, was rejected — political, not technical)
- No change management for developers (hence VS Code plugins, not new tools)
- Jenkins is acknowledged as outdated but not being replaced
- Must use the DeepSight/Atlas platform

### Solution architecture preview (not fully covered)
- VS Code plugins for developer-facing interface
- Manager-level observability web app (later phase)
- MCP connectors to standard tools (Jenkins, Airflow, Grafana, GitHub)
- Chat-like interface for querying system status (Cisco's "dream state")
- Airflow for background data collection and status aggregation
- Cost dashboard as a value-add suggestion

---

## 6. What Colin Chose NOT to Tell the Team

This is the most analytically important section. Comparing what Colin says in this briefing against the full knowledge base from Sets 01-07 reveals deliberate editorial choices.

### Not mentioned: BayOne internal politics (Set 04)

Colin makes no reference to:
- Zahra's devastation of Amit's proposals
- The "raw chicken" quality complaints
- BayOne's organizational dysfunction
- The Zahra-Colin direct channel formed to work around internal dysfunction
- Amit's two-onshore proposal that Colin challenged
- Rahul Sharma's role or any internal BayOne tension

The team hears "Zahra and Neha" as helpful celebrities and "R2" as a nice escalation contact. They receive zero indication of the organizational challenges on the BayOne side.

### Not mentioned: Sarang's failure (Set 02)

Colin never names Sarang. He never mentions that a prior BayOne consultant was on this project and failed. He does not reference the "almost zero actual familiarity" assessment, the access problems Sarang faced, or any of the cautionary context from Set 02. The team starts fresh with no awareness that this engagement has a prior failure embedded in its history.

### Not mentioned: Pricing and commercial terms (Sets 02, 04)

No budget numbers. No mention of $100K, $150-200K, or any pricing. No discussion of margins, BayOne rates, or the SOW structure. Colin frames the April 30 date as a "renewal date" but does not discuss the financial implications.

### Not mentioned: Venkat (the VP)

Colin names Arun Kumar as the VP but does not mention "Venkat" — the name used extensively in Set 04. This may be because Arun Kumar IS the VP (with Venkat being a different person or an older reference), or it may reflect Colin choosing not to get into the full org chart complexity at this stage.

### Not mentioned: The Guhan/Selva expansion (Set 05)

No reference to the $7M R&D opportunity, Guhan, Selva, or the broader expansion strategy. Colin does mention "four other projects just at Cisco" but does not name or describe any of them.

### Not mentioned: The procurement delays as BayOne's problem

Colin frames the late start as Cisco's procurement dragging its feet: "Cisco procurement dragged their feet for a month as procurement teams always do." He does not reference the full complexity visible in Set 07, where the SOW was also delayed on the BayOne side (Zahra said "this week" on March 3 and it was not resolved until later).

### Summary of editorial strategy

Colin is giving his team exactly what they need to start working and nothing that would distract, demoralize, or politically complicate their relationship with BayOne or Cisco. He removes all the noise — the internal dysfunction, the prior failure, the pricing tension — and presents a clean, exciting, well-structured engagement with clear rules and supportive contacts. This is a deliberate management choice and a healthy one for team onboarding.

---

## 7. Action Items from the Meeting

### For Saurav and Askari
1. **Review the DeepSight/Atlas platform recording.** Srinivas's 2-hour webinar. Colin does not expect them to watch the whole thing but the transcript will be provided for Claude processing.
2. **Review the documents Colin will share.** Including the plan of attack document they did not cover in the meeting.
3. **Get BayOne laptop set up** (Askari only — laptop shipped March 18).

### For Colin
1. **Send all documents** discussed in the meeting to both team members.
2. **Send the DeepSight webinar link and transcript.**
3. **Send a "who's who" sheet** of all Cisco contacts.
4. **Set up Webex teams** once all accounts are ready.
5. **Schedule next meeting** for March 19 (Thursday) instead of Friday, to accommodate Eid.
6. **Set up a shared repository** for transcripts, summaries, and project knowledge.

### For next meeting
- Walk through the formal plan of attack / solution document.
- Get Srikar into the loop (expected to be onboarded by then).
