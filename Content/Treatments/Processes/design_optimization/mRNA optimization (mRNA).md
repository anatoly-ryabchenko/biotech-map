---
tags:
  - type/process
  - stage/design_optimization
  - modality/mrna
next:
  - "[[LNP formulation & delivery]]"
feedback:
  - "[[mRNA construct design (mRNA)]]"
---
The construct designed upstream is a first draft. Optimization makes it work reliably inside cells and quietens the alarm that foreign RNA sets off — run as a test-and-refine loop over candidate sequences, because the behaviour of an mRNA is notoriously hard to predict and must be measured.

Three things are improved. First, _expression_ — how much protein each strand makes, and for how long. The [[Codon optimization|codon-optimized]] coding sequence and the untranslated regions chosen at design are varied, and the variants tested in cells to find which actually yield the most protein. Second, _stability_: the strand is nudged to fold into shapes that resist the cell's RNA-chewing enzymes, prolonging output, while avoiding folds that jam the reading machinery.

Third, and decisive, _immune quietness_. A cell treats foreign RNA as a sign of viral infection and shuts down. The [[Modified nucleosides|modified nucleoside]] N1-methylpseudouridine, built in at design, is the main defense, but optimization must also stamp out _double-stranded RNA_ — accidental paired structures that arise during manufacture and are the single strongest trigger of the cell's antiviral alarms. Sequences are chosen (and later purification designed) to minimize it. The target level of quiet depends on the use: a protein-replacement mRNA wants maximum silence, while a vaccine wants a measured amount of immune stimulation, so "optimal" is tuned accordingly.

The characteristic difficulty is that these levers interact in ways that only show up in living cells: a sequence folded for stability may be read more slowly, and a change that lifts expression can create a double-stranded stretch that trips the alarm. So optimization is empirical — cycling several candidates through cell tests rather than computing one answer — and when none performs well enough the work loops back to construct design. The output is a final, best-performing sequence, ready for its delivery vehicle.
