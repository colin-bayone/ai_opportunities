# Pricing Workflow

## When This Happens

Pricing is a late-stage activity. It requires:
- A clear understanding of the scope (from the research library)
- A defined deliverable (number of screens, documents, integrations, whatever the engagement delivers)
- Team composition decisions (who is available, what they cost)
- A target margin

It typically happens after the discovery decomposition is complete, after the approach is defined, and sometimes after a preliminary proposal has been shared and the client has expressed interest.

## Reference Files

The skill includes two reference files for pricing:

1. **Template prompt** (`.claude/skills/singularity/templates/excel_template_prompt.md`): A complete specification that Claude in Excel can execute to create a blank costing workbook from scratch. This exists in case the template file is lost, needs to be recreated, or needs to be built in a new format. It includes dummy data (Acme Corp, 120 screens, $350K), an Instructions tab, all formulas, formatting, and validation rules.

2. **Excel template** (`.claude/skills/singularity/templates/ProjectCostingTemplate.xlsx`): The ready-to-use workbook. This is the normal starting point. A user opens it, clears the dummy data, and enters their project details. Or Claude in Excel opens it and customizes it based on a pricing spec.

## The Workflow

### Step 1: Pricing Questionnaire

The skill runs an interactive Q&A with the user to gather all inputs needed to customize the template. This is a structured questionnaire, not a freeform discussion. Questions are asked in batches (max 5 per batch, per the methodology).

**Batch 1: Scope and Revenue**
- What is the deliverable? (e.g., 250 screens, 15 integrations, 1 platform)
- What unit do we measure delivery in? (screens, modules, endpoints, etc.)
- What is the quoted price / expected revenue?
- How many hours per unit do we estimate? (If unknown, the skill can research benchmarks)
- Is the POC absorbed or part of the paid scope?

**Batch 2: Team and Costs**
- Who is on the team? (Names, roles, annual salary or hourly rate for each)
- What is the load factor? (Default: 20% on top of base)
- What is the user's own allocation to this project? (percentage)
- Are there shared resources across projects? If so, what allocation per resource?

**Batch 3: Timeline and Scenarios**
- What are the delivery date options? (e.g., July vs. December)
- For each scenario: how many development months? How many stabilization months?
- How does team size change between scenarios? (e.g., 8 offshore for July, 3 for December)
- Is the user's allocation different across scenarios?

**Batch 4: Margin and Risk**
- What is the target margin? (e.g., 40% ideal, 30% floor)
- What risk reserve percentage? (e.g., 25% on base cost)
- Are there travel costs? How many trips, estimated cost per trip?
- Any hardware or consumables costs? (Often zero if client provides)

**Batch 5: Discount Strategy (if applicable)**
- Is the client likely to ask for a discount?
- What is the absolute floor margin?
- Should discounts only apply to the longer timeline? (Common strategy: never discount the compressed timeline)

### Step 2: Build the Pricing Spec

From the questionnaire answers, the skill writes a **pricing spec markdown** file in the engagement's `/<client_name>/<opportunity_name>/pricing/` folder. This file contains:

- All input parameters (rates, allocations, load factors, hours per unit)
- Month-by-month cost breakdowns for each scenario
- Risk reserve calculations
- Margin analysis at base cost and loaded cost
- Discount sensitivity table (if applicable)
- Per-unit economics (cost per screen, margin per screen, etc.)
- Throughput validation (can the team actually deliver the scope in the timeline?)

This file serves two purposes:
1. It is the **research record** of the pricing analysis (blockchain-style, append-only)
2. It is the **prompt for Claude in Excel** to customize the template workbook

### Step 3: Hand Off to Claude in Excel

The pricing spec markdown is given to Claude in Excel along with the template workbook. Claude in Excel:
- Opens the template (or creates from the template prompt if needed)
- Populates the Inputs tab with the project-specific parameters
- Adjusts scenario tabs for the correct number of months and resources
- Updates formulas, named ranges, and formatting
- Validates that the numbers match the markdown spec

The skill writes the pricing spec to a known location so the user can copy-paste it into a Claude for Excel session.

### Step 4: Iterate

If the user or their CEO has feedback (as happened in the Cisco engagement), the skill writes **correction prompts** as separate markdown files in `/<client_name>/<opportunity_name>/pricing/`. These are additive instructions for the Claude in Excel session:

```
/<client_name>/<opportunity_name>/pricing/
├── pricing_spec_2026-03-26.md                  (the main spec from the questionnaire)
├── pricing_corrections_v1_2026-03-26.md        (first round of feedback)
├── pricing_corrections_v2_2026-03-27.md        (second round)
└── ...
```

Each correction prompt is self-contained and tells Claude in Excel exactly what to change, where, and why. The pattern: describe the problem, describe the fix, provide validation steps.

## Cross-Session Artifact Pattern

This pricing workflow establishes a broader pattern the skill uses throughout: **creating markdown documents that serve as prompts for other Claude sessions.**

This pattern applies beyond pricing:
- A deliverable spec written in markdown becomes the prompt for Claude in Excel, Claude in a browser, or another Claude Code session
- A correction prompt captures iterative feedback in a reusable format
- A template prompt captures a repeatable process so it can be recreated from scratch

The skill should always write these artifacts to the appropriate engagement folder with clear, dated names. Pricing artifacts go in `/<client_name>/<opportunity_name>/pricing/`. Other cross-session artifacts go in `/<client_name>/<opportunity_name>/planning/`. They are part of the engagement record and can be referenced by future sessions.

## What Gets Documented in Research

The pricing discussion itself (the back-and-forth where decisions are made about margin targets, team composition, allocation percentages, discount strategy) is captured as a research document set, just like any other discussion:

```
/<client_name>/<opportunity_name>/research/
├── 04_discussion_pricing_strategy_2026-03-26.md
└── 04_discussion_summary_2026-03-26.md
```

The pricing spec in `/<client_name>/<opportunity_name>/pricing/` is the actionable output. The research doc is the record of how and why those decisions were made.
