# Test Matrix — `{{SCOPE}}`

Status: `{{PROPOSED_ACTIVE_VERIFIED_FAILED_INCONCLUSIVE}}`  
Source identity: `{{COMMIT_OR_ARTIFACT}}`

| Actor/state | Accepted path | Denied path | Duplicate/conflict | Recovery/change | Environment | Result |
|---|---|---|---|---|---|---|
| `{{ACTOR_OR_STATE}}` | `{{CASE}}` | `{{CASE}}` | `{{CASE}}` | `{{CASE}}` | `{{ENVIRONMENT}}` | `{{PENDING_PASS_FAIL}}` |

## Required coverage

- happy path does what the contract allows;
- unauthorized or wrong-boundary paths fail safely;
- duplicate and conflicting operations are deterministic;
- unsupported or malformed inputs do not broaden behavior;
- changed dependencies or stale state trigger the intended response;
- recovery or rollback produces the named safe state.

## Limitation

`{{WHAT_THIS_MATRIX_DOES_NOT_TEST}}`

