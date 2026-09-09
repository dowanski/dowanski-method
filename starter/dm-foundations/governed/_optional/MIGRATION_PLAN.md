# Migration Plan — `{{MIGRATION_NAME}}`

Status: `{{PROPOSED_REHEARSED_AUTHORIZED_RUN_VERIFIED_ROLLED_BACK}}`  
Migration owner: `{{PERSON_OR_ROLE}}`

## Boundary

- Source state: `{{IDENTITY}}`
- Target state: `{{IDENTITY_OR_DESCRIPTION}}`
- Data or provider affected: `{{BOUNDARY}}`
- Excluded: `{{NON_GOAL}}`

## Preconditions

- Backup or recovery point: `{{IDENTITY}}`
- Rehearsal: `{{EVIDENCE}}`
- Compatibility: `{{EVIDENCE}}`
- Authority: `{{PERMISSION_AND_PERSON}}`

## Sequence

| Step | Action | Expected result | Stop condition | Evidence |
|---|---|---|---|---|
| `{{NN}}` | `{{ACTION}}` | `{{RESULT}}` | `{{STOP}}` | `{{PROOF}}` |

## Post-migration verification

- Data integrity: `{{CHECK}}`
- Application behavior: `{{CHECK}}`
- Negative path: `{{CHECK}}`
- Monitoring period: `{{WINDOW_OR_NONE}}`

## Rollback

Use `ROLLBACK_PLAN.md` or state the complete safe reversal here when small.

