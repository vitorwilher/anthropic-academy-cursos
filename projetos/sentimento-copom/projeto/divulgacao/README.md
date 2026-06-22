# Divulgação

Materiais de comunicação para "vender" o paper *Mesmo Sinal, Calibrações Diferentes: Um Índice de Tom das Atas do Copom com Múltiplos LLMs*. Posts em redes sociais, newsletters, blog, copy avulsa.

## Estrutura

- **`templates/`** — *boilerplate* por plataforma (LinkedIn, Instagram, newsletter, Twitter/X). Copiar para a pasta de campanha e preencher.
- **`v<X.Y>_<descritivo>/`** — uma pasta por campanha de divulgação. Cada *release* ou tema novo ganha sua pasta dedicada (ex.: `v1.0_lancamento/`, `v2.0_walkforward/`).
- **`ideias.md`** — *backlog* de ideias de posts ainda não desenvolvidos (hooks, ângulos, frases soltas).

## Convenção de nomes

- Pastas de campanha: `vX.Y_<descritivo-curto>/`.
- Arquivos por plataforma dentro da campanha: `linkedin.md`, `instagram.md`, `newsletter.md`, `twitter.md`.
- Cada arquivo abre com um *block quote* contendo metadados:
  ```
  > **Status:** rascunho | em revisão | publicado
  > **Data alvo:** AAAA-MM-DD
  > **Link após publicação:** _
  ```

## Fluxo recomendado

1. Anotar ideias cruas em `ideias.md`.
2. Quando uma ideia amadurecer, criar (ou usar) pasta de campanha apropriada.
3. Copiar os templates para dentro dela e preencher.
4. Iterar: escrever, revisar, publicar.
5. Após publicar, atualizar metadados no arquivo (status → publicado, link da publicação) para arquivar o histórico.

## Imagens prontas

PNGs gerados pelo *render* do paper já estão na raiz do projeto:

- `../sentimento_copom_indice.png` — gráfico do índice calibrado vs. ΔSelic
- `../sentimento_copom_zscore.png` — gráfico de surpresa de comunicação (z-score)

Podem ser usados diretamente ou recortados para formato 1:1 (Instagram), 1.91:1 (LinkedIn) ou 16:9 (newsletter).

## Tom da comunicação

- **LinkedIn:** técnico-acessível. Audiência de economistas, gestores, analistas. Pode mencionar termos como β̂, R², overfit, mas sempre traduzindo a interpretação.
- **Instagram:** mais visual e didático. Audiência mais ampla, focada em curiosidade. Carrosséis funcionam bem.
- **Newsletter:** narrativa longa, pedagógica. Pode aprofundar metodologia. Audiência fiel da Análise Macro.
- **Twitter/X:** punchy, threadeado. 1ª frase precisa ser hook.

Em todas as plataformas, **a tese central** ("concordam na direção, divergem na intensidade") deve aparecer de forma reconhecível. É o ângulo memorável do trabalho.
