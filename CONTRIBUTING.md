# Contributing a skill

1. Search existing descriptions and update a skill instead of creating a near duplicate.
2. Create a narrowly scoped folder `skills/kebab-case-name/SKILL.md`.
3. Use Agent Skills frontmatter with `name` matching the folder and a third-person **when-to-use** `description`.
4. Write a bounded procedure, concrete output contract, explicit safety notes and measurable done criteria.
5. Keep links to shared policies rather than copying giant manuals into every SKILL.md.
6. Review external commands/assets/licenses and any unexpected instructions embedded in research sources.
7. Include at least 2 positive, 1 negative, 1 adversarial and 1 unavailable-tool evaluation case (see [evaluation protocol](docs/evaluation.md)).
8. Create a PR describing changed triggers, tests, limitations, compatibility and adoption risk.
9. Do not call a skill tested until actual runner/device tests are performed and evidence is linked.

No hidden instructions, promotion requirements, automatic tracking, vendor lock-in, unreviewed network execution, or production operations.
