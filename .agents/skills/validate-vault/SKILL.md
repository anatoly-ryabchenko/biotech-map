---
name: validate-vault
description: >-
  Run the whole-vault SPECS.md §8 invariant checks via the validation script,
  then do the manual glossary-sufficiency (Inv. 18) review. Use only when the
  maintainer explicitly asks to validate the entire vault. Read-only — never
  edits files. Not for checking the prose or substance of an individual
  document (use validate-docs).
---

Check all vault files against SPECS.md §8 invariants (and every other SPECS.md constraint that is statable as pass/fail). Run only when the maintainer asks. Read-only — never edit vault files.

---

## How to run

From the repository root (the directory containing `Content/`):

```
python3 .agents/scripts/validate_vault.py
```

The script checks invariants 1–17 automatically and prints one line per invariant: PASS, or FAIL with the specific violations (file + what is wrong). Invariant 18 (glossary sufficiency) is semantic and listed separately as a set of links to review manually.

---

## INV 18 — manual check

After running the script, for each `[[glossary term]]` link it prints:

- Open the glossary file.
- Open the linking file.
- Check that the glossary body actually explains the concept the linking page defers to it — the thing the linking page does not explain inline.
- If the glossary body does not cover that concept, report it as a violation: quote the linking sentence, state what concept is deferred, and state what is missing from the glossary.

---

## Reporting

- Per invariant: state the invariant number and text, then PASS or FAIL.
- On FAIL: list each violation on its own line — file path and what is wrong. No filler.
- INV 18: for each glossary link reviewed, state PASS or flag the gap.
- At the end: overall PASS if all clean, or a count of violations if not.
