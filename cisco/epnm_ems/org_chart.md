# Org Chart — Cisco EPNM-to-EMS

**Last Updated:** 2026-04-24

---

## Cisco — Leadership

### Guhan (Cisco)
- **Title:** Senior engineering leader (exact title still TBD)
- **Role:** Primary decision-maker. Owns the product direction for EPNM/EMS. Not present at Set 07. Joined Set 09 late (back-to-back with Zahra earlier the same day).
- **Key context:** Reframed the project scope to classic view toggle in Set 03. Delegates operational coordination to Selva.
- **Engagement style (Set 09):** Joins late, contributes densely. Reads the work product, not just slides ("now we can see something running, then just not slides"). Frames technical asks collaboratively but treats them as gates. Thinks in customer-commitment / product-management terms — sees the work as authorization input for what Cisco PM can promise customers.
- **Active asks (Set 09):**
  1. Memory and load review with EMS team before the demo (gating).
  2. Confirmation that DPM (Device Performance Management) is captured in the gap analysis as a future-implementation item.
  3. Code review BEFORE demo, with reasoning that the team needs time to surface questions and engage.
  4. Delivery-package mechanism explained (answered: simple UI toggle, parallel Angular packages).
- **Quote of strategic significance:** "Based on this, we are going to go to the product management and say, hey, we got this covered. You can go promise the customers that they will get this functionality." This is the engagement's commercial unlock — the artifact's purpose is to authorize customer commitments.

### Venkat (Cisco)
- **Title:** Senior leader, above Guhan
- **Role:** Executive sponsor with visibility into this project
- **Key context:** Exploring whether the work could fit into the July release (not a hard push). Advocates for AI-generated code. Funding source: NRE funding in Guhan's area (Provider Connectivity). Colin referenced Venkat's July/August interest in Set 07.

### Selva Subramanian (selva@cisco.com)
- **Title:** Engineering/product lead
- **Role:** Operational lead for the engagement. Coordinates between BayOne and the engineering team. Ran the Set 07 meeting intro. Held Set 09 open during the first half before Guhan arrived.
- **Key context:** US-based. Introduced the toggle/classic view concept. Engineering team reports to him (via Praveen). Created the communication infrastructure (WebEx space).
- **Engagement style (Set 09):** Warmth anchor of the Cisco-BayOne relationship. Validates technical assumptions on the record (e.g., asked Colin to confirm the toggle hits the same backend, with Guhan present). Acts as buffer when Guhan is absent. Operationally hands-on — owns demo logistics, code-review scheduling, time-zone coordination. Mixes personal banter and substance comfortably.
- **Active commitments (Set 09):**
  - Talk to the India team about the code review and brief them on the new sequencing.
  - Coordinate the demo time-zone window (PST morning / EST midday / IST evening).
  - Tuesday touch-base with Colin to lock the demo slot.
- **Quote of behavioral significance:** "Is it good or is it great? Just trying to pulse check." — He uses pulse-check questions in front of Guhan as a barometer for the relationship. Answer with substance.

---

## Cisco — Engineering Team (Set 07, April 6)

### Praveen Kumar Vangala (pvangala@cisco.com)
- **Title:** Team lead / manager
- **Role:** Organized the April 6 walkthrough meeting. Manages the tech leads. Asked Colin about product exposure level. Described the full test lifecycle.
- **Key context:** India-based. Likely the "Varel" referenced in earlier sets (phonetic match: Vangala/Varel). Tech leads report to him.

### Akhil Francis (akfranci@cisco.com)
- **Title:** Tech lead
- **Role:** Led the live EPNM product demo (inventory screens). Explained the repository structure for both products. Described the shell app architecture and design system.
- **Key context:** India-based. Most technically detailed presenter in Set 07.

### Ramesh Dhashnamoorthy (dramesh@cisco.com)
- **Title:** Tech lead / architect
- **Role:** Asked the most probing questions about AI compliance and QA approach. Security-conscious, detail-oriented.
- **Key context:** **US-based** (only exception from the India team). Will help with VM setup. Asked about Claude Code, LangGraph, and data-driven testing.

### Ramkrishna Galla (ragalla@cisco.com) — "Rama" / "Srama"
- **Title:** Tech lead
- **Role:** Provided the architectural overview of EPNM data flow (SNMP/CLI -> Oracle -> app). Confirmed Postgres in EMS. Noted Go services on the device management backend.
- **Key context:** India-based.

### Aadit Vaidyanathan (aadvaidy@cisco.com)
- **Title:** Tech lead
- **Role:** Will help with AD group access setup.
- **Key context:** India-based.

### Jenis Dharmadurai (jdharmad@cisco.com)
- **Title:** Tech lead
- **Role:** Contributed to the fault management walkthrough (correlated alarms).
- **Key context:** India-based.

### Senthilkumar Palaniyandi (spalaniy@cisco.com)
- **Title:** Tech lead
- **Role:** Accepted the meeting invite. Speaking role not clearly distinguished in transcript.
- **Key context:** India-based.

---

## Cisco — Other Referenced People

### Anand (Cisco)
- **Role:** Connected to the CICD project. Colin referenced working with "Srinivas Pita and Anand Singh" in Set 07.

### Srinivas Pita (Cisco)
- **Role:** CICD project counterpart. Colin referenced the CICD engagement as precedent for AI compliance.

### Meryl (Cisco)
- **Role:** Leads the agentic AI platform team (separate engagement track). Based in New York.

### Mecha (phonetic)
- **Role:** Initial contact who suggested BayOne could help. Referenced in Set 01 only.

---

## BayOne Solutions

### Colin Moore (colmoore@cisco.com)
- **Title:** Director of AI
- **Role:** Technical lead. Running the POC solo. Leading the engagement end-to-end.
- **Key context:** Fully onboarded with Cisco laptop, ID, and trainings. EST time zone. Will do both UI and backend work for the POC. Committed to strict Cisco AI compliance.

### Neha Malhotra (nehamalh@cisco.com)
- **Title:** Business operations / engagement management
- **Role:** Day-to-day operational contact alongside Colin. "Will be working very closely with him."
- **Key context:** First appearance in Set 07.

### Rahul Bobbili (rabobbil@cisco.com)
- **Title:** President, BayOne Solutions
- **Role:** Executive support. "Back end" business relationship. Internal accountability for Colin's responsiveness.
- **Key context:** Assured the team: "Sometimes he gets a little backlog and he just needs a little tiny internal nudge."

### Zahra Syed (zahsyed@cisco.com)
- **Title:** Director, Strategic Accounts
- **Role:** Account management, business side. PST time zone.
- **Key context:** Described the team structure: "Colin will be leading the entire engagement end-to-end. Neha will be working very closely with him and Rahul and I will be on the back end."

---

## Notes

- Praveen Kumar Vangala is likely the "Varel" referenced phonetically in Sets 01-03 (Vangala -> Varel is a plausible speech-to-text error).
- Engineering team is almost entirely India-based (IST), except Ramesh (US) and Selva (US).
- Time zone overlap for Colin (EST) and India team (IST) is approximately 4.5 hours.
- "Cerny" from Set 03 remains unresolved.
- Set 09 transcription artifacts: "Anu" (no such attendee — confirmed), "Aya" = Neha, "Zara" = Zahra.
- Set 09 attendees confirmed: Guhan, Selva (Cisco) + Colin, Neha, Zahra (BayOne).
- Transcript quality continues to be poor (speech-to-text).
