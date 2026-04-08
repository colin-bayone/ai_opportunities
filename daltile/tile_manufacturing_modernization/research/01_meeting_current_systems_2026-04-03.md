# 01 - Meeting: Current Systems and Technology Landscape

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Focused deep dive on existing technology

---

## 1. The "MES" That Is Not an MES

### What DalTile Calls MES

Mahesh stated this directly: "They call it MES, but literally it's a label printing solution that you saw in the sorting line. That's what they have that my group supports." There is no manufacturing execution system in the traditional sense. There is no work order tracking, no stage-by-stage yield accounting, and no real-time production visibility tied to product identity. The only system Mahesh's team owns and operates is the label printing infrastructure on the sorting/packaging line.

### What the Label Printing System Actually Does

The label printing system handles:
- **Box labels:** Printed at the sorting/packaging line as boxes of finished tiles are assembled. The label includes barcode, item number, manufacturing date, and other product identification.
- **Pallet labels:** Printed after boxes are palletized and wrapped. A separate label identifies the pallet as a unit for warehouse and logistics.
- **Private-label support:** DalTile manufactures tiles for other brands (Home Depot was the example given). The label printing system must select the correct label template depending on whether the product is DalTile's own brand or a private-label customer.

The label printing system does not track work orders, does not correlate to upstream production stages, and does not interface with any quality system.

---

## 2. Progress/OpenEdge Codebase

### The Language and Architecture

The label printing system is written in **Progress** (OpenEdge), a legacy 4GL database language. Mahesh described it as "really old school" and expressed clear intent to kill it: "I want to get rid of this."

Mahesh specifically asked Yogesh (BayOne leadership) whether BayOne could take the existing Progress code and modernize it as a fixed-bid project, rewriting it in .NET, C#, or Python with an Oracle or similar database backend.

### How Label Design Works (SATO Printer Language)

Labels are not designed using a label design tool or visual editor. Instead, someone has manually written raw **SATO code** (SATO is a printer command language specific to SATO thermal printers) that provides low-level instructions to the printer:

- Position coordinates for where to print each element on the label
- Barcode generation commands for the item number
- Text placement for manufacturing date and other fields

Mahesh described this: "Somebody has manually, not via a label designer, but via SATO code, has given instructions to the printer to say on this location print the barcode for item number, on this print the manufacturing date."

This approach means that label changes require someone who understands SATO printer language at the command level. There is no abstraction layer, no template system, and no drag-and-drop interface.

### The Blue Screen Computer

Colin observed a specific detail in one of the factory walkthrough videos: a computer with a blue screen (indicating a text-mode or terminal-style application) at the sorting/packaging line. This is the Progress application running on a dedicated machine. Colin noted: "I saw the blue screen, I got nervous, but then I saw on the side of it, it has a serial port which is the thing that's routed back to the printer."

This blue screen terminal is the frontend for the Progress/OpenEdge application. It communicates with the SATO printer via a serial port connection (RS-232 or similar) physically wired from the computer to the printer.

### Communication Path: Serial Port to Printer

The data flow for label printing is:

1. The Progress application on the blue screen computer determines which label to print based on the current production run
2. The application generates raw SATO printer commands
3. Those commands are sent over a **serial port** (physical wired connection) from the computer to the SATO printer
4. The printer receives the commands and prints the label
5. A PLC-controlled mechanical arm pushes the printed label onto the box as it passes on the conveyor belt

The serial port infrastructure was custom-built by the legacy team. This is not standard Ethernet/TCP-IP networking. The serial connections are point-to-point physical cables between the computer and each printer.

### PLC Integration in the Labeling Process

The label printing process is tightly coupled to PLCs on the sorting/packaging line:

- A PLC raises a physical stop mechanism when a box arrives at the labeling station
- The box is positioned and aligned
- The label is printed and cut
- A PLC-controlled mechanism pushes the label onto the box
- A scanner verifies the label was applied correctly
- The PLC releases the stop and allows the box to continue on the conveyor

Mahesh described this as a three-second window: "It literally has a three-second window where it starts tracking that the box is coming, it prints and puts the label, lets it go." This tight timing is a critical constraint for any replacement system, as latency in communication (such as a round-trip to Azure) could delay the conveyor belt.

### Why the Progress Code Must Be Replaced

Three converging factors drive replacement urgency:

1. **Team departure:** The three-person legacy team that wrote all of this code is gone. Two members have left and the third is retiring. One junior person remains who handles labeling tasks but does not have deep knowledge of the Progress codebase or the custom serial port infrastructure.

2. **Network team refusal:** The serial port network was custom-built by the legacy team. The corporate network team does not want to manage it. Mahesh stated: "The serial ports they created themselves and frankly what happened is that network team doesn't want to manage it. My team has no knowledge of it."

3. **Modernization to Ethernet/TCP-IP:** Mahesh wants to move from serial port communication to standard Ethernet and TCP/IP so that the network team can own the infrastructure: "I want to really move back to Ethernet ports and TCP/IP and say you know what, you work with the network guys to get the printer, you work with the network guys to get the drop."

---

## 3. The Legacy Three-Person Team

This team is central to understanding the current systems landscape because they built almost everything themselves:

- **Wrote the Progress/OpenEdge label printing code** that is the only "MES" DalTile has
- **Created their own servers** to run the application
- **Built their own network infrastructure** including custom serial port wiring from computers to printers
- **Programmed SATO printers** using raw SATO command language rather than a label designer

Two of the three have left. The third is retiring. One junior person remains who has some development skills and handles labeling, but does not have the depth of knowledge to maintain the custom infrastructure.

This team's departure means the institutional knowledge of how the serial port network is wired, how the Progress code works, and how the SATO printer commands are structured is disappearing. Mahesh inherited this team and is clear that he does not want to sustain this approach.

---

## 4. PI Historian Database

### What It Is

A PI historian database (OSIsoft PI, the industry-standard time-series database for industrial process data) exists at some DalTile manufacturing sites. It collects sensor data from production machines.

### What Data It Collects

The PI historian receives data from sensors throughout the production line:

- **Press counts:** How many times the press has cycled (how many tiles pressed)
- **Glaze line throughput:** How many tiles have passed through glaze application
- **Printer throughput:** How many tiles have been printed
- **Kiln throughput:** Input and output counts for kiln loading/unloading
- **LGV (Laser Guided Vehicle) status:** Position, load status, and transport tracking for the automated guided vehicles that move WIP between stages

### Which Sites Have It

Not all sites. Mahesh described it as "a couple of sites" where the historian database is operational and where "some of this data is visible to them." The Sunnyvale factory (the target site for the initial project) appears to be one of these sites, based on the dashboard that Mahesh showed during the call.

### Limitations

The PI historian captures machine-level data, not product-level data. It knows how many times a press cycled but does not know which work order those cycles belonged to. There is no correlation between the historian data and work orders, item numbers, or production batches.

---

## 5. The Semi-MES Dashboard (Eric William's Dashboard)

### What It Is

Mahesh found this dashboard via an email from Eric William (a DalTile colleague). It is a visualization layer built on top of the PI historian database. Mahesh described it as "the only true MES or semi-MES that I saw."

### What the Dashboard Shows

The dashboard provides a production flow view with the following sections:

**Press section:**
- Press numbers (1, 3, 4, 5 — press 2 has been decommissioned)
- Tile size being produced on each press (24x48, 24x24, 12x24, etc.)
- Square feet pressed per machine

**Glaze section:**
- Glaze line numbers (1 and 2 in the example shown)
- Which presses feed which glaze lines (e.g., press 1 feeds glaze lines 1 and 2)
- Product description
- Input count (square feet entering the glaze line)
- Output count (square feet exiting the glaze line)
- Uptime percentage per glaze line (significant variation observed — driven by whether upstream presses are feeding enough volume to keep the glaze line busy)

**Kiln section:**
- Kiln numbers (1, 2, 3 in the example)
- Input and output in square feet
- No correlation to which upstream glaze line or press fed which kiln

**WIP tracking:**
- Three WIP buffer zones displayed:
  1. Post-glaze, pre-kiln (tiles waiting to enter the kiln)
  2. Post-kiln, pre-polishing/rectification or pre-sorting
  3. Pre-sorting line (waiting for the sorting line)

**Sorting line section:**
- The only place where rejection data appears
- Shows loaded count, rejection percentages by category:
  - Surface defects
  - Caliber failures
  - Other coded rejection types
- Example: 15,000 loaded with 2% rejection on one line, 10% on another

**LGV section:**
- Real-time position and status of automated guided vehicles
- Load/cargo tracking
- Parking positions

**Polishing line section (some sites):**
- Separate section for polishing/rectification data (not applicable to the Sunnyvale target factory, which does not do polishing)

### Data Quality Problems

The dashboard has a critical credibility problem with sensor data reliability. Mahesh demonstrated a specific example:

- **Glaze line input:** 22,500 square feet
- **Glaze line output:** 22,800 square feet
- **Problem:** The glaze line cannot create 300 extra tiles. This is physically impossible — count can only decrease at each stage (due to breakage/waste), never increase.

Mahesh explained the consequence: "People who look at this data from an executive level start saying this is not real... once people look at this type of data, then they start doubting everything else." Executive distrust of the data undermines the entire dashboard's usefulness.

The root cause is light curtain sensor unreliability (covered in detail in section 7 below).

### What the Dashboard Lacks

Even where the data is accurate, the dashboard has fundamental gaps:

- **No work order correlation:** Production is measured in aggregate square feet per machine, not per work order or item number. Mahesh: "They don't measure work orders. They basically see how much tiles did we press, how much kiln did we use and how much output did we produce in thousands of square meters."
- **No lineage tracing between stages:** There is no connection between which press output fed which glaze line, which glaze line output went into which kiln. Mahesh: "Once you are at the kiln, which line went into which kiln? There is no correlationship."
- **No waste attribution:** The dashboard shows input and output at each stage, but the difference (waste) is not tracked, categorized, or attributed. The only rejection data appears at the sorting line.
- **Product identity lost at WIP:** When tiles go from continuous flow into WIP staging areas (particularly before and after the kiln), the dashboard loses the ability to say which product is which. Mahesh: "Once it crosses this again, you have zero idea what is this 28,000. Is it this one? Is it this one?"

### What the Dashboard Gets Right

Despite its limitations:
- It does provide real-time machine-level throughput visibility
- The LGV tracking is functional and provides useful logistics data
- It shows uptime percentages per machine, which helps identify utilization gaps
- The sorting line rejection data (surface, caliber, other) is genuine quality data, even if it only captures the final gate

---

## 6. PLC Infrastructure

### Brands and Age

Colin observed PLCs on the factory wall in the walkthrough videos and identified them as **Siemens** (or possibly Cegelec/Celine, though Siemens is the most likely interpretation given the context). He noted a mix of ages: "Some things are really old, some things are really new."

### Role of PLCs

PLCs control virtually every automated process on the factory floor:

- **Press operation:** Cycling the press to form tiles from powder
- **Conveyor belt movement:** Moving tiles between stages
- **Dryer operation:** Temperature and timing control
- **Glaze line:** Application of glaze coatings
- **Printer operation:** Digital tile printing
- **Kiln loading/unloading:** Stacking tiles onto kiln cars and unstacking after firing
- **Labeling station:** The stop/position/print/apply/release sequence (three-second window)
- **Sorting line:** Routing tiles to different stacks based on Qualitron shade/caliber classification
- **Palletizer and wrapper:** Final packaging automation

### Vendor Dependency

Mahesh explained that the PLC configuration and programming largely comes from the three equipment vendors (SACMI, Qualitron, and the surface defect tracking company). The on-site PLC team does not do much independent work: "Even the PLC guys don't really do a lot of good work. They rely on their three companies."

This means that PLC programming knowledge lives with the equipment vendors, not with DalTile. When a new machine is installed, the vendor configures the PLCs. DalTile operates but does not deeply understand or modify the PLC code.

### Data Availability from PLCs

Colin noted that PLCs are a potential source of untapped data: "Since everything's PLC driven, it's actually better because this is automated. So it's like... if it's PLC driven and there's not human in the loop interaction for the most part, it's predictable."

Colin suggested that PLC data could be used to trace tile movement through WIP areas where cameras cannot see: "We can basically get that logic out from the PLC and figure out exactly where that tile went."

However, the degree to which current PLCs expose data varies by age and model:
- **Newer machines:** Full data connectivity available ("Some of them are very, very latest and you can get all sort of data from them")
- **Older machines:** No modern connection method ("Some of the sites have older machines, so they don't have a modern way to connect to them")

---

## 7. Sensor Infrastructure and Reliability

### Light Curtain Sensors

The primary counting mechanism throughout the production line is **light curtain sensors**. These sensors create a beam of light across the conveyor belt path; when a tile passes through and breaks the beam, it registers a count.

Light curtains are present at:
- Glaze line (confirmed by Mahesh: "In the glaze line they have a light curtain basically that creates a sensor")
- Printer line (Mahesh: "I think they have a similar one in the printer")
- Likely at other stages as well, wherever the PI historian is collecting count data

### Light Curtain Reliability Problems

Light curtain sensors have well-known failure modes in this environment:

1. **Dust accumulation:** The tile manufacturing floor is not a clean environment. Ceramic dust settles on sensor lenses and emitters, degrading the optical signal. Mahesh: "These sensors have to be kept clean because otherwise they collect a lot of dust."

2. **False triggers from obstructions:** If anything other than a tile breaks the beam — a piece of paper, a book, a person's arm, debris — it registers as a tile count. Mahesh: "If somebody comes in and puts a book, now all of a sudden the count is very unrealistic."

3. **Resulting data impossibility:** The false triggers produce counts where more tiles exit a stage than entered it, which is physically impossible. Mahesh gave the specific example: "I did only 1000 press, but 1500 things came out of the printer and that's not possible. In every step you can reduce the quantity, but you never increase the quantity."

This sensor reliability problem is the direct cause of the executive credibility gap with the semi-MES dashboard data.

### Light Curtain Dual Use (Colin's Observation)

Colin noted that light curtains in some installations serve a more sophisticated purpose than simple counting. When angled, they can also measure glaze thickness: "I'm not sure if they're just a sensor in the sense that it's saying that something is gonna cross me. Sometimes they'll also have light curtains as a way... you can always tell cause there'll be an angle and it'll tell you the thickness of the glaze too." It was not confirmed whether DalTile's light curtains perform this function.

### Press Machine Displays

The press machines have built-in displays showing operational readings (not part of the light curtain system). Mahesh showed one during the walkthrough and described the opportunity: "This was what was on the press machine and these readings actually can tell you whether the press is doing the right thing or wrong thing. And ideally what I would love to do is ingest that every 5 minutes."

These press displays likely show parameters such as pressing force, cycle count, cycle time, and possibly die temperature. The data is visible on the machine but is not currently captured in any database. Ingesting it at five-minute intervals would be sufficient for MES-level monitoring without creating excessive data volume (Mahesh noted: "For one plant, we make like 400,000 square feet every single day... it doesn't make a lot of sense to store all of that data, at least for a high level MES").

### Sensors DalTile Does Not Have

The following sensor data was discussed as desirable but not currently collected:

- **Humidity/moisture sensors at kiln output:** Colin identified this as a key missing data point for predicting caliber defects. Moisture content after firing correlates to tile warping and dimensional variation.
- **Upstream moisture sensors (body prep/press):** Some sites are pushing for this. Mahesh: "They do moisture checks and things like that in the body prep and that's what many sites are pushing for now."
- **Vision/camera systems:** No cameras currently exist in the production line for quality inspection or tile tracking. Cameras are a future addition that Colin recommended.

---

## 8. Daily Counter Reset Process

All machine counters throughout the factory are **manually reset to zero every day at 6:00 AM**. Mahesh described this: "They reset the counter for the presses every single day at 6:00 AM. So essentially what they do is, there is a button or there's a way where you can say put it back to zero. They do it every... for all the machines, they do it at 6:00 AM and now they keep tracking off it from 6:00 AM."

This means:
- All production counting starts from zero each day
- The semi-MES dashboard presumably reflects same-day cumulative production since the 6:00 AM reset
- There is no ability to track a work order that spans multiple days without losing the count continuity
- Executive reporting is based on these daily counter snapshots

Mahesh wants to reset counters per work order instead of per day, which would enable work order-level yield tracking. However, this is resisted by the operations team: "They are like, no, no, no, we can't do that. All the reports go to all the executives. We don't want to do that."

The resistance has a practical basis: because one press can feed two glaze lines and multiple glaze lines can feed a single kiln, resetting counters per work order becomes complicated when multiple work orders share equipment. The current daily reset sidesteps this complexity by simply aggregating everything.

---

## 9. Equipment Vendor Ecosystem

### The Three Vendors

Three companies supply the vast majority of DalTile's tile manufacturing equipment:

1. **SACMI** (Italian) — Major ceramics equipment manufacturer. Supplies presses, dryers, glaze lines, printers, kilns, and other core production equipment. Also manufactures tiles and sells branded tiles to other companies. Mahesh: "There is one company that supplies... I'm going to say there are three companies that supply all these materials."

2. **Qualitron** — Quality inspection machine manufacturer. The Qualitron machine is the primary quality gate, performing shade and caliber classification after the kiln. Multiple Qualitron units per plant (the Sunnyvale factory has approximately 5).

3. **Surface defect tracking company** (name not clearly stated in the transcript) — Provides in-surface defect detection equipment. Likely supplies vision-based or laser-based surface inspection systems.

### Vendor Model

These vendors operate a dual business model:
- They **sell equipment** to tile manufacturers like DalTile
- They also **manufacture tiles** themselves and sell branded tiles to other companies (including DalTile's competitors)

Mahesh found this model surprising and problematic: "These three companies interestingly also produce tiles and sell it to competitors or to us as well. So they are like, we will make, we will give you the tile making process and we will sell you a machine to do the tile."

### Vendor Dependency for PLC and Machine Configuration

When a new machine or line is installed, the equipment vendor configures everything including PLC programming. DalTile's on-site teams rely on vendor support rather than developing their own process engineering expertise. Mahesh: "If you go to the site, they will tell you how to do every single thing. And the machine that they have is essentially coming from them."

This creates a dynamic where:
- DalTile operates the equipment but does not deeply understand or optimize it
- PLC logic is a black box managed by the vendor
- There is limited internal capability to extract data from machines beyond what the vendor's standard interface provides
- Newer vendor machines may have modern data connectivity; older ones do not

---

## 10. Factory Floor Networking

### The Physical Challenge

The Sunnyvale factory has a massive physical footprint. Mahesh showed satellite imagery during the call: the office building is a "tiny sliver" compared to the manufacturing floor. Plant 2 (the larger, older plant and the initial target for modernization) is significantly larger than Plant 1.

### Current Network Constraints

- **Network drops are costly:** Running Ethernet cable across the factory floor is expensive due to the distances involved and the industrial environment. Mahesh: "Since the footprint is so big, network drops and others become very costly."
- **WiFi is unreliable:** The combination of large open space, metal equipment, dust, and electrical interference from industrial equipment makes wireless connectivity spotty. Mahesh: "Wireless and network sometimes becomes a big challenge in the factories."
- **The custom serial port network is orphaned:** The legacy team's serial port infrastructure has no owner. The network team will not manage it, and Mahesh's software team does not have the knowledge to maintain it.

### Colin's Observations and Recommendations

Colin assessed the networking challenge as manageable based on what he observed in the factory videos:

- **Favorable physical layout:** The factory is flat with open, high ceilings (warehouse-style). This is good for radio-based communication.
- **XBee-type radio communication:** Colin suggested protocols used in exactly this type of environment — large distributed factories where standard WiFi is impractical and wired drops are too expensive. These are short-range radio modules commonly used in industrial IoT deployments.
- **Interference assessment:** The main risks for radio communication are metal obstructions and large AC motors. Colin assessed that the tile factory likely does not have severe versions of either: "The only time that gets tricky is if there's a lot of metal in the way or if there's these big AC motors that create a lot of interference, but you don't have that."

### Azure and Internet Dependency

The organization has Azure available. However, Mahesh raised a critical constraint: manufacturing cannot depend on internet connectivity. If Azure goes down, the factory must continue operating. Mahesh: "If the Internet goes down, they can't stop manufacturing."

The three-second labeling window is the most latency-sensitive operation. A round-trip to Azure for label data would risk delaying the conveyor belt. Colin agreed that the architecture must have complete separation of concerns: "Azure being up or down, existing or not existing shouldn't impact anything on the factory and vice versa."

This means the solution architecture requires an on-premises component (at minimum for label printing and PLC communication) with asynchronous data synchronization to Azure for dashboards, analytics, and reporting.

---

## 11. LGVs (Laser Guided Vehicles)

The factory uses automated guided vehicles (LGVs) to transport WIP between production stages. These are particularly important at the WIP buffer points:

- Moving stacked tiles from the glaze line/printer output to the kiln loading area
- Moving fired tiles from the kiln output to the sorting line area

The LGV system has its own tracking data visible in the semi-MES dashboard, showing:
- Vehicle position
- Load/cargo status
- Parking locations

Mahesh confirmed these are automated: "They use LGVs, the automated machines. So you can see all those automated machines are the ones that are basically saying where they are parked, what do they carry."

The LGV tracking data is one of the more reliable data streams in the current system, as it comes from the vehicle control system rather than from the problematic light curtain sensors.

---

## 12. Systems and Technology Summary Table

| System/Technology | Status | Data Quality | Coverage | Owner |
|---|---|---|---|---|
| Progress/OpenEdge label printing | Active, slated for replacement | N/A (not a data system) | Sorting/packaging lines | Mahesh's team (departing) |
| SATO printer hardware | Active | N/A | Sorting/packaging lines | Mahesh's team |
| Serial port network | Active, orphaned | N/A | Computer-to-printer connections | No owner (network team refuses, legacy team departed) |
| PI historian database | Active at some sites | Mixed (sensor data unreliable) | Press, glaze, printer, kiln counts | Unclear |
| Semi-MES dashboard | Active at some sites | Poor (impossible count data) | Press through sorting, LGVs | Eric William (built/shared it) |
| Light curtain sensors | Active | Unreliable (dust, false triggers) | Glaze line, printer, possibly others | Equipment vendors |
| Press machine displays | Active (local display only) | Presumed good (machine-native) | Each press machine | Equipment vendors |
| PLCs (Siemens and others) | Active, mix of old and new | Presumed good (machine-native) | Every automated stage | Equipment vendors |
| LGV tracking system | Active | Good (vehicle control system) | WIP transport between stages | Operations |
| Qualitron machines | Active | Good (purpose-built quality gate) | Post-kiln quality inspection | Equipment vendor |
| Azure (organization-level) | Available | N/A | Not yet deployed for manufacturing | IT |

---

## 13. Key Constraints for System Design

Based on the current technology landscape, any replacement or new system must account for:

1. **Three-second labeling window:** The label printing system has a hard real-time constraint. Cannot depend on cloud connectivity.
2. **Internet independence:** Manufacturing must continue if Azure or internet connectivity fails.
3. **No reliable count data from light curtains:** The sensor infrastructure produces physically impossible readings. Any MES that depends on these counts will inherit the credibility problem.
4. **Heterogeneous PLC age:** Some machines have modern connectivity; others require manual or specialized data extraction approaches.
5. **Dusty industrial environment:** All sensors, cameras, and exposed electronics must be rated for ceramic dust contamination.
6. **Large factory footprint with poor networking:** Standard WiFi and wired Ethernet are both problematic. Industrial radio (XBee or similar) or purpose-built IoT networking protocols may be required.
7. **Vendor black-box machines:** PLC logic and machine data interfaces are controlled by equipment vendors (SACMI, Qualitron, surface defect company), not by DalTile.
8. **Daily counter reset at 6:00 AM:** Current reporting depends on this daily reset. Work order-level counter resets are desired but politically and technically complicated due to equipment sharing across work orders.
9. **No internal engineering depth:** The legacy team is gone. The PLC team relies on vendors. There is one junior person. Any solution must be maintainable by a small, potentially less-experienced team.
