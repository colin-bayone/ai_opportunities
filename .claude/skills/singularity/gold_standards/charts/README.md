# Gold Standards: Charts

Chart and diagram gold standards including standalone mermaid.js diagrams and documents with embedded charts.

## Files

| File | What It Demonstrates |
|------|---------------------|
| `ecosystem_diagram.html` | Mermaid ecosystem diagram with subgraph clusters, icon nodes, and color-coded groupings. Standalone chart pattern: full-screen render with back button. |
| `session_0_platform_overview.html` | Document-with-embedded-charts pattern. Main HTML document with 3 mermaid diagrams rendered inline, each with an "Open full-screen diagram" link to the corresponding standalone chart file. From TalentAI knowledge transfer. |
| `architecture_overview.html` | Standalone full-screen architecture diagram with back button. Referenced by session_0_platform_overview.html. |
| `candidate_data_flow.html` | Standalone full-screen data flow diagram with back button. Referenced by session_0_platform_overview.html. |
| `fishbone_apps.html` | Standalone full-screen fishbone diagram with back button. Referenced by session_0_platform_overview.html. |
| `figure_1_platform_architecture.html` | Sephora QA/QE: Five-layer platform architecture with icons (Configuration, Deterministic, Playbooks, Agentic, Review, Observability). |
| `figure_2_discovery_cycle.html` | Sephora QA/QE: Self-improving discovery cycle (Agent explores → Human validates → Saved as playbook → Runs automatically). |
| `figure_3_playbook_lifecycle.html` | Sephora QA/QE: Playbook lifecycle workflow (discovered → saved → triggered → executed → checked). |
| `figure_4_confidence_scoring.html` | Sephora QA/QE: Confidence scoring mechanism showing agent result → human review → approval/correction paths. |

## How to Use

When creating a standalone chart file for a `charts/` subfolder (whether in a presentation deck or a document), use `ecosystem_diagram.html` as the structural reference. Key elements: full-viewport mermaid render, back button positioned top-left, blue-family or purple-family theme variables, clean subgraph labeling.

When embedding diagrams in a document or slide, use `session_0_platform_overview.html` as the reference. It demonstrates the correct pattern: diagram rendered inline with an "Open full-screen diagram" link that opens the standalone chart in a new tab. Every diagram gets both an inline embed and a standalone full-screen version.
