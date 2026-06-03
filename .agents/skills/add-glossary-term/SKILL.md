---
name: add-glossary-term
description: >-
  Create a glossary entry for a term and link its first use across the vault.
  Applies the SPECS.md §4.2 test for whether the term deserves a page,
  researches real mechanism from current sources, writes the page, and links
  the first occurrence in each existing file. Use when the maintainer asks to
  add or define a glossary term.
---

Create a glossary entry for a given term, link it on first use across the vault.

Input: term name (from the user's message invoking this skill).

---

## 0. Before anything else

Read:

- `SPECS.md` — authoritative; wins on any conflict with this skill.
- The content declaration (SPECS.md §1 names it and gives its path) — the stage and modality list.

Inventory existing glossary entries: list every `.md` file under `Content/Glossary/`. If an entry for this term already exists (compare case-insensitively), report its path and stop — do not overwrite without explicit instruction.

---

## 1. §4.2 test — does this term deserve a page?

Apply the SPECS.md §4.2 criteria in order. State the result of each test.

**Test A — general reader test.** If the term is something a general reader already knows — DNA, gene, protein, cell, virus, bacteria, molecule, RNA in its generic sense — it fails. The exception is a term the general reader knows by name but not by mechanism, where that mechanism is important enough to warrant a standalone explanation (e.g., Clinical Trials).

**Test B — field-specific and important.** The term must be field-specific (not general scientific knowledge) and a key detail of at least one process in the vault.

**Test C — recurrence or depth.** The term must either recur across processes, or require deeper explanation than fits inline in a single process body.

If the term fails any test, output:

```
SKIP  <term>
Reason: <one sentence giving the specific reason it fails §4.2>
```

Then stop. The maintainer may override by replying "proceed anyway" — if they do, continue from §2 without re-running the test.

If the term passes, name the criteria it meets and continue.

---

## 2. Research the term

Use web search to establish, from current sources:

1. **What the term is and how it works** — real mechanism. The reader is a non-specialist who can handle real detail but knows no field jargon; do not flatten mechanism into analogy.
2. **Why it matters in the biotech industry** — where it appears in development pipelines or clinical practice, and why it is used rather than alternatives.
3. **External resources** — find sources meeting the canonical bar in SPECS §7.5 *External resources*: the best on-ramp (course/lecture/video by a recognized authority) and the foundation (the canonical, highly-cited primary source). Prefer freely accessible sources; record URLs and titles. If nothing clears the bar for a tier, do not substitute a weak link — omit that tier.

Use at least two independent sources. Note the sources you used.

---

## 3. Write the glossary page

File path: `Content/Glossary/<Term>.md`

The filename is the term's canonical English name exactly as it should appear in wikilinks — use the standard spelling, singular unless the term is conventionally plural, no abbreviation unless the abbreviation is the recognized term. Avoid characters illegal in Obsidian filenames: `/ \ : * ? " < > | # ^ [ ]`.

Frontmatter:

```yaml
---
tags:
  - type/glossary
---
```

Body (per SPECS.md §7.5 and §6):

Write a single flowing explanation covering what the term is, how it works, and why it matters in the industry. Use the §6 voice: plain language, real mechanism, no analogies or metaphors, no jargon without immediate plain-language explanation. One flowing narrative by default; add section headings only if the content genuinely requires them. Write as long as clarity requires — never truncate. Meet the SPECS §7.5 *Substance* bar: name real methods/criteria rather than gesturing at them, use no circular or self-referential definitions, and build a hard concept up from the fundamentals a newcomer needs first.

- Link other glossary terms (from the inventory in §0) on their first appearance in this body, using `[[Term]]`.
- Format the **External resources** section exactly as SPECS §7.5 specifies (fixed label, on-ramp and foundation tiers, omit a tier when nothing clears the bar).

---

## 4. Update body links in existing pages

Search every `.md` file under `Content/` (recursively, excluding the file you just created) for occurrences of the term. Search case-insensitively and also for common plural/singular variants (e.g., if the term is "lipid nanoparticle", also search "lipid nanoparticles").

For each file that contains a match:

1. Check whether the term is already linked anywhere in the file — as `[[Canonical Term]]` or `[[Canonical Term|display text]]`.
2. If it is already linked, skip this file (no change needed).
3. If it is not yet linked, find the first plain-text occurrence in the body (after the frontmatter, not inside an existing wikilink). Replace that first occurrence with a wikilink:
   - Exact match: `[[Canonical Term]]`
   - Case or plural variant: `[[Canonical Term|original text]]` — this preserves the original wording while linking to the correct file.
4. Do not touch any other occurrence in the same file.

---

## 5. Output

After completing all work, output:

```
CREATED   Content/Glossary/<Term>.md
LINKED    <file path> — first use of "<matched text>" linked
LINKED    <file path> — first use of "<matched text>" linked as [[<Canonical Term>|<matched text>]]
```

If no existing files needed linking, say so explicitly.

State the sources used in §2.
