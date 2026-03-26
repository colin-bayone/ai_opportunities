# AI/ML Integration Best Practices

Presidio for PII detection, Tiktoken for token counting, and pgvector for embeddings.

## Presidio (PII Detection & Masking)

### Configuration
- [ ] Pattern-only mode (no spaCy models for speed)
- [ ] Saves 400MB memory and 1-2s startup time
- [ ] Singleton pattern for analyzer and anonymizer
- [ ] Initialize on first use, cache instance

### Recognizers Enabled
- [ ] EMAIL_ADDRESS
- [ ] PHONE_NUMBER
- [ ] IP_ADDRESS
- [ ] CRYPTO (Bitcoin/Ethereum wallets)
- [ ] Custom: Azure Blob Storage URLs
- [ ] Custom: Database connection strings
- [ ] Custom: API keys
- [ ] Custom: File paths

### Masking Configuration
```python
PII_MASKING_ENABLED = True  # Enable/disable masking
INFRASTRUCTURE_MASKING_ENABLED = True  # Mask infra secrets
PII_MASKING_OPERATOR = 'replace'  # Outputs <EMAIL_ADDRESS>
```

### Integration Points
- [ ] Automatic masking in all logs
- [ ] Custom logging formatter applies masking
- [ ] No PII in error messages
- [ ] No PII in audit logs
- [ ] Mask before sending to external services

## PII Masking Patterns

### Log Masking
- [ ] All logs automatically scrubbed
- [ ] Presidio runs on every log message
- [ ] Masked format: `<PII_TYPE>` (e.g., `<EMAIL_ADDRESS>`)
- [ ] Performance: Pattern-only is fast enough for logging

### Before External API Calls
- [ ] Mask PII before Azure OpenAI calls
- [ ] Mask before third-party integrations
- [ ] Store original + masked versions if needed
- [ ] Document what's masked and why

### User Display
- [ ] Show masked version in UI when appropriate
- [ ] Allow authorized users to see unmasked (with audit)
- [ ] Mask in exports and reports
- [ ] Clear indication when data is masked

## Custom Recognizers

### Infrastructure Secrets
- [ ] Azure Blob Storage URLs pattern
- [ ] Database connection strings pattern
- [ ] API key patterns (format: `key-xxx`)
- [ ] Generic secret patterns

### Adding Custom Recognizers
- [ ] Extend `PatternRecognizer` class
- [ ] Define regex patterns
- [ ] Set entity type name
- [ ] Add to recognizer registry
- [ ] Test with real examples

### Pattern Guidelines
- [ ] Balance precision vs recall
- [ ] Test for false positives
- [ ] Document pattern purpose
- [ ] Review pattern performance

## Tiktoken (Token Counting)

### Token Counting Usage
- [ ] Count tokens BEFORE OpenAI API call
- [ ] Verify input within model limits
- [ ] Estimate costs based on token count
- [ ] Monitor token usage per request

### Model-Specific Encodings
- [ ] Use `tiktoken.encoding_for_model(model_name)`
- [ ] Different models have different encodings
- [ ] GPT-4: cl100k_base encoding
- [ ] GPT-3.5-Turbo: cl100k_base encoding
- [ ] text-embedding-3-large: cl100k_base encoding

### Token Limits by Model
- [ ] GPT-4: 8,192 tokens (input + output)
- [ ] GPT-4-32k: 32,768 tokens
- [ ] GPT-3.5-Turbo: 4,096 tokens
- [ ] text-embedding-3-large: 8,191 tokens
- [ ] Always reserve tokens for response

### Truncation Strategy
- [ ] Truncate if over limit
- [ ] Truncate from middle or end (context dependent)
- [ ] Preserve important sections (beginning/end)
- [ ] Indicate truncation to user if relevant

### Token Estimation
- [ ] Tokens ≈ words * 1.3-1.5 (rough estimate)
- [ ] Use tiktoken for accurate count
- [ ] Cache encoding instance (reusable)
- [ ] Count both prompt and expected response

## pgvector (Embeddings)

### Vector Storage
- [ ] Use `VectorField` from pgvector Django package
- [ ] Dimensions match embedding model (1536 for text-embedding-3-large)
- [ ] Allow null for optional embeddings
- [ ] Index for similarity search

### Similarity Search
- [ ] Use cosine distance operator `<=>`
- [ ] L2 distance operator `<->`
- [ ] Inner product operator `<#>`
- [ ] Choose based on embedding model docs

### Query Patterns
- [ ] Annotate queryset with distance
- [ ] Filter by distance threshold (e.g., < 0.3)
- [ ] Order by distance (ascending = most similar)
- [ ] Limit results (top k)
- [ ] Combine with other filters (client_group, etc.)

### Indexing
- [ ] Create IVFFlat or HNSW index
- [ ] Index parameters tuned for dataset size
- [ ] Monitor query performance
- [ ] Rebuild index periodically if needed

### Hybrid Search
- [ ] Combine vector similarity with keyword search
- [ ] Filter by client group before similarity
- [ ] Use full-text search alongside vectors
- [ ] Rank by multiple relevance signals

## Embedding Generation Workflow

### When to Generate
- [ ] On document creation
- [ ] On document update (if content changed)
- [ ] Async with Celery (don't block request)
- [ ] Batch generate for multiple documents

### Embedding Storage
- [ ] Store embedding alongside source text
- [ ] Store model name and version
- [ ] Store generation timestamp
- [ ] Track if embedding is stale

### Cache Embeddings
- [ ] Cache by content hash
- [ ] Don't regenerate for same content
- [ ] Invalidate on content change
- [ ] Consider cache size limits

### Batch Operations
- [ ] Batch embed multiple texts in one API call
- [ ] Azure OpenAI supports up to 2048 texts
- [ ] Reduces API calls and latency
- [ ] Handle batch failures gracefully

## Security & Privacy

### PII in Embeddings
- [ ] Mask PII before generating embeddings
- [ ] Consider if masked embeddings affect search quality
- [ ] Document masking policy
- [ ] Audit embedding generation

### Embedding Access Control
- [ ] Filter embeddings by client group
- [ ] No cross-tenant similarity search
- [ ] Audit embedding queries
- [ ] Secure vector storage

### External API Security
- [ ] No PII to Azure OpenAI
- [ ] Mask before embedding generation
- [ ] Log API calls without sensitive data
- [ ] Monitor for data leakage

## Performance Optimization

### Presidio Performance
- [ ] Pattern-only mode is fast (<1ms per log)
- [ ] Singleton avoids re-initialization
- [ ] No ML models loaded (saves memory)
- [ ] Acceptable for real-time logging

### Tiktoken Performance
- [ ] Encoding instance is reusable
- [ ] Cache encoding for model
- [ ] Token counting is fast (<1ms)
- [ ] Don't count repeatedly

### pgvector Performance
- [ ] Index similarity searches
- [ ] Filter before similarity (reduce search space)
- [ ] Limit result set size
- [ ] Monitor query latency
- [ ] Consider approximate search for large datasets

## Testing

### Presidio Testing
- [ ] Test with known PII examples
- [ ] Test custom recognizers
- [ ] Test masking output format
- [ ] Verify no false negatives (PII not detected)
- [ ] Check for false positives (legitimate data masked)

### Tiktoken Testing
- [ ] Test token counts for various texts
- [ ] Test truncation logic
- [ ] Verify encoding selection per model
- [ ] Test with edge cases (empty, very long)

### pgvector Testing
- [ ] Test similarity search with known vectors
- [ ] Test filtering and ordering
- [ ] Test index usage (EXPLAIN ANALYZE)
- [ ] Test with different distance operators

## Monitoring

### Presidio Metrics
- [ ] Masking rate (% of logs with PII)
- [ ] PII types detected (email, phone, etc.)
- [ ] Custom recognizer hit rate
- [ ] Performance impact on logging

### Tiktoken Metrics
- [ ] Average token count per request
- [ ] Requests exceeding limits
- [ ] Truncation frequency
- [ ] Cost per request (token-based)

### pgvector Metrics
- [ ] Similarity search latency
- [ ] Result set sizes
- [ ] Index usage rate
- [ ] Vector dimension distribution

## Common Patterns

### Mask Before Logging
```python
from myapp.diagnostics.logging import mask_pii

sensitive_data = "Email: user@example.com"
safe_data = mask_pii(sensitive_data)
logger.info(f"Processing: {safe_data}")
# Output: "Processing: Email: <EMAIL_ADDRESS>"
```

### Count Tokens Before API Call
```python
import tiktoken

def count_and_validate(text, model="gpt-4", max_tokens=6000):
    encoding = tiktoken.encoding_for_model(model)
    token_count = len(encoding.encode(text))
    
    if token_count > max_tokens:
        raise ValueError(f"Text too long: {token_count} tokens")
    
    return token_count
```

### Similarity Search with Filters
```python
from pgvector.django import CosineDistance

def search_similar(query_embedding, client_group_id, limit=10):
    return Document.objects.filter(
        client_group_id=client_group_id,
        embedding__isnull=False
    ).annotate(
        distance=CosineDistance('embedding', query_embedding)
    ).filter(
        distance__lt=0.5
    ).order_by('distance')[:limit]
```

## Troubleshooting

### Presidio not detecting PII
- Check pattern recognizers enabled
- Verify PII format matches pattern
- Test recognizer individually
- Check if custom recognizer needed

### Token count mismatch with API
- Verify using correct model encoding
- Check API version differences
- Test with known examples
- Update tiktoken library

### pgvector search returning no results
- Check if embeddings populated
- Verify distance threshold not too strict
- Check query embedding dimensions
- Ensure index exists and used

### Slow similarity search
- Add or optimize index (IVFFlat/HNSW)
- Filter by other criteria first
- Reduce result set size
- Check query plan with EXPLAIN

## Edge Cases

### Presidio Edge Cases
- [ ] Nested PII (email in URL)
- [ ] Encoded PII (base64)
- [ ] Partial PII (masked email)
- [ ] International formats (phone, address)

### Tiktoken Edge Cases
- [ ] Empty text (0 tokens)
- [ ] Very long text (millions of tokens)
- [ ] Special characters
- [ ] Non-English text

### pgvector Edge Cases
- [ ] Null embeddings
- [ ] Zero vectors
- [ ] High-dimensional outliers
- [ ] Duplicate embeddings

## Cross-Reference

Related docs:
- `azure_openai_best_practices.md` - Embedding generation
- `postgresql_best_practices.md` - pgvector configuration
- `soc2_considerations.md` - PII handling requirements
- `web_security_best_practices.md` - Data privacy
- `performance_monitoring_best_practices.md` - ML metrics
