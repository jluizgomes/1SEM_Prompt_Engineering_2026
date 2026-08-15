"""
Aula 06 — Chain of Thought (CoT): Raciocínio Passo a Passo
FIAP · Prompt Engineering and AI · 1º Semestre 2026 · Prof. Jorge Luiz Gomes

Demonstra CoT zero-shot e few-shot, forçando o LLM a explicar
seu raciocínio antes de dar a resposta final.

Modelo padrão: qwen3.5:0.8b ( leve e rápido para testes )
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


def chamar_llm(prompt: str, system: str = "") -> str:
    """Função auxiliar para chamar o LLM via Ollama."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    resp = client.chat(model=OLLAMA_MODEL, messages=messages)
    return resp["message"]["content"]


# ── Problema matemático para testar CoT ────────────────────────────
# Problemas que exigem raciocínio passo a passo

PROBLEMAS = [
    "Se Maria tem 12 maçãs e deu 3 para cada uma de suas 4 amigas, quantas maçãs sobraram?",
    "Um trem parte de São Paulo às 8h viajando a 80 km/h. Outro parte do Rio às 9h viajando a 120 km/h. Quantas horas depois do meio-dia eles se encontram se a distância é 430 km?",
]


# ── Variante 1: Zero-shot COM CoT ──────────────────────────────────
# Pede ao modelo que pense passo a passo, sem exemplos

print("=" * 60)
print("CHAIN OF THOUGHT — ZERO-SHOT vs FEW-SHOT")
print(f"Modelo: {OLLAMA_MODEL}")
print("=" * 60)

for i, problema in enumerate(PROBLEMAS, 1):
    print(f"\n{'━' * 60}")
    print(f"PROBLEMA {i}: {problema}")
    print(f"{'━' * 60}")

    # Zero-shot CoT: instrução + "Pense passo a passo"
    prompt_zero = f"""Resolva o problema abaixo. Pense passo a passo, mostrando todo o raciocínio antes de dar a resposta final.

Problema: {problema}

Resolução passo a passo:"""

    print("\n[Zero-Shot CoT]")
    print("Prompt: \"Pense passo a passo\" (sem exemplos)\n")
    resposta_zero = chamar_llm(prompt_zero)
    print(f"Resposta:\n{resposta_zero}")

    # Few-shot CoT: mostra um exemplo de raciocínio estruturado
    prompt_few = f"""Resolva o problema abaixo. Pense passo a passo, mostrando todo o raciocínio.

Exemplo de resolução:
Problema: "João comprou 5 camisas a R$ 40 cada. Quanto pagou?"
Passo 1: Identificar as quantidades → 5 camisas, R$ 40 cada
Passo 2: Operação → 5 × 40 = 200
Resposta: João pagou R$ 200.

Agora resolva:
Problema: {problema}

Resolução passo a passo:"""

    print(f"\n[Few-Shot CoT]")
    print("Prompt: exemplo de raciocínio estruturado + problema\n")
    resposta_few = chamar_llm(prompt_few)
    print(f"Resposta:\n{resposta_few}")

print(f"\n{'=' * 60}")
print("ANÁLISE:")
print("  • Zero-Shot CoT: o modelo raciocina sozinho quando instruído")
print("  • Few-Shot CoT: o exemplo guia o formato e a profundidade do raciocínio")
print("  • CoT melhora acurácia em problemas de lógica e matemática")
print("  • trade-off: respostas mais longas = mais tokens = mais custo")
print("=" * 60)
