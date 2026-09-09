# Optional Governed Controls

Status: Installation resources; outside the active route

Copy only the record whose trigger exists, place it in the relevant Main Set,
workstream, or operations path, and update the router.

| Record | Trigger |
|---|---|
| `THREAT_MODEL.md` | Assets, trust boundaries, attacker paths, and mitigations require explicit review |
| `SECURITY_REVIEW.md` | A distinct security assessment or remediation gate exists |
| `MIGRATION_PLAN.md` | Shared or production state changes through an ordered migration |
| `ROLLBACK_PLAN.md` | Change is difficult to reverse or requires coordinated recovery |
| `INCIDENT_RECORD.md` | A real incident requires containment, evidence, decisions, and follow-up |
| `CHECKPOINT.md` | A relied-upon state must be frozen for recovery, transfer, or later work |
| `TEST_MATRIX.md` | Several actors, outcomes, environments, or negative paths need structured coverage |
| `INDEPENDENT_REVIEW.md` | Risk requires a reviewer outside the implementation lane |
| `DATA_PRIVACY_BOUNDARY.md` | Data classes, minimization, retention, or disclosure boundaries require explicit control |
| `OWNER_REVIEW.md` | The workstream has reached its named owner-acceptance gate |
| `CLOSEOUT.md` | A review disposition exists and the governed route is ready to return and close |

Do not copy every file. Governed means triggered control, not maximum paperwork.
