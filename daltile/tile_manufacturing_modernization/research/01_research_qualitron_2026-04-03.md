# 01 - Research: Qualitron (Shade and Caliber Inspection System)

**Source:** Web research
**Date:** 2026-04-06
**Document Set:** 01
**Context:** Understanding the only automated quality gate in DalTile's manufacturing process — what data it produces, how it integrates, and what expansion is possible for MES integration.

---

## Executive Summary

Qualitron is a vision inspection system manufactured by **System Ceramics** (a company within the **Coesia Group**, headquartered in Fiorano Modenese, Italy). It is the industry-leading system for post-kiln ceramic tile surface inspection, performing shade (tone/color) classification and surface defect detection. However, **Qualitron does not perform caliber (dimensional) measurement**. Caliber measurement is handled by a separate companion device called **LINER**, also made by System Ceramics. Planarity (flatness/warpage) measurement is handled by yet another companion device called **RedLine** or **PLANAR**. In practice, these three systems (Qualitron + LINER + RedLine/PLANAR) are deployed together at the end-of-line to provide the full shade + caliber + planarity quality gate before sorting.

The "Colletron" reference in the meeting transcript is almost certainly a speech-to-text error for "Qualitron." The "In-Surface" reference likely refers to **Surface Inspection**, a company within the SACMI Group that manufactures the competing **Flawmaster** inspection system. Surface Inspection is a brand/division, not a separate company named "In-Surface."

System Ceramics offers **Hypermate**, a Manufacturing Operations Management (MOM) platform that aggregates data from Qualitron and other line equipment, creates a digital twin, and enables real-time analysis. This is the primary integration pathway for connecting Qualitron data to an MES.

---

## 1. What Qualitron Is

### 1.1 Product Identity

| Attribute | Detail |
|---|---|
| **Product Name** | Qualitron (standard) / Qualitron XXL (large-format slabs) |
| **Manufacturer** | System Ceramics (Fiorano Modenese, Italy) |
| **Parent Company** | Coesia Group (Italian industrial/automation conglomerate) |
| **Product Category** | Vision inspection system for ceramic surfaces |
| **Position in Line** | Post-kiln, pre-sorting (end-of-line quality gate) |
| **Current Software Version** | Software 4.2 |

### 1.2 What Qualitron Actually Does (and Does Not Do)

**Qualitron performs:**
- **Shade (tone) classification** — Assigns tiles to shade groups based on color/tone consistency
- **Surface defect detection** — Identifies decoration defects (tone variations, banding, lines from digital printing, spots, stains)
- **Structural defect detection** — Identifies glaze application errors, structural imperfections
- **Decoration verification** — Via Creasync technology, compares each tile's printed decoration against the original digital graphic file
- **Synchronization verification** — Checks correct synchronization between structure and decoration

**Qualitron does NOT perform:**
- **Caliber (dimensional) measurement** — This is done by the separate **LINER** device
- **Planarity (flatness/warpage) measurement** — This is done by the separate **RedLine** or **PLANAR** device
- **Edge/corner defect detection** — Not its primary function (though some structural defects may be flagged)

This distinction is critical for the MES design: what DalTile likely calls "the Qualitron" may actually be a suite of System Ceramics devices (Qualitron + LINER + possibly RedLine) installed together at the end-of-line quality gate. The transcript's reference to "shade and caliber" as a single system suggests the operators may not distinguish between the individual devices.

### 1.3 Hardware Specifications

| Component | Specification |
|---|---|
| **Cameras** | 3 cameras: 2 grayscale + 1 color (latest-generation digital) |
| **Lighting** | System Electronics LED lighting system, 3-4 sources optimized for ceramic materials |
| **Self-adjustment** | Auto-adjusts to changes in tile thickness |
| **Positioning** | Micrometric positioning device for different tile thicknesses |
| **Speed** | Up to 200 pieces per minute |
| **Format Support** | Standard tiles and large-format slabs (XXL version), up to 1200x1800mm via Multigecko sorting |
| **Thickness Range** | 1 to 25mm (via Multigecko sorting integration) |

### 1.4 Software Capabilities (Software 4.2)

- **Self-learning algorithms** that refine detection during operation, continuously improving accuracy
- **Batch configuration system** — Each product has a "batch" containing all settings: format, reference images, diagnostics configuration, shade parameters, working thresholds
- **Automatic shader** (new in v4) — Completely rewritten for digital decorations. Stores decoration images and assesses differences between inspected shade and stored references
- **Manual shader** option — Operator can choose between automatic and manual shader in batch settings
- **Self-calibration** — After initial setup (which gets machine to 80-90% readiness), a further batch of tiles is passed to allow the machine to automatically calibrate diagnostics
- **Configurable shade ranges** — Multiple ranges can be set for each parameter; multiple shades can be defined with different colors for each
- **Defect classification** — Software recognizes various types of defects and transmits classifications to the sorting line control logic
- **MAN/AUTO selector** — Information is sent to the sorting line only when set to AUTO position

---

## 2. Companion Devices (The Full Quality Gate)

### 2.1 LINER — Caliber/Dimensional Measurement

| Attribute | Detail |
|---|---|
| **Function** | Monitors tile dimensions; classifies tiles into caliber groups |
| **Measurement** | Tile caliber (overall dimensions), shape defects |
| **Classification** | Trapezium effect, cushion effect, lack of square shape, out-of-caliber, and relevant caliber classes |
| **Thresholds** | User-configurable caliber threshold settings |
| **Format Support** | All shapes and sizes (tiles and slabs) |

LINER is the device that actually performs the "caliber" portion of what DalTile describes as their shade-and-caliber sorting. It measures the physical dimensions of each tile and classifies it into caliber groups based on user-defined thresholds.

### 2.2 RedLine — Planarity/Flatness Measurement

| Attribute | Detail |
|---|---|
| **Function** | Detects planarity/flatness defects |
| **Technology** | Non-contact laser triangulation: video camera + laser line generators (up to 9) |
| **Precision** | +/- 0.1mm (one-tenth of a millimeter) |
| **Measurement** | Acquires, reconstructs, visualizes and analyzes the profile of the entire tile surface |
| **Position** | Before the sorting line |

### 2.3 PLANAR — Alternative Planarity Measurement

| Attribute | Detail |
|---|---|
| **Function** | Detects curvature defects |
| **Technology** | Optical sensors (5 or 9 depending on tile size), non-contact |
| **Precision** | Tenth of a millimeter |
| **Format Support** | Any shape (hexagons, octagons, blunt corners) |
| **Usage** | Can be used on green (unfired) or fired tiles |

---

## 3. How Shade and Caliber Are Actually Measured

### 3.1 Shade Measurement

Shade measurement in ceramic tile manufacturing uses colorimetry based on the **CIE L\*a\*b\* color space**:

- **L\*** = Luminosity (0 = black, 100 = white)
- **a\*** = Red-green axis (positive = red, negative = green)
- **b\*** = Yellow-blue axis (positive = yellow, negative = blue)

**Process:**
1. Reference standard L\*a\*b\* values are defined for each shade group
2. Each tile is measured (via camera-based colorimetry in Qualitron, or via spectrophotometer for lab validation)
3. The tile is assigned to a shade group based on which reference its color falls closest to
4. Industry-standard shade codes are typically **Shade A, Shade B, Shade C** (letters indicating shade groups within a production run)
5. The CTDA shade variation rating system provides a broader classification: V1 (Uniform) through V4 (Substantial Variation)

**Qualitron's approach (Software v4):** The automatic shader stores decoration images as references and computes the difference between the inspected tile and stored references. When all measured parameters fall within ranges assigned to the same shade color, that shade is assigned. If any single parameter falls outside a range or into a different shade's range, the tile is classified as "out of shade."

### 3.2 Caliber Measurement

Caliber refers to the dimensional classification of tiles — essentially how close each tile's physical dimensions are to the nominal size.

**Measurement technology:**
- **Laser-based dimensional gauging** on the production line (in the LINER device)
- **Machine vision with cross-line laser** for ISO 10545-2 compliance (straightness of sides, rectangularity, side curvature, center curvature, warpage)
- **Laser triangulation** for 3D micro-inspection of surface profile and thickness

**Classification:**
- A difference of 1mm typically denotes a change in caliber group
- ANSI A137.1 defines caliber range as "an allowed size range for tiles to be used in the same installation"
- Tiles are grouped into caliber classes (typically 3 groups per the DalTile transcript) based on user-defined thresholds
- Modern dimensional accuracy achieves mean absolute error of 0.06mm

### 3.3 SKU Impact

The combination of shade groups and caliber groups creates the SKU matrix at the sorting line. Per the DalTile transcript: up to 3 shade groups x 3 caliber groups = up to 9 possible sort destinations per product run. Each unique shade+caliber combination must be tracked, packaged, and labeled separately.

---

## 4. Data Output and Connectivity

### 4.1 What Data Qualitron Produces

Based on available documentation, Qualitron generates the following data per tile:

| Data Element | Description |
|---|---|
| **Shade classification** | Assigned shade group (e.g., A, B, C) |
| **Defect type** | Classification of detected defect (tone, band, line, spot, stain, structural) |
| **Defect/no-defect decision** | Pass/fail for the sorting line |
| **Process images** | Captured images of each inspected tile (when integrated with Hypermate) |
| **Defect information record** | Complete data record per tile including defect details |
| **Sorting instruction** | Signal to the downstream sorting machine (Multigecko) indicating which class to assign |

### 4.2 Hypermate — The Data Integration Platform

**Hypermate** (formerly called "Prime") is System Ceramics' Manufacturing Operations Management (MOM) / smart factory platform. It is the primary pathway for extracting data from Qualitron and other line equipment.

| Capability | Detail |
|---|---|
| **Data extraction** | Extracts data from every connected machine on the line |
| **Data aggregation** | Aggregates, analyzes, and compares data in real time |
| **Digital Twin** | Creates a digital representation of the production line |
| **Per-tile traceability** | Each tile generates a complete data record including process images and defect information |
| **Real-time consultation** | Archive, extract, and consult data in real time |
| **3D plant navigation** | Visual factory floor representation |
| **MES/MOM integration** | Provides visibility into production processes |
| **Standardized data management** | Simplifies production processes through standardized data |

### 4.3 Connectivity and Protocols

**What is known:**
- Qualitron communicates with the downstream sorting line (Multigecko) via **control logic signals** — the software recognizes defects and "transmits them to the control logic of the sorting machines"
- The Multigecko sorting system receives commands via a **non real-time network such as Ethernet**
- Hypermate connects to machines on the line to extract and aggregate data
- System Ceramics' parent company Coesia operates in the Industry 4.0 space

**What is NOT publicly documented:**
- Specific industrial protocols (OPC UA, Modbus TCP, EtherNet/IP, PROFINET) are not explicitly mentioned in Qualitron documentation
- API specifications are not publicly available
- Database format for stored inspection data is not documented
- Whether Qualitron has a built-in OPC UA server or requires Hypermate as a middleware layer

**Reasonable inference for MES integration:**
Given that Hypermate is described as a MOM platform that creates a digital twin and provides MES-level visibility, the most likely integration architecture is:

```
Qualitron --> Hypermate (data aggregation layer) --> MES/Historian
LINER    -->          |
RedLine  -->          |
```

Rather than connecting directly to Qualitron's control logic, the MES integration would go through Hypermate. This is consistent with modern Industry 4.0 architectures where equipment-level data is aggregated through a middleware platform before reaching enterprise systems.

### 4.4 Data Granularity — Can More Be Captured?

This is a critical question for MES design. Based on the research:

**Currently available (with Hypermate):**
- Per-tile data records with process images and defect information
- Real-time data extraction from all connected machines
- Historical data archiving and consultation

**Likely configurable:**
- Number of shade groups and their thresholds (explicitly configurable per batch)
- Number of caliber classes and their thresholds (explicitly configurable in LINER)
- Which defect types are tracked vs. ignored
- Sensitivity of defect detection (working thresholds per batch)

**Unknown but worth investigating:**
- Whether raw measurement values (L\*a\*b\* readings, dimensional measurements in mm) can be extracted in addition to the classified results
- Whether historical trend data (shade drift over a production run, caliber drift) is available
- Whether the system can output continuous numerical values rather than discrete classifications
- What the data retention period is within Qualitron vs. Hypermate

---

## 5. Creasync — Patented Print Verification Technology

Creasync is a patented technology exclusive to System Ceramics that deserves special attention because it represents a data integration point between the decoration (printing) phase and the inspection phase.

**How it works:**
1. During decoration, tiles are printed using digital graphic files on a Creadigit printer (also by System Ceramics)
2. The original digital graphic file is made available to Qualitron
3. Qualitron compares each inspected tile's captured image against the source graphic file
4. This eliminates the need for physical reference samples (a significant time savings)
5. The system can recognize graphics even on rotated (180-degree) or sub-format tiles

**MES relevance:** Creasync implies that Qualitron already has a data link to the decoration system (Creadigit). This pre-existing integration could be a model for how inspection data flows back to earlier process stages. It also means the system has access to the design intent (the graphic file), which could enable more sophisticated quality metrics (e.g., "how far did this tile deviate from the design?") beyond simple shade classification.

---

## 6. Pre-Kiln Inspection — Additional Quality Gates

System Ceramics offers inspection systems that operate BEFORE the kiln, which could be relevant for a comprehensive MES design:

| System | Position | Function |
|---|---|---|
| **Tile Detector** | Before/at the decorator | Detects tile structure or decoration; sends input to Creadigit to select correct graphic |
| **Check Point** | Before firing (kiln entry) | Analyzes decorated or undecorated surface; checks for body and glaze defects; reduces color waste |
| **Creavision** | At digital printer | Vision and self-regulation system for digital printing quality |

These pre-kiln systems are significant because they could reduce waste by catching defects BEFORE the expensive firing process, rather than only after (where Qualitron sits).

---

## 7. Competitive Landscape

### 7.1 SACMI Group — Flawmaster+

SACMI (also Italian) is the primary competitor to System Ceramics in tile inspection.

| Attribute | Flawmaster+ (SACMI-Italvision) |
|---|---|
| **Cameras** | 3 high-resolution cameras with light sources at different angles |
| **Defect detection** | Surface, mechanical (corner, edge), reflection, decoration, shade, color, gloss |
| **Integrated caliber** | Available with integrated **Caliber Planarity Integrated (CPI)** device — "two machines in one" |
| **Installation options** | Upstream of sorting line, downstream of grinding, or at kiln exit |
| **AI capabilities** | Increasingly advanced quality control with AI (per Ceramic World Web, 2024) |
| **Brand structure** | Surface Inspection (brand) -> Flawmaster (product), now integrated with BMR/Italvision products |

**Key competitive difference:** Flawmaster+ with CPI integrates surface inspection AND caliber/planarity measurement in a single device. System Ceramics requires separate devices (Qualitron + LINER + RedLine). This may be a factor in DalTile's installed equipment.

### 7.2 The "In-Surface" Reference

The transcript reference to "In-Surface" most likely refers to **Surface Inspection**, the division/brand within the SACMI Group that manufactures the Flawmaster. This could mean:
1. DalTile has Flawmaster systems on some lines (not just Qualitron)
2. An operator or engineer was referring to the Surface Inspection brand when discussing inspection capabilities
3. "In-Surface" is a speech-to-text distortion of "Surface Inspection"

**Recent SACMI Group restructuring (2023-2025):**
- SACMI acquired 100% of BMR in 2023
- BMR then acquired 52% of Italvision
- Italvision products are being integrated with Surface Inspection products
- This creates a consolidated vision inspection portfolio within SACMI Group

### 7.3 Other Players

| Company | System | Notes |
|---|---|---|
| **Durst Group** | Digital decoration printers (Gamma series) | Not an inspection system; Durst manufactures the digital printers that decorate tiles. Their Gamma XD is a leading digital ceramic decorator. No proprietary inspection system identified. |
| **Keyence** | General vision inspection | Largest global player in vision inspection (7.26% market share). Not ceramic-specific but their systems can be configured for tile inspection. |
| **Cognex** | General vision inspection | Second-largest global player (1.90% market share). Not ceramic-specific. |
| **Intelgic** | AI-powered ceramic surface inspection | Newer entrant offering AI/ML-based ceramic inspection. Not yet at the scale of System Ceramics or SACMI. |

### 7.4 Market Context

The global AI visual inspection market reached approximately $24.1 billion in 2024 with a CAGR of ~22%. However, the ceramic tile inspection niche is dominated by two Italian companies: **System Ceramics** (Qualitron) and **SACMI** (Flawmaster). These two companies have decades of ceramic-specific expertise and installed bases in tile factories worldwide.

---

## 8. Implications for MES Design at DalTile

### 8.1 What to Confirm During Discovery

1. **Which specific devices are installed?** Qualitron alone, or Qualitron + LINER + RedLine? Or is it actually Flawmaster (SACMI) on some lines?
2. **Is Hypermate installed?** If yes, this significantly simplifies MES data integration. If no, direct device integration will be more complex.
3. **Software version?** Software 4.2 is current; older versions may have different data output capabilities.
4. **What data is currently being captured?** Just the sort decision (shade group + caliber group), or full per-tile records?
5. **Are Creasync-equipped printers (Creadigit) in use?** This would indicate an existing data link between decoration and inspection.
6. **What is the physical communication interface?** Ethernet is mentioned; need to confirm protocol (likely proprietary over TCP/IP, possibly with OPC UA available through Hypermate).

### 8.2 Integration Architecture Options

**Option A: Via Hypermate (Preferred if Available)**
- Hypermate already aggregates data from Qualitron and other line equipment
- Provides per-tile data records, real-time access, and historical archiving
- Would need to confirm Hypermate's external API/interface for the MES
- Lowest risk, most data available

**Option B: Direct Device Integration**
- Tap into the Ethernet communication between Qualitron/LINER and the sorting line
- Would capture sort decisions (shade group, caliber group, defect/no-defect)
- May miss granular data (raw measurements, images)
- Higher integration effort; requires understanding of proprietary protocol

**Option C: External Data Capture (Retrofit)**
- Install additional sensors or OPC UA gateways to capture signals
- Most complex and least desirable
- May be necessary for older equipment without Hypermate

### 8.3 Data Opportunities for MES

If Hypermate or direct integration is available, the MES could capture:

| Data Point | Value for MES |
|---|---|
| Shade classification per tile | Track shade distribution across a production run; detect shade drift |
| Caliber classification per tile | Track dimensional consistency; correlate with press or kiln parameters |
| Defect type and count | Track defect trends; identify root causes (printer issues, glaze issues, kiln issues) |
| First-pass yield | Percentage of tiles classified as first choice |
| Shade group distribution | How evenly production falls across shade groups (fewer groups = better consistency) |
| Reject rate | Tiles that fall outside all acceptable shade/caliber ranges |
| Production speed | Pieces per minute throughput at the inspection point |
| Process images | Visual documentation for quality disputes and root cause analysis |

### 8.4 Potential for Augmenting the Quality Gate

Based on the research, there are opportunities to expand what the current quality gate captures:

1. **Pre-kiln inspection** — Adding Check Point or Tile Detector before the kiln would catch defects earlier, reducing waste of fired tiles
2. **Finer shade granularity** — If raw L\*a\*b\* values can be extracted (not just classified groups), this enables statistical process control on color consistency
3. **Dimensional trending** — If raw mm measurements from LINER can be extracted, this enables correlation with upstream press parameters
4. **AI-enhanced defect classification** — System Ceramics is actively developing AI capabilities for Qualitron; newer versions may offer more detailed defect categorization
5. **Cross-line comparison** — With Hypermate, data from multiple lines can be compared to identify line-specific quality issues

---

## 9. Source Assessment and Confidence Levels

| Finding | Confidence | Basis |
|---|---|---|
| Qualitron is made by System Ceramics (Coesia Group) | **High** | Multiple official sources |
| Qualitron handles shade/surface defects, NOT caliber | **High** | Official product documentation distinguishes Qualitron from LINER |
| LINER handles caliber measurement | **High** | Official System Ceramics documentation |
| Hypermate is the data integration platform | **High** | Multiple official sources, including "Prime becomes Hypermate" announcement |
| Creasync compares tiles to digital graphic files | **High** | Patented technology, described in multiple sources |
| Software 4.2 has self-learning capabilities | **High** | Mentioned in official sources and manual references |
| "Colletron" is a speech-to-text error for "Qualitron" | **High inference** | No product called "Colletron" exists; phonetic similarity is strong |
| "In-Surface" refers to Surface Inspection (SACMI) | **Medium inference** | Surface Inspection is a real brand in this exact space; phonetic match is plausible |
| Hypermate provides MES-level data access | **Medium** | Marketing materials describe MOM/MES capabilities but specific API details are not public |
| OPC UA may be available through Hypermate | **Low-Medium** | Industry standard for this class of system, but not explicitly confirmed for Hypermate |
| DalTile uses Qualitron specifically (vs. Flawmaster) | **Medium** | Transcript context suggests "Qualitron" but should be confirmed on-site |

---

## Sources

- [Qualitron - Vision Control for Ceramic Products | System Ceramics](https://www.systemceramics.com/en/products/ceramic-machines/vision-control/qualitron)
- [Advanced Vision Inspection System - Qualitron | System Ceramics](https://www.systemceramics.com/en/solutions/product/qualitron)
- [Vision Inspection System for Ceramic Surfaces - Qualitron | System Ceramics](https://www.systemceramics.com/en/news/why-advanced-vision-inspection-systems-are-changing-the-way-ceramics-are-made)
- [Hypermate - Smart Factory Solution System | System Ceramics](https://www.systemceramics.com/en/products/ceramic-machines/smart-factory/hypermate)
- [Trace, understand, automate: Prime becomes Hypermate | System Ceramics](https://www.systemceramics.com/en/news/trace-understand-automate-prime-becomes-hypermate)
- [LINER - Quality Control Device | System Ceramics](https://www.systemceramics.com/en/innovation/ceramic-machines/vision-control/liner)
- [Red Line - Tiles Quality Control System | System Ceramics](https://www.systemceramics.com/en/ceramic-machines/quality-control/red-line)
- [PLANAR - Quality Control Device | System Ceramics](https://www.systemceramics.com/en/innovation/ceramic-machines/vision-control/planar)
- [MULTIGECKO - Tile Sorting Line | System Ceramics](https://www.systemceramics.com/en/innovation/ceramic-machines/sorting-lines/multigecko)
- [Tile Detector - Ceramic Print Quality Control | System Ceramics](https://www.systemceramics.com/en/innovation/ceramic-machines/vision-control/tile-detector)
- [Check Point - Tiles Quality Control | System Ceramics](https://www.systemceramics.com/en/innovation/ceramic-machines/vision-control/check-point)
- [Ceramic Quality Control Machines | System Ceramics](https://www.systemceramics.com/en/ceramic-machines/quality-control)
- [Ceramic Tiles Manufacturing Machine | Coesia](https://www.coesia.com/en/industries/ceramics)
- [Qualitron Manual Eng (Scribd)](https://www.scribd.com/document/662523675/Qualitron-Manual-Eng)
- [Qualitron Brochure (Scribd)](https://www.scribd.com/document/687168344/Brochure-Qualitron-En)
- [System Ceramics Qualitron Brochure PDF](https://www.systemceramics.com/sites/default/files/prod/2019-09/2019_09%20Qualitron%20IT_EN.pdf)
- [Flawmaster - SACMI Group](http://www.sacmi.com/en-US/Products-and-Services/Ceramics/Business-Units/Tiles/Tile-inspection-and-control-systems/Flawmaster.aspx?LN=en-US&idC=66667)
- [Increasingly advanced quality control with AI | Ceramic World Web](https://ceramicworldweb.com/en/technology/increasingly-advanced-quality-control-ai)
- [BMR acquires Italvision | Ceramic World Web](https://www.ceramicworldweb.com/index.php/en/news/bmr-acquires-italvision)
- [Surface Inspection launches the new Flawmaster | Ceramic World Web](https://ceramicworldweb.com/index.php/en/technology/surface-inspection-launches-new-flawmaster)
- [System Ceramics upgrades Piemme's sorting department | Ceramic World Web](https://ceramicworldweb.com/en/news/system-ceramics-upgrades-piemmes-sorting-department)
- [Advanced technologies for tile sorting and packaging | Ceramic World Web](https://www.ceramicworldweb.com/en/technology/advanced-technologies-tile-sorting-and-packaging)
- [System automation for the end-of-line | Ceramic World Web](https://www.ceramicworldweb.it/cww-en/technology/system-automation-for-the-end-of-line/)
- [Ceramic Tiles Measurement and Classification | Konica Minolta](https://sensing.konicaminolta.asia/ceramic-tiles-measurement-and-classification/)
- [How Ceramic Manufacturers Set Color Standards | Konica Minolta](https://sensing.konicaminolta.us/us/blog/how-ceramic-manufacturers-set-color-standards-for-raw-material-suppliers/)
- [Spectrophotometric Analysis for Color Consistency in Ceramic Tile | HunterLab](https://www.hunterlab.com/blog/exploring-how-spectrophotometric-analysis-can-enhance-color-consistency-in-ceramic-tile/)
- [ASTM C609 - Standard Test Method for Light Reflectance Value and Small Color Differences Between Pieces of Ceramic Tile](https://www.astm.org/c0609-23.html)
- [Dimensional deviation measurement of ceramic tiles according to ISO 10545-2 | Springer](https://link.springer.com/article/10.1007/s00170-018-2781-4)
- [Ceramics - Durst Group](https://www.durst-group.com/Segment/Ceramics)
- [Vision systems for slabs and tiles | SACMI](https://sacmi.com/en-US/control-vision-systems/vision-for-slabs-and-tiles)
- [SACMI Sorting Lines](https://sacmi.com/ceramics/tiles/automatic-sorting-packaging-palletizing-lines)
- [Qualitron Vision System | StoneContact.com](https://www.stonecontact.com/products-m5382/qualitron-vision-system-for-shade-detection-quality-control-machine)
