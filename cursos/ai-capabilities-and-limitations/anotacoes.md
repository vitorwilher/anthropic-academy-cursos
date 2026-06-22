# AI Capabilities and Limitations — Anotações

> Um bloco por aula. Cada aula tem uma seção "Para o meu curso (ideias de slide)" — é a
> fonte primária ao montar os slides. Curso **conceitual**: foco em modelo mental, não em código.

---

## 1. Getting started
**Conceitos-chave:** boas-vindas; curso conceitual; sem pré-requisito técnico.
**Resumo:** apresenta o objetivo — dar um modelo mental de como a IA generativa se comporta e por quê.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** capa + "o que você vai aprender".
**Dúvidas:**

## 2. Intro to AI Capabilities and Limitations
**Conceitos-chave:** companheiro do **4D Framework** (Delegation, Description, Discernment, Diligence); propriedades da máquina x competências humanas; continuum capacidade↔limitação.
**Resumo:** a mesma propriedade que é uma capacidade num contexto vira limitação em outro. A meta é reconhecer **que tipo** de saída inesperada ocorreu e aplicar a correção certa.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "capacidade e limitação são dois lados da mesma propriedade"; o 4D como pano de fundo.
**Dúvidas:**

## 3. What We Mean by AI
**Conceitos-chave:** IA generativa = grandes modelos de linguagem (LLMs); não é busca, não é banco de dados, não é calculadora.
**Resumo:** delimita o objeto: modelos que **geram** texto plausível, treinados em grande volume de dados. Útil distinguir de sistemas determinísticos.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "o que é (e o que não é) IA" — tabela LLM x planilha/banco/busca.
**Dúvidas:**

## 4. How AI Gets Its Character
**Conceitos-chave:** pré-treino (prever texto) → pós-treino/alinhamento (RLHF, *Constitutional AI*); "caráter" = útil, honesto, inofensivo.
**Resumo:** o comportamento do modelo vem do treino. O pré-treino cria a capacidade bruta; o alinhamento molda o tom e os limites. Ajuda a entender por que o modelo "se recusa" ou "puxa para o seguro".
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "de onde vem o jeitão do Claude" — duas etapas (pré-treino + alinhamento).
**Dúvidas:**

## 5. Next Token Prediction
**Conceitos-chave:** o modelo **prevê o próximo token** mais provável; geração probabilística; fluência ≠ veracidade; **alucinação** nasce daqui.
**Resumo:** a propriedade central. O modelo é fluente porque foi treinado para continuar texto de forma plausível — não porque "sabe" a verdade. Isso explica criatividade/fluência (capacidade) e alucinação/excesso de confiança (limitação).
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "prever a próxima palavra"; capacidade (rascunhar, reformular) x limitação (inventar número/citação com confiança).
**Dúvidas:**

## 6. Try it out (Next Token Prediction)
**Conceitos-chave:** exercício prático — observar fluência e onde a invenção aparece.
**Resumo:** pedir algo factual e checar; ver como o tom confiante esconde a incerteza.
**Código/exemplos:** prompt de teste pedindo um dado verificável e conferindo a fonte.
**Para o meu curso (ideias de slide):** callout de verificação ("nunca aceite número sem fonte").
**Dúvidas:**

## 7. Knowledge
**Conceitos-chave:** conhecimento "congelado" no treino; **knowledge cutoff**; vieses dos dados; sem acesso nativo a eventos recentes ou a dados privados.
**Resumo:** o modelo sabe o que estava nos dados até a data de corte. Capacidade: ampla cultura geral, padrões, definições. Limitação: desatualização, lacunas, viés, dados internos da sua empresa ele não conhece. Mitigação: fornecer contexto, RAG, busca/ferramentas.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "o que o modelo sabe — e até quando"; cutoff + viés; mitigação = dar o contexto (anexos, busca, RAG).
**Dúvidas:**

## 8. Try it out (Knowledge)
**Conceitos-chave:** exercício — perguntar algo recente e comparar com/sem contexto fornecido.
**Resumo:** demonstra como anexar a fonte transforma uma resposta frágil em uma resposta ancorada.
**Código/exemplos:** "sem anexo" → "com PDF anexado".
**Para o meu curso (ideias de slide):** "antes → depois" de fornecer contexto.
**Dúvidas:**

## 9. Working Memory
**Conceitos-chave:** **janela de contexto** = memória de trabalho; tudo que está na conversa; limite finito; "esquecimento" do início em conversas longas; *lost in the middle*.
**Resumo:** o modelo só "vê" o que está na janela. Capacidade: raciocinar sobre documentos longos colados ali. Limitação: estourar a janela, perder o começo, misturar conversas. Mitigação: ser conciso, resumir, recomeçar quando o assunto muda.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "memória de trabalho ≠ memória permanente"; gestão de contexto.
**Dúvidas:**

## 10. Try it out (Working Memory)
**Conceitos-chave:** exercício — conversa longa e observar perda de detalhes do início.
**Resumo:** mostra o valor de reafirmar o objetivo e de "limpar a mesa".
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** dica prática de higiene de contexto.
**Dúvidas:**

## 11. Steerability
**Conceitos-chave:** **dirigibilidade** — quanto o comportamento muda com o prompt; instruções, papéis, formato, exemplos (*few-shot*); sensível a fraseado; risco de *prompt injection*.
**Resumo:** o modelo é altamente moldável. Capacidade: você ajusta tom, formato, persona, rigor. Limitação: pode ser dirigido para o lado errado (instruções ambíguas ou maliciosas). Mitigação: instruções claras + verificação.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "você está no volante"; alavancas de prompt; lado B = injeção/ambiguidade.
**Dúvidas:**

## 12. Try it out (Steerability)
**Conceitos-chave:** exercício — mesmo pedido, prompts diferentes, resultados diferentes.
**Resumo:** demonstra o impacto de contexto/formato/exemplos.
**Código/exemplos:** "analise isso" vs. prompt estruturado.
**Para o meu curso (ideias de slide):** "antes → depois" de prompt.
**Dúvidas:**

## 13. When Properties Collide
**Conceitos-chave:** as quatro propriedades interagem; uma saída inesperada costuma ser **cruzamento** (ex.: fluência + cutoff = alucinação confiante; janela cheia + dirigibilidade = ignora instrução do início).
**Resumo:** o framework de diagnóstico: identifique qual propriedade está em jogo para escolher a correção. Núcleo do curso.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** **tabela de diagnóstico** "sintoma → propriedade → correção".
**Dúvidas:**

## 14. Next Steps
**Conceitos-chave:** uso responsável; *human in the loop*; verificação; ligar com o 4D.
**Resumo:** hábitos de verificação e quando confiar/desconfiar.
**Código/exemplos:** —
**Para o meu curso (ideias de slide):** "mensagens-chave" + "próximos passos".
**Dúvidas:**

## 15. Course Quiz — pontos revisados
**Resumo:** revisa as quatro propriedades e o diagnóstico de saídas inesperadas.
**Para o meu curso (ideias de slide):** —

---
