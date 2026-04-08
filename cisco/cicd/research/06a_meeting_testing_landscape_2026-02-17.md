# 06a - Meeting: Testing Landscape and Use Cases

**Source:** /cisco/cicd/source/meeting_discovery_rama_2026-02-17.txt
**Source Date:** 2026-02-17 (Discovery meeting with Rama)
**Document Set:** 06a (Supplementary: Rama testing/automation meeting)
**Pass:** Testing problems, scale, tools, and connection to CICD engagement

---

## Source Context

This document extracts the testing landscape, scale, tooling, and problem statements from the Rama discovery meeting. Where the 06a People document focuses on who is in the room and how they relate, this document focuses on what Rama's team does, what problems they face, and how those problems connect to the existing CI/CD engagement.

---

## 1. What Rama's Team Tests

Rama's team tests Cisco's network controller products -- the software layer that manages network devices. This is distinct from device-level validation (Arun's domain, which tests whether switches and routers behave correctly at the CLI/functional level).

### Product scope

Rama describes three categories of controller applications:

1. **Visualization** -- UI-based dashboards for viewing network state. "Visualization, everything is based on the UI."
2. **Provisioning** -- Configuring and deploying network changes. Can be done via API or UI. "Provisioning, you can do either API or UI. But customers can choose anything."
3. **Intent-driven configuration** -- Higher-level orchestration where the user specifies a desired outcome and the controller handles the steps. "Intent-driven things you give it to the products."

These three functions run across multiple business units:

| Business unit | Products | Controller |
|---------------|----------|------------|
| Service provider | Segment routing, traffic engineering | Service provider controller |
| Data center (Nexus) | Nexus features, switches | Nexus Dashboard Fabric Controller (NDFC) |
| Enterprise | Enterprise routers, enterprise switches | Enterprise controller |

Rama's statement: "Every business unit, whatever they are making the products, network management now is involved with SDN products, software-defined networking."

### Scale

The numbers Rama provides are specific and repeated for emphasis:

- **30,000-40,000 test suites per product line** -- This is the daily regression load for a single controller product.
- **21,000 scripts in one unified summary** -- Rama shows this during the meeting from his actual dashboard.
- **25,000 for one controller group** -- The Nexus Dashboard controller alone runs 25,000 tests.
- **~60,000 total across all groups** -- "You have six other groups, everybody running, it's almost 60,000 tests being run."
- **10-12 engineers dedicated to daily analysis** -- "Almost 10 engineers are looking into, or 12 engineers are looking into each line, each day."
- **12-hour run cycle** -- Jenkins queues the jobs; runs complete in approximately 12 hours.
- **3-4 hour analysis window** -- Engineers have 3-4 hours after runs complete to analyze results before the next cycle begins.

### Customer impact examples

Rama provides a concrete scenario to illustrate scale:

> "Carnival, they are installing, they want to deploy 200 switches. If you want to go and configure manually, it will take three months. Or even if you have the scripts, it will take two weeks, three weeks. But with the Nexus Dashboard, minutes."

The Nexus Dashboard controller is a customer-facing product that eliminates weeks of manual configuration. Failures in this product directly impact Cisco's enterprise customers. This is why the testing is not optional and cannot be reduced without risk.

---

## 2. Three Problem Statements

Rama presents three distinct testing challenges. He organizes them himself during the conversation, and Colin later references them as "first, second, and third use case."

### Problem 1: Regression Analysis (Time and Cost)

**The problem:** When 30,000-40,000 tests run nightly, the bottleneck is not execution -- it is analysis. Engineers must determine why tests failed, whether failures are product bugs or test infrastructure issues, and which failures are interconnected.

**The workflow Rama describes:**

1. Builds are created by 9 PM.
2. Jenkins automatically queues and runs test suites.
3. Runs complete in ~12 hours.
4. Results arrive when India-based engineers are starting their day.
5. Engineers have 3-4 hours to analyze before end of their shift.
6. Early in the release cycle, failure rates are high. Analysis cannot complete in the available window.

**The organizational pressure:**

> "It brings the chaos also, saying that, hey, you guys ran 30,000, but you are giving me analysis for only 2,000."

And:

> "If they find two or three comments, and they say quality is only 20%... people will be suspicious. Really? Did you analyze everything?"

Managers expect comprehensive analysis. When the failure rate is high, the analysis team cannot keep pace. This creates a credibility problem: partial analysis looks like laziness, even when it reflects a genuine time constraint.

**What Rama wants:** An AI-assisted system that can perform first-pass failure analysis -- grouping related failures, identifying root causes that cascade across multiple test suites, and triaging product bugs from test infrastructure issues. This would free engineers to focus on complex, ambiguous failures rather than spending time on obvious cascading failures.

**Rama's specific example:**

> "UI. I'll give one example. There is a timeout. Every screen, when you run, if there is a product bug, and the same bug, because of that, when you launch, it is giving the same thing, error on the box. And we are not able to continue. For that, we have almost 60 different test rates. And so many test cases, people need not to do that. If there is some AI tool which can look into the results, okay, this is the part, it is impacting these many, 2,000 test cases."

One product bug causes a timeout that cascades across 60 test suites and 2,000 test cases. Today, engineers discover this through manual analysis. An AI tool could identify the root failure and its blast radius immediately.

**Rama's characterization:** "Regression analysis is one of the costly functions. Where our op-ex is being a little bit overspent."

---

### Problem 2: UI Automation (Manual to Automated)

**The problem:** Rama's team faces organizational pressure to increase UI test automation. The directive comes from above -- through Nilesha's organization:

> "Nilesha is asking me... they said, you need to move the needle on the UI automation."

Currently, API-based testing is well-established: "Everything is API based. API, yes, people write scripts and that's okay." But UI testing lags behind. UI automation is "not impossible, but it is a more laborious work."

**Current tooling:**

- **Python** -- Primary scripting language for test automation
- **Selenium** -- UI automation framework in use
- **Cisco internal automation infrastructure layer** -- A Python library used across Cisco. "There is a Cisco, there is an automation infrastructure layer for Python. We use that libraries pretty much."
- **GitHub** -- Cross-Cisco sharing of automation libraries. "If I write something, I can put in the GitHub repository. Across Cisco anybody can use it."

**What Rama wants:** Code generation tools or AI-assisted approaches to accelerate UI test creation. He references copilot and code generation tools: "Either you can use copilot or something, code generation tools, repeated things. That's what they're asking me to do."

**Colin's response:** He offers to demo BayOne's UI testing capabilities for this use case specifically: "For that second and third use case, that's a fun one we can actually demo to you."

---

### Problem 3: UI Theme Changes Impacting Test Scripts

**The problem:** When the UI team changes the visual theme (colors, backgrounds, element styling), it breaks existing test scripts. The most recent example: the UI is moving from a light theme to a dark theme.

> "For example, they made one change, simple change on the UI, certainly it required me almost 4,000 scripts I have to modify."

**Why this is hard:** Theme changes are not functional changes -- the underlying provisioning or visualization logic is unchanged. But UI tests that rely on visual elements (element identification, screenshot comparison, color-coded thresholds) break when the theme changes.

**Rama's specific examples:**

- Light-to-dark theme transition requiring 4,000 script modifications
- Color-coded network health indicators: "Three thresholds will be there. If traffic thresholds are certain bandwidth... then it's a green, certain threshold level, it's a red or yellow. Does the same schema apply to different color theme? May not be."
- Map visualizations where dark theme changes lettering visibility: "GPS they have, night and day time, they have different colors. So then if you can't see the lettering, that map directions and then screws up."

**The dual problem:** Theme changes create two categories of test failure: (1) tests that break because they reference hardcoded visual elements that changed, and (2) legitimate product bugs where the theme change was not properly applied to all UI components (missing color mappings, unreadable text on new backgrounds). The team must distinguish between the two.

**Rama's characterization:** This is the newest of the three problems. It is driven by an active product decision (theme migration), not a standing operational concern.

**Colin's response:** He groups this with Problem 2 as demo-able: "That's a fun one we can actually demo to you... I know it's kind of brittle, almost. There's always a testing. It's brittle to do UX, UI testing."

---

## 3. Existing Solutions and Internal Tools

### Selective Regression Testing (SRT)

Rama confirms that Cisco already has a mechanism for selecting which tests to run based on code changes:

> "We call SRT, selective regression testing. This is based on the code changes what you make."

When a developer commits a bug fix, the system identifies which area of the code changed and triggers only the relevant test suites. Rama says this is already implemented for at least some groups: "I think that is the one enterprise and AS and NK, they used to have that."

**Significance:** Colin's first instinct was to check whether test selection was a pain point. It is not. SRT is already in place. The pain is downstream: analyzing the results of the tests that do run.

### Cisco Circuit (Internal AI Platform)

Rama references Cisco's internal AI platform:

> "Cisco, internally, there is a circuit, which is the AI kind of... it is master of all AI tools putting together. Copilot, and Windsurf, and all these works over there."

Circuit aggregates AI tools (Copilot, Windsurf, others) into a unified interface that queries from Cisco's internal database. Some teams have attempted to use Circuit for test-code matching ("looking at code, what we, the test code, and what developers are giving the software, the matching to that"), but Rama says these attempts have not addressed his actual problems: "But that is not really fitting to what we are looking at."

### Prior AI Attempts

> "Already the initiatives were there, and some companies were making some attempts on this one."

External vendors have tried to solve regression analysis through code-level matching. Rama is diplomatic but clear that these approaches did not work for his use case. The implication is that a naive "match test code to product code" approach is insufficient because the relationships between tests and failures are more complex than simple code correlation.

---

## 4. Colin's Proposed Approach: Code Graph Topology

Colin presents a specific technical approach during the meeting: building a graph topology of the code base and test suite relationships. This is not a vague suggestion -- he describes the mechanism in detail.

### The concept

> "One thing that we do to start out that work is we build essentially a graph topology of the space. This is the existing test cases and this is something that's multi-dimensional."

The graph maps relationships between:
- Source code files and their dependencies (library relationships, import chains)
- Test suites and the code they cover
- Hierarchical and lateral failure dependencies

### Key properties Colin emphasizes

**State-aware and live-updating:**

> "The trick to it is to not do it ad hoc. So for us, what we do is we'll preserve that, and it's state-aware. So whenever the code changes, the graph changes."

The graph is not a one-time snapshot. It updates as the code base changes, even tracking per-developer-branch variations ("even if it's on a specific developer's branch, because 90% of the graph is the same").

**More efficient than regex:**

> "It's actually more efficient than just something like a Regex, because Regex is nice and simple."

Colin acknowledges the pragmatic appeal of simpler tools but argues that a persistent graph can answer questions that ad hoc text matching cannot -- specifically, the hierarchical and cascading failure relationships that Rama described.

**Answers the "what is the blast radius" question:**

> "If you have this graph and it's live updating as the code changes... now you can say, because this changed, here are the ones that are relevant that should be activated. Or if it's a test that fails, now I know the hierarchy, which one is essentially the primary affected party from the code change."

This directly addresses Rama's cascade problem: one product bug causing 2,000 test failures. The graph can identify the primary failure and mark downstream failures as secondary -- eliminating the need for engineers to manually trace those dependencies.

**Answers the "what does a UI change cost" question:**

Rama gives a use case where the UI team asks: "Hey Rama, how much time or how much is this effort for reflecting in your scripts?" Today, Rama cannot answer without manual analysis. Colin says the graph can answer this:

> "Rather than asking me, if you were that graph, multi-dimensional table. This is the test repository, it will impact this much with your work. It can answer that."

### Rama's response

Rama validates the approach but flags the practical cost:

> "Yes, the executable commit may be, guys, you need to make structural changes on your core test, all these things, how you build the database kind of thing now. But that's good."

He understands that adopting the graph approach will require his team to restructure how they organize tests and track dependencies. He accepts this trade-off.

### Connection to existing BayOne work

Colin explicitly connects this approach to two existing workstreams:

1. **The CI/CD engagement (Arun's team):** "This is part of what we're doing already for Arun's team."
2. **The code modernization proposal (Nilesha's group):** "There's also a work that we aren't actively doing right now that we propose to Nilesha's group. That was about a code-based modernization... for unit test generation and coverage."

The code graph topology is the common technical foundation across all three contexts: CI/CD pipeline optimization (Arun), test coverage and unit test generation (Nilesha), and regression analysis and UI test management (Rama).

---

## 5. Relationship Between Rama's Domain and Arun's Domain

Rama draws a clear distinction between his testing scope and Arun's:

| Dimension | Arun's team | Rama's team |
|-----------|-------------|-------------|
| **What they test** | Switches and routers (device-level) | Controllers and dashboards (platform-level) |
| **Test focus** | Functional conformance -- CLI commands, algorithm behavior | User intent flows -- provisioning, visualization, UI |
| **Interface** | CLI, device interaction | UI, API, Nexus Dashboard |
| **Failure mode** | Device does not behave as specified | Controller sends wrong commands, UI renders incorrectly |

However, the two domains overlap in infrastructure:

> "I think actually our work touches each other from my understanding."

Rama sends commands through the Nexus Dashboard that ultimately execute on the devices Arun's team validates. If a device-level failure occurs, Rama's controller tests may also fail -- not because the controller is broken, but because the device it targets is. This creates a cross-domain dependency that complicates failure analysis.

**Significance for the CI/CD engagement:** The CI/CD pipeline serves both domains. Improvements to failure attribution, test selection, and analysis automation benefit both Arun's device-level validation and Rama's controller-level testing. BayOne's work on the pipeline is not domain-specific -- it is infrastructure-level, which is why it applies to both.

---

## 6. Tool Inventory

| Tool | Purpose | Notes |
|------|---------|-------|
| **Python** | Primary scripting language for test automation | Used across Rama's team and broadly across Cisco testing |
| **Selenium** | UI automation framework | Currently in use for UI tests; Rama considers it laborious for scaling |
| **Cisco automation infrastructure layer** | Internal Python library for test automation | Shared across Cisco via GitHub; provides common abstractions |
| **GitHub** | Cross-Cisco code and library sharing | "If I write something, I can put in the GitHub repository. Across Cisco anybody can use it." |
| **Jenkins** | Test execution orchestration | Automatically queues and runs the 30-40K daily test suites |
| **Cisco Circuit** | Internal AI platform | Aggregates Copilot, Windsurf, other AI tools. Used for prompting against Cisco's internal database. Not currently solving Rama's problems. |
| **SRT (Selective Regression Testing)** | Code-change-based test selection | Already implemented for some groups (enterprise, AS, NK). Reduces test volume by selecting relevant suites based on code commits. |

---

## 7. The Dual Nature of the Controller Test Problem

An important nuance that emerges from Rama's explanation: his tests sit at a layer where failures can originate from three different sources.

1. **Controller bug** -- The Nexus Dashboard itself has a defect in provisioning, visualization, or intent-driven logic.
2. **Device bug** -- The underlying switch or router is not behaving correctly, causing the controller's commands to fail.
3. **Test infrastructure issue** -- The test script itself is broken, outdated, or referencing stale UI elements.

Rama acknowledges this complexity:

> "Is it a product failure or your script failure? So such kind of things, that analysis is the key thing."

And when discussing cross-device correlation:

> "You are using three different products... and one entity is the 40 [failing] because of that, that symptom is being reflected on the UI."

This three-source failure model is why simple test-code matching (the approach prior vendors attempted) does not work. The failure might not be in the test or the code under test -- it might be in a device two layers below the controller. The graph topology approach Colin proposes addresses this by mapping relationships across all three layers.

---

## 8. Gaps and Open Questions

1. **Rama's organizational position.** He describes his work and team but does not specify his title, reporting chain, or budget authority. He appears to be a test lead or test manager, but whether he can independently authorize BayOne work or needs approval from someone above him (possibly "Sonawee" or Nilesha) is unclear.

2. **The Nilesha connection details.** Colin references a code modernization proposal to Nilesha's group. Whether this proposal was accepted, rejected, or is pending is not stated. Nilesha's CI/CD scope and how it relates to Arun's CI/CD scope is also ambiguous.

3. **Demo follow-up.** Colin committed to demoing UI testing capabilities for Problems 2 and 3. Whether this demo occurred, when, and what Rama's reaction was is not in this transcript.

4. **Budget and authorization.** No commercial terms are discussed. This meeting is purely a problem-discovery conversation. Whether Rama's testing needs would be funded through the existing Arun/Anand CI/CD engagement or require a separate scope/budget is unknown.

5. **Scale specifics per product line.** Rama gives totals (60K across all groups) but does not break down which product lines run the most tests, which have the highest failure rates, or which are the best candidates for a pilot.

6. **SRT coverage.** Selective Regression Testing is in place for "enterprise and AS and NK" but whether it covers all of Rama's product lines, and how effective it is at reducing volume, is not specified.
