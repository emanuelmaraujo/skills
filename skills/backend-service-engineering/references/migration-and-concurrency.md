# Migração e concorrência

## Migração e coexistência

- [ ] Expanda o esquema de forma compatível. Defina defaults, serialização e erros por versão. Teste leituras e escritas cruzadas, registros anteriores, campos ausentes ou inéditos e rollback do binário com o esquema expandido.
- [ ] Faça backfill em lotes retomáveis e idempotentes. Acompanhe progresso, divergências e bloqueios. Só torne o campo obrigatório ou remova o contrato antigo após confirmar cobertura do backfill, retirada dos clientes antigos e condições de recuperação.
- [ ] Revise permissões e políticas na mesma mudança que adiciona ou expõe coluna, tabela, view ou função. Confira `GRANT` efetivos de tabela e coluna, heranças e superfícies de leitura e escrita. Em PostgreSQL, RLS filtra linhas. Proteja colunas com privilégios ou interface autorizada. Revise `USING` e `WITH CHECK` conforme a operação. Exercite usuários permitidos, negados e de outro tenant com papéis equivalentes aos reais e sem bypass de RLS.
- [ ] Em PostgreSQL, defina `SET search_path` explicitamente em toda função nova ou alterada e qualifique referências de aplicação. Use schemas confiáveis com `pg_temp` por último. Prefira `SECURITY INVOKER`. Para `SECURITY DEFINER`, justifique o privilégio, revise o dono e restrinja `EXECUTE` aos papéis previstos, removendo o acesso de `PUBLIC` na mesma transação quando aplicável. [Funções no PostgreSQL](https://www.postgresql.org/docs/current/sql-createfunction.html) · [Políticas RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- [ ] Valide instalação do zero e upgrade com dados existentes quando aplicável. Registre ordem de rollout, ponto de retorno e recuperação quando reverter o esquema causaria perda de dados.

## Teste de concorrência

1. Use versão e isolamento do banco do projeto, fixture descartável e duas conexões, sessões ou workers independentes disputando o mesmo recurso. Preserve transações reais e a entrada normal.
2. Sincronize a disputa com barreira, latch ou bloqueio controlado. Confirme que o primeiro participante chegou ao ponto crítico, coordene a tentativa do segundo e libere o primeiro. Use timeout limitado e limpeza garantida. Evite sleeps arbitrários e confirme sobreposição.
3. Verifique o resultado de cada participante e o estado persistido. Para idempotência, confirme um único efeito visível mesmo após repetição. Para conflito, confirme erro ou retry previsto e ausência de escrita parcial. Varie a ordem quando ela mudar o resultado. Por exemplo, dispare o mesmo job com a mesma chave em dois workers isolados e confirme apenas um efeito depois que ambos terminarem.
4. Use o runner ou cliente já disponível. Se não houver banco ou sessões independentes, marque a verificação como BLOCKED. Evidência unitária pode cobrir a regra local.
