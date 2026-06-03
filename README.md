# Biotech Process Map

An [Obsidian](https://obsidian.md) vault that maps the **biotechnology industry as a directed graph of technical processes**. The focus is on R&D, and on the processes themselves — sometimes trading the full complexity of how processes relate to one another in favor of clarity. Each page in the core graph gives you an overview of a process: its steps and difficulties, without hiding critical details, but explaining them instead. Besides process pages, there are also pages giving an overview of drug types (modalities), R&D stages, glossary terms, and companies.

The map serves two audiences equally: people already in the industry who want a bird's-eye view of the whole landscape, and curious newcomers approaching it for the first time. Nothing assumes prior knowledge of the terminology or the industry. Any term that needs explaining is either defined on the spot in plain language or linked to a glossary page that builds it up from the ground.

## How the vault is structured

You can think of the vault as a graph (in fact, it can be visualized as one with Obsidian). Each node is a single page, and there are a few kinds of node:

- **Process** — one step in a pipeline (the bulk of the vault). Steps are wired together with two kinds of edge:
  - **`next`** — forward progression: this step feeds the next one in the R&D chain. Following `next` from any step eventually reaches the patient.
  - **`feedback`** — an iteration loop back to an earlier step (for example, preclinical trials looping back to design).
- **Modality** — one *kind* of drug (a small molecule, an antibody, a gene therapy, …). Each modality has its own pipeline from a shared start (**Find a target**) to a shared end (the **Patient** stage node), and shares steps with other modalities wherever the underlying work is genuinely the same. The map currently covers **17 modalities**.
- **Stage** — where a step sits along the pipeline. Every process belongs to exactly one stage.
- **Glossary** — a field-specific term or technique, explained from the fundamentals.
- **Company** — a card for one company, linking to the processes it actually performs.

The front door is [Content/Index.md](Content/Index.md): it lists every stage (in order), every modality, the glossary and companies folders, and a legend.

## Installation

1. Clone this repo:
```
git clone https://github.com/anatoly-ryabchenko/biotech-map
```
2. Install [Obsidian](https://obsidian.md/download)
3. Open Content folder as an Obsidian Vault.

## How to use it

*Graph View.*
To look at the map as a graph, you can open Obsidian Graph View.
By default, the graph is filtered to only show processes and not other types of nodes.
Each **node** in the graph is colored by the stage. Besides, `next` graph **edges** are colored green and `feedback` graph edges are colored red.

There are several common and useful ways you can use the graph view:
- **Explore by stage.** Since nodes are colored by stage, you can see at a glance where any step sits in the pipeline.
- **Filter by modality or stage.** A tag query `tag:#modality/<slug>` surfaces that modality's *entire* pipeline — research through delivery — because shared steps carry the tag too. `tag:#stage/<slug>` shows one stage across all modalities. Combine the two for a precise subgraph.

*Traversing the map.*
To find the textual summary of the vault structure (with links), open Index.md document. 
There, you can find the root node(s) for all modalities (types of drugs) which is the first step in its R&D process.
Additionally you can find lists of modalities and stages, each of which in itself is an important document to read.
Otherwise, you can open search (cmd+F on MacOS / ctrl+F on Windows) and find a topic you're interested in.

There are several common and useful ways in which you can traverse the map:
- **Walk a pipeline.** Each process node (except the "patient" stage node) contains at least a single `next` link - you can start at the root or a document you are interested in and follow `next` to study the R&D process of a single modality (drug type). Use backlinks if you want to go to the direction of the root.
- **Look up a term.** Open a glossary page; its **backlinks** list every process that uses it — a live answer to "where in the industry is this used?"
- **Find companies.** A process node's backlinks (filtered to `type/company`) show the companies that perform that step; open a company card to see everything it does.

---

## For developers / maintainers

The content inside the vault is mostly AI generated, however which content to generate is deduced by following some rules described in this vault. 

The vault is governed by a small set of authoritative documents and a set of skills. Before making any change to the content, read them in this order:

- **[AGENTS.md](AGENTS.md)** (also reachable as `CLAUDE.md`, a symlink) — where to look and how to behave while working in the vault: ask before non-trivial changes, explain reasoning, don't invent vocabulary, prefer the smallest change. It defers to SPECS.md for everything about the vault itself.
- **[SPECS.md](SPECS.md)** — the authoritative rules: the six node types, frontmatter/tag conventions, the `next`/`feedback` edge model, folder layout, granularity and glossary rules, writing style, and the invariant checklist. **Read it in full before the first edit.**

## Skills

Vault-specific skills live under [.agents/skills/](.agents/skills/). Each names the files it needs by *role* (e.g. "the content declaration") and resolves the path through SPECS.md:

- **add-company** — create a company card, mapping the company's activities to existing process nodes only.
- **add-glossary-term** — create a glossary entry and link its first use across the vault.
- **update-graph** — apply a validated graph change: create/edit/move/rename/split/merge process nodes, rewire `next`/`feedback` edges, and propagate the ripples.
- **validate-docs** — validate specific documents against SPECS.md for structure, writing quality, and substance.
- **validate-vault** — run the whole-vault §8 invariant checks via [.agents/scripts/validate_vault.py](.agents/scripts/validate_vault.py), then the manual glossary-sufficiency review.

## TODO

- [x] Agent SPECS.md with vault rules
- [x] Agent skills for vault manipulation
- [x] Initial Map (Pharma)
- [ ] Diagnostics
- [ ] Non-pharma treatments
- [ ] Generated content polishing