# 01 - Meeting: People

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** People identification, roles, sentiment, dynamics

---

## Participants on the Call

### Mahesh Adnani (DalTile / Mohawk Industries)
- **Role:** IT leader responsible for manufacturing technology at DalTile. Manages the team that supports the existing MES (Manufacturing Execution System) label printing system. Recently inherited a three-person team that wrote the legacy Progress/OpenEdge code for the sorting line label printers.
- **Background:** Not a ceramic engineer by background ("I'm not a tile guy"). Came into this role and is evaluating the manufacturing technology landscape with fresh eyes. Sees the inefficiencies clearly and is frustrated by the status quo.
- **Ownership:** Controls the software budget for manufacturing systems. Has a budget of approximately $250,000 for MES modernization, though that is across multiple plants. Also responsible for label printing, sorting line integration, and the custom Progress code that communicates with PLCs on the factory floor.
- **Sentiment:** Highly motivated, technically curious, and action-oriented. Uses phrases like "I want to kill Progress" and "this is stupid" when describing legacy systems. Genuinely excited about modernization possibilities. Very open and transparent about budget, constraints, and organizational challenges. Shares factory videos, satellite imagery, and internal dashboards freely.
- **Key behaviors:** Took factory walkthrough videos personally to share with Colin. Showed internal PI historian dashboards, satellite imagery of plant layout, and the existing semi-MES system. High trust relationship with Colin, evidenced by personal conversation (wife's AI agency, home repairs).
- **Decision-making:** Has budget authority for software. Hardware (PLCs, sensors) falls under a different team's budget, but Mahesh wants to take initiative and show what is possible to convince that team.
- **Organizational position:** His head office is approximately 20 minutes from the target factory (Sunnyvale plant). Wants to start with this factory because of proximity and because it is the older factory with more room for improvement.

### Colin Moore (BayOne Solutions)
- **Title:** Director of AI
- **Role:** Technical lead, discovery, solution architecture. This is a personal relationship with Mahesh, not a cold sales engagement. Colin brings manufacturing domain knowledge from prior work (diamond polishing, silicon carbide manufacturing at Coherent Corp).
- **Sentiment:** Genuinely excited ("This is gonna be a lot of fun"). Technically engaged throughout, offering specific insights about sensors, cameras, humidity measurement, PLC communication protocols, industrial-grade equipment. Not in sales mode; more like a consulting engineer having a peer-to-peer technical conversation.
- **Key observations:** Noticed specific details from the factory videos (serial port on the blue screen computer, 8020 aluminum struts for camera mounting, Siemens PLCs on the wall). Offered to write a job description (JD) for Mahesh's team hiring. Mentioned Sephora EDW modernization engagement as a credibility proof point.
- **Technical contributions:** Drew parallels to silicon carbide manufacturing, diamond polishing. Suggested humidity sensors at kiln output for caliber prediction. Proposed RabbitMQ for high-throughput data ingestion. Mentioned XBee-type radio communication for factory floor networking. Recommended Python, PostgreSQL on Azure, Azure Container Apps as the tech stack.

## People Mentioned but Not Present

### Yogesh (BayOne Solutions)
- **Role:** Appears to be a BayOne leadership figure. Mahesh has spoken with Yogesh previously about the Progress code modernization. Colin references calling Yogesh about internal operational friction at BayOne. Rahul is described as "Yogesh's counterpart."
- **Context:** Mahesh asked Yogesh whether BayOne could take the Progress code and modernize it as a fixed-bid project.

### Rahul (BayOne Solutions)
- **Role:** Described as "Yogesh's counterpart" at BayOne. Colin tells a story about Rahul questioning Colin's direct approach with Cisco ("What the hell are you doing? Did you just tell Cisco no?").
- **Context:** Referenced in an anecdote about Colin's sales approach, not directly related to DalTile.

### Mahesh's Wife
- **Context:** Recently opened an AI agency. Partnered with an ex-colleague in Texas to provide AI training programs for engineers adopting AI, plus lead generation services. Mahesh mentioned she would like to connect with Colin at some point.

### The Three-Person Legacy Team (DalTile)
- **Context:** A team that Mahesh inherited. They wrote the Progress/OpenEdge code that manages label printing on the sorting line. They also created their own servers and network infrastructure (including serial port connections). Two have left and one is retiring. Their departure is part of the urgency, as institutional knowledge of the legacy system is disappearing.
- **Significance:** This team's departure creates both urgency (no one left to maintain Progress code) and opportunity (clean slate for modernization).

### One Junior Person (DalTile)
- **Context:** Currently doing labeling work. Has some development skills. Mahesh sees potential for her to transition to Python or whatever the new stack requires, but is uncertain about the extent of her capabilities.

### Eric William (DalTile)
- **Context:** Referenced when Mahesh was searching Outlook for an email showing the existing PI historian dashboard/semi-MES system. Appears to be a colleague at DalTile who shared or built the existing visibility dashboard.

### Equipment Vendors (Three Companies)
- **Context:** Three companies supply virtually all tile manufacturing equipment globally (presses, dryers, glaze lines, printers, kilns, polishing, rectification). They also manufacture tiles themselves and sell branded tiles to competitors. One is identified as "Scamia" (likely SACMI, an Italian ceramics equipment manufacturer). Another is "Colletron" (likely Qualitron, for shade and caliber quality inspection). A third is described as a surface/in-surface defect tracking company.
- **Significance:** These vendors control the machine ecosystem. Sites rely on vendor-provided configurations rather than developing their own process engineering. This creates both a dependency and an opportunity for DalTile to differentiate through custom engineering.

## Relationship Dynamics

- **Colin and Mahesh:** Long-standing personal relationship. Mahesh appears to have previously helped Colin with RFP strategy (Colin: "Everything that you said was exactly right" about a recent RFP). They share personal life updates freely. Mahesh calls Colin by name, trusts him with sensitive internal data. This is a relationship-driven engagement, not a competitive bid.
- **Mahesh vs. Ceramic Engineers:** Mahesh is frustrated that ceramic engineers claim "you can't do testing till it is baked." He sees this as a barrier to upstream quality detection and wants to challenge it with data.
- **Mahesh vs. Finance:** Argues with finance about the true waste percentage. Finance tracks 9% waste at the sorting line (fired waste), but Mahesh sees untracked waste at press, dryer, glaze, and printer stages.
- **Mahesh vs. PLC/Hardware Team:** The hardware/PLC budget is controlled by a separate team that "is not thinking right." Mahesh wants to take initiative with his software budget to demonstrate what is possible and force their hand.
