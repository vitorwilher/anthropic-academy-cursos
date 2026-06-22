# Projetos — aulas-projeto da imersão

Aulas baseadas em **projetos reais** do portfólio da Análise Macro, adaptadas para a
**imersão em Claude Code**. Diferente das trilhas (Claude 101 → Code 101 → Platform 101),
aqui o aluno **reconstrói um projeto inteiro dirigindo o agente**, prompt a prompt.

Cada projeto segue o mesmo padrão visual dos cursos (Quarto + reveal.js, tema
[`slides/theme-am.scss`](../slides/theme-am.scss)).

## Sentimento COPOM — aula de 2 horas

Reconstruir, do zero e com o Claude Code, um **Índice de Tom das atas do Copom** calibrado
em pontos da Selic, usando **três LLMs em paralelo** (Gemini, Claude e GPT) + um baseline
léxico, validado em três camadas e entregue como **paper Quarto** reprodutível.

```
sentimento-copom/
├── slides.qmd / slides.html   # a aula de 2 horas (caixas de PROMPT por etapa)
└── projeto/                   # cópia auditável do projeto original
    ├── sentimento_copom_IA_base.qmd      # paper (chunks visíveis)
    ├── sentimento_copom_IA_publico.qmd   # edição do leitor (chunks ocultos)
    ├── scores_{gemini,claude,openai}_cache.csv
    ├── atas_cache.json / selic_cache.json
    ├── referencias.bib / CHANGELOG.md / README.md
    └── sentimento_copom_{indice,zscore}.png
```

Renderizar a aula:

```bash
quarto render projetos/sentimento-copom/slides.qmd
```

> **Regra de ouro do projeto:** nunca inventar número — todo valor (score, β̂, R², RMSE)
> sai de uma célula que roda.
