# Tailored Brands Internal Meeting - Full Decomposition

**Source:** `/tb/meetings/1.txt`
**Meeting Type:** Internal planning call
**Participants:** Colin Moore, Rahul (CEO), Suraj (Sales), and likely Rima/Anuj (Sales)
**Purpose:** Prepare for discovery meeting with Tailored Brands leadership

---

## 01. Company Overview

### Tailored Brands Corporate Structure
- **Parent Company:** Tailored Brands
- **Owned Brands:** Men's Warehouse, Joseph A. Bank
- **Geographic Focus:** Heavy presence in Texas (bread and butter revenue)
- **HQ Locations:** Dublin, CA and Houston, TX (Houston is larger; most leadership sits there)

### Business Model Highlights
- Large contracts for weddings (volume suit purchases)
- Existing system that mixes and matches suits for wedding parties
- Coordinators manually input large orders currently
- Physical retail + digital presence (omnichannel)

---

## 02. Key Personnel Map

### Executive Level

| Name | Title | Notes |
|------|-------|-------|
| **Carl Vasani** | Chief Product Officer (CPO) | Controls budget. All SOWs must be approved by Carl. Known to BayOne team for a long time (signed off on SOWs at Albertsons years ago). Been around in retail world. |

### Siva's Organization (Tech & Engineering)

| Name | Title | Reports To | Background | Key Notes |
|------|-------|------------|------------|-----------|
| **Siva** | SVP, Tech & Engineering | Carl (for budget) | Ex-Albertsons | Main sponsor. Pulled team from Albertsons. Very protective. Will share information openly. Trying to consolidate all tech/engineering under him. Losing battle on QA. |
| **Kieran Dharmavarbu** | Senior Director, UI (de facto AI lead) | Siva | Ex-Albertsons | Over all UI. AI initiatives will fall under him. Super humble, doesn't advertise knowledge. Managed 140+ contractors/FTEs. Expert in iOS, Android, mobile tech. Will answer any questions. Currently texting with BayOne team. |
| **Kalyan** | Director of AI | Siva (via Kieran likely) | Ex-Albertsons | Just appointed ~1 week ago. Background in merchandising and tech engineering. Was dabbling in DevOps. Big pet peeve: no QA/shift-left. Burned out fighting this battle at Albertsons. Very intelligent (high IQ). NOT a people person. Admitted in a meeting he doesn't know AI. |
| **Anitha Andre** | Director | Siva | Ex-Albertsons | Backend, Java, some UI. Junior director. Couldn't join upcoming meeting. Technically very strong. |
| **Program Manager (unnamed)** | Program Manager | Siva | Recently hired | Pulling budgets together. |

### QA Organization (Separate from Siva)

| Name | Title | Location | Notes |
|------|-------|----------|-------|
| **Vijay Kampole** | Senior Director, QA | Houston | NOT under Siva. There's friction. Vijay worried about losing QA area to Siva. Meeting with him pending but hasn't happened. |
| **Manoj Thora** | (Under Vijay) | Houston | BayOne knows him from Albertsons. |

### Product Organization

| Name | Title | Notes |
|------|-------|-------|
| Product Director | Director | Works with Siva's team |
| Product Senior Director | Senior Director | Handles all product |

---

## 03. Relationship Map & History

### BayOne Relationship Chain
```
Yogesh (BayOne)
    └── knows Siva (from Albertsons)
            └── Siva brought Kieran, Kalyan, Anitha from Albertsons
            └── Siva introduced BayOne to product side

Suraj (BayOne)
    └── supported Siva at Albertsons (as SVP there)
    └── helped Kieran 5 years ago (brought contractors for mobile team)
    └── worked with Manoj at Albertsons
    └── worked with Kalyan at Albertsons

Colin/BayOne team
    └── Carl Vasani knows them (was sign-off person at Albertsons long ago)
```

### Access Level
- **Siva:** Will introduce BayOne to anyone, but likes to be siloed. Very protective.
- **Kieran:** Highly accessible. "Text me what you need."
- **Carl:** Known to BayOne, accessible through Siva.
- **Vijay (QA):** Siva not volunteering easily to set up meeting. Likely friction.

---

## 04. Current BayOne Footprint at Tailored Brands

### Active Placements
| Role | Person/Status | Team |
|------|---------------|------|
| Product Manager | Active | Data analytics + customer experience |
| UI/UX | 2-3 people | Under Kieran/Anitha |
| UI/UX Offshore | 1 solid person | Under Kieran |
| UI Architect | Starting next week | Under Kieran |
| Developer/Tester (UI knowledge) | Active | Under Anitha |

### Pending Placement
- Taking over a contractor from Infosys (currently working two jobs at Apple + Tailored Brands). Will take a break, kill Infosys SOW, come onto BayOne's.

### Competition
| Vendor | Footprint |
|--------|-----------|
| **Infosys** | 2-3 contractors (2 offshore + 1 onshore with Kieran) |
| **Commerce Tools** | Code modernization work (pre-existing, before current leadership) |

---

## 05. Strategic Initiatives (2024-2026)

### From AI Research (Rahul's search)
1. **AI-Driven Customer Intelligence & Positioning**
   - Customer data platform
   - Unified data
   - ML pipelines
   - Potentially a vulnerable area for entry

2. **Cloud Native Platform Modernization**
   - DevOps transformation
   - Legacy modernization
   - API-first architecture
   - Containerization
   - Reducing operational complexity
   - Enable faster digital delivery

3. **Enterprise Sales Service Commerce Platform**
   - "Taylor Express" initiative

4. **Omnichannel Orchestration**
   - Physical/digital integration
   - They are "fairly legacy" and "behind" here

### Current Active Projects
- **Code Modernization:** In progress with Commerce Tools (external company, predates current leadership)
- **Core Modernization:** Just starting (no vendor yet for services, just a company assisting)

---

## 06. Opportunity Analysis

### Two Buckets Framework (Colin's categorization)

#### Internal AI Initiatives
- Supply chain optimization
- QA/testing automation
- Code modernization
- Internal process automation
- Developer productivity

**Colin's Assessment:** "Internal ones are almost always good, especially if they're just starting out. It's 2026 - they're late to the game."

#### External-Facing AI Initiatives
- AI-powered shopping for large contracts (weddings)
- Website features (suit picker, etc.)
- App features
- Customer-facing AI

**Colin's Assessment:** "Tend to get stuck in POC lane. Need a person with power behind it. Usually owned by one person internally who wants staff and solutions."

### Specific Opportunities Identified

| Opportunity | Assessment | Notes |
|-------------|------------|-------|
| **QA/Shift-Left + Code Modernization** | HIGH | Even if Commerce Tools is doing code mod, they're not handling QA simultaneously. "That's crazy." This is exactly what BayOne pitched to Cisco. Low headcount, high output. |
| **AI Assistance for Kalyan** | HIGH | New, potentially out of his depth, under pressure to deliver. Looking to partner. Already asking BayOne's product manager AI questions. |
| **Test Generation** | HIGH | Even without QA ownership, Siva can effectively control QA through test generation. "Just hitting key and debugging." |
| **Data/Analytics** | MEDIUM | "Where's the data? Who owns that?" - need to understand this. Product manager already working on analytics. |

### Concerns/Blockers
- Kalyan may not actually know AI (could be a front)
- Existing vendor (Commerce Tools) on code modernization
- QA ownership friction (Siva vs. Vijay)
- Short-term external projects can get stuck in POC

---

## 07. Budget & Timing

### Budget Information
- **2025 Budget:** ~$2M for a few areas
- **FTE Budget:** Contractors count against FTE budget somehow
- **Budget Approved:** February 1, 2026 (roadmaps are set)
- **Finding Budget:** "Siva will find the budget when there's a good initiative opportunity"

### Key Timing
- Leadership conference: Week after the internal meeting
- Better to meet leadership after conference (they'll have fresh priorities)
- Friday 11-12: Potential call with Siva, Kalyan, Kieran (Anitha can't join)
- Fourth/Fifth of month: Possible dates for in-person

---

## 08. Meeting Strategy & Approach

### Goals for First Meeting
1. **Establish BayOne as AI partner** - "We know AI. Help us understand what you're doing."
2. **Information gathering** - Understand their roadmap now that budgets are set
3. **Open minds** - Get Siva/Kalyan to see BayOne as partner, not just staffing

### Approach Guidance (from team)
| Do | Don't |
|----|-------|
| Listen and brainstorm | Pitch heavily |
| Ask questions | Tell them they don't know things |
| Go lighter on case studies | Overwhelm with what BayOne has done |
| Break proposals into small pieces | Propose millions of dollars |
| Stroke egos carefully | Be aggressive |
| Let them give information first | Pull information out |

**Key Quote (Suraj):** "These guys are pretty smart. We can't come in... I have to always tell people when we get to this level. Even though they might not know a lot about AI, they'll take what you have and brainstorm with it."

**Key Quote (Rahul):** "I would actually go lighter on case studies, more on just listening. We should not pitch. We should just listen and brainstorm."

### Meeting Format (Friday)
- Siva will give overall overview of what they're doing
- What he's responsible for, his team
- Kalyan, Kieran, and one other will join (Anitha can't)
- Opportunity for BayOne to ask questions
- This is phase 1; will need more meetings

---

## 09. Pre-Meeting Intelligence Gathering

### Actions Identified
| Action | Owner | Status |
|--------|-------|--------|
| Talk to placed team members for insider info | Colin | Pending |
| Get list of placed people with job descriptions | Suraj/Rima | To send |
| Set up calls with placed team members | Suraj | To arrange |
| Get public information/reports on Tailored Brands | All | Some AI research done |
| Use SalesForge for deep research | Colin | To do |
| Meet with Kieran before full meeting | Team | He's available |
| Meet with CPO Carl separately | Team | After leadership conference |

### Information Sources
- Job descriptions from placements (better quality than Albertsons)
- Placed team members can share what they're working on
- Public earnings calls and releases (SalesForge can pull)
- Kieran is highly available for questions
- Siva will share everything openly

---

## 10. Competitive Landscape

### Current Vendors
| Vendor | Work | Status |
|--------|------|--------|
| Commerce Tools | Code modernization | Established, predates current leadership |
| Infosys | Contractors (2-3 people) | Losing one to BayOne |
| (Unknown service company) | Core modernization | Just starting |

### BayOne Positioning
- Not competing on code modernization (already taken)
- Can compete on AI + QA angle
- Already have relationships and placements
- Siva is actively pulling BayOne in

---

## 11. Organizational Dynamics & Politics

### Power Structure
- **Siva** is building his empire - pulled all UI under him
- **Siva vs. Vijay (QA):** Clear tension. Siva wants QA, Vijay is protecting it.
- **Shift-left failure:** Multiple people (Kalyan, others) tried at Albertsons, burned out.
- **Seniority dynamics:** Vijay has seniority/relationships protecting QA org.

### Cultural Notes
- Very protective of their expertise
- High IQ individuals who are technically strong
- Not people persons in some cases (Kalyan)
- Humble (Kieran won't advertise his AI knowledge)
- Open to sharing information (unlike other clients)
- Need to "stroke egos" and approach gently

---

## 12. Technical Environment (Limited Info)

### Known Stack/Tools
- iOS and Android mobile development
- Java (backend)
- UI/UX development
- Data analytics
- Commerce Tools platform

### Unknown/To Discover
- Database technologies
- Cloud infrastructure
- CI/CD pipeline
- Testing frameworks
- ML/AI infrastructure (if any)
- Data platform details

---

## 13. Key Quotes

> "Siva will find the budget when there's a good initiative opportunity that saves them time and takes care of needs."

> "It's not going to be one of those clients where we have to pull information out. Whatever we need, he'll give."

> "These guys are pretty smart. Even though they might not know a lot about AI, they'll take what you have and brainstorm with it."

> "If they're writing the code, they should be testing it. But the QA teams don't need to do anything other than verify it ran. Generating the test can still happen here [with Siva]."

> "His [Kalyan's] biggest pet peeve is no QA. The shift left has not been active at Albertsons. He lost his battle. He burned out."

> "It's 2026 - that's going to be late to the game for a lot of people. They're probably feeling that too."

---

## 14. Unanswered Questions

### About the Organization
- What is the full tech stack?
- What data infrastructure exists?
- Who owns data/analytics beyond the product manager?
- What is the mobile app architecture?

### About Opportunities
- What specific AI use cases have they identified?
- What is the wedding/large contract automation scope?
- What internal tools do they use?
- What is the Commerce Tools integration scope?

### About Process
- How do they make vendor decisions?
- What is the typical SOW size/duration?
- How quickly can they move on initiatives?
- What are the FY26 specific priorities?

---

## 15. Next Steps (From Meeting)

1. **Immediate:** Talk to Kieran before full meeting
2. **This Week:** Get list of placed people + job descriptions from Suraj/Rima
3. **This Week:** Set up calls with placed team members
4. **Before Full Meeting:** Run SalesForge for deep research
5. **After Leadership Conference:** Try to meet Carl (CPO) separately
6. **2-3 Weeks Out:** In-person meeting with full team if possible
