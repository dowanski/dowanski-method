# Optional Standard Records

Status: Installation resources; outside the active route

Copy only a record whose responsibility has been earned. Place Main Set records
under `docs/` and workstream records inside the relevant active workstream.
Update the appropriate router and state the trigger.

| Record | Trigger |
|---|---|
| `WORKSTREAM_SET/` | One hard split trigger or the approved supporting-signal threshold creates an independent coordination boundary; copy the folder as one renamed unit and remove the direct Main Set packet |
| `ARCHITECTURE.md` | Durable components or dependencies change independently from the brief |
| `INTERFACES.md` | Several packets depend on one observable boundary or handoff |
| `RELEASE.md` | Integration, deployment, rollback, or live verification needs a separate gate |
| `SOURCES.md` | Research or provenance materially affects decisions or public claims |
| `DESIGN_REVIEW.md` | Human visual/copy direction must be accepted before implementation |
| `EVIDENCE_REGISTER.md` | Proof exceeds the current packet or supports several packets |
| `OWNER_REVIEW.md` | A distinct acceptance package is needed |
| `CLOSEOUT.md` | The workstream needs a durable closure and upward return |
| `RUNBOOK.md` | A repeatable ordered operation has meaningful stop/recovery behavior |
| `CHECKPOINT.md` | Work must pause, transfer, or preserve a relied-upon starting state |

Do not copy the entire directory. If several risk-heavy records become required,
reassess whether the affected workstream should use Governed weight.
