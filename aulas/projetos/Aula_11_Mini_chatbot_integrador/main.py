"""
FIAP · Prompt Engineering & AI — 1º Semestre 2026
Aula 11 — Mini chatbot integrador

Projeto local: construção de mini chatbot integrador que substituem o
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
        "OLLAMAAPIKEY não encontrada. Copie .env.example para .env e preencha a chave."
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


def demo_chatbot() -> None:
    """Demo de mini chatbot interativo."""
    print("=== Mini Chatbot ===")
    print("Olá! Eu sou um mini chatbot. Digite 'sair' para encerrar.")
    print()

    while True:
        usuario = input("Você: ")
        if usuario.lower() in ["sair", "quit", "exit"]:
            print("Até mais!")
            break

        resposta = chain.invoke({
            "persona": "um assistente útil",
            "especialidade": " conversa geral",
            "pergunta": usuario,
        })
        print(f"Chatbot: {resposta}")
        print()


def main() -> None:
    print(f"Ollama Cloud | modelo: {OLLAMA_MODEL}\n")
    demo_chatbot()


if __name__ == "__main__":
    main()