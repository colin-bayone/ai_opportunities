# Themes and Decisions: UI Conversion Discovery

**Generated:** 2026-03-13 (retrospective analysis)

---

## Theme 1: Project Definition and Scope

**Problem:** EPNM-to-EMS UI conversion challenge

**Key Evolution:**
- Feb 9: Initial unclear - "network management product" with ~200 screens
- Feb 20: Clarified to EPNM/EMS specifically; 70-100 screens; vertical work required

**Critical Insight:** NOT just UI modernization. If frontend doesn't exist in EMS, backend doesn't either. This is "vertical work."

**Technical Stack:**
| System | Backend | Frontend | Age |
|--------|---------|----------|-----|
| EPNM (legacy) | Monolithic Java | Dojo/JavaScript (some Angular) | 15+ years |
| EMS (modern) | Microservices Java | Angular | Newer |

---

## Theme 2: POC Scope and Phasing

**Core Tension:** Demonstrate capability without over-committing on free work

**Two-Phase Model (Colin's Framework):**

| Phase | Duration | Focus |
|-------|----------|-------|
| Phase 1: Exploration | ~1 week | Screen selection, codebase analysis, pattern discovery |
| Phase 2: Conversion | ~3 weeks | Implementation, testing, validation |
| Total | 4 weeks | From code access, not calendar time |

**Key Decisions:**
- Scope: 2-3 representative screens (not Cisco's suggested 10)
- Screen selection: Collaborative - Cisco SMEs propose, BayOne validates
- Timeline trigger: Starts when repo access granted, not before

---

## Theme 3: Acceleration Mechanism ("Flywheel")

**Why 2-3 screens in 4 weeks doesn't extrapolate linearly to 200 screens**

**One-Time Investment (POC builds this):**
- Codebase exploration and knowledge graph
- Pattern identification and conversion library
- Custom agent development
- Workflow design and validation
- Playwright testing infrastructure

**Per-Screen Work (diminishes over time):**
| Activity | Screen 1 | Screen 3 | Screen 10+ |
|----------|----------|----------|------------|
| Pattern discovery | Heavy | Light | Minimal |
| Implementation | Discovery-driven | Apply patterns | Template-based |
| Validation | Build baselines | Run existing | Automated |

**Staffing Multiplier:**
- POC: Colin solo, sequential = slowest pace (but establishes foundation)
- Paid: Team scale + parallel streams = multiplicative speedup

---

## Theme 4: Technical Approach

**Exploration Phase Tools:**
- Claude Code for codebase analysis
- Screen inventory and categorization
- Dependency mapping
- Pattern identification

**Conversion Phase Tools:**
- POC: Claude Code with sub-agents (manual oversight)
- Scaled: LangGraph multi-agent swarm

**Agent Roles (for scaled engagement):**
| Agent | Responsibility |
|-------|----------------|
| Architect | Strategic planning and task decomposition |
| Engineer | Technical implementation |
| Foreman | Work coordination and dependencies |
| Judge | Quality validation and testing |

**Validation:**
- Playwright for automated visual testing
- Baseline screenshots from EPNM
- Side-by-side comparison reports
- Gap documentation

---

## Theme 5: Document Quality Standards

**Issues Identified in v2 (and fixed in v3):**

| Problem | Example | Fix |
|---------|---------|-----|
| "Isn't X, it's Y" pattern | "This isn't just UI translation" | State what IS directly |
| First-person voice | "I'm working solo" | Organizational framing |
| Blog-style headers | "The Flywheel Effect" | Formal: "Acceleration Mechanism" |
| Colloquialisms | "skinning", "baked into" | Professional equivalents |
| Excessive em-dashes | 22+ in 264 lines | Limit to 5-7 |
| Rhetorical questions | "Does X mean Y? No." | Direct statements |

**Colin's Key Feedback:**
> "It's not verbose, it's sounding like total BS" - casual tone undermined credibility

---

## Theme 6: Security and Logistics

**Security Model:**
- All work on Cisco hardware (laptop in transit)
- Cisco-licensed AI tools only (cloud.ai.cisco.com)
- No code leaves Cisco infrastructure
- NDA already signed

**Access Requirements:**
- Repository access to EPNM and EMS codebases
- Running instances of both systems
- Cisco-provided Claude/AI licenses
- Cisco ID for authentication

**Dependencies (as of Feb 20):**
- Cisco laptop delivery: 1-2 weeks
- Repository access: After hardware
- SME availability: Limited ("on critical platform work")
- SME time needed: 2-3 hours for Phase 1

---

## Theme 7: Stakeholder Dynamics

**Cisco Team:**
| Name | Role | Notes |
|------|------|-------|
| Guhan | Decision-maker | Interested in "10 screens in 10 days" model |
| Selva | Technical contact | Clarifies vertical nature of work |

**BayOne Team:**
| Name | Role |
|------|------|
| Colin Moore | Director of AI, technical lead |

**Working Principles (Colin's guidance):**
1. Collaborative, not defensive
2. Present methodology as normal procedure
3. Make Cisco a partner in scope decisions
4. Sound like someone who has done this before
5. Acknowledge limits transparently

---

## Theme 8: Budget and Business Model

**POC (Free):**
- Cost to Cisco: Zero
- Staffing: Colin solo
- Deliverables: 2-3 working screens + patterns + estimation model

**Paid Engagement (If Cisco Proceeds):**
- Staffing: Team scale
- Execution: Parallel streams
- Foundation: All POC work transfers
- Velocity: Multiplicative over POC baseline

---

## Key Decisions Summary

| Decision | Who | When | Status |
|----------|-----|------|--------|
| Two-phase POC structure | Colin | Feb 21 | APPROVED |
| 2-3 screens scope | Colin | Feb 21 | APPROVED |
| Collaborative screen selection | Colin/BayOne | Feb 21 | APPROVED |
| 4-week timeline | Colin/Cisco | Feb 20 | AGREED |
| Cisco hardware only | Cisco/Colin | Feb 20 | COMMITTED |
| Professional proposal tone | Colin | Feb 21-22 | ENFORCED |

---

## Open Items

| Item | Status | Owner |
|------|--------|-------|
| Specific screen selection | Awaiting Cisco proposal | Guhan/Selva |
| Cisco laptop delivery | In progress | Cisco |
| Repository access | Pending hardware | Cisco |
| Backend service inventory | Awaiting exploration | Phase 1 |
