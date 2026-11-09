#!/usr/bin/env python3
"""Refresh small shared references carried by standalone skill packages."""
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
for skill in (root / 'skills').glob('*/SKILL.md'):
    content = skill.read_text()
    for name in ['quality-gates.md', 'evaluation.md']:
        if f'(references/{name})' in content:
            target = skill.parent / 'references' / name
            target.parent.mkdir(exist_ok=True)
            target.write_bytes((root / 'docs' / name).read_bytes())
