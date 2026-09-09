# Domain Lens — Software and Digital Products

Status: Conditional  
Use for: Applications, platforms, websites, digital tools, data systems, APIs,
and software-enabled product experiences

## Activate when

- software behavior or a digital interface is part of the proposed result;
- data, identity, integrations, deployment, or technical operation affects the
  solution;
- the first useful product boundary or end-to-end behavior is unclear.

Do not activate merely because software may eventually support a service. Use
this lens when software decisions materially affect the current discovery.

## Minimum coverage

Existing anchor answers may satisfy these responsibilities. Ask only for the
gaps.

1. **User outcome** — What must a person or system be able to accomplish?
2. **Complete journey** — What begins the interaction, what happens through it,
   and what constitutes a finished outcome?
3. **States and exceptions** — What should happen when information is missing,
   incorrect, denied, expired, delayed, duplicated, interrupted, or unavailable?
4. **Current environment** — What software, data, infrastructure, provider, or
   manual process already exists and must remain intact or interoperable?
5. **Information and authority** — What data moves, who may inspect or change
   it, and which system or human approvals are required?
6. **Interfaces and dependencies** — Which APIs, tools, services, devices,
   databases, agents, or third parties must participate?
7. **Operating qualities** — What scale, speed, availability, accessibility,
   privacy, security, recovery, and maintainability actually matter?
8. **Ownership and lifecycle** — Who will deploy, monitor, support, change,
   transfer, and retire the result?
9. **Smallest useful proof** — What bounded behavior can demonstrate value
   without pretending the entire product is complete?
10. **Acceptance** — What evidence would show that the behavior is correct and
    appropriate for the intended environment?

## Optional deepening prompts

- Which roles see different information or actions?
- Which actions are read-only, proposal-only, reversible, destructive, or
  externally visible?
- Which data relationships require a relational, document, event, file, or
  other model?
- Does any behavior need to be real-time, asynchronous, scheduled, offline, or
  resilient to retries?
- What happens when a provider, integration, agent, or network fails?
- Which existing contracts, schemas, routes, files, or user behaviors cannot be
  broken?
- What must be portable, observable, auditable, cached, localized, searchable,
  or recoverable?
- Which technical choices fit the real maintainers, budget, timeframe, and
  deployment environment?
- Which proof-of-concept can be discarded after it answers its question?
- What would make a seemingly useful feature harmful, misleading, or too costly
  to maintain?

## Mandatory escalation signals

Activate or deepen the relevant specialist branch when the project introduces:

- authentication, accounts, roles, or tenant boundaries;
- sensitive or regulated data;
- billing, money movement, legal agreement, or customer entitlement;
- agent or automation authority beyond read-only analysis;
- destructive data change, migration, irreversible action, or difficult
  rollback;
- production integration with external providers;
- prompt injection, untrusted input, generated actions, or secret exposure;
- accessibility-critical public or required-use experiences;
- high availability, safety, or material business dependence;
- several teams, repositories, environments, or release authorities.

These signals may promote a Light cycle or require qualified review. Do not
resolve them through confident language alone.

## Evidence expectations

Depending on depth, useful evidence may include:

- current-system or repository inspection;
- real journey observation or user evidence;
- architecture and interface comparison;
- a disposable technical proof;
- schema or contract rehearsal with synthetic data;
- threat, privacy, accessibility, or reliability review;
- automated and manual acceptance evidence;
- provider or live-environment verification only when separately authorized.

## Exit condition

The blueprint can state the required digital behavior, complete journey,
important exception states, information and authority boundaries, technical and
operational constraints, smallest useful proof, and evidence required before
release. A stack recommendation may follow from those facts; it may not replace
them.

## Project-generated questions

Record only questions earned by this project's answers:

| Trigger | Generated question | Decision supported | Disposition |
|---|---|---|---|
| `{{ANSWER_RISK_OR_UNKNOWN}}` | `{{QUESTION}}` | `{{DECISION}}` | Ask / Research / Defer / Block |

