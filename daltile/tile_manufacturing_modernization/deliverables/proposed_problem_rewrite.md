# Proposed Rewrite: "The Problem" Section

## What exists now

DalTile operates highly automated tile manufacturing plants producing 400,000 square feet of tile per day per plant. Despite this scale, they have virtually no software visibility into the production floor. There is no tracking of individual work orders through the manufacturing process. Quality testing happens only at the very end of the line, after the most expensive step (kiln firing), when defects are already locked in. Waste goes unmeasured at every stage except the final sorting step, and their legacy software system, written in a 1980s programming language, is unmaintained because the team that built it has departed.

## What I propose replacing it with

DalTile operates highly automated tile manufacturing plants producing 400,000 square feet of tile per day per plant. Despite this scale, they have no way to track yield, throughput, or traceability throughout the manufacturing process. There is no work order level lineage connecting raw material input to finished goods output. Production is measured only in aggregate (total square feet pressed, total kiln output), with no ability to trace a specific product through individual pieces of equipment.

This lack of traceability creates downstream consequences. Quality testing happens only at the very end of the line, after kiln firing (the most expensive step), so defects introduced at any earlier stage go undetected until the damage is locked in. Waste is unmeasured at every stage except the final sorting step, meaning the true cost of production inefficiency is unknown. A contributing factor is the legacy software system, written in a 1980s programming language, which is now unmaintained because the team that built it has departed. The result is that DalTile cannot identify where yield is lost, cannot attribute waste to specific process steps, and has no data foundation for reducing production costs at scale.

## What changed and why

1. **"no software visibility" replaced with "no way to track yield, throughput, or traceability"** - The actual problem is not about software. It is about the inability to track production at the work order level. Software visibility was a symptom description, not the root problem.

2. **Added "no work order level lineage" and "measured only in aggregate"** - These are the specific things Mahesh described. They know totals, but cannot connect any specific product to its journey through equipment.

3. **Downstream consequences are now clearly separated as consequences, not peers** - Quality testing being late and waste being unmeasured are results of having no traceability, not separate problems at the same level.

4. **Legacy system is now framed as a "contributing factor"** - It is real and in scope, but it is not the core problem. It contributes to the lack of visibility rather than being its own top-level issue.
