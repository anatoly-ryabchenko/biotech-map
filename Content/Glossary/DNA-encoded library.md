---
tags:
  - type/glossary
---
A _DNA-encoded library_ (DEL) is a way to search billions of compounds at once by giving every compound a DNA "barcode" that records its chemical structure. It sidesteps the bottleneck of [[High-throughput screening|high-throughput screening]] — testing compounds one well at a time — by testing them all together in a single tube.

The library is built by _split-and-pool_ synthesis. A pool of starting molecules, each already carrying a short DNA tag, is split into batches; each batch has one chemical building block added _and_ a matching DNA letter-sequence appended to record which block was used; the batches are recombined, then split again for the next building block. After a few rounds, each of the resulting billions of molecules carries a DNA tag spelling out its full synthetic history — and therefore its structure.

To screen, the whole pooled library is washed over the immobilized target; molecules that bind stick, the rest are rinsed away, and the bound molecules' DNA tags are read by sequencing. Because DNA can be copied and sequenced with extraordinary sensitivity, even a few bound molecules are detectable, and their sequences reveal which structures bound. This makes a DEL vastly cheaper per compound than well-by-well screening.

The catches: only chemistry that doesn't destroy the attached DNA can be used; the DNA tag can itself nudge binding; and the readout says only _what_ bound, not _how well_ — so DEL hits must be re-made without their tag and re-tested. The idea was proposed by Brenner and Lerner in 1992 and became practical decades later, once DNA sequencing turned cheap.

## External resources
- [Brenner & Lerner, "Encoded combinatorial chemistry," *PNAS* (1992)](https://www.pnas.org/doi/10.1073/pnas.89.12.5381) — the foundational proposal to tag each library compound with an amplifiable genetic barcode.
