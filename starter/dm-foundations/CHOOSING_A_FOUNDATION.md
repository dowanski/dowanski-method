# Choosing a Foundation

Documentation Weight describes the amount of explicit control a project
currently needs. It is not a maturity badge or quality score.

## Light

Choose Light when all of these are true:

- one coherent outcome is active;
- the work is low-consequence and easy to reverse;
- one primary owner and one active writer are sufficient;
- dependencies and shared state are limited;
- local or directly inspectable proof is sufficient;
- no hard Governed trigger exists.

## Standard

Choose Standard when the project is expected to grow across several stages,
sessions, decisions, or contributors. It is the recommended default when Light
would force stable intent, changing truth, planning, decisions, debt, and
execution into one oversized record.

## Governed

Choose Governed when one hard trigger exists, including:

- identity, authentication, authorization, or tenant isolation;
- billing or financial action;
- sensitive or regulated data;
- destructive or difficult-to-reverse mutation;
- production migration or consequential provider change;
- incident response, security review, or uncertain source truth;
- concurrent writers affecting shared state;
- mandatory independent verification, rollback, or audit evidence.

## Mixed weight

A Standard project may open one Governed workstream without forcing every
ordinary project task to use the same controls. Reduce that workstream after the
trigger closes and its durable truth, decisions, evidence, and debt have
returned to the Main Set.

## Reconsider the choice when

Promote when consequences, dependencies, actors, uncertainty, shared state, or
proof burden grow. Reduce when the triggering condition closes and a smaller
route can preserve current truth safely.

When uncertain, stop before implementation and ask which harm the additional
control prevents. Add a record because it owns a real responsibility—not
because a larger template happens to contain it.
