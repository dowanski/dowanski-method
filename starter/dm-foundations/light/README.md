# Dowanski Method — Light Project Foundation

Status: Starter template
Documentation Weight: Light

## What this foundation is for

Use Light for one focused, reversible, low-consequence outcome with one primary
owner, limited dependencies, and evidence that can be gathered locally.

Common fits include a small site, contained visual repair, editorial article,
local prototype, small internal utility, or read-only investigation.

Do not use Light to avoid documenting consequential identity, billing,
security, customer-data, production-migration, destructive-action, or recovery
risk. Evaluate Standard or Governed when those conditions exist.

## What is included

```text
README.md
AGENTS.md
docs/
├── README.md
├── PROJECT.md
└── WORK_PACKET.md
_examples/
└── EXAMPLE_WORK_PACKET.md
_optional/
├── README.md
├── CHECKPOINT.md
├── DESIGN_REVIEW.md
├── RELEASE_NOTE.md
└── SOURCES.md
```

Only the root files and `docs/` are active. `_examples/` and `_optional/` are
installation resources and must not appear in the active route.

## Human installation

1. Confirm every Light eligibility condition still holds.
2. Copy the active base into the project.
3. Complete `docs/PROJECT.md` with the real purpose, current state, boundaries,
   and decisions.
4. Complete one `docs/WORK_PACKET.md` for the first outcome.
5. Remove unused instructions, examples, and optional files.
6. Review `AGENTS.md` and narrow any rule that does not fit the repository.
7. Confirm the route in `docs/README.md` before implementation begins.

## Agent-assisted installation

Give the agent this instruction:

> Read `README.md`, `AGENTS.md`, and `docs/README.md`. Inspect the repository
> without changing files. Compare the project with the Light eligibility rules.
> Identify missing owner answers, inaccurate starter assumptions, and any risk
> that requires Standard or Governed weight. Propose the adapted `PROJECT.md`,
> documentation route, and first Work Packet for human review. Do not implement
> work or create additional structures until that review is accepted.

## Active reading path

1. `README.md`
2. `AGENTS.md`
3. `docs/README.md`
4. `docs/PROJECT.md`
5. `docs/WORK_PACKET.md`

## Promotion signals

Reassess for Standard when:

- a second dependent outcome appears;
- the combined Project record becomes difficult to maintain;
- work spans several sessions or contributors;
- a separate architecture, evidence, or release responsibility is needed;
- an independently coordinated workstream emerges;
- shared or external state becomes consequential.

Move directly to Governed when a hard trust, security, destructive-data,
recovery, or release trigger appears.

## Cleanup before work

- [ ] Replace every required `{{FIELD}}`.
- [ ] Convert unresolved facts into named questions rather than guesses.
- [ ] Remove fictional examples from the active project.
- [ ] Delete unused `_optional/` files from the installed copy.
- [ ] Confirm one active packet and one intended outcome.
- [ ] Confirm that documentation describes—but does not invent—real authority.
- [ ] Confirm the owner and review gate.
- [ ] Verify that no secret or private value entered the Markdown.

