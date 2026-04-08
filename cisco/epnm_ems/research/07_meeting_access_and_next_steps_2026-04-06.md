# 07 - Meeting: Access and Next Steps

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting)
**Pass:** Focused deep dive on access setup and next steps

---

## 1. Repository Access via AD Groups

The primary access gate is Active Directory group membership. Akhil explained the mechanism: "It is basically controlled through AD groups, so when we can get that activated to that item and a few groups we have to enable this access. So once after that, he can seamlessly access all the repos."

The repositories Colin needs access to (as enumerated by Akhil during the walkthrough):

**EPNM repositories (read access):**
- PI framework — core Dojo-based framework
- Wireless framework / wireless repos
- Assembly repo — contains inventory screens (UI side)
- ChassisView repo — device chassis visualizations
- Fold management (fault management) — EPA wireless repo
- A complete repository list link was provided on the Confluence page

**EMS repositories (development access):**
- **Infra UI** — shell app containing the header, top menu, and infrastructure UI components
- **Common UI** — shared component library (cards, tables, and other reusable components)
- **EMS UI** — feature-specific pages (software image management, inventory, etc.). This is the primary repo where Colin's work will live.
- Corresponding backend repos (Spring Boot, some Go services)

Akhil stated: "Mostly I think you have to work on this EMS UI." Colin's new classic-view Angular code will either be placed in a new folder within the EMS UI repo or in a separate new repo — this decision was explicitly deferred. Akhil: "Maybe you can create a folder and for now you can add it out there or you can create a separate repository also. It's up to you all. You can think about it and come up with your plan, then we can review it."

Selva confirmed: "I think for access we can all help... So what do we need to do to get his ID added?" The access provisioning will be handled by Akhil or another team member on the Cisco side.

Colin already has a Cisco-issued identity (colmoore@cisco.com) from the existing NX-OS CI/CD engagement, which should streamline the AD group additions.

---

## 2. VM Requirements

Two distinct VM needs were identified:

### EPNM — Read-Only Access
The team agreed Colin needs read-only access to an EPNM system. Ramakrishna (Rama) clarified the need: "Read only access to an EPNM system." This is for exploring the existing classic UI, understanding screen layouts, data flows, and functional behavior. No development or code deployment happens here — it is purely a reference environment.

### EMS / CNC — Development Setup
Colin needs a development setup on the EMS / Crosswork Network Controller (CNC) side. Rama described the need: "Read only access to a CNC and then when he's ready with the new code and everything, we need to help him patch it." The flow is: initial read-only access for exploration, then deployment access when Colin has code ready to patch and verify.

Rama also noted that artifact deployment requires a server: "It's only for... patching the artifact binaries and then verifying, swapping. Because definitely you might need a setup for the EPNM and one setup for CNC."

### Existing VM from CI/CD Project
Colin mentioned an existing VM from the NX-OS CI/CD project: "I think for the other project, there's one that's coming from someone named Devakar that's a little bit different. I think that one's specific to NX-OS." He correctly noted it should remain separate: "I think they're technically supposed to be separate, so I think we will need one of those."

**Decision:** New, separate VMs will be provisioned for this engagement. The CI/CD project VMs (from Divakar) are NX-OS-specific and will not be repurposed.

### Who Provides
Rama suggested leveraging US-based resources for easier setup: "I think as in the US, probably it's easy for him to get a setup from this. I know they can see. I can walk through them and I can just call them and connect with them." Ramesh appears to be the US-based team member who will facilitate this.

---

## 3. Team Space / Communication Infrastructure

### WebEx Team Space
Selva raised the question of a team space: "Are you going to have a team space? There is a team space that was started. All the folks there, or you want to create a new team space, how would you prefer?"

The group decided to create a new team space. Selva directed: "I will let Aadit or Praveen create one and then just adding, besides Colin, let us know who else needs to be added there."

Colin requested adding the entire BayOne account management team: "We'll just add the entire B1 account management team, Selva, if that's okay. And then the folks from your team." Selva agreed.

Neha confirmed she would coordinate: "Sure, Selva, I'll work with them."

The team space will serve as the primary asynchronous communication channel for day-to-day coordination between BayOne and the Cisco engineering team.

### Recurring Meeting Cadence
Selva suggested using a recurring call structure: "I can create a... this usually do with check along these calls to start with, yes." He proposed a standing meeting with the ~12 participants from this call. Aadit confirmed he would help set this up.

---

## 4. Confluence Page — Prepared Materials

One of the most notable aspects of this meeting was the Cisco team's advance preparation. A Confluence page had already been assembled with structured materials for onboarding. Akhil walked through it during the meeting, and it contained:

- **User guides** for both EPNM and EMS
- **API documentation** for both products
- **Recordings** of EPNM device onboarding and network device workflows
- **Recordings** of EMS inventory and detailed views
- **Complete repository list** with links to all relevant repos (EPNM and EMS)
- **Code pointers** to key repos (Infra UI, Common UI, EMS UI, PI framework, etc.)

Akhil introduced the page: "There is a user guide which is added here and similar in EMS... Then there is API documentation also added here. So I think our team has added some recordings so we can also go through the EPNM device onboarding and network devices. So that recording is added here. Similar way, EMS inventory and detailed views, recordings also added."

Colin was visibly impressed: "I have to give you a compliment. Usually, whenever we get into these specific projects, even that Confluence page where it was showing, here's the specific links to everything. Here's where this information is. Usually we have to go digging for that. So actually my life is a lot easier because this is really organized."

This is a significant positive indicator of the Cisco team's engagement level and organizational maturity.

---

## 5. Code Pointers — Email Follow-Up

At the close of the meeting, Selva asked about sharing code details. Akhil committed to sharing code pointers via email reply to the meeting invite: "I'll share it in this email. This details what I shared... In this meeting invite, I'll reply to it."

This email would contain the specific repository links and code navigation pointers that Akhil demonstrated during the live walkthrough, supplementing the Confluence page content with more targeted guidance.

---

## 6. Time Zone Coordination

Selva explicitly established time zones for all participants at the meeting's close:

| Participant(s) | Time Zone | Location |
|---|---|---|
| Akhil, Praveen, Aadit, Jenis, Ramakrishna, Senthil | IST (India Standard Time, UTC+5:30) | India |
| Colin Moore | EST (Eastern Standard Time, UTC-5) | US East Coast |
| Selva Subramanian | US (likely PST or CST — not specified) | US |
| Ramesh Dhashnamoorthy | US (likely PST — not specified) | US |
| Zahra Syed | PST (Pacific Standard Time, UTC-8) | US West Coast |
| Neha Malhotra, Rahul Bobbili | Not stated (likely PST based on BayOne HQ) | US |

Selva framed this explicitly: "Colin, you are in the East Coast? I just want to give everyone the sense of time zones." Colin confirmed: "Yes, I'm in EST, Eastern time." Selva noted: "This team here except me and Ramesh, everyone is in the India time zone."

Zahra's time zone was confirmed by Selva: "And then the rest of the B1 team is here and PST is from Zahra." Zahra confirmed: "That's correct."

**Operational implication:** The IST-to-EST overlap window is roughly 8:00 AM - 12:30 PM EST (6:30 PM - 11:00 PM IST). Scheduling recurring syncs will need to accommodate this narrow window. The team space becomes critical for asynchronous communication outside these hours.

---

## 7. Zahra and Rahul's Roles — Clarified

This meeting provided the clearest articulation yet of the BayOne team structure for this engagement.

**Zahra Syed** described the structure: "Colin will be leading the entire engagement end-to-end. Neha will be working very closely with him and Rahul and I will be on the back end, but Colin and Neha will be the point of contact."

**Rahul Bobbili** clarified his and Neha's support role: "The intent of adding Neha and I and our role to the call is Colin will make sure he gets back to you. Sometimes he gets a little backlog and he just needs a little tiny internal nudge. So we'll make sure that any questions you guys have, Neha and me will make sure that, you know, you get a response back."

In summary:
- **Colin Moore** — Technical lead. Sole POC executor. All technical decisions flow through him. Will work both frontend and backend.
- **Neha Malhotra** — Day-to-day engagement operations. Working "very closely" with Colin. Co-point-of-contact.
- **Zahra Syed** — Strategic account director. "Back end" support (business relationship, not code). Not day-to-day involved.
- **Rahul Bobbili** — President, BayOne. "Back end" support. Ensures responsiveness. Internal escalation path.

Selva's framing from the start: "Colin will be the main guy we'll be interfacing with... Zahra and Neha on the business side, and then Rahul will be working with Colin in this engagement."

---

## 8. Plan for Getting Colin Started

The overall onboarding sequence discussed in this meeting, synthesized from multiple conversation threads:

### Immediate (Days 1-3)
1. **AD group access** — Akhil or another team member adds Colin's Cisco ID to the required AD groups for EPNM and EMS repos
2. **Email with code pointers** — Akhil replies to meeting invite with specific repo links and navigation guidance
3. **Confluence page review** — Colin reviews the prepared Confluence page (user guides, API docs, recordings)
4. **Team space creation** — Aadit or Praveen creates WebEx team space and adds Colin, Neha, and the BayOne account management team

### Near-Term (Week 1-2)
5. **VM provisioning** — Ramesh (US-based) helps Colin get EPNM read-only access and an EMS development setup
6. **Code deep dive** — Colin performs a "full deep dive breakdown of exactly the UIs, how they map" starting with the specific POC screens (inventory, device 360, device details, fault management)
7. **Gap analysis** — Identify any backend functionality gaps between EPNM and EMS for the target screens

### POC Execution
8. **Solo development** — Colin works alone on both frontend (Angular) and backend during the POC
9. **Testing** — Enough automated testing (including Playwright UI testing) to guarantee functional equivalency
10. **POC delivery** — Demonstrate the theme toggle with classic EPNM look-and-feel running against the EMS backend

### Post-POC (if approved)
11. **Team scale-up** — Colin plus approximately three additional people
12. **Full agentic QA** — Comprehensive gap analysis against existing regression suites
13. **Target delivery** — July or August 2026 (per Venkat's earlier indication)

---

## 9. Action Item Table

| # | Action Item | Owner | Timeline | Status |
|---|---|---|---|---|
| 1 | Add Colin's Cisco ID to AD groups for EPNM and EMS repos | Akhil / Cisco team | Immediate (next business day) | Pending |
| 2 | Reply to meeting invite email with code pointers and repo links | Akhil | Immediate (after meeting) | Pending |
| 3 | Create WebEx team space for the engagement | Aadit or Praveen | Within days | Pending |
| 4 | Provide list of BayOne team members to add to team space | Neha | After team space is created | Pending |
| 5 | Set up recurring sync meeting (~12 participants) | Selva / Aadit | Within first week | Pending |
| 6 | Provision EPNM read-only VM access for Colin | Ramesh (US) / Cisco team | Week 1 | Pending |
| 7 | Provision EMS/CNC development VM for Colin | Ramesh (US) / Cisco team | Week 1-2 | Pending |
| 8 | Review Confluence page materials (user guides, recordings, API docs) | Colin | Week 1 | Pending |
| 9 | Complete code deep dive / UI mapping of target POC screens | Colin | Weeks 1-2 | Pending |
| 10 | Propose code organization plan (folder in EMS UI repo vs. new repo) | Colin | During POC | Pending |
| 11 | Ask Srinivas for permission to share NX-OS CI/CD testing approach with EPNM team | Colin | Near-term | Pending |
| 12 | Identify regression test suites applicable to POC scope areas | Cisco engineering team | During POC | Pending |

---

## 10. Open Questions

1. **Specific AD groups needed:** Which exact AD groups does Colin need? Akhil mentioned "a few groups" but did not enumerate them. This needs to be resolved during the access provisioning process.

2. **Code organization decision:** Where should the classic UI Angular code live — a subfolder within the EMS UI repo or a new dedicated repo? Akhil deferred this: "You can think about it and come up with your plan, then we can review it." Colin needs to propose an approach.

3. **VM provisioning timeline:** No firm commitment was made on when VMs would be ready. Ramesh offered to help but no specific date was set.

4. **Recurring meeting frequency and time:** Selva mentioned setting up check-in calls but no specific cadence (daily? weekly?) or time slot was agreed upon. The IST/EST overlap constraint makes this non-trivial.

5. **Backend gap specifics:** Rama estimated ~80% of backend functionality is reimplemented in EMS. The remaining ~20% for the POC-scoped screens has not been inventoried. Colin committed to flagging gaps during his deep dive, but there may be items the Cisco team already knows are missing.

6. **Who is Ramesh's US contact for VM setup?** Rama mentioned: "I know they can see. I can walk through them and I can just call them and connect with them." The specific person or team responsible for VM provisioning was not named.

7. **Confluence page access:** It is unclear whether Colin currently has access to the Confluence space where the onboarding materials were posted, or if that also requires separate access provisioning.

8. **POC timeline clarity:** Colin mentioned Venkat had indicated July or August as a delivery target, but this was not discussed or confirmed in this meeting. The POC duration itself (previously discussed as ~2 weeks) was not revisited.

9. **Test suite access:** Ramesh and Rama discussed the importance of existing regression suites, but no commitment was made on sharing those with Colin during the POC phase. The data-driven testing aspect (device configurations driving test coverage) needs further discussion.

10. **Neha's Cisco access status:** Neha was identified as a day-to-day contact, but it is unclear whether she has Cisco accounts, repo access, or will be added to the same AD groups as Colin.
