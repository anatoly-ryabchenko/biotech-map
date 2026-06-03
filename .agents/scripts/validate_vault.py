#!/usr/bin/env python3
"""
Vault invariant checker — SPECS.md §8 (invariants 1–17).
Run from the repository root (the directory containing Content/).
"""
import re, sys
from pathlib import Path
from collections import defaultdict

sys.setrecursionlimit(5000)
VAULT_ROOT = Path("Content")

if not VAULT_ROOT.exists():
    sys.exit("Error: Content/ not found. Run from the repository root.")

# ── Frontmatter parser ──────────────────────────────────────────────────────

try:
    import yaml as _yaml
    def _parse_fm(fm_text):
        return _yaml.safe_load(fm_text) or {}
except ImportError:
    def _parse_fm(fm_text):
        fm = {}
        # tags: list form
        m = re.search(r'^tags:\s*\n((?:[ \t]+-[^\n]+\n?)+)', fm_text, re.MULTILINE)
        if m:
            fm['tags'] = [re.sub(r'^[ \t]+-\s*', '', l).strip()
                          for l in m.group(1).splitlines() if l.strip()]
        else:
            # tags: inline form  tags: [a, b, c]
            m2 = re.search(r'^tags:\s*\[([^\]]+)\]', fm_text, re.MULTILINE)
            if m2:
                fm['tags'] = [t.strip() for t in m2.group(1).split(',')]
        for key in ('next', 'feedback'):
            km = re.search(rf'^{key}:\s*\n((?:[ \t]+-[^\n]+\n?)+)', fm_text, re.MULTILINE)
            if km:
                # keep raw items; title extraction happens later
                fm[key] = [l.strip().lstrip('- ').strip('"\'')
                            for l in km.group(1).splitlines() if l.strip()]
        return fm

def parse_file(path):
    text = path.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n?', text, re.DOTALL)
    if not m:
        return {}, text
    try:
        fm = _parse_fm(m.group(1))
    except Exception:
        fm = {}
    return fm, text[m.end():]

_WIKILINK = re.compile(r'\[\[(.+?)\]\]')

def extract_title(raw):
    """Extract title from '[[Title]]' or 'Title' strings."""
    hit = _WIKILINK.search(str(raw))
    return hit.group(1).strip() if hit else str(raw).strip()

# ── Load vault ──────────────────────────────────────────────────────────────

nodes = {}        # title -> {path, tags, next, feedback, body}
_dup_errors = []

for md_path in sorted(VAULT_ROOT.rglob('*.md')):
    title = md_path.stem
    if title in nodes:
        _dup_errors.append(f"Duplicate title '{title}': {md_path}  vs  {nodes[title]['path']}")
        continue
    fm, body = parse_file(md_path)
    tags = fm.get('tags') or []
    if isinstance(tags, str):
        tags = [tags]
    tags = [str(t).strip() for t in tags]

    raw_next = fm.get('next') or []
    raw_fb   = fm.get('feedback') or []
    if isinstance(raw_next, str): raw_next = [raw_next]
    if isinstance(raw_fb,   str): raw_fb   = [raw_fb]

    nodes[title] = {
        'path':     md_path,
        'tags':     tags,
        'next':     [extract_title(x) for x in raw_next],
        'feedback': [extract_title(x) for x in raw_fb],
        'body':     body,
    }

# ── Helpers ─────────────────────────────────────────────────────────────────

def type_of(n):    return [t for t in n['tags'] if t.startswith('type/')]
def stage_of(n):   return [t for t in n['tags'] if t.startswith('stage/')]
def modal_of(n):   return [t for t in n['tags'] if t.startswith('modality/')]

def is_process(n): return 'type/process' in n['tags']

# ── Build next / predecessor graphs ─────────────────────────────────────────

nxt   = defaultdict(set)   # title -> set of next titles (resolved)
preds = defaultdict(set)   # title -> set of predecessor titles via next

for title, n in nodes.items():
    for tgt in n['next']:
        if tgt in nodes:
            nxt[title].add(tgt)
            preds[tgt].add(title)

# ── Reachability ─────────────────────────────────────────────────────────────

def descendants(start):
    """Titles reachable from start via next (BFS, includes start)."""
    visited, queue = {start}, [start]
    for cur in queue:
        for s in nxt.get(cur, ()):
            if s not in visited:
                visited.add(s)
                queue.append(s)
    return visited

# ── Cycle detection in next graph ────────────────────────────────────────────

def next_cycle_edges():
    """Return list of (u, v) next-edges that are part of a cycle."""
    color = {}  # 0 unvisited | 1 in-stack | 2 done
    cycles = []
    def dfs(u):
        color[u] = 1
        for v in nxt.get(u, ()):
            if v not in nodes:
                continue
            c = color.get(v, 0)
            if c == 1:
                cycles.append((u, v))
            elif c == 0:
                dfs(v)
        color[u] = 2
    for t in nodes:
        if is_process(nodes[t]) and color.get(t, 0) == 0:
            dfs(t)
    return cycles

# ── PATIENT node ─────────────────────────────────────────────────────────────

PATIENT = 'Patient (treatment delivered)'

# ── Violations ───────────────────────────────────────────────────────────────

V = defaultdict(list)

# INV 1 — every node has exactly one type/ tag
for t, n in nodes.items():
    tt = type_of(n)
    if len(tt) != 1:
        V[1].append(f"{n['path']}: type/ tags = {tt or '(none)'}")

# INV 2 — every process has exactly one stage/ and ≥1 modality/
for t, n in nodes.items():
    if not is_process(n): continue
    st = stage_of(n)
    mt = modal_of(n)
    if len(st) != 1:
        V[2].append(f"{n['path']}: {len(st)} stage/ tag(s): {st}")
    if not mt:
        V[2].append(f"{n['path']}: no modality/ tags")

# INV 3 — process file in Content/Treatments/Processes/<stage_slug>/
for t, n in nodes.items():
    if not is_process(n): continue
    st = stage_of(n)
    if len(st) != 1: continue   # already caught by INV 2
    expected = st[0].removeprefix('stage/')
    parts = list(n['path'].parts)
    try:
        pi = parts.index('Processes')
        actual = parts[pi + 1]
        if actual != expected:
            V[3].append(f"{n['path']}: folder '{actual}', stage tag '{expected}'")
    except (ValueError, IndexError):
        V[3].append(f"{n['path']}: not under Treatments/Processes/")

# INV 4 — every stage folder has a type/stage page in Treatments/Stages/
PROC_DIR   = VAULT_ROOT / 'Treatments' / 'Processes'
STAGES_DIR = VAULT_ROOT / 'Treatments' / 'Stages'

stage_folders = {d.name for d in PROC_DIR.iterdir() if d.is_dir()} if PROC_DIR.exists() else set()

stage_page_slugs = set()
if not STAGES_DIR.exists():
    V[4].append("Treatments/Stages/ does not exist — no type/stage pages present")
else:
    for t, n in nodes.items():
        if 'type/stage' in n['tags']:
            for s in stage_of(n):
                stage_page_slugs.add(s.removeprefix('stage/'))

for slug in sorted(stage_folders):
    if slug not in stage_page_slugs:
        V[4].append(f"stage folder '{slug}' has no matching type/stage page")

# INV 5 — next/feedback targets exist
for t, n in nodes.items():
    for tgt in n['next']:
        if tgt not in nodes:
            V[5].append(f"{n['path']}: next -> [[{tgt}]] not found")
    for tgt in n['feedback']:
        if tgt not in nodes:
            V[5].append(f"{n['path']}: feedback -> [[{tgt}]] not found")

# INV 6 — next is acyclic (forward); feedback points to an ancestor (earlier node)
for u, v in next_cycle_edges():
    V[6].append(f"next-cycle: '{u}' -> '{v}'")

for t, n in nodes.items():
    if not is_process(n): continue
    for fb in n['feedback']:
        if fb not in nodes: continue
        if t not in descendants(fb):
            V[6].append(f"{n['path']}: feedback -> '{fb}' — '{fb}' cannot reach this node via next")

# INV 7 — following next from every process reaches Patient
if PATIENT not in nodes:
    V[7].append(f"Patient node '{PATIENT}' not found")
else:
    can_reach = {PATIENT}
    changed = True
    while changed:
        changed = False
        for t in nodes:
            if t not in can_reach and nxt.get(t, set()) & can_reach:
                can_reach.add(t)
                changed = True
    for t, n in nodes.items():
        if is_process(n) and t != PATIENT and t not in can_reach:
            V[7].append(f"{n['path']}: no next-path to Patient")

# INV 8 — each modality's next chain (restricted to that modality) is linear
all_mod_slugs = {mt.removeprefix('modality/')
                 for t, n in nodes.items() if is_process(n)
                 for mt in modal_of(n)}

for slug in sorted(all_mod_slugs):
    tag   = f'modality/{slug}'
    mnodes = {t for t, n in nodes.items() if is_process(n) and tag in n['tags']}
    for t in mnodes:
        succ = [s for s in nxt.get(t, ()) if s in mnodes]
        pred = [p for p in preds.get(t, ()) if p in mnodes]
        if len(succ) > 1:
            V[8].append(f"modality/{slug}: '{t}' forks within modality -> {succ}")
        if len(pred) > 1:
            V[8].append(f"modality/{slug}: '{t}' has multiple predecessors within modality: {pred}")

# INV 9 — Patient carries stage/patient and every modality/ tag in the vault
if PATIENT in nodes:
    pn = nodes[PATIENT]
    if 'stage/patient' not in pn['tags']:
        V[9].append("Patient node missing stage/patient tag")
    all_mtags = {mt for t, n in nodes.items() if is_process(n) for mt in modal_of(n)}
    missing   = all_mtags - set(modal_of(pn))
    if missing:
        V[9].append(f"Patient node missing modality tags: {sorted(missing)}")
else:
    V[9].append(f"Patient node '{PATIENT}' not found")

# INV 10 — [[links]] in bodies: dangling or in Glossary/ without type/glossary tag
LINK_RE = re.compile(r'\[\[([^\]|#\n]+?)(?:\|[^\]]+)?\]\]')

for t, n in nodes.items():
    for raw in LINK_RE.findall(n['body']):
        link = raw.strip()
        if link not in nodes:
            V[10].append(f"{n['path']}: [[{link}]] not found in vault")
        elif 'Glossary' in nodes[link]['path'].parts and 'type/glossary' not in nodes[link]['tags']:
            V[10].append(f"{n['path']}: [[{link}]] in Glossary/ but missing type/glossary tag")

# INV 11 — company cards: no stage/modality tags; all body links resolve
for t, n in nodes.items():
    if 'type/company' not in n['tags']: continue
    if stage_of(n):
        V[11].append(f"{n['path']}: company has stage/ tags: {stage_of(n)}")
    if modal_of(n):
        V[11].append(f"{n['path']}: company has modality/ tags: {modal_of(n)}")
    for link in LINK_RE.findall(n['body']):
        link = link.strip()
        if link not in nodes:
            V[11].append(f"{n['path']}: link [[{link}]] not found")

# INV 12 — no alias slugs used as modality/ tags
ALIAS_SLUGS = {'all', 'phased', 'smallish', 'protein', 'nucleic', 'advanced'}
for t, n in nodes.items():
    for mt in modal_of(n):
        slug = mt.removeprefix('modality/')
        if slug in ALIAS_SLUGS:
            V[12].append(f"{n['path']}: '{mt}' is an alias tag, not an explicit modality tag")

# INV 13 — every modality/ tag on a process has a type/modality page
mod_page_slugs = set()
for t, n in nodes.items():
    if 'type/modality' in n['tags']:
        for mt in modal_of(n):
            mod_page_slugs.add(mt.removeprefix('modality/'))

for t, n in nodes.items():
    if not is_process(n): continue
    for mt in modal_of(n):
        slug = mt.removeprefix('modality/')
        if slug not in mod_page_slugs:
            V[13].append(f"{n['path']}: '{mt}' has no type/modality page")

# INV 14 — unique titles; unique stage and modality self-slugs
for e in _dup_errors:
    V[14].append(e)

stage_self_map = defaultdict(list)
modal_self_map = defaultdict(list)
for t, n in nodes.items():
    if 'type/stage'    in n['tags']:
        for s in stage_of(n): stage_self_map[s].append(t)
    if 'type/modality' in n['tags']:
        for m in modal_of(n): modal_self_map[m].append(t)

for slug, titles in stage_self_map.items():
    if len(titles) > 1:
        V[14].append(f"Multiple type/stage pages with tag '{slug}': {titles}")
for slug, titles in modal_self_map.items():
    if len(titles) > 1:
        V[14].append(f"Multiple type/modality pages with tag '{slug}': {titles}")

# INV 15 — stage/modality tags only on processes and their own self-pages;
#           next/feedback only on process nodes
for t, n in nodes.items():
    tt = type_of(n)
    nt = tt[0] if tt else '(no type)'
    if nt == 'type/process':
        continue
    if nt == 'type/stage':
        if modal_of(n):
            V[15].append(f"{n['path']}: type/stage node has modality/ tags: {modal_of(n)}")
        if len(stage_of(n)) > 1:
            V[15].append(f"{n['path']}: type/stage node has multiple stage/ tags: {stage_of(n)}")
    elif nt == 'type/modality':
        if stage_of(n):
            V[15].append(f"{n['path']}: type/modality node has stage/ tags: {stage_of(n)}")
        if len(modal_of(n)) > 1:
            V[15].append(f"{n['path']}: type/modality node has multiple modality/ tags: {modal_of(n)}")
    else:
        # index, glossary, company — no stage/ or modality/ at all
        if stage_of(n):
            V[15].append(f"{n['path']}: {nt} has stage/ tags: {stage_of(n)}")
        if modal_of(n):
            V[15].append(f"{n['path']}: {nt} has modality/ tags: {modal_of(n)}")
    # next/feedback forbidden on all non-process nodes
    if n['next']:
        V[15].append(f"{n['path']}: {nt} has next edges: {n['next']}")
    if n['feedback']:
        V[15].append(f"{n['path']}: {nt} has feedback edges: {n['feedback']}")

# INV 16 — every feedback edge shares ≥1 modality/ tag with its source
for t, n in nodes.items():
    if not is_process(n): continue
    src = set(modal_of(n))
    for fb in n['feedback']:
        if fb not in nodes: continue
        if not src & set(modal_of(nodes[fb])):
            V[16].append(f"{n['path']}: feedback -> '{fb}' shares no modality/ tags")

# INV 17 — no unforced node boundary
# X→Y is unforced if: X has exactly one successor, Y has exactly one predecessor,
# X and Y have identical modality sets, and X and Y are in the same stage.
for t, n in nodes.items():
    if not is_process(n): continue
    if len(nxt.get(t, ())) != 1: continue
    y = next(iter(nxt[t]))
    if y not in nodes or not is_process(nodes[y]): continue
    if len(preds.get(y, ())) != 1: continue
    yn = nodes[y]
    if set(modal_of(n)) == set(modal_of(yn)) and set(stage_of(n)) == set(stage_of(yn)):
        V[17].append(f"'{t}' -> '{y}': same stage {stage_of(n)}, identical modalities — unforced boundary")

# ── Report ───────────────────────────────────────────────────────────────────

DESCS = {
    1:  "Every node carries exactly one type/ tag.",
    2:  "Every process carries exactly one stage/ tag and ≥1 modality/ tag.",
    3:  "Every process file is under Treatments/Processes/<stage_slug>/.",
    4:  "Every stage folder has a matching type/stage page in Treatments/Stages/.",
    5:  "Every next/feedback target is an existing node file.",
    6:  "next is acyclic (forward); feedback points to an earlier process.",
    7:  "Following next from any process eventually reaches Patient.",
    8:  "Each modality's next chain (restricted to that modality) is linear.",
    9:  "Patient node carries stage/patient and every modality/ tag in the vault.",
    10: "Every [[link]] in any body is non-dangling; Glossary/ files have type/glossary.",
    11: "Company cards carry no stage/modality tags; all body links resolve.",
    12: "No alias slug appears as a modality/ tag in any file.",
    13: "Every modality/ tag on a process has a matching type/modality page.",
    14: "Node titles are unique; stage and modality self-slugs are unique.",
    15: "stage/modality tags only on processes and their own self-pages; next/feedback only on processes.",
    16: "Every feedback edge shares ≥1 modality/ tag with its source.",
    17: "No unforced node boundary (same stage + same modalities + no fork/merge).",
}

print("=" * 64)
print("VAULT INVARIANT CHECK  (SPECS.md §8)")
print("=" * 64)

all_pass = True
for i in range(1, 18):
    vs = V.get(i, [])
    label = "PASS" if not vs else f"FAIL  ({len(vs)} violation{'s' if len(vs)>1 else ''})"
    print(f"\nINV {i:2d}  {DESCS[i]}")
    print(f"       {label}")
    for msg in vs:
        all_pass = False
        print(f"       • {msg}")

print()
print("─" * 64)
if all_pass:
    print("INV 1–17: all PASS")
else:
    total = sum(len(v) for v in V.values())
    print(f"INV 1–17: FAIL — {total} total violation(s)")

# INV 18 — list glossary links for manual semantic review
print()
print("─" * 64)
print("INV 18  Glossary sufficiency (SPECS.md §6, §8.18) — semantic,")
print("        requires reading. For each link below verify the glossary")
print("        page explains what the linking page defers to it.")
print()
seen = set()
for t, n in sorted(nodes.items()):
    for raw in LINK_RE.findall(n['body']):
        link = raw.strip()
        if link in nodes and 'type/glossary' in nodes[link]['tags']:
            key = (link, t)
            if key not in seen:
                seen.add(key)
                print(f"  [[{link}]]  <-  {n['path']}")
if not seen:
    print("  (no glossary links found in vault bodies)")
