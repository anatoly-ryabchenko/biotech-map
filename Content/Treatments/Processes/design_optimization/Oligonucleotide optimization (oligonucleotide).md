---
tags:
  - type/process
  - stage/design_optimization
  - modality/oligonucleotide
next:
  - "[[Oligonucleotide conjugate delivery (oligonucleotide)]]"
feedback:
  - "[[Oligonucleotide design (oligonucleotide)]]"
---
The designed oligonucleotides silence their target message in a dish, but two problems stand between that and a usable drug: they reach few tissues, and they can silence the wrong genes. Optimization, run as a make-and-test loop, fixes both — largely through chemistry and delivery.

The first axis is _chemistry tuning_ — see [[Oligonucleotide chemical modifications|oligonucleotide chemical modifications]]. Beyond the backbone and sugar changes set at design, optimization decides exactly where each modification sits, balancing three things that trade against one another: resistance to blood enzymes, binding strength to the target message, and keeping the natural-like stretch that RNase H or the [[RNA interference|RNA-interference]] machinery needs in order to cut. Over-modify and the drug is stable but inert; under-modify and it is active but quickly destroyed.

The second axis is _targeted delivery_. Naked oligonucleotides spread through the body poorly, but a striking trick solves it for the liver: attaching a small sugar cluster, [[GalNAc conjugation|GalNAc]], that a receptor found almost only on liver cells grabs and pulls inside, concentrating the drug there and allowing a simple injection under the skin. This is now the dominant route for liver-targeted siRNAs and ASOs; reaching other organs is far harder and is a major focus of work.

The third axis is _off-target silencing_. Because an oligonucleotide can silence any message that partially matches it — especially through a short "seed" stretch of a few letters — it can knock down unintended genes and cause toxicity. Optimization detects these effects and defeats them with precise tweaks: placing a destabilizing modification in the seed region weakens accidental matches while leaving the intended one intact, widening the safety margin several-fold.

The characteristic difficulty is that all three axes share the same ~20 letters, so a change made for one can ruin another. When a sequence cannot be made both safe and potent, the work loops back to choose a different site on the message. The output is an optimized oligonucleotide — stable, potent, selective — ready for its delivery formulation.
