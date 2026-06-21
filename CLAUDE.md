# CLAUDE.md

Briefing do projeto para o Claude Code. Leia também o [SKILLS.md](SKILLS.md), que reúne
o padrão visual e os "achados" técnicos dos slides.

## Objetivo

Organizar os cursos da **Anthropic Academy** e transformá-los em **slides** (Quarto +
reveal.js) para os cursos da **Análise Macro**, em **português (pt-BR)**, com exemplos de
economia e finanças.

## Estrutura

```
cursos/<curso>/            # anotações por curso (README = índice, anotacoes.md)
slides/<curso>/slides.qmd  # deck Quarto/reveal.js de cada curso
slides/theme-am.scss       # tema com a identidade da Análise Macro
slides/assets/             # logos, ilustrações SVG e o .excalidraw
index.html                 # landing page (GitHub Pages)
```

## Convenções

- Idioma: **pt-BR**. Público: **leigo** (economistas/analistas), explicar com clareza.
- Slides em **Quarto revealjs**, sempre com `embed-resources: true` (HTML autossuficiente).
- Todo deck usa `theme: [default, ../theme-am.scss]` e a logo da marca.
- Identidade visual, **tamanho da logo** e regras de layout: ver **[SKILLS.md](SKILLS.md)**.
- Não commitar artefatos de build (`.quarto/`, `*_files/`). Os `slides.html`
  (autossuficientes) **são versionados** porque vão para o GitHub Pages.

## Projeto-âncora dos cursos: Boletim Focus

Agente que baixa o PDF do Focus (BCB), extrai o texto, uma **Routine** do Claude redige o
resumo e um **GitHub Action** envia por e-mail toda segunda — automático. Atravessa as três
trilhas (Claude 101 → Code 101 → Platform 101), em **15 passos**. Regra de ouro do projeto:
**nunca inventar número**. Guia com os prompts:
https://analisemacro.github.io/imersao-claude-code/aula04-16062026.html

## Como renderizar

```bash
quarto render slides/claude-code-101/slides.qmd     # um deck
quarto preview slides/claude-code-101/slides.qmd    # com hot-reload
```

## Status dos cursos

- Claude 101 — ✅ slides prontos
- Claude Code 101 — ✅ slides prontos
- Claude Platform 101 — ✅ slides prontos
