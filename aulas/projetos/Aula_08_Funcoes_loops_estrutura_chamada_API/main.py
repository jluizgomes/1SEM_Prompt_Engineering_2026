"""
FIAP · Prompt Engineering & AI — 1º Semestre 2026
Aula 08 — Funções e loops

Projeto local: exemplos de funções Python e loops que substituem o
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
from langchain_core.output_parsers import StrOutputParser

# ─────────────────────────────────────────────────────────────
# Configuração via .env (Ollama Cloud por padrão; veja .env.example)
# ─────────────────────────────────────────────────────────────
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "https://ollama.com")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:0.8b")

if not OLLAMA_API_KEY:
    raise RuntimeError(
        "OLLAMA_APIKEY não encontrada. Copie .env.example para .env e preencha a chave."
    )

os.environ["OLLAMA_HOST"] = OLLAMA_HOST
os.environ["OLLAMA_API_KEY"] = OLLAMA_API_KEY

# ─────────────────────────────────────────────────────────────
# 1. Modelo — instância declarativa via LangChain / Ollama
# ─────────────────────────────────────────────────────────────
llm = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_HOST,
    temperature=0.7,
    num_predict=512,
)

# ─────────────────────────────────────────────────────────────
# 2. Template — ChatPromptTemplate com roles e variáveis
# ─────────────────────────────────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é {persona}. Responda sobre {especialidade}."),
    ("human", "{pergunta}"),
])

# ─────────────────────────────────────────────────────────────
# 3. Chain LCEL — o operador | funciona como um pipe
# ─────────────────────────────────────────────────────────────
chain = prompt | llm | StrOutputParser()


def demo_functions() -> None:
    """Demo de funções Python com chamadas a LLM."""
    # Função que encapsula a chain
    def perguntar(pergunta: str) -> str:
        return chain.invoke({
            "persona": "um assistente útil",
            "especialidade": "various",
            "pergunta": pergunta,
        })

    r1 = perguntar("Qual a diferença entre listas e tuplas em Python?")
    print("== Lista vs Tupla ===")
    print(r1)

    r2 = perguntar("Como faço um bolo de cenoura?")
    print("== Bolo de Cenoura ===")
    print(r2)


def main() -> None:
    print(f"Ollama Cloud | modelo: {OLLAMA_MODEL}\n")
    demo_functions()


if __name__ == "__main__":
    main()