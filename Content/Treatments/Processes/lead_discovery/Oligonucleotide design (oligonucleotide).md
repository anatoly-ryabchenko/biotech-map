---
tags:
  - type/process
  - stage/lead_discovery
  - modality/oligonucleotide
next:
  - "[[Oligonucleotide optimization (oligonucleotide)]]"
---
An oligonucleotide drug is a short, lab-made strand of genetic letters, usually about 15–25 long, designed to recognize one specific _messenger RNA_ — the working copy of a gene that a cell reads in order to build a protein. It finds its target by the same base-pairing rule that holds the two strands of DNA together (A pairs with T or U, G with C). Because the drug is chosen simply by reading off the complement of the target's sequence, design is fast and almost any gene's message is in principle addressable — including disease proteins that have no druggable pocket for a small molecule. The work has two main variants, set by the mechanism.

**Antisense oligonucleotides (ASOs)** are single strands. A _gapmer_ ASO pairs with its target message and recruits a cellular enzyme, RNase H, that cuts any RNA message wherever a DNA-like strand is bound to it — destroying the message so its protein is never made. A _splice-switching_ ASO instead binds quietly, without triggering cutting, masking a signal the cell uses when assembling the message and so changing which version of the protein gets built; this is how nusinersen treats spinal muscular atrophy.

**Small interfering RNAs (siRNAs)** are double strands. They load into a natural cellular machine, the [[RNA interference|RNA interference]] pathway, which keeps one strand as a guide, finds the matching message, and cuts it — catalytically, so one siRNA clears many copies.

A raw genetic strand is useless as a drug: enzymes in the blood shred it within minutes and it cannot cross into cells. The decisive design work is therefore chemistry — see [[Oligonucleotide chemical modifications|oligonucleotide chemical modifications]] — reworking the backbone (phosphorothioate links) and the sugar (2′-MOE, locked nucleic acid) to resist destruction and bind more tightly, while keeping enough natural-like character that RNase H or the RNA-interference machinery still accepts the strand.

The characteristic difficulty is picking a site on the message that is actually reachable: messages fold up on themselves and are coated with proteins, so many sequence-perfect oligonucleotides simply cannot get to their site, and a strand can also partially match an unintended message and silence the wrong gene. Candidates are therefore designed in batches against many different sites and screened to find the ones that work.

The output is a set of sequence-and-chemistry-defined oligonucleotides that knock down or redirect the target message, ready for optimization.
