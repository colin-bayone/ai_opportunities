# 04 - Team Sync: Blockers, Access, and Escalation Strategy

**Source:** /cisco/cicd/team/source/2026-04-16/cisco-team-sync_01.txt
**Source Date:** 2026-04-16 (Internal team sync)
**Document Set:** 04 (Weekly team sync)
**Pass:** Focused deep dive on blockers and Colin's escalation approach

---

## Meeting Setup and Purpose

Colin opens by telling the team that he is using the meeting transcript to generate files for an escalation email to Srinivas and Anand. He explicitly tells everyone to be verbose: "It's okay to be verbose right now... it's like we're prompt engineering live on a call. So it's good to share detail. It's good to be specific. Don't feel like you're talking too much. It's all for Claude." [00:02:10]

Colin frames the meeting's purpose: Srinivas asked for two things (takeaways from last meeting and open questions), but Colin wants to start with something different -- a structured round-robin of blockers. He states his thesis up front: "our team right now, our velocity is primarily gated by not technology or complexity or things being difficult, but pretty much by access." [00:02:10]

---

## Colin's Opening Characterization of the Access Situation

Before the round-robin begins, Colin delivers a pointed characterization of Cisco's access process:

- **"Circus"**: "It's like a circus right now. Not on our team side, for sure... But on Cisco's side, it's like you have to talk to 100 people just to get access to one simple thing." [00:03:31]
- **Four weeks, no DeepSight access**: "It is Thursday of the following week and we still don't have access to DeepSight. This is now 4 weeks into the project and we still don't have access to the thing that Srinivas himself is the owner of." [00:03:50]
- **Escalation plan announced**: Colin states he is putting together an email to Anand and Srinivas to make them aware of where limitations actually are, and that they are not coming from technical complexity. [00:04:01]

---

## Blocker Round-Robin Order

Colin structures the round-robin deliberately: Srikar first, then Namita, then Saurav and Vaishali last (because they have a separate laptop issue). [00:12:01]

---

## Blocker 1: Scribble/Scrubber Naming Confusion and DeepSight Repo Access

**Raised by:** Srikar Madarapu
**Affected repos:** Scribble (confirmed name) and Pulse -- the two tools Naga worked on that were assigned to BayOne team by Srinivas
**Current status:** No access. Cannot even confirm repository names or links.

### Chain of Events

1. **Srinivas assigns Scribble and Pulse work items to BayOne team** (verbally, during previous Friday's meeting). No repository links or owner information provided at time of assignment.

2. **April 9 (last Thursday):** Srikar and Namita meet with Naga in person. Naga shows them two repos: Pulse and Scribble. Naga provides a verbal walkthrough of both projects. [00:15:12 -- Namita confirms: "That was 9th of April."]

3. **After getting CI/CD repo access:** Srikar examines the GitHub Enterprise org and sees team names listed. He finds "parser agent," "pulse," and "scrubber" -- but NOT "scribble." He reasonably assumes Scrubber might be the same thing as Scribble, given they are in the same org. [00:08:30]

4. **Tuesday, April 14:** Srikar reaches out to Naga to ask if Naga is the owner and to get repo links. Naga tells Srikar to check with Srinivas instead. [00:15:18]

5. **Wednesday, April 15 ("yesterday"):** Srikar reaches out to Srinivas requesting access to the two repos Naga worked on. Srinivas responds by asking "why do you need scrubber?" -- revealing that the naming confusion has now caused a communication breakdown. Srinivas does not recognize "scrubber" as something he assigned. [00:05:47]

6. **Wednesday, April 15:** Srikar reaches back out to Naga to get the direct repo links so he can forward them to Srinivas and eliminate the naming confusion. Naga has not responded. [00:06:06]

7. **Thursday, April 16 (day of this meeting):** Srikar is physically at Cisco campus and plans to track down Naga in person to get the links "by any cost." [00:07:47]

### Namita's Clarification

Namita interjects to confirm the correct name: "Srikar, if you remember when we met Naga, he had showed us two repo. It was Pulse and Scribble. So it should be Scribble." [00:08:21]

Srikar acknowledges this but explains the source of confusion: the GitHub team listing showed "scrubber" not "scribble," leading him to use the wrong name when requesting access from Srinivas.

### Colin's Analysis of This Blocker

Colin identifies two compounding failures:

1. **Verbal-only instructions lead to naming errors**: "You verbally gave instructions. When you verbally give instructions, bad thing happened." [00:09:04]
2. **No links or owner provided at assignment**: "We didn't have a link to the repository or access given to the repository. So that's just a crazy way to work in my opinion. You know, just them mentioning what a project's called and then it's our job to go and hunt down who the repository owner is and what the link to the repo is, that's an impossible way to work." [00:09:04]

### Status of Pulse

Colin asks specifically about Pulse. Srikar confirms: "Same, same Colin." -- identical situation, same dependency on Naga, same lack of repo links or access. [00:11:01]

---

## Blocker 2: Permanent ADS Machine (Tenant ID + Standalone Bundle)

**Raised by:** Namita Ravikiran Mane
**Sub-components:** Two distinct prerequisites needed to create the permanent ADS machine.

### Sub-blocker 2a: Tenant ID

- **When first requested:** During the second or third day at Cisco, which Namita and Srikar place in early April (around April 3-4 based on context). Colin initially assumes March, but the team corrects him: "No, no, that would be in April... last week." Srikar clarifies: "Last, last Thursday" (April 3). Colin settles on "like 2 weeks ago." [00:14:00-00:14:18]
- **Approval status:** Mahaveer (Mahavir) has said he approved it.
- **Actual status:** The approval is not reflected in the portal. Namita cannot see the tenant ID at her end despite Mahaveer's stated approval. [00:12:27]

### Sub-blocker 2b: Standalone Bundle

- **When first requested:** Last Friday (April 11). Srikar confirms: "The last Friday we requested for the standalone." [00:13:49]
- **Approximate wait time at time of meeting:** ~1 week (5 days).
- **Current status:** No response received. [00:12:49]

### Colin's Framing of the ADS Machine Blocker

Colin escalates this to a fundamental project risk: "If we continue on the temporary machines, we are effectively going to have to redo all of our work every four weeks." [00:12:59]

He characterizes the temporary machines as acceptable only for initial familiarization: "The temp machines are good to get you all some familiarity with this system, but it is not enough to actually work on because it's like you have a Git repository that disappears every four weeks. And even if you do have a Git repo, you shouldn't have to set up all services from scratch every four weeks. That's crazy." [00:13:14]

---

## Blocker 3 (Implicit): No Documentation in Any Repository

**Raised by:** Saurav Kumar Mishra
**Context:** Interjected during the Scribble/Pulse discussion.

Saurav notes: "None of the repos have like any kind of documentation on that. So that also adds like a little bit more time that we do not have like any way to quick start on the repo. We have to first go dive into the repo first, figure out what is happening, and then start the work." [00:09:53]

This is not a discrete access blocker but a compounding factor -- even once access is granted, ramp-up time is extended because there are no READMEs, no architecture docs, and no onboarding materials in any of the repositories.

---

## Blocker 4 (Implicit): Three Separate GitHub Enterprise Servers

**Raised by:** Colin Moore
**Context:** Raised during escalation framing at [00:16:18].

Colin notes that Cisco operates three different GitHub Enterprise servers. This multiplies the access problem because each server requires its own access requests: "In reality too, there's like three different GitHub Enterprise servers as well, if you notice that... So that makes it even three times worse because now you have to request access even more. That's just crazy." [00:16:18]

---

## Positive Note: Justin Joseph Logs Obtained

**Confirmed by:** Namita Ravikiran Mane
**Context:** Colin specifically probes whether "no blockers" means Namita was able to get the logs from Justin Joseph. [00:22:17]

Namita confirms: "Yes." [00:22:29] This is a notable success -- one access dependency that was actually resolved. Colin confirms he saw this reflected in the breakdown Namita sent.

---

## Colin's Escalation Strategy

### The Planned Email

Colin announces he will send an email to both **Anand** (Srinivas's boss) and **Srinivas**. The escalation goes one level up deliberately -- Colin wants Anand to see the pattern. [00:04:01]

### The Ultimatum Framing

Colin's exact framing of what the email will convey:

> "Either you guys, you know, come to grips with the situation. Don't tell me to talk to 30 different people and put in 30 different requests. Give me a list of what I should do. And let's pick a date that that must be resolved by, by Cisco team. It must be resolved by the Cisco team so that we can run at full speed." [00:04:21]

Key elements of the ultimatum:
1. **Shift the burden**: Stop telling BayOne to chase access across multiple people. Cisco team must own the resolution.
2. **Concrete list**: Cisco provides a single list of what BayOne needs to do (not 30 scattered instructions from 30 people).
3. **Hard deadline**: A specific date by which all access issues must be resolved by Cisco's side.
4. **Transparency**: Colin will present the exact timeline of each blocker so Srinivas can see the pattern.

### "Dumpster Fire" Assessment

Colin escalates his characterization further when discussing the GitHub organization:

> "I don't even know how this team functions within itself. It's just a mess. They need to stop. If it was me and I was in charge, I'd say, everyone, stop everything you're doing. We're having a cleanup day. We're going to rearrange all the repositories. We're going to figure out what needs categorized as stage production and things that are just POCs, things that are in development. And we're going to clean this up because this is a dumpster fire." [00:16:18]

### What Colin Wants in the Escalation Email

Colin explicitly states he needs timelines for each blocker so he can present them transparently to Srinivas: "What kind of timeline are you looking at? So think of like whenever you first started talking to Naga, and when you got access to things or information from him, and whenever you sent requests for things... because that way I can have the timeline in mind when I talk to Srinivas too. So that way we can make sure that we're being completely transparent with him too." [00:14:22]

### Going-Forward Process Colin Will Demand

Colin states what he will require from Cisco for all future access requests: "In general going forward, if we are going to need access to a repo, I need a link to the repo, I need the owner, and I need access given, when the items are assigned, not us hunting down how to request access." [00:11:15]

Saurav endorses this and adds: "At least when we are starting the project, our checklist would be very good. Like you need these things to work on the repo and yeah, the access, go ahead and do it. That would be like a much better way to work on it rather than first telling us that you have to work on this, then go ahead and figure out what's the repo, who's the owner. Then, go on for access." [00:11:35]

---

## Consolidated Blocker Timeline

| Blocker | Raised By | First Requested | Days Waiting (as of 4/16) | Current Status |
|---|---|---|---|---|
| DeepSight access (overall) | Colin | ~March 19 (project start) | ~28 days (4 weeks) | No access |
| Scribble repo access | Srikar | April 9 (verbal from Naga); formal request chain started April 14 | 7 days since Naga meeting; 2 days since Srinivas request | Blocked on naming confusion; Naga unresponsive; Srikar to find Naga in person today |
| Pulse repo access | Srikar | April 9 (same as Scribble) | 7 days | Same status as Scribble |
| Tenant ID for permanent ADS machine | Namita | ~April 3 (2nd-3rd day at Cisco) | ~13 days | Mahaveer says approved; portal does not reflect it |
| Standalone bundle for ADS machine | Namita | April 11 (last Friday) | 5 days | Request raised; no response |
| Repository documentation | Saurav | Ongoing | N/A | No repos have any documentation; adds ramp-up time to every new access grant |

---

## Team Dynamic Notes

- Colin explicitly reassures the team multiple times that reporting blockers is not complaining: "Don't feel like you're complaining. Just be completely, you know, straightforward about it." [00:05:47] He repeats this framing for Namita's round: "No matter what it is, big or small, do not feel like you're complaining." [00:21:51]
- Colin praises the team's performance: "Not on our team side, for sure. I think you've all done an amazing job." [00:03:31]
- Colin validates Srikar's approach to the naming confusion: "You did the right thing there." [00:15:56]
- Colin explicitly takes responsibility for the Friday deliverable to reduce pressure on the team: "Don't feel like, you know, you're in a crunch for tomorrow. I'm going to take care of it for tomorrow for the slides, the diagrams, et cetera." [00:19:37]
- Colin frames the escalation as protecting the team: the email will make clear that the velocity constraint is entirely on Cisco's side, not the BayOne team's.
