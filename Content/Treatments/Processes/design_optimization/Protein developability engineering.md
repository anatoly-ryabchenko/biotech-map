---
tags:
  - type/process
  - stage/design_optimization
  - modality/antibody
  - modality/de_novo
  - modality/therapeutic_protein
next:
  - "[[Protein & peptide formulation & fill-finish]]"
feedback:
  - "[[Therapeutic protein discovery & engineering]]"
---
A protein can bind its target perfectly and still be impossible to turn into a drug. _Developability_ is the bundle of properties that decide whether a protein can be made at high concentration, survive months in a vial, and be dosed safely. This step engineers those properties in — for antibodies, computationally designed proteins, and therapeutic proteins alike. (The antibody used in a conjugate is made developable as part of antibody discovery and maturation before its payload is attached.)

Therapeutic proteins are large and stay correctly folded only within a narrow comfort zone; outside it they misbehave in characteristic ways. The chief problem is _aggregation_ — molecules sticking together into clumps, which cuts the effective dose, fouls manufacturing, and, worst, can provoke the immune system. Closely related are _high viscosity_ (a concentrated antibody solution turning syrupy, so it can't be pushed through a thin injection needle), poor _solubility_, and low _expression_ (the producing cells making too little). Engineering attacks these by reshaping the protein's surface: replacing exposed water-repelling (_hydrophobic_) patches — which drive both aggregation and viscosity — with water-friendly ones, and breaking up clusters of like charge.

Alongside these physical traits, the sequence is scrubbed of _chemical liabilities_: specific spots that slowly decay and wreck a product's shelf life or activity. Known culprits include certain amino-acid pairs prone to a degrading reaction (deamidation), methionine and tryptophan residues that oxidize, stray cysteines that form wrong internal bonds, and unwanted [[Glycosylation|glycosylation]] sites sitting in the binding region. Each is swapped for a stable equivalent, ideally without touching function. The protein's [[Immunogenicity|immunogenicity]] is likewise screened and trimmed.

The characteristic difficulty is that the binding surface and the trouble surfaces overlap: the same exposed, often hydrophobic residues that grip the target also drive aggregation, so fixing developability can erode affinity, and every change must be re-tested for both. For a computationally designed protein this stage doubles as a reality check on predictions made [[In silico|in silico]]; for a therapeutic protein, a liability that cannot be engineered out loops back to reconsider the sequence or fusion chosen at discovery. The output is a manufacturable, stable, low-immunogenicity protein, ready for formulation.
