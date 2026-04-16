# Gold Standard: Team Status Update Presentation

**Source engagement:** Cisco CI/CD (Srinivas status update deck)
**Created:** 2026-04-10
**Purpose:** Gold standard for team status update presentations. Demonstrates the presentation design language applied to a real weekly status update delivered in a client meeting. Read this deck before generating any status update presentation.

---

## What This Deck Demonstrates

| Slide | File | Patterns Demonstrated |
|-------|------|-----------------------|
| 00 | `00_title.html` | Dark full-bleed title, BayOne Solutions branding, presenter credit, date |
| 01 | `01_assigned_items_status.html` | Three-column card grid, status badges, bullet formatting (`.items`/`.item` pattern), takeaway bar |
| 02 | `02_discovery_findings_build.html` | Definition bar + two-card grid, bullet items in every card, gradient progression, takeaway bar |
| 02a | `02a_build_ecosystem_diagram.html` | Diagram slide with mermaid.js blue palette, "Open full-screen diagram" link to `charts/` for standalone full-screen view |
| 03 | `03_discovery_findings_webex.html` | Definition bar + two-card grid, bullet formatting, diplomatic framing of existing work as "prototypes" |
| 04 | `04_items_for_discussion.html` | Definition bar + two-card grid, bullet items, diplomatic "alignment needed" framing (not conflicts) |
| 05 | `05_access_status.html` | Three-column status grid with colored indicators (green granted, amber in-progress, blue needs assistance), takeaway bar |
| 06 | `06_next_steps.html` | Split panel (left: framing + access list, right: 4 numbered steps with bullet sub-items), connection strip |
| chart | `charts/build_log_ecosystem.html` | Standalone full-screen mermaid diagram, back button, blue-family theme variables, subgraph clusters with color coding |

## Key Design Rules This Deck Follows

- **Bullet formatting is the default** for all card bodies. No paragraph text in cards.
- **Navigation is on every slide** (prev/next/home, bottom-left).
- **Content uses specific details** from the source material, not vague corporate language.
- **Access status gets its own slide** because it has 8+ items.
- **Large diagrams get their own slide** (02a) rather than being crammed into content slides.
- **No individual names** in content slides. Presenter credit only on title slide.
- **No direct quotes** from any person.
- **Diplomatic framing** throughout: problems presented as "alignment needed," existing work called "prototypes," architecture framed as "initial thinking."
- **Charts subfolder** with standalone full-screen diagram that has a back button.

## Slide Navigation Chain

```
00 (title) -> 01 (assigned items) -> 02 (build findings) -> 02a (diagram)
-> 03 (webex findings) -> 04 (discussion) -> 05 (access) -> 06 (next steps)
```

First slide: prev disabled. Last slide: next disabled. Home: always 00_title.html.
