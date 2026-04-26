# 13 - Meeting: Bot Creation and MCP Ecosystem

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-20/srinivas_4-20-2026_formatted.txt
**Source Date:** 2026-04-20 (Monday afternoon Srinivas sync, first of 3x weekly cadence)
**Document Set:** 13 (Fourth Srinivas team meeting)
**Pass:** Focused deep dive on bot creation request and the Cisco MCP ecosystem

---

## Overview

The April 20 Srinivas sync produced two threads that reshape the BayOne scope and the surrounding Cisco tooling picture. The first is a concrete task assignment to create a WebEx bot helper for the NX-OS CI team, paired with Colin's pitch to wrap that delivery inside a Singularity skill that functions as a repeatable bot factory. The second is the surfacing of an expanding Cisco MCP ecosystem, including a directive to generate a Bazel MCP, a reference to an existing Wit MCP from the on-premander [unclear in transcript] team, Anupma's disclosure that the CAT MCP is on the IDE marketplace, and an announcement that an MCP viewer app will ship on DeepSight within two days. Together these threads move BayOne from a single-MCP participant (the build-failure analysis endpoint from Set 12) into a multi-MCP ecosystem where at least four MCPs intersect with the engagement. The conversation reinforces Srinivas's standing modularity directive and positions Colin's Singularity skills as a complement to Codex and MCP rather than a replacement for either.

---

## Srinivas's NX-OS CI Bot Request

Srinivas surfaced the bot request as an exploration item: "is there a way for us to can you guys explore how to create a WebEx bot helper itself that way we will add a NxCI bot help" (transcription: "NxCI" resolves to NX-OS CI). The scope is a curated question-and-answer experience: "it is a curated Q&A that way if the user is asking the same question he get an answer immediately." The driving business value is reducing first-response time on recurring questions, which ties directly to the pain-point analysis bot vision discussed in Main Set 12, where Colin and Srinivas agreed that common NX-OS CI questions repeat frequently enough that a curated answer layer would materially offload the release leads and senior engineers.

Although Srinivas used the word "explore," the follow-up exchange treats the work as a concrete task assignment, not a design study. Colin does not push back on scope, and Srinivas by the end of the conversation is already asking that the bot be created as part of a reusable skill. BayOne will produce both the bot itself and the documentation and tooling around it. The bot also inherits the deployment governance raised in Set 07 and Set 08 around Saurav's Wall-E WebEx bot and the Cisco IT compliance review: Cisco-owned repository, Cisco identifiers, sanctioned CICD pipeline. That constraint is not restated on April 20 but it is binding.

---

## Colin's Commitment to Document the Bot-Creation Process

Colin accepted the task and extended it. His commitment was twofold: "what we will do is we will both make that bot, but we will also document how to make that bot." That framing converts a one-off delivery into a reusable knowledge artifact and is consistent with Srinivas's repeated modularity directive. By committing to document the bot-creation process, Colin prepared the ground for the Singularity pitch that follows immediately after.

The documentation commitment also creates an internal obligation for BayOne. The team needs to treat the bot build not as a throwaway engineering exercise but as a case study that can be packaged into the Singularity skill. Anything hard-coded to the NX-OS CI environment will need to be abstracted or parameterized in the skill that ships later.

---

## The Singularity Skill Pitch: A Factory to Generate Bots

Colin then pitched the Singularity skill pattern directly. His framing positioned skills as a complement to the Codex and MCP tooling that the Cisco team already uses. The full pitch: "so there is Codex, but you can also create skills. So even if someone in the future was trying to make a WebEx bot, we can actually make a kind of a repeatable. This takes usually about 45 minutes for us." He followed with the factory metaphor: "a repeatable workflow. So if you ever want to make a bot in the future, it is almost like a factory to do that and generate that."

This is a significant moment. It is the first time Colin has introduced the Singularity skill pattern to Srinivas as a named capability and the first time he has offered it as a factory for bot creation rather than as an internal BayOne productivity tool. The forty-five minute figure gives Srinivas a concrete anchor for the pattern's value. Srinivas's response was unambiguous acceptance: "Yeah, I mean, I am interested in that. Yeah, create a skill which can create a new bot, right, as required." BayOne can now build a meta-deliverable, a skill that creates bots, and Cisco will treat it as a valid output of the engagement. The team can reinvest engineering time into the skill rather than building each bot from scratch, and the skill becomes a repeatable asset BayOne can reference in other engagements.

---

## Skills Positioned as a Complement to Codex and MCP

Colin reinforced the positioning: "Skills are super useful. I think they are a great complement to what you already have for MCP. And already the Codex workflow as well gives a little bit more control. We will make those as we go." Skills are additive, not substitutive. They sit alongside Codex (Cisco's internal coding assistant stack) and MCP (the endpoint-based tool exposure pattern that Set 12 operationalized).

The phrase "we will make those as we go" sets delivery cadence. Skills are not scoped as a separate deliverable stream with their own milestones and pricing. They will be produced organically as the engagement uncovers repeatable workflows. This avoids overselling the skill pattern as a product while preserving BayOne's ability to ship them opportunistically.

---

## Srinivas Reinforces the Modular and Pluggable Principle

Srinivas closed the bot and skill thread with a reinforcement of the modularity directive that has been a through-line since the earliest meetings: "Please remember that anything you guys are doing should be modular and pluggable to other workflows. So as much as possible, unless there is a very specific requirement. It should be plug and play kind of equivalent. And you are thinking in the right direction."

This is a cross-cutting constraint. It applies to the NX-OS CI bot, the Singularity skill that creates bots, the build-failure analysis MCP endpoint from Set 12, any MCPs BayOne contributes to the Bazel or CAT ecosystems, and every utility or service layer the team produces. Every deliverable must pass a modularity check before handoff. The service categorizer, the knowledge graph or dependency graph work, the point-fix agent, and the bot factory all need to be reusable across projects with minimal rework.

---

## Point-Fix Agent Vision Revisited

Srinivas returned to the point-fix agent vision and connected it to the code review agent infrastructure: "there will be an agent that is running and that can assist the folks to basically if there is any minor change right very small thing user can just talk to the agent to rebuild that particular minor issue." Examples are small-scope fixes: "some if conditions have an issue or someone forgot some semicolon." The operating principle: "we will have an agent which can do a point fix."

The architectural reuse statement came next: "we are building one agent I told you right on the for a code review will the same thing will we will use the same infrastructure, we will use it here." The pattern is single-agent, multi-use. The same agent and infrastructure that powers the code review experience will also power the point-fix experience. The agent design has to generalize across use cases, and BayOne's contributions around point-fix handling need to fit the same runtime and agent contract that the code review use case is driving.

---

## Bazel MCP Directive

Srinivas asked directly whether a Bazel MCP was needed: "Do you think there is a need for us to generate a Bazel MCP or something for people to utilize it?" He answered his own question: "We need to do that." The scope is focused on commit-search and back-out workflows: "by the search of the commit, back out related things, other things, right."

The Bazel MCP is a build-side companion to the code review and point-fix agents. Where those agents produce or edit code, the Bazel MCP validates through a per-branch build without triggering a full nightly. Srinivas framed it as a necessity, not an optional add-on.

---

## The Wit MCP Reference

In the same exchange, Srinivas referenced an existing MCP in the adjacent Cisco landscape: "there is already a Wit MCP, right? The on-premander team, they have done, they have extended them." The phrase "on-premander" is a transcription artifact and most likely refers to an on-prem-focused team inside Cisco (possibly the on-prem wonder team or a similarly named sub-team) [unclear in transcript]. The Wit MCP is already existing, already extended by that team, and presumably available for reuse.

The Wit MCP is significant less for its specific purpose, which the transcript does not describe, and more for what it signals about the broader landscape. MCPs are being built by multiple teams inside Cisco without central coordination. The BayOne build-failure analysis endpoint, the Bazel MCP that Srinivas is now directing, the Wit MCP from the on-premander team, and the CAT MCP that Anupma has built are all independent efforts BayOne needs to be aware of and possibly integrate with.

---

## Bazel MCP Integration with the Code Review Flow

Srinivas walked through a specific scenario: "We need a Bazel MCP agenda actually as a part of the code review because when we are developing infrastructure where, let us say I give 10 comments to you, right? One of the comment, you did not like it, you have half liked it, let us say, right? And you want to augment the code change, let us say."

The integration pattern is a web portal interaction that cascades into an agent-driven code change and then a build validation. The user comments on a pull request. Some comments are accepted, some partially. The agent makes the targeted change: "the agent will go and only change that piece of if condition with whatever condition that you wanted." Then validation: "I need to be able to do a point build Right to at least behind the scene to say that whatever the code I am suggesting is proper." The point build is where the Bazel MCP is invoked to confirm the agent-generated change compiles.

---

## Bazel MCP Scope: Per-Branch Point Builds

The Bazel MCP is scoped narrowly. Srinivas described it as "going to be MCP for individual Branch point of view. We will we will as a part of the Bazel in it... We will provide what is a branch details and what not and then we will skip up the build only for that." The MCP takes branch details as input and performs a focused build for that branch only, not a full system build or nightly. That is the appropriate scope for validating a small agent-generated change before proposing it to the user. A per-branch Bazel MCP can be invoked from the code review flow, the point-fix flow, or any future workflow that needs a lightweight build validation.

---

## Bazel MCP Ownership Question

Ownership is still being negotiated. Srinivas initially framed it as a Cisco-internal build: "I do not know if Colin can help the team can help us." He then spelled out the sequence: "We can go ahead and check and then see if there is anything we can do it on ourselves and then we will provide that if it is possible. Otherwise, we will touch base with Colin on that."

Cisco's internal team will attempt the Bazel MCP first, and Colin's team is the fallback. This keeps the BayOne scope boundary clean. Colin's confirmed MCP work remains the build-failure analysis endpoint from Set 12. The Bazel MCP is adjacent, not overlapping, and BayOne should track it as a conditional scope expansion rather than a committed deliverable.

---

## Anupma's CAT MCP Disclosure

One of the more consequential moments came when Srinivas asked Anupma about the CAT MCP: "the cat MCP can you find the details to get a chance." Anupma's response was immediate and open: "yes, yeah it is on the marketplace IDE marketplace you should be able to get it from there." She followed with an integration detail: "It should be integrated to the deep site automatically, right? Because we have integrated the marketplace with the deep site."

This is a notable shift from Anupma's prior posture. Earlier in the engagement, access to the CAT database and CAT-related tooling was guarded and routed through formal requests. Her disclosure that the CAT MCP is on the DeepSight marketplace, available through IDE integration, and reachable without a bespoke onboarding process is a meaningful opening. The guardedness on raw database access apparently does not extend to the MCP-exposed surface, which has been sanctioned for marketplace distribution. BayOne should verify the exact scope and authentication context, but the default path forward is to consume the CAT MCP through the marketplace.

---

## MCP Viewer App on DeepSight

Anupma also announced that her team had built an MCP viewer app: "we have one MCP viewer app on the DeepSight. So probably in another this week we will publish it." She offered it to Colin as a playground: "Then Colin, you can actually go to the DeepSight platform, launch the MCP viewer and invoke the cat MCP on that and start playing. It is like a playground kind of a thing." She committed to a notification: "I will let you know once we release it in two days."

The MCP viewer app is a meaningful accelerator. Without it, Colin would need deeper DeepSight platform access to test MCPs, which has been a slow-moving entitlement process. With the viewer, Colin can invoke the CAT MCP, inspect responses, and experiment with composition patterns without waiting for full platform integration. It is effectively a sandboxed test harness for the Cisco MCP ecosystem. The two-day timeline, pointing to roughly April 22, is tight and credible given that the app is already built and only publication remains.

---

## Implications for BayOne's MCP Work

BayOne is now interacting with a minimum of four MCPs. The build-failure analysis MCP is the one BayOne is building under the Set 12 scope. The Bazel MCP is being built by Cisco's internal team with BayOne as fallback. The Wit MCP from the on-premander team already exists. The CAT MCP from Anupma is available on the DeepSight marketplace. The MCP viewer app is the composition and inspection surface that makes it practical to work across all of these without deep platform access.

This is a positive development. Earlier in the engagement the concern was that BayOne would be gated by DeepSight onboarding timelines. The combination of marketplace distribution for the CAT MCP and the imminent MCP viewer app routes around that bottleneck. BayOne can begin learning the Cisco MCP shape, testing interactions, and designing the build-failure analysis endpoint to compose with the other MCPs, all before full DeepSight access lands.

---

## Connections Back to Prior Sets

Set 08 introduced the functional-fix plus MCP endpoint pattern and the Wall-E WebEx bot work that Saurav owns. Set 09 was where Saurav's WebEx architecture diagram first showed MCP as a layer in the bot stack. Set 12 established the build-failure analysis MCP as a concrete BayOne deliverable and nailed down the endpoint contract between BayOne and Cisco's agent.

Set 13 is where the surrounding MCP ecosystem becomes visible. The Bazel MCP directive, Wit MCP reference, CAT MCP marketplace confirmation, and MCP viewer app announcement all arrive in a single meeting. The ecosystem is maturing faster than anticipated at the start of the engagement. The working posture: build the MCPs Cisco asks BayOne to build, integrate cleanly with the ones that already exist, and use the MCP viewer app to validate integrations early.

---

## Bot Deployment Path Reminder

The April 20 meeting does not restate the bot deployment governance, but the constraint carries forward from Set 07 and Set 08. The NX-OS CI bot must follow the same deployment path Saurav's Wall-E bot follows: Cisco identifiers, Cisco-owned repositories, sanctioned CICD pipeline, no private or out-of-band deployments. The earlier IT compliance episode around the incoming team member and the web scraping concern, discussed briefly at the top of the April 20 call, is a reminder that deviations get flagged quickly by the CyberSec team. The NX-OS CI bot needs to land inside the approved path from day one.

---

## Summary of Commitments and Open Items

BayOne has taken on the NX-OS CI WebEx bot as a concrete build with a Singularity skill wrapper that functions as a bot-creation factory. Colin has committed to both the bot and the documentation around how to build it, and the skill itself is now an accepted meta-deliverable. Skills are positioned as a complement to Codex and MCP and will be delivered opportunistically as the engagement surfaces repeatable workflows. The Bazel MCP is a Cisco-led effort with BayOne as the fallback. The Wit MCP exists in the adjacent landscape and does not require BayOne action. The CAT MCP is accessible through the DeepSight marketplace, and the MCP viewer app is expected within two days, providing Colin with a playground for testing Cisco MCPs before full DeepSight access lands. Srinivas's modular and pluggable directive applies to everything in this list, without exception. [unclear in transcript: the names "Nubomar" and "Bhagiram" appear near the end of the call and may refer to Anupma, Divakar, or another participant whose name the dictation tool mangled.]
