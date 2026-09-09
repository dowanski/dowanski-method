# Dowanski Method — Standard Project Foundation

Status: Starter template
Documentation Weight: Standard

## What this foundation is for

Use Standard for a real project expected to grow across several stages,
sessions, decisions, or contributors. It is the recommended default when Light
would compress changing responsibilities into one oversized record but the work
does not require continuous high-control governance.

Common fits include product and portfolio sites, design-to-implementation work,
growing applications, bounded client workflows, and coordinated human-and-agent
development.

## What is included

```text
README.md
AGENTS.md
docs/
├── README.md
├── PROJECT_BRIEF.md
├── CURRENT_STATE.md
├── MASTER_PLAN.md
├── DECISIONS.md
├── NOW_NEXT_DEBT.md
└── WORK_PACKET.md           # direct first packet; default unless a split is earned
_examples/
└── EXAMPLE_WORKSTREAM.md
_optional/
├── WORKSTREAM_SET/          # copy only when the split test passes
│   ├── README.md
│   └── WORK_PACKET.md
├── README.md
├── ARCHITECTURE.md
├── INTERFACES.md
├── RELEASE.md
├── SOURCES.md
├── DESIGN_REVIEW.md
├── EVIDENCE_REGISTER.md
├── OWNER_REVIEW.md
├── CLOSEOUT.md
├── RUNBOOK.md
└── CHECKPOINT.md
```

Only root files and `docs/` are active. `_examples/` and `_optional/` support
installation and are never part of the default reading path.

## Installation

1. Confirm Standard is sufficient and no Governed hard trigger is present.
2. Copy the active base.
3. Complete the Main Set in the order routed by `docs/README.md`.
4. Use the direct `docs/WORK_PACKET.md` when one packet can carry the first
   outcome without an independent coordination boundary.
5. Only when the approved split test is satisfied, remove the direct packet,
   copy `_optional/WORKSTREAM_SET/` to `docs/workstreams/01-<approved-slug>/`,
   and replace the displayed and literal router paths with that exact name.
6. Complete exactly one first Work Packet in the selected route.
7. Add optional records only when the responsibility has a real trigger.
8. Remove unused prompts and installation resources.
9. Ask the owner to approve the adapted route before implementation.

## Agent-assisted installation

> Read `README.md`, `AGENTS.md`, and `docs/README.md`. Inspect the repository
> without changing files. Identify current truth, existing valid documentation,
> conflicts, authority boundaries, and Governed triggers. Propose the smallest
> adapted Main Set and one Work Packet. Use the direct packet route unless an
> independent workstream is earned; if it is earned, name the exact split
> trigger. Explain every optional record you recommend. Do not delete existing
> records, create future workstreams, or implement changes until the owner
> accepts the route.

## Active reading path

1. root `README.md`;
2. `AGENTS.md`;
3. `docs/README.md`;
4. `docs/CURRENT_STATE.md`;
5. either the direct active Work Packet or one earned active workstream README;
6. if a workstream is earned, its one active Work Packet;
7. only the task-specific record named by that packet.

## Weight changes

Promote to Governed when identity, authorization, billing, sensitive data,
destructive mutation, uncertain source truth, incident recovery, difficult
rollback, or mandatory independent verification enters scope.

Reduce to Light only when one reversible outcome remains and the separated Main
Set can be recombined without creating ambiguity.

## Cleanup before work

- [ ] Replace every required `{{FIELD}}`.
- [ ] Preserve existing valid documentation and unrelated changes.
- [ ] Remove unearned optional records and fictional examples.
- [ ] Confirm one Main Set router and exactly one first execution route: direct
      packet or earned workstream, never both.
- [ ] Confirm each active fact has one canonical home.
- [ ] Name actual authority, stop conditions, evidence, and owner gates.
- [ ] Confirm no secrets or unnecessary personal/customer data entered Markdown.
- [ ] Confirm no future workstream folder exists merely because it appears in a plan.
- [ ] If a workstream is earned, confirm the displayed path matches the literal
      router path.
