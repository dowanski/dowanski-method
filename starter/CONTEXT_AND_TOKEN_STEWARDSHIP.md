# QDI Context and Token Stewardship

Status: Conditional operating reference; persistent rules remain in AGENTS  
Purpose: Use the smallest sufficient context and effort without weakening
necessary discovery, evidence, safety, or review

## Honest capability boundary

This packet instructs a compatible agent to manage context and token-consuming
behavior carefully. It does not retrain the model, control a provider's pricing
or context window, or guarantee an exact token total.

When exact usage telemetry is available, the agent may report it. When it is not
available, the agent must not invent a count. It should instead manage the
observable causes of waste: unnecessary reading, repetition, unbounded output,
unchanged retries, aimless research, oversized handoffs, and documentation
loops.

## When to read

Read the relevant sections before reporting usage, planning materially expensive
work, diagnosing retries or documentation drag, or preparing complex resumption
or coordination. The [QDI router](qdi/README.md) selects these triggers.
The first-session explanation and persistent rules live in [AGENTS.md](AGENTS.md).
This reference does not need to be loaded on every start or continuation.

## Telemetry classes and reporting

Never merge unlike measurements into one number:

- **Account-window telemetry** may report a rounded percentage used or
  remaining, a window length, and a reset time. It may include work from other
  tasks using the same account and is not the cost of this QDI cycle alone.
- **Task or goal counters** may report execution tokens, time, or a user-defined
  budget for the current task. They are not automatically the provider's billed
  tokens or account-allowance percentage.
- **Forecasts** about completion, remaining effort, cost, or likely usage are
  estimates and must be labeled as such.

When real account telemetry exists, check it at the beginning and end of a
material work packet and at one useful midpoint or suspected budget boundary.
Do not poll repeatedly merely to narrate small changes. Report the source,
measurement type, time checked, and whether other tasks may have contributed.

When telemetry does not exist, do not create a percentage from document length,
elapsed time, message count, intuition, or a qualitative effort label.

## Priority order

When goals compete, use this order:

1. human safety and legitimate authority;
2. correctness and honest evidence;
3. the approved project outcome and acceptance gate;
4. clear, resumable current context;
5. efficient token and tool use;
6. convenience or speed.

Token savings never justify fabricating certainty, skipping a required test,
concealing a limitation, weakening a security or privacy boundary, or declaring
unfinished work complete.

## Active-context budget

The default agent route contains only:

1. the human entrypoint and canonical agent instructions;
2. Current State;
3. one Active Packet;
4. only the conditional lens, branch section, sidequest, evidence source, or
   owner-review record required by the current action.

Do not preload the complete Ledger, all Domain Lenses, all specialist branches,
all sidequests, or the archive. Resolve links on demand.

When a summary is sufficient, cite the canonical record rather than copying its
full contents into another active file.

## Conversation and output discipline

- Ask only unanswered, decision-relevant questions.
- In Grouped mode, keep related groups small enough for clear answers.
- Reflect an answer once, then record the accepted meaning and advance.
- Do not repeat background merely to demonstrate understanding.
- Use concise progress reports unless detail is required for a decision or
  requested by the human.
- Store large raw evidence in an appropriate artifact location and place only
  its claim, result, limitation, and reference in active Markdown.
- Do not generate alternative drafts, diagrams, plans, or documents without a
  decision they are meant to support.

## Research and tool-use discipline

Before a materially expensive branch, sidequest, repository scan, prototype,
multi-agent effort, or test suite, state:

- the exact decision or unknown it addresses;
- why existing information is insufficient;
- the smallest useful scope;
- the expected evidence;
- a qualitative effort level: `LOW`, `MODERATE`, or `HIGH`;
- a lower-cost alternative, if one exists;
- the stopping condition;
- whether human approval is required.

Batch independent read-only inspection when it improves efficiency. Reuse valid
existing evidence when the source state and claim have not changed. Do not rerun
a test, search, or analysis merely to produce fresh activity.

## Phase budget and verification reserve

Before a material work packet begins, define:

- one bounded outcome;
- the proof required to accept it;
- exclusions and deferred work;
- the next human gate;
- an initial effort posture or available task budget, when the environment
  supports one;
- a protected reserve for verification, repair, and final reporting.

Do not spend the verification reserve on optional exploration merely because it
is interesting. If available capacity tightens, reduce or defer optional
investigation first. Never reduce required acceptance evidence, safety review,
or an owner gate merely to meet a usage target. A new phase does not erase the
prior phase's spending or variance.

## Bad-loop circuit breaker

For every retry, record or state what changed:

- a new hypothesis;
- new source or evidence;
- changed code or document;
- changed external state;
- corrected target or instruction;
- newly granted authority.

If the same approach produces no new evidence or progress twice in succession,
stop before a third attempt. Diagnose the loop, identify the missing condition,
and recommend one of:

1. change the hypothesis or method;
2. narrow the scope;
3. obtain missing context, access, or human direction;
4. preserve the blocker and continue another eligible lane;
5. pause or stop.

A third attempt is allowed only when something material has changed. Rephrasing
the same request or rereading the same unchanged sources is not a material
change.

The circuit-breaker rule remains in the canonical agent instructions for the
life of the project. The detailed retry history remains active only while it is
needed to diagnose or recover the issue. After resolution, preserve the final
cause, correction, consequential evidence, and any lasting prevention rule in
their canonical homes. Classify the individual attempts as `REFERENCE` or
`ARCHIVE_PRIVATE` during Context Cleanup unless an incident, audit, or unresolved
failure still requires them. Do not force every future agent to reread a closed
retry sequence.

## Documentation-implementation balance

Documentation should enable the next responsible action. It has become drag
when the agent repeatedly rewrites plans, duplicates accepted facts, maintains
inactive routes, creates records without independent responsibilities, or spends
more effort describing unchanged work than reducing uncertainty or producing
evidence.

When drag appears:

1. stop creating new standing files;
2. identify the one canonical current source;
3. update Current State and the Active Packet;
4. run `qdi/CONTEXT_CLEANUP_CHECKPOINT.md`;
5. resume only after the route is smaller or the retained weight is justified.

## Compaction and resumption

Compaction is a platform-managed continuity event, not a guaranteed token-saving
action. Do not trigger, imitate, or repeatedly summarize merely to create the
appearance of compaction.

Before a pause, long sidequest, model change, agent handoff, or context-window
reset:

1. preserve the exact accepted baseline;
2. write durable discoveries to the Ledger;
3. preserve completed proof and exact evidence references rather than raw
   repeated output;
4. update Current State with current truth, authority, blocker, and next action;
5. update the Active Packet with one lane and return point;
6. record remaining required acceptance and the next human gate;
7. remove closed material from default routing;
8. check resumption from the routed files, not the conversation transcript,
   using the review depth defined in the
   [Cleanup Checkpoint](qdi/CONTEXT_CLEANUP_CHECKPOINT.md).

## Coordination discipline

Use one canonical writer for each active state or decision record. Parallel or
specialist agents may return bounded findings, but they should not independently
rewrite the same source of truth, invent permanent IDs, or create competing
status documents. Independent review should inspect the real acceptance
boundary and return findings to the canonical writer.

The number of reviewers, retry limit, usage threshold, and effort range are
project controls, not universal constants. Keep them proportionate to risk and
coordination needs. Never rush, conceal uncertainty, relabel failed proof, or
automatically consume paid credits or reset allowances to satisfy a target.

## Stewardship record

Current State should record:

- whether exact usage telemetry is available;
- the active context route;
- the last action that produced material progress;
- consecutive unchanged attempts;
- any approved `HIGH`-effort lane;
- the next cleanup trigger.

This record is operational, not a performance score. Do not optimize for fewer
tokens at the expense of a correct and responsibly verified result.
