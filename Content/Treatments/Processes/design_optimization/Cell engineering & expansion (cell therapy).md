---
tags:
  - type/process
  - stage/design_optimization
  - modality/cell_therapy
next:
  - "[[Cryopreservation & cell product formulation]]"
feedback:
  - "[[CAR-TCR construct design (cell therapy)]]"
---
This step physically builds the living drug: it takes the receptor designed earlier, puts it into real T cells, and grows those cells into a dose. For an _autologous_ therapy — the common case — the cells are the patient's own, so the whole thing is a personalized manufacturing run for one person.

The work runs in steps. First, _collection_: T cells are drawn from the patient's blood by a machine that filters out the white cells and returns the rest (a process called leukapheresis). Next, _activation_: the resting T cells are woken up — usually with tiny beads coated in the signals a T cell normally meets when called into action — so they begin dividing and will take up new genes. Then _gene delivery_: the receptor gene is inserted, most often by infecting the cells with a [[Lentiviral vector|lentiviral vector]], a stripped-down virus that splices the gene permanently into the cell's own DNA so every daughter cell inherits it; increasingly the gene is instead placed at a chosen spot using [[CRISPR|CRISPR]]. Finally, _expansion_: the engineered cells are grown in a bioreactor for one to two weeks until there are enough — often a hundred-fold increase or more — to treat the patient.

The characteristic difficulty is that the starting material is a sick patient's own cells, which differ from person to person and are often few, exhausted, or damaged by prior chemotherapy — so the identical process gives different results each run, and a batch can simply fail to grow. The cells must also stay healthy and "young" enough during expansion to work once returned; pushing them to over-grow wears them out and weakens the therapy. Because each batch is one patient's only medicine, there is no pooling and no second attempt without starting over. The output is a population of engineered cells of sufficient number and quality, ready to be frozen and formulated.
