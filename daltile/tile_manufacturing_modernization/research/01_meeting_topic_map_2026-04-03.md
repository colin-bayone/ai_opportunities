# 01 - Meeting: Topic Map

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Topic identification and proposed deep-dive file list

---

## Major Topics Identified

### 1. Manufacturing Process Flow (End-to-End)
Mahesh walked Colin through the complete tile manufacturing process using factory walkthrough videos and a PowerPoint slide. Covered every stage from raw material prep through to finished goods warehouse, including the process flow diagram (Raw Material, Body Prep, Press, Dryer, Glaze Lines/Glaze Prep, Printer, Kiln, Polishing, Rectification, Qualitron, Sorting, Packaging, Warehouse). Identified where process is continuous vs. semi-continuous (WIP buffer points). Explained the role of each piece of equipment and the conveyor belt automation.

**Rationale for own file:** This is foundational reference material. Every other topic (quality, sensors, MES) depends on understanding this process. Needs exhaustive step-by-step capture.

### 2. Quality and Waste Challenges
Multiple threads: quality testing only happens at Qualitron (post-kiln), fired waste vs. green waste distinction, the 6% regulatory limit on recycling fired tile back into raw material, ceramic engineers' resistance to upstream testing, light curtain sensor unreliability, shade and caliber as the two primary rejection criteria, waste tracking gaps (finance only tracks 9% at sorting but misses waste at every prior stage).

**Rationale for own file:** Quality is the core pain point and the primary value proposition for any solution. Dense with specific numbers, regulatory constraints, and organizational friction.

### 3. Current Systems and Technology Landscape
The existing "MES" is actually just a label printing solution written in Progress/OpenEdge with SATO printer language. Three-person legacy team departed/retiring. Serial port connections to printers. PI historian database exists at some sites with sensor data. The semi-MES dashboard (shown via Eric William's email) provides some visibility into press/glaze/kiln throughput but no work order correlation and unreliable sensor counts. LGVs (automated guided vehicles) for material transport. PLCs throughout, mix of old and new controllers (Siemens observed).

**Rationale for own file:** Understanding the existing technology baseline is critical for scoping the modernization. Multiple systems, legacy code, and infrastructure constraints.

### 4. Mahesh's Vision: Work Order Tracking and MES
Mahesh's end-state vision: a Cumulus-like MES showing real-time work order progress through each stage, yield at each step, waste tracking, label design capability, and work order-level lineage tracing. He walked through a spreadsheet concept showing work order number, item number, and stage-by-stage equipment assignment (Press 2, Glaze 2, Printer 2, Kiln 7, etc.) with barcode scanning at each handoff. Includes private-label support (Home Depot, DalTile own brand).

**Rationale for own file:** This is the client's articulated requirement. Needs precise capture of what Mahesh described, what he prioritized, and what he deferred to later phases.

### 5. Colin's Technical Recommendations and Solution Ideas
Colin's specific suggestions: humidity sensors at kiln output for caliber prediction, cameras with industrial-grade dust protection (purge gas, windshield wipers, IP-rated housings), PLC data extraction for tile tracking through WIP areas, RabbitMQ for high-throughput data ingestion, XBee radio communication for factory floor networking, Python/PostgreSQL/Azure Container Apps tech stack, separation of concerns for Azure vs. factory floor reliability. Also referenced off-the-shelf engineering dashboard platforms (~$20K for full factory).

**Rationale for own file:** Colin's technical input is the basis for BayOne's solution architecture. Needs separate capture from Mahesh's vision because it represents what BayOne can actually deliver vs. what the client imagines.

### 6. Business Context: Budget, Timeline, Scope, and Next Steps
Budget: ~$250K across multiple plants (software only, hardware separate budget under different team). Timeline: "yesterday" (urgent). Scope: Start with one line at Sunnyvale (Plant 2, the larger/older plant; Plant 1 is smaller and nearby). Two potential projects discussed: (1) MES with work order tracking and visibility, (2) Progress code modernization/label printer redesign. Next steps: Colin to visit factory, provide rough estimate, send engineering dashboard platform references, write JD for Mahesh's team. Factory has 6 presses, 6 glaze lines, 6 printers, 4 kilns, 5 Qualitrons, 5 sorting lines, 1 palletizer. Production: ~400K sq ft/day per plant.

**Rationale for own file:** Commercial and logistical details that drive scoping and pricing. Separate from technical content because different audience (proposal writers, pricing models).

---

## Proposed Deep-Dive Files

| # | Filename | Topic | Agent? |
|---|----------|-------|--------|
| 1 | `01_meeting_manufacturing_process_2026-04-03.md` | End-to-end tile manufacturing process flow | Yes |
| 2 | `01_meeting_quality_and_waste_2026-04-03.md` | Quality challenges, waste tracking gaps, regulatory constraints | Yes |
| 3 | `01_meeting_current_systems_2026-04-03.md` | Existing technology: legacy MES, PI historian, PLCs, sensors, networking | Yes |
| 4 | `01_meeting_mes_vision_2026-04-03.md` | Mahesh's vision for work order tracking, MES, label modernization | Yes |
| 5 | `01_meeting_technical_recommendations_2026-04-03.md` | Colin's solution ideas: sensors, cameras, architecture, tech stack | Yes |
| 6 | `01_meeting_business_context_2026-04-03.md` | Budget, timeline, scope, factory scale, next steps | Yes |
