# Introduction to Agent Skills — Anotações

> Um bloco por aula. Preencha conforme avança. Cada aula tem uma seção
> "Para o meu curso (ideias de slide)" — é a fonte primária ao montar os slides.
>
> Fonte: https://anthropic.skilljar.com/introduction-to-agent-skills (6 aulas, ~30 min)

---

## 1. What are skills?
**Conceitos-chave:** Skill = pasta com um `SKILL.md` que empacota instruções + recursos
reutilizáveis para uma tarefa recorrente. Frontmatter YAML (`name`, `description`) é o
"cartão de visita" que o Claude lê para decidir quando usar a skill.
**Resumo:** Em vez de repetir a mesma instrução toda conversa, você "ensina uma vez" e o
Claude aplica sozinho quando o pedido bate com a descrição (auto-invocação).
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** analogia "manual de procedimento da mesa";
diferença entre prompt avulso (some) e skill (fica e reaparece sozinha).
**Dúvidas:**

## 2. Creating your first skill
**Conceitos-chave:** estrutura mínima: uma pasta + `SKILL.md`. Frontmatter com `name`
(minúsculas, hífens, ≤64 chars, sem "claude"/"anthropic") e `description` (≤1024 chars,
clara sobre QUANDO usar). Corpo em Markdown com as instruções/passos.
**Resumo:** Criar a primeira skill é escrever um arquivo. A `description` é o campo mais
importante: é ela que faz o casamento (matching) automático funcionar.
**Código/exemplos:** `SKILL.md` de "Análise de balanço" (parecer padronizado de DRE).
**Para o meu curso (ideias de slide):** mostrar `SKILL.md` completo em bloco ```markdown.
**Dúvidas:**

## 3. Configuration and multi-file skills
**Conceitos-chave:** **progressive disclosure** em 3 camadas — metadados (~100 tokens,
sempre carregados) → corpo do `SKILL.md` (ao ativar) → recursos em `scripts/`,
`references/`, `assets/` (só quando necessário). `allowed-tools` restringe ferramentas.
Scripts rodam sem consumir contexto.
**Resumo:** Skills grandes não estouram o contexto porque o Claude carrega só o que
precisa, quando precisa. Arquivos de apoio ficam ao lado do `SKILL.md`.
**Código/exemplos:** pasta com `SKILL.md` + `references/metodologia.md` + `scripts/calc.py`.
**Para o meu curso (ideias de slide):** diagrama das 3 camadas; árvore de pastas.
**Dúvidas:**

## 4. Skills vs. other Claude Code features
**Conceitos-chave:** Skill (acionada por relevância, reutilizável, portátil) vs.
`CLAUDE.md` (contexto sempre presente do projeto) vs. hooks (automação determinística por
evento) vs. subagents (delegação com contexto próprio).
**Resumo:** Use skill quando a tarefa é recorrente mas só faz sentido em certos momentos.
`CLAUDE.md` é "sempre ligado"; skill é "liga quando o assunto aparece".
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** tabela comparativa skill x CLAUDE.md x hook x subagent.
**Dúvidas:**

## 5. Sharing skills
**Conceitos-chave:** compartilhar no time commitando a pasta da skill no repositório;
distribuir mais amplamente via **plugins**; implantar na organização toda via
**managed settings** (enterprise). Skill é só arquivos → versionável no Git.
**Resumo:** Como skill é uma pasta de arquivos, distribuir é dar acesso aos arquivos —
do repo do time ao deploy corporativo.
**Código/exemplos:** `.claude/skills/` no repositório do projeto.
**Para o meu curso (ideias de slide):** três níveis de distribuição (repo → plugin → org).
**Dúvidas:**

## 6. Troubleshooting skills
**Conceitos-chave:** principal causa de skill "não disparar" = `description` vaga ou
genérica. Boas práticas: descrição específica sobre QUANDO usar; corpo enxuto; testar com
pedidos reais; mover detalhe para arquivos de apoio.
**Resumo:** Se a skill não ativa, quase sempre é a descrição. Itere na descrição como se
itera num prompt.
**Código/exemplos:** antes/depois de uma `description`.
**Para o meu curso (ideias de slide):** checklist de depuração; antes→depois da descrição.
**Dúvidas:**

---
