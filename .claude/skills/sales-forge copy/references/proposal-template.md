# Proposal Template Guide

Structure and patterns for generating BayOne proposal documents.

## Document Structure

```
1. Cover Page
2. The Challenge (01)
3. Our Approach (02)
4. Capabilities Aligned (03)
5. Proposed Engagement (04)
6. Why BayOne (05)
7. Next Steps (06)
8. Footer
```

## Section Patterns

### Cover Page

```html
<div class="cover">
  <div class="cover-content">
    <div class="cover-label">Strategic Proposal</div>
    <h1>{Title}</h1>
    <p class="cover-subtitle">{Subtitle - what we're proposing}</p>
    <div class="cover-meta">
      <div class="cover-meta-item">
        <label>Prepared For</label>
        <span>{Client Name}</span>
      </div>
      <div class="cover-meta-item">
        <label>Date</label>
        <span>{Month Year}</span>
      </div>
      <div class="cover-meta-item">
        <label>Classification</label>
        <span>Confidential</span>
      </div>
    </div>
  </div>
  <div class="logo">Bay<span>One</span> Solutions</div>
</div>
```

### The Challenge Section

Show we understand their problem. Include:
- Lead paragraph with context
- Stat cards for key numbers
- Highlight box for core bottleneck

```html
<div class="section">
  <div class="section-number">01</div>
  <h2>The Challenge</h2>
  <p class="lead">{Context paragraph}</p>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-value">{Number}</div>
      <div class="stat-label">{Label}</div>
    </div>
    <!-- More stat cards -->
  </div>

  <div class="highlight-box">
    <p><strong>Core bottleneck:</strong> {Key problem statement}</p>
  </div>
</div>
```

### Our Approach Section

Present methodology without being overly technical:

```html
<div class="section">
  <div class="section-number">02</div>
  <h2>Our Approach: {Approach Name}</h2>
  <p class="lead">{High-level description}</p>

  <h3>{Capability 1}</h3>
  <p>{Description}</p>

  <h3>{Capability 2}</h3>
  <p>{Description}</p>
</div>
```

### Capabilities Table

Map their problems to our solutions:

```html
<div class="section">
  <div class="section-number">03</div>
  <h2>Capabilities Aligned to Your Needs</h2>

  <table>
    <thead>
      <tr>
        <th>Your Challenge</th>
        <th>Our Capability</th>
        <th>Expected Impact</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{Problem}</td>
        <td>{Solution}</td>
        <td>{Outcome}</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Proposed Engagement (Phases)

Use cards for phases:

```html
<div class="section">
  <div class="section-number">04</div>
  <h2>Proposed Engagement</h2>
  <p class="lead">{Phased approach intro}</p>

  <div class="card">
    <div class="phase-header">
      <div class="phase-number">1</div>
      <div>
        <div class="phase-title">{Phase Name}</div>
        <div class="phase-duration">{Scope description}</div>
      </div>
    </div>
    <p>{Phase details}</p>
  </div>

  <!-- More phase cards -->
</div>
```

### Why BayOne

Differentiation without overselling:

```html
<div class="section">
  <div class="section-number">05</div>
  <h2>Why BayOne</h2>
  <p class="lead">{Credibility statement}</p>

  <p>{Experience paragraph}</p>

  <div class="highlight-box">
    <p>{Key differentiator}</p>
  </div>
</div>
```

### Next Steps

Concrete actions:

```html
<div class="section">
  <div class="section-number">06</div>
  <h2>Next Steps</h2>
  <p>{Call to action}</p>

  <table>
    <thead>
      <tr>
        <th>Action</th>
        <th>Participants</th>
        <th>Outcome</th>
      </tr>
    </thead>
    <tbody>
      <!-- Action items -->
    </tbody>
  </table>
</div>
```

## Content Guidelines

### Tone
- Proposal-led, not discovery-led
- "Here's how we would help" not "Tell us your problems"
- Confident but not arrogant
- Show we did the homework

### What to Include
- Client's specific pain points (not generic)
- Quantified scope where possible
- Phased approach with clear milestones
- Why we're right for this (experience, credibility)
- Concrete next steps

### What to Avoid
- Timelines with specific dates/durations
- Pricing (separate conversation)
- Overselling or promises we can't keep
- Generic content not tailored to client
- Mentioning staffing if this is solutions track
