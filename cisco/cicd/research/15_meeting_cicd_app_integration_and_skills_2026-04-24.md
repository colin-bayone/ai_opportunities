# 15 - Meeting: CI/CD App Integration, Skills, and Regression Protection

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt
**Source Date:** 2026-04-24 (Friday afternoon Srinivas sync)
**Document Set:** 15 (Sixth Srinivas team meeting)
**Pass:** Focused deep dive on CI/CD app deployment timing, skills repository structure, MCP viewer, and the new regression-protection workstream

---

## Overview

The Friday afternoon Srinivas sync on 2026-04-24 resolved several of the open structural questions that Main Set 14 had directed BayOne to close. Three threads moved from open to decided in this meeting. First, Srinivas confirmed that the CI/CD application itself will be deployed for BayOne by the team Anupma is currently working with on the back end, removing the need for BayOne to stand up Jenkins pipelines or wrestle with staging and production controllers. Second, the question Team Set 14 had surfaced about whether the four skills currently sitting on the webex-skills branch could be merged into the main CI/CD repository was answered in favor of merging, with a longer-term plan to consume those skills through a wrapper called the DeepSight agent init pattern rather than through Codex marketplace auto-discovery. Third, Srinivas added a brand-new workstream to the engagement, asking BayOne to begin planning regression protection for both UI and backend, with explicit guidance that the resulting framework be modular and built on an adapter model so that it can be reused across other Cisco applications.

A fourth thread tied the others together. Srinivas previewed the MCP viewer application that Anupma had announced two weeks earlier in Main Set 13. He confirmed it is being launched on the DeepSight platform as a playground for testing any external MCP before integration. For the CAT MCP work specifically, the viewer becomes a place to validate behavior before BayOne wires it into the application backend.

This document captures each of those threads in turn and identifies the implications for next week.

---

## Cisco CI/CD App Deployment

The most immediately useful piece of news in the meeting was that BayOne does not have to build the CI/CD application infrastructure from scratch. Srinivas had been working with the Cisco team that maintains the existing CI/CD application, and they have agreed to deploy a copy of the application for BayOne with Anupma working on the back end. Srinivas described it this way. "This dashboard, so it will be part of the CACD app. I had a chat with the current team who's maintaining. They're going to deploy, they're working with Alpoma back end so that what is happening is we will deploy the app for you."

The intent of this arrangement is to remove operational overhead from BayOne so the team can stay focused on business logic. Srinivas continued, "That way you have an end-to-end Jenkins pipeline set and you don't have to get bogged on with other staging controller and production controller and the Jenkins pipeline. We are just setting it up that way you focus only on the actual business logic."

The timing target is Monday. Srinivas said, "Okay, so that will be live maybe by Monday and then then you can be off. Okay, you can be you can run after that." This is consistent with the broader posture Srinivas has held since the engagement began. Cisco supplies the platform, the pipelines, and the controllers. BayOne is responsible for the AI capabilities that the platform consumes. The Friday sync removed any ambiguity about whether BayOne was expected to assemble the deployment pipeline itself. It is not. The deployment is being handled by the existing CI/CD application maintainers in coordination with Anupma, and BayOne should expect a working environment to plug into starting Monday.

Note that Srinivas's reference to "Alpoma" is a transcription artifact. He means Anupma, who has been the consistent back-end counterpart on the platform side.

The implication for next week is straightforward. BayOne is no longer waiting on Jenkins pipeline conversations. The team consumes a Cisco-maintained environment, contributes business logic into the CI/CD application, and lets the platform team run the deployment plumbing.

---

## Skills Inventory on the CI/CD Repository

Colin opened the skills thread by stating BayOne's current delivery position. "Just to say this part out loud, we do have a bunch of skills built that are currently on the CI2CD repository. I'll put that in the dock so it's clear as to what has been delivered so far." Colin then enumerated four skills present on the repository as of the meeting. "There's one for Apache E-charts, there's one for WebEx bot creation. There's one for the NXOS issue categorization, and then one more that's escaping it right now. But those are now currently on the repository."

Three of the four are clearly identified. The Apache eCharts skill provides charting capabilities for visualizations across the application. The WebEx bot creation skill packages the bot construction logic that Team Set 14 had been working through. The NXOS issue categorization skill is the categorizer that Anand and the team have been refining since the early build phase. The fourth skill was not named in the meeting, and Colin committed to documenting the full inventory so that Srinivas and the Cisco team have a clear view of what BayOne has delivered. Based on the recent work, the fourth skill is likely either the build log architecture skill discussed in Main Set 12 or the skill-forge that BayOne has been using as the meta-skill for skill creation.

The action item is for Colin to publish the skills inventory in the documentation that goes into the CI/CD repository. This is a low-cost deliverable that closes a Main Set 14 commitment and gives Cisco visibility into BayOne's delivery footprint.

---

## Branch Merge Question and Skills Location

Colin then surfaced the question Team Set 14 had identified. "I think there was a question about if we are allowed to merge that, or put PR into the merge that domain, or if we should leave it on a separate branch. We didn't know."

The branch merge question is not theoretical. The four skills BayOne has produced are on the webex-skills branch in the CI/CD repository. The Team Set 14 working session had not been able to resolve whether the team should open pull requests to merge those skills into the main branch or whether the skills should stay isolated on the working branch.

Srinivas's answer required some unpacking because the meeting also surfaced the existence of a second repository, SME-KB, which had not previously been explicit in BayOne's understanding. Colin asked for clarification. "There's two different locations that you gave. One was the, it started with a K, if I'm not mistaken here." Srinivas confirmed, "This would be, this is SME-KB repo." Colin continued, "The other one is just the generic," and Srinivas closed the loop with the operating directive. "This one, all the skills, right? Whatever you're committing. Technically, what we did is we have an XPR. We'll maybe next week or something, we may announce it, but yeah, you can, for now you can, we'll re, we rework on the skills part. So, but ideally we want all the skills to be part of this repo."

The plain reading is that the main CI/CD repository is the home for all skills BayOne is producing. SME-KB is a separate concern with a different scope. Srinivas referenced an upcoming announcement that may shift the structure, possibly the rollout of what he called an "MCP fault," which in context appears to mean an MCP vault or marketplace being built on top of the main repository. He confirmed, "We are creating an MCP fault of this repo itself. And that piece is not ready. So, but we can refactor the code later on. So, you guys have to do whatever you have."

The decision for next week is therefore to merge the skills off the webex-skills branch and into the main CI/CD repository, with the understanding that the team can refactor the layout later when the MCP vault structure is announced.

---

## Codex Auto-Discovery Versus DeepSight Agent Init

The conversation about how skills get distributed to end users was the most architecturally interesting exchange in the meeting. Colin opened with a distribution pattern BayOne uses internally. "All these skills can be auto-discovered in codecs. So it's just one connection that you make. It's just a config.json file. So anyone that's already authenticated is part of this. There can be a linkage between GitHub. So every time a new skill gets uploaded here, it automatically becomes available in anyone's VS Code instance that they subscribe to them. So that's a very easy way to distribute if you want to do it that way, but just wanted to offer it up."

Colin's reference to "codecs" is a transcription artifact for Codex, the assistant runtime that ships into VS Code. The pattern he was describing is the Codex marketplace. An admin sets up a config.json that points at the GitHub repository, and from that point forward every newly committed skill is discoverable by every user authenticated to that Codex instance.

Colin also flagged the prerequisite. "If you set up a config.json file, you have to be an admin in codecs to do this. And all that has is it has what's called as a marketplace, which is literally just the GitHub page. That's it. If you're not an admin? So if you're not an admin, you can't set this up. But it's only a one-time setup for the admin themselves."

Srinivas's answer was that Cisco does not have group admin rights and does not operate Codex at the group or system level. "None of us are, our IT guys are group. And this is not done at the group level, it's not done at the entire system level."

What Cisco has built instead is a wrapper that handles skill installation per user session. Srinivas described it. "So what we are trying to do is, once you do the products, we have a wrapper which doesn't init. And once you do the init, init will actually go and pull the skills from this and install as a part of the individual's thing." He elaborated, "The invention that's what the user will do they will do a deep site agent in it there's something called ds agent and when does the in it it will largely pull the skills and installs in there."

The plain reading, after correcting "deep site" to DeepSight and "ds agent" to DeepSight agent, is that Cisco has a DeepSight agent that exposes an init command. When a user runs the init, the agent reaches into the CI/CD repository, pulls the skills, and installs them into the user's local environment. This sidesteps the Codex admin requirement entirely. The wrapper itself is the distribution mechanism.

Colin acknowledged the design favorably. "That's even better. We are trying to do even better. You don't have information. Okay, no, no, no, that's just as good." The result is that BayOne does not need to push for Codex marketplace setup at Cisco. The DeepSight agent init pattern accomplishes the same goal through a Cisco-controlled mechanism, and the operational burden is handled at user session level rather than at organization admin level.

The implication for the engagement is that BayOne's job is to keep the skills clean, well-named, and committed to the main CI/CD repository. The DeepSight agent init handles the rest.

---

## Regression Protection as a New Workstream

Srinivas added a workstream to the engagement during this meeting. "We need to also start planning on the UDIT automation so that whatever work we are doing, we are not regressing." The transcription "UDIT" almost certainly means UI and backend automation, possibly a UI-DIT abbreviation Srinivas uses internally. The intent is unambiguous.

He explained the motivation. "We'll be adding more features, more fixes, and new changes should not happen at all on the previous whatever we are telling you about. So start thinking on how we can protect ourselves." The concern is that the CI/CD application is now accumulating BayOne contributions at a steady pace. Without regression coverage, the next change can break a previous capability and the team will not catch it until a user does.

Srinivas distinguished two kinds of infrastructure that need to be in place. "Skills is, I know it's straightforward, but when we start bringing the changes to the app itself, we need to have some kind of infrastructure and two kinds of infrastructure and thinking. One is the UI based automation like a playwright or anything like that. Another one is the backend validation of all the pipeline plus the business logic of the application itself."

Two halves. UI automation, almost certainly Playwright based, exercises the application from the browser layer. Backend validation tests the pipeline plus the business logic. Together they bracket the surface area of the application so that a new commit cannot silently regress an earlier capability.

Srinivas then stated the architectural constraint that has been a constant theme through the engagement. "So if you can think of how to abstract it, as I always say that this should be independent, reasonable pieces. So try to see if you can make it abstract and modular, so that if required we can pick it up on other apps." The regression framework is not a one-off for the CI/CD application. It is a reusable asset that other Cisco product teams should be able to adopt without rewriting the core.

Colin's response made a cross-engagement reference. "Yeah, for sure. And the good news is we already have a lot of that done. There's another project that's going on at Cisco. I believe it's under Guhan Raman's team that has exactly that that we're building, so we can use. It's literally the exact same use case." The reference is to the EPNM-to-EMS UI Modernization engagement BayOne is also delivering at Cisco. That engagement has produced a regression and validation framework that maps onto the same shape Srinivas is describing here.

Srinivas accepted the reuse without objection. "Sure, yeah. Just try to get that going as soon as possible, if you can." This is a meaningful posture from a Cisco platform leader. He is not protecting territorial boundaries between product teams. He is encouraging cross-engagement reuse as long as the resulting artifact meets the modularity bar.

---

## Modular and Adapter Pattern Reinforcement

Srinivas spent a substantial portion of the meeting reinforcing the modular and adapter pattern requirements that have been a constant since the engagement started. "And make it modular so that, as I said, your goal should be any, and in the CICD when you raise, make sure that you click the diatherers for every artifact that you create."

The transcription "diatherers" is deliverables. The directive is that each deliverable BayOne produces, whether a skill, a regression component, or a backend validator, must be a standalone unit. Srinivas continued, "And if I pick the diatherers, it has to be standalone, meaning I should be able to plug and play other places."

He then specified the pattern that allows reuse without forcing duplication. "Any customisation should be done separately, if there is any, like I can you to build as an adaptor model. For example, if I want to play right automation, the model itself should be self-sufficient of its own. But if any adaptation needed for that app, it should be able to do so that I can take this playwright UI automation and plug it in any other app. And we'll tell that the images so it's adaptation layer, it should work."

The pattern, in plain form, is the adapter pattern. The Playwright UI automation core is independent. Application-specific concerns live in an adapter layer that sits between the core and the target application. To onboard a new application, BayOne writes an adapter, not a new framework. Srinivas closed the exchange with a parallel for the backend half. "Same thing on the back end also. So that's a new item getting added."

Colin's response committed to the pattern without hedge. "We can absolutely do that. That's what we do already internal. We can do that for you." This aligns with the methodology BayOne has been demonstrating across the engagement and with the standards Srinivas has been holding the team to since the kickoff in February.

---

## MCP Viewer Application

Srinivas previewed the MCP viewer application that Anupma had originally announced in Main Set 13. "On the MCP part, by the way, we are going to launch something called MCP viewer app on the deep side. So that way you will have a better way of testing any external MCP on the deep side platform itself."

He described the function clearly. "So before you integrate into the app, so anybody who says they have this MCP, you can just bring onto the MCP viewer app and then test it out. It's like a playground. And once you know it's all working good, you just take that app and CP and put it in your application backup."

The "CP" in the closing phrase is a transcription artifact for MCP. The workflow is straightforward. Validate any MCP, internal or external, in the viewer first. Confirm that the responses are correct and the integration shape is what BayOne expects. Only then commit it into the application backend.

Srinivas tied the viewer specifically to the CAT MCP work. "This cat and CP, for example, if you're spending time within the code with the API call and whatnot, if there is a way for you to quickly test and see if it's looking good, or if you want to do more visualization, what's happening, you can use that app." This is a practical convenience for the CAT MCP integration, which has been a constant API-call-shaped puzzle for the team. Instead of testing CAT MCP behavior through application code paths, BayOne can drop the MCP into the viewer, exercise it directly, and confirm correctness before integrating.

The viewer is not yet generally available. Srinivas was previewing the launch, not announcing it as live. The expectation is that it will be online within the next short window, consistent with the two-day cadence Anupma had described in Main Set 13.

---

## Cross-References to Earlier Document Sets

This meeting closes loops that were opened in two prior document sets and adds a new workstream that will trace forward through the next several sets.

Team Set 14 surfaced the branch merge question. Main Set 14 directed BayOne to upload all skills to the CI/CD repository and committed Srinivas to share the repository structure. Main Set 15 resolves both threads. The main CI/CD repository is the home for all skills for the foreseeable future. SME-KB is a separate concern with different scope. The DeepSight agent init pattern handles distribution to end-user sessions, which removes the need for the Codex marketplace setup Colin had offered as a fallback.

Main Set 13 captured Anupma's original MCP viewer announcement. Main Set 15 confirms the viewer is on track and identifies the CAT MCP integration as a primary near-term consumer of it.

The regression-protection workstream is new in this meeting. It will trace forward into next week's planning. Colin's reference to the Guhan Raman team's parallel work means the framework draft can come from the EPNM-to-EMS UI Modernization engagement. The next set will likely capture the first cut of the modular UI plus backend regression framework adapted for the CI/CD application.

---

## Implications for Next Week

The meeting produced a clear set of expectations going into the week of 2026-04-27.

The Cisco-managed CI/CD application instance is targeted to be live for BayOne on Monday. The team consumes that environment rather than building deployment plumbing. Anupma is the platform-side counterpart for the back end.

All four skills currently on the webex-skills branch get merged into the main CI/CD repository. Colin publishes the skills inventory documentation so that Cisco has visibility into the delivered footprint. The fourth skill that Colin could not name in the meeting gets identified and added to the inventory before the documentation goes in.

Distribution to end users runs through the DeepSight agent init pattern. BayOne does not need to set up Codex marketplace integration. The skills repository structure is the contract.

The MCP viewer application is the validation surface for the CAT MCP integration as soon as the viewer goes live. BayOne should plan to test CAT MCP behavior in the viewer rather than through application code paths during development.

The regression-protection workstream begins immediately. Colin pulls the modular Playwright plus backend validation framework from the EPNM-to-EMS UI Modernization engagement and adapts it for the CI/CD application. The framework follows the adapter pattern so that the core is reusable across Cisco applications and the application-specific concerns live in adapter layers. Srinivas wants this in flight as soon as possible.

Srinivas requested a one-slide weekly summary that the team can review on Mondays. Colin committed to producing the first version that day, with the artifact living in the CI/CD repository as a markdown file with mermaid diagrams as needed, tracked through GitHub issues for visibility.
