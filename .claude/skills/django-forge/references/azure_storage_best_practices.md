# Azure Storage Best Practices

Azure Blob Storage for file storage and Azure Front Door for CDN with SRI security.

## Azure Blob Storage Configuration

### Storage Account Setup
- [ ] Storage account created in Azure
- [ ] Storage account name in environment variables
- [ ] Access keys or connection string in environment variables
- [ ] Different storage accounts for dev/staging/prod
- [ ] Geo-redundant storage (GRS) in production

### Connection Configuration
```python
# django-environ pattern
AZURE_STORAGE_ACCOUNT_NAME=your-storage-account
AZURE_STORAGE_ACCOUNT_KEY=your-access-key
# Or use connection string
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...
```

### Python SDK
- [ ] `azure-storage-blob` package installed
- [ ] `BlobServiceClient` configured
- [ ] Connection pooling enabled
- [ ] Retry policy configured
- [ ] Timeout settings appropriate

## Container Organization

### Container Structure
- [ ] Separate containers for different purposes
- [ ] `uploads` - User-uploaded files
- [ ] `outputs` - Generated files (PDFs, reports)
- [ ] `temp` - Temporary processing files
- [ ] `static` - Static assets (served via CDN)
- [ ] Client group isolation via blob prefixes or separate containers

### Container Access Levels
- [ ] Private containers (default) - Authentication required
- [ ] Blob-level access - Individual blob URLs with SAS tokens
- [ ] Container-level access - Only if needed for static assets
- [ ] Public access disabled unless explicitly needed

### Naming Conventions
```python
# Blob naming pattern with client group isolation
blob_name = f"{client_group_id}/{category}/{filename}"

# Examples:
# uploads: "123/resumes/john_doe_resume.pdf"
# outputs: "123/reports/monthly_report_2025_01.pdf"
# temp: "123/processing/doc_abc123.docx"
```

## File Upload Patterns

### Direct Upload to Blob Storage
```python
from azure.storage.blob import BlobServiceClient

def upload_file_to_blob(file, container_name, blob_name):
    # Get blob service client
    blob_service_client = BlobServiceClient.from_connection_string(
        settings.AZURE_STORAGE_CONNECTION_STRING
    )
    
    # Get blob client
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )
    
    # Upload file
    blob_client.upload_blob(
        file.read(),
        overwrite=False,  # Set True to overwrite existing
        content_settings=ContentSettings(content_type=file.content_type)
    )
    
    return blob_client.url
```

### Upload with Validation
- [ ] Validate file with Magika before upload
- [ ] Check file size limits
- [ ] Verify allowed file types
- [ ] Generate unique blob name (avoid collisions)
- [ ] Set appropriate content type

```python
from myapp.services import validate_file_upload

def validated_upload(file, container_name, client_group_id):
    # Validate file
    validate_file_upload(file, max_size_mb=10)
    
    # Generate blob name
    unique_id = uuid.uuid4().hex
    blob_name = f"{client_group_id}/uploads/{unique_id}_{file.name}"
    
    # Upload
    return upload_file_to_blob(file, container_name, blob_name)
```

### Chunked Upload (Large Files)
- [ ] Use chunked upload for files >4MB
- [ ] Show progress to user
- [ ] Handle upload failures gracefully
- [ ] Resume interrupted uploads if possible

```python
def upload_large_file(file, container_name, blob_name, chunk_size=4*1024*1024):
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )
    
    # Upload in chunks
    with file.open('rb') as data:
        blob_client.upload_blob(
            data,
            overwrite=False,
            max_concurrency=4
        )
```

## File Download Patterns

### Secure Download URLs
- [ ] Use SAS (Shared Access Signature) tokens for private files
- [ ] Set expiration time on SAS tokens (1 hour default)
- [ ] Limit SAS token permissions (read-only)
- [ ] Log access to sensitive files
- [ ] Validate user permission before generating SAS

```python
from azure.storage.blob import BlobSasPermissions, generate_blob_sas
from datetime import datetime, timedelta

def generate_download_url(blob_name, container_name, expires_in_hours=1):
    # Generate SAS token
    sas_token = generate_blob_sas(
        account_name=settings.AZURE_STORAGE_ACCOUNT_NAME,
        account_key=settings.AZURE_STORAGE_ACCOUNT_KEY,
        container_name=container_name,
        blob_name=blob_name,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=expires_in_hours)
    )
    
    # Build URL
    blob_url = f"https://{settings.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
    return f"{blob_url}/{container_name}/{blob_name}?{sas_token}"
```

### Django View for Downloads
```python
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def download_file(request, file_id):
    # Get file from database
    file_obj = File.objects.get(id=file_id, client_group=request.client_group)
    
    # Check permission
    if not request.user.has_perm('view_file', file_obj):
        return HttpResponseForbidden()
    
    # Generate download URL
    download_url = generate_download_url(
        file_obj.blob_name,
        file_obj.container_name
    )
    
    # Audit log
    AuditService.log(
        action='file_downloaded',
        user=request.user,
        details={'file_id': file_id, 'filename': file_obj.name}
    )
    
    # Redirect to blob URL
    return HttpResponseRedirect(download_url)
```

## File Management

### Listing Blobs
```python
def list_blobs(container_name, prefix=None):
    container_client = blob_service_client.get_container_client(container_name)
    
    blobs = container_client.list_blobs(name_starts_with=prefix)
    
    return [blob.name for blob in blobs]
```

### Deleting Blobs
- [ ] Soft delete enabled in Azure (30-day retention)
- [ ] Hard delete only after soft delete period
- [ ] Log all deletions for audit
- [ ] Verify permissions before deletion
- [ ] Clean up orphaned blobs periodically

```python
def delete_blob(blob_name, container_name):
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )
    
    # Delete blob
    blob_client.delete_blob(delete_snapshots='include')
```

### Moving/Copying Blobs
```python
def copy_blob(source_blob, dest_blob, source_container, dest_container):
    source_url = f"https://{settings.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
    source_url += f"/{source_container}/{source_blob}"
    
    dest_client = blob_service_client.get_blob_client(
        container=dest_container,
        blob=dest_blob
    )
    
    # Copy blob
    dest_client.start_copy_from_url(source_url)
```

## Metadata and Properties

### Setting Metadata
- [ ] Store file metadata (uploaded_by, uploaded_at, file_type)
- [ ] Store client group ID in metadata
- [ ] Store processing status in metadata
- [ ] Update metadata for tracking

```python
def upload_with_metadata(file, container_name, blob_name, metadata):
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )
    
    # Upload with metadata
    blob_client.upload_blob(
        file.read(),
        metadata=metadata,
        content_settings=ContentSettings(content_type=file.content_type)
    )
```

### Reading Metadata
```python
def get_blob_metadata(blob_name, container_name):
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )
    
    properties = blob_client.get_blob_properties()
    return properties.metadata
```

## Azure Front Door CDN

### CDN Configuration
- [ ] Azure Front Door configured for static assets
- [ ] Custom domain configured (if needed)
- [ ] SSL/TLS certificate configured
- [ ] Cache rules defined
- [ ] Origin configured (Blob Storage)

### CDN URL Structure
```python
# CDN URL format
CDN_URL = "https://your-frontdoor.azurefd.net"
STATIC_URL = f"{CDN_URL}/static/"

# Example URL
# https://your-frontdoor.azurefd.net/static/css/main.css
```

### Serving Static Assets via CDN
- [ ] Static files uploaded to Blob Storage
- [ ] Front Door pulls from Blob Storage (origin)
- [ ] Cache headers set appropriately
- [ ] SRI hashes generated for security
- [ ] CORS configured for cross-origin requests

## Subresource Integrity (SRI)

### SRI Implementation
- [ ] SRI enabled in production (`ENABLE_SRI = IS_PRODUCTION`)
- [ ] SHA-384 hashes generated for CDN assets
- [ ] Hashes cached in Redis (dedicated DB 4)
- [ ] `crossorigin="anonymous"` attribute on CDN assets
- [ ] Lazy generation (generate on first use, cache 24h)

### Generating SRI Hashes
```python
import hashlib
import base64
import requests
from django.core.cache import caches

sri_cache = caches['sri']

def generate_sri_hash(url):
    # Check cache
    cache_key = f"sri:{url}"
    cached_hash = sri_cache.get(cache_key)
    if cached_hash:
        return cached_hash
    
    # Fetch asset
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    
    # Generate SHA-384 hash
    content_hash = hashlib.sha384(response.content).digest()
    sri_hash = f"sha384-{base64.b64encode(content_hash).decode()}"
    
    # Cache for 24 hours
    sri_cache.set(cache_key, sri_hash, timeout=86400)
    
    return sri_hash
```

### Template Tags for CDN Assets
```python
# Custom template tag
from django import template

register = template.Library()

@register.simple_tag
def cdn_script(asset_path):
    cdn_url = f"{settings.CDN_URL}/{asset_path}"
    
    if settings.ENABLE_SRI:
        sri_hash = generate_sri_hash(cdn_url)
        return format_html(
            '<script src="{}" integrity="{}" crossorigin="anonymous"></script>',
            cdn_url,
            sri_hash
        )
    else:
        return format_html('<script src="{}"></script>', cdn_url)
```

### Template Usage
```django
{% load cdn_tags %}

{% cdn_script "static/js/main.js" %}
{% cdn_link "static/css/main.css" %}
```

## Performance Optimization

### Cache Control Headers
- [ ] Set appropriate cache headers for static assets
- [ ] Long cache for versioned assets (1 year)
- [ ] Short cache for frequently changing content
- [ ] No-cache for dynamic content
- [ ] Cache-Control vs Expires headers

```python
def upload_static_asset(file, blob_name):
    blob_client = blob_service_client.get_blob_client(
        container='static',
        blob=blob_name
    )
    
    # Upload with cache headers
    blob_client.upload_blob(
        file.read(),
        content_settings=ContentSettings(
            content_type=file.content_type,
            cache_control='public, max-age=31536000, immutable'  # 1 year
        )
    )
```

### CDN Caching Strategy
- [ ] Edge caching for static assets
- [ ] Query string caching behavior configured
- [ ] Cache purge process for updates
- [ ] Cache warming for critical assets
- [ ] Monitor cache hit ratio

### Blob Storage Performance
- [ ] Use premium storage for high-performance needs
- [ ] Enable large file shares if needed
- [ ] Use appropriate redundancy level (LRS, GRS, RA-GRS)
- [ ] Monitor latency and throughput
- [ ] Optimize blob naming for parallelism

## Security

### Access Control
- [ ] Use private containers by default
- [ ] SAS tokens for temporary access
- [ ] Time-limited SAS tokens (1-24 hours)
- [ ] Read-only SAS tokens when possible
- [ ] Log all SAS token generation

### Encryption
- [ ] Encryption at rest enabled (Azure default)
- [ ] Encryption in transit (HTTPS only)
- [ ] Customer-managed keys (if required for compliance)
- [ ] TLS 1.2+ enforced

### Network Security
- [ ] Firewall rules restrict public access
- [ ] Virtual network integration (if needed)
- [ ] Private endpoints for enhanced security
- [ ] Disable public access unless needed

### CORS Configuration
- [ ] CORS rules defined for CDN assets
- [ ] Allowed origins specified (not wildcard `*`)
- [ ] Allowed methods limited (GET, HEAD)
- [ ] Allowed headers specified

```python
from azure.storage.blob import CorsRule

cors_rules = [
    CorsRule(
        allowed_origins=['https://yourdomain.com'],
        allowed_methods=['GET', 'HEAD'],
        allowed_headers=['*'],
        exposed_headers=['*'],
        max_age_in_seconds=3600
    )
]

blob_service_client.set_service_properties(cors=cors_rules)
```

## Lifecycle Management

### Blob Lifecycle Policies
- [ ] Auto-delete temp files after 7 days
- [ ] Move old files to cool tier after 30 days
- [ ] Move archived files to archive tier after 90 days
- [ ] Delete soft-deleted blobs after 30 days

### Azure Portal Configuration
```json
{
  "rules": [
    {
      "name": "delete-temp-files",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["temp/"]
        },
        "actions": {
          "baseBlob": {
            "delete": {
              "daysAfterModificationGreaterThan": 7
            }
          }
        }
      }
    },
    {
      "name": "move-to-cool",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["uploads/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": {
              "daysAfterModificationGreaterThan": 30
            }
          }
        }
      }
    }
  ]
}
```

## Monitoring and Logging

### Storage Analytics
- [ ] Storage analytics enabled
- [ ] Logging enabled for read/write/delete operations
- [ ] Metrics collected (capacity, transactions, latency)
- [ ] Alerts configured for anomalies
- [ ] Monitor storage capacity and growth

### Application Logging
- [ ] Log all uploads (user, file, size, timestamp)
- [ ] Log all downloads (user, file, timestamp)
- [ ] Log SAS token generation
- [ ] Log deletions (user, file, reason)
- [ ] Monitor failed operations

```python
import logging

logger = logging.getLogger(__name__)

def upload_with_logging(file, container_name, blob_name, user):
    try:
        url = upload_file_to_blob(file, container_name, blob_name)
        
        logger.info(
            f"File uploaded: user={user.id}, blob={blob_name}, "
            f"size={file.size}, container={container_name}"
        )
        
        return url
    except Exception as e:
        logger.error(
            f"Upload failed: user={user.id}, blob={blob_name}, error={str(e)}"
        )
        raise
```

## Cost Optimization

### Storage Tiers
- [ ] Hot tier for frequently accessed files
- [ ] Cool tier for infrequently accessed files (>30 days)
- [ ] Archive tier for rarely accessed files (>90 days)
- [ ] Lifecycle policies to auto-tier
- [ ] Monitor access patterns

### Cost Monitoring
- [ ] Track storage costs by container
- [ ] Monitor transaction costs
- [ ] Monitor egress costs (CDN can reduce this)
- [ ] Set budget alerts in Azure
- [ ] Regular cleanup of unused files

### Cost Reduction Strategies
- [ ] Delete temp files after processing
- [ ] Compress files before upload (if appropriate)
- [ ] Use CDN to reduce egress from Blob Storage
- [ ] Use lifecycle policies to auto-tier
- [ ] Deduplicate files (hash-based storage)

## Django Integration

### Custom Storage Backend
```python
from django.core.files.storage import Storage
from azure.storage.blob import BlobServiceClient

class AzureBlobStorage(Storage):
    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )
        self.container_name = settings.AZURE_STORAGE_CONTAINER_NAME
    
    def _save(self, name, content):
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name,
            blob=name
        )
        blob_client.upload_blob(content, overwrite=True)
        return name
    
    def url(self, name):
        return generate_download_url(name, self.container_name)
```

### FileField with Blob Storage
```python
from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/', storage=AzureBlobStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
```

## Testing

### Mocking Blob Storage
```python
from unittest.mock import Mock, patch
from django.test import TestCase

class BlobStorageTestCase(TestCase):
    @patch('azure.storage.blob.BlobServiceClient')
    def test_upload(self, mock_client):
        # Mock blob client
        mock_blob_client = Mock()
        mock_client.return_value.get_blob_client.return_value = mock_blob_client
        
        # Test upload
        upload_file_to_blob(file, 'test-container', 'test.txt')
        
        # Verify upload called
        mock_blob_client.upload_blob.assert_called_once()
```

### Integration Tests
- [ ] Test with real Azure storage in integration environment
- [ ] Use dedicated test storage account
- [ ] Clean up test files after tests
- [ ] Test SAS token generation and expiration
- [ ] Test file permissions

## Common Patterns

### Temporary File Processing
```python
import tempfile
from celery import shared_task

@shared_task
def process_uploaded_file(blob_name):
    # Download from blob storage
    blob_client = blob_service_client.get_blob_client(
        container='uploads',
        blob=blob_name
    )
    
    # Process in temp directory
    with tempfile.TemporaryDirectory() as tmpdir:
        local_path = os.path.join(tmpdir, 'temp.pdf')
        
        with open(local_path, 'wb') as f:
            f.write(blob_client.download_blob().readall())
        
        # Process file
        result = process_pdf(local_path)
        
        # Upload result
        upload_file_to_blob(result, 'outputs', f"result_{blob_name}")
```

### Client Group Isolation
```python
def get_user_blobs(user, container_name='uploads'):
    client_group_id = user.client_group_id
    prefix = f"{client_group_id}/"
    
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs(name_starts_with=prefix)
    
    return [blob.name for blob in blobs]
```

## Troubleshooting

### Upload Failures
- Check storage account connection string
- Verify container exists
- Check file size within limits
- Verify network connectivity
- Check access permissions

### Download Issues
- Verify SAS token not expired
- Check blob exists
- Verify user has permission
- Check CORS configuration for browser downloads

### CDN Issues
- Verify origin configured correctly
- Check cache rules
- Purge CDN cache if needed
- Verify DNS and SSL configuration

### SRI Hash Mismatches
- Check asset hasn't changed
- Verify hash generated correctly
- Clear SRI cache and regenerate
- Check CORS allows fetching for hash generation

## Cross-Reference

Related docs:
- `cdn_sri_best_practices.md` - Detailed SRI implementation
- `file_validation_best_practices.md` - Magika validation before upload
- `soc2_considerations.md` - Audit logging requirements
- `celery_best_practices.md` - Async file processing
- `web_security_best_practices.md` - File upload security
