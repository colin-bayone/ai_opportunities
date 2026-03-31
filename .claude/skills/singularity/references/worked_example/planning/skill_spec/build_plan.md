# Singularity Skill Build Plan

**Date:** 2026-03-28
**Status:** IN PROGRESS

---

## Build Order

### Phase 1: SKILL.md (The Core) ✅ COMPLETE
- [x] Write frontmatter (name, description, allowed-tools)
- [x] Write the invocation flow (what happens when user types /singularity)
- [x] Write hard rules
- [x] Write the mandatory permission check procedure
- [x] Write Flow 1: New Engagement
- [x] Write Flow 2: Continue Engagement
- [x] Write Flow 3: Process Source Material
- [x] Write Flow 4: Create Deliverable
- [x] Write Flow 5: Pricing
- [x] Write Flow 6: Discussion
- [x] Write reference loading instructions (which ref to load when)
- [x] Write sibling skill awareness (big4, pptx-extractor, pdf-extractor, slide skill)
- [x] Write company context loading (.claude/context/)
- [x] Write glossary and web research sections
- [x] Write cross-session artifacts section

### Phase 2: References (Detailed Methodology) ✅ COMPLETE
- [x] blockchain_methodology.md (from spec 01)
- [x] document_processing.md (from spec 02)
- [x] folder_structure.md (from spec 03)
- [x] people_tracking.md (from spec 04)
- [x] agent_architecture.md (from spec 05)
- [x] deliverables_pipeline.md (from spec 06)
- [x] session_continuity.md (from spec 07)
- [x] pricing_workflow.md (from spec 09)
- [x] anti_patterns.md (copy from big4)
- [x] professional_standards.md (copy from big4)

### Phase 3: Assets ✅ COMPLETE
- [x] Copy design spec v2.0 to assets/design/bayone_design_spec.md
- [x] Copy 5 gold standard HTMLs to assets/design/gold_standards/
- [x] Copy proposal template from sales-forge to assets/templates/
- [x] Copy ProjectCostingTemplate.xlsx to assets/templates/
- [x] Copy excel_template_prompt.md to assets/prompts/

### Phase 4: Scripts ✅ COMPLETE
- [x] Copy html_to_pdf.py from sales-forge to scripts/

### Phase 5: Hook ✅ COMPLETE
- [x] Write singularity_stop.py at .claude/hooks/
- [x] Add Write($CLAUDE_PROJECT_DIR/**) to settings.local.json
- [x] Add singularity stop hook to settings.local.json

### Phase 6: Validate
- [x] Verify complete file tree
- [x] Test hook script runs without errors
- [ ] Test invocation in a new session

### Phase 7: Rebuild via skill-forge (proper workflow)
- [x] Pre-flight checks passed
- [x] Step 0: Onboarding question asked
- [x] Step 1: Questions asked (description, inline vs reference, hooks, bridge docs, methodology template, enforcement)
- [x] Read all 13 spec documents via agent
- [x] Read gap analysis
- [x] Read existing draft SKILL.md
- [x] Read skill-forge references (skill_structure, scripts_context, hooks_system, new_features_update)
- [x] Read actual bridge document gold standard from research/
- [x] Read actual methodology document from research/
- [x] Step 2: Planning (identified all gaps, determined inline vs reference for each)
- [x] Step 3: Generated - SKILL.md rewritten with all critical and important gaps fixed:
  - [x] Document header format inline
  - [x] Agent prompt template inline with complete example
  - [x] Methodology doc as asset template
  - [x] Bridge document timing explicit in Flow 3 step 7
  - [x] Bridge document gold standard added to assets
  - [x] WebSearch added to permission check
  - [x] Org chart update timing explicit in Flow 3 step 6
  - [x] Strategy discussion proactive offering in Flow 6
  - [x] Pricing discussion captured as research set in Flow 5 step 4
  - [x] Complete deliverable type list in Flow 4
  - [x] Marker file explained in dedicated section
  - [x] Speech-to-text examples in agent prompt template
  - [x] Sibling skills with "how to offer" language
  - [x] Glossary creation triggers specified
  - [x] Discussion rules (capture reasoning, flag open items, distinguish hyperbole)
  - [x] Letter suffix convention mentioned in Flow 3
  - [x] Cover label convention noted (thematic, not literal)
- [ ] Step 3.5: Settings already configured from first pass
- [ ] Step 4: Run validation

---

## Key Design Decisions

### What happens when user types /singularity?

**Step 0: Permission Check (silent, automatic)**
1. Read .claude/settings.local.json
2. Verify Write($CLAUDE_PROJECT_DIR/**) exists
3. Verify WebSearch exists
4. If missing, stop and ask to add

**Step 1: Ask "What are we doing today?"**
Options:
1. **New engagement** - "I have a new client/opportunity to organize"
2. **Continue engagement** - "Pick up where we left off on [client/opportunity]"
3. **Process new source material** - "I have a new transcript/email/document to add"
4. **Create a deliverable** - "I need to draft a document for the client"
5. **Pricing** - "I need to build a pricing model"
6. **Discussion** - "I want to think through strategy/approach"

**Each option triggers a different flow:**

#### Option 1: New Engagement
- Ask: Client name? Opportunity name?
- Ask: What source material do you have? (transcripts, emails, docs, call preps)
- Ask: Which folders do you need? (default: all)
- Create folder structure at /<client_name>/<opportunity_name>/
- Create methodology doc
- Create marker file (.singularity_active)
- Load .claude/context/bayone_team.md
- Begin processing source material

#### Option 2: Continue Engagement
- Ask: Which engagement? (or detect from cwd)
- Read handoff doc if exists
- Read methodology doc
- Read skill notes
- Read latest summaries
- Read org chart
- Report state and ask what to do next

#### Option 3: Process Source Material
- Ask: Which engagement?
- Ask: What type? (transcript, email, call prep, debrief, other)
- Ask: Is this a new event (new set number) or supplementary (letter suffix)?
- Load appropriate reference (document_processing.md)
- Begin multi-pass processing with agent dispatch

#### Option 4: Create Deliverable
- Ask: Which engagement?
- Ask: What type? (problem restatement, info request, approach, proposal, email)
- Load deliverables_pipeline.md reference
- Load appropriate gold standard
- Load anti_patterns.md and professional_standards.md
- Draft markdown first, then HTML

#### Option 5: Pricing
- Ask: Which engagement?
- Load pricing_workflow.md reference
- Run questionnaire
- Build pricing spec
- Offer to create Excel handoff prompt

#### Option 6: Discussion
- Ask: Which engagement?
- Read prior context
- Propose discussion topics based on open threads
- Capture as discussion set in research/

### What references load when?

| User Action | References Loaded |
|---|---|
| New engagement | folder_structure.md, blockchain_methodology.md |
| Process transcript | document_processing.md, agent_architecture.md, people_tracking.md |
| Process call prep | document_processing.md |
| Process debrief | document_processing.md, people_tracking.md |
| Create deliverable | deliverables_pipeline.md, anti_patterns.md, professional_standards.md |
| Pricing | pricing_workflow.md |
| Continue engagement | session_continuity.md |
| Strategy discussion | (none needed beyond what's in SKILL.md) |

### Hook Behavior

**Marker file:** `/<client_name>/<opportunity_name>/.singularity_active`
- Created at engagement start
- Contains JSON: {"client": "...", "opportunity": "...", "started": "date"}
- Checked by stop hook
- Removed when user explicitly says they're done

**Stop hook checks:**
1. Is .singularity_active present anywhere? If not, exit 0 (not our session)
2. If present, check stop_hook_active (loop prevention)
3. Verify methodology doc exists
4. Verify org chart exists
5. If issues found, exit 2 with message

---

## Token Budget Estimate

SKILL.md target: ~400 lines (~4000 tokens)
- Frontmatter: ~20 lines
- Hard rules: ~30 lines
- Permission check: ~20 lines
- Phase descriptions: ~250 lines (lean, pointing to references)
- Reference loading guide: ~40 lines
- Sibling skills: ~20 lines
- Company context: ~10 lines

References: ~800 lines each average, loaded on demand
Assets: zero tokens (referenced by path)
Scripts: zero tokens (output only)
