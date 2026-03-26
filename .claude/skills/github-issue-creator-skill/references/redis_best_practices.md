# Redis Best Practices

Redis 8.2.0 for Celery broker/results backend, Channels layer, and production caching.

## Redis Deployment

### Local Development
- [ ] Docker image: `redis:8.2.0-bookworm`
- [ ] Docker Compose for local Redis
- [ ] Environment variables in `.env` file (django-environ)
- [ ] No authentication required for local (localhost only)
- [ ] Persistence optional in local (faster restarts without)

### Production
- [ ] **Azure Managed Redis** (NEW - replaces Azure Cache for Redis)
- [ ] Built on Redis Enterprise 7.4+ (Redis 8.0 support coming)
- [ ] Up to 99.999% availability with multi-region Active-Active
- [ ] Environment variables in **Azure Key Vault**
- [ ] Deployed in **Azure Container Apps**
- [ ] SSL/TLS enforced for all connections
- [ ] Password authentication required

### Docker Compose Configuration (Local)
```yaml
# docker-compose.yml
version: '3.8'

services:
  redis:
    image: redis:8.2.0-bookworm
    container_name: redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    # Optional: enable persistence
    # command: redis-server --appendonly yes
    networks:
      - app_network

  postgres:
    image: postgres:17
    # ... postgres config

volumes:
  redis_data:
  postgres_data:

networks:
  app_network:
```

### Azure Managed Redis Configuration

#### Tier Selection
- [ ] **Memory Optimized**: High memory-to-vCPU ratio (8:1) - ideal for dev/test
- [ ] **Balanced**: Balanced CPU-to-memory - most standard workloads
- [ ] **Compute Optimized**: High CPU-to-memory - maximum throughput, mission critical
- [ ] **Flash Optimized** (Preview): NVMe storage + RAM - cost-effective for large datasets

#### Production Settings
- [ ] High Availability enabled (multi-node replication)
- [ ] Zone redundancy enabled (Availability Zones)
- [ ] TLS 1.2+ enforced
- [ ] Microsoft Entra ID authentication (optional, in addition to access keys)
- [ ] Private endpoints for VNet isolation (optional)
- [ ] Data persistence enabled (RDB + AOF)

#### Advanced Features (Azure Managed Redis)
- [ ] Vector search capabilities (for RAG AI applications)
- [ ] JSON data structures (RedisJSON)
- [ ] Time series data types
- [ ] Probabilistic data structures
- [ ] Full-text search with secondary indexing
- [ ] Active geo-replication (multi-region)

## Environment Configuration

### Local (.env file)
```bash
# .env file (not committed to git)
DEBUG=True
ENVIRONMENT=local

# Redis - Local Docker
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
REDIS_CACHE_URL=redis://localhost:6379/2
REDIS_CHANNELS_URL=redis://localhost:6379/3
REDIS_SRI_URL=redis://localhost:6379/4
```

### Production (Azure Key Vault)
```python
# settings.py - Production configuration
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

if not DEBUG and ENVIRONMENT == 'production':
    # Connect to Azure Key Vault
    credential = DefaultAzureCredential()
    key_vault_url = env('AZURE_KEY_VAULT_URL')
    client = SecretClient(vault_url=key_vault_url, credential=credential)
    
    # Retrieve Redis connection strings from Key Vault
    REDIS_URL = client.get_secret('redis-url').value
    CELERY_BROKER_URL = client.get_secret('celery-broker-url').value
    CELERY_RESULT_BACKEND = client.get_secret('celery-result-backend-url').value
    REDIS_CACHE_URL = client.get_secret('redis-cache-url').value
    REDIS_CHANNELS_URL = client.get_secret('redis-channels-url').value
    REDIS_SRI_URL = client.get_secret('redis-sri-url').value
else:
    # Local development - use .env file
    REDIS_URL = env('REDIS_URL', default='redis://localhost:6379/0')
    CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
    # ... etc
```

### Azure Managed Redis Connection String Format
```python
# With password
REDIS_URL=rediss://:password@your-cache.redis.cache.windows.net:6380/0

# Components:
# - rediss:// = SSL/TLS connection (required in production)
# - :password = Access key from Azure portal
# - your-cache.redis.cache.windows.net = Azure Managed Redis endpoint
# - 6380 = SSL port (6379 is non-SSL, blocked in production)
# - /0 = Database number (0-15)
```

## Database Organization

### Dedicated Databases
- [ ] DB 0: Celery broker
- [ ] DB 1: Celery results backend (can be same as broker)
- [ ] DB 2: Django cache
- [ ] DB 3: Channels layer
- [ ] DB 4: SRI hash cache (dedicated for CDN integrity hashes)
- [ ] Logical separation by database number (0-15)

### Database Configuration
```python
# settings.py
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='redis://localhost:6379/0')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env('REDIS_CACHE_URL', default='redis://localhost:6379/2'),
        'OPTIONS': {
            'ssl_cert_reqs': None,  # Production: require SSL
        },
    },
    'sri': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env('REDIS_SRI_URL', default='redis://localhost:6379/4'),
        'TIMEOUT': 86400,  # 24 hours
        'OPTIONS': {
            'ssl_cert_reqs': None,  # Production: require SSL
        },
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [env('REDIS_CHANNELS_URL', default='redis://localhost:6379/3')],
        },
    },
}
```

### Production SSL Configuration
```python
import ssl
import certifi

# Production cache settings
if not DEBUG and ENVIRONMENT == 'production':
    CACHES['default']['OPTIONS'] = {
        'ssl_cert_reqs': ssl.CERT_REQUIRED,
        'ssl_ca_certs': certifi.where(),  # Use certifi for CA bundle
    }
    CACHES['sri']['OPTIONS'] = {
        'ssl_cert_reqs': ssl.CERT_REQUIRED,
        'ssl_ca_certs': certifi.where(),
    }
```

## Celery Integration

### Broker Configuration
- [ ] Redis DB 0 for message broker
- [ ] SSL/TLS in production (rediss://)
- [ ] Connection pool configured
- [ ] Visibility timeout set appropriately
- [ ] Broker connection retry on startup

### Results Backend
- [ ] Redis DB 0 or 1 for results storage
- [ ] Result expiration configured (`CELERY_RESULT_EXPIRES`)
- [ ] Results cleaned up automatically
- [ ] JSON serialization for security

### Celery Settings
```python
import ssl
import certifi

CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_EXPIRES = 3600  # 1 hour
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Production: SSL settings
if not DEBUG and ENVIRONMENT == 'production':
    CELERY_BROKER_USE_SSL = {
        'ssl_cert_reqs': ssl.CERT_REQUIRED,
        'ssl_ca_certs': certifi.where(),
    }
    CELERY_REDIS_BACKEND_USE_SSL = {
        'ssl_cert_reqs': ssl.CERT_REQUIRED,
        'ssl_ca_certs': certifi.where(),
    }
```

## Django Cache Backend

### Cache Configuration
- [ ] Redis used as cache backend in production
- [ ] In-memory cache for local development (optional)
- [ ] Dedicated Redis DB (e.g., DB 2)
- [ ] Cache timeout configured per use case
- [ ] Cache keys namespaced by app
- [ ] Cache invalidation strategy defined

### Cache Usage Patterns

#### View Caching
```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 15 minutes
def my_view(request):
    # Expensive operation
    return render(request, 'template.html', context)
```

#### Template Fragment Caching
```django
{% load cache %}
{% cache 500 sidebar %}
    <!-- Expensive sidebar rendering -->
{% endcache %}
```

#### Low-Level Cache API
```python
from django.core.cache import cache

# Set cache
cache.set('my_key', 'my_value', timeout=300)

# Get cache
value = cache.get('my_key', default=None)

# Get or set
value = cache.get_or_set('my_key', expensive_function, timeout=300)

# Delete cache
cache.delete('my_key')

# Multiple keys
cache.set_many({'key1': 'val1', 'key2': 'val2'}, timeout=300)
values = cache.get_many(['key1', 'key2'])
```

### Cache Key Patterns
- [ ] Use descriptive, namespaced keys: `app:model:id:attribute`
- [ ] Include version in key for invalidation: `app:model:v2:id`
- [ ] Use `make_key()` function for consistent key generation
- [ ] Document cache key patterns

```python
def make_cache_key(namespace, identifier, version='v1'):
    return f"{namespace}:{version}:{identifier}"

key = make_cache_key('documents', document.id)
cache.set(key, document_data, timeout=3600)
```

## Channels Layer (WebSockets)

### Channels Configuration
- [ ] Dedicated Redis DB (e.g., DB 3) for Channels
- [ ] `channels_redis` backend installed
- [ ] Capacity and expiry configured
- [ ] Channel layer tested for consumer communication
- [ ] SSL in production

### Channels Layer Settings
```python
import ssl
import certifi

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [env('REDIS_CHANNELS_URL', default='redis://localhost:6379/3')],
            'capacity': 1500,  # Max messages in channel
            'expiry': 10,  # Message expiry in seconds
        },
    },
}

# Production: Add SSL config
if not DEBUG and ENVIRONMENT == 'production':
    CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [{
        'address': env('REDIS_CHANNELS_URL'),
        'ssl': {
            'ssl_cert_reqs': ssl.CERT_REQUIRED,
            'ssl_ca_certs': certifi.where(),
        }
    }]
```

### Channel Communication
```python
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Send message to group
channel_layer = get_channel_layer()
async_to_sync(channel_layer.group_send)(
    'chat_room_123',
    {
        'type': 'chat.message',
        'message': 'Hello!',
    }
)
```

## SRI Cache (Subresource Integrity)

### Dedicated SRI Cache
- [ ] Separate Redis DB (e.g., DB 4) for SRI hashes
- [ ] 24-hour timeout for SRI entries
- [ ] Production-only (disabled in development)
- [ ] Cache keys based on CDN asset URLs
- [ ] Lazy generation (calculate on first use, cache for 24h)

### SRI Cache Usage
```python
from django.core.cache import caches

sri_cache = caches['sri']

def get_or_generate_sri(asset_url):
    cache_key = f"sri:{asset_url}"
    sri_hash = sri_cache.get(cache_key)
    
    if not sri_hash:
        sri_hash = generate_sri_hash(asset_url)
        sri_cache.set(cache_key, sri_hash, timeout=86400)  # 24 hours
    
    return sri_hash
```

## Rate Limiting

### Authentication Rate Limiting
- [ ] Rate limit keys: `auth_rate_limit:{ip}`
- [ ] Lockout keys: `auth_lockout:{ip}`
- [ ] Cache-backed (Redis in production)
- [ ] 5 failed attempts in 15 minutes = 30 minute lockout

### Rate Limit Implementation
```python
from django.core.cache import cache

def check_rate_limit(ip_address):
    cache_key = f"auth_rate_limit:{ip_address}"
    lockout_key = f"auth_lockout:{ip_address}"
    
    # Check if locked out
    if cache.get(lockout_key):
        return False
    
    # Get attempt count
    attempts = cache.get(cache_key, 0)
    
    if attempts >= 5:
        # Set lockout
        cache.set(lockout_key, True, timeout=1800)  # 30 minutes
        return False
    
    # Increment counter
    cache.set(cache_key, attempts + 1, timeout=900)  # 15 minutes
    return True
```

### API Rate Limiting
- [ ] DRF throttling uses cache backend
- [ ] Throttle keys namespaced: `throttle:scope:identifier`
- [ ] User-based and IP-based throttling
- [ ] Service-specific rate limits (extraction: 20/min)

## Performance Optimization

### Connection Pooling
- [ ] Connection pool configured in Django Redis settings
- [ ] Pool size appropriate for workload
- [ ] Connection timeout configured
- [ ] Health checks on connections

### Key Expiration
- [ ] Set appropriate TTL for all keys
- [ ] No keys without expiration (memory leak)
- [ ] Use `EXPIRE` command for dynamic TTL
- [ ] Monitor memory usage

### Memory Management (Azure Managed Redis)
- [ ] Choose appropriate tier based on memory needs
- [ ] Memory Optimized for high memory-to-vCPU ratio
- [ ] Compute Optimized for high throughput
- [ ] Flash Optimized for cost-effective large datasets
- [ ] Monitor memory usage and evictions

### Azure Managed Redis Eviction Policies
- [ ] `noeviction` - Return errors when memory limit reached (default)
- [ ] `allkeys-lru` - Evict least recently used keys (good for caching)
- [ ] `volatile-lru` - Evict LRU keys with expiration set
- [ ] `allkeys-random` - Evict random keys
- [ ] `volatile-ttl` - Evict keys with shortest TTL

## Persistence and Durability

### Azure Managed Redis Persistence
- [ ] Built-in high availability (multi-node replication)
- [ ] Automatic backups (RDB + AOF)
- [ ] Point-in-time recovery
- [ ] Zone redundancy in production
- [ ] Geo-replication for disaster recovery (optional)

### Local Development Persistence (Optional)
```yaml
# docker-compose.yml - Enable persistence for local Redis
services:
  redis:
    image: redis:8.2.0-bookworm
    command: redis-server --appendonly yes --appendfsync everysec
    volumes:
      - redis_data:/data
```

## Monitoring and Alerting

### Azure Managed Redis Metrics
- [ ] Memory usage
- [ ] Connection count
- [ ] Commands per second
- [ ] Hit/miss ratio
- [ ] Network throughput
- [ ] Replication lag (if using replication)

### Azure Monitor Integration
- [ ] Metrics exported to Azure Monitor
- [ ] Alerts configured for:
  - High memory usage (>80%)
  - High connection count
  - Low cache hit rate (<70%)
  - High latency (>10ms)
- [ ] Diagnostic logs enabled
- [ ] Integration with Azure Application Insights

### Django Monitoring
```python
from django.core.cache import cache
from django.core.cache.backends.redis import RedisCache

if isinstance(cache, RedisCache):
    client = cache._cache.get_client()
    info = client.info()
    memory_used = info['used_memory_human']
    connected_clients = info['connected_clients']
```

## Security

### Azure Managed Redis Security
- [ ] SSL/TLS 1.2+ enforced for all connections
- [ ] Access keys rotated regularly (primary and secondary keys)
- [ ] Microsoft Entra ID authentication (optional, in addition to keys)
- [ ] Private endpoints for VNet isolation (optional)
- [ ] Firewall rules configured (if not using Private Link)
- [ ] Compliance certifications: FedRAMP, HIPAA, PCI DSS, ISO 27001

### Network Security
- [ ] Redis not exposed to public internet (Azure Managed Redis handles this)
- [ ] Azure Container Apps connects via private networking
- [ ] Connection strings stored in Azure Key Vault
- [ ] Access keys in Key Vault, not in code or `.env` (production)

### Key Rotation
```bash
# Azure Managed Redis provides primary and secondary keys
# Rotate keys using Azure portal or CLI:
az redis regenerate-keys --name <cache-name> --key-type Primary

# Update Key Vault with new key:
az keyvault secret set --vault-name <vault-name> \
  --name redis-url \
  --value "rediss://:NEW_KEY@your-cache.redis.cache.windows.net:6380/0"

# Restart Azure Container Apps to pick up new key
az containerapp revision restart --name <app-name> \
  --resource-group <resource-group> \
  --revision <revision-name>
```

## High Availability

### Azure Managed Redis HA Features
- [ ] Multi-node replication (2+ replicas)
- [ ] Automatic failover
- [ ] Zone redundancy (Availability Zones)
- [ ] Active geo-replication (multi-region, optional)
- [ ] Up to 99.999% SLA with multi-region Active-Active

### Geo-Replication (Optional)
- [ ] Configure for disaster recovery
- [ ] Multi-region Active-Active for global apps
- [ ] Sub-millisecond latency in each region
- [ ] Read and write from any region
- [ ] Conflict-free Replicated Data Types (CRDTs)

## Backup and Recovery

### Azure Managed Redis Backups
- [ ] Automatic daily backups
- [ ] Point-in-time recovery
- [ ] Backups stored in geo-redundant storage
- [ ] Export data to Azure Blob Storage
- [ ] Import data from Azure Blob Storage

### Backup Commands (Azure CLI)
```bash
# Export Redis data to Azure Blob Storage
az redis export --name <cache-name> \
  --resource-group <resource-group> \
  --container <blob-container-url> \
  --prefix backup-$(date +%Y%m%d)

# Import Redis data from Azure Blob Storage
az redis import --name <cache-name> \
  --resource-group <resource-group> \
  --files <blob-url>
```

## Azure Container Apps Integration

### Container Apps Configuration
- [ ] Environment variables from Azure Key Vault
- [ ] Redis connection strings as secrets
- [ ] Managed identity for Key Vault access
- [ ] Private networking to Azure Managed Redis
- [ ] Health checks configured

### Container Apps Environment Variables
```yaml
# Azure Container Apps revision configuration
properties:
  configuration:
    secrets:
      - name: redis-url
        keyVaultUrl: https://your-vault.vault.azure.net/secrets/redis-url
      - name: celery-broker-url
        keyVaultUrl: https://your-vault.vault.azure.net/secrets/celery-broker-url
  template:
    containers:
      - name: web
        image: your-image:tag
        env:
          - name: REDIS_URL
            secretRef: redis-url
          - name: CELERY_BROKER_URL
            secretRef: celery-broker-url
          - name: ENVIRONMENT
            value: production
```

## Common Patterns

### Cache-Aside Pattern
```python
def get_document(document_id):
    cache_key = f"document:{document_id}"
    
    # Try cache first
    document = cache.get(cache_key)
    if document:
        return document
    
    # Cache miss - fetch from database
    document = Document.objects.get(id=document_id)
    
    # Store in cache
    cache.set(cache_key, document, timeout=3600)
    
    return document
```

### Cache Invalidation
```python
def update_document(document_id, **kwargs):
    # Update database
    Document.objects.filter(id=document_id).update(**kwargs)
    
    # Invalidate cache
    cache_key = f"document:{document_id}"
    cache.delete(cache_key)
```

### Write-Through Cache
```python
def save_document(document):
    # Save to database
    document.save()
    
    # Update cache
    cache_key = f"document:{document.id}"
    cache.set(cache_key, document, timeout=3600)
```

### Distributed Lock
```python
import uuid

def acquire_lock(lock_name, timeout=10):
    lock_key = f"lock:{lock_name}"
    identifier = str(uuid.uuid4())
    
    # Try to acquire lock
    if cache.add(lock_key, identifier, timeout=timeout):
        return identifier
    return None

def release_lock(lock_name, identifier):
    lock_key = f"lock:{lock_name}"
    cached_id = cache.get(lock_key)
    
    if cached_id == identifier:
        cache.delete(lock_key)
        return True
    return False
```

## Testing

### Local Testing
- [ ] Use Docker Redis for tests (same as development)
- [ ] Separate Redis DB for tests (e.g., DB 15)
- [ ] Flush test DB before/after tests
- [ ] Docker Compose with test services

### Test Setup
```python
from django.test import TestCase, override_settings

@override_settings(CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://localhost:6379/15',  # Test DB
    }
})
class CacheTestCase(TestCase):
    def setUp(self):
        cache.clear()  # Clear cache before each test
    
    def test_cache_operations(self):
        cache.set('test_key', 'test_value')
        self.assertEqual(cache.get('test_key'), 'test_value')
```

## Migration from Azure Cache for Redis

### Migration Checklist
- [ ] Review current tier (Basic/Standard/Premium/Enterprise)
- [ ] Select appropriate Azure Managed Redis tier
- [ ] Note: Azure Cache for Redis retiring (Sept 30, 2028 for Basic/Standard/Premium)
- [ ] Export data from old cache
- [ ] Create new Azure Managed Redis instance
- [ ] Import data to new cache
- [ ] Update connection strings in Azure Key Vault
- [ ] Test application with new cache
- [ ] Switch over during maintenance window
- [ ] Monitor for issues
- [ ] Decommission old cache after validation period

### Benefits of Azure Managed Redis
- [ ] 15x greater throughput performance
- [ ] Advanced features: vector search, JSON, time series
- [ ] Built on Redis Enterprise 7.4+ (vs community Redis)
- [ ] Better SLA (up to 99.999% vs 99.9%)
- [ ] Cost-effective TCO
- [ ] Faster cache creation (3.1x) and scaling (2.2x)

## Troubleshooting

### Connection Issues (Local)
- Check Docker container running: `docker ps`
- Verify port 6379 not in use: `lsof -i :6379`
- Check Redis logs: `docker logs redis`
- Test connection: `docker exec redis redis-cli ping`

### Connection Issues (Production)
- Verify SSL/TLS enabled (rediss:// not redis://)
- Check access key from Azure portal
- Verify port 6380 (SSL port, not 6379)
- Check Azure Managed Redis firewall rules
- Verify Azure Container Apps networking
- Check Key Vault access permissions

### Memory Issues
- Monitor memory usage in Azure portal
- Check eviction policy appropriate
- Review key expiration settings
- Scale to higher tier if needed
- Consider Flash Optimized tier for large datasets

### Performance Issues
- Check Azure Monitor metrics
- Review slow commands in Azure portal
- Monitor connection pool settings
- Check network latency from Container Apps to Redis
- Consider Compute Optimized tier for high throughput

## Best Practices Summary

1. **Use Docker locally** - redis:8.2.0-bookworm for consistency
2. **Use Azure Managed Redis in production** - Superior to Azure Cache for Redis
3. **Store secrets in Azure Key Vault** - Never in code or container images
4. **Use dedicated databases** - Separate DBs for different purposes
5. **Set expiration** - All keys should have TTL to prevent memory leaks
6. **Enable SSL/TLS** - Always use rediss:// in production
7. **Monitor metrics** - Azure Monitor for production insights
8. **Configure HA** - Zone redundancy and replication in production
9. **Namespace keys** - Use prefixes for organization
10. **Test with Docker Redis** - Same version as production where possible

## Cross-Reference

Related docs:
- `celery_best_practices.md` - Celery broker and results backend
- `channels_websockets_best_practices.md` - Channels layer configuration
- `cdn_sri_best_practices.md` - SRI cache usage
- `authentication_authorization_best_practices.md` - Rate limiting
- `performance_monitoring_best_practices.md` - Redis metrics
