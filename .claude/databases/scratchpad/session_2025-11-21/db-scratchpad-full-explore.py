"""
Full database exploration script - non-interactive version.
Catalogs ALL schemas and tables in the database.
"""
import sys
from pathlib import Path

# Import utilities from skill scripts directory
skill_scripts = Path(__file__).resolve().parents[4] / '.claude/skills/django-database-query-skill/scripts'
sys.path.insert(0, str(skill_scripts))

from db_utils import (
    check_sqlalchemy, load_env_file, build_connection_string,
    test_connection, get_schemas, get_tables, get_table_details,
    get_sample_values, format_reference_file, save_reference_file
)
from sqlalchemy import create_engine


def main():
    """Full database exploration workflow."""

    # Step 1: Check SQLAlchemy
    print("=" * 70)
    print("STEP 1: Checking SQLAlchemy installation")
    print("=" * 70)
    available, message = check_sqlalchemy()
    print(f"Status: {message}")
    if not available:
        sys.exit(1)
    print()

    # Step 2: Load environment file (hardcoded to .env.local)
    print("=" * 70)
    print("STEP 2: Loading database credentials")
    print("=" * 70)
    env_file = ".env.local"

    if not Path(env_file).exists():
        print(f"❌ Error: Environment file '{env_file}' not found")
        sys.exit(1)

    env_vars = load_env_file(env_file)
    print(f"✓ Loaded {len(env_vars)} variables from {env_file}")
    print()

    # Step 3: Build connection string (PostgreSQL)
    print("=" * 70)
    print("STEP 3: Building connection string")
    print("=" * 70)
    db_type = "postgresql"

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
            tables = get_tables(engine, schema)
            print(f"  {i}. {schema} ({len(tables)} tables)")
        print()
    except Exception as e:
        print(f"❌ Error listing schemas: {e}")
        sys.exit(1)

    # Step 7: Catalog ALL schemas
    print("=" * 70)
    print("STEP 6: Cataloging ALL schemas")
    print("=" * 70)

    db_name = details.get('db_name', 'database')
    all_results = []

    for schema_idx, schema_name in enumerate(schemas, 1):
        print(f"\n{'=' * 70}")
        print(f"SCHEMA {schema_idx}/{len(schemas)}: {schema_name}")
        print('=' * 70)

        # Get tables in this schema
        tables = get_tables(engine, schema_name)
        print(f"Found {len(tables)} tables in {schema_name}")

        if len(tables) == 0:
            print(f"Skipping empty schema: {schema_name}")
            continue

        # Catalog all tables in this schema
        tables_data = []

        for table_idx, table_name in enumerate(tables, 1):
            print(f"  Processing table {table_idx}/{len(tables)}: {table_name}...")

            try:
                table_info = get_table_details(engine, table_name, schema_name)

                # Get sample values for each column
                for col in table_info['columns']:
                    col_name = col['name']
                    samples = get_sample_values(engine, table_name, col_name, schema_name, limit=2)
                    col['samples'] = samples

                tables_data.append(table_info)

            except Exception as e:
                print(f"    ⚠ Warning: Error processing {table_name}: {e}")
                continue

        print(f"✓ Successfully cataloged {len(tables_data)} tables in {schema_name}")

        # Generate and save reference file for this schema
        if tables_data:
            reference_content = format_reference_file(db_name, schema_name, tables_data)
            saved_path = save_reference_file(reference_content, db_name, schema_name)
            print(f"✓ Reference file saved to: {saved_path}")

            all_results.append({
                'schema': schema_name,
                'tables_count': len(tables_data),
                'reference_path': saved_path
            })

    # Final summary
    print("\n" + "=" * 70)
    print("FULL EXPLORATION COMPLETE")
    print("=" * 70)
    print(f"Database: {db_name}")
    print(f"Schemas cataloged: {len(all_results)}")
    print()
    print("Summary:")
    for result in all_results:
        print(f"  • {result['schema']}: {result['tables_count']} tables")
        print(f"    → {result['reference_path']}")
    print()
    print("✓ All reference files have been generated!")


if __name__ == "__main__":
    main()
