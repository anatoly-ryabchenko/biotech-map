---
tags:
  - type/index
---

# Biotech Process Map

This vault maps the **biotech treatments industry as a directed graph of technical processes** — the real steps that turn a biological idea into a medicine a patient receives. It is written for a curious **non-specialist**: every page stands on its own and assumes no field jargon.

Each **process** node is one step in a pipeline. Steps are wired together with `next` (forward progression) and `feedback` (an iteration loop back to an earlier step). A **modality** is one kind of drug (a small molecule, an antibody, a gene therapy…); each modality has its own pipeline from the shared start to the shared end, sharing steps with other modalities wherever the work is genuinely the same.

## Start here

Every modality's pipeline begins at the same root node and ends at the same terminal node:

- **[[Find a target]]** — the root node, the single entry point to the graph.
- **[[Treatment & follow-up]]** — the terminal node, the shared end point where every pipeline finishes (treatment delivered, then watched over time).

From there, follow `next` edges forward through the stages from [[Find a target]] until you reach [[Treatment & follow-up]].

## How to read the map

- **Walk a pipeline.** Extended Graph colors edges by type, so `next` and `feedback` render in different colors — follow the `next` color forward from [[Find a target]] toward [[Treatment & follow-up]]. `feedback` is shown by default; its link-type filtering can toggle `feedback` off to leave only the clean forward spine.
- **Explore by stage.** Open Graph view; nodes are colored by stage (one graph group per stage), so you can see at a glance where any step sits in the pipeline.
- **Filter by modality or stage.** A tag query `tag:#modality/<slug>` surfaces that modality's *entire* pipeline (shared steps carry the tag too). `tag:#stage/<slug>` shows one stage across all modalities. Combine them for a precise subgraph.
- **Look up a term.** Open a glossary page; its backlinks list every process that uses it.
- **Find companies.** A process node's backlinks (filtered to `type/company`) show the companies that perform that step; a company card shows everything it does.

By default, modality, stage, glossary, and company nodes are hidden so you can focus on the processes themselves.

## Stages

The pipeline runs through nine stages, in this fixed order from root to patient. Each links to the page that authoritatively defines its `stage/` tag.

| # | Stage | `stage/` slug |
|---|---|---|
| 1 | [[Target discovery]] | `target_discovery` |
| 2 | [[Lead discovery]] | `lead_discovery` |
| 3 | [[Design optimization]] | `design_optimization` |
| 4 | [[Formulation and delivery]] | `formulation_and_delivery` |
| 5 | [[Preclinical studies]] | `preclinical_studies` |
| 6 | [[Manufacturing]] | `manufacturing` |
| 7 | [[Clinical trials]] | `clinical_trials` |
| 8 | [[Regulatory approval]] | `regulatory_approval` |
| 9 | [[Patient]] | `patient` |

## Modalities

The seventeen kinds of drug the map covers. Each links to the page that authoritatively defines its `modality/` tag.

| # | Modality | `modality/` slug |
|---|---|---|
| 1 | [[Small molecule]] | `small_molecule` |
| 2 | [[Peptide]] | `peptide` |
| 3 | [[Protein degrader]] | `protein_degrader` |
| 4 | [[Oligonucleotide]] | `oligonucleotide` |
| 5 | [[mRNA]] | `mrna` |
| 6 | [[Antibody]] | `antibody` |
| 7 | [[Conjugated biologic]] | `conjugated_biologic` |
| 8 | [[Therapeutic protein]] | `therapeutic_protein` |
| 9 | [[De novo]] | `de_novo` |
| 10 | [[Gene therapy]] | `gene_therapy` |
| 11 | [[Gene editing]] | `gene_editing` |
| 12 | [[Cell therapy]] | `cell_therapy` |
| 13 | [[Regenerative]] | `regenerative` |
| 14 | [[Oncolytic virus]] | `oncolytic_virus` |
| 15 | [[Vaccine]] | `vaccine` |
| 16 | [[Radiopharmaceutical]] | `radiopharmaceutical` |
| 17 | [[Microbiome]] | `microbiome` |

## Modality groups (aliases)

Aliases are documentation shorthand for sets of modalities that share enough steps to be worth naming together. They are used only when talking *about* the map — files never contain them; every `modality/` tag in a file is explicit.

| Alias | Modalities |
|---|---|
| **Advanced therapies** | `gene_therapy`, `gene_editing`, `cell_therapy`, `regenerative`, `oncolytic_virus` |
| **Protein biologics** | `antibody`, `de_novo`, `therapeutic_protein` |
| **Small molecules & degraders** | `small_molecule`, `protein_degrader` |
| **Nucleic acids** | `mrna`, `oligonucleotide` |

## Glossary and companies

- **Glossary** — field-specific terms and techniques, each explained from the ground up, in the `Glossary/` folder.
- **Companies** — one card per company, linking to the processes it performs, in the `Companies/` folder.

## Legend

- **`next`** — forward progression: this step feeds the next one. Following `next` from any process eventually reaches [[Treatment & follow-up]].
- **`feedback`** — an iteration loop back to an earlier step in the same modality (e.g. optimization looping back to design). Hide it to see the clean forward spine.
- **Stage colors** — each stage is a graph-view group (`tag:#stage/<slug>`); coloring runs as a gradient along the spine, root → patient:

| Stage | Suggested color |
|---|---|
| Target discovery | red |
| Lead discovery | orange |
| Design optimization | amber |
| Formulation and delivery | yellow |
| Preclinical studies | green |
| Manufacturing | teal |
| Clinical trials | blue |
| Regulatory approval | indigo |
| Patient | violet |

---

The rules, conventions, and constraints this vault obeys are defined in `SPECS.md` at the repository root.
