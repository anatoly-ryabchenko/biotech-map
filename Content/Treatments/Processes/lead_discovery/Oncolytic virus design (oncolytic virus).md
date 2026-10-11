---
tags:
  - type/process
  - stage/lead_discovery
  - modality/oncolytic_virus
next:
  - "[[Oncolytic virus engineering (oncolytic virus)]]"
---
An oncolytic virus is a virus engineered to infect and burst cancer cells while sparing healthy ones — and, just as importantly, to alert the immune system to the tumor as it does so. It is two things at once: a self-amplifying drug (each infected cell that bursts releases a fresh wave of virus into the tumor) and an immune trigger. This step chooses the starting virus and sets the broad design; the detailed engineering follows.

The first choice is the _backbone_ — which virus to build on. Herpes simplex virus (the basis of talimogene laherparepvec, the first oncolytic virus approved in the US and Europe; China approved an adenovirus-based one in 2005) and adenovirus are common picks, chosen because they are well understood, have room to carry added genes, and can be controlled.

The design then pursues two aims. The first is _tumor selectivity_: making the virus multiply in cancer cells but stall in normal ones. This is achieved by deleting viral genes the virus needs only when growing in a healthy cell — cancer cells, dividing rapidly and with their own antiviral defenses already broken, supply those functions themselves, so a virus stripped of them can thrive only inside a tumor. (Talimogene, for example, lacks the herpes gene _ICP34.5_, which the virus needs to switch off a healthy cell's built-in antiviral brake, a protein called PKR; many cancer cells have already lost that brake, so the stripped virus grows in them but stalls in normal cells. Viruses built on vaccinia use a different deletion — the _thymidine-kinase_ gene, for an enzyme that makes DNA building blocks — which confines them to fast-dividing cells that make plenty of that enzyme themselves.) The second aim is _arming_: inserting a gene that makes the infected tumor broadcast an immune-recruiting signal — most often GM-CSF, a molecule that pulls in and matures the immune cells which then learn to attack the cancer throughout the body.

The characteristic difficulty is a built-in tension: the more the virus is weakened for safety, the less vigorously it spreads and kills; but a virus left strong enough to clear a tumor risks harming healthy tissue, or being wiped out by the body's antiviral defenses and pre-existing immunity before it can work. Design is the search for a backbone and a set of deletions that keep the virus tumor-confined yet still potent. The output is a chosen backbone and a planned set of genetic changes, ready to be engineered.
