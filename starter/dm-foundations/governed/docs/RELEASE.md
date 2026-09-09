# Release Control

Status: `{{NOT_AUTHORIZED_NOT_APPLICABLE_PROPOSED_PRESERVED_INTEGRATION_REVIEW_RELEASED_LIVE_VERIFIED}}`  
Release owner: `{{PERSON_OR_ROLE}}`

## Release boundary

- Included changes: `{{EXACT_SCOPE}}`
- Excluded changes: `{{NON_GOALS}}`
- Source identity: `{{COMMIT_ARTIFACT_OR_DIGEST}}`
- Target environment: `{{ENVIRONMENT}}`
- Provider or system authority: `{{ACTUAL_PERMISSION_SOURCE}}`

## Entry gates

| Gate | Required evidence | Owner | Result |
|---|---|---|---|
| Source identity | `{{PROOF}}` | `{{ROLE}}` | `{{NOT_EVALUATED_PENDING_PASS_FAIL_INCONCLUSIVE_STALE}}` |
| Contract and tests | `{{PROOF}}` | `{{ROLE}}` | `{{NOT_EVALUATED_PENDING_PASS_FAIL_INCONCLUSIVE_STALE}}` |
| Independent review | `{{PROOF}}` | `{{ROLE}}` | `{{NOT_EVALUATED_PENDING_PASS_FAIL_INCONCLUSIVE_STALE}}` |
| Owner acceptance | `{{PROOF}}` | `{{ROLE}}` | `{{PENDING_ACCEPTED_REJECTED}}` |
| Rollback readiness | `{{PROOF}}` | `{{ROLE}}` | `{{NOT_EVALUATED_PENDING_PASS_FAIL_INCONCLUSIVE_STALE_NOT_APPLICABLE}}` |

## Integration and release actions

Each action requires separately verified authority:

1. `{{INTEGRATE_OR_PRESERVE}}`
2. `{{MIGRATE_OR_CONFIGURE_IF_APPLICABLE}}`
3. `{{DEPLOY_OR_DISTRIBUTE}}`
4. `{{LIVE_VERIFY}}`

## Rollback

- Trigger: `{{FAILURE_SIGNAL_OR_OWNER_DECISION}}`
- Safe target: `{{KNOWN_GOOD_IDENTITY}}`
- State/data handling: `{{RECOVERY_BOUNDARY}}`
- Authority: `{{ROLE}}`
- Verification: `{{CHECKS}}`

## Final release record

- Integrated: `{{NO_OR_IDENTITY_AND_DATE}}`
- Released: `{{NO_OR_IDENTITY_AND_DATE}}`
- Live verified: `{{NO_OR_SCOPE_DATE_AND_EVIDENCE}}`
- Limitations: `{{LIMIT_OR_NONE}}`
- Monitoring or support handoff: `{{OWNER_OR_NONE}}`
