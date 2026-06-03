---
tags:
  - type/process
  - stage/target_discovery
  - modality/small_molecule
  - modality/peptide
  - modality/protein_degrader
  - modality/oligonucleotide
  - modality/mrna
  - modality/antibody
  - modality/conjugated_biologic
  - modality/therapeutic_protein
  - modality/de_novo
  - modality/gene_therapy
  - modality/gene_editing
  - modality/cell_therapy
  - modality/regenerative
  - modality/oncolytic_virus
  - modality/vaccine
  - modality/radiopharmaceutical
  - modality/microbiome
next:
  - "[[Hit discovery (small molecule)]]"
  - "[[Degrader design (protein degrader)]]"
  - "[[Peptide design & synthesis (peptide)]]"
  - "[[Oligonucleotide design (oligonucleotide)]]"
  - "[[mRNA construct design (mRNA)]]"
  - "[[Antibody discovery]]"
  - "[[Therapeutic protein discovery & engineering]]"
  - "[[In silico protein design]]"
  - "[[Transgene & cassette design (gene therapy)]]"
  - "[[Guide & editor design (gene editing)]]"
  - "[[CAR-TCR construct design (cell therapy)]]"
  - "[[Cell source & differentiation design (regenerative)]]"
  - "[[Oncolytic virus design (oncolytic virus)]]"
  - "[[Antigen & immunogen design (vaccine)]]"
  - "[[Targeting vector & isotope selection (radiopharmaceutical)]]"
  - "[[Strain & consortium discovery (microbiome)]]"
---
Every project begins here, with one question: **what in the body should a medicine act on to change this disease?** That thing is the _target_. Everything built later is built to act on this one choice, so getting it wrong cannot be rescued downstream — most drugs that fail in patients fail because the target was never the right one, not because the molecule was poorly made.

A target is most often a single protein that is doing too much, too little, or the wrong thing in a disease. But what counts as a target depends on the kind of medicine that will eventually act on it, and these are genuinely different objects. For a small molecule, peptide, antibody, degrader, or radiopharmaceutical, the target is a specific protein whose activity should be blocked, boosted, removed, or marked. For an antibody or a cell therapy aimed at cancer, it is a _surface marker_ — a protein sitting on the outside of diseased cells and ideally almost nowhere else, so healthy tissue is spared. For a gene therapy or gene editing, the target is a gene itself: a broken gene to supply a working copy of, or an exact spot in the genome to correct. For a vaccine, it is an _antigen_ — a piece of a germ, or of a tumor, that the immune system should be trained to recognize. For a microbiome medicine, it is a missing or harmful microbial function in the gut. Naming which of these a project is after is part of the work, not a given.

**Finding a candidate target.** The strongest evidence that acting on a target will help patients comes from human biology itself. The central tool is the [[Genome-wide association study|genome-wide association study]], which scans the genomes of large groups — people with a disease against people without it — to find genetic differences that travel with the disease, pointing to the genes, and therefore the proteins, that are causally involved. Genetics is prized because it reflects a lifelong natural experiment in real humans rather than a model: drug targets backed by human genetic evidence are roughly **twice as likely** to survive clinical trials and reach approval, and projects increasingly refuse to start without it. Genetics is joined by other readouts of disease biology: measuring which genes and proteins are turned up or down in diseased tissue compared with healthy tissue, and tracing the molecular pathways those genes sit in to find the most pivotal point to act on.

**Validating it.** A candidate target is only a hypothesis until the project shows that changing it changes the disease. The decisive experiment is to switch the gene off, or turn it up, in cells or animals and watch what happens — does the disease-related behavior ease or worsen? The workhorse for this is the [[CRISPR screen|CRISPR screen]], which can knock out, silence, or activate thousands of genes at once across a population of cells and read out which ones matter for a disease-relevant outcome, turning a guess into ranked evidence. Alongside it, animals are engineered to lack or overproduce the target to confirm the effect in a whole organism, and patient tissue is checked to make sure the target is actually present where the disease is. A further question is whether the target is even reachable by a drug at all — its [[Druggability|druggability]]: a protein with a well-formed pocket can be hit by a small molecule, while one with a flat, featureless surface may only be approachable as a surface marker for an antibody, removed by a degrader, or shut off at the genetic level. Tractability like this feeds directly into the next decision.

**The output is two linked decisions.** The stage does not end in certainty — it ends in a reasoned bet that the target is causal, paired with the choice of **which kind of medicine is best suited to act on it**. That modality decision follows from the target's nature: a protein with a deep pocket invites a small molecule; a surface marker on a tumor invites an antibody or a cell therapy; a missing enzyme invites a replacement therapeutic protein or a gene therapy; a single faulty letter in the genome invites gene editing; a pathogen invites a vaccine. This is the choice that sends the project down one of the modality branches that make up the rest of the map. Because each branch is a wholly different kind of work, this is the last step every modality shares before they part.
