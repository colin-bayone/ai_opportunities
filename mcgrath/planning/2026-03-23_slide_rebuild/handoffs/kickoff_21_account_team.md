# Kickoff: Account Management Team Slides (3 slides)

## Copy-paste the prompt below into a new Claude session

---

You are building three HTML slides showing BayOne's proposed account management team for a McGrath RFP response. These are people slides with real photos, bios, and a governance structure.

**You have actual headshot images to use.** This is NOT a text-only situation. The images are at:
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/source/bio_pics/`

Files: `amit.jpg`, `colin.jpg`, `kishore.jpg`, `neha.jpg`, `sripriya.jpg`, `surej.jpg`, `zahra.jpg`

Reference these with relative paths from wherever your HTML files live (e.g., `../source/bio_pics/neha.jpg`). These are real photos that should be displayed as circular headshots.

---

## What to Build

### Slide A: Proposed Account Management Team (Org Chart + Governance)

**Source PNG:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_30/slide_30.png`
**Source content:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_30/content.md`

**Content -- Leadership row (top, 3 people):**
- **Surej KP** -- Executive Sponsor, CEO (surej.jpg)
- **Neha Malhotra** -- Account Owner, VP Growth & Customer Success (neha.jpg)
- **Sripriya K.** -- Technical Exec Sponsor, CTO (sripriya.jpg)

**Content -- Operations row (bottom, 4 people):**
- **Zahra Syed** -- Sr. Relationship Manager, Co-Account Owner (zahra.jpg)
- **Amit Grover** -- Delivery Manager, VP Solutions & Delivery (amit.jpg)
- **Colin Moore** -- Head of AI, Director of AI (colin.jpg)
- **Kishore Elimineti** -- Governance Lead, Program Leader (kishore.jpg)

**Governance & Review Cadence table:**

| Cadence | Participants | Focus |
|---------|-------------|-------|
| Weekly | Kishore + MGRC leads | Operational review, ticket health, SLA tracking |
| Monthly | Neha + Amit + MGRC management | Service delivery, CSAT, resource planning |
| Quarterly | Neha + Surej + Sripriya + MGRC VP | Strategic review, transformation roadmap |
| Annual | Full leadership team | Partnership roadmap, long-term planning |

**Design:** Circular headshots with name, role title, and subtitle beneath each. Top row (3) centered, bottom row (4) centered below. Visual hierarchy showing leadership tier above operational tier (connecting lines or layout positioning). Governance table below in a clean card or styled table. Use the BayOne purple design system.

---

### Slide B: Key Team Biographies (Page 1 -- 4 people)

**Source PNG:** `slide_31/slide_31.png` (same base path as above)
**Source content:** `slide_31/content.md`

**Bios (use exact text from content.md):**

1. **Neha Malhotra** -- Account Owner | VP, Growth & Customer Success (neha.jpg)
   25 years delivery experience, founding team member, $80M+ revenue scaling, Fortune 500 relationships, deep MGRC knowledge, founded #MakeTechPurple. San Jose State University.

2. **Zahra Syed** -- Sr. Relationship Manager | Co-Account Owner (zahra.jpg)
   C-level partnership builder, cultivated relationships with MGRC senior IT leadership, day-to-day relationship bridge. UC Irvine.

3. **Surej KP** -- Executive Sponsor | CEO & Board Member (surej.jpg)
   Previously CEO Intelliswift, CTO UST Global, Practice Head Cognizant, Regional Director TCS. Harvard Executive Leadership. Personal commitment to MGRC partnership.

4. **Amit Grover** -- Delivery Manager | VP, Solutions & Delivery (amit.jpg)
   Previously Senior Regional Director HCL (70+ professionals), Senior Manager Infosys (Supply Chain, Finance), SDM Zensar ($25M+ portfolio). BITS Pilani. Based in Pleasanton.

**Design:** Each bio gets a row: circular headshot on the left, name + role title on the right in bold, bio paragraph below. Purple accent dividers between bios. Clean, professional, not a resume dump.

---

### Slide C: Key Team Biographies (Page 2 -- 3 people)

**Source PNG:** `slide_32/slide_32.png`
**Source content:** `slide_32/content.md`

**Bios:**

1. **Sripriya Kalyanasundaram** -- Technical Executive Sponsor | CTO (sripriya.jpg)
   Harvard Business School, previously President LambdaTest, Strategy & Analytics Deloitte, SVP UiPath, Global Delivery Leader Cognizant. AI-first mindset, women in tech advocate. Executive-level technical oversight for MGRC.

2. **Colin Moore** -- Head of AI & Innovation | Director of AI (colin.jpg)
   Leads BayOne's AI practice. Previously AI/ML Manager at Coherent Corp. Core expertise: AI, LLMs, Deep Learning, IPA. Delivered enterprise AI solutions including CI/CD pipeline automation. Leads BayOne's three-horizon AI enablement roadmap for MGRC. Duquesne University.

3. **Kishore Elimineti** -- Governance Program Lead | Program Leader (kishore.jpg)
   Up to $100M+ programs, end-to-end Oracle Fusion Cloud implementations. Former Oracle Corporation (Redwood City campus, SAFe adoption, M&A integrations including $5.3B Micros). Managed Oracle Fusion migrations at Albertsons. SAFe PM, Agile Scrum Master, Stanford Advanced PM. Currently embedded at MGRC leading NextGen transformation steering committee.

**Design:** Same layout as Slide B for consistency. Three bios, same row pattern.

---

## Design References

Read these before building:
- Gold standard slides: `claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`, `slide_02_*.html`, `slide_03_*.html`
- Previously approved slides in `claude/2026-03-23_mcgrath_slides/slides_output/` (especially slide_01 for the purple gradient visual treatment)
- Build feedback: `claude/2026-03-23_mcgrath_slides/planning/04_slide_build_feedback.md`

### Design System
- **Canvas:** 16:10, max-width 1100px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`
- **Typography:** Inter (300-700)
- **Headshot styling:** Circular crop (`border-radius: 50%`), `object-fit: cover`, consistent size (e.g., 80-100px for org chart, 70-80px for bio rows), subtle border or shadow
- **No em dashes.** No contrastive framing. No colloquial language.
- **No Playwright unless Colin explicitly asks.**
- **Do NOT modify the bio text** -- build faithfully from content.md.

## Output
- `slides_output/slide_account_team_org.html`
- `slides_output/slide_account_team_bios_1.html`
- `slides_output/slide_account_team_bios_2.html`

When complete, tell the user and describe your design choices.
