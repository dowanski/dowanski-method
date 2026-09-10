# A booking idea, a clear decision, and one finished planning task

**A fictional worked example of The Dowanski Method v0.3.0.**

This shows what the documents can look like after a useful conversation—not
just the empty templates. The people, dialogue, decisions, and review below
are illustrative. No market research, customer test, or software implementation
is claimed. The finished result is a small planning document.

Read it as an example, not as instructions for your project. It lives outside
the downloadable starter and its required reading path.

[Get the starter](../README.md#start-here) · [Verification and limits](verification.md)

## 1. Start with the idea—not a blank questionnaire

> **You:** I want to make booking easier for independent tutors and their
> students. A tutor should approve a request before it becomes a booking.
>
> **Agent:** Would you like me to guide you through it, work alongside you,
> take the research and planning lead, or challenge a plan you already have?
>
> **You:** Work alongside me. One question at a time. For now, I want to work
> out the flow without connecting to anything.

The agent already knows the intended audience and the importance of approval.
It records that context rather than asking the human to repeat it. Discovery
now focuses on a meaningful gap:

> **Agent:** Then the first thing to make clear is the difference between
> requesting a time and having it confirmed. Should a student ever see
> “Booked” before the tutor has accepted?
>
> **You:** No. Until then, it should say “Awaiting tutor approval.”

The document is beginning to take shape through decisions, not through the
number of questions answered.

## 2. Offer research where it can change the direction

> **Agent:** Before we choose software or build an integration, I would suggest
> a Light Scan of existing booking tools to check that approval behavior.
> We could compare three relevant options using their official documentation,
> within an agreed effort limit, then return to the build-versus-adapt decision.
> An inconclusive result would stay inconclusive. Shall we do that now, or first
> finish the small flow you want to review?
>
> **You:** Finish the flow first. We can compare tools before we choose one.

This is an intentional research deferral, not an answer about what providers
can do. In this example no external search takes place. A real approved scan
would record its sources, findings, limitations, and exact return point.

An excerpt from **[DISCOVERY_LEDGER.md](../starter/qdi/DISCOVERY_LEDGER.md)**:

| Classification | Recorded understanding | What happens next |
|---|---|---|
| OWNER_STATEMENT | The intended users are independent tutors and their students. | Treat as the owner's intended audience, not evidence of market demand. |
| OWNER_CONFIRMED | A request is not a booking until the assigned tutor approves it. | Preserve this rule in the flow and acceptance criteria. |
| DEFERRED | Whether an existing provider meets the approval requirement is unknown. | Owner revisits before provider selection or integration; return to build versus adapt. |
| OWNER_CONFIRMED | The next result is a local, fictional-data flow sheet only. | No customer information, accounts, messages, or external connections. |

These labels separate what the human wants from what research has established.
The human does not need to repeat these answers when the plan is prepared.

## 3. Converge on a small, useful blueprint

> **Agent:** We have enough to review this one flow. We do not yet have enough
> to choose a provider or build a customer-facing booking service. I suggest
> finishing the flow sheet now and keeping that larger decision open.

Selected entries from **[PRE_BUILD_BLUEPRINT.md](../starter/qdi/PRE_BUILD_BLUEPRINT.md)**:

- **Intended change:** distinguish a request from a confirmed booking so the
  student and tutor can understand the same state.
- **Smallest useful proof:** one review sheet showing the states, who can move
  a request between them, and the wording each person sees.
- **Included now:** a fictional request, tutor approval, decline, and student
  withdrawal before approval.
- **Not included:** working software, calendars, payments, messages, real
  identities, or customer data.
- **Unresolved:** provider compatibility and market demand. Neither blocks this
  planning sheet; they remain open before a larger product commitment.
- **Tone:** plain and reassuring; never imply that a pending request is booked.
- **Candidate documentation weight:** Light, because this is one local,
  reversible planning outcome. A real booking system needs a fresh assessment.
- **Acceptance:** every state has a clear meaning, an allowed transition, and
  visible wording. No action bypasses tutor approval.
- **Implementation authority:** not granted by the blueprint.

These are excerpts, not a replacement blueprint or permission to omit relevant
sections. A real blueprint covers every material part of its scoped outcome.

The owner reviews the blueprint and cleanup, authorizes the bounded handoff,
then reviews the adapted Light foundation and packet. Only afterward do they
authorize the specific task. Those are distinct decisions even when the task
is small.

## 4. Give the next task a boundary

The adapted Light foundation uses its normal reading route:

**README → AGENTS → docs/README → docs/PROJECT → docs/WORK_PACKET**

Accepted direction moves into the project record. Closed interview history
does not become something the agent rereads on every action. The deferred
provider question stays visible with its return gate.

An excerpt from **[WORK_PACKET.md](../starter/dm-foundations/light/docs/WORK_PACKET.md)**:

### Outcome

Produce a reviewable booking-request flow sheet in `design/booking-flow.md`.

### Starting evidence

The blueprint and accepted ledger decision establish tutor approval as a
requirement. Provider capabilities remain unverified.

### Scope and authority

- Allowed: create the local Markdown flow sheet using fictional roles;
  check it against the accepted blueprint; update the packet's review record.
- Not allowed: build or publish an application, contact anyone, connect a
  service, use real student information, or choose a provider.
- Stop if a useful next step requires any excluded action or changes who
  is allowed to confirm a booking.

### Execution and verification

1. Map each state and the action that reaches it.
2. Write the label a person would see.
3. Trace request, approval, decline, and withdrawal paths.
4. Check that a student cannot confirm their own request and that a declined
   or withdrawn request cannot be silently reopened.
5. Present the sheet for owner review; preserve anything not yet established.

This packet does not ask an agent to “build the whole platform.” It gives one
piece of work a clear result and a way to review it.

## 5. Inspect the result—and a correction

The sample output in **`design/booking-flow.md`**:

| State | How it is reached | Visible wording | Allowed next action |
|---|---|---|---|
| Draft | Student prepares a request | Not sent | Student submits it. |
| Pending | Student submits the request | Awaiting tutor approval | Assigned tutor approves or declines; student may withdraw. |
| Approved | Assigned tutor approves a pending request | Booked | No further transition defined in this first planning slice. |
| Declined | Assigned tutor declines a pending request | Request declined | A new request must start separately. |
| Withdrawn | Student withdraws a pending request | Request withdrawn | A new request must start separately. |

During the illustrative review, an earlier draft described the pending label
as “Booking confirmed.” The reviewer points out that this contradicts the
accepted approval rule. The agent corrects the label and checks the remaining
states for the same mistake.

The important result is not simply cleaner wording. The original intention
survives into the artifact, and the review has a recorded rule to check against.

### Example review record

- **Corrected:** the pending label now says “Awaiting tutor approval.”
- **Reviewed:** the written paths distinguish requesting from approval; only
  the assigned tutor can approve a pending request.
- **Not verified:** executable permissions, simultaneous actions, accessibility
  of a working interface, provider compatibility, or real-world adoption.
- **Illustrative human decision:** accept the planning sheet only.
- **Remaining question:** cancellation after approval is outside this first
  slice and must be resolved before any complete booking workflow is proposed.

This is document review, not a software test result. A later implementation
would need evidence for its actual behavior and operating risks.

## 6. Close the packet without losing the next question

In the example's **[PROJECT.md](../starter/dm-foundations/light/docs/PROJECT.md)**:

- **Current state:** the flow sheet is accepted as planning material; no
  booking application has been built or released.
- **Now:** no implementation packet is active.
- **Next:** ask the owner whether to begin the provider comparison or explore
  another unresolved part of the flow. Neither starts automatically.
- **Debt:** provider compatibility, wider product demand, and post-approval
  cancellation remain open before the relevant larger commitments.
- **History:** the accepted packet becomes a frozen record. Its closeout
  points back to this project record, which owns the current truth.

The agent does not need every past conversation to resume. It needs the current
position, the accepted decisions, the unresolved questions, and the next gate.

That is the connection between QDI and DM: discovery produces a direction the
human can approve; documentation turns it into a task an agent can follow;
review checks whether the result still matches the intention.

## Try it with your own idea

[Start with the Complete starter](../README.md#start-here), using its startup
instruction and your own context. Do not copy this example's fictional decisions
or approval states into an active project.

For a shorter repair-shaped example, the Light foundation already includes an
[illustrative navigation-overlap packet](../starter/dm-foundations/light/_examples/EXAMPLE_WORK_PACKET.md).
For actual development checks and their limits, read
[Verification and Limits](verification.md).
