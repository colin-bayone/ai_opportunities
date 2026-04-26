# 09 - Meeting: Demo and Code-Review Planning

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Focused deep dive on demo timing, code review sequencing, time-zone window

---

## 1. Headline Decision State

| Item | Status as of 2026-04-24 | Source |
|---|---|---|
| Demo placeholder date | **Wednesday (next week)** — held, but soft | "instead by what Wednesday we will have like a demo or something" |
| Demo provisional new date | **Thursday or so** — pending Selva's conversation with India team | "the demo itself may move to Thursday or so" |
| New gating step | **Code review with Cisco India team BEFORE the demo** | Guhan's request, accepted on the call |
| Access provisioning to the EPNM/EMS virtual machines | **Monday** | "Monday they are waiting to give provide access to the systems" |
| Touch-base to confirm final timing | **Tuesday** | "I'm going to see how it goes and then just touch bases on Tuesday to get some time on" |

**Net:** The Wednesday demo is no longer the working assumption. Wednesday is held as a placeholder; Thursday is the more likely date once Selva talks to the India team about inserting a code review first. Final lock-in happens on Tuesday's touch-base.

---

## 2. Original Plan (Before This Call)

The pre-call plan was a simple two-beat sequence:

1. **Monday** — Cisco India team provisions BayOne with access to the virtual machines hosting the EPNM and EMS applications. This was already the only outstanding access item; everything else (initial seed data, repository access, etc.) had been resolved by Colin without needing to bother the team.
2. **Wednesday** — Demo to Guhan and Selva of the working POC: the UI toggle that switches between the classic EPNM view and the converted EMS-based view, both hitting the same backend.

The Wednesday placement was driven by giving BayOne ~48 hours after access provisioning to run the full Playwright comparative test suite against the live EPNM and EMS instances and confirm functional parity.

---

## 3. Guhan's New Ask: Insert a Code Review First

Mid-call, after Colin walked through the comprehensive analysis (14 repositories mapped, 250+ generated documentation files, 42 backend gaps catalogued, UI gap analysis in both directions), Guhan asked for an additional step before the demo:

> "Before the demo, could you have this, what's designated coding? Basically, do your code review and start review with the India team."

(Transcript renders "code review" inconsistently as "designated coding," "court review," and "the coder be" — all the same request.)

### Guhan's reasoning, verbatim

> "The reason is that way, that way if there's anything the team has, we can go back to the team and also ask questions, right? So that way they are free to root."

("free to root" reads as "free to engage" / "free to investigate" — i.e., the India team should have time to dig in and surface questions of their own rather than absorbing it all live during the demo.)

### Why this matters operationally

- Guhan wants the India team to see the generated code **before** seeing it run, so they can:
  - Audit the diffs in context
  - Form their own questions
  - Be prepared, not reactive, in the demo
- Selva immediately accepted the framing: *"Okay, so let's have the coder be right there."*
- The code review is positioned as a gate, not a parallel track. The demo follows the code review, not the other way around.

---

## 4. Selva's Pivot: Demo Likely Moves to Thursday

Selva did not commit to a hard new date on the call. He said:

> "Yeah, it would have to be something that, I mean, since we have also mentioned now the court review, let me talk to the team on that. And maybe the demo itself may move to Thursday or so."

The sequence Selva needs to validate with the India team:

1. India team gets access provisioning settled (Monday).
2. India team makes time for a code review of BayOne's converted UI branches (mid-week — likely Tuesday or Wednesday morning their time).
3. Demo follows the code review (Thursday is the working guess).
4. Selva will give the India team a heads-up about the new code-review step so they can plan around it: *"And also give them heads up about the plans of doing the code review."*

---

## 5. Time-Zone Constraint (Three-Way Window)

The demo must work simultaneously for:

- **Colin** — US East Coast (EST/EDT)
- **Selva and team** — US West Coast (PST/PDT)
- **India team** — IST

Selva's framing of the only viable window:

> "It would have to be like, I mean, time zone friendly for East Coast, PST and India. So it would have to be our morning, I guess... For him it would be more like noon for us."

Translation:

| Participant | Window |
|---|---|
| Selva (PST) | Morning |
| Colin (EST) | Around noon (3 hours ahead of PST) |
| India team (IST) | Late evening (12.5 hours ahead of EST) — the cost they bear in this window |

Selva acknowledged the awkwardness earlier in the call when discussing why they couldn't meet on Friday: *"if we would have met on Friday, he would have been real late at night. Same thing with my team and IST."* The morning-PST window is a known compromise — it's the team's go-to slot for three-region calls because it keeps the India team's evening from running too late while still being workable on the East Coast.

There was also a brief side comment, *"Yes, that'll work out yes, it's a column for your morning time"* (transcript renders "she'll" — pronoun is wrong; meant "that'll"), indicating mutual acceptance of the morning-PST framing.

---

## 6. Tuesday Touch-Base

Colin proposed a Tuesday check-in to lock the final demo time once Selva has talked to the India team and the Monday access provisioning has happened:

> "I'm going to see how it goes and then just touch bases on Tuesday to get some time on."

The Tuesday touch-base is doing two jobs:

1. Confirming Monday's access provisioning actually landed.
2. Locking the demo time now that the code review has been inserted ahead of it and Selva has had his conversation with the India team.

This is a typical "trust but verify" rhythm — Wednesday/Thursday is the target, but Colin doesn't want to assume the access happened or the India team's calendar got sorted without an explicit check-in.

---

## 7. Audit-Ready Design Already Built In

Colin pre-empted concerns about the code review being painful for the India team by describing the audit hooks he had already engineered into the work. Three explicit features:

1. **Commits attributed to the team for direct audit.**
   > "I actually put them in the commits that we did on the branch. I put them so specifically they could be audited by the team already."
   The branches are off the `develop` branch (per Akilah's chat note), named `agentic-UI-conversion` (transcript: "a Gentec UI conversion") on each of the affected repositories.

2. **Decisions documented inline with rationale.**
   > "And any of the decisions that we had to make along the way, those are also documented with the rational justification."
   Decisions live next to the code they pertain to, with the *why*, not just the *what*.

3. **Human-in-the-loop sections explicitly tagged.**
   > "So that's my human in the loop part, if you will. Any of those kind of decisions are rationales I put in myself. So those are not generated, those come from me directly."
   This separates Colin's judgment calls from agent-generated content, so reviewers can focus their scrutiny on the human decisions specifically.

The combined effect: the India team's code review should be a quick read-through, not a forensic exercise. They should be able to see at a glance what was generated, what Colin decided personally, and why each decision was made.

---

## 8. Optional VM Instance Offer

Colin offered Selva a hands-on alternative to a passive demo:

> "If you wanted to make it live on an instance for a VM or something like that on your side, we could certainly do that. That way you can play with it yourself."

This is in addition to the demo, not in place of it. The default plan is still:

- Demo runs on BayOne's environment (Colin already has EMS pulled up locally).
- All code is on the Cisco GitHub branches; the team can rebase off `develop` if desired.
- If Selva wants a runnable VM on the Cisco side instead of a screen-share, BayOne can stand that up.

Selva's response: *"I'll talk to the team on that"* — taken under advisement, no commitment either way. Likely depends on how the India team wants to interact with the artifact.

---

## 9. What Gates the Demo

In sequence, with hard dependencies:

```
Monday          → Cisco India provisions VM access (EPNM + EMS instances)
                  ↓
Monday/Tuesday  → BayOne runs Playwright comparative test against live instances
                  ↓
Tuesday         → Colin/Selva touch-base to confirm timing
                  ↓
Tue or Wed AM   → Code review with Cisco India team (NEW GATE)
                  ↓
Wed or Thu AM   → Demo to Guhan, Selva, and India team
                  (PST morning / EST midday / IST evening window)
```

The two "or" decision points are what Tuesday's touch-base resolves.

---

## 10. Who Needs to Be There

**Demo attendees:**
- Colin (presenter; BayOne)
- Guhan (Cisco — confirmed: *"expect more questions during the demo. I can handle them. I can handle them."*)
- Selva (Cisco — host)
- Cisco India team (newly added to the demo by virtue of the code review preceding it; they will already be up to speed)
- Anu (was on this call; presumed continuing)

**Code review attendees (new):**
- Colin
- Cisco India team (the engineers who own the EPNM and EMS code bases)
- Selva (likely, as host/coordinator)
- Guhan does not need to attend the code review; this is a dev-to-dev review.

---

## 11. Tone Notes (For Context)

The whole call was collaborative and low-stakes — logistics being worked out in real time, not a formal re-plan. Markers of that tone:

- Selva and Guhan repeatedly thanked Colin for taking the meeting late in his East Coast day; Guhan: *"Thanks for taking this later in your evening."*
- Guhan's pulse-check joke landed well: *"Is it good or is it great?"* — Colin's answer: *"It's completely in the direction that we were looking."*
- Guhan explicitly told Colin to take a break: *"I hope you're going to take a CIPP cap out of this or something"* (transcript garbled — likely "weekend" or "rest").
- The schedule change was framed as *"just a day or two"* and Colin's only concern was confirming the access slip didn't actually move things materially: *"I just wanted to make sure that day, I know it's just a day or two, but I wanted to make sure that didn't make a difference."*
- No tension around inserting the code review — Colin took it on board immediately and pointed at the audit hooks he'd already built. Guhan and Selva took comfort from that: the new gate doesn't add risk because the artifact was designed for it.

The decision posture is: keep things flexible, lock specifics on Tuesday, optimize for the India team's ability to engage thoughtfully.
