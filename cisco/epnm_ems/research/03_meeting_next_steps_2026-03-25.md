# 03 - Meeting: Next Steps and Logistics

**Source:** /cisco/epnm_ems/source/guhan_selva-3-25-2026.txt
**Source Date:** 2026-03-25 (POC Proposal Discussion and Scope Refinement)
**Document Set:** 03 (Third meeting, scope clarification and next steps)
**Pass:** Focused deep dive on next steps and logistics

---

## 1. Colin's Hardware Status: Cisco Laptop Received

Colin opened the meeting by announcing he had received his Cisco hardware: "You'll be happy to know I finally got my Cisco hardware." Guhan responded: "You got it, okay." Colin clarified the timing: "I'm not using it right now, I just got it yesterday." Guhan said: "Congrats." Colin then confirmed: "But finally, I'm fully onboarded."

Guhan's reaction was enthusiastic and telling of how long they had been waiting on this dependency: "May the first code you write is for us." Colin reciprocated: "Exactly, exactly."

Despite having the laptop in hand, Colin was not using it for this meeting. He stated: "I just got it yesterday. So I got it set up late last night. I haven't gotten signed into everything. I didn't want to do that before the meeting." He was using his BayOne device for this call instead.

This resolves the critical-path hardware dependency that had been flagged as an open blocker across both Set 01 (February 9) and Set 02 (February 20). The Cisco laptop was originally estimated at "a week or two" from the February 20 meeting. It arrived approximately five weeks later, on March 24, 2026.

**Status:** Resolved. Hardware is in Colin's possession as of March 24. Setup is partially complete (initial setup done the night before; sign-in to Cisco systems still pending at the time of this meeting).

---

## 2. Onboarding Trainings: Being Completed Day-Of

Colin confirmed he had access and was completing the required Cisco trainings. When discussing his Cisco access status, he stated: "At least I have been onboarded, I have Cisco ID, taking all the trainings today itself, so I'll have access to everything."

Guhan reinforced that Colin is fully cleared from an onboarding perspective: "He's completely onboarded." A second voice (likely Rahul) also confirmed: "Yeah, he's done. He's done with it."

Later in the meeting, near the end, there is a reference that appears to be Colin drafting or referencing a message about his status: "I now have my Cisco hardware in hand and have finished the setup and completion. My next items that I'll take care of for myself and the team that I could use some help with are the onboardings for the various applications and any trainings that we might need to have in order to access the needed items."

This suggests Colin was composing an update message (possibly to the CI/CD team or another Cisco contact) about his readiness. It distinguishes between general Cisco onboarding (complete) and application-specific trainings (still in progress).

**Status:** General onboarding complete. Cisco ID active. Application-specific trainings in progress on March 25. Colin expected to have full access imminently.

---

## 3. Selva to Schedule Team Session with India Domain Experts

Selva committed to arranging the next working session where the domain experts would walk Colin through the specifics of the POC. Selva stated: "The next step will be, I'll get the domain experts on this. And then we will set up a session with you to go over specific things we want."

He distinguished this session from the current meeting's high-level framing: "I gave you a high level view. Me and Guhana have given you what's the high level objective. Now the specifics of which screen are we going to do. What is the outcome here? And then what is the equivalent of that in the old product? How do you get to the code of the old product? How do you get to the code of the new? And then we give you access to both."

On timing, Selva said: "Expect something early next week." He then repeated the commitment: "I mean, I think we worked with the team the first session, maybe somewhere early next week."

Selva also flagged the geographic reality: "I'm expecting that the team will be in India, by the way, Colin." Colin's response was untroubled: "Yes. No problem."

Guhan reinforced the urgency as he was leaving: "I hope you can. Maybe you can capture these things, the high level." He directed Selva: "This is the one that we'll chat with," meaning this team session is the immediate next step.

On the number of sessions needed, Selva hedged: "That will be the, maybe I don't know, like you'll need one session or another couple of sessions to do that." He then set the expectation for independence after the initial sessions: "And then... we give you the access, and I'm hoping that from there on, you'll be able to take it forward."

Colin confirmed: "Yes."

Selva also indicated he would be present for the team session, at least partially: "Yeah. I'll be there on the meetings. Yes. So then, so it's basically, yeah, I would also see. I mean, maybe for the first few minutes, but the subject matter experts are the ones that matter there. So you don't really need me on those calls, but I'll try to see. At least for the intro and setting up the right context, I'll be there."

**Status:** Firm commitment from Selva. Target: early the following week (week of March 30). Session will include India-based domain experts. Selva will attend at least the introduction to set context.

---

## 4. What the Team Walkthrough Session Will Cover

Selva laid out a specific agenda for the upcoming team session. The scope of what will be covered:

**Which screens to target.** Selva stated the session will address "the specifics of which screen are we going to do." In the earlier part of the meeting, faults and inventory had been identified as the priority candidates. Guhan confirmed: "We also prioritized like because there are multiple screens, there are screens that we want to first start. Like the fault and I think, is it inventory or?" Selva confirmed: "It's inventory, yeah." Guhan added: "These are very common applications that customer usually go to."

**Expected outcomes for each screen.** Selva included "What is the outcome here?" as part of what the walkthrough would define -- meaning the domain experts would specify what the converted classic view should look like and how it should behave for each selected screen.

**The equivalent in the old product.** Selva stated the session would cover "what is the equivalent of that in the old product" -- meaning the team would walk Colin through how each selected functionality appears in EPNM (the legacy product) so he can understand the classic experience that needs to be replicated.

**Code access for both old and new products.** Selva explicitly stated: "How do you get to the code of the old product? How do you get to the code of the new? And then we give you access to both." This means the walkthrough session is also meant to resolve the code access logistics -- where the repositories are, how to access them, and ensuring Colin has the right permissions for both the EPNM and EMS codebases.

**Independence after access.** Selva set the expectation that after this walkthrough (one to two sessions), Colin would work independently: "And then... we give you the access, and I'm hoping that from there on, you'll be able to take it forward." Colin confirmed he could: "Yes. You do have access to Cisco. Yes, I do. And you have a device. Yes, yes."

Colin also described how his team operates once given access, reinforcing that the session does not need to be exhaustive: "We're very good at that. So we won't need much hand holding once we have access to the code base. We go and have exploration happen. Even on this, I said we kind of build our own kind of map of the application. So we understand a lot more without having to ask SMEs. So we try to make that as painless as it can be. The only time we'll ask questions is if things contradict each other or things aren't in alignment or logically speaking."

**Status:** Agenda is defined. Execution depends on the scheduled session (early next week per Selva's commitment).

---

## 5. WebEx Space Creation

Selva committed to creating a WebEx collaboration space. His exact statement: "I will create a space between you, me and Colin on WebEx and then we can decide. Other folks there and then we can decide on our time and then we can schedule."

The "you" in this statement was directed at Rahul (who was on the call). So the initial space would include three people: Selva, Colin, and Rahul.

Selva indicated this space would serve as the primary coordination channel going forward: "So I'll create the space and we'll take it out from there." He also noted that additional people could be added: "Other folks there and then we can decide."

This space would be used for:
- Scheduling the team walkthrough sessions
- Ongoing coordination between BayOne and Cisco on the POC
- A persistent communication channel outside of formal meetings

**Status:** Firm commitment from Selva. No specific date given, but implied to happen promptly (before the early-next-week team session, since scheduling would happen through this space).

---

## 6. Local San Jose Resource for Colin

Selva raised the idea of providing Colin with a local point of contact in San Jose. His statement: "I also wanted to like reconfirm with Kuhan of anyone local from San Jose. I have a few people in mind or at least one, right? That can give you the overall overview and everything, right? So that really, at least for the first week, you have someone to, if you have anything or bounce off something."

Key details:

- **Purpose:** Someone Colin can "bounce off" questions with during the initial ramp-up period, particularly the first week of active work.
- **Selva has candidates in mind:** He said "I have a few people in mind or at least one," indicating he already has a short list but has not confirmed.
- **Requires Guhan's approval:** Selva explicitly stated he needs to "reconfirm with Kuhan" (Guhan) on who this local contact will be. This was said after Guhan had already left the meeting (Guhan had a hard stop at 11:25 AM).
- **In-person proximity implied:** By specifying "local from San Jose," Selva is looking for someone who could physically meet with Colin or at minimum be in the same time zone for rapid back-and-forth.

**Status:** Selva to confirm with Guhan. Not finalized. Selva has candidates but needs Guhan's sign-off. This will likely be resolved through the WebEx space or offline between Selva and Guhan.

---

## 7. Guhan's Time Constraints and Handoff to Selva

Guhan established upfront that he had a hard stop: "11:25, I need to bail out. Salva can continue." He asked Colin: "I don't know if you really need the full hour, but we'll figure it out." Colin responded: "We may not need the full hour."

When Guhan reached his time limit, he handed off explicitly to Selva: "I think I have to have a host stop at Selva. I hope you can. Maybe you can capture these things, the high level. This is the one that we'll chat with." He was directing Selva to capture the high-level items discussed and coordinate the next steps.

Guhan also offered to stay briefly for any questions from Rahul: "And Rahul, if you have any other questions, right? I mean, I'm here to answer a few moments and then we'll probably look for the next one."

After Guhan's departure, Selva took over the logistics discussion and drove the conversation toward scheduling, the local resource, and the WebEx space creation.

Selva also acknowledged that Guhan's involvement in the team walkthrough sessions would be limited: "So you don't really need me on those calls, but I'll try to see. At least for the intro and setting up the right context, I'll be there." (Note: Selva is speaking about himself here, but the same principle applies to Guhan -- Guhan's involvement is strategic rather than operational.)

**Status:** Guhan has delegated operational coordination of next steps to Selva. Selva is the primary point of contact for scheduling and logistics going forward.

---

## 8. India Team Coordination

The domain experts who will participate in the walkthrough session are based in India. Selva stated this directly: "I'm expecting that the team will be in India, by the way, Colin." Colin responded: "Yes. No problem."

This has scheduling implications:
- India Standard Time (IST) is 12.5 to 13.5 hours ahead of US Pacific Time, depending on daylight saving.
- Sessions will need to be scheduled at times that work for both Colin (San Jose/Pacific time) and the India team.
- Colin's lack of concern suggests he is experienced with or prepared for cross-timezone collaboration.

Guhan also indicated that sharing information with the India team was important: "Sincever, I will share with my friend also, so he's in sync with us." (This is a garbled transcription; the likely meaning is that Guhan wants to share the meeting summary or key decisions with a colleague to keep them informed.)

Selva confirmed he would coordinate: "So, I can coordinate the meetings for you. So, you also want to be on those meetings, right?" (Directed at Guhan or Rahul.) The response was: "Yes. Yeah. I'll be there on the meetings."

**Status:** India-based domain experts are confirmed as the team that will be involved. Selva is responsible for coordinating the schedule across time zones. Session timing has not been specified beyond "early next week."

---

## 9. Colin to Amend the POC Document

Selva explicitly asked Colin to update the existing POC proposal document to reflect the scope reframe discussed in this meeting. Selva stated: "And if you want to amend this document for that UI thing, you can do that."

The "UI thing" refers to the classic view toggle framing that was clarified in this meeting -- the project is not about bringing missing functionality from EPNM to EMS, but rather about adding a classic view toggle to screens that already exist in EMS, using the existing EMS backend.

Colin had the POC document open during the meeting and was walking through it: "This was the document I shared." The document had been created after the Set 02 meeting and shared with Guhan and Selva. Guhan commented: "I think whatever you've given at this time, right, you've given multiple details and I mean intent is to do a few pages or a few areas like screens you said, right?"

Guhan also noted that the fundamental content of the document is still applicable: "To me, I don't think it changes the scope that much. Whatever you have here still applies." But it does need refinement: "So basically here you're saying I'm bringing in something vertically which does not exist. So we also weighed in all of this, but this is one of the things, at least it's been in our minds."

**Status:** Firm action on Colin. He needs to amend the POC document to reframe the scope from "converting missing functionality" to "classic view toggle for existing EMS screens." Guhan does not consider this a major change but it does need to be reflected in the document.

---

## 10. Selva's Timeline Commitment for Follow-Up

Selva provided a general timeline for his follow-through: "And I mean, I'll work with the team in India and give you the next two days, and then I'll get back to you with a meeting sometime next week."

Breaking this down:
- **Next two days (March 26-27):** Selva will coordinate with the India team to identify availability and prepare for the session.
- **Sometime next week (week of March 30):** The actual team walkthrough session will be scheduled.
- **Based on team availability:** Selva qualified this by saying "Based on the team's availability," indicating the date is not entirely in his control.

Colin responded positively: "Perfect."

Selva also committed to the full logistics chain: "So I'll create the space and we'll take it out from there."

**Status:** Firm commitment from Selva with a two-day preparation window and a next-week target for the session.

---

## 11. Post-Walkthrough Expectations: Colin's Starting Point

Selva set clear expectations for what happens after the initial walkthrough sessions. He stated: "And then... we give you the access, and I'm hoping that from there on, you'll be able to take it forward."

Colin then outlined what his starting process would look like. Selva asked: "So then once you've got the information and you can say hey this is my start of whatever that four week effort or whatever, but after looking at it you can even tell us what's that."

Colin explained the front-loaded nature of the work: "Initially it takes more time and then the subsequent ones will be even faster. Yes, yes, by far. So typically what we see, and this is the first, it's almost like this exponential decay cycle truly, even the time-wise, the first time is us, first of all, understanding the problem. So there's that onboarding period for us."

He then described how his team operates autonomously once they have code access: "We go and have exploration happen. Even on this, I said we kind of build our own kind of map of the application. So we understand a lot more without having to ask SMEs. So we try to make that as painless as it can be. The only time we'll ask questions is if things contradict each other or things aren't in alignment or logically speaking."

Guhan asked a probing question about how Colin would handle functional gaps between old and new UIs: "How will you figure out things like, I mean, I'm able to do a certain functionality in this new UI, and then that functionality is not even, it was there or not even there in the previous one, you'd be able to figure out and analyze between how?"

Colin responded with the Venn diagram concept: "So that's what I call almost like a Venn diagram. And our goal would be a perfect circle overlap, at least for the areas that the customers care about, as you said. But for the start out, we would essentially not know. So we'd have to map that out. We like to do that because it actually makes our life easier. So rather than trying to set up all these calendar meetings with the team and bogging everyone down, now with agents, we just go and explore. And that helps us ask the right questions, so it's a lot more efficient."

**Status:** Expectations aligned. After the walkthrough, Colin will work independently with minimal SME involvement. The team only needs to be available for questions when things contradict or are unclear.

---

## 12. Informal End-of-Meeting Discussion

After the formal meeting concluded (Guhan had departed, Selva signed off), there was an informal exchange between Colin and Rahul. This section of the transcript is significantly garbled but contains several identifiable elements:

**A message Colin was reviewing or composing:** Colin referenced or read aloud what appears to be a status update message: "I now have my Cisco hardware in hand and have finished the setup and completion. My next items that I'll take care of for myself and the team that I could use some help with are the onboardings for the various applications and any trainings that we might need to have in order to access the needed items."

**A building/location reference:** Someone mentioned "This is building 22?" and the response was: "No, we're in building 20, but we can meet them in building 22." This suggests Colin and Rahul (or another party) are physically located in a Cisco campus building and were considering an in-person meeting with another team.

**A deleted or missing message from another contact:** There was discussion about a message that someone (referred to as "Cerny" or similar -- likely a garbled name) had sent, indicating "another team is working on this." The participants could not find the message: "Did he delete the message?" and "There was a message that Cerny had sent that he said that another team is working on this and you can..." This may relate to overlapping work on the same or a related initiative.

**A potential impromptu meeting:** Colin or Rahul suggested: "Do you want to catch up with them now that we are here? What is your take? We still have 30-25 minutes to us. Let's see if we can." This suggests they were considering using the remaining time slot for a meeting with someone else who was nearby.

**Status:** Informal. These are logistical tidbits from the meeting's tail. The deleted message about another team working on the same area is potentially significant and may warrant follow-up, but no action was definitively committed to in the transcript.

---

## Summary: Action Item Table

| # | Action Item | Owner | Timeline | Status |
|---|-------------|-------|----------|--------|
| 1 | Amend POC document to reflect classic UI toggle framing | Colin | Not specified (implied soon) | Firm commitment |
| 2 | Create WebEx space for Selva, Colin, and Rahul | Selva | Immediately / before next session | Firm commitment |
| 3 | Coordinate with India team and prepare for walkthrough | Selva | Next two days (March 26-27) | Firm commitment |
| 4 | Schedule team walkthrough session with India domain experts | Selva | Early next week (week of March 30) | Firm commitment, subject to team availability |
| 5 | Confirm local San Jose resource with Guhan | Selva | Not specified (near-term) | Pending Guhan's confirmation |
| 6 | Complete Cisco application-specific trainings | Colin | Day-of (March 25) and following days | In progress |
| 7 | Finish signing into Cisco systems on new laptop | Colin | Immediately after meeting | In progress |
| 8 | Share meeting summary/decisions with colleague to keep them in sync | Guhan | Not specified | Implied commitment (garbled transcription) |

---

## Open Questions and Unresolved Points

1. **Who is the local San Jose resource?** Selva said he has "a few people in mind or at least one" but needs to confirm with Guhan. No name was given. The purpose is to give Colin someone to bounce questions off during the first week of active work. This person's identity and availability remain unknown.

2. **What specific code repositories and systems will be covered in the walkthrough?** Selva described the session covering "How do you get to the code of the old product? How do you get to the code of the new?" but no repository names, Git URLs, or system access mechanisms were specified. This is deferred to the walkthrough session itself.

3. **How many walkthrough sessions will be needed?** Selva hedged: "maybe I don't know, like you'll need one session or another couple of sessions to do that." This is undefined and will depend on complexity and how the first session goes.

4. **The deleted message about another team.** In the informal end-of-meeting discussion, there was a reference to a message (possibly deleted) from someone saying "another team is working on this." If another team at Cisco is pursuing a similar initiative (classic view toggle or UI conversion), this could represent overlapping effort or a competing approach. This was not resolved in the transcript.

5. **Building location and potential in-person meetings.** Colin and Rahul appear to be physically present on the Cisco campus (building 20, with a reference to meeting someone in building 22). Whether in-person sessions with the local San Jose resource or other team members are part of the plan was not formalized.

6. **Application-specific trainings.** Colin distinguished between general Cisco onboarding (complete) and application-specific trainings (in progress). Which specific applications or systems require additional training before he can access the EPNM/EMS codebases is not specified.

7. **Rahul's role in ongoing coordination.** Rahul was included as a participant in the WebEx space and was present on this call. His specific role in the engagement logistics going forward -- whether he is a coordinator, an escalation path, or an active participant in technical sessions -- was not explicitly defined in this meeting.

---

## Critical Path: What Must Happen Before Active POC Work Begins

Based on this meeting, the remaining blockers before Colin can begin hands-on POC work are:

1. **Colin finishes Cisco laptop setup and sign-in** -- In progress as of March 25. Should be resolved within hours or a day.
2. **Colin completes application-specific trainings** -- In progress as of March 25. Timeline unclear but appears near-term.
3. **Selva creates WebEx space** -- Committed, no specific date but implied immediate.
4. **Selva schedules team walkthrough with India domain experts** -- Target: early week of March 30. Subject to India team availability.
5. **Walkthrough session occurs** -- Colin gets walked through which screens, the old vs. new product equivalents, and code access for both products.
6. **Code access is granted** -- Selva stated: "we give you access to both." This happens as part of or immediately after the walkthrough.
7. **Local San Jose resource is confirmed** -- Selva to confirm with Guhan. Not a hard blocker but intended to support the first week.

Once items 1-6 are resolved, Colin begins independent work. The expected sequence is that items 1-3 happen within days of this meeting, item 4 is scheduled for early the following week, and items 5-6 happen during that session, placing the start of active POC work at approximately the end of the week of March 30 or early the week of April 6.
