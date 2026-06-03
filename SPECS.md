# Biotech Map Specifications

Biotech Process Map is an Obsidian vault that maps the processes of the biotech industry as a graph. 
This document defines the *conventions, rules, and constraints* the Biotech Process Map must obey.

---

## 1. Purpose of the map

The vault maps the **biotech industry as a directed graph of technical processes**, written so a curious **non-specialist** can explore it.

The intended reader of the *vault* is a motivated non-specialist, including those without a university degree in the subject or experience in the field — someone exploring which part of the industry to work in, **not** someone already in the field. They can handle real detail and real mechanism but cannot be assumed to know any field jargon; every page must be understandable end-to-end on its own terms.
The map deliberately simplifies the relationships between processes — how steps connect, branch, and group into stages — to keep the overall shape of the industry graspable for a newcomer, while keeping the processes themselves detailed, explaining real, current mechanism in depth (the reference process node sets the bar). At the same time, the language in which these details are described is plain and simple, without jargon (or it being introduced) and to the point.

The intended reader of *this document* is you and any future maintainer (human or agent): it is deliberately highly structured so it can be read, updated, and checked against. 

This document fixes the rules and constraints; the **content declaration** declares the actual content — stages (in spine order), modalities, and aliases. It is the `type/index` page, at `Content/Index.md`. This is the single place that path is recorded, so a rename of the file is reflected by editing only here; everything else refers to it by the name "the content declaration." The two documents are read together.

The vault models **conventions that are stable** while the **node set grows over time**.

---

## 2. Structure of the map

### 2.1 Nodes (six types)

A single node in an Obsidian vault is a single .md file.

| Type | Role (one line) |
|---|---|
| `index` | The vault's front door — one page; describes the map, its **content**, and lists entry points to explore. |
| `process` | A single pipeline step — the bulk of the vault. |
| `modality` | One overview page per modality; the authoritative human-readable definition of its `modality/<self>` tag. |
| `stage` | One page per stage; the authoritative human-readable definition of its `stage/<self>` tag. |
| `glossary` | One page per recurring field-specific term or technique. |
| `company` | One card per company; links to the processes (and where useful, modalities) it performs. |

This `index, process, modality, stage, glossary, company` ordering is used identically in §2.2 (Properties) and §7 (Content).

### 2.2 Properties (frontmatter)

Obsidian shows YAML frontmatter as **Properties**. The three classification dimensions — **type**, **stage**, **modality** — are all encoded as **tags** inside `tags:`.

Which tags each node type carries:

| Type | `type/` tag | `stage/` tag | `modality/` tag(s) | `next` / `feedback` |
|---|---|---|---|---|
| index | `type/index` | — | — | — |
| process | `type/process` | **exactly one** | **≥ 1** (every riding modality) | yes (0+ each) |
| modality | `type/modality` | — | `modality/<self>` | — |
| stage | `type/stage` | `stage/<self>` | — | — |
| glossary | `type/glossary` | — | — | — |
| company | `type/company` | — | — | — |

Frontmatter templates:

```yaml
# index
---
tags:
  - type/index
---
```

```yaml
# process
---
tags:
  - type/process
  - stage/<one stage slug>        # exactly one
  - modality/<m1>                 # one line per riding modality (>=1)
  - modality/<m2>
next:
  - "[[Exact target filename]]"   # 0+; omit the key entirely if none
feedback:
  - "[[Exact earlier filename]]"  # 0+; omit the key entirely if none
---
```

```yaml
# modality
---
tags:
  - type/modality
  - modality/<self>
---
```

```yaml
# stage
---
tags:
  - type/stage
  - stage/<self>
---
```

```yaml
# glossary
---
tags:
  - type/glossary
---
```

```yaml
# company
---
tags:
  - type/company
---
```

Slug format. Stage and modality slugs are snake_case (lowercase, words joined by underscores); Obsidian tags allow neither spaces nor most punctuation. The slug is derived from the page title deterministically: lowercase, replace spaces and hyphens with underscores, drop other punctuation. So Lead discovery → tag stage/lead_discovery → folder Treatments/Processes/lead_discovery/. The tag slug, the folder name, and the snake_case of the stage/modality page title always agree.

Node titles are unique across the whole vault (Obsidian resolves a bare [[Title]] by filename, so duplicates in different folders collide). Because slugs are derived by collapsing case and separators, slugs must be unique too: Lead discovery, Lead-discovery, and lead discovery all collapse to lead_discovery and would clash on both tag and folder.

### 2.3 Process relations: `next` and `feedback`

- **`next`** — forward progression: this process feeds the next one.
- **`feedback`** — an iteration loop back to an earlier process; the edge lives on the later node and points back to a process sharing at least one `modality/` tag with it. That shared modality is the one the loop belongs to (a multi-modality node may carry separate `feedback` edges for different modalities).
- A process may have several `next` edges (where modalities diverge), but for **any single modality, at most one successor carries that modality tag** — this is what keeps each modality's chain linear (§4.1, invariant 8).
- Both are lists of quoted wikilink strings equal to the target's exact filename.

**The root node.** All modalities share one root node: the single `type/process` node every modality's chain begins at. It is the `next`-target of no other node (but can be a `feedback` target), sits in the first `stage/` of the spine, and — because every modality's chain begins there — carries every `modality/` tag in the vault. Which node plays this role is recorded in the content declaration / index (§7.1); this document refers to it only as the root node. It is the first node in each modality's stage-ordered list (§7.3).

**The terminal node.** All modalities share one terminal: the single `type/process` node every modality's chain ends at. It carries stage/patient, lives in Treatments/Processes/patient/, has no `next` (but can have `feedback`), and — because every modality's chain ends there — carries every modality/ tag in the vault. Which node plays this role is recorded in the content declaration / index (§7.1); this document refers to it only as the terminal node. The patient stage is the final stage in the @Index.md stage order and has its own type/stage page like any other stage — that stage page is distinct from the terminal process node.

## 3. Folder layout

Folders are for **human browsing** — tags and edges (typed links) do everything the software acts on. Filenames = node titles exactly, so `[[Title]]` resolves.

```
Content/                                # Vault Root
  Index.md                              # type/index
  Treatments/
    Processes/
      <stage1>/                         # each process file lives in the subfolder
      <stage2>/                         # matching its single stage/ tag
      ...
    Modalities/                         # type/modality pages
    Stages/                             # type/stage pages
  Glossary/                             # type/glossary pages
  Companies/                            # type/company pages
```

`Glossary/` and `Companies/` sit at the **vault root, outside `Treatments/`**, so they can be shared with a future *Diagnostics* branch (not currently implemented) - a glossary term, or a company, may touch both treatment and diagnosis. `Modalities/` and `Stages/` are treatment-specific and stay under `Treatments/`.

**Illegal filename characters**. Because the filename doubles as the wikilink target, avoid every character Obsidian or the filesystem treats specially: / \ : * ? " < > |, plus # ^ [ ], which carry meaning inside wikilinks. Biotech titles often reach for a colon (e.g. CRISPR: base editing); reword to a plain title (CRISPR base editing) instead. If a title would naturally contain one of these characters, reword it — never escape or substitute the character.

---

## 4. Rules

### 4.1 Modality scope (a modality tag → its entire pipeline)

A process node lists a `modality/` tag for **every** modality whose pipeline includes it. A fully shared step therefore lists *all* applicable modality tags. This is what makes a single modality-tag filter surface that modality's *whole* pipeline, research through delivery, including steps it shares with others.

Filtering to any single `modality/<slug>` yields one linear next chain from that modality's root to `Patient` (`feedback` aside). Forks exist only between modalities — where shared modalities diverge or re-merge — never within one.

**Sharing is by genuine similarity, not adjacency.** Two modalities share a node only when their work at that step is the same *kind* of work, narratable as one body with inline variants. A step that is a *wholesale-different process* for a modality is its own node even when the steps immediately before and after are shared (a peptide's solid-phase synthesis is not a small molecule's chemical route). The isolated-edit rule (§4.3) folds *variants of one step* — never two distinct processes.

### 4.2 Glossary term criteria

Create a `type/glossary` entry for a field-specific term or technique that is important — a key detail of at least one process — and is either recurring across processes or needs a deeper explanation than fits inline. A term that is used once and fully explainable in a clause stays inline; a term that recurs, or that needs real depth to understand, earns a page. Link it on first use **within each document**, e.g. `[[Lipid nanoparticle]]`. 

- **Do not** create entries (or link) for terms a general reader already knows: DNA, gene, protein, cell, virus, bacteria, molecule, RNA in the generic sense. The exception is a word a general reader knows by name but not by mechanism, where that mechanism is important enough to deserve its own description (e.g. `Clinical Trials`).
- **Do** create them for field-specific terms or distinctions (e.g. messenger vs silencing RNA, a specific named technique).

### 4.3 Modality / node granularity

Model each modality's pipeline as an ordered sequence of process nodes (stage order, following `next`). Comparing two modalities is a sequence alignment — like Levenshtein distance over strings, where each node is one character. An **edit** is one node-level operation needed to turn one modality's sequence into the other's: substitute a node, insert a node, or delete a node. Shared nodes (those carrying both `modality/` tags) are the matches. A **run** is a maximal stretch of consecutive edits in that alignment — edits not separated by a matching node.

**Modality test.** Take the candidate's nearest neighbor — the existing modality with the smallest edit distance, i.e. the one you'd otherwise merge it into (state which neighbor you used on the modality page when it isn't obvious). Then:
- If the alignment contains a **run of 2 or more consecutive edits** (more than one contiguous edit) → the two are genuinely distinct; give the candidate its own `modality/` tag.
- Otherwise — every difference is an isolated single edit, however many of them — they are the same modality; **merge**, and narrate each isolated difference inline in the shared pages.

**Process-node corollary.** The same alignment decides whether a candidate step earns its own node or folds into an adjacent one. A candidate step is its own node iff **either**:

- (a) it lies within a run of 2+ consecutive edits between two modalities (the run that makes them distinct above), **or**
- (b) it falls in a different `stage/` than the node it would otherwise merge into — a node carries exactly one stage tag, so a stage boundary always forces a node boundary.

Otherwise fold it into its neighbor and narrate the difference inline.

Equivalently: **node boundaries exist only where forced** — by a stage change, or by a modality divergence of length ≥ 2.

**Editorially justified splits.** A single stage may hold more than one node for the same modality set (consecutive, with no fork or merge between them) only when the split is genuinely justified: the steps are *distinct work* **and** each is *substantial enough to stand as its own page* (the reference process node sets the bar). The clinical-trial phases are the canonical case. A split failing either test — not genuinely distinct, or too thin to fill a page — is unforced and must be merged, the difference narrated inline (§6).

*Example.* Modality A = n1·n2·n3·n4·n5, modality B = n1·n2·X·Y·n5. The alignment substitutes n3→X and n4→Y: a run of 2 → A and B are distinct
modalities. But if B were n1·X·n3·Y·n5 (two single edits separated by the shared n3), that's two isolated edits, no run of 2 → same modality; X and Y are narrated inline rather than splitting the tag.

### 4.4 Modality-group criteria (aliases)

Aliases are **documentation shorthand** for sets of modalities that share nodes worth referring to collectively. They are convenient when talking about the vault and when reasoning about shared nodes. **Files never contain aliases** — every `modality/` tag in a file is explicit.

A group earns an alias when its members share nodes that you find yourself referring to repeatedly. @Index.md should list all available aliases.

---

## 5. User experience

How a reader actually works the vault.

### 5.1 Defaults
In default UX, the user should be able to focus on the processes. Because of that, modalities, stages, glossary terms, and companies are hidden by default.

### 5.2 Explore the graph
Open Graph view. Nodes are colored by stage, (stages are listed in @Index.md) giving an at-a-glance sense of where any process sits in the pipeline.

### 5.3 Walk a pipeline
Extended Graph colors edges by type (typed links), so `next` and `feedback` render in different colors — follow the `next` color forward from root toward `Patient`. `feedback` is shown by default; Extended Graph's link-type filtering can **toggle `feedback` off** to collapse the graph to the clean spine.

### 5.4 Filter by modality / stage / both
A single tag query `tag:#modality/<slug>` shows that modality's **entire** pipeline, because shared nodes carry the tag (§4.1). `tag:#stage/<slug>` shows one stage across all modalities. Combine the two for a precise subgraph.

### 5.5 Look up a term or technique (glossary)
Open the glossary page for the term. Its **backlinks** list every process that uses it — a live answer to "where in the industry is this used."

### 5.6 Find the companies for a process (or the processes for a company)
Open a process node and look at its **backlinks**, filtered to `type/company` → the companies that perform that step. Or open a **company card** to see everything it does. (Because company→process is a plain link rather than a typed relation, these connections appear in **backlinks**, and are not colored as typed edges in the graph — by design.) A process node's backlinks also surface the modality and stage pages that reference it.

### 5.7 Plugin / graph setup
- **Extended Graph:** enable the *links* feature and assign each link type — `next` and `feedback` — its own color, so edges are distinguishable by type; link-type filtering can hide `feedback` independently (this is what lets §5.3 collapse to the spine).
- **Graph view → Groups:** one group per stage, query `tag:#stage/<slug>`.

---

## 6. Writing style

The voice for every **body**, written for the §1 non-specialist.

**The explain-or-glossary rule:** anything that needs explaining — a piece of jargon, a tool, an instrument, a technique — is either explained inline in plain words at the moment it appears, or carries a `[[glossary term]]` whose body explains it. Nothing that needs explaining is left bare. This rule underlies the bullets below.

- **Tell it as it is actually done.** If the work runs in steps, write them in order ("First… Then… Next…"); if the work itself splits into parallel or alternative paths, let the body of the page follow it. There is **no required section structure** — let the real shape of the work dictate the shape of the text.
- **Plain language, real mechanism, avoid or gently introduce jargon.** Explain how things actually work in everyday words. Do not hide mechanism behind jargon, and **do not use analogies or metaphors** — describe the real thing literally. When jargon is unavoidable, introduce it per the explain-or-glossary rule above.
- **Glossary sufficiency.** A glossary body must be complete enough that any linking page can rely on it in place of an inline explanation: whatever a page defers to [[a term]] must actually be covered there. Since a term is shared across processes, modalities, and potentially branches (§3), its body serves the union of what its linkers offload to it — not any single page, and not scoped to one modality as a process body is. 
- **Tools, data, and instruments belong inside the story** — mentioned naturally at the moment they are used, and made clear per the explain-or-glossary rule above.
- **Cover the substance, woven in, not labeled:** what the step is trying to achieve and what "good" means here; how it is done; and the specific way it is hard or fails — the concrete failure mode (what breaks, and why the method does not catch it), not a general gesture at difficulty. Provide modern mechanism (how hard parts are overcome now), not history. A step explained without its characteristic difficulty is under-detailed even if it reads clearly. These appear as narrative, not headers.
- **Length:** process bodies should be long enough to be genuinely clear end-to-end. Clarity beats brevity; never sacrifice understandability to hit a count. However, try to have short process bodies (<1000 words), and if some step is genuinely important for it, consider whether adding it to the Glossary. Other node types are as long as their content needs.
- **A process body focuses on the modalities tagged on it and differentiates between them when processes diverge by modality.** A reader filtering to one modality must encounter all the steps relevant to it, and be able to clearly understand whether a block of text relates to filtered modality or not.
- **Narrate sub-variants that run through the process.** A modality often contains variant paths that are not themselves modalities — different targets the same kind of drug can be aimed at, or different ways one step resolves — that §4.3 has decided not to split into their own node or tag. When such a distinction changes how several steps behave, name each variant once and carry it through every step it touches, making clear at each point which variant a passage describes. These live entirely in the prose; they never become a `modality/` tag or a node.
- **Use the vault's markers for shape and emphasis.** When a process runs in discrete steps, give each step a short **bold lead-in** that names it, so the skeleton is visible at a glance — this is compatible with having no fixed section structure, since the steps come from the work itself. Use _italics_ to mark a term at the moment it is defined or contrasted, and to set off the specific question a step answers. Reserve both for that; they are not decoration.
- **Ground scale in real quantities where they matter.** When how many, how long, or how costly is part of understanding a step — counts going in, how many survive a filter, rough time or expense — give real figures or honest ranges rather than vague quantifiers. Numbers are part of the mechanism, not optional color; where exact values vary or are unknown, an order-of-magnitude range beats none.

Use the **reference process node** — `Content/Treatments/Processes/lead_discovery/In silico protein design.md` ([[In silico protein design]]) — and its corresponding Glossary terms as the reference example of a well-written process: it explains every critical detail without hiding it behind jargon, and links glossary terms for difficult concepts. This is the single place that path is recorded, so a rename is reflected by editing only here; everything else refers to it as "the reference process node."

---

## 7. Content (what each node type's body should contain)

### 7.1 Index
The vault's front door (one `type/index` page). Contains: a short plain-language description of what the map is and how to read it; a link to the **shared root node** (§2.3) as the single entry point to the graph and a link to the **shared terminal node** (§2.3) as the shared end point; links to **all modality pages**, **modality group aliases**, and **all stage pages** (including stage order from the root node to the patient stage); pointers to `Glossary/` and `Companies/`; and a brief legend (stage colors, what `next`/`feedback` mean, how to filter by modality/stage). A pointer to this reference document is welcome.

### 7.2 Process
A plain-language, step-by-step story of how the process actually happens, per §6: real mechanism, no analogies, tools woven in, glossary terms linked on first use, goal/method/hard-parts carried implicitly in the narrative, <1000 words, **covering only the modalities tagged on the node**.

### 7.3 Modality
Light structure is earned here, because the content naturally splits in two:
1. a **plain-language overview of how the modality works** — what kind of thing the drug is, and the mechanism by which it acts on the body;
2. an **ordered list of that modality's nodes, grouped by stage** (where the first node is the shared **root node** (§2.3); stage order from @Index.md), each a link.

This page is the **authoritative human-readable definition** of the `modality/<self>` tag. The list is derived by selecting process nodes that carry this modality tag and ordering them by stage and `next`.

### 7.4 Stage
Mirrors the modality page:
1. a **plain-language explanation of what this stage is** — the question the industry is answering at this point in the pipeline, and what "done" looks like to move to the next stage;

This page is the **authoritative human-readable definition** of the `stage/<self>` tag.

### 7.5 Glossary
The story of one term or technique in the §6 voice — **what it is, how it works, and why it matters** in the industry. One flowing explanation by default; break into sections only if the content genuinely splits. Created as per §4.2.

**Substance.** Same bar as a process body (§6): real, current mechanism in plain words. Two failures specific to short definitional bodies are not allowed:
- *Gesturing instead of naming.* Where a real named principle, criterion, method, or quantity governs the thing, name it — never a vague placeholder. If off-targets are chosen by a rule (structural homologs, paralogs, known-liability proteins), say which; if an enzyme does more than speed a reaction (binds and orients the reactants, stabilizes the transition state, may make the reaction possible at all), say what it actually does. A merely incomplete one-line definition is wrong here.
- *Circular or self-referential wording.* Never define a thing with itself ("oily patches meet oily patches"). Use the direct standard term (hydrophobic) and explain that term once, plainly.

Build a difficult concept up from the fundamentals a newcomer needs first, in order — do not assume the hard idea (e.g. diffusion) is already understood. Link every other glossary term on its first appearance, including foundational ones the page leans on (e.g. `[[in silico]]`) — these are missed most often.

**External resources.** End the body with a section titled exactly `External resources` (fixed label). The bar is *canonical, not convenient*, organized by tier:
- *On-ramp* — the best comprehensive-yet-digestible treatment by a recognized authority: a course, lecture, or video that teaches the topic from the ground up and that you'd genuinely recommend to someone learning it.
- *Foundation* — the canonical primary source: the original or definitive paper, highly cited, that introduced the idea the industry now uses.

Prefer a few excellent links over many — quality over coverage, do not pad. Exclude encyclopedia entries, vendor/marketing white papers, SEO blog posts, and mid-tier reviews that are neither the best on-ramp nor a foundational source. If nothing clears the bar for a tier, omit that tier; if nothing clears it at all, omit the section.

### 7.6 Company
A card for one company:
1. **what it is** — a brief, plain, factual description (who they are, focus area), lay-readable;
2. **what it does in the map** — a list of **plain wikilinks** to the process nodes it performs (and, where useful, modality pages), ideally annotated with a few words on what they do at each step.

The plain links are deliberate: they generate the backlinks used to find a node's companies (§5.6). A company's `modality/stage` coverage is **discovered via its linked processes**, not duplicated as tags on the card (so it cannot drift out of sync).

**Which companies earn a card.** The company set serves the §1 reader deciding where to work, so a card is reserved for places at the frontier — somewhere you'd want to work to be on the edge of pharma. A company qualifies if it is either:
- an **established global player** — large or mid-cap pharma/biotech with global reach;
- an **emerging leader** — venture-backed at **Series A or later**, credibly advancing a modality or technique, shown by a named lead programme, notable funding, or a distinctive platform; or
- a **notable service company** — a leading CRO/CDMO or similar that performs map processes at scale (trial operations, manufacturing, etc.), where a reader might genuinely work.

Exclude seed-stage or unproven outfits, pure holding/marketing entities, and defunct companies. **Curate, don't enumerate:** prefer a representative set of notable performers per process over exhaustive coverage (cf. §7.5, "a few excellent over many").

**Geographic balance.** Do not default to US companies. Cover the major hubs — the US, Europe, and Asia (notably China and Japan) — and actively include **European** biotech, the hub most routinely overlooked. Record HQ explicitly so the balance is visible.

**Record scale.** Right after "what it is," each card carries an explicit `Scale:` line giving the company's maturity (public, or private + latest funding round), approximate headcount, and HQ — e.g. `**Scale:** Private, Series C · ~250 staff · HQ Cambridge, UK (as of 2026)`. Keep figures coarse and date them ("as of YYYY"); they go stale. Scale is factual metadata only — process coverage is still discovered via links, never duplicated as tags.

## 8. Invariants (validation checklist)
Each is binary and verifiable by inspection; a violation in a completed vault means it is malformed. During construction, reachability invariants (7, 8) may fail transiently and should be checked once a modality's chain is complete.

1. Every node carries exactly one `type/` tag.
2. Every `type/process` node carries exactly one `stage/` tag and at least one `modality/` tag.
3. Every process file sits in `Treatments/Processes/<stage>/` matching its single `stage/` tag; that folder name equals the stage slug (§2.2).
4. Every stage slug appearing under `Treatments/Processes/` has a matching `type/stage` page under `Treatments/Stages/`.
5. Every `next/feedback` target is an existing node file (no dangling links). 
6. `feedback` always points to an earlier process; `next` always points forward.
7. Following `next` (ignoring `feedback`) from any process eventually reaches the terminal node (§2.3).
8. Filtering to any single `modality/<slug>` yields one linear next chain from that modality's root to the terminal node (§4.1).
9. The terminal node carries `stage/patient` and every `modality/` tag in the vault.
10. Every `glossary` term linked in any body has a `type/glossary` file.
11. Every link on a company card resolves to an existing node; the card carries `type/company` and no `stage/`/`modality/` tags.
12. Files contain no aliases — every `modality/` tag is explicit (§4.4).
13. Every `modality/` tag appearing on a process has a matching `type/modality` page under `Treatments/Modalities/`.
14. Every node title is unique across the vault; every stage and modality slug is unique.
15. `stage/` and `modality/` tags appear only on process nodes and on the self-tag of their own `stage/modality` page; `next`/`feedback` appear only on process nodes.
16. Every `feedback` edge points to a process that shares at least one modality/ tag with its source.
17. **No unforced node boundary (§4.3).** For any `next` edge X → Y where X has exactly one successor, Y exactly one predecessor, and X and Y carry identical `modality/` tag sets, X and Y must **either be in different `stage/` tags, or be an editorially justified split (§4.3: genuinely distinct work, each substantial enough for its own page)**. Otherwise the boundary is unforced and the two must be merged, the difference narrated inline (§6).
18. **Glossary sufficiency (§6).** For every [[glossary term]] link in any body, the concept the linking page defers to that link — the thing it would otherwise have had to explain inline — is explained in the linked glossary file's body. No page relies on a glossary term for an explanation the term's body does not actually provide.