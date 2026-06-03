---
tags:
  - type/process
  - stage/design_optimization
  - modality/antibody
  - modality/conjugated_biologic
next:
  - "[[Protein developability engineering]]"
  - "[[Conjugation, linker design & characterization (conjugated biologic)]]"
feedback:
  - "[[Antibody discovery]]"
---
The panel of antibodies from discovery binds the target, but the lead usually grips too weakly and — if it came from a mouse — looks foreign to the human immune system. This step strengthens the binding and makes the antibody human: two engineering jobs done together.

_Affinity maturation_ raises how tightly the antibody holds its target. The gripping is done by small loops at the tips of the antibody, the _CDRs_ (complementarity-determining regions). Many variants are made carrying small mutations across these loops, and the tightest binders are then fished out by a display method — commonly _yeast display_, where each yeast cell shows one antibody variant on its surface and a machine sorts out the cells whose variant binds best. Repeating the cycle enriches affinity by orders of magnitude, often pushing a modest binder into the very tight (sub-nanomolar) range.

_Humanization_ strips the foreignness from animal-derived antibodies. The standard method is _CDR grafting_: the binding loops, which carry the specificity, are transplanted onto a human antibody framework, so the bulk of the molecule reads as human while the grip is preserved. This matters because a foreign antibody provokes the patient to mount an immune response against the drug itself — its [[Immunogenicity|immunogenicity]] — which neutralizes it and can cause reactions. Antibodies that came from transgenic mice or fully human libraries need little of this. For an antibody–drug conjugate, this same matured, humanized antibody is the one that will later carry the toxic payload.

The characteristic difficulty is that the goals interfere. Grafting loops onto a human framework can subtly distort them and lose affinity, so a few framework positions usually have to be tuned back; and affinity-boosting mutations can introduce new immunogenic or unstable spots. Every round must re-check that binding, humanness, and behaviour all still hold. When a lead cannot be rescued, the work loops back to discovery for a different binder. The output is a strong, human, specific antibody, ready for developability engineering.
