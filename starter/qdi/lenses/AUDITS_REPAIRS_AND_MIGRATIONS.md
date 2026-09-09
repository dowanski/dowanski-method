# Domain Lens — Audits, Repairs, and Migrations

Status: Conditional  
Use for: Inspection, diagnosis, debugging, cleanup, correction, recovery,
upgrade, transfer, modernization, and controlled change to an existing system

## Activate when

- an existing product, repository, process, dataset, design, or environment is
  being evaluated or changed;
- current truth, failure cause, intended target, preservation, or rollback must
  be established before action;
- the request may begin as an audit and later become a repair or migration.

## Classify the engagement

- **Audit** — inspect and report. It does not authorize correction.
- **Repair** — correct an identified defect within an approved boundary.
- **Migration** — move or transform state while preserving required meaning,
  access, history, and recovery.

Do not infer repair authority from an audit request or production-release
authority from a successful local migration rehearsal.

## Minimum coverage

1. **Exact target** — Which system, version, environment, path, dataset, flow,
   or artifact is in scope?
2. **Requested outcome** — Is the work diagnostic, corrective, restorative,
   transformational, comparative, or acceptance-oriented?
3. **Current truth** — What is directly observed, what is reported, and which
   sources conflict?
4. **Expected truth** — What behavior, structure, appearance, or state should
   exist, and what evidence establishes that expectation?
5. **Scope and preservation** — What may change, what must remain untouched, and
   which unrelated work or historical evidence must be preserved?
6. **Authority** — Who authorizes inspection, reproduction, correction,
   migration, rollback, release, and acceptance?
7. **Risk and reversibility** — What could be lost, exposed, corrupted, delayed,
   or made unavailable, and how can the work be isolated or reversed?
8. **Method and evidence** — Which inspection, reproduction, test, comparison,
   rehearsal, or specialist review can distinguish the cause and verify the
   result?
9. **Dependencies and downstream effects** — What consumes, trusts, or depends
   on the current state?
10. **Completion boundary** — What proves diagnosis, repair, migration,
    integration, release, and live verification separately?

## Optional deepening prompts

- Can the issue be reproduced, and under which exact conditions?
- Which claim comes from a person, source file, test, screenshot, log, provider,
  database, or live observation?
- What changed before the issue appeared?
- Which accepted baseline or checkpoint can be compared without overwriting the
  current state?
- Could several causes produce the same visible symptom?
- What is the smallest non-destructive test that separates those causes?
- Which data, permissions, identifiers, references, timestamps, or ordering must
  survive a migration?
- How will retries, concurrency, partial completion, interruption, and rollback
  behave?
- What cleanup is necessary, and what tempting cleanup is unrelated scope?
- Which residual risk or limitation must be stated after the work?

## Mandatory escalation signals

Escalate when the work touches:

- production, shared state, real customer or employee information, credentials,
  secrets, identity, permissions, billing, or destructive mutation;
- uncertain target, conflicting source of truth, missing backup, or untested
  rollback;
- security finding, privacy incident, data corruption, availability incident, or
  legal retention obligation;
- several repositories, environments, providers, schemas, or release owners;
- one-way transformation, large dataset, long-running operation, or partial
  failure;
- an audit request that begins drifting into unapproved implementation;
- evidence that the reported problem is only a symptom of a wider system issue.

## Evidence expectations

Useful evidence may include immutable snapshots, version history, source
inspection, reproducible test cases, read-only provider or database inspection,
checksums, before-and-after comparisons, synthetic rehearsals, migration dry
runs, security or accessibility review, exact environment verification, and
independent acceptance.

Evidence must match the claim. Local success does not prove a shared migration;
a passing build does not prove correct runtime behavior; a screenshot does not
prove underlying state.

## Exit condition

The blueprint can distinguish current and expected truth, exact target and
environment, inspection and mutation authority, preservation and rollback,
cause or remaining hypotheses, downstream effects, matched verification, and
the separate gates for repair, migration, release, and live acceptance.

## Project-generated questions

| Trigger | Generated question | Decision supported | Disposition |
|---|---|---|---|
| `{{ANSWER_RISK_OR_UNKNOWN}}` | `{{QUESTION}}` | `{{DECISION}}` | Ask / Research / Defer / Block |

