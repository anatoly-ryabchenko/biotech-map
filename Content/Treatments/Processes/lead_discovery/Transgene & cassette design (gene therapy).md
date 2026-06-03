---
tags:
  - type/process
  - stage/lead_discovery
  - modality/gene_therapy
next:
  - "[[Viral vector engineering]]"
---
A gene therapy treats a disease caused by a missing or broken gene by delivering a working copy of that gene into the patient's cells, so the cells themselves start making the protein they could not make before. This step designs the genetic payload — not yet the delivery vehicle (that comes next), but the instructions the vehicle will carry.

The payload is an _expression cassette_: the therapeutic gene plus the control sequences a cell needs in order to read it. Chief among these is a [[Promoter|promoter]], a stretch of DNA sitting in front of the gene that switches it on and sets how strongly, and in which tissues, it is read — choosing the promoter is how a therapy is aimed to act in the liver but nowhere else, or strongly everywhere at once. The cassette also carries a tail signal that ends each message cleanly and, often, small helper sequences that lift output. The therapeutic gene itself is usually [[Codon optimization|codon-optimized]] — respelled, using the redundancy of the genetic code, so the target cell reads it efficiently.

The dominant delivery vehicle is the [[Adeno-associated virus|adeno-associated virus]] (AAV), and it imposes the hardest design constraint: an AAV shell holds only about **4,700 DNA letters** in total, for the gene and every control sequence together. Many genes do not fit. Design becomes a packing problem — use the smallest promoter that still works, trim helper elements, shrink the gene — and when a gene simply will not fit, split it across two vectors that reassemble it inside the cell, at a steep cost in efficiency.

The characteristic difficulty is exactly this tension between completeness and size: a cassette needs enough control sequence to express well in the right place, yet every letter spent on control is a letter denied to the gene, and overshooting the limit yields vectors that package poorly or come out truncated and dead. The output is a finished cassette sequence that fits the vehicle, ready for the vehicle to be engineered around it.
