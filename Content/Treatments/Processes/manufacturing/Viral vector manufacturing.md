---
tags:
  - type/process
  - stage/manufacturing
  - modality/gene_therapy
next:
  - "[[Phase 1 — safety & dose]]"
---
For an in-body gene therapy the [[Adeno-associated virus|adeno-associated virus]] (AAV) vector _is_ the finished product, so making it at the scale and purity a medicine demands — under [[Good Manufacturing Practice|GMP]] — is one of the hardest problems in modern manufacturing. (Cell therapies also need a viral vector — a [[Lentiviral vector|lentiviral]] one — but there it is a reagent used to engineer the cells, produced as part of cell product manufacturing rather than as a standalone product. The exception is _in-body CAR-T_, the gene-therapy variant described in [[Gene therapy]] in which the patient's own T cells are engineered inside the body: its lentiviral vector is itself the finished product, so it is made and released like the AAV case below.)

Production usually starts by _transfecting_ a human producer cell line (HEK293) with the several pieces of DNA the cell needs to assemble vector particles, in large suspension bioreactors. The cells manufacture the vectors, which are then harvested and purified through chromatography and other steps.

The signature difficulty of AAV is _empty capsids_. A large fraction of the virus shells the cells make never package the gene — they come out empty — and empty shells are nearly identical to full ones, so separating them is technically brutal (density centrifugation, or finely tuned chromatography), and current methods force a trade-off between good separation and good yield. Empty capsids add to the patient's immune burden without benefit. On top of this, overall yields are low and the process expensive, while the doses needed — especially for whole-body gene therapy — are enormous, so making enough vector is a persistent bottleneck. A further hazard is accidentally generating a _replication-competent_ virus, which must be tested for and excluded. The output is a purified, full-capsid-enriched vector preparation, ready to dose patients.

For in-body CAR-T the lentiviral vector is made the same way (HEK293 cells transfected with several pieces of DNA, one of which now encodes the mutated envelope and the T-cell binder), but its difficulties differ. The lentiviral particle is a fragile fatty-membrane-wrapped structure, so harsh purification or shear destroys the infectious particles, and potency is measured as the number of particles that actually deliver their gene into T cells, not the number of particles made. Displaying the binder on the envelope can also lower yield. The scale is smaller than for whole-body AAV but not small: doses of about 10⁹ transducing units per patient (KLN-1010 at 4 × 10⁶ to 2 × 10⁷ per kilogram; ESO-T01 at 2 × 10⁸ per patient) mean each patient consumes a sizeable lot. In exchange, one lot treats many patients, in place of the one-batch-per-patient manufacturing of conventional cell therapy.
