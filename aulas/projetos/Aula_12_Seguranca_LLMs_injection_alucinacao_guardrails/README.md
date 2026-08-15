# FIAP · Prompt Engineering & AI — 1º Semestre 2026
# Projeto local: Aula 12 - Segurança em LLMs

## Visão Geral

Projeto focado em segurança de modelos de linguagem, abordando:
- Prompt injection
- Jailbreak techniques  
- Guardrails
- Alucinações
- Avaliação de segurança

## Requisitos

- Python 3.10+
- Chave da Ollama Cloud (`OLLAMA_API_KEY`) ou Ollama local via Docker

## Como rodar

```bash
cd Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails
python -m venv .venv && source .venv/bin/activate   # recomendado (macOS/Linux)
pip install -r requirements.txt
cp .env.example .env                                 # se ainda não tiver .env
# edite .env e preencha OLLAMA_API_KEY (a mesma chave já está no .env da pasta 1SEM)
python main.py
```


## Arquivos

- `main.py` — código principal da aula com demos de segurança
- `requirements.txt` — dependências do projeto
- `.env` — variáveis de ambiente (chave da API; NÃO versionar)
- `.env.example` — modelo do `.env`
- `.gitignore` — ignora `.env`, `chroma_db/`, `data/`, venv, etc.

---

*Copyright © 2026 Prof. Jorge Luiz Gomes · FIAP · Todos os direitos reservados.*