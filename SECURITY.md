# Security Policy

The distribution contains documentation templates and local packaging and
verification tools. It does not grant system access, execute project work, or
provide a hosted service.

## Reporting

When the public GitHub repository is created, enable GitHub private
vulnerability reporting before inviting security reports. Until that private
route is confirmed, contact `dowanski@pm.me` with a minimal description and no
credentials, private keys, customer data, or unnecessary exploit material.

Do not open a public issue for a vulnerability that could expose a real system
or user.

## Scope

Useful reports may include:

- a packaging script behavior that could include unintended files;
- a template instruction that encourages unsafe authority expansion;
- a secret-handling or privacy defect in the published templates;
- a path, archive, or provenance leak in an official release artifact.

Project-specific implementation failures are outside this repository's security
scope unless they are directly caused by an unchanged official template.

## Safe-use reminder

These templates do not replace a project-specific threat model, security
review, access-control design, privacy assessment, or release decision.
