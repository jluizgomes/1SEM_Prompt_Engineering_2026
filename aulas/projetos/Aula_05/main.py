"""
Aula 05 — Zero, One e Few Shot: Comparando Estratégias de Prompting
FIAP · Prompt Engineering and AI · 1º Semestre 2026 · Prof. Jorge Luiz Gomes

Este script demonstra as 3 abordagens de prompting (zero-shot, one-shot, few-shot)
usando um loop com lista de tuplas para comparar os resultados lado a lado.

Modelo padrão: qwen3.5:0.8b ( leve e rápido para testes )
Para melhor qualidade, troque para: qwen3.6:27b ou llama4:scout
"""
import os
import ollama
from dotenv import load_dotenv

# ── Carrega variáveis do .env ─────────────────────────────────────
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "https://ollama.com")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "sua_chave_ollama_aqui")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:0.8b")

client = ollama.Client(
    host=OLLAMA_HOST,
    headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"}
)


def chamar_llm(prompt: str, system: str = "") -> str:
    """Função auxiliar para chamar o LLM via Ollama."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = client.chat(model=OLLAMA_MODEL, messages=messages)
    return resp["message"]["content"]


# ── Tarefa: Classificar sentimentos ────────────────────────────────
# O aluno define a tarefa e compara os 3 estilos de prompting

TAREFA = "Classifique o sentimento do texto como: POSITIVO, NEGATIVO ou NEUTRO."
TEXTO = "O restaurante estava lotado, mas o atendimento foi péssimo."


# ── Lista de tuplas: (nome, prompt) ────────────────────────────────
# Cada tupla é uma variante de prompting para a MESMA tarefa

variantes = [
    # Zero-shot: apenas a instrução, sem exemplos
    (
        "Zero-Shot",
        f"{TAREFA}\n\nTexto: {TEXTO}"
    ),

    # One-shot: instrução + 1 exemplo
    (
        "One-Shot",
        f"""{TAREFA}

Exemplo:
Texto: "Adorei o filme, recomendo!"
Sentimento: POSITIVO

Agora classifique:
Texto: {TEXTO}
Sentimento:"""
    ),

    # Few-shot: instrução + vários exemplos
    (
        "Few-Shot",
        f"""{TAREFA}

Exemplos:
Texto: "Adorei o filme, recomendo!"
Sentimento: POSITIVO

Texto: "O atendimento foi horrível, nunca mais volto."
Sentimento: NEGATIVO

Texto: "O produto é bom, mas o preço está ok."
Sentimento: NEUTRO

Agora classifique:
Texto: {TEXTO}
Sentimento:"""
    ),
]


# ── Loop de comparação ────────────────────────────────────────────
# Percorre cada variante e exibe o resultado

print("=" * 60)
print("COMPARAÇÃO: ZERO-SHOT vs ONE-SHOT vs FEW-SHOT")
print(f"Modelo: {OLLAMA_MODEL}")
print(f"Tarefa: Classificação de sentimento")
print(f"Texto: \"{TEXTO}\"")
print("=" * 60)

for nome, prompt in variantes:
    print(f"\n{'─' * 40}")
    print(f"[{nome}]")
    print(f"Prompt enviado:\n{prompt}\n")
    print("Resposta do LLM:")

    resposta = chamar_llm(prompt)
    print(f"  → {resposta}")

print("\n" + "=" * 60)
print("ANÁLISE:")
print("  • Zero-Shot: instrução direta, sem exemplos")
print("  • One-Shot: 1 exemplo guia o formato da resposta")
print("  • Few-Shot: múltiplos exemplos consolidam o padrão")
print("  • Resultados variam conforme o modelo e a complexidade da tarefa")
print("=" * 60)
