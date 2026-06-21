# Cursos Anthropic Academy → Material da Análise Macro

Slides em **português (pt-BR)**, com exemplos de **economia e finanças**, construídos a
partir dos cursos da [Anthropic Academy](https://anthropic.skilljar.com/) e adaptados para
os cursos da **[Análise Macro](https://analisemacro.com.br/)**.

Feito com [Quarto](https://quarto.org/) + reveal.js. Identidade visual e decisões técnicas
em [SKILLS.md](SKILLS.md); briefing do projeto em [CLAUDE.md](CLAUDE.md).

🔗 **Página inicial dos slides:** https://vitorwilher.github.io/anthropic-academy-cursos/

## 🎬 Slides publicados

| Curso | Status | Slides (GitHub Pages) | Fonte |
|---|---|---|---|
| **Claude 101** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/claude-101/slides.html) | [`slides/claude-101/`](slides/claude-101/) |
| **Claude Code 101** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/claude-code-101/slides.html) | [`slides/claude-code-101/`](slides/claude-code-101/) |
| **Claude Platform 101** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/claude-platform-101/slides.html) | [`slides/claude-platform-101/`](slides/claude-platform-101/) |

> Dica de navegação no reveal.js: **setas** ← → para avançar, **F** tela cheia,
> **S** modo apresentador (com as notas), **O** visão geral.

## 🧭 Projeto-âncora: Boletim Focus

Um exemplo prático atravessa os três cursos: um **agente que resume o Boletim Focus do
Banco Central e envia por e-mail toda segunda, sozinho**.

1. **Construir** (Claude Code 101) — baixar o PDF, extrair o texto, testar, escrever o
   roteiro do agente. *Passos 1–11, na sua máquina.*
2. **Publicar** (Claude Platform 101) — subir para o GitHub. *Passo 12.*
3. **Automatizar** (Claude Platform 101) — Secrets, conectar o GitHub e criar a **Routine**
   agendada. *Passos 13–15, na nuvem.*

Guia completo com os prompts:
[analisemacro.github.io/imersao-claude-code/aula04-16062026.html](https://analisemacro.github.io/imersao-claude-code/aula04-16062026.html)

## 🗺️ Trilha de cursos (catálogo da Anthropic Academy)

Cursos já transformados em slides e os **previstos** (roadmap), seguindo o catálogo oficial:

| # | Curso (Anthropic Academy) | Situação aqui |
|---|---|---|
| 1 | Claude 101 | ✅ Slides prontos |
| 2 | Claude Code 101 | ✅ Slides prontos |
| 3 | Claude Platform 101 | ✅ Slides prontos |
| 4 | Introduction to Model Context Protocol | 🔜 Previsto |
| 5 | Model Context Protocol: Advanced Topics | 🔜 Previsto |
| 6 | Building with the Claude API | 🔜 Previsto |
| 7 | Introduction to Agent Skills | 🔜 Previsto |
| 8 | Introduction to Subagents | 🔜 Previsto |
| 9 | AI Fluency: Framework & Foundations | 🔜 Previsto |
| 10 | Introduction to Claude Cowork | 🔜 Previsto |
| 11 | Claude Code in Action | 🔜 Previsto |
| 12 | AI Capabilities and Limitations | 🔜 Previsto |

## 📁 Estrutura do repositório

```
cursos/<curso>/            # anotações por curso (índice + anotacoes.md)
slides/<curso>/slides.qmd  # deck Quarto/reveal.js
slides/theme-am.scss       # tema da Análise Macro
slides/assets/             # logos, ilustrações SVG e diagrama .excalidraw
index.html                 # landing page (GitHub Pages)
CLAUDE.md · SKILLS.md      # briefing e padrão técnico
```

## 🛠️ Como renderizar localmente

```bash
# requer o Quarto: https://quarto.org/docs/get-started/
quarto render slides/claude-code-101/slides.qmd      # gera o .html
quarto preview slides/claude-code-101/slides.qmd     # hot-reload no navegador
```

---

Feito por **Vitor Wilher** · [Análise Macro](https://analisemacro.com.br/) ·
com o [Claude Code](https://claude.com/claude-code).
