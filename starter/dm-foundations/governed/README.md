# Dowanski Method — Governed Project Foundation

Status: Starter template
Documentation Weight: Governed

## What this foundation is for

Use Governed for consequential, multi-boundary, difficult-to-reverse, or
recovery-sensitive work.

One hard trigger may be enough:

- identity, authentication, authorization, or tenant isolation;
- billing or financial action;
- customer, regulated, or otherwise sensitive data;
- destructive or difficult-to-reverse mutation;
- production migration or consequential provider change;
- security review, incident response, or source-truth recovery;
- concurrent writers affecting shared state;
- mandatory independent verification, rollback, or audit evidence.

Governed is not a higher quality grade. Use it because ambiguity carries a
material cost, then reduce it when the triggering condition closes.

## Active base

```text
README.md
AGENTS.md
docs/
├── README.md
├── PROJECT_BRIEF.md
├── CURRENT_STATE.md
├── MASTER_PLAN.md
├── ARCHITECTURE.md
├── INTERFACES.md
├── DECISIONS.md
├── NOW_NEXT_DEBT.md
├── RELEASE.md
├── operations/
│   └── README.md
└── workstreams/
    └── 01-governed-workstream/
        ├── README.md
        ├── CURRENT_STATE.md
        ├── CONTRACT.md
        ├── WORK_PACKET_INDEX.md
        ├── packets/
        │   └── 01-WORK_PACKET.md
        └── EVIDENCE_REGISTER.md
```

`_optional/` contains triggered controls; `_examples/` contains fictional
orientation. Neither belongs in the active route.

## Installation

1. Name the hard trigger or combined conditions requiring Governed weight.
2. Preserve the exact starting state before consequential changes.
3. Copy the active base and complete the Main Set.
4. Define real authority, trust boundaries, release behavior, and recovery.
5. Rename the governed workstream and order only its eligible packets.
6. Define evidence and independent review before implementation.
7. Add optional controls only when their triggers exist.
8. Remove unused prompts, fictional examples, and inactive structures.
9. Obtain owner approval of the adapted route and first packet.

Create `OWNER_REVIEW.md` only when an acceptance gate is reached. Create
`CLOSEOUT.md` only after a review disposition exists; both begin as optional
installation resources rather than active future-state records.

## Agent-assisted installation

> Read `README.md`, `AGENTS.md`, and `docs/README.md`. Inspect the repository and
> any authorized external state without changing either. Identify the exact
> Governed trigger, source-of-truth uncertainty, trust and authority boundaries,
> destructive or irreversible actions, required evidence, rollback obligations,
> and independent-review gate. Preserve conflicting or uncertain state. Propose
> the adapted Main Set, one governed workstream, and the smallest first Work
> Packet. Do not mutate, clean, migrate, deploy, or create additional
> workstreams until the owner accepts the starting state and route.

## Active reading path

1. root orientation;
2. `AGENTS.md`;
3. `docs/README.md`;
4. Main Set `CURRENT_STATE.md`;
5. active governed workstream README;
6. local `CURRENT_STATE.md` and `CONTRACT.md`;
7. `WORK_PACKET_INDEX.md`;
8. the exact eligible or blocked packet named by that index;
9. only the evidence, interface, or runbook named by that packet.

Governed does not mean whole-corpus reading.

## Reduction requirement

Every temporary governed program names its exit condition. After acceptance:

1. return durable truth, decisions, and debt to the Main Set;
2. freeze required evidence and release identities;
3. remove temporary freezes and specialist roles;
4. close and remove the workstream from active routing;
5. archive only material with recovery, audit, or provenance value;
6. verify the reduced Standard or Light route.

## Cleanup before work

- [ ] Replace every required `{{FIELD}}`.
- [ ] Verify source, environment, target, owner, and actual permissions.
- [ ] Confirm one canonical home for every active fact.
- [ ] Remove unearned optional files and fictional examples.
- [ ] Define packet ownership and prevent overlapping shared-state writers.
- [ ] Define evidence, acceptance, release, rollback, and stop conditions.
- [ ] Confirm no secret or unnecessary customer information entered Markdown.
- [ ] Confirm the independent reviewer is independent enough for the stated risk.
- [ ] Name the condition that permits weight reduction.
