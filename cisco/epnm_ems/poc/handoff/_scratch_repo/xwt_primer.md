# XWT Primer — Starting Context Only
**Session 2, 2026-04-21.**

## Purpose of this document

To hand the execution session a factual starting catalog of XWT-namespaced files surfaced by the tree-report swarm against `EPNM/pf-framework`. Nothing in this document is a conclusion. Session 2 has not read XWT source. Everything below is observable from directory and filename data only.

## Context the execution session may not have yet

Handoff doc 06 §2 contains a 25-row widget-mapping table (Dojo → Angular Material). That table was produced from the Set 08 technical research, which studied raw Dojo primitives (`dijit/*`, `dojox/*`, `dojo/*`).

The tree-report swarm found a parallel widget-toolkit namespace in the EPNM framework repo: `pf-framework/ui/core/ui_components/lib/xwt/`. XWT is not in the Set 08 research and is not in doc 06's mapping table. Whether the POC-scoped screens use XWT widgets, base Dojo widgets, or a mix, is not determinable from the tree and is not determined here.

## Observed XWT files (tree report only)

All paths are under `EPNM/pf-framework/ui/core/ui_components/lib/xwt/`. Line counts are from the tree report.

| Widget directory | Primary file | Lines | Theme file under `xwt/themes/prime/` (where observed) |
|---|---|---|---|
| `widget/table/` | `Table.js` | 5,146 | `xwt/table/Table.css` (1,748), `Toolbar.css` (1,580) |
| `widget/uishell/` | `Header.js` | 524 | `xwt/uishell/Header.css` (392) |
| `widget/navigation/` | `SlideMenu.js` | 2,394 | `xwt/navigation/slidemenu.css` (630) |
| `widget/tasknavigator/` | `TaskNavigator.js` | 1,312 | (not enumerated in extract) |
| `widget/objectselector/` | `ObjectSelector.js` | 6,929 | (not enumerated in extract) |

Additional observation: a file named `AlarmsFormatter.js` (103 lines) exists in the framework layer. Name suggests fault-specific rendering hooks. No other "Alarms" or "Fault" artifacts were surfaced in pf-framework.

## Three grid generations coexist in pf-framework (tree report only)

Agent 05 observed three distinct grid widget families present in the repo:

1. `dojox/grid/DataGrid` (base Dojo).
2. `EnhancedGridWrapper` (wrapper on top).
3. XWT `Table.js` (see above).

Which generation Inventory's Network Devices list and Fault's Alarms table actually instantiate is not in the tree. Imports at the top of `assembly/.../InventoryListView.js` and `assembly/.../AlarmListView.js` would answer it.

## Other observed facts about XWT

- **Theme location.** `xwt/themes/prime/` holds per-widget CSS. Agent 05 noted no single EPNM palette file exists; blue-and-white theme values appear to be distributed across multiple per-component CSS files under that directory.
- **Dojo relationship.** File layout suggests XWT is layered on Dojo (same repo, separate namespace). Whether XWT widgets are subclasses of `dijit` widgets, compositions of Dojo primitives, or independent reimplementations is not determinable from tree data.
- **`dojo/topic.js`** exists at `pf-framework/ui/.../dojo/topic.js` (38 lines). Whether XWT widgets use `dojo/topic` for pub/sub or use something XWT-specific is not in the tree.

## What this document is not

- Not a conversion-pattern recommendation.
- Not a proposed extension to handoff doc 06 §2.
- Not an instruction to the execution session about what to read or when.
- Not a claim that XWT is in POC scope or out of it.

## What doc 06 §2 says

The existing Dojo mapping table is still in doc 06. It has not been edited in light of XWT's existence. If the execution session finds the POC screens use XWT widgets, the execution session decides whether to extend doc 06, write a separate XWT mapping, or handle translations ad hoc in code.
