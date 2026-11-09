#!/usr/bin/env python3
"""Validate self-contained Agent Skills against the published format.

This is a *static* YAML/link checker, not an agent benchmark or official
certification. It performs no network requests and executes no skill code.
Requires PyYAML==6.0.3 (CI installs this pinned version).
"""
import argparse
import pathlib
import re
import sys
from urllib.parse import unquote

import yaml

NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


class NoDuplicateSafeLoader(yaml.SafeLoader):
    """Reject YAML duplicate keys instead of silently using the last one."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError(None, None, "frontmatter keys must be strings", key_node.start_mark)
        if key in result:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate key: {key}", key_node.start_mark)
        result[key] = loader.construct_object(value_node)
    return result


NoDuplicateSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def validate_skill(file: pathlib.Path, root: pathlib.Path):
    errors = []
    slug = file.parent.name
    try:
        raw = file.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        return [f"{slug}: cannot read SKILL.md: {exc}"]

    text = raw.replace("\r\n", "\n")
    parts = text.split("\n---\n", 1)
    if not text.startswith("---\n") or len(parts) != 2:
        return [f"{slug}: expected YAML frontmatter delimited by --- on standalone lines"]
    yaml_source = parts[0][4:]
    body = parts[1]
    try:
        metadata = yaml.load(yaml_source, Loader=NoDuplicateSafeLoader)
    except yaml.YAMLError as exc:
        return [f"{slug}: malformed YAML: {exc}"]
    if not isinstance(metadata, dict):
        return [f"{slug}: YAML frontmatter must be a mapping"]
    unknown = metadata.keys() - ALLOWED_FIELDS
    if unknown:
        errors.append(f"{slug}: unknown/runner-specific metadata keys: {sorted(unknown)}")

    name = metadata.get("name")
    if not isinstance(name, str) or not 1 <= len(name) <= 64 or not NAME_RE.fullmatch(name):
        errors.append(f"{slug}: name must be 1-64 lowercase alphanumeric/hyphen chars, with no doubled/edge hyphens")
    elif name != slug:
        errors.append(f"{slug}: name {name!r} must match folder name")

    description = metadata.get("description")
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        errors.append(f"{slug}: description must be a non-empty string of at most 1024 characters")
    elif len(description.strip()) < 35:
        errors.append(f"{slug}: description is too vague to support reliable activation")

    for key, maxlen in (("compatibility", 500), ("license", None), ("allowed-tools", None)):
        if key in metadata:
            value = metadata[key]
            if not isinstance(value, str) or not value.strip() or (maxlen and len(value) > maxlen):
                errors.append(f"{slug}: {key} must be non-empty string" + (f" (max {maxlen} chars)" if maxlen else ""))

    if "metadata" in metadata:
        extra = metadata["metadata"]
        if not isinstance(extra, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in extra.items()):
            errors.append(f"{slug}: metadata must be a mapping of string keys to string values")

    if not body.strip():
        errors.append(f"{slug}: skill body is empty")
    if len(text.splitlines()) > 500:
        errors.append(f"{slug}: SKILL.md exceeds 500 lines; move details to references/")
    if not ("## Deliverables" in body or "## Deliverable" in body):
        errors.append(f"{slug}: include a concrete deliverable section")

    base = file.parent.resolve()
    for match in LINK_RE.finditer(body):
        # Links may include an optional quoted title: [link](references/x.md "title")
        url = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        if not url or url.startswith("#") or re.match(r"^(https?://|mailto:)", url, re.I):
            continue
        path = unquote(url.split("#", 1)[0])
        if not path:
            continue
        if path.startswith("/") or re.match(r"^[A-Za-z]:", path):
            errors.append(f"{slug}: absolute local link not portable: {path}")
            continue
        target = (base / path).resolve()
        if not target.is_relative_to(base):
            errors.append(f"{slug}: link escapes standalone skill package: {path}")
        elif not target.is_file():
            errors.append(f"{slug}: missing linked file: {path}")
        elif path.startswith("references/") and target.name in {"evaluation.md", "quality-gates.md"}:
            source = root / "docs" / target.name
            if source.is_file() and source.read_bytes() != target.read_bytes():
                errors.append(f"{slug}: packaged shared reference is stale: {path}")

    return errors


def run(root: pathlib.Path):
    files = sorted((root / "skills").glob("*/SKILL.md"))
    if not files:
        return ["No skills found under skills/*/SKILL.md"], 0
    errors = []
    for file in files:
        errors.extend(validate_skill(file, root))
    return errors, len(files)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, count = run(args.root.resolve())
    for problem in errors:
        print("ERROR:", problem)
    print(f"Validated {count} skill packages, {len(errors)} structural/link errors. No AI run.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
