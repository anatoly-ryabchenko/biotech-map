---
tags:
  - type/process
  - stage/lead_discovery
  - modality/mrna
next:
  - "[[mRNA optimization (mRNA)]]"
---
Where an oligonucleotide silences a gene's message, an mRNA drug supplies one. The medicine is itself a messenger RNA — the instruction strand a cell reads to build a protein — so that the patient's own cells manufacture the desired protein for a while: a viral or tumor antigen for a vaccine, or a missing functional protein for a replacement therapy. Design here means writing and engineering that instruction so it survives long enough, is read efficiently, and does not alarm the cell that takes it up.

A construct has a fixed anatomy, each part engineered:
- a **5′ cap** — a special modified-guanosine structure at the front that marks the strand as legitimate, lets the cell's protein-building machinery latch on, and shields the strand from being chewed up from that end;
- a **5′ untranslated region** — a lead-in sequence tuned so that ribosomes load onto it readily;
- the **coding sequence** — the actual recipe for the protein;
- a **3′ untranslated region** — which influences how long the strand survives in the cell;
- a **poly-A tail** — a long run of adenosine letters that further stabilizes it.

Two design levers matter most. [[Codon optimization|Codon optimization]] rewrites the coding sequence: because the genetic code is redundant — several three-letter codons specify the same amino acid — the same protein can be spelled many ways, and choosing the codons a cell reads fastest, while tuning how the strand folds, raises how much protein is made. And the strand is assembled not from ordinary letters but from [[Modified nucleosides|modified nucleosides]], chiefly N1-methylpseudouridine in place of ordinary uridine: raw foreign RNA trips the cell's viral-RNA alarms and is destroyed or shuts the cell down, whereas the modified letter reads normally but slips past those alarms. That single substitution is what made mRNA medicines practical.

The finished sequence is the template for [[In vitro transcription|in vitro transcription]], the cell-free enzymatic reaction that later manufactures the strand in bulk.

The characteristic difficulty is that these goals pull against each other and resist prediction: a sequence folded for stability may be read more slowly, and the immune stimulation that is unwanted for a protein-replacement mRNA is partly wanted for a vaccine — so "optimal" depends on the use. Design therefore proposes several candidate sequences to be tested rather than one.

The output is one or more finished construct sequences, ready for optimization.
