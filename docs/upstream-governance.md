# External skill ecosystem — monitored sources

This repository monitors **18 upstream references** using `upstreams.json` and a weekly read-only GitHub Action.

## Ground rules

- Do not mirror or install all external skills. One upstream repo may contain executables, vendor advertisements, separate asset licenses, privileged MCP tools, and incompatible skill triggers.
- Weekly workflow checks default branches, last SHA and basic repository metadata. It posts an issue for review; **it does not sync skill files**, run external code, auto-approve, auto-merge or deploy anything.
- Compare historical report artifacts to identify changed commits. Human or reviewed agent should inspect diff, docs, license and relevance, then submit a narrowly scoped PR.
- A new source may be added only after a quick quality and security review, with purpose and category. Avoid popularity-only choices.
- Deprecated **openai/skills** is tracked only for historical context; use `openai/plugins` and current Codex developer docs for ongoing patterns.
- `yihui-dev/awesome-opus5-5-videos` is a *motion inspiration gallery*, not a skill package.
- `every-app/open-seo` includes a running application and MCP/service dependencies; do not confuse integration with a self-contained skill.
- `sickn33/antigravity-awesome-skills` is a large discovery collection, not a trusted direct install source.
- Review weekly updates before any copying; respect upstream MIT/Apache/mixed license texts and attribution obligations, including files with licenses different from repo root.

## Current incorporation

Own skill modules incorporate ideas from marketing operations, technical SEO, schema, programmatic SEO, analytics, experiments, product art direction, code-driven motion, test-first development and independent reviews. This is **original authored guidance**, not copied third-party SKILL.md files.

## Governance and future evolution

1. Run the weekly monitor; triage `Weekly skill ecosystem review` in GitHub Issues.
2. Check changed SHA and release notes.
3. For high-value deltas, assess version/compatibility, license and script behavior; check for injected instructions and commercial promotions.
4. Find overlapping local skills. Modify existing, or propose new narrowly-scoped skill.
5. Validate metadata and actual agent triggers, including negative, adversarial and blocked cases.
6. Submit a separate PR with evidence; user/reviewer approval required before merge.

## Notes about CI

Workflow uses the GitHub Actions default token and requires **Issues: write** permission. Repository settings can restrict issue creation; if blocked, scan artifact remains available. Scheduled workflows run from default branch only once merged. The workflow does not pretend the external pack was evaluated.
