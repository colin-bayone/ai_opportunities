# PostgreSQL Best Practices

PostgreSQL 17 with pgvector extension review checklist. Focus on queries, indexes, vector operations, and PostgreSQL-specific patterns.

## Database Configuration

### Connection Settings
- [ ] Connection pooling configured (via Django CONN_MAX_AGE)
- [ ] Maximum connections appropriate for application scale
- [ ] Idle connection timeout set
- [ ] No hardcoded credentials in code
- [ ] Database URL in environment variables

### PostgreSQL-Only Policy
- [ ] No SQLite usage anywhere in codebase
- [ ] All environments use PostgreSQL (local, dev, prod)
- [ ] Migrations tested against PostgreSQL only
- [ ] PostgreSQL-specific features used appropriately

## Query Optimization

### N+1 Query Prevention
- [ ] `select_related()` used for ForeignKey traversal
- [ ] `prefetch_related()` used for reverse FK and M2M
- [ ] Prefetch configured with custom querysets if needed
- [ ] No queries inside loops
- [ ] Django Debug Toolbar used to identify N+1 queries (local only)

### Query Patterns to Check
- [ ] `only()` used when fetching subset of fields
- [ ] `defer()` used to exclude large fields (text, binary)
- [ ] `values()` or `values_list()` for simple data extraction
- [ ] `iterator()` for large result sets (reduces memory)
- [ ] `bulk_create()` for batch inserts
- [ ] `bulk_update()` for batch updates
- [ ] `update()` on queryset instead of saving individual objects

### Raw SQL
- [ ] Raw SQL avoided unless necessary
- [ ] Parameterized queries used (never string concatenation)
- [ ] Complex queries explained with comments
- [ ] Raw queries tested for SQL injection vulnerabilities
- [ ] Consider using `extra()` or custom queryset methods instead

## Indexes

### Index Strategy
- [ ] Indexes on foreign keys (Django creates these automatically)
- [ ] Indexes on fields used in WHERE clauses frequently
- [ ] Indexes on fields used for ordering
- [ ] Composite indexes for multi-column queries
- [ ] Avoid over-indexing (slows writes)
- [ ] Index names follow convention

### Index Types
- [ ] B-tree indexes (default) for most cases
- [ ] GiST/GIN indexes for text search if needed
- [ ] BRIN indexes for time-series data
- [ ] Partial indexes for filtered queries
- [ ] Unique indexes for uniqueness constraints

### Index Review
- [ ] New indexes added via migrations (not manually)
- [ ] Indexes on high-cardinality columns
- [ ] No redundant indexes (covered by composite indexes)
- [ ] Index size monitored (very large indexes may hurt performance)

## pgvector Extension

### Vector Field Usage
- [ ] pgvector extension installed and migrated
- [ ] Vector fields use appropriate dimensions (match embedding model)
- [ ] Vector fields indexed with appropriate method (IVFFLAT or HNSW)
- [ ] Vector index parameters tuned (lists, probes, m, ef_construction)
- [ ] Vector operations use proper operators (`<->`, `<#>`, `<=>`)

### Vector Search Patterns
- [ ] Cosine similarity for normalized vectors: `<=>` operator
- [ ] Euclidean distance for spatial data: `<->` operator
- [ ] Inner product when appropriate: `<#>` operator
- [ ] LIMIT used to restrict results (avoid full table scan)
- [ ] Filters applied before vector search when possible
- [ ] Vector search combined with other filters efficiently

### Vector Index Creation
- [ ] IVFFLAT index for < 1M vectors: `USING ivfflat (vector_column vector_cosine_ops) WITH (lists = 100)`
- [ ] HNSW index for > 1M vectors or better recall
- [ ] Index created in migration with proper parameters
- [ ] Index build monitored (can be slow for large datasets)
- [ ] Consider creating index CONCURRENTLY in production

### Embedding Storage
- [ ] Embeddings stored as vector type, not JSON
- [ ] Embedding dimensions consistent across table
- [ ] NULL embeddings handled appropriately
- [ ] Embeddings generated before saving (not deferred)
- [ ] Batch embedding generation for efficiency

## Transactions

### Transaction Usage
- [ ] `transaction.atomic()` for multi-step operations
- [ ] Transactions as short as possible
- [ ] Read-heavy operations outside transactions when possible
- [ ] No external API calls inside transactions
- [ ] Celery tasks queued with `transaction.on_commit()`

### Transaction Isolation
- [ ] Default isolation level appropriate (READ COMMITTED)
- [ ] Serializable isolation used only when necessary
- [ ] Handle serialization failures with retries
- [ ] Avoid long-running transactions (lock contention)

### Locking
- [ ] `select_for_update()` used for pessimistic locking
- [ ] `nowait=True` or `skip_locked=True` when appropriate
- [ ] Lock scope minimized (lock only needed rows)
- [ ] Deadlock prevention (consistent lock order)
- [ ] Lock timeouts configured

## Migrations

### Migration Best Practices
- [ ] Migrations generated with `makemigrations` (not hand-written)
- [ ] Migration dependencies correct
- [ ] Large data migrations split into smaller chunks
- [ ] `RunPython` migrations reversible when possible
- [ ] No raw SQL in migrations unless necessary
- [ ] Migrations tested against production-like data volume

### Schema Changes
- [ ] New columns added with defaults or NULL allowed
- [ ] Dropping columns done in separate migration after deploy
- [ ] Renaming columns done carefully (requires multi-step migration)
- [ ] Index creation uses CONCURRENTLY in production
- [ ] Constraint addition non-blocking when possible

### Data Migrations
- [ ] Data transformations batched (don't load all rows at once)
- [ ] Progress logged for long-running migrations
- [ ] Idempotent (can be run multiple times safely)
- [ ] Tested with production data volume
- [ ] Reversible or documented as irreversible

## Full-Text Search

### PostgreSQL Full-Text Search
- [ ] `SearchVector` and `SearchQuery` used instead of LIKE
- [ ] GIN index on tsvector column for performance
- [ ] Search configuration set appropriately (e.g., 'english')
- [ ] Ranking used to order results
- [ ] Search combined with filters efficiently

### Search Patterns to Check
- [ ] `SearchVector` fields updated on model save (trigger or Django signal)
- [ ] Search queries use proper operators (`@@`)
- [ ] Weights applied to different fields (title > content)
- [ ] Fuzzy search implemented if needed (trigram similarity)

## Data Types

### Field Type Selection
- [ ] Text fields use `CharField` or `TextField` appropriately
- [ ] JSONField used for structured data (not serialized strings)
- [ ] ArrayField used for lists (not comma-separated strings)
- [ ] UUIDField used for UUIDs (not CharField)
- [ ] DateTimeField with timezone support (`USE_TZ=True`)
- [ ] DecimalField for monetary values (not FloatField)

### JSON Operations
- [ ] JSONField queries use proper lookups (`__key`, `__contains`)
- [ ] GIN index on JSONField for complex queries
- [ ] JSON structure validated before saving
- [ ] JSON not used to avoid proper schema (use relations)

### Array Operations
- [ ] ArrayField used instead of separate table for simple lists
- [ ] Array contains queries: `field__contains=[value]`
- [ ] Array overlap queries: `field__overlap=[values]`
- [ ] GIN index on ArrayField for queries

## Performance Monitoring

### Query Analysis
- [ ] `EXPLAIN` used for slow queries
- [ ] `EXPLAIN ANALYZE` for actual execution time
- [ ] Sequential scans minimized (add indexes)
- [ ] Index usage verified (not ignored by planner)
- [ ] Query plans reviewed for efficiency

### Slow Query Logging
- [ ] Slow query logging enabled (log queries > threshold)
- [ ] Slow queries reviewed and optimized
- [ ] Query patterns identified and indexed
- [ ] Connection limits monitored
- [ ] Database size and growth tracked

## Connection Pooling

### Django Configuration
- [ ] `CONN_MAX_AGE` set to enable persistent connections
- [ ] Connection lifetime appropriate (e.g., 600 seconds)
- [ ] Connection pooling at application level (not pgbouncer needed for Django)
- [ ] Connection errors handled gracefully
- [ ] Connections closed properly on errors

### Connection Limits
- [ ] Max connections set appropriately in PostgreSQL
- [ ] Application connection limit < database max connections
- [ ] Monitor connection usage (active vs idle)
- [ ] No connection leaks (all connections returned to pool)

## Backup and Recovery

### Backup Considerations
- [ ] Backups scheduled and tested
- [ ] Point-in-time recovery enabled (WAL archiving)
- [ ] Backup retention policy defined
- [ ] Restore process tested
- [ ] Backup storage separate from primary database

### Data Integrity
- [ ] Foreign key constraints enforced
- [ ] Check constraints used where appropriate
- [ ] NOT NULL constraints on required fields
- [ ] Unique constraints on unique fields
- [ ] Referential integrity maintained

## Security

### Access Control
- [ ] Principle of least privilege (app user has only needed permissions)
- [ ] No superuser access from application
- [ ] Read-only users for reporting/analytics
- [ ] Row-level security policies if needed
- [ ] Connection requires SSL in production

### SQL Injection Prevention
- [ ] All queries parameterized (Django ORM or psycopg2 with params)
- [ ] No string concatenation for SQL
- [ ] User input validated before queries
- [ ] Raw SQL reviewed carefully
- [ ] ORM methods preferred over raw SQL

## Multi-Tenancy (Client Groups)

### Data Isolation
- [ ] All tables include `client_group` or `client_group_id` field
- [ ] All queries filtered by client group
- [ ] Foreign keys include client group checks
- [ ] No cross-tenant data leakage
- [ ] Client group validated in middleware

### Query Patterns
- [ ] `get_queryset()` always filters by client group
- [ ] Related queries maintain client group filter
- [ ] Aggregations respect client group boundaries
- [ ] Database views (if used) include client group filter

## Common Anti-Patterns to Avoid

### Query Anti-Patterns
- [ ] Avoid `len(queryset)` - use `queryset.count()` instead
- [ ] Avoid `if queryset:` - use `queryset.exists()` instead
- [ ] Avoid iterating queryset multiple times - cache or use list()
- [ ] Avoid loading full objects when only need IDs - use values_list
- [ ] Avoid `filter().count() > 0` - use `exists()` instead

### Schema Anti-Patterns
- [ ] Avoid EAV (Entity-Attribute-Value) patterns
- [ ] Avoid storing denormalized data without good reason
- [ ] Avoid polymorphic associations (GenericForeignKey) when possible
- [ ] Avoid circular dependencies in models
- [ ] Avoid nullable boolean fields - use explicit states

### Vector Anti-Patterns
- [ ] Don't use cosine similarity on non-normalized vectors
- [ ] Don't fetch all vectors then sort in Python - filter in DB
- [ ] Don't create vector index on small tables (< 1000 rows)
- [ ] Don't mix vector dimensions in same table
- [ ] Don't skip vector index - queries will be slow

## Testing

### Database Tests
- [ ] Tests use TestCase (transactional) or TransactionTestCase
- [ ] Test database created/destroyed automatically
- [ ] Foreign key constraints tested
- [ ] Unique constraints tested
- [ ] Complex queries tested with realistic data
- [ ] Migration tests for complex migrations

### Performance Tests
- [ ] Query performance tested with large datasets
- [ ] Vector search tested with realistic vector count
- [ ] Index usage verified in tests
- [ ] N+1 queries caught in tests (Django Debug Toolbar)

## Monitoring Checklist

### Database Health
- [ ] Connection pool utilization monitored
- [ ] Query performance tracked
- [ ] Slow queries identified and optimized
- [ ] Database size and growth monitored
- [ ] Index bloat checked periodically
- [ ] Vacuum and analyze scheduled

### Vector Search Performance
- [ ] Vector search latency monitored
- [ ] Vector index size tracked
- [ ] Recall/precision measured if critical
- [ ] Query patterns optimized based on usage

## Cross-Reference

Related docs:
- `django_best_practices.md` - Django ORM patterns
- `celery_best_practices.md` - Async operations with DB
- `performance_monitoring_best_practices.md` - Query monitoring
- `ai_ml_integration_best_practices.md` - Embedding generation
