# Workstream Contract — `{{CONTRACT_NAME}}`

Status: `{{PROPOSED_ACCEPTED_OR_SUPERSEDED}}`  
Version: `{{VERSION_OR_DATE}}`  
Authority: `{{OWNER_OR_ROLE}}`

## Contract boundary

`{{WHAT_ALL_PACKETS_MUST_PRESERVE}}`

## Actors and authority

| Actor | May | Must not | Approval required from |
|---|---|---|---|
| `{{ACTOR}}` | `{{ALLOWED_ACTION}}` | `{{PROHIBITED_ACTION}}` | `{{ROLE}}` |

## Inputs and outputs

| Operation | Accepted input | Validation | Output or receipt | Denied behavior |
|---|---|---|---|---|
| `{{OPERATION}}` | `{{INPUT}}` | `{{CHECK}}` | `{{OUTPUT}}` | `{{SAFE_FAILURE}}` |

## Invariants

- `{{SECURITY_DATA_BEHAVIOR_OR_COMPATIBILITY_INVARIANT}}`

## Failure, retry, and recovery

- Retryable: `{{CONDITION_AND_LIMIT}}`
- Non-retryable: `{{CONDITION}}`
- Escalation: `{{ROLE_OR_ROUTE}}`
- Recovery: `{{SAFE_RESPONSE}}`

## Verification

- Positive path: `{{TEST_OR_EVIDENCE}}`
- Denied path: `{{TEST_OR_EVIDENCE}}`
- Boundary or tenant path: `{{TEST_OR_NOT_APPLICABLE}}`
- Changed-state path: `{{TEST_OR_EVIDENCE}}`

## Change control

Changing this contract requires owner acceptance, affected-packet review, and a
new version. Do not silently reinterpret the contract inside one packet.

