---
tags:
  - type/glossary
---
A _CRISPR screen_ is a way to test what thousands of genes do, all at once, by switching each one off (or on) across a large population of cells and seeing which changes matter for some outcome. It turns the question "which genes are important for this process?" from a guess into a ranked, experimental answer.

It builds on [[CRISPR|CRISPR]], the tool that can be aimed at any gene by a matching guide RNA. To run a screen, researchers make a _library_ of tens of thousands of guides — enough to target every gene in the genome, several guides each — and deliver it into a large pool of cells so that each cell takes up one guide and so has one gene disabled. The whole pool is then put under a test that reflects the biology of interest: which cells survive a drug, which grow faster, which switch on a disease marker. Afterward the cells that did the interesting thing are collected and their guides read out by sequencing — and guides that end up over- or under-represented reveal exactly which genes, when disrupted, caused the effect. Variants of the technique don't cut the gene but _silence_ it (CRISPRi) or _activate_ it (CRISPRa) instead.

In target discovery, a CRISPR screen is a powerful, unbiased way to find candidate targets: disable every gene in a disease-relevant cell model and see which ones the disease process depends on. It is also used to confirm that acting on a chosen target really changes the disease behaviour, and to find genes that make a tumour resistant to a drug. Its main limits are that the cell test must genuinely capture the disease, and that disabling a gene in a dish does not always predict what blocking its protein will do in a patient. The genome-scale human CRISPR knockout screen was established by Shalem and colleagues in 2014.

## External resources
- [Shalem et al., "Genome-scale CRISPR-Cas9 knockout screening in human cells," *Science* (2014)](https://www.science.org/doi/10.1126/science.1247005) — the foundational demonstration of genome-wide CRISPR screening to find the genes responsible for a chosen cellular outcome.
