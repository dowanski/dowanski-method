# Checkpoint — `{{CHECKPOINT_NAME}}`

Status: Frozen after acceptance  
Captured: `{{YYYY-MM-DD}}`

## Why this checkpoint exists

`{{PAUSE_TRANSFER_RECOVERY_OR_REVIEW_REASON}}`

## Exact starting state

- Source identity: `{{COMMIT_ARTIFACT_OR_STATE}}`
- Environment: `{{LOCAL_PREVIEW_OR_OTHER}}`
- Active packet: `{{PATH}}`
- Verified facts: `{{FACTS_AND_EVIDENCE}}`
- Unresolved facts: `{{UNKNOWNS}}`

## Safe resumption

1. Revalidate the source identity and environment.
2. Confirm authority has not changed.
3. Recheck unresolved facts.
4. Resume only from `{{NEXT_LEGAL_ACTION}}`.

If a relied-upon fact changes, create a successor checkpoint. Do not silently
rewrite this record.

