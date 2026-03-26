# Navigation Structure Reference

## Complete _nav.yaml Template

```yaml
navigation:
  # ============================================
  # GETTING STARTED
  # ============================================
  - title: Getting Started
    slug: getting-started
    icon: fa-rocket
    children:
      - title: Welcome to TalentAI
        slug: getting-started/welcome
      - title: Your First Day
        slug: getting-started/first-day
      - title: Quick Start Guide
        slug: getting-started/quick-start
      - title: Keyboard Shortcuts
        slug: getting-started/shortcuts

  # ============================================
  # FINDING CANDIDATES
  # ============================================
  - title: Finding Candidates
    slug: candidates
    icon: fa-users
    children:
      - title: Search Basics
        slug: candidates/search-basics
      - title: Using Filters
        slug: candidates/filters
      - title: Advanced Search
        slug: candidates/advanced-search
      - title: Saving Searches
        slug: candidates/saved-searches
      - title: Candidate Profiles
        slug: candidates/profiles
      - title: Candidate Lists
        slug: candidates/lists
      - title: Adding Notes
        slug: candidates/notes

  # ============================================
  # MANAGING JOBS
  # ============================================
  - title: Managing Jobs
    slug: jobs
    icon: fa-briefcase
    children:
      - title: Job Dashboard
        slug: jobs/dashboard
      - title: Creating a Job
        slug: jobs/creating
      - title: Job Details
        slug: jobs/details
      - title: Matching Candidates
        slug: jobs/matching
      - title: Job Pipeline
        slug: jobs/pipeline
      - title: Closing Jobs
        slug: jobs/closing

  # ============================================
  # COMMUNICATION
  # ============================================
  - title: Communication
    slug: communication
    icon: fa-envelope
    children:
      - title: Email Overview
        slug: communication/overview
      - title: Email Templates
        slug: communication/templates
      - title: Sending Emails
        slug: communication/sending
      - title: Bulk Email
        slug: communication/bulk
      - title: Email History
        slug: communication/history
      - title: Email Best Practices
        slug: communication/best-practices

  # ============================================
  # CALENDAR & SCHEDULING
  # ============================================
  - title: Calendar
    slug: calendar
    icon: fa-calendar
    children:
      - title: Calendar Overview
        slug: calendar/overview
      - title: Viewing Your Calendar
        slug: calendar/viewing
      - title: Scheduling Interviews
        slug: calendar/scheduling
      - title: Managing Events
        slug: calendar/events
      - title: Calendar Settings
        slug: calendar/settings

  # ============================================
  # ANALYTICS & REPORTS
  # ============================================
  - title: Analytics
    slug: analytics
    icon: fa-chart-bar
    children:
      - title: Dashboard Overview
        slug: analytics/dashboard
      - title: Understanding Metrics
        slug: analytics/metrics
      - title: Running Reports
        slug: analytics/reports
      - title: Exporting Data
        slug: analytics/exporting

  # ============================================
  # JOBDIVA INTEGRATION
  # ============================================
  - title: JobDiva Sync
    slug: jobdiva
    icon: fa-sync
    children:
      - title: About JobDiva Sync
        slug: jobdiva/overview
      - title: Synced Data
        slug: jobdiva/data
      - title: Sync Status
        slug: jobdiva/status
      - title: Troubleshooting Sync
        slug: jobdiva/troubleshooting

  # ============================================
  # TIPS & BEST PRACTICES
  # ============================================
  - title: Tips & Best Practices
    slug: tips
    icon: fa-lightbulb
    children:
      - title: Sourcing Best Practices
        slug: tips/sourcing
      - title: Search Strategies
        slug: tips/search-strategies
      - title: Email Outreach Tips
        slug: tips/email-outreach
      - title: Power User Features
        slug: tips/power-user
      - title: Time-Saving Shortcuts
        slug: tips/shortcuts

  # ============================================
  # FAQ & TROUBLESHOOTING
  # ============================================
  - title: FAQ
    slug: faq
    icon: fa-question-circle
    children:
      - title: Common Questions
        slug: faq/common
      - title: Account & Settings
        slug: faq/account
      - title: Troubleshooting
        slug: faq/troubleshooting
      - title: Getting Help
        slug: faq/help
```

## Icon Reference

Available Font Awesome 5 icons:

| Section | Icon | Class |
|---------|------|-------|
| Getting Started | Rocket | `fa-rocket` |
| Candidates | Users | `fa-users` |
| Jobs | Briefcase | `fa-briefcase` |
| Communication | Envelope | `fa-envelope` |
| Calendar | Calendar | `fa-calendar` |
| Analytics | Chart Bar | `fa-chart-bar` |
| JobDiva | Sync | `fa-sync` |
| Tips | Lightbulb | `fa-lightbulb` |
| FAQ | Question Circle | `fa-question-circle` |

## Slug Conventions

- Use lowercase
- Use hyphens for spaces: `search-basics` not `search_basics`
- Keep short but descriptive
- Match folder structure: `candidates/filters` → `candidates/filters.md`

## File Mapping

| Slug | File Path |
|------|-----------|
| `getting-started` | `getting-started/index.md` |
| `getting-started/welcome` | `getting-started/welcome.md` |
| `candidates` | `candidates/index.md` |
| `candidates/filters` | `candidates/filters.md` |

## Adding New Articles

1. Create the markdown file in the correct folder
2. Add entry to `_nav.yaml` under appropriate section
3. Upload both files to Azure Blob Storage
4. Test navigation in help center

## Section Guidelines

**Maximum children per section:** 8-10 articles
**If more needed:** Consider splitting into sub-sections

**Order articles by:**
1. Most common/important first
2. Logical workflow order
3. Basic → Advanced progression
