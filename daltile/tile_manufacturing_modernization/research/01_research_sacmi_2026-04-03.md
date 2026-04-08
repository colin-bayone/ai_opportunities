# 01 - Research: SACMI (Ceramics Equipment Manufacturer)

**Source:** Web research
**Date:** 2026-04-06
**Document Set:** 01
**Context:** Understanding the primary equipment vendor ecosystem for DalTile's tile manufacturing lines, specifically data connectivity and Industry 4.0 capabilities that affect MES integration scope.

---

## 1. Company Overview

**Full Name:** SACMI -- Societa Anonima Cooperativa Meccanici Imola

**Founded:** 1919, by nine unemployed metalworkers in Imola, Italy

**Legal Structure:** Worker cooperative (cooperative managed according to principles of cooperative democracy and member participation)

**Headquarters:** Imola, Italy

**2024 Revenue:** EUR 1.728 billion (down from EUR 2+ billion in 2023, with the decrease attributed to slowdown in the ceramic sector due to international tensions and sluggish global construction market)

**2024 EBITDA:** EUR 323 million

**2024 Net Profit:** Exceeded EUR 200 million

**2024 Net Equity:** EUR 1.055 billion (first time exceeding EUR 1 billion)

**Employees:** 4,700+

**Global Footprint:** 70+ production, distribution, and service companies across 25-28 countries

**Group Structure:** Subsidiaries controlled via holding company HPS SpA

**Patent Activity:** 276 new patent applications filed in 2024

SACMI is not a single-product company. It operates across multiple sectors: Ceramics, Rigid Packaging, Beverage, Food, Metals, Advanced Technologies, and Automation (vision and olfactory systems). The ceramics division is one of several major business units. This is relevant because it means SACMI has deep automation and controls expertise that extends beyond ceramics.

### SACMI USA

SACMI USA is headquartered in Des Moines, Iowa, with operations since 1994. In recent years, SACMI opened a new branch in Brentwood, Tennessee -- positioned to serve the southeastern U.S. ceramic manufacturing district (where DalTile has multiple plants in Tennessee, Texas, Oklahoma, Alabama, and Pennsylvania). SACMI USA maintains:

- A workshop for manufacturing and overhauling punches and dies
- 30+ employees dedicated to the North American market
- Warehouse stock valued at $7+ million
- Customer support and after-sales service operations

---

## 2. Product Lines for Ceramic Tile Manufacturing

SACMI provides complete turnkey plants for tile production, covering every stage from raw material preparation to palletization. The following is a breakdown of their major product categories.

### 2.1 Body Preparation

SACMI manufactures complete body preparation systems. Their "Smart Powder Plant Control Room" application allows centralized management of the body preparation department, receiving raw material and formulation data directly from ERP systems.

### 2.2 Pressing / Forming

SACMI is the world leader in ceramic press manufacturing. Two primary technology families:

**PH Series (Hydraulic Presses):**
- Traditional hydraulic pressing for standard tile sizes
- The "Imola Series" is the flagship line
- PH 8200: Newest generation, described as SACMI's first "digital native" press model. Uses Ethernet Powerlink field bus for machine automation (not OPC-UA natively -- see data connectivity section below). Ultra-high communication speeds for precise control of all machine parameters. Designed for 4.0 integration from the ground up.
- PH 5200 Veloce: High-speed model, up to 14 cycles/minute for 600x600mm tiles. Features power-boosting hydraulic circuits and improved filtration/cooling.
- PH 3950: Mid-range model, referenced in recent installations
- PH 3020: Also referenced in current deployments
- Operating pressures: 170-300 bar range depending on model and mode

**Continua+ (Continuous Compaction for Slabs and Large Tiles):**
- Continuous belt-based compaction (not hydraulic cycle-based)
- Designed specifically for large-format tiles and slabs
- PCR models (e.g., PCR 2180, PCR 2120) are the forming machines in the Continua+ family
- Productivity rates up to 12 linear meters per minute, translating to 30,000+ sqm per day
- The PCR 2120 is described as "the smartest member of the Continua+ family"
- First Continua lines deployed at Cooperativa Ceramica d'Imola in 2011

### 2.3 Drying

- Horizontal and vertical dryer configurations
- Model examples: E7P 200 (multi-deck), EM5 320
- Described as "efficient high-output thermal machines" for tiles and ceramic slabs

### 2.4 Glazing Lines and Accessories

- "Waterfall" curtain glazing systems
- "Airless" spray glazing systems
- Glazing machines for both regular-size tiles and large ceramic slabs

### 2.5 Digital Decoration

SACMI acquired/partnered with Intesa for digital printing capabilities (often branded SACMI-Intesa). Product lines:

**DHD (Digital Wet Decorating Machine):**
- Inkjet printers for inks, glazes, and other materials
- Uses "Flatjet" spray-on-demand technology
- Nozzle diameters of 500 microns (25x greater pigment flow than typical inkjet)
- Enables fully digitalized glazing lines

**DDG (Digital Decoration and Glazing):**
- Two-module system (upstream and downstream of digital inkjet decorator)
- Applies grits and glues for textures (wood, natural stone appearances)
- Deposits structuring inks for high-definition micro-textures
- Synchronized with SACMI's "Deep Digital" line concept
- Centrally controlled by HERE software platform

### 2.6 Firing (Kilns)

**MAESTRO Kiln Range:**
- Single and double-channel roller kilns
- Innovative heat and air control systems
- Heat recovery and energy-saving devices
- Digital set-up capabilities
- Model examples: FMA217, FMS355

**Sustainability Innovations:**
- SACMI developed the world's first 100% hydrogen-fueled kiln (operational in their Kiln Lab)
- Premiered a 100% electric kiln prototype at Tecna 2024
- Both represent steps toward climate-neutral ceramic manufacturing

### 2.7 Sorting, Inspection, Packaging, and Palletization

- Complete automatic sorting lines
- Integration with Flawmaster+ vision system (see Section 4)
- Stacking, packaging, and palletization systems

---

## 3. Industry 4.0 / Smart Factory Platform: H.E.R.E.

SACMI's primary digital offering is the **H.E.R.E. platform** ("Here Enhancing [digital manufacturing]"). This is the most critical element for understanding MES integration scope.

### 3.1 What H.E.R.E. Is

H.E.R.E. is a modular, scalable software platform that provides integrated digital control of ceramic manufacturing data and processes, from raw materials to shipment. It is positioned as an **MES-level system** -- SACMI explicitly describes it as implementing "advanced MES functions" and serving as "the infrastructural link between Information Technology and Operational Technology levels."

**Key implication for DalTile:** If SACMI equipment at DalTile plants already runs H.E.R.E., any custom MES would need to either integrate with it, replace it, or sit alongside it. If the equipment does NOT have H.E.R.E., the integration path is directly to the machine PLCs and controllers.

### 3.2 H.E.R.E. Modules

The platform consists of hierarchical modules operating at machine, controls/PLC, department, and factory supervision levels:

| Module | Function |
|--------|----------|
| **Plant Layout** | Real-time overview of entire plant status |
| **Machine Monitoring** | Real-time viewing and control of machine process data |
| **Status Chart** | Operational status of machines over time |
| **Trends** | Tracks machine process parameters over time (temperature, pressure setpoints, etc.) |
| **Alarms** | Collects and analyzes machine alarm signals with integrated reporting |
| **Production Reports** | Personalized web-based production reports |
| **Smart Powder Plant Control Room** | Centralized body preparation department management; receives formulations from ERP |
| **ID-Tiles** | Digital tracking of individual tiles/slabs through production stages (unique identity card per piece) |
| **Recipe Management** | Manages production recipes and product requirements |
| **Operational Scheduling** | Advanced scheduling and production optimization |
| **Intralogistics** | Material handling and logistics management with robotics and autonomous vehicles |

### 3.3 ERP Integration

In its most advanced configuration, H.E.R.E. interfaces with the client's ERP system and:
- Calculates product requirements
- Receives raw material and formulation data
- Optimizes production stages via recipe management
- Performs advanced operational scheduling

### 3.4 ID-Tiles Tracking System

Launched at Tecna 2024, ID-Tiles is a standout module. It:
- Prints unique codes on individual tiles/slabs
- Tracks each piece through every production stage
- Checkpoints along the production line collect data and add it to the slab's "digital identity card"
- Enables full traceability from forming to shipment

### 3.5 Modularity and Co-Design

SACMI emphasizes that H.E.R.E. is not an all-or-nothing deployment. It can be introduced incrementally, with modules activated over time. They use a "co-design" approach, configuring the platform to each customer's specific needs.

### 3.6 "Easy Factory" Vision (Tecna 2024)

At Tecna 2024, SACMI presented its "Easy Factory" concept built on three pillars:
1. **Productivity** -- high-performance machines with automation
2. **Control** -- digital controls throughout the entire production process
3. **Eco-friendly design** -- sustainable thermal processes for climate-neutral goals

The Easy Factory vision emphasizes "simple and intuitive" human-machine interaction through "seamless integration of mechatronics, vision systems and AI."

---

## 4. Quality Control and Vision Systems

SACMI operates a dedicated Control and Vision Systems division (through subsidiary Italvision).

### Flawmaster+

The flagship quality control product:
- Automatic sorting system for ceramic surface inspection
- Three high-resolution cameras with light sources at different angles
- Detects surface defects, mechanical defects, decoration defects, shade/color defects
- Uses AI and neural networks for self-learning and continuous improvement
- Can create reference models using AI as an alternative to digital printer graphics files
- Installs at multiple points: upstream of sorting line, downstream of grinding, or at kiln exit
- Supports automatic size changes and on-the-fly product changeovers
- Operates in M2M (machine-to-machine) configuration with other line equipment
- Optional Caliber Planarity Integrated (CPI) module for dimensional checks (diagonals, side shape, warpage, concavity, convexity)

**MES Relevance:** Flawmaster+ generates significant quality data (defect rates, types, trends by batch) that a custom MES would want to consume. Understanding its data output format and connectivity is a key integration point.

---

## 5. Data Connectivity and Communication Protocols

This section is critical for MES integration scoping. The available information is partly incomplete because SACMI does not publicly document all protocol specifications.

### 5.1 What Is Known

**Ethernet Powerlink:**
- SACMI's newer presses (PH 8200 and likely other recent models) use Ethernet Powerlink as the fieldbus protocol for machine-level automation.
- Ethernet Powerlink is a real-time Ethernet standard (managed by the EPSG -- Ethernet Powerlink Standardization Group). It provides deterministic, high-speed communication between drives, sensors, and controllers within the machine.
- This is the **intra-machine** communication protocol, not the protocol for external MES/SCADA integration.

**H.E.R.E. Platform as Middleware:**
- H.E.R.E. operates at a hierarchical level spanning machines, controls/PLC, department supervision, and factory supervision.
- It collects data from SACMI machines and makes it available for higher-level systems (ERP, MES).
- The platform supports "in-Cloud sharing of machine operating data."

**Machine-to-Machine (M2M):**
- The Flawmaster+ vision system and other equipment operate in M2M configuration, suggesting direct machine-to-machine communication channels exist.

### 5.2 What Is NOT Publicly Documented

The following details were not found through public web research and represent key discovery questions for SACMI:

- **OPC-UA support:** No explicit mention of OPC-UA server capabilities on SACMI machines was found. However, given that SACMI uses PLCs (likely Siemens or B&R given the Ethernet Powerlink connection to B&R Automation), OPC-UA may be available at the PLC level even if SACMI does not advertise it. Modern Siemens S7-1500 PLCs have built-in OPC-UA servers.
- **Modbus support:** Not documented publicly.
- **REST APIs or web services:** H.E.R.E. provides "web-based production reports," suggesting some web service layer exists, but no public API documentation was found.
- **Historian integration:** No specific historian product or integration was mentioned, though the Trends module in H.E.R.E. stores time-series process data.
- **Database access:** No information on whether H.E.R.E. uses an accessible database (SQL, time-series DB) or a proprietary data store.
- **Data export formats:** No documentation on CSV/JSON/XML export capabilities.

### 5.3 Likely Integration Architecture

Based on industry norms and the available evidence, the probable data connectivity stack for modern SACMI equipment is:

```
Layer 0: Sensors and Actuators
    |
Layer 1: Machine-level PLCs (Ethernet Powerlink fieldbus)
    |  Likely B&R or Siemens PLCs
    |
Layer 2: H.E.R.E. Platform (if installed)
    |  Proprietary middleware collecting from PLCs
    |  Web-based dashboards and reports
    |
Layer 3: ERP Integration
    |  Interfaces with SAP or similar
    |
External MES Integration Options:
    - Option A: Connect to PLCs directly via OPC-UA (if PLC supports it)
    - Option B: Connect to H.E.R.E. platform via its API (if one exists)
    - Option C: Bypass both and use edge gateways on the machine network
    - Option D: Use OPC-UA gateways to bridge from Powerlink/Modbus
```

### 5.4 Critical Questions for SACMI (or DalTile Engineering)

1. What PLC vendor/model does SACMI use on each machine type (presses, kilns, dryers)?
2. Is OPC-UA available natively on any SACMI machine controllers?
3. Is the H.E.R.E. platform installed at any DalTile plant?
4. If H.E.R.E. is installed, does it expose data via OPC-UA, REST API, or database access?
5. What data points does each machine type make available (cycle counts, temperatures, pressures, alarm codes, quality metrics)?
6. Are there existing SCADA or historian systems at DalTile plants that already collect data from SACMI equipment?
7. What is the generation/age of SACMI equipment at each DalTile plant? (Older equipment may have limited or no digital connectivity.)

---

## 6. Business Model: Equipment Manufacturer AND Connected to Tile Production

### 6.1 Clarification on Vertical Integration

The engagement context noted that SACMI "also manufactures tiles themselves and sells to competitors." Based on research, the actual relationship is more nuanced:

**SACMI itself does not produce tiles for commercial sale.** SACMI is purely an equipment and technology company. However, there is a closely related entity:

**Cooperativa Ceramica d'Imola** is a separate cooperative also based in Imola, Italy. It is one of SACMI's oldest and most prominent customers, having been the catalyst for SACMI entering the ceramics press market after World War II. The two cooperatives share deep historical ties and geographic proximity but are separate legal entities.

Cooperativa Ceramica d'Imola produces tiles under the "Imola" and "Leonardo" brands and has invested tens of millions of euros in SACMI equipment (e.g., a EUR 40 million investment approved for 2017-2019, including Continua+ lines).

### 6.2 What This Means for DalTile

- SACMI does not compete with DalTile as a tile producer. They are a pure equipment/technology vendor.
- SACMI's closest tile-producing partners (like Cooperativa Ceramica) use SACMI equipment, which means SACMI gets continuous real-world feedback that feeds back into product development.
- The engagement context may have been referring to other vendors in the tile equipment space (e.g., KEDA or SITI B&T) who may have different vertical integration models, or it may have been referring to the Cooperativa Ceramica relationship.

### 6.3 Cooperative Structure Implications

As a worker cooperative, SACMI operates differently from a typical publicly traded equipment company:
- Decision-making is driven by member-workers rather than shareholders
- The cooperative structure emphasizes long-term investment in R&D over short-term profit maximization
- This partially explains the EUR 71 million annual R&D investment and 276 patent applications in a single year
- Pricing may be less aggressive but technology investment tends to be higher than typical private competitors

---

## 7. Competitors in the Ceramics Equipment Space

Three categories of competitors are relevant to understanding the vendor landscape at DalTile.

### 7.1 Tier 1: Complete Plant Suppliers (Direct SACMI Competitors)

**SITI B&T Group (Italy)**
- Founded 1961, listed on the Italian stock market
- Provides complete plants for tile production, sanitaryware, and agglomerated quartz
- Operates through brands including Projecta Engineering (digital decoration), Ancora/Diatex/Mec Abrasives (surface finishing), B&T White (sanitaryware)
- Claims to be "the only complete manufacturing supplier" offering end-to-end plant ownership
- Has its own Smart Factory / Industry 4.0 offerings including predictive maintenance programs based on OEE analytics
- Has offered performance-based service packages where SITI B&T takes "total responsibility for a section of the customer's plant"
- Now owned by One Equity Partners (private equity)

**KEDA Industrial Group (China)**
- Founded 1992, listed on Shanghai Stock Exchange (600499)
- Major Chinese competitor with 70+ subsidiaries in 60 countries
- Product range: presses (including KD16008 large-tonnage), kilns (including world's first 3.85m ultra-wide kiln and double-layer kilns), polishing lines, distribution systems
- Developed China's first high-tonnage press (KD3200)
- Pricing typically significantly below Italian manufacturers
- Strong presence in developing markets (Southeast Asia, Africa, South America)

### 7.2 Tier 2: Specialist Competitors

| Company | Specialty | Country |
|---------|-----------|---------|
| **System Ceramics** (Coesia Group) | Complete process systems, digital printing, forming, sorting | Italy |
| **KERAjet** | Digital inkjet decoration | Spain |
| **BMR Italia** | Surface finishing, polishing, squaring | Italy |
| **EFI Cretaprint** | Digital inkjet printing | Spain/USA |
| **Breton** | Large slab technology | Italy |
| **CMF Technology** | Digital decoration | Italy |
| **Manfredini & Schianchi** | Raw material preparation | Italy |

### 7.3 Competitive Landscape Summary

The ceramics equipment market is overwhelmingly Italian-dominated at the technology leadership tier, with Chinese manufacturers (led by KEDA) competing aggressively on price and increasingly on technology. The global ceramic machinery market was valued at approximately USD 5.2 billion in 2022, with a projected CAGR of 5.3% through 2032.

**Note on "Three Major Vendors":** The engagement context referenced three major equipment vendors at DalTile. Based on market positioning, the most likely trio would be SACMI, SITI B&T (or its subsidiary brands), and either KEDA or System Ceramics. This should be confirmed with DalTile engineering during discovery.

---

## 8. Pricing Indicators

SACMI does not publish pricing. Equipment is quoted on a per-project basis. However, available reference points include:

- **Complete production lines:** Cooperativa Ceramica d'Imola invested EUR 40 million over 3 years (2017-2019) for multiple Continua+ lines, kilns, and dryers. This suggests a single major line installation costs in the range of EUR 10-20 million.
- **Used equipment:** A used SACMI complete wall and floor tile plant was listed on industrial equipment marketplace AaronEquipment.com, though pricing was not shown.
- **SACMI USA spare parts inventory:** Valued at $7+ million, suggesting ongoing maintenance/spare parts costs are substantial.
- **Industry benchmarks:** For a greenfield tile plant producing 10,000-15,000 sqm/day, total equipment investment typically ranges from EUR 15-40 million depending on automation level and tile format.
- **Chinese alternatives:** KEDA and other Chinese manufacturers typically price 30-50% below Italian equivalents, which creates pricing pressure on SACMI for cost-sensitive markets.

---

## 9. Key Findings and MES Integration Implications

### 9.1 What Favors Custom MES Integration

1. **SACMI is investing heavily in digital/4.0:** Their H.E.R.E. platform, ID-Tiles tracking, and Easy Factory vision all indicate that modern SACMI equipment is designed with data connectivity in mind.
2. **PLC-based architecture:** The use of industrial PLCs (with Ethernet Powerlink fieldbus) means standard industrial protocols can likely be used to extract data, even if SACMI does not explicitly document OPC-UA support.
3. **H.E.R.E. as MES middleware:** If already deployed, H.E.R.E. may provide a data aggregation layer that simplifies integration vs. connecting to each machine individually.
4. **Web-based reporting:** H.E.R.E.'s web-based report generation suggests some form of accessible data layer.

### 9.2 What Creates Risk or Complexity

1. **Proprietary data layer:** SACMI has not publicly documented APIs, database schemas, or standard integration protocols for H.E.R.E. This may mean integration requires SACMI cooperation or reverse engineering.
2. **Equipment age variation:** DalTile's plants likely have equipment spanning multiple generations. Older SACMI presses (pre-PH 8200) may have limited or no digital connectivity.
3. **Vendor lock-in potential:** SACMI's H.E.R.E. platform positions them to be the MES layer for their own equipment, which could create friction if DalTile wants a vendor-agnostic MES.
4. **Mixed vendor environment:** If DalTile uses equipment from SACMI plus two other vendors, each may have different protocols and data models, requiring a normalization layer.
5. **Ethernet Powerlink is not OPC-UA:** The intra-machine protocol (Powerlink) does not inherently support OPC-UA. An OPC-UA gateway or PLC with OPC-UA server capabilities would be needed.

### 9.3 Recommended Discovery Actions

1. **Inventory DalTile's SACMI equipment** by plant, including model numbers and approximate installation dates.
2. **Determine H.E.R.E. deployment status** at each DalTile plant.
3. **Request SACMI technical documentation** on data export capabilities (OPC-UA support, API specifications, database access).
4. **Identify PLC vendor and model** on each machine type (this determines OPC-UA availability).
5. **Map existing data flows** -- does DalTile already have SCADA or historian systems collecting from SACMI equipment?
6. **Engage SACMI USA (Brentwood, TN office)** as a technical resource for integration questions.

---

## Sources

- [SACMI Tiles Overview](https://sacmi.com/en-US/ceramics/tiles)
- [SACMI Corporate Homepage](https://sacmi.com/)
- [SACMI Wikipedia](https://en.wikipedia.org/wiki/SACMI)
- [H.E.R.E. Software Platform](https://sacmi.com/en-US/ceramics/tiles/here-software)
- [Sacmi HERE: A Modular, Scalable Approach to Digitalization (Ceramic World Web)](https://www.ceramicworldweb.com/en/technology/sacmi-here-modular-scalable-approach-digitalization)
- [H.E.R.E., The New Frontier in Line Supervisors (Ceramic World Web)](https://ceramicworldweb.com/en/technology/here-new-frontier-line-supervisors-sacmi)
- [The Easy Factory at Tecna 2024 (Ceramic World Web)](https://ceramicworldweb.com/en/news/easy-factory-sacmi-presents-tecna-its-project-new-ceramic-industry)
- [The Easy Factory at Tecna 2024 (SACMI)](https://sacmi.com/en-US/tecna-2024)
- [SACMI 2024 Revenue Report](https://sacmi.com/en-US/corporate/news/21538/sacmi-group-2024-revenues-surpass-%E2%82%AC1-7-billion)
- [SACMI Financial Performance](https://www.sacmi.it/en-us/Corporate/About-Us/Financial-info)
- [PH 8200 Imola Series Smart Press](https://sacmi.com/en-US/ceramics/news/5304/new-sacmi-ph8200-imola-series-the-smart-pressing-era-begins)
- [First PH8200 Supplied to Romani Group (Ceramic World Web)](https://www.ceramicworldweb.com/en/news/first-sacmi-ph8200-press-supplied-romani-group)
- [Continua+ Technology](https://sacmi.com/en-US/ceramics/tiles/continua)
- [SACMI Pressing Overview](https://sacmi.com/en-US/ceramics/tiles/ceramic-pressing)
- [PH Veloce 5200 (Ceramic Tiles Blog)](https://ceramictilesblog.com/sacmi-veloce-ph-5200-press-high-speed-press/)
- [PH Range](https://sacmi.com/en-US/ceramics/tiles/pressing/hydraulic_presses/ph-range)
- [SACMI Drying](https://sacmi.com/en-US/ceramics/tiles/drying)
- [SACMI Firing / Kilns](https://sacmi.com/en-US/ceramics/tiles/firing)
- [MAESTRO Kiln Range](https://sacmi.com/en-US/Ceramics/Tiles/firing/Single-channel-roller-kiln/MAESTRO)
- [First 100% Hydrogen Kiln (SACMI)](https://sacmi.com/en-US/ceramics/news/19660/The-first-tile-fired-in-a-100-hydrogen-kiln-It-s-from-SACMI)
- [SACMI Glazing Lines](https://sacmi.com/en-US/ceramics/tiles/glazing-lines-and-accessories)
- [DDG Digital Decoration and Glazing](https://sacmi.com/en-US/ceramics/tiles/decoration/ddg-digital-decorating-machine)
- [SACMI DDG New Frontier (Ceramic World Web)](https://ceramicworldweb.com/en/technology/sacmi-ddg-new-frontier-ceramic-decoration)
- [SACMI Digital Decoration Overview](https://sacmi.com/en-US/ceramics/tiles/decoration)
- [Vision Systems for Slabs and Tiles](https://sacmi.com/en-US/control-vision-systems/vision-for-slabs-and-tiles)
- [Flawmaster+ AI Quality Control (Ceramic World Web)](https://ceramicworldweb.com/en/technology/increasingly-advanced-quality-control-ai)
- [ID-Tiles Tracking (Ceramic World Web)](https://ceramicworldweb.com/en/technology/id-tiles-authentic-italian-made-slabs)
- [Sacmi Intralogistics Investment (Ceramic World Web)](https://ceramicworldweb.com/en/news/sacmi-steps-investment-intralogistics)
- [SACMI USA](https://sacmiusa.com/)
- [SACMI USA Tennessee Branch](https://sacmi.com/en-US/corporate/news/5541/sacmi-usa-opens-a-new-branch-in-tennessee)
- [SACMI USA Brentwood Branch (Ceramic World Web)](https://www.ceramicworldweb.com/en/news/sacmi-usa-opens-new-branch-brentwood-tennessee)
- [Cooperativa Ceramica d'Imola Investment (SACMI)](https://www.sacmi.it/en-US/ceramics/news/20015/Cooperativa-Ceramica-d%E2%80%99Imola-investment-with-SACMI-gathers-momentum)
- [Cooperativa Ceramica Chooses PCR2120 (Ceramic World Web)](https://www.ceramicworldweb.com/en/news/cooperativa-ceramica-dimola-chooses-new-pcr2120-smartest-member-continua-family)
- [The Cooperative District of Imola (Academic PDF)](https://base.socioeco.org/docs/imola_0.pdf)
- [SITI B&T Group Brands](https://sitibt.com/our-brands)
- [SITI B&T Smart Factory (Ceramic World Web)](https://www.ceramicworldweb.com/en/news/smart-factory-siti-bt-group-ceramics-china)
- [SITI B&T Service 4.0 (Ceramic World Web)](https://www.ceramicworldweb.it/cww-en/spotlight/the-service-40-plan-by-siti-bt)
- [System Ceramics](https://www.systemceramics.com/en)
- [KEDA Industrial Group](https://kedagroup.com/about/)
- [Ceramic Machinery Market Report (Acumen Research)](https://www.acumenresearchandconsulting.com/ceramic-machinery-market)
- [Tennessee Ceramics Industry (Area Development)](https://www.areadevelopment.com/contributedcontent/q4-2023/tennessee-ceramic-industry-attracts-international-investment.shtml)
- [Cerbras New SACMI Line (Ceramic World Web)](https://ceramicworldweb.com/en/news/cerbras-installs-new-sacmi-line-equipped-record-breaking-kiln)
- [Motto Continua+ Line in India (Ceramic World Web)](https://ftp.ceramicworldweb.com/en/news/india-motto-has-started-new-sacmi-continua-line)
- [SACMI Company Organization](https://sacmi.com/en-US/corporate/about-us/organization)
