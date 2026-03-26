# Wave 5 Agent 3: BayOne Design Specification
**Source:** Codebase - specs/bayone-design-spec.md
**Focus:** Brand guidelines and document formatting requirements
**Extracted:** 2026-03-04

---

# BAYONE DESIGN SPECIFICATION - COMPLETE EXTRACTION

## BRAND COLOR PALETTE (Mandatory)

### Primary Purple Gradient
- `#2e1065` - Deep purple (cover backgrounds, summary tables)
- `#4c1d95` - Rich purple (gradient midpoint)
- `#5b21b6` - Solid purple (table headers, badges)
- `#6d28d9` - Vibrant purple (gradient endpoint)
- `#a855f7` - Light purple (section numbers, accents)
- `#e879f9` - Magenta/pink (cover labels, logo accent)

### Neutral Colors
- `#0f172a` - Near-black (headings, strong text)
- `#334155` - Dark gray (body text)
- `#64748b` - Medium gray (secondary text, labels)
- `#e2e8f0` - Light gray (borders, dividers)
- `#f8fafc` - Off-white (alternating rows, subtle backgrounds)
- `#ffffff` - White

### Gradient Specifications
- **Cover/Hero:** `linear-gradient(135deg, #2e1065 0%, #4c1d95 50%, #6d28d9 100%)`
- **Subtle Purple Tint:** `linear-gradient(135deg, rgba(124,58,237,0.05) 0%, rgba(168,85,247,0.08) 100%)`
- **Icon/Badge:** `linear-gradient(135deg, #7c3aed, #a855f7)`

---

## TYPOGRAPHY SYSTEM

### Font Stack (Mandatory)
- **Primary:** `'Inter', -apple-system, BlinkMacSystemFont, sans-serif`
- **Import:** Google Fonts: `https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap`

### Type Scale

| Element | Size | Weight | Color | Line Height |
|---------|------|--------|-------|-------------|
| Cover Title | 56px | 700 | white | 1.1 |
| Cover Subtitle | 22px | 300 | white (80%) | 1.4 |
| Section Heading (h2) | 32px | 700 | #0f172a | 1.2 |
| Subsection Heading (h3) | 20px | 600 | #0f172a | 1.3 |
| Lead Paragraph | 18px | 400 | #64748b | 1.8 |
| Body Text | 15px | 400 | #334155 | 1.7 |
| Table Text | 14px | 400 | #334155 | 1.5 |
| Table Header | 12px | 600 | white | 1.4 |
| Section Number | 12px | 600 | #a855f7 | 1.2 |

---

## SPACING SYSTEM (8px Grid)

| Token | Value | Usage |
|-------|-------|-------|
| xs | 8px | Tight spacing, inline gaps |
| sm | 12px | Between related items |
| md | 16px | Paragraph margins |
| lg | 24px | Section padding, card padding |
| xl | 32px | Between sections |
| 2xl | 48px | Major section breaks |
| 3xl | 64px | Container padding, section margins |
| 4xl | 80px | Cover page padding |

---

## DOCUMENT STRUCTURE (Standard)

1. **Cover Page** - Full viewport, deep purple gradient
2. **Table of Contents** (optional for longer docs)
3. **Executive Summary / Overview**
4. **Body Sections** - Numbered (01, 02, 03...)
5. **Summary** - Final table or recap
6. **Footer** - Logo and confidentiality note

---

## COMPONENT SPECIFICATIONS

### Cover Page
- Min-height: 100vh
- Padding: 80px
- Background: Full purple gradient (135deg)
- Logo positioned absolute bottom-right at 80px, 80px
- "One" in BayOne logo colored `#e879f9`

### Tables
- Header background: `#5b21b6` (solid purple)
- Header text: white, uppercase, 12px, 600 weight
- Cell padding: 14px 16px
- Border-collapse: collapse
- Alternating row background: `#f8fafc`
- Rounded top corners: 8px

### Highlight Box (Callouts)
- Background: Subtle purple gradient
- Border-left: 4px solid `#a855f7`
- Padding: 24px 28px
- Border-radius: 0 8px 8px 0

### Cards
- Background: white
- Border: 1px solid `rgba(124,58,237,0.15)`
- Border-radius: 12px
- Padding: 28px

### Stat Cards
- Background: `linear-gradient(135deg, rgba(124,58,237,0.06) 0%, rgba(168,85,247,0.04) 100%)`
- Stat value: 36px, 700 weight, `#7c3aed`
- Stat label: 13px, 500 weight, `#64748b`

---

## FORMATTING RULES

### DO's
- Use numbered section labels (01, 02, 03...) - MANDATORY
- Use ample whitespace between sections
- Keep tables clean with rounded top corners
- Use subtle purple tints for backgrounds
- Lead each major section with brief overview paragraph
- Use highlight boxes sparingly for key points
- Preserve colors in print output

### DON'Ts
- Do NOT use bullet points in prose - write in natural paragraphs
- Do NOT use emojis
- Do NOT use excessive bold text
- Do NOT use multiple colors beyond purple palette
- Do NOT use busy patterns or textures
- Do NOT overuse gradients

---

## WRITING STYLE

- Confident but not arrogant
- Clear and direct
- Professional without being stiff
- Avoid jargon unless speaking to technical audience

---

## PRINT OPTIMIZATION

- Page size: 8.5in x 11in
- Margin: 0.4in
- `-webkit-print-color-adjust: exact`
- `print-color-adjust: exact`
- Headers must have `break-after: avoid`
- Tables must have `break-inside: avoid`

---

**Full extraction:** 150+ lines with complete design specifications
