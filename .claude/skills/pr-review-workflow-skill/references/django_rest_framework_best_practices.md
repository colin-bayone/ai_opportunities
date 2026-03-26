# Django REST Framework Best Practices

DRF patterns for your stack: DRF 3.16+, token authentication, URL path versioning, and integration with your custom auth system.

## API Versioning

### URL Path Versioning
- [ ] Versioning style set to `URLPathVersioning`
- [ ] Version in URL path: `/api/v1/endpoint/`, `/api/v2/endpoint/`
- [ ] `DEFAULT_VERSION` set (usually 'v1')
- [ ] `ALLOWED_VERSIONS` list defined (e.g., ['v1', 'v2'])
- [ ] Version accessible via `request.version`
- [ ] No version in URL defaults to `DEFAULT_VERSION`

### API URL Patterns
```python
urlpatterns = [
    path('api/v1/', include('myapp.api.v1.urls')),
    path('api/v2/', include('myapp.api.v2.urls')),
]
```

### Version-Specific Code
- [ ] Serializers organized by version: `serializers/v1.py`, `serializers/v2.py`
- [ ] Views organized by version: `views/v1.py`, `views/v2.py`
- [ ] Shared code in base classes
- [ ] Breaking changes only in new versions
- [ ] Deprecation notices for old versions

## Authentication

### Token Authentication
- [ ] `TokenAuthentication` in `DEFAULT_AUTHENTICATION_CLASSES`
- [ ] Token model used (`rest_framework.authtoken`)
- [ ] Tokens generated on user creation or explicitly
- [ ] Token in Authorization header: `Authorization: Token <token>`
- [ ] Token validation on each request
- [ ] Tokens never logged or exposed

### Custom Authentication Backend Integration
- [ ] Token authentication works with `StaffSSOOnlyBackend`
- [ ] Tokens respect multi-tenancy (client group)
- [ ] Token generation respects user type (staff vs external)
- [ ] Failed token auth logged for audit

### Service Account Authentication
- [ ] `IsAirflowServiceAccount` permission class for Airflow endpoints
- [ ] Service account tokens separate from user tokens
- [ ] Service accounts have limited permissions
- [ ] Service account usage audited

### Authentication Settings
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # For browsable API
    ],
}
```

## Permissions

### Default Permissions
- [ ] `DEFAULT_PERMISSION_CLASSES` set to `IsAuthenticated` (or stricter)
- [ ] Public endpoints explicitly use `AllowAny`
- [ ] Permission checks documented for each view

### Custom Permission Classes

#### IsAirflowServiceAccount
- [ ] Validates service account token
- [ ] Checks service account is active
- [ ] Used only on orchestration endpoints
- [ ] Returns 403 for non-service accounts

#### Client Group Permissions
- [ ] Custom permission class checks client group membership
- [ ] Validates user belongs to object's client group
- [ ] Used on multi-tenant endpoints
- [ ] Clear error messages for permission denied

### Permission Patterns
```python
class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasClientGroupAccess]
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), HasRole('admin')]
        return super().get_permissions()
```

## Throttling (Rate Limiting)

### Default Throttle Rates
- [ ] `DEFAULT_THROTTLE_RATES` configured
- [ ] Authenticated users: 1000/hour (adjust as needed)
- [ ] Anonymous users: Lower limit or blocked
- [ ] Burst vs sustained rate limiting

### Service-Specific Rate Limits
- [ ] Extraction service limits in settings:
  - Upload: 20/min per user
  - Get content: 100/min per user
  - Get metadata: 200/min per user
  - Bulk get: 20/min (each fetches up to 50 items)
- [ ] Custom throttle classes for service-specific limits
- [ ] Rate limit exceeded returns 429 status

### Throttle Classes
```python
class ExtractionUploadThrottle(UserRateThrottle):
    rate = '20/min'
    scope = 'extraction_upload'

class ExtractionBulkThrottle(UserRateThrottle):
    rate = '20/min'
    scope = 'extraction_bulk'
```

### Rate Limit Settings
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/hour',
        'extraction_upload': '20/min',
        'extraction_bulk': '20/min',
    }
}
```

## Serializers

### ModelSerializer Best Practices
- [ ] Use `ModelSerializer` over `Serializer` when possible
- [ ] Explicitly list fields in `Meta.fields` (avoid `'__all__'`)
- [ ] Use `read_only_fields` for fields that shouldn't be updated
- [ ] Validate field-level with `validate_<field_name>()`
- [ ] Validate object-level with `validate()`
- [ ] Return serialized data, not model instance

### Client Group Filtering in Serializers
- [ ] Serializers filter related objects by client group
- [ ] `to_representation()` enforces client group boundaries
- [ ] Nested serializers respect client group context
- [ ] No cross-tenant data leakage

### Serializer Validation
- [ ] All user input validated
- [ ] Custom validators for complex business logic
- [ ] Raise `ValidationError` with clear messages
- [ ] Validation errors logged (without sensitive data)

### Version-Specific Serializers
- [ ] V1 serializers in `serializers/v1.py`
- [ ] V2 serializers in `serializers/v2.py`
- [ ] Shared logic in base serializer
- [ ] V2 can add fields, rename fields, change validation
- [ ] Breaking changes only in new versions

## ViewSets and Views

### ViewSet Organization
- [ ] Use `ModelViewSet` for full CRUD
- [ ] Use `ReadOnlyModelViewSet` for read-only endpoints
- [ ] Use `GenericAPIView` with mixins for custom combinations
- [ ] Use `APIView` for non-model endpoints

### Queryset Filtering
- [ ] `get_queryset()` filters by client group
- [ ] `get_queryset()` filters by user permissions
- [ ] No unfiltered querysets returned
- [ ] Prefetch/select related for performance

### Client Group Context
```python
class MyViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        client_group = self.request.session.get('client_group_id')
        return MyModel.objects.filter(client_group_id=client_group)
    
    def perform_create(self, serializer):
        client_group_id = self.request.session.get('client_group_id')
        serializer.save(
            client_group_id=client_group_id,
            created_by=self.request.user
        )
```

### Action Decorators
- [ ] `@action(detail=True)` for custom object actions
- [ ] `@action(detail=False)` for custom list actions
- [ ] Specify HTTP methods: `methods=['post']`
- [ ] Custom permissions per action
- [ ] URL name auto-generated: `{basename}-{action-name}`

## Response Formatting

### Standard Response Format
- [ ] Consistent response structure across endpoints
- [ ] Success responses include data
- [ ] Error responses include error details
- [ ] Status codes follow HTTP standards

### Status Codes
- [ ] 200 OK - Successful GET, PUT, PATCH
- [ ] 201 Created - Successful POST
- [ ] 204 No Content - Successful DELETE
- [ ] 400 Bad Request - Validation errors
- [ ] 401 Unauthorized - Authentication required
- [ ] 403 Forbidden - Permission denied
- [ ] 404 Not Found - Resource not found
- [ ] 429 Too Many Requests - Rate limit exceeded
- [ ] 500 Internal Server Error - Server errors

### Error Response Format
```json
{
    "error": "Validation failed",
    "details": {
        "field_name": ["Error message"]
    }
}
```

## Pagination

### Pagination Settings
- [ ] `DEFAULT_PAGINATION_CLASS` set
- [ ] `PAGE_SIZE` configured (e.g., 50, 100)
- [ ] Use `PageNumberPagination` or `LimitOffsetPagination`
- [ ] Large datasets always paginated
- [ ] Pagination metadata in response

### Custom Pagination
```python
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
```

## Filtering, Searching, Ordering

### Django Filters
- [ ] `django-filter` backend configured (if used)
- [ ] Filterset classes for complex filtering
- [ ] Filter by client group always included
- [ ] Filter parameters documented

### Search
- [ ] `SearchFilter` backend for text search
- [ ] `search_fields` defined on viewsets
- [ ] Search works with pagination
- [ ] Search across related models if needed

### Ordering
- [ ] `OrderingFilter` backend for sorting
- [ ] `ordering_fields` defined
- [ ] Default ordering set
- [ ] Ordering by multiple fields supported

## File Uploads via API

### File Upload Endpoints
- [ ] File size limits enforced (same as web: 2MB, 5MB, 10MB)
- [ ] Magika validation applied
- [ ] Content-type validation
- [ ] Multipart form data handled correctly
- [ ] File upload rate limited

### File Upload Serializer
```python
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    
    def validate_file(self, value):
        # Use Magika validator
        validate_file_upload(value, max_size_mb=5)
        return value
```

### File Response
- [ ] File downloads authenticated
- [ ] Content-Type header set correctly
- [ ] Content-Disposition for downloads
- [ ] Streaming for large files
- [ ] Azure Blob URLs for stored files

## Testing API Endpoints

### APITestCase
- [ ] Use `rest_framework.test.APITestCase`
- [ ] `APIClient` for making requests
- [ ] Token authentication in tests
- [ ] Test all CRUD operations
- [ ] Test permissions and authorization

### Test Patterns
```python
class MyAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(...)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
    
    def test_list_endpoint(self):
        response = self.client.get('/api/v1/myendpoint/')
        self.assertEqual(response.status_code, 200)
```

### Test Coverage
- [ ] Test successful requests (2xx)
- [ ] Test validation errors (400)
- [ ] Test authentication required (401)
- [ ] Test permission denied (403)
- [ ] Test not found (404)
- [ ] Test rate limiting (429)

## API Documentation

### Browsable API
- [ ] Browsable API enabled in dev (`SessionAuthentication`)
- [ ] Browsable API disabled in production (or protected)
- [ ] Custom templates for browsable API (optional)

### Schema Generation
- [ ] Schema generated with `drf-spectacular` or built-in
- [ ] Schema endpoint: `/api/schema/`
- [ ] OpenAPI 3.0 format
- [ ] Descriptions for endpoints and fields
- [ ] Examples in schema

### API Documentation Views
- [ ] Swagger UI or ReDoc for interactive docs
- [ ] Documentation accessible to authenticated users
- [ ] Examples of requests and responses
- [ ] Authentication instructions

## Security

### Input Validation
- [ ] All input validated in serializers
- [ ] File uploads validated with Magika
- [ ] No raw SQL queries from user input
- [ ] Query parameters validated

### Output Sanitization
- [ ] No sensitive data in responses (passwords, tokens, internal IDs)
- [ ] PII masked if logged
- [ ] Client group boundaries enforced
- [ ] No error stack traces in production

### CORS
- [ ] CORS headers configured if needed (`django-cors-headers`)
- [ ] Allowed origins whitelist (no `*`)
- [ ] Allowed methods specified
- [ ] Credentials allowed only if necessary

## Performance

### Query Optimization
- [ ] `select_related()` for foreign keys
- [ ] `prefetch_related()` for reverse FKs and M2M
- [ ] `only()` to fetch specific fields
- [ ] `defer()` to exclude large fields
- [ ] Pagination for large datasets

### Caching
- [ ] Cache expensive calculations
- [ ] Cache external API calls
- [ ] Use Redis cache backend
- [ ] Cache invalidation on updates
- [ ] Cache-Control headers set

### Async Views (if using)
- [ ] Views marked `async def` where appropriate
- [ ] Database queries use `sync_to_async` if needed
- [ ] External API calls async
- [ ] Error handling for async views

## Celery Integration

### Async Task Triggering
- [ ] Long-running operations triggered via Celery
- [ ] Task ID returned to client
- [ ] Status endpoint for task progress
- [ ] Task results cached for retrieval
- [ ] Task errors handled gracefully

### Task Status Endpoint
```python
@api_view(['GET'])
def task_status(request, task_id):
    task = AsyncResult(task_id)
    return Response({
        'state': task.state,
        'result': task.result if task.ready() else None
    })
```

## Extraction Service API (Example)

Based on your extraction service rate limits:

### Upload Endpoint
- [ ] Rate limit: 20 uploads/min per user
- [ ] File validation with Magika
- [ ] Returns extraction job ID
- [ ] Triggers Celery task
- [ ] Client group context captured

### Get Content Endpoint
- [ ] Rate limit: 100/min per user
- [ ] Retrieves extracted content by ID
- [ ] Filters by client group
- [ ] Returns cached results if available

### Get Metadata Endpoint
- [ ] Rate limit: 200/min per user
- [ ] Returns metadata without full content
- [ ] Lightweight response

### Bulk Get Endpoint
- [ ] Rate limit: 20/min (each fetches up to 50 items = 1000 max/min)
- [ ] Accepts list of IDs
- [ ] Returns results for IDs user has access to
- [ ] Efficient bulk query

## Common Patterns

### Client Group Filtering ViewSet
```python
class ClientGroupFilteredViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        client_group_id = self.request.session.get('client_group_id')
        return self.queryset.filter(client_group_id=client_group_id)
    
    def perform_create(self, serializer):
        client_group_id = self.request.session.get('client_group_id')
        serializer.save(client_group_id=client_group_id)
```

### Version-Based View Selection
```python
from rest_framework.views import APIView

class MyAPIView(APIView):
    def get_serializer_class(self):
        if self.request.version == 'v1':
            return MySerializerV1
        elif self.request.version == 'v2':
            return MySerializerV2
        return MySerializerV1  # default
```

### Service-Specific Throttling
```python
class ExtractionUploadView(APIView):
    throttle_classes = [ExtractionUploadThrottle]
    
    def post(self, request):
        # Handle upload
        pass
```

## Troubleshooting

### 401 Unauthorized on valid token
- Check token in Authorization header format: `Token <token>`
- Verify `TokenAuthentication` in `DEFAULT_AUTHENTICATION_CLASSES`
- Check token exists in database

### Rate limit not working
- Verify throttle classes configured
- Check cache backend for throttling (Redis recommended)
- Verify throttle scope matches view

### Cross-tenant data leakage
- Check `get_queryset()` filters by client group
- Verify serializer doesn't expose related objects from other tenants
- Test with users from different client groups

### Pagination not working
- Check `DEFAULT_PAGINATION_CLASS` set
- Verify `PAGE_SIZE` configured
- Check queryset returns multiple items

## Cross-Reference

Related docs:
- `authentication_authorization_best_practices.md` - Auth integration
- `celery_best_practices.md` - Async task patterns
- `redis_best_practices.md` - Cache backend for throttling
- `web_security_best_practices.md` - API security
- `soc2_considerations.md` - Audit logging for API
