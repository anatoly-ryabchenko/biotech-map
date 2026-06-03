---
name: update-graph
description: >-
  Apply a validated graph change to the vault — create, edit, move, rename,
  split, or merge process nodes; rewire next/feedback edges; propagate
  modality-tag ripples; and update the affected modality, stage, and Patient
  pages. Use when the maintainer hands over a final, SPECS-reviewed change
  description to execute. Not for proposing or designing changes.
---

Apply a validated graph change to the vault. The input is a change description in final form — already reviewed against SPECS.md. Execute it faithfully and completely.

---

## 0. Before anything else

Read these files before touching anything:

- `SPECS.md` — authoritative for every rule below; if anything in this skill and SPECS.md conflict, SPECS.md wins.
- The content declaration (SPECS.md §1 names it and gives its path) — the live list of stages (in spine order), modalities, and aliases. Called "the content declaration" below.

Then re-read the change description carefully and identify every operation it contains: creates, edits, moves, renames, splits, merges, tag changes, edge rewirings.

---

## 1. Hard stops — report and do nothing if any of these apply

Stop immediately and report the specific problem to the user; do not proceed:

- The change names a stage slug that does not appear in the content declaration.
- The change names a modality slug that does not appear in the content declaration.
- The change names a node as a `next`/`feedback` target and that file does not exist in the vault.
- The change is ambiguous: two or more reasonable readings produce different vault states.
- The change contradicts a SPECS.md rule (e.g., would create a node with two `stage/` tags, or put a `feedback` edge on the earlier node, or leave a modality chain non-linear).

If none of these apply, proceed through the sections below in order.

---

## 2. Slug derivation

When you need a stage or modality slug from a human-readable name: lowercase, replace spaces and hyphens with underscores, drop other punctuation. Verify against the content declaration — the slug must already be declared there.

---

## 3. Create a new process node

1. Determine the stage slug from the change. Derive the folder: `Content/Treatments/Processes/<stage_slug>/`.
2. Filename = the node title exactly (no extension tweak; Obsidian resolves `[[Title]]` by filename).
3. Write the file with this frontmatter:

```yaml
---
tags:
  - type/process
  - stage/<stage_slug>
  - modality/<m1>
  - modality/<m2>          # one line per modality; ≥ 1
next:
  - "[[Exact target title]]"   # omit key if none
feedback:
  - "[[Exact earlier title]]"  # omit key if none; on the *later* node
---
```

4. Write the body per SPECS.md §6–7.2 (real mechanism, plain language, no analogies, tools woven in, glossary terms linked on first use, <1000 words, covering only the tagged modalities).
5. Wire both endpoints (§5 below).
6. Update modality and stage pages (§6 below).

---

## 4. Edit an existing process node

Open the file. Apply only what the change specifies — body text, tag additions/removals, edge additions/removals. Do not alter anything not mentioned. After editing, wire/unwire edges at both endpoints and update modality/stage pages as needed.

---

## 5. Move / rename a process node

A rename is a move: the old filename is the old title, the new filename is the new title.

1. Create the new file at the correct path with the new title.
2. Copy content from the old file; apply any additional edits from the change.
3. Find every file in the vault that references the old title in `next:`, `feedback:`, or body `[[old title]]` links. Update each reference to `[[new title]]`.
4. Delete the old file.
5. Wire edges and update modality/stage pages.

To find inbound references: grep the `Content/` tree for `[[old title]]` (case-sensitive, because Obsidian wikilinks are case-sensitive on most filesystems).

---

## 6. Split a node into two

The change will name the original node and the two new nodes (with titles and stages).

1. Create both new files per §3.
2. Redirect all inbound `next`/`feedback` links that pointed to the original: those that logically now point to the first half go there; those that logically now point to the second half go there. The change description must make this assignment clear — if it does not, stop (hard stop §1, ambiguous).
3. Wire the `next` edge from the first new node to the second.
4. Delete the original file.
5. Update modality and stage pages.

---

## 7. Merge two nodes into one

The change will name the two source nodes and the surviving node.

1. The surviving node gets the union of modality tags from both sources.
2. All inbound `next`/`feedback` links that pointed to either source must be redirected to the surviving node.
3. The surviving node inherits `next` edges (deduplicated) from both sources.
4. Body: merge content per the change description.
5. Delete the node that does not survive.
6. Update modality and stage pages.

---

## 8. Propagate modality-tag ripples

When a node gains or loses a modality tag, that change must propagate to every node on the continuous shared run for that modality.

**Gaining a modality:** identify the contiguous run of nodes already sharing the affected modality and the surrounding context. Every node in that shared run must gain the new modality tag.

**Losing a modality:** the reverse — every node in the shared run must lose the tag, unless it carries the tag for a reason independent of the run.

To find the run: follow `next` edges forward and backward from the changed node, collecting nodes that carry the same modality tag, stopping at divergence points.

---

## 9. Wire and verify edges

For every `next` or `feedback` edge added or removed:

- **Add `next` A → B:** add `"[[B]]"` to A's `next` list. No change needed on B (the edge lives on the source node only).
- **Add `feedback` A → B (A is later, B is earlier):** add `"[[B]]"` to A's `feedback` list. Confirm A and B share at least one `modality/` tag.
- **Remove an edge:** delete the entry from the source node's `next` or `feedback` list. If the list becomes empty, remove the key entirely.
- **No dangling links:** every entry in `next` and `feedback` must correspond to an existing file. Verify before writing.

---

## 10. Update modality pages

For each modality page whose pipeline changes (a node was added, removed, renamed, or reordered):

- Open `Content/Treatments/Modalities/<Modality page title>.md`.
- Find the ordered node list (grouped by stage). Update it: add new nodes in stage order, remove deleted nodes, rename renamed nodes, reorder if `next` chain order changed.
- Stage order is the spine order from the content declaration.

---

## 11. Update stage pages

For each stage page whose node list changes:

- Open `Content/Treatments/Stages/<Stage page title>.md`.
- Update the ordered list of processes: add, remove, or rename as needed.

---

## 12. Update the Patient node

If any modality is added to the vault (new modality page created), add its tag to `Content/Treatments/Processes/patient/Patient (treatment delivered).md`. The Patient node must carry every `modality/` tag in the vault.

---

## 13. Output

After completing all changes, output a list of every file touched, with a one-line reason for each:

```
CREATED   Content/Treatments/Processes/design_optimization/Example node.md — new process node
EDITED    Content/Treatments/Processes/lead_discovery/Antibody discovery.md — added next edge to new node
EDITED    Content/Treatments/Modalities/Antibody (biologic).md — added new node to pipeline list
EDITED    Content/Treatments/Stages/Lead discovery.md — added new node to stage list
```

Use verbs: CREATED, EDITED, MOVED, DELETED, RENAMED.
