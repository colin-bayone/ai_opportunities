# 07 - Meeting: Testing and QA Approach

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting)
**Pass:** Focused deep dive on testing and QA approach discussion

---

## Context for the Exchange

This testing and QA discussion emerged in the second half of the meeting, after Akhil and Rama had completed their walkthrough of the EPNM UI screens (network devices, device 360, device details, and fault management/alarms), and after Ramesh had raised and resolved questions about AI tool compliance (Claude Code, LangGraph, all on Cisco-issued hardware and accounts). Colin pivoted the conversation to QA by asking the Cisco team about their existing testing processes and how BayOne should prepare to make validation easier.

What makes this exchange significant is that it surfaced a fundamental tension: the Cisco team has a mature, decade-old test infrastructure with thousands of test cases, but the UI is changing, which means existing UI-based tests will not work against the new classic UI. The discussion evolved into two distinct scopes: what testing looks like during the POC versus what testing looks like during a full engagement.

---

## Colin Opens the QA Topic

Colin introduced the topic proactively, framing it as both a value-add and a practical concern. His statement (closely paraphrased):

"Part of what we can offer is also something that will save you some time, hopefully, which is a more agentic QA/QE service. That, again, we're just building custom for you. It's just part of what we can offer. That does not have to replace a traditional QA/QE step, especially because this will go production. That's just meant to catch problems, really. Save us some time, get us moving quicker."

Colin then asked the Cisco team directly: "What does that process look like today? For how QA/QE are happening before this gets deployed for production. So even for these new changes, what should we do on our side to make that easier on your end?"

This is a significant framing choice. Colin positioned the agentic QA as complementary to (not replacing) Cisco's existing quality process, and he explicitly acknowledged that production deployment means Cisco's own QA standards must be met. He was asking them to tell him what the bar is.

---

## Praveen's Response: The Existing Test Infrastructure

Praveen indicated he was going to ask the same question Colin raised ("I was going to ask that question -- your question, right?"), suggesting the Cisco team had this concern independently.

Praveen then provided the most detailed description of the existing test infrastructure heard across all meetings to date. His statement (closely paraphrased):

"The functionality -- this functionality product has been developed for over more than 10 years. So all features go through our test lifecycle of functional testing, scale testing, end-to-end testing, UI testing, API testing, migration testing, across releases, upgrade, scale. And we also have probably customer-specific profiles and so on and so forth. And we have automation in place too for some of the regression. So it goes to thousands and thousands of test cases, right, across different devices and functionality."

### What Praveen Described

The test lifecycle consists of at least seven distinct testing categories:

| Test Category | Description (inferred from context) |
|---|---|
| **Functional testing** | Verifying that individual features work as designed |
| **Scale testing** | Testing under load with large numbers of devices |
| **End-to-end testing** | Full workflow testing across feature boundaries |
| **UI testing** | Testing the user interface specifically |
| **API testing** | Testing backend API endpoints |
| **Migration testing** | Testing across product releases (EPNM version upgrades) |
| **Upgrade testing** | Testing that upgrade paths preserve functionality |

Additional elements mentioned:

- **Customer-specific profiles:** Test configurations that represent specific customer deployments. This is significant because it means testing is not just against generic configurations but against real-world deployment patterns.
- **Automation for regression:** Some portion of the regression test suite is already automated.
- **Thousands of test cases:** Praveen said "thousands and thousands" -- this is not a small test suite.
- **Cross-device coverage:** Tests span "different devices and functionality," meaning the test matrix includes device type as a variable.

### Praveen's Direct Question to Colin

Praveen then asked the central question (closely paraphrased):

"Now what's the best way now for us to confirm that what is developed is on par with that area of -- let's say network inventory, device details, device 360, alarms view, events view, and the specific fault area?"

He then offered two options and asked Colin to react:

**Option 1 -- Demo and manual validation:** "One is obviously the tech leads here, they would try to -- you would do a demo probably, you would execute some testing, right, and give a code guide. I don't know if you plan to use coverage tools or something -- not just the code coverage, functional coverage too."

**Option 2 -- Regression suite reuse:** "The second option could be to see, can any of the regression suites be invoked? I would think on those lines."

Praveen also asked a probing question about prior experience: "We want to hear from you too. How did you do in any other area if this was done earlier?"

This is Praveen performing due diligence. He was not just accepting Colin's claim of agentic QA capability; he was asking for specifics and precedent. He explicitly distinguished between code coverage and functional coverage, indicating sophistication in his testing expectations.

---

## Colin's Response: Playwright Agents and Dashboard Visibility

Colin responded to both of Praveen's options, strongly favoring the second (regression suite reuse) and then layering on the Playwright agent approach.

### On Regression Suite Integration

Colin's statement (closely paraphrased):

"I think from my perspective that is better because what we can do even earlier is -- because the worst thing is when you have testing, if you have a large test suite, is everything looks good. We test even manually and we make sure everything is great. But then you run the test suite and there's a bunch of holes. So we can do that in an automated way even during the conversion."

This is a practical argument: manual testing creates false confidence if it diverges from what the automated test suite expects. By integrating with the existing regression suite during development (not after), holes are caught incrementally rather than in a big-bang test run at the end.

### On Playwright Agents for UI Testing

Colin then described the Playwright agent capability (closely paraphrased):

"The other part is even from a user experience section. We typically will have some agents that use Playwright to actually do automated UI testing, even beyond just function coverage or code coverage type tests. That is a really nice capability we have as we go forward because that saves us a lot of time."

He elaborated on the value proposition by describing the failure mode it prevents:

"That saves us from saying, you know, AI said, look, all this is done. And then you go and actually try it as a human and you say, what? This doesn't look right at all. So we have a way to use Playwright with agents to even do the automated equivalent of what a human being would do for the testing."

This is a significant claim. Colin is describing Playwright agents that do not just run deterministic test scripts but perform the "automated equivalent of what a human being would do." This positions the Playwright agents as doing exploratory testing, not just regression testing -- clicking around, trying different options, evaluating visual output.

### On Leveraging Test Suite Awareness Early

Colin continued (closely paraphrased):

"So the more awareness we have of the test suites, the better we can automate that and the less work there will be at the end. Especially because I know -- I think what, there's a release coming up and what we'll also get out of this POC is kind of the timing and the cadence that we can do this at."

This ties the testing approach to the business timeline. Colin referenced a release target (later identified as July or August, per Venkat's prior statements) and positioned test suite awareness as critical to de-risking that timeline.

### On Prior Experience

Praveen had asked "Has a similar exercise been done on any product for any other thing?" Colin responded:

"Yes, so that is exactly what we're doing with Srinivas right now and that's also every single project internal to BayOne that we do. That is my mandate that we do that for every single project. I actually don't have a traditional QA/QE team. Because this works so well. It's still -- we have QA/QE experts that are manning the agents and recognizing things. But at the same time every single project we do happens this way for testing."

This is a strong statement: Colin is claiming that BayOne's entire internal QA practice runs on the agentic model, not on traditional QA/QE teams. The humans are supervisors of agents, not direct testers. He cited the concurrent Srinivas/NX-OS CI/CD project as a live example of this same approach at Cisco.

---

## Praveen's Follow-Up: Visibility and Validation

Praveen pressed further on what the Cisco team would actually see (closely paraphrased):

"I'm trying to elaborate a little bit to convince myself how we will be involved in validating that, right? Would you share us the results after you write the Playwright and other automated test cases? Is that how this will go? Or what would you expect from this forum to say that the expected scope is achieved?"

This is Praveen asking for the governance model. He was not satisfied with knowing that testing happens; he wanted to know how the Cisco team validates the testing, how they see results, and what their role is in declaring "done."

### Colin's Answer: Dashboard Visibility

Colin responded with a specific answer about transparency (closely paraphrased):

"From my end, the way that you would see those results is we would give you, of course, something like a dashboard view. So you could see the test, the agents that ran, what they saw, what their conclusion was. That's the same view that we get on our end because basically that gives us a way to have corrective feedback for the agents."

He then described what the team needs from Cisco:

"I think from this team's side, it's more just knowing kind of what bars we have to hit. If it's just a matter of pointing us to, here's the test suite, here's the expected run-through of it, beyond just simply doing the manual testing, that is probably the most helpful thing."

And on transparency:

"But we can have the agents fully transparent, take it from there. And on your end, you'll have full visibility into everything that we can see too. So you'll see what I say is the good, the bad, and the ugly. Agents don't always work great the first time. But you'll be able to see -- so for instance, here's a Playwright that goes and clicks around a screen, tries out different options with some more deterministic testing workflow to guarantee equivalency between."

He then scoped the visibility by engagement phase:

"Maybe not as in detail for the POC, but certainly the full scope you'll get some good visibility on how that QA is progressing because that can give you kind of an indicator as we make progress through it because there's a lot of screens to do."

### What Colin Committed To

1. A dashboard view showing agent test runs, observations, and conclusions
2. Full transparency -- the Cisco team sees the same view BayOne sees
3. Honest reporting including failures ("the good, the bad, and the ugly")
4. Deterministic testing workflows for equivalency validation
5. Less detailed visibility during POC, full visibility during full engagement

### What Colin Asked For

1. Access to the existing test suites
2. The expected run-through (what passes, what the bar is)
3. Pointers to what "done" looks like for each area

---

## Praveen on Data-Driven Testing and Device Configurations

Praveen then raised a critical nuance about the nature of the testing that goes beyond simple UI validation (closely paraphrased):

"Some of them are screens and UI, which is obvious. And some of the functionalities, data driven -- the configurations you have on devices. Operations performed -- so it's based on the input and that data that is driven, right, given. So that's where I think I'm interested in seeing, right, before both these areas. It's heavily device configuration driven -- different possible configurations that are possible on the devices."

He continued with the key point:

"The input test cases and data is what will give the coverage, right? So you can have -- it's one single row entry, but it can be different with different values and different regular expression or different syntax for each value in some of the cases."

### What Praveen Was Describing

This is data-driven testing where:

- The same UI screen or workflow behaves differently depending on the device type and its configuration
- A single test case (one row in the test matrix) can have many variations in values, regular expressions, and syntax
- The device configurations are the primary input variable, not just the UI elements
- Coverage is achieved by exercising the full matrix of device types and configuration patterns, not just by clicking through screens

This is a critical point for the engagement because it means Playwright-based UI testing alone is insufficient. The testing must also account for the data dimension: the same screen rendering differently based on different device configurations, different SNMP values, different CLI output patterns.

### Praveen's Direct Question About Test Reuse

Praveen asked explicitly (closely paraphrased):

"So that's where I was thinking, will you take the existing test cases and integrate along with -- how is your, you can call it regression too, right? On product A, I have 10,000 test cases, let's say. When I go to product B, the same 10,000 test cases should work here."

This is the clearest articulation of Praveen's expectation: the existing test cases from EPNM should be runnable against the new classic UI on EMS. The test cases are the source of truth for equivalency, not just visual inspection.

---

## Colin's Response on Coverage Gaps and Cross-Pollination

Colin responded to the test reuse question and then extended it (closely paraphrased):

"And I'll ask Srinivas as well for permission to share across what we're doing for NX-OS, because that might give you the clearest view of what specifically we can do with this testing."

He then offered a preview:

"I'll say at a high level, what we can do as well is look for coverage gaps as well. So, you know, even existing unit tests -- 10 years is a long time for an application. A lot of things accumulate over that period. So we can even look at and say, here is some suggestions for this as well in case any holes are found, especially moving over to a new stack, new architecture. Maybe the old unit tests are still working, but maybe there's more that could be needed for true full coverage."

He qualified: "It's not saying to rewrite all the tests, anything like that. Mostly just doing an even deeper gap analysis to make sure that every angle is covered."

This is Colin going beyond the immediate ask (make the existing tests pass) to offer proactive value (find where the existing tests are themselves insufficient). He tied this to the architecture migration: tests that were adequate for the monolithic EPNM architecture may not cover everything needed in the microservices-based EMS architecture.

---

## Ramesh's Contribution: Existing Tests Will Not Work

Ramesh (or Praveen, building on Ramesh's point) then made a critical observation. The exchange (closely paraphrased):

**Ramesh/Praveen:** "If you can do the midpoint of the existing test and then see the same test passing with the newer classic UI-driven flow -- right, that's the point one. And then if there are gaps in anything in the existing test, we can find out or add anything there that will also be good."

**Praveen (clarifying):** "The existing test will not work, right? So at least the UI-based, they will not work because the UI is going to change. So are we saying that a replica of the existing test case will be created?"

**Colin:** "Yes, yes."

**Praveen (confirming):** "For example, if you're doing a device add and then testing out certain attributes, you would need to do that using the classic UI flow and say that similar functionality has been done. And the POC will include this item as well."

### Why This Is Critical

Praveen identified the fundamental testing problem: the existing UI tests are written against the EPNM UI (Dojo/legacy framework). The new classic UI will be rewritten in Angular. Even though the visual appearance and UX flow will be identical, the underlying DOM structure, component hierarchy, selectors, and event handling will be completely different. Therefore:

1. Existing UI test selectors will not match the new Angular components
2. Existing test automation scripts that depend on Dojo-specific DOM patterns will fail
3. New test cases must be created that replicate the same functional coverage but target the Angular-based classic UI

This means BayOne's scope includes not just building the classic UI toggle but also creating test cases that validate the classic UI against the same functional expectations as the original EPNM test suite.

---

## POC vs. Full Engagement Testing Scope

Colin then drew a clear line between what testing looks like in the POC versus the full engagement (closely paraphrased):

"So for the testing, what we'll have to do for the POC, we won't do the full strut of it. We'll do enough that we can guarantee the existing equivalency. So if there's, let's say, for instance, unit tests that are missing, that will be even internally to us before I come back to you and say, OK, we're done with the POC. That's what I would want to run on my end to make sure that I'm not wasting your time. If I say everything's done, I want that to mean that everything is done and tested. So that part will be there."

And on the agentic gap analysis:

"Now, for the agentic part for the gap analysis, that probably will wait till the full engagement, just because that will take some time and that'll make the POC drag out."

### POC Testing Scope

- Enough testing to guarantee existing functional equivalency for the selected screens
- Internal unit testing before declaring the POC complete
- No agentic gap analysis (deferred to full engagement)
- Colin personally accountable since it is a one-person POC

### Full Engagement Testing Scope

- Full agentic QA with Playwright agents
- Coverage gap analysis (finding holes in existing test suites)
- Dashboard visibility for Cisco team
- Regression suite integration
- Data-driven test case creation for device configuration matrix
- This is where the "replica of existing test cases" for the Angular UI would be fully built out

Colin tied the timeline motivation to Venkat's delivery target: "I think whenever we had talked to Venkat he was mentioning something like July, which is why my motivation is to get the POC kind of out the door, prove this to you as quick as I can so that we have a good enough runway to aim for something closer. I think he had mentioned either July or August as a target, which is tight, but we'll make it work."

---

## Summary of Testing Commitments and Expectations

| Item | POC Scope | Full Engagement Scope |
|---|---|---|
| Functional equivalency testing | Yes -- enough to prove the selected screens work | Yes -- comprehensive across all screens |
| Unit tests | Internal to BayOne, run before declaring done | Full coverage, including new tests for gaps |
| Playwright agent testing | Limited or none | Full automated UI testing with agent-driven exploration |
| Existing regression suite integration | Awareness and understanding | Full integration, existing tests replicated for new UI |
| Data-driven device configuration testing | Not explicitly committed | Expected, per Praveen's description of test matrix |
| Coverage gap analysis | Not included | Included, with proactive identification of missing tests |
| Dashboard visibility for Cisco team | Limited detail | Full transparency, same view as BayOne |
| Agentic QA service | Not included | Full service with judge agent, corrective feedback loops |

---

## Open Questions

1. **Who provides the existing test suites?** Colin asked for access to the test suites and their expected run-through, but no specific person was assigned to provide this. The tech leads (Akhil, Rama, Janice) are the likely contacts, but no action item was captured.

2. **What format are the existing test cases in?** Praveen described "thousands and thousands of test cases" with data-driven variations across device configurations. The automation framework, test case format, and how they are organized (by feature area, by device type, by test category) were not discussed.

3. **How will test case replication work in practice?** Praveen confirmed that existing UI tests will not work and that replicas must be created. But the mechanics were not specified: will BayOne receive the existing test cases as a specification and write new Angular-compatible versions? Or will BayOne need to reverse-engineer the test intent from the test scripts?

4. **Customer-specific profiles in testing.** Praveen mentioned "customer-specific profiles" as part of the test infrastructure. Whether these are in scope for the POC or full engagement was not discussed. These could represent a significant expansion of the test matrix.

5. **Scale testing for the classic UI.** Praveen listed scale testing as part of the lifecycle. Whether the new classic UI needs its own scale testing (large number of devices, large alarm volumes) was not discussed.

6. **Who validates the dashboard?** Colin committed to providing a dashboard view of agent test results. Whether the Cisco team has the bandwidth or mandate to actively review this dashboard, or whether it would be a passive artifact, was not established.

7. **Cross-project sharing.** Colin offered to share the NX-OS testing approach (with Srinivas's permission) as a reference point. Whether this sharing happened and whether it influenced the EMS testing approach is an open thread.

8. **Test environment requirements.** The meeting discussed needing a VM and EPNM/CNC server access for development and patching. Whether the test suites require specific test environments (lab devices, simulated device configurations) was not addressed.

9. **API testing scope.** Praveen listed API testing as part of the lifecycle. Since the classic UI will talk to the new EMS backend (not the EPNM backend), API-level testing of the integration points between the Angular classic UI and the EMS APIs was not explicitly discussed.

10. **Migration and upgrade testing.** These categories in the test lifecycle were mentioned but not discussed in the context of the classic UI toggle. Whether the toggle feature itself needs migration testing (between EMS releases) is an open question.

---

## Key Quotes

**Colin introducing the QA topic:**
> "Part of what we can offer is also something that will save you some time, hopefully, which is a more agentic QA/QE service. That, again, we're just building custom for you. It's just part of what we can offer. That does not have to replace a traditional QA/QE step, especially because this will go production. That's just meant to catch problems, really."

**Praveen describing the existing test infrastructure:**
> "All features go through our test lifecycle of functional testing, scale testing, end-to-end testing, UI testing, API testing, migration testing, across releases, upgrade, scale. And we also have probably customer-specific profiles and so on and so forth. And we have automation in place too for some of the regression. So it goes to thousands and thousands of test cases, right, across different devices and functionality."

**Praveen asking how BayOne validates:**
> "Now what's the best way now for us to confirm that what is developed is on par with that area of -- let's say network inventory, device details, device 360, alarms view, events view, and the specific fault area?"

**Colin on the danger of manual-only testing:**
> "The worst thing is when you have testing, if you have a large test suite, is everything looks good. We test even manually and we make sure everything is great. But then you run the test suite and there's a bunch of holes."

**Colin on Playwright agents:**
> "We typically will have some agents that use Playwright to actually do automated UI testing, even beyond just function coverage or code coverage type tests."

**Colin on what Playwright agents prevent:**
> "That saves us from saying, you know, AI said, look, all this is done. And then you go and actually try it as a human and you say, what? This doesn't look right at all. So we have a way to use Playwright with agents to even do the automated equivalent of what a human being would do for the testing."

**Colin on BayOne's internal QA model:**
> "I actually don't have a traditional QA/QE team. Because this works so well. We have QA/QE experts that are manning the agents and recognizing things. But at the same time every single project we do happens this way for testing."

**Praveen pressing for visibility:**
> "I'm trying to elaborate a little bit to convince myself how we will be involved in validating that, right? Would you share us the results after you write the Playwright and other automated test cases?"

**Colin on dashboard transparency:**
> "From my end, the way that you would see those results is we would give you, of course, something like a dashboard view. So you could see the test, the agents that ran, what they saw, what their conclusion was. That's the same view that we get on our end."

**Colin on honest reporting:**
> "You'll see what I say is the good, the bad, and the ugly. Agents don't always work great the first time."

**Praveen on data-driven testing:**
> "Some of the functionalities, data driven -- the configurations you have on devices. Operations performed -- so it's based on the input and that data that is driven. It's heavily device configuration driven -- different possible configurations that are possible on the devices."

**Praveen on test matrix complexity:**
> "It's one single row entry, but it can be different with different values and different regular expression or different syntax for each value in some of the cases."

**Praveen on test reuse expectation:**
> "On product A, I have 10,000 test cases, let's say. When I go to product B, the same 10,000 test cases should work here."

**Praveen identifying the core testing problem:**
> "The existing test will not work, right? So at least the UI-based, they will not work because the UI is going to change. So are we saying that a replica of the existing test case will be created?"

**Colin on POC vs. full engagement testing:**
> "For the testing, what we'll have to do for the POC, we won't do the full strut of it. We'll do enough that we can guarantee the existing equivalency."

**Colin on the agentic gap analysis deferral:**
> "For the agentic part for the gap analysis, that probably will wait till the full engagement, just because that will take some time and that'll make the POC drag out."

**Colin on timeline motivation:**
> "I think whenever we had talked to Venkat he was mentioning something like July, which is why my motivation is to get the POC kind of out the door, prove this to you as quick as I can so that we have a good enough runway."

**Colin on coverage gap detection:**
> "Even existing unit tests -- 10 years is a long time for an application. A lot of things accumulate over that period. So we can even look at and say, here is some suggestions for this as well in case any holes are found, especially moving over to a new stack, new architecture."
