# AGENTS.md

SPECS.md is authoritative for everything about the vault — structure, conventions, constraints, and what else to read before working (it points to the content declaration and the reference example). **Read SPECS.md in full before your first edit.** This file only covers how to behave while working here. Where the two could overlap, defer to SPECS.md and do not restate it. 

Don't assume. If something is unclear, ask before continuing.

## Ask first, and explain

This project is also a way for me (the maintainer) to learn the domain and the system, not only to publish it. Before any non-trivial change, explain what you intend to do and why, then wait for my confirmation. *Non-trivial* means anything touching tags, `next`/`feedback` edges, whether a node exists, vocabulary, or the mechanism a body asserts; fixing prose, formatting, or typos in an existing body is trivial.

Do not assume I already know the relevant biotech, Obsidian, or graph concepts — spell out the reasoning in plain words. If something seems obvious to you, that is often exactly what's worth explaining.

When you explain, be concise and specific: state the actual point, not a description of it. Detail only where it's load-bearing; an example only when the point is otherwise ambiguous. No analogies, no jargon.

## Treat SPECS.md as authoritative but not infallible

If you find an internal inconsistency, an ambiguity, or a rule that the content seems to contradict, flag it and stop — do not silently work around it or pick an interpretation. Surfacing these is useful, not a nuisance.

## Skills name needed files by role, not path

A skill names the files it needs by their role (e.g. "the content declaration", "the reference process node"); the literal path lives once in SPECS.md (§1 for the content declaration, §6 for the reference process node). Resolve the role to a path through SPECS.md when you run a skill — do not hardcode or assume the path.

If, while running a skill, you find you need a file the skill never named for the task at hand, do not guess or read around the gap: flag it to me and wait for direction. A skill that omits a file it should name is a defect worth surfacing.

## Don't invent vocabulary

The set of stages, modalities, and aliases is fixed (SPECS.md says where it's declared). Never coin a new stage or modality on your own. If the content seems to need one, propose it, explain why, and stop — silently adding one breaks the tag/folder/page agreement across the whole vault.

## Prefer the smallest change

Default to narrating a difference inside an existing node rather than splitting; split only when the test genuinely calls for it. The natural tendency is to over-create — resist it.

## Get the substance right

Process and glossary bodies describe real mechanism for a non-specialist. Verify specifics against sources rather than writing from memory; correct, current mechanism matters more than fluent prose.

## Validation is manual

Do not run the SPECS.md §8 invariant checklist automatically after edits — it's expensive and I'll trigger it deliberately. Validation lives in a dedicated skill; run it only when I ask, and otherwise leave validation to me.

## Commits use Conventional Commits

Write commit messages in the [Conventional Commits](https://www.conventionalcommits.org/) format: `type(optional scope): description`, e.g. `docs: explain Extended Graph edge coloring` or `feat(glossary): add entry for antigen`. Use the type that fits the change (`feat`, `fix`, `docs`, `refactor`, `chore`, etc.). Commit only when asked.

## Keep instruction files agent-neutral

AGENTS.md, SPECS.md, and the skills are shared across agents. When editing any of them, write so the text holds for any agent: no first-person agent identity, no agent-specific tool names or assumptions. If you cannot keep that requirement - ask before proceeding.