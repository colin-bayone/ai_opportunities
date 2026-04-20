# 02 - Meeting: Visual QA Project Scope and Four Consumer Groups

**Source:** /sephora/qa_qe_playwright/source/vaibhav_colin_sync_4-9-2026.txt
**Source Date:** 2026-04-09 (Follow-up sync, project scoping conversation)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on visual QA project scope and the four consumer groups

---

## How the Topic Was Introduced

Vaibhav opened the meeting by framing the ask as an acceleration of items already on Sephora's QE roadmap: "There are a few things that I was discussing with Deepika and some of the things that we wanted to venture into. It's in the road map, in our road map, but we just want to accelerate a few things." [00:02:09]. This is not a net-new idea. It is an existing roadmap item that Vaibhav wants to pull forward, and BayOne is being brought in specifically to accelerate it.

He named the gap directly: "One of the biggest gap that we currently have is from visual testing perspective, right from our site." [00:02:47]. He then listed the specific domains that fall under visual testing: "Various sort of localization, UI/UX issues, content validations, some just exploratory testing." [00:02:47-00:03:04]. These four sub-domains are important because they recur as the specific needs of the four consumer groups he defines moments later.

## The Two Environments

Before naming the consumer groups, Vaibhav established the environmental scope. The tool must operate in two distinct environments:

1. **Nonprod/preview environment** -- "where most of the AB testing is conducted" [00:03:04]. This is the primary validation environment. The mention of AB testing is significant: it means the visual testing tool will encounter variant pages, not just canonical layouts. The tool must handle the reality that any given page may be displaying one of multiple AB test variants at any time.

2. **Production environment** -- the purpose here is different. Vaibhav framed it as "run them loose in a production environment and try to isolate any anomalies on the site" [00:03:04-00:03:24]. "Run them loose" is a notable phrase. It implies autonomous, broad-scope scanning rather than targeted test execution. The production use case is anomaly detection, not pre-release validation.

This dual-environment requirement is foundational. Every consumer group's requirements must be fulfilled in both environments, though the purpose differs: nonprod is for validation before release, production is for anomaly isolation after release.

## The Four Consumer Groups

Vaibhav introduced the consumer framework at [00:07:58]: "Currently I see there are four main consumers of this tool, right?" He then defined each in sequence.

### Consumer Group 1: QE Team

**Vaibhav's words:** "One is absolutely from QE perspective, we are testing various aspects of VQA." [00:07:58-00:08:04]

**Decomposition:**
- This is Vaibhav's own organization. The QE team is the most natural consumer of a visual QA tool.
- "Various aspects of VQA" is deliberately broad. Vaibhav did not narrow it down for the QE team's use case. This suggests the QE team is the catch-all consumer: localization testing, UI/UX validation, content checks, exploratory testing -- all four of the gap areas he named in the opening.
- The QE team's requirements were not detailed beyond this because the QE use case is essentially the full scope of the tool. The other three consumer groups each have a narrower slice with specific additional needs layered on top.

**What is NOT said:** Vaibhav did not describe what the QE team's current manual process looks like for visual testing, nor did he specify which aspects of visual QA are highest priority for QE. This is an open question for the requirements deep dive.

### Consumer Group 2: Development Teams

**Vaibhav's words:** "Second is to give our development teams during development referring to the UX or Figma designs and all they ensure that the development is on track." [00:08:04-00:08:19]

**Decomposition:**
- This is a shift-left use case. The development teams are not doing post-build testing; they are checking their in-progress work against design specifications during development.
- The reference to "UX or Figma designs" means the tool needs to compare rendered UI against Figma source files or design assets. This is a specific technical requirement: Figma integration or at minimum the ability to accept Figma exports as baseline references.
- "Ensure that the development is on track" frames this as a development aid, not a quality gate. Developers would use this to self-check before submitting for formal QE review.
- The development team is consuming the tool in a fundamentally different workflow stage than the QE team. QE tests after build; development teams test during build.

**Implication for tool design:** The tool needs to be usable by developers in their workflow, not just by QE in a testing pipeline. This likely means a different interface or integration point -- possibly IDE integration, CI/CD pipeline hooks, or a lightweight self-service mode that does not require QE tooling expertise.

**Connection to Colin's description:** Colin's mention of BayOne's internal practice included an MCP server that "connects to Figma" [00:10:45-00:10:49]. This directly addresses the development team's need. Colin did not explicitly draw the connection in the meeting, but the alignment is there. The Figma MCP server from BayOne's internal tooling maps to this consumer group's core requirement.

### Consumer Group 3: UI/UX Team

**Vaibhav's words:** "Third consumer is from a UI/UX team perspective because they partner very heavily with our business team, so they should have the ability of some sort of configuring this tool to be able to define some pixel level differential thresholds or certain baseline components or even some sort of an approval routing where you define, yeah, this is the threshold if it's beyond this... what do we do, right? What needs to be done?" [00:08:19-00:08:51]

**Decomposition:**
- This is the most technically specific consumer group description Vaibhav gave. Three distinct capabilities were named:

  **a) Pixel-level differential thresholds.** The UI/UX team needs to configure how sensitive the visual comparison is. A threshold defines how many pixels (or what percentage of pixel difference) is acceptable before flagging a discrepancy. This is configurable per team, not global. The UI/UX team has different tolerance levels than, say, the QE team doing exploratory testing.

  **b) Baseline components.** The UI/UX team needs to define and maintain baseline visual states for components. This implies a component-level comparison model, not just full-page screenshots. The tool must be able to isolate individual UI components (buttons, headers, product cards, navigation elements) and compare them independently against their defined baselines.

  **c) Approval routing.** When a threshold is exceeded, the tool must route the discrepancy to someone for a decision. Vaibhav's phrasing -- "this is the threshold if it's beyond this, what do we do, right? What needs to be done?" -- indicates a workflow requirement, not just alerting. There must be an approval or disposition flow: someone reviews the discrepancy and decides whether it is acceptable, requires a fix, or updates the baseline.

- The business partnership dynamic matters. Vaibhav said the UI/UX team "partners very heavily with our business team." This means the UI/UX team is not just enforcing design standards -- they are accountable to business stakeholders for visual quality. The tool becomes evidence in that business partnership. If the business team says "this doesn't look right," the UI/UX team needs the tool to either confirm or disprove that at a pixel level.

- The configurability requirement is distinctive. Of all four consumer groups, only the UI/UX team was described as needing to configure the tool's behavior (thresholds, baselines, routing). The other groups consume the tool's output; the UI/UX team needs to govern its parameters.

**Open questions:**
- Who are the approvers in the routing workflow? UI/UX leads? Business stakeholders? Both?
- Are baselines maintained per component, per page, per brand/sub-brand, or some other granularity?
- What happens when a baseline needs to be updated (e.g., after a deliberate redesign)? Who has authority to update baselines?
- Are thresholds global to the UI/UX team or per-component/per-page?

### Consumer Group 4: Producers / Digital Content Team

**Vaibhav's words:** "And then 4th is our producers, which is purely our content or a digital production team which create content, various kind of contents, whether it's just new items with different attributes or static content or images or whatever they will be immensely happy with such a tool that can validate their content publishing process, right? Because currently it's all manual and it's done in staging environment and pushed to production and there is a very minimal validation in production after it's left staging." [00:08:51-00:09:26]

**Decomposition:**
- This is the only consumer group where Vaibhav described the current process in detail: it is entirely manual, performed in staging, and has "very minimal validation in production after it's left staging."
- The content types are enumerated: "new items with different attributes or static content or images." This covers:
  - **New product items:** Products being added to the catalog, each with attributes (price, description, color swatches, size options, etc.). Visual validation would confirm these render correctly.
  - **Static content:** Non-product content such as banners, editorial pages, landing pages, promotional content blocks. These are typically authored in a CMS and published to staging.
  - **Images:** Product photography, lifestyle images, marketing assets. These need to render correctly (right dimensions, no broken links, correct placement on page).

- The producers' workflow is publish-then-validate: content is created, pushed to staging, manually checked in staging, then promoted to production. The pain point Vaibhav identified is that after it hits production, there is almost no validation. This means content errors that slip through manual staging review go live undetected.

- "They will be immensely happy with such a tool" -- Vaibhav's word choice signals that the producers are a high-impact adoption group. The current manual process is clearly painful enough that even a basic visual validation tool would be a significant improvement. This consumer group may offer the fastest time-to-value for a proposal.

- The validation for producers is fundamentally different from the other three groups. QE tests functionality and visual correctness. Development teams compare against Figma designs. UI/UX teams enforce pixel-level standards. Producers need to confirm that the content they published actually appears correctly on the site -- that items show the right images, static content renders in the right place, and nothing is broken or missing.

**Open questions:**
- What CMS or content management platform do producers use to publish content?
- How many content items are published per day/week/sprint? What is the volume that manual validation currently handles?
- Is there any automated validation at all today, even basic link checking or image dimension verification?
- Do producers have access to nonprod/preview, or do they only see staging and production?
- When a content error is found in production, what is the remediation process? Rollback? Hotfix?

## The "Similar but Different" Framing

After defining all four groups, Vaibhav stated: "These are main 4 consumers of this tool and obviously all four functions will have similar but different requirements of it." [00:09:31-00:10:06]

This is a critical architectural statement. Vaibhav is explicitly saying:
1. There is one tool, not four.
2. All four groups use the same underlying capability.
3. The differentiation is in requirements, not in the fundamental technology.

Colin immediately reinforced this: "For me, the first thing that I'll say even without thinking about it is one kind of unified back end approach to all four cases. It'll eliminate a lot of the work. You'll have reusable modular components even beyond those four areas. If you want to do something even beyond that in the future, you'll have something extensible for yourself." [00:10:09-00:10:45]

He then offered social proof: "The same tool we built internally for our QE team is the same one our marketing team uses for new content generation." [00:10:45]. This directly maps to the QE/Producers split -- Colin's own organization already has two consumer groups (QE and marketing) using one unified tool.

## Vaibhav's Intent to Detail Requirements

Vaibhav said: "I'll be happy to kind of sit with you and detail out all the requirements." [00:09:31-00:10:06]. This was a commitment to a future requirements session, not a signal that the meeting was a requirements session itself. The meeting established the framework (four consumer groups, dual environments, similar-but-different needs); the detailed requirements for each group remain to be captured.

He then added the timeline pressure: "But now I'm hoping to do it by middle of this year, right? So that's what's triggering this urgency." [00:10:06-00:10:09]. "Middle of this year" means mid-2026, giving roughly 2-3 months from this April 2026 meeting to deliver a working solution.

## Cross-Device/Browser Testing via BrowserStack

Vaibhav added one more technical dimension after the four-group discussion: "And other element is of course the ability for us to run this test across multiple combination of devices and browsers etcetera. So we are hoping to get BrowserStack enterprise license so that would give us the ability to run them across these combinations... that would be something that'll be hopefully very soon available to us." [00:11:01-00:11:19]

**Decomposition:**
- BrowserStack enterprise license is not yet in place but is expected "very soon." This is a Sephora procurement action running in parallel.
- The requirement is explicit: the visual testing tool must support cross-device and cross-browser testing. BrowserStack is the intended infrastructure for that capability.
- "Enterprise license" specifically -- not just BrowserStack. This means broad organizational access, not a team-specific subscription. The scale implies this is meant to be used widely, consistent with the four-consumer-group model.
- The proposal should assume BrowserStack will be available and design the solution to integrate with it, but should not depend on it being in place on day one.

**Open questions:**
- Which browsers and devices are priority for Sephora? (Chrome, Safari, Firefox? iOS, Android? Specific device models?)
- Does BrowserStack integration mean Playwright running on BrowserStack's grid, or is there a separate BrowserStack-native testing layer?
- Is cross-device/browser testing equally important for all four consumer groups, or is it primarily a QE and UI/UX concern?

## Colin's Internal Practice as Proof of Concept

Colin described BayOne's internal visual QA tooling as validation that this approach works [00:04:46-00:07:44]. Key details from his description that map to the four consumer groups:

- **LangGraph-based orchestration** with custom agents and custom tools, plus MCP servers. This is the unified backend he later advocates for.
- **Playwright as the primary automation agent** -- aligned with Sephora's existing Playwright investment.
- **Multiple agent flows from a single platform:** exploratory flow ("pretend you're a brand new user, go to this application, click around, see what you can find, note down any bugs"), which maps to the QE team's exploratory testing need. Structured regression flows for deterministic testing. The same platform supports both.
- **QA artifact generation:** screenshots, progression tracking, detailed logging of every action including the GitHub SHA tag for traceability. This addresses the producers' validation need (proving content published correctly) and the UI/UX team's evidence need (pixel-level comparison artifacts).
- **Review agent:** a secondary agent that reviews the primary agent's output before surfacing it to a human. "There's still even a review agent that has to pass it first to make sure it's worth the human being's time to review." [00:07:44]. This is relevant to the UI/UX team's approval routing requirement -- the review layer could be the first stage of routing.
- **Desktop and mobile view support** already built in: "that works for both desktop and mobile view" [00:05:21]. This pre-positions the BrowserStack cross-device requirement.
- **Non-destructive guardrails:** agents are restricted to non-destructive actions unless explicitly in a sandbox environment. This matters for production anomaly detection, where the tool must observe but never modify.
- **Figma MCP server** mentioned: "In the MCP I was talking about earlier, that connects to Figma." [00:10:45]. This directly serves Consumer Group 2 (Development teams referencing Figma designs).

## The Build vs. Buy Context

Vaibhav stated: "There is a choice right now between build versus buy. I'm inclining towards building it ourselves so we can personalize the solution, but then it all depends on how things progress." [00:21:04]. This is relevant to the visual QA scope because:
- A bought solution would come with its own consumer group model that may not match Sephora's four-group structure.
- Building allows the tool to be designed around the four consumer groups from the start.
- Vaibhav's preference for build reinforces that the proposal should emphasize customization and configurability for each consumer group, not a one-size-fits-all product.

He also mentioned the in-house portal: "We are building an in-house Open WebUI equivalent portal... so once we have the solution, once we have the boilerplate solution in place, it won't be too difficult to port it over to what we have." [00:18:17-00:18:25]. This indicates the visual QA tool's interface layer may eventually live within Sephora's own portal, which changes the UI/UX requirements for the tool itself -- it may not need a polished standalone frontend if it will be embedded in Sephora's portal.

## Gap Analysis: What Vaibhav Named vs. What Was Detailed

| Gap Area (from opening) | Consumer Group Mapping | Detail Level in Meeting |
|--------------------------|----------------------|------------------------|
| Localization | Not explicitly assigned to any group | No detail given. Localization testing was listed as a gap but no consumer group was named as its owner. Open question: does this fall to QE, UI/UX, or producers? |
| UI/UX issues | Consumer Group 3 (UI/UX team) | Most detailed. Pixel thresholds, baselines, approval routing. |
| Content validations | Consumer Group 4 (Producers/Digital Content) | Moderate detail. Content types enumerated, current manual process described. |
| Exploratory testing | Consumer Group 1 (QE team) | Minimal detail from Vaibhav. Colin filled in with his description of exploratory agent flows. |

## Summary of Open Questions for Requirements Deep Dive

1. What specific visual QA tasks does each consumer group perform manually today?
2. What are the priority browsers and devices for cross-device/browser testing?
3. Who are the approvers in the UI/UX team's approval routing workflow?
4. At what granularity are visual baselines maintained (component, page, brand)?
5. What is the content publishing volume that producers currently validate manually?
6. Where does localization testing ownership sit across the four consumer groups?
7. How does the nonprod/preview environment handle AB test variants, and how should the visual testing tool account for them?
8. What is the integration path with Sephora's in-house Open WebUI equivalent portal?
9. What existing tools or processes (if any) does each consumer group currently use for any form of visual validation?
10. What does the CMS/content management pipeline look like for the producers' publishing workflow?

---

*This is a blockchain-style document. It will not be edited after creation.*
