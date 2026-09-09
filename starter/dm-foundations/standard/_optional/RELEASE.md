# Release

Status: `{{PROPOSED_PRESERVED_INTEGRATED_RELEASED_LIVE_VERIFIED}}`  
Release owner: `{{PERSON_OR_ROLE}}`

## Exact boundary

- Included artifact or changes: `{{BOUNDARY}}`
- Excluded: `{{NON_GOAL}}`
- Source identity: `{{COMMIT_OR_ARTIFACT}}`
- Destination: `{{ENVIRONMENT_OR_NOT_YET_AUTHORIZED}}`

## Gates

| Gate | Required evidence | Owner | Result |
|---|---|---|---|
| Integration | `{{CHECK}}` | `{{ROLE}}` | `{{PENDING_PASS_FAIL}}` |
| Release | `{{CHECK}}` | `{{ROLE}}` | `{{PENDING_PASS_FAIL}}` |
| Live verification | `{{CHECK}}` | `{{ROLE}}` | `{{PENDING_PASS_FAIL}}` |

## Rollback or removal

- Trigger: `{{FAILURE_OR_DECISION}}`
- Safe target: `{{KNOWN_STATE}}`
- Authority: `{{ROLE}}`
- Verification after rollback: `{{CHECK}}`

## Result

`{{NOT_RELEASED_OR_SCOPED_RESULT_WITH_DATE_AND_EVIDENCE}}`

