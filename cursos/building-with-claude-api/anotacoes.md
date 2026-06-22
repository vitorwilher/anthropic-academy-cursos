# Building with the Claude API — Anotações

> Um bloco por módulo do curso (a página da plataforma divide cada módulo em várias
> aulas; aqui agrupo por módulo). Cada bloco tem uma seção "Para o meu curso (ideias de
> slide)" — é a fonte primária ao montar os slides. Idioma do material: pt-BR, público
> leigo (economistas/analistas). Fonte da grade: Skilljar + Coursera (jun/2026).

---

## 1. Getting Started with Claude
**Aulas:** Overview of Claude models · Accessing the API · Getting an API key · Making a request · Multi-turn conversations · System prompts · Temperature · Response streaming · Structured data
**Conceitos-chave:** chave de API (variável de ambiente), SDK `anthropic`, Messages API, `model`/`max_tokens`/`messages`, system prompt, conversas multi-turno (API é stateless — reenviar histórico), streaming, saída estruturada (`output_config.format`).
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** primeira chamada à Messages API em Python; system prompt; multi-turno; streaming; saída estruturada — exemplo financeiro (resumir relatório macro).
**Dúvidas:**

## 2. Prompt Engineering & Evaluation
**Aulas:** Prompt evaluation · A typical eval workflow · Generating test datasets · Running the eval · Model/Code based grading · Prompt engineering (clear and direct, specific, XML tags, examples)
**Conceitos-chave:** avaliar prompts com datasets; grading por código e por modelo (LLM-judge); técnicas de prompting (clareza, especificidade, tags XML, exemplos few-shot).
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** ser claro e específico; estrutura com tags XML; few-shot; ideia de eval (medir qualidade do prompt antes de produção).
**Dúvidas:**

## 3. Claude Features and Tool Use
**Aulas:** Introducing tool use · Tool functions/schemas · Handling message blocks · Sending tool results · Multi-turn with tools · Multiple tools · Fine-grained tool calling · Text edit tool · Web search tool · Extended thinking · Image support · PDF support · Citations · Prompt caching · Code execution and the Files API
**Conceitos-chave:** tool use (definição com `input_schema`, `tool_use`/`tool_result`, loop agêntico, tool runner), thinking adaptativo, visão/PDF (blocos `image`/`document`), prompt caching (prefix match, `cache_control`), código + Files API.
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** definir uma ferramenta e o loop; PDF (resumir Relatório de Inflação); prompt caching para reusar documento grande; thinking adaptativo.
**Dúvidas:**

## 4. Model Context Protocol (MCP)
**Aulas:** Introducing MCP · MCP clients · Defining tools/resources/prompts with MCP · Implementing a client · MCP review
**Conceitos-chave:** MCP como "USB-C" das integrações; servidores expõem tools/resources/prompts; conector MCP na Messages API (`mcp_servers` + `mcp_toolset`).
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** o que é MCP e por que padroniza integrações; exemplo de conectar uma fonte de dados (cotações/base interna).
**Dúvidas:**

## 5. Retrieval Augmented Generation (RAG)
**Aulas:** Introducing RAG · Text chunking · Text embeddings · The full RAG flow · BM25 lexical search · Multi-index RAG pipeline · Reranking · Contextual retrieval
**Conceitos-chave:** RAG = buscar trechos relevantes e injetar no prompt; chunking; embeddings; busca lexical (BM25) + semântica; reranking; contextual retrieval.
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** por que RAG (responder com base em documentos da casa, com fonte); fluxo: chunk → embed → buscar → responder.
**Dúvidas:**

## 6. Claude Code & Computer Use
**Aulas:** Anthropic apps · Claude Code setup · Claude Code in action · Enhancements with MCP servers · Parallelizing Claude Code · Automated debugging · Computer Use
**Conceitos-chave:** Claude Code (agente no terminal); Computer Use (Claude controla GUI via screenshots + mouse/teclado, client-side).
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** Claude Code para construir/depurar; Computer Use em uma frase (já há curso Code 101 — manter leve).
**Dúvidas:**

## 7. Agentic Workflows
**Aulas:** AI workflows · Parallelization · Chaining · Routing · Agents and tools · Environment inspection · Workflows vs agents
**Conceitos-chave:** workflows (você orquestra: paralelização, encadeamento, roteamento) vs agentes (o modelo decide a trajetória); quando usar cada um.
**Resumo:**
**Código/exemplos:**
**Para o meu curso (ideias de slide):** três padrões de workflow; workflow vs agente (comece simples); fechamento conectando ao projeto Focus.
**Dúvidas:**

## Final Assessment + Course Wrap Up
**Resumo:**
**Para o meu curso (ideias de slide):** mensagens-chave + próximos passos.

---
