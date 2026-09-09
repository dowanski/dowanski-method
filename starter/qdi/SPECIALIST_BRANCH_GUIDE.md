# QDI Specialist Branch Guide

Status: Conditional operating guidance  
Purpose: Expand the Discovery Map into only the deeper questioning the project
has earned

## Branch rule

This guide is not a second mandatory questionnaire. Use only the approved active
branch. Every question must support its named decision, evidence need, boundary,
test, or operating responsibility.

Begin each branch by completing its contract in `BRANCH_PLAN.md` and the active
packet. End when the decision has sufficient evidence for convergence—not when
every example below has been discussed.

## 01 — Product and experience

### Activate when

- people will use, receive, experience, or depend on an interface, service, or
  workflow;
- the first useful version or journey remains unclear;
- accessibility, trust, failure, or recovery materially changes usability.

### Decisions to support

- what the experience must enable;
- who it serves and in what context;
- which journey and states belong in the first useful proof;
- what can wait;
- what makes the experience understandable and trustworthy.

### Question areas

- What triggers the journey, and what is the user trying to finish?
- What must they know, provide, choose, approve, or receive at each stage?
- What happens for normal, loading, empty, denied, expired, incorrect, failed,
  interrupted, and recovery states?
- Which devices, environments, abilities, assistive technologies, languages, or
  levels of comfort change the design?
- Which moments create uncertainty or require reassurance?
- What is the smallest complete journey that produces meaningful value?
- What should remain deliberately manual or outside the experience?
- How will representative people or operators evaluate it?

### Expected output

Prioritized requirements, journey and state map, first-version boundary,
accessibility context, trust expectations, and testable experience criteria.

### Exit condition

The principal user outcome and required states are coherent, bounded, and
testable enough to inform the blueprint.

## 02 — Market and commercial

### Activate when

- adoption, purchasing, funding, pricing, competition, or sustainable delivery
  affects whether the project should proceed;
- a public or client-delivered offering lacks evidence of demand;
- the buyer, user, payer, or route to market is unclear.

### Decisions to support

- whether a real audience and need are sufficiently supported;
- who chooses, uses, pays, or authorizes;
- how the value reaches them;
- whether delivery and support can be sustained;
- whether to proceed, research, narrow, reposition, or stop.

### Question areas

- Who experiences the problem strongly enough to seek change?
- What evidence exists beyond the founder's interest?
- Which direct competitors, substitutes, internal processes, and do-nothing
  options already serve the need?
- What is meaningfully different, and is that difference valuable to the
  intended audience?
- Who pays or funds the result, and how do their expectations differ from the
  user's?
- What are the realistic discovery, sales, onboarding, delivery, support,
  retention, and exit paths?
- Which costs grow with each user or customer?
- Which market-size, location, timing, price, or willingness assumptions require
  research rather than conversation?

### Expected output

Audience and payer hypotheses, market and alternative evidence, positioning
constraints, delivery model, commercial unknowns, and an evidence-calibrated
go/continue/redirect/stop recommendation.

### Exit condition

The commercial theory is either supported enough for the next stage, converted
into bounded research, accepted as an explicit limitation, or rejected.

## 03 — Brand, tone, and content

### Activate when

- identity, naming, language, content, trust, or emotional experience affects
  adoption or use;
- different surfaces require different communication behavior;
- visual or verbal references influence the intended direction.

### Decisions to support

- what the work should communicate and make someone feel;
- which language and visual qualities belong;
- how the voice changes by context;
- what must never be implied;
- how content should lead understanding and action.

### Question areas

- What should someone understand in the first encounter?
- What should they feel, and what would break that feeling?
- Which values or traits must be demonstrated rather than merely claimed?
- Which words, metaphors, labels, and promises fit the work?
- Which language feels inflated, generic, misleading, exclusionary, or
  directionally wrong?
- How should tone differ across marketing, product UI, help, errors, consent,
  support, and technical documentation?
- Which references capture the intended essence, and which attractive examples
  should not be copied?
- What content order helps someone understand, trust, decide, and act?

### Expected output

Positioning, naming direction where needed, voice rules, vocabulary and
anti-language, reference rationale, content hierarchy, and design principles.

### Exit condition

The verbal and experiential direction is distinct, internally consistent,
honest about the product, and usable by later design and implementation work.

## 04 — Technical architecture and stack

### Activate when

- the project requires software, data, integrations, deployment, migration, or
  ongoing technical operation;
- more than one viable approach exists;
- existing systems, maintainers, cost, scale, reliability, or risk constrain the
  choice.

### Required sequence

Do not begin by selecting a preferred technology. Establish:

1. required behavior and journeys;
2. users, expected scale, performance, availability, and lifecycle;
3. data relationships, sensitivity, retention, and authority;
4. interfaces, integrations, real-time, asynchronous, or offline needs;
5. current infrastructure, migration, and compatibility constraints;
6. maintainer capability, ownership, budget, and timeframe;
7. security, privacy, accessibility, compliance, monitoring, recovery, and
   retirement expectations;
8. candidate options and tradeoffs;
9. recommendation and owner decision.

### Question areas

- Which capabilities must exist, and which qualities must the system maintain?
- What already exists and must remain intact or interoperable?
- What information moves where, under whose authority, and at what frequency?
- What fails if a dependency, network, provider, or automated step is
  unavailable?
- What must be reversible, observable, auditable, portable, or independently
  testable?
- Who will maintain the result, and which choices fit their actual capability?
- Which costs, limits, vendor dependencies, or licensing terms matter?
- What small technical proofs are required before adopting the architecture?
- Why is the recommendation stronger than each serious alternative for this
  exact project?

### Expected output

Architectural requirements, interface boundaries, option comparison, stack
recommendation with traceable reasons, rejected alternatives, technical proofs,
and accepted tradeoffs.

### Exit condition

The recommendation follows from the project's accepted needs and constraints,
has a named owner decision, and does not disguise untested assumptions as
architecture.

## 05 — Data, authority, and security

### Activate when

- information is collected, inferred, stored, changed, shared, retained, or
  deleted;
- accounts, permissions, agents, automation, provider access, money, sensitive
  data, destructive mutation, or external communication enter scope;
- failure could harm a person, organization, asset, or trusted system.

### Decisions to support

- what data and authority exist;
- who or what may perform each action;
- what requires human approval;
- what must be prevented, logged, detected, revoked, recovered, or reviewed;
- which qualified assessment is required.

### Question areas

- What information exists, where does it originate, and who owns or stewards it?
- Which information is sensitive, unnecessary, regulated, or unsafe to place in
  prompts, logs, documentation, or public evidence?
- Who may inspect, recommend, decide, create, change, communicate, delete, or
  restore each class of information?
- How is access granted, narrowed, checked, revoked, and audited?
- Which agent actions are read-only, proposal-only, human-approved, reversible,
  or prohibited?
- What could go wrong through error, abuse, misunderstanding, concurrency,
  dependency failure, or malicious input?
- How will failure be prevented, detected, contained, communicated, recovered,
  and learned from?
- Which privacy, security, legal, accessibility, financial, or other qualified
  reviews exceed this protocol's competence?

### Expected output

Data inventory and lifecycle, authority model, approval and revocation gates,
trust boundaries, threat and failure questions, evidence requirements, recovery
posture, prohibited actions, and specialist-review queue.

### Exit condition

Material data and authority paths are visible, high-consequence unknowns have
owners and gates, and no conversation-level conclusion substitutes for required
qualified review.

## 06 — Operations and delivery

### Activate when

- the result must be operated, supported, monitored, changed, released,
  transferred, recovered, or retired;
- work crosses people, agents, teams, vendors, or environments;
- a successful build could still fail through unclear ownership or handoff.

### Decisions to support

- who operates and owns each ongoing responsibility;
- how work is delegated and reviewed;
- how change, release, support, recovery, transfer, and retirement function;
- which knowledge must survive a handoff.

### Question areas

- Who is accountable after the initial build, and what do they need to operate
  confidently?
- Which work is human-led, agent-assisted, automated, externally provided, or
  deliberately manual?
- Where does responsibility transfer, and what evidence permits that transfer?
- How are incidents, dependency failures, user problems, and support requests
  received and triaged?
- What must be monitored, how often, by whom, and what action follows a signal?
- Who authorizes releases, changes, rollback, restoration, and retirement?
- What happens when a maintainer, provider, tool, or required dataset is no
  longer available?
- Which runbooks, training, documentation, or transfer evidence are actually
  required?

### Expected output

Responsibility map, operating and support boundaries, delegation model,
monitoring expectations, release and recovery path, handoff needs, and lifecycle
ownership.

### Exit condition

The proposed result has an operable home after construction, or the lack of one
is treated as a blocking or accepted limitation.

## 07 — Evidence, QA, and acceptance

### Activate when

- a claim, design, behavior, migration, safety boundary, release, or result must
  be proven;
- the owner needs a defensible definition of done;
- different environments or reviewers could produce conflicting conclusions.

### Decisions to support

- what must be demonstrated before and during implementation;
- which evidence matches each claim;
- who accepts the result;
- what blocks release or returns the project to discovery.

### Question areas

- Which statements are owner beliefs, hypotheses, external facts, design
  intentions, implemented behavior, or live operational claims?
- What evidence can support each without overstating its scope?
- Which behaviors require automated tests, manual review, representative-user
  evaluation, source inspection, provider evidence, or live verification?
- Which environments, devices, browsers, accessibility modes, permissions,
  failure states, and data conditions must be covered?
- Who is independent enough and authorized to accept the result?
- What severity or kind of finding blocks the next stage?
- What limitation can be accepted, and who accepts it?
- Which result would invalidate an assumption and return the project to QDI?

### Expected output

Claim-to-evidence map, test and review strategy, acceptance authority, release
gates, limitation language, and rediscovery triggers.

### Exit condition

The intended result can be evaluated through evidence whose scope matches the
claims, with named acceptance authority and failure gates.

## Convergence return

When a branch closes:

1. record its decision, supporting evidence, limitations, and surviving unknowns;
2. update the Discovery Ledger and Current State;
3. return its result to the named Pre-Build Blueprint destination;
4. identify whether it changed another branch or anchor;
5. reopen only the smallest affected boundary;
6. continue with the next approved branch or begin convergence.

