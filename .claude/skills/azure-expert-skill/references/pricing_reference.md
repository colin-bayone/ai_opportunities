# Azure Pricing Reference

**Last Updated:** 2026-01-06
**Region Focus:** East US 2 (default)

**IMPORTANT:** Prices change frequently. Always verify with official sources before quoting costs.

---

## Official Pricing URLs

| Service | Pricing Page |
|---------|--------------|
| Container Apps | https://azure.microsoft.com/en-us/pricing/details/container-apps/ |
| PostgreSQL Flexible | https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/ |
| Redis Enterprise | https://azure.microsoft.com/en-us/pricing/details/cache/ |
| Storage (Blob) | https://azure.microsoft.com/en-us/pricing/details/storage/blobs/ |
| Key Vault | https://azure.microsoft.com/en-us/pricing/details/key-vault/ |
| Container Registry | https://azure.microsoft.com/en-us/pricing/details/container-registry/ |
| Virtual Network | https://azure.microsoft.com/en-us/pricing/details/virtual-network/ |
| Private Link | https://azure.microsoft.com/en-us/pricing/details/private-link/ |
| Log Analytics | https://azure.microsoft.com/en-us/pricing/details/monitor/ |
| Azure AI / OpenAI | https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/ |

**Pricing Calculator:** https://azure.microsoft.com/en-us/pricing/calculator/

---

## Container Apps (Consumption Plan)

### Pricing Components

| Component | Price (East US 2) |
|-----------|-------------------|
| vCPU | $0.000024 per vCPU-second |
| Memory | $0.000003 per GiB-second |
| Requests | First 2M free, then $0.40 per million |

### Calculation Example

For 1 Container App running 24/7 with 0.5 vCPU and 1 GiB:
```
Seconds per month = 730 hours × 3600 = 2,628,000

vCPU cost = 0.5 × 2,628,000 × $0.000024 = $31.54
Memory cost = 1.0 × 2,628,000 × $0.000003 = $7.88

Monthly total (1 replica) = $39.42
```

### Free Tier
- 180,000 vCPU-seconds per month
- 360,000 GiB-seconds per month
- 2 million requests per month

---

## PostgreSQL Flexible Server

### Compute Pricing (East US 2)

| Tier | SKU | vCores | Memory | Price/Hour |
|------|-----|--------|--------|------------|
| Burstable | B1ms | 1 | 2 GB | ~$0.0175 |
| Burstable | B2s | 2 | 4 GB | ~$0.0350 |
| General Purpose | D2s_v3 | 2 | 8 GB | ~$0.1240 |
| General Purpose | D4s_v3 | 4 | 16 GB | ~$0.2480 |
| Memory Optimized | E2s_v3 | 2 | 16 GB | ~$0.1450 |

### Storage Pricing

| Type | Price per GB/Month |
|------|-------------------|
| Premium SSD | ~$0.115 |
| Backup (up to 100% of storage) | Free |
| Additional backup | ~$0.095 |

### Example Calculation

D2s_v3 with 128 GB storage:
```
Compute = $0.1240 × 730 hours = $90.52/month
Storage = $0.115 × 128 GB = $14.72/month

Monthly total = $105.24
```

---

## Azure Cache for Redis

### Enterprise Tier

| SKU | Cache Size | Price/Month (approx) |
|-----|-----------|---------------------|
| E10 | 12 GB | ~$380 |
| E20 | 25 GB | ~$760 |
| E50 | 50 GB | ~$1,520 |
| E100 | 100 GB | ~$3,040 |

### Basic/Standard Tier

| SKU | Cache Size | Price/Month (approx) |
|-----|-----------|---------------------|
| C0 | 250 MB | ~$16 |
| C1 | 1 GB | ~$40 |
| C2 | 2.5 GB | ~$73 |
| C3 | 6 GB | ~$147 |

---

## Storage Account (Blob)

### Hot Tier - LRS (East US 2)

| Component | Price |
|-----------|-------|
| Storage | $0.0184 per GB/month |
| Write ops (10K) | $0.05 |
| Read ops (10K) | $0.004 |
| List ops (10K) | $0.05 |
| Data retrieval | $0.00 |

### Cool Tier - LRS

| Component | Price |
|-----------|-------|
| Storage | $0.01 per GB/month |
| Write ops (10K) | $0.10 |
| Read ops (10K) | $0.01 |
| Data retrieval | $0.01 per GB |

---

## Key Vault

### Standard Tier

| Operation Type | Price |
|---------------|-------|
| Secrets operations (10K) | $0.03 |
| Keys operations (10K) | $0.03 |
| Certificate operations (10K) | $0.03 |
| Certificate renewals | $3.00 each |

Typical monthly cost for small deployment: < $5

---

## Container Registry

| Tier | Price/Day | Storage | Included Bandwidth |
|------|-----------|---------|-------------------|
| Basic | $0.167 | 10 GB | - |
| Standard | $0.667 | 100 GB | - |
| Premium | $1.667 | 500 GB | - |

### Geo-replication (Premium only)

Additional ~$1.667 per day per replica region

---

## Private Endpoints

| Component | Price |
|-----------|-------|
| Private endpoint (per hour) | $0.01 |
| Data processed (per GB) | $0.01 (after first 100 GB) |

### Monthly Cost per Endpoint
```
$0.01 × 730 hours = $7.30/month
```

5 Private Endpoints = ~$36.50/month

---

## Virtual Network

| Component | Price |
|-----------|-------|
| VNet | Free |
| Subnets | Free |
| VNet Peering (same region) | $0.01 per GB |
| VNet Peering (cross-region) | $0.035 per GB |

---

## Log Analytics

| Component | Price |
|-----------|-------|
| Data ingestion | $2.76 per GB |
| Data retention (first 31 days) | Free |
| Data retention (beyond 31 days) | $0.10 per GB/month |
| Basic logs ingestion | $0.65 per GB |

---

## Reserved Capacity Discounts

| Term | Discount |
|------|----------|
| 1 Year Reserved | ~20% |
| 3 Year Reserved | ~40% |

Available for:
- PostgreSQL Flexible Server
- Redis Enterprise
- Container Apps (Dedicated Plan)

---

## Cost Optimization Tips

1. **Use Burstable VMs** for non-production PostgreSQL
2. **Scale to zero** Container Apps when not in use
3. **Use Cool storage** for infrequently accessed data
4. **Reserve capacity** for predictable workloads
5. **Right-size** based on actual usage metrics
6. **Use Azure Cost Management** to monitor spending

---

## Important Notes

1. Prices shown are estimates and may vary
2. Always verify with official pricing pages
3. Enterprise agreements may have different pricing
4. Taxes are not included
5. Data transfer costs may apply
6. Prices vary by region
