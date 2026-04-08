# 01 - Meeting: Summary

**Source:** /cisco/epnm_ems/source/guhan_selva-2-9-2026.txt
**Source Date:** 2026-02-09 (Initial Discovery Meeting, In-Person)
**Document Set:** 01 (First meeting between BayOne and Guhan Selva regarding EPNM-to-EMS)
**Pass:** Summary of all Set 01 documents

---

## Overview

First in-person meeting between Colin Moore (BayOne, Director of AI) and Guhan Selva (Cisco, senior engineering leader) at Cisco offices. The meeting introduced the EPNM-to-EMS UI conversion opportunity and established the working relationship.

## Key Takeaway

Cisco has a legacy network management product (EPNM) with approximately 200 UI screens that major customers are demanding be available in the newer microservices-based product (EMS). The traditional approach of staffing 10 engineers for a year is rejected. Guhan is looking for an AI-accelerated approach that also provides strategic guidance on modernization direction. BayOne is positioned to deliver a POC at its own cost, with Colin running it personally.

## Documents in This Set

| File | Focus |
|------|-------|
| `01_meeting_people_2026-02-09.md` | Attendees, roles, dynamics. Guhan as decision-maker, Colin as technical lead. |
| `01_meeting_topic_map_2026-02-09.md` | Topics identified, proposed file breakdown. |
| `01_meeting_business_drivers_2026-02-09.md` | Why now: customer demand for legacy UI, business pressure, "everything is priority" problem, consolidation of parallel AI efforts. |
| `01_meeting_technical_landscape_2026-02-09.md` | EPNM vs EMS architecture, 45-50M lines of code, Java backend, Dojo vs Angular frontend, three parallel efforts (UI conversion, agentic platform, Azure HD). |
| `01_meeting_bayone_methodology_presentation_2026-02-09.md` | Colin's code modernization approach: simplification, knowledge graphs, Claude Code, LangGraph agent swarms. Guhan interrupted mid-presentation to schedule a deeper session. |
| `01_meeting_security_and_access_2026-02-09.md` | All code on Cisco hardware, Cisco-licensed AI tools, NDA signed, laptop and Cisco ID pending. |
| `01_meeting_next_steps_and_expectations_2026-02-09.md` | POC proposal, 4-week decision timeline, hardware confirmation, priority screen identification, 3:00 PM deep-dive session scheduled same day. |

## Critical Facts Established

1. **Scale:** 45-50 million lines of code across 6-8 products. ~200 UI screens to convert.
2. **Architecture:** EPNM is legacy monolithic (Java + Dojo/JS). EMS is microservices (Java + Angular). Both share Java backends.
3. **Constraint:** Traditional staffing and timeline rejected. Guhan explicitly said the old way of "putting 10 people to it" is "going away."
4. **Strategic need:** Guhan wants more than implementation. He wants guidance on direction, alignment with product lifecycle management, and help consolidating parallel AI efforts.
5. **Security:** Hard perimeter. All work on Cisco hardware with Cisco-licensed tools.
6. **POC model:** BayOne invests at cost to prove capability before scoped engagement.
7. **Key people:** Varel leads the UI conversion team. Meryl leads the agentic AI platform team (based in New York). Both are potential engagement touchpoints.

## Open Questions After Set 01

1. What does "200 screens" mean technically? Are these distinct pages, views, components?
2. Which screens will Guhan's team prioritize for the POC?
3. Was the 3:00 PM deep-dive session recorded or transcribed?
4. What is the exact relationship between the EPNM-to-EMS conversion and Meryl's agentic platform work?
5. What is the commercial model for the POC (hours, fixed, investment)?
6. When will the Cisco laptop and ID be available?
7. What does Guhan mean by "agent-ready" architecture? Is this aspirational or a hard requirement?
8. Product management has not yet made the priority call. When will that happen?
