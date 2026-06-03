---
tags:
  - type/process
  - stage/manufacturing
  - modality/antibody
  - modality/de_novo
  - modality/therapeutic_protein
next:
  - "[[Phase 1 — safety & dose]]"
---
Antibodies, designed proteins, and therapeutic proteins are too large and intricate to synthesize chemically, so they are _grown_ by living cells — and biomanufacturing is the craft of doing that at scale, reliably, under [[Good Manufacturing Practice|GMP]]. It splits into two halves.

_Upstream_ is the cell culture. The gene for the protein is put into a host cell line — almost always Chinese hamster ovary (CHO) cells, prized because they fold human proteins correctly and attach human-like sugar chains ([[Glycosylation|glycosylation]]) — and the cells are grown in large stirred bioreactors of thousands of litres, with tightly controlled temperature, acidity, oxygen, and feeding, secreting the protein into the broth.

_Downstream_ is purification: pulling one protein cleanly out of a soup of cells, debris, and other cell proteins. The workhorse first step for antibodies is _Protein A chromatography_, a column carrying a bacterial protein that grabs antibodies by their Fc stem while almost everything else washes away, giving high purity in a single pass (designed proteins lacking an Fc use other capture methods). Further chromatography polishes the product, and dedicated steps _clear viruses_ — a low-acidity hold and special filters that inactivate and remove any stray viral contamination, since the product came from living mammalian cells.

The characteristic difficulty is biological variability: living cells are sensitive, and small shifts in the culture can change how much protein is made and — critically — its sugar pattern, which affects how the drug works and how long it lasts, so the process must be controlled tightly enough to make every batch effectively identical. A contaminated bioreactor can destroy an entire campaign. The output is a purified, correctly modified protein drug substance, made to specification and ready for trials.
