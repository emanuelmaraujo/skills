#!/usr/bin/env python3
"""Stdlib-only static check for SKILL.md metadata and a simple scenario matrix."""
import pathlib,re,sys,json
root=pathlib.Path(__file__).resolve().parents[1]
slugs=[]
problems=[]
for file in sorted((root/"skills").glob("*/SKILL.md")):
    data=file.read_text(encoding="utf-8")
    name=re.search(r"(?m)^name:\s*(.+)$", data)
    desc=re.search(r"(?m)^description:\s*(.+)$",data)
    slug=file.parent.name
    slugs.append(slug)
    if not data.startswith("---\n") or data.count("---\n")<2:
        problems.append(f"{slug}: missing frontmatter")
    if not name or name.group(1).strip() != slug:
        problems.append(f"{slug}: name mismatch")
    if not desc or len(desc.group(1).strip())<55:
        problems.append(f"{slug}: weak trigger description")
    if len(data)>16000:
        problems.append(f"{slug}: exceeds 16k characters; consider references")
    for link in re.findall(r'\]\((references/[^)]+)\)', data):
        target = file.parent / link
        if not target.is_file():
            problems.append(f"{slug}: missing packaged reference {link}")
        elif target.read_bytes() != (root / 'docs' / target.name).read_bytes():
            problems.append(f"{slug}: stale shared reference; run scripts/sync_skill_references.py")
    for marker in ["## Deliverable","## Deliverables"]:
        if marker in data:
            break
    else:
        problems.append(f"{slug}: missing deliverable")
if len(slugs)!=len(set(slugs)):
    problems.append("duplicate slugs")
assert slugs, "No skills"
print(json.dumps({"skills":len(slugs),"problems":problems},indent=2))
sys.exit(1 if problems else 0)
