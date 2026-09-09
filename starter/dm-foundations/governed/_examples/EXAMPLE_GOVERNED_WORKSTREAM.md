# Fictional Example — Permission Migration

Status: Example only; never active authority  
Fictional project: Harbor Inventory

## Trigger

The project is replacing one shared administrative role with tenant-scoped
roles. Incorrect behavior could expose one fictional workspace’s records to
another, and the migration changes shared database state.

Selection: Governed workstream inside an otherwise Standard product.

## Packet sequence

1. Verify the existing schema, policy behavior, and recoverable baseline.
2. Accept the new role and tenant contract.
3. Prepare the additive migration and negative tests locally.
4. Independently review tenant boundaries and rollback evidence.
5. Obtain owner acceptance of the preserved candidate.
6. Authorize shared migration and release separately.
7. Verify the live result and reduce the temporary governed route.

## Boundary

The workstream may prepare and test an additive candidate locally. It may not
run a shared migration, alter billing, change customer content, or deploy
without separate authority.

## Evidence

Positive-path tests are insufficient. The evidence contract includes wrong-
tenant, wrong-role, replay, conflicting-state, and rollback cases.

## Lesson

The documentation is heavier because identity, tenant isolation, shared state,
and recovery make ambiguity consequential—not because the feature is prestigious.

