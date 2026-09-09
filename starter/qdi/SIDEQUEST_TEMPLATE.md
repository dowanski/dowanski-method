# QDI Sidequest — `{{ID_AND_TITLE}}`

Status: Proposed  
Created: `{{DATE}}`  
Owner: `{{OWNER_OR_ROLE}}`
Record ID: `{{ALLOCATED_QDI_CYCLE_SIDEQUEST_ID}}`
Research level: `{{LIGHT_SCAN_STANDARD_RESEARCH_OR_DEEP_RESEARCH}}`

Use this packet for dedicated research, not every quick lookup. Select the level
under the [Research selection](DISCOVERY_ANCHORS.md#research-selection) rules.
A routine check within existing read-only scope can be recorded directly in
the Ledger without a new packet.

The coordinator allocates this ID through `QDI_RECORD_INDEX.md` before other
records reference the sidequest.

## Trigger and return

- Triggering anchor or branch: `{{EXACT_POSITION}}`
- Unresolved question: `{{QUESTION_CONVERSATION_CANNOT_RESOLVE}}`
- Why conversation is insufficient: `{{REASON}}`
- Decision this work must inform: `{{DECISION}}`
- Why this research level is sufficient: `{{EVIDENCE_NEED_NOT_PRESTIGE}}`
- Saved phase: `{{PHASE_TO_RESUME}}`
- Exact return point: `{{WHERE_QDI_RESUMES}}`

The return point must be recorded in `CURRENT_STATE.md` before this sidequest
becomes active.

## Scope

- Included: `{{BOUNDED_SCOPE}}`
- Excluded: `{{EXPLICIT_EXCLUSIONS}}`
- Relevant geography, period, population, or environment: `{{CONTEXT_OR_NONE}}`
- Starting assumptions: `{{ASSUMPTIONS_TO_TEST}}`
- Evidence already available: `{{REUSE_OR_EXPLAIN_WHY_STALE_OR_INSUFFICIENT}}`

## Evidence and actions

- Permitted sources: `{{SOURCE_BOUNDARY}}`
- Permitted actions: `{{READ_ONLY_OR_EXACT_ACTIONS}}`
- Evidence standard: `{{WHAT_COUNTS_AS_SUPPORT}}`
- Required deliverable: `{{REPORT_TEST_PROTOTYPE_OR_REVIEW}}`
- Confidence and limitation language: `{{EXPECTED_CALIBRATION}}`
- Tool availability checked: `{{AVAILABLE_OR_LIMITATION}}`
- Counterevidence or conflicting sources to assess: `{{RELEVANT_CHECKS}}`

If the needed tools or sources are unavailable, report the limitation before
claiming progress. Do not invent searches or substitute memory for inspected
current evidence. Offer supplied sources, narrower work, or deferral.

## Authority

- Read-only work authorized: `Yes / No / Limited to ...`
- Account access authorized: `No / Exact account and scope`
- External contact authorized: `No / Exact party and message boundary`
- Spending authorized: `No / Exact approved limit`
- System mutation authorized: `No / Exact target and reversible action`

Unresolved authority means the corresponding action is prohibited.

## Effort and checkpoints

- Approved effort/time boundary: `{{BOUND_OR_OWNER_AGREED_REVIEW_INTERVAL}}`
- Spending/token ceiling, if measurable and authorized: `{{BOUND_OR_UNAVAILABLE}}`
- Next checkpoint and report: `{{WHEN_AND_WHICH_DECISION_GAPS_TO_REPORT}}`

Deep Research may exceed thirty minutes when justified and authorized; it is
not complete merely because time passed or a source count was reached. Never
invent usage percentages. At the boundary, stop and report; extending research
requires applicable authority, not silent scope growth. Preserve effort for
verification, synthesis, documentation, and return. Do not weaken evidence to
fit a ceiling: surface what remains unresolved instead.

## Stop conditions

Stop when:

- `{{THE_DECISION_HAS_SUFFICIENT_EVIDENCE}}`;
- `{{THE_APPROVED_TIME_OR_COST_BOUNDARY_IS_REACHED}}`;
- `{{A_NEW_PERMISSION_OR_SPECIALIST_REQUIREMENT_APPEARS}}`;
- `{{THE_SOURCE_STATE_CANNOT_BE_VERIFIED}}`.

## Human gate before activation

The human chooses one:

- [ ] Run this sidequest now.
- [ ] Narrow it first.
- [ ] Record it and continue QDI.
- [ ] Accept the unknown as a stated limitation.
- [ ] Pause or stop the project.

Decision and date: `{{PENDING}}`
Prior authorization, if applicable: `{{EXACT_ACCEPTED_SCOPE_AND_RECORD_OR_NONE}}`

The human may authorize a bounded research plan in advance; cite that decision
only when this packet actually fits it. Otherwise present the recommendation
and obtain a decision before activation. Approach A–D alone is not approval.

## Findings

### Evidence found

`{{NOT_YET_RUN}}`

### Inference and confidence

`{{NOT_YET_RUN}}`

### Disagreement or missing evidence

`{{NOT_YET_RUN}}`

### What changed, survived, or remains open

`{{NOT_YET_RUN}}`

### Newly earned questions

`{{NOT_YET_RUN}}`

### Coverage resolved without re-questioning

`{{AFFECTED_ANCHORS_AND_CANONICAL_EVIDENCE}}`

### Recommendation and human decision needed

`{{ACCEPT_DIRECTION_COMPARE_RESEARCH_FURTHER_OR_REVIEW_BLUEPRINT_WITH_REASON}}`

## Return record

- Completion status: `Not started`
- Ledger updated: `No`
- Current State updated: `No`
- Return point restated to human: `No`
- QDI resumed at: `{{SAVED_RETURN_POINT}}`
- Human confirmation: `Pending`

Record material findings automatically within the agreed storage boundary.
Ask for acceptance of consequential direction, not permission for every note.
Explain why new evidence changes the next move; resume the saved point or
explicitly reconcile a changed direction. Raw reports become reference after
their useful evidence and limitations are integrated.
