# The Dowanski Method

**From an idea to work an agent can follow—and a human can review.**

A set of Markdown templates—plain-text files you and your AI agent can read and
update—to help plan a project and keep its work organized. Explore the idea
together, record the decisions that matter, and give each next step a clear
purpose, boundary, and review point.

Use it to shape an idea, plan a feature, or bring clearer direction to ongoing
work. Start with QDI—Questions, Documentation, Implementation—then choose the
smallest documentation foundation that fits your project.

Built from Dowanski's working practice and shared so you can inspect it, adapt
it, and improve your own workflow. It is a method to try, not a claim that every
project or agent should work the same way.

**Current edition:** [v0.3.0 — Adaptive Discovery](https://github.com/dowanski/dowanski-method/releases/tag/v0.3.0).

Choose how you want to work with your agent, build on what you already know,
and explore useful research together. This edition adds four collaboration
choices, three research levels, and clearer guidance on when to move forward.
See [what changed and why](CHANGELOG.md).
The [previous v0.2.0 edition](https://github.com/dowanski/dowanski-method/releases/tag/v0.2.0)
remains available with its original downloads.

## Start here

Want to see what the files become? **[Follow a small worked example](guides/worked-example.md)**
from an idea to a recorded decision, a work packet, and a reviewed result.
It is a fictional planning example, not a customer case study.

If you are reading the source repository, open [the complete starter](starter/README.md).
Keep it in a separate private folder or a deliberately isolated project path;
do not replace an existing project's instructions. The
**[Complete starter ZIP](https://github.com/dowanski/dowanski-method/releases/download/v0.3.0/dowanski-method-complete-v0.3.0.zip)**
is the recommended download.

Open the starter folder in a compatible agent environment with local-file
access and say:

> Read `README.md` and `AGENTS.md` completely, then begin the Dowanski QDI
> Discovery Protocol. Do not read `dm-foundations/` and do not implement the
> project.

Those filenames refer to the **starter folder**, not this repository's
maintenance instructions. For a packet inside an existing repository, follow
the [contained-path instructions](starter/INSTALLATION_AND_STORAGE.md).

## What happens next

```text
Your idea → QDI discovery → accepted blueprint → bounded handoff
         → one tailored DM foundation → review → authorized implementation
```

- **Discovery that adapts.** Choose one question at a time or small groups.
  Thirty-three anchors guide coverage; relevant follow-ups deepen the work.
- **Research with a return point.** A sidequest has a question, boundary, and
  stopping condition, then returns to the conversation it interrupted.
- **Documentation with a job.** Current state, decisions, work packets,
  evidence, and cleanup each have an explicit home and reading route.
- **Human accountability.** The agent must challenge drift, preserve
  uncertainty, and stop at the stated gates. Planning does not authorize action.

<details>
<summary>A conversation, not a questionnaire — see an example</summary>

An illustrative exchange after the initial setup—not a provider recommendation
or a result from a real project:

> **You:** “I want to make booking easier for independent tutors and their
> students. Tutors should approve a request before the booking is confirmed.”
>
> **Agent:** “You’ve given us a clear picture of who this is for and what you
> want to make easier. Before we build, I’d suggest checking whether an existing
> booking tool can support the approval process you have in mind. I can take a
> quick, focused look and bring back a recommendation. Then we can decide together
> whether to use what’s available, adapt it, or build something new. Would you
> like me to explore that?”

The agent builds on what you share, suggests useful research, and returns to
the decision at hand. You choose the direction and approve the next step.

</details>

## One start, three possible foundations

| Foundation | Appropriate shape of work |
|---|---|
| Light | One coherent, reversible, low-consequence outcome |
| Standard | A growing project with stages, decisions, and handoffs |
| Governed | Consequential work requiring explicit control and review records |

These are documentation weights, not quality grades. The complete starter
includes all three **inactive** foundations. After discovery and approval, the
agent adapts one. Advanced direct downloads omit QDI and require an already
established project context and authority.

## Downloads — v0.3.0

| Package | Files | Use |
|---|---:|---|
| [Complete starter](https://github.com/dowanski/dowanski-method/releases/download/v0.3.0/dowanski-method-complete-v0.3.0.zip) | 96 | Recommended: QDI first, with three inactive foundations |
| [Light](https://github.com/dowanski/dowanski-method/releases/download/v0.3.0/dowanski-method-light-v0.3.0.zip) | 14 | Advanced direct foundation; omits QDI |
| [Standard](https://github.com/dowanski/dowanski-method/releases/download/v0.3.0/dowanski-method-standard-v0.3.0.zip) | 26 | Advanced direct foundation; omits QDI |
| [Governed](https://github.com/dowanski/dowanski-method/releases/download/v0.3.0/dowanski-method-governed-v0.3.0.zip) | 34 | Advanced direct foundation; omits QDI |

Counts include bundled license/version notices, not daily reading requirements.
[SHA-256 checksums](https://github.com/dowanski/dowanski-method/releases/download/v0.3.0/SHA256SUMS.txt)
cover the four ZIPs. GitHub's generated **Source code** download contains the
maintainer repository; use **Complete starter** for the ready-to-adopt packet.

## Explore without reading everything

- [How the system fits together](guides/how-it-works.md)
- [Installation, downloads, and storage](guides/getting-started.md)
- [What has been tested—and what has not](guides/verification.md)
- [A worked example: from an idea to a reviewed plan](guides/worked-example.md)
- [Inspect the discovery router](starter/qdi/README.md)
- [Feedback and contribution boundaries](CONTRIBUTING.md)
- [Security reporting](SECURITY.md)

## Questions and experiences welcome

Curious about where to start, or have you tried it on a project?
[Ask a question or share what you learned](https://github.com/dowanski/dowanski-method/issues/new?template=experience.yml).
Tell us what helped, what you adapted, or what could be clearer.
[Report a specific problem](https://github.com/dowanski/dowanski-method/issues/new?template=problem.yml)
when an instruction or file did not work as expected.

These conversations are public. Keep private project details out; use
[the private security route](SECURITY.md) for sensitive concerns.

No service account, subscription, or runtime dependency is required to read the
files. Your chosen agent and tools have their own access, availability, and
usage costs. Markdown instructions do not retrain a model, enforce compliance,
or guarantee autonomous success. Keep qualified review where the work needs it.

Templates and tools are MIT-licensed; public explanations are CC BY 4.0.
[License scope and attribution](NOTICE.md).

Created by [Dowanski](https://dowanski.com). More working ideas in the
[Reading Room](https://dowanski.com/reading-room).
