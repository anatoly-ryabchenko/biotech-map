---
tags:
  - type/process
  - stage/preclinical_studies
  - modality/protein_degrader
next:
  - "[[In vivo efficacy & PK (small molecules & degraders)]]"
---
A degrader is judged in cells by a different yardstick than an ordinary drug: not whether it binds, but whether it destroys. This step confirms, in living disease-relevant cells, that the degrader actually lowers the target protein's level and that doing so produces the wanted effect.

The central readouts are the _degradation metrics_ measured directly in cells — the **DC50** (the concentration that clears half the target) and **Dmax** (the most that can be cleared) — plus the _kinetics_: how fast the protein disappears, and how long it stays down after the drug is washed away, since a degrader's effect outlasts its presence (the protein must be re-made before activity returns). A functional [[Assay|assay]] then checks that removing the protein does what was intended to the cell.

Selectivity is assessed in a way peculiar to this modality. Because a degrader could in principle drag other proteins to destruction, the whole cell's protein content is surveyed — by mass-spectrometry proteomics — to see _everything_ whose level changed, catching unintended "collateral" degradation that a simple binding assay would miss entirely. Early [[ADME|ADME]] work concentrates on the degrader's poor cell entry, the recurring weakness of these oversized molecules.

The characteristic difficulty is that degradation depends on the cell's own disposal machinery — how much of the chosen [[E3 ligase|E3 ligase]] and proteasome a cell has — which varies between cell types, so a degrader potent in one cell can be weak in another where that machinery is scarce; and the [[Ubiquitin-proteasome system|ubiquitin–proteasome system]] can adapt over time, blunting the effect. These cell-context effects are invisible in a binding assay and only surface here. The output is in-cell confirmation that the degrader clears its target — selectively, durably, and with the intended consequence.
