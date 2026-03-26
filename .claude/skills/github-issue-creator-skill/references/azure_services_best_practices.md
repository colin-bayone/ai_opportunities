# Azure Services Best Practices

Azure AI Search, Azure Communication Email, and Azure Identity (MSAL) integration patterns.

## Azure AI Search

### Service Configuration
- [ ] Azure AI Search service created
- [ ] Service endpoint in environment variables
- [ ] Admin key or query key in environment variables
- [ ] Different indexes for dev/staging/prod
- [ ] Appropriate pricing tier for workload

### Connection Configuration
```python
# django-environ pattern
AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
AZURE_SEARCH_ADMIN_KEY=your-admin-key
AZURE_SEARCH_QUERY_KEY=your-query-key
AZURE_SEARCH_INDEX_NAME=documents-index
```

### Python SDK
- [ ] `azure-search-documents` package installed
- [ ] `SearchClient` for querying
- [ ] `SearchIndexClient` for index management
- [ ] Retry policy configured
- [ ] Timeout settings appropriate

## Document Indexing

### Index Schema Definition
```python
from azure.search.documents.indexes.models import (
    SearchIndex, SimpleField, SearchableField, ComplexField
)

def create_index_schema():
    return SearchIndex(
        name=settings.AZURE_SEARCH_INDEX_NAME,
        fields=[
            SimpleField(
                name="id",
                type="Edm.String",
                key=True,
                filterable=True
            ),
            SearchableField(
                name="title",
                type="Edm.String",
                searchable=True,
                analyzer_name="en.microsoft"
            ),
            SearchableField(
                name="content",
                type="Edm.String",
                searchable=True,
                analyzer_name="en.microsoft"
            ),
            SimpleField(
                name="client_group_id",
                type="Edm.Int32",
                filterable=True,
                sortable=True
            ),
            SimpleField(
                name="created_at",
                type="Edm.DateTimeOffset",
                filterable=True,
                sortable=True
            ),
            SearchableField(
                name="metadata",
                type="Collection(Edm.String)",
                searchable=True,
                filterable=True,
                facetable=True
            )
        ]
    )
```

### Creating/Updating Index
- [ ] Index created during deployment
- [ ] Schema versioning strategy defined
- [ ] Index updates don't lose data
- [ ] Backup strategy for index data
- [ ] Test schema changes in dev first

```python
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential

def create_or_update_index():
    credential = AzureKeyCredential(settings.AZURE_SEARCH_ADMIN_KEY)
    index_client = SearchIndexClient(
        endpoint=settings.AZURE_SEARCH_ENDPOINT,
        credential=credential
    )
    
    index = create_index_schema()
    index_client.create_or_update_index(index)
```

### Adding Documents to Index
- [ ] Documents indexed asynchronously with Celery
- [ ] Batch indexing for efficiency (up to 1000 docs)
- [ ] Error handling for failed indexing
- [ ] Retry logic for transient failures
- [ ] Index only after database commit

```python
from azure.search.documents import SearchClient
from celery import shared_task

@shared_task
def index_document(document_id):
    # Fetch document from database
    doc = Document.objects.get(id=document_id)
    
    # Prepare for indexing
    search_doc = {
        "id": str(doc.id),
        "title": doc.title,
        "content": doc.content,
        "client_group_id": doc.client_group_id,
        "created_at": doc.created_at.isoformat(),
        "metadata": [doc.category, doc.type]
    }
    
    # Index document
    credential = AzureKeyCredential(settings.AZURE_SEARCH_ADMIN_KEY)
    search_client = SearchClient(
        endpoint=settings.AZURE_SEARCH_ENDPOINT,
        index_name=settings.AZURE_SEARCH_INDEX_NAME,
        credential=credential
    )
    
    search_client.upload_documents([search_doc])
```

### Batch Indexing
```python
from django.db import transaction

@shared_task
def index_documents_batch(document_ids):
    documents = Document.objects.filter(id__in=document_ids)
    
    search_docs = [
        {
            "id": str(doc.id),
            "title": doc.title,
            "content": doc.content,
            "client_group_id": doc.client_group_id,
            "created_at": doc.created_at.isoformat()
        }
        for doc in documents
    ]
    
    # Batch upload (max 1000 per batch)
    search_client.upload_documents(search_docs)
```

## Vector Search with Azure AI Search

### Vector Field Configuration
- [ ] Vector field added to index schema
- [ ] Vector dimensions match embedding model (1536 for text-embedding-3-large)
- [ ] Vector search configuration defined
- [ ] Hybrid search combining vectors and keywords

```python
from azure.search.documents.indexes.models import (
    VectorSearch, HnswAlgorithmConfiguration, VectorSearchProfile
)

def create_vector_index_schema():
    return SearchIndex(
        name=settings.AZURE_SEARCH_INDEX_NAME,
        fields=[
            # ... other fields ...
            SearchField(
                name="content_vector",
                type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                searchable=True,
                vector_search_dimensions=1536,
                vector_search_profile_name="my-vector-profile"
            )
        ],
        vector_search=VectorSearch(
            algorithms=[
                HnswAlgorithmConfiguration(
                    name="my-hnsw-config",
                    parameters={
                        "m": 4,
                        "efConstruction": 400,
                        "efSearch": 500,
                        "metric": "cosine"
                    }
                )
            ],
            profiles=[
                VectorSearchProfile(
                    name="my-vector-profile",
                    algorithm_configuration_name="my-hnsw-config"
                )
            ]
        )
    )
```

### Hybrid Search (Keywords + Vectors)
```python
def hybrid_search(query_text, query_embedding, client_group_id, top=10):
    search_client = SearchClient(
        endpoint=settings.AZURE_SEARCH_ENDPOINT,
        index_name=settings.AZURE_SEARCH_INDEX_NAME,
        credential=AzureKeyCredential(settings.AZURE_SEARCH_QUERY_KEY)
    )
    
    results = search_client.search(
        search_text=query_text,
        vector_queries=[{
            "vector": query_embedding,
            "k_nearest_neighbors": top,
            "fields": "content_vector"
        }],
        filter=f"client_group_id eq {client_group_id}",
        select=["id", "title", "content"],
        top=top
    )
    
    return list(results)
```

## Search Queries

### Basic Search
```python
def search_documents(query, client_group_id, top=10):
    search_client = SearchClient(
        endpoint=settings.AZURE_SEARCH_ENDPOINT,
        index_name=settings.AZURE_SEARCH_INDEX_NAME,
        credential=AzureKeyCredential(settings.AZURE_SEARCH_QUERY_KEY)
    )
    
    results = search_client.search(
        search_text=query,
        filter=f"client_group_id eq {client_group_id}",
        select=["id", "title", "content"],
        top=top,
        include_total_count=True
    )
    
    return results
```

### Faceted Search
```python
def faceted_search(query, client_group_id):
    results = search_client.search(
        search_text=query,
        filter=f"client_group_id eq {client_group_id}",
        facets=["metadata", "created_at,interval:day"],
        top=50
    )
    
    facets = results.get_facets()
    return {
        'results': list(results),
        'facets': facets
    }
```

### Autocomplete and Suggestions
- [ ] Suggester configured in index
- [ ] Autocomplete endpoint for search box
- [ ] Suggestions for "did you mean"

```python
from azure.search.documents.indexes.models import SearchSuggester

# In index schema
suggesters=[
    SearchSuggester(
        name="sg",
        source_fields=["title", "content"]
    )
]

# Autocomplete usage
def autocomplete(query, client_group_id):
    results = search_client.autocomplete(
        search_text=query,
        suggester_name="sg",
        filter=f"client_group_id eq {client_group_id}",
        autocomplete_mode="twoTerms"
    )
    
    return [r.text for r in results]
```

## Client Group Isolation

### Filtering by Client Group
- [ ] All searches filtered by `client_group_id`
- [ ] Filter applied at query level (not post-processing)
- [ ] No cross-tenant data leakage
- [ ] Test with multiple client groups

```python
# Always include client group filter
filter_expression = f"client_group_id eq {client_group_id}"

results = search_client.search(
    search_text=query,
    filter=filter_expression,
    # ... other parameters
)
```

## Document Updates and Deletions

### Updating Documents
```python
@shared_task
def update_indexed_document(document_id):
    doc = Document.objects.get(id=document_id)
    
    search_doc = {
        "id": str(doc.id),
        "title": doc.title,
        "content": doc.content,
        # Partial update with @search.action
        "@search.action": "merge"
    }
    
    search_client.merge_documents([search_doc])
```

### Deleting Documents
```python
@shared_task
def delete_indexed_document(document_id):
    search_client.delete_documents([{"id": str(document_id)}])
```

### Keeping Index in Sync
- [ ] Use Django signals to trigger indexing
- [ ] Index on document save (after commit)
- [ ] Remove from index on document delete
- [ ] Periodic full re-index for consistency

```python
from django.db.models.signals import post_save, post_delete
from django.db import transaction

@receiver(post_save, sender=Document)
def document_saved(sender, instance, created, **kwargs):
    transaction.on_commit(
        lambda: index_document.delay(instance.id)
    )

@receiver(post_delete, sender=Document)
def document_deleted(sender, instance, **kwargs):
    transaction.on_commit(
        lambda: delete_indexed_document.delay(instance.id)
    )
```

## Azure Communication Email

### Service Configuration
- [ ] Communication Services resource created
- [ ] Email domain verified
- [ ] Connection string in environment variables
- [ ] Sender address verified
- [ ] SPF, DKIM, DMARC configured

```python
# django-environ pattern
AZURE_COMMUNICATION_CONNECTION_STRING=endpoint=https://...
AZURE_COMMUNICATION_EMAIL_FROM=noreply@yourdomain.com
```

### Python SDK
- [ ] `azure-communication-email` package installed
- [ ] `EmailClient` configured
- [ ] Retry policy for transient failures
- [ ] Email templates stored in Django

### Sending Emails

#### Simple Email
```python
from azure.communication.email import EmailClient

def send_email(to_address, subject, body_html):
    client = EmailClient.from_connection_string(
        settings.AZURE_COMMUNICATION_CONNECTION_STRING
    )
    
    message = {
        "senderAddress": settings.AZURE_COMMUNICATION_EMAIL_FROM,
        "recipients": {
            "to": [{"address": to_address}]
        },
        "content": {
            "subject": subject,
            "html": body_html
        }
    }
    
    poller = client.begin_send(message)
    result = poller.result()
    
    return result
```

#### Email with Attachments
```python
def send_email_with_attachment(to_address, subject, body_html, attachment_path):
    with open(attachment_path, 'rb') as f:
        attachment_content = f.read()
    
    import base64
    attachment_b64 = base64.b64encode(attachment_content).decode()
    
    message = {
        "senderAddress": settings.AZURE_COMMUNICATION_EMAIL_FROM,
        "recipients": {
            "to": [{"address": to_address}]
        },
        "content": {
            "subject": subject,
            "html": body_html
        },
        "attachments": [
            {
                "name": os.path.basename(attachment_path),
                "contentType": "application/pdf",
                "contentInBase64": attachment_b64
            }
        ]
    }
    
    poller = client.begin_send(message)
    return poller.result()
```

### Email Templates
- [ ] Templates stored in Django templates
- [ ] Context variables for personalization
- [ ] Plain text fallback for HTML emails
- [ ] Consistent branding across emails

```python
from django.template.loader import render_to_string

def send_templated_email(to_address, template_name, context):
    subject = render_to_string(f'emails/{template_name}_subject.txt', context).strip()
    body_html = render_to_string(f'emails/{template_name}.html', context)
    
    return send_email(to_address, subject, body_html)
```

### Async Email Sending
- [ ] Send emails asynchronously with Celery
- [ ] Retry on failure
- [ ] Log email sends for audit
- [ ] Track email delivery status

```python
from celery import shared_task

@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3, 'countdown': 60}
)
def send_email_async(to_address, subject, body_html):
    try:
        result = send_email(to_address, subject, body_html)
        
        # Log successful send
        logger.info(
            f"Email sent: to={to_address}, "
            f"message_id={result.message_id}, status={result.status}"
        )
        
        return result.message_id
    except Exception as e:
        logger.error(f"Email failed: to={to_address}, error={str(e)}")
        raise
```

### Email Types

#### Verification Email
```python
def send_verification_email(user, verification_url):
    context = {
        'user': user,
        'verification_url': verification_url
    }
    
    send_templated_email(
        user.email,
        'verification',
        context
    )
```

#### Password Reset Email
```python
def send_password_reset_email(user, reset_url):
    context = {
        'user': user,
        'reset_url': reset_url
    }
    
    send_templated_email(
        user.email,
        'password_reset',
        context
    )
```

#### Notification Email
```python
def send_notification_email(user, notification_type, **kwargs):
    context = {
        'user': user,
        **kwargs
    }
    
    send_templated_email(
        user.email,
        f'notifications/{notification_type}',
        context
    )
```

## Azure Identity (MSAL)

### Microsoft Authentication Library
- [ ] `msal` package installed
- [ ] Client ID and tenant ID in environment variables
- [ ] Client secret in environment variables
- [ ] Redirect URI configured in Azure AD

```python
# django-environ pattern
AZURE_AD_CLIENT_ID=your-client-id
AZURE_AD_TENANT_ID=your-tenant-id
AZURE_AD_CLIENT_SECRET=your-client-secret
AZURE_AD_REDIRECT_URI=https://yourdomain.com/auth/callback
```

### MSAL Configuration
```python
import msal

def get_msal_app():
    authority = f"https://login.microsoftonline.com/{settings.AZURE_AD_TENANT_ID}"
    
    return msal.ConfidentialClientApplication(
        settings.AZURE_AD_CLIENT_ID,
        authority=authority,
        client_credential=settings.AZURE_AD_CLIENT_SECRET
    )
```

### OAuth Flow (Already Integrated via django-allauth)
- [ ] Microsoft provider configured in django-allauth
- [ ] Authorization endpoint redirects to Microsoft
- [ ] Callback handles OAuth response
- [ ] Token exchange handled by allauth
- [ ] User info extracted from token

### Token Acquisition for API Calls
```python
def get_access_token(scope):
    app = get_msal_app()
    
    result = app.acquire_token_for_client(scopes=[scope])
    
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception(f"Token acquisition failed: {result.get('error_description')}")
```

### Calling Microsoft Graph API
```python
import requests

def get_user_profile(user_principal_name):
    token = get_access_token("https://graph.microsoft.com/.default")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        f"https://graph.microsoft.com/v1.0/users/{user_principal_name}",
        headers=headers
    )
    
    return response.json()
```

## Monitoring and Logging

### Azure AI Search Monitoring
- [ ] Query metrics tracked (QPS, latency)
- [ ] Index size and document count monitored
- [ ] Failed queries logged
- [ ] Search analytics enabled
- [ ] Alert on degraded performance

### Email Delivery Monitoring
- [ ] Email send success/failure tracked
- [ ] Delivery status polled if needed
- [ ] Bounce and complaint handling
- [ ] Email volume monitored
- [ ] Alert on high failure rate

### MSAL Token Monitoring
- [ ] Token acquisition failures logged
- [ ] Token expiration handled
- [ ] API call failures logged
- [ ] Rate limiting respected

## Cost Optimization

### Azure AI Search
- [ ] Appropriate pricing tier (Basic, Standard, etc.)
- [ ] Monitor queries per second (QPS)
- [ ] Optimize index size (remove unused fields)
- [ ] Use query keys for read-only access
- [ ] Consider replica count for load

### Azure Communication Email
- [ ] Monitor email volume
- [ ] Batch emails when possible
- [ ] Avoid duplicate sends
- [ ] Clean up distribution lists
- [ ] Track cost per email

## Security

### Azure AI Search Security
- [ ] Use query keys for search queries (not admin keys)
- [ ] Admin keys only for indexing and management
- [ ] Keys in environment variables, never in code
- [ ] Rotate keys regularly
- [ ] Network security rules if needed

### Email Security
- [ ] SPF, DKIM, DMARC configured
- [ ] Sender reputation monitored
- [ ] No sensitive data in subject lines
- [ ] PII masked or excluded from emails
- [ ] Unsubscribe links for marketing emails

### MSAL Security
- [ ] Client secret secured
- [ ] Token cache secured (if used)
- [ ] Redirect URI validated
- [ ] State parameter for CSRF protection
- [ ] HTTPS enforced for callbacks

## Testing

### Mocking Azure Services
```python
from unittest.mock import Mock, patch
from django.test import TestCase

class AzureSearchTestCase(TestCase):
    @patch('azure.search.documents.SearchClient')
    def test_search(self, mock_client):
        # Mock search results
        mock_results = [
            {'id': '1', 'title': 'Test Doc'}
        ]
        mock_client.return_value.search.return_value = mock_results
        
        # Test search function
        results = search_documents('test', client_group_id=1)
        self.assertEqual(len(results), 1)
```

### Integration Tests
- [ ] Test with real Azure services in integration environment
- [ ] Use dedicated test resources
- [ ] Clean up test data after tests
- [ ] Test client group isolation
- [ ] Test error handling

## Cross-Reference

Related docs:
- `azure_openai_best_practices.md` - Embeddings for vector search
- `postgresql_best_practices.md` - Alternative to Azure AI Search (pgvector)
- `celery_best_practices.md` - Async indexing and email sending
- `authentication_authorization_best_practices.md` - Microsoft SSO integration
- `soc2_considerations.md` - Audit logging for services
