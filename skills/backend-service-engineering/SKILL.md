---
name: backend-service-engineering
description: "Implementa ou audita serviços backend, workers e fluxos de dados com concorrência, transações, filas, migrações, coexistência de clientes ou desempenho de banco."
---

# backend-service-engineering

Aplique o [guia compartilhado de execução e entrega](references/quality-gates.md). Identifique runtime, banco, versão, ferramentas de migração, papéis e contratos existentes. Em auditoria, inspecione código, plano e evidência disponível. Limite a execução a verificações autorizadas com dados descartáveis.

## Procedimento

1. Mapeie pontos de entrada, invariantes, transações e operações repetíveis. Use restrições no banco e os mecanismos de idempotência e entrega confiável já adotados. Verifique duplicidade, disputa, falha parcial e retry.
2. Para mudanças de esquema ou contratos, aplique o [checklist de migração e coexistência](references/migration-and-concurrency.md#migração-e-coexistência) antes de expor a nova interface. Teste clientes antigos e novos na mesma fase transitória e prove o rollback da aplicação durante essa fase.
3. Para invariantes concorrentes, use o [teste com sessões independentes](references/migration-and-concurrency.md#teste-de-concorrência). Para consultas lentas, compare planos, estimativas, índices e volume lido com dados representativos em condições equivalentes e ambiente permitido.
4. Verifique pelos pontos de entrada normais. Use logs e métricas sem segredos. Para SLO e saúde de produção, use `service-reliability-observability`. Use `secure-coding-baseline` para controles transversais e esta skill para a consistência e as permissões específicas da migração.

## Deliverables

Use o relatório compartilhado. Inclua invariantes, matriz por versão e papel, plano de migração e recuperação quando aplicável e evidência do teste de concorrência.
