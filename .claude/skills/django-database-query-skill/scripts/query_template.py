"""
Template script for database queries using cataloged schema.
Copy this to .claude/databases/scratchpad/session_<date>/ and customize.

This template shows how to:
1. Load the reference file to verify table/column names
2. Write queries using exact names from the reference
3. Keep queries simple and readable
"""
import sys
from pathlib import Path

# Import utilities from skill scripts directory
skill_scripts = Path(__file__).resolve().parents[4] / '.claude/skills/django-database-query-skill/scripts'
sys.path.insert(0, str(skill_scripts))

from db_utils import load_env_file, build_connection_string, create_engine
from sqlalchemy import text


def load_reference(db_name: str, schema: str) -> str:
    """Load the schema reference file."""
    ref_path = Path(__file__).resolve().parents[4] / '.claude' / 'databases' / db_name / schema / 'reference.md'
    
    if not ref_path.exists():
        print(f"❌ Reference file not found: {ref_path}")
        print("Run the catalog script first to generate the reference.")
        sys.exit(1)
    
    with open(ref_path) as f:
        return f.read()


def verify_table_columns(reference: str, table: str, columns: list) -> bool:
    """Verify that a table and its columns exist in the reference."""
    if f"TABLE: {table}" not in reference:
        print(f"❌ Table '{table}' not found in reference")
        return False
    
    # Extract the table section
    table_section_start = reference.find(f"TABLE: {table}")
    next_table = reference.find("TABLE:", table_section_start + 1)
    if next_table == -1:
        table_section = reference[table_section_start:]
    else:
        table_section = reference[table_section_start:next_table]
    
    # Check each column
    for col in columns:
        if f"{col} |" not in table_section:
            print(f"❌ Column '{col}' not found in table '{table}'")
            print(f"\nAvailable columns in {table}:")
            # Show available columns
            lines = table_section.split('\n')
            for line in lines:
                if '|' in line and '[Column |' not in line:
                    parts = line.split('|')
                    if len(parts) > 0:
                        col_name = parts[0].strip()
                        if col_name:
                            print(f"  - {col_name}")
            return False
    
    return True


def main():
    """Main query workflow."""
    
    print("=" * 80)
    print("Database Query Script")
    print("=" * 80)
    print()
    
    # Step 1: Load environment and connect
    print("Step 1: Loading database credentials...")
    env_file = input("Enter path to env file [.env]: ").strip() or ".env"
    
    if not Path(env_file).exists():
        print(f"❌ Environment file '{env_file}' not found")
        sys.exit(1)
    
    env_vars = load_env_file(env_file)
    print(f"✓ Loaded {len(env_vars)} variables from {env_file}")
    
    db_type = input("Database type (postgresql/sqlite) [postgresql]: ").strip() or "postgresql"
    conn_str, details = build_connection_string(env_vars, db_type)
    
    if conn_str is None:
        print(f"❌ Error: {details}")
        sys.exit(1)
    
    print(f"✓ Connection configured for {details.get('db_name')}")
    print()
    
    # Step 2: Load reference file
    print("Step 2: Loading schema reference...")
    db_name = details.get('db_name', 'database')
    schema = input("Enter schema name [public]: ").strip() or "public"
    
    reference = load_reference(db_name, schema)
    print(f"✓ Loaded reference for {db_name}.{schema}")
    print()
    
    # Step 3: Verify tables/columns before querying
    print("Step 3: Verifying tables and columns...")
    
    # CUSTOMIZE THIS SECTION for your specific query
    # Example: verify 'users' table has 'id', 'email', 'created_at' columns
    tables_to_verify = {
        'users': ['id', 'email', 'created_at'],
        # Add more tables as needed
    }
    
    for table, columns in tables_to_verify.items():
        print(f"  Checking {schema}.{table}...")
        if not verify_table_columns(reference, table, columns):
            sys.exit(1)
        print(f"  ✓ {table} verified")
    
    print()
    
    # Step 4: Execute queries
    print("Step 4: Executing queries...")
    print("=" * 80)
    print()
    
    engine = create_engine(conn_str)
    
    with engine.connect() as conn:
        # CUSTOMIZE YOUR QUERIES HERE
        # Example query - replace with your actual queries
        
        # Query 1: Count users
        print("Query 1: Count total users")
        result = conn.execute(text(f"""
            SELECT COUNT(*) as total
            FROM {schema}.users;
        """))
        total = result.fetchone()[0]
        print(f"  Result: {total} users")
        print()
        
        # Query 2: Get recent users
        print("Query 2: Get 10 most recent users")
        result = conn.execute(text(f"""
            SELECT id, email, created_at
            FROM {schema}.users
            ORDER BY created_at DESC
            LIMIT 10;
        """))
        
        print("  Results:")
        for row in result:
            print(f"    ID: {row[0]}, Email: {row[1]}, Created: {row[2]}")
        print()
        
        # Add more queries as needed
    
    print("=" * 80)
    print("✅ Query execution complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
