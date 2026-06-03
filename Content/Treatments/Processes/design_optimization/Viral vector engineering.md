---
tags:
  - type/process
  - stage/design_optimization
  - modality/gene_therapy
  - modality/cell_therapy
next:
  - "[[Vector formulation & delivery (gene therapy)]]"
  - "[[Cell engineering & expansion (cell therapy)]]"
feedback:
  - "[[Transgene & cassette design (gene therapy)]]"
---
A viral vector is a virus stripped of its ability to cause disease and repurposed to carry a therapeutic gene into cells — nature's most efficient gene-delivery machine, redirected. This step engineers the vehicle: for a gene therapy it is the product the patient receives; for a cell therapy it is the tool that will deliver the receptor gene into cells in the next step.

Two vector families dominate. The [[Adeno-associated virus|adeno-associated virus]] (AAV) is the workhorse for in-body gene therapy — it does not normally splice into the genome and is generally well tolerated, but holds only a small gene. The [[Lentiviral vector|lentiviral vector]] permanently integrates its cargo into the cell's DNA and carries more, which makes it the standard for engineering cells (as in cell therapy), where the new gene must be inherited by every descendant of the treated cell.

The central engineering problem is _tropism_ — which cells the vector enters. A natural virus infects the wrong range of tissues, so its outer shell is re-engineered to redirect it: displaying small targeting peptides on the surface, or, more powerfully, [[Directed evolution|directed evolution]] — building huge libraries of shell variants, selecting the ones that enter the wanted tissue, and repeating — to evolve a shell that homes to, say, muscle or brain while avoiding the rest. The shell is also tuned to slip past pre-existing immunity, since many people already carry antibodies against common natural AAVs that would neutralize the vector on contact.

The characteristic difficulty is specificity and the immune system together: a vector injected into the body can be wiped out by antibodies before it arrives, can trigger dangerous immune reactions at the high doses needed to reach enough cells, and — if its tropism is loose — dumps its gene in the wrong organs. Engineering a shell that is both well-aimed and stealthy is unsolved in general and worked out target by target. When a gene won't fit a usable vector, the work loops back to cassette design. The output is an engineered vector design that delivers to the right cells — passed on to be produced and (for gene therapy) formulated, or (for cell therapy) used to engineer cells.
