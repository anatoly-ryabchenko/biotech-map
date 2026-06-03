---
tags:
  - type/process
  - stage/lead_discovery
  - modality/small_molecule
next:
  - "[[Lead optimization (small molecule)]]"
---
A small molecule is a compact, chemically synthesized compound — usually under about 500 daltons — small enough to slip inside cells and lodge in a pocket on the target protein, switching its activity off or on. This step's job is to find a _hit_: a first compound that measurably acts on the target. A hit is not a drug — it typically binds weakly and touches other proteins too — but it is the chemical starting point everything downstream is shaped from.

The core problem is that the space of possible drug-like molecules is astronomically large (estimated above 10⁶⁰ compounds), so the work is really about searching that space cleverly. Several search strategies are used, often in parallel, each tested in an [[Assay|assay]] — a controlled measurement that produces a readable signal when a compound does something to the target.

**High-throughput screening.** [[High-throughput screening|High-throughput screening]] physically tests a curated library of existing compounds — often hundreds of thousands to a few million — against the target with robotics, one tiny well at a time. Hit rates are low, commonly well under 1%, and many apparent hits are artifacts that must be weeded out.

**Fragment-based discovery.** [[Fragment-based drug discovery|Fragment-based screening]] starts much smaller, with molecular pieces of 100–300 daltons. Because each piece is so simple, a library of only a few thousand covers chemical space efficiently and is more likely to find something that binds — but it binds very weakly, needs sensitive biophysical detection, and must then be grown or linked into a full-size molecule.

**DNA-encoded libraries.** A [[DNA-encoded library|DNA-encoded library]] attaches a unique DNA barcode to each compound, so billions of molecules can be pooled, washed over the target together, and the binders identified by reading their barcodes — far cheaper than testing them one at a time.

**Virtual screening.** [[Virtual screening|Virtual screening]] does a first pass on a computer: millions to billions of catalog molecules are computationally [[Docking|docked]] into the target's pocket and scored, so only the most promising are physically made and tested.

The characteristic difficulty is the false positive. Many compounds register as hits without truly binding the target — they clump together in solution, react indiscriminately with proteins, or interfere with the assay's readout. So every apparent hit is re-tested in an independent assay and its binding confirmed by a direct physical measurement before it is trusted. What "good" means here is not just activity but a confirmed, specific, chemically sensible interaction.

The output is a set of confirmed hits, usually clustered into a few chemical _series_ that share a common scaffold, handed to optimization to be reshaped into a real drug.
