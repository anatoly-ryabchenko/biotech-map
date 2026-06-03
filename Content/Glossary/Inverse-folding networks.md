---
tags:
  - type/glossary
---
A protein is a chain of amino acids that folds into a three-dimensional shape, and that shape determines what the protein does. Normal *folding* goes one way: start with a sequence of amino acids, end up with the shape it adopts (see [[protein folding principles]]). An inverse-folding network runs that direction backwards. It is given a desired 3D shape — typically a backbone proposed by a [[backbone-generation networks]] model — and proposes amino-acid sequences predicted to be *foldable into* that shape.

The leading models are machine-learning networks trained on large collections of known protein structures paired with their real sequences. Given a fixed backbone, the model looks at the local geometry around each position — which atoms are nearby, how the chain is oriented there — and predicts which amino acid fits at that spot, position by position, until it has a full sequence consistent with the scaffold. ProteinMPNN (Baker Lab, 2022) is the standard example; it routinely produces sequences for backbones that older physics-based methods failed on.

The key distinction this rests on is what "foldable into" actually means, because it is weaker than it sounds. It means the target shape is a *stable, low-energy arrangement* for that sequence: if you could place the chain in that exact shape, it would hold there rather than unravel. It does **not** guarantee that the chain, left to fold on its own from scratch, will choose that shape. The same sequence may have an even more stable arrangement it prefers — a deeper resting state — and settle into that instead, ignoring the shape it was designed for. An inverse-folding network checks only that the intended shape is *a* good fit, not that it is the *best* fit and therefore the one the chain will actually adopt.

That gap is exactly why a separate check is needed afterward. The proposed sequence is run through a [[structure-prediction networks]] model, which forecasts the shape the sequence would really fold into; only if that predicted shape matches the intended one is the design kept. Inverse folding proposes, structure prediction verifies — they are deliberately different tools answering different questions.

A designed shape is useless without a real amino-acid chain that produces it. Inverse-folding networks are the bridge from "here is the shape I want" to "here is a protein you could actually build," and they do it in seconds for shapes that have no natural counterpart, which is what makes [[in silico]] design of brand-new proteins practical at all.

## External resources
- [David Baker, "Introduction to Protein Design and Protein Design Algorithms" (iBiology talk)](https://www.ibiology.org/biochemistry/introduction-protein-design-protein-design-algorithms/) — an accessible lecture covering the two reciprocal problems of protein design: predicting structure from sequence, and finding a sequence for a desired structure.
- [Dauparas et al., "Robust deep learning–based protein sequence design using ProteinMPNN," *Science* (2022)](https://www.science.org/doi/10.1126/science.add2187) — the foundational paper for modern learned inverse folding.
