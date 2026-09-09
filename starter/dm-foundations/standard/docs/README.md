# Documentation Router

Status: `{{ACTIVE_OR_REVIEW}}`  
Purpose: Select the smallest sufficient context for the current task

## Always read

1. `../README.md`
2. `../AGENTS.md`
3. `CURRENT_STATE.md`

## Installation-only route

Use this complete route only while the root foundation status is `Starter
template`:

1. `../README.md`
2. `../AGENTS.md`
3. `PROJECT_BRIEF.md`
4. `CURRENT_STATE.md`
5. `MASTER_PLAN.md`
6. `DECISIONS.md`
7. `NOW_NEXT_DEBT.md`
8. `WORK_PACKET.md`, or the copied workstream README when the split test has
   earned that alternative
9. if a workstream is earned, its Work Packet

After adaptation, delete this installation route and use the non-cumulative
task routes below. An environment may bind `AGENTS.md` before step 1 without
changing the human reading path.

## Lifecycle status glossary

- **Proposed:** route drafted; entry conditions or authority are incomplete.
- **Ready:** all packet entry conditions are satisfied; bounded execution may begin.
- **Active:** authorized execution is underway.
- **Blocked:** a named requirement prevents the next in-scope action.
- **In review:** the claimed result and matched evidence await the named gate.
- **Closed:** review disposition is recorded, truth has returned to the parent,
  and the route has been removed.

Lifecycle status never implies evidence, acceptance, integration, release, or
live-verification status.

## Task routes

| Task | Read next |
|---|---|
| Understand purpose, audience, scope, or success | `PROJECT_BRIEF.md` |
| Continue the active work | Direct route: `WORK_PACKET.md`; earned workstream route: `workstreams/{{ACTIVE_WORKSTREAM}}/README.md`, then its current packet |
| Review dependency order or open a later stage | `MASTER_PLAN.md` |
| Confirm a durable choice | `DECISIONS.md` |
| Determine current focus or material obligation | `NOW_NEXT_DEBT.md` |
| Review architecture, interfaces, evidence, release, or research | Only the exact active record linked by Current State or the workstream packet |
| Investigate history | The superseded record or version-history location linked by the current source |

Routes are not cumulative. Do not read every row for an ordinary task.

## Active execution route

Shape: `{{DIRECT_WORK_PACKET_OR_WORKSTREAM_SET}}`  
Direct packet: `{{WORK_PACKET_PATH_OR_NOT_APPLICABLE}}`  
Active workstream: `{{WORKSTREAM_PATH_OR_NOT_APPLICABLE}}`  
Current packet: `{{PACKET_PATH}}`  
Next owner gate: `{{OWNER_GATE}}`

Exactly one execution shape may be routed. A Workstream Set is not required by
Standard weight alone.

## Authority order

1. Explicit current human instruction
2. Observed repository, provider, or live reality
3. Current Main Set
4. Active workstream contract and packet
5. Historical records

If observed reality conflicts with current documentation, stop implementation,
record the discrepancy, and repair source truth before proceeding.

## Archive boundary

Archived and superseded records are evidence, not active authority. Do not add
an archive route until material earns preservation beyond ordinary version
history.
