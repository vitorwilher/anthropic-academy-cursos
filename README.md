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
| **Introdução ao MCP** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/introduction-to-mcp/slides.html) | [`slides/introduction-to-mcp/`](slides/introduction-to-mcp/) |
| **MCP: Tópicos Avançados** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/mcp-advanced-topics/slides.html) | [`slides/mcp-advanced-topics/`](slides/mcp-advanced-topics/) |
| **Construindo com a Claude API** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/building-with-claude-api/slides.html) | [`slides/building-with-claude-api/`](slides/building-with-claude-api/) |
| **Introdução às Agent Skills** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/agent-skills/slides.html) | [`slides/agent-skills/`](slides/agent-skills/) |
| **Introdução aos Subagents** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/subagents/slides.html) | [`slides/subagents/`](slides/subagents/) |
| **AI Fluency: Frameworks e Fundamentos** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/ai-fluency/slides.html) | [`slides/ai-fluency/`](slides/ai-fluency/) |
| **Introdução ao Claude Cowork** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/claude-cowork/slides.html) | [`slides/claude-cowork/`](slides/claude-cowork/) |
| **Claude Code na Prática** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/claude-code-in-action/slides.html) | [`slides/claude-code-in-action/`](slides/claude-code-in-action/) |
| **Capacidades e Limitações da IA** | ✅ Pronto | [Abrir slides](https://vitorwilher.github.io/anthropic-academy-cursos/slides/ai-capabilities-and-limitations/slides.html) | [`slides/ai-capabilities-and-limitations/`](slides/ai-capabilities-and-limitations/) |

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

Cursos transformados em slides, seguindo o catálogo oficial:

| # | Curso (Anthropic Academy) | Situação aqui |
|---|---|---|
| 1 | Claude 101 | ✅ Slides prontos |
| 2 | Claude Code 101 | ✅ Slides prontos |
| 3 | Claude Platform 101 | ✅ Slides prontos |
| 4 | Introduction to Model Context Protocol | ✅ Slides prontos |
| 5 | Model Context Protocol: Advanced Topics | ✅ Slides prontos |
| 6 | Building with the Claude API | ✅ Slides prontos |
| 7 | Introduction to Agent Skills | ✅ Slides prontos |
| 8 | Introduction to Subagents | ✅ Slides prontos |
| 9 | AI Fluency: Framework & Foundations | ✅ Slides prontos |
| 10 | Introduction to Claude Cowork | ✅ Slides prontos |
| 11 | Claude Code in Action | ✅ Slides prontos |
| 12 | AI Capabilities and Limitations | ✅ Slides prontos |

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
