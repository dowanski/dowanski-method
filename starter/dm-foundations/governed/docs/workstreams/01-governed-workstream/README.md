# Governed Workstream — `{{WORKSTREAM_NAME}}`

Status: `{{PROPOSED_READY_ACTIVE_BLOCKED_IN_REVIEW_CLOSED}}`  
Parent: `../../CURRENT_STATE.md`  
Owner: `{{PERSON_OR_ROLE}}`

## Outcome and trigger

- Outcome: `{{INDEPENDENTLY_ACCEPTED_RESULT}}`
- Governed trigger: `{{RISK_AUTHORITY_RECOVERY_OR_RELEASE_BOUNDARY}}`
- Consequence: `{{WHAT_FAILURE_COULD_HARM}}`
- Reduction condition: `{{WHAT_MUST_CLOSE_OR_STABILIZE}}`

## Parent authority

- Inherited: `{{PROJECT_AUTHORITY}}`
- Narrowed locally: `{{LOCAL_BOUNDARY}}`
- Explicitly prohibited: `{{ACTIONS_OR_SURFACES}}`
- New owner decision required for: `{{BOUNDARY}}`

## Local route

1. this README;
2. `CURRENT_STATE.md`;
3. `CONTRACT.md`;
4. `WORK_PACKET_INDEX.md`;
5. the exact eligible or blocked packet named by that index;
6. `EVIDENCE_REGISTER.md` and only records named by the packet;
7. instantiate `OWNER_REVIEW.md` from `_optional/` only at the acceptance gate;
8. instantiate `CLOSEOUT.md` from `_optional/` only after the decision.

## Ownership and concurrency

| Surface | Writer | Reviewer | Integration owner | Other writers prohibited |
|---|---|---|---|---|
| `{{SURFACE}}` | `{{PERSON_OR_AGENT}}` | `{{ROLE}}` | `{{ROLE}}` | `{{YES_OR_BOUNDARY}}` |

## Dependencies

- Begins after: `{{VERIFIED_DEPENDENCY}}`
- Blocks: `{{DOWNSTREAM_WORK_OR_NONE}}`
- External/shared state: `{{SYSTEM_AND_AUTHORITY_OR_NONE}}`

## Exit gate

- Required evidence: `{{EVIDENCE_SUMMARY}}`
- Independent review: `{{ROLE_AND_SCOPE}}`
- Owner decision: `{{EXACT_ACCEPTANCE_BOUNDARY}}`
- Release authorization: `{{SEPARATE_GATE_OR_NOT_APPLICABLE}}`

## Upward return

On closure, return current truth, durable decisions, surviving debt, evidence
identity, release posture, and the next legal entry to the Main Set.
