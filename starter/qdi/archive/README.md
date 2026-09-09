# QDI Archive

Status: Inactive support route

Store closed or superseded QDI packets here only when their history remains
useful for provenance, resumption, or explaining a changed decision.

## Rules

- Update the active source before archiving its predecessor.
- Remove archived files from the active router.
- Prefix archived files with a date or stable sequence identifier.
- State what superseded or closed the record.
- Preserve an indexed record's stable ID and update its path and status in
  `../QDI_RECORD_INDEX.md`.
- Never reuse an archived or removed ID.
- Preserve a tombstone when another record still references an approved removed
  ID.
- Do not alter accepted historical evidence merely to match current language.
- Do not read this directory during ordinary continuation unless
  `../CURRENT_STATE.md` names a specific reason and file.
- Prefer version history when a separate archived copy adds no decision value.
