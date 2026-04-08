# 01 - Meeting: Projects and Priorities

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Focused deep dive on distinct projects, immediate vs. aspirational, and actual client asks

---

## Summary of the Two-Project Framing

Near the end of the call (56:31), Mahesh explicitly proposed structuring the engagement as **two projects**:

1. **Project 1 -- Progress Modernization / Label Printer Solution:** Kill Progress (OpenEdge), replace SATO code-based label programming with a proper label designer, move from serial ports to Ethernet/TCP-IP.
2. **Project 2 -- MES / Work Order Visibility:** Real-time work order tracking through manufacturing stages, yield at each step, waste tracking, and a visual dashboard (Cumulus-like) showing end-to-end status.

Mahesh's ideal scenario is that the label printer designer becomes **part of the MES solution** so that when a work order reaches the sorting/packaging line, the system already knows which label template to apply. He stated: "If the label designer was part of this solution as well... that would be the best scenario for me."

---

## Project-by-Project Decomposition

### 1. MES / Work Order Visibility (Primary Ask)

**Who raised it:** Mahesh -- this is the central reason for the engagement.

**Priority:** Immediate. This is what Mahesh wants to show leadership. He said (49:30): "What I want to do is do a project where I can show on a high level at least one line where I can show end to end of this is what is happening on a work order by work order basis. Yield at each step and the real-time visibility of everything happening."

**What Mahesh described in detail:**
- Today they measure production only in aggregate: total tiles pressed, total square meters of kiln output, total finished output. No work-order-level tracking exists. "They don't measure work orders. They basically see how much tiles did we press, how much kiln did we use and how much output did we produce in thousands of square meters. They don't even look at it from an item perspective."
- He wants a planner to define a work order (e.g., WO#123, Item#4567) with specific equipment assignments: Press 2, Glaze 2, Printer 2, Kiln 7, Quality 3, Sorting Line 3, Packaging Line 2.
- At each stage, an operator scans to start and complete that portion of the work order. This creates the "shop traveler" pattern (Colin's term).
- The system should show: how many pressed, how many through the dryer, how many through the glaze line, how many through the printer, how many into the kiln, how many out, and waste at each stage.
- He wants to show the start time and end time for each stage, per work order.
- He explicitly wants to track waste that is currently invisible: "They track this [sorting line rejection] as their wastage" but ignore waste at press, dryer, glaze, and printer stages. Finance calculates approximately 9% waste but Mahesh argues it is higher because only post-kiln waste is measured.

**The lineage/traceability problem Mahesh described:**
- Work-in-process (WIP) buffers at four points break the continuous flow: (1) before the kiln, (2) after the kiln, (3) at palletization, (4) finished goods.
- At the kiln stage, correlation between product and machine is lost entirely. One press can feed two glaze lines; three glaze lines can feed one kiln. After the kiln, there is no way to know which product was which.
- The existing PI Historian dashboard at one site shows this problem clearly: input to a glaze line might read 22,500 tiles but output reads 22,800 -- an impossibility that causes executives to distrust all the data.
- Mahesh stated: "Once you are at the kiln, which line went into which kiln? There is no correlationship. You kind of lose the track of part number once you get to the kiln."
- Current workaround: they reset all machine counters daily at 6:00 AM and track from there. Mahesh wants per-work-order resets, but the plant team resists because of the many-to-many routing between equipment.

**What Mahesh explicitly asked BayOne to do:**
- Build a work-order-tracking MES system that provides per-stage yield visibility.
- Deploy on Azure (Mahesh confirmed they have Azure), but with local/on-floor components to ensure manufacturing does not stop if internet goes down.
- Provide a rough estimate so he can assess viability before a site visit.

**What Colin suggested:**
- Azure deployment with Postgres, Python, Azure Container Apps -- all cost-optimized.
- A phased proposal: "Here's what we could do now, here's what comes later" -- starting with something that trends toward a full MES without requiring the full scope immediately.
- A Cumulus-like dashboard ("Cumulus 3.0") as the visual front end.
- Separation of concerns as a design principle: "Azure being up or down, existing or not existing shouldn't impact anything on the factory and vice versa."

**Dependencies / sequencing:**
- This is the foundation project. Everything else (sensors, AI/ML, upstream quality) builds on this.
- Start with one line at Sunnyvale Plant 2, then expand.

---

### 2. Label Printer Modernization / Kill Progress

**Who raised it:** Mahesh -- this is a concrete, scoped problem he wants solved.

**Priority:** Immediate. Mahesh framed this as one of the two projects he wants to start. He said (56:31): "I would love to have a project that says I'm killing Progress and I am just giving a label print solution to them of some nature."

**What Mahesh described in detail:**
- The current system runs on Progress (OpenEdge) with custom code written by a three-person team (two have left, one is retiring).
- Labels are programmed using SATO printer language -- literally coding label layouts via SATO commands rather than using a visual label designer. "They are literally programming this printer using SATO language rather than a designer label."
- The blue-screen application on the sorting/packaging line communicates with the label printer via serial port to a custom network the team built themselves.
- The network team does not want to manage the custom network. Mahesh's remaining team has no knowledge of it.
- Labels serve multiple purposes: box labels (with item barcodes, manufacturing dates) and pallet labels.
- They also print labels for private-label customers (e.g., Home Depot branded products), so the label system must support multiple label templates per item/customer.
- The PLC interaction: a box arrives on the conveyor, a PLC raises a stop, the label is printed and physically pushed onto the box by a mechanical arm, a scanner verifies it, and the conveyor resumes. The entire window is approximately three seconds.

**What Mahesh explicitly asked BayOne to do:**
- Rewrite the Progress code in a modern language. He mentioned ".NET or C# or Python and maybe Oracle database or something like that" as possibilities. He had already discussed this with Yogesh (BayOne).
- Create a proper label designer (visual, not code-based) so plant operators can design labels without programming.
- Move from serial ports to Ethernet/TCP-IP connectivity for the printers.
- Mahesh wants to hand off PLC/network responsibility to the network team: "You work with the network guys to get the printer. You work with the network guys to get the drop. I am not doing anything in this other than just giving you a label printer designer."

**What Mahesh flagged as a complication:**
- "The only problem that I see is that there is a lot of PLC type of work as well." The label application process is PLC-driven (stop, print, push, scan, release) and that timing is tight (three-second window).
- Any cloud-based solution cannot introduce latency into this process. There must be local components on the factory floor for the label printing workflow.

**What Colin observed:**
- He saw the serial port on the side of the blue-screen computer and was reassured: "That is something that we can definitely talk to. Even if you were to take that computer away." This means the printer interface is accessible and replaceable.
- Colin recommended Python as the development language and Postgres on Azure for the database.

**Ideal integration with MES:**
- Mahesh wants the label designer to be part of the MES so that when a work order reaches the sorting line, the system automatically knows which label template to use based on item number and customer (own-brand vs. private-label).

---

### 3. Sensor/Camera Infrastructure for Quality

**Who raised it:** Mahesh raised the idea of cameras; Colin expanded significantly on sensors.

**Priority:** Medium-term. Mahesh discussed cameras as something he wants but acknowledged it needs investigation. He asked Colin directly: "Where do we put the cameras? We put it on the conveyor belt or do we put it somewhere above?"

**What was discussed:**
- Mahesh wants cameras and/or sensors at multiple points in the line to detect waste events (tiles being discarded when the conveyor belt shifts a tile out of alignment, for example).
- He noted that the environment is dusty and sensors/cameras need to withstand that. Existing light-curtain sensors have reliability problems: dust accumulation, accidental blockage by a book or paper causing false counts.
- He specifically mentioned that glaze lines and printers have some existing light-curtain sensors, but they are unreliable.
- He asked about the number of cameras: "Do you think like 15-20 cameras per line should be more than enough?"

**What Colin suggested:**
- Industrial-grade cameras with windshield-wiper attachments or purge gas systems for dust mitigation.
- Camera count: "You could probably even get away with less" than 15-20. He wants to assess in person.
- The factory has 80/20 aluminum extrusion (T-slot) framing throughout, making camera mounting easy.
- Humidity sensors at the kiln output -- "The missing data point you're missing from the kiln is the moisture content, so you could always have very simple humidity sensors that are outside of the output of the kiln."
- IP-rated sensors matched to the equipment's own environmental spec.
- XBee or similar radio protocols for data communication across the large factory floor without requiring network drops.

**What Colin planned to do:**
- Assess camera placement and count during an on-site visit. He wants to determine minimum, ideal, and overkill configurations.
- Scope the hardware cost with an asterisk: "Before I say here's the hardware cost, we'll see the extent of it."

**Categorization:** This is something Mahesh wants BayOne to advise on and potentially implement, but the specifics depend on the site visit. It supports both the MES project (counting/tracking) and the future quality prediction project.

---

### 4. PI Historian / Data Ingestion

**Who raised it:** Mahesh brought up the existing PI Historian installations; Colin suggested the architecture.

**Priority:** Medium-term, but foundational for sensor data. Some sites already have PI Historian capturing press counts, glaze applications, and print counts. The data exists but is unreliable (light-curtain sensor issues).

**What Mahesh described:**
- "A couple of sites where they actually do have Historian database and couple of sites can tell you exactly how much press they have done or whatnot."
- He wants to ingest machine readings (he showed press machine readings on screen) every five minutes: "Ideally what I would love to do is ingest that every 5 minutes so that you can say this is all good, this is all good or bad."
- He raised the volume concern: "For one plant, we make like 400,000 square feet every single day. So there's so many presses... it doesn't make a lot of sense to store all of that data, at least for a high level MES."

**What Colin suggested:**
- RabbitMQ for high-throughput message ingestion: "If it's high throughput, it's almost always going to be something like RabbitMQ as the way to do essentially task queuing."
- Historian for time-series sensor data, separate from the MES work-order tracking.

**Categorization:** Mahesh wants this but frames it as secondary to the MES visibility project. It would be part of a later phase or a parallel workstream. Colin positioned it as something that feeds into the engineering dashboards.

---

### 5. Cumulus-like Dashboard / Engineering Dashboards

**Who raised it:** Mahesh mentioned Cumulus as his visual reference; Colin expanded on off-the-shelf options.

**Priority:** This is how Mahesh wants to visualize the MES data. It is part of the MES project, not a separate project.

**What Mahesh described:**
- He wants a visual representation showing the manufacturing process flow with real-time quantities per stage: "If I can show them a Cumulus-like screen which shows them look, this is your process and you are trying to make 10,000, out of which 5,000 has already been pressed, 4,000 has already been dried."
- He showed Colin an existing dashboard from another site built on PI Historian data. It shows press-to-glaze-to-kiln flow with square footage counts, WIP tracking, and sorting line rejection rates. But it lacks work-order-level granularity and has data integrity issues (input/output mismatches).

**What Colin suggested:**
- Off-the-shelf engineering dashboard platforms at approximately $20K for a whole factory: "Configurable engineering dashboards... literally a drag and drop type interface. It almost looks like C# that you're building these in, very low code, no code, but also actually a real thing."
- He offered to send Mahesh information on these platforms.
- Alternatively, building a custom dashboard as part of the MES ("Cumulus 3.0") deployed on Azure.

**Categorization:** The dashboard is the front end of the MES. Mahesh wants a custom solution eventually ("The end goal is having an MES of our own, which we developed like Cumulus") but an off-the-shelf dashboard for sensor/engineering data could be a quick win alongside the custom MES.

---

### 6. Upstream Quality Prediction (AI/ML)

**Who raised it:** Mahesh raised the desire; Colin validated the feasibility and provided technical direction.

**Priority:** Aspirational / later-stage. Mahesh explicitly called this a future goal: "My thought is to really apply more logic at this stage at some point, but first stage is obviously to show them a little bit of visibility."

**What Mahesh described:**
- Ceramic engineers tell him "you can't do testing till it is baked," meaning quality testing only happens at the Qualitron sorting machine after the kiln.
- Mahesh disagrees and wants to prove upstream quality prediction is possible. "They only reject for shade and caliber. So if we can figure shade and caliber somewhere upstream in the process, we are golden."
- He identified that shade is driven by glaze line + printer + kiln. Caliber (dimensional accuracy, flatness, curvature) is driven by moisture, kiln temperature, and press parameters.
- He noted a challenge: after printing, a protective white glaze coat is applied before the kiln, making visual inspection of the printed tile appear useless. But he theorized that comparing pre-kiln printed images (before the protective coat) to known good tiles at that stage could work.
- He noted that at some plants, the printer-to-protective-glaze gap is only about five seconds, limiting the window for visual capture.

**What Colin stated:**
- Upstream quality prediction is absolutely feasible: "You can definitely do it. You just need the data to correlate back." He cited parallel experience with diamond polishing (opaque before polish, transparent after -- same correlation problem, solved with data).
- Humidity sensors at kiln output would correlate to caliber: "If your kiln is consistently at a particular temperature, then if your moisture is not changing much then it should perform exactly the same."
- Raw material moisture specs plus kiln output humidity would predict caliber with "pretty good accuracy, assuming that everything else is constant."
- The correlation approach: "There's never -- that's a very common process engineer thing. Like you can't know if it's gonna be good or bad until the end. It is not true."

**Categorization:** This is explicitly a future aspiration. It depends on (a) having the MES and data infrastructure in place, (b) having cameras and sensors deployed, and (c) having enough historical data to build models. Mahesh and Colin aligned that this comes after the foundation is built.

---

### 7. Team Building / Staffing

**Who raised it:** Mahesh asked Colin for guidance on building his internal team.

**Priority:** Immediate/parallel. Mahesh needs a team to own this work long-term. He currently has almost no team: "The three people who are managing this have left or two have left and one is retiring. I have one very junior person who is doing labeling."

**What Mahesh asked:**
- "How would you say that the team needs to be constructed on my end if we were going a custom route?"

**What Colin recommended (three roles, phased):**

1. **Architect / Manufacturing Engineer (Hire now):** "Someone who understands it from the whole process perspective, but is technical enough that they understand what the system is. Maybe they're not a full-time developer themselves, but someone who can at least diagnose." Ideally someone who has been a developer in the past.

2. **Hardware/IoT/Sensor Person (Hire now):** "Someone who's done a lot of things with sensors, IoT, automation." Explicitly not a PLC engineer -- "I would stay away from them because they're going to be very rigid." This person needs to speak the same language as the architect and pair well with them.

3. **Quality/Process Engineer (Hire later):** "The natural next step is improving things after you now have all this data." Not needed for the early phase, but critical once the data infrastructure is in place.

**What Colin offered to do:**
- Write job descriptions for these roles: "If you want, I can even write you a JD for them too. I'd be happy to do that." Mahesh accepted.

**Categorization:** This is something Mahesh wants to do himself (internal hiring) with advisory support from Colin. Writing JDs is a concrete BayOne deliverable that Colin volunteered.

---

### 8. Multi-Plant Rollout

**Who raised it:** Mahesh, as context for the budget and scope.

**Priority:** Future. Start with one line at one plant, prove it, then expand.

**What Mahesh described:**
- The $250K budget "is not just for one plant." It covers the software side of a multi-plant program.
- Sunnyvale Plant 2 is the target starting plant because Mahesh's office is 20 minutes away.
- Plant 2 has approximately: 6 presses, 6 glaze lines, 6 printers, 4 kilns, 5 Qualitron machines, 5 sorting lines, and 1 palletizer/wrapper.
- Plant 1 is adjacent but smaller with less equipment.
- The plan is: prove the concept at Plant 2, then roll out to other plants.

**What Colin suggested:**
- The proposal will include an asterisk for hardware: he needs to see the site to scope the number of lines, cameras, sensors, etc.
- Start with one line within Plant 2, not the whole plant.

**Categorization:** Multi-plant is the long-term vision. BayOne should scope for one line at Plant 2 as the immediate engagement, with a roadmap for expansion.

---

### 9. Uptime / Utilization Tracking

**Who raised it:** Mahesh, as an add-on to the MES.

**Priority:** Desired as part of the MES but not the primary driver.

**What Mahesh said (1:01:36):** "Ideally as we do this program, I would definitely want to know uptime because if we are doing this, we should be able to say this much is the uptime for Press 2, this much is the uptime for Glaze 2 or whatever it may be. Because utilization is a big thing for them."

**What Colin observed:**
- The existing PI Historian dashboard already shows an "uptime" column per machine at the glaze-line level. Colin asked whether the variation in uptime was demand-driven (only running machines when there is product to feed) or indicative of problems. Mahesh confirmed it is demand-driven: "I didn't have enough production coming from the press, so I couldn't keep these two lines up."

**Categorization:** This is a feature within the MES, not a separate project. If the MES tracks work order start/end times per machine, uptime and utilization can be derived. It is a dashboard/reporting concern.

---

### 10. Network Modernization on Factory Floor

**Who raised it:** Mahesh described the problem; Colin offered solutions.

**Priority:** Prerequisite for other projects but owned by the network team, not Mahesh's team.

**What Mahesh described:**
- The previous team built custom serial-port networks on the factory floor. "The serial ports they created themselves and frankly the network team doesn't want to manage it. My team has no knowledge of it."
- He wants to move to standard Ethernet/TCP-IP so the network team can own it: "I want to really move back to Ethernet ports and TCP-IP."
- The manufacturing floor has poor network infrastructure: the plant footprint is enormous relative to the office, network drops are expensive, wireless is unreliable in the dusty environment.

**What Colin suggested:**
- XBee-style radio communication protocols for distributed sensor data collection across the large factory floor, avoiding the need for wired network drops.
- The flat, open-ceiling warehouse layout is favorable for wireless/radio protocols.
- The main concern would be interference from large AC motors, which he assessed as unlikely given the equipment observed.

**Categorization:** Mahesh does not want BayOne to own network modernization. He wants to hand network responsibility to the internal network team. However, whatever BayOne builds (MES, label solution) must be designed to work with standard Ethernet/TCP-IP and not perpetuate the legacy serial-port approach. Network modernization is a constraint/requirement, not a deliverable.

---

## What Mahesh Explicitly Asked BayOne to Do

1. **Provide a rough estimate** for the engagement so he can assess viability. He said (58:14): "Will be nice to at least have a rough estimate... if you can give me a rough, rough estimate, that would be really helpful for me to at least start thinking about whether this is even viable or not."

2. **Build the MES / work order visibility system** -- one line at Sunnyvale Plant 2, with a visual dashboard, work-order-level tracking, per-stage yield, and waste tracking.

3. **Rewrite the Progress/label printer system** -- replace Progress code with modern language, create a visual label designer, move to Ethernet/TCP-IP. He had already discussed this with Yogesh as a potential fixed-bid project.

4. **Visit the factory** to assess camera/sensor placement and scope hardware needs. Mahesh offered to host.

5. **Write job descriptions** for his internal hires (architect, hardware/IoT person). Colin volunteered this and Mahesh accepted.

6. **Send information on off-the-shelf dashboard platforms** (~$20K) that could provide engineering dashboards for sensor data. Colin offered this.

## What Mahesh Wants to Do Internally

- Hire an architect, hardware/IoT person, and eventually a quality/process engineer.
- Hand off network/PLC responsibility to the internal network team.
- Move the factory floor from serial to Ethernet/TCP-IP (internal network team responsibility).
- Negotiate internally around the daily counter-reset process and the resistance to per-work-order resets.

## What Colin Suggested as Possibilities (Not Explicitly Requested)

- RabbitMQ for high-throughput sensor data ingestion.
- Humidity sensors at kiln output for caliber correlation.
- XBee/radio protocols for factory floor communication.
- Industrial-grade cameras with dust mitigation (purge gas, windshield wipers).
- Off-the-shelf engineering dashboard platforms (~$20K).
- Azure Container Apps for deployment, Postgres on Azure for the database.
- A phased proposal approach: immediate scope with a roadmap to full MES.
- Upstream quality prediction using sensor correlation data (validated Mahesh's aspiration as feasible).

## What Was Discussed as Future Aspirations

- Full MES with all measurements, tracking, and label design integrated -- Mahesh said (1:17:44): "That's the end goal. The end goal is having an MES of our own, which we developed like Cumulus, which has all these measurements that we can do, all kind of tracking that we can do, all kind of label designing that we can do."
- AI/ML-based upstream quality prediction for shade and caliber before the kiln.
- Multi-plant rollout beyond Sunnyvale.
- Capturing and ingesting all machine sensor data (press readings, etc.) every five minutes via PI Historian.
- Per-work-order machine counter resets (currently blocked by internal resistance).

---

## Sequencing and Dependencies

```
Phase 0 (Parallel / Immediate)
  - Factory site visit by Colin
  - Rough estimate / proposal
  - Write JDs for Mahesh's team
  - Send off-the-shelf dashboard platform info

Phase 1 (First Engagement)
  - Project A: Label Printer Modernization
    - Rewrite Progress code (Python, Postgres)
    - Visual label designer
    - Ethernet/TCP-IP connectivity
    - PLC interaction (3-second window constraint)
    - Local/on-floor deployment for latency-critical operations
  - Project B: MES / Work Order Visibility (One Line, Plant 2)
    - Work order definition and planning interface
    - Scan-based stage tracking (shop traveler)
    - Per-stage yield and waste calculation
    - Cumulus-like visual dashboard
    - Azure deployment with local edge components
    - Ideally: label designer integrated into MES

Phase 2 (After Foundation)
  - Sensor/camera deployment on the line
  - PI Historian data ingestion (machine readings every 5 min)
  - Engineering dashboards (off-the-shelf or custom)
  - Uptime/utilization tracking derived from MES data
  - Expand to additional lines at Plant 2

Phase 3 (Aspirational)
  - Upstream quality prediction (AI/ML)
    - Camera-based shade prediction pre-kiln
    - Humidity + raw material correlation for caliber prediction
  - Quality/process engineer hire to act on insights
  - Multi-plant rollout
  - Full MES with complete sensor integration
```

---

## Budget and Constraints

- **Budget:** Approximately $250K, covering software across multiple plants (not just one). Hardware (PLCs, sensors, cameras) is a separate budget owned by another team, but Mahesh wants to drive that conversation.
- **Timeline:** "If we could do yesterday, that would have been better, but today will work." No fixed deadline stated, but urgency is high.
- **Technology:** Azure (confirmed), Python (Colin's recommendation, accepted), Postgres on Azure (Colin's recommendation).
- **Critical constraint:** Factory floor operations must never depend on cloud availability. Local/edge components are required for anything in the manufacturing path (especially the label printer's 3-second PLC cycle).
- **Starting scope:** One line at Sunnyvale Plant 2. Mahesh's office is 20 minutes away.
- **Staffing gap:** Mahesh's current team is essentially one junior person. The three-person legacy team is gone. BayOne fills the development gap; Mahesh needs to hire for long-term ownership.

---

## Key Quotes

**Mahesh on the primary ask (49:30):**
> "What I want to do is do a project where I can show on a high level at least one line where I can show end to end of this is what is happening on a work order by work order basis. Yield at each step and the real-time visibility of everything happening."

**Mahesh on killing Progress (56:31):**
> "I would love to have a project that says I'm killing Progress and I am just giving a label print solution to them of some nature. Ideally I would like it to be part of this MES."

**Mahesh on the end goal (1:17:44):**
> "That's the end goal. The end goal is having an MES of our own, which we developed like Cumulus, which has all these measurements that we can do, all kind of tracking that we can do, all kind of label designing that we can do."

**Mahesh on wanting a rough estimate (58:14):**
> "Will be nice to at least have a rough estimate... if you can give me a rough, rough estimate, that would be really helpful for me to at least start thinking about whether this is even viable or not."

**Mahesh on the budget (59:12):**
> "I'm going to say $250,000, but that's not just for one plant... my budget is more software budget."

**Colin on upstream quality prediction feasibility (36:07):**
> "You can definitely do it. You just need the data to correlate back."

**Colin on the phased approach (1:22:50):**
> "If you want this now and you want this later, that's fine. If you want to just get set up for an MES without saying that that's the full scope, but at least something that will trend towards that and get you there eventually."

**Colin on separation of concerns (1:25:10):**
> "Total separation of concerns. Azure being up or down, existing or not existing shouldn't impact anything on the factory and vice versa."
