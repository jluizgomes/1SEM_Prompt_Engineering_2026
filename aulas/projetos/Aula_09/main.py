"""
Aula 09 — Conversação com Histórico: Chat Interativo com Memória
FIAP · Prompt Engineering and AI · 1º Semestre 2026 · Prof. Jorge Luiz Gomes

Demonstra:
- while True (loop infinito controlado)
- Lista de dicionários como histórico de conversa
- .append() para adicionar mensagens
- Truncação de histórico para não estourar a janela de contexto
- Comando especial "sair" para encerrar

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
    """Chama o LLM com histórico de mensagens."""
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


# ── Configuração do chat ───────────────────────────────────────────

SYSTEM_PROMPT = (
    "Você é um assistente educado e prestativo. "
    "Responda de forma clara e concisa."
)

MAX_HISTORICO = 10  # Máximo de pares pergunta/resposta no histórico


# ── Loop principal do chat ─────────────────────────────────────────

def iniciar_chat():
    """Loop infinito de conversa com histórico."""
    print("=" * 60)
    print("CHAT COM HISTÓRICO")
    print(f"Modelo: {OLLAMA_MODEL}")
    print(f"Digite 'sair' para encerrar")
    print("=" * 60)

    # Lista de dicionários — armazena todo o histórico
    historico = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        # Lê a entrada do usuário
        entrada = input("\nVocê: ").strip()

        # Comando especial para sair
        if entrada.lower() in ["sair", "exit", "quit", "q"]:
            print("\nAté logo! Conversa encerrada.")
            break

        # Ignora entrada vazia
        if not entrada:
            continue

        # Adiciona a mensagem do usuário ao histórico
        historico.append({"role": "user", "content": entrada})

        # Truncação: mantém apenas as últimas N mensagens (além do system)
        # Isso evita estourar a janela de contexto do modelo
        if len(historico) > MAX_HISTORICO + 1:  # +1 por causa do system prompt
            historico = [historico[0]] + historico[-(MAX_HISTORICO):]

        try:
            # Chama o LLM com todo o histórico
            resp = client.chat(
                model=OLLAMA_MODEL,
                messages=historico,
                options={"temperature": 0.7, "num_predict": 300}
            )
            resposta = resp["message"]["content"]
        except Exception as e:
            print(f"\nErro ao chamar o LLM: {e}")
            # Remove a última mensagem do usuário em caso de erro
            historico.pop()
            continue

        # Adiciona a resposta do assistente ao histórico
        historico.append({"role": "assistant", "content": resposta})

        # Exibe a resposta
        print(f"\nAssistente: {resposta}")

        # Mostra tamanho do histórico (para fins didáticos)
        print(f"  [Histórico: {len(historico)} mensagens]")


# ── Ponto de entrada ───────────────────────────────────────────────

if __name__ == "__main__":
    iniciar_chat()
