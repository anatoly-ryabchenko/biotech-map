---
tags:
  - type/process
  - stage/lead_discovery
  - modality/cell_therapy
next:
  - "[[Viral vector engineering]]"
---
A cell therapy turns living immune cells — usually T cells, the immune system's killers — into a drug by giving them a new receptor that makes them recognize and destroy diseased cells, most often cancer. This step designs that receptor; building it into real cells comes later. There are two variants.

A [[Chimeric antigen receptor|chimeric antigen receptor]] (CAR) is a synthetic receptor stitched together from parts of several proteins. Its outward-facing end is a binder — typically an _scFv_, the grabbing tips of a [[Monoclonal antibody|monoclonal antibody]] fused into one compact unit — chosen to latch onto a marker on the surface of the diseased cell. That binder connects, through a hinge and a segment that spans the cell membrane, to signaling parts inside the cell: the core "fire" signal (from a piece called CD3ζ) plus one or two _costimulatory_ domains (from 4-1BB or CD28) that set how strongly the cell switches on and how long it survives afterward. 4-1BB tends to give slower, longer-lived cells; CD28 faster, more intense ones. This wiring is the chief design lever.

The other variant is an engineered _T-cell receptor_ (TCR-T): rather than a synthetic receptor reading surface markers, the cell is given a natural-style receptor re-engineered to recognize small protein fragments displayed on the cell's surface. This reaches targets _inside_ the diseased cell that a surface-only CAR cannot see, but works only for patients whose tissue type matches the receptor.

The characteristic difficulty is choosing a target marker truly confined to diseased cells. Because the engineered cell kills everything carrying its marker, a target that also appears on healthy tissue causes serious, sometimes fatal, on-target damage — so most of the design risk lives in the choice of what the binder aims at, not in the wiring. A second concern designed for here is an off-switch: a way to shut the cells down if they over-react. The output is a finished receptor design, ready to be built into cells.

The same receptor designs can also be delivered without removing any cells, by injecting a vector that engineers the patient's T cells inside the body (in-body CAR-T). Because the work from there on is gene-therapy work, it is narrated under [[Gene therapy]], beginning at [[Transgene & cassette design (gene therapy)]].
