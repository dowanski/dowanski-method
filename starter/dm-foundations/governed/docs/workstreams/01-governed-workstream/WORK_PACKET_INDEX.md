# Work Packet Index

Status: Current  
Integration owner: `{{PERSON_OR_ROLE}}`

| Packet | Mode | Outcome | Depends on | Writer | Eligible | May inspect while blocked | May update while blocked | Evidence gate | Acceptance |
|---|---|---|---|---|---|---|---|---|---|
| `packets/01-WORK_PACKET.md` | `{{DISCOVERY_OR_IMPLEMENTATION}}` | `{{OUTCOME}}` | `{{DEPENDENCY_OR_NONE}}` | `{{PERSON_OR_AGENT}}` | `{{YES_NO_AND_REASON}}` | `{{NONE_OR_EXACT_READ_ONLY_ACTIONS}}` | `{{NONE_OR_EXACT_DOCUMENTATION_PATHS}}` | `{{GATE}}` | `{{PENDING_OR_RESULT}}` |

## Eligibility rules

A packet is eligible only when:

- its dependency evidence exists;
- source and target identities match current state;
- its writer owns an isolated surface;
- authority is explicit;
- contract questions are resolved;
- required rollback or preservation exists;
- the reviewer and evidence gate are named.

A blocked Discovery packet may inspect named evidence and update only the exact
documentation or evidence-register paths separately named by the index. It may
not mutate application source, target systems, databases, providers, shared
state, or external state. A blocked Implementation packet performs no
implementation.

## Convergence rule

Parallel packets do not merge their own results into shared state unless the
index names that authority. Independent outputs converge through
`{{INTEGRATION_PACKET_OR_OWNER_GATE}}`.

This is not an activity tracker. Update it when eligibility, dependency,
ownership, evidence, or acceptance changes.
