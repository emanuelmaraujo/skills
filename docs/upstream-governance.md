# Workflow leve de evolução das Agent Skills

**Objetivo:** melhorar as skills conforme forem usadas, aproveitando projetos de referência já conhecidos. Não consumir tokens de Claude, Codex ou ChatGPT automaticamente.

## Modo A — Radar GitHub Actions (automático e leve)

- Uma vez por semana, o GitHub Actions consulta **somente metadados** dos repositórios declarados em `upstreams.json`.
- A primeira execução cria uma issue única com a linha de base dos SHAs. Execuções futuras comparam os últimos commits: **só comentam quando há mudança**.
- O comentário contém links diretos para comparar versões externas. Ele **não analisa código com IA, não executa scripts externos, não copia skills e não abre PR de alteração automaticamente**.
- Sem instalações, APIs pagas, modelos de IA, cron em VPS, scripts locais ou uso de tokens de agentes. Usa runner padrão `ubuntu-latest`, Python stdlib e `gh` já disponível.
- `workflow_dispatch` permite disparar a consulta manualmente. Se não houver novidades, não cria comentários repetidos.
- Dependência: a configuração de Issues/Actions do repositório deve permitir `issues: write` ao token. A execução agendada ocorre na branch padrão após merge. GitHub Actions pode atrasar horários de cron.
- **Custos:** em repositório público, minutos dos runners padrão do GitHub Actions são gratuitos. Se o repositório ficar privado, passar a usar runners maiores, publicar artefatos em grande volume ou ativar serviços de terceiros, reavaliar cobrança antes de continuar.
- Registro de status: issue “Radar de skills — upstreams” e resumo das execuções do Actions.

## Modo B — Melhorar uma skill (manual, mediante feedback)

1. Identificar a skill e descrever **o resultado real** que falhou ou que poderia melhorar. Não exigir benchmark de todo o catálogo.
2. Abrir [issue de feedback](../issues/new/choose) com cenário, esperado e observado; se disponível, link para PR/execução.
3. Selecionar **1–3 fontes de referência** consolidadas, priorizando documentação e SKILL.md de autores conhecidos: Anthropic, OpenAI Plugins, Matt Pocock, Corey Haines, Vercel, etc. Consultar apenas os arquivos relevantes; evitar ler centenas de skills.
4. Comparar escopo, abordagem, exemplos, limites e licença. **Nunca copiar automaticamente** scripts, propagandas embutidas, tokens ou instruções inseguras de terceiros.
5. Criar branch e PR de melhoria **apenas daquela skill**, acrescentando referências/exemplos sob demanda se necessário.
6. Executar só verificações estáticas leves locais/CI existentes. Quando você já estiver usando a skill com César/Claude/Codex, coletar feedback natural da execução; avaliações adicionais com IA apenas quando você pedir explicitamente.
7. Revisar o diff e fazer merge somente após autorização. Atualizar instalações globais de forma explícita, não por mudança automática silenciosa.

## Prompt para Work ou César — executar apenas quando solicitado

> Analise a issue de feedback selecionada do repositório `emanuelmaraujo/skills`. Examine somente a skill afetada e até três implementações de referência bem mantidas. Preserve o propósito, melhore gatilho, instruções especializadas, exemplos, portabilidade e segurança; não faça análise geral do catálogo nem benchmarking com IA. Use branch isolada, validação estática barata e PR revisável. Não faça merge, deploy, instalações externas ou testes pagos. Se não houver feedback concreto, registre sugestões e não reescreva arquivos por reescrever.

## Diferença importante

O GitHub Actions **detecta novidades**. Melhorar o conteúdo exige julgamento humano ou uso pontual de um agente quando autorizado. Nenhum workflow gratuito de GitHub implica raciocínio de IA gratuito. O relatório aprofundado do ChatGPT é um processo separado e não é acionado por este GitHub Action.
