# Django UI/UX Comprehensive Audit Skill

**Purpose:** Systematically audit all pages, features, and functionality in a Django application with visual screenshots and detailed documentation.

---

## Skill Activation

This skill performs a comprehensive UI/UX audit of the TalentAI Django application.

**When to use:**
- After major UI changes
- Before production releases
- For Issue #430 UI/UX redesign audit
- To verify branding consistency
- To test all features work correctly

---

## Configuration

**Application Details:**
- URL: `http://localhost:8000`
- Test Credentials: `test@example.com` / `testpassword123`
- Django URLs List: `.django-workflow/issue-430-audit/all-urls.txt` (724 URLs)

**Audit Scope:**
- All accessible pages (GET requests)
- Interactive elements (buttons, links, forms)
- Feature functionality (create, delete, send, etc.)
- Console errors and network failures
- Branding consistency ("Django Base" vs "TalentAI")
- Navigation and breadcrumbs
- Mobile responsiveness

---

## Audit Workflow

### Phase 1: URL Discovery & Classification
1. Read all 724 URLs from `all-urls.txt`
2. Classify by category:
   - Authentication (`/accounts/*`)
   - Diagnostics (`/__pulsecheck__/*`, `/__debug__/*`)
   - Candidates (`/candidates/*`)
   - AI Toolkit (`/ai-toolkit/*`)
   - Email (`/email/*`)
   - Matching (`/matching/*`)
   - Roles (`/roles/*`)
   - Skills (`/skill-ontology/*`)
   - Resume Parser (`/resume-parser/*`)
   - MCQ Testing (`/screening/mcq/*`)
   - Admin (`/admin/*`)
   - API (`/api/*`)

3. Filter out:
   - API endpoints (audit separately)
   - Admin pages (audit separately)
   - Debug/diagnostic pages (skip)
   - Parameterized URLs without test data (`<int:pk>`, `<uuid:id>`)

### Phase 2: Systematic Page Audit

For each URL category, create a Playwright script that:

1. **Authenticates** with test credentials
2. **Navigates** to each URL in category
3. **Captures screenshots:**
   - Desktop (1920x1080)
   - Mobile (375x812)
   - Tablet (768x1024) - if time permits

4. **Tests interactions:**
   - Click all visible buttons
   - Click all nav links
   - Fill and submit any forms (with test data)
   - Test dropdown menus
   - Test modals/popups

5. **Checks for issues:**
   - "Django Base" branding text
   - Missing breadcrumbs
   - Broken links (404s)
   - Console errors
   - Network failures
   - Missing images
   - JavaScript errors

6. **Documents findings:**
   - Page title
   - URL and HTTP status
   - Features tested
   - Issues found
   - Screenshot filenames

### Phase 3: Feature-Specific Testing

Test key user workflows:

**Candidate Management:**
- Search for candidates
- Filter candidates
- View candidate detail
- Execute actions on candidate

**Email Management:**
- View inbox
- View sent items
- Compose email
- Send email

**Skill Ontology:**
- Browse skills
- Create skill
- Edit skill

**Resume Parser:**
- Upload resume
- View parsed data

**Role Management:**
- Create role
- View roles
- Edit role

**MCQ Testing:**
- Create test
- View tests
- Take test (if possible)

### Phase 4: Consolidation & Reporting

Generate comprehensive reports:

1. **MASTER_AUDIT_REPORT.md:**
   - Executive summary
   - Total pages audited
   - Issues by severity (P0, P1, P2)
   - Issues by category (Branding, Navigation, Functionality)
   - Working vs broken pages

2. **Category-specific reports:**
   - `CANDIDATES_AUDIT.md`
   - `EMAIL_AUDIT.md`
   - `ROLES_AUDIT.md`
   - `SKILLS_AUDIT.md`
   - `RESUME_PARSER_AUDIT.md`
   - etc.

3. **audit-data.json:**
   - Structured data for analysis
   - All URLs tested
   - All issues found
   - All screenshots captured

4. **screenshots/** directory structure:
   ```
   screenshots/
   ├── candidates/
   ├── email/
   ├── roles/
   ├── skills/
   ├── resume-parser/
   └── mcq-testing/
   ```

---

## Execution Instructions

### Step 1: Prepare Environment

Ensure Django server is running:
```bash
./run.sh local
```

Ensure Playwright is available:
```bash
python3 -c "import playwright; print('OK')"
```

### Step 2: Create Audit Scripts

For each major category, create a focused Playwright audit script:

**Template:**
```python
#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import os

CATEGORY = "candidates"  # or email, roles, etc.
SCREENSHOT_DIR = f".django-workflow/issue-430-audit/screenshots/{CATEGORY}"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def login(page):
    page.goto('http://localhost:8000/accounts/login/')
    page.fill('input[name="login"]', 'test@example.com')
    page.fill('input[type="password"]', 'testpassword123')
    page.click('button:has-text("Sign In")')
    page.wait_for_load_state('networkidle')
    if 'Django Debug Toolbar' in page.title():
        page.locator('a#redirect_to').click()
        page.wait_for_load_state('networkidle')

def audit_page(page, url, name):
    # Visit page
    # Take screenshots
    # Click buttons
    # Check for issues
    # Document findings
    pass

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login(page)

        # Audit all pages in category
        # ...

        browser.close()

if __name__ == "__main__":
    main()
```

### Step 3: Run Category Audits

Run audits in sequence or parallel:

```bash
# Sequential (safer)
python3 audit_candidates.py
python3 audit_email.py
python3 audit_roles.py
# etc.

# Or parallel (faster but more resource intensive)
python3 audit_candidates.py &
python3 audit_email.py &
python3 audit_roles.py &
wait
```

### Step 4: Generate Reports

Create consolidation script that:
- Reads all audit JSON files
- Merges findings
- Generates master report
- Creates issue summaries

---

## Output Structure

```
.django-workflow/issue-430-audit/
├── all-urls.txt                      # 724 URLs from Django
├── MASTER_AUDIT_REPORT.md            # Executive summary
├── CANDIDATES_AUDIT.md               # Category reports
├── EMAIL_AUDIT.md
├── ROLES_AUDIT.md
├── SKILLS_AUDIT.md
├── RESUME_PARSER_AUDIT.md
├── MCQ_TESTING_AUDIT.md
├── audit-data.json                   # All findings as JSON
├── screenshots/
│   ├── candidates/
│   │   ├── search-desktop.png
│   │   ├── search-mobile.png
│   │   ├── detail-desktop.png
│   │   └── ...
│   ├── email/
│   ├── roles/
│   └── ...
└── scripts/
    ├── audit_candidates.py
    ├── audit_email.py
    └── ...
```

---

## Success Criteria

**Audit is complete when:**
- ✅ All non-API, non-admin URLs visited
- ✅ Screenshots captured for all working pages
- ✅ All interactive elements tested
- ✅ All issues documented with severity
- ✅ Master report generated
- ✅ Category reports generated
- ✅ JSON data exported

**Quality checks:**
- Every working page has 2+ screenshots (desktop + mobile)
- Every issue has page URL and screenshot reference
- Console errors are logged
- Branding issues are flagged
- Navigation issues are documented

---

## Known Limitations

1. **Parameterized URLs:** URLs like `/candidates/<int:pk>/` need test data
2. **Authentication walls:** Some pages may require specific permissions
3. **Dynamic content:** Content loaded via AJAX may not be captured
4. **External services:** Features requiring external APIs may fail
5. **Time constraints:** Full audit of 724 URLs may take 30-60 minutes

---

## Post-Audit Actions

After audit completion:

1. **Review master report** - Understand scope of issues
2. **Prioritize issues** - P0 critical, P1 high, P2 medium
3. **Create sub-issues** - Under umbrella issues #479, #480, #481, #484
4. **Share findings** - With team for review
5. **Plan fixes** - Create implementation roadmap

---

## Maintenance

This skill should be re-run:
- After fixing major branding issues
- After navigation refactoring
- Before major releases
- When new features are added
- As part of QA process

---

**Last Updated:** November 24, 2025
**Issue:** #430 - Overall UI/UX Redesign and Rebranding
