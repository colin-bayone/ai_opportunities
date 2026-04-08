# Meeting 2: Regression Testing & UI Automation with Rama

**Date:** February 17, 2026
**Location:** Cisco Office, 3rd Floor (in-person, Room 73)
**Duration:** ~20-25 minutes
**Recording Status:** Not recorded

---

## Participants

| Name | Organization | Role | Scope in Meeting |
|------|--------------|------|------------------|
| Colin Moore | BayOne | Director of AI | Technical discussion, solution ideation |
| Rama (Ramagar) | Cisco | Test Manager, Nexus Dashboard | Problem statement presenter, domain expert |
| Rahul Bobbili | BayOne | Delivery | Facilitator, introductions |

**Context:** Rahul connected Colin with Rama opportunistically during the on-site visit. This is a separate project from the CI/CD work with Arun's team, but has significant technical crossover.

---

## Meeting Context

**How This Meeting Happened:**
Rahul was walking Colin around and saw an opportunity to connect him with Rama ("If you're available, we'll get you connected to our AI person"). Informal, opportunistic introduction.

**Rama's Domain:**
- **Team:** Nexus Dashboard testing (network controllers)
- **Scope:** UI and API testing for SDN (Software-Defined Networking) controllers
- **Products:** Visualization, provisioning, and intent-driven network management
- **Scale:** 30,000-60,000 test cases running daily across multiple groups

**Relationship to CI/CD Project:**
- **Arun's team** (CI/CD project): Tests switch/router functionality directly (CLI, functional conformance)
- **Rama's team** (this meeting): Tests Nexus Dashboard (controller that SENDS commands to switches)
- They're complementary: "My job will be done, that's it. As long as I kick in that CLI, I don't care whether [Arun's team] is doing the same job or not."

---

## Problem Statements (From Rama)

### Problem 1: Regression Analysis (Primary Pain Point)

**The Scale:**
- 30,000-60,000 test cases run daily
- Jenkins automatically queues jobs
- Runs complete in ~12 hours
- Results need manual analysis

**The Pain:**
- 10-12 engineers spend 3-4+ hours daily analyzing results
- Each engineer reviews 5-6 test suites
- Early in release cycle: many failures, chaos ("it's a nightmare")
- Late in release cycle: fewer failures, more stable
- Engineers questioned: "Did you really analyze everything?"

**The Ask:**
> "How do we provide these AI tools can do this kind of failure analysis?"

**Example Given:**
UI timeout errors cascade across 60 test suites, affecting 2000+ test cases. Engineers manually trace back to root cause. AI could identify: "This one bug is impacting these many test cases" instantly.

**Key Quote (Rama):**
> "Regression analysis is one of the costly functions. Where our op-ex is being a little bit overspent, we want to manage it better or use that bandwidth to develop automation or do something else."

### Problem 2: UI Automation (Secondary Pain Point)

**Context:**
- Currently heavy on API-based testing
- Leadership (Milesh, Nilesha, Sonawee) pushing to "move the needle" on UI automation
- UI testing is "laborious work"

**Current Stack:**
- Selenium tools
- Cisco automation infrastructure layer for Python
- Shared Git repository (cross-Cisco reusable)

**The Pain:**
- UI changes require massive script updates
- Example: Simple UI change required modifying 4,000 scripts

**Key Quote (Rama):**
> "UAE [UI Automation] is not impossible, but it is a more laborious work."

### Problem 3: UI Theme Changes (Emerging Pain Point)

**Context:**
- Cisco moving to dark theme / night mode
- Previously white background, now black
- Different color schemas for different themes

**The Challenge:**
- Traffic thresholds shown as green/yellow/red
- Does same schema apply to dark theme?
- Need to re-validate all screenshots/visual comparisons
- Some places modified, some not - need to catch inconsistencies

**Key Quote (Rama):**
> "Last time you showed us... dark blue and then it was night, black color. So then what happens is three shots [screenshots]. Some screenshots will be there..."

---

## Colin's Technical Response

### On Test Selection (SRT)
Colin probed whether test selection was a pain point. Rama clarified:
- **Selective Regression Testing (SRT)** already exists
- Based on code changes, chooses relevant 1,000-1,500 tests vs. all 40,000
- Enterprise and AS/NK teams use this
- Not the current bottleneck

### On Failure Analysis Hierarchy
Colin described the dual relationship between test failures:

**Hierarchical:**
> "Sometimes it's a repeat error that's flagged, but it was already covered by this up here. It's kind of just noise at that point. If you fix this one, it fixes the downstream."

**Dependency-based:**
> "Other times... this is happening because this one, so there's a dependency more than there's a hierarchy."

**Rama's Response:**
> "I think that is the complex one... how you correlate, there is [a situation where] you are using three different products... and one entity's [failure] symptom is being reflected on the UI."

### On Graph Topology Solution
Colin proposed a solution from the CI/CD work:

**The Approach:**
- Build a graph topology of the codebase
- Multi-dimensional representation of relationships
- Files, libraries, dependencies all mapped
- **State-aware:** Graph updates as code changes
- **Efficient:** No live queries needed; pre-computed relationships

**Use Cases:**
1. **Impact Analysis:** "If I want to see what files a library touches... how do I know what impact [a change] will have?"
2. **Test Activation:** "Because this changed, here are the ones that are relevant that should be activated"
3. **Failure Hierarchy:** "If it's a test that fails, now I know the hierarchy, which one is essentially the primary affected party"
4. **UI Change Impact:** Rama asked - "How much effort for reflecting [UI changes] in your scripts?" The graph could answer automatically.

**Rama's Response:**
> "I got what you mentioned. But yeah, I think that's a good part to fix this."

**Caveat Acknowledged:**
> "But it requires, yes, the executable commit may be, guys, you need to make structural changes on your core test, all these things, how you build the database kind of thing now."

### On UI Automation Demo
Colin offered to demo solutions for Problems 2 and 3:

> "For that second and third use case, that's a fun one we can actually demo to you. So we've got some really cool [solutions], because I know it's kind of brittle, almost. There's always a testing. It's brittle to do UX, UI testing."

**Rama's Response:**
> "Sure. We will look forward."

---

## Crossover with CI/CD Project

### Direct Technical Crossover

| Area | CI/CD Project (Arun) | Rama's Team |
|------|---------------------|-------------|
| **Testing Focus** | Switch/router functional conformance | Nexus Dashboard (controller) UI/API |
| **Test Volume** | Part of 39 gates | 30K-60K daily test cases |
| **Pain Point** | Pipeline visibility, failure diagnosis | Regression analysis, UI automation |
| **Jenkins** | Used for CI | Used for test orchestration |
| **AI Platform** | DeepSight Atlas | Cisco Circuit |

### Graph Topology Work
Colin mentioned this is already planned for Arun's team:
> "This is actually good, because this is part of what we're doing already for Arun's team."

Also mentioned work proposed to Nilesha's group:
> "There's also work that we aren't actively doing right now that we propose to Nilesha's group... about code-based modernization... for unit test generation and coverage."

### Potential Synergies
1. **Shared Graph Infrastructure:** Build once, leverage for both teams
2. **Failure Analysis Patterns:** Same AI techniques applicable to both
3. **UI Testing Solutions:** Could extend to multiple Cisco teams
4. **Cisco Circuit Integration:** Both projects likely need to integrate with internal AI

---

## People Mentioned

| Name | Role | Context |
|------|------|---------|
| **Rama (Ramagar)** | Test Manager | Nexus Dashboard testing, problem statement owner |
| **Arun Kumar Singh** | Director | CI/CD project owner, mentioned for context |
| **Nilesha** | (Role unclear) | CI/CD work, NDFC, unit test coverage proposal |
| **Milesh** | (Leadership) | Pushing Rama on UI automation ("move the needle") |
| **Sonawee** | (Leadership) | Mentioned with Milesh, "mad master" (unclear) |
| **Rahul Bobbili** | BayOne Delivery | Facilitated this meeting |

---

## Cisco Internal Tools Mentioned

| Tool | Purpose |
|------|---------|
| **Cisco Circuit** | Internal AI platform (aggregates Copilot, Windsurf, others) |
| **Selenium** | UI automation |
| **Python Automation Layer** | Cisco-wide automation infrastructure, shared via Git |
| **Jenkins** | Test job orchestration |

---

## Data Points (Rama's Team)

- **Daily Test Volume:** 30,000-60,000 test cases
- **Run Time:** ~12 hours
- **Analysis Staff:** 10-12 engineers
- **Analysis Time:** 3-4+ hours per day
- **Test Suites per Engineer:** 5-6
- **Example Impact:** Single UI change → 4,000 script modifications
- **Example Cascade:** One bug → 2,000 test case failures

---

## Decisions / Agreements

| Decision | Context |
|----------|---------|
| Colin will digest and come back with ideas | For all three problem statements |
| Potential demo for UI testing solutions | Problems 2 and 3 |
| Rama provided regression data example | Showed 21K+ scripts, 25K sanity runs |

---

## Open Items / Next Steps

| Item | Owner | Notes |
|------|-------|-------|
| Digest problem statements and propose solutions | Colin | Leverage CI/CD work where applicable |
| Demo UI testing solutions | Colin/BayOne | For problems 2 and 3 |
| Further discussion on graph topology approach | Both | May require structural changes to test framework |
| Connect on Nilesha overlap | TBD | Unit test coverage work may be related |

---

## Key Quotes

**Rama on the core problem:**
> "Running is okay. Running, yes, we can build so many equipment and repeat the test and everything. Analysis is the key thing. That is where the time is spent."

**Rama on engineer burden:**
> "It's a nightmare. If they're failed, if the high percentage failed, then they go cranky. Oh, I need to look and find analysis for everything."

**Rama on op-ex:**
> "Regression analysis is one of the costly functions. Where our op-ex is being overspent, we want to manage it better."

**Colin on the opportunity:**
> "This is actually good, because this is part of what we're doing already for Arun's team."

**Colin on graph topology:**
> "The trick to it is to not do it ad hoc. So for us, what we do is we'll preserve that, and it's state-aware. So whenever the code changes, the graph changes."

---

## Strategic Observations

1. **Natural Extension:** This work is a natural extension of the CI/CD project, not a separate engagement. Same patterns, different application.

2. **Scale Multiplier:** If BayOne solves this for Rama's team, the same solution likely applies to "multiple groups" across Cisco (Rama: "This is a common problem across multiple groups").

3. **Proof Point:** Success here would be highly visible - 10-12 engineers freed up from 3-4 hours/day of analysis work.

4. **UI Testing Opportunity:** Rama's UI automation pain could be a differentiator. Colin hinted at having "really cool" solutions for this.

5. **Cisco Circuit Awareness:** Need to understand how BayOne solutions integrate with Cisco Circuit (their internal AI aggregator).

---

## Files Referenced

- Rama showed unified regression summary (21K+ scripts, 25K sanity runs)
- Example dashboard with failure analysis columns
- Mentioned Git repository for shared automation libraries
