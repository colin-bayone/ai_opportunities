# 08 - Research: Summary

**Source:** Web research
**Source Date:** 2026-04-07
**Document Set:** 08 (Technical Research)
**Pass:** Summary

---

## Overview

Three parallel web research documents covering the complete technology landscape for the EPNM-to-EMS classic view toggle engagement. Produced to give the BayOne team a working reference for the POC and beyond.

## Documents in This Set

| File | Focus | Size |
|------|-------|------|
| `08_research_epnm_legacy_stack_2026-04-07.md` | EPNM stack: Dojo 1.x (Dijit widgets, AMD, pub/sub, stores, lifecycle), Oracle DB integration, Java monolith patterns, SNMP/CLI device management. End-to-end code example. Key conversion risks. | Comprehensive |
| `08_research_ems_modern_stack_2026-04-07.md` | EMS stack: Angular 21 (signals, standalone components, Material), Harbor/Magnetic design system, Spring Boot REST patterns, Go services for device management, PostgreSQL (Oracle migration), microservices architecture and shell app pattern. | Comprehensive |
| `08_research_conversion_patterns_2026-04-07.md` | Conversion patterns: 25-row Dijit-to-Angular widget mapping, AMD-to-ES6 modules, data binding (watch -> signals/observables), event handling (pub/sub -> RxJS), lifecycle mapping, state management (stores -> services), theme toggle architecture (CSS custom properties + ThemeService), API integration (shared services with display adapters), shell app integration (toggle placement, routing, folder structure). Full code examples throughout. | ~900 lines |
| `08_research_summary_2026-04-07.md` | This file |

## Key Takeaway

The conversion patterns document is the most immediately actionable. It provides concrete, code-level mappings for every aspect of the Dojo-to-Angular conversion, including a complete theme toggle architecture and a per-screen migration checklist. The EPNM and EMS stack references provide the context needed to understand why those patterns work the way they do.

## Priority for POC

1. **Conversion patterns** — Use the widget mapping table and theme toggle architecture immediately
2. **EMS stack reference** — Understand the shell app architecture and where classic UI code fits
3. **EPNM stack reference** — Consult when encountering unfamiliar Dojo patterns in the legacy code
