# 01 - Meeting: Colin's Technical Recommendations

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Focused deep dive on technical recommendations and solution architecture

---

## 1. Manufacturing Domain Expertise and Cross-Industry Parallels

### Silicon Carbide Manufacturing Analogy

Colin immediately recognized the Daltile tile manufacturing process as structurally identical to silicon carbide manufacturing. His specific comparison: instead of water drying out (as in tile), you are drying out a solvent; instead of a hydraulic press, you have a Cold Isostatic Press (CIP) to form blanks from raw material. The kiln firing, WIP staging, and post-fire quality inspection stages all follow the same pattern. This parallel gives Colin direct experiential knowledge of the process engineering challenges Mahesh described, particularly around upstream quality detection and post-fire waste.

### Diamond Polishing Analogy (Coherent Corp Parallels)

Colin drew a second parallel to diamond polishing to address Mahesh's concern that ceramic engineers claim "you can't do testing until it is baked." Colin's counterpoint: diamond as-grown is super rough and opaque -- you cannot see through it. After polishing, it becomes transparent. The tile process is the same: after printing, the tile shows its color, then a white protective glaze coat is applied (making it opaque again), and only after kiln firing does the final color emerge. Colin's argument: you can absolutely correlate upstream measurements to downstream outcomes. The claim that you cannot know quality before firing is a common process engineer assertion that is demonstrably false if you have the data to build the correlation. This is not a theoretical position -- Colin has done this in analogous industries.

### Upstream Quality Detection Principle

Colin stated his position clearly: "It is not true. You can definitely do it. You just need the data to say this to correlate back." His reasoning: if all else is constant and the kiln is constant, you get constant output. If something is different upstream, you can track that difference because you will have earlier process steps with sensor data. The two primary rejection categories (shade and caliber) are both amenable to upstream detection:

- **Shade** is a function of the glaze line, printer, and kiln conditions -- all measurable
- **Caliber** (thickness, flatness, dimensional conformance) is a function of raw material moisture content and kiln conditions -- both measurable

Colin predicted with high confidence that correlating raw material moisture content plus kiln output humidity to caliber outcomes would yield actionable predictive data. He stated: "I promise that without knowing much about this, that's something that's missing."

---

## 2. Sensor and Camera Recommendations

### Humidity Sensors at Kiln Output

Colin's most specific sensor recommendation: place humidity sensors at the output of the kiln to capture the moisture content of tiles post-firing. This is the "missing data point" that would allow correlation of raw material moisture (input) + kiln conditions (process) to caliber outcomes (output). He described this as "really basic" but "definitely worth it" for something like this process. The combination of raw material moisture specs plus kiln output humidity would enable prediction of caliber with "pretty good accuracy, assuming that everything else is constant."

### Industrial-Grade Camera Protection for Dusty Environments

Mahesh raised the concern that the factory floor is dusty and sensors/cameras get dirty, causing unreliable data (the light curtain sensors already have this problem -- they produce phantom counts when obstructed). Colin provided three specific solutions for camera protection in dusty industrial environments:

1. **Purge gas** -- a gas line near the camera that keeps dust away from the lens. Common in industrial settings.
2. **Windshield wipers** -- cameras with built-in miniature wipers that clean the lens automatically. These are industrial-grade cameras made specifically for this purpose.
3. **IP-rated housings** -- selecting sensor and camera hardware with the correct Ingress Protection rating for a dust environment. Colin's shortcut for specifying the right IP rating: "We'll be cheating because we'll just look at what spec the equipment itself is rated at, and that'll be the same as the sensor spec." In other words, match the IP rating of the new sensors/cameras to the existing equipment ratings already deployed on the factory floor.

### Camera Mounting on Existing 80/20 Aluminum Struts

Colin observed from the factory videos that there is extensive 80/20 aluminum extrusion framing throughout the factory. These are extruded aluminum structural members with T-slot channels -- industry standard for mounting equipment, sensors, cameras, and other accessories. Colin noted that the 80/20 is "already there for the most part," meaning camera installation would be physically straightforward: mount directly to existing struts without building new infrastructure. He also observed that proper guarding (safety enclosures) is already in place around the automated equipment, which creates additional mounting opportunities and defined sightlines for cameras.

### Camera Count Estimate

When Mahesh asked whether 15-20 cameras per line would be sufficient, Colin confirmed yes, and suggested it might be possible to get away with fewer. He said the factor that typically drives him toward fewer cameras is network complexity rather than coverage needs. He proposed scoping three tiers during a site visit: minimum required, ideal, and overkill. His approach would be to do quick tests on-site to determine the right number.

### Existing Sensor Data -- Low-Hanging Fruit

Colin emphasized that before adding new sensors, Mahesh should inventory what signals the existing equipment already produces but nobody is capturing. Every piece of equipment has built-in sensors: the presses have sensors that measure pressing force, the glaze lines have light curtains (some of which measure glaze thickness, not just presence), and the kilns have temperature sensors. Colin's recommendation: figure out what signals are "for free" before specifying new hardware.

### Light Curtain Observations

Colin noted that the light curtains in the glaze line may be more sophisticated than Mahesh realized. Some light curtains are set at an angle and measure the thickness of the glaze coating, not just whether a tile is passing through. This is an important distinction because glaze thickness is a quality-relevant parameter that may already be available as data.

---

## 3. PLC Data Extraction and Tile Tracking Through WIP Areas

### The Core Tracking Problem

Mahesh described the fundamental traceability challenge: tiles travel in continuous pairs through press, dryer, glaze, and printer stages, but then enter WIP staging areas before the kiln where tiles from multiple lines are stacked together. After kiln firing, there is no way to correlate which tiles came from which upstream line or work order. The Pi historian dashboard Mahesh showed demonstrates this gap -- it tracks machine-level throughput (square footage in, square footage out) but has no work-order-level lineage through the kiln and WIP stages.

### Colin's PLC-Based Solution

Colin's key insight: since everything in the WIP staging areas is PLC-driven (automated stackers, conveyors, LGVs), the tile movement is predictable and deterministic. There is no human in the loop moving tiles randomly. Colin compared this to the self-driving vehicle principle: "It only works if all the vehicles are self-driving." Because the PLC-driven movement follows programmed logic, even when tiles are out of camera vision (inside the kiln, stacked in WIP drawers), their location can be inferred from the PLC control logic.

Colin's recommendation: extract the movement logic from the PLCs to build a deterministic tracking model. If the PLC tells a stacker to place a tile in position X of rack Y, and the PLC later tells the kiln feeder to pull from rack Y position X, the lineage is preserved computationally even without visual tracking. Colin stated this could be validated "very quickly to make sure that's a valid idea in the first place."

### Siemens PLC Identification

Colin observed from the factory videos that some of the PLC controllers on the walls appeared to be Siemens (or possibly Celine -- likely Siemens S7 series based on context). He noted a mix of older and newer equipment, with some controllers being quite modern. This is relevant because modern Siemens PLCs support OPC-UA and other standardized data extraction protocols, while older ones may require different integration approaches.

### Serial Port Observation (Label Printer)

Colin noticed a specific technical detail in the video of the label printing station (video 12): the blue-screen Progress-language computer controlling the label printer has a serial port visible on its side. This serial port is the communication link to the SATO label printer. Colin's assessment: "That is something that we can definitely talk to. Even if you were to take that computer away..." -- meaning the printer's serial interface can be driven by a modern replacement system. The fact that it is serial (RS-232) rather than some proprietary protocol makes replacement straightforward.

---

## 4. Communication Protocols and Factory Networking

### XBee Radio Communication for Factory Floor

Mahesh raised the challenge that the manufacturing floor has poor network infrastructure -- the facility is enormous compared to the office footprint, Ethernet drops are expensive, and WiFi is unreliable in the dusty environment with heavy equipment. Colin recommended XBee radio modules as the solution. XBees are radio communication devices commonly used in exactly this type of large, distributed factory environment where traditional networking is impractical.

Colin's reasoning for XBees:
- The factory floor is flat and open (warehouse-style high ceilings) -- ideal for radio propagation
- No need for network drops or strong WiFi coverage
- Can transmit sensor data back to one or a few central collection points
- The only environments where XBees struggle are those with a lot of metal obstructions or large AC motors creating electromagnetic interference -- Daltile's factory does not have these problems based on the video walkthrough

### RabbitMQ for High-Throughput Sensor Data Ingestion

Colin recommended RabbitMQ as the message broker for ingesting sensor data. His reasoning: Mahesh mentioned wanting to capture press readings every 5 minutes across equipment producing 400,000 square feet per day -- this is high-throughput data ingestion. Colin specified that RabbitMQ provides:

- **Task queuing** -- sensors and data sources publish messages; workers consume and process them asynchronously
- **Distributed load** -- can handle the volume from multiple lines, multiple factories without bottlenecking
- **High throughput** -- designed for exactly the kind of continuous, high-volume data stream that manufacturing sensor networks produce

Colin's framing: the throughput requirement is what "changes one specific thing in this, which is the communication protocol." If the data volume is high, RabbitMQ is "almost always" the right choice.

---

## 5. Technology Stack and Architecture

### Core Stack

Colin specified the following technology stack:

| Component | Technology | Rationale |
|---|---|---|
| Programming language | Python | "100%. Python." No elaboration needed -- it is the standard for this type of work |
| Database | PostgreSQL on Azure | Cost-optimized; Colin specified "Postgres on Azure" rather than SQL Azure (Azure SQL Database), suggesting Flexible Server for PostgreSQL |
| Deployment | Azure Container Apps | Cost-optimized containerized deployment |
| Cloud platform | Azure | Daltile already has Azure; aligns with Colin's standard practice |
| Message broker | RabbitMQ | High-throughput sensor data ingestion and task queuing |

Note: Mahesh asked "database would be SQL Azure?" and Colin corrected to "Postgres on Azure." This is a deliberate choice -- PostgreSQL is more cost-effective than Azure SQL Database for this workload profile and avoids Microsoft SQL Server licensing costs.

### Off-the-Shelf Engineering Dashboard Platforms

Colin recommended that Mahesh consider an off-the-shelf engineering dashboard platform rather than building custom visualization from scratch. Key details:

- **Cost:** approximately $20,000 for a full factory
- **Capabilities:** configurable engineering dashboards with drag-and-drop interfaces; described as "almost looks like C#" in the builder -- low-code/no-code but "also actually a real thing, not like an up and coming thing"
- **Use case:** if sensors are already producing data and the need is for visualization, the dashboard platform handles the front end while the custom-built system handles the back end (data collection, ingestion, processing, storage)
- **Caveat:** "You have to build the system that connects to it" -- the dashboard platform is a visualization layer, not the complete solution

Colin offered to send Mahesh specific platform recommendations. This positions the dashboarding as a separate concern from the data infrastructure, which is sound architecture.

---

## 6. Reliability Engineering: Separation of Azure and Factory Floor

### The Principle

Colin articulated a core architectural principle: "Total separation of concerns. Azure being up or down, existing or not existing, shouldn't impact anything on the factory, and vice versa. We'll call it reliability engineering."

This was prompted by Mahesh raising a critical constraint: the label printing system has a three-second window to detect an incoming box, print the label, apply it, and release the box. If Azure latency exceeds that window, the entire conveyor belt stops. More broadly, if the Internet goes down, manufacturing cannot stop.

### On-Premises Processing for Latency-Critical Operations

Colin agreed completely with Mahesh's concern and extended it to a general principle:

- **Anything latency-critical** (such as the 3-second label printing window) must run on premises with no dependency on cloud connectivity
- **On-prem language models** -- Colin specifically noted that for manufacturing use cases, large language models should be on-premises, not cloud-hosted: "Do not touch a language model that's online if it's for manufacturing. That's one of those niche use cases where it's actually good to have it on prem... you can always guarantee that it's online as long as the power's on."
- **Azure as data lake and analytics** -- cloud is for aggregation, historical analysis, dashboarding, and non-time-critical functions
- **Local files or services on the factory floor** -- Mahesh mentioned "a sliver of some files or whatever else" on the factory floor, and Colin agreed this is the right approach for ensuring continuity

### Historian Database Consideration

Mahesh mentioned that some Daltile sites already have PI historian databases collecting machine data. Colin acknowledged this is the right tool for time-series machine data ("Historian for that"). The historian handles the high-frequency, high-volume machine telemetry (press cycles, temperatures, etc.) while the MES-level system handles work order tracking, lineage, and quality correlation.

---

## 7. Shop Traveler Concept for Work Order Tracking

When Mahesh described his vision for a work order tracking system -- where a planner specifies which press, glaze line, printer, kiln, quality station, sorting line, and packaging line a work order will use, and operators scan to start and complete each stage -- Colin immediately named this pattern: "We would call this usually a shop traveler."

A shop traveler is a manufacturing concept where a document (physical or digital) accompanies a work order through every production step, recording what happened at each stage, on which equipment, with what parameters. Colin's recognition of this pattern indicates he has implemented similar systems and understands the data model required.

Mahesh's specific vision for the shop traveler:

| Stage | Equipment Assignment | Tracking |
|---|---|---|
| Press | Press 2 | Scan to start, scan to complete |
| Glaze | Glaze 2 | Scan to start, scan to complete |
| Printer | Printer 2 | Scan to start, scan to complete |
| Kiln | Kiln 7 | Scan to start, scan to complete |
| Quality (Colletron) | Q3 | Automated |
| Sorting | Sorting Line 3 | Scan to start, scan to complete |
| Packaging | Packaging Line 2 | Automated (label print) |

The label printing system would automatically select the correct label design based on the work order's item number and customer (Daltile own-brand vs. Home Depot private label vs. other OEM customers).

---

## 8. Staffing Recommendations for Mahesh's Team

Colin provided a three-person team structure recommendation, phased by need:

### Hire 1: Architect / Manufacturing Systems Engineer (Immediate)

- Someone who understands the entire manufacturing process from a systems perspective
- Technically capable enough to understand the data systems, even if not a full-time developer
- Ideally someone who has been a developer in the past but has moved into a broader role
- Can diagnose technical issues and serve as the bridge between manufacturing operations and the technology team

### Hire 2: Hardware/IoT/Sensor Specialist (Immediate)

- A hardware-centric person who specializes in sensors, IoT, and automation
- Explicitly **not** a PLC engineer -- Colin warned: "I would stay away from them because they're going to be very rigid." PLC engineers tend to be locked into specific vendor ecosystems and legacy approaches
- Must be someone who speaks the same language as the architect (Hire 1) -- Colin emphasized the pairing needs to work interpersonally: "You don't want to mix like an old guy that's got a ton of experience with PLCs with some younger guy that's really good with the whole process. They won't get along."
- Colin offered to write a job description (JD) for this role using his "generators" (likely AI-assisted JD generation). Mahesh accepted.

### Hire 3: Quality Engineer / Process Engineer (Later)

- Not needed for the initial build-out, but necessary for the natural next phase
- Once the MES is producing data and tracking lineage, the next step is using that data to improve the process and reduce costs
- This person would drive tactical improvements based on the new visibility
- Colin noted: "It depends upon the existing engineering team. If you don't have a quality guy or a process engineer" -- implying this hire might already exist elsewhere in the organization

### Colin's Observation About Junior Talent

Colin made an interesting staffing observation: "You actually can do more with younger people. You wouldn't think that, but it's the same for a lot of these things." This suggests he prefers building teams with adaptable, tech-native junior engineers over expensive senior specialists who may be rigid in their approaches.

---

## 9. Observations from Factory Video Walkthrough

Colin watched Mahesh's screen-shared factory walkthrough videos (numbered approximately 1-16) and made the following specific technical observations:

### Physical Infrastructure
- **80/20 aluminum framing** -- extensive throughout the factory, providing ready-made camera/sensor mounting points with T-slot channels
- **Proper guarding** -- safety enclosures around automated equipment, providing additional structure and defined viewing angles for cameras
- **Conveyor belts** -- fully automated transfer between process stages with no manual intervention when the line is running correctly

### Control Systems
- **Siemens PLCs** (or similar) visible on the walls -- a mix of older and newer models
- **Serial port** on the label printing station PC -- RS-232 connection to the SATO printer, replaceable by modern interface
- **Blue-screen Progress application** -- the current "MES" (actually just a label printing controller) running on an aging platform
- **SATO printer** -- label printer controlled via SATO programming language rather than a label design tool

### Equipment Vendors
- Three primary equipment suppliers who also manufacture tiles themselves (competitors who sell the same machines to Daltile): Sacmi (transcribed as "scammy"), Colletron (surface/defect inspection equipment), and a third unnamed supplier
- These vendors supply presses, dryers, glaze lines, printers, polishing/rectification equipment, and quality inspection machines
- The vendor relationship creates a dependency where Daltile relies on vendor-provided engineering rather than developing proprietary process knowledge

### Factory Scale (Sunnyvale/Muskogee Plant)
- Plant 2 is significantly larger than Plant 1
- Plant 2 equipment: approximately 6 presses, 6 glaze lines, 6 printers, 4 kilns, 5 Colletron quality machines, 5 sorting lines, 1 palletizer
- Production: approximately 400,000 square feet per day
- Mahesh's office is approximately 20 minutes from this factory (selected as the pilot site for that reason)

---

## 10. Process Error Sources -- Colin's Diagnostic Framework

Colin articulated a general principle for diagnosing manufacturing errors: "If you think about what could possibly happen at any diagram like this, it's either you have a potentially destructive step or a step where something is physically moving from location A to location B. Those are really where your errors come from, aside from a machine actually just being out of spec."

Applied to the Daltile process:

1. **Destructive steps:** kiln firing (can cause warping/caliber issues, color shifts), pressing (dimensional issues if press is miscalibrated)
2. **Movement/transfer steps:** conveyor belt transfers where tiles can be "treated a little" (knocked, misaligned) causing them to not feed properly into the next stage
3. **Machine drift:** equipment operating out of specification, detectable by correlating upstream sensor data to downstream quality outcomes

Colin's approach to error detection: instrument each destructive and transfer step, then correlate the readings to final quality outcomes. If all upstream parameters are constant and the kiln is constant, output should be constant. Any deviation in output can be traced back to whichever upstream parameter changed.

---

## 11. MES Vision and Delivery Approach

### What Mahesh Wants

Mahesh described his vision as a "Cumulus-like screen" (referring to Cumulus MES software as a visual reference) that provides:

- Work-order-level tracking through every production stage
- Real-time visibility of WIP at each stage (how many pressed, how many dried, how many through glaze, etc.)
- Waste tracking at each stage (not just at the final Colletron inspection)
- Yield calculation at each step (currently only calculated at the sorting line)
- Label design tool replacing the Progress/SATO direct-programming approach
- Equipment utilization and uptime visibility

### Colin's Delivery Approach

Colin proposed a phased, flexible approach:

- Start with one line at one factory (the Sunnyvale/Muskogee plant near Mahesh's office)
- Build in Azure from the start, trending toward the full MES vision
- Provide the proposal with flexibility markers ("asterisks") for hardware costs pending site visit
- Structure as "if you want this now and this later" to allow incremental investment
- Site visit to scope camera/sensor requirements, network topology, and equipment integration points

### Budget Context

Mahesh disclosed an approximate software budget of $250,000, which covers multiple plants (not just one). The budget is categorized as software -- PLCs and sensors would come from a separate team's budget, though that team "is not thinking right" and Mahesh wants to take the initiative to show what is possible.

---

## 12. Key Action Items Colin Committed To

1. **Write a JD** for Mahesh's hardware/IoT/sensor specialist hire
2. **Send off-the-shelf dashboard platform recommendations** with pricing (approximately $20K for full factory)
3. **Prepare a flexible proposal** with cost estimates and phasing options
4. **Schedule a site visit** to the Sunnyvale/Muskogee factory for hands-on scoping
5. **Test camera placement** during the site visit with quick on-site validation
6. **Scope network/communication requirements** including XBee feasibility assessment
