---
tags:
  - type/process
  - stage/lead_discovery
  - modality/gene_editing
next:
  - "[[Editing optimization & off-target assessment (gene editing)]]"
---
Where a gene therapy adds a working copy of a gene, gene editing repairs the gene already in place — rewriting the patient's own DNA at one exact spot. The tool is [[CRISPR|CRISPR]]: a protein (Cas9) that cuts DNA, steered to a chosen site by a short _guide RNA_ whose letters match the sequence there. Design here means writing that guide and choosing which kind of editor to send with it.

Writing the guide is, on its face, just reading off the roughly 20-letter sequence that matches the target site — but two constraints make it hard. The Cas protein only acts immediately next to a short signature sequence in the DNA called a _PAM_, so an edit can only be placed where a PAM happens to sit nearby. And a guide that matches the intended site may also partially match other places in the three-billion-letter genome, where the editor would act by mistake. So many candidate guides are designed and ranked, trading on-target efficiency against the fewest close matches elsewhere.

Choosing the editor sets what kind of change is possible — narrated here as three variants of rising sophistication:
- **Nuclease editing** makes a clean cut through both DNA strands; the cell's own hurried repair usually just garbles and disables the gene — good for switching off a harmful one.
- **Base editing** uses a Cas protein that no longer cuts, fused to an enzyme that chemically rewrites one DNA letter into another (C to T, or A to G) within a small window — a precise single-letter correction with no cut, but limited to certain swaps.
- **Prime editing** fuses a copy-writing enzyme that pastes in a short, newly written sequence carried by an extended guide, allowing many kinds of correction and freer placement, though at lower efficiency.

A further variant runs through every later step: editing done _inside the body_ versus on cells taken _out_, edited, and returned. The characteristic difficulty is that a single wrong edit elsewhere in the genome is permanent and potentially dangerous — it can switch on a cancer gene — so the entire modality is built around proving the edit lands only where intended, which is the work of the next step. The output is a designed guide (or guides) and a chosen editor.
