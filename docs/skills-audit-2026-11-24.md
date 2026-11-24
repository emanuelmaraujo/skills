# Revisão do catálogo de skills

Inventário de origem com 36 skills. A revisão compara gatilhos, procedimentos e entregáveis. As decisões abaixo cobrem as 36 entradas e registram as lacunas priorizadas.

| Área | Skills revisadas e decisão |
| --- | --- |
| Pesquisa e direção web | `web-reference-researcher` coleta referências, `product-art-direction` define a linguagem, `design-system-architect` implementa padrões e `web-design-orchestrator` coordena projetos com várias etapas. Manter. |
| Construção e UX | `premium-landing-builder` entrega páginas comerciais, `premium-dashboard-builder` entrega interfaces operacionais e `web-conversion-ux` diagnostica atritos. Manter. |
| Motion e 3D web | `web-motion-engineer` trata interações, `web-3d-experience-builder` trata cena interativa e `code-driven-motion-storytelling` trata narrativa roteirizada. Manter. |
| Qualidade de frontend | `frontend-visual-qa`, `web-accessibility-audit`, `web-performance-engineer` e `web-security-review` têm evidências distintas de visual, acessibilidade, desempenho e segurança no navegador. Manter. |
| Marca | `logo-design` cria o master. `logo-animation`, `logo-motion-design` e `logo-motion-review` usam o mesmo master, timing e verificação. Consolidar as três últimas em `logo-animation`, com referência para criação vetorial, transparência e revisão avulsa. |
| SEO | `seo-technical-auditor`, `seo-structured-data-engineer`, `seo-content-strategy`, `seo-programmatic-architecture` e `seo-ai-search-visibility` cobrem rastreamento, marcação, pauta, escala e visibilidade em IA, respectivamente. Manter. |
| Dados e experimentos | `marketing-analytics-engineer` instrumenta eventos. `growth-experiment-designer` define a comparação e a regra de decisão. Manter. |
| Engenharia e skills | `engineering-tdd-implementer` implementa guiado por testes, `engineering-independent-review` revisa alterações e `agent-skill-quality-engineer` avalia instruções e ativação. Manter. |
| Backend e APIs | `backend-service-engineering` implementa serviços e banco, `api-contract-design` define interface e compatibilidade, `api-security-review` revisa autorização e exposição. Manter e aprofundar diagnóstico de consultas na skill de backend. |
| Segurança na entrega | `secure-coding-baseline` aplica controles no código. `devsecops-pipeline-hardening` trata permissões, segredos e controles do pipeline. Manter. |
| Vulnerabilidades | `vulnerability-triage-remediation` prioriza alertas contínuos. `pentest-governance-remediation` cobre escopo, regras de engajamento e tratamento do laudo. Manter, usando a triagem comum para acompanhar achados. |
| Governança | `cybersecurity-baseline` diagnostica a cobertura dos controles da organização. Manter como entrada e encaminhar as verificações específicas. |

## Lacunas trabalhadas

| Momento | Nova skill | Entrega |
| --- | --- | --- |
| Antes de construir | `threat-modeling` | Fluxos de dados, fronteiras de confiança e controles vinculados a riscos. |
| Quando o serviço está em operação | `service-reliability-observability` | Sinais de saúde para APIs e filas, SLOs, alertas e instruções de diagnóstico. |
| Na concessão e revisão de acesso | `identity-access-governance` | Matriz de papéis e fluxo de admissão, movimentação e desligamento. |
| Durante um incidente | `security-incident-response` | Triagem, preservação de evidências, contenção autorizada e recuperação. |
| Antes de depender do backup | `backup-recovery-assurance` | Metas de recuperação e prova de restauração em ambiente isolado. |

O catálogo proposto tem 39 entradas. Quem invoca os nomes antigos de motion deve usar `logo-animation`. Os cenários documentados nas novas skills são casos de avaliação propostos.
