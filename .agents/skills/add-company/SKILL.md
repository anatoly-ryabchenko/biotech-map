---
name: add-company
description: >-
  Create a company card node under Content/Companies/ for a named company:
  research it from current sources, map its activities to existing process
  nodes only, write the card, and report gaps. Use when the maintainer asks to
  add or create a company in the vault. Does not create new process nodes or
  invent node titles.
---

Create a company card in the vault for a given company name.

Input: company name (from the user's message invoking this skill).

---

## 0. Before anything else

Read these files before researching or writing anything:

- `SPECS.md` — authoritative for every rule below; if anything here and SPECS.md conflict, SPECS.md wins.
- The content declaration (SPECS.md §1 names it and gives its path) — the live list of stages (in spine order), modalities, and aliases.

Then inventory the vault's process nodes: list every `.md` file under `Content/Treatments/Processes/`. This is the complete set of nodes a company card may link to. Do not assume any node exists — verify by listing the directory.

---

## 1. Hard stops — report and do nothing if any of these apply

- The company name is ambiguous (e.g., a common word with multiple unrelated companies). Ask the user to clarify before proceeding.
- A company card with the same name already exists in `Content/Companies/`. Report this; do not overwrite without explicit instruction.
- The company does not clear the inclusion bar in SPECS.md §7.6 ("Which companies earn a card"). After researching (§2), confirm it is an established global player, an emerging leader (venture-backed, Series A or later, with evidence), or a notable service company. If it does not qualify, report which test it fails and do not write a card without explicit instruction.

---

## 2. Research the company

Use web search to establish, from current sources:

1. **What the company is** — founding, headquarters, focus area, key programmes or products, and broad therapeutic/technology approach. Keep this factual and lay-readable; do not copy marketing language.
2. **Its scale** — maturity (public, or private + latest funding round), approximate headcount, and HQ, for the `Scale:` line (§4). Keep figures coarse and note the year.
3. **What processes it performs** — map its actual activities to the process nodes you inventoried in §0. Be specific: if the company does antibody discovery, find the node titled `Antibody discovery`; if it runs clinical trials, find the relevant clinical-trials node(s). Cross-reference modality pages and stage pages when helpful.

Use at least two independent sources (company website + a reputable secondary source such as a news article, regulatory filing, or industry database). Note the sources you used.

---

## 3. Map to existing nodes only

For each company activity you identified, check whether a corresponding process node exists in the vault (from the inventory in §0).

- **If a node exists:** include it in the card (§4).
- **If no node exists but the company clearly performs that process:** add it to the gap report (§5). Do not create a new process node; do not link to a non-existent node.

The test is: does the company's activity correspond to a process the vault currently models? A rough match is not enough — the activity must fall within the scope of an existing node, not merely be adjacent to it.

---

## 4. Write the company card

File path: `Content/Companies/<Company name>.md`

The filename is the company's common name exactly as it would appear in a wikilink from other pages.

Frontmatter:

```yaml
---
tags:
  - type/company
---
```

No `stage/` or `modality/` tags. No `next` or `feedback` keys.

Body structure (per SPECS.md §7.6):

1. **What it is** — two to four sentences: who they are, where they are based, what they focus on, and any key approved products or notable programmes. Plain language, factual, no superlatives.

2. **Scale** — an explicit `Scale:` line right after "what it is" (§7.6): maturity (public, or private + latest funding round), approximate headcount, and HQ, with the year. Coarse figures only. Example:

```
**Scale:** Private, Series C · ~250 staff · HQ Cambridge, UK (as of 2026)
```

3. **What it does in the map** — a plain list of wikilinks to the process nodes it performs, each annotated with a short phrase (one clause) describing what the company does at that step. Format:

```
- [[Process node title]] — what the company does here
- [[Process node title]] — what the company does here
```

Use the exact node filename as the wikilink target (case-sensitive). Do not group by stage or modality in the file — a flat list is correct; Obsidian's backlinks do the grouping.

---

## 5. Gap report

After writing the card, output a plaintext report to the user listing any processes the company clearly performs that have no corresponding node in the vault. For each gap, name the activity and state which stage it would fall under. Do not invent node titles — describe the activity in plain words. Example:

```
GAP  Preclinical studies — in vivo toxicology studies in non-human primates (no general GLP-tox node for this species scope currently exists)
GAP  Manufacturing — continuous manufacturing process for small molecules (no node for continuous vs batch distinction)
```

If there are no gaps, say so explicitly.

---

## 6. Output

After completing the card, output:

```
CREATED   Content/Companies/<Company name>.md
```

Then the gap report (§5).

State the sources used for the research.
