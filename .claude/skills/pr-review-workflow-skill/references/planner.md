# PR Review Workflow - Reference Docs Development Planner

## Progress Tracker

### Completed ✓

- [x] `django_best_practices.md` - Core Django patterns
- [x] `scope_creep_guide.md` - Scope analysis patterns

### In Progress 🔄

- [ ] `soc2_considerations.md` - SOC2 compliance checklist
- [ ] `web_security_best_practices.md` - General web security
- [ ] `authentication_authorization_best_practices.md` - Auth patterns specific to your stack

### Planned 📋

#### Core Stack (Priority 1)

- [ ] `django_rest_framework_best_practices.md` - DRF with token auth, URL versioning
- [ ] `celery_best_practices.md` - Celery 5.5+ with Redis broker patterns
- [ ] `postgresql_best_practices.md` - PostgreSQL 17 + pgvector patterns
- [ ] `redis_best_practices.md` - Redis as broker, cache, Channels layer

#### Azure Integration (Priority 2)

- [ ] `azure_openai_best_practices.md` - Azure OpenAI via AI Foundry
- [ ] `azure_storage_best_practices.md` - Blob Storage + Front Door CDN
- [ ] `azure_services_best_practices.md` - AI Search, Communication Email, Identity

#### Frontend & Real-time (Priority 3)

- [ ] `htmx_best_practices.md` - HTMX patterns, OOB swaps, events
- [ ] `django_templates_best_practices.md` - Template components, inclusion tags
- [ ] `channels_websockets_best_practices.md` - Channels + channels-redis patterns
- [ ] `cdn_sri_best_practices.md` - CDN strategy with SRI security

#### Document Processing (Priority 4)

- [ ] `document_processing_best_practices.md` - PDF/DOCX/image handling
- [ ] `file_validation_best_practices.md` - Magika-based validation patterns

#### AI/ML Stack (Priority 5)

- [ ] `ai_ml_integration_best_practices.md` - Presidio, Tiktoken, pgvector
- [ ] `pii_detection_best_practices.md` - PII masking with Presidio

#### Middleware & Monitoring (Priority 6)

- [ ] `custom_middleware_best_practices.md` - Your middleware patterns
- [ ] `audit_logging_best_practices.md` - Immutable audit logs, signal handlers
- [ ] `performance_monitoring_best_practices.md` - MetricsCollector patterns

## Reference Doc Standards

Each reference doc should:

1. Be specific to your actual tech stack and patterns
2. Include real examples from your codebase structure
3. Have checkboxes for PR review items
4. Be concise (prefer multiple small docs over one large doc)
5. Cross-reference related docs where relevant

## Notes

- Frontend/UI/UX info provided - use for HTMX, templates, CDN docs
- All docs should match actual implementation patterns, not generic advice
