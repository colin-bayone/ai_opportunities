# SOW Document Session Handoff - Comprehensive Context

**Date:** February 16, 2026
**Handoff from:** Session 3 (current)
**Reason:** Session became unreliable; file mysteriously disappeared during editing

---

## Part 1: Business Context and Purpose

### Who We Are
**BayOne Solutions** is a consulting firm engaged with Cisco on their NX-OS CI/CD pipeline improvement project.

**Key BayOne People:**
- **Colin Moore** - Director of AI, technical lead for this engagement
- **Rahul** - President
- **Amit** - Delivery
- **Zahra** - Sales

**Key Cisco People:**
- **Arun** - VP
- **Srini/Srinivas** - Senior Engineering Manager
- **Anand** - Director
- **Divakar/Diwakar** - Engineering Lead

### The Bigger Picture
BayOne is positioning itself as more than just a staffing firm - we provide strategic consulting, AI-driven solutions, and methodology expertise. This SOW work is part of demonstrating that capability.

### Why We're Doing This SOW Work
**Goal:** Create a standardized, professional, reusable SOW template for BayOne Solutions.

**The workflow we're building:**
1. Start with an existing client SOW (in this case, a Cisco SOW PDF)
2. Convert it to structured HTML with professional styling
3. Improve the visual presentation and consistency
4. Create a "golden" working version that prints correctly
5. **NEXT STEP:** Template it so it becomes a reusable workflow for generating future SOWs

This is similar to the pattern we used for the Cisco capabilities deck (`claude/2026-02-10_capabilities_deck/slides/`) and the Sephora proposal (`sephora/deliverables/01_ai_acceleration_proposal.html`). BayOne has a design system (`specs/bayone-design-spec.md`) that we follow for all client-facing materials.

---

## Part 2: What We Started With

### Source Document
- **Original PDF:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building Nexus 9000 (switches).pdf`
- **Reference ID:** 33282
- **Title:** FY26Q3_Building Nexus 9000 (switches) product line _Bayone
- **Budget:** Rs 4,393,740.00 INR
- **Timeline:** 11/5/2025 - 4/30/2026
- **Prepared by:** Mahaveer Jinka (Cisco)
- **Vendor Contact:** Ashish Singh (BayOne)

### Document Structure (12 pages)
1. Cover page with Cisco logo
2. General Information (currency, budget, location, timeline, owner, vendor info)
3. Section 1: General Information (legal terms)
4. Section 2: Services and Work Product (objectives, SLAs, deliverables, acceptance, resources, personnel, place of performance)
5. Section 3: Payment
6. Financials (Fixed Bid with 6 monthly milestones - Nov 2025 through Apr 2026)
7. Totals summary
8. Signature blocks (Owner and Vendor)

Each page has a footer with "Confidential" and "Page X of 12".

---

## Part 3: The Conversion Workflow

### Phase 1: PDF to Markdown (Session 2)
- Extracted all text content from the PDF
- Preserved document structure, tables, lists
- Created: `SOW-Building-Nexus-9000-switches.md`
- Verified fidelity against original PDF

### Phase 2: Markdown to HTML v1 (Session 2)
- Applied Cisco styling (Cisco blue `#049fd9`, Times New Roman font)
- Created page containers with footers
- Added Cisco logo (PNG with SVG fallback)
- Print-optimized for 8.5" x 11"
- Created: `SOW-Building-Nexus-9000-switches.html` (original v1, now renamed to `-old`)

### Phase 3: HTML v2 Improvements (Session 2)

**Round 1 - 6 Improvements:**
1. Footer styling refinements
2. Table formatting consistency
3. Field label alignment
4. Section header styling
5. Margin adjustments
6. Print CSS foundation

**Round 2 - 10 Improvements:**
1. Simplified footer (removed center title, kept Confidential + Page X of 12)
2. Indentation for section content (0.25in margin)
3. Field labels bold with proper min-width
4. Table headers with background color (`#f0f4f8`)
5. SLA table padding improvements
6. Line height adjustments (1.5)
7. Section separators (subtle top border on h3)
8. Signature block restructured as table
9. Cover page with PNG Cisco logo
10. Instruction text styling (yellow background, gold left border)

**Round 3 - Started but hit print issues:**
- Fixed inconsistent bullets (some milestones used `-` instead of `<ul><li>`)
- Attempted to prevent table splitting
- Attempted to keep headers with content
- **THIS IS WHERE PRINT PROBLEMS EMERGED**

### Phase 4: Print Problem Discovery and Solution (Session 3)

**The Problem:**
When printing to PDF via browser, footers appeared mid-content instead of at page bottoms. The CSS `position: absolute` footer positioned relative to `.page` div containers, but browser print reflows content and breaks pages wherever needed - completely ignoring the `.page` boundaries.

**What We Tried (and failed):**
- Changing border colors
- Fixed page heights in inches (`height: 9.25in`)
- Various `page-break-*` CSS rules
- Different positioning approaches

**The Solution:**
User discovered that Playwright's `displayHeaderFooter` feature operates at the PDF generation layer, not the CSS layer. This is the correct abstraction level.

**Created:** `html_to_pdf_playwright.py` - a Python utility that:
- Loads HTML in headless Chromium
- Injects CSS to hide HTML-based `.page-footer` elements
- Lets content flow naturally (no forced page heights)
- Uses Playwright's footer_template with special classes (`.pageNumber`, `.totalPages`)
- Generates PDF with proper footers on every physical page

### Phase 5: Final Fixes (Session 3)
- Fixed signature line underlines (border-bottom with `!important`)
- Fixed spacing below signature lines (padding-top on `.info-label`)
- Fixed logo path after browser recovery
- Renamed v3 to main version

---

## Part 4: Current State - The "Golden" Working Version

### Primary Files (USE THESE)
```
/home/cmoore/programming/cisco_projects/cicd/SOW/
├── SOW-Building-Nexus-9000-switches.html     # GOLDEN HTML VERSION
├── SOW-Building-Nexus-9000-switches.pdf      # GOLDEN PDF VERSION
```

### Key Utility
```
├── html_to_pdf_playwright.py                 # PDF converter with proper footers
├── html_to_pdf_playwright_README.md          # Documentation for the utility
```

### Prototype for Future
```
├── SOW-toc-prototype.html                    # Table of contents prototype (not integrated yet)
```

### Old/Backup Files
```
├── SOW-Building-Nexus-9000-switches-old.html # Original v1
├── SOW-Building-Nexus-9000-switches-v2.html  # Intermediate version
├── recover/                                  # Browser-saved recovery files from incident
```

### Supporting Files
```
├── SOW-Building-Nexus-9000-switches.md       # Markdown source
├── SOW-conversion-notes.md                   # Conversion notes
├── screenshots/                              # Playwright screenshots from verification
```

---

## Part 5: How to Generate PDFs

### Using the Playwright Utility
```bash
cd /home/cmoore/programming/cisco_projects/cicd/SOW

# Basic conversion (default: "Confidential" left, "Page X of Y" right)
python3 html_to_pdf_playwright.py SOW-Building-Nexus-9000-switches.html SOW-Building-Nexus-9000-switches.pdf

# Custom footer text
python3 html_to_pdf_playwright.py input.html output.pdf --footer-left "Draft" --footer-right "Page {page}"

# No footer
python3 html_to_pdf_playwright.py input.html output.pdf --no-footer

# Custom margins
python3 html_to_pdf_playwright.py input.html output.pdf --margin-bottom 1.5in
```

### Prerequisites
```bash
pip install playwright
playwright install chromium
```

### How It Works
1. Hides HTML `.page-footer` elements (they don't work in print)
2. Lets content flow naturally with `page-break-inside: avoid` on tables/signatures
3. Forces cover page to its own page with `page-break-after: always`
4. Injects Playwright footer template on every physical page

---

## Part 6: CSS Details in Current HTML

### Signature Table Styling (the fix that took multiple attempts)
```css
.signature-table .sig-line {
    border-bottom: 1px solid black !important;
    min-width: 200px;
}

.signature-table .date-line {
    border-bottom: 1px solid black !important;
    width: 120px;
}

.signature-table .info-label {
    width: 130px;
    padding-top: 10px !important;  /* Creates space between signature line and Title/Name rows */
}
```

### Key CSS Variables
```css
:root {
    --cisco-blue: #049fd9;
    --cisco-dark-blue: #005073;
    --text-color: #333333;
    --border-color: #000000;
    --light-gray: #f5f5f5;
}
```

### Table Border Approach (not individual cell borders - causes 3D effect)
```css
table {
    border: 1px solid var(--border-color);
}
table th, table td {
    border-bottom: 1px solid var(--border-color);
}
table tr:last-child td {
    border-bottom: none;
}
```

---

## Part 7: Next Steps - Templating

**The goal after this handoff:**
Turn the golden version into a reusable template workflow.

### What Needs to be Templated
1. **Header/Cover Page**
   - Client logo (currently Cisco)
   - Document title
   - Reference ID
   - Prepared by

2. **General Information Section**
   - Currency
   - Budget amount
   - Work location
   - Tax category
   - Timeline dates
   - Owner/Cost Center
   - Service Category
   - Vendor info

3. **Milestones/Financials**
   - Variable number of milestones
   - Each with: Name, Type, Dates, Amounts, Description, Acceptance Criteria, BAN

4. **Totals Section**
   - Calculated from milestones

5. **Signature Block**
   - Owner name/title
   - Vendor name/title

### The Workflow (Clarified by User)

**This is NOT a fully automated script.** It is an agentic workflow that requires Claude Code to interpret documents and make judgment calls.

**User provides:** Source documents (PDFs, emails, whatever the client sends)

**Claude Code does:**
1. Reads/analyzes the source documents
2. Extracts relevant fields into structured format (YAML)
3. Reviews/refines with user as needed
4. Generates HTML from template + YAML
5. Converts to PDF via Playwright utility

**Why it can't be fully automated:** The extraction and field population requires language model judgment - reading messy client docs, interpreting content, making decisions about what goes where.

**Implementation approach:**
- Wrap this as a Claude Code skill
- YAML is an intermediary format (generated by Claude, not manually written by user)
- Use the existing golden SOW to create a sample YAML schema (all fields are filled out)
- Create a template version of the HTML with placeholders
- Build a render script (YAML + template → HTML)

**Starting point for next session:**
1. Extract a sample YAML from the current SOW to define the schema
2. Create a template version of the HTML with placeholders
3. Build render script
4. Wrap in a skill

---

## Part 8: Related Work and References

### BayOne Design System
- **Spec file:** `/home/cmoore/programming/cisco_projects/cicd/specs/bayone-design-spec.md`
- Purple gradient brand palette (#2e1065 to #6d28d9)
- Inter font family
- Numbered sections (01, 02, 03...)
- No emojis
- Print-optimized for 8.5" x 11"

### Similar Deliverables Created
- **Cisco Capabilities Deck:** `claude/2026-02-10_capabilities_deck/slides/`
- **Sephora Proposal:** `sephora/deliverables/01_ai_acceleration_proposal.html`
- **Resource Plan:** `claude/2026-02-02_resource-planning/deliverables/resource_plan_for_cisco.html` (this file shows good print patterns)

### Skills Created
- **sales-forge:** `.claude/skills/sales-forge/` - For generating proposals and pitch decks
- Uses similar HTML-to-PDF workflow with Playwright

---

## Part 9: Session Transcripts

### Session 1 (Feb 13)
**File:** `/home/cmoore/programming/cisco_projects/cicd/2026-02-13-we-just-got-done-doing-a-really-great-slide-deck-a_SKILL_213PM_cleaned.txt`

**Content:** Mostly Sephora engagement work, but established:
- BayOne design spec patterns
- HTML document generation workflow
- Created sales-forge skill
- Playwright PDF conversion approach

### Session 2 (Feb 13, continued)
**Referenced in:** Context summary at start of Session 3

**Content:**
- PDF to Markdown conversion
- Markdown to HTML v1
- HTML v2 with Round 1 and Round 2 improvements
- Started Round 3 (print issues emerged)

### Session 3 (Feb 16 - Current)
**File:** `/home/cmoore/programming/cisco_projects/cicd/2026-02-16-this-session-is-being-continued-from-a-previous-co_givingup_1049AM.txt`

**Content:**
- Attempted CSS fixes for print (all failed)
- User discovered Playwright solution
- Created `html_to_pdf_playwright.py`
- Fixed signature lines and spacing
- File disappearance incident and recovery
- Created TOC prototype
- This handoff document

---

## Part 10: Critical Lessons Learned

### Technical
1. **CSS `position: absolute` does not work for print footers** - It positions relative to containing elements, not physical pages
2. **Browser print reflows content** - Your `.page` div boundaries are meaningless to the print engine
3. **Use Playwright for PDF generation** - Its `displayHeaderFooter` operates at the right abstraction level
4. **Don't use inches in CSS for print** - It's unreliable and doesn't account for browser differences

### Process
1. **Always ask before making changes** - User prefers explicit approval
2. **Don't hide content without permission** - Footer hiding caused frustration
3. **Don't rename/move files without permission** - File disappeared during this session
4. **Keep backups** - The v2 backup saved us when v3 disappeared
5. **Browser "Save As" can recover work** - User saved v3 from browser when file disappeared

---

## Part 11: Project Structure Reference

```
/home/cmoore/programming/cisco_projects/cicd/
├── CLAUDE.md                    # Project instructions (READ THIS)
├── SOW/                         # SOW document work (THIS PROJECT)
│   ├── SOW-Building-Nexus-9000-switches.html    # GOLDEN VERSION
│   ├── SOW-Building-Nexus-9000-switches.pdf     # GOLDEN VERSION
│   ├── html_to_pdf_playwright.py                # PDF utility
│   └── ...
├── specs/
│   └── bayone-design-spec.md    # BayOne design system
├── claude/
│   ├── 2026-02-10_capabilities_deck/   # Cisco capabilities deck
│   └── 2026-02-02_resource-planning/   # Resource planning docs
├── sephora/                     # Sephora engagement (separate project)
├── project/                     # Current state documents
└── history/                     # Numbered changelog
```

---

## Part 12: For the Next Session

### Immediate Priority
1. Read this handoff document
2. Read `CLAUDE.md` for project instructions
3. Verify the golden HTML/PDF still look correct
4. Discuss templating approach with user

### Do NOT
- Make changes without explicit approval
- Use inches in CSS
- Try to fix print footers with CSS (use Playwright)
- Delete or rename files without permission

### The User's Working Style
- Prefers approval before edits
- Wants visibility into what's changing
- Gets frustrated when AI makes assumptions
- Values incremental, verified progress over speed
