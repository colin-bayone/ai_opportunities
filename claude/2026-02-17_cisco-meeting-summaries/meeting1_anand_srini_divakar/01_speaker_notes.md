# Speaker-Specific Notes: Meeting 1

Quick reference for who said what and their areas of ownership.

---

## Anand (Director, Cisco)

**Present:** First ~10 minutes, then briefly at end

**Key Statements:**
- "We really want these things to kind of help us a lot."
- "If we do our job right, your job will be easier. That's how I get ready with the maintenance overload or operational overheads."
- On quarter timing: "I know practically it's never possible to start quarter here and there, so we understand that, and we're very flexible on that. Whenever we get started, the quarter starts then."
- "It's called business reality versus engineering reality."

**Owns:**
- Escalation path for blockers
- Status meeting cadence (2-week check-ins)
- Unblocking access/onboarding issues
- Monitoring this engagement as test case for scaling onboarding process

**Follow-up with Anand:**
- Schedule 2-week status meeting
- SOW finalization (via Zahra)

---

## Divakar (Engineering Lead, Cisco)

**Present:** Throughout meeting (primary contact for Phase 2)

**Key Statements:**
- On systems: "There are different teams for different systems. It's a crossover."
- On ticketing: "We had [Jira] for a year or so. We tried it. But a lot of pushback from the engineers... I think we are used to very informal."
- On access turnaround: "Should not be more than half a day, maybe a day max."
- On dev environment: "If you have a read-only access, you cannot stage anything... You could make it on your workspace and commit... but if you try to push it, GitHub is going to reject your arguments."
- On database: "All of our services are in MySQL."
- On containers: "It's not a Docker container. It is a Podman container from Red Hat."
- On pipeline data: "It's a MongoDB... one location."
- On logging: "We have Splunk connected to our Jenkins to be able to push all our data into Splunk."
- On ADS machines: "That would be a Linux machine to be provisioned to these users so they can log into those machines to check out the code or view the code and be able to build."
- On Bazel: "We just rolled out [Bazel] to production... working with every branch owner to enable Bazel for all of them."

**Owns:**
- GitHub Enterprise access (after training)
- Jenkins access and context
- ADS machine provisioning
- Infrastructure questions (database, logging)
- Airflow outreach (different team)
- DevX Platform outreach (different team)

**Follow-up with Divakar:**
- Complete GitHub training (unlocks access)
- ADS machine provisioning
- MySQL provisioning check with IT
- Airflow team contact

---

## Srinivas/Srini (Senior Engineering Manager, Cisco)

**Present:** Phase 3 (~30 minutes, joined after debugging Bazel issues)

**Key Statements:**

*On DeepSight Platform:*
- "What we have is an AI platform. It's for DeepSight... this is already live."
- "We call this the entire infrastructure DeepSight Atlas."
- "We already have almost like 8 or 10 apps, but we're going to release one at a time."
- "This week we launched Triage... end of this week we're gonna launch Runbook."
- "We already have a CI/CD application built today. In the next two weeks, I work with Arun's team, Rui is there, to launch that application."

*On BayOne's Role:*
- "You are not building anything in AI stack because all the AI stack is given to you. Everything else is given to you."
- "All you have to do is build an [MCP], build a patch of prompts queries and stitch it here."
- "My expectation is within like two months, we should have an app running live here. Because all the infrastructure is already built for you."
- "I do not want [Colin] to spend time on say what infra will look like... We are already 90% there."

*On Technical Philosophy:*
- "You need to step back and say, how do I make this infrastructure generally so that we can leverage it in other places."
- "Always put two hats when you evaluate. One, will you solve my current need? Two, can it be extensible?"
- "Anything we do should be future proof and ready to enable the agentic infrastructure."
- "So anytime I myself deviate, you have to correct me."
- "I go very fast, very, very fast. People know me who are working with me."

*On Working Relationship:*
- "Once you start working, it's engineer-to-engineer conversation. You'll find a good partner."
- "Once you are onboarding, you are my friend. So I'll treat you the way or treat me the same way as a colleague."
- "You can always correct me saying that you are wrong. I don't mind in the private or for me it doesn't matter."
- "You should always say, can we have a recorded session."

*On Onboarding Pain:*
- "Any time any new engineer joins... we are spending a lot of time to get the ADS or the provision to those engineers. And it is done by Cisco but it is taking time from us."

**Owns:**
- DeepSight platform and AI strategy
- DeepSight presentation recording share
- Rui handoff coordination (CI/CD app)
- Technical direction and extensibility requirements
- Agentic infrastructure vision
- Monitoring WebEx space and expediting blockers

**Follow-up with Srinivas:**
- Watch DeepSight presentation (1-1.5 hours)
- Coordinate Rui handoff after CI/CD app launches
- Pull into other meetings once app is running

---

## Colin Moore (Director of AI, BayOne)

**Key Statements:**

*On MCP/Integration Vision:*
- "I'm hoping we'll have some kind of MCP on top of [Jenkins] to be able to talk to GitHub to get data like how many comments are going through, how many branches are there, what is having issues."

*On Existing Platform:*
- "We have a similar platform, so that's a really cool thing. Yours is much nicer, I have to say, for the UI, but it's similar approach to it."

*On Organization:*
- "I keep things very organized. Even from an AI perspective, we have to, I would say, practice like we play."

*On Quality Philosophy (shared with Srinivas):*
- "My first boss... told me the Golden Rule... Where I feel good is whenever I can walk away from things and I don't have to hear about them or touch them in 10 years. That's great for me. That means I did something right."

*On Client Engagement:*
- "Sometimes in solutions... there's two types of client. Type one wants you to do something exactly as prescribed, and against all of your instincts, you have to do it. Refreshing that's not [the case here]."

**Committed To:**
- NDA signed by end of day Feb 17
- GitHub Enterprise training (3-4 hours)
- Watch DeepSight presentation (1-1.5 hours)
- Ensure all 5 team members complete training
- Always request recorded sessions going forward
- Keep everything organized from project perspective

---

## New Contact Mentioned: Rui

**Not Present** - mentioned by Srinivas

**Context:**
- Works on Arun's team
- Building existing CI/CD app for DeepSight
- App launching in 2-3 weeks
- BayOne will pick up from Rui's work and extend it

**Follow-up:**
- Srinivas will add Rui request to WebEx group
- Coordinate handoff after app launches

---

## Transcription Corrections

| Transcript Says | Actually Means |
|-----------------|----------------|
| "the worker" | Divakar |
| "basil" / "bezel" | Bazel (Google build system) |
| "total less" | Atlas (DeepSight Atlas) |
| "Java" / "Gerard" / "C" | Zahra |
| "LCP" | Likely MCP (Model Context Protocol) or internal term |
| "CAC retooling" | CAT (Commit Approval Tool) |
| "Degas platform" | DevX Platform |
