# Feb 20, 2026 Discovery Call - Structured Decomposition

**Meeting:** UI Conversion Discovery with Guhan and Selva
**Date:** February 20, 2026
**Attendees:** Colin Moore (BayOne), Guhan (Cisco), Selva (Cisco)

---

## 1. Problem Statement

**The Product:** EPNM (Evolved Programmable Network Manager) and EMS (Element Management System) - both are Cisco network element management platforms that handle network inventory, topology, and automation lifecycle management.

**Old vs New:**
- **EPNM (Legacy):** Monolithic architecture, Java backend, Dojo/JavaScript frontend with some Angular. Customers have used this UI for 15+ years.
- **EMS (Modern):** Microservices-based architecture, Java backend, Angular frontend. Built over 2 years with new UX design.

**Why Customers Want Old UI Back:**
- Network operators are trained on the legacy interface
- Customers don't want to invest in retraining operators
- Some key customers are refusing to migrate to EMS without their familiar UI
- This is blocking the business goal of migrating EPNM customers to EMS

**Technical Constraints:**
- The two architectures are fundamentally different (monolith vs microservices)
- "Surgery" was done on the old core - code can't simply be copied
- It's not just UI - the corresponding backend logic also doesn't exist in EMS
- Missing functionality is "vertical" - if frontend doesn't exist, backend doesn't either
- Legacy documentation is sparse ("trying to find the way around the code")

---

## 2. Key Facts Learned

**Scale:**
- 70-100 UI screens total need conversion (different numbers mentioned)
- Not expecting all screens converted - looking for POC + estimation model

**Architecture & Stack:**

| Component | EPNM (Legacy) | EMS (Modern) |
|-----------|---------------|--------------|
| Backend | Java | Java |
| Frontend | Dojo, JavaScript, some Angular | Angular |
| Architecture | Monolithic | Microservices |

**Approach Cisco Wants:**
- Take EPNM screens and backend, convert to work within EMS
- Customer should see identical experience (same visualization, same operations)
- Focus POC on screens that have NOT yet been brought into EMS (maximize value)

**Team Availability:**
- Cisco team is on "critical platform work" - limited time to invest
- They'll provide context and priority screens, but BayOne needs to work mostly independently
- Periodic checkpoints for clarification and progress updates

**Code Access & Security:**
- All work must happen on Cisco hardware (Colin getting laptop in 1-2 weeks)
- Must use Cisco-licensed AI tools (cloud.ai.cisco.com or similar)
- No downloading code to personal machines
- NDA already signed

---

## 3. Decisions Made

1. **POC Approach:** BayOne will do a hands-on POC demonstrating actual code conversion (not just analysis)
2. **POC Focus:** Will target screens/functionality NOT yet in EMS (rather than redoing already-migrated features)
3. **Security Model:** All work on Cisco hardware, Cisco AI licenses - code never leaves Cisco
4. **Timeline Target:** 4-week timeframe mentioned by Guhan for making "important decisions"
5. **Working Model:** Cisco provides context and priorities; BayOne works independently with periodic checkpoints

---

## 4. Action Items

**BayOne:**
- [ ] Write POC proposal with scope (Colin to send summary after meeting)
- [ ] Get firm date on Cisco laptop arrival
- [ ] Get Cisco ID finalized (was expected same day)
- [ ] Once hardware arrives, get set up with Cisco Claude/AI licenses

**Cisco:**
- [ ] Identify priority screens for conversion (team will help prioritize)
- [ ] Provide running system access when ready for testing
- [ ] Help set up Cisco AI tool licenses for Colin
- [ ] Provide initial context on selected screens (Selva mentioned team will do this)

---

## 5. Notable Points Made

**From Guhan:**
- "One of the outcomes I'm looking for... we are able to do 10 screens in 10 days, we can do 17 in 17 days - some sort of estimation" - wants to extrapolate timeline for customers
- "This is work we didn't anticipate but it's important for product" - this was unplanned but customer-driven
- "Let's do what we can in four weeks" - clear timeline pressure
- Team won't have time to pair extensively - need independent execution

**From Selva:**
- "It's not UI alone... along with it comes the backend logic" - clarifying scope is vertical
- "Focus on ones we've not brought in yet" - don't redo work already done
- "For now, keep the same user experience and bring it to the new and make it work end-to-end"
- "Team is on critical platform... they need to give you context and everything, then you take independently"

**From Colin:**
- Described Claude Code + LangGraph agent swarm approach (architect, engineer, foreman, judge agents)
- Mentioned Playwright for automated visual testing
- Committed to working within Cisco security requirements

---

## 6. Open Questions

**Technical:**
- What are the exact screens to target for POC?
- How much backend logic is involved for typical screens?
- Are there API contracts or is it direct database access in EPNM?
- What testing infrastructure exists? (unit tests, integration tests)

**Logistics:**
- When exactly will Cisco laptop arrive?
- Who on Cisco team will provide initial context? (Selva implied "the team")
- What Cisco AI tool access process looks like?

**Scope:**
- How many screens is realistic for a free POC? (Cisco suggested ~10 - that's likely too many)
- What constitutes "success" for the POC?
- What deliverables beyond working code? (Documentation? Estimation model?)
