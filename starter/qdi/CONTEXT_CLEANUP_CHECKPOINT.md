# QDI Context Cleanup Checkpoint

Status: Not yet run  
Checkpoint scope: `Sidequest close / Branch close / QDI cycle close / Context-drag repair`  
Human owner: `{{OWNER_OR_ROLE}}`  
Date: `{{DATE}}`  
Record ID: `{{ALLOCATED_QDI_CYCLE_CLEANUP_ID}}`

## Purpose

Reduce active context without losing the decisions, evidence, responsibility, or
history the project may still need.

This checkpoint prevents completed discovery from remaining in the default
agent route after its value has changed. It also detects when maintaining and
rereading documentation is slowing the work it was meant to support.

Cleanup is active-context reduction, not automatic deletion.

## When this checkpoint is required

Run a contained checkpoint:

- when a sidequest closes;
- when a specialist branch closes;
- before the Pre-Build Blueprint enters Owner Review;
- before an approved QDI cycle becomes eligible for the later QDI-to-DM handoff;
- before a new Project, Workstream, or Work Packet QDI cycle inherits prior
  context;
- when a documentation-drag signal appears.

Sidequest and branch checkpoints may be brief. The pre-handoff checkpoint must
review the complete active QDI route.

A contained close uses the coordinator's recorded route-only self-review below;
it does not require another agent merely because a small investigation ended.
Independent resumption review is required before cycle-level Owner Review or
handoff, and after material routing/authority conflicts or recovery failures.
Human acceptance remains required; combine a contained cleanup review with the
substantive return decision when practical, rather than creating another meeting.

## Documentation-drag and bad-loop signals

Mark every signal observed:

- [ ] The agent repeatedly rereads or summarizes the same files before acting.
- [ ] Several documents claim to contain current truth for the same fact.
- [ ] A closed branch, sidequest, or packet remains in the active router.
- [ ] Old conclusions conflict with current owner-confirmed direction.
- [ ] The active agent must read historical material to identify the next action.
- [ ] More documentation is being created than decisions are being made.
- [ ] Routine status reporting or document maintenance is materially delaying
  useful discovery, verification, or implementation.
- [ ] The agent is caught in a loop of reviewing, rewriting, or repairing
  documentation without reducing uncertainty or advancing a gate.
- [ ] Placeholders, abandoned structures, or duplicate indexes remain active
  after their purpose ended.
- [ ] Raw evidence or logs are pasted into several Markdown files.
- [ ] The same search, test, tool call, or reasoning approach has repeated
  without a new hypothesis, source, changed state, or useful evidence.
- [ ] A resolved retry sequence remains in the active route even though only its
  cause, correction, evidence, or prevention rule is still relevant.
- [ ] Long outputs are being reloaded when a scoped result and reference would
  support the current decision.
- [ ] A high-effort lane expanded without a named decision, expected evidence,
  effort posture, or stopping condition.
- [ ] A new QDI cycle is inheriting the complete prior transcript instead of the
  smallest accepted parent truth.
- [ ] A fresh agent cannot identify current truth, authority, active objective,
  next action, and unresolved risk from the routed files.

If a signal is present, identify its cause. Do not respond by creating another
standing document unless the cause is a genuinely missing responsibility.

## Classification rule

Every reviewed record receives one disposition:

1. **KEEP_ACTIVE** — needed to understand or operate the current QDI lane.
2. **HANDOFF_CANDIDATE** — approved, decision-relevant truth that may enter the
   later QDI-to-DM handoff.
3. **REFERENCE** — potentially useful evidence that does not belong in the
   default reading route.
4. **ARCHIVE_PRIVATE** — completed or superseded history preserved outside the
   active path.
5. **REMOVE_REDUNDANT** — duplicate, abandoned, placeholder-only, or activity
   material whose removal has explicit human approval or is already preserved
   adequately through version history.

`REMOVE_REDUNDANT` is a recommendation until the human approves the exact file
or content. The agent must not delete consequential or uncertain material merely
because it appears old.

## Record inventory and disposition

Use a relative link or an existing stable identifier. Do not create identifiers
for every file merely to complete this table.

| Record | Current responsibility | Disposition | Canonical successor or destination | Reason | Human approval |
|---|---|---|---|---|---|
| `{{RELATIVE_LINK_OR_STABLE_ID}}` | `{{PURPOSE}}` | `{{DISPOSITION}}` | `{{LINK_ID_OR_NONE}}` | `{{WHY}}` | Pending |

## Canonical-truth check

For every duplicated or conflicting fact:

| Fact or decision | Current canonical home | Competing location | Resolution | Owner gate |
|---|---|---|---|---|
| `{{FACT}}` | `{{ACTIVE_LINK}}` | `{{OTHER_LINK}}` | Link / Supersede / Archive / Remove | `{{GATE}}` |

One active fact receives one canonical home. Other active records link to it
rather than reproducing the complete content.

## Active route after cleanup

List only what a fresh agent must read to resume the current lane:

1. `{{HUMAN_ENTRY_OR_PROJECT_README}}`
2. `{{CANONICAL_AGENT_INSTRUCTIONS}}`
3. `{{CURRENT_STATE}}`
4. `{{ONE_ACTIVE_PACKET_OR_OWNER_REVIEW}}`
5. `{{ONE_ADDITIONAL_RECORD_IF_ACTUALLY_REQUIRED}}`

Reason each additional active file is necessary:

`{{RATIONALE_OR_NONE}}`

## Context and token stewardship check

- Exact usage telemetry available: `Yes / No / Unknown`
- Last material-progress action: `{{ACTION_AND_RESULT}}`
- Consecutive unchanged attempts: `{{COUNT}}`
- Repeated content removed from active records: `{{SUMMARY_OR_NONE}}`
- Raw output moved outside active Markdown: `{{REFERENCE_OR_NONE}}`
- Evidence reused instead of rerun: `{{REFERENCE_OR_NONE}}`
- HIGH-effort lane still active: `{{LANE_REASON_AND_STOP_CONDITION_OR_NONE}}`
- Context retained beyond the default route: `{{FILE_AND_REASON_OR_NONE}}`
- Next cleanup trigger: `{{TRIGGER}}`

## Handoff candidate set

List only distilled information eligible for the later handoff. This checkpoint
does not generate or authorize that handoff.

- `{{APPROVED_BLUEPRINT_OR_SECTION}}`
- `{{OWNER_DECISION_OR_CORRECTION}}`
- `{{UNRESOLVED_QUESTION_WITH_OWNER_IMPACT_AND_GATE}}`
- `{{EVIDENCE_REFERENCE_REQUIRED_FOR_A_DECISION}}`

Exclude raw transcripts, duplicate summaries, completed prompt scaffolding,
inactive branches, and unreviewed inference.

## Reference and private archive set

### Reference outside the default route

`{{EVIDENCE_OR_CONTEXT_WITH_POSSIBLE_FUTURE_VALUE}}`

### Archive privately

`{{RAW_QA_COMPLETED_BRANCHES_CLOSED_SIDEQUESTS_SUPERSEDED_CONCLUSIONS}}`

### Retention, privacy, or access condition

`{{WHERE_IT_LIVES_WHO_CAN_ACCESS_AND_WHEN_IT_MAY_BE_REMOVED}}`

Archived information has historical value but no current authority unless an
active owner-approved record explicitly readopts it.

## Redundancy-removal proposal

| Exact target | Why it is redundant | Where necessary value survives | Recovery method | Human decision |
|---|---|---|---|---|
| `{{FILE_SECTION_OR_PLACEHOLDER}}` | `{{REASON}}` | `{{CANONICAL_HOME_OR_HISTORY}}` | `{{VERSION_HISTORY_BACKUP_OR_NONE}}` | Pending |

Do not use a broad directory, unresolved variable, or pattern as a deletion
target. If scope is uncertain, leave the material intact and ask.

## Resumption check — proportionate, with recorded evidence

For a contained sidequest/branch close with no material routing or authority
conflict, inspect the proposed active route against the checklist below yourself.
Record `Coordinator route-only self-review`, the files inspected, result, and
remaining limits. Do not call that an independent or fresh-agent test.

For cycle-level review, pre-handoff acceptance, or a material route/authority
repair, obtain an authorized independent resumption check. If another compatible
agent is unavailable or its use is not authorized, keep that required check
pending and report the blocker; do not substitute self-review as an independent
pass or start another agent without permission.

For an independent check, give the reviewer only the proposed active route.
For either kind of check, establish the following from those routed files,
not from chat memory or the archive:

- [ ] what the human is trying to accomplish;
- [ ] what is currently accepted and how it is known;
- [ ] the active QDI level and phase;
- [ ] the current objective, question, or decision;
- [ ] the next eligible action;
- [ ] what authority exists and what remains prohibited;
- [ ] unresolved risks, contradictions, or unknowns that matter now;
- [ ] the next human gate;
- [ ] where any active sidequest returns.

Failure means the route is missing necessary current context or still depends
on unnecessary historical context. Repair the canonical route rather than
loading the entire archive.

## Checkpoint decision

- Drag or loop detected: `Yes / No`
- Cause: `{{CAUSE_OR_NONE}}`
- Active route reduced: `Yes / No / Not needed`
- Canonical conflicts resolved: `Yes / No / None`
- Handoff candidate set prepared: `Yes / No / Not this checkpoint scope`
- Archive and reference destinations named: `Yes / No`
- Redundant removal authorized: `Yes / No / None proposed`
- Review kind: `Coordinator route-only self-review / Independent resumption check`
- Independent check required: `Yes / No — scope and reason`
- Resumption result and evidence: `Pass / Fail / Pending named review; inspected route and limits`
- Human decision: `Pending`
- Remaining concern: `{{CONCERN_OR_NONE}}`

## Exit condition

The checkpoint closes only when:

1. each reviewed record has one disposition;
2. the active route contains the smallest sufficient current context;
3. canonical truth and successor relationships are clear;
4. archives and references are removed from default routing;
5. no deletion occurred without exact human authority;
6. the handoff candidate set excludes raw and unapproved material;
7. the required resumption check passes; self-review is not labeled independent,
   and a required independent check is not waived;
8. the QDI Record Index has no collision, broken active path, reused ID, or
   missing successor relationship;
9. unchanged retries and unbounded high-effort lanes are stopped or justified;
10. the human accepts the cleanup result.
