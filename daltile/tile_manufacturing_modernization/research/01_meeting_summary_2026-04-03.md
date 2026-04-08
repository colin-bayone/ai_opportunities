# 01 - Meeting: Summary

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Summary of all Set 01 documents

---

## What Happened

Mahesh Adnani (DalTile/Mohawk Industries IT leader for manufacturing technology) walked Colin Moore through the complete tile manufacturing process via factory walkthrough videos, a PowerPoint process flow diagram, satellite imagery of the Sunnyvale plant, and the existing PI historian dashboard. This was a discovery call between two people with a long-standing personal relationship. The conversation covered the manufacturing process, current technology gaps, Mahesh's modernization vision, and next steps for a potential BayOne engagement.

## Key Findings

### The Opportunity
DalTile has a highly automated tile manufacturing line with virtually zero software visibility into what is happening. Quality testing occurs only at the end of the process (Qualitron, post-kiln), waste tracking is incomplete (finance reports 9% but misses upstream waste), and there is no work order-level lineage tracing. The existing "MES" is actually just a label printing solution written in legacy Progress/OpenEdge code, and the team that maintained it has departed.

### What Mahesh Wants
Two interrelated projects:
1. **MES with work order tracking** — real-time visibility of work orders moving through each stage, yield and waste at every step, lineage tracing, uptime/utilization tracking. A "Cumulus-like" dashboard. This is the primary ask.
2. **Label printer modernization** — replace Progress/OpenEdge code and SATO printer programming with a proper label designer, move from serial ports to Ethernet/TCP-IP. Ideally integrated into the MES.

Aspirational/later-phase items include upstream quality prediction using sensors and cameras, AI/ML for caliber and shade defect prediction, and multi-plant rollout.

### What BayOne Can Offer
Colin demonstrated deep manufacturing domain expertise throughout, drawing parallels to silicon carbide and diamond polishing. He proposed a concrete technical stack (Python, PostgreSQL on Azure, Azure Container Apps) with specific sensor and camera recommendations, reliability engineering principles (factory floor independence from Azure), and communication protocols for the large factory footprint (XBee, RabbitMQ). He also suggested off-the-shelf engineering dashboard platforms (~$20K) as a possible complement.

### Business Parameters
- **Budget:** ~$250K across multiple plants (software only; hardware is a separate team's budget)
- **Timeline:** Urgent ("yesterday would have been better")
- **Starting scope:** One line at Sunnyvale Plant 2 (the larger, older plant near Mahesh's office)
- **Factory scale:** 6 presses, 6 glaze lines, 6 printers, 4 kilns, 5 Qualitrons, 5 sorting lines, 1 palletizer. ~400K sq ft/day production.

## Documents in This Set

| File | Topic |
|------|-------|
| `01_meeting_people_2026-04-03.md` | All people identified, roles, sentiment, dynamics |
| `01_meeting_topic_map_2026-04-03.md` | Topic identification and proposed file breakdown |
| `01_meeting_manufacturing_process_2026-04-03.md` | End-to-end tile manufacturing process flow with all stages |
| `01_meeting_quality_and_waste_2026-04-03.md` | Quality testing gaps, fired vs. green waste, 6% regulatory limit, sensor reliability |
| `01_meeting_current_systems_2026-04-03.md` | Legacy Progress code, PI historian, PLCs, sensors, networking infrastructure |
| `01_meeting_mes_vision_2026-04-03.md` | Mahesh's work order tracking concept, Cumulus-like dashboard, label modernization |
| `01_meeting_technical_recommendations_2026-04-03.md` | Colin's sensor/camera proposals, tech stack, architecture, staffing recommendations |
| `01_meeting_business_context_2026-04-03.md` | Budget, timeline, factory scale, next steps, political dynamics |
| `01_meeting_projects_and_priorities_2026-04-03.md` | Distinct projects identified, immediate vs. aspirational, actual asks to BayOne |
| `01_meeting_summary_2026-04-03.md` | This file |

## Agreed Next Steps

| Owner | Action |
|-------|--------|
| Colin | Visit Sunnyvale factory |
| Colin | Provide rough estimate (with asterisk for hardware costs pending visit) |
| Colin | Send references for off-the-shelf engineering dashboard platforms |
| Colin | Write job descriptions for Mahesh's team hiring (architect, hardware/IoT specialist) |
| Mahesh | Forward factory walkthrough videos and images |
| Mahesh | Finalize NDA with BayOne |

## Open Questions

1. What specific signals are currently available from each piece of equipment that are not being captured?
2. What is the exact network infrastructure on the factory floor (drops, WiFi coverage, interference)?
3. What data does the PI historian currently ingest, and can it be expanded or replaced?
4. What are the three equipment vendors' connectivity capabilities for modern and legacy machines?
5. Can PLC data be extracted to fill the tile tracking gap through WIP buffer areas?
6. What does Mahesh's boss or the hardware team need to see to approve sensor/camera investment?
7. What is the exact scope and effort for the Progress code replacement (how much code, how many sites)?
