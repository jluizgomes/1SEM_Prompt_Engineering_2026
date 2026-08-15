"""
Aula 02 — Como um LLM pensa: tokens, contexto, temperatura
Projeto demonstrativo: Contador de tokens e conceitos

Demonstra os conceitos de:
- Tokens — unidades de texto que o modelo processa
- Context Window — limite de tokens que o modelo "enxerga"
- Temperatura — controle de criatividade vs. previsibilidade
"""

import re


# =============================================================================
# PARTE 1: O que são Tokens?
# =============================================================================

def estimar_tokens(texto):
    """
    Estima o número de tokens em um texto.

    LLMs não trabalham com palavras inteiras — trabalham com TOKENS.
    Tokens são pedaços de texto que o modelo processa.

    Exemplos:
    - "Olá" → 1 token
    - "inteligência" → 3 tokens (inte|li|gên)
    - "ChatGPT" → 2 tokens (Chat|GPT)
    - "FIAP" → 1 token (se está no vocabulário)

    Em português, 1 token ≈ 0.5-0.7 palavras (mais que em inglês!)
    """
    # Estimativa simples (o tokenizer real do modelo é mais complexo)
    # Divide por espaços e pontuação
    palavras = re.findall(r'\b\w+\b|[^\w\s]', texto)
    return len(palavras)


def contar_caracteres(texto):
    """Conta caracteres totais e sem espaços."""
    return len(texto), len(texto.replace(" ", ""))


def analisar_tokens(texto):
    """Análise completa de tokens de um texto."""
    n_tokens = estimar_tokens(texto)
    n_chars, n_chars_sem_espaco = contar_caracteres(texto)
    palavras = texto.split()
    n_palavras = len(palavras)

    return {
        "texto": texto[:50] + "..." if len(texto) > 50 else texto,
        "tokens_estimados": n_tokens,
        "palavras": n_palavras,
        "caracteres": n_chars,
        "caracteres_sem_espaco": n_chars_sem_espaco,
        "ratio_tokens_por_palavra": n_tokens / max(n_palavras, 1),
    }


# =============================================================================
# PARTE 2: Context Window — Janela de Contexto
# =============================================================================

def demonstrar_context_window():
    """
    Context Window é o limite de tokens que o modelo pode processar.
    Tudo o que está DENTRO da janela é "enxergado" pelo modelo.
    Tudo o que está FORA é ignorado.

    Exemplos de tamanhos:
    - GPT-3.5: 4.096 tokens (~3.000 palavras em PT)
    - GPT-4: 8.192 ou 128.000 tokens
    - Claude 3: 200.000 tokens
    - Modelos locais: 2.048 a 32.768 tokens
    """
    JANELA_MAXIMA = 2048  # Simulando um modelo pequeno

    # Contexto crescente
    contexto = "Você é um assistente útil."

    cenarios = [
        ("Prompt curto", "Qual é a capital do Brasil?"),
        ("Prompt médio", "Explique o que é machine learning em 3 parágrafos, com exemplos práticos."),
        ("Prompt longo", "Escreva um artigo completo sobre inteligência artificial, cobrindo história, aplicações, desafios éticos, tendências futuras, impacto no mercado de trabalho, regulamentação, e comparação entre abordagens."),
    ]

    for nome, prompt in cenarios:
        total = estimar_tokens(contexto) + estimar_tokens(prompt)
        porcentagem = (total / JANELA_MAXIMA) * 100
        status = "✅" if porcentagem < 80 else "⚠️" if porcentagem < 100 else "❌"

        print(f"\n  {status} {nome}:")
        print(f"     Contexto: {estimar_tokens(contexto)} tokens")
        print(f"     Prompt: {estimar_tokens(prompt)} tokens")
        print(f"     Total: {total} / {JANELA_MAXIMA} tokens ({porcentagem:.0f}%)")


# =============================================================================
# PARTE 3: Temperatura — Criatividade vs. Previsibilidade
# =============================================================================

def simular_temperatura():
    """
    Temperatura controla a "aleatoriedade" das respostas.

    Temperatura baixa (0.0 - 0.3):
    → Respostas mais previsíveis e focadas
    → Bom para: código, fatos, análise

    Temperatura média (0.4 - 0.7):
    → Equilíbrio entre criatividade e coerência
    → Bom para: escrita, conversas

    Temperatura alta (0.8 - 1.0):
    → Respostas mais criativas e surpreendentes
    → Bom para: brainstorming, poesia, criatividade
    """
    print("\n  Exemplo: 'Escreva uma frase sobre_programação'")
    print()

    respostas = {
        0.0: "Programação é a arte de instruir um computador.",
        0.3: "Programação transforma lógica em soluções digitais.",
        0.7: "Programar é como construir castelos de código — cada linha sustenta o sonho.",
        1.0: "Programação: onde vírgulas são filosofia e bug são acasos felizes.",
    }

    for temp, resposta in respostas.items():
        barra = "█" * int(temp * 20) + "░" * (20 - int(temp * 20))
        print(f"  Temperatura {temp:.1f} [{barra}]")
        print(f"  → \"{resposta}\"\n")


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  AULA 02 — TOKENS, CONTEXTO E TEMPERATURA")
    print("=" * 60)

    # --- Tokens ---
    print("\n📌 PARTE 1: O que são Tokens?")
    print("-" * 50)

    textos_exemplo = [
        "Olá, mundo!",
        "A inteligência artificial está transformando o mundo.",
        "FIAP é uma das melhores faculdades de tecnologia do Brasil.",
        "O modelo GPT-4 processa até 128.000 tokens por vez.",
    ]

    for texto in textos_exemplo:
        info = analisar_tokens(texto)
        print(f"\n  Texto: \"{info['texto']}\"")
        print(f"  Tokens estimados: {info['tokens_estimados']}")
        print(f"  Palavras: {info['palavras']}")
        print(f"  Caracteres: {info['caracteres']}")

    print("\n\n💡 Regra prática em Português:")
    print("  1 token ≈ 0.6 palavras")
    print("  1.000 tokens ≈ 600 palavras ≈ 1 página")

    # --- Context Window ---
    print("\n\n📌 PARTE 2: Context Window")
    print("-" * 50)
    demonstrar_context_window()

    print("\n\n💡 Dica: Quando o contexto fica grande, o modelo 'esquece' o início.")

    # --- Temperatura ---
    print("\n\n📌 PARTE 3: Temperatura")
    print("-" * 50)
    simular_temperatura()

    print("💡 Resumo:")
    print("  • Tokens = unidades de texto que o modelo processa")
    print("  • Contexto = janela visível ao modelo (limitada!)")
    print("  • Temperatura = controle de criatividade (0=frio, 1=criativo)")
