---
tags:
  - type/process
  - stage/design_optimization
  - modality/peptide
next:
  - "[[Protein & peptide formulation & fill-finish]]"
feedback:
  - "[[Peptide design & synthesis (peptide)]]"
---
A peptide that binds the target still has the fatal flaw of its class: left as a plain chain, it survives only minutes in the body. The body's protein-cutting enzymes (_proteases_) snip it apart, and the kidneys filter the small fragments straight out. Optimization is mostly the campaign to fix this while keeping the binding intact, again run as a make-and-test loop.

Three families of modification dominate, used alone or together:

**Protease resistance.** The enzymes that chop peptides recognize ordinary amino acids in ordinary arrangements. Swapping in mirror-image (D-) or other unnatural amino acids at the spots where enzymes cut, or closing the chain into a ring (_cyclization_) so it has no loose ends for end-cutting enzymes to grab, blunts this destruction. The diabetes and obesity drugs in the GLP-1 class, for example, carry such a substitution that defeats the specific enzyme (DPP-4) that would otherwise inactivate the natural hormone within two minutes.

**Half-life extension.** Even a protease-proof peptide is cleared fast unless it is made to travel with something large. The leading trick is _lipidation_: attaching a fatty-acid chain that latches onto albumin, the abundant long-lived carrier protein in blood. Riding on albumin shields the peptide from filtration and proteases — this is what turned native GLP-1's roughly two-minute half-life into semaglutide's week-long one, enabling once-weekly dosing. Attaching inert polymer chains (PEGylation) achieves a similar slowdown by sheer size.

**Shape locking.** Constraining the floppy chain — by cyclization or a chemical staple — so it already holds its binding shape raises potency, because the peptide no longer pays an energy penalty to fold each time it binds.

The characteristic difficulty is that every fix risks the binding: a stabilizing substitution or a staple sits on the same small molecule that has to grip the target, so improving stability can quietly destroy affinity, and the two must be re-balanced each cycle. When no variant holds both, the work loops back to design. The output is an optimized peptide that both binds well and lasts in the body, ready to be formulated.
