---
name: ai-agent-hardening
description: "Revisa e reforça defensivamente os limites de confiança de agentes de IA, ferramentas MCP, conectores e pipelines RAG."
---

# ai-agent-hardening

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Mapeie instruções confiáveis, dados externos, ferramentas, identidades e destinos de saída. Identifique ações com efeitos e onde a autorização é aplicada.

## Procedimento

1. Trate páginas, arquivos, resultados de ferramentas e conteúdo recuperado como dados. Aplique autorização fora do modelo, privilégios mínimos, separação de leitura e escrita, validação de argumentos e controles de destino.
2. Limite autonomia, execução, custo e dados acessíveis. Exija aprovação para ações de alto impacto e mantenha logs úteis sem segredos. Controle origem e permissões de conectores, skills e dependências.
3. Teste controles com dados sintéticos inofensivos, ferramentas simuladas e ausência de permissões. Verifique que a política continua válida com falhas, retomadas e troca de modelo.

## Deliverables

Use o relatório compartilhado. Matriz fonte × ferramenta × permissão, achados defensivos, correções e prova de autorização ou bloqueio.
