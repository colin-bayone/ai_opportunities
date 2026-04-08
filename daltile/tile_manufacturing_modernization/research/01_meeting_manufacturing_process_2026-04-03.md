# 01 - Meeting: Manufacturing Process Flow (End-to-End)

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Focused deep dive on tile manufacturing process

---

## Overview

Mahesh Adnani walked Colin through the complete tile manufacturing process using factory walkthrough videos (recorded on his phone during a recent plant visit) and a PowerPoint slide showing the process flow diagram. The conversation covered every stage from raw material preparation through finished goods warehousing, with Mahesh providing video walkthroughs of each step and Colin drawing parallels to other manufacturing processes (silicon carbide, diamond polishing) to contextualize the engineering challenges.

The factory shown is Dal-Tile's Muskogee (Oklahoma) facility, referred to as "Plant 2." Mahesh's head office is approximately 20 minutes away. Plant 1 is adjacent but smaller with less equipment.

---

## Process Flow Diagram (from PowerPoint)

The PowerPoint slide titled "Tile Making" showed the following linear process flow:

```
Raw Material --> Body Prep --> Press --> Dryer --> Glaze Lines <-- Glaze Prep
                                                      |
                                                   Printer
                                                      |
                                                    Kiln
                                                      |
                                              [Polishing] (optional)
                                                      |
                                            [Rectification] (optional)
                                                      |
                                               Qualitron
                                          (Shade and Caliber)
                                                      |
                                            Sorting (MES currently
                                               integration)
                                                      |
                                              Packaging
                                                      |
                                            Warehouse (FGI)
```

Polishing and Rectification are marked as optional. The factory shown in the walkthrough videos does not perform these steps. Glaze Prep feeds into the Glaze Lines as a parallel input (proprietary glaze material preparation).

---

## Stage-by-Stage Manufacturing Process

### 1. Raw Material Preparation

**What happens physically:** Clay, dirt, and other raw materials are mixed and rolled in large ball mills to create a slurry. The slurry is then converted back to a dry powder form suitable for pressing.

**Mahesh's characterization:** "You basically take dirt, clay and a few things, you mix them and you roll them in these big giant balls, if you will, to make it into a slurry and then back to a powder."

**Priority:** Mahesh deprioritized this stage, stating: "This side of the process I'm not so worried about because this is more like a raw material preparation. Ideally we would want to go there, but I think we have bigger problems before we go there."

**Quality checks at this stage:** Some sites perform moisture checks during body prep. Several sites are pushing for more measurement at this stage. The moisture content of the raw material is one variable that Colin identified as critical for predicting downstream caliber outcomes.

**Recycling constraint:** Pre-fired material (everything before the kiln) can be crumbled and fully recycled back into raw material. Post-fired material can only constitute 6% of the raw material input, per regulations or internal R&D standards. This creates an economic inflection point at the kiln stage.

### 2. Body Prep

**What happens physically:** The powder from raw material preparation is prepared and conditioned for pressing. This includes ensuring proper moisture content and consistency of the material before it enters the press.

**Detail level from transcript:** Mahesh did not elaborate extensively on body prep as a distinct step, grouping it conceptually with raw material preparation.

### 3. Press

**What happens physically:** Powder is fed into a hydraulic press. The press compresses the powder with water and binding materials into a flat tile shape of the specified dimensions. The press stamps out tiles one at a time, and they are immediately placed onto a conveyor belt.

**Mahesh's description:** "This is your actual press. It's pressing this material and it is creating a tile of this size, for example. And the conveyor belt is bringing these tiles, moving them into this location."

**Tile at this stage:** A raw, fragile, unfired tile. Still contains significant moisture.

**Equipment count (Plant 2):** 6 presses. Mahesh also referenced 7 presses at one point when describing the work order planning scenario. The Pi historian dashboard shown during the call displayed presses labeled 1, 3, 4, and 5 (press 2 was noted as removed/gone).

**Tile sizes produced:** Range from 6x48 (long plank format) to 24x24 (largest square tile). Intermediate sizes mentioned include 12x24, 24x24, and 24x48.

**Sensors at this stage:** Press machines have readouts displaying operational parameters (Mahesh showed a screenshot from a press machine display). These readings "can tell you whether the press is doing the right thing or wrong thing." Some sites have Pi historian database connections that can capture press counts. Currently, operators reset press counters daily at 6:00 AM and track cumulative square feet pressed per day.

**Waste at this stage:** 100% waste occurs during initial setup when configuring a new item, until conveyors and alignment are dialed in. Pre-kiln waste is considered low priority by the operations team because the material can be fully recycled.

**Automation:** Fully automated, no human intervention. Press feeds directly to dryer via conveyor belt.

### 4. Dryer

**What happens physically:** A long oven-like structure (inline dryer) that removes excess moisture from the freshly pressed tile. The tile passes through on a conveyor belt. The purpose is to reduce moisture so the tile can be handled without cracking, but the tile is still unfired and fragile at this point.

**Mahesh's description:** "This long thing, if you will, is essentially a small oven. You can think of it, which is basically drying the tile. And at the end of this you will basically have a tile that is not yet done. It is not baked yet, but it is still a raw tile."

**Tile at this stage:** "Still brittle. It's not still a tile, but at least it is going to not crack immediately if somebody was to just touch it."

**Sensors at this stage:** Some sites track the count of tiles entering vs. exiting the dryer through the Pi historian dashboard. The dashboard Mahesh showed indicated that out of 15,000 square feet pressed, only 14,000 made it to the dryer (indicating loss between press and dryer).

**Automation:** Fully automated, continuous flow from press. No human intervention. "There's nobody on the floor. It is just one machine feeding to the other through a conveyor belt. There is no manual intervention whatsoever."

**Process continuity:** Press and dryer operate as a continuous unit. "Think of it as press and drying as the first stage."

### 5. Glaze Lines (with Glaze Prep)

**What happens physically:** A proprietary glaze material is prepared separately (Glaze Prep) and applied to the dried tile. The glaze acts as a primer coat, similar to applying a white base coat before painting a wall. Multiple coats of glaze may be applied across multiple stations within the glaze line.

**Mahesh's description:** "Think of it as applying a primer. So if you are painting a wall, you are painting a white color first right before you do the actual color." The glaze line applies coating, and "on the other side when you see the tile, it is almost like a white color tile at that particular point."

**Multiple glaze applications:** Mahesh showed two glaze line videos. "There are multiple coatings of the glaze line you do." The tile passes through multiple stations within the glaze line.

**Equipment count (Plant 2):** 6 glaze lines. The Pi historian dashboard showed glaze lines with varying uptime, indicating they are not all running simultaneously. Uptime variation is driven by press throughput: "I didn't have enough production coming from the press, so I couldn't keep these two lines busy."

**Fan-out from press to glaze:** One press can feed multiple glaze lines. The Pi historian dashboard showed press 1 feeding glaze lines 1 and 2. In principle, 4 presses could feed 6 glaze lines depending on production needs.

**Sensors at this stage:** Glaze lines have light curtain sensors that count tiles passing through. Some sites can report how many times glaze has been applied. However, light curtain sensors are unreliable in the dusty environment: "If somebody comes in and puts a book, now all of a sudden the count is very unrealistic." This leads to impossible data such as more tiles exiting the glaze line than entered (e.g., 22,500 input but 22,800 exited).

**Waste at this stage:** Glaze material is a costly component. Operations starts caring about waste once glaze is applied because it cannot be freely recycled like pre-glaze material.

**Automation:** Fully automated, conveyor belt driven.

### 6. Printer (Digital Printing)

**What happens physically:** A large digital printer applies the decorative pattern/design to the glazed tile. The tile enters with the white glaze coat and exits with visible color and pattern. This is the step that gives each tile its visual appearance (wood grain, marble, stone pattern, etc.).

**Mahesh's description:** "At the end of the printer line you will see... now you have an actual something that you would call it as a tile seen. Obviously it's not still with the polish and the color brightness, because once it goes to the oven, obviously the colors will become more enhanced."

**Post-print protective glaze:** After printing, there is another line of glaze applied on top of the printed pattern. This protective coat prevents the printed color from burning during kiln firing. "Before they put it into the heat, you will see they apply another white coat on top of it so that that can burn and the next layer will shine." This means the tile is no longer visually inspectable after the printer stage at most factories. However, Mahesh noted that the timing of this protective coat varies by site: "In other sites the printer actually prints and then immediately puts a glaze like within the next 5 seconds."

**Quality inspection opportunity (Colin and Mahesh discussion):** Colin identified this as a potential upstream quality checkpoint. Even though the tile is subsequently covered with protective glaze, a camera at the printer output (before the protective coat) could capture the printed pattern and correlate it to final Qualitron output. Mahesh agreed: "If I took a picture of that stage and I start comparing not to the final output but to this output... the final output will be much more colorful or much more enhanced, but at least you can compare it to this image."

**Equipment count (Plant 2):** 6 printers.

**Sensors at this stage:** Some sites have light curtain sensors at the printer. Same reliability issues as glaze line sensors.

**Automation:** Fully automated, conveyor belt driven.

### 7. WIP Buffer (Pre-Kiln Staging)

**What happens physically:** After printing (and post-print protective glazing), tiles are stacked into batches and placed into shelf-like holding structures. LGVs (laser-guided vehicles / automated guided vehicles) transport these stacked batches from the printer area to the kiln staging area. Tiles are loaded into carriers/carts that feed the kiln.

**Mahesh's description:** "Once it is printed then it is going to just stack it up and it is going to keep it ready for an LGV to come and pick it up. You can see it is stacking it up, where once the whole stack is done, it's going to move this material to the right... rolling onto this, and then it is just going to put it up on one of these shelves, and these are basically tied to a machine, and they are just keeping it ready for the next batch for the oven."

**Process continuity:** "This to me is the first place where the process gets broken from a continuous fashion to a semi-continuous fashion because this is the first area where you see actually WIP happening. Because before this it's all continuous, you know, one process after the other."

**Tracking challenge:** Two tiles run parallel on the conveyor up through the printer. At this stage, they are combined with other tiles: "Now it is going into a huge area. At this point you kind of lose track of which tile went where, because now we are going into a WIP staging area and it's no longer two tiles, it's maybe 8 to 10 tiles put together."

**Manual quality sampling:** Because of the long process distance between printer and Qualitron (with the kiln in between), some sites perform hourly manual quality sampling at this stage: "Every hour somebody walks in and says let me take one of the tiles from the printer and let me just put it in the kiln in the first location and they mark it with a marker. Then they wait for that tile to come out of the kiln, go and do the analysis directly."

### 8. Kiln (Firing)

**What happens physically:** Tiles are fed into a large kiln (industrial-scale oven) where they undergo a multi-stage thermal process: initial heating, temperature ramp-up to peak firing temperature, cooling, and in some cases additional temperature changes. The kiln transforms the raw tile into a hardened ceramic product and enhances the color/pattern vibrancy.

**Mahesh's description:** "A pretty huge kiln area where the kilns are just heating it up initially for a temperature, then raising the temperature, eventually cooling it down. And then raising it back again because of the process that they need to go through."

**Physical scale:** Mahesh emphasized the enormous size of the kilns, showing video of the kiln area. Multiple conveyor lines feed tiles into the kiln entrance.

**Equipment count (Plant 2):** 4 kilns. Kilns are labeled (e.g., "Kiln 7" was referenced during the walkthrough). The Pi historian dashboard showed kilns 1, 2, and 3 with production data.

**Fan-in from glaze/printer to kiln:** Multiple press/glaze/printer lines converge into fewer kilns. For example, 6 presses feeding 6 glaze lines and 6 printers may converge to 4 kilns. This fan-in pattern contributes to the WIP buffer before the kiln.

**Correlation loss at kiln:** The kiln is where product-level traceability breaks down: "Once you are at the kiln, which line went into which kiln? Because there is no correlation. So now what you do is you start doing only measurement on your machines, you don't do measurements on your product." Mahesh explained that after the kiln, the part number "magically" reappears at sorting, but with no lineage of which specific press/glaze/printer line produced which tiles in a given kiln batch.

**Quality implications:** The kiln is the critical transformation step. The ceramic engineers maintain that quality testing cannot be done until after firing ("you can't do testing till it is baked, for whatever reason"). Colin challenged this assumption, noting it is common across manufacturing but not necessarily true with sufficient upstream data collection.

**Waste significance:** Post-kiln waste ("fired waste") is the most costly category. Post-fired material can only be recycled at a maximum of 6% of raw material input. Mahesh reported hearing repeatedly that "our fired waste is more than our green waste," which he found problematic given the lack of upstream testing.

### 9. WIP Buffer (Post-Kiln Staging)

**What happens physically:** Tiles exit the kiln and are stacked into holding areas/shelving, creating another WIP buffer. These tiles await transport to the next stage (Qualitron or polishing/rectification if applicable).

**Mahesh's description:** "The output of the kiln is again going into a WIP. The big oven is running through. Once it is done, it is now stacking up in these type of places, power lifts, and just keeping the tiles together. But again it is creating another area of work order inventory because it's not going directly to the next line. Now what happens is, and this causes them some problems."

**WIP tracking:** The Pi historian dashboard showed WIP tracking with three categories:
1. Post-glaze, pre-kiln WIP (gone from glaze line but not yet entered kiln)
2. Post-kiln, pre-polishing/rectification WIP (out of kiln, awaiting next step)
3. Pre-sorting line WIP (waiting for sorting)

### 10. Polishing (Optional)

**What happens physically:** Mechanical polishing of the fired tile surface to achieve a glossy finish.

**Applicability:** Not performed at the Muskogee Plant 2 facility shown during the walkthrough. "The factory that I showed you doesn't do this polishing and rectification." The Pi historian dashboard included polishing line data, suggesting other Dal-Tile factories use this step.

### 11. Rectification (Optional)

**What happens physically:** Mechanical trimming/grinding of tile edges to achieve precise dimensional uniformity.

**Applicability:** Not performed at the Muskogee Plant 2 facility. Optional step in the process flow diagram.

### 12. Qualitron (Quality Inspection)

**What happens physically:** An automated quality inspection machine that evaluates tiles for shade (color consistency) and caliber (dimensional accuracy including height, weight, dimensions, thickness, and flatness/curvature).

**Mahesh's description:** "It's basically determining what type of product it is." The Qualitron assigns shade and caliber classifications to each tile.

**Classification outputs:** Tiles are classified by shade (e.g., shade 1, shade 2, shade 3) and caliber (caliber 1, caliber 2, caliber 3). This creates multiple SKU variants from what was originally a single work order.

**Rejection categories (from Pi historian dashboard):** Surface defects, caliber, and other coded rejection types. The sorting line data showed rejection rates varying significantly (e.g., 2% to 10%).

**Significance:** The Qualitron is "the only true testing" point in the entire process. Everything upstream relies on the kiln output being acceptable. Mahesh emphasized: "They only reject for shade and caliber." Colin noted that if shade and caliber could be predicted upstream, it would be transformative: "If we can figure shade and caliber somewhere upstream in the process, we are golden."

**Equipment count (Plant 2):** 5 Qualitrons.

**Shade contributors:** Glaze line, printer, and kiln collectively create the shade. The glaze and print determine the applied color; the kiln firing enhances and finalizes it.

**Caliber contributors:** Mahesh hypothesized that caliber relates to "height, weight, dimension, thickness, and whether it's flat or whether it's curvy." Warping/bending occurs during kiln firing. Colin suggested caliber could be predicted from a combination of raw material moisture content, dryer performance, and kiln consistency.

### 13. Sorting Line

**What happens physically:** Based on the Qualitron classification, tiles are automatically sorted into groups by shade and caliber combination. Multiple shade/caliber groups create separate SKUs. Tiles are stacked into groups, with each group containing tiles of the same shade and caliber.

**Mahesh's description:** "They will say this one is shade one, this one is shade two, this one is shade three. This one is caliber one, caliber two, caliber three. And then they will basically make three SKUs based on the shade and the caliber, and they will stack it into a particular group."

**Current MES integration:** The sorting line is the only stage where the current "MES" (label printing solution) operates. This is the Progress-based software running on machines with blue screens and serial port connections to SATO label printers.

**Equipment count (Plant 2):** 5 sorting lines.

**Waste tracking:** This is the only stage where waste/rejection is formally tracked. Finance uses the sorting line rejection rate (e.g., 9%) as the total wastage figure, ignoring all upstream losses. Mahesh challenged this: "It's more than 9% wastage. You can see there's wastage over here, over here, over here. They're not even tracking any of that."

### 14. Packaging (Boxing and Labeling)

**What happens physically:** Sorted tile groups are fed into a boxing machine. The machine places tiles into boxes. A label printer prints and applies a label to each box using a PLC-controlled mechanical process:
1. Box arrives on conveyor belt
2. PLC raises a stop mechanism to position the box
3. Box is aligned/adjusted
4. Label is printed and cut
5. A push mechanism applies the label to the box
6. Box is scanned to verify label placement
7. Box continues on conveyor

**Label printing technology:** SATO label printers controlled by a custom Progress application (the "blue screen" software). Labels are programmed via SATO printer language directly in code, not through a visual label designer. The Progress application communicates with the printer via serial port. Mahesh wants to modernize this: "They are literally programming this printer using SATO language rather than a designer label."

**Private label support:** Dal-Tile manufactures tiles for other brands (e.g., Home Depot). Different work orders/item numbers require different label formats depending on whether the product is sold under the Dal-Tile brand or a private label customer brand.

**Equipment:** PLC-controlled boxing and labeling machines at the sorting line output.

### 15. Palletizing

**What happens physically:** Boxes are arranged onto pallets by an automated palletizer. The palletizer builds pallet loads from the boxed tiles.

**Equipment count (Plant 2):** 1 palletizer. "You don't need so many palletizers, wrappers."

### 16. Pallet Wrapping and Labeling

**What happens physically:** Completed pallets go through a multi-step finishing process:
1. Banding/strapping ("putting the ribbon")
2. Plastic wrap ("wrapping it up through plastic")
3. Pallet-level label printing and application

**Mahesh's description:** "The pallet comes in from here and then it just rollers. They're putting the ribbon. After the ribbon, they're basically just wrapping it up through plastic. And then they are basically putting a pallet print label, because now you have a pallet, you want to put a label that is for the pallet itself."

### 17. Warehouse (Finished Goods Inventory)

**What happens physically:** Wrapped and labeled pallets are transported to the finished goods warehouse (FGI) for storage and eventual shipping.

**WIP at this stage:** The finished goods warehouse represents the final WIP/inventory buffer point.

---

## WIP Buffer Points Summary

Mahesh identified 3-4 WIP (work-in-process) buffer points where the continuous process breaks:

| WIP Point | Location | Description |
|-----------|----------|-------------|
| WIP 1 | Pre-Kiln | Tiles stacked into shelves after printing, awaiting kiln. First break from continuous flow. LGVs transport between stages. |
| WIP 2 | Post-Kiln | Tiles stacked after exiting kiln, awaiting Qualitron/sorting. Creates work order inventory correlation challenges. |
| WIP 3 | Pre-Palletizer | Sorted and boxed tiles awaiting palletizing. |
| WIP 4 | Finished Goods | Palletized product in warehouse. |

**Continuous segments:**
- Press through Printer (including Dryer and Glaze Lines): Fully continuous conveyor belt flow, no human intervention, no breaks
- Qualitron through Packaging: Continuous once tiles enter the Qualitron

**Semi-continuous segments:**
- Printer to Kiln: WIP buffer with LGV transport
- Kiln to Qualitron: WIP buffer

---

## Equipment Counts and Fan-In/Fan-Out (Plant 2, Muskogee)

| Stage | Equipment Count | Notes |
|-------|----------------|-------|
| Press | 6 | Pi dashboard showed presses 1, 3, 4, 5 (press 2 removed) |
| Glaze Lines | 6 | Uptime varies based on press throughput |
| Printers | 6 | One-to-one with glaze lines in most cases |
| Kilns | 4 | Multiple press/glaze/printer lines fan into fewer kilns |
| Qualitrons | 5 | Quality inspection machines |
| Sorting Lines | 5 | Parallel to Qualitrons |
| Palletizer | 1 | Sufficient for all sorting line output |

**Fan-in/Fan-out patterns:**
- 6 presses can feed 6 glaze lines (generally 1:1, but one press can feed 2 glaze lines)
- 6 glaze lines feed 6 printers (1:1)
- 6 printers fan into 4 kilns (multiple lines per kiln)
- 4 kilns fan out to 5 Qualitrons and 5 sorting lines
- 5 sorting lines fan into 1 palletizer

Mahesh noted the variability: "One of this press could feed 2 glaze lines and then three of these glaze lines could feed a single kiln." This dynamic routing makes work-order-level tracing difficult because the same work order can be split across multiple downstream machines.

---

## LGV (Laser-Guided Vehicle) Material Transport

LGVs (automated guided vehicles) handle material transport between stages, particularly at WIP buffer points. They move stacked tiles between the printer area and kiln staging, and between the kiln output and the Qualitron/sorting area.

**Data from LGVs:** The Pi historian dashboard included an LGV section showing "where they are parked, what they carry and all of that." Mahesh noted this data comes from the LGVs themselves and is visible on the right side of the dashboard.

---

## Conveyor Belt Automation

The entire production line is conveyor belt driven. Two tiles run side by side on the conveyor from press through printer. There is zero human intervention required when the line is running properly.

**Mahesh's characterization:** "Everything is automated. Literally there's no human if the line was working perfectly. You don't need a single human there. Unfortunately, the line doesn't work always smoothly, so there are people involved. But they are mostly there to fix the issue when something goes wrong."

**Colin's observation on automation advantage:** Because the process is PLC-driven rather than human-driven, movement is predictable. This means even when tiles go out of camera view (e.g., entering the kiln WIP staging), logic from the PLC can determine exactly where each tile went, enabling tracing without continuous visual tracking.

---

## Physical Plant Context

### Plant 2 (Muskogee, Primary Target)
- **Satellite view reference:** Mahesh showed a satellite/aerial view of the Dal-Tile Muskogee facility
- **Scale:** The manufacturing building is very large; the office area ("this tiny sliver") is dwarfed by the factory footprint. The parking area that fits approximately 8 cars provided a scale reference for the overall building length
- **Layout:** Press operations begin at one end; finished goods exit at the far opposite end
- **Proximity:** Mahesh's head office is approximately 20 minutes away
- **Characterization:** This is the older of the two plants but has been selected as the modernization target due to proximity

### Plant 1 (Adjacent)
- Located adjacent to Plant 2 on the same property
- Smaller facility with less equipment
- Shorter building footprint visible from satellite view

### Network Infrastructure
- Factory floor networking is poor: "They have not done a real good network structure in the manufacturing floor"
- Given the enormous footprint, network drops are costly
- Not a clean environment, so wireless connectivity is challenging
- Colin suggested XBee-type radio communication protocols as a solution for distributed factory environments with limited Wi-Fi

### Production Volume
- Approximately 400,000 square feet of tile per day per plant
- The Pi historian dashboard showed daily production figures (e.g., 15,000 sq ft from one press, 28,000 sq ft through a kiln)

---

## Sensor and Data Collection Landscape

### Existing Sensors
- **Press machines:** Have operational parameter displays/readouts. Some sites connected to Pi historian database
- **Glaze lines:** Light curtain sensors for tile counting
- **Printers:** Light curtain sensors for tile counting
- **LGVs:** Track location, cargo, and status

### Light Curtain Sensor Problems
Light curtain sensors are deployed at glaze lines and printers for counting tiles, but they are unreliable in the dusty manufacturing environment:
- Dust accumulation on sensors causes miscounts
- Physical obstructions (someone placing an object near the sensor) cause false counts
- Result: impossible data, such as more tiles exiting a stage than entering (e.g., 22,500 input to glaze line, 22,800 output)
- Executive trust in the data erodes when they see impossible numbers: "Once people look at this type of data, then they start doubting everything else"

### Pi Historian Database (Select Sites Only)
Two sites have Pi historian databases that collect machine data. The dashboard shown during the call displayed:
- Press-level production (square feet by press number, tile size)
- Glaze line throughput (input vs. output square feet, uptime percentage)
- Kiln throughput (input vs. output)
- WIP levels at three staging points
- Polishing line data
- Sorting line data (including rejection rates by category)
- LGV positions and status

### Current Measurement Approach
- Measurement is machine-based, not product/work-order-based
- Track square meters of output, not items or work orders
- Press counters reset daily at 6:00 AM
- No correlation between stages (cannot trace which press output went through which kiln)
- No error categorization between stages (only at Qualitron/sorting)
- Finance tracks only sorting line rejection as total wastage, ignoring all upstream losses

---

## Equipment Vendors

Three companies supply virtually all tile manufacturing equipment globally. Mahesh identified two by name:

1. **SACMI** (referred to as "Scammy" in transcript) - Italian equipment manufacturer providing presses and other equipment
2. **Qualitron** (also "In-Surface") - Defect detection/quality inspection machines and possibly other surface inspection equipment
3. **Third vendor (unnamed)** - Provides additional equipment

These companies have an unusual business model: they not only sell equipment but also manufacture tiles themselves, selling branded tiles to competitors. "These three companies interestingly also produce tiles and sell it to competitors or to us as well. So they are like, we will make, we will give you the tile making process and we will sell you a machine to do the tile."

Mahesh noted that most tile manufacturers rely heavily on these vendors for process know-how rather than developing their own engineering capabilities: "A lot of people just rely on those machines rather than creating their own engineering to say, how can I make this better?"

---

## Key Process Characteristics

### What Daltile Tracks Today vs. What They Should Track

| Metric | Current State | Desired State |
|--------|--------------|---------------|
| Production volume | Square feet per day, per machine | Per work order, per stage |
| Work order routing | Not tracked (no work order at machine level) | Full routing: which press, glaze, printer, kiln, Qualitron, sorting line |
| WIP levels | Rough counts by staging area | Per work order WIP at each buffer point |
| Waste/yield | Only at sorting line (Qualitron stage) | At every stage from press through packaging |
| Lineage tracing | None through kiln (correlation lost) | End-to-end from press to finished goods |
| Machine uptime | Daily aggregate | Per work order, enabling utilization analysis |

### Quality Rejection (Only at Qualitron/Sorting)
- **Shade rejection:** Color inconsistency. Driven by glaze line, printer, and kiln interaction
- **Caliber rejection:** Dimensional deviation (thickness, flatness, curvature, edge straightness). Driven by raw material moisture, press consistency, and kiln firing profile
- **Surface rejection:** Surface defects (tracked in sorting line data)
- **Overall reported rejection rate:** Example of 9% at sorting, but actual total loss across all stages is higher

### The "Green Waste vs. Fired Waste" Divide
- **Green waste** (pre-kiln): Can be fully recycled into raw material. Operations considers this "no loss." Includes waste from press, dryer, glaze, and printer stages
- **Fired waste** (post-kiln): Can only be recycled at 6% of raw material input. This is where financial loss is recognized
- **Implication:** Executives have repeatedly noted that fired waste exceeds green waste. Mahesh's argument: "This is stupid. Why are you not doing any testing [upstream] if you think that's what you want to do?" This is a core driver for wanting upstream quality inspection
