# Work Packet — `{{OUTCOME_NAME}}`

Status: `{{PROPOSED_READY_ACTIVE_BLOCKED_IN_REVIEW_CLOSED}}`  
Parent: `PROJECT.md`  
Owner or reviewer: `{{PERSON_OR_ROLE}}`

## Outcome

`{{ONE_COHERENT_OBSERVABLE_RESULT}}`

## Starting evidence

- Current state: `{{WHAT_WAS_OBSERVED}}`
- Evidence: `{{PATH_COMMAND_SCREEN_OR_OTHER_SOURCE}}`
- Known uncertainty: `{{UNCERTAINTY_OR_NONE}}`

## Questions required before implementation

1. `{{QUESTION_OR_RESOLVED_ANSWER}}`

Do not begin while an unanswered question would force a material guess.

## Scope

Included:

- `{{ALLOWED_CHANGE_SURFACE}}`

Not included:

- `{{EXPLICITLY_EXCLUDED_WORK}}`

## Authority

Allowed:

- inspect `{{ALLOWED_PATH_OR_SYSTEM}}`;
- change `{{ALLOWED_PATH_OR_SYSTEM}}`;
- run `{{SAFE_LOCAL_CHECKS}}`.

Requires new human authority:

- `{{DEPLOYMENT_EXTERNAL_WRITE_DELETION_CONTACT_OR_OTHER_BOUNDARY}}`.

## Dependencies

- Must be true before work: `{{DEPENDENCY_OR_NONE}}`
- Must remain unchanged: `{{PROTECTED_BEHAVIOR_OR_SURFACE}}`

## Execution

1. `{{FIRST_BOUNDED_ACTION}}`
2. `{{SECOND_BOUNDED_ACTION}}`
3. `{{UPDATE_CURRENT_TRUTH_OR_DECISION_IF_NEEDED}}`

## Verification

| Claim | Required evidence | Source / observer | Environment / date | Result | Limitation |
|---|---|---|---|---|---|
| `{{CLAIM}}` | `{{MATCHED_CHECK}}` | `{{SOURCE_OR_OBSERVER}}` | `{{ENVIRONMENT_AND_DATE}}` | `{{PENDING_PASS_FAIL_INCONCLUSIVE}}` | `{{LIMIT_OR_NONE}}` |

Passing evidence proves only the named claim in the named environment and
starting state. It does not imply owner acceptance, release, or live operation.

## Stop conditions

Stop and return to the owner when:

- the starting state does not match this packet;
- the target or authority is uncertain;
- required work crosses the excluded boundary;
- verification fails in a way that changes the proposed approach;
- unrelated material would need to be overwritten or removed.

## Result and closeout

- Changed: `{{SUMMARY_OR_NOT_YET_IMPLEMENTED}}`
- Verified: `{{SCOPED_EVIDENCE_OR_NOT_YET_VERIFIED}}`
- Not verified: `{{LIMITATION_OR_NONE}}`
- Intentionally unchanged: `{{PROTECTED_SCOPE}}`
- Remaining debt: `{{DEBT_OR_NONE}}`
- Human decision: `{{PENDING_ACCEPTED_REJECTED_NOT_REQUIRED}}`
- Next legal entry: `{{SUCCESSOR_OR_RETURN_TO_PROJECT}}`
- Frozen on acceptance: `{{YES_OR_PENDING}}`
- Return to parent: `{{CURRENT_TRUTH_DECISION_DEBT_AND_NEXT_ENTRY}}`
- Remove from active route: `{{YES_AFTER_REVIEW_OR_PENDING}}`
- Successor: `{{NONE_OR_EXACT_PATH_AFTER_ENTRY_CONDITIONS_ARE_MET}}`
