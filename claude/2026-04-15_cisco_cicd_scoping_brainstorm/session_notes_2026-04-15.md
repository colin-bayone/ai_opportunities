# Cisco CI/CD Scoping Brainstorm — Session Notes

**Date:** 2026-04-15
**Context:** Preparing for Anand scoping meeting for next quarter. Colin debriefing and venting before sharing internal team meeting transcript.

---

## Engagement State Summary (Validated by Colin)

The research library (Sets 01-10, 57 documents) and team sub-singularity (Set 01) are accurate. Colin confirmed the understanding is "completely right."

### Timeline Reality

- **Original plan:** Start January 2026. Deliver A+F by April 30.
- **What happened:** Procurement delays ate nearly two months. Hardware provisioning ate another month. Team only started getting real access in late March/early April.
- **Current position:** April 15. Renewal is April 30 (15 days away). The six A-F capability areas have not been started. First tasks (WebEx scraper, build log analysis, recording transcriber) are in flight but are Srinivas-directed priorities, not the original A-F deliverables.

### Colin's Core Frustrations (April 15 Debrief)

1. **Access is the single biggest impediment.** Everything at Cisco requires a separate access request, provisioning cycle, and turnaround. There is no streamlined process. The team has been "clawing away at getting access to things" for weeks.

2. **Scattered ownership.** No clear ownership or structure or process on the Cisco side. Different teams own different systems (Airflow, CAT, DevX, GitHub Enterprise, ADS machines, DeepSight). Each requires separate contact, separate provisioning, separate escalation. Nobody owns the whole picture on Cisco's end except maybe Srinivas, who is already overloaded.

3. **Scope drift risk.** The six items (A-F) are presumably what BayOne will be measured against for contract renewal and budget requests. However, Srinivas has directed the team toward other work (WebEx scraper, recording transcriber, build log analysis). These are related to the broader CI/CD mission but do not directly track against the A-F deliverables.

4. **Accountability inversion.** Colin's concern: "We do not want to screw ourselves with this and have Anand or anyone else try to say that we're not doing what we should have done. Whenever they're the ones changing the scope, they're the ones not giving access, they're the ones taking forever to give us things, and we're just sitting here trying to do our best to work with this fucked up system."

5. **Some bright spots.** Justin Joseph has been extremely helpful. Anupma has been helpful to an extent. Srinivas has been helpful, but the overall system is too fragmented for anyone to fully unblock.

6. **Colin's assessment:** Without a targeted resolution to the access problem with a deadline, there is a rocky path forward.

### The Strategic Problem for Next Quarter Scoping

The meeting with Anand for next quarter needs to address:

- What was supposed to happen vs. what actually happened (and why)
- Who is accountable for the delays (Cisco procurement, hardware, access)
- How to align Srinivas's directed work with the A-F deliverable framework so BayOne is not measured against things they were never allowed to start
- What realistic scope and budget looks like for next quarter given the late start
- What access commitments need to be in place before BayOne can commit to deliverables

### Internal Team Meeting

Colin described the internal team meeting he just had as "a bit of a dumpster fire" that will reveal even more context. Transcript to follow in this session's source folder.

---

## Internal Meeting Transcript — Key Additions to the Picture

The April 15 internal meeting (source: `internal_yikes_4152026_formatted.txt`) revealed several things that were not visible from the engagement research library alone:

1. **Colin was never consulted on the $100K/quarter pricing.** He was told the number after the fact. This is the root of the margin problem.

2. **RS committed Colin at 100% utilization to Cisco as a sales tactic.** Colin softened this in the written proposal to "heavily involved at start, tapering off," but the verbal commitment is what Cisco heard. This creates both a cost problem (Colin's loaded rate at any allocation eats the margin) and a credibility problem if Cisco notices reduced involvement.

3. **The actual work is far simpler than what was scoped.** Colin's words: "They said they had a Ferrari built for us and we go and it's like a soapbox derby car that a seven-year-old made." The complexity was massively overstated by Cisco. The bottleneck is access, not technical difficulty. Colin said he could do the entire project with a single person.

4. **The Q4 ask landed at $168K** ($216K total at 35% GM, minus $48K carry-forward from Q3 surplus). Risk reserve was set to zero because the $100K baseline was already too low and adding reserve would make the ask look indefensible.

5. **Saurav is a flight risk at $11.18/hr.** Colin has been pushing for a raise and promotion. No success so far. If Saurav leaves, the project is in serious trouble.

6. **The meeting was rushed.** Anand moved the call from 12:30 to 11:45 while the team was still working through the numbers. They went into the Anand meeting without full alignment on the costing approach.

See decomposition files for detail:
- `transcript_analysis_costing_and_margin.md`
- `transcript_analysis_scope_and_deliverables.md`
- `transcript_analysis_meeting_dynamics.md`

## Colin's Costing Frustration (April 15 Debrief, Post-Transcript)

### How the Pricing Got Set

Rahul Sharma (President, not Rahul Bobbili from the sales team) threw out $100-150K/quarter in the very first meeting with Cisco. This was before discovery, before any work estimate, before understanding the problem. Zero thought process behind the number. He said it in the initial meeting without even knowing what the scope was.

Colin approached Rahul Sharma multiple times afterward asking how to calculate gross margin for this engagement. Response each time: "Don't worry about it. We're just going to put our foot in the door. We're going to do this even if it's some expense to us for the first quarter because we need to get the work started with them."

Colin was never included in the pricing conversation in any planning capacity. Worse, they then decided to include Colin in the financial costing as an hourly resource, even though he is salaried as Director of AI for the entire company. His time is not an hourly line item, but they are treating it as one.

### The $122K Q3 Number Explained

- Cisco's fiscal Q3 starts January 26, 2026.
- Original budget: $100K/quarter.
- Additional $22K rolled forward from a prior contractor named Saurav Tiwari (not the same Saurav on the current project). Tiwari preceded the current engagement and quit mid-contract. That unspent money from December 2025 was rolled into Q3.
- Total Q3: $122K.

### The Compounding Problems

1. **The ask is almost double with no scope change.** They are going from $100K/quarter to $168-178K/quarter. The scope has not changed. The scope creep from Srinivas is a totally separate issue that has no correlation to why the number is going up. The number is going up because the original number was pulled from thin air.

2. **Headcount was exposed to Cisco.** Because they showed headcount rather than keeping it outcome-based, Cisco can now divide the total by headcount and back into hourly rates. This makes BayOne's margins visible and limits negotiating leverage going forward.

3. **People are being arbitrarily added.** Anuj and Amit drove a pricing conversation where they are adding offshore resources and costing them at nearly triple the internal rate, without understanding why those people are there or what they will do.

4. **The internal team cannot do basic math consistently.** The meeting transcript shows people going in circles on loaded rates, load factors, margin calculations, and quarterly hours. Multiple formulas gave different answers. They went into the Anand meeting without alignment.

5. **Colin is being forced to clean up a mess he did not create.** He is the technical lead. He should not be the one unfucking a pricing situation that was caused by the president throwing out a random number, the delivery team not understanding margins, and the sales team exposing headcount to the client.

### Colin's Core Position

This entire financial mess traces back to one decision: Rahul Sharma picking a number out of the air in the first meeting. Everything since then has been people scrambling to make that number work, and now that it obviously does not work, they are going to Cisco and essentially saying "we don't know how to do math, so give us almost double." The optics of this are terrible, especially combined with the fact that BayOne has delivered almost nothing in Q3 due to Cisco-caused delays.

## Internal Dynamics (April 15)

Colin is furious. Anuj and Amit inserted themselves into the pre-Anand prep meeting despite not being involved since December. They drove a chaotic pricing conversation that produced a half-baked number less than an hour before talking to a Senior Director at Cisco. The meeting with Anand had to be rescheduled because BayOne was so unprepared.

Neither Anuj nor Amit are actually on the Anand call. The people doing the real work and taking the call are Colin, Neha, and Zahra. Neha and Zahra both report to Anuj. Colin sent a message to the team chat expressing his frustration at the lack of structure and last-minute insertions.

## Files in This Session

- `session_notes_2026-04-15.md` — this file, running log
- `source/internal_yikes_4152026.txt` — raw transcript
- `source/internal_yikes_4152026_formatted.txt` — formatted transcript
- `source/internal_scoping_prep_2026-04-15_formatted.txt` — earlier manual formatting attempt (ignore, superseded by script output)
- `transcript_analysis_costing_and_margin.md` — rate details, margin math, numbers from the meeting
- `transcript_analysis_scope_and_deliverables.md` — scope creep, deliverable risk, Cisco delay timeline
- `transcript_analysis_meeting_dynamics.md` — internal BayOne dysfunction, what was not resolved
- `transcript_analysis_costing_root_cause.md` — chain of failures from Rahul Sharma's arbitrary number through today
- `strategy_take_anand_meeting.md` — recommended approach, concrete list of what Srinivas claimed was ready but is not

## Pending

- [ ] Outcome of the Anand meeting
- [ ] Whether the scope vs. money separation strategy was used
- [ ] Next steps for Q4 SOW
