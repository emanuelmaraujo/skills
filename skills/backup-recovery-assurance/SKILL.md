---
name: backup-recovery-assurance
description: "Planeja e verifica backup, recuperação de serviço e continuidade quando a tarefa envolve RPO, RTO ou testes de restauração."
---

# backup-recovery-assurance

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique o que precisa voltar a funcionar, onde estão os dados e quais dependências também precisam ser recuperadas. Use métodos de restauração compatíveis com o ambiente.

## Procedimento

1. Mapeie serviços críticos, dependências e proprietários. Acorde RPO para perda aceitável de dados e RTO para retomada. Confira cobertura, retenção, proteção de cópias e acesso de recuperação.
2. Defina um exercício em ambiente isolado com destino, permissões, ordem de recuperação e descarte seguro. Valide integridade, consistência e uma operação real do serviço restaurado.
3. Meça o tempo e o ponto de recuperação obtidos. Registre diferenças frente à meta, ações e data de reteste. Exija autorização específica para restaurar sobre produção.

## Deliverables

Use o relatório compartilhado. Matriz serviço × RPO/RTO, roteiro, resultado do exercício e ações corretivas.
