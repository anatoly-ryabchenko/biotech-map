---
tags:
  - type/process
  - stage/lead_discovery
  - modality/protein_degrader
next:
  - "[[Degrader optimization (protein degrader)]]"
---
A protein degrader does not block its target — it destroys it. Cells run a built-in disposal system, the [[Ubiquitin-proteasome system|ubiquitin–proteasome system]], that tags unwanted proteins with a small marker called ubiquitin and feeds them into a barrel-shaped shredder, the proteasome. A degrader hijacks this system to mark a chosen disease protein for destruction. Because it only has to touch the target briefly rather than permanently occupy a working pocket, it can act on targets with no good pocket at all — many proteins long written off as "undruggable." This step designs that first degrader; the work splits into two kinds of molecule.

**PROTACs.** A PROTAC is one molecule with three parts: one end binds the target protein, the other end grabs one of the cell's [[E3 ligase|E3 ubiquitin ligases]] (the enzymes that actually attach ubiquitin), and a chemical _linker_ joins them. When both ends are engaged, the PROTAC holds target and ligase together in a [[Ternary complex|ternary complex]]; the ligase then tags the target with ubiquitin and the proteasome destroys it. The PROTAC is released intact and repeats the cycle, so it works catalytically — a little goes a long way. In practice two ligases dominate because good small-molecule handles exist for them: cereblon (CRBN) and VHL.

**Molecular glues.** A molecular glue is much smaller and has no explicit target-binding end. It binds the E3 ligase and subtly reshapes its surface so the ligase now sticks to a protein it would normally ignore, dragging that new "neosubstrate" to destruction. Glues are smaller and more drug-like but far harder to design on purpose.

Designing a degrader means picking the E3 ligase, a starting chemical handle for the target, and — for a PROTAC — a linker, whose length and stiffness decide whether target and ligase can actually be held in a productive arrangement. The characteristic difficulty is that binding both ends well does not guarantee degradation: the ternary complex has to position the target so the ligase's ubiquitin-attaching machinery can reach an exposed spot on it, and a badly chosen linker gives a molecule that binds everything yet degrades nothing. A second quirk is the _hook effect_: at high concentrations the degrader saturates target and ligase separately instead of bridging them, so degradation paradoxically drops off — a trap molecular glues, being one-ended, avoid.

The output is an initial degrader that measurably lowers the target protein's level inside cells, ready for optimization.
