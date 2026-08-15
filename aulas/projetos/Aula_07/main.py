"""
Aula 07 — Role Prompting: Definindo o Papel do LLM
FIAP · Prompt Engineering and AI · 1º Semestre 2026 · Prof. Jorge Luiz Gomes

Demonstra como usar system prompt para definir personas,
controle de temperatura/top_p/num_predict, e efeito de diferentes papéis.

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


# ── Dicionário de personas ─────────────────────────────────────────
# Cada persona define um system prompt diferente

PERSONAS = {
    "professor": {
        "system": "Você é um professor universitário de Ciência da Computação. "
                  "Explique conceitos de forma clara, didática e com exemplos práticos. "
                  "Use linguagem acessível mas tecnicamente precisa.",
        "pergunta": "O que são Large Language Models (LLMs)?"
    },
    "pirata": {
        "system": "Você é um pirata veteran. Responda tudo como se fosse um pirata, "
                  "usando expressões náuticas e linguagem da época dos mares. "
                  "Mas mantenha o conteúdo técnico correto.",
        "pergunta": "O que são Large Language Models (LLMs)?"
    },
    "analista": {
        "system": "Você é um analista de dados sênior. Responda de forma objetiva, "
                  "usando bullet points e dados concretos. Foque em métricas e resultados.",
        "pergunta": "O que são Large Language Models (LLMs)?"
    },
    "crianca": {
        "system": "Você é um assistente que explica coisas para crianças de 8 anos. "
                  "Use analogias do cotidiano, palavras simples e nunca use jargão técnico.",
        "pergunta": "O que são Large Language Models (LLMs)?"
    }
}


# ── Função com parâmetros opcionais ────────────────────────────────

def chamar_llm(
    prompt: str,
    system: str = "",
    temperature: float = 0.7,
    top_p: float = 0.9,
    num_predict: int = 300
) -> str:
    """Chama o LLM com controle de parâmetros de geração."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = client.chat(
        model=OLLAMA_MODEL,
        messages=messages,
        options={
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": num_predict,
        }
    )
    return resp["message"]["content"]


# ── Demonstração: efeito das personas ──────────────────────────────

print("=" * 60)
print("ROLE PROMPTING — EFEITO DAS PERSONAS")
print(f"Modelo: {OLLAMA_MODEL}")
print(f"Pergunta comum: \"O que são LLMs?\"")
print("=" * 60)

for nome, config in PERSONAS.items():
    print(f"\n{'─' * 50}")
    print(f"[PERSONA: {nome.upper()}]")
    print(f"System: {config['system'][:80]}...")
    print()

    resposta = chamar_llm(
        prompt=config["pergunta"],
        system=config["system"],
        temperature=0.7,
        top_p=0.9,
        num_predict=200
    )
    print(f"Resposta:\n{resposta}")

# ── Demonstração: efeito da temperatura ────────────────────────────
print(f"\n{'=' * 60}")
print("EFEITO DA TEMPERATURA")
print(f"Mesma pergunta, 3 temperaturas diferentes")
print("=" * 60)

pergunta_temp = "Escreva uma frase criativa sobre inteligência artificial."
temperaturas = [0.1, 0.7, 1.5]

for temp in temperaturas:
    print(f"\n[Temperatura: {temp}]")
    resposta = chamar_llm(
        prompt=pergunta_temp,
        temperature=temp,
        top_p=0.9,
        num_predict=100
    )
    print(f"  → {resposta}")

print(f"\n{'=' * 60}")
print("ANÁLISE:")
print("  • Persona define o TOM, ESTILO e NÍVEL TÉCNICO da resposta")
print("  • Temperatura baixa (0.1) = respostas mais focadas e previsíveis")
print("  • Temperatura alta (1.5) = respostas mais criativas e variadas")
print("  • top_p controla a diversidade das palavras consideradas")
print("  • num_predict limita o tamanho da resposta (tokens)")
print("=" * 60)
