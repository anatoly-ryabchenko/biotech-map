---
tags:
  - type/glossary
---
Protein properties prediction is the use of computational models to estimate, before any protein is physically made, how good a candidate design is — so that a large pool of designs can be narrowed and ranked on a computer instead of in the lab. In [[in silico]] protein design a single run can produce thousands of candidate shapes and sequences; testing them all in the lab would be impossibly slow and expensive, so their likely properties are predicted first and the pool is filtered down to dozens or hundreds and ranked, with only the top candidates sent forward.

The predicted properties fall into a few groups.

*Folding and structure confidence* asks whether the sequence is likely to fold into the intended shape at all. The main signal here comes from [[structure-prediction networks]]: how closely the predicted shape matches the design, and how confident the model is — for example the pLDDT score, a per-position confidence from 0 to 100 where higher means the model is surer of the local shape. A low-confidence or mismatched fold is a reason to drop a candidate early.

*Interface and binding quality* asks how well the designed protein actually meets its target — whether the contacting surfaces fit together closely, how tightly they are predicted to bind, and whether the binding is to the intended target rather than the wrong molecules (see [[docking]]). A design can fold perfectly and still grip its target weakly or in the wrong place.

*Developability* properties ask whether the protein can survive being manufactured and handled, independent of whether it does its job. These include solubility (will it dissolve rather than clump), stability (will it stay folded at the relevant temperature and acidity), aggregation propensity (will copies stick to each other and fall out of solution), and [[Protein expression|expression]] (will the cells used to produce it actually make it in usable amounts). These are predicted by separate machine-learning models trained on measured proteins, often reading the sequence and structure to flag, for instance, sticky patches likely to drive aggregation. A design that scores well on function but poorly on developability is expensive or impossible to turn into a real product.

Wet-lab work is the bottleneck of protein design — each experiment is slow and costly. In-silico properties prediction is the filter that keeps that bottleneck from being flooded, removing candidates predicted to misfold, bind poorly, or be unmanufacturable, and ranking the survivors so the most promising are tested first. Its limits mirror those of the models it relies on: predicted scores can be confidently wrong, especially for novel designs unlike anything in the training data, which is why these rankings guide lab work rather than replace it.
