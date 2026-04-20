# Architecture Diagram Draft

**Purpose:** Mermaid diagram showing the five-layer platform architecture for embedding in the preliminary approach HTML.
**Palette:** Purple (deliverable documents)
**Direction:** Top-to-bottom (TB), layered architecture

---

## Mermaid Code

```mermaid
graph TB

    subgraph L5["Layer 5: Observability"]
        OBS["`**Traceability and Diagnostics**
        Action logs, performance trends,
        edge case analysis, coverage metrics`"]
    end

    subgraph L4["Layer 4: Review and Confidence"]
        REV["`**Review Agent**
        Filters noise before
        human review`"]
        CONF["`**Confidence Scoring**
        Human-validated track records,
        decreasing review thresholds`"]
    end

    subgraph L3["Layer 3: Agentic Exploration"]
        EXPLORE["`**Exploratory Testing**
        Discovers anomalies in
        unfamiliar application states`"]
        VISUAL["`**Visual Understanding**
        Distinguishes intentional changes
        from genuine defects`"]
        DISCOVER["`**Workflow Discovery**
        Constructs new testing workflows
        for validation and save`"]
    end

    subgraph L2["Layer 2: Saved Playbooks"]
        PLAYBOOK["`**Deterministic Playbooks**
        Validated workflows saved as
        repeatable, release-mapped assets`"]
        CICD["`**CI/CD Integration**
        Tests triggered by code changes
        via GitHub Actions`"]
        SCHEDULE["`**Scheduled Execution**
        Nightly regressions and sweeps
        via Apache Airflow`"]
    end

    subgraph L1["Layer 1: Deterministic Automation"]
        PW["`**Playwright**
        Browser automation, screenshots,
        cross-device and cross-browser`"]
        MAP["`**Codebase Mapping**
        Component relationships, change
        impact, test targeting`"]
        DOCKER["`**Isolated Execution**
        Docker containers for development,
        Azure Container Apps in production`"]
    end

    subgraph CONFIG["Configuration Layer"]
        BASELINE["`**Baseline Reference**
        Prior state, Figma designs,
        component standards, expected content`"]
        TOLERANCE["`**Tolerance Settings**
        Pixel-level to broad,
        per team or per component`"]
        WORKFLOW["`**Workflow Integration**
        Reports, alerts, approval routing,
        CI/CD triggers per consumer group`"]
        CONNECTORS["`**Tool Connectors**
        Figma MCP, CMS integration,
        BrowserStack, repository access`"]
    end

    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 --> L5
    DISCOVER -.->|"Validated workflows"| PLAYBOOK
    CONFIG -.-> L1
    CONFIG -.-> L2
    CONFIG -.-> L3

    style L1 fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    style L2 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    style L3 fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#3b0764
    style L4 fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12
    style L5 fill:#fef9c3,stroke:#ca8a04,stroke-width:2px,color:#713f12
    style CONFIG fill:#f8fafc,stroke:#94a3b8,stroke-width:2px,color:#475569

    style PW fill:#dbeafe,stroke:#2563eb,stroke-width:1px,color:#1e3a5f
    style MAP fill:#dbeafe,stroke:#2563eb,stroke-width:1px,color:#1e3a5f
    style DOCKER fill:#dbeafe,stroke:#2563eb,stroke-width:1px,color:#1e3a5f
    style PLAYBOOK fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#14532d
    style CICD fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#14532d
    style SCHEDULE fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#14532d
    style EXPLORE fill:#ede9fe,stroke:#7c3aed,stroke-width:1px,color:#3b0764
    style VISUAL fill:#ede9fe,stroke:#7c3aed,stroke-width:1px,color:#3b0764
    style DISCOVER fill:#ede9fe,stroke:#7c3aed,stroke-width:1px,color:#3b0764
    style REV fill:#ffedd5,stroke:#ea580c,stroke-width:1px,color:#7c2d12
    style CONF fill:#ffedd5,stroke:#ea580c,stroke-width:1px,color:#7c2d12
    style OBS fill:#fef9c3,stroke:#ca8a04,stroke-width:1px,color:#713f12
    style BASELINE fill:#f8fafc,stroke:#94a3b8,stroke-width:1px,color:#475569
    style TOLERANCE fill:#f8fafc,stroke:#94a3b8,stroke-width:1px,color:#475569
    style WORKFLOW fill:#f8fafc,stroke:#94a3b8,stroke-width:1px,color:#475569
    style CONNECTORS fill:#f8fafc,stroke:#94a3b8,stroke-width:1px,color:#475569
```

## Design Notes

- **Layer colors follow the mermaid design standards semantic palette:**
  - Layer 1 (Deterministic): Blue (Code/Source category, foundational)
  - Layer 2 (Playbooks): Green (Proposed/New, the assets being built)
  - Layer 3 (Agentic): Purple (AI/Intelligence)
  - Layer 4 (Review): Orange (External/Integration, the human-system boundary)
  - Layer 5 (Observability): Yellow (Observability/Monitoring)
  - Configuration: Gray (cross-cutting, applies to multiple layers)

- **The dashed arrow from Discover to Playbook** shows the key feedback loop: AI-discovered workflows becoming deterministic assets

- **The dashed arrows from Configuration** show that the config layer feeds into the lower three layers (how tests run, what playbooks target, what agents explore)

- **Reading direction is bottom-up** conceptually (foundation at bottom, observability at top) but the graph renders top-to-bottom per mermaid conventions. The layer numbering makes the intended order clear.

## Integration Plan

This diagram will be rendered inline in Section 02 of the HTML deliverable using the mermaid.js async rendering pattern with the purple palette theme initialization, per the mermaid design standards.
