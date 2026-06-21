# Slides

Material destilado das anotações dos cursos, em formato de apresentação.

**Ferramenta sugerida:** [Quarto](https://quarto.org/) com saída `reveal.js`
(Markdown → slides HTML). Cada curso tem um `.qmd` de rascunho.

## Renderizar

```bash
quarto render slides/claude-code-101/slides.qmd
# ou, para preview ao vivo:
quarto preview slides/claude-code-101/slides.qmd
```

> Se preferir outra ferramenta (Marp, reveal.js puro, PowerPoint via Pandoc),
> é só avisar que ajusto os templates.
