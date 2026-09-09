# Domain Lens — Operations and Workflows

Status: Conditional  
Use for: Internal processes, recurring work, handoffs, automation, coordination,
administrative systems, and service operations

## Activate when

- work moves repeatedly among people, agents, tools, or systems;
- delay, duplication, loss, confusion, inconsistency, or manual effort is part
  of the problem;
- automation or process redesign is being considered;
- success depends on reliable operation after the first implementation.

## Minimum coverage

1. **Trigger and outcome** — What starts the workflow, and what verified result
   should finish it?
2. **Current path** — What actually happens today, including informal work and
   workarounds?
3. **Participants** — Which people, roles, agents, tools, databases, providers,
   or physical conditions touch it?
4. **Inputs and state** — What information, materials, approvals, and conditions
   enter or change through the process?
5. **Handoffs** — Where do responsibility, authority, information, or state
   transfer?
6. **Decision points** — Which steps require judgment, approval, interpretation,
   or an exception rather than routine execution?
7. **Friction and failure** — Where can work be lost, delayed, duplicated,
   misunderstood, blocked, or completed incorrectly?
8. **Automation boundary** — What should be automated, assisted, proposed,
   observed, or deliberately remain human?
9. **Operation and recovery** — Who monitors, corrects, resumes, escalates, and
   maintains the workflow?
10. **Acceptance** — How does the system confirm that its final output and
    downstream effect are correct?

## Optional deepening prompts

- Which steps exist because of a real requirement, and which are historical
  habit?
- Where is the same information entered, transformed, or interpreted more than
  once?
- What must be true before each step can begin?
- Which queues, waiting periods, deadlines, limits, dependencies, and service
  expectations matter?
- What happens for incomplete, conflicting, late, duplicated, unauthorized, or
  malformed input?
- Which exceptions are frequent enough to design explicitly?
- How can a person inspect, approve, reject, correct, retry, or override an
  automated recommendation?
- What audit trail is needed to explain who or what acted and why?
- Could removing one bottleneck create overload, risk, or delay elsewhere?
- Which part of the process should be improved before software is introduced?

## Mandatory escalation signals

Escalate when the workflow includes:

- customer, employee, financial, identity, health, or other sensitive data;
- automated decisions or communications with material external effect;
- money movement, eligibility, access control, deletion, or irreversible action;
- several organizations, teams, providers, or conflicting authorities;
- high-volume work, concurrency, retries, duplicate events, or strict timing;
- hidden manual recovery performed by one person;
- no reliable current baseline or disagreement about how the process works;
- an automation proposal that treats a symptom while moving failure elsewhere.

## Evidence expectations

Useful evidence may include process observation, participant interviews,
workflow maps, existing forms and records, timing or queue data, error and
incident patterns, dependency inspection, synthetic rehearsals, failure-state
tests, and operator review.

The idealized procedure is not evidence of the actual workflow. Record the
difference between policy, documentation, and observed practice.

## Exit condition

The blueprint can show the current and intended workflow, inputs, outputs,
participants, decision and authority points, handoffs, exceptions, automation
boundary, operational owner, recovery behavior, and evidence of correct
completion.

## Project-generated questions

| Trigger | Generated question | Decision supported | Disposition |
|---|---|---|---|
| `{{ANSWER_RISK_OR_UNKNOWN}}` | `{{QUESTION}}` | `{{DECISION}}` | Ask / Research / Defer / Block |

