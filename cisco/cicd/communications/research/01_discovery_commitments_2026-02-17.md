# 01 - Discovery Meeting: Commitments and Action Items

**Source:** cisco/cicd/communications/source/meeting1_anand_srini_divakar-2-17-2026.txt
**Source Date:** 2026-02-17 (In-person discovery at Cisco office)
**Document Set:** 01 (Feb 17 Discovery Meeting)
**Pass:** Focused on commitments made by both sides and action items

---

## 1. Commitments Made by Cisco

### Divakar

| Commitment | Context | Status as of Meeting |
|---|---|---|
| Provide Jenkins access to BayOne engineers | Divakar has full context on Jenkins and will be the point of access | Pending -- requires onboarding completion first |
| Provision ADS machines for BayOne engineers | Linux machines in Cisco data center for code checkout, viewing, and building | Pending -- Divakar acknowledged this is historically slow and flagged it as a known bottleneck |
| Check with IT on MySQL provisioning | Determine whether an additional MySQL instance is needed or whether BayOne can use an existing one; Cisco currently has ~3 database services from IT | Pending |
| Initiate contact with Airflow team | Divakar does not own Airflow; needs to connect BayOne with the team that does | Pending -- no timeline given |
| Initiate contact with CAT team | Separate team owns CAT; Divakar needs to make the introduction | Pending -- no timeline given |
| Grant GitHub Enterprise access after training completion | Access is read-only; requires engineers to complete 3-4 hour training first | Pending -- blocked on onboarding |
| Share answers to remaining clarification questions | Divakar indicated he has answers to 6 of the open questions and would share after the meeting | Pending |

### Srinivas

| Commitment | Context | Status as of Meeting |
|---|---|---|
| Share DeepSight Atlas recorded presentation with Colin | A 1-1.5 hour recording of Srinivas's presentation to the entire DCT organization covering the platform architecture and capabilities | Committed to sharing via the BayOne WebEx space, pending NDA confirmation |
| Launch existing CI/CD app on DeepSight Atlas within 2-3 weeks | Rui's existing CI/CD application to be deployed on the DeepSight Atlas platform in its current form | In progress -- Srinivas planned to work with Arun's team and Rui to make this happen |
| Post request to WebEx group for Rui to prepare CI/CD app handoff | Explicitly asked to put the request in the WebEx group so Rui and the team are aligned | Committed during meeting |
| Pull Colin into broader meetings | Once onboarded, Srinivas will include Colin in meetings beyond the CI/CD scope so BayOne has context on the broader platform direction and can build toward phase 1 with full information | Future -- after onboarding |
| Provide SDK and platform documentation for DeepSight Atlas | "We'll provide SDK and everything" -- BayOne builds on top of existing infrastructure | Future -- after onboarding and NDA |

### Anand

| Commitment | Context | Status as of Meeting |
|---|---|---|
| Unblock as needed | Will expedite if things are not moving; told Colin to ping him directly if questions go unanswered in the WebEx space | Standing commitment |
| Monitor onboarding process | Agreed to watch the BayOne onboarding as a test case, given Divakar's flagged concerns about ADS provisioning delays for new engineers | Standing commitment |
| Flexible on quarter timing | Confirmed "whenever we get started, the quarter starts then" -- no penalty for onboarding delays eating into fiscal quarter | Agreed during meeting |
| Schedule follow-up in two weeks | Proposed a catch-up meeting in two weeks with Colin, Anand, and Divakar (and potentially Arun depending on progress) | Agreed -- target date approximately March 3, 2026 |
| Manage SOW completion | Acknowledged the SOW is still pending; indicated his team (and Zahra) would handle it | In progress |

---

## 2. Commitments Made by BayOne (Colin)

| Commitment | Context | Status as of Meeting |
|---|---|---|
| Complete GitHub Enterprise training | 3-4 hour mandatory training course; Colin to do it first, then ensure all 5 team members complete it | Pending -- Colin committed to being first |
| Get NDA signed by end of day February 17 | NDA was not yet signed; Colin confirmed background check was complete and committed to same-day NDA execution | In progress -- Colin pinged Rahul during the meeting; Rahul confirmed background check done |
| Watch DeepSight Atlas recorded presentation | 1-1.5 hour recording to understand the platform architecture, UI patterns, and how the CI/CD app fits in | Pending -- blocked on receiving the recording (requires NDA) |
| Keep everything organized from a project perspective | Colin volunteered this; Srinivas reinforced the importance of recorded sessions and meticulous documentation | Standing commitment |
| Onboard full team through access process | 5 people total: 3 onshore (Colin + 1 immediate + 1 within 2 weeks), 2 offshore (identified and active). All to complete background check, hardware provisioning, training, and access requests. | In progress -- staggered onboarding |
| Use WebEx space as primary collaboration channel | Agreed to use the existing BayOne-Cisco WebEx space for questions, status updates, and engineer-to-engineer communication | Active |
| Gather requirements during onboarding gap | While waiting for access and the CI/CD app launch on DeepSight Atlas (2-3 week window), Colin's team should focus on requirements gathering and platform study | Pending |

---

## 3. Action Items with Owners and Timing

| # | Action Item | Owner | Timing |
|---|---|---|---|
| 1 | Sign NDA | Colin (coordinate with Zahra/Rahul) | End of day February 17, 2026 |
| 2 | Complete GitHub Enterprise training | Colin (first), then all 5 BayOne engineers | Within 1 day of access |
| 3 | Share DeepSight Atlas recording in WebEx space | Srinivas | After NDA confirmation |
| 4 | Watch DeepSight Atlas recording | Colin | Immediately after receiving it |
| 5 | Provision ADS machines for BayOne engineers | Divakar | As engineers complete onboarding |
| 6 | Check MySQL instance availability with IT | Divakar | No specific date; post-meeting |
| 7 | Initiate contact with Airflow team | Divakar | No specific date |
| 8 | Initiate contact with CAT team | Divakar | No specific date |
| 9 | Post CI/CD app handoff request to WebEx group for Rui | Srinivas | Immediately post-meeting |
| 10 | Launch existing CI/CD app on DeepSight Atlas | Srinivas / Rui / Arun's team | Within 2-3 weeks (~early March 2026) |
| 11 | Add BayOne engineers to WebEx space | Divakar / Colin | As engineers are identified and onboarded |
| 12 | Finalize SOW | Anand / Zahra | In progress; no hard deadline stated |
| 13 | Schedule and hold follow-up meeting | Anand / Colin | 2 weeks from meeting (~March 3, 2026) |
| 14 | Second discovery session (continuation) | Colin / Divakar / Srinivas | February 18, 2026 (next day) |
| 15 | Share answers to remaining clarification questions | Divakar | After meeting |
| 16 | Onboard first additional engineer (person already with Colin) | Colin | Immediately |
| 17 | Onboard second onshore engineer | Colin | Within 2 weeks |
| 18 | Hardware provisioning for BayOne engineers | Rahul Bhubali (BayOne side) | Already initiated |

---

## 4. What Was Promised for the 2-Week Follow-Up Meeting

Anand outlined the following expectations for the ~March 3 catch-up:

- **Attendees:** Colin, Anand, Divakar (and potentially Arun depending on progress)
- **Purpose:** Review onboarding progress, assess whether access has been granted, determine if BayOne can begin substantive work
- **Expected status by then:**
  - BayOne engineers should have completed GitHub Enterprise training
  - ADS machine provisioning should be in progress or complete
  - Colin should have watched the DeepSight Atlas recording and have a working understanding of the platform
  - The existing CI/CD app should be nearing or at launch on DeepSight Atlas
  - Requirements gathering should be underway
- **Cadence after that:** Anand suggested they would determine ongoing meeting cadence at the 2-week mark. He mentioned possibly involving Arun "depending on where we are" and was "open to suggestions" on format.

---

## 5. Unanswered Discovery Questions

The clarification document (`cisco-questions-for-clarification.md`) contains 31 questions organized into 8 sections. The meeting covered questions rapidly, reaching through approximately question 17 before time ran out. A second session was scheduled for February 18 to continue.

### Questions Addressed (at least partially) During the Meeting

| Q# | Topic | What Was Learned |
|---|---|---|
| 1 | PR volume, developer count, branches | Not directly answered with numbers; deferred to after access is granted |
| 2 | Number of repositories, workflow consistency | Not directly answered; implied variation across teams |
| 3 | Baseline metrics | Not directly answered |
| 4 | Quantitative improvement targets | Not directly answered |
| 5 | MVP timeline and capabilities | Srinivas set expectation of ~2 months after onboarding for a working app on DeepSight Atlas |
| 6 | APIs/data access for CAT, DevX, Jenkins, Airflow, Grafana | Jenkins: Divakar has full context. Airflow: separate team, contact pending. CAT: separate team, contact pending. |
| 7 | Log formats and data schemas | MongoDB for raw pipeline data (single instance). Splunk connected to Jenkins but access restricted. |
| 8 | Sample data/logs | Not provided; requires access first |
| 9 | What Grafana doesn't provide | Not directly answered |
| 10 | Chat interface question types | Partially addressed -- DeepSight Atlas provides the chat interface framework |
| 14 | Jenkins/Airflow log data | Jenkins logs accessible directly; Splunk access unlikely for BayOne |
| 15 | Common failure patterns | Not directly answered |
| 16 | Diagnosis output format | Not directly answered; DeepSight Atlas UI patterns will dictate format |
| 27 | AI models/services -- bring your own or Cisco-provided | Answered: use DeepSight Atlas platform. Cisco provides the AI stack. |
| 28 | AI model restrictions | Answered: everything runs through DeepSight Atlas |
| 29 | Infrastructure hosting | Answered: all on-premises |
| 30 | Security/compliance/network constraints | Partially answered: VPN required, read-only repo access, ADS machines for code access |
| 31 | Screen share / day-in-the-life session | Srinivas committed to recorded sessions; DeepSight Atlas recording covers platform overview |

### Questions That Remain Fully Open

| Q# | Topic | Notes |
|---|---|---|
| 1 | PR volume, developer count, branches | Requires access to answer quantitatively |
| 2 | Repository count and workflow consistency | Requires access |
| 3 | Baseline metrics (merge times, failure rates) | Requires access |
| 4 | Quantitative success targets | Not discussed |
| 9 | Grafana visibility gaps | Not discussed |
| 11 | Developer box: specific data to capture | Not discussed |
| 12 | Developer box: collection mechanism | Not discussed |
| 13 | Developer box: team variation | Not discussed |
| 15 | Common gate failure patterns | Not discussed |
| 16 | Diagnosis output format preference | Not discussed (DeepSight Atlas may constrain this) |
| 17 | CDT gaps beyond current coverage | Not discussed |
| 18 | Condition-level vs. function-level coverage | Not discussed |
| 19 | Coverage tracking scope (dev box, CI, both) | Not discussed |
| 20 | Boundary with internal AI code review project | Not discussed |
| 21 | Acceptable auto-correct failure types | Not discussed |
| 22 | AI autonomy governance policy | Not discussed |
| 23 | Governance criteria as part of scope | Not discussed |
| 24 | Release lead information needs | Not discussed |
| 25 | Existing release lead dashboards | Not discussed |
| 26 | Automated follow-up identification | Not discussed |

### New Questions Raised by the Meeting

These were not in the original clarification document but emerged from discovery:

1. What is the full architecture of DeepSight Atlas, and what SDK/APIs does it expose for application development?
2. What is the current state of Rui's CI/CD app -- what does it do, what are its limitations, and what is the handoff plan?
3. What is the Jira situation -- Divakar said they tried it for a year but engineers pushed back, and it is no longer actively used. What, if anything, replaced it?
4. How does the DeepSight Atlas deployment pipeline work for new applications -- what is the process from code commit to production?
5. What are the specific "infrastructure pieces" Srinivas wants built for reuse and agentic infrastructure beyond the immediate CI/CD requirements?

---

## 6. Commitment Status Summary

| Category | Total | Complete | In Progress | Pending |
|---|---|---|---|---|
| Cisco commitments | 12 | 0 | 3 | 9 |
| BayOne commitments | 7 | 0 | 3 | 4 |
| Action items | 18 | 0 | 3 | 15 |

**Key dependency chain:** NDA signature (action item 1) unblocks DeepSight Atlas recording (action item 3), which unblocks platform understanding (action item 4). In parallel, GitHub training (action item 2) unblocks repository access, and ADS provisioning (action item 5) unblocks code access. The CI/CD app launch (action item 10) is on Cisco's side and independent of BayOne's onboarding. All paths converge at the 2-week follow-up meeting (action item 13).
