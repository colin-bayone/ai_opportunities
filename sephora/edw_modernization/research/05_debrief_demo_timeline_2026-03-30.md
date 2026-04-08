# 05 - Debrief: Demo Timeline and Logistics

**Source:** /sephora/edw_modernization/source/saurav_colin_3302026.txt
**Source Date:** 2026-03-30 (Internal Debrief)
**Document Set:** 05 (Saurav/Colin Debrief)
**Pass:** Focused deep dive on demo timeline, logistics, and workload management

---

## Timeline Commitments and Deadlines

### Saurav's Development Estimate

Saurav estimated that the first iteration of the fully integrated demo could be ready by **6:30 PM IST the following day (March 31)**. However, he immediately qualified this by flagging the risk of issues arising during integration: "resolving some issues which may arise in the middle or something. So that's something we need to consider." His own recommendation was **Thursday (April 3)** as a more realistic target that builds in a buffer for debugging and issue resolution.

### Colin's Counter: Push for Friday, Fallback Thursday

Colin responded to Saurav's Thursday recommendation by pushing the target one day later: "Let me push for Friday. If not, we'll go Thursday." The reasoning is not explicitly stated but aligns with Colin's pattern of building in additional buffer and managing client expectations. Saurav confirmed he could meet either target: "Yep, I can do it."

The cover story for the delay was already in place. Colin had told Sephora the previous week that he "got pulled into an escalation," which provides the justification for the later demo date without revealing internal capacity constraints.

### Sephora's Budget Deadline

A hard external constraint anchors the entire timeline: Sephora must **lock in their budget numbers by the end of April**. Colin reported from his in-person visit that "they're getting all antsy about it." This means the demo must happen well before end of April to give Sephora time to process the results and finalize budget allocation.

### Competitive Context

Colin relayed that Sephora has "actually told all other vendors beyond us, no, not interested anymore." The implication: if BayOne shows them "anything in the direction of this working," the project is theirs. This both reduces competitive pressure and raises the stakes -- the demo does not need to be perfect, but it needs to demonstrably work.

---

## Screen Recording Plan and Specifications

### Purpose: Buy Time for the Full Demo

The screen recording serves as an **interim deliverable** to send to Sephora on March 30 (the day of this call) to "get them off our back" and create runway for the Thursday/Friday full demo. Colin framed it explicitly: "we can send them over to that, them that like today... and that gives us a runway for Thursday, Friday."

### Recording Specifications

Colin laid out specific requirements for the screen recording:

1. **Full-screen mode** -- the recording must be made with the browser in full-screen so the interface fills the entire frame
2. **No voiceover** -- Colin was explicit: "you don't have to do any kind of voiceover or anything like that"
3. **Trim off .HTML file indicators** -- the recording should not reveal that the demo is running as a local HTML file. Colin stated: "I would trim off or make it like full screen so they don't see like it's a dot HTML that's running." He acknowledged the craftiness: "If I sound sneaky, it's because I've had to do demos before"
4. **Use the existing hardcoded dashboard demo** -- the recording is of the current Streamlit/HTML demo with hardcoded data, not the fully integrated version

### Who Records

Either Saurav or Colin could produce the recording. Saurav offered to do it; Colin said "either we can screen record that or I can screen record that. I don't think that should be a problem for me to do." The final agreement was that Saurav would handle the recording, confirmed when Saurav asked at the end of the call whether to remove specific columns before recording.

---

## Columns to Remove Before Recording (and Why)

Saurav raised at the end of the call that the UI currently displays several summary fields after a pipeline run completes. Two specific columns were flagged for removal before recording:

1. **Estimated Cost** -- shows the dollar cost of LLM API calls for the pipeline run
2. **LLM Calls** -- shows the number of language model API invocations

### Colin's Rationale

Colin explained the removal with a specific mental math scenario: "what's gonna happen in their mind is they're gonna take that number and multiply it by 6000. You know, because let's say we have 6000 reports and each report is, you know, $3, you know you're now looking at $20,000 in language model calls."

The concern is threefold:
- The cost figures are **un-optimized** -- "we have not spent like a month to optimize this like we would if we were doing this truly at scale"
- No **model comparisons** have been performed that could reduce costs
- Showing costs "unnecessarily starts the conversation too early" about pricing before BayOne has had the chance to optimize

### Fields to Keep

Saurav and Colin agreed that three summary fields are appropriate to display: **validation score**, **total tokens**, and **duration**. These demonstrate capability without triggering premature cost-sensitivity discussions.

---

## Azure Deployment Offer

### Saurav's Proposal

Saurav proactively suggested an alternative to a screen recording or live demo: deploy the application to a server and share a link so Sephora can "try it on their own." He framed this as "better than the recording so that they can also see all the outputs and the better details."

### Colin's Specifications for Deployment

Colin immediately agreed and elaborated on the deployment parameters:

1. **Time-bound credentials** -- "we can call it time-bound login credentials"
2. **Server shutdown after one week** -- "these credentials will work for the next week, AKA I'll shut the server off in a week"
3. **Authentication required** -- "we can even have it like with a special authentication type thing"
4. **Sephora's data preloaded** -- the deployment would include Sephora's actual source and target files so they see results relevant to their own data

### Colin's Role in Deployment

Colin volunteered to handle the Azure deployment himself: "That's definitely one way I can help you too, because I can help get that online on my side." This keeps the deployment work off Saurav's plate so Saurav can focus entirely on integration.

### Timing

The Azure deployment was discussed as a complement to the full demo, not as a replacement for the screen recording. The deployment would likely be prepared in parallel with or after the full integration, giving Sephora a hands-on experience beyond the live demo.

---

## Workload Management Decisions

### Colin Absorbing Saurav's Cisco Responsibilities

Colin made an explicit commitment to take on all of Saurav's Cisco work for the week: "I'm going to absorb your responsibilities into mine for Cisco this week." He instructed Saurav that at the team meeting later that day, "if I say like, here's our deadline for things this week for Cisco, don't worry about anything."

Colin also wanted to manage optics within the team: "I don't want people to think like I'm giving you special treatment or something like that." The plan was to handle the reassignment quietly -- Colin would simply take on whatever Cisco items were assigned to Saurav without making it a visible exception.

Saurav's Cisco deliverables would still carry his name ("they'll be your deliverables"), but Colin would do the actual work.

### GitHub Training Deferral

One specific item assigned to Saurav for the week was a **GitHub training**. Colin deprioritized it entirely: "You can do that literally whenever it doesn't matter. So it's not like it has to be done this week. It's like on the To Do List for you this week." Saurav can complete it at any point with no deadline pressure.

### Net Effect

Saurav's entire week was cleared to focus exclusively on the Sephora demo integration. Every other obligation -- Cisco deliverables, GitHub training, team meeting action items -- was either absorbed by Colin or deferred indefinitely.

---

## Priority Ordering

Colin stated the explicit priority stack at the end of the call:

| Priority | Task | Notes |
|----------|------|-------|
| **1** | Screen recording of the demo | Send to Sephora on March 30 (same day) to buy time |
| **2** | Full integration and demo | Target Thursday (April 3), push for Friday (April 4) |
| **3** | Cisco work | Colin absorbing this; Saurav should ignore |

The GitHub training was not even ranked -- it sits entirely outside the priority stack as a background item with no deadline.

---

## Saurav's Demo Participation Logistics

### Colin's Intent

Colin wanted Saurav to present at the live demo: "I do want you to be a part of that demo if if the time can work out at all." His motivation was twofold -- Saurav built the solution and deserves the visibility, and presenting at Sephora "gives you some good visibility at Sephora too, which is always a good thing."

### The Timezone Problem

Saurav is based in India. Sephora demos would be scheduled during US Pacific business hours, which translates to approximately **3:30 AM IST** or similarly unreasonable hours. Colin acknowledged this directly: "I know you woke up at 9:00 AM today, but by the way, the demo's at 5:00 AM the following morning. Yeah, I don't want to do that to you."

### Colin's Approach

Colin framed participation as an opportunity, not an obligation: "Is that like a directive from me? No." He laid out the decision tree:

- If the demo can be scheduled with enough advance notice for Saurav to adjust his sleep schedule, Saurav presents
- If Saurav has been up all night working on integration and cannot reasonably present, Colin demos on his behalf: "Of course I can demo for you"
- Colin committed to pushing for scheduling that gives Saurav adequate notice: "I'll get that information done as soon as we can. And if it's not at least a reasonable sleep notice for you, we'll see if we can just get them later on in the week"

This is why Colin pushed the demo toward Thursday/Friday rather than accepting Tuesday or Wednesday -- more lead time gives Saurav a better chance of being able to participate.

---

## Contingency Plans

### If Demo Cannot Happen Tomorrow (March 31)

Screen recording sent same day (March 30) buys time. Full demo pushed to Thursday or Friday. Cover story already established (Colin's "escalation" from the prior week).

### If Saurav Cannot Present

Colin demos solo. Saurav's work is fully represented regardless.

### If Integration Issues Arise

Saurav's Thursday estimate already includes buffer for "resolving some issues which may arise in the middle." Colin's push to Friday adds another day of buffer beyond that.

### If Sephora Wants More Than a Recording

The Azure deployment option provides a self-service interactive experience. Time-bound credentials control access. Server shutdown after one week limits exposure. This was positioned as complementary to the live demo rather than a substitute.

### Skills-Based Alternative

Saurav also demonstrated a parallel implementation using Claude skills (on a separate branch called "Azure land chain" or similar). This approach showed lower API call counts, lower token costs, and faster execution. However, Colin noted that skills are "plainly readable markdown files," creating IP sensitivity concerns. The decision was to bias toward the architectural solution for the demo but keep the skills approach available as a fallback or comparison point. Colin explicitly deferred deeper exploration of this path: "Not yet. Not yet. Anyway, definitely for that."

---

## Schedule for the Rest of March 30

Colin outlined his schedule for the remainder of the day after this debrief:

1. Meeting with Ambar (next hour)
2. Cisco team meeting (Saurav will attend; Ricar will be present this week, having been out the prior week)
3. Quick meeting with Askari
4. Available time after -- offered to Saurav for follow-up: "if you need anything, then we can talk there"

Saurav confirmed: "if needed, we can then connect again."
