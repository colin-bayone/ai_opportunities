# Celery Best Practices

Async task processing with Celery 5.5+ and Redis broker based on your stack.

## Celery Configuration

### Broker and Backend
- [ ] Redis used as message broker
- [ ] Redis used as results backend
- [ ] `CELERY_BROKER_URL` configured (e.g., `redis://localhost:6379/0`)
- [ ] `CELERY_RESULT_BACKEND` configured (same or different Redis DB)
- [ ] Connection pooling enabled
- [ ] Broker connection retry on startup

### Settings
```python
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
```

### Task Configuration
- [ ] `CELERY_TASK_SERIALIZER = 'json'` (not pickle for security)
- [ ] `CELERY_ACCEPT_CONTENT = ['json']` (whitelist)
- [ ] `CELERY_TASK_TRACK_STARTED = True` (for task monitoring)
- [ ] `CELERY_TASK_TIME_LIMIT` set for long-running tasks
- [ ] `CELERY_TASK_SOFT_TIME_LIMIT` set (softer limit before hard kill)

### Result Expiration
- [ ] `CELERY_RESULT_EXPIRES` set (e.g., 3600 seconds = 1 hour)
- [ ] Results cleaned up automatically
- [ ] Critical results saved to database before expiration
- [ ] Task IDs returned to client for status checking

## Task Definitions

### Task Decorator
- [ ] Tasks defined with `@shared_task` (not `@app.task`)
- [ ] Task name specified explicitly: `@shared_task(name='myapp.mytask')`
- [ ] Binding tasks when needed: `@shared_task(bind=True)` for self reference
- [ ] Default retry settings: `autoretry_for`, `retry_kwargs`, `max_retries`

### Task Organization
- [ ] Tasks in `tasks.py` within each app
- [ ] Task names namespaced by app: `appname.taskname`
- [ ] Related tasks grouped together
- [ ] Shared tasks in common module if used across apps

### Task Example
```python
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(
    name='myapp.process_document',
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3, 'countdown': 60},
    time_limit=300,
    soft_time_limit=270
)
def process_document(self, document_id):
    try:
        # Task logic
        logger.info(f"Processing document {document_id}")
        # ...
        return {'status': 'success'}
    except Exception as exc:
        logger.error(f"Error processing document {document_id}: {exc}")
        raise self.retry(exc=exc)
```

## Task Invocation

### Calling Tasks Asynchronously
- [ ] Use `.delay()` for simple invocation: `task.delay(arg1, arg2)`
- [ ] Use `.apply_async()` for advanced options
- [ ] Specify queue: `apply_async(queue='high_priority')`
- [ ] Specify countdown/eta: `apply_async(countdown=60)` or `apply_async(eta=datetime)`
- [ ] Link tasks: `apply_async(link=other_task.signature())`

### Task Signatures
- [ ] Create signatures for complex workflows: `task.signature(args, kwargs)`
- [ ] Use `task.s()` shortcut: `task.s(arg1, arg2)`
- [ ] Chain tasks: `chain(task1.s(), task2.s(), task3.s())`
- [ ] Group tasks: `group(task1.s(), task2.s())`
- [ ] Chord (group + callback): `chord(group)(callback.s())`

### Return Values
- [ ] Task returns result that can be serialized to JSON
- [ ] Complex objects serialized to dict or string
- [ ] Results stored in Redis results backend
- [ ] Client retrieves result with task ID

## Error Handling

### Retry Logic
- [ ] Tasks configured with `autoretry_for` for specific exceptions
- [ ] `retry_kwargs` defines retry behavior (max_retries, countdown)
- [ ] Exponential backoff: `retry_backoff=True`, `retry_backoff_max=600`
- [ ] Manual retry: `self.retry(exc=exc, countdown=60)` (requires `bind=True`)

### Exception Handling
- [ ] Catch specific exceptions, not bare `except:`
- [ ] Log errors with context (task name, args, exc)
- [ ] Don't retry on non-recoverable errors
- [ ] Store error details for debugging
- [ ] Notify on critical failures

### Task Failure Callbacks
```python
@shared_task
def on_failure_callback(request, exc, traceback):
    logger.error(f"Task {request.id} failed: {exc}")
    # Send notification, log to database, etc.
```

## Task Monitoring

### Task State
- [ ] Check task state with `AsyncResult(task_id).state`
- [ ] States: PENDING, STARTED, SUCCESS, FAILURE, RETRY, REVOKED
- [ ] Use `ready()` to check if task completed
- [ ] Use `successful()` to check if task succeeded
- [ ] Use `failed()` to check if task failed

### Task Results
```python
from celery.result import AsyncResult

task = AsyncResult(task_id)
if task.ready():
    if task.successful():
        result = task.result
    elif task.failed():
        error = task.info  # Exception instance
```

### Progress Tracking
- [ ] Update task state during execution: `self.update_state(state='PROGRESS', meta={...})`
- [ ] Store progress in meta: `meta={'current': 50, 'total': 100}`
- [ ] Client polls task status endpoint
- [ ] WebSocket notifications for real-time updates

## Queues and Routing

### Queue Configuration
- [ ] Define queues in `CELERY_TASK_ROUTES`
- [ ] Default queue: 'default'
- [ ] Priority queues: 'high_priority', 'low_priority'
- [ ] App-specific queues: 'extraction', 'parsing'
- [ ] Dedicated queues for resource-intensive tasks

### Task Routing
```python
CELERY_TASK_ROUTES = {
    'myapp.high_priority_task': {'queue': 'high_priority'},
    'myapp.slow_task': {'queue': 'low_priority'},
    'extraction.*': {'queue': 'extraction'},
}
```

### Worker Configuration
- [ ] Start workers for specific queues: `celery -A project worker -Q high_priority`
- [ ] Multiple workers for different queues
- [ ] Worker concurrency: `-c 4` (4 worker processes)
- [ ] Worker pool: `--pool=prefork` (default) or `gevent`, `eventlet`

## Periodic Tasks

### Celery Beat
- [ ] `CELERY_BEAT_SCHEDULE` configured for periodic tasks
- [ ] Schedule defined with `crontab` or `timedelta`
- [ ] Beat scheduler runs separately: `celery -A project beat`
- [ ] Beat schedule stored in Django database (`django_celery_beat`)

### Periodic Task Example
```python
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'cleanup-old-files': {
        'task': 'myapp.cleanup_old_files',
        'schedule': crontab(hour=2, minute=0),  # 2 AM daily
    },
    'process-pending-jobs': {
        'task': 'myapp.process_pending_jobs',
        'schedule': timedelta(minutes=5),  # Every 5 minutes
    },
}
```

### Beat Scheduler
- [ ] Only one beat scheduler instance running
- [ ] Beat scheduler separate from workers
- [ ] Beat uses database scheduler for dynamic schedules
- [ ] `django-celery-beat` app installed and migrated

## Integration with Django

### Task Context
- [ ] Client group context passed to task if needed
- [ ] User ID passed to task (not user object)
- [ ] Task fetches objects from database using IDs
- [ ] No request object passed to tasks

### Database Transactions
- [ ] Tasks committed to queue after database transaction
- [ ] Use `transaction.on_commit()` to delay task until commit
- [ ] Avoid race conditions between view and task
- [ ] Task re-fetches objects to get latest state

### Transaction Pattern
```python
from django.db import transaction

@transaction.atomic
def my_view(request):
    obj = MyModel.objects.create(...)
    transaction.on_commit(lambda: process_object.delay(obj.id))
```

### Audit Logging in Tasks
- [ ] Tasks create audit log entries
- [ ] Task captures user context (passed as argument)
- [ ] `AuditService` used in tasks
- [ ] Task execution audited with `@audit_command` if exposed as management command

## Performance Optimization

### Task Granularity
- [ ] Tasks fine-grained (seconds to minutes, not hours)
- [ ] Long tasks split into smaller chunks
- [ ] Use chains for multi-step workflows
- [ ] Avoid tasks calling other tasks synchronously

### Prefetching
- [ ] Worker prefetch multiplier configured: `CELERY_WORKER_PREFETCH_MULTIPLIER = 4`
- [ ] Lower multiplier for long-running tasks (1-2)
- [ ] Higher multiplier for fast tasks (4-8)
- [ ] Prevents workers from prefetching too many tasks

### Concurrency
- [ ] Worker concurrency matches CPU cores (for CPU-bound tasks)
- [ ] Higher concurrency for I/O-bound tasks
- [ ] Use gevent/eventlet for I/O-heavy workloads
- [ ] Monitor worker utilization

### Result Storage
- [ ] Only store results if needed
- [ ] Use `ignore_result=True` for fire-and-forget tasks
- [ ] Results expire automatically (`CELERY_RESULT_EXPIRES`)
- [ ] Critical results saved to database before expiration

## Security

### Task Arguments
- [ ] No sensitive data in task arguments (logged and stored)
- [ ] Pass object IDs, not objects
- [ ] Fetch sensitive data inside task
- [ ] Validate all task arguments

### Task Authorization
- [ ] Tasks check user permissions if needed
- [ ] Client group boundaries enforced
- [ ] User ID validated before processing
- [ ] No privilege escalation through tasks

### Broker Security
- [ ] Redis password configured (`redis://:password@host:port/db`)
- [ ] Redis only accessible from app servers (firewall)
- [ ] TLS for Redis connection in production (if supported)
- [ ] No public access to Redis

## Logging

### Task Logger
- [ ] Use `get_task_logger(__name__)` in tasks
- [ ] Task name, ID, args logged automatically
- [ ] Log task start, success, failure
- [ ] PII masked in logs (via Presidio)
- [ ] Structured logging for parsing

### Log Levels
- [ ] INFO for task lifecycle (start, success)
- [ ] WARNING for retries
- [ ] ERROR for failures after retries
- [ ] DEBUG for detailed execution steps

## Testing Celery Tasks

### Eager Mode
- [ ] `CELERY_TASK_ALWAYS_EAGER = True` in test settings
- [ ] Tasks execute synchronously in tests
- [ ] No Celery worker needed for tests
- [ ] Test task logic without async complexity

### Task Testing Patterns
```python
from django.test import TestCase, override_settings

@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class TaskTestCase(TestCase):
    def test_my_task(self):
        result = my_task.delay(arg1, arg2)
        self.assertTrue(result.successful())
        self.assertEqual(result.result, expected_value)
```

### Integration Tests
- [ ] Test task with real Redis in integration tests
- [ ] Test retry logic
- [ ] Test error handling
- [ ] Test periodic tasks

## Monitoring and Alerting

### Flower
- [ ] Flower dashboard for monitoring: `celery -A project flower`
- [ ] View active tasks, workers, queues
- [ ] Monitor task success/failure rates
- [ ] Protected with authentication

### Metrics
- [ ] Track task execution time
- [ ] Monitor queue lengths
- [ ] Alert on task failures
- [ ] Alert on worker downtime
- [ ] Integrate with monitoring system (e.g., Prometheus)

### Health Checks
- [ ] Periodic task to verify workers alive
- [ ] Check Redis connection
- [ ] Monitor task latency
- [ ] Alert on degraded performance

## Deployment

### Worker Process Management
- [ ] Systemd or Supervisor to manage Celery workers
- [ ] Auto-restart on failure
- [ ] Graceful shutdown on deploy
- [ ] Multiple worker processes for redundancy

### Beat Scheduler Management
- [ ] Only one beat scheduler instance
- [ ] Beat in separate process/container
- [ ] Auto-restart on failure
- [ ] Beat schedule backed up

### Docker Deployment
- [ ] Separate containers: web, worker, beat
- [ ] Workers scale horizontally
- [ ] Redis as external service
- [ ] Environment variables for configuration

## Common Patterns

### Document Processing Pipeline
```python
@shared_task
def extract_text(document_id):
    # Extract text from document
    return {'document_id': document_id, 'text': text}

@shared_task
def analyze_text(result):
    document_id = result['document_id']
    text = result['text']
    # Analyze text
    return {'document_id': document_id, 'analysis': analysis}

# Chain tasks
chain(extract_text.s(doc_id), analyze_text.s()).apply_async()
```

### Batch Processing
```python
@shared_task
def process_batch(item_ids):
    results = []
    for item_id in item_ids:
        result = process_item(item_id)
        results.append(result)
    return results

# Or use group for parallel processing
job = group(process_item.s(item_id) for item_id in item_ids)
result = job.apply_async()
```

### Periodic Cleanup
```python
@shared_task
def cleanup_old_files():
    cutoff = timezone.now() - timedelta(days=30)
    old_files = File.objects.filter(created_at__lt=cutoff)
    count = old_files.count()
    old_files.delete()
    return f"Deleted {count} old files"
```

## Troubleshooting

### Task not executing
- Check worker is running: `celery -A project inspect active`
- Verify task registered: `celery -A project inspect registered`
- Check queue routing configuration
- Verify Redis connection

### Task stuck in PENDING
- Worker not running or not consuming from queue
- Task routing incorrect (wrong queue)
- Redis connection issue
- Task not registered with worker

### Task retrying infinitely
- Check retry configuration (max_retries)
- Verify exception being caught is retriable
- Check logs for actual error
- Consider exponential backoff

### Results not available
- Check `CELERY_RESULT_BACKEND` configured
- Verify result hasn't expired (`CELERY_RESULT_EXPIRES`)
- Check Redis connection for results backend
- Ensure task returns serializable result

## Integration with Extraction Service

Based on your extraction service architecture:

### File Upload Task
```python
@shared_task(name='extraction.process_upload')
def process_upload(file_path, user_id, client_group_id):
    # Validate file with Magika
    # Extract content
    # Store in database
    # Cache results
    return extraction_id
```

### Rate Limiting Integration
- [ ] Tasks respect service rate limits
- [ ] Queue management prevents overload
- [ ] Monitor queue depth
- [ ] Back pressure if queue too long

## Cross-Reference

Related docs:
- `redis_best_practices.md` - Redis as broker and backend
- `django_rest_framework_best_practices.md` - API triggering tasks
- `performance_monitoring_best_practices.md` - Task monitoring
- `audit_logging_best_practices.md` - Auditing task execution
- `soc2_considerations.md` - Compliance for async operations
