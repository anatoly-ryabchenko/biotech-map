---
tags:
  - type/process
  - stage/manufacturing
  - modality/gene_therapy
next:
  - "[[Phase 1 — safety & dose]]"
---
For an in-body gene therapy the [[Adeno-associated virus|adeno-associated virus]] (AAV) vector _is_ the finished product, so making it at the scale and purity a medicine demands — under [[Good Manufacturing Practice|GMP]] — is one of the hardest problems in modern manufacturing. (Cell therapies also need a viral vector — a [[Lentiviral vector|lentiviral]] one — but there it is a reagent used to engineer the cells, produced as part of cell product manufacturing rather than as a standalone product.)

Production usually starts by _transfecting_ a human producer cell line (HEK293) with the several pieces of DNA the cell needs to assemble vector particles, in large suspension bioreactors. The cells manufacture the vectors, which are then harvested and purified through chromatography and other steps.

The signature difficulty is _empty capsids_. A large fraction of the virus shells the cells make never package the gene — they come out empty — and empty shells are nearly identical to full ones, so separating them is technically brutal (density centrifugation, or finely tuned chromatography), and current methods force a trade-off between good separation and good yield. Empty capsids add to the patient's immune burden without benefit. On top of this, overall yields are low and the process expensive, while the doses needed — especially for whole-body gene therapy — are enormous, so making enough vector is a persistent bottleneck. A further hazard is accidentally generating a _replication-competent_ virus, which must be tested for and excluded. The output is a purified, full-capsid-enriched vector preparation, ready to dose patients.
