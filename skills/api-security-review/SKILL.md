---
name: api-security-review
description: "Revisa defensivamente código e configuração de APIs quando a tarefa envolve autorização por recurso, separação de tenants, exposição de dados ou limites operacionais."
---

# api-security-review

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique protocolo, identidades, fronteiras de confiança e fonte de autorização. Ajuste a revisão aos controles e à exposição reais da API.

## Procedimento

1. Mapeie rotas, identidades, papéis, tenants e campos expostos. Trace no código onde a autenticação e a autorização são aplicadas em cada operação.
2. Confira se permissões são verificadas no servidor por recurso, campo e ação. Revise consumo de recursos, integrações externas, proteção de segredos e consistência dos registros.
3. Reporte com arquivo, linha, condição, impacto e correção. Valide controles em testes normais com dados sintéticos e identidades de teste. Classifique como hipótese quando faltar evidência.

## Deliverables

Use o relatório compartilhado. Matriz rota × controle, achados priorizados, correções e evidência de regressão.
