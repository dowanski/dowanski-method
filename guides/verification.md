# Verification and Limits

## What a local check can establish

Run `python3 tools/verify.py` from the repository root. It checks the starter
file inventory, Markdown paths, startup and phase routes, selected authority
invariants, reproducible packaging, license inclusion, and extracted
source/download equivalence. It also injects known defects into disposable
copies and confirms that the intended checks reject them.

The checker runs locally with Python's standard library. It does not call a
model, upload project information, or grant access to another repository.
Details are in [the tool guide](../tools/README.md).

## Human and agent evidence

Development included isolated, fictional Light, Standard, and Governed project
exercises, targeted repairs, and resumption checks. Those observations informed
the templates. Private transcripts and source-project records are not included.

The later routing/compression revision and shared continuing controls have
structural, fault-injection, and local scenario evidence. They have **not**
received a new independent-agent run. Do not infer independent validation of
every current instruction from the earlier exercises.

## What this does not prove

- Identical behavior across models, hosts, tools, or projects.
- Successful unattended delivery or a particular quality score.
- A security certification or replacement for a project-specific review.
- Actual token savings, a model benchmark, or an account-usage guarantee.
- That every semantic contradiction can be detected automatically.
- That a proposed workflow has human approval or permission to act.

The files guide compatible agents; they are not executable enforcement. Start
with bounded work, inspect decisions and output, and strengthen the controls
your project needs. Report a failure with the version, file, expected behavior,
and a sanitized description through [the feedback process](../CONTRIBUTING.md).
