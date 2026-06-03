---
tags:
  - type/process
  - stage/design_optimization
  - modality/protein_degrader
next:
  - "[[Oral & solid formulation (small molecules & degraders)]]"
feedback:
  - "[[Degrader design (protein degrader)]]"
---
The initial degrader proves the concept — it lowers the target protein's level — but is rarely efficient or drug-like enough to use. Optimization runs as the same design–make–test–analyze loop as for a small molecule, but the thing being measured and tuned is different, because a degrader's job is not to bind but to cause destruction.

The central readouts are _degradation metrics_: the **DC50** (the concentration that clears half the target protein) and the **Dmax** (the greatest fraction of the protein that can be cleared at all). A degrader can bind both ends superbly yet degrade poorly, so chemists optimize against these destruction numbers directly, not just against binding strength. For a PROTAC, the most powerful lever is the _linker_ joining the two ends: its length, stiffness, and chemistry decide whether the target and the [[E3 ligase|E3 ligase]] are held in a geometry where ubiquitin can actually be transferred. Small linker changes can swing degradation dramatically, so many linker variants are made and screened — increasingly with a fast "direct-to-biology" approach that tests crude reaction products without full purification to cover more options quickly.

The other dominant problem is getting the molecule into the cell. A PROTAC is far larger than an ordinary small molecule — it sits "beyond the rule of five," the rough size and chemistry range within which molecules are usually orally absorbed — so it tends to be poorly soluble and to cross cell membranes badly. A great deal of optimization goes into trimming and disguising the molecule (for instance swapping certain bonds, or exploiting the way these floppy molecules can fold up to hide their polar parts) to claw back permeability without losing degradation.

The characteristic difficulty is this collision between the size needed to bridge two proteins and the compactness needed to enter cells and be taken orally — a tension ordinary inhibitors never face. When it cannot be resolved within a series, the project loops back to redesign with a different handle or ligase. The output is an optimized degrader, efficient and drug-like enough to advance.
