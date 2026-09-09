# Documentation Router

Status: `{{ACTIVE_REVIEW_OR_RECOVERY}}`  
Purpose: Route each task through current truth, explicit authority, and the
smallest sufficient governed context

## Always read

1. `../README.md`
2. `../AGENTS.md`
3. `CURRENT_STATE.md`

## Task routes

| Task | Read next |
|---|---|
| Understand project purpose or global authority | `PROJECT_BRIEF.md`, then linked decisions |
| Continue governed work | `workstreams/{{ACTIVE_WORKSTREAM}}/README.md` |
| Inspect system structure or trust seams | `ARCHITECTURE.md` |
| Inspect an input, output, handoff, or service boundary | `INTERFACES.md` |
| Determine packet eligibility | Active workstream `WORK_PACKET_INDEX.md` |
| Execute or safely investigate one packet | Active workstream `CONTRACT.md`, `WORK_PACKET_INDEX.md`, then the exact eligible or blocked packet named by that index |
| Verify a claim | Active workstream `EVIDENCE_REGISTER.md`, then the named evidence source |
| Prepare integration, release, rollback, or live verification | `RELEASE.md` and the exact routed runbook |
| Investigate an incident, migration, recovery, or security condition | Only the triggered record linked by the active workstream |
| Investigate history | The exact frozen checkpoint, closeout, or archive source linked by current truth |

Routes are not cumulative. Read only the branch required for the assigned task.

## Active governed workstream

`workstreams/{{ACTIVE_WORKSTREAM}}/`

- Current packet: `{{PACKET_PATH}}`
- Active writer: `{{PERSON_OR_AGENT}}`
- Independent reviewer: `{{PERSON_OR_ROLE}}`
- Next owner gate: `{{GATE}}`
- Weight-reduction condition: `{{CONDITION}}`

## Authority order

1. Explicit current owner instruction and real system permission
2. Observed repository, provider, database, and live reality
3. Accepted Main Set
4. Active workstream contract, packet index, and the exact eligible or blocked packet named by that index
5. Frozen evidence and historical records

If current documents and reality disagree, ordinary implementation stops and a
source-truth or recovery decision begins.

## Archive and evidence boundary

Archived records are read-only history. Evidence artifacts support named claims
but do not become global truth automatically. Raw evidence follows its own
privacy, retention, and access rules.
