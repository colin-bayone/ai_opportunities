# Decisions Log — 2026-04-24

**Source meeting:** Set 09 (POC progress check-in with Guhan and Selva)
**Source transcript:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt

This document captures the decisions made and the open items that emerged from the April 24 meeting. It is a living document that complements the append-only research library: where the research library captures *what was said*, this file captures *what was decided* and *what remains undecided*.

---

## Decisions Made

### D-09-01: POC scope holds at inventory + fault management
**Decision:** The POC will demo the toggle conversion of the inventory screens (network devices, device 360, device details) and fault management screens (alarms, events, syslogs). DPM and other functional areas remain out of POC scope.
**Source:** Colin and Guhan, Set 09. Guhan confirmed: "It's not part of the POC, you're right, but that's in the gap."
**Status:** Confirmed.

### D-09-02: Toggle implementation as bolt-on, not invasive
**Decision:** Classic UI ships as parallel Angular packages alongside the existing EMS UI. The toggle is a single UI control at the top of inventory and fault-management screens. The same backend serves both UIs — no backend forking. EMS Angular code is not modified.
**Source:** Colin's design choice, validated by Selva on the record: "And then when you do that, it will still talk to the same backend. We're not spawning different backends, right?" Colin: "Absolutely. Identically the same."
**Status:** Confirmed.

### D-09-03: Code review with Cisco India team inserted before demo
**Decision:** A code review session with the Cisco India team will occur BEFORE the formal demo, not after. Reasoning: the team needs time to surface questions and engage on answers before the demo locks in expectations.
**Source:** Guhan's request: "It's good before the day, even if you want to push it by the [day base]. The reason is that way... if there's anything the team has, we can go back to the team and also ask questions, right? So that way they are free to root [engage]."
**Status:** Confirmed. Selva to coordinate with the India team.

### D-09-04: Demo timing flexes to accommodate code review and time-zone window
**Decision:** Demo originally placeholder for Wednesday next week. With code review inserted, demo may move to Thursday. Time-zone window: PST morning / EST midday / IST evening. Tuesday touch-base between Colin and Selva to lock the slot.
**Source:** Selva: "And maybe the demo itself may move to Thursday or so. And it would have to be like, I mean, time zone friendly for East Coast, PST and India. So it would have to be our morning, I guess."
**Status:** Provisional. Locks Tuesday.

### D-09-05: Bookmarks behavior left as EMS-native for POC
**Decision:** Bookmarks behave differently in EPNM vs. EMS. The POC will port them as-is from EMS rather than reproduce EPNM behavior. Cross-screen impact makes a fix outside POC scope.
**Source:** Colin's example: "Bookmarks. something that simple, a different concept in EPNM than it is in EMS. So what we did there is we said, we'll leave it alone for now... if that is a gap, that's something that is more global scope that would impact pretty much every screen in EMS. So it's not possible to just do it within the scope of fault management inventory."
**Status:** Confirmed. Documented in the constraints doc shared with the team.

### D-09-06: No architectural-debt fixes during POC
**Decision:** Colin observed multiple instances of inconsistent patterns in EMS (e.g., column handling in tables) but deliberately did not make architectural fixes during POC. Reasoning: those decisions require team involvement. Available as a future-engagement value lever.
**Source:** Colin: "I didn't want to make that decision on a POC without the team involved, but with the team getting involved with us, that's a really easy way. We can make that go a lot quicker than not."
**Status:** Confirmed. Logged as an architectural decisions register for the broader scope conversation.

### D-09-07: Database seed via meeting-recording screenshots
**Decision:** Rather than ask the Cisco team for production-like seed data, Colin extracted screenshots from a previously shared meeting recording and used them to pre-seed the database. This avoided team disruption.
**Source:** Colin: "all we did was we took that meeting recording that you shared and basically used the screenshots from that to [pre-seed] the database."
**Status:** Confirmed. Already done.

---

## Open Items (Pending Decision)

### O-09-01: Who in the EMS team conducts the memory and load review?
**Context:** Guhan asked for a code review with someone in the EMS team that explicitly evaluates generated-code memory footprint and system-load impact, before the demo. The reviewer has not been named.
**Owner:** Selva to coordinate.
**Why this matters:** Gating ask. Cannot be skipped.

### O-09-02: Should BayOne pre-build a DPM gap brief for the demo?
**Context:** Guhan flagged DPM as customer-critical. Pre-building a brief that calls out DPM coverage in the gap analysis would demonstrate preparation and trust the product-management framing.
**Owner:** Colin (BayOne).
**Why this matters:** Guhan's signal that DPM matters is a leading indicator of which scope items the product-management conversation will hinge on.

### O-09-03: Will the demo include the full 14-repo mapping reveal, or stay scoped to the POC?
**Context:** Strategic decision. Showcasing the mapping at the demo accelerates the full-scope conversation but may dilute the POC narrative. Two-narrative discipline (per the summary doc) suggests keeping the demo POC-focused with the mapping as a "second-half" reveal.
**Owner:** Colin and Zahra (BayOne) to align.
**Why this matters:** Sequencing affects how the commercial-unlock conversation unfolds.

### O-09-04: What format does Cisco product management need?
**Context:** Guhan's commercial unlock quote ("we are going to go to the product management... you can go promise the customers") implies a specific deliverable will need to land at Cisco PM. Format, audience, depth — all unspecified.
**Owner:** Colin and Zahra (BayOne) to ask Guhan or Selva.
**Why this matters:** Future deliverables need to be designed for product-management consumption, not just engineering review.

### O-09-05: Pricing recalibration timing
**Context:** Full-system mapping completion materially de-risks the full-scope conversion. The pricing model may need to be revisited. The "full vertical slice" / "full-stack" language flagged in earlier sets is now even more inconsistent with reality.
**Owner:** Colin and Zahra (BayOne).
**Why this matters:** When BayOne re-engages on full-scope pricing, the de-risked posture should change the pricing posture — likely a fixed-scope, accelerated-timeline pricing model rather than time-and-materials.

### O-09-06: Pre-meeting protocol for Tuesday touch-base with Selva
**Context:** Tuesday touch-base will lock the demo slot, India team status, and code review window. Colin should walk in with: confirmed VM access status, pre-built DPM gap brief (if D-09-02 is approved), proposed time-zone slot.
**Owner:** Colin (BayOne).
**Why this matters:** The Tuesday call is when the demo logistics close out. Going in prepared is the leverage point.

### O-09-07: Guhan's exact title and reporting line
**Context:** Open since Set 07. Has not been resolved.
**Owner:** Colin or Zahra to surface naturally; not pressing.
**Why this matters:** Affects how to frame deliverables for him and his organizational stakeholders.

### O-09-08: Selva's "good or great" pulse-check answer
**Context:** Selva asked the question in front of Guhan. He will likely ask again. The right answer is something Colin can pre-think: substantive, partnership-affirming, and forward-looking.
**Owner:** Colin (BayOne).
**Why this matters:** Selva uses the answer to calibrate how he represents the BayOne relationship to Guhan and the broader team.

---

## Affirmed Items (Re-confirmed in Set 09)

- **Backend stays.** Selva's validation question on the toggle hitting the same backend reaffirmed the architectural commitment from Set 03.
- **Solo execution model.** Colin running the POC solo continues to work for the team. The database-seed workaround pattern (work around when possible, only escalate when truly blocked) is now established.
- **AI compliance posture.** Not re-litigated in Set 09. The Set 07 stance held.
- **Audit-ready commit pattern.** Commits attributed to Cisco team members; in-line decision rationales authored by Colin distinct from agent-generated content; "human in the loop" portions tagged.
