# Agent Instructions

## Purpose

Work inside `{{PROJECT_NAME}}` through the active documentation route and one
bounded Work Packet at a time.

## Required reading

This file may be loaded automatically by an agent environment. Before acting,
begin the canonical route at the root `README.md`.

1. `README.md`
2. `docs/README.md`
3. `docs/CURRENT_STATE.md`
4. the direct `docs/WORK_PACKET.md` named by the router, or the earned active
   workstream README named by the router
5. if a workstream is earned, its current `WORK_PACKET.md`
6. only additional records explicitly routed by the active packet

Do not preload the complete Main Set, inactive workstreams, `_examples/`,
`_optional/`, or history.

## Authority

- The project owner is `{{OWNER_OR_ROLE}}`.
- Human instructions, real system permissions, and observed state outrank
  documentation assumptions.
- Child workstreams inherit parent rules and may narrow them; they may not
  silently broaden authority.
- Do not publish, deploy, contact outside parties, mutate providers, expose
  secrets, delete consequential data, or change another workstream without
  explicit authority.
- Stop on an unresolved target, permission, starting-state, trust-boundary, or
  destructive-action question.

## Work discipline

- Preserve unrelated work and inspect before editing.
- Keep one coherent outcome per packet.
- Avoid unrelated cleanup and speculative architecture.
- Update the one canonical current source rather than copying facts.
- Record only durable decisions, material debt, and matched evidence.
- Use version history and tool artifacts for routine activity.
- Prefer a direct Main Set Work Packet for one coherent outcome. Create a child
  workstream only when its independent coordination boundary is approved.

## Verification and reporting

- Define or confirm evidence before implementation.
- Verify only the scope claimed.
- Distinguish implementation, verification, acceptance, integration, release,
  and live verification.
- Report limitations and intentionally unchanged surfaces.
- Return project-wide truth, decisions, and surviving debt to the Main Set.
- Close and remove completed routes only after their review gate passes.

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
