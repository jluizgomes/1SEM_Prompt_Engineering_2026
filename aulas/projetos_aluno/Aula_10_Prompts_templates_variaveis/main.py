"""
FIAP · Prompt Engineering & AI — 1º Semestre 2026
Esqueleto para alunos — complete os TODOS abaixo.
Aula 10 — Templates e variáveis dinâmicas

Projeto local: experimentos com templates e variáveis dinâmicas que substituem o
chamar_llm() manual do 1º semestre — menos código, mais composição.

Como rodar:
    1. pip install -r requirements.txt
    2. confirme o .env (OLLAMA_HOST / OLLAMA_API_KEY / OLLAMA_MODEL)
    3. python main.py
"""
import os

from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

# ─────────────────────────────────────────────────────────────
# Configuração via .env (Ollama Cloud por padrão; veja .env.example)
# ─────────────────────────────────────────────────────────────
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "https://ollama.com")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:120b")

if not OLLAMA_API_KEY:
    raise RuntimeError(
        "OLLAMAAPIKEY não encontrada. Copie .env.example para .env e preencha a chave."
    )

os.environ["OLLAMA_HOST"] = OLLAMA_HOST
os.environ["OLLAMA_API_KEY"] = OLLAMA_API_KEY

# ─────────────────────────────────────────────────────────────
# 1. Modelo — instância declarativa (o mesmo do 1º semestre, via LangChain)
# ─────────────────────────────────────────────────────────────
llm = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_HOST,
    temperature=0.7,
    num_predict=512,          # equivalente a max_tokens
)

# ─────────────────────────────────────────────────────────────
# 2. Template — ChatPromptTemplate com roles e variáveis
# ─────────────────────────────────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é {persona}. Responda sobre {especialidade}."),
    ("human", "{pergunta}"),
])

# ─────────────────────────────────────────────────────────────
# 3. Chains LCEL — o operador | funciona como um pipe
# ─────────────────────────────────────────────────────────────
chain_texto = prompt | llm | StrOutputParser()    # → str
chain_json = prompt | llm | JsonOutputParser()     # → dict (prompt pede JSON)


def demo_templates() -> None:
    """Demo de templates com variáveis dinâmicas."""
    # TODO: Use chain_texto.invoke() com 3 sets diferentes de variáveis
    # TODO: Imprima as respostas e note a variação
    pass


def main() -> None:
    print(f"Ollama Cloud | modelo: {OLLAMA_MODEL}\n")
    # TODO: Chamar demo_templates()


if __name__ == "__main__":
    main()