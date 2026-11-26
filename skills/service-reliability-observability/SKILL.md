---
name: service-reliability-observability
description: "Melhora a operação de APIs, workers e serviços quando a tarefa envolve SLOs, métricas, alertas, traces ou saúde de filas."
---

# service-reliability-observability

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique serviços, jornadas críticas e sinais que a operação já coleta. Ajuste indicadores e alertas ao volume, ao impacto e à capacidade de acompanhamento.

## Procedimento

1. Defina a jornada e um indicador observável. Para APIs, considere disponibilidade e latência. Para workers, inclua idade do job mais antigo, tempo até conclusão, retries e falhas definitivas. Documente janela e denominador.
2. Use telemetria existente. Correlacione logs, métricas e traces por identificadores sem dados pessoais. Defina alertas acionáveis com sinais sustentados, responsáveis e runbook.
3. Teste com dados sintéticos ou telemetria histórica. Evidencie o caminho do sintoma ao diagnóstico, verifique supressão de ruído e declare lacunas de visibilidade.

## Deliverables

Use o relatório compartilhado. SLIs e SLOs propostos, painel ou especificação, alertas acionáveis, runbook e verificação.
