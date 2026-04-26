# 07a - Cross Reference: CI/CD-Relevant Excerpts From EPNM One-on-One

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/week_2026-04-14/day_2026-04-14/singularity-and-cisco-deepagents-and-ui-modernizat_01.txt
**Source Date:** 2026-04-14 (60-minute Colin-Saurav one-on-one, primarily about the separate EPNM-to-EMS UI Modernization engagement)
**Document Set:** 07a (supplementary to Set 07, the Apr 13 Monday team planning meeting)
**Pass:** Targeted extraction of CI/CD-relevant content only. The bulk of this meeting concerns the EPNM engagement and is intentionally not captured here.

---

## 1. Saurav staffed on both CI/CD and EPNM simultaneously

This matters because it changes the CI/CD team roster. Saurav is now a dual-project resource, and this was decided by Colin in this meeting, not at the Apr 13 team meeting.

Colin's rationale is that CI/CD does not currently fill Saurav's bandwidth. At 01:13:30 Colin said, "you can already tell the pace of work for CICD isn't quite there. You know, I told Neha and Zahra yesterday, I was like, there's no reason why we need four people right now. Like, honestly, like, there's a lot to do, but the pace at which it's able to get done." Saurav replied, "It's like hiring them for like sitting and waiting for access."

At 01:13:51 Colin confirmed the dual assignment: "even the people that are already on the project, I can, you're already onboarded onto Cisco. You already have, you know, accounts and hardware and all that. So I can pull you into this project, which makes that margin even better." At 01:36:36 Colin restated the conclusion: "with CICD, I can kind of put you on for both because I already know CICD is at the current pace is not going to take 100% of your bandwidth. Plus, you have all the access."

Saurav also asked the CI/CD-specific access question at 01:21:16: "so do we get like access to the what do you call their whole CICD pipeline?" Colin responded at 01:21:26, "Correct. Full, full open seasoning." Saurav immediately followed with, "So we can like keep on exploring for like CICD as well while working on this," and Colin agreed.

**Implication for CI/CD engagement:** Saurav has full pipeline access and is effectively a half-time resource available to the CI/CD engagement while working EPNM in parallel. This should be reflected in the CI/CD team roster and tracking; the prior assumption of four dedicated CI/CD team members is no longer complete.

---

## 2. Srikar and Namita protected as CI/CD-only

This matters because it establishes an explicit staffing rule for the CI/CD team that is invisible in any other artifact.

At 01:33:42 Colin said he plans to check in on Srikar and Namita, then at 01:33:54 stated the protection rule directly: "like Srikar and Namita, like Srinivas, like they sit next to him. So if they disappear to go work on EPNM, he's going to get ******." Saurav acknowledged. At 01:34:05 Colin confirmed he is willing to take the risk himself ("I'm okay") but not with Srikar and Namita.

The reasoning is physical co-location and client perception. Srikar and Namita are the visible BayOne presence sitting next to Srinivas Pitta. Pulling them onto EPNM would be noticed immediately and would damage the CI/CD engagement relationship.

**Implication for CI/CD engagement:** Srikar and Namita are the steady-state visible on-site presence and are off-limits to any cross-assignment. Any future bandwidth shortfalls on EPNM must be absorbed by Saurav, Colin, or other non-visible resources, not by reassigning Srikar or Namita.

---

## 3. CI/CD costing model critique: headcount versus deliverable pricing

This matters because it captures Colin's after-the-fact diagnosis of a structural problem in the CI/CD engagement that constrains every staffing decision downstream.

At 01:34:07 Colin vented, "I did not have anything to do with the costing or resourcing for the CIC project. That was entirely another person. That's very important to be one. That's all I will say. That throughout a random number without really much thought, and got a yes back when they weren't expecting a yes." At 01:34:39 he named the mechanism: "it's headcount based for CICD. I hate headcount based because people will nickel and dime you."

Colin contrasted with the buyer-side analogy at 01:34:49: "Tell me how much this is worth to you. Don't ask me when you buy a car how many people were involved in the creation of the car and what their hourly rates were. Tell me how much the car is worth." At 01:35:05 he tied this to consulting positioning: "do you think PWC is telling you how much a headcount resource is? You know, they don't do that... They're going off of deliverables and timelines."

At 01:35:43 Colin gave the blunt summary, "CICD, the person that did the costing at first was a dummy. I can't say who it is because they would fire me if I said, frankly, but you know, they made it headcount based because they were used to staffing." At 01:36:06 he named the concrete constraint this created: "Now I have to have two people in person in California. which is like the most costly." He noted at 01:36:17 that even with Srikar and Namita on site, "if it were me, I would say there's no reason why you actually have to be in person for more than one person here." He added at 01:36:28 that Justin Joseph himself works entirely virtual.

**Implication for CI/CD engagement:** The headcount-based pricing model locks in the two-person California on-site constraint and suppresses margin. The EPNM engagement is being deliberately priced outcome-based as a contrast. Any future CI/CD phase or follow-on should be repositioned to deliverable-based pricing before signing.

---

## 4. Cross-pollination: DeepSight architecture critique applies to CI/CD

This matters because Saurav's independent architectural review of Justin Joseph's DeepSight build produced a set of critiques that apply directly to the CI/CD engagement's scope.

Saurav walked Colin through what the Cisco CI/CD team actually built. At 00:16:07 he summarized: "they have the build logs. OK, they are using Regex to what you call get the error out of there. Then they have, I think, BCE it is called, which like create a graph of like dependencies and how exactly the error fails. That is included with what you call your Bazel." [BCE is almost certainly BEP, Bazel's Build Event Protocol; Saurav switches between "BEP" and "BEC" later.] He continued: "we are based on those, we are creating a workspace... they are creating a two separate file. One is for your BEC or BEP and another is like the extracted what do you call logs which are from the Bazel and they are placing that in a folder and passing that whole workspace to codex."

Saurav's central critique, at 00:17:46, is that the regex parsing layer should be replaced with a skill: "Here what they can do is just create a skill file and check out that skill file inside the what do you call workspace. They can like even what you call totally skip in the what do you call deterministic parsing of the Bazel logs which they are doing." At 00:18:26 he extended the point: "You can have a skill for that, for Bazel, for Gmail, for any other like log. It is much better and what you call more granular than like coding and then changing the architecture if something changes. It's like just update a skill file." He also noted a missing verification step at 00:19:25: "it is building that on its own and then testing like dopally as well in that workspace. It just does the fix and directly start the build process."

At 00:11:34 Saurav had already observed the broader gap: "on the repo I did not see any agent.md, no cloud files or no scales, no hooks, nothing. Everything is blank. Just code, not even documentation."

Colin agreed and extended with his own framing at 00:21:09: "regex is, yes, it's fast, yes, it's simple, but also remember that they are probably most likely using Codex to write those scripts... they pick the top N." At 00:21:48 he added, "unless you have every possible error, it is not possible to have a regex flow that is truly holistic." At 00:22:16 his conclusion: "it's inherently brittle. And the reason why I know what they built so far is probably even worse, and it's probably written by Codex, and it's probably the top N errors. Like you said, I think there's like 27 regex patterns matching."

On distribution, at 00:30:47 Saurav suggested a single git repo pattern for skills: "a single get repo which can be like, what do you call it, tracked and updated, correct? And if anyone wants to like, what do you call it, use those skills," they could be pulled from an enterprise skills location. At 00:31:52 he noted the pre and post hook gap: "you will be like always missing the pre and post hooks, correct? They can do a lot of work deterministically. Like those are totally game changers."

**Implication for CI/CD engagement:** The DeepSight critique is a ready-made BayOne recommendation for Justin Joseph's team, centered on four moves: replace hard-coded regex patterns with a Bazel log parsing skill, add AGENTS.md and pre/post hooks to the Codex workspace, add a build-verification step after each attempted fix, and distribute the skill set through a single tracked git repo rather than bundling logic into Python scripts. Colin's separate phrasing, that regex patterns belong in a database table rather than in Python code, complements the skill-file recommendation by suggesting the actual error catalog should be data-driven and refreshable on Bazel version change.

---

## 5. CI/CD tracking repo on BayOne GitHub still pending

This matters because Saurav explicitly reminded Colin that the CI/CD tracking repo was still not online, which ties directly to action items carried out of Set 07.

At 01:47:56 Saurav raised it: "one more thing I think, I don't know, maybe you have not created the repo yet, but yesterday or day before yesterday, I think we decided to like create the tracking repo for like CICD on BayOne and as well. And like, yeah, I think that is also currently not online."

Colin answered at 01:48:25: "Yes, I'll give both of those. I think Singularity you should have now. I'll send you the links to both of them though. I have both online. Yesterday I had to wait for Namita. She hadn't created her GitHub and I wanted to, I had made a GitHub team for all of you. But yeah, I'll send you the links to those repositories."

The sequence is: GitHub team has been created, repositories are technically up, Namita was the last blocker because she had not yet created a personal GitHub account, and as a result the invites to the team had not gone out at the time of this call.

**Implication for CI/CD engagement:** The CI/CD tracking repository and team membership are the unblocking step for any shared tracking or skill-development work. This connects to Set 07's action items #39 and #68. Once Namita completes her GitHub account setup and is added to the team, all CI/CD team members should be invited so that subsequent skill and documentation work can be version-controlled from a single source.

---

## 6. Org chart datum: Venkat Krishna as cross-portfolio VP

This matters because it is the first confirmation that the CI/CD engagement and the EPNM engagement share an executive sponsor above the engineering-management level.

At 01:00:44 Colin explained, "Skip up two levels in New York, and you get to the VP of a couple of different platforms, which include Nexus OS, like for CI/CD. They include this platform for EPNM and CNC. This person's name is Venkat. So, Venkat Krishna, he is like big boss at Cisco, like really big." At 01:01:24 he added an anecdote about seniority: "his Cisco username is venkat at cisco.com. So, think, think of how many Venkats are at Cisco. He's important enough that he got his is just venkat at cisco.com." [Some wording is blurred in the transcript; the substance is clear.]

Colin also placed the middle layer. At 00:58:56 he said, "this project is for someone named Guhan. Guhan is like Anand for, you know, the Cisco project for the CICD project." At 00:59:22: "Selva is like Srinivas level. There's a person named Selva." At 01:00:33: "all of these guys report up to Guhan. So, Guhan is like an Anand Singh from the CICD engagement."

At 01:10:07 Colin referenced Venkat again in the context of negotiating leverage on EPNM: "You guys try to explain to Venkat that you didn't get this done." The point is that Venkat owns both portfolios, and accountability for either engagement rolls up to him.

**Implication for CI/CD engagement:** Venkat Krishna is a shared executive sponsor across both Cisco engagements. This provides an organic escalation path and a cross-reference for client relationship mapping. Guhan on EPNM is the structural equivalent of Anand Singh on CI/CD, and Selva on EPNM is the structural equivalent of Srinivas Pitta on CI/CD. Any future stakeholder map for the CI/CD engagement should record Venkat at the top shared with EPNM.

---

## Files and sets referenced

- **Set 07 (parent of this supplementary):** Apr 13 Monday team planning meeting. Action items #39 and #68 connect to the tracking repo discussion in section 5.
- **Main Set 11:** Apr 10 Srinivas Pitta call. Context for the on-site presence constraint described in section 2 and the costing model constraints described in section 3.
- **Source transcript for this supplementary:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/week_2026-04-14/day_2026-04-14/singularity-and-cisco-deepagents-and-ui-modernizat_01.txt
- **Related cross-engagement context:** EPNM-to-EMS UI Modernization engagement (separate from CI/CD; see cisco/epnm_to_ems/ for the primary engagement tracking).
