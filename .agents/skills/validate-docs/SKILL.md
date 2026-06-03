---
name: validate-docs
description: >-
  Validate one or more specific vault documents against SPECS.md for structural
  correctness, writing quality, and substance. Use when the maintainer asks to
  check, validate, or review specific node file(s) — process, modality, stage,
  glossary, or company — or all .md files under Content/. Reports violations and
  proposes corrections; never edits without confirmation. Not for whole-vault
  invariant checks (use validate-vault).
---

Validate one or more vault documents against SPECS.md for structural correctness and writing quality.

**Input:** one or more vault-relative paths (e.g. `Content/Treatments/Processes/<stage>/<Process title>.md`), or `*` to validate all `.md` files under `Content/`.

---

## 0. Read authoritative sources first

Before examining any document, read these in full:

- `SPECS.md` — the authoritative rule set. Every check below is derived from it; if anything in this skill and SPECS.md conflict, SPECS.md wins.
- The content declaration (SPECS.md §1 names it and gives its path) — the live list of stages (spine order), modalities, and aliases. Called "the content declaration" below.
- The reference process node (SPECS.md §6 names it and gives its path) — the model of a well-written process to follow.

Do not skip or skim these. The checks in §§1–3 require knowing the declared stage and modality slugs, the live node list, and what "well-written" looks like in practice.

---

## 1. Structural checks (SPECS.md §§2–4, §8)

For each document, check every item that applies to its node type. Record violations precisely: quote the offending content, cite the SPECS.md rule, and state what the fix must be.

### 1.1 Frontmatter — all node types

- Exactly one `type/` tag present and valid (index / process / modality / stage / glossary / company). (Inv. 1)
- No unexpected keys for the node type (e.g., `next`/`feedback` only on process nodes). (§2.2, Inv. 15)
- No alias appears as a `modality/` tag — every modality tag must be explicit. (§4.4, Inv. 12)
- All `stage/` and `modality/` slug values are declared in the content declaration. (Inv. 4, Inv. 13)
- No filename contains illegal characters (/ \ : * ? " < > | # ^ [ ]). (§3)
- File sits in the correct folder for its node type. (§3)

### 1.2 Process nodes (additional)

- Exactly one `stage/` tag. (Inv. 2)
- At least one `modality/` tag. (Inv. 2)
- File is under `Content/Treatments/Processes/<stage_slug>/` where `<stage_slug>` matches the single stage tag. (Inv. 3)
- Every `next` and `feedback` target resolves to an existing file. (Inv. 5)
- `feedback` points backward (an earlier stage in the spine, or at least not forward); `next` points forward. (Inv. 6)
- Every `feedback` target shares at least one `modality/` tag with this node. (Inv. 16)
- Check for unforced node boundaries (Inv. 17): if this node has exactly one `next` successor, that successor has exactly one predecessor, and both carry identical `modality/` tag sets, they must differ in `stage/` tag. Flag if not.

### 1.3 Modality nodes

- Tags: `type/modality` and `modality/<self>` only. (§2.2)
- File under `Content/Treatments/Modalities/`. (§3)

### 1.4 Stage nodes

- Tags: `type/stage` and `stage/<self>` only. (§2.2)
- File under `Content/Treatments/Stages/`. (§3)

### 1.5 Glossary nodes

- Tag: `type/glossary` only. (§2.2)
- File under `Content/Glossary/`. (§3)

### 1.6 Company nodes

- Tag: `type/company` only — no `stage/` or `modality/` tags. (§2.2, Inv. 11)
- File under `Content/Companies/`. (§3)
- Every wikilink in the body resolves to an existing node file. (Inv. 11)

### 1.7 Cross-vault checks (when `*` is given)

- Node titles are unique across the vault. (§2.2)
- Stage and modality slugs are unique. (§2.2)
- Every `[[glossary term]]` link in any body has a matching `type/glossary` file. (Inv. 10)
- The Patient node carries every `modality/` tag declared in the content declaration. (Inv. 9)

---

## 2. Content checks (SPECS.md §§6–7)

These apply to the **body** of each document. The goal is not stylistic preference — it is whether the body fulfills the spec for its node type and serves the intended non-specialist reader.

### 2.1 Process body (§§6, 7.2)

- **Real mechanism, no analogies or metaphors.** Flag any sentence that substitutes an analogy ("like a lock and key") for a literal description of mechanism. Quote it.
- **Explain-or-glossary rule.** Every piece of field-specific jargon is either explained inline in plain words at the moment it appears, or linked to a glossary page. A bare unexplained jargon term is a violation. List each one found.
- **Glossary links on first use within the document.** If a term is linked once and then used again unlinked, that is fine. If a term is used before the link appears, flag it.
- **Glossary sufficiency.** For every `[[term]]` link, verify that the linked glossary file actually explains what the linking page defers to it. If the glossary body does not cover the concept the linking page relies on, flag it as a violation of Inv. 18.
- **Tools, instruments, and assays** are mentioned in context, not in a separate "tools" section.
- **No required section structure** — but the narrative must carry goal/method/hard-parts implicitly. Flag if the body reads like a list of facts with no through-line.
- **Modality coverage.** The body covers only the modalities tagged on the node. If modalities are tagged that the body never describes, or the body describes a modality not tagged, flag it.
- **Length.** Target under 1000 words. Note if substantially over, but do not flag length as a hard error — clarity beats brevity.
- **Substance accuracy.** For any mechanistic claim that can be verified against public scientific sources, note whether the claim is consistent with established knowledge. Flag claims that appear to contradict current consensus or that are too vague to be useful to the intended reader. Verify against sources, not memory (per AGENTS.md).

### 2.2 Modality body (§7.3)

- Part 1: plain-language overview of how the modality works — what the drug is, how it acts.
- Part 2: ordered list of the modality's nodes grouped by stage (stage order from the content declaration), each a wikilink.
- First node in the list is the root (no other node in the same modality points to it via `next`).
- The list matches what is derivable by following `next` through process nodes tagged with this modality.

### 2.3 Stage body (§7.4)

- Part 1: plain-language explanation of what this stage is — the question the industry is answering, and what "done" looks like.
- Part 2: ordered list of processes in this stage, each a wikilink.
- States the stage's fixed position in the spine.

### 2.4 Glossary body (§§6, 7.5)

- Covers: what the term is, how it works, why it matters in the industry.
- Complete enough to serve as a standalone explanation for every page that links to it (Inv. 18).
- Explain-or-glossary rule applies here too — glossary terms can link to other glossary terms; bare unexplained jargon is a violation.
- Links to external resources (high-level and primary literature) where present; note if absent.
- Substance accuracy: same standard as process bodies.

### 2.5 Company body (§7.6)

- Part 1: brief plain description of who the company is and what it focuses on.
- Part 2: list of plain wikilinks to process nodes (and optionally modality pages) with brief annotations.

### 2.6 Index body (§7.1)

- Links to all modality pages, all modality group aliases, and all stage pages.
- Stage order (root to Patient) is present and matches the content declaration.
- Pointers to Glossary and Companies.
- Brief legend: stage colors, what `next`/`feedback` mean, how to filter by modality/stage.

---

## 3. Substance verification (AGENTS.md: verify against sources, not memory)

For process and glossary bodies, identify every mechanistic claim. For each claim that is specific enough to verify, use web search to check it against current scientific consensus (peer-reviewed sources, established databases, or authoritative reviews). Do not rely on training-time knowledge alone — retrieve current sources.

Report:
- Claims verified and consistent with sources (brief note).
- Claims that could not be verified (too vague, or no good source found).
- Claims that contradict current consensus or are outdated: quote the claim, cite the conflicting source, and state what the correct mechanism is.

---

## 4. Per-document report

For each document validated, produce a report in this structure:

```
### <Filename> (<node type>)

**Structural violations**
- [RULE §X.Y / Inv. N] <quoted offending content> — <what must change>
  (none if clean)

**Writing / content violations**
- [§X.Y] <description of the problem> — <what must change>
  (none if clean)

**Substance issues**
- <claim quoted> — <what the sources say; cite source>
  (none if clean)
```

If a document is fully clean, say so explicitly.

---

## 5. Corrected version

For each document that has at least one violation:

1. Draft a corrected version of the full document.
2. Present it in a fenced code block labeled with the file path.
3. Do **not** write the corrected version to disk yet.
4. Wait for the maintainer to explicitly confirm acceptance of each corrected document before making any change. Accept one document at a time if multiple are being corrected.

On confirmation, replace the file contents with the corrected version. Then report which file was written.

---

## 6. What not to do

- Do not fix documents silently — always report, propose, wait.
- Do not change documents the maintainer has not confirmed.
- Do not invent new stages, modalities, or aliases. If a fix would require one, stop, flag it, and ask.
- Do not treat length as a hard blocker — only flag it as a note.
- Do not rewrite a body for style alone when the content is structurally and factually correct. The minimum correct fix is preferred.
