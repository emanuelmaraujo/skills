# Architecture and discovery

## Principles

1. **One trigger, one job**: each skill description tells the agent when to load it. Avoid copying the entire atlas into every skill.
2. **Progressive disclosure**: frontmatter → selected SKILL.md → project-specific repo/docs → optional external reference.
3. **Evidence-based handoffs**: the orchestrator assigns narrow tasks and accepts evidence, not unsupported claims.
4. **Small compatibility surface**: standard frontmatter `name` and `description`; plain Markdown; portable across Agent Skills-compatible runners.
5. **Project constraints dominate templates**: site galleries are inspiration; product code and brand are authoritative.

## Routing

- Need references or competitor audit → `web-reference-researcher`
- Need tokens, brand consistency → `design-system-architect`
- Need landing/marketing → `premium-landing-builder`
- Need operational UI or SaaS app → `premium-dashboard-builder`
- Need motion → `web-motion-engineer`
- Need interactive 3D → `web-3d-experience-builder`
- Need layout/screenshots regression → `frontend-visual-qa`
- Need WCAG/keyboard → `web-accessibility-audit`
- Need CWV or JS footprint → `web-performance-engineer`
- Need frontend threat review → `web-security-review`
- Need signup/affiliate/checkout friction → `web-conversion-ux`
- Need multiple disciplines together → `web-design-orchestrator`

## Overlap rule

Orchestrator **routes**; specialist **executes**. Builder includes baseline accessibility and performance; deep audits are separate only when triggered by risk, acceptance criteria or complexity.

## Change policy

No implied install rights; never blindly run README scripts, vendor MCP commands or copy assets. PR before merge; no production writes. Preserve user authorization and platform constraints.
