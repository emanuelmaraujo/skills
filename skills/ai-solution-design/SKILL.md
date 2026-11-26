---
name: ai-solution-design
description: "Planeja e implementa soluções de IA com modelos, ferramentas, RAG ou workflows conforme o caso e os critérios de qualidade do projeto."
---

# ai-solution-design

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique problema, usuários, custo do erro, dados, sistemas, orçamento e supervisão. Defina uma linha de base simples para comparação.

## Procedimento

1. Escolha fluxo determinístico, chamada de modelo, recuperação de documentos ou agentes com base no resultado esperado. Para recuperação, defina fontes, atualização, filtros de acesso, referências e comportamento sem evidência.
2. Defina esquema de entrada e saída, validações, exceções, escalonamento humano e limites de tempo e custo. Em operações com efeitos, preveja idempotência e estado consistente.
3. Valide em amostra representativa e projete observabilidade, fallback e reversão. Use ai-evaluation para medir e ai-agent-hardening quando houver ferramentas ou dados externos.

## Deliverables

Use o relatório compartilhado. Desenho da solução, decisões, protótipo ou plano de implementação e critérios de avaliação.
