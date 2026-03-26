# File Validation Best Practices

Magika-based file validation patterns using AI-powered content detection.

## Magika Configuration

### Singleton Pattern
- [ ] One Magika instance per application (expensive initialization)
- [ ] Instance created on first use, cached for reuse
- [ ] Thread-safe singleton implementation
- [ ] Initialize in service layer, not in view

### Initialization
- [ ] Import magika library at module level
- [ ] Create instance only when first validation needed
- [ ] Handle initialization errors gracefully
- [ ] Log initialization time (typically 1-2 seconds)

## Validation Workflow

### Core Validation Steps
```
1. Check file is not empty
2. Check file size within limit
3. Detect content type with Magika
4. Verify detected type in allowed list
5. Reject if any validation fails
```

### Validation Order
- [ ] Fast checks first (empty, size)
- [ ] Expensive checks last (Magika detection)
- [ ] Fail fast on any validation failure
- [ ] No processing after validation failure

## File Type Detection

### Content-Based Detection
- [ ] Magika analyzes actual file content (not extension)
- [ ] Detects file type from magic bytes and patterns
- [ ] More reliable than extension-based detection
- [ ] Detects common evasion techniques

### Supported File Types
- [ ] PDF, DOC, DOCX - Documents
- [ ] TXT, RTF, HTML - Text formats
- [ ] JPG, JPEG, PNG - Images
- [ ] CSV, JSON - Data formats
- [ ] Check Magika output against your allowed types

### Type Mapping
- [ ] Map Magika output to application types
- [ ] Handle multiple names for same type (e.g., "jpg" vs "jpeg")
- [ ] Document type mappings in code
- [ ] Update allowed types in settings

## Size Limits

### App-Specific Limits
- [ ] Job Parser: 2MB max
- [ ] Resume Parser: 5MB max
- [ ] Global default: 10MB
- [ ] Document limits in settings, not hardcoded

### Size Validation
- [ ] Check file size before reading content
- [ ] Use `file.size` attribute (Django)
- [ ] Reject oversized files immediately
- [ ] Return clear error message with limit

## Allowed Types Configuration

### Centralized Configuration
```python
FILE_ALLOWED_TYPES = {
    'uploads': ['pdf', 'doc', 'docx', 'txt', 'rtf', 'html', ...],
    'outputs': ['pdf', 'docx', 'txt', 'json', 'csv', 'html'],
    'temp': ['pdf', 'doc', 'docx', 'txt', 'jpg', 'jpeg', 'png', ...]
}
```

### Type Lists
- [ ] Separate lists for different contexts (uploads, outputs, temp)
- [ ] Lowercase type names for consistency
- [ ] Document why each type is allowed
- [ ] Review periodically and remove unused types

## Validation Service

### Service Layer Pattern
- [ ] Validation logic in service, not view
- [ ] Reusable across views and APIs
- [ ] Single source of truth for validation
- [ ] Easy to test independently

### Validation Function
- [ ] Accept file object and context (app, max_size)
- [ ] Return success/failure with error message
- [ ] Raise exception or return result object
- [ ] Log validation failures with context

## Error Handling

### Validation Failures
- [ ] Empty file - "File is empty"
- [ ] Too large - "File exceeds X MB limit"
- [ ] Invalid type - "File type not allowed. Allowed: ..."
- [ ] Detection failure - "Could not determine file type"

### User-Friendly Messages
- [ ] Clear explanation of failure reason
- [ ] List allowed file types
- [ ] Include size limit in message
- [ ] No technical details exposed

### Logging
- [ ] Log validation failures with file info
- [ ] Include detected type vs allowed types
- [ ] Log file size and source
- [ ] Don't log file content

## Security Considerations

### Extension Spoofing
- [ ] Don't trust file extension
- [ ] Validate actual content with Magika
- [ ] Reject files with mismatched extension/content
- [ ] Example: `malware.exe` renamed to `document.pdf`

### Malicious Files
- [ ] Magika detects many evasion techniques
- [ ] Still validate size limits (prevent DoS)
- [ ] Consider additional malware scanning
- [ ] Isolate file processing

### Path Traversal
- [ ] Don't use original filename for storage
- [ ] Generate random filename
- [ ] Store files outside web root
- [ ] Use Azure Blob Storage with proper ACLs

## Integration Points

### Form Validation
- [ ] Validate on form submission
- [ ] Show validation errors inline
- [ ] Client-side validation optional (UX)
- [ ] Server-side validation mandatory

### API Validation
- [ ] Validate in serializer or view
- [ ] Return 400 Bad Request on failure
- [ ] Include error details in response
- [ ] Rate limit file uploads

### Celery Tasks
- [ ] Re-validate file in async task
- [ ] Don't trust validation from request
- [ ] File could change between validation and processing
- [ ] Log validation in task

## Performance

### Validation Performance
- [ ] Magika detection: ~10-50ms per file
- [ ] Singleton avoids init overhead (1-2 seconds)
- [ ] Size check: <1ms
- [ ] Total validation: <100ms typical

### Optimization
- [ ] Cache validation results if file unchanged (by hash)
- [ ] Validate before uploading to storage
- [ ] Process large files async (Celery)
- [ ] Don't validate same file multiple times

## Testing

### Unit Tests
- [ ] Test with valid files for each allowed type
- [ ] Test with invalid file types
- [ ] Test with empty files
- [ ] Test with oversized files
- [ ] Test with renamed files (extension spoofing)
- [ ] Mock Magika for faster tests

### Test Files
- [ ] Create test files for each type
- [ ] Include edge cases (tiny, large, corrupted)
- [ ] Test across different allowed type lists
- [ ] Store test files in fixtures directory

### Integration Tests
- [ ] Test end-to-end file upload
- [ ] Test with real Magika instance
- [ ] Test validation failure paths
- [ ] Verify error messages

## Monitoring

### Metrics to Track
- [ ] Validation success/failure rate
- [ ] Most common rejected types
- [ ] Validation time (p50, p95, p99)
- [ ] Size distribution of uploads

### Alerting
- [ ] High rejection rate (possible attack)
- [ ] Slow validation times
- [ ] Magika initialization failures
- [ ] Unusual file types attempted

## Common Patterns

### View Validation Pattern
```python
# In view or API endpoint
try:
    validate_file_upload(file, max_size_mb=5, allowed_types=['pdf', 'docx'])
except ValidationError as e:
    return Response({'error': str(e)}, status=400)
```

### Form Field Validation
```python
# In forms.py
def clean_file(self):
    file = self.cleaned_data['file']
    validate_file_upload(file, max_size_mb=2, allowed_types=settings.FILE_ALLOWED_TYPES['uploads'])
    return file
```

### Serializer Validation
```python
# In serializers.py
def validate_file(self, value):
    validate_file_upload(value, max_size_mb=5)
    return value
```

## Configuration Examples

### Settings Organization
```python
# File size limits (MB)
FILE_SIZE_LIMITS = {
    'job_parser': 2,
    'resume_parser': 5,
    'default': 10,
}

# Allowed file types by context
FILE_ALLOWED_TYPES = {
    'uploads': ['pdf', 'doc', 'docx', 'txt', 'rtf', 'html'],
    'outputs': ['pdf', 'docx', 'txt', 'json', 'csv'],
    'temp': ['pdf', 'doc', 'docx', 'txt', 'jpg', 'jpeg', 'png'],
}
```

### Context-Aware Validation
```python
def validate_upload(file, context='default'):
    max_size = FILE_SIZE_LIMITS.get(context, FILE_SIZE_LIMITS['default'])
    allowed_types = FILE_ALLOWED_TYPES.get(context, FILE_ALLOWED_TYPES['uploads'])
    validate_file_upload(file, max_size_mb=max_size, allowed_types=allowed_types)
```

## Troubleshooting

### Magika detection fails
- Check file is not empty
- Verify file is readable
- Check Magika initialized correctly
- Review file format (might be corrupted)

### False positives (valid files rejected)
- Check Magika output type name
- Add type to allowed list if legitimate
- Review type mapping logic

### False negatives (invalid files accepted)
- Verify validation called
- Check allowed types list not too broad
- Review size limits

### Slow validation
- Check Magika singleton working
- Monitor file sizes
- Consider async validation for large files

## Edge Cases

### Uncommon File Types
- [ ] CSV with no extension
- [ ] Plain text with wrong extension
- [ ] HTML in TXT file
- [ ] Images embedded in documents

### Corrupted Files
- [ ] Partial downloads
- [ ] Truncated files
- [ ] Wrong encoding
- [ ] Mixed formats

### Handling Strategy
- [ ] Detect and reject corrupted files
- [ ] Log detection for investigation
- [ ] Return clear error to user
- [ ] Don't crash on corrupted input

## Cross-Reference

Related docs:
- `document_processing_best_practices.md` - Processing validated files
- `web_security_best_practices.md` - Upload security
- `soc2_considerations.md` - File upload audit
- `celery_best_practices.md` - Async validation
- `azure_storage_best_practices.md` - Secure storage
