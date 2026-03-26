"""
Database utility functions for Django database operations.
Uses SQLAlchemy to interact with PostgreSQL and SQLite databases.
"""
import os
from typing import Dict, List, Tuple, Optional, Any, TYPE_CHECKING
from datetime import datetime
from pathlib import Path
import json

if TYPE_CHECKING:
    from sqlalchemy.engine import Engine

try:
    from sqlalchemy import create_engine, inspect, text, MetaData, Table
    from sqlalchemy.engine import Engine as _Engine
    SQLALCHEMY_AVAILABLE = True
    Engine = _Engine
except ImportError:
    SQLALCHEMY_AVAILABLE = False
    Engine = Any  # Fallback type for when SQLAlchemy is not installed


def check_sqlalchemy() -> Tuple[bool, str]:
    """Check if SQLAlchemy is installed and return status message."""
    if SQLALCHEMY_AVAILABLE:
        import sqlalchemy
        return True, f"SQLAlchemy {sqlalchemy.__version__} is installed"
    else:
        return False, "SQLAlchemy is not installed. Install with: pip install sqlalchemy psycopg2-binary"


def load_env_file(env_path: str) -> Dict[str, str]:
    """Load environment variables from a .env file."""
    env_vars = {}
    if not os.path.exists(env_path):
        return env_vars
    
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                # Remove quotes if present
                value = value.strip().strip('"').strip("'")
                env_vars[key.strip()] = value
    return env_vars


def build_connection_string(env_vars: Dict[str, str], db_type: str = 'postgresql') -> Tuple[Optional[str], Dict[str, Any]]:
    """
    Build SQLAlchemy connection string from environment variables.
    Returns (connection_string, connection_details) or (None, error_dict).
    """
    details = {}
    
    # Check for DATABASE_URL first (common in Django/Heroku)
    if 'DATABASE_URL' in env_vars:
        return env_vars['DATABASE_URL'], {'source': 'DATABASE_URL', 'url': env_vars['DATABASE_URL']}
    
    # Build from individual components
    if db_type == 'postgresql':
        db_name = env_vars.get('DB_NAME') or env_vars.get('POSTGRES_DB')
        db_user = env_vars.get('DB_USER') or env_vars.get('POSTGRES_USER')
        db_password = env_vars.get('DB_PASSWORD') or env_vars.get('POSTGRES_PASSWORD')
        db_host = env_vars.get('DB_HOST') or env_vars.get('POSTGRES_HOST')
        db_port = env_vars.get('DB_PORT') or env_vars.get('POSTGRES_PORT')
        
        details = {
            'db_name': db_name,
            'db_host': db_host,
            'db_port': db_port,
            'db_user': db_user,
            'db_type': 'postgresql'
        }
        
        if not all([db_name, db_user, db_host]):
            return None, {'error': 'Missing required database credentials', 'details': details}
        
        # Build connection string
        password_part = f":{db_password}" if db_password else ""
        port_part = f":{db_port}" if db_port else ":5432"
        conn_str = f"postgresql://{db_user}{password_part}@{db_host}{port_part}/{db_name}"
        
        return conn_str, details
    
    elif db_type == 'sqlite':
        db_path = env_vars.get('DB_PATH') or env_vars.get('SQLITE_DB')
        if not db_path:
            return None, {'error': 'Missing SQLITE_DB or DB_PATH'}
        
        details = {'db_path': db_path, 'db_type': 'sqlite'}
        return f"sqlite:///{db_path}", details
    
    return None, {'error': f'Unsupported database type: {db_type}'}


def test_connection(connection_string: str) -> Tuple[bool, str]:
    """Test database connectivity."""
    try:
        engine = create_engine(connection_string)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            result.fetchone()
        return True, "Connection successful"
    except Exception as e:
        return False, f"Connection failed: {str(e)}"


def get_schemas(engine: Engine) -> List[str]:
    """Get list of all schemas in the database."""
    inspector = inspect(engine)
    return inspector.get_schema_names()


def get_tables(engine: Engine, schema: Optional[str] = None) -> List[str]:
    """Get list of all tables in a schema."""
    inspector = inspect(engine)
    return inspector.get_table_names(schema=schema)


def get_table_details(engine: Engine, table_name: str, schema: Optional[str] = None) -> Dict[str, Any]:
    """
    Get detailed information about a table including columns, types, constraints, and sample data.
    Returns a dictionary with table metadata.
    """
    inspector = inspect(engine)
    
    # Get columns
    columns = inspector.get_columns(table_name, schema=schema)
    
    # Get primary keys
    pk_constraint = inspector.get_pk_constraint(table_name, schema=schema)
    primary_keys = pk_constraint.get('constrained_columns', [])
    
    # Get foreign keys
    foreign_keys = inspector.get_foreign_keys(table_name, schema=schema)
    
    # Get unique constraints
    unique_constraints = inspector.get_unique_constraints(table_name, schema=schema)
    
    # Get indexes
    indexes = inspector.get_indexes(table_name, schema=schema)
    
    # Build column details with constraints
    column_details = []
    for col in columns:
        constraints = []
        
        if col['name'] in primary_keys:
            constraints.append('PRIMARY KEY')
        
        if not col['nullable']:
            constraints.append('NOT NULL')
        
        # Check unique constraints
        for uc in unique_constraints:
            if col['name'] in uc['column_names']:
                constraints.append('UNIQUE')
                break
        
        # Check foreign keys
        for fk in foreign_keys:
            if col['name'] in fk['constrained_columns']:
                ref_table = fk['referred_table']
                ref_col = fk['referred_columns'][0] if fk['referred_columns'] else ''
                constraints.append(f'FOREIGN KEY -> {ref_table}({ref_col})')
                break
        
        column_details.append({
            'name': col['name'],
            'type': str(col['type']),
            'nullable': col['nullable'],
            'constraints': constraints,
            'default': col.get('default')
        })
    
    return {
        'name': table_name,
        'schema': schema,
        'columns': column_details,
        'primary_keys': primary_keys,
        'foreign_keys': foreign_keys,
        'unique_constraints': unique_constraints,
        'indexes': indexes
    }


def get_sample_values(engine: Engine, table_name: str, column_name: str, 
                     schema: Optional[str] = None, limit: int = 2) -> List[Any]:
    """Get sample non-null values from a column."""
    try:
        schema_prefix = f'"{schema}".' if schema else ''
        query = text(f'SELECT DISTINCT "{column_name}" FROM {schema_prefix}"{table_name}" WHERE "{column_name}" IS NOT NULL LIMIT :limit')
        
        with engine.connect() as conn:
            result = conn.execute(query, {"limit": limit})
            samples = [row[0] for row in result]
            
            # Format samples
            formatted_samples = []
            for sample in samples:
                if isinstance(sample, (dict, list)):
                    sample_str = json.dumps(sample)
                    if len(sample_str) > 250:
                        sample_str = sample_str[:250] + "..."
                    formatted_samples.append(sample_str)
                elif isinstance(sample, str):
                    if len(sample) > 250:
                        sample = sample[:250] + "..."
                    formatted_samples.append(f'"{sample}"')
                else:
                    formatted_samples.append(str(sample))
            
            return formatted_samples
    except Exception as e:
        return [f"Error: {str(e)}"]


def format_reference_file(db_name: str, schema: str, tables_data: List[Dict[str, Any]], 
                         timestamp: Optional[str] = None) -> str:
    """
    Format the schema reference file in the specified markdown format.
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = []
    lines.append(f"# Database: {db_name} ({schema} schema)")
    lines.append(f"Last updated: {timestamp}")
    lines.append("")
    lines.append("## Table List")
    
    # Table list
    for table_data in tables_data:
        col_count = len(table_data['columns'])
        lines.append(f"- {table_data['name']} ({col_count} columns)")
    
    lines.append("")
    lines.append("## Schema Details")
    lines.append("")
    
    # Detailed schema for each table
    for table_data in tables_data:
        lines.append(f"TABLE: {table_data['name']}")
        lines.append("  [Column | Type | Constraints | Sample1 | Sample2]")
        
        for col in table_data['columns']:
            col_name = col['name']
            col_type = col['type']
            constraints = ', '.join(col['constraints']) if col['constraints'] else '-'
            
            # Get samples
            samples = col.get('samples', [])
            sample1 = samples[0] if len(samples) > 0 else '-'
            sample2 = samples[1] if len(samples) > 1 else '-'
            
            lines.append(f"  {col_name} | {col_type} | {constraints} | {sample1} | {sample2}")
        
        lines.append("")
    
    return '\n'.join(lines)


def save_reference_file(content: str, db_name: str, schema: str, base_path: str = ".claude/databases") -> str:
    """
    Save the reference file to the appropriate location.
    Returns the path where the file was saved.
    """
    ref_dir = Path(base_path) / db_name / schema
    ref_dir.mkdir(parents=True, exist_ok=True)
    
    ref_path = ref_dir / "reference.md"
    with open(ref_path, 'w') as f:
        f.write(content)
    
    return str(ref_path)


def get_reference_age(db_name: str, schema: str, base_path: str = ".claude/databases") -> Optional[float]:
    """
    Get the age of the reference file in days.
    Returns None if file doesn't exist.
    """
    ref_path = Path(base_path) / db_name / schema / "reference.md"
    
    if not ref_path.exists():
        return None
    
    mtime = ref_path.stat().st_mtime
    age_seconds = datetime.now().timestamp() - mtime
    return age_seconds / (24 * 3600)  # Convert to days
