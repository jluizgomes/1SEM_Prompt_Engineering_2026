"""
Aula 08 — Função chamar_llm(): Modularizando Chamadas ao LLM
FIAP · Prompt Engineering and AI · 1º Semestre 2026 · Prof. Jorge Luiz Gomes

Demonstra a construção de uma função reutilizável com:
- def (definição de função)
- Parâmetros com valores padrão (defaults)
- return (valor de retorno)
- enumerate (loop com contador)
- Tipo de retorno explícito (-> str)

Modelo padrão: qwen3.5:0.8b
"""
import os
import ollama
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "https://ollama.com")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "sua_chave_ollama_aqui")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:0.8b")

client = ollama.Client(
    host=OLLAMA_HOST,
    headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"}
)


# ── Função principal: chamar_llm() ─────────────────────────────────
# Esta é a versão final da função que os alunos devem entender

def chamar_llm(
    prompt: str,
    system: str = "",
    temperature: float = 0.7,
    top_p: float = 0.9,
    num_predict: int = 300,
    modelo: str = ""
) -> str:
    """
    Chama o modelo de linguagem via API Ollama.

    Parâmetros:
        prompt (str): Texto da pergunta ou instrução.
        system (str): Instrução de sistema (persona). Padrão: vazio.
        temperature (float): Criatividade (0.0 a 2.0). Padrão: 0.7.
        top_p (float): Diversidade de vocabulário (0.0 a 1.0). Padrão: 0.9.
        num_predict (int): Máximo de tokens na resposta. Padrão: 300.
        modelo (str): Nome do modelo. Padrão: usa variável de ambiente.

    Retorna:
        str: Texto gerado pelo modelo.
    """
    # Se nenhum modelo foi especificado, usa o padrão
    if not modelo:
        modelo = OLLAMA_MODEL

    # Monta a lista de mensagens
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    # Chama a API
    resp = client.chat(
        model=modelo,
        messages=messages,
        options={
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": num_predict,
        }
    )

    # Retorna apenas o texto da resposta
    return resp["message"]["content"]


# ── Demonstração 1: Uso básico com enumerate ───────────────────────

print("=" * 60)
print("FUNÇÃO chamar_llm() — USO BÁSICO")
print(f"Modelo: {OLLAMA_MODEL}")
print("=" * 60)

perguntas = [
    "O que é Python?",
    "Quais são os tipos de dados em Python?",
    "Como funciona uma lista em Python?",
]

# enumerate() retorna (índice, valor) — útil para numerar itens
for i, pergunta in enumerate(perguntas, start=1):
    print(f"\n[{i}] Pergunta: {pergunta}")
    resposta = chamar_llm(pergunta, num_predict=150)
    print(f"    Resposta: {resposta}\n")


# ── Demonstração 2: Uso com system prompt (persona) ────────────────

print(f"\n{'=' * 60}")
print("USO COM SYSTEM PROMPT (PERSONA)")
print("=" * 60)

system_expert = (
    "Você é um especialista em Python com 10 anos de experiência. "
    "Responda de forma técnica e concisa, com exemplos de código quando relevante."
)

for i, pergunta in enumerate(perguntas, start=1):
    print(f"\n[{i}] Pergunta: {pergunta}")
    resposta = chamar_llm(pergunta, system=system_expert, num_predict=200)
    print(f"    Resposta: {resposta}\n")


# ── Demonstração 3: Uso com modelo diferente ──────────────────────
# Nota: modelos diferentes podem não estar disponíveis

print(f"\n{'=' * 60}")
print("USO COM MODELO DIFERENTE")
print("=" * 60)

modelos_teste = ["qwen3.6:27b", "llama4:scout", "gemma4:9b"]

for modelo in modelos_teste:
    print(f"\n[Testando modelo: {modelo}]")
    try:
        resposta = chamar_llm(
            "Olá! Quem é você?",
            modelo=modelo,
            num_predict=50
        )
        print(f"  → {resposta}")
    except Exception as e:
        print(f"  → Modelo não disponível: {e}")


print(f"\n{'=' * 60}")
print("CONCEITOS DESENHOVOLVIDOS:")
print("  • def — definição de função com parâmetros")
print("  • Valores padrão (defaults) — temperature=0.7")
print("  • return — retorna valor para quem chamou")
print("  • enumerate() — loop com contador automático")
print("  • Tipo de retorno (-> str) — documentação da função")
print("  • if not modelo — condicional com valor padrão")
print("=" * 60)
