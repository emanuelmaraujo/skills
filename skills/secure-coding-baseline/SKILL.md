---
name: secure-coding-baseline
description: "Aplica ou audita controles de segurança para mudanças de código, incluindo validação, autorização, fronteiras de saída, impressão e requisitos ASVS."
---

# secure-coding-baseline

Aplique o [guia compartilhado de execução e entrega](references/quality-gates.md). Identifique stack, entradas, dados sensíveis e fronteiras de confiança. Em auditoria, inspecione controles e execute apenas verificações autorizadas.

## Procedimento

1. Valide tipo, formato e tamanho na fronteira confiável. Use consultas parametrizadas, codificação de saída adequada ao destino, autorização no servidor, mínimo privilégio e erros sem dados sensíveis. Revise segredos, arquivos, dependências e configuração do fluxo. Use primitivas criptográficas consolidadas e permitidas.
2. Quando texto de cliente chegar a um spooler, driver ou impressora, siga o dado até os bytes finais. Use uma API de texto isolada de comandos ou rasterize com o mecanismo aprovado. Em protocolo bruto, mantenha comandos em caminhos tipados com parâmetros internos validados. Rejeite ou substitua controles no texto segundo a política do produto e valide os bytes emitidos após normalização, encoding e truncamento. Gere quebras e comandos permitidos pelo formatador confiável. Capture o transporte em teste e use fixtures com controles genéricos, acentos e comprimentos limite. Confirme que os campos aparecem apenas como texto permitido e que os comandos confiáveis do job permanecem idênticos. [Referência de comandos ESC/POS](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/commands.html)
3. Use a versão do [OWASP ASVS](https://asvs.owasp.org/) adotada pelo projeto ou identifique a edição oficial consultada. Para cada requisito pertinente, registre ID versionado (como `v5.0.0-1.2.5` se houver chamadas ao sistema), aplicabilidade, fluxo ou arquivo, evidência, resultado e lacuna. Use o texto oficial para delimitar a cobertura. Registre o controle do protocolo de impressão como requisito do projeto quando a cobertura ASVS for insuficiente.
4. Verifique casos permitidos, negados e de erro pela interface normal. Aplique controles transversais aqui e use a skill responsável para mecanismos específicos, como permissões de migração no backend.

## Deliverables

Use o relatório compartilhado. Inclua evidência por controle, requisitos ASVS aplicados, correções autorizadas e lacunas de verificação.
