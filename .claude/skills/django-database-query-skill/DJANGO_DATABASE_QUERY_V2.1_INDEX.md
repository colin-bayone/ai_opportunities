# Django Database Query Skill v2.1 - Download Index

## 🔴 CRITICAL: v2.1 Fixes Major Bug in v2!

**If you downloaded v2, upgrade immediately!** v2 had a broken import that caused ModuleNotFoundError.

v2.1 also adds amazing sub-agent support - set up once in 30 seconds, use forever!

---

## 📥 Download All Files

### Core Documentation
- **[README.md](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/README.md)** - What's new in v2.1 + critical bug fix info
- **[SKILL.md](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/SKILL.md)** - Main instructions (v2.1 - added STEP 0 + sub-agent section)
- **[EXAMPLE_REFERENCE.md](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/EXAMPLE_REFERENCE.md)** - Sample reference file format

### Scripts Directory
- **[db_utils.py](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/scripts/db_utils.py)** - Core utility functions
- **[catalog_schema_template.py](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/scripts/catalog_schema_template.py)** - Cataloging template (v2.1 - FIXED imports! ✅)
- **[query_template.py](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/scripts/query_template.py)** - Query template

### References Directory
- **[operations_guide.md](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/references/operations_guide.md)** - Operations reference

### Examples Directory (NEW!)
- **[db-analyst.md](computer:///mnt/user-data/outputs/django-database-query-skill-v2.1/examples/db-analyst.md)** - Sub-agent template (NEW in v2.1! 🚀)

---

## 🚀 Quick Start with Sub-Agent

The **easiest way** to use this skill:

### Step 1: One-Time Setup (30 seconds)
```bash
# Copy the example agent to your project
mkdir -p .claude/agents
cp .claude/skills/django-database-query-skill/examples/db-analyst.md .claude/agents/
```

### Step 2: Use It Anytime!
```
@db-analyst find the StoredFile table in our database
```

```
@db-analyst catalog the jobdiva schema
```

```
@db-analyst analyze GET endpoint coverage
```

The sub-agent:
- ✅ Checks SQLAlchemy installation first
- ✅ Never assumes schema names
- ✅ Lists all options and asks you to choose
- ✅ Creates reference files properly
- ✅ Writes comprehensive scripts (not 10 tiny ones)

---

## 🔴 Critical Fixes in v2.1

### Bug Fixed: Import Error
**v2 Problem:**
```python
from db_utils import create_engine  # ❌ WRONG!
ImportError: cannot import name 'create_engine'
```

**v2.1 Fix:**
```python
from sqlalchemy import create_engine  # ✅ CORRECT!
```

### New: STEP 0 Pre-Flight Checks
Now enforces checking SQLAlchemy installation BEFORE running scripts.

### New: "Never Assume" Reminders
Prominent warnings throughout to prevent:
- ❌ Assuming schema is "public"
- ❌ Assuming SQLAlchemy is installed
- ❌ Assuming env file location
- ❌ Guessing table/column names

---

## 📂 Folder Structure

```
django-database-query-skill/
├── README.md (v2.1)
├── SKILL.md (v2.1 - STEP 0 + sub-agent)
├── EXAMPLE_REFERENCE.md
├── scripts/
│   ├── db_utils.py
│   ├── catalog_schema_template.py (v2.1 - FIXED!)
│   └── query_template.py
├── references/
│   └── operations_guide.md
└── examples/  (NEW!)
    └── db-analyst.md (NEW sub-agent!)
```

---

## 🔄 Upgrade Instructions

### From v2 → v2.1
**UPGRADE IMMEDIATELY!** v2 has a critical bug.

1. Download all files
2. Replace your `django-database-query-skill/` folder
3. Copy the sub-agent: `cp examples/db-analyst.md ../../.claude/agents/`

### From v1 → v2.1
**Highly recommended!**

1. Download all files
2. Replace your `django-database-query-skill/` folder
3. Set up sub-agent for best experience

**Your existing data is safe:**
- Reference files in `.claude/databases/` - unchanged
- Scratchpad scripts - still work
- Overall workflow - same, just better

---

## 📊 What Changed

| File | Status | Change |
|------|--------|--------|
| catalog_schema_template.py | 🔴 CRITICAL | Fixed create_engine import bug |
| SKILL.md | ✅ ENHANCED | Added STEP 0, sub-agent section, "Never Assume" |
| examples/db-analyst.md | ✅ NEW | Sub-agent template ready to use |
| README.md | ✅ UPDATED | Documents v2.1 changes |
| db_utils.py | ⚪ UNCHANGED | Still works perfectly |
| query_template.py | ⚪ UNCHANGED | Still works perfectly |
| operations_guide.md | ⚪ UNCHANGED | Still works perfectly |

---

## 💡 Why v2.1 is Essential

**Real-world session showed:**
1. v2 import bug caused immediate crash ❌
2. Didn't check SQLAlchemy, crashed again ❌
3. Assumed "public" schema without asking ❌
4. Wrote 5+ tiny scripts instead of 1 comprehensive one ❌

**v2.1 fixes ALL of these:**
1. Import bug fixed ✅
2. STEP 0 enforces dependency checks ✅
3. "Never Assume" reminders everywhere ✅
4. Sub-agent writes comprehensive scripts ✅

---

## 🎉 Enjoy Your Sub-Agent!

Seriously, the `@db-analyst` approach is **game-changing**. Set it up once, use it forever. No more:
- Manually running catalog scripts
- Forgetting to check dependencies
- Assuming schema names
- Writing 10 little scripts

Just: `@db-analyst do the thing` and it handles everything properly.

**Questions?** Check the README.md or SKILL.md for details!
