# Durable Decisions

Status: Current

## `{{YYYY-MM-DD}}` — `{{DECISION_TITLE}}`

- Authority: `{{PERSON_OR_ROLE}}`
- Decision: `{{WHAT_BECAME_BINDING}}`
- Starting evidence: `{{EVIDENCE}}`
- Alternatives considered: `{{OPTIONS}}`
- Reason: `{{WHY}}`
- Security, data, release, or recovery implication: `{{IMPLICATION_OR_NONE}}`
- Affected contracts or packets: `{{PATHS}}`
- Supersedes: `{{PRIOR_DECISION_OR_NONE}}`
- Review trigger: `{{EVENT_THAT_REOPENS_THE_DECISION}}`

Record only decisions with durable consequence. Preserve an accepted predecessor
and point it to its successor rather than silently rewriting it.

