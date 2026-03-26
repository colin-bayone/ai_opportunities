# CDN & SRI Best Practices

CDN strategy with Subresource Integrity (SRI) security using Azure Front Door and dedicated Redis cache.

## CDN Configuration

### Azure Front Door
- [ ] CDN configured for static assets
- [ ] Origin points to static file storage (Azure Blob or app server)
- [ ] Caching rules configured appropriately
- [ ] Cache duration set for different asset types
- [ ] Compression enabled (gzip/brotli)

### CDN URL Strategy
- [ ] CDN URLs in environment variables
- [ ] Different CDN URLs for dev/staging/prod
- [ ] Custom domain configured (not Azure default)
- [ ] HTTPS enforced for all CDN assets
- [ ] Fallback to local assets if CDN unavailable

## Subresource Integrity (SRI)

### SRI Fundamentals
- [ ] SRI enabled in production only (`ENABLE_SRI = IS_PRODUCTION`)
- [ ] SRI hashes generated using SHA-384 (not SHA-256 or SHA-512)
- [ ] Hashes included in `integrity` attribute
- [ ] `crossorigin="anonymous"` on all SRI assets
- [ ] SRI cannot be disabled in production (fail-safe)

### SRI Cache Configuration
- [ ] Dedicated Redis DB for SRI hashes (e.g., DB 4)
- [ ] Cache timeout: 24 hours
- [ ] Lazy generation: hash calculated on first use
- [ ] Cache key: `sri:{asset_url}`
- [ ] No SRI in development (disabled)

### SRI Hash Generation
- [ ] Hashes generated from actual CDN content
- [ ] HTTP request to CDN to fetch asset
- [ ] SHA-384 algorithm used
- [ ] Base64 encoding of hash
- [ ] Format: `sha384-{base64_hash}`

## Template Tags

### CDN Template Tags
- [ ] `{% cdn_asset 'path' %}` - Returns CDN URL
- [ ] `{% cdn_script 'name' %}` - Generates `<script>` with SRI
- [ ] `{% cdn_link 'name' %}` - Generates `<link>` with SRI
- [ ] `{% cdn_head_assets %}` - All head assets (CSS, preconnects)
- [ ] `{% cdn_body_assets %}` - All body scripts
- [ ] `{% sri_status %}` - Debug SRI configuration (dev only)

### Tag Usage
- [ ] Tags loaded: `{% load cdn_tags %}`
- [ ] Asset name matches configuration
- [ ] No hardcoded CDN URLs in templates
- [ ] Fallback for missing assets
- [ ] No duplicate asset loading

## Asset Types

### CSS Assets
- [ ] Loaded in `<head>` section
- [ ] Critical CSS inline (if any)
- [ ] Non-critical CSS with proper attributes
- [ ] SRI hash on CDN CSS files
- [ ] `crossorigin="anonymous"` present

### JavaScript Assets
- [ ] Loaded before `</body>` or with `async`/`defer`
- [ ] Dependencies loaded in correct order
- [ ] SRI hash on CDN JavaScript files
- [ ] `crossorigin="anonymous"` present
- [ ] No blocking scripts in `<head>` unless necessary

### Font Assets
- [ ] Fonts from CDN (Google Fonts, CDN-hosted)
- [ ] Preconnect to font domains: `<link rel="preconnect">`
- [ ] `font-display: swap` for web fonts
- [ ] Fallback fonts defined in CSS
- [ ] No FOIT (Flash of Invisible Text)

## Security

### CORS Configuration
- [ ] CDN allows requests from your domain
- [ ] `crossorigin="anonymous"` on all SRI assets
- [ ] CORS headers on CDN response
- [ ] No credentials sent to CDN
- [ ] CDN origin trusted

### Integrity Validation
- [ ] Browser validates integrity hash
- [ ] Asset fails to load if hash mismatch
- [ ] Error logged if integrity check fails
- [ ] No fallback to non-SRI version (security risk)
- [ ] Alert on repeated integrity failures

### Production Requirements
- [ ] SRI mandatory in production (cannot be disabled)
- [ ] `IS_PRODUCTION` requires both `DEBUG=False` AND `ENVIRONMENT=production`
- [ ] No bypass mechanism in production
- [ ] SRI status endpoint secured (admin only)

## Performance

### Caching Strategy
- [ ] Browser caching configured (Cache-Control headers)
- [ ] Long cache duration for versioned assets (1 year)
- [ ] Short cache for non-versioned assets
- [ ] CDN caching configured (edge caching)
- [ ] Cache invalidation strategy defined

### Asset Optimization
- [ ] JavaScript minified
- [ ] CSS minified
- [ ] Images optimized (WebP, compression)
- [ ] SVGs minified
- [ ] No unnecessary assets loaded

### Lazy Loading
- [ ] Images lazy loaded: `loading="lazy"`
- [ ] Non-critical scripts deferred
- [ ] Third-party scripts loaded async
- [ ] Fonts preloaded if critical

## Asset Management

### Asset Organization
- [ ] Static files in `static/` directory
- [ ] Collected to `STATIC_ROOT` with `collectstatic`
- [ ] Versioned assets (query string or filename)
- [ ] No duplicate assets
- [ ] Unused assets removed

### WhiteNoise Integration
- [ ] WhiteNoise serves static files
- [ ] Compression enabled (gzip)
- [ ] Static file caching configured
- [ ] Manifest file generated
- [ ] No 404s for missing static files

## CDN Asset Configuration

### Phoenix Theme Assets
- [ ] Bootstrap CSS from CDN
- [ ] Bootstrap JS from CDN
- [ ] Popper.js from CDN (if needed by Bootstrap)
- [ ] Phoenix theme assets from CDN
- [ ] Version pinned in configuration

### Icon Libraries
- [ ] Feather Icons from CDN
- [ ] FontAwesome from CDN
- [ ] Icon sprites cached
- [ ] No duplicate icon libraries

### JavaScript Libraries
- [ ] Lodash from CDN
- [ ] MathJax from CDN (when needed)
- [ ] Chart.js from CDN (if used)
- [ ] Library versions pinned

## Monitoring

### SRI Metrics
- [ ] Track SRI cache hit rate
- [ ] Monitor SRI hash generation time
- [ ] Alert on SRI validation failures
- [ ] Log assets without SRI in production
- [ ] Track CDN performance

### CDN Metrics
- [ ] Monitor CDN response time
- [ ] Track CDN cache hit rate
- [ ] Alert on CDN errors
- [ ] Monitor bandwidth usage
- [ ] Track asset load failures

## Fallback Strategy

### CDN Unavailable
- [ ] Fallback to local assets if CDN fails
- [ ] Monitor CDN availability
- [ ] Alert on CDN downtime
- [ ] Graceful degradation
- [ ] User experience maintained

### SRI Failure
- [ ] Log SRI validation failures
- [ ] Alert on repeated failures
- [ ] Investigate hash mismatch
- [ ] No fallback to non-SRI (security)
- [ ] Fix root cause, not symptoms

## Testing

### SRI Testing
- [ ] Test SRI hash generation
- [ ] Test SRI validation in browser
- [ ] Test CDN asset loading
- [ ] Test with and without cache
- [ ] Test integrity failure scenario

### CDN Testing
- [ ] Test CDN URL generation
- [ ] Test asset accessibility from CDN
- [ ] Test CORS configuration
- [ ] Test caching behavior
- [ ] Test different environments (dev/staging/prod)

## Common Issues

### CORS Errors
- [ ] Check `crossorigin="anonymous"` present
- [ ] Verify CDN CORS headers
- [ ] Check Access-Control-Allow-Origin header
- [ ] No credentials sent to CDN
- [ ] CDN configuration allows origin

### Integrity Mismatch
- [ ] CDN asset content changed
- [ ] Hash needs regeneration
- [ ] Cache cleared and rehashed
- [ ] Asset version mismatch
- [ ] CDN not serving expected content

### Assets Not Loading
- [ ] Check CDN URL correct
- [ ] Verify asset exists on CDN
- [ ] Check network connectivity
- [ ] Verify HTTPS vs HTTP
- [ ] Check browser console for errors

### Cache Issues
- [ ] Redis cache backend configured
- [ ] Cache keys namespaced correctly
- [ ] Cache timeout appropriate
- [ ] Cache cleared when needed
- [ ] Redis memory not exhausted

## Development vs Production

### Development Mode
- [ ] SRI disabled (`ENABLE_SRI = False`)
- [ ] Local assets used (no CDN)
- [ ] WhiteNoise serves static files
- [ ] No SRI hash generation
- [ ] Fast development iteration

### Production Mode
- [ ] SRI enabled (`ENABLE_SRI = True`)
- [ ] CDN assets used
- [ ] SRI hashes generated and cached
- [ ] Production CDN URLs
- [ ] Strict security enforced

## Asset Updates

### Updating CDN Assets
- [ ] New asset version deployed to CDN
- [ ] SRI cache cleared for updated assets
- [ ] New hashes generated
- [ ] Version numbers updated in config
- [ ] Cache invalidation triggered

### Cache Invalidation
- [ ] Clear Redis SRI cache: `cache.delete_many()`
- [ ] Clear CDN cache if needed
- [ ] Force hash regeneration
- [ ] Verify new hashes correct
- [ ] Test after invalidation

## Security Best Practices

### SRI Benefits
- [ ] Protects against CDN compromise
- [ ] Prevents MITM attacks on assets
- [ ] Ensures asset integrity
- [ ] Defense-in-depth strategy
- [ ] Compliance requirement (SOC2)

### SRI Limitations
- [ ] Only works with CORS-enabled CDNs
- [ ] Requires `crossorigin` attribute
- [ ] Hash must match exactly
- [ ] Dynamic content cannot use SRI
- [ ] Browser support required (modern browsers only)

## Configuration Checklist

### Required Settings
- [ ] `ENABLE_SRI` configured
- [ ] `IS_PRODUCTION` logic correct
- [ ] CDN URLs in environment
- [ ] SRI cache backend configured
- [ ] Template tags registered

### CDN Asset Registry
- [ ] Asset names defined
- [ ] CDN URLs for each asset
- [ ] Versions pinned
- [ ] Fallback URLs defined
- [ ] Asset dependencies documented

## Cross-Reference

Related docs:
- `redis_best_practices.md` - SRI cache backend
- `django_templates_best_practices.md` - CDN template tags
- `web_security_best_practices.md` - CSP and asset security
- `soc2_considerations.md` - SRI as security control
- `performance_monitoring_best_practices.md` - CDN metrics
