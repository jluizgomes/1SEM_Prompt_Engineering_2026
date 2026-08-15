"""
Aula 01 — O que é IA: Da ficção à realidade
Projeto demonstrativo: Classificador de texto por palavras-chave

Demonstra os conceitos de:
- IA (Inteligência Artificial) — regras manuais
- ML (Machine Learning) — padrões aprendidos dos dados
- Deep Learning — redes neurais complexas
"""

# =============================================================================
# PARTE 1: IA Clássica — Regras manuais (hardcoded)
# =============================================================================

def classificar_ia_classica(texto):
    """
    Classifica texto usando regras manuais definidas por um humano.
    Isso é IA 'clássica' — o programador define TODAS as regras.
    """
    texto_lower = texto.lower()

    # Regras definidas manualmente
    if any(palavra in texto_lower for palavra in ["preço", "valor", "quanto custa", "comprar"]):
        return "💰 Comercial"
    elif any(palavra in texto_lower for palavra in ["erro", "bug", "não funciona", "problema"]):
        return "🔧 Suporte Técnico"
    elif any(palavra in texto_lower for palavra in ["horário", "quando", "data", "agenda"]):
        return "📅 Agendamento"
    elif any(palavra in texto_lower for palavra in ["obrigado", "ajuda", "por favor"]):
        return "🤝 Atendimento"
    else:
        return "❓ Não classificado"


# =============================================================================
# PARTE 2: Simulando ML — Aprendizado a partir de exemplos
# =============================================================================

# Base de dados de treino (simulada)
TREINO = {
    "comercial": ["quanto custa o plano?", "qual o valor?", "quero comprar"],
    "suporte": ["meu app quebrou", "está dando erro", "não funciona"],
    "agendamento": ["que horas abre?", "qual o horário?", "preciso marcar"],
}

def calcular_similaridade(texto, exemplos):
    """
    Calcula quantas palavras do texto aparecem nos exemplos.
    Em ML real, isso seria um vetor de embeddings + similaridade coseno.
    """
    palavras_texto = set(texto.lower().split())
    palavras_exemplos = " ".join(exemplos).lower().split()
    intersecao = palavras_texto.intersection(set(palavras_exemplos))
    return len(intersecao) / max(len(palavras_texto), 1)


def classificar_ml_simulado(texto):
    """
    Classifica usando similaridade com exemplos de treino.
    Simula como um classificador de ML funcionaria.
    """
    melhor_categoria = "❓ Não classificado"
    melhor_score = 0.0

    for categoria, exemplos in TREINO.items():
        score = calcular_similaridade(texto, exemplos)
        if score > melhor_score:
            melhor_score = score
            melhor_categoria = categoria.capitalize()

    return f"{melhor_categoria} (confiança: {melhor_score:.0%})"


# =============================================================================
# PARTE 3: Deep Learning — Conceito (sem implementação)
# =============================================================================

def explicar_deep_learning():
    """
    Deep Learning usaria redes neurais com múltiplas camadas
    para aprender padrões complexos automaticamente.

    Em vez de:
    - Regras manuais (IA clássica)
    - Exemplos rotulados (ML supervisionado)

    Deep Learning:
    - Aprende representações hierárquicas dos dados
    - Camada 1: palavras → camada 2: frases → camada 3: significado
    - Exige muitos dados e computação (GPUs)
    """
    return """
    ╔══════════════════════════════════════════════════════╗
    ║          EVOLUÇÃO DA INTELIGÊNCIA ARTIFICIAL        ║
    ╠══════════════════════════════════════════════════════╣
    ║                                                      ║
    ║  IA Clássica    → Regras manuais编写adas por humanos   ║
    ║       ↓                                            ║
    ║  Machine Learning → Aprende padrões de exemplos     ║
    ║       ↓                                            ║
    ║  Deep Learning  → Redes neurais multi-camada        ║
    ║       ↓                                            ║
    ║  IA Generativa  → Cria conteúdo novo (ChatGPT)     ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  AULA 01 — O QUE É IA: DA FICÇÃO À REALIDADE")
    print("=" * 60)

    # Textos de teste
    testes = [
        "Quanto custa o plano premium?",
        "Meu aplicativo está com erro, não funciona",
        "Que horas vocês abrem amanhã?",
        "Muito obrigado pela ajuda!",
        "A inteligência artificial vai mudar o mundo",
    ]

    print("\n📋 TESTE 1: IA Clássica (Regras Manuais)")
    print("-" * 50)
    for texto in testes:
        resultado = classificar_ia_classica(texto)
        print(f"  \"{texto}\"")
        print(f"  → {resultado}\n")

    print("\n📋 TESTE 2: ML Simulado (Similaridade)")
    print("-" * 50)
    for texto in testes:
        resultado = classificar_ml_simulado(texto)
        print(f"  \"{texto}\"")
        print(f"  → {resultado}\n")

    print(explicar_deep_learning())

    print("💡 CONCEITO-CHAVE:")
    print("  IA Generativa (como ChatGPT) é a evolução mais recente.")
    print("  Ela NÃO classifica — ela CRIA texto novo baseado em padrões")
    print("  aprendidos com bilhões de exemplos de texto da internet.\n")
