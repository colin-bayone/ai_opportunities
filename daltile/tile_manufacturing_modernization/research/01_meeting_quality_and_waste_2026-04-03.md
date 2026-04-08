# 01 - Meeting: Quality and Waste Challenges

**Source:** /daltile/tile_manufacturing_modernization/source/mahesh_and_colin_4-3-2026.txt
**Source Date:** 2026-04-03 (Discovery Call / Factory Walkthrough)
**Document Set:** 01 (Discovery Meeting)
**Pass:** Focused deep dive on quality and waste

---

## 1. Current Quality Testing Architecture

### 1.1 Qualitron: The Single Quality Gate

The only real quality testing in the entire manufacturing process happens at the Qualitron machine, which sits after the kiln and before the sorting line. Mahesh stated this explicitly: "the true testing is happening only at this stage. Qualitron is the only [place they] trust." The Qualitron evaluates each tile and classifies it as good, bad, or marginal. Tiles that fail are ejected from the line. Tiles that pass proceed to the sorting line.

This means that every upstream process step -- pressing, drying, glazing, printing, and kiln firing -- has zero inline quality testing. A defect introduced at the press, a misapplied glaze, or an inconsistent print run will not be detected until the tile has already been fired in the kiln, at which point the waste implications are fundamentally different (see Section 3 below on the green waste versus fired waste distinction).

### 1.2 Sorting Line: Shade and Caliber Classification

At the sorting line (immediately downstream of the Qualitron), tiles are classified along two primary dimensions:

- **Shade:** The color/visual appearance of the finished tile. Shade is a function of the glaze line application, the printer output, and the kiln firing process. Mahesh identified all three as contributors: "the shade is all with the glaze line and the printer... glaze line, printer, and the oven is creating the shade." The sorting line typically allows three shade grades (shade 1, shade 2, shade 3).

- **Caliber:** The dimensional accuracy of the finished tile. Mahesh described caliber as encompassing "height, weight, dimension and the thickness and whether it's flat or whether it's curvy." Caliber deviations -- particularly warping and bending -- occur during kiln firing: "one of the things that they don't want is that... this happens when you heat, it may bend in some ways." The sorting line typically allows three caliber grades (caliber 1, caliber 2, caliber 3).

From these two dimensions, the sorting line creates up to three SKUs per production run, stacking tiles into groups by shade/caliber combination. Tiles that fall outside acceptable shade or caliber ranges are rejected.

Mahesh was direct: "to tell you frankly, they only reject for shade and caliber. So if we can figure shade and caliber somewhere upstream in the process, we are golden."

### 1.3 Hourly Manual Sampling: The Only Upstream Check

Because of the large WIP buffer between the printer and the kiln (tiles are stacked into drawers/shelves and wait for an AGV to transport them to the kiln), there is a significant time lag between production and quality feedback. To mitigate this, some sites use a manual hourly sampling process:

1. Every hour, a worker walks to the printer output
2. They pull one or two tiles from the printer line
3. They mark the tiles with a physical marker
4. They place the marked tiles into the kiln at the first position (to get them through firing as fast as possible)
5. They wait for the marked tiles to exit the kiln
6. They visually inspect the output tiles to determine if quality is acceptable
7. Based on this single sample, they decide whether the batch is good or whether they need to stop the line

Mahesh described this process as their only form of proactive quality monitoring: "instead of saying everything coming to the printer is going to a waiting area, they will take one of the tiles or two of the tiles, they will mark it, they will put it into the kiln, wait for it to come out of the kiln and say yes for this hour also the batch looks good or no, it is not good and we need to stop the line and do something."

The fundamental problem: by the time a quality issue is detected through this hourly manual sampling, "they have thousands of square feet that's already in the conveyor belt" and in WIP staging. There is no ability to take quick corrective action because of the massive pipeline of in-process inventory between the point of defect introduction and the point of detection.

---

## 2. Sensor Infrastructure and Reliability Problems

### 2.1 Light Curtain Sensors

Some sites have light curtain sensors installed at the glaze line and printer. These sensors count tiles passing through each stage. Mahesh specifically noted: "in the glaze line they have a light curtain basically that creates a sensor. I think they have a similar one in the printer."

However, these sensors are fundamentally unreliable in the factory environment:

- **Dust contamination:** The factory floor is not a clean environment. Dust accumulates on the sensors and degrades their accuracy. Mahesh stated: "these sensors have to be kept clean because otherwise what happens is they collect a lot of dust."

- **Physical obstruction:** Workers or objects can inadvertently block the light curtains. Mahesh gave a specific example: "if somebody comes in and puts a book, now all of a sudden the count is very unrealistic." Any physical object breaking the light curtain beam registers as a tile count, producing impossible data.

- **Impossible count increases:** The unreliable sensors produce data that shows more tiles exiting a stage than entered it -- a physical impossibility. Mahesh described the specific problem: "I did only 1000 press, but 1500 things came out of the printer and that's not possible. In every step you can reduce the quantity, but you never increase the quantity." On the existing PI historian dashboard, a concrete example was visible: "the input to the glaze line was 22,500 but exited was 22,800 and so how did the glaze line press 300 tiles becomes a question."

- **Credibility collapse:** These data quality issues cause executives to distrust all production data. Mahesh explained: "once people look at this type of data, then they start doubting everything else to say this is not real."

### 2.2 Press Machine Readings

The press machines do have built-in instrumentation. Mahesh showed Colin the readings displayed on a press machine screen and noted: "these readings actually can tell you whether the press is doing the right thing or wrong thing." He expressed a desire to "ingest that every 5 minutes" to get early warning signals. However, this data is not currently being captured or stored in any systematic way for most sites.

### 2.3 PI Historian Database (Limited Sites)

A couple of sites do have a PI historian database that collects sensor data. These sites "can tell you exactly how much press they have done or whatnot." But even at these sites, the sensor reliability issues (blocked light curtains, dust) undermine the data quality. The existing PI-based dashboard that Mahesh showed Colin demonstrated the data integrity problems with impossible count increases.

---

## 3. Waste: Green Waste vs. Fired Waste

### 3.1 The Regulatory Constraint

This is the single most important distinction in Daltile's waste economics. There are two fundamentally different categories of waste, separated by the kiln:

- **Green waste (before kiln):** Any tile that is discarded before firing can be fully recycled. The unfired clay, even if it has been pressed, dried, glazed, and printed, can be crumbled back into raw material and fed back into the beginning of the process. Mahesh: "anything before [the kiln], they don't even think it's [waste] because it's like everything can be put in back."

- **Fired waste (after kiln):** Once a tile has been fired in the kiln, regulatory or R&D constraints limit how much fired material can be reintroduced into the raw material supply. The limit is 6%. Mahesh stated this precisely: "once it is fired they can only put 6% back... the raw material cannot have more than 6% of fired tile, as per their regulations or whatever R&D has agreed on."

This 6% constraint means that fired waste is essentially a total loss -- the material, the energy used to fire it, the machine time across every upstream process, and the labor cost. Mahesh underscored this point: "since our quality is happening over here [at the Qualitron, post-kiln], our fired waste is more than our green waste."

### 3.2 The Perverse Logic of Post-Kiln-Only Quality

Because the only quality testing happens after firing (at the Qualitron/sorting line), the factory systematically converts what could be green waste (recyclable) into fired waste (nearly total loss). This is the core frustration Mahesh expressed: quality problems that could theoretically be detected before firing -- bad shade from the printer, dimensional issues from the press -- are only caught after firing, when the 6% recycling limit makes the waste far more costly.

Mahesh stated: "I have heard multiple times to say since our quality is happening over here, our fired waste is more than our green waste. And so I'm like, this is stupid, right? Why are you not doing any testing over here if you think that that's what you want to do?"

### 3.3 Where Waste Occurs (and Goes Untracked)

Waste occurs at multiple stages in the process, but most of it is invisible to the finance and executive teams:

**During line setup/changeover:** When configuring a new item, the press starts and produces "100% waste till the point they have set the conveyors and everything in the proper alignment." The same startup waste problem cascades through the dryer, glaze line, and printer as each stage is tuned for the new product. This waste is not systematically tracked.

**Conveyor belt misalignment:** During normal operation, tiles can be damaged or discarded if "the conveyor belt has [jostled] the [tile] a little bit and it won't go in the proper way to the next process." Workers simply throw damaged tiles off the line. This waste occurs at any point along the conveyor belt and is not captured.

**Between press and glaze line:** The existing PI dashboard at one site showed 15,000 square feet pressed but only 14,000 making it to the dryer -- a 1,000 square foot gap with no explanation or error tracking.

**Between glaze line and kiln:** Similarly, the dashboard showed quantities declining between stages with no recorded reason. Mahesh pointed out: "no idea on what type of errors happened between these two."

**In the kiln itself:** The dashboard showed 28,000 square feet entering kilns but only 27,000 exiting -- another 1,000 square feet gap. Mahesh: "don't know what happened to the rest, right? No errors, nothing, right?"

**At the sorting line (the only tracked waste):** The sorting line is the sole point where rejection is formally recorded. This is where finance gets its 9% waste figure.

### 3.4 Finance's 9% Waste Calculation: The Undercount

Finance tracks waste only at the sorting line and reports a 9% waste rate. Mahesh considers this a significant undercount because it ignores all upstream waste. He stated explicitly: "they have this calculation to say 9% wastage, but it's more than 9% wastage. You can see there's wastage over here, there's wastage over here, there's wastage over here. They're not even tracking any of that. You know, to tell you, frankly, they track this [sorting line] as their wastage."

From the dashboard data Mahesh showed, visible waste gaps between stages (press to dryer, dryer to glaze, glaze to kiln, kiln to sorting) suggest substantial untracked waste well beyond the 9% reported figure. The dashboard example showed rejection rates at the sorting line itself varying: 2% rejection in one case, 10% rejection in another, depending on the production run.

### 3.5 Daltile's Dismissive Attitude Toward Pre-Kiln Waste

A significant cultural factor: because tiles are "just dirt" and pre-kiln waste can be fully recycled into raw material, the organization does not think of pre-kiln waste as waste at all. Mahesh described this mindset: "at any point, if there's a waste, they can just crumble it back again and put it back as a raw material. So they don't even think of waste as waste because they think like, oh, I can reuse everything, so I lost nothing."

Mahesh pushed back on this reasoning: "the reality is you lost all the effort that you did in pressing, drying, all the machine use and electricity paid, your employee, you know, employee costs paid, those are again costs that you pay." The machine time, energy, and labor consumed to produce tiles that are then crumbled back to raw material represent real economic loss even though the material cost is theoretically recovered.

The organization begins to care about waste only once glaze and print materials have been applied, because "those two are costly component of the raw material." But even then, they do not track waste formally until after firing, at the sorting line.

---

## 4. Ceramic Engineers' Resistance to Upstream Testing

### 4.1 "You Can't Do Testing Till It Is Baked"

Mahesh identified a significant organizational barrier: the ceramic engineers who run the factory floor insist that quality testing is impossible before kiln firing. Mahesh reported: "ceramic engineers who run the show tell me that you can't do testing till it is baked for whatever reason."

This belief has specific technical grounding -- the tile's appearance changes dramatically through the process. After printing, a protective glaze coat is applied that turns the tile white again before firing. Mahesh explained: "they don't want to burn this color. Because when it goes to the heat, the heat may burn this color. So what they do is before they put it into the heat, you will see they apply another white coat on top of it so that that can burn and the next layer will shine." After the protective coat, "if you take the picture at this stage it is useless because you can't figure out the print."

At some sites, the printer output is visible briefly before the protective glaze is applied. At other sites, "the printer actually prints and then immediately puts a glaze like within the next 5 seconds so that cycle of visibility of the color is limited."

### 4.2 Mahesh's Counterarguments

Despite the ceramic engineers' position, Mahesh sees paths to upstream quality detection:

- **Pre-glaze image correlation:** Mahesh proposed comparing images taken at the printer stage (before the protective white coat) to the final output, reasoning that even though "the final output will be much more colorful or much more enhanced, at least you can compare it to this image." The idea is that a consistent correlation between pre-coat and post-fire appearance could enable pre-firing shade detection.

- **Moisture sensing for caliber prediction:** Mahesh hypothesized that caliber problems (warping, dimensional deviation) could be predicted by monitoring moisture content upstream: "if your kiln is consistently at a particular temperature, then you know if your moisture is not changing much then it should perform exactly the same. So the fact that you know for whatever reason in a batch you know 10 or 20 of these are coming out bad means either the kiln has a problem or something is going on upstream in the process."

---

## 5. Colin's Technical Suggestions for Upstream Quality Detection

### 5.1 Humidity Sensors at Kiln Output

Colin identified moisture content as the critical missing data point for predicting caliber. He recommended: "very simple humidity sensors that are outside of the output of the kiln to get that humidity and trace it over time. You're gonna be able to correlate that down to that caliber."

He further proposed combining raw material moisture data with kiln output humidity data: "raw material specs for moisture content of that step plus at the kiln. Now I'm gonna be able to predict at pretty good accuracy what that caliber is, assuming that everything else is constant."

### 5.2 Upstream Sensor Correlation for Early Defect Detection

Colin challenged the ceramic engineers' position head-on, drawing from experience in adjacent industries: "You can't know if it's gonna be good or bad until the end. It is not true. You can definitely do it. You just need the data to say this, to correlate back." He argued that the belief that quality cannot be predicted before firing is "a very common process engineer thing" that data consistently disproves.

Colin's approach: collect data at every upstream stage, then use correlation analysis to identify leading indicators of post-kiln quality. Even without AI, pure sensor data would provide significant insight: "even without AI in the mix, if you just go into pure sensors, you can tell a lot with this."

He also identified the general categories of where defects come from in any process like this: "if you think about what could possibly happen at any diagram like this, it's either you have a potentially destructive step or a step where something is physically moving from location A to location B. Those are really where your errors come from, aside from a machine actually just being out of whack, out of spec."

### 5.3 Cross-Industry Parallels

Colin drew parallels to two other industries he has worked in to validate the upstream-testing approach:

- **Diamond polishing:** Diamond as-grown is opaque; you cannot see through it until after polishing. Yet quality can be predicted before polishing. Colin noted: "even from... like when we were polishing diamond, diamond has grown is super rough. You can't actually test it because you can't see through it. It's opaque. After polishing, now you can see it. It's the exact same thing here where it's white and kind of this powdery protective coating, and then afterwards it becomes colorful again. You can still correlate them, you just need the data to do it."

- **Silicon carbide manufacturing:** Colin noted that the tile manufacturing process is "almost identical in a way to silicon carbide. It's the same thing, except instead of water drying out, you're drying out a solvent. And instead of a press like this, you have something called a SIP, which is a cold isostatic press." The same upstream quality correlation techniques apply.

### 5.4 Light Curtain Thickness Measurement

Colin noted that light curtain sensors can do more than simple presence detection. More sophisticated configurations can measure glaze thickness: "I'm not sure if they're just a sensor in the sense that it's saying that something is gonna cross me. Sometimes they'll also have light curtains as a way -- it's more sophisticated. You can always tell cause there'll be an angle and it'll tell you the thickness of the glaze too."

### 5.5 Industrial Camera and Sensor Solutions for Dusty Environments

Colin addressed the practical concern of deploying sensors in the dusty factory environment. He identified multiple solutions:

- **Purge gas:** A purge gas system near cameras that keeps the lens clean
- **Industrial cameras with wipers:** "They actually make cameras, believe it or not, with a little windshield wiper... they're industrial grade. They're made for that purpose."
- **IP-rated sensors:** Selecting sensors with the proper ingress protection rating for a dust environment. Colin suggested matching sensor specs to the existing equipment ratings: "we'll just look at what spec the equipment itself is [rated at] and that'll be the same as the sensor spec."

---

## 6. Production Volume and Scale Context

The quality and waste challenges operate at significant scale:

- **Daily production volume:** Approximately 400,000 square feet per day at one plant. Mahesh: "for one plant, we make like 400,000 square feet every single day."
- **Equipment count (Sunnyvale plant):** 6 presses, 6 glaze lines, 6 printers, 4 kilns, 5 Qualitrons, 5 sorting lines, 1 palletizer
- **Tile size range:** From 6"x48" planks to 24"x24" squares (largest: 24"x24")
- **Dashboard rejection rates observed:** 2% in one sorting line example, 10% in another, 9% as the finance-reported overall average at sorting
- **Dashboard quantity gaps:** 15,000 sq ft pressed but only 14,000 to dryer (1,000 gap); 28,000 into kilns but 27,000 out (1,000 gap)
- **Counter reset practice:** All machine counters are manually reset daily at 6:00 AM, preventing work-order-level tracking

---

## 7. The Tracking Correlation Gap

A structural problem compounds the quality and waste challenge: there is no work-order-level correlation across stages. The existing dashboard tracks machine-level throughput (press 1 produced X square feet, glaze line 1 processed Y square feet), but because multiple products can flow through the same equipment and the WIP buffers break any direct lineage, there is no way to say which product's tiles were lost at which stage.

Mahesh described the problem at the kiln boundary specifically: "once you are at the kiln, which line went into which kiln? Because there is no correlationship... how much of this product got wasted in the kiln, I have zero idea because it could be all this product, it could be zero of this product."

The correlation breaks in both directions:

- **Forward:** One press can feed two glaze lines. Three glaze lines can feed one kiln. There is no tracking of which specific tiles from which work order went through which equipment path.
- **At WIP buffers:** When tiles enter the WIP staging areas (before kiln, after kiln, before sorting), they lose their identity. Multiple work orders commingle. When they emerge from the kiln, "magically part number [shows] up over here" at the sorting line, but the connection to what happened in the kiln is unknown.

This means waste between stages cannot be attributed to specific work orders, products, or root causes -- it is simply a quantity gap in the dashboard with no error codes, no categorization, and no accountability.

---

## 8. Summary of Quality and Waste Gaps

| Gap | Current State | Impact |
|-----|---------------|--------|
| Quality testing happens only post-kiln | Qualitron is the sole automated quality gate | Converts recyclable green waste into costly fired waste (6% recycling limit) |
| No upstream quality checks | Ceramic engineers believe pre-fire testing is impossible | Thousands of square feet of defective material accumulate in WIP before detection |
| Hourly manual sampling is the only proactive check | One or two tiles per hour, manually marked and tracked through kiln | Statistically inadequate sample; hours of lag between defect introduction and detection |
| Light curtain sensors are unreliable | Dust and physical obstructions produce impossible count data | Executives distrust all production data; sensor infrastructure lacks credibility |
| Finance tracks only sorting-line waste (9%) | Waste at press, dryer, glaze, printer, and kiln stages is untracked | True waste rate is higher than reported; no visibility into upstream losses |
| No work-order-level correlation across stages | Dashboard tracks machine throughput, not product lineage | Waste between stages cannot be attributed to products, root causes, or equipment paths |
| Pre-kiln waste is dismissed as non-waste | Recycling raw material does not account for machine time, energy, or labor costs | Hidden economic loss from upstream rework that never appears in waste calculations |
| Counter reset practice prevents granular tracking | All machine counters reset daily at 6:00 AM | Cannot associate production counts with specific work orders or time windows smaller than a full day |
