# Phase 3 Session 3: Phoenix Theme Skill + Standalone Agents

## Executive Summary

1. **Phoenix Theme Skill is a sophisticated orchestrator** with 7 sub-agents, progressive data disclosure via JSON indexes, and comprehensive workflow definitions - a mature pattern for complex domain skills

2. **Data catalog uses hierarchical indexing** with `_master_index.json` mapping pages to components, and per-folder `_index.json` files enabling efficient navigation of 100+ HTML files

3. **Phoenix agents use minimal frontmatter** (name, description, model) compared to forge agents which add tools lists and configuration tables - both are valid patterns

4. **The phoenix-skill-to-agents relationship is implicit** - agents reference the skill's data but the connection is documented in prose, not structured metadata

5. **Workflow orchestration is embedded in SKILL.md** rather than using explicit coordination mechanisms - different from the forge's Judge/Foreman/Worker pattern

6. **All phoenix agents specify `model: sonnet`** for cost efficiency, while forge agents use `model: opus` for complex judgment tasks - this is intentional differentiation

7. **Both patterns lack 2026 Agent Teams features** - no `groups`, `dependencies`, `allowed_tools`, or structured handoff protocols from the latest best practices

---

## Files Analyzed

### Phoenix Theme Skill Core
- `.claude/skills/phoenix-theme-skill/SKILL.md` (366 lines)
- `.claude/skills/phoenix-theme-skill/data/components/_master_index.json` (531 lines)

### Phoenix Data Samples
- `.claude/skills/phoenix-theme-skill/data/components/modules_components_alerts/_index.json`
- `.claude/skills/phoenix-theme-skill/data/components/modules_components_alerts/00_alert_subtle_examples.html`
- `.claude/skills/phoenix-theme-skill/data/components/modules_components_card/_index.json`
- `.claude/skills/phoenix-theme-skill/data/components/modules_components_card/00_basic_example.html`

### Phoenix Standalone Agents (7)
- `.claude/agents/phoenix-catalog-explorer.md` (182 lines)
- `.claude/agents/phoenix-chart-advisor.md` (259 lines)
- `.claude/agents/phoenix-django-explorer.md` (246 lines)
- `.claude/agents/phoenix-implementation-planner.md` (413 lines)
- `.claude/agents/phoenix-pattern-validator.md` (327 lines)
- `.claude/agents/phoenix-screenshot-analyzer.md` (265 lines)
- `.claude/agents/phoenix-template-generator.md` (463 lines)

### Comparison Agents
- `.claude/agents/architect.md` (230 lines)
- `.claude/agents/judge.md` (455 lines)
- `.claude/agents/foreman.md` (260 lines)
- `.claude/agents/planner.md` (246 lines)
- `.claude/agents/code-worker.md` (285 lines)

---

## Detailed Analysis

### Phoenix Theme Skill

#### SKILL.md Architecture

The Phoenix Theme Skill is an **orchestrator pattern** that:

1. **Coordinates 7 sub-agents** rather than doing work itself
2. **Provides quick lookups** via summary markdown files (2-15 KB each)
3. **Delegates heavy work** to specialized agents
4. **Defines 6 explicit workflows** for different user intents:
   - Workflow 1: Component Search
   - Workflow 2: Mockup Analysis
   - Workflow 3: UI Alignment Review
   - Workflow 4: Brainstorming Session
   - Workflow 5: Data-Driven Dashboard Design
   - Workflow 6: Implementation Handoff

**Key Design Decisions:**

| Decision | Rationale |
|----------|-----------|
| Summary files readable, catalog via scripts | Context window management |
| Parallel execution (Catalog + Screenshot) | Performance optimization |
| Sequential execution (Template -> Validator) | Dependency requirement |
| Phoenix components only, no custom | Quality gate enforcement |
| Font Awesome 5 (not 6) | Version lock to Phoenix 1.23.0 |
| HTMX only, no Ajax | Tech stack constraint |

**Frontmatter (SKILL.md):**
```yaml
---
name: phoenix-theme-skill
description: |
  Assists developers working with the Phoenix Bootstrap theme v1.23.0...
  This skill orchestrates specialized sub-agents for different tasks:
  - phoenix-catalog-explorer: Search the 219-page Phoenix catalog
  - phoenix-screenshot-analyzer: Analyze mockup images
  [... 5 more agents listed ...]
---
```

**Notable:** No `model`, `tools`, `groups`, or other structured configuration - just name and description.

---

### Data Catalog Pattern

#### _master_index.json Structure

```json
{
  "extracted_at": "1765949198.3344626",
  "pages_processed": 12,
  "total_components": 93,
  "pages": [
    {
      "page": "modules/components/alerts.html",
      "components": [
        {
          "name": "Alert Subtle Examples",
          "type": "code_block",
          "file": "00_alert_subtle_examples.html"
        }
      ]
    }
  ]
}
```

**Purpose:** Maps Phoenix documentation pages to extracted component files.

#### Per-Folder _index.json Structure

```json
{
  "page": "modules/components/alerts.html",
  "components": [
    {
      "name": "Alert Subtle Examples",
      "type": "code_block",
      "file": "00_alert_subtle_examples.html"
    },
    {
      "name": "Alert Outline Examples",
      "type": "code_block",
      "file": "01_alert_outline_examples.html"
    }
  ]
}
```

**Purpose:** Local index for component discovery within a category folder.

#### Component HTML Files

```html
<!-- Component: Alert Subtle Examples -->
<!-- Type: code_block -->
<!-- Source: modules/components/alerts.html -->

<div class="alert alert-subtle-primary" role="alert">A simple primary alert</div>
```

**Purpose:** Extracted, commented HTML snippets ready for use in templates.

#### Progressive Disclosure Pattern

```
Query Flow:
1. Agent reads _master_index.json (small, fast)
2. Agent identifies relevant page/folder
3. Agent reads specific _index.json
4. Agent reads specific component HTML file(s)
```

**Benefit:** Never loads all 100+ files; loads only what's needed.

---

### Phoenix Agents

| Agent | Purpose | Model | Key Patterns |
|-------|---------|-------|--------------|
| phoenix-catalog-explorer | Search 219-page Phoenix catalog | sonnet | YAML output format, structured results |
| phoenix-chart-advisor | Recommend charts based on data | sonnet | **Interactive questionnaires**, decision trees |
| phoenix-django-explorer | Analyze Django models/views | sonnet | Data-to-widget mapping, gap analysis |
| phoenix-implementation-planner | Create handoff documentation | sonnet | Multi-file output, implementation sequences |
| phoenix-pattern-validator | Validate Phoenix compliance | sonnet | Quality gates, severity levels, fix suggestions |
| phoenix-screenshot-analyzer | Analyze mockup images | sonnet | Visual inventory, component mapping, ASCII layouts |
| phoenix-template-generator | Generate Django templates | sonnet | Code patterns, HTMX integration, **screenshot verification** |

#### Frontmatter Comparison

**Phoenix Agents (minimal):**
```yaml
---
name: phoenix-catalog-explorer
description: |
  Search and retrieve Phoenix Bootstrap theme components...
  Use this agent when:
  - User describes a UI element they need
  - Starting any Phoenix component search
  This agent runs in PARALLEL with the Screenshot Analyzer...
model: sonnet
---
```

**Forge Agents (more structured):**
```yaml
---
name: architect
description: Strategic coordinator for implementation planning...
model: opus
---

# In body, has Configuration table:
| Property | Value |
|----------|-------|
| Model | Opus |
| Async | No |
| Tools | Read, Glob, Write |
```

#### Unique Phoenix Agent Patterns

1. **Interactive Questionnaires** (phoenix-chart-advisor):
   - Multi-phase discovery questions
   - Checkbox-style question sets
   - Decision trees for chart selection

2. **Screenshot Verification** (phoenix-template-generator):
   ```bash
   poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py
   ```
   - Agents can verify their own output visually

3. **ASCII Layout Blueprints** (phoenix-screenshot-analyzer):
   ```
   ┌─────────────────────────────────────────────────────────────┐
   │ Navbar Top (full width)                                     │
   ├────────────┬────────────────────────────────────────────────┤
   │  Navbar    │ Main Content Area                              │
   │  Vertical  │ ┌──────────┬──────────┬──────────┬──────────┐ │
   └────────────┴─┴──────────┴──────────┴──────────┴──────────┴─┘
   ```

4. **CRITICAL Image Handling Rules** (phoenix-screenshot-analyzer):
   - "ALWAYS list ALL images first"
   - "Read EVERY image"
   - "Never skip images"

---

### Comparison with Other Agents

#### Forge Swarm Pattern (architect, foreman, judge, code-worker)

| Agent | Role | Model | Key Difference |
|-------|------|-------|----------------|
| architect | Strategic decomposition | opus | Creates task-manifest.md, **does NOT code** |
| engineer | Technical design | opus | Adds HOW to architect's WHAT |
| foreman | Orchestrates workers | opus | Manages waves, spawns workers, tracks rework |
| judge | Quality evaluation | opus | CRITICAL/MAJOR gates, **APPROVED/REWORK/BLOCKED** |
| code-worker | Implementation | opus (in config) / sonnet (in frontmatter) | Writes actual code |
| planner | Combined arch+eng | sonnet | Efficiency for MEDIUM/LOW complexity |

#### Key Architectural Differences

| Aspect | Phoenix Pattern | Forge Pattern |
|--------|-----------------|---------------|
| **Coordination** | SKILL.md orchestrates implicitly | Foreman orchestrates explicitly |
| **Quality Gates** | phoenix-pattern-validator checks compliance | Judge has 10 named gates (SOC2, DRY, etc.) |
| **Output Tracking** | No formal tracking | task-log.json, rework-queue.json |
| **Rework** | Not explicitly defined | Max 3 iterations, then BLOCKED |
| **Escalation** | User notified via skill | **Always escalate BLOCKED** to user |
| **Model Selection** | All sonnet | Opus for judgment, varied for workers |

#### Frontmatter Fields Used

| Field | Phoenix Agents | Forge Agents | Notes |
|-------|---------------|--------------|-------|
| name | Yes | Yes | Required |
| description | Yes (verbose) | Yes (concise) | Phoenix includes "Use when" |
| model | Yes (sonnet) | Yes (opus) | In frontmatter |
| tools | No | No (in body as table) | Not in frontmatter |
| groups | No | No | 2026 feature |
| dependencies | No | No | 2026 feature |

---

## Good Patterns (Keep)

### 1. Progressive Data Disclosure
The hierarchical index pattern (`_master_index.json` -> `_index.json` -> component files) is excellent for managing large datasets without overloading context.

**Recommendation:** Skill-forge should generate this pattern for any skill with >20 data files.

### 2. Explicit Workflow Definitions
Phoenix SKILL.md defines 6 workflows with clear triggers and steps:
```
### Workflow 2: Mockup Analysis
**Trigger**: User provides screenshot/image

1. Parse request -> note image path
2. Launch PARALLEL:
   - Screenshot Analyzer (primary)
   - Catalog Explorer (pre-warm with common terms)
3. Wait for both
...
```

**Recommendation:** Skill-forge should generate workflow templates with triggers and parallel/sequential notation.

### 3. "Use This Agent When" Lists
Phoenix agents explicitly list their invocation triggers:
```yaml
Use this agent when:
- User describes a UI element they need
- Starting any Phoenix component search
- Need to find matching Phoenix patterns
```

**Recommendation:** All agent descriptions should include explicit trigger conditions.

### 4. YAML/Structured Output Formats
Both phoenix-catalog-explorer and judge define explicit output schemas:
```yaml
results:
  - rank: 1
    relevance: "high"
    title: "Page Title"
    url: "https://..."
```

**Recommendation:** Skill-forge should encourage structured output definitions.

### 5. Quality Gates with Severity Levels
Judge distinguishes CRITICAL vs MAJOR vs MINOR:
```markdown
### CRITICAL Gates
- No Truncation
- No Hacky Workarounds
- SOC2 Compliance
- Security (OWASP)
- Tests Pass

### MAJOR Gates
- Idempotency
- DRY Principle
```

**Recommendation:** Pattern validators should use severity-based gate systems.

### 6. Self-Verification Checklists
code-worker includes self-verification:
```markdown
### Self-Verification Checklist
- [x] Follows patterns from technical-design.md
- [x] Uses HTMX (no JavaScript added)
- [x] Django best practices followed
```

**Recommendation:** Workers should verify their own output before submission.

### 7. Screenshot Tool Integration
phoenix-template-generator can verify its output visually:
```bash
poetry run python ...scripts/05_screenshot_html.py demo.html
```

**Recommendation:** Agents with visual output should have verification tools.

---

## Outdated Patterns (Update)

### 1. Missing `allowed_tools` in Frontmatter
2026 best practices specify tools in frontmatter:
```yaml
---
name: agent-name
allowed_tools: [Read, Write, Glob, Grep, Bash]
---
```

**Current State:** Tools listed in body tables or not at all.

### 2. No `groups` or `dependencies` Fields
Agent Teams feature from Dec 2025 enables:
```yaml
---
groups: [phoenix-team, ui-team]
dependencies: [catalog-explorer]
---
```

**Current State:** Dependencies described in prose only.

### 3. Implicit Agent Discovery
Phoenix agents are discovered by name convention. No registry or explicit linking.

**Should Be:** Explicit agent manifests or group definitions.

### 4. No Handoff Protocol Specification
Agents output to files, but there's no standardized handoff format:
```yaml
handoff:
  format: yaml
  location: "{session_path}/implementation/completed-work/{task_id}.md"
  schema: task-completion-v1
```

### 5. Model Selection Not Dynamic
All phoenix agents hardcode `model: sonnet`. No ability to upgrade for complex tasks.

**Should Support:**
```yaml
model:
  default: sonnet
  upgrade_when: complexity > HIGH
```

### 6. No Telemetry or Metrics
Judge tracks rework counts, but no formal telemetry:
```yaml
metrics:
  - rework_rate
  - approval_confidence
  - time_to_complete
```

### 7. Missing Safety/Guard Rails
No explicit safety constraints in frontmatter:
```yaml
safety:
  max_file_edits: 10
  prohibited_paths: [".env", "secrets/*"]
  require_approval_for: [database_migrations]
```

---

## Unique Patterns (Consider)

### 1. Interactive Questionnaires (phoenix-chart-advisor)
Multi-phase discovery questions with checkboxes:
```
**Question Set 1: Goals**
What story do you want the data to tell?

[ ] Show progress toward goals (gauge, progress bars)
[ ] Compare items/categories (bar, radar)
[ ] Show trends over time (line, area)
```

**Value:** Structured user input gathering for complex decisions.

### 2. ASCII Layout Blueprints (phoenix-screenshot-analyzer)
Visual representation of page structure:
```
┌─────────────────────────────────────────────────────────────┐
│ Navbar Top (full width)                                     │
├────────────┬────────────────────────────────────────────────┤
│  Sidebar   │ Main Content Area                              │
```

**Value:** Human-readable layout documentation.

### 3. Data-to-Widget Mapping Tables (phoenix-django-explorer)
```
| Data Pattern | Widget Type | Example |
|--------------|-------------|---------|
| Count of items | Stat Card | "245 Active Candidates" |
| Items by status | Pie/Donut Chart | Applications by stage |
```

**Value:** Systematic mapping from data patterns to UI components.

### 4. Pitfall Documentation
Multiple agents include "Pitfalls to Avoid":
```markdown
### Pitfalls to Avoid
1. Don't use Font Awesome 6 icons (Phoenix uses FA5)
2. Don't hardcode URLs (use {% url %} tags)
```

**Value:** Error prevention through explicit anti-patterns.

### 5. Reference URL Requirements
Phoenix agents require documentation URLs:
```markdown
Every significant component should have:
- Component name
- Phoenix reference URL
- Key Bootstrap classes noted
```

**Value:** Traceability to source documentation.

### 6. Rework Loop Detection (judge)
```
If this is a rework submission:
1. Compare to previous submission
2. If >90% identical: BLOCKED (stuck in loop)
```

**Value:** Prevents infinite rework cycles.

### 7. Coordination Notes in Evaluations
Judge includes sections for cross-agent coordination:
```markdown
### Coordination Notes

#### For Architect
{If architectural review needed}

#### For Engineer
{If technical design adjustment needed}

#### For Foreman
{Coordination requirements}
```

**Value:** Explicit handoff to other agents when issues cross boundaries.

---

## Recommendations for Skill-Forge

### 1. Generate Agent Registry
Skill-forge should create a manifest file:
```yaml
# .claude/skills/{skill}/agents.yaml
agents:
  - name: catalog-explorer
    purpose: Search component catalog
    model: sonnet
    parallel_with: [screenshot-analyzer]

  - name: template-generator
    purpose: Generate templates
    model: sonnet
    depends_on: [catalog-explorer]
```

### 2. Support Data Catalog Pattern
When a skill has structured data, generate:
```
data/
  _master_index.json    # Full catalog index
  {category}/
    _index.json         # Category index
    {item}.{ext}        # Individual files
```

### 3. Include Workflow Templates
SKILL.md should have workflow blocks:
```yaml
workflows:
  - name: Component Search
    trigger: "User describes UI element needed"
    steps:
      - agent: catalog-explorer
        parallel: false
      - agent: template-generator
        parallel: false
        depends_on: [catalog-explorer]
```

### 4. Standardize Quality Gates
Pattern validators should use:
```yaml
quality_gates:
  critical:
    - name: No Truncation
      check: "No incomplete implementations"
    - name: Security
      check: "OWASP compliance"
  major:
    - name: DRY
      check: "No code duplication"
```

### 5. Add Interactive Question Support
For complex skills, enable:
```yaml
questionnaire:
  phase1:
    question: "What story do you want data to tell?"
    options:
      - label: "Show progress"
        leads_to: gauge_charts
      - label: "Compare items"
        leads_to: bar_charts
```

### 6. Support Visual Verification
Skills with visual output should include:
```yaml
verification:
  type: screenshot
  script: scripts/verify_output.py
  output_format: png
```

### 7. Explicit Escalation Paths
```yaml
escalation:
  on_blocked: always_user
  on_max_rework: user_decision
  on_security_issue: immediate_halt
```

### 8. Model Upgrade Hints
```yaml
model:
  default: haiku
  use_sonnet_for: [complex_searches, multi_file_generation]
  use_opus_for: [architectural_decisions, security_review]
```

---

## Appendix: Full Agent Frontmatter Comparison

### Phoenix Agents Frontmatter

| Agent | name | description | model | Other |
|-------|------|-------------|-------|-------|
| phoenix-catalog-explorer | Yes | Multi-line with "Use when" | sonnet | None |
| phoenix-chart-advisor | Yes | Multi-line with "Use when" + "interactive" | sonnet | None |
| phoenix-django-explorer | Yes | Multi-line with "Use when" | sonnet | None |
| phoenix-implementation-planner | Yes | Multi-line with "Use when" | sonnet | None |
| phoenix-pattern-validator | Yes | Multi-line with "Use when" | sonnet | None |
| phoenix-screenshot-analyzer | Yes | Multi-line with "Use when" | sonnet | None |
| phoenix-template-generator | Yes | Multi-line with "Use when" | sonnet | None |

### Forge Agents Frontmatter

| Agent | name | description | model | Other |
|-------|------|-------------|-------|-------|
| architect | Yes | One-line | opus | None |
| foreman | Yes | One-line | opus | None |
| judge | Yes | One-line | opus | None |
| planner | Yes | One-line | sonnet | None |
| code-worker | Yes | One-line | sonnet | None |

### Configuration Table Pattern (Forge agents in body)

```markdown
## Configuration

| Property | Value |
|----------|-------|
| Model | Opus |
| Async | No |
| Tools | Read, Glob, Write |
```

**Observation:** Forge agents document tools in body tables, not frontmatter. Phoenix agents don't document tools explicitly.

---

## Conclusion

The Phoenix Theme Skill represents a mature, well-designed orchestrator pattern with sophisticated data management (progressive disclosure via JSON indexes) and clear workflow definitions. The standalone agents are specialized and focused, with good "Use when" documentation.

However, both Phoenix and Forge patterns predate the 2026 Agent Teams features and could benefit from:
1. Frontmatter-based tool specifications
2. Explicit agent groups and dependencies
3. Standardized handoff protocols
4. Model upgrade hints
5. Built-in telemetry support

Skill-forge should learn from both patterns:
- **From Phoenix:** Data catalog pattern, interactive questionnaires, visual verification
- **From Forge:** Quality gates, rework tracking, explicit escalation paths

The combination would create a robust skill generation system capable of producing sophisticated, well-orchestrated agent teams.
