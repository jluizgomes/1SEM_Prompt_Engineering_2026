"""
Aula 10 — montar_prompt(): Templates Reutilizáveis com F-Strings
FIAP · Prompt Engineering and AI · 1º Semestre 2026 · Prof. Jorge Luiz Gomes

Demonstra:
- Definição de funções com múltiplos parâmetros
- F-strings para interpolação de variáveis
- **dict (unpacking de dicionário) em chamadas de função
- Templates parametrizados reutilizáveis

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


def chamar_llm(
    prompt: str,
    system: str = "",
    temperature: float = 0.7,
    num_predict: int = 300
) -> str:
    """Chama o LLM."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    resp = client.chat(
        model=OLLAMA_MODEL,
        messages=messages,
        options={"temperature": temperature, "num_predict": num_predict}
    )
    return resp["message"]["content"]


# ── Templates de prompts com f-strings ─────────────────────────────

def montar_prompt_resumo(texto: str, idioma: str = "português") -> str:
    """Monta prompt para resumir um texto."""
    return f"""Resuma o texto abaixo em no máximo 3 frases claras e objetivas.

Idioma do resumo: {idioma}

Texto:
{texto}

Resumo:"""


def montar_prompt_classificar(texto: str, categorias: list) -> str:
    """Monta prompt para classificar texto em categorias."""
    cats = ", ".join(categorias)
    return f"""Classifique o texto abaixo em uma das categorias: [{cats}]

Texto: {texto}

Categoria:"""


def montar_prompt_traduzir(texto: str, idioma_origem: str, idioma_destino: str) -> str:
    """Monta prompt para traduzir texto."""
    return f"""Traduza o texto abaixo de {idioma_origem} para {idioma_destino}.
Mantenha o tom e o estilo original.

Texto original:
{texto}

Tradução:"""


def montar_prompt_codigo(linguagem: str, descricao: str, nivel: str = "intermediário") -> str:
    """Monta prompt para gerar código."""
    return f"""Escreva uma função em {linguagem} que {descricao}.

Nível de complexidade: {nivel}
Inclua comentários explicativos no código.
Use boas práticas de programação.

Código:"""


def montar_prompt_analise(dados: str, tipo_analise: str) -> str:
    """Monta prompt para analisar dados."""
    return f"""Analise os dados abaixo e forneça uma análise {tipo_analise}.

Dados:
{dados}

Forneça:
1. Resumo executivo
2. Insights principais
3. Possíveis ações recomendadas

Análise:"""


# ── Demonstração de **dict unpacking ───────────────────────────────

def montar_prompt_generico(**kwargs) -> str:
    """
    Template genérico que aceita qualquer combinação de parâmetros.
    Usa **kwargs para receber um dicionário de variáveis.
    """
    # Monta o prompt dinamicamente com base nos kwargs fornecidos
    partes = []
    if "tarefa" in kwargs:
        partes.append(f"Tarefa: {kwargs['tarefa']}")
    if "contexto" in kwargs:
        partes.append(f"Contexto: {kwargs['contexto']}")
    if "exemplo" in kwargs:
        partes.append(f"Exemplo: {kwargs['exemplo']}")
    if "formato" in kwargs:
        partes.append(f"Formato de saída: {kwargs['formato']}")
    if "restricoes" in kwargs:
        partes.append(f"Restrições: {kwargs['restricoes']}")

    return "\n".join(partes) + "\n\nResposta:"


# ── Demonstração: usando os templates ──────────────────────────────

print("=" * 60)
print("montar_prompt() — TEMPLATES REUTILIZÁVEIS")
print(f"Modelo: {OLLAMA_MODEL}")
print("=" * 60)

# 1. Resumo
print("\n[1] TEMPLATE DE RESUMO")
texto_exemplo = (
    "A inteligência artificial generativa tem transformado indústrias inteiras. "
    "Desde a criação de conteúdo até a automação de processos complexos, "
    "LLMs como GPT e Qwen estão sendo integrados em ferramentas do dia a dia. "
    "No entanto, desafios como alucinações, vieses e custos de computação "
    "continuam sendo barreiras para adoção em larga escala."
)
prompt_resumo = montar_prompt_resumo(texto_exemplo, idioma="português")
print(f"Prompt montado:\n{prompt_resumo}")
resposta = chamar_llm(prompt_resumo, num_predict=150)
print(f"Resposta: {resposta}")

# 2. Classificação
print(f"\n{'─' * 60}")
print("[2] TEMPLATE DE CLASSIFICAÇÃO")
prompt_class = montar_prompt_classificar(
    "Estou muito feliz com o produto, superou minhas expectativas!",
    categorias=["positivo", "negativo", "neutro"]
)
print(f"Prompt montado:\n{prompt_class}")
resposta = chamar_llm(prompt_class, num_predict=50)
print(f"Resposta: {resposta}")

# 3. Geração de código
print(f"\n{'─' * 60}")
print("[3] TEMPLATE DE CÓDIGO")
prompt_codigo = montar_prompt_codigo(
    linguagem="Python",
    descricao="calcule a média de uma lista de números",
    nivel="iniciante"
)
print(f"Prompt montado:\n{prompt_codigo}")
resposta = chamar_llm(prompt_codigo, num_predict=200)
print(f"Resposta:\n{resposta}")

# 4. **dict unpacking
print(f"\n{'─' * 60}")
print("[4] **dict UNPACKING")
config = {
    "tarefa": "Explique o conceito de embedding",
    "contexto": "Para estudantes de graduação de computação",
    "exemplo": "Similar a como palavras próximas em um dicionário estão juntas",
    "formato": "Parágrafos curtos com analogia do cotidiano",
    "restricoes": "Máximo 100 palavras"
}
prompt_generico = montar_prompt_generico(**config)
print(f"Prompt montado com **dict:\n{prompt_generico}")
resposta = chamar_llm(prompt_generico, num_predict=150)
print(f"Resposta: {resposta}")

print(f"\n{'=' * 60}")
print("CONCEITOS DESENVOLVIDOS:")
print("  • def com múltiplos parâmetros e valores padrão")
print("  • F-strings para interpolação de variáveis em strings")
print("  • **dict unpacking — passar dicionário como kwargs")
print("  • Templates reutilizáveis — mesma função, diferentes entradas")
print("  • Separação entre montar_prompt() e chamar_llm()")
print("=" * 60)
