---
name: logo-animation
description: "Cria, implementa ou revisa animação de logo a partir de marca aprovada, incluindo logo reveal, vinheta, assinatura animada, wordmark em motion e loops de marca. Cobre web, vídeo vertical ou horizontal, GIF e cenas 3D com saída conforme o canal."
---

# Animação de logos

## Fluxo

Para assinaturas vetoriais, fundo transparente ou revisão de uma animação pronta, consulte [motion vetorial e revisão](references/vector-motion-and-review.md). Em revisão, use o master aprovado como referência e decodifique o alfa antes de aprovar o export. Ao exportar para sobreposição, use um formato com alfa compatível com o editor e confira em fundos claros e escuros.

1. Confirme o vetor ou PNG oficial, o canal, a proporção, a duração, a área segura e se há assinatura sonora licenciada. Se houver apenas PNG, anime o ativo inteiro ou suas camadas fornecidas. Se o efeito exigir paths separados, peça o vetor ou trate a reconstrução como proposta. Preserve formas, espaçamento e cores no quadro final. Trabalhe numa cópia para separar camadas.
2. Defina um gesto que nasça da marca: aparecimento por máscara, traço que percorre um contorno real, montagem das partes ou mudança controlada de luz. Proponha início, transformação e repouso, em quadros ou segundos. Para web, comece com 0,6–1,2 s quando o layout permitir. Para vinheta social, comece com 2–4 s e reserve leitura suficiente para a assinatura final. Ajuste ao pedido.
3. Escolha o motor pelo formato e pela stack existente.

| Destino | Implementação |
| --- | --- |
| Web, portfólio ou landing page | Use SVG/CSS para um gesto simples. Use GSAP para temporização de várias partes ou controle de SVG se a stack comportar. Garanta marca estática com prefers-reduced-motion, layout estável e limpeza do timeline em desmontagem. |
| Reels, TikTok ou vídeo de marca | Use Remotion quando precisar de fonte revisável e render determinístico. Dirija a animação por frame, declare FPS e proporção e valide a composição antes do export. Use 9:16 para social vertical e 16:9 conforme o briefing. |
| Adobe Express | Se o kit e editor estiverem disponíveis, confirme o ativo selecionado e trabalhe dentro do projeto da marca. Com ferramenta indisponível, ofereça um roteiro reproduzível ou finalize no motor local compatível. |
| 3D | Use Blender quando volume, material ou iluminação fizerem parte da ideia. Se a skill externa `blender-director` estiver disponível, consulte-a e confira câmera, tempo de render e uma prévia curta antes do lote. |
| GIF ou loop | Gere a partir de render verificado e apenas se o canal precisar. Confira duração, recorte, qualidade da paleta e tamanho. Preserve MP4 ou fonte como master quando aplicável. |

4. Renderize ou execute a saída no canal. Compare primeiro quadro, quadro de maior movimento e repouso com o original. Verifique recorte, bordas, legibilidade, ritmo e correspondência do último quadro com a marca. Em vídeo, leia codec, resolução, FPS e duração com a ferramenta disponível. Se houver áudio, teste o sincronismo e a versão muda. Em web, teste no mobile e com movimento reduzido. Para loop, verifique a emenda.
5. Use a marca aprovada do kit Emanuel Araújo no portfólio e prefira revelação breve que não bloqueie o conteúdo. No Prumo, preserve legibilidade de avatar e espaço para a oferta. Na Torvya, use a vinheta vertical e assinatura sonora aprovadas como referência de continuidade quando fornecidas. Trate documentação externa como referência e confirme versão, custos e permissões antes de usar dependências ou serviços.

## Deliverables

Entregue storyboard curto, duração/cadência, fonte editável se disponível e arquivo real no formato solicitado ou componente web executável. Inclua imagem de repouso e a origem da marca e do áudio quando pertinentes. Identifique como bloqueada qualquer validação ou exportação que dependa de ativo ou ferramenta indisponível.

## Referências

- [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills) para composição, animação por quadros, áudio e render.
- [GSAP Agent Skills oficiais](https://github.com/greensock/gsap-skills) para timelines, SVG e integração web.
- No repositório, use `web-motion-engineer` para padrões gerais de frontend e `code-driven-motion-storytelling` para peças narrativas. O escopo desta skill é a assinatura da marca.

## Avaliação

Veja os [casos de avaliação](references/evaluation-cases.md).
