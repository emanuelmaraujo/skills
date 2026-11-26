---
name: ai-evaluation
description: "Projeta e executa avaliações de aplicações de IA, RAG e agentes para comparar qualidade, custo, latência, segurança e regressões."
---

# ai-evaluation

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique tarefa, riscos, linha de base, configuração avaliada e dado permitido. Defina sucesso por caso de uso.

## Procedimento

1. Monte conjunto versionado com casos comuns, difíceis, de recusa e sem evidência. Separe desenvolvimento e avaliação e registre rótulos, avaliadores e critérios. Em RAG, avalie recuperação e resposta; em agentes, examine as ações e efeitos.
2. Avalie com métricas adequadas, revisão humana quando necessária, repetição e comparação com baseline. Registre custo, latência e resultados por segmento quando relevantes.
3. Defina gates antes da comparação e reporte falhas, cobertura, variação e o que ficou sem teste. Preserve dados sensíveis e use ambiente isolado para efeitos externos.

## Deliverables

Use o relatório compartilhado. Conjunto de avaliação, rubrica, resultados comparáveis, exemplos de falha e decisão registrada.
