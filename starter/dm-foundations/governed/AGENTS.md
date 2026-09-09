# Agent Instructions

## Purpose

Operate inside `{{PROJECT_NAME}}` through explicit authority, bounded packets,
matched evidence, and human-accountable release gates.

## Required reading

1. `README.md`
2. `docs/README.md`
3. `docs/CURRENT_STATE.md`
4. the active workstream README
5. its `CURRENT_STATE.md` and `CONTRACT.md`
6. its `WORK_PACKET_INDEX.md`
7. the exact eligible or blocked packet named by that index
8. only records explicitly routed by that packet

Do not preload archives, closed packets, optional templates, raw evidence, or
unrelated workstreams.

## Authority

- Project owner: `{{OWNER_OR_ROLE}}`
- Release authority: `{{RELEASE_ROLE}}`
- Independent reviewer: `{{REVIEW_ROLE}}`
- Real permissions and explicit current human decisions outrank documented
  assumptions.
- A child may narrow inherited authority; it may not broaden it.
- Documentation never grants external access.

Without explicit packet authority, do not:

- write to shared or production systems;
- handle, expose, or invent secret values;
- change identity, tenant, billing, or authorization behavior;
- delete, migrate, restore, or clean uncertain data;
- contact outside parties;
- merge, deploy, publish, roll back, or retire a release;
- change another writer’s surface;
- suppress failed or inconclusive evidence.

## Starting-state protection

- Inspect before changing.
- Preserve uncertainty and conflicting evidence.
- Do not “clean up” a repository, database, provider, or branch until its
  recovery value and authority are known.
- Stop if source identity, target environment, ownership, or rollback is
  unclear.

## Execution

- Work only from the exact packet named by `WORK_PACKET_INDEX.md`. An
  implementation packet must be eligible. A discovery packet may inspect and
  preserve evidence while blocked only when the index names that read-only
  authority; it may not mutate the project or external state.
- One writer owns one isolated change surface.
- Follow the shared `CONTRACT.md` and Main Set interfaces.
- Do not combine unrelated external mutations.
- Record durable conclusions, not activity theater.
- Escalate when a discovered dependency or consequence exceeds the packet.

## Evidence and release

- Match every status claim to named evidence.
- Keep verification, human acceptance, integration, release, and live
  verification separate.
- Treat stale or changed starting conditions as a reason to reverify.
- Do not self-approve an independent-review requirement.
- Return project-wide truth and debt upward after review.
- Close the governed route and reduce its weight when the trigger ends.

## Continuing controls

These controls remain active throughout implementation, review, and maintenance:

- Challenge drift, contradictions, unsupported claims, and proposed shortcuts.
  Explain the evidence and consequence, recommend a correction, and seek a
  human decision when authority or direction changes. Update your recommendation
  when better evidence arrives.
- Use one canonical writer per state record. Read only the current route and
  triggered references; reuse valid evidence when its source and claim are unchanged.
- Before expensive work, name its purpose, scope, expected proof, effort, and
  stop condition. Reserve capacity for verification and repairs.
- For every retry, state what materially changed. After two consecutive attempts
  without new evidence or progress, stop before a third unchanged attempt.
  Diagnose, change the approach, or preserve the blocker and return point.
- Report exact usage only from actual telemetry. Distinguish account-wide usage
  from task counters; label forecasts. If telemetry is unavailable, say so.
  Never estimate a usage percentage from words or elapsed time or automatically
  consume paid resets.
- Efficiency never waives required quality, evidence, safety, accessibility,
  authority, independent review, or human acceptance.
- Before pause or handoff, preserve current truth, evidence, authority, blocker,
  next action, and gate in the existing state/packet route.
- At closure or documentation drag, resolve duplicate current truth, remove
  closed work from active routing, and preserve useful history. Keep a resolved
  retry's cause, correction, proof, and prevention rule; archive individual
  attempts when no longer needed. Obtain exact authority before consequential
  deletion. Do not create a second status tracker.

For material changes to accepted purpose, scope, authority, risk, architecture,
or proof, preserve a named return point and begin a linked QDI successor before
the affected implementation continues.
