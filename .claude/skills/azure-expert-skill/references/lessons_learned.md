# Azure Expert Skill - Lessons Learned

**Purpose:** This file is the self-learning knowledge base for the Azure Expert Skill. When commands fail or unexpected behavior occurs, solutions are documented here to prevent future issues.

**Last Updated:** 2026-01-06

---

## How to Add Entries

When a command fails or unexpected behavior occurs:

1. Document the error with context
2. Analyze root cause
3. Document the solution
4. Add prevention tips

Use this format:

```markdown
## [DATE] Issue: [Brief Description]

**Context:** [What was being attempted]

**Command:** `[the command that failed]`

**Error:**
```
[error output]
```

**Root Cause:** [analysis of why it failed]

**Solution:** [what fixed it]

**Prevention:** [how to avoid in future]

**Tags:** [relevant tags like: container-apps, postgres, network, auth]
```

---

## Entries

### 2026-01-06 Issue: Incomplete Resource Configuration for Browser Handoffs

**Context:** User was creating Azure resources (PostgreSQL, Redis) in the Azure Portal and needed configuration details. I provided sparse, incomplete information that forced the user to repeatedly ask follow-up questions for basic details like cache size, memory, networking options, and authentication settings.

**Problem:**
- Initial Redis info only included: Name, Type, SKU name, Location, Min TLS
- Missing: Cache size (250 MB), networking config, eviction policy, clustering policy, persistence settings, port, access keys authentication
- User had to ask "what about networking?" and "what about Access Keys Authentication?" because I failed to anticipate

**Root Cause:**
1. Not using sub-agents (azure-config-exporter, azure-resource-explorer) to get comprehensive data
2. Not anticipating all fields the user will encounter in the Azure Portal
3. Rushing to provide quick answers instead of thorough ones

**Solution:** When providing resource configuration for browser-based creation, ALWAYS include:

**For ANY Azure resource:**
- All Basics tab fields (name, RG, location, SKU with specs like memory/vCores/storage)
- All Networking tab fields (public access, private endpoint, VNet, subnet, DNS)
- All Advanced/Configuration tab fields
- All Tags
- Security settings (authentication methods, TLS, encryption)

**For PostgreSQL specifically:**
- SKU + vCores + memory
- Storage size + IOPS
- Version
- HA mode, geo-redundancy
- Backup retention
- Networking: VNet integration vs private endpoint, delegated subnet
- Authentication method

**For Redis specifically:**
- SKU + cache size in MB/GB
- Clustering policy
- Eviction policy
- Persistence (RDB/AOF settings)
- Port
- TLS version
- Access Keys Authentication (Enabled/Disabled)
- Networking: Public access or private endpoint, VNet, subnet

**Prevention:**
1. Before providing resource config, query ALL properties from stage resource using comprehensive API calls
2. Map response to portal tabs: Basics, Networking, Advanced, Tags
3. Include every field the user will see in the portal
4. When in doubt, include MORE information not less

**Tags:** process, browser-handoff, thoroughness, redis, postgres, configuration

---

### 2026-01-06 Issue: Fabricated Cost Estimates

**Context:** User asked about Redis SKU options. I provided a table with monthly costs that I made up instead of verifying from official Azure pricing.

**Problem:**
- Stated Balanced_B0 was ~$70/mo
- Portal showed actual cost: $23.81/mo
- I was off by 3x

**Root Cause:**
1. Guessed costs instead of looking them up
2. Violated skill rule: "Costs must NEVER be guessed"
3. Did not cite official Azure pricing sources

**Solution:** NEVER estimate Azure costs without verification. Either:
1. Use the portal's cost estimate (most accurate)
2. Fetch from official pricing page: https://azure.microsoft.com/en-us/pricing/
3. Use Azure Pricing Calculator: https://azure.microsoft.com/en-us/pricing/calculator/
4. If unsure, say "check the portal for accurate pricing" instead of guessing

**Prevention:**
1. When asked about costs, respond with: "Let me check official pricing" or "The portal will show accurate cost on the review page"
2. Never include cost columns in SKU comparison tables unless verified
3. If providing estimates, always caveat with "verify in portal" and cite source

**Tags:** costs, pricing, accuracy, redis

---

### 2026-01-06 Issue: Used jq Without Checking Availability

**Context:** Attempted to parse JSON output from Azure CLI using `jq` command.

**Command:** `az rest --method get --url "..." | jq '.'`

**Error:**
```
/bin/bash: line 1: jq: command not found
```

**Root Cause:**
1. Assumed `jq` was installed without checking
2. Did not document the failure per skill protocol
3. Just silently moved on to a different approach

**Solution:**
- Use `az` CLI's built-in `--query` parameter with JMESPath for JSON filtering
- Or use `-o json` and parse with Python if complex manipulation needed
- Don't assume external tools are installed

**Prevention:**
1. Prefer Azure CLI's native `--query` parameter over piping to `jq`
2. If a command fails, ALWAYS document it in lessons_learned.md
3. Don't silently move on from failures - that defeats the self-learning purpose

**Tags:** bash, jq, tools, failure-to-document

---

### 2026-01-06 Issue: Repeatedly Missing Networking Tab Fields

**Context:** User creating Storage Account in portal. I provided networking config but missed the top-level "Public network access" radio button options.

**Problem:**
- Missed the main "Public network access" selector (3 options: Allow all, Restrict inbound, Restrict both)
- This is at least the 3rd time I've missed networking fields (Redis, Key Vault, Storage)
- User had to ask again: "you consistently miss things in the networking tab"

**Root Cause:**
1. Networking tabs often have multiple levels of settings (top-level access + detailed firewall rules)
2. I query CLI which returns flat properties, but portal shows hierarchical UI
3. Not systematically checking ALL networking options

**Solution:** For ANY Azure resource networking config, ALWAYS include:

1. **Top-level access setting** (public/private/hybrid options)
2. **Firewall rules** (IP allowlist, default action)
3. **VNet integration** (service endpoints, VNet rules)
4. **Private endpoint** (if applicable)
5. **Exceptions/bypass** (trusted services)

**Prevention:**
1. When providing networking config, explicitly list each section header from the portal
2. Don't assume "PublicNetworkAccess: Enabled" tells the whole story
3. If a resource has a networking tab, assume there are 3-5 different settings to configure

**Tags:** networking, storage, portal, thoroughness, repeated-failure

---

### 2026-01-07 Issue: Wrong Django Model Name for AI Endpoints

**Context:** User needed to check/update the API version for the embedding endpoint in production. I provided a shell command with the wrong model import.

**Command:** `python manage.py shell -c "from intelligence.ai_models.models import AIEndpoint; ..."`

**Error:**
```
ImportError: cannot import name 'AIEndpoint' from 'intelligence.ai_models.models'
```

**Root Cause:**
1. Assumed model name was `AIEndpoint` without checking the actual codebase
2. Did not read `intelligence/ai_models/models/__init__.py` to verify exports
3. Guessed based on what seemed like a reasonable name

**Solution:** The correct model is `UnifiedEndpoint`:
```bash
python manage.py shell -c "from intelligence.ai_models.models import UnifiedEndpoint; ..."
```

**Prevention:**
1. ALWAYS check `__init__.py` or grep for actual class names before providing shell commands
2. Use `grep "class.*Endpoint" path/to/models/` to find actual model names
3. Don't assume model names - verify them first

**Tags:** django, models, imports, shell-commands

---

### 2026-01-07 Issue: az containerapp exec Fails in Non-Interactive Context

**Context:** Tried to run `az containerapp exec` from Claude Code CLI to check container database values.

**Command:** `az containerapp exec -n talent-ai-app-stage-aca -g talent_ai_stage-rg --command "python manage.py shell -c ..."`

**Error:**
```
termios.error: (25, 'Inappropriate ioctl for device')
```

**Root Cause:**
1. `az containerapp exec` requires an interactive TTY
2. Claude Code's bash tool doesn't provide a TTY
3. The command tried to set terminal modes that don't exist in this context

**Solution:**
- Cannot run `az containerapp exec` from Claude Code CLI
- User must run these commands manually in their terminal
- Or use Azure Portal console

**Prevention:**
1. Don't attempt `az containerapp exec` commands - they will always fail
2. When container access is needed, provide the command for the USER to run
3. Consider using Container Apps jobs for one-off commands if automation is needed

**Tags:** container-apps, exec, tty, interactive, shell-commands

---

### 2026-01-06 Issue: Template Entry

**Context:** This is a template entry to demonstrate the format.

**Command:** `az example-command`

**Error:**
```
Example error message
```

**Root Cause:** Example root cause analysis.

**Solution:** Example solution steps.

**Prevention:** Example prevention tips.

**Tags:** template, example

---

## Index by Tag

### browser-handoff
- 2026-01-06: Incomplete Resource Configuration for Browser Handoffs

### configuration
- 2026-01-06: Incomplete Resource Configuration for Browser Handoffs

### postgres
- 2026-01-06: Incomplete Resource Configuration for Browser Handoffs

### redis
- 2026-01-06: Incomplete Resource Configuration for Browser Handoffs
- 2026-01-06: Fabricated Cost Estimates

### costs
- 2026-01-06: Fabricated Cost Estimates

### pricing
- 2026-01-06: Fabricated Cost Estimates

### accuracy
- 2026-01-06: Fabricated Cost Estimates

### bash
- 2026-01-06: Used jq Without Checking Availability

### tools
- 2026-01-06: Used jq Without Checking Availability

### failure-to-document
- 2026-01-06: Used jq Without Checking Availability

### process
- 2026-01-06: Incomplete Resource Configuration for Browser Handoffs

### thoroughness
- 2026-01-06: Incomplete Resource Configuration for Browser Handoffs

### authentication
- (entries will be added as issues are encountered)

### container-apps
- 2026-01-07: az containerapp exec Fails in Non-Interactive Context

### django
- 2026-01-07: Wrong Django Model Name for AI Endpoints

### models
- 2026-01-07: Wrong Django Model Name for AI Endpoints

### imports
- 2026-01-07: Wrong Django Model Name for AI Endpoints

### shell-commands
- 2026-01-07: Wrong Django Model Name for AI Endpoints
- 2026-01-07: az containerapp exec Fails in Non-Interactive Context

### exec
- 2026-01-07: az containerapp exec Fails in Non-Interactive Context

### tty
- 2026-01-07: az containerapp exec Fails in Non-Interactive Context

### interactive
- 2026-01-07: az containerapp exec Fails in Non-Interactive Context

### network
- (entries will be added as issues are encountered)

### private-endpoints
- (entries will be added as issues are encountered)

### keyvault
- (entries will be added as issues are encountered)

### storage
- (entries will be added as issues are encountered)

---

## Quick Reference: Common Solutions

| Error Pattern | Likely Solution |
|---------------|-----------------|
| "ResourceNotFound" | Check resource name and resource group |
| "AuthorizationFailed" | Check RBAC permissions |
| "Forbidden" | Check network rules / private endpoint |
| "Connection refused" | Check firewall rules |
| "Name already exists" | Choose unique name |
| "Quota exceeded" | Request quota increase or use different region |
| "InvalidParameter" | Check parameter format and allowed values |

---

## GitHub Issues Created

When solutions are documented here, corresponding GitHub issues are created for human review:

| Date | Issue # | Topic |
|------|---------|-------|
| (issues will be tracked here) | | |
