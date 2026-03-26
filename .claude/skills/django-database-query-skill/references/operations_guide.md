# Database Operations Reference

This reference provides detailed guidance on database operations workflows and best practices.

## Environment File Detection

When working with database operations, always start by identifying the correct environment file:

### Common Environment File Locations
- `.env`
- `.env.local`
- `.env.development`
- `.env.production`
- `config/.env`

### Environment Variable Naming Conventions

**PostgreSQL:**
- `DATABASE_URL` - Full connection string (preferred)
- `DB_NAME` or `POSTGRES_DB` - Database name
- `DB_USER` or `POSTGRES_USER` - Username
- `DB_PASSWORD` or `POSTGRES_PASSWORD` - Password
- `DB_HOST` or `POSTGRES_HOST` - Hostname
- `DB_PORT` or `POSTGRES_PORT` - Port (default: 5432)

**SQLite:**
- `DB_PATH` or `SQLITE_DB` - Path to SQLite database file

### Never Assume Defaults

Do NOT assume default values for database credentials. If environment variables are missing:
1. Ask the user to specify the correct values
2. List what's missing
3. Only suggest defaults if NO environment file is present

## Scratchpad Organization

All database scratchpad scripts should be organized by session:

```
.claude/databases/scratchpad/
└── session_2025-11-18/
    ├── db-scratchpad-connectivity.py
    ├── db-scratchpad-list-schemas.py
    └── db-scratchpad-catalog-public.py
```

### Scratchpad Naming Convention
Format: `db-scratchpad-<purpose>.py`

Purpose should be:
- Lowercase
- Hyphen-separated
- 15 characters or less
- Descriptive of operation

Examples:
- `db-scratchpad-test-conn.py`
- `db-scratchpad-list-tables.py`
- `db-scratchpad-get-users.py`

## Reference File Format

Reference files are stored at:
```
.claude/databases/<db_name>/<schema>/reference.md
```

### Format Structure

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
```

### Constraints to Capture
- PRIMARY KEY
- FOREIGN KEY -> table(column)
- UNIQUE
- NOT NULL
- CHECK constraints (if present)
- DEFAULT values (if present)

### Sample Value Handling
- Capture 2 sample values per column
- For strings: wrap in quotes
- For JSON objects: truncate to 250 chars if longer, append "..."
- For NULL columns: use "-"
- Show actual values, not "sample:" prefix

## Reference File Refresh Logic

Reference files should be refreshed when:

1. **File doesn't exist** - Always generate
2. **File is older than 2 days** - Auto-refresh
3. **Column/table error detected** - Refresh to sync with actual schema
4. **User explicitly requests** - Refresh on demand
5. **Claude determines it's needed** - If detecting potential schema mismatch

### Detecting Schema Mismatches

Watch for these error patterns:
```
psycopg2.errors.UndefinedColumn: column <name> does not exist
psycopg2.errors.UndefinedTable: relation "<table>" does not exist
```

When detected, immediately refresh the reference file before retrying.

## Schema Selection Workflow

For databases with multiple schemas:

1. **List all available schemas** with table counts:
   ```
   1. public (25 tables)
   2. auth (8 tables)
   3. analytics (42 tables)
   ```

2. **Ask user which schema(s) to catalog**
   - Allow multiple selections
   - Let user explore before deciding
   - Show context to help them choose

3. **For large schemas (>30 tables)**
   - List all tables in reference file
   - Ask which specific tables to detail
   - Only fetch column info for selected tables

## SQLAlchemy Best Practices

### Connection Management
Always use context managers:
```python
with engine.connect() as conn:
    result = conn.execute(text("SELECT ..."))
```

### Parameterized Queries
Always use parameterized queries to prevent SQL injection:
```python
query = text("SELECT * FROM users WHERE id = :user_id")
result = conn.execute(query, {"user_id": 42})
```

### Schema Handling
For PostgreSQL, always specify schema when not using default:
```python
inspector.get_tables(schema='my_schema')
```

For SQLite, schema is None:
```python
inspector.get_tables(schema=None)
```

## Error Handling

Common errors and solutions:

### Connection Refused
- Check if database server is running
- Verify hostname and port
- Check firewall rules

### Authentication Failed
- Verify username and password
- Check user permissions
- Ensure database exists

### Module Not Found
- Install required packages: `pip install sqlalchemy psycopg2-binary`
- For SQLite: SQLAlchemy is sufficient

### UndefinedColumn/UndefinedTable
- Refresh reference file
- Verify schema name
- Check table/column spelling

## Workflow Checklist

Before any database operation:

- [ ] SQLAlchemy is installed
- [ ] Environment file is identified and loaded
- [ ] Connection details are stated clearly
- [ ] Connectivity is tested successfully
- [ ] Reference file exists and is up-to-date
- [ ] User has approved the operation plan

## Using the Query Template

After cataloging your schema, use `query_template.py` for writing queries:

**Copy and customize:**
```bash
cp .claude/skills/django-database-query-skill/scripts/query_template.py \
   .claude/databases/scratchpad/session_2025-11-18/db-scratchpad-myquery.py
```

**The template shows how to:**
1. Load the reference file
2. Verify tables and columns exist before querying
3. Handle verification failures gracefully
4. Write clean, simple queries

**Key principle:** Always verify against the reference before writing queries!

## Writing Simple, Clean Scripts

**DO:**
- ✅ Write straightforward, readable code
- ✅ Use the templates as starting points
- ✅ One script per logical task
- ✅ If something breaks, rewrite it cleanly
- ✅ Comment your queries to explain what they do

**DON'T:**
- ❌ Write separate scripts for every tiny step
- ❌ Use complex string replacements and edits  
- ❌ Over-engineer with abstractions
- ❌ Try to patch broken code repeatedly - rewrite it
- ❌ Assume column names - always verify

**Example of keeping it simple:**
```python
# Good: Clear, readable, verifies before querying
with open(ref_path) as f:
    ref = f.read()

if 'TABLE: users' in ref and 'email |' in ref:
    result = conn.execute(text("""
        SELECT email, created_at 
        FROM users 
        WHERE id = :user_id
    """), {"user_id": 42})
```

```python
# Bad: Over-complicated, fragile
class QueryBuilder:
    def __init__(self, ref_loader, validator, executor):
        self.ref = ref_loader.load()
        self.validator = validator
        # ... 50 more lines of abstraction
```
