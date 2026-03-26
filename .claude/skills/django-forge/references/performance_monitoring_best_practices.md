# Performance Monitoring Best Practices

Performance monitoring patterns using MetricsCollector and system diagnostics.

## MetricsCollector Service

### Core Functionality
**Check in PR**:
- [ ] Singleton pattern (one instance per process)
- [ ] Thread-safe data structures
- [ ] Tracks last 1000 requests
- [ ] Error counts by status code
- [ ] Endpoint statistics
- [ ] CPU/memory usage (psutil)
- [ ] Minimal performance impact

### Metrics Tracked
- [ ] Request times (per endpoint)
- [ ] Error counts (4xx, 5xx)
- [ ] Request volume (requests/minute)
- [ ] Endpoint hit counts
- [ ] Response status distribution
- [ ] System resources (CPU, memory, threads)

## MetricsMiddleware Integration

### Middleware Pattern
**Check in PR**:
- [ ] Placed after auth middleware
- [ ] Times each request
- [ ] Records status code
- [ ] Captures endpoint path
- [ ] Updates MetricsCollector
- [ ] No exceptions suppress errors
- [ ] Minimal overhead

### Data Collection
**Check in PR**:
- [ ] Request start time captured
- [ ] Duration calculated in milliseconds
- [ ] Endpoint path normalized (remove IDs)
- [ ] User context included (if needed)
- [ ] Client group context (for multi-tenancy)

## Monitoring Endpoints

### /monitor/ Dashboard
**Check in PR**:
- [ ] DEBUG-only or admin-only access
- [ ] HTML dashboard with charts
- [ ] Real-time metrics display
- [ ] Recent requests list
- [ ] Error rate visualization
- [ ] System resource usage

### /monitor/metrics/ API
**Check in PR**:
- [ ] JSON endpoint for programmatic access
- [ ] Authenticated access only
- [ ] Structured metrics data
- [ ] Prometheus format (optional)
- [ ] Rate limit on metrics endpoint

## System Metrics (psutil)

### Resource Monitoring
**Check in PR**:
- [ ] CPU usage percentage
- [ ] Memory usage (RSS, available)
- [ ] Thread count
- [ ] Open file descriptors (if available)
- [ ] Network connections (if available)
- [ ] Process uptime

### Collection Frequency
**Check in PR**:
- [ ] System metrics cached (expensive to collect)
- [ ] Cache duration: 10-30 seconds
- [ ] On-demand collection for dashboard
- [ ] Async collection for heavy metrics
- [ ] Error handling for unavailable metrics

## Performance Thresholds

### Alerting Thresholds
**Define in settings**:
- [ ] Slow request threshold (e.g., >2 seconds)
- [ ] Error rate threshold (e.g., >5% errors)
- [ ] Memory usage threshold (e.g., >80%)
- [ ] CPU usage threshold (e.g., >90%)
- [ ] Alert channels configured

### Logging Slow Requests
**Check in PR**:
- [ ] Requests exceeding threshold logged
- [ ] Include endpoint, duration, user
- [ ] Include query count (N+1 detection)
- [ ] Stack trace for very slow requests (>5s)
- [ ] Alert on repeated slow endpoints

## Database Query Monitoring

### Query Counting
**Check in PR**:
- [ ] Count queries per request (django-debug-toolbar in dev)
- [ ] Log requests with excessive queries (>20)
- [ ] Track query time per request
- [ ] Identify N+1 query patterns
- [ ] Alert on query explosions

### Slow Query Detection
**Check in PR**:
- [ ] Database slow query log enabled (PostgreSQL)
- [ ] Threshold: >100ms queries logged
- [ ] Queries analyzed with EXPLAIN ANALYZE
- [ ] Missing indexes identified
- [ ] Query optimization documented

## Cache Monitoring

### Redis Cache Metrics
**Check in PR**:
- [ ] Hit/miss ratio tracked
- [ ] Key count monitored
- [ ] Memory usage monitored
- [ ] Eviction count tracked
- [ ] Connection pool status

### Cache Performance
**Check in PR**:
- [ ] Cache latency measured
- [ ] Miss patterns identified
- [ ] Cache warming strategies
- [ ] TTL effectiveness analyzed
- [ ] Invalidation patterns reviewed

## Celery Task Monitoring

### Task Performance
**Check in PR**:
- [ ] Task execution time tracked
- [ ] Failed task count monitored
- [ ] Queue length monitored
- [ ] Worker utilization tracked
- [ ] Task retry patterns analyzed

### Flower Integration
**Check in PR**:
- [ ] Flower dashboard accessible
- [ ] Authentication enabled
- [ ] Real-time task monitoring
- [ ] Worker health checks
- [ ] Historical task data available

## API Performance Monitoring

### Endpoint Metrics
**Check in PR**:
- [ ] Per-endpoint response times
- [ ] Request volume per endpoint
- [ ] Error rates per endpoint
- [ ] Payload sizes tracked
- [ ] Rate limit hit counts

### DRF Monitoring
**Check in PR**:
- [ ] Serializer performance tracked
- [ ] Query count per API call
- [ ] Throttle status monitored
- [ ] Token validation time tracked

## Real-Time Monitoring

### WebSocket Monitoring
**Check in PR**:
- [ ] Active WebSocket connections count
- [ ] Message rate per connection
- [ ] Connection duration tracked
- [ ] Disconnect reasons logged
- [ ] Channel layer health checked

### Streaming Monitoring
**Check in PR**:
- [ ] Streaming response times
- [ ] Chunk delivery rate
- [ ] Client disconnects tracked
- [ ] Buffer usage monitored

## External Service Monitoring

### Azure Service Health
**Check in PR**:
- [ ] Azure OpenAI: latency, token usage, errors
- [ ] Azure Blob Storage: upload/download times, errors
- [ ] Azure AI Search: query times, indexing status
- [ ] Third-party API: response times, error rates

### Circuit Breaker Pattern
**Check in PR**:
- [ ] Circuit breaker for external services (optional)
- [ ] Fail fast on repeated failures
- [ ] Automatic recovery attempts
- [ ] Fallback behavior defined
- [ ] Circuit state monitored

## Performance Testing

### Load Testing
**Check in PR**:
- [ ] Load tests before production deployment
- [ ] Baseline performance documented
- [ ] Peak load tested (2-3x normal)
- [ ] Degradation patterns identified
- [ ] Bottlenecks documented

### Profiling
**Check in PR**:
- [ ] Profile slow endpoints with cProfile or similar
- [ ] Identify hot spots in code
- [ ] Database query analysis
- [ ] Memory profiling for leaks
- [ ] Regular profiling in staging

## Alerting

### Alert Conditions
**Check in PR**:
- [ ] Error rate >5% for 5 minutes
- [ ] Slow requests >10% for 5 minutes
- [ ] Memory usage >80%
- [ ] CPU usage >90% for 2 minutes
- [ ] Database connections exhausted
- [ ] Celery queue backlog >100
- [ ] External service failures

### Alert Channels
**Check in PR**:
- [ ] Email alerts for critical issues
- [ ] Slack/Teams integration
- [ ] PagerDuty for on-call (production)
- [ ] Alert severity levels defined
- [ ] Alert escalation paths

## Dashboard and Visualization

### Monitoring Dashboard
**Check in PR**:
- [ ] Real-time metrics display
- [ ] Historical trend charts
- [ ] Error rate visualization
- [ ] Endpoint performance comparison
- [ ] System resource graphs

### External Monitoring
**Check in PR**:
- [ ] Prometheus/Grafana integration (optional)
- [ ] Application Insights (Azure)
- [ ] Custom dashboards
- [ ] SLA tracking
- [ ] Uptime monitoring

## Logging Integration

### Structured Logging
**Check in PR**:
- [ ] JSON structured logs
- [ ] Request ID in all logs
- [ ] Duration logged for operations
- [ ] PII masked in logs (Presidio)
- [ ] Log aggregation (ELK, Azure Monitor)

### Log Levels
**Check in PR**:
- [ ] DEBUG: Development only
- [ ] INFO: Normal operations, request lifecycle
- [ ] WARNING: Degraded performance, retries
- [ ] ERROR: Failures, exceptions
- [ ] CRITICAL: System failures, security events

## Performance Optimization Workflow

### Identify Issues
1. Monitor metrics for anomalies
2. Check slow request logs
3. Analyze database queries
4. Review cache hit rates
5. Check external service latency

### Diagnose Root Cause
- [ ] Profile slow endpoints
- [ ] Analyze database query plans
- [ ] Check for N+1 queries
- [ ] Review cache strategy
- [ ] Check system resources

### Implement Fix
- [ ] Add database indexes
- [ ] Optimize queries with select_related/prefetch_related
- [ ] Implement caching
- [ ] Async processing with Celery
- [ ] Optimize algorithm/logic

### Verify Improvement
- [ ] Re-test with same load
- [ ] Compare before/after metrics
- [ ] Monitor for regressions
- [ ] Update performance baselines
- [ ] Document optimization

## Testing Performance Changes

### Benchmark Tests
**Check in PR**:
- [ ] Benchmark critical endpoints before/after changes
- [ ] Use consistent test data
- [ ] Run multiple iterations for average
- [ ] Test under load (concurrent requests)
- [ ] Document results

### Regression Detection
**Check in PR**:
- [ ] Performance tests in CI/CD
- [ ] Alert on >20% degradation
- [ ] Compare against baseline
- [ ] Profile changes that degrade performance
- [ ] Block merges with major regressions

## Common Performance Issues

### Database Issues
- [ ] N+1 queries (missing select_related/prefetch_related)
- [ ] Missing indexes
- [ ] Large result sets without pagination
- [ ] Complex queries without optimization
- [ ] Connection pool exhaustion

### Caching Issues
- [ ] Low cache hit rate
- [ ] Cache misses for common queries
- [ ] Incorrect TTL values
- [ ] Cache stampede on expiration
- [ ] Over-caching (memory issues)

### Code Issues
- [ ] Synchronous external API calls
- [ ] Large file processing in request
- [ ] Unnecessary serialization
- [ ] Inefficient algorithms
- [ ] Memory leaks

## Troubleshooting

### High Response Times
1. Check database query count and times
2. Check cache hit rate
3. Check external service latency
4. Profile endpoint code
5. Check system resources

### High Error Rates
1. Check error logs for patterns
2. Review recent deployments
3. Check external service status
4. Verify database connectivity
5. Check resource constraints

### Memory Leaks
1. Profile memory usage over time
2. Check for unclosed connections
3. Review cache usage
4. Check thread-local cleanup
5. Analyze object retention

## Cross-Reference

Related docs:
- `custom_middleware_best_practices.md` - MetricsMiddleware patterns
- `postgresql_best_practices.md` - Database monitoring
- `redis_best_practices.md` - Cache monitoring
- `celery_best_practices.md` - Task monitoring
- `azure_openai_best_practices.md` - External service monitoring
- `django_best_practices.md` - Query optimization
