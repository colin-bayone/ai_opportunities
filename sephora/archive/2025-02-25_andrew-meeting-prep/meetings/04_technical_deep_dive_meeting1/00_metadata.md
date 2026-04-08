# Meeting 4 - Metadata

## Basic Information

| Field | Value |
|-------|-------|
| **Date** | Early March 2026 (estimated March 10-12 based on context) |
| **Type** | Technical Deep Dive / Demo Scoping |
| **Location** | Virtual (Video Call) |
| **Duration** | ~45-50 minutes (estimated from transcript) |
| **Meeting Number** | 4 of 4 (in Sephora engagement series) |

## Attendees

### BayOne
| Name | Role | Participation |
|------|------|---------------|
| Colin Moore | Director of AI | Primary presenter, technical lead |
| Neha Malhotra | VP of Growth and Customer Success | Meeting facilitator |
| Zahra Syed | Sales | Support, meeting coordination |
| Rahul Bobbili | President | On call (minimal participation) |

### Sephora
| Name | Role | Participation |
|------|------|---------------|
| Andrew Ho | Sr. Director, Data & Analytics | Vision owner, decision maker on call |
| Gariashi Chakrabarty | Director, Data Engineering / BI & Analytics | Technical gatekeeper, execution lead |
| Maher Burhan | Enterprise Architect (Consultant) | Architecture validation |
| Sergei Shtypuliak | SME - IBM Tools, Consultant (Cognos, DataStage) | 10-15 year veteran, technical deep knowledge |
| Itisha Singh | Sephora team member | On call |

### Sephora (Not Present but Referenced)
| Name | Role | Context |
|------|------|---------|
| Vlad | CIO | Mani's boss, mentioned for report access |
| Mani Soundararajan | VP, Data & Analytics | Andrew & Gariashi's boss, decision maker |
| Monica | Sephora team member | Mentioned for coordinating Cognos report access |

## Organizational Hierarchy (Confirmed)

```
Vlad (CIO)
  └── Mani Soundararajan (VP)
        ├── Andrew Ho (Sr. Director)
        └── Gariashi Chakrabarty (Director)
              └── Sergei Shtypuliak (SME/Consultant)
        └── Maher Burhan (Enterprise Architect/Consultant)
```

## Transcription Corrections Applied

| Original | Corrected | Context |
|----------|-----------|---------|
| "Shaka" | Zahra Syed | BayOne sales team member |
| "my hair", "Mahir", "Malika" | Maher Burhan | Enterprise Architect (Consultant) |
| "Sir" (some contexts) | Sergei Shtypuliak | IBM tools SME (Consultant) |
| "Gaurishi", "Garishia", "Karish" | Gariashi Chakrabarty | Director, Data Engineering |
| "Cardinals", "Card notes", "coughing" | Cognos | IBM reporting tool |
| "Lake bridge" | Lakehouse | Databricks Lakehouse |
| "EW" | EDW | Enterprise Data Warehouse |

## Meeting Context

This was the technical deep dive meeting that followed Meeting 3. The purpose was to gather technical details from Sephora's architects (Mahar, Sergey) to scope a demo/POC.

**Key context:** There was initial confusion about expectations - Sephora expected to see a demo today, while BayOne expected to gather requirements for building a demo. This was resolved gracefully mid-meeting.

## Meeting Outcome

**Status:** Successful - Clear next steps established

**Agreed deliverables:**
1. Sephora to provide one Cognos report XML definition (from Finance track)
2. Sephora to provide Databricks schema/catalog information for target mapping
3. BayOne to build demo showing lift-and-shift conversion without direct system access
4. Optional: DataStage job definition for additional demo scope

## Source File

`sephora/context/meeting4-technical-deep-dive.txt`
