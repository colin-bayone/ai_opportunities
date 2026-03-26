# BayOne Design Specification

**Primary Reference:** `/specs/bayone-design-spec.md`

This skill references the master design spec located in the repository's `/specs/` directory. Always read the primary reference for the latest design guidelines.

## Quick Reference

### Brand Colors
- `--purple-darkest: #2e1065` - Cover backgrounds
- `--purple-dark: #4c1d95` - Gradient midpoint
- `--purple-mid: #5b21b6` - Table headers
- `--purple-bright: #6d28d9` - Gradient endpoint
- `--purple-accent: #a855f7` - Section numbers, accents
- `--purple-glow: #e879f9` - Cover labels, logo accent

### Typography
- Font: Inter (Google Fonts)
- Cover title: 56px, 700 weight
- Section heading (h2): 32px, 700 weight
- Body text: 15px, 400 weight

### Key Components
- `.cover` - Full-page gradient cover
- `.section-number` - Purple "01" style labels
- `.highlight-box` - Purple-bordered callouts
- `.stat-grid` / `.stat-card` - Metrics display
- `.card` - Bordered content cards

### Print Optimization
Always include `@media print` rules for 8.5" x 11" output.

---

**For complete CSS and HTML templates, read:** `/specs/bayone-design-spec.md`
