"""Fast offline tests for the skill structure validator (no model or network)."""
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skills import run


GOOD = """---
name: example-skill
description: Use when auditing an example and demonstrating a concrete deterministic output.
metadata:
  version: "0.2.0"
---
# Example
## Deliverables
Report with a source link and one finding.
[Guide](references/guide.md)
"""


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name)
        self.folder = self.root / "skills" / "example-skill"
        (self.folder / "references").mkdir(parents=True)
        (self.folder / "references" / "guide.md").write_text("# Guide", encoding="utf-8")
        self.file = self.folder / "SKILL.md"
        self.file.write_text(GOOD, encoding="utf-8")

    def errors(self):
        return run(self.root)[0]

    def test_valid_package(self):
        self.assertEqual([], self.errors())

    def test_invalid_name(self):
        self.file.write_text(GOOD.replace("name: example-skill", "name: Example--Skill"), encoding="utf-8")
        self.assertTrue(any("name must" in x for x in self.errors()))

    def test_duplicate_yaml_key(self):
        self.file.write_text(GOOD.replace("name: example-skill", "name: example-skill\nname: other"), encoding="utf-8")
        self.assertTrue(any("duplicate key" in x for x in self.errors()))

    def test_missing_reference(self):
        (self.folder / "references" / "guide.md").unlink()
        self.assertTrue(any("missing linked" in x for x in self.errors()))

    def test_escape_package(self):
        self.file.write_text(GOOD.replace("references/guide.md", "../../secrets.txt"), encoding="utf-8")
        self.assertTrue(any("escapes" in x for x in self.errors()))

    def test_description_length(self):
        self.file.write_text(GOOD.replace("Use when auditing an example and demonstrating a concrete deterministic output.", "x" * 1025), encoding="utf-8")
        self.assertTrue(any("description must" in x for x in self.errors()))


if __name__ == "__main__":
    unittest.main()
