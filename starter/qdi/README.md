# QDI Router

Status: Routing reference

Purpose: Select the smallest sufficient context for the current action

## Resume route

Read [AGENTS](../AGENTS.md), [Current State](CURRENT_STATE.md), and
[Active Packet](ACTIVE_PACKET.md) after the root README on a new session.
Within a session, reuse unchanged instructions. Current State owns the resume
position; Active Packet owns one lane and its next action. The Ledger preserves
provenance. A route is permission to read only within the accepted scope.

## Phase routes

Use exactly one active phase. Read only the relevant section of each selected
module, plus the instructions needed to interpret it. Update Current State and
Active Packet together when the phase changes.

| Phase | Read for this action | Advance when / next route |
|---|---|---|
| `SEED` | [Discovery Anchors](DISCOVERY_ANCHORS.md), Opening contract and seed | Storage bounded, collaboration/delivery recorded, human confirms seed → `ANCHOR_DISCOVERY` |
| `ANCHOR_DISCOVERY` | [Discovery Anchors](DISCOVERY_ANCHORS.md), next-move rules and relevant coverage only | A consequential branch is earned → `BRANCH_PLANNING`; readiness supported → `CONVERGENCE`; otherwise continue the useful gap |
| `BRANCH_PLANNING` | [Branch Plan](BRANCH_PLAN.md), [Lens router](lenses/README.md) | Human accepts branch scope and order → `SPECIALIST_DISCOVERY`; none earned → `CONVERGENCE` |
| `SPECIALIST_DISCOVERY` | [Branch Plan](BRANCH_PLAN.md), selected section of [Specialist Guide](SPECIALIST_BRANCH_GUIDE.md), one active branch packet | Named proof/decision complete → cleanup, then next approved branch or `CONVERGENCE` |
| `SIDEQUEST_ACTIVE` | One named active packet created from [Sidequest Template](SIDEQUEST_TEMPLATE.md) | Results integrated and cleanup accepted → exact saved phase and return point |
| `CONVERGENCE` | [Pre-Build Blueprint](PRE_BUILD_BLUEPRINT.md), scoped unresolved Ledger items | Required evidence sufficient and cleanup passed → `OWNER_REVIEW`; gaps → named discovery route |
| `OWNER_REVIEW` | [Owner Review](OWNER_REVIEW.md), accepted review versions of Blueprint and cleanup | Proceed → `APPROVED_FOR_HANDOFF`; continue/redirect → named discovery route; defer/stop → corresponding phase |
| `APPROVED_FOR_HANDOFF` | [Owner Review](OWNER_REVIEW.md); [Handoff Template](QDI_TO_DM_HANDOFF.md) only with explicit generation authority | Present generated handoff; accepted setup authority → [DM receiver](../dm-foundations/README.md); otherwise wait at the human gate |
| `DEFERRED` | Current State and Active Packet only | Recorded restart condition and human direction → named phase |
| `STOPPED` | Current State and the recorded stop decision only | Human explicitly reopens → linked successor cycle |

Do not read every row or ask anchors in order. Supplied context and research
can resolve several anchors. Material evidence and risk—not count—decide readiness.

## Conditional event routes

Events supplement the active phase; they do not silently replace it.

| Trigger | Read or update | Return / keep outside active context |
|---|---|---|
| Storage/access unselected or changing | [Installation](../INSTALLATION_AND_STORAGE.md) | Record boundary; return to active phase |
| Record answer, evidence, correction, contradiction, or decision | [Discovery Ledger](DISCOVERY_LEDGER.md), classification rules and relevant entry only | Record once; history outside default route |
| Classify work or check domain gaps | [Lens router](lenses/README.md), only relevant lenses | Return to active question/branch; other lenses stay inactive |
| Dedicated research earned under the anchor guide's level rules | [Sidequest Template](SIDEQUEST_TEMPLATE.md) | Save phase/return point; accept scope, level, effort, and authority; integrate before returning |
| Allocate/resolve/move a durable ID; full cleanup or handoff | [Record Index](QDI_RECORD_INDEX.md) | Return to triggering action; ordinary questions do not receive IDs |
| Close sidequest/branch; before review, handoff, or child cycle; documentation drag | [Cleanup Checkpoint](CONTEXT_CLEANUP_CHECKPOINT.md) | Accept reduced route; return to next eligible phase |
| Report usage; plan expensive work; diagnose retry/reading loops; prepare complex resumption or coordination | [Stewardship policy](../CONTEXT_AND_TOKEN_STEWARDSHIP.md), relevant sections | Keep persistent rules in AGENTS; detailed history becomes reference after resolution |
| Investigate specific closed evidence | [Archive router](archive/README.md), then named record | Historical evidence only; return to active question |

Every event records its result in the existing canonical file. Do not create a
second standing index or status document.

## Recovery and exclusion

If the next target is missing, inspect its link and Current State. Resolve an
existing durable ID through the Record Index; otherwise repair from accepted
current evidence. If intent or authority remains ambiguous, stop the affected
action and ask the human. Never substitute a similar filename or an archive
entry as current authority.

After copying or moving a record, validate its outgoing relative links from
the new location, repair incoming active links, and update any indexed path
without changing its ID. Return links must still resolve; historical copies
must remain distinguishable from current authority.

Reconcile mismatched phase/packet values before acting. An active sidequest
must name its saved return point; without it, repair the packet before research.
Closed branches, unrelated evidence, other lenses, and unused foundations stay
outside active context. An instruction to read them all is context drift.

All files under `dm-foundations/` stay inactive during discovery. Only the
accepted handoff's setup gate opens the receiver. Implementation still requires
review of the adapted DM route and first bounded Work Packet.
