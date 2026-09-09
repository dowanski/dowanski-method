# Getting Started

## Choose the right material

The **Complete starter** is the default: QDI discovery plus an inactive library
of Light, Standard, and Governed DM foundations. Start with QDI; do not merge the
three foundations or ask the agent to preload the entire download.

The three **direct foundation** ZIPs are for experienced adopters who already
have sufficiently accepted project context, boundaries, and review criteria.
They omit QDI and do not grant implementation permission. If those foundations
are missing, use the complete starter instead.

The [v0.2.0 release](https://github.com/dowanski/dowanski-method/releases/tag/v0.2.0)
provides these assets (replace `<VERSION>` with `0.2.0`):

- `dowanski-method-complete-v<VERSION>.zip`
- `dowanski-method-light-v<VERSION>.zip`
- `dowanski-method-standard-v<VERSION>.zip`
- `dowanski-method-governed-v<VERSION>.zip`
- `SHA256SUMS.txt`

GitHub's automatically generated source archive is the maintainer repository,
not the ready-to-adopt starter. If using source, the adopter packet is under
[`starter/`](../starter/README.md). The root `AGENTS.md` is for maintainers.

## Establish a private working location

Read [Installation and Storage](../starter/INSTALLATION_AND_STORAGE.md) before
copying into an existing project. You can work in a local folder, in an approved
private repository path, or use the recommended hybrid: private raw discovery,
then distilled, accepted conclusions in the implementation repository.

Opening a private repository does not make every file safe to commit. Confirm
ignore rules, access, backups, and what may leave the machine. Never overwrite
existing `README.md` or `AGENTS.md` files just because names match.

## Begin and resume

Use the exact startup instruction in the [starter README](../starter/README.md).
The agent establishes boundaries, explains its context/usage discipline, offers
Guided or Grouped questioning, and asks for the idea in your own words.

You can stop and resume. The current position belongs in Current State; the
next eligible action belongs in Active Packet. A resumed agent follows the
router instead of rereading the complete interview history.

After discovery, review the blueprint and cleanup. Handoff generation, DM setup,
and implementation have distinct permissions. A useful next step may be more
discovery, a change of direction, deferral, or no build at all.

## Check what you downloaded

Compare the ZIP's SHA-256 hash with the manifest from the same verified release.
On macOS/Linux, a command such as `shasum -a 256 <archive.zip>` prints the hash;
on PowerShell, use `Get-FileHash <archive.zip> -Algorithm SHA256`.

A matching hash checks the bytes against that manifest. It is not a separate
signature or proof of the publisher's identity. Use the intended publisher and
release, inspect the files, and give the agent only the access it needs.
