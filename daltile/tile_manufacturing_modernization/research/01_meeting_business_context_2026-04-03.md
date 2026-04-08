# 01 - Meeting: Business Context

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Focused deep dive on budget, timeline, scope, and next steps

---

## Budget and Financial Constraints

### Stated Budget

Mahesh disclosed a budget of **approximately $250,000**, with two critical qualifiers:

1. **Multi-plant budget, not single-plant:** "That's not just for one plant" -- the $250K covers software investment across multiple DalTile manufacturing facilities, not exclusively the Sunnyvale target plant.
2. **Software-only budget:** "My budget is more software budget" -- Mahesh's budget authority covers software, application development, and related costs. Hardware expenditures (PLCs, sensors, cameras, networking equipment) fall under a separate team's budget that Mahesh does not control.

### Hardware Budget Gap

Mahesh explicitly called out that the hardware team "hasn't even thought about PLCs and sensors and others. That usually goes to the other team, but you know that team is not thinking right." This creates both a gap and an opportunity: Mahesh wants to take the initiative to demonstrate what is possible with sensors and cameras, even though the hardware budget belongs to another group. Colin's proposal needs to account for this split by putting an asterisk on hardware costs.

### Off-the-Shelf Dashboard Platforms

Colin mentioned that there are existing commercial dashboard platforms that could provide configurable engineering dashboards for approximately **$20,000 per factory**. He described these as drag-and-drop, low-code/no-code interfaces that look similar to C# development environments. Colin offered to send Mahesh references for these platforms. This could reduce the custom development scope if Mahesh finds them suitable.

### Sephora Engagement as Pricing Credibility

Colin referenced the Sephora engagement as a credibility signal: a three-year enterprise data warehouse (EDW) modernization that BayOne is delivering in nine months, involving 6,000 reports migrated from IBM Cognos/on-prem SQL Server to Databricks. Colin emphasized outcome-based billing rather than time-based billing: "We're billing by outcomes, not by time." He also mentioned a separate deal where BayOne quoted $500K, the client countered at $200K, and Colin walked away -- establishing that BayOne prices based on value, not desperation.

### Cost Optimization Signals

Colin noted that the proposed technology stack is "all cost optimized" -- Azure Container Apps for deployment, PostgreSQL on Azure for database. This signals awareness of Mahesh's budget constraints and an intent to keep infrastructure costs manageable.

---

## Timeline and Urgency

### Extreme Urgency

When Colin asked about timeline, Mahesh's response was unambiguous: **"If we could do yesterday, that would have been better, but today will work."** He followed with: "Give me whatever is realistic and I think we can make it fly."

### Urgency Drivers

Several factors compound the urgency:

1. **Team attrition:** Of the three-person team that previously managed the Progress-based MES/label printing system, two have left and one is retiring. This leaves a single junior person handling label operations.
2. **Technical debt:** The existing Progress codebase is aging, the serial-port networking infrastructure is unsupported, and the team that built it is gone.
3. **No visibility into production:** DalTile currently tracks production only in aggregate square meters per machine per day, not by work order or item number. Mahesh described this as "they don't really track almost anything."
4. **Waste accounting disagreement:** Mahesh is in active disagreement with finance over waste calculations. Finance reports approximately 9% waste based only on the sorting line rejection data, but Mahesh argues the true waste is significantly higher because waste at the press, dryer, glaze line, printer, and kiln stages is not tracked at all. "It's more than 9% wastage. You can see there's wastage over here, there's wastage over here, there's wastage over here. They're not even tracking any of that."

### No Timeline Constraint from Mahesh

Mahesh did not impose a deadline or phased timeline. His urgency is about starting as soon as possible, not about hitting a specific date. Colin's flexible proposal approach ("here's what we could do now, here's what comes later") aligns with this.

---

## Scope: What Is In vs. Out for the First Engagement

### Two Potential Projects Identified

Mahesh explicitly said: "I don't mind doing 2 projects." The two projects are:

#### Project 1: MES with Work Order Tracking and Real-Time Visibility

This is Mahesh's primary goal. The desired system would provide:

- **Work order-level tracking** through every production stage (press, dryer, glaze line, printer, kiln, Qualitron, sorting, packaging)
- **Real-time visibility** via a dashboard (Mahesh referenced "Cumulus" -- likely a SCADA/HMI-style visualization) showing work order progress through each stage
- **Yield tracking at each step** -- how many tiles pressed, how many survived each stage, where waste occurred
- **Start/end timestamps** for each stage per work order
- **Waste attribution** tied to specific work orders and stages, not just aggregate daily numbers
- **Label printing integration** -- the MES would include a modern label designer that replaces the Progress-based system, supporting both DalTile's own labels and private-label/OEM labels (Home Depot, etc.)
- **Work order routing** -- the planner assigns specific equipment (e.g., Press 2, Glaze Line 2, Printer 2, Kiln 7, Qualitron 3, Sorting Line 3, Packaging Line 2) and operators scan to confirm each stage

#### Project 2: Progress Code Modernization / Label Printer Redesign

This is a more contained, fixed-bid project to:

- **Kill the Progress codebase** entirely
- **Replace the custom Sato-language label programming** with a proper label designer interface
- **Move the backend** from Progress to Python/.NET/C# with a modern database (Oracle or PostgreSQL)
- **Migrate from serial ports to Ethernet/TCP-IP** for printer communication, so the network team can manage connectivity instead of Mahesh's team

Mahesh's ideal scenario is that Project 2 becomes a component of Project 1: "Ideally I would like it to be part of this MES."

### Scope Boundaries: First Engagement

- **One line at one factory:** Mahesh wants to start with a single production line at the Sunnyvale Plant 2 facility.
- **Plant 2 specifically:** "I want to do just one of this factory, this factory specifically because you know my head office where I sit is like 20 minutes away from this factory."
- **Not the full MES dream on day one:** Colin proposed a phased approach: "If you want this now and you want this later, you know that's fine. If you want to, you know, like for instance, just get set up for an MES without saying that that's the full scope, but at least something that will trend towards that and get you there eventually."

### What Is Explicitly Out of Scope (for now)

- **Raw material preparation:** Mahesh said "this side of the process I'm not so worried about because this is more like a raw material preparation. Ideally we would want to go there, but I think we have bigger problems before we go there."
- **Multiple plants:** The first engagement is Sunnyvale Plant 2 only. Plant 1 and other DalTile/Mohawk facilities come later.
- **AI/ML quality prediction:** While both Mahesh and Colin discussed the potential for upstream quality detection (cameras at the printer stage, moisture sensors at the kiln), Mahesh positioned this as a future state: "First stage is obviously to show them a little bit of visibility."
- **Polishing and rectification lines:** The Sunnyvale Plant 2 facility shown in the walkthrough does not perform polishing or rectification after the kiln. These steps are optional and site-dependent.

---

## Factory Physical Details

### Sunnyvale Location

DalTile's Sunnyvale facility consists of two plants:

- **Plant 2:** The larger and older of the two. This is the target for the first engagement. Mahesh showed a satellite view indicating the manufacturing building is very long -- the parking area fits approximately 8 cars, and the production line runs from one end to the other of the entire building. The press is at one end; the finished product line is at the far opposite end. Mahesh described it as "obviously much longer" than Plant 1.
- **Plant 1:** Smaller, located nearby ("right over here in this area"), with fewer/lesser equipment than Plant 2.
- **Office building:** A "tiny sliver" compared to the manufacturing floor footprint.
- **Mahesh's proximity:** His office is approximately 20 minutes from the Sunnyvale factory, making it practical for oversight and iteration.

### Factory Environment

- **Dusty environment:** Not a cleanroom. Dust accumulation on sensors is a known problem -- light curtain sensors in particular become unreliable when dirty.
- **Open warehouse-style layout:** High ceilings, flat floor, relatively open space. Colin noted this is advantageous for wireless communication solutions (XBees or similar radio-based protocols).
- **Existing 8020 aluminum extrusion framing:** Colin observed this in the walkthrough videos, noting it makes camera and sensor mounting straightforward -- the channels in the extrusion are designed for attachments.
- **Network infrastructure gap:** Wireless and wired networking on the manufacturing floor is poor. The building's size makes network drops expensive. This is a known constraint that any solution must address.

---

## Equipment Counts and Production Volumes

### Sunnyvale Plant 2 Equipment Inventory

Mahesh provided specific counts for Plant 2:

| Equipment Type | Count | Notes |
|---|---|---|
| Presses | 6 | Some satellite view showed presses 1, 3, 4, 5 (press 2 was removed at one site's PI display) |
| Glaze lines | 6 | Multiple coating stages per line |
| Printers | 6 | Digital inkjet printers replacing old-school glaze application |
| Kilns | 4 | Very large; multiple temperature zones (heat, raise, cool, raise again) |
| Qualitrons (Qualitron/Colletron) | 5 | Automated quality/defect inspection machines |
| Sorting lines | 5 | Sort by shade and caliber into 3 SKUs |
| Palletizer | 1 | Single wrapping/palletizing station at end of line |

Mahesh noted the equipment count varies by stage: "Sometimes goes from 6 to 4 and then 4 to 5" -- meaning the process has a funnel shape where more upstream equipment feeds into fewer downstream units.

### Production Volume

- **Approximately 400,000 square feet per day** at one plant (Sunnyvale). Mahesh stated: "For one plant, we make like 400,000 square feet every single day."
- Tile sizes range from **6x48 inches** (plank format) to **24x24 inches** (largest square tile produced).

### Equipment Vendors

Three companies supply virtually all tile manufacturing equipment globally:

1. **System Ceramics (Sacmi)** -- presses, dryers, and other equipment (transcribed as "scammy")
2. **Qualitron/Colletron** -- surface defect detection and quality inspection machines (transcribed as "Colletron" and "inside in surface")
3. A third unnamed company

These vendors are also competitors: they manufacture tiles themselves and sell to private labels. Mahesh found this remarkable -- the same companies that sell DalTile its machines also produce tiles and brand them for competitors or for retailers like Home Depot.

---

## WIP (Work-in-Process) and Production Flow

### Four WIP Staging Areas

Mahesh identified 3-4 places where work-in-process inventory accumulates, breaking the continuous flow:

1. **Before the kiln** -- tiles stack into drawers/shelves waiting for kiln capacity
2. **After the kiln** -- fired tiles stack waiting for Qualitron/sorting
3. **Before palletizing** -- sorted/boxed tiles waiting for palletizer
4. **Finished goods inventory** -- wrapped pallets in warehouse

### The Lineage Problem

The WIP stages create a critical data traceability gap. At the kiln stage, tiles from multiple press/glaze/printer lines converge. There is currently **zero correlation** between which work order's tiles entered which kiln, and which emerged. Mahesh emphasized this repeatedly:

- "Once you are at the kiln, which line went into which kiln? Because there is no correlationship."
- "How much of this product got wasted in the kiln, I have zero idea because it could be all this product, it could be zero of this product."
- After the kiln, the part number "magically" reappears at the sorting line with no verifiable lineage.

Colin responded that since the process is PLC-driven and predictable (no human-in-the-loop), tile position can be traced through logic extracted from the PLCs even when out of camera view.

---

## Agreed Next Steps

### Colin's Action Items

1. **Factory visit:** Colin offered to visit the Sunnyvale factory in person. Mahesh confirmed this as the logical next step: "Sounds to me that the next step would be that you visit and see it and then gauge what it would take." Colin would use the visit to assess camera placement, sensor opportunities, network infrastructure, and line layout.

2. **Rough estimate with hardware asterisk:** Mahesh requested "a rough, rough estimate" to determine viability. Colin agreed to provide a proposal with flexibility built in: "I'll put there is like an asterisk because what I'll want to do is see the extent... before I say like here's like the hardware cost." The proposal will include options: "Here's what we could do now, here's what comes later."

3. **Off-the-shelf dashboard platform references:** Colin offered to send Mahesh information about commercial engineering dashboard platforms (~$20K per factory) that provide drag-and-drop configurable dashboards for sensor data visualization. This could complement or partially replace custom MES development.

4. **Job description for Mahesh's team:** Colin offered to write a JD for the IoT/sensor/hardware-centric role that Mahesh needs to hire. Mahesh accepted: "Oh yeah, if you don't mind doing that, that would be great." Colin also outlined the ideal team structure:
   - **Manufacturing engineer/architect** -- someone who understands the full process and is technical enough to work with the system, possibly a former developer
   - **Hardware-centric IoT/sensor person** -- explicitly NOT a PLC engineer ("I would stay away from them because they're going to be very rigid"), but someone experienced with sensors, IoT, and automation
   - **Process/quality engineer** (future hire) -- needed once data is available, to drive process improvement initiatives

### Mahesh's Action Items

1. **Forward factory walkthrough videos and images:** Mahesh recorded videos during his factory walkthrough and showed them during the call. He committed to labeling them properly and forwarding: "I'm going to nicely label them and then I think I can forward these files to you."

2. **NDA with BayOne:** Mahesh indicated an NDA is imminent: "I don't have an NDA yet, but very soon I will have an NDA with BayOne, so that's not a problem." He shared materials from his personal files in the interim, indicating trust and willingness to proceed before formal paperwork.

---

## Private Label / OEM Business Model Context

DalTile (a Mohawk Industries subsidiary) manufactures tiles not only under its own brand but also for **private labels**. Mahesh confirmed: "We make it for other companies and we label for them as well. So basically like for example, Home Depot may sell something as a Home Depot brand, but we have created it."

This has direct implications for the MES and label printing system:

- The label printer must support **multiple label formats** per production run -- DalTile's own labels versus retailer-specific labels (Home Depot, etc.)
- Work order routing must include the label format as a parameter: "If this item number is our product, we know that it's going to be our label, but if it is Home Depot product... then I know that the label for that is a different label."
- The existing Progress-based system handles this via hardcoded Sato printer commands; the replacement needs a visual label designer that supports multiple templates.

---

## Equipment Vendor Dynamics

The tile manufacturing equipment market has a unique and somewhat paradoxical structure that Mahesh found remarkable:

- **Three companies** (System Ceramics/Sacmi, Qualitron/Colletron, and one unnamed) supply virtually all manufacturing equipment globally.
- These same companies **also manufacture tiles** and sell them to retailers and competitors as private-label products.
- They sell the machines, provide training, and then walk away: "Once they have given the machine, now it's yours to do whatever you want."
- DalTile and its competitors rely heavily on these vendors for process knowledge rather than developing proprietary manufacturing engineering: "A lot of people just rely on those machines rather than creating their own engineering to say, how can I make this better."
- Mahesh drew an analogy to the automotive industry, noting that only two companies in the US manufacture cards (likely referring to ceramic tiles for a specific application), both using machines from an Italian company.

This vendor dependency creates an opportunity: any proprietary process intelligence that DalTile develops through an MES and sensor system would be a competitive differentiator, since competitors are all using the same equipment with the same default capabilities.

---

## Competitive and Political Dynamics

### Hardware Team Inertia

The team responsible for PLCs, sensors, and physical infrastructure is not aligned with Mahesh's modernization vision. Mahesh stated they "haven't even thought about" sensors and cameras, and characterized them as "not thinking right." This creates a political dynamic where Mahesh is taking initiative outside his formal budget authority (software) to demonstrate possibilities that should motivate hardware investment.

### Finance Disagreement on Waste

Mahesh is in active disagreement with finance over waste metrics. Finance tracks waste only at the sorting line (approximately 9% rejection rate), but Mahesh argues that waste occurs throughout the production process and is not measured:

- Waste during press setup (100% waste until conveyors are aligned for a new item)
- Waste during dryer, glaze line, and printer setup
- Waste from conveyor belt misalignment ("They throw away tiles just because the conveyor belt has treated the tile a little bit")
- Untracked shrinkage between stages (e.g., 15,000 sq ft pressed but only 14,000 made it to the dryer)

The company's cultural attitude compounds this: "At any point, if there's a waste, they can just crumble it back again and put it back as a raw material. So they don't even think of waste as waste." Mahesh counters that this ignores machine time, electricity, and labor costs. Furthermore, post-firing waste is regulated: only 6% of fired tile material can be recycled back into raw material, making kiln waste genuinely costly.

### Ceramic Engineers vs. Data-Driven Approach

The ceramic engineers who "run the show" maintain that quality testing cannot happen until tiles are fired (post-kiln). Both Colin and Mahesh challenged this assumption. Colin argued from experience with analogous industries (diamond polishing, silicon carbide manufacturing) that upstream quality correlation is absolutely possible with sufficient sensor data. Mahesh identified that the only rejection criteria are **shade** and **caliber** -- both of which could theoretically be predicted upstream from glaze line parameters, printer output, and moisture content before firing.

### Counter Reset Politics

The factory currently resets all machine counters daily at 6:00 AM. Mahesh wants to reset counters per work order to enable work-order-level tracking. The operations team resists this: "No, no, no, we can't do that. All the reports go to all the executives. We don't want to do that." Their concern is valid -- one work order can split across multiple glaze lines, and multiple glaze lines can feed a single kiln -- making simple counter resets unreliable without proper lineage tracing. This reinforces the need for the MES to solve the lineage problem first.

---

## Technology Stack and Architecture Decisions

### Agreed Technology Direction

| Component | Decision |
|---|---|
| Language | Python ("100%") |
| Database | PostgreSQL on Azure |
| Deployment | Azure Container Apps |
| Cloud | Azure (DalTile already has Azure) |
| Communication (high throughput) | RabbitMQ for task queuing and distributed load |
| On-premise component | Required -- manufacturing cannot depend on cloud availability |

### Critical Architecture Constraint: Reliability Engineering

Mahesh raised a non-negotiable constraint: **the manufacturing floor cannot depend on Azure availability.** His specific example was the label printer, which has a three-second window to detect a box, print and apply a label, and release the box. If Azure communication takes longer than that, the conveyor belt stalls.

Colin agreed completely and framed it as "total separation of concerns -- Azure being up or down, existing or not existing shouldn't impact anything on the factory and vice versa." He called this "reliability engineering" and noted that for manufacturing, any AI/ML components should run on-prem rather than cloud-dependent.

Mahesh elaborated: "There will have to be a sliver of some files or whatever else that we can do that needs to be on the factory floor so that at least that continuity doesn't break if Azure is down."

### Networking Solutions

Colin proposed **XBee-style radio communication** for the factory floor as an alternative to expensive network drops and unreliable Wi-Fi. He noted the factory's characteristics (flat, open ceilings, warehouse-style) are ideal for this approach. The only concerns would be metal interference or large AC motors, which the factory does not appear to have in problematic quantities.

### Historian Database

Mahesh mentioned that some DalTile sites already have **PI Historian** databases collecting machine data. The Sunnyvale site has some PI data (the Excel-based dashboard he showed was fed by PI). Colin suggested this is the right approach for high-volume sensor data ingestion, recommending 5-minute intervals for press readings and similar telemetry.

---

## Mahesh's Hiring Needs and Team Gaps

### Current Team State

- **Original team:** Three people writing Progress code, managing custom serial-port networks, and maintaining the label printing system
- **Current state:** Two have left, one is retiring. One junior person remains who handles labeling and has some development skills that could translate to Python
- **Gap:** No one to maintain the existing Progress system, no one qualified to build or manage a modern MES

### Recommended Team Structure (Colin's Advice)

1. **Manufacturing engineer / architect** -- understands the full production process, technically capable (ideally a former developer), can diagnose system issues. This person serves as the bridge between manufacturing operations and the software system.

2. **Hardware-centric IoT/sensor person** -- experienced with sensors, IoT devices, and automation. Colin explicitly recommended against hiring a PLC engineer: "I would stay away from them because they're going to be very rigid." The IoT person should speak the same technical language as the architect and work collaboratively.

3. **Process/quality engineer** (future hire, not needed immediately) -- once the MES is producing data, this person drives tactical process improvements and cost reduction. "The natural next step is improving things after you now have all this data."

Colin offered to write JDs for these positions, and Mahesh accepted.

---

## Existing PI-Based Dashboard (What They Have Today)

Mahesh showed an email from a colleague (Eric Williams) containing the closest thing DalTile has to an MES at another site. This system, built on PI Historian data, provides:

- **Press overview:** Shows presses 1, 3, 4, 5 with tile sizes (24x48, 24x24, 12x24) and square feet pressed
- **Press-to-glaze-line mapping:** Shows which press feeds which glaze line (e.g., P1 feeds Glaze Line 1 and 2)
- **Stage-level quantities:** Pressed, entered dryer, exited dryer, entered glaze line, exited glaze line -- but with known data integrity issues (e.g., 22,500 entered glaze but 22,800 exited, which is physically impossible)
- **WIP tracking:** Three WIP buckets (post-glaze/pre-kiln, post-kiln/pre-sorting, pre-sorting)
- **Kiln throughput:** Aggregated only (28,000 sq ft in, 27,000 out, with no error categorization)
- **Sorting line rejection data:** The only stage with quality metrics -- rejection by surface defect, caliber, and other codes. Shows approximately 2-10% rejection rates depending on the line.
- **AGV (Automated Guided Vehicle) tracking:** Shows where AGVs are parked and what they carry
- **Uptime tracking:** Per-machine uptime percentages, showing significant variation in glaze lines (driven by production demand, not equipment failure)

The critical limitations of this existing system:

1. **No work order tracking** -- everything is measured by machine, not by product/order
2. **No lineage through the kiln** -- correlation between upstream lines and kiln/post-kiln is lost
3. **Sensor data integrity issues** -- light curtain sensors produce impossible counts (more output than input), causing executives to distrust the data entirely
4. **Daily counter resets** -- all machine counters reset at 6:00 AM, preventing work-order-level granularity

---

## Colin's Proposal Approach

Colin outlined a flexible, phased proposal strategy:

1. **Asterisk for hardware costs:** The software/development estimate will be concrete, but hardware costs (cameras, sensors, networking equipment) will be flagged as TBD pending a factory visit where Colin can assess actual needs.

2. **Phased scope:** "Here's what we could do now, here's what comes later" -- allowing Mahesh to start within his software budget and build toward the full MES vision incrementally.

3. **Start in Azure from day one:** Even if the first phase is limited, building on Azure from the start means the system grows into the full MES naturally rather than requiring a replatform later.

4. **Reliability-first architecture:** On-premise edge components for anything time-critical (label printing, PLC communication), with Azure for dashboards, data aggregation, and analytics.

5. **Outcome-based value proposition:** Consistent with Colin's approach on other engagements (Sephora, Cisco), pricing based on delivered outcomes rather than time-and-materials.
