# SKILLS.md — padrão visual e achados técnicos dos slides

Tudo o que foi descoberto e padronizado ao construir os decks. Reaproveite em qualquer
curso novo para manter consistência.

## Stack

- **Quarto** (>= 1.6) com saída **reveal.js**.
- Tema compartilhado: [`slides/theme-am.scss`](slides/theme-am.scss).
- Verificação visual com **Google Chrome headless** (prints), sem depender de "achismo".

## Cabeçalho YAML padrão de um deck

```yaml
format:
  revealjs:
    theme: [default, ../theme-am.scss]
    logo: ../assets/logo-am.png
    embed-resources: true        # HTML autossuficiente (essencial — ver achado #1)
    slide-number: c/t            # "atual / total"
    width: 1280
    height: 720
    incremental: true
    code-overflow: wrap
    transition: slide
title-slide-attributes:
  data-background-image: ../assets/logo-am.png
  data-background-size: 400px    # logo CENTRAL da capa (ver achado #2)
  data-background-position: center 12%
```

## Identidade visual (paleta da Análise Macro)

| Cor | Hex | Uso |
|---|---|---|
| Navy | `#1c2d4f` | títulos, dividers, pílula do número |
| Azul | `#18a0d7` | destaques, filete sob h2, marcadores |
| Azul claro | `#56c2ec` | apoio |
| Fundo claro | `#f3f7fb` | cards/ilustrações |
| Texto | `#16233d` | corpo |

## Logo — tamanhos e regras (importante)

- **Capa (central):** via `title-slide-attributes` → `data-background-size: 400px`,
  `data-background-position: center 12%` (acima do título, sem sobrepor).
- **Canto inferior direito (todos os slides):** opção `logo:` do reveal, estilizada no
  tema com **`height: 130px !important`** (valores menores ficaram pequenos demais).
- **Slides escuros (dividers):** a logo colorida some no fundo navy. Solução — recolorir
  para branco com filtro CSS, detectando a classe global do reveal:
  ```scss
  .reveal.has-dark-background .slide-logo,
  .reveal-viewport.has-dark-background .slide-logo {
    filter: brightness(0) invert(1);
  }
  ```

## Número do slide (canto superior direito)

- Movido para o topo com uma "pílula" navy. **Achado:** o `background-color` só pega com
  **`!important`** (o reveal sobrescreve via variável CSS). Sem isso, em slide claro fica
  texto branco invisível.

## Caixa de PROMPT

- Prompts coláveis ficam em `::: {.prompt}` (um por slide), com rótulo "PROMPT — cole no
  Claude Code".
- Fonte do código do prompt: **`font-size: 0.9em`** (versões menores ficaram ilegíveis).
- **Não** usar `{.smaller}` em slide de prompt — encolhe tudo.

## Dividers de seção

- `# Título {background-color="#1c2d4f"}` → o reveal adiciona `has-dark-background` e
  deixa o texto branco automaticamente. Emoji no título dá vida (🎯 💬 ⚙️ 🔌 ✅).

## Achados que evitam retrabalho

1. **`embed-resources: true`** — sem isso, logo/ilustrações quebram ao abrir o HTML
   (caminho relativo) no Dropbox ou ao mover o arquivo. Com isso, vira um HTML único.
2. **Listas incrementais** — bullets só aparecem ao apertar →. Um slide "em branco" no
   print normalmente é só isso (não é bug).
3. **Emoji dentro de SVG** carregado via `<img>` pode não renderizar — nas ilustrações
   use **formas e texto**, não emoji.
4. **Navegação por hash** nos prints headless: `#/h` (horizontal) e `#/h/v` (vertical).
   Os slides de conteúdo (h2) ficam como **subslides verticais** sob cada seção (h1).

## Conferir um slide com print real (Chrome headless)

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL="file://$PWD/slides/claude-code-101/slides.html"
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1280,720 --virtual-time-budget=6000 \
  --screenshot=/tmp/slide.png "${URL}#/7/2"
```

## Ilustrações e diagramas

- SVGs próprios em [`slides/assets/`](slides/assets/): `illus-linechart`, `illus-bars`,
  `illus-network`, `illus-terminal`, `illus-chat`.
- Diagrama da jornada do projeto: **`fluxo-projeto-focus.excalidraw`** (fonte editável na
  extensão Excalidraw do VS Code) + **`fluxo-projeto-focus.svg`** (o que aparece no slide).
  Para atualizar: edite o `.excalidraw`, exporte como SVG por cima do `.svg`.

## Slides em duas colunas (texto + imagem)

```markdown
:::: {.columns}
::: {.column width="58%"}
- bullets
:::
::: {.column width="42%"}
![](../assets/illus-network.svg)
:::
::::
```
