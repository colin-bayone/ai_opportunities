# Path Verification: presentation_design_language.md

**Source file:** `.claude/skills/singularity/references/presentation_design_language.md`
**Verified:** 2026-04-13
**Base path:** `.claude/skills/singularity/`

---

## Directory and File Path References

All paths are resolved relative to `.claude/skills/singularity/` unless they begin with `.claude/skills/singularity/` (in which case they resolve from the repo root).

| # | Line | Path as Written | Resolved Absolute Path | Exists |
|---|------|----------------|----------------------|--------|
| 1 | 12 | `.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/` | `assets/design/gold_standards/presentations/srinivas_status/` | yes |
| 2 | 19 | `.claude/skills/singularity/assets/slide_examples/` | `assets/slide_examples/` | yes |
| 3 | 20 | `assets/design/gold_standards/presentations/srinivas_status/` | `assets/design/gold_standards/presentations/srinivas_status/` | yes |
| 4 | 228 | `assets/design/gold_standards/charts/example_ecosystem_diagram.html` | `assets/design/gold_standards/charts/example_ecosystem_diagram.html` | yes |
| 5 | 228 | `assets/design/gold_standards/presentations/srinivas_status/02a_build_ecosystem_diagram.html` | `assets/design/gold_standards/presentations/srinivas_status/02a_build_ecosystem_diagram.html` | yes |
| 6 | 230 | `references/mermaid_design_standards.md` | `references/mermaid_design_standards.md` | yes |
| 7 | 332 | `gold_standards/knowledge_transfer/session_0_platform_overview.html` | `assets/design/gold_standards/knowledge_transfer/session_0_platform_overview.html` | yes |
| 8 | 332 | `gold_standards/knowledge_transfer/charts/` | `assets/design/gold_standards/knowledge_transfer/charts/` | yes |
| 9 | 334 | `gold_standards/presentations/srinivas_status/02a_build_ecosystem_diagram.html` | `assets/design/gold_standards/presentations/srinivas_status/02a_build_ecosystem_diagram.html` | yes |
| 10 | 334 | `charts/build_log_ecosystem.html` | `assets/design/gold_standards/presentations/srinivas_status/charts/build_log_ecosystem.html` | yes |
| 11 | 343 | `gold_standards/presentations/srinivas_status/05_access_status.html` | `assets/design/gold_standards/presentations/srinivas_status/05_access_status.html` | yes |
| 12 | 373 | `.claude/skills/singularity/assets/slide_examples/` | `assets/slide_examples/` | yes |
| 13 | 373 | `.claude/skills/singularity/assets/mermaid_shape_library/` | `assets/mermaid_shape_library/` | yes |
| 14 | 373 | `assets/design/gold_standards/presentations/srinivas_status/` | `assets/design/gold_standards/presentations/srinivas_status/` | yes |
| 15 | 373 | `assets/design/gold_standards/knowledge_transfer/` | `assets/design/gold_standards/knowledge_transfer/` | yes |

## Slide Example File References (by name only, in Example Layout Patterns section)

These files are referenced by filename only (no directory path) in the layout pattern descriptions. They are expected to exist in `assets/slide_examples/`.

| # | Line | Filename Referenced | Exists in `assets/slide_examples/` |
|---|------|--------------------|------------------------------------|
| 16 | 296 | `example_title.html` | yes |
| 17 | 296 | `example_closing.html` | yes |
| 18 | 302 | `example_split_concept.html` | yes |
| 19 | 302 | `example_profile.html` | yes |
| 20 | 309 | `example_definition_bar.html` | **NO** |
| 21 | 309 | `example_two_column.html` | **NO** |
| 22 | 309 | `example_evolution_row.html` | **NO** |
| 23 | 316 | `example_three_column.html` | yes |
| 24 | 316 | `example_grid_takeaway.html` | yes |
| 25 | 323 | `example_agenda.html` | yes |

## Summary

- **15 directory/file path references:** all 15 resolve and exist on disk.
- **10 slide example filenames:** 7 exist, **3 are missing**.

### Missing Files

The following 3 example HTML files are referenced in the "Example Layout Patterns" section (line 309, under "Definition Bar + Content Area") but do not exist in `assets/slide_examples/`:

1. `example_definition_bar.html`
2. `example_two_column.html`
3. `example_evolution_row.html`

The `slide_examples/` directory currently contains 7 files:
- `example_agenda.html`
- `example_closing.html`
- `example_grid_takeaway.html`
- `example_profile.html`
- `example_split_concept.html`
- `example_three_column.html`
- `example_title.html`

### Path Inconsistency Notes

Several paths in the document use inconsistent prefixes to refer to the same locations:

- Lines 7/8/9 on the `gold_standards/` paths: some references include the `assets/design/` prefix, others start at `gold_standards/` directly (lines 332, 334, 343). Both resolve correctly because the `gold_standards/` prefix is understood to be under `assets/design/`, but the inconsistency could cause confusion for an automated reader.
- Line 334 references `charts/build_log_ecosystem.html` as a relative path from the `srinivas_status/` context. This is correct but relies on implicit context from the surrounding sentence.
