# 07 - Meeting: People

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting — first meeting with Cisco engineering team)
**Pass:** People identification and dynamics

---

## Attendees

### Cisco (8 people)

#### Selva Subramanian (selva@cisco.com)
- **Role:** Engineering/product lead. Ran the meeting intro, provided high-level context, then handed off to his team.
- **Sentiment:** Organized, facilitative. Created the meeting infrastructure. Set the frame clearly: "We have an agreement on what areas to focus on for the POC."
- **Dynamics:** Introduced the team, gave context on the two products, then let his tech leads present. Stepped in for clarification on key points (backend stays, toggle approach).

#### Praveen Kumar Vangala (pvangala@cisco.com) — Meeting Organizer
- **Role:** Team lead or manager for the engineering team. Organized the meeting invite.
- **Key statements:** Asked Colin about his exposure to EPNM and CNC products. Set the stage: "Team wants to understand... how much you are exposed to both the products." Stated the team are "tech leads here who have worked on both the products."
- **Dynamics:** Ran the operational aspects of the meeting. Likely the equivalent of "Varel" from earlier sets or a different team lead under Selva.

#### Akhil Francis (akfranci@cisco.com)
- **Role:** Tech lead. Led the screen walkthrough of EPNM inventory and device management.
- **Key contributions:** Demonstrated the EPNM UI live (network devices, device 360, device details). Explained the repository structure for both EPNM and EMS. Clarified the theme toggle concept: "Default will be EPNM theme... once I toggle it to EMS UI then the current design should be shown."
- **Technical detail:** Described the shell app architecture (Infra UI repository), common components (common UI), and EMS UI repository structure. Listed EPNM repos: PI framework, wireless framework, assembly repo for inventory, ChassisView repo, fold management.

#### Ramesh Dhashnamoorthy (dramesh@cisco.com)
- **Role:** Tech lead or architect. US-based (only India-based exception from the team).
- **Key contributions:** Asked about AI tool compliance. Wanted to understand Claude Code and LangGraph architecture, whether tools are cloud-hosted or local, and Cisco compliance. Also asked about testing approach in detail: existing test cases, functional coverage, data-driven testing.
- **Sentiment:** Thorough, security-conscious, QA-focused. Asked the most probing questions.

#### Aadit Vaidyanathan (aadvaidy@cisco.com)
- **Role:** Tech lead. India-based.
- **Key context:** Mentioned will help with access setup (AD groups).

#### Jenis Dharmadurai (jdharmad@cisco.com)
- **Role:** Tech lead. India-based.
- **Key contributions:** Mentioned correlated alarms in the fault management walkthrough.

#### Ramkrishna Galla (ragalla@cisco.com) — referred to as "Rama" or "Srama"
- **Role:** Tech lead. India-based.
- **Key contributions:** Provided the architectural overview of how EPNM works: devices queried via SNMP/CLI, data stored in Oracle, applications consume from database for visualization/monitoring/configuration. Noted Postgres in the new product (Oracle dependency removed).
- **Sentiment:** Detail-oriented. Provided the clearest architectural explanation of the data flow.

#### Senthilkumar Palaniyandi (spalaniy@cisco.com)
- **Role:** Tech lead. India-based.
- **Key context:** Listed as accepted on meeting invite. Speaking role not clearly distinguished in transcript.

### BayOne (4 people)

#### Colin Moore (colmoore@cisco.com)
- **Role:** Director of AI. Leading the POC personally.
- **Sentiment:** Engaged, technically sharp, respectful of the team's domain expertise. Gave a compliment on the Confluence page organization.
- **Key statements:**
  - "My first pass ticket has started. I'll focus it on these specific screens, and then I'll expand it out."
  - "I actually feel pretty good about this as we're going."
  - "Usually, whenever we get into these specific projects, even that confluence page... Usually we have to go digging for that. So actually my life is a lot easier."
- **Dynamics:** Asked targeted technical questions (Oracle vs Postgres, backend migration status, repository locations). Committed to strict Cisco compliance.

#### Rahul Bobbili (rabobbil@cisco.com)
- **Role:** President, BayOne. Background support.
- **Key statement:** Assured the team that Neha and he would make sure Colin stays responsive: "Sometimes he gets a little backlog and he just needs a little tiny internal nudge."

#### Neha Malhotra (nehamalh@cisco.com)
- **Role:** Business operations / engagement management.
- **Key context:** Will work closely with Colin on the engagement. Day-to-day operational contact alongside Colin.

#### Zahra Syed (zahsyed@cisco.com)
- **Role:** Director, Strategic Accounts. Business side.
- **Key context:** Described BayOne team roles: "Colin will be leading the entire engagement end-to-end. Neha will be working very closely with him and Rahul and I will be on the back end."

---

## Meeting Dynamics

- **Setting:** WebEx video call. Colin was late (meeting was on wrong Cisco account). 12 attendees total.
- **Tone:** Professional, collaborative, technically substantive. The most operationally detailed meeting so far.
- **Key shift from prior sets:** This is the first meeting with the actual engineering team. Prior meetings were with Guhan and Selva only. Now the tech leads are presenting, demonstrating the product, and asking their own questions.
- **Trust signals:** Cisco team prepared a Confluence page with links to repos, user guides, recordings, and API docs. Akhil did a live product demo. Ramesh asked probing but fair questions about AI compliance.
- **Time zones:** Team is mostly India-based (IST). Colin is EST. Selva and Ramesh are US-based.
