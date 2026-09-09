# Complete Starter Installation and Storage

Status: Conditional setup guidance  
Read when: storage, access, sharing, or the destination is unresolved or changing

## Choose the working home

The agent needs filesystem access to the selected folder to maintain and resume
the Markdown system. A path identifies a location; permission must still cover
the intended action.

| Mode | Fits best | Main tradeoff |
|---|---|---|
| Standalone local | A new idea or private exploration before a repository exists | Backup and versioning need separate setup |
| Repository-contained | A feature, audit, repair, or migration in a known controlled project | Raw discovery may enter shared or public history |
| Hybrid — recommended | Private discovery followed by accepted project documentation | Transfer only approved, sanitized conclusions |

For most new projects, use hybrid: keep working QDI in a private folder, approve
the Pre-Build Blueprint, authorize the handoff, then adapt one DM foundation in
the approved project location. Rejected ideas, personal context, and raw research
usually do not belong in permanent project history.

## Standalone or hybrid setup

1. Create a clearly named folder such as `Project Name — QDI Discovery`.
2. Copy the complete starter into it with its internal structure intact.
3. Open that folder in Cursor, Codex, or another compatible agent environment.
4. Use the start instruction in [README.md](README.md).
5. If a repository will supply evidence, identify its exact location and the
   permitted read-only scope. QDI-folder access does not authorize repository
   inspection or modification.
6. Select a private backup or versioning approach. Local storage is not an
   automatic backup.

For hybrid use, the future repository destination can remain undecided during
discovery. Resolve it before an approved DM setup.

## Repository-contained setup

1. Put the complete packet under a contained path, such as
   `docs/qdi-discovery/`.
2. Preserve existing root instructions and routers. Read them first and resolve
   conflicting scope or authority before activating QDI.
3. Give this path-specific instruction:

   > Read `docs/qdi-discovery/README.md` and
   > `docs/qdi-discovery/AGENTS.md` completely, then begin the Dowanski QDI
   > Discovery Protocol. Do not read `docs/qdi-discovery/dm-foundations/` and
   > do not implement the project.

4. Review QDI records before staging, committing, pushing, sharing, or attaching
   them to an issue or pull request.
5. After an accepted handoff, adapt only the chosen foundation at the separately
   approved destination. Never overwrite the project's governing files or copy
   all three weights into its active documentation.

A private team may retain all discovery in its repository when access,
retention, and review policies support it. Confirm who can read it, what is
prohibited from history, how unfinished conclusions are reviewed, and whether
retention obligations can be met. Public repositories should not receive an
unreviewed Discovery Ledger.

## Privacy and authority

Never record credentials, tokens, keys, recovery codes, or other secret values.
Minimize personal, customer, employee, health, financial, and confidential
details. Prefer roles, synthetic examples, redaction, or protected references
when exact identities are unnecessary.

Local, committed, pushed, published, and live are separate states. Permission
for one does not imply the next. Review before sharing and preserve only
history needed for decisions, proof, accountability, and resumption.

The bundled foundations remain inactive until the accepted handoff names a
weight, exact destination, and allowed documentation paths.

## Record the decision and return

In [Current State](qdi/CURRENT_STATE.md), record storage mode, packet location,
related repository, permitted access, commit/push authority, privacy/retention
constraints, and backup expectations. Keep the accepted setup decision in the
Ledger with a reference to Current State for the live values.

Return to the [QDI router](qdi/README.md) and its current phase. An unresolved
repository boundary permits local conversation, but blocks repository
inspection, mutation, commit, push, or publication.
