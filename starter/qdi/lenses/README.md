# QDI Domain Lens Library

Status: Conditional support route  
Purpose: Protect domain-specific discovery quality after the universal anchors
identify what kind of work is being considered

## Relationship to the protocol

Domain Lenses sit between broad anchor coverage and specialist branches:

```text
33 universal Discovery Anchors
        ↓
project and context classification
        ↓
one or more earned Domain Lenses
        ↓
project-specific follow-up questions
        ↓
earned specialist branches
        ↓
convergence and Pre-Build Blueprint
```

The anchors discover the broad shape. A Domain Lens checks that the shape is
understood deeply enough for its kind of work. Specialist branches then resolve
particular product, market, brand, technical, data, operational, or acceptance
decisions.

## Available lenses

| Lens | Use when the intended work primarily involves |
|---|---|
| `SOFTWARE_AND_DIGITAL_PRODUCTS.md` | Software, applications, platforms, websites, data systems, or digital product behavior |
| `SERVICES_AND_BUSINESSES.md` | An offer, customer relationship, commercial model, service delivery, or business operation |
| `OPERATIONS_AND_WORKFLOWS.md` | A repeatable process, handoff, automation, internal operation, or coordination system |
| `DESIGN_AND_CONTENT.md` | Visual, interaction, brand, editorial, content, communication, or design-to-build work |
| `AUDITS_REPAIRS_AND_MIGRATIONS.md` | Inspection, diagnosis, correction, recovery, transfer, upgrade, or controlled change to an existing system |

A project may activate several lenses. Do not load all five merely because they
are available.

## Activation rule

Activate a lens only when:

1. the seed or anchor answers show that its domain materially affects the
   project;
2. the existing answers do not yet satisfy its minimum coverage;
3. the agent records why it is needed in `../BRANCH_PLAN.md` or
   `../ACTIVE_PACKET.md`;
4. the lens remains proportional to the selected discovery depth.

The agent may recommend activation. The human may accept, remove, combine,
reorder, deepen, or narrow the recommendation.

## How to use a lens

For the active lens:

1. credit answers already established by the 33 anchors;
2. identify only the unsatisfied minimum coverage;
3. ask the least leading question that can close each material gap;
4. use optional prompts only when the answer, consequence, or uncertainty earns
   them;
5. generate new questions from the project's actual language and conditions;
6. activate a specialist branch or sidequest when conversation alone is not
   sufficient;
7. record the result and stop when the exit condition is met.

Do not copy every question into the Discovery Ledger. Record the questions that
were actually asked and the durable result.

## Generated-question rule

Each lens deliberately leaves room for questions that could not be known before
the human described the project. A generated question must state or make clear:

- which answer, contradiction, risk, or unknown triggered it;
- which decision or boundary it supports;
- why the existing anchor or lens coverage is insufficient;
- whether it must be answered now, researched, deferred, or made blocking.

A generated question does not become part of the permanent universal library
merely because it helped one project. Repeated questions may be proposed for a
later evidence-backed library revision.

## Quality rule

More questions do not automatically produce better discovery. The lens has done
its job when the human and agent can make the named decision without hiding a
material unknown, contradiction, authority problem, or evidence gap.
