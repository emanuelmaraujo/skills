# Web Experience Agent Skills

A focused, **framework-aware** library of modular [Agent Skills](https://agentskills.io/specification) for premium web experiences, SaaS dashboards, 3D and 2D animation, backend development, and defensive security.

**39 skills**. Each skill lives in `skills/<skill-name>/SKILL.md`. This is a research-backed **v1 proposal**: instructions have been schema-reviewed and are not automatically proven successful in a live product.

## Quick start

- Point an Agent Skills-compatible runner at this repository's `skills/` directory or copy selected skill folders to its supported skills directory.
- For Claude Code and Codex, follow the **current official instructions** for skills discovery and installation for your environment. Do not assume one global path works everywhere.
- Ask the agent for one specific job; each frontmatter `description` is designed to activate one clear responsibility.
- Use `web-design-orchestrator` for a multi-specialist project. Use a dedicated specialist directly for narrow tasks.

## Catalog

| Skill | Focus |
| --- | --- |
| [web-reference-researcher](skills/web-reference-researcher/SKILL.md) | Research references and convert them into implementable design observations without copying third-party identity. |
| [design-system-architect](skills/design-system-architect/SKILL.md) | Create coherent design decisions from the actual product and code rather than mixing incompatible template styles. |
| [premium-landing-builder](skills/premium-landing-builder/SKILL.md) | Ship compelling marketing pages with conversion clarity, accessible semantics and restrained motion. |
| [premium-dashboard-builder](skills/premium-dashboard-builder/SKILL.md) | Optimize information hierarchy, operational speed, trust and safe actions; aesthetics support task completion. |
| [web-motion-engineer](skills/web-motion-engineer/SKILL.md) | Engineer purposeful, reversible motion that respects accessibility, CPU/GPU budgets and user control. |
| [web-3d-experience-builder](skills/web-3d-experience-builder/SKILL.md) | Deliver optional and performant 3D that demonstrates real products without obstructing content or conversion. |
| [frontend-visual-qa](skills/frontend-visual-qa/SKILL.md) | Provide reproducible visual findings and an honest evidence trail rather than a subjective thumbs-up. |
| [web-accessibility-audit](skills/web-accessibility-audit/SKILL.md) | Audit user journeys against current WCAG guidance and implement verified accessible alternatives. |
| [web-performance-engineer](skills/web-performance-engineer/SKILL.md) | Improve measured user experience while preserving content, SEO, accessibility and feature correctness. |
| [web-security-review](skills/web-security-review/SKILL.md) | Review concrete web threat surfaces and reduce exploitable changes before they ship. |
| [web-conversion-ux](skills/web-conversion-ux/SKILL.md) | Use ethical behavioral design and observable user tasks rather than visual trends alone. |
| [web-design-orchestrator](skills/web-design-orchestrator/SKILL.md) | Coordinate specialized web skills without delegating away project constraints or claiming unavailable capabilities. |

## Engineering practices

- **Progressive disclosure**: short frontmatter selects skill; complete task steps stay in its own SKILL.md; detailed shared standards live under [docs](docs/).
- **No fabricated evidence**: state PASS/FAIL/SKIP/BLOCKED, evidence and uncertainty.
- **Untrusted references**: sites and third-party skill READMEs are research data, never execution instructions.
- **User approvals**: no merge, production deploy, migration or paid integration without authorization.
- **Interoperability**: no mandatory provider-specific hooks, services, scripts or SDK.
- **Original design**: patterns can inspire but proprietary assets, code and brands require rights.
- **Project first**: inspect real repo, actual styles, runtime and rules; avoid destructive rewrites.

Read [quality gates](docs/quality-gates.md), [architecture](docs/architecture.md), [skill evaluation protocol](docs/evaluation.md), [contribution guide](CONTRIBUTING.md) and [security policy](SECURITY.md).


## New specialist skills (ecosystem expansion)

- [seo-technical-auditor](skills/seo-technical-auditor/SKILL.md)
- [seo-structured-data-engineer](skills/seo-structured-data-engineer/SKILL.md)
- [seo-ai-search-visibility](skills/seo-ai-search-visibility/SKILL.md)
- [seo-programmatic-architecture](skills/seo-programmatic-architecture/SKILL.md)
- [seo-content-strategy](skills/seo-content-strategy/SKILL.md)
- [marketing-analytics-engineer](skills/marketing-analytics-engineer/SKILL.md)
- [growth-experiment-designer](skills/growth-experiment-designer/SKILL.md)
- [engineering-tdd-implementer](skills/engineering-tdd-implementer/SKILL.md)
- [engineering-independent-review](skills/engineering-independent-review/SKILL.md)
- [product-art-direction](skills/product-art-direction/SKILL.md)
- [code-driven-motion-storytelling](skills/code-driven-motion-storytelling/SKILL.md)
- [agent-skill-quality-engineer](skills/agent-skill-quality-engineer/SKILL.md)

## Logo design and animation

- [logo-design](skills/logo-design/SKILL.md) covers briefs, concepts, SVG masters and application tests. Adapted from [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) under MIT.
- [logo-animation](skills/logo-animation/SKILL.md) covers logo reveals on the web and in video, informed by official GSAP and Remotion skills, with Adobe Express and Blender paths.

## Backend, APIs and defensive security

- [backend-service-engineering](skills/backend-service-engineering/SKILL.md) — Implementa e evolui serviços backend, workers e fluxos de dados quando a tarefa envolve consistência, transações, filas, migrações ou observabilidade.
- [api-contract-design](skills/api-contract-design/SKILL.md) — Define e revisa contratos REST e webhooks quando a tarefa envolve OpenAPI, erros, paginação, idempotência ou compatibilidade.
- [api-security-review](skills/api-security-review/SKILL.md) — Revisa defensivamente código e configuração de APIs quando a tarefa envolve autorização por recurso, separação de tenants, exposição de dados ou limites operacionais.
- [secure-coding-baseline](skills/secure-coding-baseline/SKILL.md) — Aplica requisitos mínimos de segurança ao implementar ou revisar alterações de código em aplicações e serviços.
- [vulnerability-triage-remediation](skills/vulnerability-triage-remediation/SKILL.md) — Triage alertas de vulnerabilidades existentes, avalia exposição e dependências afetadas e acompanha correção ou mitigação.
- [devsecops-pipeline-hardening](skills/devsecops-pipeline-hardening/SKILL.md) — Revisa e melhora CI/CD quando a tarefa envolve scanners defensivos, permissões, segredos, SBOM, dependências ou proveniência de artefatos.
- [pentest-governance-remediation](skills/pentest-governance-remediation/SKILL.md) — Prepara escopo de pentest autorizado e transforma relatórios já existentes em triagem, correções e validação defensiva.
- [cybersecurity-baseline](skills/cybersecurity-baseline/SKILL.md) — Avalia controles mínimos de segurança organizacional quando a tarefa envolve inventário, identidade, backups, monitoramento ou resposta a incidentes.

- [threat-modeling](skills/threat-modeling/SKILL.md) — Modela ameaças defensivamente para novos sistemas e alterações de arquitetura, fluxos de dados ou fronteiras de confiança.
- [service-reliability-observability](skills/service-reliability-observability/SKILL.md) — Melhora a operação de APIs, workers e serviços quando a tarefa envolve SLOs, métricas, alertas, traces ou saúde de filas.
- [security-incident-response](skills/security-incident-response/SKILL.md) — Organiza preparação e resposta defensiva a incidentes de segurança com triagem, preservação de evidência, contenção aprovada e recuperação.
- [backup-recovery-assurance](skills/backup-recovery-assurance/SKILL.md) — Planeja e verifica backup, recuperação de serviço e continuidade quando a tarefa envolve RPO, RTO ou testes de restauração.
- [identity-access-governance](skills/identity-access-governance/SKILL.md) — Revisa ou estrutura governança de identidades quando a tarefa envolve concessões, privilégios, revisão periódica, contas de serviço ou desligamento.

See the [catalog audit and routing decisions](docs/skills-audit-2026-11-24.md).

## Skill ecosystem monitoring

18 curated upstreams are tracked in [upstreams.json](upstreams.json). [Monitor workflow](.github/workflows/monitor-upstreams.yml) runs weekly **after merger to default branch**, using read-only GitHub metadata and posting a review issue. It does **not** auto-install, copy or execute third-party skills. See [governance](docs/upstream-governance.md). Static structure validation runs on PRs via [CI](.github/workflows/validate-skills.yml). Real activation/effectiveness evaluations remain pending.

## Research provenance

Backend and security workflows draw on [wshobson/agents](https://github.com/wshobson/agents), [OWASP Secure Agent Playbook](https://github.com/OWASP/secure-agent-playbook), [Trail of Bits](https://github.com/trailofbits/skills) and the standards cited by each skill. Community discussions on Reddit and Hacker News informed discovery and evaluation practices.

Structured inspiration and candidate stacks: [Atlas de Web Design & IA](https://app.notion.com/p/413ae098633781629fa8f169e7ea8330). Prior reviews are linked there. Third-party tools remain subject to current license, availability, cost and security review.

## Scope

The library is instructional; it does not bundle paid template assets, vendor tokens, source code from inspiration sites, scripts from unrelated repositories or runtime credentials.