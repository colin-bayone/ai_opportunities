"""
Template script for cataloging database schema.
Copy this to .claude/databases/scratchpad/session_<date>/ and run it.

⚠️ BEFORE RUNNING THIS SCRIPT:
1. Check SQLAlchemy is installed: python -c "import sqlalchemy; print(f'SQLAlchemy {sqlalchemy.__version__}')"
   If not: poetry add sqlalchemy psycopg2-binary (or pip install)
2. Verify env file exists: ls -la .env*
3. Verify database is running (e.g., pg_isready for PostgreSQL)

DO NOT modify the import section unless you know what you're doing!
The imports are pre-configured to work from the session directory location.
"""
import sys
from pathlib import Path

# Import utilities from skill scripts directory
# Script location: .claude/databases/scratchpad/session_DATE/db-scratchpad-catalog.py
# Skill location:  .claude/skills/django-database-query-skill/scripts/db_utils.py
skill_scripts = Path(__file__).resolve().parents[4] / '.claude/skills/django-database-query-skill/scripts'
sys.path.insert(0, str(skill_scripts))

from db_utils import (
    check_sqlalchemy, load_env_file, build_connection_string,
    test_connection, get_schemas, get_tables, get_table_details,
    get_sample_values, format_reference_file, save_reference_file
)
from sqlalchemy import create_engine


def main():
    """Main cataloging workflow."""
    
    # Step 1: Check SQLAlchemy
    print("=" * 70)
    print("STEP 1: Checking SQLAlchemy installation")
    print("=" * 70)
    available, message = check_sqlalchemy()
    print(f"Status: {message}")
    if not available:
        sys.exit(1)
    print()
    
    # Step 2: Load environment file
    print("=" * 70)
    print("STEP 2: Loading database credentials")
    print("=" * 70)
    env_file = input("Enter path to env file (e.g., .env, .env.local): ").strip()
    
    if not Path(env_file).exists():
        print(f"❌ Error: Environment file '{env_file}' not found")
        sys.exit(1)
    
    env_vars = load_env_file(env_file)
    print(f"✓ Loaded {len(env_vars)} variables from {env_file}")
    print()
    
    # Step 3: Build connection string
    print("=" * 70)
    print("STEP 3: Building connection string")
    print("=" * 70)
    db_type = input("Database type (postgresql/sqlite) [postgresql]: ").strip() or "postgresql"
    
    conn_str, details = build_connection_string(env_vars, db_type)
    
    if conn_str is None:
        print(f"❌ Error: {details.get('error', 'Unknown error')}")
        print(f"Details: {details}")
        sys.exit(1)
    
    print("Connection details:")
    for key, value in details.items():
        if key not in ['password']:  # Don't print password
            print(f"  {key}: {value}")
    print()
    
    # Step 4: Test connection
    print("=" * 70)
    print("STEP 4: Testing database connectivity")
    print("=" * 70)
    success, message = test_connection(conn_str)
    print(f"Status: {message}")
    if not success:
        sys.exit(1)
    print()
    
    # Step 5: Create engine
    engine = create_engine(conn_str)
    
    # Step 6: List schemas
    print("=" * 70)
    print("STEP 5: Listing available schemas")
    print("=" * 70)
    try:
        schemas = get_schemas(engine)
        print(f"Found {len(schemas)} schemas:")
        for i, schema in enumerate(schemas, 1):
            print(f"  {i}. {schema}")
        print()
    except Exception as e:
        print(f"❌ Error listing schemas: {e}")
        # For SQLite, there's no schema concept
        if db_type == 'sqlite':
            schemas = [None]
            print("SQLite database - no schema concept, proceeding with main database")
        else:
            sys.exit(1)
    
    # Step 7: Select schema
    print("=" * 70)
    print("STEP 6: Selecting schema to catalog")
    print("=" * 70)
    
    if db_type == 'sqlite':
        selected_schema = None
        schema_name = "main"
    else:
        schema_input = input("Enter schema name to catalog (or 'list' to see all): ").strip()
        
        if schema_input.lower() == 'list':
            for schema in schemas:
                tables = get_tables(engine, schema)
                print(f"  {schema}: {len(tables)} tables")
            schema_input = input("Enter schema name to catalog: ").strip()
        
        selected_schema = schema_input
        schema_name = schema_input
    
    print(f"Selected schema: {schema_name}")
    print()
    
    # Step 8: Get tables
    print("=" * 70)
    print("STEP 7: Listing tables in schema")
    print("=" * 70)
    tables = get_tables(engine, selected_schema)
    print(f"Found {len(tables)} tables:")
    for i, table in enumerate(tables, 1):
        print(f"  {i}. {table}")
    print()
    
    # Step 9: Decide which tables to detail
    print("=" * 70)
    print("STEP 8: Determining tables to catalog in detail")
    print("=" * 70)
    
    if len(tables) <= 30:
        print(f"≤30 tables detected - will catalog all tables in detail")
        tables_to_detail = tables
    else:
        print(f">30 tables detected - asking user which tables to focus on")
        focus_input = input("Enter table names to focus on (comma-separated, or 'all'): ").strip()
        
        if focus_input.lower() == 'all':
            tables_to_detail = tables
        else:
            tables_to_detail = [t.strip() for t in focus_input.split(',')]
    
    print(f"Will catalog {len(tables_to_detail)} tables in detail")
    print()
    
    # Step 10: Catalog tables
    print("=" * 70)
    print("STEP 9: Cataloging table details")
    print("=" * 70)
    
    tables_data = []
    
    for i, table_name in enumerate(tables_to_detail, 1):
        print(f"Processing {i}/{len(tables_to_detail)}: {table_name}...")
        
        try:
            table_info = get_table_details(engine, table_name, selected_schema)
            
            # Get sample values for each column
            for col in table_info['columns']:
                col_name = col['name']
                samples = get_sample_values(engine, table_name, col_name, selected_schema, limit=2)
                col['samples'] = samples
            
            tables_data.append(table_info)
            
        except Exception as e:
            print(f"  ⚠ Warning: Error processing {table_name}: {e}")
            continue
    
    print(f"✓ Successfully cataloged {len(tables_data)} tables")
    print()
    
    # Step 11: Format and save reference
    print("=" * 70)
    print("STEP 10: Generating and saving reference file")
    print("=" * 70)
    
    db_name = details.get('db_name', 'database')
    reference_content = format_reference_file(db_name, schema_name, tables_data)
    
    saved_path = save_reference_file(reference_content, db_name, schema_name)
    print(f"✓ Reference file saved to: {saved_path}")
    print()
    
    print("=" * 70)
    print("CATALOGING COMPLETE")
    print("=" * 70)
    print(f"Database: {db_name}")
    print(f"Schema: {schema_name}")
    print(f"Tables cataloged: {len(tables_data)}")
    print(f"Reference file: {saved_path}")


if __name__ == "__main__":
    main()
