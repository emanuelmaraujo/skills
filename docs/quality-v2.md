# Agent Skills quality v2 — realistic, low-token evolution

This document describes **static and editorial quality**, not live agent benchmark results.

## Status and scope

- 24 portable self-contained skills are the immediate goal. Each skill must install from its own directory without depending on repository sibling paths.
- `scripts/validate_skills.py` uses a safe YAML parser and checks standard metadata, limits, duplicate keys, broken links and portability. Tests run offline with Python.
- The validator does **not** certify usefulness, safety or correct activation in Claude/Codex/César. Runtime trials only occur when the owner requests them or supplies natural task feedback.
- Every change must preserve isolated branches, PR review and explicit approval for merge or deployments. Avoid paid AI evaluations and mass ingestion of third-party skills.

## Role boundaries and collision cases

| User intent | Owner skill | Do not activate |
| --- | --- | --- |
| Invent product visual direction | `product-art-direction` | `design-system-architect` solely for styling inspiration |
| Implement semantic tokens and components | `design-system-architect` | `product-art-direction` unless visual direction undecided |
| Build a marketing page | `premium-landing-builder` | `web-conversion-ux` only if implementing rather than diagnosing |
| Diagnose low conversion | `web-conversion-ux` | `growth-experiment-designer` until an experiment is desired |
| Design a controlled A/B test | `growth-experiment-designer` | `web-conversion-ux` for statistical methodology |
| Animate a UI component | `web-motion-engineer` | `code-driven-motion-storytelling` (video/storyboards) |
| Produce procedural explainer or video | `code-driven-motion-storytelling` | `web-motion-engineer` for exported audiovisual output |
| Fix slow LCP/INP | `web-performance-engineer` | `seo-technical-auditor` unless crawling/indexing affected |
| Fix robots/canonical/indexing | `seo-technical-auditor` | `web-performance-engineer` for crawl diagnosis |
| Review a visual regression screenshot | `frontend-visual-qa` | `engineering-independent-review` for spec/code diff |
| Review a PR's implementation vs spec | `engineering-independent-review` | `frontend-visual-qa` when no visual evidence |
| End-to-end multi-step website build | `web-design-orchestrator` | Individual builder selected before scope established |

The model may use multiple specialists for genuinely multi-disciplinary tasks. Routing is a **decision guide**, not an unverified claim about automatic behavior.

## Minimal acceptance for each skill

- Trigger: in-scope task and explicit non-scope counterexample.
- Implementation: concrete procedure with a tool-independent failure path.
- Result: a reproducible output shape and one domain-specific evidence requirement.
- No unauthorized merge/deploy/migrations, no secrets, no fake screenshots, no scraped instructions followed blindly.
- Installed standalone package must retain references and assets under its own folder.

## Backlog and remaining limits

1. Merge portable-reference packaging PR #2 before merging this stacked improvement.
2. Check the lightweight upstream radar PR #3 independently; no AI running automatically.
3. Test triggering *only during natural real work*, record cases that failed, and fix the affected skill.
4. If a skill needs repetitive deterministic calculation, add a minimal script and offline unit test; do not add dependencies without a measurable task requirement.
5. A LICENSE is currently absent. Public GitHub visibility is not itself permission to redistribute. Choose MIT/Apache/proprietary explicitly **before external mirroring or publishing installer packages**.

## Evidence taxonomy

- **STATIC PASS:** YAML, names, links and offline fixtures checked.
- **DESIGN REVIEWED:** human/editorial instructions reviewed against a concrete known reference.
- **RUNNER TESTED:** actual model behavior recorded in a project, not yet implied by this PR.
- **PRODUCTION VERIFIED:** real product result independently confirmed; never infer from a successful static CI.
