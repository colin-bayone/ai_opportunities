# Agent 08: Source Ground-Truth Pass

Source files read in full:

1. /home/cmoore/programming/ai_opportunities/cisco/epnm_ems/source/ceo_rahul_call_2026-03-30_formatted.txt
2. /home/cmoore/programming/ai_opportunities/cisco/epnm_ems/source/venkat_notes_2026-03-30.txt
3. /home/cmoore/programming/ai_opportunities/cisco/epnm_ems/source/selva_and_team_4-6-2026_formatted.txt
4. /home/cmoore/programming/ai_opportunities/cisco/epnm_ems/source/selva_and_team_4-6-2026__1.png
5. /home/cmoore/programming/ai_opportunities/cisco/epnm_ems/source/selva_and_team_4-6-2026__2.png

---

## 1. Screenshot 1 Description

The image is a Webex meeting invite / participant panel, captured as a screenshot from what appears to be a calendar client (likely Webex or a mail client overlay). Visible content:

- Meeting title: "EPNM Features Walkthrough"
- Date/time: "Monday, April 6, 2026" and "12:00 PM - 1:00 PM"
- A Webex meeting URL is partially visible: `https://cisco.webex.com/cisco.php?MTID=m3d4967df256a1e4394a5464fe35eef...` (truncated). The domain is `cisco.webex.com`.
- Two action buttons: "Join" and "Add a room"
- Participant count: "Participants (12)" with a "Copy" button
- Participant list visible in this screenshot (top portion of the list):
  1. Praveen Kumar Vangala (labeled "Organizer")
  2. Colin Moore
  3. Aadit Vaidyanathan (Accepted)
  4. Akhil Francis (Accepted)
  5. Jenis Dharmadurai (Waiting for response)
  6. Neha Malhotra (Waiting for response)
  7. Rahul Bobbili (Accepted)
  8. Ramesh Dhashnamoorthy (Accepted) — partially visible / bottom of visible list
- Footer: "You accepted." with an "Edit response" link

Key ground-truth detail: the organizer's full name is confirmed as **Praveen Kumar Vangala** (not "Varel" or any of the phonetic mangling that appears in the transcripts).

## 2. Screenshot 2 Description

Same meeting invite panel, scrolled further down to show additional participants. Visible content:

- Same header: "EPNM Features Walkthrough", Monday, April 6, 2026, 12:00 PM - 1:00 PM, same Webex URL
- "Join" and "Add a room" buttons
- Participant list visible in this screenshot (lower portion):
  1. Jenis Dharmadurai (Waiting for response)
  2. Neha Malhotra (Waiting for response)
  3. Rahul Bobbili (Accepted)
  4. Ramesh Dhashnamoorthy (Accepted)
  5. Ramkrishna Galla (Accepted)
  6. Selva Subramanian (highlighted / selected, Accepted)
  7. Senthilkumar Palaniyandi (Accepted)
  8. Zahra Syed (Accepted)
- Footer again: "You accepted." with "Edit response"

Combined attendee list (all 12) confirmed across both screenshots:

1. Praveen Kumar Vangala (Organizer)
2. Colin Moore
3. Aadit Vaidyanathan
4. Akhil Francis
5. Jenis Dharmadurai
6. Neha Malhotra
7. Rahul Bobbili
8. Ramesh Dhashnamoorthy
9. Ramkrishna Galla
10. Selva Subramanian
11. Senthilkumar Palaniyandi
12. Zahra Syed

Note: The transcript mentions a "Santil" and a "Janice" and a "Rama" / "Srama" / "Drama". Cross-referencing against this authoritative attendee list:

- "Janice" in the transcript = Jenis Dharmadurai
- "Santil" in the transcript = Senthilkumar Palaniyandi
- "Rama" / "Srama" / "Drama" in the transcript = Ramkrishna Galla (likely; the transcript garbles his name multiple ways)
- "Adamesh" / "Ramay" / "Ramay" in the transcript = Ramesh Dhashnamoorthy (the one person in the US)
- "Adith" in the transcript = Aadit Vaidyanathan
- "Akhil" in the transcript = Akhil Francis (confirmed directly)
- "Rahul Bobbili" is distinct from "Rahul" (BayOne CEO) who is also mentioned in the meeting context

---

## 3. Ground-Truth Additions from Rahul Call Transcript (2026-03-30)

This is mostly an internal BayOne commercial call between Colin and Rahul (CEO). Filtering hard for technical / scope content only:

- No substantive technical detail about EPNM, EMS, or the POC scope appears in this transcript. The call is commercial (pricing strategy, change request clauses, risk reserve, procurement protection) and operational (meeting load, talent / hiring for a manager named Priya whose mother is ill, Suva/Selva scheduling too many meetings).
- One adjacent technical-ish remark: Rahul suggests that for the Money / Sephora engagement, the POC resulted in a per-conversion time of **"two minutes, with 97% plus accuracy on their production environment"** and "6,000 conversions" needed. This is Sephora/Money, not EPNM/EMS; flagging only because it is the only concrete technical metric in the call and could be confused with EPNM work if skimmed.
- No scope-relevant ground-truth to add for EPNM/EMS POC from this transcript.

## 4. Ground-Truth Additions from Venkat Notes (2026-03-30)

Stripping positioning and commercial advice. Only items that could affect POC scope or technical framing:

- Venkat explicitly named **"Provider Connectivity area (Guhan's team)"** as a demand area. This confirms that Guhan leads the Provider Connectivity team within the CNC / EMS organization (useful for attribution and for understanding who "Guhan" is in the April 6 transcript).
- Funding source mentioned: **"NRE funding"** (Non-Recurring Engineering). This is a Cisco funding mechanism the engagement may be tapped from; relevant to the execution session only insofar as it explains why the POC exists in a funded state.
- Venkat's example of the canonical use case was explicitly "Legacy product EPNM, Migrating UI from EPNM -> CNC platform, AI generating code for modernization." This confirms the framing of the POC as UI migration from EPNM to CNC (of which EMS is a component).
- No additional technical detail beyond that.

## 5. Ground-Truth Additions from Selva Team Transcript (April 6)

This is the high-value source. Going through carefully for details that deep-dive summaries may have compressed.

### 5a. Attendee / introduction details

- Pradeep (or Praveen) gives the intro. The transcript text alternates between "Praveen" and "Pradeep" but the meeting screenshots confirm the organizer is **Praveen Kumar Vangala** — "Pradeep" in the transcript is a speech-to-text error.
- Selva explicitly says "this team here except me and Ramesh, everyone is in the India time zone." So **Ramesh Dhashnamoorthy is the one Cisco team member in the US**, alongside Selva (who is also US-based). The rest of Praveen's team (Aadit, Akhil, Jenis, Ramkrishna, Senthilkumar, plus Rahul Bobbili) are all in India.
- Colin confirmed he is in **EST (Eastern time)**.
- BayOne-side roles (explicitly stated by Selva on the call): "Colin will be leading the entire engagement end-to-end. Neha will be working very closely with him and Rahul and I will be on the back end, but Colin and Neha will be putting in contact." Zara and Neha are the BayOne business-side contacts; Rahul (CEO) and Selva on the back end.

### 5b. Technical / architecture details from the walkthrough

Some items that may be lighter or missing in the deep-dives:

- **EPNM UI stack**: "EPNM is written in Dojo legacy" — specifically "Dojo based framework" with a blue-and-white theme. The core framework repo is described as "Doge is returning the PI framework" (speech-to-text artifact; likely means "Dojo-based Prime framework" or the EPNM "Prime Infrastructure" core framework). There is also a separate "wireless framework" / "wireless repos" that contains part of the Prime UI and framework UI, Dojo based.
- **EPNM repository structure** (explicitly listed by Praveen/Akhil):
  - Core framework repo (Dojo Prime framework)
  - Wireless framework / wireless repos (Prime UI + framework UI, Dojo-based)
  - Inventory screens -> "assembly repo" (plus other repos containing inventory-related things)
  - Chassis View -> its own "ChassisView repo"
  - Fault management -> "EPA wireless repo" and "fold" on the backend (speech-to-text; likely "fault" backend)
  - "Assembly is in the UI side" and "EMS assurance is also backend side"
  - A complete repository list link was provided in the Confluence page / email invite (Colin complimented the organization of the Confluence page)
- **CNC / EMS UI stack**:
  - Angular (specifically **"latest Angular 21 is used here"**) — note Angular 21 is unusual if the meeting date (April 2026) is taken at face value; this is what Praveen/Akhil stated.
  - Design system: **"magnetic design system"**, also referred to as **"Harbor and magnetic design system"** (the exact phrasing: "it's a design system called Harbor and magnetic design system you're using"). Likely this means Harbor is the component library and Magnetic is the broader Cisco design system (or vice-versa). Flag as uncertain.
  - Shell app architecture: The header, top menu, and other infrastructure UI components come from an **"Infra UI repository"** (the "shell app").
  - **"Common UI"** repository holds shared components (cards, tables — "these are called common components").
  - **"EMS UI"** repository is the third repo and contains EMS-specific pages (software image management, etc.). Praveen said: "Mostly I think you have to work on this CMS UI" (should read "EMS UI" — "CMS" is a speech-to-text error).
  - Backend: "mostly a Spring Boot, yes" but Ramkrishna clarified: "It depends, right? So, somewhere... Yeah, based application is being used. There are areas, at least on the device management side, and there are **Go services running at the back end**." So the new stack is a mix of Spring Boot (Java) and Go (for device management areas specifically).
  - Database migration: **Oracle (EPNM) -> PostgreSQL (CNC/EMS)**. "By the way, there's no Oracle in the new product. There's Postgres in the new product. We've gotten rid of Oracle dependency." (This is in the deep-dives but worth reconfirming.)
- **Data flow**: The application "in most of the cases... won't directly go to the rest [device]. It reads from the database correct." So both EPNM and EMS read from the DB, not directly from devices (SNMP / CLI collection happens separately, persists to DB, and the UI reads from DB).
- **Backend reuse vs reimplementation**: Ramkrishna's quote: "So, it's not exactly migrated in a way. Things got reimplemented. Some of it, at least 80% of it, is there in the other product as in the newer product." This is a ~80% figure for backend functional coverage in EMS vs EPNM. The remaining 10-20% gap is acknowledged and will require a gap analysis (Colin's commitment).
- **Asset images / device pictures**: Colin asked specifically about "pictures, images for the actual network devices" (device chassis images etc.) — whether they were stored in Oracle natively. Answer: "For the new UI, it is part of the application, not stored in Oracle and all." So device images are bundled into the application in the new EMS, not DB-hosted.
- **Inventory screen details** observed during the live walkthrough:
  - Landing screen is "dashboard"
  - Left nav: Inventory -> Network Device -> Device Management -> Network Devices
  - Filters: "filtered by all devices. You can filter by device type and locations"
  - Add Device: IP address + step forward (SNMP, Telnet, HTTP, HTTPS, etc.)
  - Bulk Import: downloadable sample CSV
  - Table actions: edit, delete
  - Admin states: maintain state, managed state, schedule maintenance state, schedule managed state, disable the handler inventory
  - Additional filtering: by group and sites
  - Export actions: export device, new box certificate, OEM commands
  - Device 360 pop-up: accessed via info icon; tabs include alarms, modules, interfaces; interface tab can launch another 360 view (nested); tabs for location, recent changes; actions include "device console"
  - Device Details (hyperlinked device name): left side shows "chassis view"; other left-menu sections include system summary view, device details, chassis view, and "enrollment" / configurations
- **Fault Management screen details**:
  - Navigation: Monitor -> Alarms and Events
  - Columns + table actions: quick filter and advance filter
  - Correlated alarms and 360 view
  - Clear alarms action
  - "Different pop-up most recent events"
  - "All events eight hours / past eight hours" (default time range)
  - Secondary events table on "events page"
  - Syslogs section
  - **Every row has expandable data as information** (general information, etc.) — this is a UI behavior detail worth preserving for the Angular rebuild.
- **Scope split**:
  - Part 1: Inventory device / network devices + Device 360 + Device Details + Chassis View + Interface 360
  - Part 2: Fault management (alarms, events, syslogs, correlated alarms)
  - Selva explicit quote: "whatever we covered earlier is part one of the POC, like the inventory device, like that's target for the POC. This is part two, and this is a different area."
- **Toggle behavior**: Default on login to CNC UI should be the **EPNM theme** (classic view default), with the toggle switching to the "current" (Magnetic/Harbor) EMS UI. Explicit quote: "the default, once I log into the crossword UI, the default will be showing the VPN theme" (VPN = EPNM, speech-to-text error). "basically the left menu and ... the other area should be crossword EPNM (?) current field should be shown instead of magnetic."
- **Code placement**: Praveen offered flexibility — "Maybe you can create a folder [in EMS UI repo] and for now you can add it out there or you can create a separate repository also. It's up to you all. You can think about it and come up with your plan, then we can review it." But Selva constrained it: "it has to be part of the new EMS build."

### 5c. Access / environment / operational

- **Access request**: Controlled through "my groups" (AD groups). Akhil needs to activate Colin's ID into "few groups we have to enable this access." Ramesh (US-based) was flagged as the best person to help Colin get onboarded ("as in the US, probably it's easy for him to get a setup from this... I can walk through them and I can just call them and connect with them").
- **Teams / comms**: A Webex "team space" already exists for the POC. Selva told Neha to "add the entire B1 account management team... and then the folks from your team" to that space.
- **VM / hardware**: Colin does not currently have a VM for this project. He has a VM for the NX-OS project with Srinivas Pita / Anand Singh (Colin called him "Anansing" in the transcript; likely "Anand Singh"). The EPNM/CNC engagement will need its own VM. Ramkrishna clarified development setup is "mostly on the EMS" side with "EPNM mostly for reading" (read-only access to an EPNM system), read-only access to a CNC system, then patching when new code is ready.
- **AI compliance** (important for execution session):
  - Ramkrishna Galla (likely) raised the AI-tools compliance question explicitly.
  - Colin's committed tool stack for this POC:
    1. **Claude Code** (via "Cisco issued" / Cisco-authorized cloud access) for development
    2. **LangGraph** for deployment, running locally on a Cisco-issued laptop
  - No external or third-party cloud-based tools beyond what Cisco provides.
  - All work on Cisco hardware, Cisco-issued accounts.
  - Colin explicitly referenced the precedent of the NX-OS CI/CD pipeline work with Srinivas Pita and Anand Singh as the model for compliance.
  - DeepSite was mentioned as another tool Colin has helped with inside Cisco — so the team is already familiar with Colin's AI compliance posture.
  - No library or software installs without pre-approval; Colin is "the master gatekeeper."
- **Team size**:
  - POC: Colin alone, both UI and backend. Explicit confirmation from Ramkrishna: "for the POC, you're going to work on both UI and backend, right? That's right. You are the one person working both UI and backend? Yes."
  - Full engagement: Colin plus approximately three other people.
  - Colin noted agentic flows parallelize well, so adding people genuinely adds throughput.
- **Timeline**: Selva / Colin reference Venkat's stated target of **"July or August"** for the full delivery, tight but feasible. POC first, then scale.

### 5d. QA / testing discussion (heavily discussed, worth preserving)

- Ramkrishna's framing of Cisco's existing test coverage: "functional testing, scale testing, end-to-end testing, UI testing, API testing, migration testing, across releases, upgrade, scale... probably customer-specific profiles... automation in place too for some of the regression so it goes to thousands and thousands of test cases right across different devices and functionality."
- Ramkrishna proposed two paths: (1) Colin demos + tech leads validate, possibly using code coverage + functional coverage tooling; (2) reuse existing regression suites.
- Colin committed to: Playwright-based agentic UI testing, dashboard-style result visibility, gap analysis for existing unit tests (especially for the new Angular stack where old UI tests cannot port directly).
- Jenis Dharmadurai noted the UI-based tests will not carry over and a "replica of the existing test case will be created" for the classic UI flow.
- For the POC specifically, Colin said: "for the testing, what we'll have to do for the POC, we won't do the full strut of it. We'll do enough that we can guarantee the existing equivalency." The deeper agentic gap analysis is deferred to the full engagement.

### 5e. Side remarks / interpersonal / dynamic context

- Colin apologized at the start for being late — had logged into the wrong Cisco account.
- There are **two Rahuls** in play: Rahul Bobbili (Cisco-side attendee) and Rahul (BayOne CEO, Colin's side, not on this call but referenced). Don't confuse them.
- Selva's closing compliment and meta-note: "The intent of adding Neha and I and our role to the call is Colin will make sure he gets back to you. Sometimes he gets a little backlog and he just needs a little tiny internal nudge. So we'll make sure that any questions you guys have, Neha and me will make sure that, you know, you get a response back." — This is a candid acknowledgement that Selva and Neha are acting as accountability / expediters for Colin's responsiveness. Useful context for the execution session: routine communication through the Webex team space is fine, but if there is a delay, Selva and Neha expect to be looped in.
- Colin gave an unprompted compliment on Cisco's Confluence page organization ("Usually we have to go digging for that. So actually my life is a lot easier because this is really organized"). This suggests the documentation handoff quality is high — the execution session should expect good Confluence documentation for repos, user guides, API docs, and recordings.
- Ramkrishna Galla had connectivity issues mid-call ("I was shifting the new home, right? The internet is not good") — minor.
- Colin showed warmth / relationship-building pattern throughout (thank-yous, compliments, easing the team's workload by committing to not require hand-holding). Useful tone cue for the execution session.
- Aadit was also referred to as "Adamesh" once and as "Adit" once by Selva — these are the same person (Aadit Vaidyanathan).

---

## 6. Transcription Errors and Likely Corrections

Consolidated list of speech-to-text errors in the three transcripts with best-guess corrections. Ranked by recurrence / impact.

| Appears as | Correction | Confidence |
|---|---|---|
| "Varel" / "Pradeep" / "Praveen" | **Praveen Kumar Vangala** (meeting organizer) | High (confirmed by screenshot) |
| "Janice" | **Jenis Dharmadurai** | High (confirmed by screenshot) |
| "Santil" | **Senthilkumar Palaniyandi** | High (confirmed by screenshot) |
| "Rama" / "Srama" / "Drama" | **Ramkrishna Galla** | High (confirmed by screenshot; he is the one doing most of the senior technical commentary) |
| "Adamesh" / "Ramay" | **Ramesh Dhashnamoorthy** (the US-based tech lead) | High |
| "Adit" / "Adith" | **Aadit Vaidyanathan** | High |
| "Suva" / "Sura Vashwa" / "Sarva" | **Selva Subramanian** | High |
| "Anansing" | **Anand Singh** (NX-OS project collaborator with Srinivas Pita) | High |
| "Srinivas Pita" | **Srinivas Pita** (likely correct; Cisco NX-OS CI/CD lead — referenced in other engagement materials) | High |
| "money" (as a client name in Rahul call) | **Mani** (a person's name referenced alongside "Mambir" on the Sephora engagement) | Medium — context is commercial not technical |
| "Zara" | **Zahra Syed** (BayOne business-side; sometimes spelled "Zahra" or "Zara") | High |
| "Soma" | Likely a BayOne back-office / HR person named "Soma" (candidate offer process) | Medium |
| "Priya" | Sick mother; possibly **Pooja** or similar — flagged as uncertain; unrelated to EPNM scope | Low relevance |
| "superisoni" / "the Prius person" | Likely a candidate name "the Prius person" from Priya's referral — unrelated to EPNM | Low relevance |
| "ECLI" | **CLI** (command-line interface; listed alongside SNMP as a credential / collection mechanism) | High |
| "Doge" / "Doze" / "dojo" | **Dojo** (JavaScript framework used by EPNM) | High |
| "PI framework" | **Prime framework** (Cisco Prime Infrastructure framework; EPNM is built on Prime) | High |
| "CMS UI" (when Praveen said "work on this CMS UI") | **EMS UI** (the EMS frontend repository) | High |
| "VPN theme" / "VPN UI" / "V PN" / "PMM" / "UA asset" | **EPNM theme / EPNM UI** (the classic look is the EPNM classic view) | High |
| "EPA wireless repo" (for fault management) | Likely **EPNM wireless repo** or the EPNM fault / alarm repo — flagged as uncertain | Medium |
| "fold" / "fold management" | **Fault management** | High |
| "ChassisView" (as "chassis view") | Correct; kept as-is | High |
| "crossword UI" / "Crosswork" | **Crosswork UI** (Cisco Crosswork Network Controller) | High |
| "cloud code" | **Claude Code** (Anthropic's CLI; this is literally what Colin uses) | High |
| "land graph" / "land graph" | **LangGraph** (the orchestration framework Colin uses for deployment) | High |
| "deep site" | **DeepSite** (Cisco-approved AI tool referenced as precedent) | Medium-High |
| "back end" pronunciations inconsistent | **backend** | High |
| "back up" (context: "new UI is talking to the back up") | **backend** | High |
| "Harbor and magnetic design system" | Confirmed Cisco uses **Magnetic** design system; **Harbor** is likely a separate Cisco component library or an alternative name — flagged as uncertain but both are real terms | Medium |
| "NRE funding" | **NRE funding** (Non-Recurring Engineering) — correct as heard | High |
| "Venkat" / "Venkatin" | **Venkat** (Cisco-side sponsor) | High |
| "Guhan" | **Guhan** (leads Provider Connectivity area per Venkat notes) | High |
| "Angular 21" | Likely correct as stated, though unusual; flag as said by Praveen/Akhil on-record | Report as stated |
| "B1" / "bay one" | **BayOne** (Colin's firm) | High |
| "EBI" (from Rahul call, "not our EBI") | Likely **EB-1** visa reference OR a Big-Four-style exec term; context commercial, not scope-relevant | Low relevance |
| "Zara" (in Rahul call) vs "Zahra Syed" (on invite) | Same person: **Zahra Syed** | High |
| "Sephora" vs "Money" (in Rahul call) | Separate clients mentioned casually; "Money" is likely a separate BayOne engagement nickname unrelated to EPNM scope | Low relevance |

Additional artifact: the transcript frequently renders "EPNM UI" as "PMM" or "UA" or other variants. Assume any short two/three letter token in technical context that does not obviously parse is either EPNM, EMS, CLI, API, or SNMP.

