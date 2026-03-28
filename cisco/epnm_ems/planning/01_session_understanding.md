# Session Understanding: UI Conversion Discovery

**Session Date:** February 20, 2026
**Prepared by:** Claude (continuation session)
**Context:** Resuming interrupted work from earlier session

---

## What Happened in the Previous Session

The previous session was working on processing meeting output from the Feb 20, 2026 discovery call with **Guhan and Selva** from Cisco. This is a **separate project** from the CI/CD work with Anand/Srinivas/Divakar.

The session was interrupted ("stop hooks kept firing off") before completing the assigned tasks.

---

## Source Materials Available

1. **Session Handoff:** `planning/00_session_handoff.md` - Instructions for this session
2. **Feb 20 Transcript:** `source/guhan_selva-2-20-2026.txt` - Primary discovery call
3. **Discovery Documents:** `discovery_session_v1.html` and `discovery_questions_v1.md` - Documents used during call

---

## Project: UI Conversion (EPNM to EMS)

### The Problem (from Feb 20 transcript)

Cisco has two products:
- **EPNM** (Legacy) - Element management, network inventory, topology management. 15+ years old. NOT microservices.
- **EMS** (Modern) - Microservices-based version of the same functionality.

**The issue:** Key customers want the old UI back. They're used to it after 15 years and don't want to retrain network operators on the new UI.

**Engineering challenge:**
- Cannot simply copy code - architectures are fundamentally different
- It's not just UI - backend logic is also different (vertical slices)
- If functionality wasn't brought to the new UI, the corresponding backend also doesn't exist
- Cisco invested 2 years building the new UI, so they need to make the old UI work within the new architecture

### Technical Stack

**Backend:** Java (both old and new)

**Frontend:**
- Old (EPNM): Dojo, JavaScript, minimal Angular
- New (EMS): Angular

**Key constraint:** Old system is tightly coupled (monolith), new is microservices. Direct code porting won't work.

### What Cisco Needs

1. Take old EPNM code
2. Convert to work within EMS architecture
3. Provide same user experience as old UI
4. 70-80-100+ screens potentially - they know not everything will be converted
5. Want estimates: "if we can do 10 screens in 10 days, we can do 17 in 17 days"

### Our Approach (from meeting)

1. Start with **Claude Code** for initial exploration and pattern recognition
2. Scale to **LangGraph agent swarm** for larger implementation:
   - Master Architect agent
   - Engineer agent (planning)
   - Foreman agent (spawns sub-workers)
   - Judge agent (quality control)
3. Automated testing with **Playwright** for visual verification
4. Continuous gap analysis through agent peer communication

### Access and Security

- All work must be on **Cisco laptop** (pending - estimated 1-2 weeks)
- Use **Cisco-provided AI licenses** (not BayOne's own)
- No code leaves Cisco hardware
- Use Cisco ID for access
- Rahul Bobbili working on hardware confirmation

### Timeline

- **4 weeks** for POC timeline (Guhan's preference)
- Colin's Cisco laptop expected in ~2 weeks
- Initial conversations can start before laptop arrives
- Cisco team will identify priority screens for conversion

### Agreed Next Steps (from meeting)

1. Colin to write POC proposal (summary of meeting)
2. Cisco team to identify specific screens for conversion
3. Get confirmed date on Cisco laptop
4. Once laptop arrives, set up call to navigate resources
5. Colin to get Cisco ID finalized

---

## Tasks Per Handoff Instructions

### Task 1: Meeting Decomposition

**Output needed:**
1. Problem Statement (detailed)
2. Key Facts Learned
3. Decisions Made
4. Action Items
5. Points Made (notable statements)
6. Open Questions

### Task 2: POC Proposal Brainstorming

**Key constraints:**
- **Free POC** to demonstrate capability
- 10 screens is too much for free work
- Need realistic, smaller scope (1-3 screens suggested)
- Goal: demonstrate AI-accelerated conversion, not do full job
- Don't over-commit

**Brainstorm areas:**
- Realistic scope for free POC
- What demonstrates capability without over-committing
- Success criteria
- What we need from Cisco

---

## Working Style Reminders

From handoff:
- Be collaborative partner, bring ideas proactively
- But stay grounded - don't make independent assumptions
- Colin will be actively involved
- Balance: thoughtful collaboration, not passive order-taking or runaway execution

---

## Distinction from CI/CD Project

This UI conversion work is **separate from** the CI/CD work with Anand/Srinivas/Divakar. That project focuses on:
- NX-OS CI/CD pipeline improvement
- Items A (Developer Box) and F (Branch Health)
- DeepSight platform integration
- Jenkins, Airflow, CAT, etc.

The UI conversion is for Guhan and Selva's team - different product, different scope.
