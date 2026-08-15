"""
Aula 04 — Anatomia do Prompt: Primeiro Código Python
Demonstra os 4 componentes de um prompt: contexto, instrução, entrada e formato.

Uso:
    python main.py
"""

import os
import ollama
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Configuração da API
client = ollama.Client(
    host=os.getenv("OLLAMA_HOST", "https://ollama.com"),
    headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"}
)
MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:0.8b")


def chamar_llm(prompt, system=""):
    """Chama o modelo LLM com um prompt opcional de sistema."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = client.chat(model=MODEL, messages=messages)
    return resp["message"]["content"]


# =============================================================================
# PARTE 1: Os 4 Componentes de um Prompt
# =============================================================================

def demonstrar_componentes():
    """Demonstra como montar prompts usando contexto, instrução, entrada e formato."""

    print("\n📌 OS 4 COMPONENTES DE UM PROMPT")
    print("-" * 50)

    # Prompt sem componentes (ruim)
    prompt_ruim = "Traduza"
    print(f"\n  ❌ Prompt ruim: \"{prompt_ruim}\"")
    print(f"     Problema: Falta contexto, instrução, entrada e formato!")

    # Prompt com todos os componentes (bom)
    contexto = "Você é um tradutor profissional de inglês para português."
    instrucao = "Traduza o texto abaixo mantendo o tom formal."
    entrada = "The weather is beautiful today."
    formato = "Responda apenas com a tradução, sem explicações."

    prompt_bom = f"""Contexto: {contexto}

Instrução: {instrucao}

Entrada: {entrada}

Formato: {formato}"""

    print(f"\n  ✅ Prompt bom:")
    print(f"  {prompt_bom}")

    # Chama o LLM
    print(f"\n  🤖 Resposta do modelo:")
    resposta = chamar_llm(prompt_bom)
    print(f"  → {resposta}")


# =============================================================================
# PARTE 2: Variáveis e F-strings
# =============================================================================

def demonstrar_variaveis():
    """Demonstra como usar variáveis e f-strings em prompts."""

    print("\n\n📌 VARIÁVEIS E F-STRINGS")
    print("-" * 50)

    # Exemplo 1: Variável simples
    linguagem = "Python"
    prompt1 = f"Explique o que é {linguagem} em uma frase."
    print(f"\n  Prompt 1: {prompt1}")
    resposta1 = chamar_llm(prompt1)
    print(f"  Resposta: {resposta1}")

    # Exemplo 2: Múltiplas variáveis
    contexto = "Estudante de engenharia da computação"
    duvida = "Qual a diferença entre PIL e OpenCV?"
    prompt2 = f"""Você é um tutor de programação.

Contexto: {contexto}
Pergunta: {duvida}

Responda de forma simples e didática."""

    print(f"\n  Prompt 2:")
    print(f"  {prompt2}")
    resposta2 = chamar_llm(prompt2)
    print(f"  Resposta: {resposta2}")


# =============================================================================
# PARTE 3: Dicionários e Listas
# =============================================================================

def demonstrar_dicionarios():
    """Demonstra como usar dicionários para organizar prompts."""

    print("\n\n📌 DICIONÁRIOS E LISTAS")
    print("-" * 50)

    # Dicionário de personas
    personas = {
        "professor": "Você é um professor universitário de Ciência da Computação.",
        "pirata": "Você é um pirata do século XVII que fala sobre tecnologia.",
        "chef": "Você é um chef de cozinha que explica programação usando culinária.",
    }

    pergunta = "O que é uma variável?"

    for nome, persona in personas.items():
        print(f"\n  🎭 Persona: {nome}")
        prompt = f"{persona}\n\nPergunta: {pergunta}"
        resposta = chamar_llm(prompt)
        print(f"  Resposta: {resposta[:100]}...")

    # Lista de exemplos
    exemplos = [
        {"contexto": "estudante", "pergunta": "O que é loop?"},
        {"contexto": "desenvolvedor", "pergunta": "O que é API?"},
    ]

    print(f"\n\n📋 Lista de exemplos:")
    for i, ex in enumerate(exemplos, 1):
        prompt = f"Você é um tutor para {ex['contexto']}s.\n\nPergunta: {ex['pergunta']}"
        resposta = chamar_llm(prompt)
        print(f"\n  {i}. [{ex['contexto']}] {ex['pergunta']}")
        print(f"     → {resposta[:80]}...")


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  AULA 04 — ANATOMIA DO PROMPT: PRIMEIRO CÓDIGO")
    print("=" * 60)

    print("\n💡 Conceitos-chave desta aula:")
    print("  • Contexto: Quem é o modelo nesta tarefa?")
    print("  • Instrução: O que o modelo deve fazer?")
    print("  • Entrada: Qual é o dado/processamento necessário?")
    print("  • Formatado: Como o resultado deve ser apresentado?")

    demonstrar_componentes()
    demonstrar_variaveis()
    demonstrar_dicionarios()

    print("\n\n" + "=" * 60)
    print("  ✅ AULA 04 COMPLETA!")
    print("=" * 60)
