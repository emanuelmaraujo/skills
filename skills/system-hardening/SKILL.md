---
name: system-hardening
description: "Planeja e valida hardening defensivo de sistemas operacionais, servidores, contêineres e serviços gerenciados."
---

# system-hardening

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique tipo e versão do ativo, função, ambiente, dependências e caminho de recuperação. Selecione referências aplicáveis à versão e ao risco.

## Procedimento

1. Inventarie configuração efetiva por leitura. Priorize serviços desnecessários, privilégios, atualizações, acesso administrativo, registros e padrões de rede. Registre controles aplicáveis e exceções justificadas.
2. Para cada ajuste, defina efeito esperado, compatibilidade, verificações e reversão. Teste em ambiente representativo ou grupo piloto autorizado antes de ampliar.
3. Confira configuração e saúde funcional após a mudança. Registre desvios, riscos residuais e responsáveis. Alterações em produção exigem autorização específica.

## Deliverables

Use o relatório compartilhado. Baseline versionada com configuração esperada, prioridades, plano de piloto e evidência de verificação.
