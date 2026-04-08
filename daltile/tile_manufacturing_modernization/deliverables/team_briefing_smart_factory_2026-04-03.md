# DalTile Smart Factory Opportunity: Team Briefing

**Date:** 2026-04-06
**Audience:** Internal BayOne team member (computer vision and smart factory specialist)
**Purpose:** Background briefing ahead of onboarding call

---

## The Client

DalTile is a division of Mohawk Industries, the world's largest flooring manufacturer. They make ceramic and porcelain tiles at multiple plants across the US. Our primary contact is Mahesh Adnani, an IT leader responsible for manufacturing technology. Colin and Mahesh worked together previously at Coherent Corporation, where they built a custom manufacturing visibility platform. This is a relationship-driven engagement with no competitive bid.

## The Factory

The target facility is DalTile's Sunnyvale (Muskogee, Oklahoma) plant, referred to internally as "Plant 2." It is the larger of two adjacent plants, with a production volume of approximately 400,000 square feet of tile per day. The facility operates:

- 6 hydraulic presses
- 6 glaze lines
- 6 digital printers
- 4 kilns
- 5 Qualitron inspection machines
- 5 sorting lines
- 1 palletizer and wrapping station

The manufacturing floor is large (comparable to a warehouse), dusty, and has limited network infrastructure. Existing connectivity is a mix of serial ports, spotty WiFi, and costly hardwired drops.

## The Manufacturing Process

Tile manufacturing is a linear, highly automated process with virtually no human intervention when running smoothly:

1. **Raw Material / Body Prep** -- Clay and minerals are mixed into a slurry and dried to powder
2. **Press** -- Powder is hydraulically pressed into tile blanks of various sizes (6x48 to 24x24 inches)
3. **Dryer** -- Pressed tiles pass through an oven to remove excess moisture (tiles are still fragile at this point)
4. **Glaze Lines** -- A proprietary base coat (primer) is applied, followed by multiple glaze layers
5. **Printer** -- Industrial inkjet printers apply the design/pattern to the tile surface
6. **Protective Coat** -- A second white glaze layer is applied over the printed design to protect it during firing
7. **Kiln** -- Tiles are fired at high temperature through massive kilns, emerging as finished hard tiles with enhanced color
8. **Polishing / Rectification** -- Optional finishing steps (not performed at this plant)
9. **Qualitron** -- Automated shade (color) and caliber (dimensional) inspection. The ONLY quality gate in the entire process.
10. **Sorting** -- Tiles classified into SKUs by shade grade and caliber grade (up to 3 of each)
11. **Packaging** -- Boxed, labeled, palletized, wrapped, and sent to finished goods warehouse

**Critical flow characteristics:**
- Stages 2 through 6 are continuous (conveyor belt, no human touch)
- There are four WIP (work-in-process) buffer points where tiles are stacked and batched, breaking the continuous flow: before the kiln, after the kiln, at palletization, and finished goods
- Equipment fans in and out: 6 press lines can feed 6 glaze lines, which converge to 4 kilns, then fan back out to 5 sorting lines
- LGVs (laser-guided vehicles) transport stacked tiles between WIP buffer areas

## The Core Problem: No Visibility, No Traceability, Late Quality Detection

### Quality testing happens too late

The Qualitron machine, after the kiln, is the only automated quality check. Tiles are rejected for two reasons:

- **Shade** -- color inconsistency (driven by glaze, printing, and kiln firing)
- **Caliber** -- dimensional issues like thickness variation, warping, or curvature (driven by moisture content and kiln conditions)

Everything upstream of the Qualitron, including press, dryer, glaze, printer, and kiln, has zero inline quality testing. The only upstream check is a manual hourly process where a worker pulls a tile from the printer, marks it with a physical marker, places it at the front of the kiln queue, waits for it to fire, then visually inspects it. By the time a defect is detected, thousands of square feet of tile are already in the pipeline.

### Waste is underreported

Finance reports approximately 9% waste based on sorting line rejections (post-kiln). But waste occurs at every stage: press startup waste, dryer waste, glaze misapplication, printer errors. None of this upstream waste is measured or tracked. Mahesh believes true waste is significantly higher than reported.

There is a critical economic threshold at the kiln: pre-kiln waste ("green waste") can be fully recycled back into raw material. Post-kiln waste ("fired waste") can only constitute 6% of raw material input per regulatory and R&D constraints. This means detecting defects before firing has dramatically higher economic value than detecting them after.

### No work order lineage

Today the factory tracks production only in aggregate: total square feet pressed, total kiln output, total finished goods. There is no correlation between a specific work order and its journey through individual pieces of equipment. Once tiles enter the WIP buffer before the kiln, identity is lost entirely, and it does not reappear until sorting.

### Existing sensors are unreliable

Light curtain sensors at some stages count tiles, but they produce impossible data (more tiles exiting a stage than entering it) because dust contamination and physical obstructions cause false triggers. Executives who see this data stop trusting all of it.

## Where Computer Vision and Sensors Fit

This is where the opportunity gets interesting from a smart factory perspective:

### Upstream quality detection

The ceramic engineers at DalTile claim "you can't test until it is baked." Colin disagrees. The data to predict post-kiln quality exists at upstream stages, it is just not being captured. Specifically:

- **Shade prediction:** The tile's printed design is visible between the printer and the protective glaze coat. Even though the final fired color differs from the pre-fire appearance, correlating pre-fire images to post-fire outcomes over time would build a predictive model. The window for image capture varies by plant: some sites have a few seconds of visibility, others have a longer gap between printer and protective coat.

- **Caliber prediction:** Caliber issues (warping, thickness variation) correlate strongly to two variables: raw material moisture content and kiln firing conditions. Simple humidity sensors at the kiln output would capture post-fire moisture data. Combined with raw material moisture specs and kiln temperature profiles, this creates a predictive dataset for caliber outcomes.

### Camera deployment

The factory has favorable physical conditions for camera installation:
- Extensive 80/20 aluminum extrusion framing throughout the facility provides ready-made mounting points
- Existing safety guarding around automated equipment creates defined sightlines
- Tiles move on flat, open conveyor belts with consistent spacing

Challenges:
- Dusty environment requires industrial-grade cameras with purge gas, built-in wipers, or appropriate IP-rated housings
- Camera count estimated at 15-20 per production line, possibly fewer
- Factory floor networking needs a solution (XBee radio modules or similar for large-footprint, low-infrastructure communication)

### PLC data extraction for traceability

One of the most promising opportunities: since all tile movement through WIP staging areas is PLC-driven (automated stackers, LGVs, kiln feeders), the movement is deterministic and predictable. Even when tiles are out of camera vision (stacked in racks, inside the kiln), their position can be inferred from PLC control logic. This means traceability does not require cameras at every point. Instead, it requires extracting the movement logic from the existing Siemens PLCs to build a computational tracking model. Colin observed modern Siemens PLCs on the factory walls during the video walkthrough.

### Existing untapped sensor data

Before specifying new hardware, there is a significant opportunity in capturing data the existing equipment already produces:
- Press machines have readout displays showing operational parameters (pressure, cycle counts)
- Glaze line light curtains may measure glaze thickness (not just presence), depending on the angle
- Kilns have temperature sensors and zone control data
- The PI Historian database at some sites already ingests some of this data, but with no work order correlation

Colin's recommendation: inventory what signals are "free" before specifying new hardware.

### Reliability engineering constraint

Any solution must operate independently of cloud connectivity. The factory runs 24/7 and cannot stop production if Azure goes down. Latency-critical operations (label printing has a three-second window) must process locally. Sensor data collection and quality monitoring should operate on-floor with cloud sync for analytics and dashboards.

## The Engagement Shape

Mahesh has a software budget of approximately $250,000 across multiple plants. Hardware (PLCs, sensors, cameras) falls under a different team's budget that Mahesh does not control, but he wants to demonstrate what is possible to force that team's hand.

The plan is to start with one production line at the Sunnyvale Plant 2 and prove the concept before expanding. Colin's next step is to visit the factory, assess the physical environment, and develop a phased proposal.

Tech stack: Python, PostgreSQL on Azure, Azure Container Apps, with on-floor edge components for reliability.

## What We Need From You

Your expertise in computer vision and smart factory systems is directly relevant to several threads in this engagement:

1. Camera placement strategy and hardware specification for a dusty industrial environment
2. Vision-based quality inspection: feasibility of correlating pre-fire tile images to post-fire outcomes
3. Sensor architecture: what to capture, where, and how to get it back to a central system in a large facility with limited networking
4. PLC data extraction approaches for traceability through WIP staging
5. Edge computing architecture for on-floor processing with cloud analytics

## Equipment Vendor Ecosystem

### SACMI (Imola, Italy)

SACMI is a EUR 1.7 billion Italian worker cooperative (founded 1919), the world leader in ceramic press manufacturing. 4,700+ employees across 70+ companies in 25+ countries. U.S. office in Brentwood, Tennessee. Supplies equipment across the full line: PH series hydraulic presses, dryers, DHD series inkjet printers, DDG texture systems, MAESTRO kilns, and Flawmaster+ AI-powered quality inspection.

**Critical discovery item:** SACMI offers its own MES-level platform called **H.E.R.E.** with modules for plant monitoring, machine control, trends, alarms, production reports, recipe management, ERP integration, and individual tile tracking (ID-Tiles). If deployed at Muskogee, any custom solution must integrate with it, replace it, or coexist.

**Data connectivity:** Newer SACMI equipment uses Ethernet Powerlink fieldbus (not OPC-UA natively). Integration depends on what PLCs sit underneath (likely B&R or Siemens, both support OPC-UA).

### System Ceramics / Qualitron (Fiorano Modenese, Italy)

System Ceramics (Coesia Group) manufactures the Qualitron system. Critical finding: **Qualitron handles only shade and surface defects.** Caliber is measured by a companion device called **LINER** (laser-based dimensional gauging). Planarity by **RedLine/PLANAR**. What DalTile calls "the Qualitron" is likely 2-3 devices installed together.

- Shade measurement uses CIE L*a*b* color space with configurable thresholds
- System Ceramics offers **Hypermate**, a data platform that aggregates per-tile records from Qualitron, LINER, and other line equipment in real time. This is the most viable integration path.

### Third Vendor (Unidentified)

Likely **Surface Inspection** (SACMI Group brand, makes Flawmaster), or possibly SITI B&T Group (Italy) or KEDA (China). To be confirmed during site visit.

## Computer Vision Opportunities in Detail

### Pre-Fire Shade Prediction via Image Correlation

The core hypothesis: capture images of tiles after the printer (where the design is visible), correlate with post-fire Qualitron shade classifications over thousands of tiles, and build a predictive model.

- **Capture window:** Several seconds at this plant between printer and protective coat (as short as 5 seconds at other plants). High-speed line-scan cameras triggered by conveyor encoders.
- **Color space:** Qualitron uses CIE L*a*b*. Pre-fire capture should use calibrated color pipeline for meaningful correlation.
- **Illumination:** Consistent, repeatable illumination essential. Semi-enclosed conveyor at printer stage is favorable for controlled LED arrays or dome illumination.
- **Reference comparison:** Each tile has a known target design from the printer's digital file. Deviation metric may predict shade classification.
- **Training data:** Initial deployment collects paired pre-fire/post-fire data for supervised learning.

### Dimensional Measurement for Caliber Prediction

- **Laser triangulation profiling:** Laser line across tile surface with angled camera measures height variations, thickness uniformity, edge straightness.
- **Structured light scanning:** Full 3D surface profiling for pre-fire warping/bowing detection.
- **Correlation target:** Raw material moisture + pre-fire dimensions + kiln temperature profiles should predict post-fire caliber classification.

### Conveyor Counting and Tile Tracking

Vision-based counting via overhead cameras would replace unreliable light curtain sensors. Cannot produce phantom counts from dust. Can assign temporary identity to each tile for traceability through continuous segments.

### Waste Detection at Reject Points

Cameras at known reject/discard points count and classify waste events in real time, providing the upstream waste visibility that finance currently lacks.

## Site Visit Discovery Questions

### Equipment and Vendor Data
- Which equipment is SACMI vs. System Ceramics vs. third vendor? Model/generation?
- Is SACMI H.E.R.E. deployed? Which modules?
- Is Hypermate deployed alongside Qualitron?
- What data does each controller expose? What protocols?
- What generation are the Siemens PLCs? S7-300 (legacy), S7-1500 (modern), or mix?

### Vision and Camera Deployment
- Conveyor speed at each stage?
- Ambient lighting at printer output? Consistent or variable?
- Window between printer output and protective glaze coat at this plant?
- Where are physical reject/discard points?
- Dust particle size and density (determines IP rating and cleaning interval)?

### Sensor and Network Infrastructure
- What does the PI Historian capture at this plant? Polling interval?
- Press readout displays: digital outputs or visual only?
- Glaze line light curtains: measure thickness (angled) or presence only (perpendicular)?
- Network topology on factory floor? Existing Ethernet drops?
- Wireless access points or mesh networks?
- Distance from furthest equipment to nearest network closet?

### PLC and Traceability
- Can we access PLC programs for WIP stacking and kiln feeding? Documented?
- What determines rack position for tile stacks before kiln? Deterministic or first-available?
- Kiln routing logic: PLC or manual operator?
- Can LGV fleet management system export movement logs?
