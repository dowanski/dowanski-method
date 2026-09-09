# Release Checklist

Publication is a human-authorized maintainer operation, not a consequence of
passing tests. Apply this checklist to each proposed release.

1. Accept the exact source diff, public copy, security policy, license scope,
   version, and repository identity. Confirm that no private source history or
   sensitive material is included.
2. Set the approved version in `starter/VERSION` and reconcile the changelog,
   root release status, and release notes. Recheck the resulting source; do not
   reuse artifacts from another version.
3. Run `python3 tools/verify.py`, inspect its limits, and perform the necessary
   human review or agent exercise for any behavioral change.
4. Generate four archives with `python3 tools/package.py --output <new-directory>`.
   Keep that output outside the source repository. Verify the ZIPs and manifest.
5. Obtain explicit authority for repository creation, visibility, commit/push,
   version tag, and release publication. Preserve existing repositories.
6. Commit only the accepted source using the approved author identity. Do not
   import private planning history. Tag the exact reviewed commit.
7. Create a draft GitHub Release. Attach all four versioned ZIPs and
   `SHA256SUMS.txt`; include accurate notes and current evidence limitations.
8. Verify the draft asset selection, then publish only within granted authority.
   Enable the confirmed private security-reporting route before linking to it.
9. Download all public assets as a visitor. Compare hashes, inspect and extract
   them safely, and verify startup and selected-foundation routes again.
10. Only then activate exact download links and update the owner-approved
    profile or website. Those surfaces have their own publication authority.

Do not replace a published asset silently. Correct it through a reviewed new
version with an explanation. A checksum manifest is integrity evidence, not an
independent cryptographic signature of the publisher.
