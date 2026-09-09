# Local Packaging and Verification

Requirements: Python 3.10 or newer. Both tools use only the standard library;
no package installation, credentials, network, Git write, or publishing occurs.

From the repository root:

```sh
python3 tools/verify.py
python3 tools/package.py --output ../dowanski-method-review-assets
```

The output directory must be new, outside the source repository, and not reached
through a symbolic link. The packager refuses existing output; it never deletes
or replaces it. Choose a new directory for another saved build. Verification
uses disposable temporary directories and leaves the source unchanged.

## Source and reproducibility

`starter/` is the sole template source. `starter/VERSION` supplies the version.
`starter-files.json` is its reviewed path allowlist. When intentionally adding
or removing a template, update that sorted list in the same reviewed change.
An unlisted file—including hidden metadata—blocks packaging.

The complete archive preserves the starter's tree. Each direct archive contains
only its foundation plus VERSION, MIT license, and the direct-specific notice.
No private build records, validators, or maintainer instructions are included.

ZIPs use sorted paths, fixed timestamps/permissions, and stored (uncompressed)
entries to avoid compression-library differences. These small text packages
favor byte reproducibility over compression. The manifest lists SHA-256 hashes
of the four ZIPs. Matching hashes do not independently authenticate a publisher.

## Check boundaries

The verifier checks inventory, path safety, source links, selected written
authority/routing invariants, unchanged rebuilds, clean extraction, direct/
bundled parity, base installation, notice inclusion, and common accidental
private-data patterns. Fault injection confirms selected checks fail closed.

It does not call an AI model or prove that an agent will obey the written rules.
It is not an exhaustive secret scanner, legal review, or security certification.
Human semantic review remains required for instruction changes. See
[verification and limits](../guides/verification.md).
