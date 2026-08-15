"""
FIAP · Prompt Engineering & AI — 1º Semestre 2026
Aula 12 — Segurança em LLMs: Injeção, Jailbreak, Alucinações e Guardrails

Esqueleto para alunos — complete os TODOS abaixo.
Projeto local: demonstrações de ataques e defesas em modelos de linguagem
via LangChain + Ollama.

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
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:0.8b")

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
# 2. Template base — usado nas demonstrações
# ─────────────────────────────────────────────────────────────
prompt_base = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de IA útil e inofensivo."),
    ("human", "{input}"),
])

# ─────────────────────────────────────────────────────────────
# 3. Chains LCEL — o operador | funciona como um pipe
# ─────────────────────────────────────────────────────────────
chain_texto = prompt_base | llm | StrOutputParser()    # → str
chain_json = prompt_base | llm | JsonOutputParser()     # → dict (se prompt pedir JSON)


def demo_injecao_prompt() -> None:
    # TODO: Implement demo de injection de prompt
    # TODO: Tente fazer o modelo ignorar suas instruções de segurança
    pass


def demo_jailbreak() -> None:
    # TODO: Implement demo de jailbreak clássico
    # TODO: Tente bypassar as diretrizes de segurança do modelo
    pass


def demo_alucinacao() -> None:
    # TODO: Implement demo de alucinação
    # TODO: Verifique se o modelo está inventando fatos com confiança
    pass


def demo_guardrails_simples() -> None:
    # TODO: Implement demo de guardrails básico
    # TODO: Filtre saídas com palavras-chave proibidas
    pass


def main() -> None:
    print(f"Ollama Cloud | modelo: {OLLAMA_MODEL}\n")
    # TODO: Chamar todas as funções demo()


if __name__ == "__main__":
    main()