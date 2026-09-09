# Operations Router

Status: `{{ACTIVE_OR_NOT_YET_REQUIRED}}`  
Operational owner: `{{PERSON_OR_ROLE}}`

## Purpose

Route repeatable operational, incident, recovery, migration, and rollback tasks
without mixing them into ordinary implementation.

## Active runbooks

| Trigger | Runbook | Required authority | Last verified |
|---|---|---|---|
| `{{TRIGGER_OR_NONE}}` | `{{PATH}}` | `{{ROLE_OR_PERMISSION}}` | `{{YYYY_MM_DD}}` |

## Emergency boundary

- Preserve first when: `{{UNCERTAIN_OR_DESTRUCTIVE_STATE}}`
- Never record: secret values, unnecessary customer data, or raw credentials.
- Contact or escalation: `{{SAFE_INTERNAL_ROUTE}}`
- Incident record: `{{PATH_OR_CREATED_ONLY_WHEN_TRIGGERED}}`

## Maintenance

Reverify a runbook when its dependency, permission, interface, environment, or
recovery target changes. Retire it from this route when its operation no longer
exists.

