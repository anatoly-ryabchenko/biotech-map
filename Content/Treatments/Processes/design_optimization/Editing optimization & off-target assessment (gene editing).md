---
tags:
  - type/process
  - stage/design_optimization
  - modality/gene_editing
next:
  - "[[LNP formulation & delivery]]"
feedback:
  - "[[Guide & editor design (gene editing)]]"
---
A working edit is not enough. A gene-editing drug must edit the right spot efficiently _and_ essentially never edit anywhere else, because every wrong edit is permanent. This step optimizes the editing and, above all, hunts for off-target activity — the modality's defining safety question.

_Optimization_ improves on-target performance. Among the candidate guides from design, the ones that edit most efficiently are identified, and the [[CRISPR|CRISPR]] machinery itself is refined: high-fidelity versions of the cutting protein, engineered to act only on a near-perfect match, are used to cut down stray activity, and the guide RNA's chemistry is tuned for stability. How the editor is delivered also matters and is settled here in principle — delivering it briefly, as a short-lived mRNA or a pre-made protein rather than as DNA that lingers, limits how long it can act and so limits stray edits.

_Off-target assessment_ is the heart of the step. The genome is three billion letters long, and a guide can partially match many other places. Unbiased, genome-wide methods are used to find everywhere the editor actually cuts: techniques such as GUIDE-seq drop a traceable tag into every cut site in living cells, so the off-target locations can be sequenced and counted — detecting edits that occur in well under 1% of cells. Candidate guides are ranked by how clean this profile is, and any guide with a worrying off-target is dropped.

The characteristic difficulty is that off-targets are easy to miss and impossible to undo: a rare edit in a dangerous spot — switching on a cancer gene — might appear in only a handful of cells and slip past an insensitive assay, yet matter enormously in a patient carrying it for life. So the assays must be exhaustive and the bar near zero. The choice between editing inside the body and editing extracted cells (which can be checked before being returned) bears directly on this. Unacceptable guides loop back to design. The output is a validated guide-and-editor with a clean off-target profile, ready for delivery formulation.
