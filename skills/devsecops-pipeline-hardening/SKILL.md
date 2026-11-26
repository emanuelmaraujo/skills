---
name: devsecops-pipeline-hardening
description: "Revisa e melhora CI/CD quando a tarefa envolve scanners defensivos, permissões, segredos, SBOM, dependências ou proveniência de artefatos."
---

# devsecops-pipeline-hardening

Aplique primeiro o [guia compartilhado de execução e entrega](references/quality-gates.md).

## Contexto de aplicação

Identifique plataforma de CI, eventos confiáveis, publicação de artefatos e fronteiras de acesso. Traduza os controles para os mecanismos disponíveis na plataforma adotada.

## Procedimento

1. Mapeie eventos, origens de PR, runners, permissões, saídas e fronteiras de confiança. Use permissões mínimas, referências imutáveis para ações e credenciais de curta duração quando suportadas. Isole segredos de código não confiável.
2. Aproveite SAST, SCA e detecção de segredos já adotados. Separe sinais auditáveis de bloqueios, defina tratamento de falsos positivos e mantenha exceções com prazo. Produza SBOM e proveniência quando a cadeia de entrega exigir.
3. Verifique YAML e fluxos de PR, release e rollback em ambiente autorizado antes de promover. Registre a cobertura efetiva.

## Deliverables

Use o relatório compartilhado. Mudanças de pipeline, matriz de permissões e gates, resultados e lacunas.
