# 07 — Stakeholders and Organization

**Purpose of this document:** Who everyone is, what their role is, where decisions come from, and the dynamics the execution session needs to be aware of. Also contains the speech-to-text name resolutions — the transcripts have garbled several names consistently and the attendee screenshots from the 2026-04-06 meeting are the authoritative source.

---

## 1. Cisco Leadership

### Guhan

- **Title:** Senior engineering leader. Exact title not specified in the transcripts.
- **Role:** Primary decision-maker for this engagement. Owns the product direction for EPNM and EMS. Leads the Provider Connectivity area (per Venkat's positioning notes). Frames scope and sets strategic direction.
- **Working style:** Action-oriented, time-constrained. Frequent international travel (India, Sweden, Israel). At the 2026-03-25 scope reframe meeting had a hard stop at 11:25 and explicitly handed off to Selva: "Salva can continue." Was not present at the 2026-04-06 technical walkthrough.
- **Key decisions owned:** The engagement scope framing. He introduced the fork-the-UI sentence: "It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel." He ruled out backend rewrite. He set the success test: "Final test will be to show the same thing comes up everywhere."
- **For the execution session:** Unlikely to interact with Guhan directly. Scope changes that materially affect the commitments he made in the Set 03 reframe meeting need to go through Selva first, who will escalate if necessary.

### Venkat

- **Title:** Senior leader above Guhan.
- **Role:** Executive sponsor. Explores whether AI-accelerated work fits his broader industry narrative. Advocates internally for "100 percent AI-generated code" as a differentiation story. Exploring whether this POC could deliver within a July or August 2026 timeframe (noted as exploratory, not a hard deadline).
- **Funding context:** The engagement is being funded through NRE (Non-Recurring Engineering) funding in the Provider Connectivity area.
- **For the execution session:** Venkat does not interact directly with the POC execution. His visibility comes through Guhan and Selva. The execution session should be aware that the POC is under executive sponsorship by a leader who views it as a flagship use case.

---

## 2. Cisco Operational Counterparts

### Selva Subramanian (selva@cisco.com)

- **Title:** Engineering / product lead.
- **Role:** Operational counterpart for BayOne. Runs day-to-day coordination, scheduling, scope calls, access coordination, and communication between BayOne and the Cisco engineering team.
- **Location:** US-based.
- **Key ownership:** Introduced the classic view toggle concept. Created the WebEx team space. Coordinated the 2026-04-06 walkthrough. Is the first escalation point when something needs a decision or a scope question needs answering.
- **For the execution session:** Selva is the primary contact for anything substantive. Route scope questions, access escalations, and substantive progress checkpoints to Selva. Minor technical questions should go to the relevant tech lead before Selva.

### Praveen Kumar Vangala (pvangala@cisco.com)

- **Title:** Team lead / manager for the engineering team.
- **Role:** Manages the India-based tech leads. Organized the 2026-04-06 walkthrough meeting. Describes the test lifecycle and the test-suite landscape. Sets the operational frame for team interactions.
- **Location:** India-based.
- **Name resolution:** Praveen is likely the person referred to phonetically as "Varel" in the earlier transcripts from Sets 01 through 03. Vangala → Varel is a plausible speech-to-text corruption. Some Set 07 transcripts also render "Praveen" as "Pradeep"; the screenshots confirm Praveen Kumar Vangala.
- **For the execution session:** Praveen is the operational lead on the India side. Coordinate through him for team availability and tech lead engagement.

---

## 3. Cisco Tech Leads (India-based unless noted)

### Akhil Francis (akfranci@cisco.com)

- **Role:** Tech lead. Led the live product walkthrough (Inventory, Device Details, Chassis View, Device 360). Explained the repository structure for both EPNM and EMS. Clarified the shell app architecture (Infra UI, Common UI, EMS UI).
- **Location:** India-based.
- **Key technical contributions:** Most detailed presenter in Set 07. Articulated the default-classic-view-on-login requirement. Committed to emailing code pointers and repository links after the walkthrough.
- **For the execution session:** Akhil is the primary contact for Inventory-related questions and for repository-layout or code-location questions. He owes the email with code pointers — check for it, and follow up if not received.

### Ramesh Dhashnamoorthy (dramesh@cisco.com)

- **Role:** Tech lead or architect. Asked the most rigorous questions about AI tool compliance and QA approach in the 2026-04-06 walkthrough.
- **Location:** US-based. The only India-team member actually in the US, which makes him the suggested contact for VM provisioning setup (Ramkrishna pointed at Ramesh as the easier US route for environment setup).
- **Name resolution:** Transcripts render him as "Adamesh" or "Ramay" in some places. Screenshots confirm Ramesh Dhashnamoorthy.
- **Sentiment:** Thorough, security-conscious, QA-focused. The most probing voice in the walkthrough on compliance and testing.
- **For the execution session:** Ramesh is the best contact for AD group enrollment and VM provisioning follow-up. He is also a useful sounding board for QA approach questions because of his detailed engagement in that thread.

### Ramkrishna Galla (ragalla@cisco.com)

- **Role:** Tech lead. Provided the clearest architectural overview of EPNM data flow: SNMP/CLI polling → Oracle → application → UI. Explained Oracle-to-Postgres migration context. Noted Go services on the device management side. Stated the "at least 80 percent" backend reimplementation figure.
- **Location:** India-based.
- **Name resolution:** Transcripts render him as "Rama," "Srama," or "Drama" (speech-to-text mangling of his first name). Screenshots confirm Ramkrishna Galla. He is the senior technical voice on the architectural explanation.
- **For the execution session:** Ramkrishna is the best contact for architectural questions about data flow, backend boundaries, and the overall product structure.

### Aadit Vaidyanathan (aadvaidy@cisco.com)

- **Role:** Tech lead. Will help with AD group access setup. Will help create the WebEx team space.
- **Location:** India-based.
- **Name resolution:** Transcripts sometimes render him as "Adith" or "Adit" or "Adamesh." Screenshots confirm Aadit Vaidyanathan.
- **For the execution session:** Aadit is an operational contact for access and team-space setup. Follow-up on AD group provisioning can flow through him.

### Jenis Dharmadurai (jdharmad@cisco.com)

- **Role:** Tech lead. Contributed to the fault management walkthrough. Confirmed correlated alarms and the clear-alarm action. Raised the concrete question about whether a replica of existing test cases would be built for the classic UI (Colin confirmed yes, deferred to the full engagement).
- **Location:** India-based.
- **Name resolution:** Transcripts render as "Janice." Screenshots confirm Jenis Dharmadurai. Appears to own the fault management backend ("Janice's backend" in the transcript).
- **For the execution session:** Jenis is the primary contact for Fault Management specifics.

### Senthilkumar Palaniyandi (spalaniy@cisco.com)

- **Role:** Tech lead. Accepted the 2026-04-06 meeting invite. Speaking role not distinguished in the transcript.
- **Location:** India-based.
- **Name resolution:** Transcripts render as "Santil." Screenshots confirm Senthilkumar Palaniyandi.
- **For the execution session:** Unclear specialty. Default routing for questions goes through Praveen or the tech lead whose area the question covers.

---

## 4. Cisco People Referenced But Not Present

### Anand Singh (Cisco)

- **Role:** Connected to the NX-OS CI/CD project. Colin referenced working with "Srinivas Pita and Anand Singh" on that engagement.
- **Relevance to EPNM-EMS:** Provides the operational precedent for AI-compliance posture. Not involved in the EPNM-EMS POC directly.

### Srinivas Pita (Cisco)

- **Role:** CICD (NX-OS) project counterpart. Colin cited him as the precedent for AI compliance. Colin's action item 11 in the Set 07 list: ask Srinivas for permission to share the NX-OS CI/CD testing approach with the EPNM team.

### Meryl (Cisco)

- **Role:** Leads a separate agentic AI platform team based in New York.
- **Relevance:** Referenced in Set 01 only. Not involved in this engagement.

### Mecha (phonetic)

- **Role:** The original contact who suggested BayOne could help. Referenced in Set 01 only. Not present at any meeting.

### Cerny (phonetic)

- **Role:** Unclear. Referenced once in Set 03 in an informal end-of-meeting comment about another team working in this area. Never resolved.

---

## 5. BayOne Team

### Colin Moore (colmoore@cisco.com)

- **Title:** Director of AI, BayOne Solutions.
- **Role:** Technical lead. Running the POC solo. Leading the engagement end-to-end from the BayOne side.
- **Location:** US East Coast, EST time zone.
- **Status:** Fully onboarded with Cisco hardware, Cisco ID, and applicable Cisco trainings. Has concurrent experience on the Cisco NX-OS CI/CD engagement (working with Srinivas Pita and Anand Singh) which established the AI-compliance posture model for this POC.
- **For the execution session:** Colin is the orchestrator. Scope changes, material decisions, external escalations, and anything that could contradict a Cisco-side commitment should be surfaced to Colin before acting. Small technical decisions inside the scope Colin has already committed to (implementation approach on a given screen, library choice within the approved set, component naming) are the execution session's call.

### Neha Malhotra (nehamalh@cisco.com)

- **Title:** Business operations / engagement management, BayOne.
- **Role:** Day-to-day operational partner to Colin. First appearance in Set 07. "Will be working very closely with him."
- **For the execution session:** Neha coordinates logistics — team space, invites, meeting scheduling. If Colin is unavailable and something operational needs to move, Neha is the route. Rahul characterized the Neha-Colin pairing as accountability and expediting for Colin's responsiveness: "Sometimes he gets a little backlog and he just needs a little tiny internal nudge."

### Rahul Bobbili (rabobbil@cisco.com)

- **Title:** President, BayOne Solutions.
- **Role:** Executive support. Back-end business relationship. Present at the 2026-03-25 and 2026-04-06 meetings but minimal speaking role in either.
- **For the execution session:** Rahul is Colin's escalation route above Colin himself. The execution session does not interact with Rahul directly in normal course.

### Zahra Syed (zahsyed@cisco.com)

- **Title:** Director, Strategic Accounts, BayOne.
- **Role:** Account management. Describes the BayOne team structure on calls: "Colin will be leading the entire engagement end-to-end. Neha will be working very closely with him and Rahul and I will be on the back end."
- **Location:** US West Coast, PST time zone.
- **For the execution session:** Zahra is the business-side account contact. Not involved in technical execution.

---

## 6. Speech-to-Text Name Resolutions (authoritative)

The transcripts have consistently garbled several names. The 2026-04-06 meeting invite screenshots (`source/selva_and_team_4-6-2026__1.png` and `__2.png`) are the authoritative source. Use these corrections when reading any transcript.

| Transcript rendering | Correct name | Confidence |
|---|---|---|
| "Varel" / "Pradeep" / "Praveen" (inconsistent) | **Praveen Kumar Vangala** | High (confirmed by screenshot) |
| "Janice" | **Jenis Dharmadurai** | High |
| "Santil" | **Senthilkumar Palaniyandi** | High |
| "Rama" / "Srama" / "Drama" | **Ramkrishna Galla** | High |
| "Adamesh" / "Ramay" | **Ramesh Dhashnamoorthy** | High |
| "Adith" / "Adit" | **Aadit Vaidyanathan** | High |
| "Suva" / "Sura Vashwa" / "Sarva" | **Selva Subramanian** | High |
| "Anansing" | **Anand Singh** | High |
| "Zara" | **Zahra Syed** | High |
| "ECLI" | **CLI** (command-line interface) | High |
| "Doge" / "Doze" | **Dojo** (JavaScript framework) | High |
| "PI framework" | **Prime framework** (Cisco Prime Infrastructure framework) | High |
| "CMS UI" | **EMS UI** (the EMS frontend repository) | High |
| "VPN theme" / "VPN UI" / "PMM" | **EPNM theme / EPNM UI** | High |
| "fold" / "fold management" | **Fault management** | High |
| "crossword UI" / "Crosswork" | **Crosswork UI** (Cisco Crosswork Network Controller) | High |
| "cloud code" | **Claude Code** | High |
| "land graph" | **LangGraph** | High |
| "deep site" | **DeepSite** (or **DeepSeek** — phonetics unclear, both are real Cisco-context AI tools) | Medium |
| "back up" (in backend context) | **backend** | High |
| "EPA wireless repo" | likely **EPNM wireless repo** or the EPNM fault/alarm repo | Medium |
| "echos" (in context of "different echos for testing") | likely **angles** or **vectors** (different perspectives) | Medium |

---

## 7. Where Decisions Come From

Decision ownership:

| Area | Primary owner |
|---|---|
| Scope commitments (what the POC is) | Guhan, with Selva as the operational interpreter |
| Scope changes or expansion | Selva, escalating to Guhan if material |
| Operational logistics (meetings, access, team space) | Selva, Praveen, with Aadit or Akhil on specifics |
| Technical scope within the classic view for a given screen | Akhil (Inventory), Jenis (Fault Management), Ramkrishna (cross-cutting architecture) |
| AI compliance and tooling boundary | Ramesh raised, Colin enforces |
| BayOne-side commitments | Colin |
| BayOne operational execution | Colin and Neha |
| Customer-facing narrative | Cisco (Guhan, Venkat); BayOne does not communicate externally |

### What the execution session should decide without escalation

- Internal implementation details: component naming, file organization within the proposed folder structure, minor library choices within the approved tool set, Angular-idiomatic code patterns.
- Application of the conversion patterns research to specific screens.
- Internal unit test design.
- Playwright agent behavior and test implementation.

### What the execution session should raise before acting

- Anything that contradicts Guhan's scope commitments (see `03_objectives_and_scope.md` and `04_strategic_approach.md`).
- Any backend change beyond narrow API-level touchup.
- Introduction of any new tool, library, or service beyond the approved Cisco-issued Claude Code and local LangGraph.
- Any AD group request or VM request that was not part of the Set 07 action item list.
- Any customer-facing artifact (customers never see the AI; Colin enforces).
- The code-organization proposal (subfolder in EMS UI repo versus new repo) — Colin owes this to Akhil with a review loop.

---

## 8. Time Zones and Communication Cadence

### Geographic distribution

| Participant(s) | Time Zone |
|---|---|
| Akhil, Praveen, Aadit, Jenis, Ramkrishna, Senthilkumar | IST (UTC+5:30) |
| Colin Moore | EST (UTC-5) |
| Selva Subramanian | US (specific zone not stated in transcripts) |
| Ramesh Dhashnamoorthy | US (likely PST) |
| Zahra Syed | PST (UTC-8) |
| Neha Malhotra, Rahul Bobbili | US (unspecified) |

### Overlap window

IST and EST overlap roughly 8:00 AM to 12:30 PM EST (6:30 PM to 11:00 PM IST). This narrow window constrains synchronous meetings. Asynchronous coordination in the WebEx team space is the default; synchronous calls are scheduled into the overlap when they are needed.

### Channels

- **WebEx team space** — the primary async channel. Per Set 07, Selva, Aadit, and Praveen own creation. Neha coordinates the BayOne-side invite list.
- **Email** — Akhil committed to emailing code pointers and repo links after the Set 07 walkthrough.
- **Recurring sync meeting** — approximately 12 participants (the full Set 07 attendee group). Cadence not finalized as of the Set 07 meeting. Action item for Selva or Aadit to set up.

### Etiquette

- The India team is on a critical release path. Respect bandwidth constraints. Default to async.
- Code exploration and agent-driven analysis should be the first move for a question. Meetings are for decisions, clarifications, or things the code genuinely does not answer.
- Colin (or the execution session via Colin) is expected to batch questions and engage the team efficiently, not nibble at individual questions.
- Selva and Neha act as accountability for responsiveness on the BayOne side. If the execution session senses a delay in its own response to a Cisco question, loop Neha or Selva in.
