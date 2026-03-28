# Acceleration Mechanism: Why POC Velocity Does Not Extrapolate Linearly

**Reference Document for POC Proposal**
**February 2026**

---

## Overview

The four-week POC duration does not extrapolate linearly to full-scale conversion. The POC front-loads infrastructure investment that does not repeat for subsequent screens: codebase exploration, pattern identification, agent development, workflow design, and tooling setup all happen once.

Once this infrastructure is in place, per-screen work becomes predictable. The POC establishes a baseline velocity under the slowest possible execution mode: single resource, sequential work, infrastructure still being developed. Any estimate derived from this baseline is inherently conservative. Additional team members and the LangGraph multi-agent architecture provide linear or better improvements to delivery velocity; projections based on POC performance therefore represent a reliable floor rather than an optimistic target. BayOne is prepared to discuss staffing and timeline projections after the exploration phase, when analysis provides the data needed for accurate estimation.

---

## One-Time Infrastructure Investment

| Work | Output |
|------|--------|
| Codebase exploration | Knowledge graph mapping architecture, dependencies, and patterns |
| Pattern identification | EPNM-to-EMS conversion library specific to this codebase |
| Agent development | Custom LangGraph agents tuned to this architecture, encoding discovered patterns and edge cases |
| Workflow design | Validated conversion process with quality gates |
| Tooling setup | Playwright test infrastructure, CI integration, comparison reporting |

This infrastructure is developed during the POC at BayOne's investment.

---

## Per-Screen Work

| Activity | First Screen | Subsequent Screens |
|----------|--------------|-------------------|
| Pattern discovery | Extensive | Minimal (patterns already cataloged) |
| Agent tuning | Significant | Incremental (agents already trained) |
| Implementation | Discovery-driven | Application of known transformations |
| Validation | Establish baselines | Execute existing comparisons |
| Gap identification | Novel findings | Variations on documented gaps |

The first screen carries the full weight of infrastructure development. The second screen benefits from all prior work. By the third screen, execution follows established patterns rather than requiring discovery.
