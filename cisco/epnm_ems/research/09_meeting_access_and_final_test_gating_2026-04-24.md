# 09 - Meeting: Access Status and Final-Test Gating

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Focused deep dive on remaining access gate, Playwright readiness, and Colin's workaround pattern

---

## 1. Headline

As of the Friday 2026-04-24 check-in, the POC has exactly **one remaining external dependency** before final comparative validation can run: **access to the virtual machines that have live EPNM and EMS applications running**. Every other access item that the engagement initially anticipated needing from the Cisco team has already been resolved by Colin himself, without requiring team intervention. Provisioning of those VMs is the explicit Monday agenda item.

Selva opened the meeting by framing the access posture this way:

> "everything is good on the access side. I know that's something we're going to address, right? Yes, yes. So I think it's just kind of the final hurdle for us. But the team's been really responsive."

That sentence is the operational summary of where the engagement stands going into the final demo week. There is no other open access ticket. There is no pending credential, no missing repository permission, no outstanding approval. There is one VM-provisioning step left, and the demo work has been built so that the remaining step is purely a **validation gate**, not a **build gate**.

---

## 2. The Single Remaining Dependency: Live EPNM and EMS VMs

### 2.1 What is being requested

Colin needs access to virtual machines on Cisco's side that have:

1. A **live, running instance of EPNM** (the legacy thick-client / Angular application that the POC is converting away from), and
2. A **live, running instance of EMS** (the modern microservice-based target architecture that the POC is converting toward).

Both must be reachable simultaneously from the BayOne side so that the same user flows can be exercised against both systems back-to-back.

### 2.2 Colin's exact framing in the meeting

> "what we're waiting on right now and what we'll talk about on Monday is the virtual machines that have the EPNM and EMS applications running. So we can do that comparative analysis on our end. That way we don't frankly embarrass ourselves before we come to you. If something's definitely missing or if something is not as expected, that'll let us actually test this out properly."

Later in the same meeting, Colin reiterated the boundary precisely:

> "The only remaining step for us right now that's pending, it's gated by that access to the virtual machines is for a live instance of EPNM and EMS. So that way we can see what we've done matches exactly those two cases."

The repetition is intentional. Colin is being scrupulous about not letting Guhan and Selva believe there is any other open dependency. The access side is otherwise closed.

### 2.3 Why it must be live (not screenshots, not spec docs)

The conversion that BayOne has built is a UI toggle that swaps the front-end while keeping the back-end identical. To certify that the toggle's "EMS view" of the inventory and fault management screens is **functionally indistinguishable** from the "EPNM view," the test harness must be able to drive both UIs against the same back-end and compare their behavior on identical inputs. That is by definition a live-system requirement. Static artifacts (screenshots, mockups, recorded videos) cannot exercise the back-end. They were sufficient for **building** the front-end (see Section 4 on the database seed workaround), but they are not sufficient for **validating** that the front-end is correct.

Guhan confirmed the architectural premise during the meeting when he pressed Colin on the toggle behavior:

> "So one thing, the POC, you have the classic view and then you have the current way to do the UI, right? So you switch back and forth. ... And then when you do that, it will still talk to the same backend. We're not spawning different backends, right?"

Colin's reply: "Absolutely. Absolutely. Identically the same. Yes." Because the back-end is identical, the only thing left to validate is that the new front-end produces the same observable behavior as the legacy front-end. That validation is a comparative, side-by-side execution against live instances of both, and that is what the VMs unblock.

---

## 3. Purpose of the Access: Comparative Testing via Playwright Agentic Suite

### 3.1 The test harness is already built and waiting

The most operationally important point in this meeting is that **the test infrastructure is not the bottleneck**. Colin built it during the week, ahead of receiving the VMs, so that the moment the VMs arrive the validation can run immediately. Two near-identical statements from Colin make this explicit:

> "We've got our agent workflow already good to go. So as soon as the team gives us access to the systems, we'll be in good shape so we can run our comparative test to make sure what we build with the toggle is exactly the same functionality on eP&M."

> "We have our whole agentic test suite with Playwright that can do that, so that'll be quick whenever we get that access."

Two facts come out of those statements:

1. The test framework is **Playwright** (browser automation), driven by an **agentic** layer (autonomous agents that can author, execute, and reconcile test outcomes rather than executing static scripted assertions).
2. The suite is **pre-authored**. It is not waiting on the VMs in order to be designed. It is waiting on the VMs in order to be **pointed at a target**.

That distinction matters because it converts what could have been a serial dependency (no VMs → no test design → no test execution → no validation) into a parallel one (test design happened in parallel with the VM-provisioning conversation, and only execution waits on the VMs). The serial portion is now reduced to whatever wall-clock time it takes Playwright to drive both UIs through the agreed-upon flows once the VMs are reachable.

### 3.2 Why Playwright + agentic is the right choice for this comparative

A traditional Playwright test suite would have to be hand-authored against a static expected-state per screen, and any drift between EPNM and EMS that was not anticipated by the test author would cause either a false positive (pass when behavior actually differs) or a false negative (fail because the test author guessed wrong about the expected state). The agentic layer addresses that by letting the agents discover behavioral parity dynamically: drive the same input on both UIs, capture the observable result on both sides, and reconcile. This is the pattern Colin alluded to elsewhere in the meeting when he said the agentic workflow is "fairly hands-off" and that "we audit it ourselves while it's running, so we can make sure everything's working properly."

### 3.3 What the comparative test will actually certify

For each in-scope screen (inventory and fault management for the POC), the comparative will verify:

- **Visual correspondence:** the converted EMS-style UI surfaces the same data fields, in the same arrangement, with the same affordances as the EPNM UI for the same back-end state.
- **Behavioral correspondence:** user actions (filter, sort, drill-down, edit, save) produce the same back-end side-effects and the same observable UI updates on both views.
- **Data correspondence:** the data displayed on both views is sourced from the identical back-end and is therefore guaranteed identical (this is mostly a structural guarantee from the toggle architecture, but the comparative confirms it empirically).
- **Gap identification:** any place where the two views legitimately diverge (because EMS introduces something EPNM never had, or vice versa) is surfaced and tagged against the gap analysis Colin already produced (42 back-end gaps documented).

Without the live VMs, none of these can be confirmed by execution. They can only be reasoned about from code. Colin's standard for the demo is empirical, not just analytical, which is why he is unwilling to call the work done until the comparative runs.

---

## 4. Colin's Pattern: Minimize Team Disruption, Work Around When Possible

### 4.1 The general principle Colin stated

> "I've tried to do as much as I can to not bother the team unless we actually really, really needed something."

This is not a one-off comment. It is the operating principle that explains why the access side is in the state it is in at the end of the week. Every item that could have been resolved without the Cisco team's intervention was resolved by Colin alone. The VM access is what is left precisely **because** it cannot be resolved without team intervention. It is the residue of a deliberate filter.

### 4.2 The database-seed workaround: the canonical example

The clearest worked example from the week is the database seeding. The converted UI needs realistic data to render against in order to be exercised, demonstrated, and built. The naive path would have been to ask the Cisco team for a database dump, a sanitized export, or read access to a populated EMS instance. Colin chose a different path:

> "even from that, if you're interested, all we did was we took that meeting recording that you shared and basically used the screenshots from that to pre-seed the database. So we didn't even have to bother the team for that."

The mechanic: a previously shared meeting recording (presumably an earlier walkthrough of EPNM/EMS by the Cisco team) contained on-screen data while screens were being demonstrated. Colin extracted screenshots from that recording, used them as the source of truth for what realistic inventory and fault-management records look like in production, and pre-seeded BayOne's local database with synthetic-but-realistic equivalents derived from those screenshots. The team was never asked. No additional request was filed. The build proceeded.

This is operationally important for two reasons:

1. **It demonstrates a pattern of resourcefulness that the client should be made aware of.** Colin explicitly invited Selva and Guhan to see this ("if you're interested"), which reads as gentle visibility rather than self-promotion. The point is: *this is how we work; we do not multiply your team's workload to get our work done.*
2. **It implicitly justifies why the VM access is being asked for.** When a vendor has demonstrably worked around every other dependency, the residual ask carries credibility. Colin is not asking for the VMs because it would be convenient. He is asking because he has already exhausted the alternatives.

### 4.3 Other access items: all resolved

In the meeting, after listing the VM gate, Colin said:

> "I was able to kind of resolve all the other items, even the initial data that was seeding into the database."

The phrasing "even the initial data" suggests the database seed was the most tempting one to escalate, and the most plausible to ask the team about. If even that one was worked around, the smaller items (repository access, branch creation, build environment setup, codec subscription usage, GitHub commit visibility) are by implication also resolved without team intervention. Colin's commits are already on the relevant branches ("a Gentec UI conversion" branch off develop for each of the 14 in-scope repositories), the team can audit them at will, and nothing is gated on a permissions or credentials question.

---

## 5. Quality Gate vs. Build Gate: The Important Distinction

### 5.1 The build is done

> "So conversion is ready, conversion is done. We are just doing our final tests."

> "we are right at the tail end of this"

> "we have pretty much the full roadmap done already for the full scope here, which is pretty cool. That happened a lot faster than we thought it would."

The conversion code exists, it is committed to GitHub on per-repository feature branches, the team can audit it, and the supporting deliverables (gap analysis, end-to-end repo map across all 14 repositories, UI/backend/data gap inventories, architectural-decision rationale documents) are also in place. The VM access is **not** gating any of that. The VM access is gating the **last validation step** that confirms what is already built actually behaves identically to EPNM end-to-end.

### 5.2 Why Colin frames it as a quality gate

The operative phrase from Colin is:

> "we don't frankly embarrass ourselves before we come to you. If something's definitely missing or if something is not as expected, that'll let us actually test this out properly."

The standard Colin is holding the team to is not "demo-ready." It is "demo-defensible." A demo that runs cleanly on BayOne's laptops and falls over the moment a Cisco engineer asks "does that match what we have today?" would technically meet the spec but would damage credibility. The comparative test against live EPNM and EMS is what lets the team answer that question with evidence rather than with assertion. This is why Colin is holding the work back from being declared "complete" until the comparative runs, even though the build itself is finished.

### 5.3 What can and cannot happen without the VMs

**Can happen without the VMs:**

- Code review by the India team. Selva and Guhan agreed during the meeting to schedule this for early in the week, possibly Tuesday, ahead of the demo. The branches are visible and auditable on GitHub today.
- Architectural-decision review. Colin's rationale documents are already in the repo and can be read and discussed.
- Gap-analysis review. The 42 back-end gaps and the UI/data gap inventories are already documented and can be discussed without a live system.
- A demo using BayOne's locally-running EMS instance with the seeded synthetic data. Colin confirmed: "we have EMS running on our end right now. I was able to get that pulled up. So we can show that."

**Cannot happen without the VMs:**

- The Playwright agentic comparative validating that EPNM and EMS-toggle produce identical observable behavior end-to-end against the same back-end.
- Empirical evidence (rather than analytical argument) backing claims of behavioral parity in the demo.
- Surfacing of any drift the build inadvertently introduced that pure code review would not catch.

### 5.4 Implication for demo timing

If the VMs are provisioned on Monday as planned, the comparative runs early in the week, the demo lands on schedule (the meeting discussion converged on Wednesday or Thursday morning Pacific time, working around East Coast and India time-zone constraints), and the demo is delivered with comparative validation in hand. If the VMs slip, the demo can still proceed with the local instance and the documented analysis. It just lands without the empirical validation layer underneath it. The work would not be lost; the credibility argument for it would be slightly weaker. That is the entire shape of the risk created by the one remaining external dependency.

---

## 6. The Monday Agenda Item

The meeting closed with a clear handoff for Monday. Selva's framing:

> "the next thing is Monday they are waiting to give provide access to the systems and everything and I think, well, instead by what Wednesday we will have like a demo or something."

VM access provisioning is the explicit Monday agenda item with the India team. The conversation also fixed the sequencing for the rest of the week:

- **Monday:** VM access provisioning. India team meeting at 9 a.m. Pacific.
- **Tuesday (tentative):** Code review session with the India team, requested by Guhan ahead of the demo so that any team questions can surface in time to be addressed before the formal demo. Guhan: "let me talk to the team on that. And maybe the demo itself may move to Thursday or so."
- **Wednesday or Thursday morning Pacific:** Demo, time-zone-friendly for East Coast, Pacific, and India simultaneously (mid-morning Pacific = noon Eastern = late evening India).

The code review is being inserted before the demo specifically because, as Guhan put it:

> "that way if there's anything the team has, we can go back to the team and also ask questions, right? So that way they are free to root."

The intent is that the comparative test runs and the code review happens in parallel during the early week, and the demo on Wednesday or Thursday is the consolidated showcase of work that has already been independently validated by both an automated comparative and a human code review.

---

## 7. State of All Other Access Items (Resolved)

Putting the access ledger in one place:

| Item | Resolution | How |
|---|---|---|
| Source code access (14 repositories) | Resolved | Already provisioned; develop branches accessible; per-repo feature branch `agentic UI conversion` (transcribed as "a Gentec UI conversion") created off develop for the in-scope work. |
| Database seed data | Resolved | Pre-seeded from screenshots extracted from a prior Cisco team meeting recording. No team request filed. |
| Local EMS environment | Resolved | EMS running locally on Colin's side; demo can be driven from this instance if needed. |
| Codec / development tooling | Resolved | Cisco codec subscription used to capacity throughout the week ("I maxed out on the Cisco codec subscription pretty much every day this week"). No additional asks. |
| Commit visibility for team audit | Resolved | Colin tagged the team directly on the relevant commits so they could be audited by the India team without further action ("I actually put them in the commits that we did on the branch. I put them so specifically they could be audited by the team already"). |
| Architectural decision rationale | Resolved | Documented in-line in the rationale file Colin maintains as the human-in-the-loop layer. ("Any of those kind of decisions are rationales I put in myself. So those are not generated, those come from me directly.") |
| **Live EPNM and EMS VMs for comparative testing** | **Pending — Monday** | **The single remaining external dependency.** |

The asymmetry of the table is the point. Six of seven items are resolved, the seventh is the one item that genuinely cannot be self-served, and that one is on Monday's agenda.

---

## 8. Summary

- **One external dependency remains for the POC:** access to live EPNM and EMS virtual machines on Cisco's side.
- **The dependency is a quality gate, not a build gate.** The build is done; the gating is on the comparative validation step.
- **The validation infrastructure is already in place.** A Playwright agentic test suite is pre-authored and ready to point at the VMs on day one of access.
- **Colin's workaround pattern is the explanation for why the access ledger looks the way it does.** Every item that could be self-served was self-served. The database seed was rebuilt from screenshots out of a prior meeting recording rather than asking the team for a data export. The pattern is: minimize disruption, only escalate when truly blocked, and surface the workarounds gently to the client so they see the discipline behind the engagement.
- **VM provisioning is the Monday agenda item.** Code review is tentatively Tuesday. Demo is Wednesday or Thursday morning Pacific.
- **The demo can technically run without the comparative validation,** using the local EMS instance and the documented analysis, but the comparative is what makes the demo defensible against the question "does this actually match what we have today?" That is the operational reason Colin is holding the work back from "complete" until the comparative runs.
