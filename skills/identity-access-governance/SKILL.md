---
name: identity-access-governance
description: "Revisa ou estrutura governança de identidades quando a tarefa envolve concessões, privilégios, revisão periódica, contas de serviço ou desligamento."
---

# identity-access-governance

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique onde identidades, papéis e concessões são mantidos, inclusive se houver múltiplos provedores. Use os mecanismos do ambiente e preserve a rastreabilidade do ciclo de vida.

## Procedimento

1. Inventarie identidades humanas, contas de serviço e contas de contingência. Registre recurso, papel, proprietário, motivo e validade sem exportar segredos. Separe identidades privilegiadas e de uso diário.
2. Modele admissão, movimentação e desligamento com aprovador, prazo, evidência e revogação. Revise MFA, menor privilégio, segregação de funções e permissões herdadas.
3. Valide com amostra e registre exceções com responsável e expiração. Para remoções em lote ou mudanças em políticas de autenticação, avalie dependências, reversão e autorização específica.

## Deliverables

Use o relatório compartilhado. Matriz de acesso, fluxo de ciclo de vida, evidência amostral e fila de remediação.
