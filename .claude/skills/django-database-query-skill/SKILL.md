---
name: django-database-query
description: Deterministic database schema cataloging and query operations for Django projects using PostgreSQL or SQLite. Use when working with database queries, schema exploration, or when Claude needs to know exact table/column names to prevent hallucinations. Triggers include queries about database structure, errors indicating wrong column/table names (UndefinedColumn/UndefinedTable), requests to explore database schema, or any task requiring accurate database knowledge. This skill creates and maintains reference files with complete schema information to eliminate guessing.
---

# Django Database Query

## Overview

This skill provides a systematic workflow for database operations in Django projects, with emphasis on preventing hallucinations about table and column names. It creates and maintains accurate schema reference files using SQLAlchemy to inspect PostgreSQL and SQLite databases.

**Key principle:** Never guess table or column names. Always verify against actual schema.

## 🚀 Recommended: Use a Sub-Agent

**The easiest way to use this skill is through a specialized sub-agent.** Set it up once, use it forever.

### One-Time Setup (Takes 30 seconds)

**Step 1: Create the agent file**
```bash
mkdir -p .claude/agents
cp .claude/skills/django-database-query-skill/examples/db-analyst.md .claude/agents/
```

**Step 2: Use it anytime**
```
@db-analyst find the StoredFile table in our database
```

```
@db-analyst analyze GET endpoint coverage comparing database to implemented code
```

```
@db-analyst catalog the jobdiva schema
```

**Why use a sub-agent:**
- ✅ Separate context keeps main conversation clean
- ✅ Pre-configured to follow the skill's workflow
- ✅ Never assumes - always checks dependencies first
- ✅ Writes comprehensive scripts instead of many small ones
- ✅ Reusable across all your projects

**The sub-agent will:**
1. Check SQLAlchemy is installed
2. Ask which env file to use (never assumes)
3. List ALL schemas (never assumes "public")
4. Create reference files
5. Perform your requested analysis

See `examples/db-analyst.md` for the full agent definition.

### Alternative: Manual Workflow

If you prefer to run the workflow manually, continue reading below.

## When to Use This Skill

Use this skill when:
- User asks about database structure or schema
- Errors indicate wrong column/table names (e.g., `UndefinedColumn`, `UndefinedTable`)
- Starting any database query work
- User requests to explore or understand database
- Previous attempts failed due to schema assumptions

## Core Workflow

Every database operation follows this sequence:

### STEP 0: Pre-Flight Checks (DO THIS FIRST!)

**Before running ANY database operations, verify:**

**1. Check SQLAlchemy Installation**
```bash
python -c "import sqlalchemy; print(f'SQLAlchemy {sqlalchemy.__version__}')"
```

If not installed:
```bash
poetry add sqlalchemy psycopg2-binary
# or
pip install sqlalchemy psycopg2-binary --break-system-packages
```

**2. Verify Environment File Exists**
```bash
ls -la .env*
```

If multiple env files exist, ASK the user which one to use. Common patterns:
- `.env` - default
- `.env.local` - local development
- `.env.dev` - development environment
- `.env.production` - production (be careful!)

**3. Verify Database is Running** (optional but recommended)
```bash
# For PostgreSQL:
pg_isready

# For SQLite:
ls -la path/to/database.db
```

**Only proceed to Step 1 after these checks pass!**

### 🚨 Critical: NEVER ASSUME!

This skill exists to STOP assumptions about database schema. Follow these rules:

**DO NOT ASSUME:**
- ❌ Schema is "public" - LIST all schemas first, then ask user
- ❌ SQLAlchemy is installed - CHECK first (Step 0)
- ❌ Environment file location - ASK user which .env file
- ❌ Database credentials - LOAD from chosen env file
- ❌ Table names - CATALOG and verify with reference
- ❌ Column names - VERIFY against reference before queries
- ❌ Database is running - CHECK or handle connection errors gracefully

**The whole point of this skill is eliminating guesswork!**

### 1. Check SQLAlchemy (Updated from old Pre-Flight)

Before any database work:

**Check SQLAlchemy installation:**
```python
import sys
sys.path.insert(0, '/path/to/skill/scripts')
from db_utils import check_sqlalchemy

available, message = check_sqlalchemy()
print(message)
if not available:
    sys.exit(1)
```

If not installed, instruct user: `pip install sqlalchemy psycopg2-binary`

### 2. Environment File Discovery

**Never assume default database credentials.** Always identify and load the correct environment file.

**Ask user to specify environment file** or suggest based on common patterns:
- `.env`
- `.env.local`
- `.env.development`
- `.env.production`

**State what you found:**
```
Checking for database credentials...
Found: .env.local
Loading credentials from: .env.local
```

**Load and validate:**
```python
from db_utils import load_env_file, build_connection_string

env_vars = load_env_file('.env.local')
conn_str, details = build_connection_string(env_vars, 'postgresql')

if conn_str is None:
    print(f"Missing credentials: {details}")
    # Ask user for missing values
```

### 3. Connection Verification

**Before proceeding, state connection details and test connectivity:**

```
Database connection details:
  Database: my_project_db
  Host: localhost
  Port: 5432
  User: postgres
  Type: PostgreSQL
  Env file: .env.local

Testing connectivity...
```

```python
from db_utils import test_connection

success, message = test_connection(conn_str)
print(f"Connection test: {message}")
if not success:
    sys.exit(1)
```

### 4. Schema Cataloging

**Check if reference file exists and is current:**

```python
from db_utils import get_reference_age

age_days = get_reference_age(db_name, schema_name)

if age_days is None:
    print("No reference file found - will create")
elif age_days > 2:
    print(f"Reference file is {age_days:.1f} days old - refreshing")
else:
    print(f"Reference file is current ({age_days:.1f} days old)")
```

**Refresh conditions:**
- File doesn't exist
- File is >2 days old
- Error indicates column/table mismatch
- User requests refresh

**Cataloging workflow:**

1. **List available schemas:**
```python
from db_utils import get_schemas, get_tables
from sqlalchemy import create_engine

engine = create_engine(conn_str)
schemas = get_schemas(engine)

print("Available schemas:")
for schema in schemas:
    table_count = len(get_tables(engine, schema))
    print(f"  - {schema} ({table_count} tables)")
```

2. **Ask user which schema(s) to catalog** - show options and let them choose

3. **For selected schema, list all tables:**
```python
tables = get_tables(engine, selected_schema)
print(f"Found {len(tables)} tables in {selected_schema}")
```

4. **Determine detail level:**
   - If ≤30 tables: catalog all in detail
   - If >30 tables: ask user which tables to focus on, but list all in reference

5. **Create scratchpad script** for cataloging operation

### 5. Scratchpad Script Creation

**Always use scratchpad Python scripts - never execute queries directly in terminal.**

**CRITICAL: All scratchpad scripts MUST be created in the session directory, NOT in project code directories!**

**Create session directory:**
```python
from datetime import datetime
from pathlib import Path

session_dir = Path(f".claude/databases/scratchpad/session_{datetime.now().strftime('%Y-%m-%d')}")
session_dir.mkdir(parents=True, exist_ok=True)
```

## 🚨 IMPORTANT: Use the Provided Template - Don't Write From Scratch!

**DO NOT write individual scripts for each step!** We provide a complete 200+ line template that does ALL the workflow steps in one interactive script.

**The Right Way:**

**STEP 1: Copy the template**
```bash
# From project root
mkdir -p .claude/databases/scratchpad/session_2025-11-18
cp .claude/skills/django-database-query-skill/scripts/catalog_schema_template.py \
   .claude/databases/scratchpad/session_2025-11-18/db-scratchpad-catalog.py
```

**Note:** The template has pre-configured import paths that work from the session directory. The import section is already correct - don't modify it!

**STEP 2: RUN IT AS-IS (it's already interactive!)**
```bash
python .claude/databases/scratchpad/session_2025-11-18/db-scratchpad-catalog.py
```

**The template is ALREADY INTERACTIVE.** It will prompt you for everything:
- Environment file? → It asks
- Database type? → It asks  
- Which schema? → It asks
- Which tables? → It asks (or auto-catalogs all if ≤30)

**STEP 3: Only customize AFTER you've run it once and know what you need**

🚨 **DO NOT customize the template before running it!**
The template is designed to be run as-is. Run it first to see what it does, THEN customize only if you need non-interactive behavior for repeated runs.

**The template already includes:**
- ✅ SQLAlchemy installation check
- ✅ Environment file loading
- ✅ Connection string building
- ✅ Connection testing
- ✅ Schema listing
- ✅ Table cataloging with samples
- ✅ Reference file generation
- ✅ Interactive prompts for all decisions

**Only write custom scripts if:**
- You need very specific non-interactive behavior
- You're doing something NOT covered by cataloging (e.g., custom queries)
- Then use `query_template.py` as a starting point

## File Location Rules

**Full file path format:**
```
.claude/databases/scratchpad/session_YYYY-MM-DD/db-scratchpad-<purpose>.py
```

**❌ WRONG locations:**
- `jobdiva/scratchpad.py` - Don't put in project directories!
- `db-scratchpad-test.py` - Don't put in root directory!
- `scripts/db-test.py` - Don't put in scripts directory!

**✅ CORRECT locations:**
- `.claude/databases/scratchpad/session_2025-11-18/db-scratchpad-catalog.py` (copied from template)
- `.claude/databases/scratchpad/session_2025-11-18/db-scratchpad-custom-query.py` (custom use case)

**Script naming:** `db-scratchpad-<purpose>.py` where purpose is ≤15 chars

### 6. Generate and Save Reference File

The reference file follows this exact format:

```markdown
# Database: my_db (public schema)
Last updated: 2025-11-18 14:30:22

## Table List
- users (3 columns)
- orders (8 columns)

## Schema Details

TABLE: users
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 42 | 127
  email | VARCHAR(255) | UNIQUE, NOT NULL | "user@example.com" | "admin@example.com"
  created_at | TIMESTAMP | NOT NULL | "2025-01-15 10:23:45" | "2025-01-16 08:12:33"

TABLE: orders
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 5
  user_id | INTEGER | FOREIGN KEY -> users(id), NOT NULL | 42 | 127
  ...
```

**Key formatting rules:**
- Header row `[Column | Type | Constraints | Sample1 | Sample2]` is documentation, not part of table
- String samples in quotes
- JSON objects truncated to 250 chars with "..." if longer
- No "sample:" prefix before values
- Use "-" for columns with no samples

**Save location:** `.claude/databases/<db_name>/<schema>/reference.md`

Use utility functions:
```python
from db_utils import get_table_details, get_sample_values, format_reference_file, save_reference_file

# Get details for each table
tables_data = []
for table_name in tables_to_catalog:
    table_info = get_table_details(engine, table_name, schema)
    
    # Add sample values
    for col in table_info['columns']:
        samples = get_sample_values(engine, table_name, col['name'], schema, limit=2)
        col['samples'] = samples
    
    tables_data.append(table_info)

# Format and save
content = format_reference_file(db_name, schema_name, tables_data)
saved_path = save_reference_file(content, db_name, schema_name)
```

### 7. Using the Reference File for Queries

**After cataloging, you have a reference file with ALL table and column names.** Use it!

**Location:** `.claude/databases/<db_name>/<schema>/reference.md`

**Before writing ANY query:**

1. **Read the reference file to verify table/column names exist**
2. **Check the exact spelling and data types**
3. **Write your query using the verified names**

**Example workflow:**

```python
from pathlib import Path

# Load the reference
ref_path = Path('.claude/databases/my_db/public/reference.md')
with open(ref_path) as f:
    reference = f.read()

# Verify table and columns exist before querying
if 'TABLE: users' in reference and 'email |' in reference:
    # Safe to query - we know these exist
    query = text("SELECT email FROM public.users WHERE id = :user_id")
else:
    print("❌ Table or column not found in reference!")
    # Don't guess - check the reference or re-catalog
```

**Use the query template for your queries:**

We provide `scripts/query_template.py` which shows how to:
- Load and verify against the reference file
- Write clean, simple queries
- Handle verification failures gracefully

**To use it:**
```bash
# Copy template to session directory
cp .claude/skills/django-database-query-skill/scripts/query_template.py \
   .claude/databases/scratchpad/session_2025-11-18/db-scratchpad-myquery.py

# Customize the queries in the template
# Then run it
python .claude/databases/scratchpad/session_2025-11-18/db-scratchpad-myquery.py
```

**Write simple, clean scripts - don't over-engineer:**

❌ **DON'T:**
- Write separate scripts for every little step
- Use complex string replacements and edits
- Try to be too clever with abstractions

✅ **DO:**
- Write straightforward, readable scripts
- Use the templates as starting points
- Keep it simple - if something breaks, rewrite it cleanly
- One script per logical task (e.g., one for cataloging, one for analysis)

## User Communication Guidelines

**Always narrate what you're doing:**
- "Checking for SQLAlchemy installation..."
- "Loading credentials from .env.local..."
- "Testing database connectivity..."
- "Reference file is 3 days old, refreshing..."

**Ask questions when ambiguous:**
- "I see both .env and .env.local. Which should I use?"
- "Found 3 schemas. Which would you like to catalog?"
- "There are 150 tables. Should I catalog all or focus on specific ones?"

**Get approval before operations:**
- "I will now connect to my_db on localhost:5432. Proceed? [y/n]"
- "Ready to catalog 8 tables in the public schema. Continue? [y/n]"

**Never assume:**
- Don't guess database credentials
- Don't assume schema names
- Don't assume default ports/hosts
- Don't execute without showing the plan

## Error Recovery

**When encountering schema errors:**

1. **Detect the error pattern:**
```
psycopg2.errors.UndefinedColumn: column users.full_name does not exist
```

2. **Explain the issue:**
```
The query referenced column 'full_name' which doesn't exist.
This indicates our schema reference may be out of sync.
Refreshing reference file...
```

3. **Refresh reference file** following cataloging workflow

4. **Verify correct column name** from updated reference

5. **Retry operation** with correct schema

## Utility Scripts

This skill provides reusable utilities in `scripts/`:

**Python Module:**
- `db_utils.py` - Core database utility functions

**Template Scripts:**
- `catalog_schema_template.py` - Complete interactive cataloging workflow
- `query_template.py` - Template for writing queries using reference file

### db_utils.py Functions

**Core functions:**
- `check_sqlalchemy()` - Verify SQLAlchemy installation
- `load_env_file(path)` - Load environment variables
- `build_connection_string(env_vars, db_type)` - Build SQLAlchemy connection string
- `test_connection(conn_str)` - Test database connectivity
- `get_schemas(engine)` - List all schemas
- `get_tables(engine, schema)` - List tables in schema
- `get_table_details(engine, table, schema)` - Get full table metadata
- `get_sample_values(engine, table, column, schema, limit)` - Get sample column values
- `format_reference_file(db_name, schema, tables_data)` - Format reference markdown
- `save_reference_file(content, db_name, schema)` - Save reference to correct location
- `get_reference_age(db_name, schema)` - Check reference file age

### catalog_schema_template.py

Complete workflow for cataloging database schema. Includes all steps from pre-flight checks through reference file generation. Copy to session directory and run as-is.

### query_template.py

Template for writing database queries that use the cataloged reference file. Shows how to:
- Load and verify against reference file
- Write clean, simple queries
- Handle verification failures

Copy to session directory and customize for your specific queries.

## Additional References

For detailed guidance on:
- Environment variable patterns
- Scratchpad organization
- Reference file format specifics
- Common errors and solutions
- SQLAlchemy best practices

See `references/operations_guide.md`

## Critical Reminders

1. **Never execute database queries directly in terminal** - always use Python scratchpad scripts
2. **Never assume database credentials** - always ask user or load from env file
3. **Always verify connectivity** before operations
4. **Always check reference file age** before queries
5. **Always use SQLAlchemy** for database operations
6. **Keep user informed** - narrate actions, ask questions, get approvals
7. **Be deterministic** - same inputs should produce same outputs
8. **Keep scratchpad files** for debugging - organize by session date
