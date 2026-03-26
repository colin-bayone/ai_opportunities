# Wave 2 Research Findings

**Completed:** 2026-03-03
**Folders Explored:** SOW/, mcgrath/, zeblock/, project/

---

## Summary

Wave 2 explored project/client folders and revealed **commercial patterns, engagement models, and partnership structures** highly relevant to Ariat:

| Folder | Primary Value | Ariat Relevance |
|--------|--------------|-----------------|
| `SOW/` | Cisco SOW template, outcome-based model, India delivery | **HIGH** - GCC delivery model example |
| `mcgrath/` | Enterprise MSP RFP, shared responsibility, hybrid pricing | **VERY HIGH** - Same engagement patterns |
| `zeblock/` | Partnership structure, GCC planning, co-innovation model | **MEDIUM** - Partnership patterns |
| `project/` | Cisco CI/CD current state, AI capabilities, hybrid delivery | **HIGH** - Testing AI capabilities |

---

## Folder 1: SOW/

### What It Contains
- Complete SOW for Cisco NX-OS CI/CD engagement (SOW #33282)
- Budget: Rs 4,393,740 INR (~$53K USD) over 6 months
- Location: Bangalore, India (BGL15)
- Timeline: November 2025 - April 2026

### Key Service Model

**Outcome-Based (Not Staff Augmentation):**
- BayOne manages service outcome AND resources
- Resource replacement responsibility on BayOne
- Weekly SLAs with automatic fee adjustments for failures
- 100% regression execution, 100% failure analysis targets

**AI Development Services:**
- Build tools using AI technologies
- Data pipeline development
- AI model design, development, testing
- Production deployment
- Supporting code and infrastructure

### Commercial Structure

| Phase | Timeline | Amount (INR) |
|-------|----------|--------------|
| Phase 1 (66% features) | Nov-Jan 2026 | Rs 690,580/month |
| Phase 2 | Feb-Apr 2026 | Rs 774,000/month |
| **Total** | 6 months | **Rs 4,393,740** |

### GCC-Relevant Patterns
- Bangalore-based delivery with IST timezone overlap
- Working hours: 08:00-17:00 IST, M-F
- Cisco holiday calendar adherence
- Fixed bid pricing with performance adjustments
- Primary contact structure (BayOne Lead)

### Reusable Content
- `/SOW/SOW-Building-Nexus-9000-switches.html` - Professional SOW template
- `/SOW/templates/sow-schema-sample.yaml` - Data model for SOW generation
- `/SOW/SESSION_HANDOFF.md` - Workflow documentation

---

## Folder 2: mcgrath/

### What It Contains
- Comprehensive MSP RFP response for McGrath RentCorp
- 36 clarifying questions submitted
- Gap analysis, competitive assessment, architecture mapping
- Win strategy documentation

### Client Profile
- **McGrath RentCorp:** NASDAQ: MGRC, equipment rental company
- ~1,383 employees across 4 business units
- 30+ consecutive years of dividend increases
- Focus: operational excellence, compliance, customer success

### Scope Complexity

| Dimension | Scale |
|-----------|-------|
| Solution areas | 10+ (Salesforce, Oracle Fusion, RecVue, MuleSoft, etc.) |
| Integrations | 50+ documented |
| Compliance frameworks | 8 (NIST, SOC 2, HIPAA, PCI, GDPR, CMMC, CPRA, ISO-27001) |
| Specific requirements | 180+ line items |
| Go-live timeline | 7 weeks (May 18 - July 6, 2026) |

### BayOne Positioning

**Incumbent Advantage:**
- 5 embedded resources already at McGrath
- Institutional knowledge foundation
- Reduced knowledge transfer timeline

**Shared Responsibility Model:**
- Not full outsource; collaborative partnership
- Majority of RFP scope marked "Shared"
- Clear RACI definition required

**Hybrid Pricing:**
- Fixed monthly retainer for core operations
- Variable pool for enhancement/transformation
- Year 1 aggressive, normalized Years 2-3

**Strategic Subcontracting:**
- Bid strong on core areas (Salesforce, Oracle functional)
- Partner for gaps (MuleSoft deep development, OCI infrastructure)

### Key Differentiators
1. Insider advantage (5 embedded resources)
2. Shared responsibility embrace
3. Phased implementation (de-risked)
4. Hybrid pricing (predictability + flexibility)
5. Diversity (women-owned/led, MakeTechPurple)
6. Technical depth in demo phase

### Reusable Content
- `/mcgrath/rfp_docs/final/architecture.md` - Architecture overview template
- `/mcgrath/rfp_docs/final/sla.csv` - SLA/KPI framework (P1/P2/P3/P4 tiers)
- `/mcgrath/rfp_docs/final/specific_requirements.csv` - Requirements matrix
- `/mcgrath/questions/FINAL_submission_questions.md` - Strategic Q&A approach

---

## Folder 3: zeblock/

### What It Contains
- Partnership exploration with Zeblok Computational
- Meeting transcript and executive summary
- Company profile and critical analysis

### Partnership Context
- **Zeblok:** AI infrastructure startup (air-gapped AI deployment)
- **Founder:** Mouli Narayanan (20 years Wall Street, ex-JPMorgan)
- **Product:** Ai-MicroCloud - "shrink Azure, deploy anywhere"
- **Focus:** Defense, manufacturing, retail, education

### GCC-Relevant Content

**Zeblok's India Operations:**
- Already has subsidiary in India
- Actively planning GCC operations
- India as delivery center (execution, not market)

**BayOne India Strategy (from transcript):**
- Building delivery center in Chennai/Bangalore
- India focus is execution, not market
- Partnering with existing vendors
- India as testing ground for partnership models

**Testing/QA Vertical:**
- Identified as high-traction area for both companies
- Agentic test case generation highlighted
- AI-native development paradigm emerging

### Partnership Model ("Zeblok Labs")
- Co-innovation framework
- Physical lab in Bay Area
- Market-ready solutions for specific industries
- Joint developer resources

### Reusable Content
- `/zeblock/zeblok_partnership_executive_summary_v2.html` - Partnership summary template
- `/zeblock/claude/2026-03-02_partnership_meeting/research/05_critical_analysis_colin.md` - Strategic assessment approach

---

## Folder 4: project/

### What It Contains
- Current state of Cisco CI/CD engagement
- Single document: `engagement-status.md`
- Last updated: February 2, 2026

### Current Project Status
- **Phase:** Discovery - Preparing for initial engagement
- **Target:** 20-30% reduction in average PR merge time

### Active Priorities (Phase 1)

| Item | Focus | Status |
|------|-------|--------|
| **A - Developer Box** | Visibility, insights, AI-assisted debugging | Selected |
| **F - Branch Health** | Failure attribution, dashboards | Selected |

### Deferred Items

| Item | Focus | Status |
|------|-------|--------|
| C | Unified interface/ single pane of glass | Not selected |
| B | Gate failure diagnosis | Deferred |
| D | Coverage tracking | Deferred |
| E | Self-healing | Deferred (most complex) |

### Budget & Staffing Model
- Budget: $100K/quarter
- Onshore: 1-1.5 FTE (Bay Area)
- Offshore: 4-5 resources (India)
- Discovery: 1-2 weeks

### AI Capabilities Being Built

**Phase 1:**
- Telemetry and instrumentation for developer box
- Coverage metrics visibility
- AI-assisted debugging (pattern recognition, cause suggestion)
- Release lead dashboards with failure attribution
- Automated follow-up (notifications, assignments, escalations)

**Future Phases:**
- Unified chat interface (natural language queries)
- AI-driven failure diagnosis
- Self-healing (autonomous correction with governance)

### Reusable Patterns for Ariat
- Hybrid delivery model (onshore lead + offshore team)
- Phased implementation with quick wins first
- Build on existing systems (not replacement)
- AI-assisted debugging transferable to testing
- Failure attribution applicable to retail operations

---

## Cross-Cutting Themes (Wave 2)

### Theme 1: Shared Responsibility Model
- McGrath: Majority of scope marked "Shared"
- SOW: BayOne manages outcome + resources, not just bodies
- **Ariat Application:** GCC as partnership, not pure outsource

### Theme 2: Hybrid Pricing with Flexibility
- McGrath: Fixed retainer + variable pool
- SOW: Fixed bid with performance adjustments
- **Ariat Application:** Predictability for finance + flexibility for growth

### Theme 3: Phased Implementation
- McGrath: Phase 1 Onboard → Phase 2 Operate/Transform
- Cisco: Phase 1 A+F → Phase 2+ B/C/D/E
- **Ariat Application:** Start small, prove value, scale

### Theme 4: Incumbent/Embedded Advantage
- McGrath: 5 embedded resources = institutional knowledge
- Cisco: Existing relationships with engineering teams
- **Ariat Application:** Position BayOne resources as long-term partners

### Theme 5: India Delivery Center
- SOW: Bangalore delivery, IST overlap
- Zeblock: India as execution, not market
- Cisco: 4-5 offshore resources for scaling
- **Ariat Application:** Direct parallel to GCC model

### Theme 6: Compliance as Differentiator
- McGrath: 8 frameworks (NIST, SOC 2, HIPAA, etc.)
- SOW: SLA compliance with fee adjustments
- **Ariat Application:** Compliance readiness is table stakes

---

## Key Files for Ariat Slides

### Engagement Models
- `/SOW/SOW-Building-Nexus-9000-switches.html`
- `/mcgrath/rfp_docs/McGrath RFP Analysis BayOne_plaintext.txt`

### SLA/KPI Frameworks
- `/mcgrath/rfp_docs/final/sla.csv`

### Architecture Templates
- `/mcgrath/rfp_docs/final/architecture.md`

### Partnership Structures
- `/zeblock/zeblok_partnership_executive_summary_v2.html`

### AI Capabilities
- `/project/engagement-status.md`

---

## Next Steps

Wave 3 will explore:
1. `context/` - Internal context files
2. `documents/` - Legacy client-facing and internal documents
3. `new_context_2-2-2026/` - Meeting transcripts and emails
4. `specs/` - Design specifications
