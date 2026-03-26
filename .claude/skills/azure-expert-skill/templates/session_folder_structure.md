# Azure Session Folder Structure Template

Use this structure for all Azure Expert Skill sessions.

## Naming Convention

```
claude/<YYYY-MM-DD>_AZURE_<topic>/
```

Examples:
- `claude/2026-01-06_AZURE_production_deployment/`
- `claude/2026-01-07_AZURE_cost_analysis/`
- `claude/2026-01-08_AZURE_network_troubleshooting/`

## Full Structure

```
claude/<YYYY-MM-DD>_AZURE_<topic>/
│
├── planning/                         # Approach planning
│   └── 00_session_started_YYYYMMDD_HHMM.md
│
├── goals/                            # Requirements and goals
│   └── (user-defined goals)
│
├── progress/                         # Status tracking
│   ├── 00_initial_status.md
│   └── (progress updates)
│
├── decisions/                        # Questions and decisions
│   └── (decision records)
│
├── research/                         # Investigation and intel
│   └── (research findings)
│
├── issues_and_improvements/          # Unresolved issues
│   └── (issues discovered)
│
├── documentation/                    # All generated documentation
│   ├── markdown/                    # .md files
│   │   ├── 01_resource_inventory_YYYYMMDD_HHMM.md
│   │   ├── 02_vnet_topology_YYYYMMDD_HHMM.md
│   │   └── ...
│   ├── json/                        # .json files
│   │   └── ...
│   └── csv/                         # .csv files
│       └── ...
│
├── exports/                          # Raw Azure exports
│   ├── raw_resources_YYYYMMDD_HHMM.json
│   ├── containerapp_*.json
│   ├── postgres_*.json
│   └── ...
│
├── scripts/                          # Session-specific scripts
│   └── (any custom scripts for this session)
│
├── agent_logs/                       # Activity logs per agent
│   ├── resource_explorer.log
│   ├── network_analyzer.log
│   ├── config_exporter.log
│   ├── cost_estimator.log
│   ├── deploy_debugger.log
│   ├── research_agent.log
│   ├── documentation_generator.log
│   ├── container_executor.log
│   └── browser_handoff.log
│
├── command_log.md                    # Master command log
│
└── source/                           # User-provided files
    ├── screenshots/
    └── (CSV exports, etc.)
```

## File Naming Convention

All generated files follow this pattern:

```
{NN}_{topic}_{YYYYMMDD_HHMM}.{ext}

NN        = Sequential number (01, 02, 03...)
topic     = snake_case description
YYYYMMDD  = Date (20260106)
HHMM      = Time in 24hr format (1430)
ext       = md, json, or csv
```

## Example Files

| Sequence | File Name |
|----------|-----------|
| 01 | `01_resource_inventory_20260106_1430.md` |
| 02 | `02_vnet_topology_20260106_1432.md` |
| 03 | `03_container_apps_20260106_1435.md` |
| 04 | `04_database_configuration_20260106_1438.md` |
| 05 | `05_cost_breakdown_20260106_1445.md` |

## Agent Log Format

Each agent log file follows this format:

```
================================================================================
AGENT: {agent_name}
SESSION: {session_folder_name}
================================================================================

[YYYY-MM-DD HH:MM:SS] {comment}
                      | {command}

[YYYY-MM-DD HH:MM:SS] {comment}
                      | {command}
```

## Command Log Format

The master command log (`command_log.md`) uses this format:

```markdown
# Azure Session Command Log

**Session:** {session_folder_name}
**Created:** {timestamp}

---

## Commands Executed

| Timestamp | Agent | Command | Result |
|-----------|-------|---------|--------|
| 2026-01-06 14:30:15 | resource_explorer | `az resource list -g rg` | success |
| 2026-01-06 14:30:18 | resource_explorer | `az containerapp show -n app -g rg` | success |
```
