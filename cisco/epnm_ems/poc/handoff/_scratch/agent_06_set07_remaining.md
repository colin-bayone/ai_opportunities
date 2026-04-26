# Agent 06 — Set 07 Remaining Deep Dives (Testing, QA, Access, Next Steps)

**Source files:**
- `07_meeting_testing_and_qa_approach_2026-04-06.md`
- `07_meeting_access_and_next_steps_2026-04-06.md`

Source meeting date: 2026-04-06 (EPNM Features Walkthrough, Selva and team).

---

## 1. Existing Test Infrastructure at Cisco

Source: `07_meeting_testing_and_qa_approach_2026-04-06.md`

Praveen described the existing test infrastructure as follows. The EPNM product functionality has been developed for more than ten years, and all features pass through a mature test lifecycle.

### The seven testing categories

1. **Functional testing** — Verifies that individual features work as designed.
2. **Scale testing** — Tests under load with large numbers of devices.
3. **End-to-end testing** — Full workflow testing across feature boundaries.
4. **UI testing** — Testing the user interface specifically.
5. **API testing** — Testing backend API endpoints.
6. **Migration testing** — Testing across product releases (for example, EPNM version upgrades).
7. **Upgrade testing** — Testing that upgrade paths preserve functionality.

### Additional elements of the existing test infrastructure

- **Customer-specific profiles.** Test configurations representing specific customer deployments. Testing runs not only against generic configurations but also against real-world deployment patterns.
- **Automation for regression.** A portion of the regression suite is already automated.
- **Thousands of test cases.** Praveen used the phrase "thousands and thousands of test cases" across different devices and functionality.
- **Cross-device coverage.** Tests span different devices and different functionality; the test matrix includes device type as a variable.

### Data-driven testing approach

Praveen described that testing is heavily data-driven. Specifically:

- The same UI screen or workflow behaves differently depending on the device type and its configuration.
- A single test case (one row in the test matrix) can have many variations in values, regular expressions, and syntax for each value.
- The device configurations are the primary input variable, not just the UI elements.
- Coverage is achieved by exercising the full matrix of device types and configuration patterns, not just by clicking through screens.

Praveen's direct framing: "On product A, I have 10,000 test cases, let's say. When I go to product B, the same 10,000 test cases should work here."

### Named tools, frameworks, and repositories

The two source files did not name a specific test automation framework, test-case management tool, or dedicated repository for the test suites. Praveen referred to regression suites and existing automation in general terms only. No specific repository path for tests was surfaced in these two files.

---

## 2. Why Existing UI Tests Will Not Work for the Classic UI

Source: `07_meeting_testing_and_qa_approach_2026-04-06.md`

### The reasoning the team gave

Praveen stated the problem directly: "The existing test will not work, right? So at least the UI-based, they will not work because the UI is going to change. So are we saying that a replica of the existing test case will be created?" Colin confirmed: "Yes, yes."

The underlying reasoning, as captured in the file:

- The existing UI tests are written against the EPNM UI, which uses Dojo and legacy framework components.
- The new classic UI will be rewritten in Angular.
- Even though the visual appearance and user-experience flow will be identical, the underlying DOM structure, component hierarchy, selectors, and event handling will be completely different.
- Therefore:
  1. Existing UI test selectors will not match the new Angular components.
  2. Existing test automation scripts that depend on Dojo-specific DOM patterns will fail.
  3. New test cases must be created that replicate the same functional coverage but target the Angular-based classic UI.

### What needs to be built as replacement

Praveen articulated the expectation with a concrete example: "For example, if you're doing a device add and then testing out certain attributes, you would need to do that using the classic UI flow and say that similar functionality has been done. And the POC will include this item as well."

In summary, the replacement work required:

- A replica of the existing UI test cases, targeting the Angular-based classic UI.
- Preservation of the same functional coverage as the original EPNM UI test suite.
- Coverage of the data-driven dimension (different device types, configurations, values, regular expressions, syntax variations), not just click-through of UI elements.
- Scope includes not just building the classic UI toggle but also creating test cases that validate the classic UI against the same functional expectations as the original EPNM test suite.

---

## 3. Testing Expectations for the POC Specifically

Source: `07_meeting_testing_and_qa_approach_2026-04-06.md`

Colin drew a clear line between POC testing and full-engagement testing.

### POC testing scope (in scope)

- Enough testing to guarantee existing functional equivalency for the selected screens (Inventory and Fault Management).
- Internal unit testing by BayOne before declaring the POC complete. Colin said: "If there's, let's say, for instance, unit tests that are missing, that will be even internally to us before I come back to you and say, OK, we're done with the POC."
- Colin personally accountable for testing since the POC is a one-person effort.
- Awareness and understanding of the existing regression suite (but not full integration at POC stage).

### Deferred to post-POC (full engagement)

- Full agentic QA with Playwright agents.
- Coverage gap analysis (identifying holes in existing test suites).
- Dashboard visibility for the Cisco team.
- Full regression-suite integration.
- Data-driven test case creation for the device configuration matrix.
- The full replica of existing test cases for the Angular UI.

Colin explicitly deferred the gap analysis: "For the agentic part for the gap analysis, that probably will wait till the full engagement, just because that will take some time and that'll make the POC drag out."

### Colin's Playwright agent approach as explained

Colin described the Playwright agent capability in the meeting:

- BayOne uses agents that drive Playwright to perform automated UI testing, going beyond functional coverage or code coverage.
- The agents do more than run deterministic test scripts; they perform the "automated equivalent of what a human being would do for the testing." Colin described this as clicking around a screen, trying out different options, and combining exploratory behavior with deterministic testing workflow.
- The stated purpose is to prevent the failure mode where the AI declares work complete but a human-eye check reveals visible defects.
- BayOne's internal model: "I actually don't have a traditional QA/QE team. We have QA/QE experts that are manning the agents and recognizing things. But at the same time every single project we do happens this way for testing." The concurrent Srinivas / NX-OS CI/CD project was cited as a live example of the same approach at Cisco.
- Colin committed to a dashboard view for the Cisco team showing the tests, the agents that ran, what they saw, and their conclusions. The Cisco team would see the same view BayOne sees, including failures ("the good, the bad, and the ugly"). Visibility will be limited during the POC and more detailed during the full engagement.

### Classic-vs-new equivalency verification

- The verification goal is that the new classic UI on EMS is "on par with" the EPNM equivalent screens: network inventory, device details, device 360, alarms view, events view, and the specific fault area.
- Colin preferred regression suite reuse over demo-and-manual-validation. Integrating with the existing regression suite during development catches holes incrementally rather than in a big-bang test run at the end.
- Colin offered: "Here's a Playwright that goes and clicks around a screen, tries out different options with some more deterministic testing workflow to guarantee equivalency between" the old and new UIs.
- Colin asked the Cisco team for: access to the existing test suites, the expected run-through (what passes, what the bar is), and pointers to what "done" looks like for each area.

---

## 4. Access Provisioning Requirements

Source: `07_meeting_access_and_next_steps_2026-04-06.md`

### Active Directory group access

The primary access gate is Active Directory group membership. Akhil's statement: "It is basically controlled through AD groups, so when we can get that activated to that item and a few groups we have to enable this access. So once after that, he can seamlessly access all the repos."

The specific AD groups Colin needs were not enumerated in the meeting. Akhil referred to "a few groups" without listing them.

### Repositories to which Colin needs access

**EPNM repositories (read access):**

- PI framework — core Dojo-based framework.
- Wireless framework / wireless repos.
- Assembly repo — contains inventory screens (UI side).
- ChassisView repo — device chassis visualizations.
- Fold management (fault management) — EPA wireless repo.
- A complete repository list link was provided on the Confluence page.

**EMS repositories (development access):**

- **Infra UI** — shell app containing the header, top menu, and infrastructure UI components.
- **Common UI** — shared component library (cards, tables, and other reusable components).
- **EMS UI** — feature-specific pages (software image management, inventory, and similar). This is the primary repository where Colin's work will live. Akhil: "Mostly I think you have to work on this EMS UI."
- Corresponding backend repositories (Spring Boot, with some Go services).

### VM requirements

Two distinct VMs are needed:

- **EPNM — read-only access.** For exploring the existing classic UI, understanding screen layouts, data flows, and functional behavior. Ramakrishna (Rama): "Read only access to an EPNM system." Purely a reference environment; no development or code deployment.
- **EMS / CNC — development setup.** Initial read-only access for exploration, then deployment access when Colin has code ready to patch and verify. Rama: "Read only access to a CNC and then when he's ready with the new code and everything, we need to help him patch it." Rama also noted that artifact deployment requires a server: "It's only for patching the artifact binaries and then verifying, swapping. Because definitely you might need a setup for the EPNM and one setup for CNC."

Decision: new, separate VMs will be provisioned for this engagement. The existing VMs from the NX-OS CI/CD project (provisioned by Divakar) are NX-OS-specific and will not be repurposed. Colin noted the two efforts are "technically supposed to be separate."

Rama suggested leveraging US-based resources for easier setup; Ramesh appears to be the US-based team member who will facilitate this. The specific US contact or team who will actually provision the VMs was not named.

### Cisco ID

Colin already has a Cisco-issued identity (colmoore@cisco.com) from the existing NX-OS CI/CD engagement. This existing Cisco ID should streamline the AD group additions. The provisioning is expected to be handled by Akhil or another Cisco team member. Selva: "I think for access we can all help... So what do we need to do to get his ID added?"

### Confluence page

A Confluence page had already been assembled by the Cisco team before this meeting. Akhil walked Colin through it live. Contents:

- User guides for both EPNM and EMS.
- API documentation for both products.
- Recordings of EPNM device onboarding and network device workflows.
- Recordings of EMS inventory and detailed views.
- Complete repository list with links to all relevant repositories (EPNM and EMS).
- Code pointers to key repositories (Infra UI, Common UI, EMS UI, PI framework, and others).

It is not explicitly confirmed in the file whether Colin currently has access to the Confluence space or whether that also requires separate access provisioning. This was called out as an open question.

### Other access mechanisms described

- **Email with code pointers.** Akhil committed to replying to the meeting invite via email with specific repository links and code navigation pointers, supplementing the Confluence page.
- **WebEx team space.** A new WebEx team space will be created. Aadit or Praveen will create it. The BayOne account management team plus the Cisco engineering team will be added.

---

## 5. Next-Steps Action Items from Set 07

Source: `07_meeting_access_and_next_steps_2026-04-06.md`

The source file lists twelve action items in a dedicated table. All items are marked with status "Pending" in the file.

| # | Action Item | Owner | Timeline | Status |
|---|---|---|---|---|
| 1 | Add Colin's Cisco ID to AD groups for EPNM and EMS repositories | Akhil / Cisco team | Immediate (next business day) | Pending |
| 2 | Reply to meeting invite email with code pointers and repository links | Akhil | Immediate (after meeting) | Pending |
| 3 | Create WebEx team space for the engagement | Aadit or Praveen | Within days | Pending |
| 4 | Provide list of BayOne team members to add to team space | Neha | After team space is created | Pending |
| 5 | Set up recurring sync meeting (approximately 12 participants) | Selva / Aadit | Within first week | Pending |
| 6 | Provision EPNM read-only VM access for Colin | Ramesh (US) / Cisco team | Week 1 | Pending |
| 7 | Provision EMS/CNC development VM for Colin | Ramesh (US) / Cisco team | Week 1-2 | Pending |
| 8 | Review Confluence page materials (user guides, recordings, API documentation) | Colin | Week 1 | Pending |
| 9 | Complete code deep dive / UI mapping of target POC screens | Colin | Weeks 1-2 | Pending |
| 10 | Propose code organization plan (folder in EMS UI repo vs. new repo) | Colin | During POC | Pending |
| 11 | Ask Srinivas for permission to share NX-OS CI/CD testing approach with the EPNM team | Colin | Near-term | Pending |
| 12 | Identify regression test suites applicable to POC scope areas | Cisco engineering team | During POC | Pending |

The file explicitly states all twelve items remain pending, with no completion status marked for any.

---

## 6. Time Zone and Communication Coordination

Source: `07_meeting_access_and_next_steps_2026-04-06.md`

### Time zones, as established by Selva at the end of the meeting

| Participant(s) | Time Zone | Location |
|---|---|---|
| Akhil, Praveen, Aadit, Jenis, Ramakrishna, Senthil | IST (India Standard Time, UTC+5:30) | India |
| Colin Moore | EST (Eastern Standard Time, UTC-5) | US East Coast |
| Selva Subramanian | US (likely PST or CST, not specified in file) | US |
| Ramesh Dhashnamoorthy | US (likely PST, not specified in file) | US |
| Zahra Syed | PST (Pacific Standard Time, UTC-8) | US West Coast |
| Neha Malhotra, Rahul Bobbili | Not stated (likely PST based on BayOne HQ) | US |

Selva's framing: "Colin, you are in the East Coast? I just want to give everyone the sense of time zones." Colin confirmed: "Yes, I'm in EST, Eastern time." Selva noted: "This team here except me and Ramesh, everyone is in the India time zone." Zahra confirmed her PST location when Selva said "And then the rest of the B1 team is here and PST is from Zahra."

### Operational implication

The IST-to-EST overlap window is roughly 8:00 AM to 12:30 PM EST, which corresponds to roughly 6:30 PM to 11:00 PM IST. Recurring syncs will need to accommodate this narrow window. The team space becomes critical for asynchronous communication outside these hours.

### WebEx team space

- A new WebEx team space will be created.
- Selva directed: "I will let Aadit or Praveen create one and then just adding, besides Colin, let us know who else needs to be added there."
- Colin requested adding the entire BayOne account management team plus the folks from the Cisco engineering team. Selva agreed.
- Neha confirmed: "Sure, Selva, I'll work with them."
- The team space will serve as the primary asynchronous communication channel for day-to-day coordination.

### Recurring meeting cadence

- Selva suggested a standing call structure: "I can create a... this usually do with check along these calls to start with, yes."
- Proposed: a standing meeting with the approximately 12 participants from this call.
- Aadit confirmed he would help set it up.
- Specific cadence (daily vs. weekly) and specific time slot were not agreed upon; the file notes this remains to be finalized and lists it among open questions.

---

## 7. Open Questions After Set 07

Source: Both files. The two source files flag the following items as explicitly unresolved.

### From the testing and QA file

1. **Who provides the existing test suites?** Colin asked for access and run-through, but no specific person was assigned. The tech leads (Akhil, Rama, Janice) are the likely contacts but no action item captured.
2. **What format are the existing test cases in?** Automation framework, test-case format, and organization (by feature area, by device type, by test category) were not discussed.
3. **How will test case replication work in practice?** Unclear whether BayOne receives existing test cases as a specification and writes new Angular-compatible versions, or whether BayOne must reverse-engineer test intent from test scripts.
4. **Customer-specific profiles in testing.** Whether these are in scope for the POC or full engagement was not discussed. They could represent a significant expansion of the test matrix.
5. **Scale testing for the classic UI.** Whether the new classic UI needs its own scale testing (large numbers of devices, large alarm volumes) was not discussed.
6. **Who validates the dashboard?** Whether the Cisco team has bandwidth or mandate to actively review the QA dashboard or whether it is a passive artifact was not established.
7. **Cross-project sharing.** Whether Colin's offer to share the NX-OS testing approach (with Srinivas's permission) actually happens, and whether it influences the EMS testing approach, is an open thread.
8. **Test environment requirements.** Whether the test suites require specific test environments (lab devices, simulated device configurations) was not addressed.
9. **API testing scope.** Because the classic UI will talk to the new EMS backend (not the EPNM backend), API-level testing of the integration points between the Angular classic UI and the EMS APIs was not explicitly discussed.
10. **Migration and upgrade testing.** Whether the toggle feature itself needs migration testing (between EMS releases) is an open question.

### From the access and next steps file

1. **Specific AD groups needed.** Akhil referred to "a few groups" but did not enumerate them. To be resolved during access provisioning.
2. **Code organization decision.** Whether the classic UI Angular code lives in a subfolder within the EMS UI repo or a new dedicated repo. Akhil deferred this and asked Colin to propose an approach.
3. **VM provisioning timeline.** No firm date was committed. Ramesh offered to help but no specific date was set.
4. **Recurring meeting frequency and time.** Cadence (daily vs. weekly) and specific slot were not agreed upon; the IST/EST overlap constraint makes this non-trivial.
5. **Backend gap specifics.** Rama estimated approximately 80 percent of backend functionality is reimplemented in EMS. The remaining approximately 20 percent for the POC-scoped screens has not been inventoried. Colin committed to flagging gaps during his deep dive, but there may be items the Cisco team already knows are missing.
6. **Who is the US contact for VM setup?** Rama alluded to US-based colleagues but the specific person or team responsible for VM provisioning was not named.
7. **Confluence page access.** Unclear whether Colin currently has access to the Confluence space or whether that also requires separate access provisioning.
8. **POC timeline clarity.** Colin mentioned Venkat had indicated July or August as a delivery target, but this was not discussed or confirmed in this meeting. The POC duration itself (previously discussed as about two weeks) was not revisited.
9. **Test suite access.** No commitment was made on sharing regression suites with Colin during the POC phase. The data-driven testing aspect (device configurations driving test coverage) needs further discussion.
10. **Neha's Cisco access status.** Unclear whether Neha has Cisco accounts, repository access, or will be added to the same AD groups as Colin.
