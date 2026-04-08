# Discovery Discussion Guide
## EDW Modernization Partnership
### Prepared for Andrew Ho & Grishi Chakraborty
### February 25, 2026

---

## Meeting Purpose

This is a collaborative working session to deepen our understanding of Sephora's EDW modernization initiative. Mani shared the strategic vision; we're here to learn from Andrew and Grishi's technical and execution perspective.

**Our goal:** Listen, learn, and gather input to shape a proposal that genuinely fits your needs.

---

## 01 | What We Understand So Far

Based on our conversation with Mani, here's our current understanding. We'd welcome your corrections, additions, and perspective.

### The Initiative

| Aspect | Our Understanding |
|--------|-------------------|
| **Project** | EDW Modernization — a 3-year program |
| **Approach** | Re-engineering, not migration (critical distinction) |
| **Source** | SQL Server + IBM Cognos + DataStage |
| **Target** | Databricks (data layer); Cognos retained for now |
| **Philosophy** | Progress over perfection; don't let semantic layer slow momentum |

### The Scale

| Metric | What We've Heard |
|--------|------------------|
| Reports | Thousands (6,000 referenced) |
| SSAS Cubes | 8 |
| KPIs | 800+ |
| Source Systems | 20+ |
| Timeline | 3 years, with hope to accelerate to 2027 |

### The Approach

**Track-Based Execution**
- Finance first (nearly complete)
- Merchandising and Supply Chain as potential next tracks
- Patterns established from Finance to apply forward

**Governance Structure**
- Core table includes Databricks, Microsoft, Data Platform, BI SMEs
- Andrew and Terti leading semantic layer direction
- Grishi's team executing day-to-day modernization

**Question for You:**
> What would you add, correct, or emphasize differently?

---

## 02 | What We'd Like to Learn

We're preparing a proposal for Mani with three engagement options. Your input will shape what we recommend.

### About the Work

| Question | Why It Matters |
|----------|----------------|
| What's been the biggest challenge in the Finance track? | Learn from your experience |
| Where do you see the biggest opportunities for acceleration? | Focus our proposal |
| What would a successful pilot look like to you? | Define success criteria |

### About the Tools

| Question | Why It Matters |
|----------|----------------|
| What's working well with current AI tooling (Lutra, Flow, etc.)? | Build on what works |
| Where are the gaps that current tools don't address? | Find where we can add value |
| What AI approaches have you tried that disappointed? | Avoid repeating mistakes |

### About the Partnership

| Question | Why It Matters |
|----------|----------------|
| How do you see external partners fitting into the governance structure? | Understand our potential role |
| What would make an external partnership valuable vs. overhead? | Ensure we add, not subtract value |
| What's Databricks specifically proposing for AI acceleration? | Understand the landscape |

---

## 03 | Ideas We're Exploring

Based on what Mani shared, we've been thinking about areas where AI might help. These are early ideas — we'd value your reaction.

### Pattern Detection & Clustering

**The Idea:** Rather than treating each report as unique, identify common structures across the portfolio. Reports sharing similar schemas or query patterns could be grouped and re-engineered together.

**Potential Value:** Enable batch re-engineering instead of report-by-report

**Our Question:**
> Does this align with how you're approaching the work? What would make this more or less useful?

### Codebase & Logic Extraction

**The Idea:** Use AI to scan legacy Cognos/SQL code and surface buried business logic, dependencies, and potential risks before they become blockers.

**Potential Value:** Reduce "surprises" during re-engineering; accelerate SME review

**Our Question:**
> Where is buried logic the biggest pain point? How are you currently handling this?

### Validation Acceleration

**The Idea:** Use deterministic + AI hybrid approaches to validate source-to-target mappings, flagging only anomalies for human review rather than reviewing everything manually.

**Potential Value:** Focus SME time on exceptions, not routine verification

**Our Question:**
> What's the current validation burden? Where does it create bottlenecks?

---

## 04 | What We'd Find Helpful

To make our proposal as concrete and useful as possible, we'd benefit from:

| Request | Purpose |
|---------|---------|
| **Sample reports** (if possible) | Understand complexity distribution |
| **Your perspective on pilot scope** | Right-size the engagement |
| **Budget range guidance** | Ensure proposal is realistic |
| **Timeline context** | When does next track start? |

We're not asking you to commit to anything — just help us understand so we can bring something useful back to Mani.

---

## 05 | Our Relevant Experience

For context on why we're here:

**Colin Moore, Director of AI**
- Previously led BI and AI at a 40,000-employee company
- Undertook similar EDW modernization (to Snowflake)
- Direct experience with SSAS/SSRS, Cognos-like environments
- Understands that "re-engineering" is fundamentally different from "migration"

**BayOne's Position**
- Not a platform vendor — we're tool-agnostic
- Can work alongside Databricks and existing tools, not replace them
- Focused on methodology and acceleration, not selling software
- Long-term relationship with Sephora through staffing engagement

---

## 06 | Discussion Guide

### Opening
"Thank you for making time. Mani shared the strategic vision for EDW modernization — we're here to learn from your perspective on what's actually happening in execution. We're preparing a proposal for Mani, and your input will shape what we recommend."

### Core Questions
1. "What's been the biggest challenge so far in the Finance track?"
2. "Where do you see the biggest opportunities for AI to actually help?"
3. "What tools are working? What gaps remain?"
4. "What would success look like for a pilot engagement?"
5. "How should we think about integrating with your governance structure?"

### If Time Permits
6. "Can we get sample reports to make our proposal more concrete?"
7. "What budget range should we be thinking about?"
8. "What should we definitely avoid proposing?"

### Closing
"This has been really valuable. We want to make sure the proposal we bring back to Mani actually fits your reality, not just the strategic vision. What else should we know?"

---

## Next Steps

| Action | Owner | Timeline |
|--------|-------|----------|
| Incorporate your feedback into proposal | BayOne | This week |
| Send case studies as promised to Mani | BayOne | Tomorrow |
| Proposal review with Mani | All | Week after next |
| Sample reports (if agreed) | Sephora | As available |

---

*This is a collaborative working document, not a formal proposal.*
*The formal proposal will follow based on this discussion.*

---

**BayOne Solutions**
Confidential — Prepared for Sephora
