# Azure Cost Breakdown

**Generated:** {YYYY-MM-DD HH:MM:SS}
**Last Updated:** {YYYY-MM-DD HH:MM:SS}
**Agent:** azure-cost-estimator
**Session:** {session_folder_name}
**Resource Group:** {resource_group}
**Region:** {region}
**Currency:** USD

---

## Executive Summary

| Category | Monthly Estimate | Annual Estimate |
|----------|-----------------|-----------------|
| Compute | ${X.XX} | ${X.XX} |
| Database | ${X.XX} | ${X.XX} |
| Cache | ${X.XX} | ${X.XX} |
| Storage | ${X.XX} | ${X.XX} |
| Networking | ${X.XX} | ${X.XX} |
| Security | ${X.XX} | ${X.XX} |
| Monitoring | ${X.XX} | ${X.XX} |
| **TOTAL** | **${XXX.XX}** | **${X,XXX.XX}** |

**Important:** These are estimates based on current pricing and assumed usage patterns.

---

## Detailed Cost Analysis

### {Category Name} (${X.XX}/month)

**Source:** [{Service Name} Pricing]({pricing_url})
**Accessed:** {date}

**Resources:**

| Resource | SKU/Tier | Units | Unit Price | Monthly Cost |
|----------|----------|-------|------------|--------------|
| {name} | {sku} | {units} | ${X.XX} | ${X.XX} |

**Calculation:**
```
{Show the math}

Example:
Hours per month: 730
Rate: $X.XX per hour
Monthly cost: 730 × $X.XX = ${total}
```

**Assumptions:**
- {assumption 1}
- {assumption 2}

---

### {Next Category}

{Repeat the same structure for each category}

---

## Cost by Resource

| Resource Name | Type | SKU | Monthly Cost | % of Total |
|---------------|------|-----|--------------|------------|
| {name} | {type} | {sku} | ${X.XX} | X% |

---

## Cost Trends

| Period | Estimated Cost | Notes |
|--------|---------------|-------|
| Current Month | ${X.XX} | Based on current usage |
| Next Month | ${X.XX} | {any expected changes} |
| 12-Month Projection | ${X,XXX.XX} | Assuming stable usage |

---

## Cost Optimization Recommendations

### High Impact

1. **{Recommendation Title}**
   - Current: {current state}
   - Recommended: {recommended action}
   - Potential Savings: ${X.XX}/month (X%)
   - Effort: Low/Medium/High
   - Risk: Low/Medium/High

### Medium Impact

2. **{Recommendation Title}**
   - Current: {current state}
   - Recommended: {recommended action}
   - Potential Savings: ${X.XX}/month (X%)

### Reserved Capacity Savings

| Resource | 1-Year Reserved | Savings | 3-Year Reserved | Savings |
|----------|-----------------|---------|-----------------|---------|
| {name} | ${X.XX}/mo | X% | ${X.XX}/mo | X% |

---

## Comparison: Stage vs Production

| Category | Stage Cost | Estimated Prod Cost | Difference |
|----------|------------|---------------------|------------|
| Compute | ${X.XX} | ${X.XX} | +X% |
| Database | ${X.XX} | ${X.XX} | +X% |
| {etc} | | | |
| **TOTAL** | **${XXX.XX}** | **${XXX.XX}** | **+X%** |

**Production Assumptions:**
- {assumption about production sizing}
- {assumption about traffic}

---

## Disclaimers

1. All prices are estimates based on publicly available pricing as of {date}
2. Actual costs depend on actual usage patterns
3. Prices may vary by region and change over time
4. Tax not included
5. Enterprise agreements may have different pricing
6. Data transfer costs may apply and are not fully estimated

---

## Sources Referenced

| Resource | Pricing URL | Accessed |
|----------|-------------|----------|
| {Service} | {url} | {date} |

---

## Appendix: Raw Pricing Data

### Official Pricing Pages

- Container Apps: https://azure.microsoft.com/en-us/pricing/details/container-apps/
- PostgreSQL: https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/
- Redis: https://azure.microsoft.com/en-us/pricing/details/cache/
- Storage: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
- Private Link: https://azure.microsoft.com/en-us/pricing/details/private-link/
- Key Vault: https://azure.microsoft.com/en-us/pricing/details/key-vault/

### Pricing Calculator

For customized estimates: https://azure.microsoft.com/en-us/pricing/calculator/
