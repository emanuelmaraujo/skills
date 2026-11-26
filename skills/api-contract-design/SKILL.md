---
name: api-contract-design
description: "Define e revisa contratos de APIs e integrações quando a tarefa envolve esquemas, erros, paginação, idempotência ou compatibilidade."
---

# api-contract-design

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique consumidores, protocolo e contratos de compatibilidade. Adapte os exemplos ao transporte e ao esquema adotados pelo projeto.

## Procedimento

1. Identifique consumidores, recursos, operações e requisitos do contrato existente. Use o formato do projeto, como OpenAPI para HTTP, esquema de RPC ou contrato de eventos. Documente entradas, saídas, erros e regras de evolução.
2. Defina semântica de erros e, conforme aplicável, status de transporte, paginação estável, limites, campos opcionais, idempotência e evolução sem quebra. Para webhooks, especifique assinatura, versão, retries e deduplicação.
3. Revise exemplos e prove via testes de contrato em casos válidos, inválidos, vazios e legados. Encaminhe a revisão de autorização para api-security-review.

## Deliverables

Use o relatório compartilhado. Contrato, exemplos, análise de compatibilidade e relatos de teste.
