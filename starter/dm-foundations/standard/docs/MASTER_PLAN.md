# Master Plan

Status: `{{PROPOSED_OR_ACCEPTED}}`

## Destination

`{{PROJECT_END_STATE_FOR_CURRENT_SCOPE}}`

## Dependency-ordered stages

### 01 — `{{STAGE_NAME}}`

- Entry: `{{WHAT_MUST_BE_TRUE_BEFORE_START}}`
- Outcome: `{{WHAT_THIS_STAGE_PRODUCES}}`
- Exit: `{{EVIDENCE_AND_DECISION_REQUIRED}}`
- Status: `{{PROPOSED_READY_ACTIVE_BLOCKED_IN_REVIEW_CLOSED}}`

### 02 — `{{STAGE_NAME}}`

- Entry: `{{DEPENDENCY}}`
- Outcome: `{{OUTCOME}}`
- Exit: `{{GATE}}`
- Status: `{{PROPOSED_OR_OTHER}}`

## Deferred work

- `{{VALUABLE_BUT_NOT_AUTHORIZED_WORK_AND_TRIGGER}}`

## Workstream creation rule

Create a workstream folder only when the stage becomes authorized and has an
independent coordination boundary. Do not pre-create empty future structures.

## Scope-change rule

If discovery changes the destination, order, authority, or release boundary:

1. stop affected implementation;
2. record the proposed change and reason;
3. update `DECISIONS.md` after owner acceptance;
4. update this plan and affected current routes;
5. resume only from the newly accepted entry point.

