# Meeting 1 Answers Captured
**Date:** February 17, 2026
**Attendees:** Colin (BayOne), Anand (Cisco), Divakar (Cisco), Srinivas (Cisco)
**Source:** meeting1_anand_srini_divakar-2-17-2026.txt

This document captures answers to discovery questions from the first in-person meeting.

---

## Answers Captured

### Q1: Is there an internal ticketing system (ServiceNow, Jira, etc.) we should use to request access?

**Answer:** No formal ticketing system in use. The team tried Jira for about a year but received significant pushback from engineers who said they couldn't create a ticket every time they needed something. The culture is very informal - people ping directly and say "take care of this." Divakar noted: "We are used to very informal... today I don't think there is an informal to talk something."

The preferred method is the WebEx space (BayOne CICD WG). Anand reinforced this, saying if questions aren't getting answered, escalate through the WebEx space and he'll help expedite. Srinivas also emphasized using the WebEx space and said he'd add engineers to the group who can answer questions.

**Implication:** No ticket system to request access through. Use WebEx space for all requests. Anand and Srinivas will monitor and help unblock if needed.

**Status:** ANSWERED

---

### Q2: Who is the single point of contact responsible for ensuring BayOne team members receive access?

**Answer:** Divakar is the primary point of contact for access. When asked directly, he said: "At least for the ones which are on the top, I would be the one." He specifically mentioned he has full context on Jenkins and will handle provisioning ADS machines (Linux machines needed for code access and building).

However, different teams own different systems, so Divakar will need to coordinate:
- **GitHub Enterprise:** Requires training (3-4 hours), then Divakar can grant access after completion
- **Jenkins:** Divakar has full context and direct ownership
- **Airflow:** Needs to contact another team
- **CAT:** Needs to contact another team
- **DevX:** Another team owns it, but "we can get to that data as well"

For escalation, Anand made clear he would ensure things move if they get stuck: "if something is not moving, then I will be expedited" and "I'll try to make sure that I'm paying attention." He also said to ping him directly if needed to resolve blockers.

Srinivas added that for the DeepSight AI platform side, he would be the contact and would connect BayOne with the right engineers.

**Status:** ANSWERED

---

### Q3: What is the typical turnaround time for access provisioning?

**Answer:** Divakar said turnaround depends on completing required training, but once that's done: "Should not be more than half a day, maybe a day max." The bottleneck is the training itself (3-4 hours for GitHub Enterprise). Once training is complete, access can be granted quickly.

Srinivas mentioned a related internal pain point: "any time any new engineer joins... we are spending a lot of time to get the ADSR or the provision to those engineers. And it is done by Cisco but it is taking time from us... there is no set procedure on what they need to follow." Anand acknowledged this as something to monitor and improve as they scale.

*Note: This internal onboarding friction is not directly our problem to solve, but it's good they're aware of it. Could be a future avenue for business process automation work.*

**Status:** ANSWERED

---

### Q4: What is the network access model for external contractors? (VPN credentials, IP whitelisting, etc.)

**Answer:** The network access model is VPN. Divakar was clear: "It will be VPN. If you don't have VPN, it probably won't allow you to connect to emails or machines or anything."

There are two options for machines:
1. Get a separate Cisco-provided machine with Cisco image
2. Use your own laptop and install the Cisco image on it ("There's some documentation related to that one")

When asked if the team has Mac vs Windows preferences, Divakar said: "No, there are people who [use] Windows as well. Sometimes teams are specific to that platform." So no strong platform preference.

Rahul Bobbili on BayOne's side has already initiated the equipment/network access process for at least some team members.

**Status:** ANSWERED

---

### Q5: Who initiates the network access process, and what information do you need from us to start it?

**Answer:** This wasn't directly answered in detail. Colin mentioned that Rahul Bobbili "has already initiated that for at least the equipment side for this network access process" and Divakar seemed to confirm that's the right approach.

The implication is that BayOne initiates through Rahul Bobbili coordinating with Cisco. The specific information needed from BayOne wasn't enumerated in this meeting.

It sounds like much will be resolved by using Cisco-provided equipment, but nothing certain has been established here. Need to keep a close eye on this to ensure no issues arise.

**Status:** PARTIALLY ANSWERED - needs follow-up

---

### Q6: Are there different access tiers for onshore vs. offshore team members?

**Answer:** No. Divakar said directly: "No, I don't think." Colin confirmed the team size (five people total, three onshore including himself, two offshore) and Divakar didn't indicate any different treatment would be needed for offshore vs. onshore.

**Status:** ANSWERED

---

### Q7: Who initiates the background check process - does Cisco send us forms, or do we need to contact someone specific?

**Answer:** This is handled on the BayOne side through Rahul Bobbili coordinating with Cisco. The process is already well in place. Colin's background verification is now complete and NDA has been signed.

**Status:** ANSWERED (already known/resolved)

---

### Q8: Can we begin non-sensitive discovery work (documentation review, architecture discussions) while background checks are in progress?

**Answer:** Yes. Colin asked directly if non-sensitive discovery work could begin to get the ball rolling, and they responded affirmatively. Colin replied "OK, I always have to ask to be on the safe side."

Srinivas reinforced this by sharing information about the DeepSight platform even before confirming NDA was signed, saying "I assume that NDA is signed. I'll share you an email ID" with a presentation and recording. He was willing to share materials to get Colin started on understanding the platform.

Anand also emphasized using the WebEx space to collaborate and getting questions answered even before full onboarding: "we want to make it that use of the [WebEx] to collaborate."

**Status:** ANSWERED

---

### Q9: Will BayOne developers receive Cisco-managed machines, or use their own with VPN access?

**Answer:** Two options for laptops:
1. Get a separate Cisco-provided machine with Cisco image
2. Use your own laptop and install the Cisco image on it

Colin is getting a Cisco image laptop.

Additionally, for accessing and building code, Divakar will provision ADS machines (Linux machines in Cisco's data center): "You need an ADS machine to view the code and other things over there... That would be a Linux machine to be provisioned to these users so they can log into those machines to check out the code or view the code and be able to build and stuff like that." Divakar confirmed: "I would be the one to give that access."

These Linux machines are accessible over VPN, effectively allowing remote team members to act like they're on-site. However, the Linux machines are not critical for BayOne's core development work - they serve as a staging area to interact with Cisco infrastructure or run builds, since that can't be done on local machines that aren't on-prem.

**Status:** ANSWERED

---

### Q10: How can we test developer-side tooling if we don't have the same local environment as Cisco engineers?

**Answer:** Divakar explained that ADS Linux machines provide the environment: "Once you get into that [ADS machine], then you can start checking out the [workspace] and be able to build the code and look at the code."

For the CI/CD tooling itself, Divakar noted: "We have a development, but we are not using it as much." BayOne would have read-only access to watch PR validations but couldn't open new PRs directly.

The ADS machines serve as the environment where BayOne can test and interact with the codebase. However, the specifics of how to test developer-side tooling (like an agent on developer machines for Item A) wasn't fully explored in this meeting.

**Status:** PARTIALLY ANSWERED - ADS machines provide access, but Item A testing approach needs further discussion

---

### Q11: Is there a staging or dev environment for CI/CD tooling where we can safely test changes before production?

**Answer:** There was a communication gap here. Divakar discussed read-only access to Cisco's repos and their underutilized dev environment, but that wasn't the actual question.

The real question was about governance for BayOne's development work: Where does BayOne's code go? Will Cisco provide a repository? If BayOne writes code, what's the workflow for committing and reviewing it? Read-only access to Cisco's repos is helpful for understanding their codebase, but BayOne needs somewhere to commit their own development work.

Srinivas later mentioned that for DeepSight: "as a part of the deep side, we have the repos created for every application" and BayOne would "commit a code there" with code review from others. This may partially answer the question for the DeepSight/AI platform side, but the broader governance question for all BayOne work was not fully addressed.

Either Cisco tells us what to use, or BayOne will need to set something up independently and coordinate.

**Status:** NOT ANSWERED - communication gap, needs follow-up on development workflow governance

---

### Q12: What is the process for provisioning on-prem servers for this project? Do we spec requirements and Cisco provisions, or is there a self-service model?

**Answer:** Divakar wasn't entirely sure about the process: "I think it's self-service, but I don't know. Yeah, I'll check with IT and that one. So we have about three services which we are using from the IT. Do I need to procure another one? I don't know."

Colin mentioned they could always stack on top of existing services if available. However, Colin also noted that BayOne can't be specific about sizing requirements yet - they don't have the discovery details about scope or throughput to properly size things. Questions like number of transactions, rows, and concurrent connections need to be answered first.

Regardless of the provisioning model (self-service vs. IT provisions), the key gap is that **who will actually set up the infrastructure has not been identified**.

**Status:** PARTIALLY ANSWERED - Divakar will check with IT, but process and ownership not confirmed

---

### Q13: What database options are available on-prem? (PostgreSQL, MySQL, Oracle, etc.)

**Answer:** Divakar said directly: "All of our services are in MySQL, so I can give you MySQL." Colin confirmed that's fine.

However, if this ends up being a separate/new service rather than stacking on existing infrastructure, Postgres could still be an option. Colin noted that Postgres would serve them better technically, and this could be discussed with Srinivas if he wants technical input. Either way, any relational DB works for BayOne.

**Status:** ANSWERED - MySQL available, Postgres possible if separate service

---

### Q14: Are there existing shared services we should leverage, or should we plan for isolated infrastructure for this project?

**Answer:** Mixed answer depending on the area:

**For AI/DeepSight platform:** Clearly leverage existing. Srinivas was emphatic that the infrastructure is already built - BayOne wouldn't build anything from scratch on the AI stack side. He said: "All you have to do is build an MCP, build a patch of prompts queries and stitch it here... you're not doing anything from scratch, because you'll provide SDK and everything."

**For other infrastructure (database, compute, etc.):** Still TBD. Divakar mentioned "we have about three services which we are using from the IT" and would need to check if a new one needs to be procured. Colin mentioned the option to stack on top of existing services.

**For Airflow:** Colin offered flexibility - if there's a Linux machine on site where Docker containers can be deployed, BayOne could spin something up for early development, or leverage what Cisco already has.

**Status:** PARTIALLY ANSWERED - clear for DeepSight (leverage existing), TBD for other infrastructure

---

### Q15: Is there a preferred deployment pattern? (containers, VMs, bare metal)

**Answer:** Divakar mentioned: "It's a container, but it's not a Docker container. It is a [Podman] container from Red Hat. So we have that provision."

This came up when discussing Airflow deployment options. Their environment uses Podman (Red Hat's container runtime) rather than Docker.

However, they seemed a bit uncertain here and didn't appear to have much practical experience with containerization. In general, if a Linux server is available, there's no reason Docker couldn't be used instead. This is something Colin can clarify with Srinivas.

**Status:** PARTIALLY ANSWERED - Podman mentioned, but flexibility likely exists; needs clarification with Srinivas

---

### Q16: Where does raw pipeline data currently live? (data warehouse, direct database, Prometheus TSDB, etc.)

**Answer:** Divakar answered directly: "It's an on-prem... it's MongoDB." When asked if it's one location or multiple, he confirmed: "No, it's one location."

Note: Divakar distinguished between MongoDB and MySQL but didn't discuss them together, suggesting they serve different purposes. MongoDB likely stores the raw/unstructured pipeline data, while MySQL is used for relational services. Airflow would need something relational, so MongoDB and Airflow are not mixed - MongoDB is probably storing data in an unstructured format.

**Status:** ANSWERED - MongoDB on-prem, single location

---

### Q17: What is the logging stack? (ELK, Splunk, Graylog, etc.)

**Answer:** Divakar said: "We have Splunk connected to our Jenkins to be able to push all our data into Splunk. But I don't know if you can access that one."

He explained Splunk is primarily for the security team: "Splunk is given for the security team for them to go and snoop and find out if there is anything going on maliciously."

However, he offered an alternative: "I can give you the Jenkins access for you to go directly and pick up the log information from there."

Colin confirmed that direct connection would be fine, noting it would be part of the next quarter integration work (Box C) that connects all services together. The good thing about interfacing directly with services is that it's predictable.

**Status:** ANSWERED - Splunk exists but may not be accessible; direct Jenkins access offered as alternative

---

### Q18: What are the data retention policies - how far back can historical analysis go?

**Answer:** Not discussed. The meeting ran out of time before this question was addressed.

**Status:** NOT ANSWERED

---

### Q19: Should we deploy our work to Cisco's existing Airflow instance, or stand up a separate instance for isolation?

**Answer:** Not really answered. Divakar mentioned Podman containers (Red Hat), but this didn't actually address the question of whether BayOne should use Cisco's existing Airflow instance or stand up a separate one.

This touches on two unresolved items:
1. The development environment for BayOne's work and isolation - not answered
2. Airflow deployment strategy - not clear

Likely a miscommunication - Divakar didn't seem to understand what was being asked. Needs further discussion.

**Status:** NOT ANSWERED - miscommunication, needs follow-up

---

### Q20: If using the existing Airflow instance, who is the Airflow SME we should coordinate with?

**Answer:** Divakar mentioned early in the meeting: "I'm watching airflow. I think I need to get in touch with another team."

So Divakar doesn't own Airflow directly - it's managed by another team. No specific SME name was provided.

**Status:** PARTIALLY ANSWERED - know it's another team, but no specific contact identified

---

### Q21: What version of Airflow is currently deployed?

**Answer:** Not discussed in the meeting.

**Status:** NOT ANSWERED

---

### Q22: What AI/LLM services are available to us?

**Answer:** Srinivas showed the DeepSight platform, which is already live. He said: "We already have almost like eight or 10 [apps], but we're going to release one at a time." They've launched triage, runbook is coming end of week, telemetry aggregation exists, and they have a CICD pipeline app in development.

BayOne won't build AI infrastructure from scratch: "You are not building anything in AI stack because all the AI stack is given... Everything else is given to you. All you have to do is build an MCP, build a patch of prompts queries and stitch it here." The platform provides SDK and everything needed.

Srinivas's expectation: "once you get the good understanding of the requirements, and once you onboard your engineers, my expectation is within like two months, we should have an app running live here. Because all the infrastructure is already built for you."

**Status:** ANSWERED - DeepSight platform provides AI infrastructure; BayOne builds on top

---

### Q23: Are there restrictions on what data we can send to these APIs?

**Answer:** Not specifically discussed.

**Status:** NOT ANSWERED

---

### Q24: Are there rate limits or cost considerations we should design around?

**Answer:** Not specifically discussed.

**Status:** NOT ANSWERED

---

### Q25: Is there an internal AI platform team we should coordinate with?

**Answer:** Yes - Srinivas is the contact for DeepSight. He showed the platform live, explained the architecture, and will connect BayOne with his team. He shared a recorded presentation (1-1.5 hours) explaining the platform capabilities.

Srinivas will pull BayOne into other meetings: "at some point, we'll pull you into other set of meetings also, so that when the CICD applications are running, I'll make pull you guys in, so that you know what's happening behind the scene."

**Status:** ANSWERED - Srinivas is the DeepSight contact

---

### Q49: What is the scope of the internal AI project, and where does it overlap with Items A-F?

**Answer:** Srinivas clarified there's an existing CICD application already built: "we already have a CICD application built today. In the next two weeks, I work with Arun's team, Rui is there, to launch that application."

The existing app will be live on the DeepSight platform in 2-3 weeks. It's described as "set up purpose, it does not solve the entire thing" - meaning it's foundational but not complete.

**Status:** ANSWERED - existing CICD app is foundational, will be live in 2-3 weeks

---

### Q50: Should our work integrate with that project, extend it, or remain separate?

**Answer:** Integrate and build on top. Srinivas was clear: "the way I am thinking is for Colin to start, in the next two weeks if Colin is trying to gather the requirement... By that time, if we get our app like next two to three weeks live on the deep side platform with the current form, whatever we have, then Colin can pick it up from there."

He added: "Colin can actually and team can actually take that... stack whatever we have done and build on top of it based on the new requirements."

Srinivas emphasized not duplicating effort: "I do not want Colin to spend time on say what infra will look like, what it is. We will already, we are already 90 percent there, just 5-10 percent there is small issues."

**Status:** ANSWERED - build on top of existing work, do not duplicate infrastructure

---

### Q51: Who owns that project, and should we coordinate with them?

**Answer:** Rui (on Arun's team) is working on the existing CICD app. Srinivas offered to put the request in the WebEx group to connect with Rui.

**Status:** ANSWERED - Rui on Arun's team; coordinate through Srinivas

---

### Q58: What are Cisco's expectations for progress reporting?

**Answer:** Anand said start with a catch-up two weeks after onboarding, then determine ongoing cadence: "So let's two weeks from now, let's do a catch-up between maybe three of us here. And then following week and then we come and catch like how to do it."

He was open to suggestions: "I'm open to suggestions too."

**Status:** ANSWERED - two-week check-in after onboarding, then determine cadence together

---

### Q59: What format works best?

**Answer:** Srinivas strongly emphasized recorded sessions: "One thing I insist... you should always say, can we have a recorded session... make sure that they are recorded and you can refer back and because many other team members will say, hey, take a day, record, go through all the recording."

He added: "Saying something versus recording in place, how to do it, that will make you like 10 constants."

**Status:** ANSWERED - recorded sessions strongly preferred for knowledge transfer

---

### Q60: Who should receive status updates, and who has authority to approve direction changes?

**Answer:** Anand at his level, with Arun involved depending on progress: "at my level and then maybe I have to also keep some places where I can involve Arun also depending on where we are."

For day-to-day unblocking, Anand said to ping him: "if something is not moving, then I will be expedited."

**Status:** ANSWERED - Anand for regular updates, Arun involved as needed

---

### Q61: If helpful, we can propose a reporting cadence - would that be useful?

**Answer:** Anand was open to it: "I'm open to suggestions too."

**Status:** ANSWERED - yes, open to suggestions

---

### Q62: What channel should BayOne use for day-to-day technical questions?

**Answer:** WebEx space (BayOne CICD WG). Confirmed multiple times. Anand said: "we want to make it that use of the [WebEx] to collaborate."

Srinivas added: "keep using the WebEx space... if something is not moving, then I will be expedited."

**Status:** ANSWERED - WebEx space (BayOne CICD WG)

---

### Q63: What are Cisco's delivery expectations for Q3?

**Answer:** Flexible. Anand acknowledged: "I know practically it's never possible to start quarter here and there, so we understand that, and we're very flexible on that."

He added: "Cisco would like to have started, but obviously, really, it's not possible. So we know we deal with these things, so we'll manage it entirely whatever way, most logical way. It's called business reality versus engineering reality."

**Status:** ANSWERED - flexible, understand reality of onboarding delays

---

### Q64: Given current onboarding status, is there flexibility on timeline?

**Answer:** Yes, full flexibility. Anand said directly: **"So whenever we get started, the quarter starts then."**

The engagement timeline will be measured from when BayOne actually has access and can begin work, not from the calendar Q3 start date.

**Status:** ANSWERED - quarter starts when BayOne starts; full flexibility

---

### Q65: What is the realistic target date for BayOne to have meaningful access?

**Answer:** Not given a specific date, but Anand indicated "a week or two to get on board in process." Focus is on getting access quickly, with first check-in two weeks after onboarding begins.

**Status:** PARTIALLY ANSWERED - 1-2 weeks for onboarding, no specific date

---

