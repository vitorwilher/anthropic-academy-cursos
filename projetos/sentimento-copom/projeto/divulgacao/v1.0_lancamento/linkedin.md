# LinkedIn — Mesmo Sinal, Calibrações Diferentes (lançamento v1.0)

> **Status:** rascunho
> **Data alvo:** 2026-04-26
> **Link após publicação:** _
> **Anexo:** PDF do paper (`sentimento_copom_IA_publico.pdf`)

## Hook (primeira tela do feed)

Três LLMs leem a mesma ata do Copom. Concordam sobre a direção — e discordam sobre a intensidade.

## Corpo

Acabou de sair a v1.0 de um paper que coautorei com Luiz Henrique Barbosa Filho:

**Mesmo Sinal, Calibrações Diferentes: Um Índice de Tom das Atas do Copom com Múltiplos LLMs.**

A pergunta é simples: dá para transformar o texto de uma ata do Copom em pontos percentuais da Selic — e três modelos de IA chegariam à mesma resposta?

Rodamos o **mesmo prompt** sobre as **mesmas 46 atas** (de ago/2020 em diante) em três modelos: Gemini Flash Lite, Claude Haiku 4.5 e GPT-4.1-mini. Cada ata recebeu um score de -3 (fortemente *dovish*) a +3 (fortemente *hawkish*), depois calibrado contra a variação efetiva da Selic.

A tese que sustenta o paper: **três LLMs concordam sobre a direção do tom de uma ata, mas divergem sobre a intensidade**. Para quem usa IA como termômetro de comunicação de banco central, isso muda como o número deve ser lido — score bruto não basta, calibração importa.

O paper completo está no anexo: metodologia, três camadas de validação (in-sample, holdout e walk-forward), tabelas, gráficos e código.

## Call to action

Se você usa LLMs para ler comunicação de banco central — qual provedor entraria no seu *ensemble*?

## Hashtags (5–10 focadas funcionam melhor)

#PolíticaMonetária #Copom #BancoCentral #Selic #LLM #IA #DataScience #Econometria #AnáliseMacro #NLP

## Imagem sugerida

- [ ] Capa do paper (titlepage com logo Análise Macro)
- [x] Gráfico do índice calibrado (`sentimento_copom_indice.png`) — formato 1.91:1
- [ ] Gráfico de z-score (`sentimento_copom_zscore.png`)
- [ ] Outra: __________

---

## Texto pronto para publicar (copie a partir daqui)

Três LLMs leem a mesma ata do Copom. Concordam sobre a direção — e discordam sobre a intensidade.

Acabou de sair a v1.0 de um paper que coautorei com Luiz Henrique Barbosa Filho:

Mesmo Sinal, Calibrações Diferentes: Um Índice de Tom das Atas do Copom com Múltiplos LLMs.

A pergunta é simples: dá para transformar o texto de uma ata do Copom em pontos percentuais da Selic — e três modelos de IA chegariam à mesma resposta?

Rodamos o mesmo prompt sobre as mesmas 46 atas (de ago/2020 em diante) em três modelos: Gemini Flash Lite, Claude Haiku 4.5 e GPT-4.1-mini. Cada ata recebeu um score de -3 (fortemente dovish) a +3 (fortemente hawkish), depois calibrado contra a variação efetiva da Selic.

A tese que sustenta o paper: três LLMs concordam sobre a direção do tom de uma ata, mas divergem sobre a intensidade. Para quem usa IA como termômetro de comunicação de banco central, isso muda como o número deve ser lido — score bruto não basta, calibração importa.

O paper completo está no anexo: metodologia, três camadas de validação (in-sample, holdout e walk-forward), tabelas, gráficos e código.

Se você usa LLMs para ler comunicação de banco central — qual provedor entraria no seu ensemble?

#PolíticaMonetária #Copom #BancoCentral #Selic #LLM #IA #DataScience #Econometria #AnáliseMacro #NLP
