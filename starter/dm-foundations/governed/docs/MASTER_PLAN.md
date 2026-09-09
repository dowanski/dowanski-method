# Master Plan

Status: `{{PROPOSED_OR_ACCEPTED}}`

## Destination

`{{PROJECT_END_STATE_FOR_CURRENT_SCOPE}}`

## Dependency-ordered stages

### `{{NN}}` — `{{STAGE_NAME}}`

- Entry evidence: `{{WHAT_MUST_BE_VERIFIED}}`
- Authority required: `{{ROLE_OR_PERMISSION}}`
- Outcome: `{{RESULT}}`
- Exit evidence: `{{PROOF}}`
- Acceptance: `{{OWNER_OR_REVIEWER}}`
- Release effect: `{{NONE_OR_BOUNDARY}}`
- Status: `{{PROPOSED_READY_ACTIVE_BLOCKED_IN_REVIEW_CLOSED}}`

## Deferred or prohibited lanes

- Deferred: `{{WORK_AND_ACTIVATION_TRIGGER}}`
- Prohibited in current authority: `{{ACTION_OR_SURFACE}}`

## Concurrency and integration

- Safely independent work: `{{PACKETS_OR_NONE}}`
- Shared-state owner: `{{ROLE}}`
- Convergence gate: `{{GATE}}`

## Scope-change rule

Stop affected execution, preserve state, record the proposed change, obtain the
required decision, update current truth and contracts, then re-establish packet
eligibility before resuming.

Do not pre-create inactive stage folders.

