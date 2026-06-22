# Ideias — backlog de hooks e ângulos

Anotações soltas de ângulos do paper que valem virar conteúdo. Quando uma ideia amadurecer, levá-la para uma pasta de campanha.

## Hooks por ângulo

### Tese central (sempre presente em variações)

- ~~**"Três LLMs leem a mesma ata e dão respostas diferentes — qual confiar?"**~~
  ~~Direto à tese. Conduz para "concordam na direção, divergem na intensidade".~~ — usado em `v1.0_lancamento/linkedin.md` (2026-04-26)

- **"Mesmo sinal, calibrações diferentes: o que três IAs dizem sobre cada ata do Copom"**
  Eco do título do paper. Bom para LinkedIn formal.

### Ângulo "overfit do Claude"

- **"O Claude tem o maior β̂ in-sample. E o pior desempenho out-of-sample. Por quê?"**
  Conduz para o trade-off viés-variância. Audiência técnica (data science / economistas).

- **"Quando 'mais sensível' não significa 'melhor'"**
  Versão genérica do ponto acima. Funciona como insight de ML aplicado.

### Ângulo "geração de modelo importa muito"

- **"Trocar gpt-4o-mini por gpt-4.1-mini elevou o R² de 0,11 para 0,66"**
  Apelo prático para quem usa LLMs em produção. Newsletter e LinkedIn.

### Ângulo "metodologia importa"

- **"Walk-forward derrubou o vencedor aparente do holdout"**
  Educativo sobre validação cruzada. Conduz para a importância de testar fora da amostra.

- **"O que fazer quando o modelo mais simples vence o teste? Investigar a janela."**
  Lição metodológica abstrata, com o caso concreto do baseline ganhando o holdout.

### Ângulo "small & cheap funciona"

- **"Você não precisa de um modelo de US$ 20/M tokens para ler o Copom"**
  Mensagem prática: modelos pequenos já capturam o essencial.

### Ângulo "ferramenta para o mercado"

- **"Como transformar uma ata do Copom em pontos percentuais da Selic"**
  Vende a ideia de tradução tom → métrica monetária. Bom para audiência de mesa.

- **"Um índice de tom calibrado para o Copom: o que três LLMs concordam (e onde divergem)"**
  Versão mais formal, para newsletter ou post longo.

### Ângulo "bastidores / pipeline"

- **"Construindo um pipeline reprodutível com LangChain, Pydantic e cache local"**
  Conteúdo de engenharia, audiência de devs. LinkedIn técnico ou blog.

- **"Por que um cache de 200 KB economiza meu paper toda semana"**
  Hook em torno do cache incremental. Apelo prático.

## Hashtags base (seleção rotativa por post)

#PolíticaMonetária #Copom #BancoCentral #Selic #IA #LLM #DataScience #Economia #AnáliseMacro #PythonBrasil #NLP #Econometria #ChatGPT #Claude #Gemini

## Lembretes

- O título do paper ("**Mesmo Sinal, Calibrações Diferentes**") é compacto e memorável. Vale repetir como assinatura entre posts.
- Os números mais "vendáveis": $R^2 \approx 0{,}66$ (OpenAI), 32% de vantagem na walk-forward, 73% de diferença na sensibilidade entre o melhor e pior LLM.
- Sempre que possível, mencionar que o exercício é **reprodutível** e **continuamente atualizável** (a cada nova ata do Copom).
