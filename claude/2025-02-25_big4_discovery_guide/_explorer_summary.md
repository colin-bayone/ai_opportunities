# Session Summary: 2025-02-25_big4_discovery_guide

## Client/Opportunity
**Sephora** - EDW (Enterprise Data Warehouse) Modernization Initiative

## Purpose
This folder contains preparation materials for a discovery discussion meeting between BayOne Solutions and Sephora's technical leadership (Andrew Ho and Grishi Chakraborty) on February 25, 2026. The session was designed to understand Sephora's EDW modernization initiative from a technical execution perspective and gather input to shape a proposal for AI-accelerated modernization services.

## Files

### state.json (261 bytes)
Metadata file tracking the session state: topic is "Sephora EDW Discovery Discussion Guide for Andrew Ho and Grishi Chakraborty," created on 2025-02-25, references original document location in sephora folder.

### source/02_discovery_discussion_guide.md (7.0K)
Markdown version of the discovery discussion guide. Contains meeting purpose, current understanding of Sephora's EDW initiative, questions to explore, three early-stage AI ideas, requests for information, relevant background on BayOne and Colin Moore (Director of AI), discussion guide with core and optional questions, and next steps.

### source/02_discovery_discussion_guide.html (24K)
Professionally formatted HTML version of the same discussion guide with BayOne branding (purple and teal color scheme), styled for presentation and printing. Includes cover page, same content sections as markdown, and footer.

## Key Deliverables

1. **Discovery Discussion Guide** - A structured meeting agenda and question framework designed to:
   - Validate understanding of Sephora's EDW modernization scope (6,000 reports, 8 SSAS cubes, 800+ KPIs, 20+ source systems)
   - Learn from Finance track execution (first track, nearly complete)
   - Explore gaps in current AI tooling (Lutra, Flow mentioned as existing tools)
   - Gather input on three proposed AI acceleration approaches:
     - Pattern Detection & Clustering (batch re-engineering of similar reports)
     - Codebase & Logic Extraction (AI-assisted discovery of buried business logic in legacy code)
     - Validation Acceleration (hybrid deterministic + AI validation of mappings)

2. **Background Positioning** - Documents BayOne's relevant experience:
   - Colin Moore: Led BI/AI at 40,000-employee company, undertook similar EDW modernization to Snowflake
   - BayOne positioning: Tool-agnostic (not a platform vendor), methodology-focused, long-term relationship with Sephora through staffing

3. **Structured Conversation Framework** - 8 core discussion questions covering:
   - Finance track challenges and learnings
   - AI opportunities and gaps
   - Partnership integration
   - Success criteria for pilot engagement

## Cross-References

### Internal to Sephora Engagement
- **Mani**: Strategic stakeholder who previously briefed BayOne on the vision; another discovery meeting being held with technical leads (Andrew Ho, Grishi Chakraborty)
- **Andrew Ho**: Technical leadership, leading semantic layer direction alongside Terti
- **Grishi Chakraborty**: Execution leadership, team responsible for day-to-day modernization work

### Technology & Tools Referenced
- **Current Environment**: SQL Server, IBM Cognos, DataStage, SSAS (8 cubes)
- **Target Environment**: Databricks (data layer), Cognos retained for BI layer
- **Existing AI Tools**: Lutra and Flow (tools already in use; BayOne exploring how to complement)
- **Partner**: Databricks (mentioned as part of governance structure, proposing AI acceleration)

### Governance & Structure
- Core governance table includes: Databricks, Microsoft, Data Platform SMEs, BI SMEs
- Track-based execution model: Finance (complete), with Merchandising and Supply Chain as next tracks
- 3-year modernization timeline with hope to accelerate to 2027

### Long-term Relationship
- BayOne has existing staffing engagement with Sephora
- This proposal is building on that relationship

## Suggested Home
This content should live under the **`/sephora/`** root folder. 

The state.json file indicates the original document location as `sephora/2025-02-25_andrew-meeting-prep/deliverables/02_discovery_discussion_guide.html`, suggesting the proper home is within the Sephora client folder. This appears to be a copy created in the claude session folder for planning/discussion purposes.

---

## Additional Notes

- **Type of Engagement**: Pre-proposal discovery (not yet a formal proposal)
- **Scope**: 3 potential engagement options being prepared for presentation to Mani
- **Next Steps**: 
  - Incorporate feedback into proposal (BayOne, this week of 2025-02-25)
  - Send case studies to Mani (BayOne, next day)
  - Proposal review with Mani (week after next)
  - Request for sample reports from Sephora (as available)
- **Deliverable Format**: Professional HTML with print styling, designed for presentation
- **Confidentiality**: Marked "Confidential — Prepared for Sephora"

