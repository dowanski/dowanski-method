# QDI Record Index

Status: Conditional reference  
Purpose: Resolve durable QDI records after titles, filenames, or locations
change without assigning administrative IDs to every file

## Use boundary

Do not read this index during ordinary questioning. Read or update it only when:

- creating a durable cross-referenced record;
- following an ID whose current path is unknown;
- moving, closing, archiving, or superseding an indexed record;
- running the Context Cleanup Checkpoint;
- preparing the later QDI-to-DM handoff;
- investigating historical evidence.

Readable relative links remain the primary navigation system. IDs are the stable
identity when a durable reference must survive a move or rename.

## ID eligibility test

Assign an ID only when at least one condition is true:

1. the record must survive a rename or move;
2. more than one active or historical record will reference it;
3. it preserves a consequential decision, sidequest, checkpoint, branch packet,
   or accepted blueprint;
4. it may cross from QDI into the later DM handoff.

Do not assign IDs to ordinary `README.md`, `AGENTS.md`, routers,
`CURRENT_STATE.md`, the Discovery Ledger as a whole, temporary notes, every
question, every evidence item, or placeholder files merely because they exist.

## Project-scoped format

The QDI workspace or repository supplies the project namespace. IDs are unique
within that project.

| Durable record | Format | Example |
|---|---|---|
| QDI cycle | `QDI-C##` | `QDI-C01` |
| Specialist branch packet | `QDI-C##-BR##` | `QDI-C01-BR01` |
| Sidequest | `QDI-C##-SQ##` | `QDI-C01-SQ01` |
| Durable decision | `QDI-C##-D##` | `QDI-C01-D01` |
| Context Cleanup Checkpoint | `QDI-C##-CC##` | `QDI-C01-CC01` |
| Pre-Build Blueprint | `QDI-C##-BP##` | `QDI-C01-BP01` |
| QDI-to-DM Handoff | `QDI-C##-H##` | `QDI-C01-H01` |

Use two digits until the sequence exceeds `99`; then expand without renumbering
earlier records. Never recycle an identifier or insert a replacement into a
historical gap.

## Allocation rules

1. One coordinator agent owns allocation for the active QDI cycle.
2. Read this index before assigning an ID.
3. Confirm the record passes the eligibility test.
4. Use the active Cycle ID from `CURRENT_STATE.md`.
5. Find the highest assigned number for that record type and increment it.
6. Add the index row before other files begin referencing the new ID.
7. Keep the ID unchanged through title, status, or path changes.
8. Never reuse an ID from a removed, abandoned, or archived record.
9. Specialized or parallel agents must request or receive a reserved ID from the
   coordinator; they may not allocate permanent IDs independently.
10. If two records receive the same ID, stop, preserve both artifacts, and ask
    the coordinator to resolve the collision. Do not silently renumber an
    accepted record.

## Status values

- `ACTIVE`
- `IN_REVIEW`
- `ACCEPTED`
- `BLOCKED`
- `DEFERRED`
- `CLOSED`
- `SUPERSEDED`
- `ARCHIVED_PRIVATE`
- `REMOVED_TOMBSTONE`
- `ABANDONED`

Status does not create authority. An `ACCEPTED` discovery record still does not
authorize implementation.

## Record index

| ID | Type | Title | Status | Current relative path | Successor | Return or review note |
|---|---|---|---|---|---|---|
| `QDI-C01` | Project QDI cycle | `{{PROJECT_NAME_OR_INITIAL_DISCOVERY}}` | ACTIVE | `CURRENT_STATE.md` | None | Begins at Anchor 01 |

## Movement and cleanup rules

- `KEEP_ACTIVE` — keep the ID and update the active path if it changed.
- `HANDOFF_CANDIDATE` — keep the ID and mark its accepted handoff eligibility in
  the review note; do not create the handoff here.
- `REFERENCE` — keep the ID and path but remove the record from the default
  router.
- `ARCHIVE_PRIVATE` — keep the ID, change status and path, and remove current
  authority.
- `SUPERSEDED` — keep both IDs and add the successor ID to the prior row.
- `REMOVE_REDUNDANT` — if another record still references the ID, retain a
  `REMOVED_TOMBSTONE` row with the successor or recovery note. If the record was
  never referenced and carries no durable value, human-approved removal does not
  require a new tombstone ID.

An archived or superseded ID never becomes current again by itself. An active
owner-approved record must explicitly readopt the necessary truth.

## Collision and integrity check

At every full Context Cleanup Checkpoint, confirm:

- [ ] every indexed ID is unique;
- [ ] every active indexed path exists;
- [ ] titles and statuses match their current records;
- [ ] moved records retained their IDs;
- [ ] superseded rows name valid successors;
- [ ] archived rows are absent from the default reading route;
- [ ] no removed ID was reused;
- [ ] no ordinary control or temporary file received an unnecessary ID;
- [ ] only the coordinator allocated permanent IDs.
