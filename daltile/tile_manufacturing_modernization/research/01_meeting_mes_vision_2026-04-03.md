# 01 - Meeting: Mahesh's MES Vision and Work Order Tracking

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Focused deep dive on MES vision and requirements

---

## 1. The End-State Vision: A "Cumulus-Like" MES

Mahesh's articulated end goal is a custom-built MES that replaces the current disjointed set of tools (PI historian dashboard, Progress-based label printing, manual tracking) with a unified system providing real-time visibility into manufacturing operations at the work order level. He explicitly referenced "Cumulus" as the aspirational model, describing the interface he envisions as a "Cumulus-like screen" that shows the entire process with live data.

His exact framing of the end goal (at 1:17:44 in the transcript): "That's the end goal. The end goal is having an MES of our own, which we developed like Cumulus, which has all these measurements that we can do, all kind of tracking that we can do, all kind of label designing we can do because that's where I'm going, if you will, with this."

Key capabilities Mahesh described wanting in this system:

- **Work order-level tracking** through every manufacturing stage
- **Real-time visual display** of work order progress (how many tiles pressed, dried, glazed, printed, fired)
- **Yield tracking at every stage**, not just at the sorting line
- **Waste tracking at every stage**, not just the 9% currently measured at sorting
- **Lineage tracing**: which work order went through which specific piece of equipment, end-to-end
- **Equipment uptime and utilization tracking** for every machine
- **Label design capability** integrated into the MES, replacing the SATO code programming approach
- **Private label support** for different brands (DalTile own brand vs. Home Depot vs. others)
- **Planner interface** for setting up work order routing through specific equipment

---

## 2. The Spreadsheet Walkthrough: Work Order Routing Concept

At approximately 43 minutes into the call, Mahesh opened Excel and built a live example of the data structure he envisions. He described this as the interface a production planner would use to set up and track a work order.

### The Concept

A planner creates a work order and assigns it to specific equipment at each stage. Mahesh walked through this example:

| Field | Value |
|-------|-------|
| **Work Order Number** | 123 |
| **Item Number** | 4567 |

| Stage | Equipment Assignment |
|-------|---------------------|
| Press | Press 2 |
| Glaze | Glaze 2 |
| Printer | Printer 2 |
| Kiln | Kiln 7 |
| Quality (Qualitron) | Quality 3 |
| Sorting Line | Sorting Line 3 |
| Packaging Line | Packaging Line 2 |

### The Planner Workflow

Mahesh described the planner's role in setting up this routing: "I want to say to a person who is planning to say this is what you are setting up. Now I know which press you're going to use because I have 7 presses. I have 7 glaze lines or 7 printers. I have maybe 4 kilns and I have how many ever these."

The planner would define the route before the work order starts, specifying which equipment at each stage will process this particular order. This creates the blueprint against which actual production is tracked.

### Why This Matters

Currently, the facility has no work order-level correlation in production. They track aggregate machine throughput (total square feet pressed by Press 1 in a day) but cannot say which specific product or order was responsible for those numbers. Mahesh's frustration with the existing PI dashboard (at 1:13:48): "I want to walk away from this. I want to start tracking work order."

---

## 3. Barcode Scanning at Handoff Points

Mahesh described a scanning-based workflow to track work order progression through the factory:

- **At each stage start**: An operator scans a barcode to register that work order 123 is now being processed at that station. "Every time a job starts you scan it to say now I'm starting this job."
- **At each stage completion**: A scan registers that the stage is complete for that work order.
- **At the kiln**: "When you start the kiln and you start feeding this order number to Kiln 7, you say I'm starting this job. Now we know it is Kiln 7 and it is going back into a WIP."
- **At the sorting line**: "You're scanning the job number and we know that now we have to look at Quality 3 and this is the item number being produced."
- **At packaging**: The final scan triggers label printing with the correct label for that item number and brand.

Mahesh described forcing these scan points: "You force them to scan something over here when they start a job, you force them to scan something when they do this, you force them to do something when they do these two and then packaging is the last step."

Colin identified this as a standard manufacturing pattern, calling it a "shop traveler" -- a concept Mahesh immediately confirmed.

---

## 4. Work Order-Level Yield and Waste Tracking

### The Real-Time Visual

Mahesh described the visual he wants to show (at 34:37): "If I can show them a Cumulus-like screen which shows them look, this is your process and you are trying to make 10,000 out of which you know 5,000 has already been pressed, 4,000 has already been dried and whatnot."

He wants a stage-by-stage view for each work order showing:
- Start quantity and end quantity at each stage
- The delta (waste/loss) at every stage transition
- Current location of in-process tiles

### Waste Tracking Gap

Mahesh explained that waste happens throughout the process but is only formally tracked at the sorting line (Qualitron/Collectron stage). His specific complaints:

1. **Setup waste is untracked**: When configuring a new item, the press starts and produces "100% waste till the point they have set the conveyors and everything in the proper alignment." This waste happens at every stage downstream as each machine is tuned.
2. **Conveyor belt waste is untracked**: "They throw away tiles just because the conveyor belt has treated the tile a little bit and it won't go in the proper way to the next process."
3. **Finance underreports waste**: Finance calculates waste at 9% based solely on sorting line rejections, but Mahesh argues the true waste is higher because losses at press, dryer, glaze line, printer, and kiln are invisible. "They have this calculation to say 9% wastage, but it's more than 9% wastage. You can see there's wastage over here, there's wastage over here, there's wastage over here. They're not even tracking any of that."

His vision: "I want to show them that 100 tiles" -- referring to waste at each individual stage being tracked and displayed as part of the work order's visual.

### Current Measurement Approach (What Mahesh Wants to Replace)

Today, the factory measures aggregate daily throughput rather than work order yield: "They basically measure -- they don't measure work orders. They basically see how much tiles did we press, how much kiln did we use and how much output did we produce in thousands of square meters. They don't even look at it from an item perspective or anything else perspective."

---

## 5. Lineage Tracing: Work Order to Equipment Mapping

Mahesh described a fundamental traceability gap. The current PI dashboard shows aggregate numbers for each machine but has no correlation between stages. He walked Colin through the existing dashboard data to illustrate:

- Press 1 fed Glaze Line 1 and Glaze Line 2 -- you can infer this from quantity, but there is no formal link.
- Once tiles enter the kiln WIP buffer, all correlation breaks: "Once you are at the kiln, which line went into which kiln? Because there is no correlationship."
- After the kiln, part numbers "magically" reappear at the sorting line with no explanation of how they were tracked through the kiln: "How did the magically part number show up over here?"

The lineage Mahesh wants:
- Work Order 123, Item 4567 was pressed at Press 2
- Then glazed at Glaze 2
- Then printed at Printer 2
- Then fired at Kiln 7
- Then quality-checked at Quality 3
- Then sorted at Sorting Line 3
- Then packaged at Packaging Line 2

This end-to-end lineage does not exist today. The MES vision is fundamentally about creating this chain.

### Why Lineage Matters for Counter Resets

Mahesh connected lineage tracing directly to the counter reset problem (see Section 8). Without work order-level lineage, the factory cannot reset counters per work order because one press may feed multiple glaze lines, and multiple glaze lines may feed one kiln. The mix-and-match routing makes per-work-order tracking impossible without the lineage system.

---

## 6. Equipment Uptime and Utilization Tracking

Mahesh explicitly stated that uptime tracking should be a byproduct of the MES (at 1:01:36): "Ideally as we do this program, I would definitely want to know uptime because you know if we are doing this, we should be able to say this much is the uptime for Press 2, this much is the uptime for Glaze 2 or whatever it may be."

He noted that utilization is "a big thing for them" -- meaning plant management cares deeply about whether equipment is running or idle.

The existing PI dashboard already shows uptime percentages for some equipment. In the example Mahesh walked through, glaze line uptime varied significantly (some lines at high uptime, others much lower). Colin asked whether this variation was due to throughput demand, and Mahesh confirmed: "I didn't have enough production coming from the press, so I couldn't keep these two lines up or I couldn't feed these lines all day busy."

The MES vision would give this uptime data more context by tying it to specific work orders and showing why equipment was idle.

---

## 7. Label Design Modernization

### The Current State

The existing label printing system is what DalTile calls their "MES" -- but Mahesh bluntly reframed this: "They call it MES, but literally it's a label printing solution that you saw in the sorting line. That's what they have that my group supports."

The system consists of:
- **Progress/OpenEdge application** (the blue screen visible in the factory video) that manages label data
- **SATO printer language**: Labels are programmed by writing SATO code that specifies pixel-level placement of barcodes, text, and fields. "They are literally programming this printer using SATO language rather than a designer label."
- **Serial port connection** from the blue-screen PC to the SATO printer
- **PLC interaction**: A PLC raises a stop gate when a box arrives, the label is printed and pushed onto the box by a mechanical arm, and the PLC releases the box -- all within a three-second window

### What Mahesh Wants

A proper label designer where users can visually design labels rather than programming them in SATO code. This label designer would be part of the MES and would:
- Allow visual drag-and-drop label design
- Support different label templates per brand/customer
- Automatically select the correct label based on the work order's item number
- Work for both box labels (at the sorting/packaging stage) and pallet labels (at the palletizer)

Mahesh wants to separate concerns: "I am not doing this business of, you know, managing the PLCs for you and all of that. I want to really design a label printer and say, you know what I have designed the label for you. Now you figure out how the PLCs work and stop and get printed."

He also wants to move from serial port connections to TCP/IP Ethernet: "I want to really move back to Ethernet ports and TCP/IP and say you know what you work with the network guys to get the printer."

### Network Infrastructure for Labels

Mahesh described a legacy infrastructure problem: the three-person team that originally built the system created their own serial port network and server infrastructure. That team is now gone (two departed, one retiring). Neither the network team nor Mahesh's current team wants to maintain this custom serial infrastructure.

---

## 8. Private Labeling Requirement

DalTile manufactures tiles for multiple brands. Mahesh described three label scenarios:

1. **DalTile own-brand products**: Use DalTile's own label design
2. **Home Depot branded products**: DalTile manufactures the tile but applies Home Depot's labels. "Home Depot may sell something as a Home Depot brand, but we have created it for example."
3. **Other private-label customers**: Any brand that contracts DalTile to produce tiles under their name

The MES needs to handle this automatically: when a work order is created with a specific item number, the system should know which brand's label to print. Mahesh walked through this logic: "If this item number is our product, we know that it's going to be our label, but if it is DalTile [referring to the parent brand distinction] or it's Home Depot product, it will have a [different item number] and then I know that the label for that is a different label than my own print label."

This label selection must happen automatically at the sorting line based on the work order/item number association established at planning time.

---

## 9. The Tile Tracking Challenge at WIP Buffer Points

### The Problem

Mahesh identified a fundamental challenge with tracking individual tiles through the factory. The process is continuous from press through printer (tiles move single-file or two-abreast on conveyor belts), but at two critical points the process breaks into batch mode:

1. **Before the kiln (pre-kiln WIP)**: After printing (and the final glaze coat), tiles are stacked by an automated stacker onto shelves/racks. An LGV (automated guided vehicle) picks up stacks and stages them in a buffer area waiting for kiln capacity. "This is the first place where the process gets broken from a continuous fashion to a semi-continuous fashion because this is the first area where you see actually WIP happening."

2. **After the kiln (post-kiln WIP)**: Tiles exit the kiln and are again stacked and staged before moving to the Qualitron and sorting line.

At these WIP points, individual tile identity is lost. Tiles from potentially different work orders or different press runs get mixed into stacks. "At this point you kind of lose track of which tile went where because you know now we are going into a WIP staging area and it's no longer two tiles, it's maybe 8 to 10 tiles put together into that particular WIP area."

Mahesh stated the concern directly: "Once it goes to the kiln as well, you're losing the position of the tile."

### Colin's Proposed Solution: PLC Data for Tracking Through WIP

Colin argued that the PLC-driven automation actually makes this problem solvable. Because the stacking, LGV transport, and unstacking are all automated (not manual), the system is predictable. His reasoning: "Since everything's PLC driven, it's actually better because this is automated... it's predictable, which means that even if they are going in multiple things, maybe it's out of vision. So we can basically get that logic out from the PLC and figure out exactly where that tile went."

The key insight: even though cameras cannot see tiles once they are stacked and moved into buffer areas, the PLCs controlling the stackers, LGVs, and kiln feeders know exactly which stack went where and in what order. By reading PLC data, the system can maintain the lineage chain without needing visual confirmation of every tile.

Mahesh confirmed the predictability: "Yeah, yeah, it is definitely predictable."

---

## 10. Counter Reset Discussion: Daily vs. Per-Work-Order

### Current Practice

The factory resets all machine counters (press count, glaze line count, etc.) once per day at 6:00 AM. From that point, they track cumulative production throughout the day. Mahesh described this: "They reset the counter for the presses every single day at 6:00 AM. So essentially what they do is there is a button or there's a way where you can say put it back to zero. They do it at 6:00 AM and now they keep tracking off it from 6:00 AM."

### What Mahesh Wants

Reset counters per work order rather than per day: "If you can do that, I want to reset that for every work order. Once the work order is done, reset it."

This would give true per-work-order production counts rather than requiring after-the-fact estimation of which portion of a day's production belonged to which work order.

### Why the Factory Resists

The operations team pushes back on per-work-order resets for two reasons:

1. **Executive reporting dependency**: "All the reports go to all the executives. We don't want to do that." The daily counter data feeds into established reporting that leadership relies on.

2. **Complex equipment routing**: One press can feed multiple glaze lines, and multiple glaze lines can feed a single kiln. "I can see why because you know they have one work order from this that can go into two glaze lines. Possibly, right? Because even though it's not happening, but in an ideal world where you have 4 presses and you have 6 glaze lines, one of this press could feed 2 glaze lines and then three of these glaze lines could feed a single kiln."

The fear is that resetting a counter on a shared piece of equipment would corrupt the data for other products running on adjacent lines. Mahesh acknowledged: "They are fearful of resetting because the way the mix match is, it's not necessarily very standard."

Colin responded that lineage tracing is the prerequisite to solving this: without knowing which work order went through which equipment and when, per-work-order counting is impossible. The MES vision, with its barcode scanning at each handoff and PLC-based tracking through WIP points, would provide the data infrastructure needed to make per-work-order counters viable without disrupting aggregate reporting.

---

## 11. Mahesh's Two-Project Thinking

Mahesh articulated that he sees two distinct but related projects:

### Project 1: MES / Visibility System
- Work order tracking and routing
- Real-time visual dashboard showing progress through each stage
- Yield and waste tracking at every step
- Equipment uptime and utilization
- Lineage tracing end-to-end
- Barcode scanning at handoff points
- Camera and sensor integration for automated counting

### Project 2: Progress Code Modernization / Label Printer Replacement
- Kill the Progress/OpenEdge application
- Replace SATO code programming with a visual label designer
- Move from serial port communication to TCP/IP Ethernet
- Support private labeling (multiple brand labels per production line)
- Integrate label design into the MES so label selection is driven by work order data

Mahesh's ideal scenario is that these merge: "Ideally I would like it to be part of this MES." He wants the label designer built into the MES so that when a work order reaches the sorting/packaging stage, the MES automatically tells the printer which label to produce based on the item number and brand.

He explicitly stated the preference at 56:51: "I would love to have a project that says I'm killing Progress and I am just giving a label print solution to them of some nature. Ideally I would like it to be part of this MES."

---

## 12. Motivation: "Show Them What Is Possible"

Mahesh framed his motivation for the MES project in terms of organizational change, not just technical capability. His key statement (at 1:20:40): "I want to show them what is possible because right now they can't even see what is possible."

He elaborated on this:
- He wants to start with one factory (Sunnyvale, Plant 2) because his head office is 20 minutes away, making it easy to oversee
- This factory is the older one, meaning if the MES works here, it can be deployed to newer, better-equipped facilities more easily
- His budget ($250K) is explicitly for software development of the MES, not for sensors and hardware (which falls under a different team's budget)
- He is taking on the sensor/camera/PLC scope himself even though it is not technically in his charter because "that team is not thinking right, so I want to at least take that on and show them what could be the possibility"

The underlying strategy: Mahesh wants a working proof of concept at one factory that demonstrates the potential, which he can then use to build executive support for broader rollout. He is working somewhat ahead of his organization's readiness, bridging between software (his domain) and hardware/PLC (traditionally another team's domain) because he sees the gap.

---

## 13. The Existing PI Dashboard: What Mahesh Wants to Replace

To understand the MES vision, it is important to understand what Mahesh is moving away from. He showed Colin the existing PI-historian-based dashboard (sent by Eric William internally) and walked through its limitations.

### What the Dashboard Shows
- Press-level data: Press 1, 3, 4, and 5 (Press 2 was decommissioned), with tile size (24x48, 24x24, 12x24), square feet pressed, and uptime
- Glaze line data: Which press feeds which glaze line, entry count, exit count, product description
- Kiln data: Aggregate square feet in, aggregate square feet out
- WIP tracking: Three WIP buffer zones (pre-kiln, post-kiln, pre-sorting) with quantity estimates
- Sorting line: Rejection percentages by type (surface, caliber, other codes)
- LGV data: Automated vehicle positions and cargo

### What the Dashboard Lacks
- **No work order correlation**: Everything is aggregate by machine, not by product or work order
- **No cross-stage lineage**: "They have no correlationship" between which press output went to which glaze line went to which kiln. At the kiln, all lineage is lost.
- **Unreliable counts**: The input-to-output numbers frequently do not reconcile. Mahesh showed an example where glaze line input was 22,500 but exit was 22,800 -- an impossibility that undermines executive trust. "People who look at this data from an executive level start saying this is not real because you can't make a tile in a glaze line."
- **No error categorization before sorting**: There is no data on why tiles were lost between stages. "No idea on what type of errors happened. No idea on what type of errors happened between these two."
- **Measurement on machines, not on products**: "You start doing only measurement on your product rather only on the machines. You don't do measurements on your product."

Mahesh's summary of his stance toward this dashboard (at 1:13:48): "I want to walk away from this."

---

## 14. Summary of All Capabilities Mahesh Described Wanting

| Capability | Category | Priority Signal |
|-----------|----------|----------------|
| Work order-level progress tracking through every stage | Core MES | Primary -- described in detail with spreadsheet example |
| Real-time visual dashboard (Cumulus-like) | Core MES | Primary -- referenced multiple times as the end goal |
| Barcode scanning at stage handoffs (start/complete) | Core MES | Primary -- described as the enforcement mechanism |
| Work order-to-equipment lineage (end-to-end) | Core MES | Primary -- identified as the missing link in current system |
| Yield tracking at every stage, not just sorting | Core MES | Primary -- central to the value proposition |
| Waste tracking at every stage | Core MES | Primary -- Mahesh argued finance underreports waste |
| Equipment uptime and utilization | Core MES | Secondary -- "ideally" wants this as part of the program |
| Per-work-order counter resets (replacing daily resets) | Core MES | Desired but blocked by organizational resistance |
| Visual label designer (replacing SATO code) | Label Modernization | Primary -- wants to "kill Progress" |
| TCP/IP Ethernet printer connectivity (replacing serial) | Label Modernization | Primary -- infrastructure modernization |
| Private label support (DalTile, Home Depot, others) | Label Modernization | Primary -- operational requirement |
| Label selection driven by work order/item number | Integration | Primary -- ties MES to label system |
| Camera-based counting and tracking | Sensor/Hardware | Desired -- discussed placement challenges |
| Upstream quality sensing (pre-kiln) | Sensor/Hardware | Long-term aspiration -- mentioned as future phase |
| PLC data ingestion (press readings, machine parameters) | Sensor/Hardware | Desired -- showed press readings he wants to ingest every 5 minutes |
| Historian database for sensor data | Sensor/Hardware | Desired -- already exists at some sites |

---

## 15. Short-Term vs. Long-Term Priorities

### Short-Term (What Mahesh Wants First)
- One production line at Sunnyvale Plant 2 instrumented and tracked
- Work order-level visibility: know what is happening on a per-order basis
- Basic yield and waste tracking at each stage
- Label printing modernization (kill Progress, implement visual designer)
- Show executives "what is possible"

### Long-Term (What Mahesh Defers to Later)
- Full camera-based quality inspection (comparing tile images pre-kiln to post-kiln output)
- Upstream quality sensing to predict shade and caliber before the kiln
- Moisture sensors and process parameter correlation to predict output quality
- Raw material preparation monitoring ("this side of the process I'm not so worried about because this is more like a raw material preparation. Ideally we would want to go there, but I think we have bigger problems")
- Multi-plant rollout beyond Sunnyvale
- Full PLC integration for automated tracking through WIP buffer points (Colin's suggestion, which Mahesh was receptive to but did not initially scope)
