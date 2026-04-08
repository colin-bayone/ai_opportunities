# 06a - Meeting: People

**Source:** /cisco/cicd/source/meeting_discovery_rama_2026-02-17.txt
**Source Date:** 2026-02-17 (Discovery meeting with Rama, same day as main discovery)
**Document Set:** 06a (Supplementary: Rama testing/automation meeting)
**Pass:** People identification

---

## Source Context

This is a speech-to-text transcript of a brief, informal discovery meeting that took place immediately after the main Set 06 discovery session (Colin with Anand, Srinivas, and Divakar). Divakar facilitated the introduction, bringing Rama into the conversation before departing. The meeting is casual -- it begins with Divakar walking Colin over to Rama's area, and ends with handshakes and a commitment to follow up with a demo.

The transcript quality is rough. Key corrections applied throughout:

- **"Ramagar"** = Rama (confirmed by Divakar saying "This is Rama" and multiple repetitions)
- **"Erwin" / "Erwin's team"** = Arun / Arun Kumar's team (confirmed by context: "Erwin, Erwin Kumar's work is network product validations" matches the Arun Kumar Singh identified in Set 06)
- **"AAPI"** = API (context: "Everything is AAPI based. AAPI, yes, people write scripts")
- **"Milesh"** = Nilesha (context: Nilesha is referenced in connection with NDFC and code modernization)
- **"Sonawee"** = likely a person's name (appears once, possibly a manager or director in Rama's chain)

---

## People Present in the Meeting

### 1. Rama

**Role:** Testing and automation lead at Cisco. Responsible for UI and API test automation across Nexus Dashboard Fabric Controller (NDFC) and related service provider controller products.

**First encounter.** Rama does not appear in Sets 01-06. He is introduced by Divakar as someone whose team does "testing on these devices" and who is "trying to take help of AI to automate."

**What this source reveals:**

**Domain and responsibility.** Rama manages testing for Cisco's network controller products -- specifically the Nexus Dashboard platform, which handles visualization, provisioning, and intent-driven network management. His scope covers:

- Service provider products: segment routing, traffic engineering
- Controller platforms: Nexus Dashboard (visualization, provisioning, intent-driven configuration)
- Enterprise controllers (referenced but not detailed)

He distinguishes his work from Arun's team explicitly:

> "Arun Kumar's work is network product validations. Like an extra switches. Your switches has its own functionality. Right. So that functionality, it has a CLI, it has to send to the device and the functional conformance."

Rama's domain is the controller layer, not the device layer. His tests validate that the controller correctly sends commands to devices, manages provisioning flows, and renders UI correctly. He says: "My intention is to send, kick in that CLI, because they have that through Nexus Dashboard, we'll be sending the command. My job will be done, that's it."

**Scale of operation.** Rama provides specific numbers:

- 30,000-40,000 test suites per product line, run daily
- One unified summary he shares shows 21,000 scripts in a single run, 25,000 for one controller group alone
- Six or more groups running simultaneously, totaling approximately 60,000 tests
- 10-12 engineers dedicated to daily analysis of results

These are not hypothetical numbers. Rama pulls up actual regression dashboards during the meeting and walks through them.

**Speaking style.** Rama is a practitioner who explains through examples. He builds his points inductively -- starts with a specific scenario ("say for example, UI. I'll give one example. There is a timeout."), walks through the mechanics, then generalizes to the problem statement. He does not speak in abstractions. When he describes the regression analysis problem, he walks through the exact workflow: Jenkins queues jobs, runs complete in 12 hours, results arrive, engineers have 3-4 hours to analyze, early cycle failures overwhelm that window.

He is transparent about pain points without being defensive:

> "If they find two or three comments, and they say quality is only 20%... people will be suspicious. Really? Did you analyze everything?"

This reveals the organizational pressure his team faces: they must demonstrate thorough analysis, and anything less than comprehensive coverage invites scrutiny from management.

**Openness to solutions.** Rama does not come into the conversation with a specific tool request. He presents three problem statements and asks for ideas. He listens to Colin's code graph topology explanation attentively, asks clarifying questions, and validates the approach:

> "I got what you mentioned. But yeah, I think that's a good part to fix this."

He also notes the practical constraint: "Yes, the executable commit may be, guys, you need to make structural changes on your core test, all these things, how you build the database kind of thing now. But that's good."

He is willing to accept structural changes to his test infrastructure if the payoff is real. He is not looking for a magic solution that requires zero effort on his side.

**Signals for the engagement:**

- **Rama is a potential expansion point.** His testing challenges are distinct from but adjacent to the CI/CD engagement with Arun's team. Colin explicitly connects the two: "This is part of what we're doing already for Arun's team."
- **He controls significant test infrastructure.** 60,000 daily tests across multiple product lines means his team is a major consumer of CI/CD pipeline capacity. Any CI/CD optimization that touches test execution, analysis, or selection directly impacts his operation.
- **He is a doer, not a political player.** He does not mention organizational dynamics, competing priorities, or budget. He talks about tests, scripts, failures, and analysis time. He will evaluate BayOne on whether the solutions actually work.

---

### 2. Divakar

**Role:** Same as Set 06 -- infrastructure gatekeeper. In this meeting, he serves as the facilitator who introduces Rama to Colin.

**What this source reveals (incremental to Set 06):**

Divakar's role here is connector. He walks Colin to Rama's area, provides the initial framing ("they're doing this testing on these devices... they wanted to understand, to see how AI can help them out"), and then steps out. He reappears briefly near the end.

His framing is deliberately open-ended. He does not prescribe a solution or set specific expectations. He says:

> "He can recommend something once he analyzes it."

This is Divakar creating space for Colin to operate. He trusts Colin enough after the main discovery session to make this introduction without needing to supervise the conversation. This is a signal of the rapport established in Phase 1 of the Set 06 meeting.

Divakar also provides the bridge context:

> "So, probably we can talk about Srinivas project, if you are okay with that?"

He frames the introduction as connected to the Srinivas engagement, not as a separate initiative. This suggests Divakar sees Rama's testing needs as adjacent to the CI/CD work and is deliberately creating a connection.

---

### 3. Colin Moore

**Role:** Same as Set 06 -- BayOne Director of AI, engagement lead.

**What this source reveals (incremental to Set 06):**

**Technical consulting in real time.** Unlike the Set 06 meeting where Colin was primarily in discovery mode (asking questions, recording answers), here he shifts into solution mode. He listens to Rama's three problem statements and immediately connects them to work he is already doing:

> "This is actually good, because this is part of what we're doing already for Arun's team."

He then explains the code graph topology approach -- how building a multi-dimensional graph of the code base and test suite relationships can answer regression impact questions without ad hoc analysis. He adapts the explanation to Rama's specific context:

> "Almost like a Venn diagram. Here's my actual code base and here are my tests. It shows up, so basically it's a relation."

He offers a concrete mechanism (the graph is state-aware, updates as code changes, works per-developer-branch) and connects it to the hierarchy/dependency distinction Rama raised about test failures.

**Demo offer.** Colin closes with a specific commitment:

> "One thing we can do, once we have some time to digest, I can actually, for that second and third use case, that's a fun one we can actually demo to you."

He identifies the UI testing (Use Case 2: automation) and theme change impact (Use Case 3) as demo-able. This is not a vague follow-up -- he is saying "we have tools that address this specific problem and I will show you."

**Bridging engagements.** Colin explicitly ties Rama's needs back to the Arun engagement twice:

1. "This is part of what we're doing already for Arun's team."
2. "We're already going to be doing pretty much the exact same thing on almost the same code base."

He then introduces the Nilesha connection: "There's also a work that we aren't actively doing right now that we propose to Nilesha's group. That was about a code-based modernization." He is building a picture for Rama where BayOne's existing and proposed work is relevant to Rama's problems, not pitching something new.

**Consulting instinct: skip the non-problem.** Colin's first move after hearing the problem statement is to check whether selective regression testing (choosing which tests to run) is a pain point. When Rama says it is already handled ("We call SRT, selective regression testing... that is the selective regression"), Colin immediately moves on:

> "But if that's not a pain point, we can just skip over that."

This is effective consulting: do not solve problems the client does not have. Rama confirms they already have SRT based on code commit analysis, and Colin pivots to where the actual pain is -- the analysis of results.

---

## People Referenced But Not Present

### 4. Nilesha

**Role:** Cisco lead responsible for both NDFC CI/CD and a code modernization initiative. Connected to Rama's domain.

**What Colin says:**

> "There's also a work that we aren't actively doing right now that we propose to Nilesha's group. Nilesha, we propose. That was about a code-based modernization."

**What Rama says:**

> "Nilesha is doing the CICD? Oh yeah, I think so, yes."

And:

> "Milesh is asking me, in the nation, Sonawee, they were asked, they are mad master. They said, you need to move the needle on the UI automation."

Nilesha emerges as a cross-cutting figure. She has a CI/CD scope (confirmed by Rama: "Nilesha is doing the CICD") and a code modernization scope (Colin's prior proposal). She is also connected to the pressure on Rama's team to improve UI automation. The "move the needle on UI automation" directive appears to come from Nilesha's chain of command (possibly "Sonawee," a person higher in the org).

**Significance:** Nilesha is a potential nexus between three workstreams:

1. The Arun/Srinivas CI/CD engagement (BayOne's current scope)
2. The code modernization proposal (BayOne's proposed scope)
3. Rama's testing automation needs (newly discovered scope)

If Nilesha's CI/CD work overlaps with Arun's, there may be coordination needed. If her code modernization initiative proceeds, it could create a second engagement pathway for BayOne. She is the person who connects the CI/CD pipeline side to the test automation side.

---

### 5. Arun (Arun Kumar Singh)

**Role:** Same as Set 06 -- VP at Cisco, Rui's manager, budget authority for the CI/CD engagement.

Referenced by Rama to distinguish their respective domains:

> "Arun Kumar's work is network product validations. Like an extra switches."

Rama is clear that his work (controller-level testing) is distinct from Arun's (device-level validation), but they share infrastructure: "I think actually our work touches each other from my understanding."

This confirms what was ambiguous in Set 06: Arun's team focuses on switch/device validation, while Rama's team focuses on controller/dashboard validation. The CI/CD pipeline serves both, which is why improvements to the pipeline benefit both domains.

---

### 6. "Sonawee" (Unresolved)

Referenced once:

> "Milesh is asking me, in the nation, Sonawee, they were asked, they are mad master. They said, you need to move the needle on the UI automation."

The speech-to-text quality makes this difficult to parse. "Sonawee" appears to be a person's name -- possibly a director or senior manager who is driving the UI automation push. The phrase "they are mad master" likely means something like "they are the master / they own this decision." The key fact is that pressure to improve UI automation is coming from above Rama, through Nilesha's organization.

---

## Revised Relationship Map (Incorporating Set 06a)

```
Cisco Side                                       BayOne Side
----------                                       -----------
Venkat (VP, Anand's boss)                        Colin Moore (Director of AI)
  |                                                + presented code graph approach
  +-- Anand (sponsor, budget holder)               + offered demo for UI testing
  |     |                                          + bridged Rama's needs to CICD
  |     +-- Srinivas (technical visionary)
  |     |     +-- DeepSight platform
  |     |     +-- Rui (CI/CD app)
  |     |
  |     +-- Divakar (infrastructure gatekeeper)
  |           + facilitated Rama introduction
  |
  +-- Arun (VP)
  |     + device-level validation (switches)
  |     + Rui reports here
  |
  +-- Nilesha (NDFC)
  |     + CI/CD scope (confirmed by Rama)
  |     + code modernization (BayOne proposal)
  |     + UI automation pressure on Rama
  |
  +-- Rama (testing/automation lead)
  |     + controller-level testing (Nexus Dashboard)
  |     + 30-40K test suites daily per product line
  |     + ~60K total across all groups
  |     + 10-12 engineers on analysis
  |     + Python, Selenium, Cisco automation libraries
  |     + Three problem statements:
  |       1. Regression analysis (time/cost)
  |       2. UI automation (manual to automated)
  |       3. UI theme changes (4,000+ script impact)
  |
  +-- "Sonawee" (unclear role, above Rama)
        + driving UI automation mandate
```

**Key relationship:** Rama and Arun's teams are distinct but share infrastructure. Rama says: "I think actually our work touches each other." The CI/CD pipeline serves both device validation (Arun) and controller testing (Rama). BayOne's work for Arun's team has direct applicability to Rama's domain.

---

## Working Style Summary

| Person | Pace | Communication | Key phrase |
|--------|------|---------------|------------|
| Rama | Methodical, example-driven | Builds from specific cases to general problems; transparent about constraints | "Analysis is the key thing. That is where the time is spent." |
| Divakar (in this meeting) | Brief connector role | Open-ended framing, trusts Colin to operate independently | "He can recommend something once he analyzes it." |
| Colin (in this meeting) | Solution-oriented | Bridges existing work to new problems; skips solved areas; offers demos | "This is part of what we're doing already for Arun's team." |
