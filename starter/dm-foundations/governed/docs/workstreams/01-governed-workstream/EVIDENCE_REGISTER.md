# Evidence Register

Status: Active  
Scope: `{{GOVERNED_WORKSTREAM}}`

| Claim | Required proof | Evidence identity | Starting state | Environment | Result | Limitation | Stale trigger | Reviewer |
|---|---|---|---|---|---|---|---|---|
| `{{CLAIM}}` | `{{MATCHED_PROOF}}` | `{{PATH_RECEIPT_REPORT_OR_COMMAND}}` | `{{IDENTITY}}` | `{{ENVIRONMENT}}` | `{{NOT_EVALUATED_PENDING_PASS_FAIL_INCONCLUSIVE_STALE}}` | `{{LIMIT}}` | `{{CHANGE_REQUIRING_RECHECK}}` | `{{ROLE}}` |

## Evidence rules

- Record what the artifact proves and does not prove.
- Preserve raw output in its authorized evidence store.
- Do not paste secrets, customer data, or large logs into this file.
- A changed dependency, source identity, environment, or contract can make
  evidence stale.
- Independent review records reviewer identity and scope without implying
  release authority.
