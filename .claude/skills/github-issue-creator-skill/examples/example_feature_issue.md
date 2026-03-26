# Issue: Functional Candidate Search with Mock Data

**Dependencies:** Issue - Refactor Candidate Search into Modular Template Components  
**Estimated Complexity:** Medium - Connecting templates to functional logic

---

## Description

Transform modular template components into fully functional candidate search page with filtering, stats, and pagination.

**What This Builds:**
- Working candidate search at /candidates/search/
- View logic with mock candidate data generation
- Filter operations (skills, experience, location, salary, keywords)
- Stats calculation for badge display
- Pagination for result sets
- Fully interactive UI

**What This Enables:**
- Real user interaction with search
- Foundation for CBV conversion
- Testable search and filter logic
- Pattern for data-to-template integration

**Why This Matters:**
Bridges gap between static templates and production features. Creates functional core that will be enhanced with HTMX and AI.

---

## Technical Approach

### Architecture Overview

```
User Request
     ↓
Django FBV (candidate_search_view)
     ↓
Generate/Filter Mock Candidates
     ↓
Calculate Stats
     ↓
Render with Modular Templates
```

**Key Components:**
- **FBV:** Handles requests, coordinates logic
- **Mock Data Generator:** Creates realistic candidates
- **Filter Service:** Applies user filter selections
- **Stats Calculator:** Badge counts
- **Templates:** Display results (already built)

### Mock Data Strategy

Generate 50-75 diverse candidates with realistic combinations:
- Skills match experience level (senior → advanced skills)
- Salary appropriate for experience
- Geographic distribution
- Good Fit ~40%, Contacted ~15%, Replied ~5%

**Data Structure:**
```python
candidate = {
    'id': 1,
    'name': 'Adam Smith',
    'title': 'Senior Network Engineer',
    'skills': ['Python', 'AWS', 'Network Monitoring'],
    'experience_years': 12,
    'good_fit': True,
    # ... etc
}
```

**Think about:**
- Store in memory vs separate file?
- How to make skills realistic (Python + Django, not random)?
- Should some candidates have missing fields for edge case testing?

---

## Tasks

### 1. Create View Function

**Create:** `recruitment/candidates/views.py`

Implement FBV handling search requests.

**Pattern:**
```python
def candidate_search_view(request):
    # Parse filter params from request.GET
    filters = {
        'skills': request.GET.getlist('skills'),
        'experience': request.GET.get('experience'),
        # ... etc
    }
    
    # Get/generate candidates
    # Apply filters
    # Calculate stats
    # Paginate
    # Build context
    # Render template
    
    return render(request, 'candidates/search.html', context)
```

**Think about:**
- Generate mock data on each request or cache?
- How to structure filter parsing?

---

### 2. Generate Mock Candidate Data

**Create:** `recruitment/candidates/mock_data.py`

Generate diverse, realistic candidates.

**Pattern:**
```python
def generate_mock_candidates():
    # List to hold candidates
    # Generate in batches (10 at a time, 5 batches = 50)
    # For each candidate:
    #   Assign realistic skills based on role
    #   Set salary based on experience
    #   Distribute good_fit/contacted/replied
    # Return candidate list
    pass
```

**Think about:**
- How to ensure skill combinations make sense?
- Should we include edge cases (missing fields)?

---

### 3. Implement Filter Logic

**Add to view:** Filter operations

Implement filters for skills (multi-select), experience (range), location, salary, keywords.

**Pattern:**
```python
def apply_filters(candidates, filters):
    filtered = candidates
    
    # Skills filter
    if filters.get('skills'):
        # AND logic: has ALL selected skills
        # OR logic: has ANY selected skill
        # Your choice - document it
        pass
    
    # Experience filter
    # Location filter
    # Salary range filter
    # Keyword search
    
    return filtered
```

**Think about:**
- Skills filter: AND vs OR logic?
- Location: exact match or contains?
- Which filters narrow results most? Apply those first.

---

### 4. Calculate Stats for Badges

**Add to view:** Stats calculation

Calculate counts for badge display.

**Pattern:**
```python
def calculate_stats(candidates):
    return {
        'total': len(candidates),
        'good_fit': len([c for c in candidates if c['good_fit']]),
        'contacted': len([c for c in candidates if c['contacted']]),
        'replied': len([c for c in candidates if c['replied']]),
    }
```

Your stats_badges.html template expects this structure.

---

### 5. Wire Up URL Routing

**Create:** `recruitment/candidates/urls.py`

Configure URL pattern and include in main URLs.

**Pattern:**
```python
# recruitment/candidates/urls.py
urlpatterns = [
    path('search/', candidate_search_view, name='candidate_search'),
]

# Main urls.py
path('candidates/', include('recruitment.candidates.urls')),
```

---

### 6. Add Pagination

**Add to view:** Paginate large result sets

Use Django's Paginator.

**Pattern:**
```python
from django.core.paginator import Paginator

paginator = Paginator(filtered_candidates, 25)
page_number = request.GET.get('page', 1)
page_obj = paginator.get_page(page_number)

context['candidates'] = page_obj
```

**Think about:**
- Should filters reset pagination to page 1?
- How to maintain filter state across page navigation?

---

## Testing

### Manual Testing Flow

1. Navigate to /candidates/search/
2. Verify page loads with all mock candidates
3. Select skill filter (e.g., "Python") → Results update
4. Add experience filter (e.g., "5-10 years") → Results narrow
5. Enter search keywords → Results filter by text
6. Clear all filters → Full list returns
7. Navigate through pages → Verify pagination works
8. Check stats badges show correct counts

### Filter Combinations

Test multiple filters together:
- Skills: Python + Django
- Experience: 5-10 years
- Location: Chicago
- Verify: Only candidates matching ALL criteria appear

### Edge Cases

- No results: Very restrictive filter combination
- All candidates: Clear all filters
- Single result: Specific combination
- Missing data: Candidates with null fields
- Page boundaries: Last page with < 25 results

---

## Acceptance Criteria

**Functionality:**
- [ ] FBV created in recruitment/candidates/views.py
- [ ] Mock data generator creates 50+ realistic candidates
- [ ] All filter types working (skills, experience, location, salary, keywords)
- [ ] Filters can be combined (AND logic across filter types)
- [ ] Stats badges show correct counts after filtering
- [ ] "Clear All Filters" resets to full list
- [ ] Pagination works (25 per page)
- [ ] URL routing configured correctly

**Code Quality:**
- [ ] View logic clean and organized
- [ ] Helper functions for filtering/stats
- [ ] Mock data has realistic combinations
- [ ] No hardcoded URLs in templates

**User Experience:**
- [ ] Page is fully interactive
- [ ] Filter state visible in sidebar
- [ ] Loading states (if applicable)
- [ ] No template rendering errors
- [ ] Mobile responsive

---

## Notes

### Using Claude Code Effectively

**For Mock Data Generation:**
"Generate 75 candidates with varied technical skills across backend (Python, Java), frontend (React, Angular), mobile (Swift, Kotlin), devops (Docker, K8s), and data science (TensorFlow, PyTorch). Include realistic salary ranges and geographic distribution."

**For Filter Logic:**
Claude Code can help implement clean filter patterns. Share your data structure and desired filter behavior.

**For Testing:**
Use Claude Code to help write comprehensive test scenarios covering all filter combinations.

### Django Patterns Reference

**Function-Based Views:**
Standard pattern for straightforward request handling. Keep logic in view, delegate complex operations to helper functions.

**Context Building:**
Build context dict with all data templates need. Better to pass too much than too little.

**Filter Pattern:**
Start with full dataset, progressively filter based on parameters. Maintain clear filter order (most restrictive first).

### Mock Data Best Practices

**Realistic Combinations:**
- Python developer → Django, PostgreSQL, AWS (makes sense)
- Frontend developer → React, TypeScript, Jest (makes sense)
- Don't randomly assign skills

**Distribution:**
- ~40% Good Fit (realistic conversion rate)
- ~15% Contacted (active pipeline)
- ~5% Replied (realistic response rate)

**Edge Cases:**
Include some candidates with:
- Missing fields (test null handling)
- Unusual skill combinations
- Very high/low experience

### Common Pitfalls

1. **Over-filtering:** Filters too restrictive → no results
2. **Under-filtering:** Not actually filtering → all results shown
3. **Filter state loss:** Pagination clears filters
4. **Stats miscalculation:** Counting wrong subset
5. **Template expectations:** Context missing expected keys

### Filter Architecture Decisions

**Skills Filter - AND vs OR:**
- **AND:** Candidate must have ALL selected skills (more restrictive, precise results)
- **OR:** Candidate has ANY selected skill (more results, broader matches)

Your call based on use case. Document choice in code.

**Location Matching:**
- Exact string match (simple)
- Contains substring (more flexible - "Chicago" matches "Greater Chicago Area")
- Normalized comparison (handle variations)

Consider which makes sense for your data.

### Future Migration Path

This FBV will later become a CBV with:
- Class structure for reusability
- HTMX for dynamic updates
- Registry integration for AI
- Real database models
- Additional enhancements as the feature matures

For now: Keep it simple, make it work, document patterns.

---

## Related Issues

- Depends on: Refactor Candidate Search into Modular Template Components
- Blocks: HTMX Integration for Dynamic Filtering
- Blocks: AI-Powered Candidate Matching

---

## Additional Context

This creates the functional foundation - after this, converting to CBV and adding HTMX is straightforward since the core logic exists and works.
