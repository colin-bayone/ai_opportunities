# Django Database Query Skill v2.1 - Critical Fixes + Sub-Agent Support

## 🔴 Critical Bug Fix in v2.1

**v2 had a critical import bug that broke the catalog template!** If you downloaded v2, please upgrade to v2.1.

**The Bug:**
```python
# v2 - BROKEN:
from db_utils import (..., create_engine)  # ❌ create_engine not in db_utils!

# v2.1 - FIXED:
from db_utils import (...)
from sqlalchemy import create_engine  # ✅ Correct!
```

## 🎉 What's New in v2.1

### 1. **Fixed Critical Import Bug** 🔴
- `catalog_schema_template.py` now correctly imports `create_engine` from `sqlalchemy`
- Template works immediately after copying - no more ModuleNotFoundError

### 2. **Sub-Agent Support (Recommended!)** 🚀
- NEW: `examples/db-analyst.md` - Ready-to-use sub-agent definition
- One-time 30-second setup, use forever
- Just `@db-analyst find the table` - that's it!
- Sub-agent follows all skill principles (never assumes, checks dependencies)

### 3. **STEP 0: Pre-Flight Checks** ✅
- Added mandatory pre-flight checklist
- Check SQLAlchemy FIRST
- Verify env file exists
- Verify database is running

### 4. **"Never Assume" Section** 🚨
- Prominent reminders throughout
- This skill exists to STOP guessing!
- No more assuming "public" schema
- No more assuming dependencies installed

## Should You Upgrade?

**From v2 → v2.1: YES, IMMEDIATELY!** 🔴
- v2 has a critical bug that breaks the template
- v2.1 fixes it plus adds awesome sub-agent support

**From v1 → v2.1: YES, HIGHLY RECOMMENDED!** 🟢
- All v2 improvements plus critical fixes
- Sub-agent approach is game-changing

## Quick Start with Sub-Agent (30 seconds)

```bash
# 1. Copy the example agent (one time only)
mkdir -p .claude/agents
cp .claude/skills/django-database-query-skill/examples/db-analyst.md .claude/agents/

# 2. Use it anytime!
```

Then in Claude Code:
```
@db-analyst find the StoredFile table
```

```
@db-analyst catalog the jobdiva schema
```

```
@db-analyst analyze database coverage
```

Done! The sub-agent handles everything - checks dependencies, lists schemas, creates references, performs analysis.

## What's Fixed from Real-World Usage

These fixes came from watching a real session crash and burn:

### Issue 1: Import Error
```
ImportError: cannot import name 'create_engine' from 'db_utils'
```
**Fixed:** create_engine now imported from sqlalchemy correctly

### Issue 2: Didn't Check SQLAlchemy
Script ran and immediately crashed with ModuleNotFoundError
**Fixed:** STEP 0 pre-flight checks + warnings in template

### Issue 3: Assumed Schema
"Let me check the public schema..." without listing options
**Fixed:** Prominent "Never Assume" reminders + sub-agent enforces it

### Issue 4: Too Many Scripts
Wrote coverage-analysis.py, then find-implemented.py, then...
**Fixed:** Sub-agent writes ONE comprehensive script

### Issue 5: Copied db_utils.py Unnecessarily
Because imports were broken, had to copy to session directory
**Fixed:** Imports work correctly now, no copying needed

## File Changes from v2

| File | Status | Change |
|------|--------|--------|
| `catalog_schema_template.py` | 🔴 **CRITICAL FIX** | Fixed create_engine import + added pre-flight warnings |
| `SKILL.md` | ✅ **ENHANCED** | Added STEP 0, sub-agent section, "Never Assume" reminders |
| `examples/db-analyst.md` | ✅ **NEW** | Ready-to-use sub-agent definition |
| `README.md` | ✅ **UPDATED** | This file - documents v2.1 changes |
| Other files | ⚪ **UNCHANGED** | db_utils.py, query_template.py, etc. |

## 📁 New File Structure (v2.1)

```
django-database-query-skill/
├── README.md (v2.1 - updated)
├── SKILL.md (v2.1 - STEP 0 + sub-agent section)
├── EXAMPLE_REFERENCE.md
├── scripts/
│   ├── db_utils.py
│   ├── catalog_schema_template.py (v2.1 - FIXED imports!)
│   └── query_template.py
├── references/
│   └── operations_guide.md
└── examples/  (NEW in v2.1!)
    └── db-analyst.md (NEW - sub-agent template)
```

## 🎯 Key Improvements

**For Import Bug:**
- Fixed critical create_engine import
- Template works immediately
- No more ModuleNotFoundError

**For Workflow:**
- STEP 0 enforces dependency checks
- "Never Assume" reminders everywhere
- Sub-agent approach prevents common mistakes

**For Sub-Agent:**
- One-time setup, infinite use
- Handles entire workflow automatically
- Pre-configured to follow all best practices

## 🔄 Upgrade from v2

If you downloaded v2 (the broken version), simply replace your skill folder with v2.1.

**What stays compatible:**
- All reference files in `.claude/databases/`
- All existing scratchpad scripts
- The overall workflow

**What improves:**
- Template actually works now!
- Sub-agent approach available
- Better guardrails against assumptions

## Quick Start

1. **Catalog your database:**
```bash
mkdir -p .claude/databases/scratchpad/session_$(date +%Y-%m-%d)
cp .claude/skills/django-database-query-skill/scripts/catalog_schema_template.py \
   .claude/databases/scratchpad/session_$(date +%Y-%m-%d)/db-scratchpad-catalog.py
python .claude/databases/scratchpad/session_$(date +%Y-%m-%d)/db-scratchpad-catalog.py
```

2. **Write queries using the reference:**
```bash
cp .claude/skills/django-database-query-skill/scripts/query_template.py \
   .claude/databases/scratchpad/session_$(date +%Y-%m-%d)/db-scratchpad-myquery.py
# Edit db-scratchpad-myquery.py to customize your queries
python .claude/databases/scratchpad/session_$(date +%Y-%m-%d)/db-scratchpad-myquery.py
```

## Files Changed from v1

- **SKILL.md**: Added Step 7, improved Section 5, better template instructions
- **catalog_schema_template.py**: Fixed import paths
- **query_template.py**: NEW - template for post-cataloging queries
- **operations_guide.md**: Added query template section and simplicity guidance
- **README.md**: NEW - this file

## Support

If you encounter issues:
1. Check that import paths in templates match your skill location
2. Verify you're creating scripts in `.claude/databases/scratchpad/session_DATE/`
3. Run templates AS-IS before customizing
4. Use reference files to verify table/column names before querying
