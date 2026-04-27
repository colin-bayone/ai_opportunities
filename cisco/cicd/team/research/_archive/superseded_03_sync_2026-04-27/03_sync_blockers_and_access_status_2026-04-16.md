# 03 - Team Sync: Blockers and Access Status

**Source:** /claude/2026-04-15_cisco_cicd_scoping_brainstorm/source/cisco-team-sync_4-16-2026.txt.txt
**Source Date:** 2026-04-16 (Wednesday team sync)
**Document Set:** 03 (Third team sub-singularity set)
**Pass:** Focused deep dive on blockers, access requests, and resolution timelines

---

## 1. Colin's Framing: Access Is the Primary Velocity Constraint

Colin opened the meeting by explicitly stating the purpose: this call would serve as a blocker inventory. He told the team the meeting transcript itself would be used to generate files to send to Srinivas: "I'm using this, I'll use this meeting transcript to help me to generate some of the files that I'm going to be sending up to Srinivas. So keep that in mind. It's okay to be verbose right now."

He then gave his assessment of the team's situation: "I think from my perspective, our team right now, our velocity is primarily gated by not technology or complexity or things being difficult, but pretty much by access."

Colin characterized Cisco's access management as chaotic: "It's like a circus right now. Not on our team side, for sure. I think you've all done an amazing job to do that. But on Cisco's side, it's like you have to talk to 100 people just to get access to one simple thing."

### Colin's Planned Email to Anand and Srinivas

Colin stated he is preparing a formal email to both Anand (Srinivas's boss) and Srinivas to surface these access issues. His language was specific about the intended tone:

- "I'm going to be putting together an email to Anand and Srinivas to basically say, hey guys, you know, this is great, everything's good, but you need to be aware of where the limitations actually are."
- He wants to frame it as an ultimatum: "Give me a list of what I should do. And let's pick a date that that must be resolved by, by Cisco team. It must be resolved by the Cisco team so that we can run at full speed."
- "Don't tell me to talk to 30 different people and put in 30 different requests."

Colin explicitly said he wants to escalate to Anand, not just Srinivas: "I'm going to really, you know, make very obvious and transparent to Anand, who is Srinivas' boss. Like, I don't even know how this team functions within itself. It's just a mess."

He told the team not to self-censor: "No matter what it is, big or small, do not feel like you're complaining. I'm just getting all the things documented for today."

---

## 2. Blocker #1: Pulse and Scribble Repository Access

### Who reported it: Srikar Madarapu

### Current Status: Blocked

Srikar reached out to Srinivas the previous day (April 15) requesting access to the two repositories that Naga built (Pulse and Scribble). However, there is a naming confusion that has created an impasse.

### The Naming Confusion

When Srikar accessed the CI/CD GitHub org after receiving CI/CD access, he saw repositories including "parser agent," "pulse," and "scrubber" -- but no repository called "scribble." Srikar assumed "scrubber" might be "scribble" and requested access using that name. Srinivas responded by asking why Srikar needed access to "scrubber," which is apparently a different tool entirely. This created confusion that halted the access request.

Srikar's explanation: "There is one called scrubber on the teams, like when you go to the teams, like you see the teams in the arc. So it doesn't say anywhere scribble, so it says scrubber only. So I thought like I referred to that and I asked him."

Namita provided clarification from a prior meeting: "Srikar, if you remember when we met Naga, he had showed us two repo. It was Pulse and Scribble. So it should be Scribble." The two repos are Pulse and Scribble, but "scribble" does not appear in the list of repositories visible to the team.

### Root Cause (Colin's Assessment)

Colin attributed this to Cisco's disorganization. It would have been "reasonable to think that all of those tools would live within the same repo," but they do not. He stated the fundamental problem: "We didn't have a link to the repository or access given to the repository. So that's just a crazy way to work in my opinion. Them mentioning what a project's called and then it's our job to go and hunt down who the repository owner is and what the link to the repo is, that's an impossible way to work."

### Timeline

| Date | Event |
|---|---|
| April 9 (Wednesday) | Srikar and Namita met with Naga. Naga showed them both Pulse and Scribble. Verbal walkthrough only -- no repo links provided. |
| April 10 (Thursday) | In the standup, DeepSight repo access was listed as blocked, pending Srinivas approval (documented in 01_standup_blockers). |
| April 10 (Friday) | Srinivas meeting. Pulse and Scribble access was raised. Srinivas assigned these as work items to the BayOne team but did not provide repo links or grant access at that time. |
| April 15 (Tuesday) | Srikar reached out to Naga to get repo links and confirm whether Naga is the owner. Naga told Srikar to check with Srinivas. Srikar then messaged Srinivas requesting access. Srinivas responded asking why Srikar needs "scrubber" (the wrong name). Srikar went back to Naga to get the correct, direct links to avoid further confusion. No response from Naga as of this call. |
| April 16 (Wednesday, this call) | Still blocked. Srikar planned to meet Naga in person at Cisco to resolve it: "I'll be meeting Naga if he's here and get that access object today by any cost." |

### Colin's Intended Framing for Anand

Colin will use this as a case study in his email: "Srinivas assigned those items to us last week, and we're still waiting on even knowing what the repository name is." He said he will propose that going forward, when items are assigned: "I need a link to the repo, I need the owner, and I need access given when the items are assigned, not us hunting down how to request access."

Saurav added supporting commentary: "At least when we are starting the project, our checklist would be very good. Like you need these things to work on the repo and yeah, the access, go ahead and do it."

---

## 3. Blocker #2: Permanent ADS Machine

### Who reported it: Namita Ravikiran Mane

### Current Status: Blocked (two sub-dependencies, both unresolved)

The permanent ADS (Application Development Server) machine requires two things that the team does not have:

1. **Tenant ID:** Namita reported that Mahavir said he approved it, but the tenant ID is still not visible at her end. This was first requested early in the engagement -- Namita said "it will be like during the second or third day at Cisco," and Srikar clarified "last Thursday" (April 10). Colin initially thought it was "even back in March," but the team corrected him that it was still in April, approximately two weeks prior to this call.

2. **Standalone bundle:** A separate request that was raised on Friday, April 11 (Srikar confirmed: "The last Friday we requested for the standalone"). No response received.

### Timeline

| Date | Event |
|---|---|
| ~April 3-4 (2nd or 3rd day at Cisco) | Tenant ID first requested. |
| April 10 (Thursday) | Standalone bundle request raised. Mahavir said he approved the tenant ID, but it is not visible to Namita. |
| April 11 (Friday) | Standalone bundle request raised (Srikar's recollection). |
| April 16 (Wednesday, this call) | Both still unresolved. Namita: "These two things are very important to create Alias machine. The first is tenant ID and the second is the standalone bundle." |

### Why This Matters (Colin's Framing)

Colin escalated the urgency of this blocker with specific business justification:

- "We need it. It was told that we would have it."
- "If we continue on the temporary machines, we are effectively going to have to redo all of our work every four weeks."
- "That's a non-starter for me. Like the temp machines are good to get you all some familiarity with this system, but it is not enough to actually work on because it's like you have a Git repository that disappears every four weeks."
- "Even if you do have a Git repo, you shouldn't have to set up all services from scratch every four weeks. That's crazy."

This blocker was also documented in the April 10 standup (01_standup_blockers) where the permanent ADS was listed as "Blocked" requiring the DCN Switching tenant.

---

## 4. Blocker #3: WebEx API Limitation (Org-Level Token)

### Who reported it: Srikar Madarapu

### Current Status: Architectural blocker -- requires Cisco org-level decision

Srikar explained a fundamental limitation in the WebEx API that affects the Pulse/meeting transcript work. Using a personal developer access token, a user can only access meetings that they themselves created. They cannot programmatically access meetings created by others, even if they were an attendee.

Srikar's explanation: "If let's say like I'm the user and I'm creating the meeting, I can use my API key like access token and extract the recordings as well as that transcript, everything related to the meetings. But if Namita is like creating the meeting and I have to access that meeting, I can only download transcript manually from that meeting link. But if I have to access through the API, then I have to get the access token of Namita, but which is not like usually the right way."

The solution requires an organization-level token: "Only the manager level, I think they can create like org level token to extract these recording details like transcript, audio, and other details which are done from the WebEx API."

Saurav confirmed the technical architecture: "It's not like a bot, it's a service app on WebEx which is doing all of these with like scope permissions."

### Implications

Colin connected this to a broader security concern. An org-level access token to meetings raises access control questions: "What if I was to say, whoever the CEO of Cisco is, I want to read all of his meetings. Is there access control properly scoped in these existing apps?"

Saurav noted an ironic defense of the current architecture: the per-user token model, while creating duplication, does solve the data leakage problem: "Maybe they have built it like intentionally bad. The way they have currently built it, it does solve the problem of this like chat leaking because everyone is scraping their own chats and doing their own work."

Colin acknowledged this but said the proper solution is "properly gated org level tokens for a given probably a team" rather than accepting the duplication trade-off.

### Action Required

This needs to be raised with Srinivas as a design decision. BayOne cannot build a production-grade meeting transcript system without an org-level or service-app-level token, which only someone with organizational authority at Cisco can provision.

---

## 5. Blocker #4: Three Separate GitHub Enterprise Servers

### Who reported it: Colin Moore

### Current Status: Structural impediment

Colin identified that Cisco runs at least three separate GitHub Enterprise servers. He mentioned this while discussing the Scribble/Pulse naming confusion: "In reality too, there's like three different GitHub Enterprise servers as well, if you notice that."

Saurav confirmed: "Yeah, yep."

Colin's assessment: "So that makes it even three times worse because now you have to request access even more. That's just crazy."

### Implications

This multiplies the access burden. Each repository could be on a different GitHub Enterprise instance, meaning that having access to one instance grants no access to repos on another. The team must identify which instance a repo lives on before they can even begin the access request process.

This was not documented in the April 10 standup blockers -- it is a new observation surfaced in this call.

---

## 6. Blocker #5: No Documentation on Any Repositories

### Who reported it: Saurav Kumar Mishra

### Current Status: Ongoing impediment

Saurav stated: "None of the repos have like any kind of documentation on that. So that also adds like a little bit more time that we do not have like any way to quick start on the repo. We have to first go dive into the repo first, figure out what is happening, and then start the work."

This was reinforced later when Srikar and Namita reported that they asked Justin about existing architecture diagrams: "Justin mentioned like they don't have any of such kind. In general, like we asked like they use Miro or anything. They said like just the PowerPoint. They use for architecture diagrams and all."

Colin turned this into an opportunity: "Documentation of architecture. That's something that we can do pretty darn easily. We can build a skill or some plugin for them that'll go and auto document architecture every time there's a code change."

---

## 7. Blocker #6: Saurav's Hardware Situation (Loaner Laptop)

### Who reported it: Colin Moore (indirectly -- Colin said he was saving Saurav and Vaishali for last "because you have the laptop thing")

### Current Status: Not fully discussed in this call

Colin indicated that Saurav has a hardware issue with a loaner laptop. He said: "I'm going to keep you and Vaishali for last because you have the laptop thing." However, the detailed discussion of this blocker did not fully occur during the recorded portion of Colin's participation.

From context in the call, Saurav's original laptop is described as "dead" -- his previously-built WebEx bot was on "my like dead laptop on local." The team is working with whatever replacement hardware is available.

Vaishali also appears to lack WebEx access -- Colin told her: "Vaishali, you're the odd one out right now. You can make a WebEx account with your BayOne email, and I can add you in temporarily."

---

## 8. Blocker #7: Rui Guo's NexusT Agent -- Potential Scope Conflict

### Who reported it: Colin Moore

### Current Status: Open question requiring Srinivas clarification

Colin showed the team a WebEx channel called "NxOS CI Workflow" where a Cisco employee named Rui Guo has already built a production-grade application called the "NexusT Agent." This agent performs automated failure analysis using GPT 5.4, generates write-ups, provides a topology view, and offers a chat interface for failure cases in the Nexus pipeline.

Colin's concern: "There are like 4 teams doing the same thing." He listed the potential overlaps:
- Rui Guo's NexusT agent
- Justin's existing build analysis work
- The CI workflow team
- BayOne's assigned work

Colin's specific questions for Srinivas:
- "What are we doing here? Like, are we building a duplicate of this?"
- "Should we be working with Rui directly?"
- "Is this just a POC, like you said, sir, for a hackathon? Or is this something that we are trying to build off of?"
- "How does our work relate to Justin's work relate to this?"

He also noted that Rui's work contradicts an earlier requirement from Srinivas: "Ironically, they had kind of violated something they had told us in the beginning, which is that they wanted something inside of VS Code itself." Rui's agent is a standalone application, not a VS Code integration.

Colin flagged that accessing Rui's repo would require yet another access request: "It's on yet another repo. So I don't know if we'll get access to this unless we're friends with Rui."

This is not a traditional access blocker but rather a scope blocker -- without clarity on how BayOne's work relates to Rui's, the team risks building something that duplicates existing production work.

---

## 9. Blocker #8: Missing Meeting Transcript (April 11 Friday Meeting)

### Who reported it: Colin Moore

### Current Status: Open request to team

Colin mentioned he found a recording from the Friday April 11 meeting with Srinivas but cannot see a transcript for it in the WebEx desktop app: "Whenever I'm on the WebEx desktop app, I am not able to see a transcript for that last Friday meeting."

He asked the team to look for it: "If anyone wants to look for that and find it, if you can send that file in the group chat, if it's possible, that's great."

This is a minor but notable blocker because Colin uses meeting transcripts as primary source material for his Singularity processing and for preparing materials for Srinivas.

---

## 10. Items Resolved Since April 10 Standup

### Resolved: Justin's Build Logs

Namita confirmed she was able to get all the logs from Justin Joseph. Colin asked: "You were able to get all the logs from Justin Joseph then?" Namita confirmed: "Yes." Colin acknowledged: "Okay, so that is good and I think I was reading that in the breakdown that you sent as well."

This was previously listed as dependent on ADS/NFS access in the April 10 blockers matrix.

### Resolved: GitHub NX-OS Repository Access

Not explicitly discussed as a blocker in this call, which implies it is now working. In the April 10 standup, this was listed as "Granted as of morning of 4/10" with pending verification.

### Resolved: Namita's WebEx Access

Namita appears to be fully functional on WebEx. Colin added team members to the "NxOS CI Workflow" channel during the call. However, Vaishali still lacks WebEx access.

### Partially Resolved: Temporary ADS Machines

The temporary machines are functional (evidenced by the team being able to access logs), but the permanent machine remains blocked. The 4-week expiry clock is ticking on the temporary machines.

---

## 11. Access Dependency Chain (Updated from April 10)

```
Pulse/Scribble Repos
  |-- Requires: Srinivas approval (since April 10)
  |-- Sub-blocker: naming confusion (scribble vs. scrubber)
  |-- Sub-blocker: Naga unresponsive to link requests
  |-- Sub-blocker: repos may be on different GitHub Enterprise instance

Permanent ADS Machine
  |-- Requires: Tenant ID (requested ~April 3-4, Mahavir "approved" but not visible)
  |-- Requires: Standalone bundle (requested April 11, no response)
  |-- Without this: all work resets every 4 weeks

WebEx API (Org-Level Token)
  |-- Requires: Cisco org-level decision
  |-- Without this: no programmatic access to other users' meeting transcripts
  |-- Current workaround: manual download from meeting links

Rui Guo's NexusT Agent
  |-- Requires: scope clarification from Srinivas
  |-- Requires: access to Rui's repo (not yet requested)
  |-- Risk: BayOne work may duplicate existing production system

Three GitHub Enterprise Servers
  |-- Each repo may require separate access requests on different instances
  |-- No central directory or documentation of which repos live where
```

---

## 12. Colin's Ultimatum Strategy

Colin's planned approach for the email to Anand and Srinivas has several components:

1. **Praise the team, flag the process:** "This is great, everything's good, but you need to be aware of where the limitations actually are."

2. **Shift responsibility to Cisco:** "It must be resolved by the Cisco team so that we can run at full speed."

3. **Demand a deadline:** "Let's pick a date that that must be resolved by."

4. **Demand a single point of contact or clear process:** "Give me a list of what I should do" -- rather than being told to contact 30 different people.

5. **Escalate to Anand directly:** Colin repeatedly mentioned Anand by name as someone who needs to see this. Anand is Srinivas's boss. Colin's intent is to make the access dysfunction visible at a level above Srinivas.

6. **Propose a new access protocol:** For any future repo assignment, Colin will request three things upfront: a link to the repo, the owner, and access granted at the time of assignment.

7. **Frame the cleanup recommendation:** Colin said if he were in charge, he would tell Cisco: "Everyone, stop everything you're doing. We're having a cleanup day. We're going to rearrange all the repositories. We're going to figure out what needs categorized as stage production and things that are just POCs, things that are in development."

---

## 13. Colin's Meeting with Anand

Colin mentioned he has a meeting with Anand (and Yogesh and Rahul) scheduled for the same day: "I got to meet up with Anand at what? I think like noon PST or maybe a little bit 11:30 AM PST to talk about the renewal contract. And I'm going to bring up some of these things when we have that conversation."

He framed the access issues as connected to the contract renewal: "Let me take some time to get ready for that and get everything ready so that we get more money for this."

---

## 14. New Action Items from This Call

| Item | Owner | Status |
|---|---|---|
| Meet Naga in person at Cisco to get Pulse and Scribble repo links | Srikar | Planned for today (April 16) |
| Prepare email to Anand and Srinivas cataloging all access blockers with timelines | Colin | In progress -- using this transcript |
| Look for Friday April 11 meeting transcript and share in group chat | Team (anyone) | Open |
| Get WebEx scraper working to extract NxOS CI Workflow channel messages | Srikar (initial), team effort | In progress -- Srikar extracted ~6,500 messages but hit timeout/duplication issues |
| Vaishali to create WebEx account with BayOne email | Vaishali | Open |
| Add all team members to NxOS CI Workflow WebEx channel | Colin | Completed during call |
| Meet with Anand to discuss renewal contract and raise access issues | Colin | Scheduled for ~11:30 AM - noon PST, April 16 |
| Schedule follow-up session with Namita and Srikar on architecture | Colin | Planned for later April 16 |

---

## 15. Open Questions and Unresolved Points

1. **Is Scribble on a different GitHub Enterprise instance than the CI/CD repo?** The team can see "scrubber" in the CI/CD org but not "scribble." It may live on an entirely different GitHub Enterprise server.

2. **Who is the actual owner of the Scribble repository?** Naga built it, but Srinivas may be the admin. Neither has provided a direct link.

3. **Why has the tenant ID not appeared despite Mahavir's approval?** Namita reported Mahavir said he approved it, but it is not visible. Is this a systems delay, a permissions issue, or was the approval not actually processed?

4. **How will Cisco provision an org-level WebEx token?** This is not a simple access request -- it requires an organizational decision about scope and authorization. No one at Cisco has been identified as the person to make this decision.

5. **What is BayOne's role relative to Rui Guo's NexusT agent?** Four teams appear to be doing overlapping work. Without Srinivas's clarification, BayOne risks duplicating production-ready work.

6. **What is the status of Saurav's replacement hardware?** The topic was flagged but not fully discussed. His original laptop is dead, and the WebEx bot he built is inaccessible on it.

7. **Will Vaishali have full access to Cisco systems?** She currently lacks WebEx access and appears to be the least connected team member to Cisco's infrastructure.

8. **Are the scraped WebEx messages (6,500) deduplicated and accurate?** Colin noted duplicate timestamps, duplicate body messages, and duplicate senders in the CSV, suggesting the paginated API is returning overlapping results. Srikar planned to investigate time-based API parameters as a fix.

---

## 16. Summary: Blocker Status Matrix (as of April 16)

| # | Blocker | Reporter | First Requested | Current Status | Dependency |
|---|---|---|---|---|---|
| 1 | Pulse repo access | Srikar | April 9 (verbal from Naga) | Blocked -- naming confusion, no repo link, Naga unresponsive | Srinivas approval + correct repo identification |
| 2 | Scribble repo access | Srikar | April 9 (verbal from Naga) | Blocked -- same as above | Srinivas approval + correct repo identification |
| 3 | Permanent ADS machine (Tenant ID) | Namita | ~April 3-4 | Blocked -- "approved" by Mahavir but not visible | Cisco infrastructure team |
| 4 | Permanent ADS machine (Standalone bundle) | Namita/Srikar | April 11 | Blocked -- no response | Cisco infrastructure team |
| 5 | WebEx org-level token | Srikar | New (identified this call) | Architectural blocker -- not yet formally requested | Cisco organizational decision |
| 6 | Scope clarity (NexusT vs. BayOne work) | Colin | New (identified this call) | Open question for Srinivas | Srinivas clarification |
| 7 | Three GitHub Enterprise servers | Colin | New (identified this call) | Structural impediment -- no resolution path defined | Cisco organizational structure |
| 8 | No repo documentation | Saurav | Ongoing | No resolution expected -- BayOne may propose automated solution | None -- accepted as baseline condition |
| 9 | Saurav's dead laptop / loaner quality | Saurav | Pre-existing | Flagged but not fully discussed | BayOne hardware provisioning |
| 10 | Vaishali WebEx access | Colin | This call | Vaishali to create BayOne WebEx account | Vaishali action |
| 11 | Friday April 11 meeting transcript | Colin | This call | Team to locate and share | Anyone with access |

### Resolved Since April 10

| Item | Resolution |
|---|---|
| Justin's build logs | Namita confirmed she received all logs |
| GitHub NX-OS repo access | Functioning (no longer mentioned as blocker) |
| Temporary ADS machines | Working but time-limited (4-week expiry) |
