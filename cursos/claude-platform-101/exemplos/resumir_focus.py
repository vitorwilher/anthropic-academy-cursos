"""resumir_focus.py — gera o resumo do Boletim Focus via API do Claude.

É a "variante via API" do projeto Boletim Focus (Claude Platform 101): o mesmo
resumo que a Routine produz, mas feito por código que VOCÊ roda. Serve para ensinar,
no projeto de verdade, os conceitos do curso — primeira chamada de API, escolha de
modelo e tool use.

Regra de ouro do projeto: NUNCA inventar número.

Uso:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."        # no Windows: setx / variável de ambiente
    python resumir_focus.py                       # usa o data/focus_*.txt mais recente
    python resumir_focus.py --txt data/focus_2026-06-15.txt
    python resumir_focus.py --tools               # versão com tool use (mediana_focus)
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

import anthropic

MODELO = "claude-sonnet-4-6"

SISTEMA = (
    "Você resume o Boletim Focus do Banco Central para um público de economia e "
    "finanças. NUNCA invente número: toda mediana citada deve estar no texto. "
    "Escreva em português, em até 200 palavras."
)


def ultimo_txt(pasta: str = "data") -> str:
    """Retorna o caminho do focus_*.txt mais recente em `pasta`."""
    arquivos = sorted(glob.glob(os.path.join(pasta, "focus_*.txt")))
    if not arquivos:
        sys.exit(f"Nenhum focus_*.txt encontrado em {pasta}/ — rode o pipeline antes.")
    return arquivos[-1]


# --------------------------------------------------------------------------- #
# Versão 1 — chamada simples (primeira chamada de API)
# --------------------------------------------------------------------------- #
def resumir(texto: str) -> str:
    """Pede o resumo ao Claude em uma única chamada de API."""
    client = anthropic.Anthropic()  # lê ANTHROPIC_API_KEY do ambiente
    msg = client.messages.create(
        model=MODELO,
        max_tokens=600,
        system=SISTEMA,
        messages=[
            {
                "role": "user",
                "content": (
                    "Resuma o boletim abaixo com as medianas de IPCA, Selic, PIB e "
                    "câmbio e as 3 maiores revisões da semana:\n\n" + texto
                ),
            }
        ],
    )
    return "".join(b.text for b in msg.content if b.type == "text")


# --------------------------------------------------------------------------- #
# Versão 2 — com tool use (o modelo busca o número exato em vez de inventar)
# --------------------------------------------------------------------------- #
FERRAMENTAS = [
    {
        "name": "mediana_focus",
        "description": (
            "Retorna a mediana de mercado de um indicador (ex.: IPCA, Selic, PIB, "
            "câmbio) lendo o texto do Focus. Use para CADA número citado."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"indicador": {"type": "string"}},
            "required": ["indicador"],
        },
    }
]


def mediana_focus(indicador: str, texto: str) -> str:
    """Extrator simples (demo): acha a 1ª linha que cita o indicador e o 1º número.

    Num projeto real, troque por uma consulta à tabela já estruturada do Focus.
    """
    for linha in texto.splitlines():
        if indicador.lower() in linha.lower():
            m = re.search(r"\d+[.,]\d+", linha)
            if m:
                return m.group(0)
    return "não encontrado no texto"


def resumir_com_ferramenta(texto: str) -> str:
    """Resume rodando o agent loop: o modelo chama mediana_focus para cada número."""
    client = anthropic.Anthropic()
    mensagens = [
        {
            "role": "user",
            "content": (
                "Resuma o Focus abaixo (medianas de IPCA, Selic, PIB e câmbio + as 3 "
                "maiores revisões). Para CADA mediana, chame a ferramenta "
                "mediana_focus e use o valor retornado — não cite número sem "
                "consultá-la.\n\n" + texto
            ),
        }
    ]
    while True:
        resp = client.messages.create(
            model=MODELO,
            max_tokens=800,
            system=SISTEMA,
            tools=FERRAMENTAS,
            messages=mensagens,
        )
        if resp.stop_reason != "tool_use":
            return "".join(b.text for b in resp.content if b.type == "text")

        # registra o pedido do modelo e devolve os resultados das ferramentas
        mensagens.append({"role": "assistant", "content": resp.content})
        resultados = []
        for bloco in resp.content:
            if bloco.type == "tool_use":
                valor = mediana_focus(bloco.input.get("indicador", ""), texto)
                resultados.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": bloco.id,
                        "content": valor,
                    }
                )
        mensagens.append({"role": "user", "content": resultados})


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resume o Boletim Focus via API do Claude."
    )
    parser.add_argument("--txt", help="caminho do .txt (padrão: o mais recente em data/)")
    parser.add_argument(
        "--tools",
        action="store_true",
        help="usa tool use (mediana_focus) para garantir os números",
    )
    args = parser.parse_args()

    caminho = args.txt or ultimo_txt()
    with open(caminho, encoding="utf-8") as f:
        texto = f.read()

    print(f"[i] Resumindo {caminho} com {MODELO}"
          f"{' + tool use' if args.tools else ''}...\n")
    print(resumir_com_ferramenta(texto) if args.tools else resumir(texto))


if __name__ == "__main__":
    main()
