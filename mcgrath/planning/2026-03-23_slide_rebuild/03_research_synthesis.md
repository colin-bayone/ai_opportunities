# Research Synthesis

Consolidated findings from all three research sessions, ready to inform build-phase handoffs.

---

## 1. Anti-Patterns Reference (from Autopsy, research/05)

### Root Cause
All 18 skipped slides share one root cause: they were assembled by someone thinking like a staffing company (Amit), not a solutions vendor (Colin). The deck defaults to proving BayOne is large, diverse, and process-heavy -- exactly the pitch a staffing firm makes.

### Top 5 Anti-Patterns for Builders
1. **No WIP markers, internal names, or TODO items.** Ever. (Slides 16, 20, 25, 35, 38, 39)
2. **No resume dumps.** Profiles should be 2-3 sentences, curated to the client's stack. (Slides 38, 39)
3. **No generic process diagrams.** Ticket flows, escalation matrices, and governance charts are table stakes -- don't waste slides on them unless differentiated. (Slides 15, 17, 18)
4. **No staffing company positioning.** Global maps, supplier awards, diversity stats splash pages, L&D platform screenshots, and CSR programs all scream body shop. (Slides 06, 07, 08, 41, 42, 43, 44)
5. **No indefensible claims without evidence (the Sarang lesson).** "20% cost optimization on Day 1" without proof invites skepticism. (Slide 35)

Full list: 22 anti-patterns across 5 categories in research/05_bad_slide_autopsy.md.

---

## 2. Content Source Decisions (from Crossover, research/06)

### Ariat Wins 8 of 9 Pairs

| Slide Topic | Use Source | Key Reason |
|-------------|-----------|------------|
| Title + Stats | Ariat 01 (MERGE M01+M02) | Team photo, elevator pitch, stats bar in one slide |
| Client Logos | Ariat 02 | More current logos (Netflix, GE, Atlassian, Workday) |
| Tech Stack | Either | Identical content |
| Services | Ariat 04 | 8 services with concise taglines vs 6 verbose paragraphs |
| Make Tech Purple | Ariat 09 | Slightly cleaner, includes MTP logo |
| AI Enablement | Ariat 10 + HTML gold standard | Night and day. McGrath 24 is WIP garbage. |
| Why BayOne | Ariat 06 | Icon grid with concise language vs flat bullet list |
| Closing | Ariat 19 | Team photo vs plain white |

### 3 Slides to ADD from Ariat
1. **Partnership Models (Ariat 05)** -- 4 engagement types, bridges services-to-solution gap
2. **Enterprise AI Solutions (Ariat 11)** -- HTML gold standard exists. AI across HR/Finance/Legal/Marketing
3. **Quality Engineering (Ariat 12)** -- HTML gold standard exists. 6 AI-powered QE capabilities

### 1 Slide NOT to Add
- **Key Differentiators (Ariat 07)** -- Redundant with "Why BayOne?"

### Key Content Notes for Builders
- Use "1,000+ projects" (Ariat), not "750+ projects" (McGrath)
- Consider preserving "Security First" from McGrath 37 when building Why BayOne
- McGrath 24's Cisco-specific content (InstallBase, MACDs) must NOT appear in the McGrath proposal

---

## 3. New Slide Order (from Reordering, research/07)

### Narrative Arc
*"We understand your NextGen transformation challenge and we've built a solution around it. AI-driven operations are our core differentiator, and we'll prove it with a phased delivery backed by real metrics and real case studies. Here's what it costs, here's why we're worth it, let's get started."*

### 7-Section Structure (29 positions, 30 slides with 14+24 combined)

**Section 1: OPENING & CREDIBILITY (4 slides)**
| New # | Old # | Title |
|-------|-------|-------|
| 1 | 01 | Title Slide |
| 2 | 11 | Executive Summary (needs total rewrite) |
| 3 | 02 | About BayOne (stats) |
| 4 | 03 | Client Logos |

**Section 2: THE SOLUTION (5 slides)**
| New # | Old # | Title |
|-------|-------|-------|
| 5 | 10 | Support Proposal Solution (divider) |
| 6 | 13 | RFP Scope Summary |
| 7 | 14+24 | Transformation Journey + AI Enablement (COMBINED) |
| 8 | 12 | Solution Summary |
| 9 | 48 | BayOne Operations Snapshot (moved from #30) |

**Section 3: DELIVERY APPROACH (4 slides)**
| New # | Old # | Title |
|-------|-------|-------|
| 10 | 21 | Phase 1 Discovery (divider) |
| 11 | 22 | Operational Maturity (4 phases) |
| 12 | 23 | Service Quality Audit Process |
| 13 | 46 | Measurement By Metrics (moved from #28) |

**Section 4: PROOF (5 slides)**
| New # | Old # | Title |
|-------|-------|-------|
| 14 | 30 | Why BayOne? (divider, repurposed as proof gateway) |
| 15 | 31 | Case Study Title -- Oracle HCM |
| 16 | 32 | Case Study 1 -- Oracle Fusion HCM |
| 17 | 33 | Case Study 2 -- Oracle ERP Reporting |
| 18 | 34 | Case Study 3 -- Oracle EBS Support |

**Section 5: RISK & ASKS (3 slides)**
| New # | Old # | Title |
|-------|-------|-------|
| 19 | 26 | Risks & Mitigation Part 1 |
| 20 | 27 | Risks & Mitigation Part 2 |
| 21 | 28 | Key Asks |

**Section 6: COMMERCIAL (2 slides)**
| New # | Old # | Title |
|-------|-------|-------|
| 22 | 36 | Managed Service Commercials (HANDS OFF) |
| 23 | 47 | Prerequisites (moved from #29) |

**Section 7: WHY BAYONE & CLOSE (6 slides)**
| New # | Old # | Title |
|-------|-------|-------|
| 24 | 37 | BayOne's Advantage |
| 25 | 05 | Service Offerings (moved from intro) |
| 26 | 09 | Make Tech Purple (moved from intro) |
| 27 | 04 | Technology Stack (moved from intro) |
| 28 | 29 | Summary (3 pillars) |
| 29 | 45 | Closing |

### Biggest Moves
- AI story: position 15 -> position 7 (first quarter of deck)
- Exec Summary: position 8 -> position 2 (first substantive slide)
- Operations Snapshot: position 30 -> position 9 (into solution section)
- KPIs: position 28 -> position 13 (into delivery section)
- Tech Stack/Services/MTP: positions 4-6 -> positions 25-27 (intro to near-close)
- Case studies: now BEFORE risks (build confidence, then address concerns)

---

## 4. Gaps Identified

### Governance/Communication Gap (MODERATE)
Skipped slides 16, 17, 18 were badly executed but the CONCEPT is needed. RFP evaluators expect governance structure. Recommendation: one well-designed slide combining communication model + escalation + governance. Would fit in Section 3 after slide 12.

### Assumptions Gap (MINOR)
Skipped slide 20 (Assumptions) protects BayOne legally. Key assumptions could be folded into slide 47 (Prerequisites) or kept separate.

---

## 5. Open Questions for Colin

1. **Slide 31 (Case Study Title):** Keep as standalone title card for visual pacing, or fold into slide 32?
2. **Governance gap:** Add a new, well-designed governance/communication slide?
3. **Ariat Slide 11 (Enterprise AI Solutions):** Add for AI depth? Has HTML gold standard.
4. **Ariat Slide 05 (Partnership Models):** Add to explain engagement types?
5. **Ariat Slide 12 (Quality Engineering):** Add? Has HTML gold standard.
6. **Closing section length:** Is 6 slides too many? Could Tech Stack (04) be dropped?
7. **Assumptions:** Fold into Prerequisites (47) or separate slide?
8. **Slides 26 + 28 overlap:** Risks Part 1 and Key Asks share content. Deduplicate?

---

## 6. Updated Slide Count

| Category | Count |
|----------|-------|
| Current BUILD slides | 30 |
| Merged (14+24) | -1 |
| Merged (01+02 per crossover recommendation) | -1 |
| Potential adds from Ariat (05, 11, 12) | +3 |
| Potential governance replacement slide | +1 |
| **Estimated final count** | **~32 slides** |
