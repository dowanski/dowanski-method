# Work Packet 01 — `{{PACKET_NAME}}`

Status: `{{PROPOSED_READY_ACTIVE_BLOCKED_IN_REVIEW_CLOSED}}`  
Mode: `{{DISCOVERY_OR_IMPLEMENTATION}}`  
Parent: `../README.md`  
Contract: `../CONTRACT.md`  
Writer: `{{PERSON_OR_AGENT}}`  
Reviewer: `{{PERSON_OR_ROLE}}`

## Outcome

`{{ONE_BOUNDED_INDEPENDENTLY_REVIEWABLE_RESULT}}`

## Starting evidence

- Source identity: `{{COMMIT_ARTIFACT_SCHEMA_OR_STATE}}`
- Target identity: `{{ENVIRONMENT_SYSTEM_OR_NONE}}`
- Observed behavior — evidence / environment / last verified: `{{OBSERVATION_OR_NOT_YET_OBSERVED}}`
- Owner-stated requirement or invariant — owner record / date: `{{REQUIREMENT_OR_NONE}}`
- Required evidence preservation: `{{IDENTITY_LOCATION_OR_NONE}}`
- Required rollback or recovery for allowed mutations: `{{PLAN_OR_NOT_APPLICABLE_NO_MUTATION_AUTHORIZED}}`
- Known uncertainty: `{{QUESTION_OR_NONE}}`

Never restate an owner requirement as observed current behavior.

## Questions and decisions

| Question | Impact | Owner | Required before |
|---|---|---|---|
| `{{QUESTION_OR_NONE}}` | `{{IMPACT}}` | `{{ROLE}}` | `{{IMPLEMENTATION_INTEGRATION_OR_RELEASE}}` |

## Scope and non-goals

Allowed change surface:

- `{{EXACT_PATH_COMPONENT_SCHEMA_OR_SYSTEM}}`

Not included:

- `{{EXPLICIT_NON_GOAL}}`

Protected:

- `{{CUSTOMER_EXISTING_VERSION_OTHER_WORKSTREAM_OR_SHARED_STATE}}`

## Authority

- May inspect: `{{BOUNDARY}}`
- May change: `{{BOUNDARY}}`
- May run: `{{TESTS_TOOLS_OR_LOCAL_OPERATIONS}}`
- Must not: `{{EXTERNAL_DESTRUCTIVE_RELEASE_OR_OTHER_ACTION}}`
- New authority required for: `{{BOUNDARY}}`
- May inspect while blocked: `{{NONE_OR_EXACT_READ_ONLY_DISCOVERY_ACTIONS}}`
- May update while blocked: `{{NONE_OR_EXACT_DOCUMENTATION_OR_EVIDENCE_PATHS}}`

Blocked Discovery may update only named documentation and evidence records. It
must not mutate application source, target systems, databases, providers,
shared state, or external state.

## Dependencies and invariants

- Entry evidence: `{{PROOF}}`
- Contract invariant: `{{INVARIANT}}`
- Shared-state ownership: `{{ROLE_OR_NONE}}`
- Downstream consumer: `{{PACKET_SYSTEM_OR_NONE}}`

## Execution

1. `{{BOUNDED_ACTION}}`
2. `{{BOUNDED_ACTION}}`
3. `{{NEGATIVE_OR_FAILURE_PATH_WORK}}`
4. `{{DOCUMENTATION_AND_EVIDENCE_RETURN}}`

## Verification contract

| Claim | Required proof | Environment | Result | Limitation | Reviewer |
|---|---|---|---|---|---|
| `{{CLAIM}}` | `{{MATCHED_TEST_INSPECTION_OR_RECEIPT}}` | `{{ENVIRONMENT}}` | `{{NOT_EVALUATED_PENDING_PASS_FAIL_INCONCLUSIVE_STALE}}` | `{{LIMIT_OR_NONE}}` | `{{ROLE}}` |

Required negative cases:

- `{{DENIED_DUPLICATE_CONFLICTING_CROSS_BOUNDARY_OR_UNSUPPORTED_CASE}}`

## Stop conditions

Stop when:

- source, target, ownership, authority, or rollback is uncertain;
- starting evidence becomes stale;
- contract and observed behavior disagree;
- work crosses the packet or trust boundary;
- a negative path cannot fail safely;
- another writer affects the same shared surface;
- evidence becomes inconclusive;
- cleanup could destroy useful recovery state.

## Result and closeout

- Implemented: `{{NO_OR_SCOPED_SUMMARY}}`
- Evidence posture: `{{NOT_EVALUATED_PARTIAL_VERIFIED_FAILED_INCONCLUSIVE_STALE}}`
- Independent review: `{{PENDING_PASS_FAIL_NOT_REQUIRED}}`
- Owner acceptance: `{{PENDING_ACCEPTED_CONDITIONAL_REJECTED}}`
- Integration/release: `{{NOT_AUTHORIZED_OR_EXACT_POSTURE}}`
- Intentionally unchanged: `{{PROTECTED_SCOPE}}`
- Remaining risk or debt: `{{NONE_OR_ITEM}}`
- Return to parent: `{{FACT_DECISION_EVIDENCE_AND_NEXT_ENTRY}}`
