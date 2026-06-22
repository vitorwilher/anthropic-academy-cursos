# Model Context Protocol: Advanced Topics — Anotações

> Um bloco por aula. Preencha conforme avança. Cada aula tem uma seção
> "Para o meu curso (ideias de slide)" — é a fonte primária ao montar os slides.
> Pré-requisito: curso "Introdução ao MCP" (este é a sequência avançada).

---

## 1. Introduction
**Conceitos-chave:** visão geral dos recursos avançados; o que muda em relação ao básico.
**Resumo:** o curso vai além de tools/resources/prompts e cobre sampling, notificações,
roots e os transportes (STDIO e StreamableHTTP) para produção.
**Código/exemplos:**
**Para o meu curso (ideias de slide):** slide de abertura "de onde paramos" — recapitular
o básico (tools, resources, prompts) e mostrar o mapa do avançado.
**Dúvidas:**

## 2. Let's get started!
**Conceitos-chave:** setup do ambiente, SDK (Python), cliente + servidor de exemplo.
**Resumo:** preparar projeto com servidor e cliente MCP para exercitar os recursos.
**Código/exemplos:** `FastMCP`, `mcp dev`, MCP Inspector.
**Para o meu curso (ideias de slide):** mencionar o MCP Inspector como ferramenta de debug.
**Dúvidas:**

## 3. Sampling
**Conceitos-chave:** sampling = o **servidor** pede ao **cliente** uma chamada de LLM.
Inverte o fluxo: custo e modelo ficam do lado do cliente.
**Resumo:** o servidor não precisa de chave de API própria; delega a inferência ao host.
O host mantém controle (human-in-the-loop, escolha de modelo).
**Código/exemplos:** `ctx.session.create_message(...)` / `sampling/createMessage`.
**Para o meu curso (ideias de slide):** analogia — o servidor "terceiriza" o raciocínio
para o cliente. Exemplo finanças: servidor classifica o tom de uma ata sem ter LLM próprio.
**Dúvidas:**

## 4. Sampling walkthrough
**Conceitos-chave:** implementação passo a passo do sampling.
**Resumo:** tool que, ao rodar, dispara um `create_message` de volta ao cliente.
**Código/exemplos:** `messages`, `max_tokens`, `system_prompt`, `model_preferences`.
**Para o meu curso (ideias de slide):** bloco python com a tool que chama sampling.
**Dúvidas:**

## 5. Log and progress notifications
**Conceitos-chave:** notificações = mensagens **sem resposta** do servidor ao cliente.
Logging (níveis) e progress (operações longas).
**Resumo:** feedback em tempo real para tarefas demoradas; melhora UX.
**Código/exemplos:** `ctx.info(...)`, `ctx.report_progress(...)`.
**Para o meu curso (ideias de slide):** analogia — barra de progresso. Exemplo: baixar e
processar várias séries do BCB, reportando 1/4, 2/4...
**Dúvidas:**

## 6. Notifications walkthrough
**Conceitos-chave:** implementação de logging + progress.
**Resumo:** usar o objeto `Context` para emitir notificações dentro de uma tool.
**Código/exemplos:** `await ctx.report_progress(progress, total)`.
**Para o meu curso (ideias de slide):** bloco python com loop + report_progress.
**Dúvidas:**

## 7. Roots
**Conceitos-chave:** roots = fronteiras de **acesso a arquivos/diretórios** que o cliente
concede ao servidor. Segurança + descoberta.
**Resumo:** o servidor não vasculha o disco; opera só dentro dos roots permitidos.
**Código/exemplos:** `roots/list`, capability `roots`.
**Para o meu curso (ideias de slide):** analogia — crachá que abre só certas portas.
Exemplo: servidor só enxerga a pasta `dados/` do projeto.
**Dúvidas:**

## 8. Roots walkthrough
**Conceitos-chave:** cliente declara roots; servidor consulta a lista.
**Resumo:** `list_roots()` do lado do servidor para descobrir os diretórios autorizados.
**Código/exemplos:** `await ctx.session.list_roots()`.
**Para o meu curso (ideias de slide):** bloco mostrando o servidor listando roots.
**Dúvidas:**

## 9. Survey
**Conceitos-chave:** pausa/checkpoint do curso. (sem conteúdo técnico)
**Resumo:** —
**Para o meu curso (ideias de slide):** não vira slide.

## 10. JSON message types
**Conceitos-chave:** MCP roda sobre **JSON-RPC 2.0**: requests, responses, notifications.
Comunicação **bidirecional**.
**Resumo:** entender o formato das mensagens ajuda a depurar. request tem `id`;
notification não tem `id` (sem resposta).
**Código/exemplos:** blocos JSON de `request` / `response` / `notification`.
**Para o meu curso (ideias de slide):** tabela request vs response vs notification.
**Dúvidas:**

## 11. The STDIO transport
**Conceitos-chave:** STDIO = servidor roda **localmente**, comunicação por stdin/stdout.
**Resumo:** simples, ideal para dev e ferramentas locais; processo filho do host.
**Código/exemplos:** `transport="stdio"`.
**Para o meu curso (ideias de slide):** analogia — conversa por um cano local. Quando usar.
**Dúvidas:**

## 12. The StreamableHTTP transport
**Conceitos-chave:** StreamableHTTP = servidor **remoto**, acessível via HTTP.
Substitui o antigo HTTP+SSE.
**Resumo:** um único endpoint; suporta streaming via SSE quando necessário.
**Código/exemplos:** `transport="streamable-http"`, endpoint `/mcp`.
**Para o meu curso (ideias de slide):** local vs remoto; quando publicar um servidor.
**Dúvidas:**

## 13. StreamableHTTP in depth
**Conceitos-chave:** detalhes — POST único, respostas JSON ou stream SSE, sessões.
**Resumo:** o cliente faz POST; o servidor responde direto ou abre um stream.
**Código/exemplos:** headers `Mcp-Session-Id`, `Accept: text/event-stream`.
**Para o meu curso (ideias de slide):** diagrama de requisição/streaming.
**Dúvidas:**

## 14. State and the StreamableHTTP transport
**Conceitos-chave:** stateful vs stateless; sessões com `Mcp-Session-Id`.
**Resumo:** servidores remotos precisam pensar em estado/escala (múltiplos clientes,
balanceamento). Modo stateless facilita horizontal scaling.
**Código/exemplos:** `stateless_http=True`.
**Para o meu curso (ideias de slide):** trade-off estado vs escala; produção.
**Dúvidas:**

## 15. Assessment on MCP concepts
**Conceitos-chave:** avaliação dos conceitos.
**Resumo:** revisão de sampling, notificações, roots, JSON-RPC, transportes.
**Para o meu curso (ideias de slide):** slide de "mensagens-chave" recapitulando.

## 16. Wrapping up
**Conceitos-chave:** fechamento e próximos passos.
**Resumo:** levar o servidor a produção; segurança; conectar ao Claude.
**Para o meu curso (ideias de slide):** próximos passos + ligação com a customização (Focus).

---
