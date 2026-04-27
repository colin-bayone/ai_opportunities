# 16 - Srinivas Sync: ADS Provisioning Resolution

**Source:** /cisco/cicd/source/week_2026-04-27/day_2026-04-27/srinivas_team_meeting_2026-04-27_formatted.txt
**Source Date:** 2026-04-27 (Monday Cisco-side Srinivas sync, 1pm PST, ~60 minutes)
**Document Set:** 16 (Main chain Cisco-side Srinivas meeting)
**Pass:** Focused deep dive on the ADS provisioning resolution driven by Anand and Divakar that closes Blocker 1 of the prep deliverable

---

## Executive summary

Permanent ADS provisioning, the number one blocker on Colin's prep deliverable for the week, was resolved live in the meeting within roughly six minutes. Anand cut Colin off mid-agenda to pull the ADS topic to the front. Divakar, who joined late, drove the operational resolution. The agreed plan is to retire four to five underused VMs from a previous procurement and stand up two new ADS machines for the BayOne engineering team, with one of the existing machines left available as an interim work surface for the entire week. Hardware was confirmed at 16-core CPU, 32 GB memory, 100 GB local storage, no backup, with Srinivas explicitly confirming 16 cores as the minimum required for the team's RAM-loaded workload. Timeline commitments are firm on the interim machine being available immediately, with the new machines targeted for today evening but realistically by tomorrow or later in the week. CN-SJC-STANDALONE bundle membership for the new machines was raised by Divakar and Anand committed to verify against existing email.

This unblocks Blocker 1 of the prep deliverable and also indirectly clears the dependency chain for DeepSight access, the CI/CD application deployment fallback path, and the Friday WebEx bot deployment.

---

## Anand's intervention pattern

Colin had just finished walking through the structure of the weekly status sheet, taken Srinivas's feedback on collapsing sub-items under a single top-level bullet per workstream, and was beginning the second current-work line ("So then, uh, the WebEx spot...") when Anand cut in directly:

> "I just want to start out with the ADS thing. I think you are on the same item, probably. What exactly is needed and what Mahaveer should help?"

This is a classic executive-sponsor intervention. Anand, as the senior Cisco stakeholder on the call, had clearly read or been briefed on the deliverable, recognized that ADS was the upstream blocker driving the rest of the agenda, and pre-empted Colin's bottom-up walk-through to drive direct resolution while Divakar was on the line. Anand's framing is operational, not deliberative, and points immediately at a specific person who can help (Mahaveer reference, likely Divakar's team).

Anand stays engaged throughout the resolution, offering ratifying comments at each turn:
- "I don't think anybody's using it." (confirming the underused VMs are safe to retire)
- "Yeah, that we can serve. So multiple engineers can serve in this night."
- "Yeah, makes sense. I think let's go with two now. And if we can put in more and then they can access and that."
- "Okay, let me look at my email, ladies. What you're saying? Okay, cool." (committing to verify CN-SJC-STANDALONE bundle membership)

Anand does not delegate the conversation; he stays in it from start to finish and personally takes the bundle-verification action item.

---

## Divakar's late arrival and polite deflection

Divakar joined the call late. His self-introduction at 00:00:55 acknowledges the late arrival without dwelling on it:

> "Hey, Clyde. Did I first really okay? So many things to join. Yes, really."

The transcript is mangled, but the intent is a polite, brief acknowledgment ("first really" is likely "first one really" or similar) and a soft excuse ("so many things to join") rather than an apology. He moves immediately into the meeting flow without further comment.

When Divakar later raises the issue of him not being able to attend every meeting (in the context of asking Srinivas to attend his own working sessions for parallel-effort awareness), he frames it as a mutual scheduling issue rather than a defensive posture:

> "There are times where we are actually losing. I am not able to join all the meetings, but I do whenever I have a time, definitely will come."

This is consistent with Divakar's posture as the operational lead who is in many meetings simultaneously and triages attendance. The tone is collaborative, not apologetic.

---

## The operational resolution, step by step

### Step 1: Anand opens the topic, Colin frames the dependency

Colin's framing of why ADS is the upstream blocker:

> "So ads I think is upstream of a lot of different things here because ads is upstream of deep site. It's upstream of being able to deploy on anything more than a temp server, which makes it upstream of this week's deliverable too."

Colin then surfaces the two sub-questions from the deliverable: who is responsible for Permanent ADS provisioning, and is it even possible given the resource constraint flagged on April 24.

### Step 2: Divakar asks the sizing question

> Divakar: "How many ads machines are we looking at to collect?"
> Colin: "Uh, just the one. Just the one. We really just need one to get done."

Colin asks for one machine. Divakar, working from what is operationally available to him, immediately proposes a more generous configuration.

### Step 3: Divakar proposes the retire-and-procure plan

> "I can probably go with uh- huh. I think we procured about four or five different uh VMs last time. Can I retire them? I think I meant you mentioned that they're not as powerful as you want them to be."

Anand confirms nobody is using them. Divakar continues:

> "Retire them and I'll procure a couple of additional machines for the engineers here."
> "I think we can use the same RDS [ADS] machine, but uh maybe we can procure two. That way they can have access to both of them if they need to use that."

Anand ratifies: "Yeah, makes sense. I think let's go with two now."

The plan crystallized in this exchange:
- Retire four (or four to five) underused VMs from a previous procurement
- Procure two new ADS machines for the BayOne engineering team
- Leave one of the existing machines available as the interim work surface

### Step 4: The interim machine commitment

Divakar's exact commitment on the interim machine:

> "We can leave one machine, the previous machines whatever we have procured, we can leave one machine for them to use it in the meantime. Eight days procedure will take little time, but other four I am going to retire and I am going to create two. But while that is going on, they can use one of that machine."

And again, more explicitly later:

> "I will leave one of them, the top for the first one. Rest of the ones I'll retire and I'll put it in. But the bundle is available for them this entire week. I'll return it next week."

The interim machine is available for the full current week. Retirement of the rest happens in parallel with the new procurement.

### Step 5: Hardware spec lock-in

This is the part of the conversation where Srinivas, having been quiet during the operational handoff between Anand and Divakar, steps in to lock in the hardware floor.

Divakar opens with the use-case question:

> "Once you get the ADFS server, what are the things you want to use on that? I think, To the new one,"

Srinivas responds:

> "We need that at least sixteen core radius for this team because we have to bring in the radius right? And then the data."

In context, "radius" here is RAM. Srinivas is saying the team needs a 16-core machine plus enough RAM to load the data into memory. Divakar's response confirms 16 cores is also his ceiling:

> "Yeah, I'll procure a 16 core. The maximum cores I can get is 16."

Srinivas pushes back to make clear this is not a negotiation:

> "But that is the minimum we need though for this project."

Divakar's response captures the full envelope:

> "So that's the minimum, that's the maximum. Got it. And the maximum memory I can get you is 32 GB. I cannot go beyond that."

Srinivas accepts: "That's fine. At that, those at least that piece is those two information is good enough."

Storage and backup are settled in one line:

> Divakar: "It's going to local 100 GB and no backup I'll give you."
> Srinivas (implicit acceptance): "Yeah, no backup, yeah, right now no no."

**Final hardware spec:**
- CPU: 16 cores (both the team's minimum and Divakar's procurement ceiling)
- Memory: 32 GB (Divakar's procurement ceiling)
- Storage: 100 GB local
- Backup: none
- Quantity: two machines

Srinivas adds an important caveat about scope: "Not for this machine. We need for other, but not right now." This signals that for future workstreams (likely the larger data-loaded chat backend), more capacity will be needed but is not in scope today.

### Step 6: Bundle membership

Divakar raises this against Anand directly:

> "So make sure that they're part of our bundle, CNS JS bundle [CN-SJC-STANDALONE bundle]. That one I think is already part of as far as you know. Just can help with that one."

Anand's response is to commit to verify against email:

> "Okay, let me look at my email, ladies. What you're saying? Okay, cool."

This is a Cisco-side action, not a BayOne action. The team should expect Anand to either confirm membership or raise it again if there is an issue.

### Step 7: Timeline commitment

Srinivas asks the direct timeline question:

> "So Diwakar can provision one and give it to you immediately today. Diwakar, can you do it in next few minutes? That way ADS."

Divakar's response sets the realistic expectation:

> "I am going to give it. But the mission [machine] which I procured for you, they are available for the immediate users."

Then more precisely:

> "By today evening mostly other other things are to be taken care of. So it will take a day or probably we'll see. It might be early. I cannot guarantee, but that's why I am leaving one machine for you. You can visit that machine for next one week. When the other machines come up, I'll give it to you, but I've got to leave the one machine for you."

**Timeline commitments captured:**
- Interim machine: available immediately, for the entire current week
- New machines: target today evening, realistically a day, possibly earlier, no guarantee
- The interim machine is the safety net specifically because Divakar will not commit to a hard date on the new ones

### Step 8: Local user ID verification

Anand surfaces a small open item:

> "The local user ID has Q 1, Q 2. I think. Okay, I'll just going to double check. We're not using it."

Divakar: "Yeah, send it to me. I'm going to verify that one."

Srinivas confirms: "We are not using Duo Office at all, Anand. That much I know."

This is a minor verification step on existing user IDs on the interim machine, not a blocker.

### Step 9: Communication of access

Srinivas closes the topic by asking Anand (likely the "Adhvik" reference) to post the machine details to the WebEx engagement space so the BayOne team can see them:

> "Adhvik, just put it in the webex where then team can see it?"
> Divakar: "Yeah, I'm going to do that right now actually. And the ones who wants to send me the details,"
> Anand: "Then I'll put that. I just sent it to your members' message."

The handoff to the team is via the engagement WebEx space, consistent with the asynchronous-unblocking pattern already in place.

---

## Mapping to the prep deliverable's Blocker 1

Blocker 1 in the prep deliverable read:

> **Permanent ADS availability.** The team has been requesting Permanent ADS access since April 14, with follow-up on April 21. On April 24, Permanent ADS resources were noted as currently constrained on the Cisco side.
> - Who is responsible for Permanent ADS provisioning, and is that even possible given the current resource constraints?
> - If no Permanent ADS servers are currently available on the Cisco side, how could one be provisioned for this engagement?

Both sub-questions are answered:

| Prep deliverable question | Resolution from the meeting |
|---|---|
| Who is responsible for Permanent ADS provisioning? | Divakar Rayapureddy is responsible. He owns procurement of the new machines and the retirement of the underused existing VMs. Anand owns the bundle-membership verification. |
| Is Permanent ADS provisioning even possible given resource constraints? | Yes. The constraint is solved by retiring four to five underused VMs from a previous procurement and reallocating that capacity to two new ADS machines for the team. |
| If no Permanent ADS servers are available, how could one be provisioned? | Two new machines provisioned at 16-core / 32 GB / 100 GB local / no backup, plus one existing machine left available for the entire current week as the interim work surface. |

The deliverable's Friday caveat ("If a Permanent ADS is not available, the only possible path forward for Friday is to deploy on the Temporary ADS server, which is now connected and ready") is no longer the binding fallback. The interim machine that Divakar is leaving available, plus the two new machines targeted for today evening to within-the-week, mean the team has a Permanent ADS path open for Friday in addition to the Temp ADS already connected.

---

## Open hardware and access questions remaining

Most of the substance is closed. The residual open items as of the meeting close:

1. **Bundle membership verification.** Anand committed to verify CN-SJC-STANDALONE bundle membership for the new machines against his email. Outstanding.
2. **Local user ID verification on the interim machine.** Anand to confirm whether the existing Q1 / Q2 user IDs on the prior machine are unused so the team can take them over. Srinivas confirmed Duo Office is not in use. Outstanding but minor.
3. **Hard delivery date for the two new machines.** Divakar will not commit firmer than "today evening, probably a day, might be early, cannot guarantee." This is mitigated by the interim machine being available for the full week.
4. **Posting of access details to the WebEx engagement space.** Divakar committed to post immediately; Anand committed to add to the members' message. Team should watch for this asynchronously.

---

## Downstream implications for the rest of the engagement

The unblock has knock-on effects on three other items that were either explicitly or implicitly waiting on it:

- **DeepSight access.** Earlier in the deliverable, DeepSight credentials were gated on the team operating from an ADS environment. Once the interim machine is in hand today and the new machines are stood up this week, the DeepSight gate clears and the language model access path (Blocker 2) becomes actionable. Srinivas confirmed later in the meeting: "as soon as you get the AD server, you need to build the A CACD app and try to deploy on your ADS server and see if you can bring it up." DeepSight is expected to handle the language model credential plumbing automatically once the team is on ADS.
- **CI/CD application deployment fallback.** The deliverable noted BayOne is ready to stand up the CI/CD application directly on Temp ADS as a fallback if the Cisco platform team deployment is not ready. With Permanent ADS now in motion, the team has a stronger primary surface for the Friday deployment.
- **Friday WebEx bot.** WebEx bot deployment is gated on bot compliance and IT audit (separate Blocker 3), but the bot's runtime needs ADS to host. The ADS unblock removes one variable from the Friday path even as the IT audit timing remains outside BayOne's control.

---

## Why this is the major operational outcome of the meeting

Three things make this the headline outcome:

1. **It was the longest-standing blocker in the deliverable.** The team had been waiting on Permanent ADS since April 14, with follow-ups on April 21 and April 24. It was item one on the prep deliverable's critical-path list for a reason.
2. **It was resolved live, not deferred to follow-up.** Anand pulled it forward, Divakar committed to specific hardware and a specific delivery posture, and the conversation closed with concrete actions on both sides. There is no "we'll get back to you" in this segment.
3. **It is the cause behind multiple downstream items.** Removing this blocker shifts the engagement from a defensive posture (relying on Temp ADS as the only viable Friday path) to an offensive one (interim machine immediately, new permanent machines this week, DeepSight and CI/CD application both able to come online on the new infrastructure).

The pattern is also a useful tell on the engagement dynamics. Anand operates as a hands-on executive sponsor who will pre-empt agenda flow when he sees a critical-path item; Divakar operates as the operational lead who can commit hardware in real time without escalation; Srinivas defers to both on the operational specifics but locks in the technical floor (the 16-core minimum) when it matters. This is a healthy stakeholder configuration for the engagement.
