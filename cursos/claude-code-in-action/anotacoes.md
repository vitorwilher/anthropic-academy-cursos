# Claude Code in Action — Anotações

> Um bloco por aula (lições reais da Anthropic Academy). Cada aula tem uma seção
> "Para o meu curso (ideias de slide)" — é a fonte primária ao montar os slides.
> Fonte: https://anthropic.skilljar.com/claude-code-in-action

---

## 1. Introduction
**Conceitos-chave:** visão geral do curso; o que é o Claude Code como agente no terminal.
**Resumo:** curso operacional/avançado, sequel do Code 101.
**Código/exemplos:**
**Para o meu curso (ideias de slide):** posicionar como "mão na massa" — não repetir o 101.
**Dúvidas:**

## 2. What is a coding assistant?
**Conceitos-chave:** assistente de código vs. autocomplete; agente que usa ferramentas (ler/editar arquivos, rodar shell), opera em loop.
**Resumo:** diferença entre completar código e um agente que age sobre o repositório inteiro.
**Código/exemplos:**
**Para o meu curso (ideias de slide):** comparar autocomplete x agente; o loop pensar→agir→observar.
**Dúvidas:**

## 3. Claude Code in action
**Conceitos-chave:** demo de uma tarefa real ponta a ponta.
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** exemplo de tarefa real (corrigir bug num script de coleta de dados).
**Dúvidas:**

## 4. Claude Code setup
**Conceitos-chave:** instalação (CLI/extensão), login, primeiro `claude` na pasta.
**Resumo:** já coberto no 101 — aqui só recapitular rápido.
**Código/exemplos:** `npm install -g @anthropic-ai/claude-code`; `claude`.
**Para o meu curso (ideias de slide):** breve, não duplicar a checklist do 101.
**Dúvidas:**

## 5. Project setup
**Conceitos-chave:** `/init` para gerar o `CLAUDE.md`; rodar na raiz do projeto.
**Resumo:** `/init` faz o Claude explorar o repo e escrever um CLAUDE.md inicial.
**Código/exemplos:** `/init`
**Para o meu curso (ideias de slide):** `/init` como ponto de partida + revisar o CLAUDE.md gerado.
**Dúvidas:**

## 6. Adding context
**Conceitos-chave:** `CLAUDE.md`, `@` menções de arquivos, atalhos/hotkeys, Plan Mode, Thinking Mode, gerenciamento de contexto.
**Resumo:** como alimentar o contexto certo: memória, menção explícita de arquivos, planejar antes de agir, pensar mais em problemas difíceis.
**Código/exemplos:** `@src/baixar_focus.py`; Shift+Tab → Plan Mode; "think"/"think hard".
**Para o meu curso (ideias de slide):** Plan Mode e Thinking Mode como diferenciais do curso; @ menções para apontar arquivos; hotkeys.
**Dúvidas:**

## 7. Making changes
**Conceitos-chave:** loop explore→plan→code→commit; revisar diffs; permissões.
**Resumo:** dirigir o agente em mudanças reais, aprovando ações.
**Código/exemplos:**
**Para o meu curso (ideias de slide):** o loop agêntico aplicado; aprovar/rejeitar edições; modos de permissão.
**Dúvidas:**

## 8. Custom commands
**Conceitos-chave:** slash commands customizados em `.claude/commands/*.md`; argumentos com `$ARGUMENTS`.
**Resumo:** empacotar prompts recorrentes como `/comando` reutilizável (no projeto ou no usuário).
**Código/exemplos:** `.claude/commands/revisar.md` → vira `/revisar`.
**Para o meu curso (ideias de slide):** criar `/sanity-check` para o pipeline de dados; markdown com $ARGUMENTS.
**Dúvidas:**

## 9. MCP servers with Claude Code
**Conceitos-chave:** Model Context Protocol; conectar ferramentas/dados externos; `claude mcp add`; escopos (local/project/user); `.mcp.json`.
**Resumo:** estender o Claude Code com servidores MCP (GitHub, bancos, APIs).
**Código/exemplos:** `claude mcp add ...`; `/mcp` para listar.
**Para o meu curso (ideias de slide):** MCP dentro do Code (não só no Chat); exemplo conectar base de dados/cotações.
**Dúvidas:**

## 10. Github integration
**Conceitos-chave:** MCP/integração do GitHub; `gh`; criar PRs, revisar, comentar; @claude no GitHub Actions.
**Resumo:** trabalhar com issues/PRs direto do Claude Code.
**Código/exemplos:** `gh auth login`; servidor MCP do GitHub.
**Para o meu curso (ideias de slide):** abrir PR, revisar diff, conectar ao repo do Focus.
**Dúvidas:**

## 11. Introducing hooks
**Conceitos-chave:** hooks = comandos shell disparados em eventos do ciclo de vida do Claude Code.
**Resumo:** automatizar comportamento determinístico (formatar, testar, bloquear).
**Código/exemplos:**
**Para o meu curso (ideias de slide):** o que são hooks e por que (determinismo vs. pedir ao modelo).
**Dúvidas:**

## 12. Defining hooks
**Conceitos-chave:** eventos: PreToolUse, PostToolUse, UserPromptSubmit, Stop, SessionStart, etc.; matchers; config em `settings.json`.
**Resumo:** estrutura JSON de um hook (event → matcher → command).
**Código/exemplos:** `.claude/settings.json` com `hooks`.
**Para o meu curso (ideias de slide):** anatomia de um hook; tabela de eventos.
**Dúvidas:**

## 13. Implementing a hook
**Conceitos-chave:** escrever um hook concreto; receber JSON via stdin; código de saída.
**Resumo:** exemplo prático de implementação.
**Código/exemplos:** hook que roda `black`/`ruff` em PostToolUse de Edit.
**Para o meu curso (ideias de slide):** formatar Python automaticamente após edição.
**Dúvidas:**

## 14. Gotchas around hooks
**Conceitos-chave:** hooks rodam com suas permissões; exit code 2 bloqueia; cuidado com loops/lentidão; segurança.
**Resumo:** armadilhas comuns.
**Código/exemplos:**
**Para o meu curso (ideias de slide):** callout de pitfalls (segurança, exit codes, performance).
**Dúvidas:**

## 15. Useful hooks!
**Conceitos-chave:** exemplos úteis: rodar testes, formatar, notificar.
**Resumo:**
**Código/exemplos:** PostToolUse → pytest; Stop → notificação.
**Para o meu curso (ideias de slide):** hook "rodar pytest -m 'not network' após editar src/".
**Dúvidas:**

## 16. Another useful hook
**Conceitos-chave:** segundo exemplo (ex.: bloquear edição de arquivos sensíveis / proteger .env).
**Resumo:**
**Código/exemplos:** PreToolUse que bloqueia escrita em `.env`/secrets.
**Para o meu curso (ideias de slide):** guard-rail: nunca deixar o agente tocar credenciais.
**Dúvidas:**

## 17. The Claude Code SDK
**Conceitos-chave:** uso headless/programático; `claude -p` (print mode); SDK Python/TS; CI; saída estruturada.
**Resumo:** rodar o Claude Code sem interação, em scripts e pipelines (GitHub Actions).
**Código/exemplos:** `claude -p "..." --output-format json`.
**Para o meu curso (ideias de slide):** headless no CI; ligar com o agente do Focus que roda na nuvem.
**Dúvidas:**

## 18. Quiz on Claude Code
**Resumo:** revisão dos conceitos.
**Para o meu curso (ideias de slide):** não vira slide próprio; reforça mensagens-chave.

## 19. Summary and next steps
**Resumo:** consolidação; próximos passos.
**Para o meu curso (ideias de slide):** slide de conclusão (mensagens-chave + próximos passos).

---
