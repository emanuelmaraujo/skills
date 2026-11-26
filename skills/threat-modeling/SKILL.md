---
name: threat-modeling
description: "Modela ameaças defensivamente para novos sistemas e alterações de arquitetura, fluxos de dados ou fronteiras de confiança."
---

# threat-modeling

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique ativos, atores e fronteiras relevantes à mudança. Ajuste a técnica de modelagem ao sistema e à maturidade da documentação.

## Procedimento

1. Delimite ativos, atores, dependências e dados sensíveis. Desenhe fluxos e fronteiras de confiança, incluindo integrações externas e acessos administrativos.
2. Identifique condições de risco por fronteira com STRIDE ou taxonomia já usada. Descreva impacto e controles em termos defensivos, sem sequências de exploração. Separe riscos observados de hipóteses.
3. Priorize por probabilidade e impacto no contexto. Para cada risco material, defina controle, responsável, critério de verificação e risco residual. Reavalie quando o desenho mudar.

## Deliverables

Use o relatório compartilhado. Diagrama de fluxo, registro de riscos, decisões e verificações de controles.
