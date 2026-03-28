# Handoff 16 Results: 3 Ariat Addition Slides

## Status: COMPLETE

All three slides built and output to `slides_output/`.

---

## Slide 1: Partnership Models

**File:** `slides_output/slide_new_partnership_models.html`
**Source:** Ariat slide 05 (no HTML gold standard; designed from scratch using deck design language)
**Layout:** 2x2 card grid with numbered badges (01-04), bottom context bar

### Design Decisions
- Modeled after the Enterprise AI Solutions 2x2 card grid pattern, adapted for fewer items per card (3 feature bullets each vs 4)
- Managed Services card highlighted as "Recommended for McGrath" with subtle border treatment and a small badge
- Bottom context bar with two callouts: "Blended Approach" (models can be combined) and "Evolve Over Time" (transition across Years 1-3)

### McGrath Tailoring
- Managed Services framed around Oracle Fusion, Salesforce, and integration support with SLA-driven delivery
- Fixed Capacity references quarterly Oracle patches and institutional knowledge
- T&M positioned for enhancement requests and transformation projects
- Managed Projects references QA automation and integration projects specifically
- Bottom bar references the Year 1/2/3 pricing structure from the RFP

### Icons Used (no duplicates)
- Card headers: number badges (01-04)
- M1: fa-handshake, fa-gauge-high, fa-arrows-spin
- M2: fa-clock, fa-sliders, fa-file-invoice-dollar
- M3: fa-users, fa-calendar-check, fa-building-columns
- M4: fa-bullseye, fa-shield-halved, fa-flag-checkered
- Context bar: fa-puzzle-piece, fa-rotate

---

## Slide 2: Enterprise AI Solutions

**File:** `slides_output/slide_new_enterprise_ai.html`
**Source:** Gold standard `slide_02_enterprise_ai_solutions.html`
**Layout:** 2x2 card grid (identical structure to gold standard)

### Changes from Gold Standard
- Header title: "McGrath Support Proposal" (was "Enterprise AI Capabilities")
- Lead subtitle: Added "within your Oracle Fusion and enterprise ecosystem"
- **HR card tagline:** "across Oracle Fusion HCM" added; Onboarding item references "Fusion HCM"; Workforce Analytics references "across business units"
- **Finance card tagline:** References "Oracle Fusion Financials, RecVue billing, and Avalara tax"; Invoice item references "in Fusion"; Reporting item references "ARCS and FRS"; Forecasting item references "EPBCS"
- **Legal card tagline:** "across your vendor landscape" added; CLM item references "Salesforce CLM"; Compliance item references "SOC 2, PCI, NIST" (McGrath's actual compliance frameworks)
- **Marketing card tagline:** "connected to Salesforce CRM" added; Personalization references "Customer Hub"; Analytics item references "Tableau and Snowflake"

### What Stayed the Same
- All card icons preserved from gold standard
- All item icons preserved from gold standard
- CSS structure identical (copied from gold standard)
- Card layout, border treatments, gradient colors all preserved
- All four capability item titles preserved verbatim

### Slide number: 08 (placeholder, follows AI Strategy at 07)

---

## Slide 3: Quality Engineering

**File:** `slides_output/slide_new_quality_engineering.html`
**Source:** Gold standard `slide_03_quality_engineering.html`
**Layout:** Chevron flow bar + 3x2 detail card grid (identical structure to gold standard)

### Changes from Gold Standard
- Header title: "McGrath Support Proposal" (was "Enterprise AI Capabilities")
- Lead subtitle: Added "for McGrath's Oracle Fusion and integration landscape"
- **Test Case Clustering:** Tagline references "quarterly Oracle patches"; Similarity Analysis references "by Fusion module"; Reduced Manual Effort references "replacing today's 100% manual testing approach" (key McGrath pain point from RFP)
- **Intelligent Routing:** Tagline references "tickets and test decisions across your integration landscape"; Industry Adaptable renamed to "Multi-Vendor Routing" referencing Oracle, Salesforce, MuleSoft teams
- **Root Cause Analysis:** Tagline references "50+ integrations"; Dependency Mapping references "MuleSoft, OIC, and Fusion"; Cascade Detection references "integration failure triggers"; Impact Detection references "systems and integration points"
- **Agentic Diagnosis:** Tagline references "configurations and integrations"; Codebase Exploration renamed to "Configuration Analysis" referencing "Fusion and integration settings"; Pattern Learning references "quarterly patch cycles"
- **Visibility Dashboard:** Tagline references "MuleSoft, OIC, and Oracle Fusion deployment stack"; Unified Interface now references "integration health"; Conversational Queries example changed to "Which integrations failed last night?"; Failure Attribution references "vendor or system responsible"; Changed fa-layer-group to fa-desktop to avoid duplicate icon
- **Automated Testing:** Tagline reframed as "End-to-end test automation with regression coverage for quarterly Oracle Fusion releases"; Playwright UI/UX renamed to "UI/UX Testing" referencing "Customer Hub and Oracle Fusion interfaces"; Unit Test Coverage renamed to "Integration Coverage" referencing "50+ connection points"; Regression Analysis references "per quarterly patch"

### What Stayed the Same
- Chevron flow bar with 6 items (identical names, identical CSS)
- Card grid structure and layout
- All gradient colors and border treatments
- Most card header icons preserved
- CSS structure identical (copied from gold standard)

### Slide number: 09 (placeholder, follows Enterprise AI at 08)

---

## Quality Checklist

| Check | Partnership Models | Enterprise AI | Quality Engineering |
|-------|-------------------|---------------|---------------------|
| Header: BayOne logo + McGrath Support Proposal | Yes | Yes | Yes |
| Footer: gradient bar + slide number | Yes | Yes | Yes |
| 16:10 aspect ratio | Yes | Yes | Yes |
| Inter font, Font Awesome icons | Yes | Yes | Yes |
| Purple gradient palette | Yes | Yes | Yes |
| No em dashes in text | Yes | Yes | Yes |
| No contrastive framing | Yes | Yes | Yes |
| No icon duplicates within slide | Yes | Yes | Yes (fixed fa-layer-group) |
| McGrath-specific content woven in | Yes | Yes | Yes |
| Compared against gold standard | N/A (new design) | Yes | Yes |

## McGrath Details Woven In

From RFP documents, the following McGrath-specific details were incorporated across slides:
- **Oracle Fusion** (ERP, HCM, Financials, SCM, ARCS, FRS, EPBCS)
- **Salesforce** (CRM, CPQ, CLM)
- **MuleSoft / OIC** (50+ integrations)
- **RecVue** (billing), **Avalara** (tax)
- **Snowflake / Tableau** (data and analytics)
- **Customer Hub** (nopCommerce portal)
- **FreshService** (ITSM)
- **100% manual testing** (current state, key pain point)
- **Quarterly Oracle patches** (regression testing trigger)
- **SOC 2, PCI, NIST compliance** frameworks
- **P1-P4 SLA structure** and Year 1/2/3 pricing model
- **Shared Responsibility** model preference
