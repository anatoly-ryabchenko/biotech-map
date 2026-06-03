---
tags:
  - type/glossary
---
_Virtual screening_ is searching for drug candidates on a computer instead of at the bench — predicting, for a huge catalogue of molecules, which are most likely to bind the target, so that only the best are actually made and tested. It is the [[In silico|in silico]] front end to hit discovery, and it can sift libraries far larger than any physical screen — hundreds of millions to billions of molecules.

There are two broad approaches. _Structure-based_ virtual screening uses the three-dimensional shape of the target's binding pocket and computationally [[Docking|docks]] each candidate into it, scoring how well it fits and how tightly it should bind. _Ligand-based_ virtual screening is used when the pocket's structure is unknown: starting from molecules already known to bind, it ranks new molecules by chemical similarity to those known binders. Either way, the output is a ranked shortlist.

The value is leverage — computing is cheap next to synthesizing and assaying — but the result is only a prediction. Scoring functions estimate binding crudely and produce many _false positives_ (molecules that score well yet don't actually bind) and false negatives, so virtual screening narrows and prioritizes candidates rather than confirming them; the shortlist still has to be made and tested in a real [[Assay|assay]].

## External resources
- [*Molecular Docking: Principles and Methods* (DrugDesign.org)](https://www.drugdesign.org/chapters/molecular-docking/) — a free, ground-up tutorial on the docking and scoring functions that underlie structure-based virtual screening, including where they succeed and fail.
