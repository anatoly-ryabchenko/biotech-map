---
tags:
  - type/process
  - stage/design_optimization
  - modality/de_novo
next:
  - "[[Protein developability engineering]]"
feedback:
  - "[[In silico protein design]]"
---
The in-silico design step produces thousands of computer-confident proteins, but prediction and reality often part ways. This step is the first time those designs are physically made and measured — the reality check the whole de novo approach depends on, since the prediction models, trained mostly on natural proteins, are least reliable exactly where a genuinely novel design sits.

The work runs in order. First the chosen designs are physically produced: each amino-acid sequence is turned back into a gene, the gene is put into bacteria or other host cells, and the cells are made to build the protein — see [[Protein expression|protein expression]]. The first hard filter is simply whether a design _expresses_ at all and comes out _soluble_ rather than as insoluble junk; many computationally perfect designs fail right here. Surviving proteins are then tested for the two things that matter. _Does it fold into the intended shape?_ — probed by how the protein behaves in solution and, for the best candidates, by solving its actual structure, either with X-ray crystallography or with cryo-electron microscopy (flash-freezing the protein and imaging it with a beam of electrons). _Does it bind the target as intended?_ — measured directly by methods such as surface plasmon resonance, which flows the target over the immobilized protein and reads in real time how strongly and how durably they hold together.

Modern design has made this far less of a lottery than it once was: for well-behaved binder targets, recent methods report that a large fraction of designs — often the majority — express, fold, and bind. But harder goals such as [[Negative design|selective non-binding]], conformational switching, and especially enzymes still emerge weak and need improvement, commonly by [[Directed evolution|directed evolution]]: making many random variants and selecting the best, over and over, to boost activity many-fold.

The characteristic difficulty is the _false positive_ inherited from design: because the prediction networks share assumptions, a design can earn top scores yet not fold or bind at all, and only the bench reveals it. Failed designs loop back to in-silico design carrying that information. The output is a small set of experimentally confirmed, real proteins, ready for developability engineering.
