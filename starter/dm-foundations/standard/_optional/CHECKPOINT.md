# Checkpoint — `{{CHECKPOINT_NAME}}`

Status: Frozen after acceptance  
Captured: `{{YYYY-MM-DD}}`  
Owner: `{{PERSON_OR_ROLE}}`

## Reason

`{{PAUSE_TRANSFER_RECOVERY_OR_RELIED_UPON_DECISION}}`

## Exact state

- Source identity: `{{COMMIT_ARTIFACT_OR_STATE}}`
- Environment: `{{ENVIRONMENT}}`
- Active route: `{{PATH}}`
- Verified facts: `{{FACTS_AND_EVIDENCE}}`
- Unresolved facts: `{{UNKNOWNS}}`
- Authority at capture: `{{BOUNDARY}}`

## Resumption

1. Revalidate source, environment, and authority.
2. Confirm dependencies and unresolved facts.
3. Resume from `{{NEXT_LEGAL_ACTION}}` only.

Create a successor checkpoint if a relied-upon fact changes. Do not rewrite the
accepted snapshot.
