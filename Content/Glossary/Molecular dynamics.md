---
tags:
  - type/glossary
---
Molecular dynamics (MD) is a physics simulation of how a molecular system moves over time. Rather than predicting a single static shape, it tracks where every atom goes, producing a trajectory — a sequence of frames showing the system in motion rather than one frozen picture.

The simulation works by repeatedly answering one question: given where all the atoms are right now, what force does each one feel, and where does it move next? The forces come from a **force field** — a model that approximates the energy of the system from the positions of its atoms. The force field assigns a mathematical cost to stretching bonds, bending angles, pushing atoms too close together, and to the attractions and repulsions between charged or hydrophobic (water-repelling) groups. Its parameters are fitted in advance to quantum-chemistry calculations and experimental measurements. From those energies the simulation computes the force on each atom, then uses Newton's laws of motion to advance every atom a tiny step forward in time. It then recomputes the forces and repeats.

Each step has to be extremely short — typically a few femtoseconds (a femtosecond is one quadrillionth of a second). The step must be shorter than the fastest motion in the system, the vibration of chemical bonds; a larger step would let atoms pass through each other and the simulation would blow up. Because steps are so short, reaching even a microsecond of simulated time takes on the order of a billion sequential steps, which is why MD is computationally demanding and why much of the field's effort goes into running it faster.

What the trajectory reveals is behavior a single predicted structure cannot show: how stable a fold is (does it hold together or drift apart), which shapes a flexible region samples, and whether a binding event drives a larger change in shape. In protein design this is used to probe whether a designed protein actually does its intended job — for a conformational modulator, for instance, whether binding genuinely pushes the target into the desired shape rather than merely sticking to it. Why proteins adopt and hold a given fold at all is covered in [[protein folding principles]].

The central limitation: classical MD does not model chemical reactions. Because the force field treats bonds as fixed springs, it cannot describe a bond breaking or a new bond forming — the events at the heart of what an enzyme does. Capturing that chemistry requires either a quantum treatment of the reacting region ([[Quantum Mechanics - Molecular Mechanics]]) or machine-learned models that reproduce quantum-level forces ([[neural network approaches for chemical interactions]]).

## External resources
- [EMBL-EBI, "Basis of molecular dynamics simulations" (training course)](https://www.ebi.ac.uk/training/materials/biomolecular-simulations-materials/molecular-dynamics-simulations/basis-of-molecular-dynamics-simulations/) — a free, ground-up training module from a recognized authority on force fields, time steps, and what a trajectory tells you.
- [McCammon, Gelin & Karplus, "Dynamics of folded proteins," *Nature* (1977)](https://www.nature.com/articles/267585a0) — the foundational paper that first ran a molecular dynamics simulation on a protein, opening the field.
