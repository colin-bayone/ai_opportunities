# 02 - Communications: Summary

**Source:** cisco/cicd/communications/source/external/chat1.txt, chat2.txt, discovery_meeting_brainstorming.txt
**Source Date:** 2026-02-10 through 2026-03-31 (Full external communication record)
**Document Set:** 02 (External Communications)
**Pass:** Summary of all Set 02 documents

---

## What This Set Contains

- **02_comms_timeline_and_pattern_2026-03-31.md** -- Complete chronological message record from both the group WebEx space and the private Colin-Anand chat, analysis of Anand's escalation pattern across five interventions, gap analysis of Colin's promises versus what was delivered, and a detailed breakdown of what Anand is actually asking for when he requests "a tentative plan"
- **02_comms_blocker_analysis_2026-03-31.md** -- Seven specific blockers preventing work from starting (with owner, days outstanding, and what has been tried for each), a list of six work products BayOne can produce today without Cisco access, a proposed unblock strategy with specific asks and 48-hour fallback escalations, and a concrete two-week "coming out swinging" plan targeting deliverables before the April 30 contract renewal

## State of the Engagement as of March 31

The engagement is 50 days old. It has produced one deliverable: the February 18 discovery notes. The team is assembled (five members), hardware is in hand as of March 25, and the team has reviewed the DeepSight platform recording. However, no Cisco system access has been granted -- no VPN, no GitHub repository access, no ADS machines, no DeepSight platform access. The same four access needs identified on February 17 have been listed in the group chat twice (March 13 and March 25) without resolution. Anand asked for a plan on March 27. As of March 31, no plan has been shared and his follow-up ("Any update on this?") has gone unanswered.

## Anand's Escalation Pattern

Anand's behavior follows a textbook executive escalation curve across five interventions. He began with energy and direction on February 10 ("Let us engage... Please get started"), moved to a pointed check-in on March 3 ("How is it going? Is everyone on board? How about TOI?"), escalated to explicit frustration on March 12 ("This is loosing steam"), took direct action on March 26 by adding his own resource (Shih-Ta Chi) to unblock onboarding, and on March 27 shifted from asking for status to demanding a plan ("Can we come up with a tentative plan for next couple of weeks?"). His March 31 follow-up -- four words, no elaboration -- signals that he has said what he needs and is waiting. The next escalation will likely go above BayOne's engagement level or trigger a conversation about whether the engagement is working.

## Seven Blockers by Owner

**BayOne-owned (actionable today):**

| # | Blocker | Days Outstanding |
|---|---------|------------------|
| 1 | GitHub Enterprise Training -- completion of the mandatory 3-4 hour course (link provided Feb 17; unclear if VPN is required) | 42 days |
| 7 | No Regular Status Cadence -- no standing meeting or structured update rhythm has been proposed | 50 days |

**Cisco-owned (requires Cisco action):**

| # | Blocker | Owner | Days Outstanding |
|---|---------|-------|------------------|
| 2 | ADS Linux Machine Provisioning | Divakar | 42 days |
| 3 | VPN Setup and Network Access | Shih-Ta Chi / IT | 42 days |
| 4 | DeepSight Platform Access and SDK onboarding | Srinivas | 42 days |
| 5 | Airflow SME Identification and introduction | Divakar | 42 days |
| 6 | Divakar Availability (resolving -- he returned March 27) | Cisco | ~14 days |

## What "Coming Out Swinging" Requires

The contract renewal date is April 30 -- 30 days away. "Coming out swinging" means producing visible, shareable engineering work in the next two weeks that shifts the narrative from "BayOne has been waiting" to "BayOne has been building." The blocker analysis lays out six specific deliverables:

1. **Week 1:** Complete GitHub training for the full team (zero-dependency, eliminates one blocker entirely), produce a structured DeepSight Integration Technical Analysis from the recording (architecture diagram, integration points, proposed application design), and deliver a Discovery Agenda Package for each of the five planned IC-level sessions (with objectives, known context, specific questions, and required Cisco attendees).

2. **Week 2:** Produce a technical design document for Developer Box Instrumentation (Deliverable A -- telemetry schema, collection approach, pipeline design), build a static HTML prototype of the Branch Health Dashboard (Deliverable F -- what a release lead would actually see), and drive every remaining discovery question to either answered or specifically assigned with a date and owner.

Both weeks include structured written status updates sent to the WebEx group. By April 14, BayOne should have seven concrete artifacts to show Anand, making it clear that the remaining blockers are on the Cisco side while BayOne has been engineering in parallel.

## The Single Most Important Action

Respond to Anand with a plan, not a status update. Anand has received three status updates from Colin (February 18, March 13, March 25). Each one was optimistic in tone but structurally identical: things are moving, here is a list of what we still need. On March 27, Anand stopped asking for updates and asked for a plan -- specific actions, specific dates, specific owners, for the next two weeks. That request has gone unanswered for four days. The March 31 "Any update on this?" is a follow-up on the unanswered plan request, not a request for another status report. The response must contain a forward-looking two-week calendar with named owners and dated commitments that Anand can hold people to. Until that plan is in his hands, the engagement remains in a credibility deficit that optimistic messaging cannot close.
