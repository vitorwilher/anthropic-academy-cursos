# Introduction to Subagents — Anotações

> Um bloco por aula. Cada aula tem uma seção "Para o meu curso (ideias de slide)" — é a
> fonte primária ao montar os slides. Fonte: Anthropic Academy + docs oficiais
> (https://code.claude.com/docs/en/sub-agents).

---

## 1. What are subagents?
**Conceitos-chave:** subagent = assistente de IA especializado que roda em **janela de
contexto própria**, com system prompt, acesso a ferramentas e permissões próprios. Recebe
uma tarefa, trabalha independente e **devolve só o resultado/resumo** ao agente principal
— depois encerra. Subagents embutidos: **Explore** (read-only, Haiku, busca em código),
**Plan** (pesquisa no plan mode, read-only), **general-purpose** (todas as ferramentas).
**Resumo:** servem para **preservar contexto** (exploração e logs ficam fora da conversa
principal), **impor restrições** (limitar ferramentas), **reusar configurações** entre
projetos e **controlar custo** (rotear para modelos rápidos/baratos como Haiku).
**Código/exemplos:** "Use the Explore subagent to find where X is defined".
**Para o meu curso (ideias de slide):** analogia do assistente de pesquisa que vai à
biblioteca, lê 200 páginas e volta com 1 parágrafo — você não carrega as 200 páginas. O
porquê do contexto isolado: a janela de contexto é finita; encher de log/busca degrada o
trabalho. Mostrar os 3 embutidos numa tabela.
**Dúvidas:** —

## 2. Creating a subagent
**Conceitos-chave:** subagent é um **arquivo markdown com frontmatter YAML** + corpo
(system prompt). Campos: `name` (obrigatório, minúsculas-com-hifens), `description`
(obrigatório — Claude decide quando delegar a partir dela), `tools` (allowlist; herda
todas se omitido), `model` (`sonnet`/`opus`/`haiku`/`fable`/`inherit`). Comando
**`/agents`** abre interface (abas Running/Library) para criar com setup guiado ou
"Generate with Claude". Locais: **`.claude/agents/`** (projeto, versionado, time) e
**`~/.claude/agents/`** (usuário, todos os projetos). Edição direta no disco exige
reiniciar a sessão; via `/agents` vale na hora.
**Resumo:** criar = escrever o arquivo (ou usar `/agents`), salvar no escopo certo,
limitar ferramentas, escolher modelo. Subagent recebe **só** o system prompt do corpo +
ambiente básico, não o system prompt completo do Claude Code.
**Código/exemplos:**
```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---
You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```
**Para o meu curso (ideias de slide):** mostrar o arquivo anatomicamente (frontmatter vs
corpo). Tabela escopo projeto vs usuário. Demonstrar `/agents`. Exemplo econ: subagent
"resumidor-fonte" só leitura.
**Dúvidas:** —

## 3. Designing effective subagents
**Conceitos-chave:** boas práticas — **foco único** (cada subagent excelente em UMA
tarefa), **descrição detalhada** ("use proactively" encoraja delegação automática),
**limitar ferramentas** (segurança e foco; ex.: reviewer sem Edit/Write), **versionar**
(subagents de projeto vão para o git). `disallowedTools` para negar ferramentas
específicas. Escolher modelo por tarefa (Haiku para busca barata, Sonnet/Opus para
raciocínio). System prompt detalhado: diga o que olhar e como formatar a saída.
**Resumo:** subagent genérico demais não é delegado nem útil. Descrição clara = Claude
sabe quando chamar. Menos ferramentas = menos risco e mais foco.
**Código/exemplos:** `description: Expert code review specialist. Proactively reviews
code... Use immediately after writing or modifying code.`
**Para o meu curso (ideias de slide):** checklist das 4 boas práticas. Antes/depois de
descrição (vaga vs acionável). Por que read-only para um pesquisador.
**Dúvidas:** —

## 4. Using subagents effectively
**Conceitos-chave:** **delegação automática** (Claude decide pela `description` + contexto)
vs **explícita**: linguagem natural ("use the X subagent..."), **`@-mention`** (garante
aquele subagent), **`--agent <name>`** (sessão inteira assume o subagent). Padrões:
**isolar operações volumosas** (testes/logs/docs ficam no contexto do subagent, só o
resumo volta); **pesquisa paralela** (vários subagents independentes ao mesmo tempo, depois
o Claude sintetiza); **encadear** (sequência, cada um passa contexto ao próximo).
Foreground (bloqueia) vs background (concorrente, auto-nega prompts). **Quando NÃO usar:**
tarefas triviais (overhead não compensa), trabalho que precisa do histórico completo da
conversa (use um *fork*), ou quando muitos subagents devolvendo resultados longos enchem o
contexto principal de volta. Cada invocação = instância nova com contexto fresco (não
lembram conversas anteriores, salvo `memory`).
**Resumo:** delegue o que é volumoso/independente/repetitivo; mantenha o principal limpo.
Paralelize só quando os caminhos não dependem entre si.
**Código/exemplos:** "Research the authentication, database, and API modules in parallel
using separate subagents". "Use a subagent to run the test suite and report only the
failing tests".
**Para o meu curso (ideias de slide):** as 3 formas de invocar. Diagrama da pesquisa
paralela (uma fonte por subagent → síntese). Box "quando NÃO usar". Aviso: resultados
voltam ao contexto principal — não exagere no número de subagents.
**Dúvidas:** —

---
