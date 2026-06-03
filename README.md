# Biotech Process Map

An [Obsidian](https://obsidian.md) vault that maps the **biotech treatments industry as a directed graph of technical processes** — the real steps that turn a biological idea into a medicine a patient receives. Every page is written to stand on its own and assumes no field jargon.

## Who it's for

This map is for a curious **non-specialist** — someone exploring which part of the industry to work in, *not* someone already in the field. You don't need a degree in the subject or any prior experience. The pages go into real detail and real mechanism, but nothing assumes you already know the terminology: any term that needs explaining is either explained on the spot in plain words or links to a glossary page that explains it from the ground up.

The relationships *between* steps are deliberately simplified to keep the overall shape of the industry graspable; the steps themselves are explained in depth.

## How the vault is structured

The vault is a graph. Each node is a single page, and there are a few kinds of node:

- **Process** — one step in a pipeline (the bulk of the vault). Steps are wired together with two kinds of edge:
  - **`next`** — forward progression: this step feeds the next one. Following `next` from any step eventually reaches the patient.
  - **`feedback`** — an iteration loop back to an earlier step (for example, optimization looping back to design).
- **Modality** — one *kind* of drug (a small molecule, an antibody, a gene therapy, …). Each modality has its own pipeline from a shared start (**Find a target**) to a shared end (the **Patient** node), and shares steps with other modalities wherever the underlying work is genuinely the same. The map currently covers **17 modalities**.
- **Stage** — where a step sits along the pipeline. There are **9 stages** in a fixed order, from `target_discovery` through to `patient`. Every process belongs to exactly one stage.
- **Glossary** — a field-specific term or technique, explained from the fundamentals.
- **Company** — a card for one company, linking to the processes it actually performs.

The front door is [Content/Index.md](Content/Index.md): it lists every stage (in order), every modality, the glossary and companies folders, and a legend. **Start there.**

Folders (`Treatments/Processes/<stage>/`, `Treatments/Modalities/`, `Treatments/Stages/`, `Glossary/`, `Companies/`) exist only for human browsing — the software navigates by tags and edges, not folders.

## Using Obsidian with this vault

Open the `Content/` folder as an Obsidian vault. A few features carry most of the experience:

- **Walk a pipeline.** The [Extended Graph](https://github.com/ElsaTam/obsidian-extended-graph) plugin colors edges by type (typed links): `next` and `feedback` render in different colors, so the forward spine from **Find a target** toward **Patient** stands out at a glance. `feedback` is shown by default; Extended Graph's link-type filtering can toggle it off to leave only the clean forward spine.
- **Explore by stage.** Open **Graph view**. Nodes are colored by stage (see below), so you can see at a glance where any step sits in the pipeline.
- **Filter by modality or stage.** A tag query `tag:#modality/<slug>` surfaces that modality's *entire* pipeline — research through delivery — because shared steps carry the tag too. `tag:#stage/<slug>` shows one stage across all modalities. Combine the two for a precise subgraph.
- **Look up a term.** Open a glossary page; its **backlinks** list every process that uses it — a live answer to "where in the industry is this used?"
- **Find companies.** A process node's backlinks (filtered to `type/company`) show the companies that perform that step; open a company card to see everything it does.

By default, modality, stage, glossary, and company nodes are hidden so you can focus on the processes themselves.

## Stage coloring

The 9 stages run as a fixed spine from research to patient, and the intended scheme colors the Graph view as a **gradient along that spine**, root → patient:

| # | Stage | Suggested color |
|---|---|---|
| 1 | Target discovery | red |
| 2 | Lead discovery | orange |
| 3 | Design optimization | amber |
| 4 | Formulation and delivery | yellow |
| 5 | Preclinical studies | green |
| 6 | Manufacturing | teal |
| 7 | Clinical trials | blue |
| 8 | Regulatory approval | indigo |
| 9 | Patient | violet |

The color then tells you instantly how far along the pipeline a step is. Each stage is a Graph-view **group** with the query `tag:#stage/<slug>`.

> **Note:** the per-stage Graph-view groups are configured in the vault (one group per stage, via Extended Graph's color groups), so stages are already colored. Their current colors do **not** yet follow the gradient above, however — that gradient remains the intended target (see TODO).

## TODO

Setup that still needs doing in Obsidian:

- **Tune stage colors.** The per-stage Graph-view groups exist (one per stage, `tag:#stage/<slug>`), but their colors are currently arbitrary — update them to follow the gradient in the table above.

---

## For developers / maintainers

The vault is governed by a small set of authoritative documents and a set of skills. Before making any change to the content, read them in this order:

- **[AGENTS.md](AGENTS.md)** (also reachable as `CLAUDE.md`, a symlink) — where to look and how to behave while working in the vault: ask before non-trivial changes, explain reasoning, don't invent vocabulary, prefer the smallest change. It defers to SPECS.md for everything about the vault itself.
- **[SPECS.md](SPECS.md)** — the authoritative rules: the six node types, frontmatter/tag conventions, the `next`/`feedback` edge model, folder layout, granularity and glossary rules, writing style, and the §8 invariant checklist. **Read it in full before the first edit.**
- **[Content/Index.md](Content/Index.md)** — the *content declaration*: the actual stages (in spine order), the 17 modalities, and the modality-group aliases. SPECS.md states the rules; Index.md declares the concrete content those rules apply to.
- **[MODALITIES-AND-PROCESSES.md](MODALITIES-AND-PROCESSES.md)** — the structural target for the treatments branch: the full set of modalities and process nodes with the `modality/` tags each carries. A regeneration reference, not a content spec — bodies follow SPECS.md.

### Skills

Vault-specific skills live under [.agents/skills/](.agents/skills/). Each names the files it needs by *role* (e.g. "the content declaration") and resolves the path through SPECS.md:

- **add-company** — create a company card, mapping the company's activities to existing process nodes only.
- **add-glossary-term** — create a glossary entry and link its first use across the vault.
- **update-graph** — apply a validated graph change: create/edit/move/rename/split/merge process nodes, rewire `next`/`feedback` edges, and propagate the ripples.
- **validate-docs** — validate specific documents against SPECS.md for structure, writing quality, and substance.
- **validate-vault** — run the whole-vault §8 invariant checks via [.agents/scripts/validate_vault.py](.agents/scripts/validate_vault.py), then the manual glossary-sufficiency review.
